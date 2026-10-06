"""Silent imports, active optimized checks and source-safe outputs."""
from pathlib import Path
import ast
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[3]
ENTRY=ROOT/'computations/verification/ramified_higher_commutant.py'
CHILD=ENTRY.parent/'ramified_higher/checks.py'

class HigherRamifiedPortability(unittest.TestCase):
    def test_imports_and_no_assertions(self):
        for p in (ENTRY,CHILD):
            self.assertFalse(any(isinstance(x,ast.Assert) for x in ast.walk(ast.parse(p.read_text()))))
            for optimized in (False,True):
                cmd=[sys.executable]+(['-O'] if optimized else [])+['-B','-c','import importlib.util,sys; s=importlib.util.spec_from_file_location("m",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)',str(p)]
                r=subprocess.run(cmd,check=True,capture_output=True,text=True)
                self.assertEqual(r.stdout,'');self.assertEqual(r.stderr,'')
    def test_optimized_zero_inverse_rejected(self):
        code='import importlib.util,sys; s=importlib.util.spec_from_file_location("m",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); m.initialize_field(); m.inv(m.ZERO)'
        r=subprocess.run([sys.executable,'-O','-c',code,str(CHILD)],capture_output=True,text=True)
        self.assertNotEqual(r.returncode,0);self.assertIn('Exact check failed',r.stderr)
    def test_source_output_rejected(self):
        r=subprocess.run([sys.executable,str(ENTRY),'--output',str(ENTRY.parent)],capture_output=True,text=True)
        self.assertNotEqual(r.returncode,0);self.assertIn('Output inside maintained source is forbidden',r.stderr)

if __name__=='__main__':unittest.main()
