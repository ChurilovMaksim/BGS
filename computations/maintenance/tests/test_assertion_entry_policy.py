#!/usr/bin/env python3
"""Coverage, mutation and CLI/import regressions; unittest checks survive -O."""
import ast
from concurrent.futures import ThreadPoolExecutor
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location('assertion_policy', ROOT/'computations/maintenance/assertion_policy.py')
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)
MODES = ('-O', '-OO', 'env1', 'env2')


def run(script, mode, directory, *, imported=False, args=()):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    env.pop('PYTHONOPTIMIZE', None)
    cmd = [sys.executable, '-B']
    if mode.startswith('-'):
        cmd.append(mode)
    elif mode.startswith('env'):
        env['PYTHONOPTIMIZE'] = mode[-1]
    if imported:
        cmd += ['-c', 'import runpy,sys; runpy.run_path(sys.argv[1], run_name="verification_import")', str(script)]
    else:
        cmd += [str(script), *map(str, args)]
    return subprocess.run(cmd, cwd=directory, env=env, text=True,
                          capture_output=True, timeout=30)


class AssertionEntryPolicyTests(unittest.TestCase):
    def test_preserved_spectral_inputs_are_not_maintained_entries(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            historical = root/'computations/reference/spectral_research'
            historical.mkdir(parents=True)
            (historical/'source.py').write_text('assert False\n')
            # Other reference code retains the usual guard requirement.
            maintained = root/'computations/reference/other'
            maintained.mkdir()
            (maintained/'helper.py').write_text('assert False\n')
            self.assertEqual(policy.violations(root),
                             ['computations/reference/other/helper.py'])

    def test_static_coverage_and_guard_removal_mutations(self):
        self.assertEqual(policy.violations(ROOT), [])
        for path, tree in policy.protected_entries(ROOT):
            with self.subTest(path=str(path)):
                self.assertTrue(policy.guarded(tree))
                guard = next(node for node in tree.body if isinstance(node, ast.If))
                tree.body.remove(guard)
                self.assertFalse(policy.guarded(tree), 'Guard deletion was not detected')

    def test_guard_precedes_imports_and_handles_future_and_docstring(self):
        good = '"doc"\nfrom __future__ import annotations\n' + policy.GUARD + 'import os\nassert False\n'
        self.assertTrue(policy.guarded(ast.parse(good)))
        self.assertFalse(policy.guarded(ast.parse('import os\n' + policy.GUARD)))
        self.assertFalse(policy.guarded(ast.parse('if __name__ == "__main__":\n    ' + policy.GUARD.replace('\n', '\n    '))))
        self.assertTrue(policy.required(Path('computations/new_helper.py'), ast.parse('assert False')))
        self.assertFalse(policy.required(Path('computations/verification/new_checker.py'), ast.parse('print("PASS")')))

    def test_import_closure_and_explicit_check_only_modules(self):
        with tempfile.TemporaryDirectory(prefix='bgs_policy_closure_') as tmp:
            root = Path(tmp)
            directory = root/'computations/verification'
            directory.mkdir(parents=True)
            (directory/'helper.py').write_text('assert False\n')
            (directory/'producer.py').write_text('import helper\n')
            (directory/'outer.py').write_text('from producer import main\n')
            (directory/'explicit.py').write_text('raise ValueError("failure")\n')
            self.assertEqual({p.stem for p, t in policy.protected_entries(root)},
                             {'helper', 'producer', 'outer'})
        protected = {p.stem for p, t in policy.protected_entries(ROOT)}
        for name in ('actual_path_theorems', 'isospectral_clock_control',
                     'scientific_registry_audit', 'text_control_audit'):
            self.assertNotIn(name, protected)

    def test_package_initializers_and_repository_parent_named_tests(self):
        with tempfile.TemporaryDirectory(prefix='bgs_package_policy_') as tmp:
            root = Path(tmp)/'tests'/'BGS'
            directory = root/'computations/verification'
            package = directory/'pkg'/'inner'
            package.mkdir(parents=True)
            (directory/'pkg/__init__.py').write_text('assert False\n')
            (package/'__init__.py').write_text('value = 1\n')
            (package/'leaf.py').write_text('value = 2\n')
            imports = {
                'plain': 'import pkg',
                'dotted': 'import pkg.inner.leaf',
                'from_package': 'from pkg import inner',
                'from_dotted': 'from pkg.inner.leaf import value',
            }
            for name, statement in imports.items():
                (directory/(name+'.py')).write_text(statement+'\n')
            excluded = directory/'tests'
            excluded.mkdir()
            (excluded/'fixture.py').write_text('assert False\n')
            entries = policy.protected_entries(root)
            actual = {p.relative_to(Path('computations/verification')).as_posix()
                      for p, tree in entries}
            self.assertEqual(actual, {'pkg/__init__.py', 'pkg/inner/__init__.py',
                                     'pkg/inner/leaf.py',
                                     *(name+'.py' for name in imports)})
            self.assertNotIn('tests/fixture.py', actual)
            self.assertEqual(len(policy.violations(root)), 7)

    def test_all_optimized_entries_and_imports_fail_before_side_effects(self):
        paths = [path for path, tree in policy.protected_entries(ROOT)]
        jobs = [(path, mode, imported) for path in paths for mode in MODES for imported in (False, True)]
        def check(job):
            path, mode, imported = job
            with tempfile.TemporaryDirectory(prefix='bgs_optimized_entry_') as tmp:
                directory = Path(tmp)
                output = directory/'certificate.json'
                result = run(ROOT/path, mode, directory, imported=imported,
                             args=('--output', output))
                return job, result, list(directory.iterdir())
        with ThreadPoolExecutor(max_workers=8) as pool:
            for job, result, files in pool.map(check, jobs):
                with self.subTest(path=str(job[0]), mode=job[1], imported=job[2]):
                    self.assertNotEqual(result.returncode, 0)
                    self.assertIn(policy.MESSAGE, result.stderr)
                    self.assertEqual(result.stdout, '')
                    self.assertEqual(files, [], 'Optimized verifier created an output')

    def test_false_predicate_mutations_for_every_protected_module(self):
        # A synthetic load-bearing false predicate, not a domain-specific identity.
        # Each normal mutation must fail; each optimized mutation must fail earlier.
        paths = policy.protected_entries(ROOT)
        def check(item):
            path, tree = item
            guard = next(node for node in tree.body if isinstance(node, ast.If))
            lines = (ROOT/path).read_text().splitlines(True)
            lines.insert(guard.end_lineno, 'assert False, "injected false verification predicate"\n')
            outcomes = []
            with tempfile.TemporaryDirectory(prefix='bgs_predicate_mutation_') as tmp:
                directory = Path(tmp)
                script = directory/'mutant.py'
                script.write_text(''.join(lines))
                for mode in ('normal', *MODES):
                    output = directory/'certificate.json'
                    result = run(script, mode, directory, args=('--output', output))
                    outcomes.append((mode, result, output.exists()))
            return path, outcomes
        with ThreadPoolExecutor(max_workers=8) as pool:
            for path, outcomes in pool.map(check, paths):
                for mode, result, exists in outcomes:
                    with self.subTest(path=str(path), mode=mode):
                        self.assertNotEqual(result.returncode, 0)
                        self.assertEqual(result.stdout, '')
                        self.assertFalse(exists)
                        self.assertIn('injected false verification predicate'
                                      if mode == 'normal' else policy.MESSAGE,
                                      result.stderr)

    def test_frozen_constant_false_identity_and_valid_control(self):
        source = (ROOT/'computations/verification/frozen_full_lag_gap.py').read_text()
        self.assertEqual(source.count('F(51451, 1000)'), 1)
        with tempfile.TemporaryDirectory(prefix='bgs_frozen_mutation_') as tmp:
            directory = Path(tmp)
            for variant, text in [('valid', source), ('false', source.replace('F(51451, 1000)', 'F(51452, 1000)'))]:
                script = directory/(variant+'.py')
                script.write_text(text)
                for mode in ('normal', *MODES):
                    with self.subTest(variant=variant, mode=mode):
                        output = directory/(variant+mode+'.json')
                        result = run(script, mode, directory, args=('--output', output))
                        if variant == 'valid' and mode == 'normal':
                            self.assertEqual(result.returncode, 0, result.stderr)
                            self.assertEqual(json.loads(output.read_text())['status'], 'passed')
                        else:
                            self.assertNotEqual(result.returncode, 0)
                            self.assertFalse(output.exists())
                            self.assertIn('AssertionError' if mode == 'normal' else policy.MESSAGE, result.stderr)


if __name__ == '__main__':
    unittest.main()
