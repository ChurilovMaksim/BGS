#!/usr/bin/env python3
"""Successful exact factorial/mixed-sector controls only.

General:107 networks,5 full-End Grams,11928 proper zero-block strata,
1154 all-zero ranks and exact Haar covariance. Mixed:7 N2 physical cases,
4 literal port cases with verified nonnormal fixtures and shared Haar moments.
Two historical full-suite timeouts are preserved, never rerun as successful
checks. No floating author replay is recast as exact; no finite check proves
actual-map flatness, the universal theorem or the signed residual estimate.
"""
from pathlib import Path
import argparse
import contextlib
import importlib.util
import io
import json
import os
import resource
import time


def load(name):
    p=Path(__file__).resolve().parent/'factorial_diagonal'/f'{name}.py'
    spec=importlib.util.spec_from_file_location('factorial_'+name,p)
    module=importlib.util.module_from_spec(spec)
    exec(compile(p.read_bytes(),str(p),'exec'),module.__dict__)
    return module


def run():
    with contextlib.redirect_stdout(io.StringIO()):
        general=load('general').run()
        m=load('mixed')
        small={'physical':[m.physical(2,[1,1],[2],True),m.physical(2,[1,2],[3],True),m.physical(2,[1,1]),m.physical(2,[1,2])]}
        ports={'ports':[m.ports(3,2,2),m.ports(3,2,3),m.ports(3,2,2,True),m.ports(4,2,2)],'shared_Haar_controls':m.shared_moments()}
        n2={'physical':[m.physical(2,[2,2],[4],True),m.physical(2,[2,2]),m.physical(2,[1,1,2])]}
    return {'general':general,'small':small,'ports':ports,'n2_m4':n2}


def main():
    for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS']:os.environ[key]='1'
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU,(280,280))
    print(json.dumps(run(),indent=2))


if __name__=='__main__':main()
