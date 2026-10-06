#!/usr/bin/env python3
"""Finite W/Q/EQ and combined-interface controls; no analytic formalization.

W: exact symbolic twisted Hill identities m=1, forty rational cycles m2..9,
and rational contraction margins. Q: exact Wick/covariance/alias controls
m1..12 and Weyl parity grades<=8. EQ: exact 32-mode symbol and derivative
budget only. No sampling establishes equidistribution, bundle regularity,
quantum asymptotics or full signed BGS. Inputs are fixed source expressions.
"""
from pathlib import Path
import argparse
import importlib.util
import json
import resource


def run(mode):
    p = Path(__file__).resolve().parent/'weighted_support'/f'{mode}.py'
    spec = importlib.util.spec_from_file_location('weighted_check',p)
    module = importlib.util.module_from_spec(spec)
    exec(compile(p.read_bytes(),str(p),'exec'),module.__dict__)
    return {'mode':mode,'result':module.run()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode',choices=['physical','quantum','equidistribution','combined','stationary'])
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU,(180,180))
    print(json.dumps([run(m) for m in ([args.mode] if args.mode else ['physical','quantum','equidistribution','combined','stationary'])],indent=2))


if __name__ == '__main__':
    main()
