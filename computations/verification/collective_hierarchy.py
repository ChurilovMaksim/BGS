#!/usr/bin/env python3
"""Exact collective hierarchy controls, with separately selected diagnostics.

Default: ordered-word Haar/Gram construction at 11 (N,m) pairs, actual
rational-Householder trace identity at 7 pairs, and 36 exact Kostka rows.
NumPy ordered-word Gram products are bounded int64: at most (5!)^2*4^5
in this finite range, safely below 2^63. Printed float approximations in
Kostka rows are display only. --diagnostics additionally replays explicitly
floating quadratic/slow-source controls; these do not certify asymptotics.
No source writes. All actual-family analytic inputs retain their review scope.
"""
import os
for _key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:
    os.environ[_key] = '1'
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io
import json
import resource


def load(name):
    p = Path(__file__).resolve().parent/'collective'/f'{name}.py'
    spec = importlib.util.spec_from_file_location('collective_'+name,p)
    module = importlib.util.module_from_spec(spec)
    if name == 'trace':
        ordered = load('ordered')
        for symbol in ['parts','compositions','cycle_type','insertion']:
            module.__dict__[symbol] = getattr(ordered,symbol)
    exec(compile(p.read_bytes(),str(p),'exec'),module.__dict__)
    return module


def run(diagnostics=False):
    names = ['ordered','trace','kostka']
    if diagnostics:
        names += ['quadratic_diagnostic','slow_diagnostic']
    results = {}
    with contextlib.redirect_stderr(io.StringIO()):
        for name in names:
            results[name] = load(name).run_all()
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--diagnostics',action='store_true')
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU,(180,180))
    print(json.dumps(run(args.diagnostics),indent=2))


if __name__ == '__main__':
    main()
