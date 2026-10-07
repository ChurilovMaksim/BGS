"""Intermediate arithmetic helper imports and explicit failures remain portable."""
from pathlib import Path
import subprocess
import sys
import unittest

V = Path(__file__).resolve().parents[3]/'computations/verification'
LOAD = 'import importlib.util,sys;s=importlib.util.spec_from_file_location("m",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)'


class IntermediateLayerPortability(unittest.TestCase):
    def test_imports_are_silent(self):
        for p in [V/'intermediate_old_layers_certificates.py',*sorted((V/'intermediate_old_layers').glob('*.py'))]:
            for flags in ([], ['-O']):
                r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD,str(p)],capture_output=True,text=True,check=True)
                self.assertEqual(r.stdout+r.stderr,'')

    def test_explicit_failure_survives_optimization(self):
        for flags in ([], ['-O']):
            r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD+';m.require(False,"negative control")',str(V/'intermediate_old_layers_certificates.py')],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('negative control',r.stderr)


if __name__ == '__main__':
    unittest.main()
