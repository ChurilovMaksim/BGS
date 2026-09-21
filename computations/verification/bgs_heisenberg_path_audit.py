#!/usr/bin/env python3
"""Finite/exact regression for the recovered fixed-map Weyl path-escape theorem.

This checks algebraic constants, the raw modular Weyl commutator magnitude,
cyclic forcing fixtures, and the all-characteristic encounter-rank kernel.
It does not prove the asymptotic path-sum theorem or BGS.
"""
from __future__ import annotations
from fractions import Fraction as F
import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp

TAU = F(1, 10**80)
R0 = 9
S = np.array([[3, 4], [2, 3]], dtype=int)

ZERO=(F(0),F(0))
def cadd(a,b): return (a[0]+b[0],a[1]+b[1])
def cmul(a,b): return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def cscale(a,t): return (a[0]*t,a[1]*t)
def cabs(a): return sp.sqrt(sp.Rational(a[0].numerator,a[0].denominator)**2+sp.Rational(a[1].numerator,a[1].denominator)**2)

def add(*ps):
    out={}
    for p in ps:
        for v,z in p.items(): out[v]=cadd(out.get(v,ZERO),z)
    return {v:z for v,z in out.items() if z!=ZERO}
def scale(p,t): return {v:cscale(z,t) for v,z in p.items()}
def mul(p,q):
    out={}
    for v,z in p.items():
        for w,y in q.items():
            key=(v[0]+w[0],v[1]+w[1])
            out[key]=cadd(out.get(key,ZERO),cmul(z,y))
    return {v:z for v,z in out.items() if z!=ZERO}

def physical_fourier_coefficients():
    one={(0,0):(F(1),F(0))}
    def cosq(k): return {(k,0):(F(1,2),F(0)),(-k,0):(F(1,2),F(0))}
    sinq={(1,0):(F(0),F(-1,2)),(-1,0):(F(0),F(1,2))}
    cosp={(0,1):(F(-3,10),F(-2,5)),(0,-1):(F(-3,10),F(2,5))}
    r=mul(add(one,scale(cosq(7),F(-1))),add(one,cosq(1)))
    f=add(cosq(7),scale(r,F(1,10)),scale(mul(r,sinq),F(1,100)),scale(mul(r,cosp),F(1,100)),scale(one,F(-1,10)))
    assert f.get((0,0),ZERO)==ZERO
    return f

def raw_weyl_coefficients():
    # physical e^{2pi i(kq+lp)} maps to raw T(l,k)
    return {(l,k):z for (k,l),z in physical_fourier_coefficients().items()}

def coefficient_constants():
    coeff=raw_weyl_coefficients()
    a1=sp.simplify(sum((abs(v[0])+abs(v[1]))*cabs(z) for v,z in coeff.items()))
    target=2*sp.sqrt(101)/25+sp.Rational(1307,200)
    assert sp.simplify(a1-target)==0
    assert max(abs(a)+abs(b) for a,b in coeff)==R0
    qstar=sp.N(2*sp.pi*sp.Rational(1,10**80)*a1*R0,80)
    Q=sp.Float('5e-78',100)
    t=1/sp.sqrt(Q)
    lam=3+2*sp.sqrt(2)
    gamma=(2*sp.log(t)/lam+7*sp.log(1-sp.sqrt(Q)))/R0
    z=sp.exp(-gamma)
    Z=((1+z)/(1-z))**2-1
    assert qstar < Q
    assert gamma > sp.Rational(339,100)
    assert Z < sp.Rational(145,1000)
    A=sp.log(t)/R0
    assert A < sp.Rational(989,100)
    assert sp.N(4*A+25*sp.log(Z),60) < -8
    return {
        'nonzero_coefficients':len(coeff),
        'A1':str(target),
        'A1_decimal':str(sp.N(target,20)),
        'R0':R0,
        'qstar_decimal':str(qstar),
        'gamma_decimal':str(sp.N(gamma,20)),
        'Z_gamma_decimal':str(sp.N(Z,20)),
    }

def T_raw(N,a,b):
    a%=N; b%=N; inv2=pow(2,-1,N)
    M=np.zeros((N,N),dtype=complex)
    for x in range(N):
        y=(x+a)%N
        phase=np.exp(2j*np.pi*((b*(x+inv2*a))%N)/N)
        M[x,y]=phase
    return M

def raw_commutator_checks():
    coeff=raw_weyl_coefficients()
    fixtures=0
    maxerr=0.0
    for N in (11,19):
        for r,z in sorted(coeff.items())[:12]:
            Tr=T_raw(N,*r)
            for n in ((1,2),(3,1),(4,5),(0,1)):
                Tn=T_raw(N,*n)
                C=Tr@Tn-Tn@Tr
                target=((n[0]+r[0])%N,(n[1]+r[1])%N)
                Tout=T_raw(N,*target)
                c=np.trace(Tout.conj().T@C)/N
                sigma=r[0]*n[1]-r[1]*n[0]
                expected=2*abs(math.sin(math.pi*sigma/N))
                err=abs(abs(c)-expected)
                maxerr=max(maxerr,err); fixtures+=1
                assert err < 2e-12,(N,r,n,c,expected)
    return {'fixtures':fixtures,'max_abs_error':maxerr}

def forcing_checks():
    lam=3+2*math.sqrt(2)
    worst=0.0; fixtures=0
    patterns=[[(1,0),(-1,1)],[(2,-1),(0,1),(-2,0)],[(j%5-2,(3*j)%7-3) for j in range(11)],[(j%9-4,(5*j)%11-5) for j in range(37)]]
    for ns in patterns:
        m=len(ns); lhs=sum(abs(a)+abs(b) for a,b in ns); rhs0=0
        for j,(a,b) in enumerate(ns):
            c,d=ns[(j+1)%m]
            sa=3*a+4*b; sb=2*a+3*b
            rhs0 += abs(c-sa)+abs(d-sb)
        if rhs0:
            ratio=lhs/rhs0; worst=max(worst,ratio)
            assert lhs <= (lam/2+1e-12)*rhs0
        fixtures+=1
    return {'fixtures':fixtures,'max_lhs_over_forcing':worst,'lambda_over_2':lam/2}

def adj_cycle(m):
    A=np.zeros((m,m),dtype=int)
    for i in range(m):
        j=(i+1)%m; A[i,j]=A[j,i]=1
    return A

def rank_mod(A,p):
    A=(A.copy()%p).astype(object); n=A.shape[0]; rr=0
    for c in range(n):
        piv=next((i for i in range(rr,n) if int(A[i,c])%p),None)
        if piv is None: continue
        A[[rr,piv]]=A[[piv,rr]]
        inv=pow(int(A[rr,c])%p,-1,p)
        for j in range(c,n): A[rr,j]=(int(A[rr,j])*inv)%p
        for i in range(n):
            if i==rr: continue
            f=int(A[i,c])%p
            if f:
                for j in range(c,n): A[i,j]=(int(A[i,j])-f*int(A[rr,j]))%p
        rr+=1
    return rr

def encounter_rank_checks():
    checks=0; worst=0.0
    for m in range(5,8):
        A=adj_cycle(m)
        for perm in itertools.permutations(range(m)):
            B=A-A[np.ix_(perm,perm)]
            s=int(np.count_nonzero(np.any(B!=0,axis=1)))
            if not s: continue
            for p in (2,101):
                r=rank_mod(B,p)
                assert 25*r>=s,(m,perm,p,s,r)
                worst=max(worst,s/r); checks+=1
    return {'field_checks':checks,'max_support_over_rank':worst,'tested_characteristics':[2,101]}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    data={
        'status':'PASS',
        'scope':'Finite/exact regression for recovered raw-Weyl path-escape algebra; not a proof of the asymptotic theorem or BGS.',
        'constants':coefficient_constants(),
        'raw_commutator':raw_commutator_checks(),
        'cyclic_forcing':forcing_checks(),
        'encounter_rank':encounter_rank_checks(),
    }
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
if __name__=='__main__': main()
