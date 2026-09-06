#!/usr/bin/env python3
"""Exact finite checks of two-radius rigidity and quadrature covariance.

Complex arithmetic is represented by pairs of Fractions. Orbit equivalence
uses descent of the exact Euclidean norm, not a finite iterate window.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import json
from pathlib import Path
from multiradius_rigidity import exhaustive_two_component

ZERO = (F(0), F(0))

def plus(a,b):return (a[0]+b[0],a[1]+b[1])
def times(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def scale(c,a):return (c*a[0],c*a[1])
def conjugate(a):return (a[0],-a[1])
def mv(A,v):return (A[0]*v[0]+A[1]*v[1],A[2]*v[0]+A[3]*v[1])
def det(u,v):return u[0]*v[1]-u[1]*v[0]
def power_vector(A,v,n):
    for _ in range(n):v=mv(A,v)
    return v

def representative(A,v):
    inverse=(A[3],-A[1],-A[2],A[0])
    def key(w):return (w[0]*w[0]+w[1]*w[1],w)
    while True:
        best=min((v,mv(A,v),mv(inverse,v)),key=key)
        if best==v:return v
        v=best

def orbit_bracket(A,g,r):
    shifted={power_vector(A,v,r):c for v,c in g.items()}
    coefficients={}
    for u,a in g.items():
        for v,b in shifted.items():
            w=(u[0]+v[0],u[1]+v[1])
            coefficient=scale(-det(u,v),times(a,b))
            if w!=(0,0) and coefficient!=ZERO:
                orbit=representative(A,w)
                coefficients[orbit]=plus(coefficients.get(orbit,ZERO),coefficient)
    return {v:c for v,c in coefficients.items() if c!=ZERO}

def inner(f,g):
    out=ZERO
    for v,c in f.items():out=plus(out,times(conjugate(c),g.get(v,ZERO)))
    return out

def gram_controls():
    matrices=[(2,1,1,1),(3,2,4,3),(-2,-1,-1,-1)]
    v=(1,0);cases=0;entries=0
    for A in matrices:
        for d in (1,2,3):
            w=power_vector(A,v,d)
            for a,b in ((1,1),(2,1),(1,3)):
                for phase in ((F(1),F(0)),(F(3,5),F(4,5))):
                    c0=scale(a,phase);cd=times((F(0),F(b)),phase)
                    g={v:c0,(-v[0],-v[1]):conjugate(c0),
                       w:cd,(-w[0],-w[1]):conjugate(cd)}
                    lags=list(range(d+1,d+6))
                    columns=[orbit_bracket(A,g,r) for r in lags]
                    def D(k):return det(v,power_vector(A,v,k))
                    for i,r in enumerate(lags):
                        for j,s in enumerate(lags):
                            expected=0 if r!=s else 4*((a**4+b**4)*D(r)**2
                                      +a*a*b*b*(D(r+d)**2+D(r-d)**2))
                            assert inner(columns[i],columns[j])==(F(expected),F(0))
                            entries+=1
                    cases+=1
    return {'exact_gram_matrices':cases,'exact_gram_entries':entries,
            'normalization':'Gram divided by pi squared',
            'orbit_method':'exact norm descent, no iteration cutoff'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-degree',type=int,default=6)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    if not 1<=args.max_degree<=7:
        parser.error('--max-degree must be between one and seven')
    result={'scope':'finite exact controls, not the arbitrary-degree proof',
            'two_radius':exhaustive_two_component(args.max_degree),
            'quadrature_covariance':gram_controls()}
    text=json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    print(text,end='')

if __name__=='__main__':main()
