#!/usr/bin/env python3
"""Run the locality dependency suite with an atomic per-command checkpoint.

This is a targeted suite, not all historical symbolic verifiers. Existing
successful rows are resumed only when every scientific source fingerprint
and the individual log hash match. Missing or interrupted rows remain pending.
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
import threading
import time

ROOT=Path(__file__).resolve().parents[2]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--build',type=Path,required=True)
    p.add_argument('--logs',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--resume',action='store_true')
    p.add_argument('--limit',type=int)
    args=p.parse_args()
    if args.limit is not None and args.limit<1: p.error('--limit must be positive')
    args.logs.mkdir(parents=True,exist_ok=True);args.output.parent.mkdir(parents=True,exist_ok=True)
    sources={str(q.relative_to(ROOT)):sha(q) for folder in ('computations','formalization','mathematics')
             for q in (ROOT/folder).rglob('*') if q.is_file() and q.suffix in ('.py','.cpp','.lean','.md')
             and '__pycache__' not in q.parts and '.lake' not in q.parts}
    sources['CMakeLists.txt']=sha(ROOT/'CMakeLists.txt')
    sources['requirements.txt']=sha(ROOT/'requirements.txt')
    fingerprint=hashlib.sha256(json.dumps(sources,sort_keys=True).encode()).hexdigest()
    plan=[]
    for name in ('fixed_strength_locality','fixed_strength_classical','locality_robustness',
                 'pell_floquet_regression','pell_weighted_echo_regression','spectral_lattice_clustering',
                 'repository_audit'):
        path=ROOT/'computations/verification'/f'{name}.py'
        cmd=[sys.executable,str(path)]
        if name in ('fixed_strength_locality','fixed_strength_classical','locality_robustness'):
            cmd+=['--output',str(ROOT/'evidence/certificates'/f'{name}.json')]
        if name=='fixed_strength_locality': cmd+=['--extended']
        if name=='pell_floquet_regression':
            cmd+=['--cpp',str(args.build.resolve()/'pell_pair_orthogonality')]
        plan.append((name,cmd,path))
    path=ROOT/'computations/analysis/spectral_diagnostics.py'
    plan.append(('spectral_diagnostics',[sys.executable,str(path),'verify'],path))
    for path in sorted((ROOT/'computations/cpp').glob('*.cpp')):
        cmd=[str(args.build.resolve()/path.stem)]
        if path.stem=='cat_map_order': cmd+=['verify']
        plan.append(('cpp_'+path.stem,cmd,path))
    rows={}
    if args.resume and args.output.exists():
        old=json.loads(args.output.read_text())
        if old.get('source_fingerprint')!=fingerprint:
            raise SystemExit('Source fingerprint changed: refusing to reuse old checks.')
        for r in old['checks']:
            log=args.logs/(r['name']+'.log')
            if r['exit_code']==0 and log.exists() and sha(log)==r['log_sha256']:
                rows[r['name']]=r
    lock=threading.Lock()
    def checkpoint():
        current=[rows[n] for n,_,_ in plan if n in rows]
        remaining=[n for n,_,_ in plan if n not in rows]
        status=('PASS' if len(current)==len(plan) and all(r['exit_code']==0 for r in current)
                else 'INCOMPLETE' if remaining else 'FAIL')
        data={'producer':'computations/maintenance/verify_locality_packet.py','status':status,
              'scope':'Targeted locality/echo/clustering dependencies, structural audit, spectral diagnostics, and all C++ binaries in this worktree. Not all historical symbolic Python verifiers; Lean and TeX are separate.',
              'input_commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
              'python':platform.python_version(),'source_fingerprint':fingerprint,'source_sha256':sources,
              'checks':current,'pending':remaining,'passed':sum(r['exit_code']==0 for r in current),
              'total':len(plan)}
        temp=args.output.with_suffix(args.output.suffix+'.tmp')
        temp.write_text(json.dumps(data,indent=2)+'\n');os.replace(temp,args.output)
    checkpoint()
    remaining=[entry for entry in plan if entry[0] not in rows]
    if args.limit is not None: remaining=remaining[:args.limit]
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',MPLBACKEND='Agg')
    def run(entry):
        name,cmd,source=entry;log=args.logs/(name+'.log');start=time.monotonic()
        with log.open('w') as output:
            try:
                code=subprocess.run(cmd,cwd=ROOT,env=env,stdout=output,stderr=subprocess.STDOUT,timeout=180).returncode
            except subprocess.TimeoutExpired:
                code=124
            except OSError as exc:
                output.write(str(exc)+'\n');code=127
        with lock:
            rows[name]={'name':name,'source':str(source.relative_to(ROOT)),'source_sha256':sha(source),
                        'command':cmd,'exit_code':code,'seconds':round(time.monotonic()-start,3),
                        'log_sha256':sha(log)}
            checkpoint()
        print(name,code,flush=True)
    with ThreadPoolExecutor(max_workers=2) as pool:
        list(pool.map(run,remaining))
    current_sources={str(q.relative_to(ROOT)):sha(q) for folder in ('computations','formalization','mathematics')
                     for q in (ROOT/folder).rglob('*') if q.is_file() and q.suffix in ('.py','.cpp','.lean','.md')
                     and '__pycache__' not in q.parts and '.lake' not in q.parts}
    for name in ('CMakeLists.txt','requirements.txt'):
        if (ROOT/name).is_file(): current_sources[name]=sha(ROOT/name)
    changed=sorted(name for name in set(sources)|set(current_sources)
                   if sources.get(name)!=current_sources.get(name))
    if changed:
        data=json.loads(args.output.read_text())
        data['status']='INVALIDATED'
        data['changed_sources']=changed
        temp=args.output.with_suffix(args.output.suffix+'.tmp')
        temp.write_text(json.dumps(data,indent=2)+'\n');os.replace(temp,args.output)
        raise SystemExit('Sources changed during checks: '+str(changed))
    if len(rows)!=len(plan): raise SystemExit(2)
    if any(r['exit_code'] for r in rows.values()): raise SystemExit(1)

if __name__=='__main__': main()
