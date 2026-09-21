#!/usr/bin/env python3
"""Exact finite regression for the recovered N=19^k hyperbolic dephasing input.

Checks matrix order, primitive-orbit basis, Parseval at N=19, and the residue
finite-type dichotomy. The analytic p-adic van der Corput theorem is external
and is not machine-proved here.
"""
from __future__ import annotations
import argparse, cmath, json, math
from pathlib import Path

P=19
S=((3,4),(2,3))

def mm(A,B,n): return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(2))%n for j in range(2)) for i in range(2))
def mpow(A,e,n):
    R=((1,0),(0,1)); B=A
    while e:
        if e&1:R=mm(R,B,n)
        B=mm(B,B,n); e//=2
    return R

def qmul(x,y,n):
    a,b=x;c,d=y
    return ((a*c+2*b*d)%n,(a*d+b*c)%n)
def qpow(x,e,n):
    R=(1,0); B=x
    while e:
        if e&1:R=qmul(R,B,n)
        B=qmul(B,B,n); e//=2
    return R

def order_checks():
    assert 2 not in {(x*x)%P for x in range(1,P)}
    rows=[]
    I=((1,0),(0,1))
    for k in range(1,8):
        N=P**k; o=20*P**(k-1)
        assert mpow(S,o,N)==I
        for q in (2,5,19):
            if o%q==0: assert mpow(S,o//q,N)!=I
        rows.append({'k':k,'N':N,'order':o})
    assert qpow((3,2),20,P*P)==(1,4*P)
    return rows

def primitive_basis_checks():
    failures=0
    for a in range(P):
        for b in range(P):
            if a==b==0: continue
            sr=((3*a+4*b)%P,(2*a+3*b)%P)
            direct=(a*sr[1]-b*sr[0])%P
            formula=(2*(a*a-2*b*b))%P
            if direct!=formula or direct==0: failures+=1
    assert failures==0
    return {'primitive_vectors':P*P-1,'failures':failures}

def parseval_check():
    N=P; J=list(range(10)); r=(1,0)
    weights=[complex((j%3)-1,(j%2)*0.5) for j in J]
    orbit=[]
    for j in J:
        A=mpow(S,j,N); orbit.append(((A[0][0]*r[0]+A[0][1]*r[1])%N,(A[1][0]*r[0]+A[1][1]*r[1])%N))
    lhs=0.0
    for x in range(N):
        for y in range(N):
            z=0j
            for w,v in zip(weights,orbit): z += w*cmath.exp(2j*math.pi*((x*v[0]+y*v[1])%N)/N)
            lhs += abs(z)**2
    rhs=N*N*sum(abs(w)**2 for w in weights)
    rel=abs(lhs-rhs)/rhs
    assert rel<1e-12
    return {'lhs':lhs,'rhs':rhs,'relative_error':rel}

def finite_type_check():
    fail=[]; branches={'quadratic':0,'cubic':0}
    for A in range(P):
        for B in range(P):
            if A==B==0: continue
            for u in range(1,P):
                d2=(4*A*u*u)%P; d3=(8*B*u*u*u)%P
                if A:
                    branches['quadratic']+=1
                    if not d2: fail.append((A,B,u,d2,d3))
                else:
                    branches['cubic']+=1
                    if not B or not d3: fail.append((A,B,u,d2,d3))
    assert not fail
    return {'failures':0,'branch_fixtures':branches}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--output',type=Path); args=ap.parse_args()
    data={'status':'PASS','scope':'Exact finite arithmetic/regression only; Cluckers analytic van der Corput input and asymptotic BGS are separate.',
          'orders':order_checks(),'primitive_basis':primitive_basis_checks(),'parseval':parseval_check(),'finite_type':finite_type_check()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True); args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
