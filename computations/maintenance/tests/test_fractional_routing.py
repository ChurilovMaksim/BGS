"""Exercise the maintained routing helper, including all nine current entries."""
from pathlib import Path
import json
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]


class FractionalRouting(unittest.TestCase):
    def test_current_routing_and_corruption_contract(self):
        for flags in ([], ['-O']):
            with tempfile.TemporaryDirectory() as directory:
                output = Path(directory) / 'routing.json'
                result = subprocess.run([sys.executable, '-B', *flags,
                    str(ROOT / 'computations/verification/fractional_hamming/check_routing.py'),
                    '--output', str(output)], capture_output=True, text=True, timeout=30,
                    env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
                self.assertEqual((result.returncode, result.stdout, result.stderr), (0, '', ''))
                receipt = json.loads(output.read_text())
                self.assertTrue(receipt['all_nine_current_entries_covered'])
                self.assertTrue(receipt['scientific_corruption_rejected'])
                self.assertEqual(len(receipt['calls']), 10)
                self.assertTrue(receipt['repository_unchanged'])


if __name__ == '__main__':
    unittest.main()
