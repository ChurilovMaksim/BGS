#!/usr/bin/env python3
"""Exact finite controls for balanced_phase_controllability.md.

This verifies the sufficient edge-gap criterion, not a numerical Lie rank.
The universal theorem is the trigonometric proof in the mathematics note.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from math import gcd
import json
from pathlib import Path
import sympy as sp

def add(*vs):return tuple(sum(t) for t in zip(*vs))
def minus(a,b):return tuple(x-y for x,y in zip(a,b))

def check_dimension(N:int)->dict:
    if N<3 or N%2==0:raise ValueError('N must be odd and at least three')
    x=sp.Symbol('x');phi=sp.Poly(sp.cyclotomic_poly(4*N,x),x)
    mod=[int(c) for c in reversed(phi.all_coeffs())];d=len(mod)-1
    def reduce(a):
        a=list(a)+[0]*max(0,d-len(a))
        for k in range(len(a)-1,d-1,-1):
            c=a[k]
            if c:
                for j in range(d):a[k-d+j]-=c*mod[j]
            a[k]=0
        return tuple(a[:d])
    mon=[]
    for k in range(4*N):mon.append(reduce([0]*k+[1]))
    def M(k):return mon[k%(4*N)]
    def square(a):
        c=[0]*(2*d-1)
        for i,u in enumerate(a):
            if u:
                for j,v in enumerate(a):
                    if v:c[i+j]+=u*v
        return reduce(c)
    energies=[minus(add(M(4*j),M(N+4*j),M(-4*j)),M(N-4*j)) for j in range(N)]
    assert len(set(energies))==N
    unbalanced=[add(M(4*j),M(-4*j)) for j in range(N)]
    assert len(set(unbalanced))<N
    units=[k for k in range(1,N) if gcd(k,N)==1]
    for step in units:
        gaps=[minus(energies[(j+step)%N],energies[j]) for j in range(N)]
        assert all(any(g) for g in gaps)
        assert len({square(g) for g in gaps})==N
        assert len({j*step%N for j in range(N)})==N
    return {'N':N,'cyclotomic_degree':d,'unit_steps':len(units),
            'exact_nonzero_gaps_checked':N*len(units),
            'distinct_squared_gaps_for_every_step':True,
            'pure_cosine_negative_control':True}

def main()->None:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dimensions',type=int,nargs='+',default=[3,5,7,9,11,15,21,25])
    ap.add_argument('--output',type=Path)
    args=ap.parse_args();rows=[check_dimension(N) for N in args.dimensions]
    out={'scope':'finite exact edge-gap criteria, not the all-N proof or a computed Lie rank',
         'arithmetic':'Z[x]/Phi_(4N)(x)', 'cases':rows,
         'total_unit_steps':sum(r['unit_steps'] for r in rows),
         'total_gaps':sum(r['exact_nonzero_gaps_checked'] for r in rows)}
    text=json.dumps(out,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text)
    print(text,end='')
if __name__=='__main__':main()
