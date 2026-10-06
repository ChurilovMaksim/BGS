"""Portable-entry and fail-closed-input controls, independent of the full replay."""
from pathlib import Path
import ast
import importlib.util
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
ENTRY = ROOT / 'computations/verification/ramified_first_seven_trace.py'

def module():
    spec = importlib.util.spec_from_file_location('ramified_test', ENTRY)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

class RamifiedPortability(unittest.TestCase):
    def test_silent_normal_and_optimized_import(self):
        self.assertFalse(any(isinstance(n, ast.Assert) for n in ast.walk(ast.parse(ENTRY.read_text()))))
        for optimized in (False, True):
            cmd = [sys.executable] + (['-O'] if optimized else [])
            cmd += ['-B', '-c', 'import importlib.util,sys; s=importlib.util.spec_from_file_location("check",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)', str(ENTRY)]
            result = subprocess.run(cmd, check=True, capture_output=True, text=True)
            self.assertEqual(result.stdout, '')
            self.assertEqual(result.stderr, '')
    def test_input_tampering_and_zero_inverse(self):
        m = module()
        m.verify_certificate()
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / 'bad.json'
            p.write_text('{}\n')
            with self.assertRaises(RuntimeError):
                m.verify_certificate(p)
        with self.assertRaises(RuntimeError):
            m.inv(m.zero)
        with self.assertRaises(RuntimeError):
            m.power(m.zero, -1)
    def test_source_output_rejected(self):
        result = subprocess.run([sys.executable, str(ENTRY), '--output', str(ENTRY.parent / 'forbidden.json')], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Output inside maintained source is forbidden', result.stderr)
        self.assertFalse((ENTRY.parent / 'forbidden.json').exists())

if __name__ == '__main__':
    unittest.main()
