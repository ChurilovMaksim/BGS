#!/usr/bin/env python3
"""Adversarial source/schema controls for the finite Schur replay only."""
from pathlib import Path
import copy
import importlib.util
import json
import math
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


C = load(ROOT / 'computations/verification/schur/comparison.py', 'comparison_test')
R = load(ROOT / 'computations/verification/schur/full_replay.py', 'replay_test')


class SchurPortability(unittest.TestCase):
    def setUp(self):
        self.expected = {family: (ROOT / entry['expected']).read_bytes()
                         for family, entry in R.FAMILIES.items()}

    def mutation_rejected(self, family, mutate):
        value = json.loads(self.expected[family])
        mutate(value)
        with self.assertRaises(ValueError):
            C.compare(self.expected[family], json.dumps(value).encode(), family)

    def test_known_provenance_paths_only(self):
        for family in R.FAMILIES:
            value = json.loads(self.expected[family])
            value.update(runtime_seconds=0.25, python='test Python version', sympy='test SymPy version')
            exact, provenance = C.compare(self.expected[family], json.dumps(value).encode(), family)
            self.assertTrue(provenance['scientific_equality'])
            self.assertEqual(provenance['expected_provenance']['python'],
                             json.loads(self.expected[family])['python'])
            self.assertEqual(provenance['observed_provenance']['python'], 'test Python version')
            self.assertEqual(exact, C.scientific_bytes(C.separate(json.loads(self.expected[family]), family)[0]))

    def test_nested_environment_key_injection_rejected(self):
        for family in R.FAMILIES:
            for key in ['runtime_seconds', 'elapsed_seconds', 'python', 'sympy', 'environment', 'provenance']:
                self.mutation_rejected(family, lambda value, key=key: value['counts'].update({key: 0}))

    def test_scientific_values_and_structure_rejected(self):
        for family in R.FAMILIES:
            self.mutation_rejected(family, lambda v: v.update(extra_key='injected'))
            self.mutation_rejected(family, lambda v: v.pop('counts'))
            self.mutation_rejected(family, lambda v: v.update(counts=[]))
            self.mutation_rejected(family, lambda v: v['counts'].update({next(iter(v['counts'])): 0}))
            self.mutation_rejected(family, lambda v: v['counts'].update({next(iter(v['counts'])): True}))
            self.mutation_rejected(family, lambda v: v['nonclaims'].append('injected'))
            self.mutation_rejected(family, lambda v: v.update(status='failed'))
            self.mutation_rejected(family, lambda v: v.update(arithmetic='floating'))
        self.mutation_rejected('author', lambda v: v['full_B_through_6'].update({'1': '2'}))
        self.mutation_rejected('independent', lambda v: v['fixtures']['scalar'].update(max_power=6))

    def test_finite_runtime_and_environment_validation(self):
        for family in R.FAMILIES:
            for elapsed in [-1, float('nan'), float('inf'), -float('inf'), True, '1', None,
                            R.FAMILIES[family]['wall_seconds'] + 1]:
                self.mutation_rejected(family, lambda v, e=elapsed: v.update(runtime_seconds=e))
            for field in ['python', 'sympy']:
                for invalid in ['', 1, None, {}, 'x' * 4097]:
                    self.mutation_rejected(family, lambda v, k=field, x=invalid: v.update({k: x}))
                self.mutation_rejected(family, lambda v, k=field: v.pop(k))

    def test_duplicate_keys_and_nonfinite_tokens_rejected(self):
        for raw in [b'{"x":1,"x":2}', b'{"x":NaN}', b'{"x":Infinity}', b'{"x":-Infinity}']:
            with self.assertRaises(ValueError):
                C.parse_json(raw)

    def test_bounded_mismatch_paths(self):
        a = {str(i): {'scientific': i} for i in range(100)}
        b = {str(i): {'scientific': -1} for i in range(100)}
        paths = C.mismatch_paths(a, b)
        self.assertEqual(len(paths), 12)
        self.assertTrue(all(len(p['path']) <= 240 for p in paths))
        self.assertIn('/0/scientific', [p['path'] for p in paths])

    def test_source_corruption_rejected_before_execution(self):
        targets = [R.BINDING_PATH,
            'computations/verification/schur/author_checks.py',
            'computations/verification/schur/independent_checks.py',
            'computations/verification/schur/comparison.py',
            'mathematics/balanced_pair_schur_reduction.md',
            R.FAMILIES['author']['expected'], R.FAMILIES['independent']['expected'],
            'archive/evidence/schur_reduction_20261007/raw/review/review.md']
        with tempfile.TemporaryDirectory(prefix='bgs-schur-corruption-') as directory:
            clone = Path(directory) / 'overlay'
            shutil.copytree(ROOT, clone, ignore=shutil.ignore_patterns('__pycache__', 'portable'))
            for target in targets:
                path = clone / target
                original = path.read_bytes()
                path.write_bytes(original + b'\n')
                with self.assertRaisesRegex(RuntimeError, 'mismatch'):
                    R.cache_inputs(clone)
                path.write_bytes(original)
            self.assertTrue(R.cache_inputs(clone))

    def test_entrypoint_replay_corruption_rejected(self):
        with tempfile.TemporaryDirectory(prefix='bgs-schur-entry-') as directory:
            clone = Path(directory)
            wrapper = clone / 'balanced_pair_schur.py'
            shutil.copy2(ROOT / 'computations/verification/balanced_pair_schur.py', wrapper)
            (clone / 'schur').mkdir()
            (clone / 'schur/full_replay.py').write_text('raise SystemExit(0)\n')
            for flags in [[], ['-O']]:
                run = subprocess.run([sys.executable, '-B', *flags, str(wrapper)],
                                     capture_output=True, text=True, timeout=10)
                self.assertNotEqual(run.returncode, 0)
                self.assertIn('replay source hash mismatch', run.stderr)

    def test_output_cannot_overwrite_historical_inputs(self):
        with tempfile.TemporaryDirectory(prefix='bgs-schur-output-') as directory:
            clone = Path(directory) / 'overlay'
            shutil.copytree(ROOT, clone, ignore=shutil.ignore_patterns('__pycache__', 'portable', 'qa'))
            module = load(clone / 'computations/verification/schur/full_replay.py', 'collision_replay')
            output = clone / 'archive/evidence/schur_reduction_20261007/raw/author'
            before = (output / 'execution_manifest.json').read_bytes()
            with self.assertRaisesRegex(RuntimeError, 'overwrite authenticated source'):
                module.run_replay(output, ['normal'], False, root=clone)
            self.assertEqual(before, (output / 'execution_manifest.json').read_bytes())

    def test_expected_bytes_are_cached_before_child_execution(self):
        with tempfile.TemporaryDirectory(prefix='bgs-schur-cache-') as directory:
            clone = Path(directory) / 'overlay'
            shutil.copytree(ROOT, clone, ignore=shutil.ignore_patterns('__pycache__', 'portable'))
            module = load(clone / 'computations/verification/schur/full_replay.py', 'cached_replay')
            altered = json.loads(self.expected['author'])
            altered['full_B_through_6']['1'] = '999'
            forged = (json.dumps(altered) + '\n').encode()

            def forge(command, output, family, timeout=None):
                # An executing child overwrites its reference and emits the same forged bytes.
                # A comparator that rereads the reference would accept this scientific mutation.
                (clone / module.FAMILIES[family]['expected']).write_bytes(forged)
                Path(command[command.index('--output') + 1]).write_bytes(forged)
                return {'command': command, 'runtime_seconds': 0.0,
                        'exit_status': 0, 'status': 'completed', 'stdout': '', 'stderr': ''}

            module.execute = forge
            output = Path(directory) / 'result'
            with self.assertRaisesRegex(RuntimeError, 'scientific output mismatch'):
                module.run_replay(output, ['normal'], False, root=clone)
            report = json.loads((output / 'comparison.json').read_bytes())
            self.assertEqual(report['status'], 'failed')
            self.assertFalse(report['inputs_unchanged'])
            self.assertIn('/full_B_through_6/1', report['failure'])


if __name__ == '__main__':
    unittest.main()
