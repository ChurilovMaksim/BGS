#!/usr/bin/env python3
"""CLI assertion-guard regression; finite checks only, not a theorem certificate.

Run: python3 -m unittest discover -s computations/maintenance/tests
              -p test_collective_assertion_guard.py
"""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


class CollectiveAssertionGuardTests(unittest.TestCase):
    def test_valid_and_false_coordinate_identity(self):
        repo = Path(__file__).resolve().parents[3]
        source_path = repo/'computations/verification/collective_diffusion_gap.py'
        source = source_path.read_text()
        needle = 'predicted=add(diag,mul(off,add(phase(relative,n),phase(-relative,n)),n))'
        self.assertEqual(source.count(needle), 1, 'Mutation target changed')
        mutated = source.replace(needle, needle.replace('add(diag,', 'add({0:F(1)},diag,'))
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
                   PYTHONPATH=str(repo/'computations/verification'))
        env.pop('PYTHONOPTIMIZE', None)
        with tempfile.TemporaryDirectory(prefix='bgs_guard_regression_') as tmp:
            directory = Path(tmp)
            for variant, content in [('valid', source), ('mutated', mutated)]:
                script = directory/(variant+'.py')
                script.write_text(content)
                for mode in ['normal', '-O', '-OO', 'PYTHONOPTIMIZE=1', 'PYTHONOPTIMIZE=2']:
                    with self.subTest(variant=variant, mode=mode):
                        report = directory/(variant+'_'+mode.replace('=', '_')+'.json')
                        command = [sys.executable, '-B']
                        child_env = env.copy()
                        if mode.startswith('-O'):
                            command.append(mode)
                        elif mode.startswith('PYTHONOPTIMIZE='):
                            child_env['PYTHONOPTIMIZE'] = mode[-1]
                        command += [str(script), '--output', str(report)]
                        process = subprocess.run(command, env=child_env, text=True,
                                                 capture_output=True, timeout=300)
                        detail = process.stdout + process.stderr
                        if mode == 'normal' and variant == 'valid':
                            self.assertEqual(process.returncode, 0, detail)
                            result = json.loads(process.stdout)
                            self.assertEqual(result['status'], 'PASS')
                            self.assertEqual(json.loads(report.read_text()), result)
                            self.assertEqual(result['counts']['q_coordinate_coefficients'], 3107)
                            self.assertEqual(result['counts']['p_coordinate_entries'], 49062)
                        else:
                            self.assertNotEqual(process.returncode, 0, detail)
                            self.assertNotIn('"status": "PASS"', process.stdout)
                            self.assertFalse(report.exists(), 'Failed verification wrote a certificate')
                            if mode != 'normal':
                                self.assertIn('Verification requires assertions', process.stderr)
                            else:
                                self.assertIn('AssertionError: (3, 0, 0, 0, 0)', process.stderr)


if __name__ == '__main__':
    unittest.main()
