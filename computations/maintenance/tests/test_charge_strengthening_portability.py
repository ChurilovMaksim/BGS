"""Bounded fail-closed controls for the portable charge strengthening overlay."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
PORTS = ROOT / 'computations/verification/charge_strengthening'
WRAPPER = ROOT / 'computations/verification/charge_strengthening_replay.py'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ComparisonTests(unittest.TestCase):
    def setUp(self):
        self.comp = load('charge_comparison_test', PORTS / 'comparison.py')
        self.expected = {'science': {'n': 3, 'passed': True}, 'list': [1, 2],
                         'sha256_source': 'a' * 64}

    def compare(self, value):
        return self.comp.compare('author-exact-v1', self.expected, value,
                                 {'python': '3.12.14', 'runtime_seconds': 1.0},
                                 {'python': '3.13.5', 'runtime_seconds': 2.0})

    def test_environment_difference_is_provenance(self):
        report = self.compare(copy.deepcopy(self.expected))
        self.assertTrue(report['scientific_comparison']['equal'])
        self.assertNotEqual(report['provenance']['expected'], report['provenance']['observed'])
        self.assertEqual(report['excluded_runtime_environment_paths'], [])

    def test_scientific_change_reports_exact_path(self):
        changed = copy.deepcopy(self.expected)
        changed['science']['n'] = 4
        report = self.compare(changed)['scientific_comparison']
        self.assertFalse(report['equal'])
        self.assertEqual(report['mismatches'][0]['path'], '/science/n')

    def test_missing_and_unexpected_structure(self):
        changed = copy.deepcopy(self.expected)
        del changed['science']['n']
        changed['environment'] = {'python': 'must not be stripped'}
        changed['science']['runtime_seconds'] = 1
        report = self.compare(changed)['scientific_comparison']
        self.assertEqual(report['mismatch_count'], 3)
        self.assertEqual({x['path'] for x in report['mismatches']},
                         {'/science/n', '/environment', '/science/runtime_seconds'})

    def test_type_length_source_and_bounded_paths(self):
        changed = copy.deepcopy(self.expected)
        changed['science']['passed'] = 1
        changed['list'].append(3)
        changed['sha256_source'] = 'b' * 64
        self.assertEqual(self.compare(changed)['scientific_comparison']['mismatch_count'], 3)
        report = self.comp.differences(list(range(50)), [-1] * 50, limit=5)
        self.assertEqual(report['mismatch_count'], 50)
        self.assertEqual(len(report['mismatches']), 5)
        self.assertTrue(report['truncated'])

    def test_unknown_schema_duplicate_and_nonfinite_rejected(self):
        with self.assertRaises(ValueError):
            self.comp.compare('unknown', {}, {}, {}, {})
        for content in ['{"n":1,"n":2}', '{"runtime_seconds":NaN}', '{"n":Infinity}']:
            with self.assertRaises(ValueError):
                self.comp.loads_json(content)

    def test_nonfinite_provenance_runtime_rejected(self):
        for value in [float('nan'), float('inf'), -1.0, True, '1.0']:
            with self.assertRaises(ValueError):
                self.comp.compare('author-exact-v1', {}, {},
                                  {'runtime_seconds': value}, {})

    def test_raw_expected_bytes_remain_unchanged(self):
        raw = b'{"n": 3, "source": "keep"}\n'
        expected = self.comp.loads_json(raw)
        changed = copy.deepcopy(expected)
        changed['source'] = 'changed'
        self.comp.compare('author-exact-v1', expected, changed, {}, {})
        self.assertEqual(expected, {'n': 3, 'source': 'keep'})
        self.assertEqual(raw, b'{"n": 3, "source": "keep"}\n')


class ExecutionTests(unittest.TestCase):
    def invoke(self, args, cwd):
        env = os.environ.copy()
        env['PYTHONDONTWRITEBYTECODE'] = '1'
        return subprocess.run([sys.executable, '-B'] + args, cwd=cwd, env=env,
                              capture_output=True, timeout=90)

    def test_silent_imports_normal_and_optimized(self):
        paths = [PORTS / name for name in ['author_checks.py', 'independent_checks.py',
                                          'switch_checks.py', 'comparison.py']] + [WRAPPER]
        code = ('import importlib.util,sys; sys.path.insert(0,' + repr(str(PORTS)) + ');'
                'paths=' + repr([str(p) for p in paths]) + ';'
                '\nfor i,p in enumerate(paths):\n'
                ' s=importlib.util.spec_from_file_location("testmod"+str(i),p);'
                ' m=importlib.util.module_from_spec(s);s.loader.exec_module(m)\n')
        with tempfile.TemporaryDirectory() as directory:
            for mode in [[], ['-O']]:
                proc = self.invoke(mode + ['-c', code], directory)
                self.assertEqual(proc.returncode, 0, proc.stderr)
                self.assertEqual(proc.stdout + proc.stderr, b'')
                self.assertEqual(list(Path(directory).iterdir()), [])

    def test_each_maintained_checker_failure_survives_optimization(self):
        with tempfile.TemporaryDirectory() as directory:
            for name in ['author_checks.py', 'independent_checks.py', 'switch_checks.py']:
                for mode in [[], ['-O']]:
                    args = mode + [str(PORTS / name), '--inject-failure']
                    if name != 'author_checks.py':
                        args += ['--output', str(Path(directory) / 'must_not_exist.json')]
                    proc = self.invoke(args, directory)
                    self.assertNotEqual(proc.returncode, 0)
                    expected = b'injected switch failure' if name == 'switch_checks.py' else b'injected failure'
                    self.assertIn(expected, proc.stderr)
                    self.assertFalse((Path(directory) / 'must_not_exist.json').exists())

    def test_source_corruption_rejected_before_execution(self):
        mapping = json.loads((ROOT / 'record/charge_strengthening_replay_sources.json').read_text())
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / 'portable'
            for row in mapping['files'] + [{'path': 'record/charge_strengthening_replay_sources.json'}]:
                path = row['path']
                target = copied / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes((ROOT / path).read_bytes())
            for relative in ['computations/verification/charge_strengthening/author_checks.py',
                             'archive/evidence/charge_strengthening_20261007/raw/author/exact_results.json',
                             'mathematics/onestep_charge_gap.md']:
                target = copied / relative
                original = target.read_bytes()
                target.write_bytes(original + b'\n# deliberate corruption\n')
                for mode in [[], ['-O']]:
                    proc = self.invoke(mode + [str(copied / WRAPPER.relative_to(ROOT))], directory)
                    self.assertNotEqual(proc.returncode, 0)
                    self.assertIn(b'Source SHA256 mismatch:', proc.stderr)
                target.write_bytes(original)
            proc = self.invoke([str(copied / WRAPPER.relative_to(ROOT))], directory)
            self.assertEqual(proc.returncode, 0, proc.stderr)
            self.assertEqual(proc.stdout + proc.stderr, b'')

    def test_expected_bytes_cached_before_external_mutation(self):
        wrapper = load('charge_replay_cache_test', WRAPPER)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'expected.json'
            raw = b'{"n":3}\n'
            path.write_bytes(raw)
            wrapper.expected_provenance = lambda family, result: {
                'result_sha256': hashlib.sha256(result.read_bytes()).hexdigest()}
            cached = wrapper.cache_expected([('author', 'code.py', path, 'author-exact-v1')])
            path.write_bytes(b'{"n":4}\n')
            self.assertEqual(cached['author']['bytes'], raw)
            self.assertEqual(cached['author']['provenance']['result_sha256'],
                             hashlib.sha256(raw).hexdigest())

    def test_wrapper_failure_and_stale_outputs(self):
        with tempfile.TemporaryDirectory() as directory:
            proc = self.invoke(['-O', str(WRAPPER), '--inject-failure'], directory)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn(b'injected failure', proc.stderr)
            work = Path(directory) / 'stale'
            work.mkdir()
            (work / 'old.json').write_text('{}\n')
            proc = self.invoke([str(WRAPPER), '--output-dir', str(work)], directory)
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn(b'stale results', proc.stderr)


if __name__ == '__main__':
    unittest.main()
