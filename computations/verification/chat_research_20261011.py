#!/usr/bin/env python3
"""Bounded exact controls for the scoped 11 October research checkpoint.

Runs Fraction Jack coefficients, independent integer C++ SSYT, Pfaffian
densities and critical cumulant words. Finite coverage is not an asymptotic
proof. New logs/results go under build, never into old evidence records.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
from fractions import Fraction as F

ROOT=Path(__file__).resolve().parents[2]
SCRIPTS=ROOT/'computations/verification/chat_20261011/scripts'

def limits():
    resource.setrlimit(resource.RLIMIT_CPU,(50,50))
    resource.setrlimit(resource.RLIMIT_AS,(1073741824,1073741824))

def interval_laplace(N,a,w):
    # Exact integration over a full unfolded circle; h=1-exp(-f)=1/2
    # on a window of width w. This is a finite discontinuous-test control.
    points=[F(j)-(a if j%2 else 0) for j in range(N)]
    cuts={F(0),F(N)}
    for x in points:
        for shift in (-N,0,N):
            for endpoint in (x+shift-w/2,x+shift+w/2):
                if 0<endpoint<N:cuts.add(endpoint)
    cuts=sorted(cuts);total=F(0)
    for lo,hi in zip(cuts,cuts[1:]):
        t=(lo+hi)/2
        count=sum(abs(t-x-shift)<w/2 for x in points for shift in (-N,0,N))
        total+=(hi-lo)*F(1,2)**count
    return total/N

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path,default=ROOT/'build/chat-research-20261011')
    ap.add_argument('--cpp',type=Path)
    args=ap.parse_args();out=args.output.resolve();out.mkdir(parents=True,exist_ok=True)
    env=dict(os.environ,PYTHONOPTIMIZE='0',OMP_NUM_THREADS='1',OPENBLAS_NUM_THREADS='1',MKL_NUM_THREADS='1')
    commands=[]
    def run(name,cmd):
        p=subprocess.run(list(map(str,cmd)),cwd=ROOT,env=env,text=True,capture_output=True,timeout=60,preexec_fn=limits)
        log=out/(name+'.log');log.write_text(p.stdout+p.stderr)
        assert len(log.read_bytes())<=1048576,(name,'output cap exceeded')
        commands.append({'name':name,'argv':list(map(str,cmd)),'returncode':p.returncode,'log_sha256':hashlib.sha256(log.read_bytes()).hexdigest()})
        p.check_returncode();return p.stdout
    cpp=args.cpp.resolve() if args.cpp else out/'circular_phase_ssyt_verifier'
    if not args.cpp:run('compile',['g++','-O2','-std=c++17','-Wall','-Wextra','-Wpedantic',ROOT/'computations/cpp/circular_phase_ssyt_verifier.cpp','-o',cpp])
    cpp_result=json.loads(run('cpp',[cpp]));assert cpp_result['all_passed']
    (out/'cpp_results.json').write_text(json.dumps(cpp_result,indent=2)+'\n')
    run('jack',[sys.executable,SCRIPTS/'exact_checks.py',out/'cpp_results.json',out/'jack_results.json'])
    run('pfaffian',[sys.executable,SCRIPTS/'pfaffian_controls.py',out/'pfaffian_results.json'])
    run('cumulant',[sys.executable,SCRIPTS/'cumulant_formula_controls.py',out/'cumulant_results.json'])
    interval_cases=[]
    for N in range(2,42,2):
        for a in (F(1,2),F(3,5),F(2,3),F(3,4)):
            w=1-a/3
            clock=interval_laplace(N,F(0),w);shifted=interval_laplace(N,a,w)
            assert clock==1-w/2
            assert shifted-clock==(w-(1-a))/8>0
            interval_cases.append({'N':N,'a':str(a),'w':str(w),'difference':str(shifted-clock)})
    assert interval_laplace(10,F(0),F(4,5))==F(3,5)
    assert interval_laplace(10,F(3,5),F(4,5))==F(13,20)
    walsh_cases=[]
    for d in range(1,8):
        N=2**d
        A=[[(-1)**((i&j).bit_count()) for j in range(N)] for i in range(N)]
        assert sum(A[i][i] for i in range(N))==0
        assert all(sum(A[i][k]*A[j][k] for k in range(N))==(N if i==j else 0)
                   for i in range(N) for j in range(N))
        residues=[sum(A[i][j]**2 for i in range(N) for j in range(N)
                      if (j-i)%N==a) for a in range(N)]
        assert residues==[N]*N
        walsh_cases.append({'N':N,'cleared_orthogonality':True,'zero_trace':True,
                            'equal_cyclic_difference_weights':True})
    results={name:json.loads((out/(name+'_results.json')).read_text()) for name in ('jack','pfaffian','cumulant')}
    assert all(x['all_passed'] for x in results.values())
    summary={'all_passed':True,'arithmetic':'Exact rational and independent C++ integer SSYT','controls':{k:{f:v for f,v in x.items() if f not in ('records','dimension_controls','non_claims')} for k,x in results.items()},'alternating_clock_cases':len(interval_cases),'walsh_clock_controls':walsh_cases,'resource_caps_per_child':{'wall_seconds':60,'cpu_seconds':50,'address_space_bytes':1073741824,'output_bytes':1048576,'threads':1},'commands':commands,'non_claims':['Finite controls do not prove the unbounded-signature, all-order or asymptotic theorems.','Indicator-window clock control is a mechanism diagnostic; the smooth-test statement is proved analytically.','The changed-clock family is not the maintained literal BGS map.','This script does not compile Lean or run Wolfram.']}
    (out/'interval_results.json').write_text(json.dumps(interval_cases,indent=2)+'\n')
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k not in ('commands','non_claims')}))
    return 0

if __name__=='__main__':raise SystemExit(main())
