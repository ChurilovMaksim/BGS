#!/usr/bin/env python3
"""Execute maintained Python/C++ verifiers with source and log hashes.

This is execution coverage, not a line-by-line mathematical proof audit.
"""
from __future__ import annotations
import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import os
from pathlib import Path
import platform
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[2]

def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build',type=Path,required=True)
    parser.add_argument('--logs',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--workers',type=int,default=2)
    args=parser.parse_args()
    args.logs.mkdir(parents=True,exist_ok=True)
    items=[]
    for p in sorted((ROOT/'computations/verification').glob('*.py')):
        if '__main__' in p.read_text():
            cmd=[sys.executable,str(p)]
            if p.stem=='pell_floquet_regression':
                cmd+=['--cpp',str(args.build.resolve()/'pell_pair_orthogonality')]
            items.append((p.stem,cmd,p))
    p=ROOT/'computations/analysis/spectral_diagnostics.py'
    items.append(('spectral_diagnostics_verify',[sys.executable,str(p),'verify'],p))
    for p in sorted((ROOT/'computations/cpp').glob('*.cpp')):
        cmd=[str(args.build.resolve()/p.stem)]
        if p.stem=='cat_map_order':cmd+=['verify']
        items.append(('cpp_'+p.stem,cmd,p))
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MPLBACKEND='Agg')
    def check(item):
        name,cmd,source=item;start=time.monotonic()
        with (args.logs/(name+'.log')).open('w') as stream:
            try:
                code=subprocess.run(cmd,cwd=ROOT,env=env,stdout=stream,stderr=subprocess.STDOUT,timeout=360).returncode
            except subprocess.TimeoutExpired:code=124
        row={'name':name,'source':str(source.relative_to(ROOT)),
             'sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
             'command':cmd,'exit_code':code,'seconds':round(time.monotonic()-start,3),
             'log_sha256':hashlib.sha256((args.logs/(name+'.log')).read_bytes()).hexdigest()}
        print(name,code,flush=True)
        if code:print((args.logs/(name+'.log')).read_text()[-4000:],flush=True)
        return row
    with ThreadPoolExecutor(max_workers=args.workers) as pool:rows=list(pool.map(check,items))
    data={'producer':'computations/maintenance/verify_workspace.py',
          'scope':'Execution of every maintained executable Python and C++ verifier on this worktree; not a complete proof audit. Lean and TeX are separate build steps.',
          'input_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
          'python':platform.python_version(),'checks':rows,
          'passed':sum(r['exit_code']==0 for r in rows),'total':len(rows)}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2)+'\n')
    if data['passed']!=data['total']:raise SystemExit('Verification failed; inspect saved logs.')

if __name__=='__main__':
    main()
