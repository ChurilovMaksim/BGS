"""Import and nonnormal-fixture regressions for the mixed exact controls."""
from pathlib import Path
import subprocess
import sys
import unittest

V = Path(__file__).resolve().parents[3]/'computations/verification'
LOAD = 'import importlib.util,sys;s=importlib.util.spec_from_file_location("m",sys.argv[1]);m=importlib.util.module_from_spec(s);s.loader.exec_module(m)'


class FactorialDiagonalPortability(unittest.TestCase):
    def test_silent_imports(self):
        for p in [V/'factorial_diagonal_extension.py',*sorted((V/'factorial_diagonal').glob('*.py'))]:
            for flags in ([], ['-O']):
                r = subprocess.run([sys.executable,*flags,'-B','-c',LOAD,str(p)],capture_output=True,text=True,check=True)
                self.assertEqual(r.stdout+r.stderr,'')

    def test_normal_circulant_cannot_pass_nonnormal_control(self):
        code = 'from pathlib import Path;import sys;s=Path(sys.argv[1]).read_text().replace("(S.eye(n) + 2 * cyc + 3 * swap) / 6","(S.eye(n) + 2 * cyc) / 3");d={};exec(compile(s,"negative-control","exec"),d);d["fixture"](3)'
        for flags in ([], ['-O']):
            r = subprocess.run([sys.executable,*flags,'-B','-c',code,str(V/'factorial_diagonal/general.py')],capture_output=True,text=True)
            self.assertNotEqual(r.returncode,0)
            self.assertIn('Exact check failed',r.stderr)


if __name__ == '__main__':
    unittest.main()
