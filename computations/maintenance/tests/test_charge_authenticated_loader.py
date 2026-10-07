"""Ensure authenticated charge comparator ignores poisoned bytecode caches."""
from pathlib import Path
import hashlib
import importlib.util
import json
import marshal
import struct
import tempfile
import types
import unittest

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / 'computations/verification/charge_strengthening_replay.py'


class AuthenticatedChargeLoader(unittest.TestCase):
    def test_matching_timestamp_pyc_is_not_executed(self):
        module = types.ModuleType('charge_loader_test')
        module.__file__ = str(SOURCE)
        exec(compile(SOURCE.read_bytes(), str(SOURCE), 'exec'), module.__dict__)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            rel = 'computations/verification/charge_strengthening/comparison.py'
            path = root / rel
            path.parent.mkdir(parents=True)
            raw = (ROOT / rel).read_bytes()
            path.write_bytes(raw)
            manifest = root / 'record/charge_strengthening_replay_sources.json'
            manifest.parent.mkdir()
            manifest.write_text(json.dumps({'schema':'bgs-charge-replay-sources-v1',
                'files':[{'path':rel,'sha256':hashlib.sha256(raw).hexdigest()}]}))
            module.ROOT = root
            module.MODULES = path.parent
            module.SOURCE_MAP = manifest
            poison = "LOAD_ORIGIN='untrusted_timestamp_pyc'\ndef compare(*args): return {'scientific_comparison':{'equal':True}}\n"
            for optimized in (None, '1'):
                cache = Path(importlib.util.cache_from_source(str(path), optimization=optimized))
                cache.parent.mkdir(exist_ok=True)
                header = importlib.util.MAGIC_NUMBER + struct.pack('<III', 0, int(path.stat().st_mtime), len(raw))
                cache.write_bytes(header + marshal.dumps(compile(poison, str(path), 'exec')))
            comp = module.comparator()
            self.assertFalse(hasattr(comp, 'LOAD_ORIGIN'))
            result = comp.compare('author-exact-v1', {'answer':1}, {'answer':999}, {}, {})
            self.assertFalse(result['scientific_comparison']['equal'])
            path.write_bytes(raw + b'\n')
            with self.assertRaisesRegex(RuntimeError, 'Source SHA256 mismatch'):
                module.comparator()


if __name__ == '__main__':
    unittest.main()
