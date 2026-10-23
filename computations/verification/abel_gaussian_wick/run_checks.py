#!/usr/bin/env python3
"""Run bounded finite controls; do not equate them with theorem proofs.

Each child runs in its own temporary directory with python -O. The checked
programs raise explicit exceptions on failure. JSON output and source hashes
are preserved. No physical fixed-coupling asymptotic, Lean or PDF build runs.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
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
TASKS = (
    ('abel', 'verify_abel.py', 180),
    ('rigidity', 'verify_rigidity.py', 180),
    ('factorial', 'verify_gaussian_factorial.py', 180),
    ('hessian', 'verify_gaussian_hessian.py', 240),
    ('generic_tensors', 'verify_generic_tensors.py', 180),
    ('symbolic_mean', 'derive_collision_mean.py', 60),
)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(task, output):
    name, filename, cap = task
    source = HERE / filename
    dependencies = ['verify_abel.py'] if name == 'rigidity' else []
    began = time.monotonic()
    command = [sys.executable, '-O', filename]
    with tempfile.TemporaryDirectory(prefix='bgs-research-check-') as temp:
        work = Path(temp)
        shutil.copy2(source, work / filename)
        for dependency in dependencies:
            shutil.copy2(HERE / dependency, work / dependency)
        env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
                   MKL_NUM_THREADS='1', PYTHONHASHSEED='0')
        try:
            result = subprocess.run(command, cwd=work, env=env,
                                    stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                    timeout=cap)
            stdout, stderr, rc = result.stdout, result.stderr, result.returncode
            status = 'PASS' if rc == 0 else 'FAIL'
        except subprocess.TimeoutExpired as exc:
            stdout, stderr, rc = exc.stdout or b'', exc.stderr or b'', None
            status = 'TIMEOUT'
        if status == 'PASS':
            try:
                payload = json.loads(stdout)
                if payload.get('status', 'PASS') != 'PASS':
                    status = 'FAIL'
            except (ValueError, AttributeError):
                status = 'INVALID-OUTPUT'
        dest = output / name
        dest.mkdir(parents=True, exist_ok=True)
        (dest / 'result.json').write_bytes(stdout)
        (dest / 'stderr.log').write_bytes(stderr)
    row = dict(name=name, status=status, returncode=rc, command=command,
               timeout_seconds=cap, elapsed_seconds=round(time.monotonic()-began, 4),
               source=filename, source_sha256=sha(source),
               dependencies_sha256={p: sha(HERE / p) for p in dependencies},
               result_sha256=sha(dest / 'result.json'),
               stderr_sha256=sha(dest / 'stderr.log'))
    print(name, status, flush=True)
    return row


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    with ThreadPoolExecutor(max_workers=4) as pool:
        rows = list(pool.map(lambda task: run(task, args.output), TASKS))
    receipt = dict(schema='bgs-abel-gaussian-checks-v1', date='2026-10-16',
                   base_commit='b425a36141cd81c7ef4e832984e7f7ff5074ddc7',
                   python=sys.version, platform=platform.platform(),
                   scope='Six bounded finite arithmetic/numerical/symbolic controls; no universal theorem certificate, physical asymptotic, PDF or Lean build.',
                   tasks=rows, all_passed=all(r['status']=='PASS' for r in rows))
    (args.output / 'receipt.json').write_text(json.dumps(receipt, indent=2)+'\n')
    return 0 if receipt['all_passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
