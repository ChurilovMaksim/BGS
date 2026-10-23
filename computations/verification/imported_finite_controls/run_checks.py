#!/usr/bin/env python3
"""Replay the imported finite controls in isolated temporary directories.

Requires numpy, scipy, sympy and mpmath from the repository requirements.
No test computes the literal frozen asymptotic limit. Scripts and outputs
are pinned separately; source presence is not execution evidence.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time

HERE = Path(__file__).resolve().parent

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--only', help='Comma-separated task names')
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    tasks = json.loads((HERE / 'tasks.json').read_text())
    if args.only:
        selected = set(args.only.split(','))
        unknown = selected - {t['name'] for t in tasks}
        if unknown:
            parser.error('Unknown tasks: ' + ', '.join(sorted(unknown)))
        tasks = [t for t in tasks if t['name'] in selected]
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', PYTHONHASHSEED='0')
    rows = []
    for task in tasks:
        name = task['name']
        src = HERE / task['script']
        began = time.monotonic()
        with tempfile.TemporaryDirectory(prefix='bgs-chat-check-') as tmp:
            work = Path(tmp)
            # Each checker writes beside itself; only its small dependency
            # directory is copied. No maintained source/evidence is modified.
            for dep in src.parent.glob('*.py'):
                if dep.name != 'run_checks.py':
                    shutil.copy2(dep, work / dep.name)
            cmd = [sys.executable, '-O', src.name, *task['args']]
            print('START', name, flush=True)
            try:
                result = subprocess.run(cmd, cwd=work, env=env,
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.STDOUT,
                                        timeout=task['timeout_seconds'])
                output, rc = result.stdout, result.returncode
                status = 'PASS' if rc == 0 else 'FAIL'
            except subprocess.TimeoutExpired as exc:
                output, rc, status = exc.stdout or b'', None, 'TIMEOUT'
            dest = args.output / name
            dest.mkdir(exist_ok=True)
            (dest / 'run.log').write_bytes(output)
            artifacts = {}
            for artifact in work.glob('*.json'):
                shutil.copy2(artifact, dest / artifact.name)
                artifacts[artifact.name] = hashlib.sha256(artifact.read_bytes()).hexdigest()
            row = dict(name=name, status=status, returncode=rc,
                       elapsed_seconds=round(time.monotonic()-began, 4),
                       command=cmd, source=src.relative_to(HERE).as_posix(),
                       source_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
                       outputs_sha256=artifacts)
            rows.append(row)
            print('END', name, status, flush=True)
    report = dict(schema='bgs-chat-replay-v1', date='2026-10-16',
                  python=sys.version, platform=platform.platform(),
                  review='Author self-review and finite execution; no independent referee certificate.',
                  scope='Imported finite checks only. Proxy couplings are not literal frozen BGS asymptotics.',
                  tasks=rows, all_passed=all(r['status']=='PASS' for r in rows))
    (args.output / 'receipt.json').write_text(json.dumps(report, indent=2)+'\n')
    return 0 if report['all_passed'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
