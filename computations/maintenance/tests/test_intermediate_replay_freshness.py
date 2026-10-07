"""A successful process cannot reuse a staged historical replay result."""
from pathlib import Path
import base64
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]
WRAPPER = ROOT / 'computations/verification/intermediate_old_layers_certificates.py'
EVIDENCE = Path('evidence/intermediate_old_layers_20261007')
EXPECTED = {'exact_checks': 7, 'gcd_degree': 0, 'result': 'PASS'}


def fixture(root, producer, same_path=True):
    evidence = root / EVIDENCE
    evidence.mkdir(parents=True)
    raw = json.dumps(EXPECTED).encode()
    digest = hashlib.sha256(raw).hexdigest()
    blob = evidence / 'input.json'
    blob.write_text(json.dumps({'payload': base64.b64encode(raw).decode()}))
    expected = 'result.json' if same_path else 'historical.json'
    (evidence / 'input_map.json').write_text(json.dumps({
        'groups': {'fixture': {expected: digest}},
        'blobs': {digest: str(blob.relative_to(root))},
        'steps': [{'name': 'first_position', 'module': 'producer.py',
                   'group': 'fixture', 'expected': expected,
                   'result': 'result.json', 'source_sha256': 'fixture'}],
    }))
    (root / 'producer.py').write_text(producer)
    return blob, blob.read_bytes()


class IntermediateReplayFreshness(unittest.TestCase):
    def test_noop_missing_and_early_return_fail_with_or_without_staged_result(self):
        for flags in ([], ['-O']):
            for same_path in (False, True):
                for body in ('pass', 'return None'):
                    with self.subTest(flags=flags, same_path=same_path, body=body):
                        with tempfile.TemporaryDirectory() as directory:
                            root = Path(directory)
                            blob, before = fixture(root, 'def run(root):\n    ' + body + '\n', same_path)
                            result = subprocess.run([sys.executable, *flags, '-B', str(WRAPPER), '--root', str(root)],
                                                    capture_output=True, text=True)
                            self.assertNotEqual(result.returncode, 0)
                            self.assertIn('did not create a fresh regular result', result.stderr)
                            self.assertEqual(blob.read_bytes(), before)

    def test_new_correct_result_passes_and_new_wrong_result_fails(self):
        for flags in ([], ['-O']):
            for good in (True, False):
                with self.subTest(flags=flags, good=good), tempfile.TemporaryDirectory() as directory:
                    root = Path(directory)
                    output = dict(EXPECTED, gcd_degree=0 if good else 1)
                    producer = ('import json\n'
                                'def run(root):\n'
                                '    if (root / "result.json").exists():\n'
                                '        raise RuntimeError("output was already staged")\n'
                                '    (root / "result.json").write_text(json.dumps(' + repr(output) + '))\n')
                    blob, before = fixture(root, producer)
                    result = subprocess.run([sys.executable, *flags, '-B', str(WRAPPER), '--root', str(root)],
                                            capture_output=True, text=True)
                    self.assertEqual(result.returncode == 0, good, result.stderr)
                    self.assertEqual(blob.read_bytes(), before)
                    if good:
                        row = json.loads(result.stdout)['runs'][0]
                        self.assertTrue(row['fresh_result_created'])
                        self.assertTrue(row['private_step_workspace'])
                    else:
                        self.assertIn('gcd_degree', result.stderr)
                        self.assertIn('preserved diagnostics', result.stderr)

    def test_mutating_original_input_is_rejected(self):
        producer = ('import json\n'
                    'def run(root):\n'
                    '    expected = json.loads((root / "historical.json").read_text())\n'
                    '    (root / "historical.json").write_text("changed")\n'
                    '    (root / "result.json").write_text(json.dumps(expected))\n')
        for flags in ([], ['-O']):
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                blob, before = fixture(root, producer, same_path=False)
                result = subprocess.run([sys.executable, *flags, '-B', str(WRAPPER), '--root', str(root),
                                         '--replay-output-dir', str(root / 'evidence_out')],
                                        capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('modified an original input', result.stderr)
                self.assertEqual(blob.read_bytes(), before)
                self.assertEqual(json.loads((root / 'evidence_out/0/actual.json').read_text()), EXPECTED)
                self.assertEqual(json.loads((root / 'evidence_out/0/expected.json').read_text()), EXPECTED)

    def test_symlink_result_is_not_fresh_regular_output(self):
        producer = ('def run(root):\n'
                    '    (root / "result.json").symlink_to(root / "historical.json")\n')
        for flags in ([], ['-O']):
            with tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                fixture(root, producer, same_path=False)
                result = subprocess.run([sys.executable, *flags, '-B', str(WRAPPER), '--root', str(root)],
                                        capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn('fresh regular result', result.stderr)


if __name__ == '__main__':
    unittest.main()
