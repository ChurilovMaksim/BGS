"""Guard explicit checks, import silence and source-safe default outputs."""
from pathlib import Path
import ast
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'computations/verification'
NAMES = ('actual_algebra_check', 'actual_factor_check', 'actual_field_check',
         'actual_casoratian_check', 'actual_commutant_common', 'seven_primary_certificate',
         'global_rotated_box_trace')

class ActualCommutantPortability(unittest.TestCase):
    def test_silent_imports_explicit_checks(self):
        for name in NAMES:
            with self.subTest(name=name):
                source = (DIRECTORY / (name + '.py')).read_text()
                self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(ast.parse(source))))
                for optimized in (False, True):
                    cmd = [sys.executable] + (['-O'] if optimized else [])
                    cmd += ['-B', '-c', 'import sys; sys.path.insert(0, sys.argv[1]); __import__(sys.argv[2])', str(DIRECTORY), name]
                    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
                    self.assertEqual(result.stdout, '')
                    self.assertEqual(result.stderr, '')
    def test_output_defaults_under_build(self):
        for name in NAMES[:4]:
            source = (DIRECTORY / (name + '.py')).read_text()
            self.assertNotIn('default=Path.cwd()', source)
            self.assertIn("'build' / 'actual_commutant'", source)
            self.assertIn('def main(', source)

if __name__ == '__main__':
    unittest.main()
