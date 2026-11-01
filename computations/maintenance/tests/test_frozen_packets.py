#!/usr/bin/env python3
"""The frozen-packet exemption is narrow, fail-closed and leaves non-packet code covered."""
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[3]


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT/rel)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


frozen = load('frozen_packets_t', 'computations/maintenance/frozen_packets.py')
policy = load('assertion_policy_t', 'computations/maintenance/assertion_policy.py')


def mini_root(tmp):
    root = Path(tmp)
    (root/'computations/maintenance').mkdir(parents=True)
    for name in ('frozen_packets.py', 'assertion_policy.py'):
        shutil.copy(ROOT/'computations/maintenance'/name, root/'computations/maintenance'/name)
    packet = root/'computations/verification/lineZ'
    packet.mkdir(parents=True)
    body = b'assert 1 + 1 == 2\n'
    (packet/'frozen.py').write_bytes(body)
    (packet/'unpinned.py').write_bytes(b'assert True\n')
    (root/'computations/verification/maintained.py').write_bytes(b'assert True\n')
    digest = hashlib.sha256(body).hexdigest()
    (packet/'SHA256SUMS').write_text(digest + '  frozen.py\n')
    registry = {'schema': 'bgs-frozen-evidence-packets-v1', 'directories': ['computations/verification/lineZ'],
                'files': {'computations/verification/lineZ/frozen.py':
                          {'sha256': digest, 'pinned_in': 'computations/verification/lineZ/SHA256SUMS'}}}
    (root/frozen.REGISTRY).write_text(json.dumps(registry))
    return root, packet


class FrozenPacketTests(unittest.TestCase):
    def test_repository_registry_valid(self):
        self.assertEqual(frozen.problems(ROOT), [])
        data = frozen.load(ROOT)
        for rel in data['files']:
            self.assertTrue(rel.startswith('computations/verification/line'), rel)
        self.assertLessEqual(frozen.exempt(ROOT), set(data['files']))

    def test_only_registered_byte_identical_files_are_exempt(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, packet = mini_root(tmp)
            self.assertEqual(frozen.exempt(root), {'computations/verification/lineZ/frozen.py'})
            self.assertEqual(sorted(policy.violations(root)),
                             ['computations/verification/lineZ/unpinned.py',
                              'computations/verification/maintained.py'])
            # Editing a frozen file removes its exemption (fail-closed).
            (packet/'frozen.py').write_bytes(b'assert 1 + 1 == 3\n')
            self.assertEqual(frozen.exempt(root), set())
            self.assertIn('computations/verification/lineZ/frozen.py', policy.violations(root))

    def test_registry_outside_packet_directories_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, packet = mini_root(tmp)
            data = json.loads((root/frozen.REGISTRY).read_text())
            data['directories'].append('computations/maintenance')
            data['files']['computations/verification/maintained.py'] = data['files']['computations/verification/lineZ/frozen.py']
            (root/frozen.REGISTRY).write_text(json.dumps(data))
            bad = frozen.problems(root)
            self.assertTrue(any('not a computations/verification/line' in b for b in bad))
            self.assertTrue(any('outside the listed packet directories' in b for b in bad))
            self.assertEqual(frozen.exempt(root), set())

    def test_pin_mismatch_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, packet = mini_root(tmp)
            (packet/'SHA256SUMS').write_text('0' * 64 + '  frozen.py\n')
            self.assertTrue(frozen.problems(root))
            self.assertEqual(frozen.exempt(root), set())

    def test_compile_check_syntax_warning_scope(self):
        with tempfile.TemporaryDirectory() as tmp:
            root, packet = mini_root(tmp)
            bad = b'x = "\\ "\nassert 1 + 1 == 2\n'
            (packet/'frozen.py').write_bytes(bad)
            digest = hashlib.sha256(bad).hexdigest()
            data = json.loads((root/frozen.REGISTRY).read_text())
            data['files']['computations/verification/lineZ/frozen.py']['sha256'] = digest
            (root/frozen.REGISTRY).write_text(json.dumps(data))
            (packet/'SHA256SUMS').write_text(digest + '  frozen.py\n')
            self.assertEqual(frozen.compile_check(root), [])
            (packet/'unpinned.py').write_bytes(bad)
            failures = frozen.compile_check(root)
            self.assertEqual(len(failures), 1)
            self.assertIn('lineZ/unpinned.py', failures[0])
            (packet/'frozen.py').write_bytes(b'def broken(:\n')
            self.assertTrue(any('frozen.py' in f for f in frozen.compile_check(root)))

    def test_repository_compile_check(self):
        self.assertEqual(frozen.compile_check(ROOT), [])


if __name__ == '__main__':
    unittest.main()
