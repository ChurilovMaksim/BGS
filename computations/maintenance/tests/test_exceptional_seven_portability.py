"""Bounded integer checker import and optimized-failure controls."""
from pathlib import Path
import subprocess
import sys
import unittest

ENTRY = Path(__file__).resolve().parents[3]/'computations/verification/exceptional_seven_commutant.py'
LOAD = 'import importlib.util,sys; s=importlib.util.spec_from_file_location("m",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)'


class ExceptionalSevenPortability(unittest.TestCase):
    def test_silent_imports_and_active_failures(self):
        for flags in ([], ['-O']):
            cmd = [sys.executable, *flags, '-B', '-c', LOAD, str(ENTRY)]
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            self.assertEqual(result.stdout + result.stderr, '')
            cmd[-2] += '; m.require(False,"negative control")'
            result = subprocess.run(cmd, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn('negative control', result.stderr)


if __name__ == '__main__':
    unittest.main()
