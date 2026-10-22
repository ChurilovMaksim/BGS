#!/usr/bin/env python3
"""Source-bound bounded exact Schur replay; silent on success and import."""
from pathlib import Path
import hashlib
import importlib.util

REPLAY_SHA256 = 'd59bede7888fc5da5d123ea628ccf7e3faa3245fe8aba154e1454434a93f12ee'


def main(argv=None):
    path = Path(__file__).resolve().parent / 'schur/full_replay.py'
    if hashlib.sha256(path.read_bytes()).hexdigest() != REPLAY_SHA256:
        raise RuntimeError('Schur replay source hash mismatch')
    spec = importlib.util.spec_from_file_location('bgs_schur_replay', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.main(argv)


if __name__ == '__main__':
    raise SystemExit(main())
