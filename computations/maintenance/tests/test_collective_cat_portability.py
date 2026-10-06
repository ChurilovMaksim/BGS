"""New entry points remain silent; explicit domain checks survive optimization."""
from pathlib import Path
import subprocess
import sys
import unittest

V = Path(__file__).resolve().parents[3]/'computations/verification'
LOAD = 'import importlib.util,sys;s=importlib.util.spec_from_file_location("m",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)'


class CollectiveCatPortability(unittest.TestCase):
    def test_silent_entry_and_helper_imports(self):
        paths = [V/name for name in ['collective_hierarchy.py','cat_jet_certificates.py','fm008_independent.py','ordered_diagonal_companion.py']]
        paths += sorted((V/'cat_jet').glob('*.py'))
        paths += sorted((V/'collective').glob('*.py'))
        paths += sorted((V/'ordered_diagonal').glob('*.py'))
        for p in paths:
            for flags in ([], ['-O']):
                r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD,str(p)],capture_output=True,text=True,check=True)
                self.assertEqual(r.stdout+r.stderr,'')

    def test_zero_root_difference_rejected(self):
        for flags in ([], ['-O']):
            r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD+';m.vroot(7,7)',str(V/'fm008_independent.py')],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('zero root difference',r.stderr)

    def test_ordered_explicit_failure_active(self):
        for flags in ([], ['-O']):
            r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD+';m.require(False,"negative control")',str(V/'ordered_diagonal/exact.py')],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('negative control',r.stderr)


if __name__ == '__main__':
    unittest.main()
