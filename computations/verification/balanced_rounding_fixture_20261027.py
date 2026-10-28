#!/usr/bin/env python3
"""Finite fixture: rational nullspace and moments, floating point angles.

K=4, M=2, N=11. Diagnostic only: not original matrices, no asymptotic proof.
No third-party dependencies.
"""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from fractions import Fraction as F
import cmath
import math

M,K,N=2,4,11
ks=[0,1,2,3,1,0,2,3,0,1,2]
initial=[F(j,12) for j in range(1,12)]
p=initial[:]
z=[1+0j,1j,-1+0j,-1j]
cols=[]
for k in ks:
    col=[]
    for m in range(1,M+1):
        d=z[(k+1)%K]**m-z[k]**m
        col.extend((F(int(d.real)),F(int(d.imag))))
    cols.append(col)
def moments(x):
    return [sum(x[j]*cols[j][i] for j in range(N)) for i in range(2*M)]
def nullvec(indices):
    a=[[cols[j][i] for j in indices] for i in range(2*M)]
    piv=[]; row=0
    for c in range(len(indices)):
        pivot=next((r for r in range(row,2*M) if a[r][c]),None)
        if pivot is None: continue
        a[row],a[pivot]=a[pivot],a[row]
        q=a[row][c]; a[row]=[v/q for v in a[row]]
        for r in range(2*M):
            if r!=row:
                q=a[r][c]; a[r]=[x-q*y for x,y in zip(a[r],a[row])]
        piv.append(c); row+=1
        if row==2*M: break
    free=next(c for c in range(len(indices)) if c not in piv)
    v=[F(0) for _ in indices]; v[free]=F(1)
    for r,c in enumerate(piv): v[c]=-a[r][free]
    return v
steps=0
while len(idx:=[j for j,x in enumerate(p) if 0<x<1])>2*M:
    v=nullvec(idx)
    endpoints=[(1-p[j])/q if q>0 else -p[j]/q for j,q in zip(idx,v) if q]
    t=min(endpoints); assert t>0
    for j,q in zip(idx,v): p[j]+=t*q
    assert moments(p)==moments(initial) and all(0<=x<=1 for x in p)
    steps+=1
rounded=[int(x>=F(1,2)) for x in p]
h=2*math.pi/K
for m in range(1,M+1):
    d=sum(complex(float(rounded[j]-p[j]))*(z[(ks[j]+1)%K]**m-z[ks[j]]**m) for j in range(N))
    assert abs(d)<=M*m*h+1e-12
    raw=sum(cmath.exp(1j*m*(ks[j]+float(initial[j]))*h) for j in range(N))
    snap=sum(z[(ks[j]+rounded[j])%K]**m for j in range(N))
    assert abs(raw-snap)<=N*m*m*h*h/2+M*m*h+1e-12
print(f'PASS: N={N}, K={K}, M={M}; {steps} exact rational balancing steps')
