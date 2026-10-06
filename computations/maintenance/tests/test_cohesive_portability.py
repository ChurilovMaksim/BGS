"""Portable research entry points stay silent and optimized checks remain active."""
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[3]
V = ROOT/'computations/verification'
LOAD = 'import importlib.util,sys;s=importlib.util.spec_from_file_location("m",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)'


class CohesivePortability(unittest.TestCase):
    def test_silent_imports(self):
        paths = [V/'exact_homoclinic.py', V/'spectral_extensions.py', V/'weighted_periodic_support.py']
        paths += sorted((V/'spectral_extension').glob('*.py'))
        paths += sorted((V/'weighted_support').glob('*.py'))
        for p in paths:
            for flags in ([], ['-O']):
                r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD,str(p)],capture_output=True,text=True,check=True)
                self.assertEqual(r.stdout+r.stderr, '')

    def test_optimized_arithmetic_corruption_rejected(self):
        code = 'from pathlib import Path;import sys;s=Path(sys.argv[1]).read_text().replace("F(51451, 1000)","F(51452, 1000)");d={};exec(compile(s,"negative-control","exec"),d);d["run"]()'
        p = V/'weighted_support/equidistribution.py'
        for flags in ([], ['-O']):
            r = subprocess.run([sys.executable,*flags,'-B','-c',code,str(p)],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('Exact check failed',r.stderr)

    def test_invalid_modes_rejected(self):
        for name in ['spectral_extensions.py','weighted_periodic_support.py']:
            r = subprocess.run([sys.executable,'-O','-B',str(V/name),'--mode','unbounded'],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('invalid choice',r.stderr)


if __name__ == '__main__':
    unittest.main()
