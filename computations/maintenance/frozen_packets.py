#!/usr/bin/env python3
"""Frozen, hash-pinned evidence packets under computations/verification/line*/.

The registry computations/maintenance/frozen_evidence_packets.json lists the
verbatim packet files that are outside the assertion-entry policy and the
compileall SyntaxWarning-as-error step (owner decision, 2026-11-01). The
exemption is per file and fail-closed: a listed file is exempt only while its
current sha256 equals the registered value and that value appears verbatim in
the registered pin file (the packet SHA manifest or dated receipt). This
module never certifies mathematics; it only scopes two code-hygiene checks.

  python computations/maintenance/frozen_packets.py --check
  python computations/maintenance/frozen_packets.py --compile-check
"""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRY = 'computations/maintenance/frozen_evidence_packets.json'
PACKET_DIR = re.compile(r'^computations/verification/line[A-Za-z0-9_]+$')


def load(root: Path = ROOT) -> dict:
    data = json.loads((root / REGISTRY).read_text(encoding='utf-8'))
    if data.get('schema') != 'bgs-frozen-evidence-packets-v1':
        raise ValueError('frozen packet registry schema changed')
    return data


def problems(root: Path = ROOT) -> list[str]:
    data = load(root)
    out = []
    dirs = data['directories']
    if dirs != sorted(set(dirs)):
        out.append('directories not sorted/unique')
    for d in dirs:
        if not PACKET_DIR.match(d) or not (root / d).is_dir():
            out.append('not a computations/verification/line*/ packet directory: ' + d)
    pins = {}
    for rel, row in data['files'].items():
        if not rel.endswith('.py') or '/'.join(rel.split('/')[:3]) not in dirs:
            out.append('file outside the listed packet directories: ' + rel)
            continue
        pin = row['pinned_in']
        if pin not in pins:
            p = root / pin
            pins[pin] = p.read_text(encoding='utf-8', errors='replace') if p.is_file() else None
        if pins[pin] is None:
            out.append('missing pin file: ' + pin)
        elif row['sha256'] not in pins[pin]:
            out.append('registered sha256 not in pin file: ' + rel)
    used = {'/'.join(rel.split('/')[:3]) for rel in data['files']}
    out += ['directory with no pinned file: ' + d for d in dirs if d not in used]
    return out


def drift(root: Path = ROOT) -> list[str]:
    """Registered packet files that are missing or no longer byte-identical."""
    out = []
    for rel, row in load(root)['files'].items():
        p = root / rel
        if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest() != row['sha256']:
            out.append('frozen packet file changed or missing (now in policy scope): ' + rel)
    return out


def exempt(root: Path = ROOT) -> set[str]:
    """Repository-relative paths currently exempt (registered and byte-identical)."""
    data = load(root)
    if problems(root):
        return set()
    result = set()
    for rel, row in data['files'].items():
        p = root / rel
        if p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest() == row['sha256']:
            result.add(rel)
    return result


def compile_check(root: Path = ROOT) -> list[str]:
    """Byte-compile every .py under computations/ in memory.

    SyntaxWarning is an error everywhere except for currently exempt frozen
    packet files, which must still compile (a SyntaxError always fails).
    Nothing is written to __pycache__.
    """
    import warnings
    skip = exempt(root)
    failures = []
    for p in sorted((root / 'computations').rglob('*.py')):
        rel = p.relative_to(root).as_posix()
        if '__pycache__' in rel.split('/'):
            continue
        source = p.read_bytes()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore' if rel in skip else 'error', SyntaxWarning)
            try:
                compile(source, rel, 'exec', dont_inherit=True)
            except (SyntaxError, SyntaxWarning, ValueError) as exc:
                failures.append(f'{rel}: {type(exc).__name__}: {exc}')
    return failures


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--compile-check', action='store_true')
    a = ap.parse_args()
    bad = problems()
    if a.compile_check:
        failed = bad or compile_check()
        if failed:
            print('compile-check: FAIL\n' + '\n'.join(failed), file=sys.stderr)
            return 1
        print(f'compile-check: OK (SyntaxWarning is an error outside {len(exempt())} exempt frozen packet files)')
        return 0
    bad += drift()
    if bad:
        print('frozen-packets: FAIL\n' + '\n'.join(bad), file=sys.stderr)
        return 1
    data = load()
    print(f"frozen-packets: OK ({len(data['directories'])} packet directories, {len(data['files'])} registered files, all byte-identical and exempt)")
    return 0


if __name__ == '__main__':
    sys.exit(main())
