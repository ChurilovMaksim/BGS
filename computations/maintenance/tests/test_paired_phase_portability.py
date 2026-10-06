"""Bounded paired-phase entry policy and imported helper silence."""
from pathlib import Path
import ast
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[3]
DIRECTORY=ROOT/'computations/verification'

class PairedPhasePortability(unittest.TestCase):
    def test_silent_imports_explicit_checks(self):
        paths=[DIRECTORY/'paired_phase_reductions.py']+sorted((DIRECTORY/'paired_phase').glob('*.py'))
        for p in paths:
            self.assertFalse(any(isinstance(n,ast.Assert) for n in ast.walk(ast.parse(p.read_text()))))
            self.assertTrue(any(isinstance(n,ast.FunctionDef) and n.name=='main' for n in ast.parse(p.read_text()).body))
            for optimized in (False,True):
                cmd=[sys.executable]+(['-O'] if optimized else [])+['-B','-c','import importlib.util,sys; s=importlib.util.spec_from_file_location("m",sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m)',str(p)]
                r=subprocess.run(cmd,check=True,capture_output=True,text=True)
                self.assertEqual(r.stdout,'');self.assertEqual(r.stderr,'')
    def test_source_output_rejected(self):
        r=subprocess.run([sys.executable,str(DIRECTORY/'paired_phase_reductions.py'),'--output',str(DIRECTORY)],capture_output=True,text=True)
        self.assertNotEqual(r.returncode,0);self.assertIn('Output inside maintained source is forbidden',r.stderr)

if __name__=='__main__':unittest.main()
