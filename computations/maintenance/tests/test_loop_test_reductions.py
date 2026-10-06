"""Portable regression for explicit failures, optimized execution and silent import."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[2] / 'verification' / 'loop_test_reductions.py'


class LoopReductionTests(unittest.TestCase):
    def invoke(self, optimized, *args, cwd=None):
        return subprocess.run([sys.executable]+(['-O'] if optimized else [])+[str(SCRIPT),*args],capture_output=True,text=True,cwd=cwd,check=False)

    def test_valid_normal_and_optimized(self):
        for optimized in (False,True):
            with self.subTest(optimized=optimized):
                result=self.invoke(optimized)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertTrue(json.loads(result.stdout)['all_passed'])

    def test_each_explicit_failure_in_both_modes(self):
        for optimized in (False,True):
            for target in ('pair','cubic','tensor'):
                with self.subTest(optimized=optimized,target=target):
                    result=self.invoke(optimized,'--inject-failure',target)
                    self.assertEqual(result.returncode,2)
                    self.assertIn('CHECK FAILED:',result.stderr)
                    self.assertEqual(result.stdout,'')

    def test_silent_import_in_both_modes(self):
        for optimized in (False,True):
            with self.subTest(optimized=optimized), tempfile.TemporaryDirectory() as temp:
                code='import sys; sys.path.insert(0, '+repr(str(SCRIPT.parent))+'); import loop_test_reductions'
                env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1')
                result=subprocess.run([sys.executable]+(['-O'] if optimized else [])+['-c',code],cwd=temp,capture_output=True,text=True,env=env,check=False)
                self.assertEqual(result.returncode,0,result.stderr)
                self.assertEqual(result.stdout,'')
                self.assertEqual(result.stderr,'')
                self.assertEqual(list(Path(temp).iterdir()),[])

    def test_portable_explicit_output(self):
        with tempfile.TemporaryDirectory() as temp:
            output=Path(temp)/'result.json'
            result=self.invoke(False,'--output',str(output),cwd=temp)
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertEqual(json.loads(output.read_text()),json.loads(result.stdout))


if __name__ == '__main__':
    unittest.main()
