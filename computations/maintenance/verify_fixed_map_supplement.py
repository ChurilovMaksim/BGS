#!/usr/bin/env python3
"""Audit and replay recovered research in isolation, preserving source evidence."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT/'supplement/fixed_map'
CHECKS = [
    ('algebraic-return/simple_spectrum.py', ['--replay']),
    ('algebraic-return/verify_cpp.py', []),
    ('algebraic-return/quantitative_bounds.py', []),
    ('ergodic-transfer/finite_checks.py', []),
    ('coherent-return/gap_identity.py', []),
    ('coherent-return/return_memory.py', []),
    ('design-return/all_dimensions.py', []),
    ('design-return/design_return.py', []),
    ('design-return/finite_symbol_normal_form.py', []),
    ('design-return/fixed_kick_bandwidth.py', []),
    ('design-return/frozen_crossover.py', []),
    ('design-return/frozen_matrix_check.py', []),
    ('design-return/frozen_sharp_return.py', []),
    ('design-return/sparse_orbit_checks.py', []),
    ('block-memory/verify.py', []),
    ('report-audit-20260919/verify.py', []),
    ('report-audit-20260919/cubic_variance.py', []),
    ('report-audit-20260919/independent_variance_review.py', []),
    ('report-audit-20260919/folded_spectrum_control.py', []),
    ('secular-route/exact_structure_checks.py', []),
    ('weighted-secular/determinant_control.py', []),
    ('weighted-secular/weighted_probe.py', ['--dimensions', '15', '19', '23']),
    ('weighted-secular/center_checks.py', []),
    ('weighted-secular/jacobi_audit.py', []),
    ('resolvent-flow/checks.py', []),
    ('resolvent-flow/low_order.py', []),
    ('fixed-map-audit/classical.py', []),
    ('fixed-map-audit/conventions.py', []),
]


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, default=ROOT/'build/fixed-map-replay')
    parser.add_argument('--only', action='append', default=[])
    parser.add_argument('--audit-only', action='store_true')
    parser.add_argument('--workers', type=int, default=2)
    args = parser.parse_args()
    out = args.output_dir.resolve()
    if out == SOURCE or out.is_relative_to(SOURCE) or SOURCE.is_relative_to(out):
        raise SystemExit('Output must be disjoint from the maintained supplement.')
    out.mkdir(parents=True, exist_ok=True)
    inventory = json.loads((SOURCE/'inventory.json').read_text())
    for row in inventory['files']:
        assert sha(SOURCE/row['path']) == row['sha256'], row['path']
        if row['path'].endswith('.py'):
            compile((SOURCE/row['path']).read_bytes(), row['path'], 'exec')
    selected = [(p,a) for p,a in CHECKS if not args.only or p in args.only]
    unknown = set(args.only)-{p for p,_ in CHECKS}
    if unknown:
        raise SystemExit('Unknown check: '+str(sorted(unknown)))
    record = {'status':'RUNNING', 'inventory_files':len(inventory['files']),
              'scope':'Source integrity, Python syntax and selected finite replays; not a proof of asymptotic claims.',
              'checks':[], 'source_manifest_sha256':sha(SOURCE/'inventory.json'),
              'not_rerun':['Wolfram scripts', 'echo Monte Carlo exploration',
                           'redesigned-symbol monodromy experiment'],
              'python':sys.version.split()[0]}
    # Each task gets a private copy: certificate producers and diagnostic
    # writers cannot race or overwrite retained evidence or other replays.
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MPLBACKEND='Agg', PYTHONDONTWRITEBYTECODE='1')
    inherited = [str(Path(p).resolve()) for p in env.get('PYTHONPATH','').split(os.pathsep) if p]
    env['PYTHONPATH'] = os.pathsep.join([str(ROOT/'computations/verification'), *inherited])
    def execute(item):
        path, arguments = item
        work = out/'runs'/path.replace('/','__').removesuffix('.py')
        copied = work/'build'
        shutil.copytree(SOURCE, copied, dirs_exist_ok=True)
        command = [sys.executable, str(copied/path), *arguments]
        log = work/'execution.log'
        start = time.monotonic()
        try:
            with log.open('w') as stream:
                done = subprocess.run(command, cwd=work, env=env, stdout=stream,
                                      stderr=subprocess.STDOUT, timeout=600)
            status, code = ('PASS' if done.returncode == 0 else 'FAIL'), done.returncode
        except subprocess.TimeoutExpired:
            status, code = 'TIMEOUT', None
        result = {'script':path, 'arguments':arguments, 'status':status,
                  'exit_code':code, 'seconds':round(time.monotonic()-start,3),
                  'source_sha256':sha(SOURCE/path), 'log':str(log.relative_to(out)),
                  'log_sha256':sha(log)}
        print(json.dumps(result), flush=True)
        return result
    if not args.audit_only:
        with ThreadPoolExecutor(max_workers=args.workers) as pool:
            for result in pool.map(execute, selected):
                record['checks'].append(result)
                (out/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
    for row in inventory['files']:
        assert sha(SOURCE/row['path']) == row['sha256'], 'Source changed during replay'
    record['status'] = 'PASS' if all(r['status']=='PASS' for r in record['checks']) else 'FAIL'
    record['audit_only'] = args.audit_only
    (out/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'status':record['status'],'executed':len(record['checks'])}))
    if record['status'] != 'PASS':
        raise SystemExit(1)


if __name__ == '__main__':
    main()
