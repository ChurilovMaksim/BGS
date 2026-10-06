"""Entry-point, identity and input-validation regressions for first-seven replay."""
from pathlib import Path
import ast
import hashlib
import importlib.util
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
ENTRY = ROOT / 'computations/verification/first_seven_commutant.py'
DATA = ROOT / 'computations/verification/first_seven/certificate.txt'

def module():
    spec = importlib.util.spec_from_file_location('first_seven_replay_test', ENTRY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class FirstSevenPortability(unittest.TestCase):
    def test_silent_imports_and_explicit_checks(self):
        for path in [ENTRY, ENTRY.parent / 'first_seven/dictionary.py']:
            tree = ast.parse(path.read_text())
            self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(tree)))
            for optimized in (False, True):
                args = [sys.executable] + (['-O'] if optimized else [])
                args += ['-B', '-c', 'import importlib.util,sys; s=importlib.util.spec_from_file_location("control",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)', str(path)]
                result = subprocess.run(args, check=True, text=True, capture_output=True)
                self.assertEqual(result.stdout, '')
                self.assertEqual(result.stderr, '')
    def test_certificate_tampering_rejected(self):
        m = module()
        m.verify_input(DATA)
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'data.txt'
            p.write_bytes(DATA.read_bytes() + b'0\n')
            with self.assertRaises(RuntimeError):
                m.verify_input(p)
    def test_source_output_rejected(self):
        with self.assertRaises(ValueError):
            module().output_directory(ENTRY.parent)

if __name__ == '__main__':
    unittest.main()
