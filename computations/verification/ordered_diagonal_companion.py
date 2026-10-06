#!/usr/bin/env python3
"""Independent exact bounded controls for the ordered-diagonal companion.

Eight rational full-End cases; full ordered N3,m4 Gram; two Q(i) cases;
noncommuting cyclic products and exact N2 moment/failure controls.
No finite experiment proves the asymptotic N estimate. No source writes.
"""
from pathlib import Path
import importlib.util
import contextlib
import io
import json
import resource


def load(name):
    p=Path(__file__).resolve().parent/'ordered_diagonal'/f'{name}.py'
    spec=importlib.util.spec_from_file_location('ordered_'+name,p)
    module=importlib.util.module_from_spec(spec)
    exec(compile(p.read_bytes(),str(p),'exec'),module.__dict__)
    return module


def run():
    with contextlib.redirect_stdout(io.StringIO()):
        return load('bounded').run(load('exact'))


def main():
    resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3))
    resource.setrlimit(resource.RLIMIT_CPU,(180,180))
    print(json.dumps(run(),indent=2))


if __name__=='__main__':main()
