"""Check the four-cut runner rejects source-output overlap before writes."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
RUNNER = ROOT / 'computations/verification/run_four_cut_kernel.py'
spec = importlib.util.spec_from_file_location('four_cut_runner', RUNNER)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)

class OutputPolicyTests(unittest.TestCase):
    def test_source_and_ancestor_rejected_without_creation(self):
        paths = [ROOT, ROOT.parent, ROOT/'mathematics',
                 ROOT/'evidence/four_cut_output_must_not_exist',
                 ROOT/'computations/verification/four_cut_output_must_not_exist']
        for mode in ([], ['-O']):
            for path in paths:
                existed = path.exists()
                result = subprocess.run([sys.executable, *mode, str(RUNNER), '--output', str(path)],
                                        capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertRegex(result.stderr, 'Output (overlaps|must be outside)')
                self.assertEqual(path.exists(), existed)
                self.assertEqual(result.stdout, '')

    def test_external_build_and_symlink_resolution(self):
        self.assertEqual(runner.validate_output(ROOT/'build/four-cut-test'), ROOT/'build/four-cut-test')
        with tempfile.TemporaryDirectory(prefix='bgs-output-policy-') as tmp:
            p = Path(tmp)
            self.assertEqual(runner.validate_output(p/'new'), p/'new')
            alias = p/'source-link'
            alias.symlink_to(ROOT, target_is_directory=True)
            with self.assertRaises(RuntimeError):
                runner.validate_output(alias/'mathematics/new')
            existing_file = p/'file'
            existing_file.write_text('keep')
            with self.assertRaises(RuntimeError):
                runner.validate_output(existing_file)
            self.assertEqual(existing_file.read_text(), 'keep')

if __name__ == '__main__':
    unittest.main()
