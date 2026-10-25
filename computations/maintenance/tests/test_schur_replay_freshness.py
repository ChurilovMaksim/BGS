#!/usr/bin/env python3
"""Freshness and input-identity controls, without generating new reference science.

Run this file normally and with -O. Synthetic child behaviors always compare
against the losslessly preserved, pinned historical expected scientific bytes.
"""
from pathlib import Path
import contextlib
import hashlib
import io
import importlib.util
import json
import os
import py_compile
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
REPLAY = Path('computations/verification/schur/full_replay.py')
ENTRY = Path('computations/verification/balanced_pair_schur.py')


def load(path):
    spec = importlib.util.spec_from_file_location('schur_freshness_fixture', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


R = load(ROOT / REPLAY)


def fixture(directory):
    root = Path(directory) / 'root'
    rows = json.loads((ROOT / R.BINDING_PATH).read_bytes())['files']
    for relative in [R.BINDING_PATH, *rows, str(REPLAY), str(ENTRY)]:
        target = root / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes((ROOT / relative).read_bytes())
    return root, load(root / REPLAY)


def completed(command):
    return {'command': command, 'runtime_seconds': 0.0, 'exit_status': 0,
            'status': 'completed', 'stdout': '', 'stderr': ''}


def emit(module, root, command, family):
    path = Path(command[command.index('--output') + 1])
    if path.exists() or path.is_symlink():
        raise RuntimeError('fixture found output staged before producer execution')
    path.write_bytes((root / module.FAMILIES[family]['expected']).read_bytes())
    return path


class SchurReplayFreshness(unittest.TestCase):
    def invoke(self, module, root, output, mode='normal', controls=False):
        try:
            result = module.run_replay(output, [mode], controls, root=root)
            error = None
        except RuntimeError as exc:
            result, error = None, str(exc)
        report = json.loads((output / 'comparison.json').read_bytes())
        manifest = json.loads((output / 'execution_manifest.json').read_bytes())
        self.assertEqual(report['status'], 'passed' if error is None else 'failed')
        self.assertEqual(manifest['run']['exit_status'], 0 if error is None else 1)
        return result, error, report, manifest

    def test_empty_or_invalid_programmatic_mode_plan_is_rejected_before_execution(self):
        for modes in ([], None, 'normal', ['unknown'], ['../escape'], [[]]):
            with self.subTest(modes=modes), tempfile.TemporaryDirectory() as directory:
                root, module = fixture(directory)
                output = Path(directory) / 'output'
                calls = []
                module.execute = lambda *args: calls.append(args)
                with self.assertRaisesRegex(RuntimeError, 'nonempty normal/optimized plan'):
                    module.run_replay(output, modes, False, root=root)
                self.assertEqual(calls, [])
                self.assertFalse(output.exists())

    def test_noop_early_return_and_missing_reject_prefilled_or_absent_results(self):
        for mode in ('normal', 'optimized'):
            for family in R.FAMILIES:
                for prefill in (False, True):
                    for body in ('pass', 'def main():\n    return 0\nmain()', 'raise SystemExit(0)'):
                        with self.subTest(mode=mode, family=family, prefill=prefill, body=body):
                            with tempfile.TemporaryDirectory() as directory:
                                root, module = fixture(directory)
                                output = Path(directory) / 'output'
                                output.mkdir()
                                if prefill:
                                    for name, entry in module.FAMILIES.items():
                                        (output / (name + '_' + mode + '.json')).write_bytes((root / entry['expected']).read_bytes())
                                original = module.execute
                                called = []

                                def producer(command, workspace, name, timeout=None):
                                    called.append(name)
                                    if name == family:
                                        flags = ['-O'] if mode == 'optimized' else []
                                        return original([sys.executable, '-B', *flags, '-c', body], workspace, name, timeout)
                                    emit(module, root, command, name)
                                    return completed(command)

                                module.execute = producer
                                _, error, report, _ = self.invoke(module, root, output, mode)
                                self.assertIn('fresh regular contained result', error)
                                self.assertTrue(report['inputs_unchanged'])
                                self.assertFalse(report['runs'][-1]['fresh_result_created'])
                                self.assertEqual(called[-1], family)

    def test_new_correct_results_pass_and_workspaces_exclude_original_expectations(self):
        for mode in ('normal', 'optimized'):
            with self.subTest(mode=mode), tempfile.TemporaryDirectory() as directory:
                root, module = fixture(directory)
                output = Path(directory) / 'output'
                output.mkdir()
                workspaces = []
                for family, entry in module.FAMILIES.items():
                    (output / (family + '_' + mode + '.json')).write_bytes((root / entry['expected']).read_bytes())

                def producer(command, workspace, family, timeout=None):
                    self.assertEqual(list(workspace.iterdir()), [])
                    self.assertFalse((root / module.FAMILIES[family]['expected']).is_relative_to(workspace))
                    workspaces.append(workspace)
                    emit(module, root, command, family)
                    return completed(command)

                module.execute = producer
                result, error, report, manifest = self.invoke(module, root, output, mode)
                self.assertIsNone(error)
                self.assertEqual(result, 0)
                self.assertEqual(len(set(workspaces)), 2)
                for row in report['runs']:
                    self.assertTrue(row['fresh_result_created'])
                    self.assertTrue(row['inputs_authenticated_after_child'])
                    self.assertTrue(row['output_absent_before_execution'])
                    self.assertFalse(row['original_expected_bytes_staged'])
                self.assertEqual(len(manifest['declared_results']), 5)

    def test_new_wrong_science_is_rejected_and_actual_diagnostics_retained(self):
        for mode in ('normal', 'optimized'):
            for family in R.FAMILIES:
                with self.subTest(mode=mode, family=family), tempfile.TemporaryDirectory() as directory:
                    root, module = fixture(directory)
                    output = Path(directory) / 'output'

                    def producer(command, workspace, name, timeout=None):
                        path = emit(module, root, command, name)
                        if name == family:
                            value = json.loads(path.read_bytes())
                            value['counts'][next(iter(value['counts']))] = 0
                            path.write_text(json.dumps(value))
                        return completed(command)

                    module.execute = producer
                    _, error, report, _ = self.invoke(module, root, output, mode)
                    self.assertIn('scientific output mismatch', error)
                    self.assertIn('/counts/', error)
                    self.assertTrue(report['runs'][-1]['fresh_result_created'])
                    self.assertFalse(report['runs'][-1]['scientific_equality'])
                    self.assertTrue((output / (family + '_' + mode + '.json')).is_file())

    def test_symlink_directory_fifo_and_hardlink_results_rejected(self):
        for mode in ('normal', 'optimized'):
            for kind in ('symlink', 'directory', 'fifo', 'hardlink', 'ancestor'):
                with self.subTest(mode=mode, kind=kind), tempfile.TemporaryDirectory() as directory:
                    root, module = fixture(directory)
                    output = Path(directory) / 'output'
                    outside = Path(directory) / 'outside'
                    outside.mkdir()
                    sentinel = outside / 'result.json'
                    sentinel.write_bytes((root / module.FAMILIES['author']['expected']).read_bytes())
                    before = sentinel.read_bytes()

                    def producer(command, workspace, family, timeout=None):
                        path = Path(command[command.index('--output') + 1])
                        if kind == 'symlink':
                            path.symlink_to(sentinel)
                        elif kind == 'directory':
                            path.mkdir()
                        elif kind == 'fifo':
                            os.mkfifo(path)
                        elif kind == 'hardlink':
                            os.link(sentinel, path)
                        else:
                            workspace.rmdir()
                            workspace.symlink_to(outside, target_is_directory=True)
                        return completed(command)

                    module.execute = producer
                    _, error, report, _ = self.invoke(module, root, output, mode)
                    self.assertIn('fresh regular contained result', error)
                    self.assertFalse(report['runs'][-1]['fresh_result_created'])
                    self.assertEqual(sentinel.read_bytes(), before)

    def test_output_and_input_symlink_ancestors_rejected_before_child(self):
        for mode in ('normal', 'optimized'):
            for kind in ('output_leaf', 'output_ancestor', 'result_leaf', 'result_hardlink', 'input_leaf', 'input_ancestor'):
                with self.subTest(mode=mode, kind=kind), tempfile.TemporaryDirectory() as directory:
                    root, module = fixture(directory)
                    output = Path(directory) / 'output'
                    outside = Path(directory) / 'outside'
                    outside.mkdir()
                    sentinel = outside / 'sentinel.json'
                    sentinel.write_text('protected outside bytes')
                    before = sentinel.read_bytes()
                    if kind == 'output_leaf':
                        output.symlink_to(outside, target_is_directory=True)
                    elif kind == 'output_ancestor':
                        output.symlink_to(outside, target_is_directory=True)
                        output /= 'nested'
                    elif kind in ('result_leaf', 'result_hardlink'):
                        output.mkdir()
                        target = output / 'author_normal.json'
                        if mode == 'optimized':
                            target = output / 'author_optimized.json'
                        if kind == 'result_leaf':
                            target.symlink_to(sentinel)
                        else:
                            os.link(sentinel, target)
                    elif kind == 'input_leaf':
                        target = root / module.FAMILIES['author']['expected']
                        raw = target.read_bytes()
                        target.unlink()
                        sentinel.write_bytes(raw)
                        before = raw
                        target.symlink_to(sentinel)
                    else:
                        target = root / 'computations/verification/schur'
                        moved = root / 'saved_schur'
                        target.rename(moved)
                        target.symlink_to(moved, target_is_directory=True)
                    called = []
                    module.execute = lambda *args: called.append(args)
                    with self.assertRaisesRegex(RuntimeError, 'symlink|unaliased'):
                        module.run_replay(output, [mode], False, root=root)
                    self.assertEqual(called, [])
                    self.assertEqual(sentinel.read_bytes(), before)

    def test_input_mutation_stops_before_next_child_including_control_children(self):
        targets = [R.BINDING_PATH, str(REPLAY), str(ENTRY),
                   'computations/verification/schur/comparison.py',
                   'computations/verification/schur/author_checks.py',
                   'computations/verification/schur/independent_checks.py',
                   R.FAMILIES['author']['expected'], R.FAMILIES['independent']['expected'],
                   'mathematics/trace-bridge/balanced_pair_schur_reduction.md']
        for mode in ('normal', 'optimized'):
            for controls in (False, True):
                for target in targets:
                    with self.subTest(mode=mode, controls=controls, target=target), tempfile.TemporaryDirectory() as directory:
                        root, module = fixture(directory)
                        output = Path(directory) / 'output'
                        calls = []

                        def producer(command, workspace, family, timeout=None):
                            calls.append(command)
                            if '--output' in command:
                                emit(module, root, command, family)
                            path = root / target
                            path.write_bytes(path.read_bytes() + b'\nmutated')
                            return completed(command)

                        module.execute = producer
                        _, error, report, _ = self.invoke(module, root, output, mode, controls)
                        self.assertIn('input bytes changed', error)
                        self.assertFalse(report['inputs_unchanged'])
                        self.assertEqual(len(calls), 1)
                        row = report['controls'][0] if controls else report['runs'][0]
                        self.assertFalse(row['inputs_authenticated_after_child'])
                        self.assertIn(target, row['changed_inputs'])

    def test_replacing_input_identity_or_symlink_is_rejected_with_correct_result(self):
        for mode in ('normal', 'optimized'):
            for kind in ('replace_same_bytes', 'symlink_same_bytes'):
                with self.subTest(mode=mode, kind=kind), tempfile.TemporaryDirectory() as directory:
                    root, module = fixture(directory)
                    output = Path(directory) / 'output'
                    target = root / module.FAMILIES['author']['expected']

                    def producer(command, workspace, family, timeout=None):
                        emit(module, root, command, family)
                        raw = target.read_bytes()
                        saved = target.with_suffix('.saved')
                        target.rename(saved)
                        if kind == 'replace_same_bytes':
                            target.write_bytes(raw)
                        else:
                            target.symlink_to(saved)
                        return completed(command)

                    module.execute = producer
                    _, error, report, _ = self.invoke(module, root, output, mode)
                    self.assertIn('input bytes changed', error)
                    self.assertFalse(report['inputs_unchanged'])
                    self.assertTrue(report['runs'][0]['scientific_equality'])

    def test_nonzero_or_timeout_child_preserves_its_actual_result(self):
        for mode in ('normal', 'optimized'):
            for status, code in (('completed', 7), ('timed_out', 124)):
                with self.subTest(mode=mode, status=status), tempfile.TemporaryDirectory() as directory:
                    root, module = fixture(directory)
                    output = Path(directory) / 'output'

                    def producer(command, workspace, family, timeout=None):
                        emit(module, root, command, family)
                        return dict(completed(command), status=status, exit_status=code, stderr='failure diagnostics')

                    module.execute = producer
                    _, error, report, _ = self.invoke(module, root, output, mode)
                    self.assertIn('exact replay failed', error)
                    self.assertEqual(report['runs'][0]['stderr'], 'failure diagnostics')
                    self.assertTrue((output / ('author_' + mode + '.json')).is_file())

    def test_timestamp_valid_precompiled_cache_cannot_replace_authenticated_source(self):
        for relative in (Path('computations/verification/schur/comparison.py'), REPLAY):
            with self.subTest(relative=relative), tempfile.TemporaryDirectory() as directory:
                root, module = fixture(directory)
                path = root / relative
                original = path.read_bytes()
                poison = b'raise RuntimeError("poisoned precompiled cache executed")\n'
                path.write_bytes(poison + b'#' * (len(original) - len(poison)))
                cached_stat = path.stat()
                py_compile.compile(str(path), doraise=True, optimize=sys.flags.optimize)
                path.write_bytes(original)
                os.utime(path, ns=(cached_stat.st_atime_ns, cached_stat.st_mtime_ns))
                # This confirms the fixture really is accepted by the old loader.
                with self.assertRaisesRegex(RuntimeError, 'poisoned precompiled cache'):
                    load(path)
                if relative == REPLAY:
                    entry = load(root / ENTRY)
                    with contextlib.redirect_stdout(io.StringIO()):
                        with self.assertRaises(SystemExit) as result:
                            entry.main(['--help'])
                    self.assertEqual(result.exception.code, 0)
                else:
                    checked = module.load_comparison(root)
                    self.assertTrue(callable(checked.compare))

    def test_entrypoint_rejects_symlink_replay_before_source_execution(self):
        with tempfile.TemporaryDirectory() as directory:
            root, module = fixture(directory)
            path = root / REPLAY
            actual = path.with_suffix('.original')
            path.rename(actual)
            path.symlink_to(actual)
            entry = load(root / ENTRY)
            with self.assertRaisesRegex(RuntimeError, 'symlink'):
                entry.main(['--help'])

    def test_repair_map_preserves_original_seals_and_binds_current_wrappers(self):
        mapping = json.loads((ROOT / 'record/schur_replay_freshness_repair_map.json').read_bytes())
        for entry in mapping['maintained_wrapper_deltas']:
            original = (ROOT / entry['historical_copy']).read_bytes()
            current = (ROOT / entry['maintained_path']).read_bytes()
            self.assertEqual(hashlib.sha256(original).hexdigest(), entry['historical_sha256'])
            self.assertEqual(hashlib.sha256(current).hexdigest(), entry['maintained_sha256'])
        self.assertEqual(hashlib.sha256((ROOT / R.BINDING_PATH).read_bytes()).hexdigest(), R.BINDING_SHA256)
        self.assertTrue(mapping['scientific_inputs_unchanged'])
        for path, expected in mapping['unchanged_scientific_bindings'].items():
            self.assertEqual(hashlib.sha256((ROOT / path).read_bytes()).hexdigest(), expected)


if __name__ == '__main__':
    unittest.main()
