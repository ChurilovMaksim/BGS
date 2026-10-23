"""Fixed-schema provenance separation and durable Hamming mismatch evidence."""
from pathlib import Path
import copy
import importlib.util
import json
import sys
import tempfile
from types import SimpleNamespace
import unittest

ROOT = Path(__file__).resolve().parents[3]
PORTS = ROOT / 'computations/verification/fractional_hamming'
RAW = ROOT / 'archive/evidence/fractional_hamming_20261007/raw'


def source_module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    # Tests exercise actual source bytes even when an old pyc is present.
    exec(compile(path.read_bytes(), str(path), 'exec'), module.__dict__)
    return module


cmp = source_module('fractional_comparison', PORTS / 'comparison.py')
EXPECTED = (RAW / 'author/results.json').read_bytes()


def current_author():
    value = cmp.parse_json(EXPECTED)
    value.pop('elapsed_seconds')
    value['python'] = 'Different Python interpreter runtime'
    value['sympy'] = 'Different SymPy runtime'
    return value


def raw(value):
    return json.dumps(value).encode()


class FractionalProvenance(unittest.TestCase):
    def test_versions_are_retained_separately_and_science_exact(self):
        expected, actual, report = cmp.compare(EXPECTED, raw(current_author()), 'author')
        self.assertTrue(report['scientific_comparison']['equal'])
        self.assertEqual(cmp.scientific_bytes(expected), cmp.scientific_bytes(actual))
        self.assertEqual(report['expected_provenance']['python'], cmp.parse_json(EXPECTED)['python'])
        self.assertEqual(report['observed_provenance']['python'], current_author()['python'])
        self.assertEqual(report['separated_top_level_paths'], ['/python', '/sympy', '/elapsed_seconds'])

    def test_version_types_and_empty_values_rejected(self):
        for field in ('python', 'sympy'):
            for value in (True, 314, [], {}, None, ''):
                with self.subTest(field=field, value=value):
                    data = current_author(); data[field] = value
                    with self.assertRaises(ValueError):
                        cmp.compare(EXPECTED, raw(data), 'author')

    def test_missing_versions_and_unknown_roots_rejected(self):
        for field in ('python', 'sympy'):
            data = current_author(); data.pop(field)
            with self.assertRaises(ValueError):
                cmp.compare(EXPECTED, raw(data), 'author')
        for field in ('runtime', 'environment', 'unknown'):
            data = current_author(); data[field] = 'metadata-like scientific addition'
            with self.assertRaises(ValueError):
                cmp.compare(EXPECTED, raw(data), 'author')

    def test_expected_timing_required_and_strictly_typed(self):
        data = cmp.parse_json(EXPECTED); data.pop('elapsed_seconds')
        with self.assertRaises(ValueError):
            cmp.compare(raw(data), raw(current_author()), 'author')
        for value in (True, '0', [], -1):
            data = cmp.parse_json(EXPECTED); data['elapsed_seconds'] = value
            with self.assertRaises(ValueError):
                cmp.compare(raw(data), raw(current_author()), 'author')

    def test_actual_optional_timing_still_typed(self):
        for value in (True, '0', [], -1):
            data = current_author(); data['elapsed_seconds'] = value
            with self.assertRaises(ValueError):
                cmp.compare(EXPECTED, raw(data), 'author')

    def test_scientific_value_change_is_reported(self):
        data = current_author(); data['cases'][0]['balanced_dimension'] += 1
        report = cmp.compare(EXPECTED, raw(data), 'author')[2]['scientific_comparison']
        self.assertFalse(report['equal'])
        self.assertIn('/cases/0/balanced_dimension', [row['path'] for row in report['mismatches']])

    def test_integer_float_and_bool_changes_rejected(self):
        for value in (float(current_author()['cases'][0]['N']), True):
            data = current_author(); data['cases'][0]['N'] = value
            report = cmp.compare(EXPECTED, raw(data), 'author')[2]['scientific_comparison']
            self.assertFalse(report['equal'])
            self.assertTrue(any(row['reason'] == 'type mismatch' for row in report['mismatches']))

    def test_nested_runtime_names_remain_scientific(self):
        for name in ('python', 'sympy', 'elapsed_seconds', 'runtime_seconds', 'environment'):
            data = current_author(); data['cases'][0][name] = 'unapproved nested field'
            report = cmp.compare(EXPECTED, raw(data), 'author')[2]['scientific_comparison']
            self.assertFalse(report['equal'])

    def test_duplicate_nonfinite_and_unknown_schema_rejected(self):
        for value in (b'{"python":"x","python":"y"}', b'{"x":NaN}', b'{"x":Infinity}', b'{"x":1e999}'):
            with self.assertRaises(ValueError):
                cmp.parse_json(value)
        with self.assertRaises(ValueError):
            cmp.compare(EXPECTED, raw(current_author()), 'unknown')

    def test_split_case_has_no_provenance_exclusions(self):
        full = (RAW / 'review/results/verified/all_results.json').read_bytes()
        data = cmp.parse_json(full)['top_gram']
        report = cmp.compare(full, raw(data), 'independent', 'top_gram')[2]
        self.assertTrue(report['scientific_comparison']['equal'])
        self.assertEqual(report['separated_top_level_paths'], [])
        altered = copy.deepcopy(data)
        if isinstance(altered, dict):
            altered['python'] = 'extra'
        else:
            altered[0]['python'] = 'extra'
        self.assertFalse(cmp.compare(full, raw(altered), 'independent', 'top_gram')[2]['scientific_comparison']['equal'])

    def test_synthesis_boolean_is_not_integer(self):
        original = (RAW / 'review/synthesis_results.json').read_bytes()
        data = cmp.parse_json(original); data['all_radii'] = 1
        self.assertFalse(cmp.compare(original, raw(data), 'synthesis')[2]['scientific_comparison']['equal'])


class FractionalDurableEvidence(unittest.TestCase):
    def fixture(self, corrupt=False, invalid=False):
        module = source_module('fractional_wrapper', ROOT / 'computations/verification/fractional_hamming_replay.py')
        def run(command, **kwargs):
            if '--case' in command:
                case = command[command.index('--case') + 1]
                family = 'independent'
                value = cmp.parse_json((RAW / 'review/results/verified/all_results.json').read_bytes())
                name = 'full_end' if case.startswith('full_end_') else case
                data = value[name]
                if case.startswith('full_end_'):
                    n, m = map(int, case.removeprefix('full_end_').split('_'))
                    data = [row for row in data if (row['N'], row['m']) == (n, m)]
                if corrupt:
                    if isinstance(data, dict):
                        data['unexpected_science'] = True
                    else:
                        data.append({'unexpected_science': True})
            else:
                family = Path(command[command.index('--output') - 1]).stem.replace('_checks', '')
                data = current_author() if family == 'author' else cmp.parse_json((RAW / 'review/synthesis_results.json').read_bytes())
            if family == 'author' and corrupt:
                data['cases'][0]['balanced_dimension'] += 1
            if family == 'author' and invalid:
                data['python'] = True
            Path(command[command.index('--output') + 1]).write_bytes(raw(data))
            return SimpleNamespace(returncode=0, stdout='', stderr='')
        original_run = module.subprocess.run
        self.addCleanup(setattr, module.subprocess, 'run', original_run)
        module.subprocess.run = run
        return module

    def test_success_retains_actual_expected_logs_and_provenance(self):
        module = self.fixture()
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'fresh'
            self.assertEqual(module.main(output_dir=output), 0)
            receipt = json.loads((output / 'execution_receipt.json').read_bytes())
            self.assertEqual(receipt['status'], 'passed')
            self.assertTrue(receipt['source_unchanged'])
            self.assertEqual((output / 'author.expected.raw').read_bytes(), EXPECTED)
            for name in ('author.actual.raw', 'author.stdout', 'author.stderr', 'author.comparison.json',
                         'author.actual.scientific.json', 'author.expected.scientific.json'):
                self.assertTrue((output / name).is_file(), name)

    def test_failure_retains_raw_results_and_exact_mismatch_paths(self):
        module = self.fixture(corrupt=True)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'fresh'
            with self.assertRaisesRegex(AssertionError, 'differs from frozen scientific output'):
                module.main(output_dir=output)
            receipt = json.loads((output / 'execution_receipt.json').read_bytes())
            self.assertEqual(receipt['status'], 'failed')
            self.assertTrue(receipt['source_unchanged'])
            comparison = json.loads((output / 'author.comparison.json').read_bytes())
            self.assertFalse(comparison['scientific_comparison']['equal'])
            self.assertTrue((output / 'author.actual.raw').is_file())
            self.assertEqual((output / 'author.expected.raw').read_bytes(), EXPECTED)

    def test_invalid_provenance_failure_also_retains_raw_results(self):
        module = self.fixture(invalid=True)
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'fresh'
            with self.assertRaisesRegex(AssertionError, 'Invalid top-level version provenance'):
                module.main(output_dir=output)
            receipt = json.loads((output / 'execution_receipt.json').read_bytes())
            self.assertEqual(receipt['status'], 'failed')
            self.assertIn('comparison_error', receipt['runs'][0])
            self.assertTrue((output / 'author.actual.raw').is_file())

    def test_all_eight_split_cases_retain_success_and_failure(self):
        for corrupt in (False, True):
            for case in sorted(cmp.CASES):
                with self.subTest(case=case, corrupt=corrupt), tempfile.TemporaryDirectory() as directory:
                    module = self.fixture(corrupt=corrupt)
                    output = Path(directory) / 'fresh'
                    if corrupt:
                        with self.assertRaisesRegex(AssertionError, 'differs from frozen scientific output'):
                            module.cli(case, ['--output-dir', str(output)])
                    else:
                        self.assertEqual(module.cli(case, ['--output-dir', str(output)]), 0)
                    receipt = json.loads((output / 'execution_receipt.json').read_bytes())
                    self.assertEqual(receipt['status'], 'failed' if corrupt else 'passed')
                    self.assertEqual(receipt['case'], case)
                    self.assertTrue((output / 'independent.actual.raw').is_file())
                    self.assertTrue((output / 'independent.expected.raw').is_file())
                    self.assertTrue((output / 'independent.comparison.json').is_file())

    def test_timeout_retains_partial_logs_and_regular_actual(self):
        module = self.fixture()
        def timeout(command, **kwargs):
            Path(command[command.index('--output') + 1]).write_bytes(raw(current_author()))
            raise module.subprocess.TimeoutExpired(command, 1, output=b'partial stdout', stderr=b'partial stderr')
        module.subprocess.run = timeout
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'fresh'
            with self.assertRaises(module.subprocess.TimeoutExpired):
                module.main(output_dir=output)
            receipt = json.loads((output / 'execution_receipt.json').read_bytes())
            self.assertEqual(receipt['status'], 'failed')
            self.assertTrue(receipt['runs'][0]['timed_out'])
            self.assertIsNone(receipt['runs'][0]['exit_code'])
            self.assertTrue((output / 'author.actual.raw').is_file())
            self.assertEqual((output / 'author.stdout').read_bytes(), b'partial stdout')
            self.assertEqual((output / 'author.stderr').read_bytes(), b'partial stderr')

    def test_existing_or_source_output_directory_rejected(self):
        module = self.fixture()
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(AssertionError, 'fresh and absent'):
                module.main(output_dir=Path(directory))
        with self.assertRaisesRegex(AssertionError, 'external'):
            module.main(output_dir=ROOT / 'build')


if __name__ == '__main__':
    unittest.main()
