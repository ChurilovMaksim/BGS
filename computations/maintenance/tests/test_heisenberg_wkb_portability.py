"""Portable entry-point checks for the new bounded WKB fixtures."""
from pathlib import Path
import ast
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
DIRECTORY = ROOT / 'computations/verification/heisenberg_wkb'

class WkbPortability(unittest.TestCase):
    def test_silent_imports_and_explicit_checks(self):
        for path in sorted(DIRECTORY.glob('*.py')):
            with self.subTest(path=path.name):
                tree = ast.parse(path.read_text())
                self.assertFalse(any(isinstance(node, ast.Assert) for node in ast.walk(tree)))
                self.assertTrue(any(isinstance(node, ast.FunctionDef) and node.name == 'main' for node in tree.body))
                for optimized in (False, True):
                    command = [sys.executable] + (['-O'] if optimized else [])
                    command += ['-B', '-c', 'import sys; sys.path.insert(0, sys.argv[1]); __import__(sys.argv[2])', str(DIRECTORY), path.stem]
                    result = subprocess.run(command, capture_output=True, text=True, check=True)
                    self.assertEqual(result.stdout, '')
                    self.assertEqual(result.stderr, '')
    def test_no_source_output_writes(self):
        for path in DIRECTORY.glob('*.py'):
            tree = ast.parse(path.read_text())
            writes = [node for node in ast.walk(tree) if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr in ('write_text', 'write_bytes')]
            self.assertEqual(writes, [], path.name)

if __name__ == '__main__':
    unittest.main()
