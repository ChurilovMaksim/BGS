#!/usr/bin/env python3
"""Source-bound bounded exact Schur replay; silent on success and import."""
from pathlib import Path
import hashlib
import importlib.util
import os
import stat

REPLAY_SHA256 = 'dda9af075541853724f34027f50bd35fa636624a7d4f3647fe24272dc4437d4e'


def main(argv=None):
    path = Path(__file__).resolve().parent / 'schur/full_replay.py'
    for component in (path, *path.parents):
        if component.is_symlink():
            raise RuntimeError('Schur replay source path/ancestor is a symlink')
    info = path.lstat()
    if not stat.S_ISREG(info.st_mode):
        raise RuntimeError('Schur replay source is not a regular file')
    fd = os.open(path, os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK)
    with os.fdopen(fd, 'rb') as stream:
        current = os.fstat(stream.fileno())
        if (info.st_dev, info.st_ino) != (current.st_dev, current.st_ino):
            raise RuntimeError('Schur replay source identity changed')
        raw = stream.read()
    if hashlib.sha256(raw).hexdigest() != REPLAY_SHA256:
        raise RuntimeError('Schur replay source hash mismatch')
    spec = importlib.util.spec_from_file_location('bgs_schur_replay', path)
    module = importlib.util.module_from_spec(spec)
    # Execute exactly the verified source bytes, ignoring any precompiled cache.
    exec(compile(raw, str(path), 'exec'), module.__dict__)
    return module.main(argv)


if __name__ == '__main__':
    raise SystemExit(main())
