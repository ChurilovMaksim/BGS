#!/usr/bin/env python3
"""Finite exact controls; universal proofs are in weighted_wiener_resonance.md."""
from __future__ import annotations
import argparse
from collections import Counter
from fractions import Fraction as F
import json
from pathlib import Path

def mv(A,v):return (A[0]*v[0]+A[1]*v[1],A[2]*v[0]+A[3]*v[1])
def add(u,v):return (u[0]+v[0],u[1]+v[1])
def neg(u):return (-u[0],-u[1])
def det(u,v):return u[0]*v[1]-u[1]*v[0]
def q(A,v):return det(v,mv(A,v))
def mul(f,g):
    h=Counter()
    for v,a in f.items():
        for w,b in g.items():h[add(v,w)]+=a*b
    return {v:a for v,a in h.items() if a}
def C(A,f):return {mv(A,v):a for v,a in f.items()}
def linear(f,g,alpha=F(1),beta=F(1)):
    h=Counter({v:alpha*a for v,a in f.items()})
    for v,a in g.items():h[v]+=beta*a
    return {v:a for v,a in h.items() if a}
def cube(f):return mul(mul(f,f),f).get((0,0),0)
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);args=ap.parse_args()
    matrices=[(2,1,1,1),(3,2,4,3),(4,1,3,1),(-2,-1,-1,-1)]
    vectors=[(a,b) for a in range(-3,4) for b in range(-3,4) if a or b]
    cases=0
    for A in matrices:
        assert A[0]*A[3]-A[1]*A[2]==1 and abs(A[0]+A[3])>2
        for u in vectors:
            for v in vectors:
                w=v;values=Counter()
                for r in range(1,65):
                    w=mv(A,w);k=add(u,w)
                    if k!=(0,0):values[q(A,k)]+=1
                assert max(values.values(),default=0)<=2
                cases+=1
    A=(2,1,1,1);v=(1,0);w=mv(A,v);z=add(v,w)
    seed={v:F(1),neg(v):F(1),w:F(2),neg(w):F(2),z:F(1),neg(z):F(1)}
    cg=C(A,seed);f=linear(seed,cg,beta=-F(1,2));h=linear(cg,seed,beta=-F(1,2))
    data=[cube(seed),mul(mul(seed,seed),cg).get((0,0),0),mul(seed,mul(cg,cg)).get((0,0),0),cube(f),cube(h)]
    assert data==[24,4,16,27,0]
    q0=F(1,2);zz=F(-1);w1=F(4);w2=F(36)
    cross_p=-q0*(w1*(zz+q0*q0)+w2*(1+q0*q0*zz))
    cross_q=-q0*(w1*(1+q0*q0*zz)+w2*(zz+q0*q0))
    assert (cross_p,cross_q)==(-12,12)
    out={'scope':'finite exact controls, not the universal proof','two_visit_pair_cases':cases,'times_per_pair':64,
         'classical_cubic_moments':[int(x) for x in data],
         'bracket_cross_spectrum_at_pi_divided_by_pi_squared':[int(cross_p),int(cross_q)]}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
