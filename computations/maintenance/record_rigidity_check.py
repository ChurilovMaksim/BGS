#!/usr/bin/env python3
"""Run one explicitly supplied check and retain its status and source hashes.

This is execution provenance, not a certificate of an analytic theorem.
Usage: record_rigidity_check.py LABEL -- command arguments...
"""
from __future__ import annotations
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]

def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def source_hashes() -> dict[str, str]:
    return {str(p.relative_to(ROOT)): digest(p)
            for sub in ('mathematics', 'literature', 'computations', 'manuscript')
            for p in sorted((ROOT / sub).rglob('*'))
            if p.is_file() and p.suffix in ('.py', '.cpp', '.md', '.tex', '.lean')}

def main() -> None:
    if len(sys.argv) < 4 or sys.argv[2] != '--':
        raise SystemExit('Usage: record_rigidity_check.py LABEL -- command arguments...')
    label, command = sys.argv[1], sys.argv[3:]
    if not label.replace('_', '').replace('-', '').isalnum():
        raise SystemExit('Use a simple alphanumeric label.')
    dst = ROOT / 'evidence'
    dst.mkdir(exist_ok=True)
    log = dst / 'logs' / (label + '.log')
    log.parent.mkdir(exist_ok=True)
    before = source_hashes()
    start = time.monotonic()
    when = dt.datetime.now(dt.timezone.utc).isoformat()
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    with log.open('w') as stream:
        result = subprocess.run(command, cwd=ROOT, env=env, stdout=stream, stderr=subprocess.STDOUT)
    after = source_hashes()
    entry = {'label': label, 'command': command, 'cwd': '.', 'started_utc': when,
             'elapsed_seconds': round(time.monotonic() - start, 3),
             'returncode': result.returncode, 'sources_unchanged': before == after,
             'source_sha256': after, 'log': str(log.relative_to(ROOT)),
             'log_sha256': digest(log),
             'scope': 'Executed command only; no external proof review or analytic formalization inferred.'}
    (dst / (label + '_execution.json')).write_text(json.dumps(entry, indent=2) + '\n')
    print(label, 'returncode', result.returncode, 'seconds', entry['elapsed_seconds'],
          'sources unchanged', entry['sources_unchanged'])
    raise SystemExit(result.returncode)

if __name__ == '__main__':
    main()
