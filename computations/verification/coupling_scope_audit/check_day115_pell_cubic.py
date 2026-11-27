#!/usr/bin/env python3
"""Exact finite five-step cubic check from Day 115, November 27 review packet."""

from itertools import combinations
from collections import defaultdict
from math import sin, cos, pi

def require(condition, description):
    if not condition:
        raise RuntimeError(description)


def main():
    N=41
    inv2=pow(2,-1,N)
    L=4000
    R={0:4,1:2,-1:2,6:-1,-6:-1,7:-2,-7:-2,8:-1,-8:-1}
    R=defaultdict(int,R)
    add=lambda u,v:(u[0]+v[0],u[1]+v[1])
    mul=lambda u,v:(u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0])
    zero=(0,0)




    steps=[]
    modes={}
    for k in range(-9,10):
        v=(2000*(abs(k)==7)+100*R[k]-400*(k==0),-5*(R[k-1]-R[k+1]))
        if v != zero: modes[(0,k%N)]=v
        for l in (-1,1):
            v=(-3*R[k],-4*l*R[k])
            if v != zero: modes[(l%N,k%N)]=v
    require(sum(abs(a) + abs(b) for a, b in modes.values()) == 4744, "literal Fourier l1 numerator")
    require(len(modes)==32, 'len(modes)==32')
    for j in range(5):
        steps.append(modes)
        modes={((3*a+4*b)%N,(2*a+3*b)%N):c for (a,b),c in modes.items()}
    require(modes==steps[0], 'modes==steps[0]')
    B=defaultdict(lambda:zero)
    for modes in steps:
        for v,c in modes.items(): B[v]=add(B[v],c)
    require(len(B)==150, 'len(B)==150')
    require(B[(0,0)]==zero and sum(x*x+y*y for x,y in B.values())==33015940, 'B[(0,0)]==zero and sum(x*x+y*y for x,y in B.values())==33015940')
    T=[zero]*N
    for i,j,k in combinations(range(5),3):
        for (a,b),c1 in steps[i].items():
            for (c,d),c2 in steps[j].items():
                c3=steps[k].get(((-a-c)%N,(-b-d)%N),zero)
                ix=((a*d-b*c)*inv2)%N
                if c3 != zero: T[ix]=add(T[ix],mul(mul(c1,c2),c3))
    require(T[14]==(6480000000,0) and T[25]==(-3239986000,0), 'T[14]==(6480000000,0) and T[25]==(-3239986000,0)')
    require(all(v==0 for _,v in T), 'all(v==0 for _,v in T)')
    require(sum(abs(v) for k,(v,_) in enumerate(T) if k not in (14,25))<10**9, 'sum(abs(v) for k,(v,_) in enumerate(T) if k not in (14,25))<10**9')
    diff=[(T[k][0]-T[-k][0],T[k][1]+T[-k][1]) for k in range(N)]
    # Only relations over Q(i) among 1,zeta,...,zeta^40 are multiples
    # of 1+zeta+...+zeta^40. A nonconstant T-Tbar certifies Im(T) != 0.
    nonzero=any(v!=diff[0] for v in diff)
    require(nonzero, 'nonzero')
    print("T coefficients",[(k,v) for k,v in enumerate(T) if v != zero])
    print("T minus conjugate",[(k,v) for k,v in enumerate(diff) if v != zero])
    print("imaginary part nonzero:",nonzero)
    z=sum((cos(2*pi*k/N)+1j*sin(2*pi*k/N))*complex(*v) for k,v in enumerate(T))/L**3
    print("normalized T (display only)", z)
    print("intensity cubic (display only)", 2*N**5*z.imag)
    print("positive-minus-negative cubic (display only)", 4*N**5*z.imag)


if __name__ == "__main__":
    main()
