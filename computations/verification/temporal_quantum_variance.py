#!/usr/bin/env python3
"""Independent dense-matrix check of the no-alias quantum variance bound.

Floating-point regression only. The mathematical proof is in the canonical
manuscript; no Heisenberg-scale or eigenphase-universality claim is made.
"""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from extremal_resonance import det, mv, power, witness, transport, combine

def weyl(N, v):
    a,b=v; x=np.arange(N); out=np.zeros((N,N),dtype=complex)
    out[x,(x-b)%N]=np.exp(2j*np.pi*a*(x-b/2)/N)
    return out

def quantize(N, f):
    out=np.zeros((N,N),dtype=complex)
    for v,z in f.items(): out+=complex(*z)*weyl(N,v)
    return out

def check(a,g,coeff,n,N):
    m=len(coeff); R=max(max(map(abs,v)) for v in g)
    anorm=max(abs(a[0])+abs(a[1]),abs(a[2])+abs(a[3]))
    assert 2*R*anorm**(n-1)*(1+anorm**m)<N
    q=[quantize(N,transport(a,g,j)) for j in range(n+m)]
    T=np.zeros((N,N),dtype=complex)
    for l in range(n):
        for r,c in enumerate(coeff,1): T+=(0.5j*N*c)*(q[l]@q[l+r]-q[l+r]@q[l])
    value=float(np.vdot(T,T).real/(n*N))
    fourier={}
    for l in range(n):
        al=power(a,l)
        for r,c in enumerate(coeff,1):
            ar=power(a,r)
            for u,z in g.items():
                for v,w in g.items():
                    av=mv(ar,v); k=mv(al,(u[0]+av[0],u[1]+av[1]))
                    d=det(u,av)
                    fourier[k]=fourier.get(k,0)-c*N*np.sin(np.pi*d/N)*complex(*z)*complex(*w)
    predicted=float(sum(abs(z)**2 for z in fourier.values())/n)
    u,v=witness(a,sorted(g),m); D=det(u,mv(power(a,m),v))
    lower=2*coeff[-1]**2*N*N*np.sin(np.pi*D/N)**2*abs(complex(*g[u])*complex(*g[v]))**2
    error=abs(value-predicted)/max(1,value)
    hermitian=float(np.linalg.norm(T-T.conj().T)/max(1,np.linalg.norm(T)))
    assert error<1e-10 and hermitian<1e-10 and value+1e-9*max(1,value)>=lower
    return {'A':a,'N':N,'times':n,'lags':m,'variance':value,'fourier_variance':predicted,
            'witness_determinant':D,'lower_bound':float(lower),'relative_error':error,
            'hermiticity_error':hermitian}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path)
    args=ap.parse_args(); rows=[]
    g={(1,0):(2,3),(-1,0):(2,-3),(0,1):(1,-2),(0,-1):(1,2)}
    for a in [(2,1,1,1),(-2,-1,-1,-1),(3,-1,1,0)]:
        for n in [1,2]:
            for coeff in [[1],[2,-1]]: rows.append(check(a,g,coeff,n,181))
    a=(4,1,3,1); f={(1,0):(1,0),(-1,0):(1,0)}
    q0=quantize(3,f);q1=quantize(3,transport(a,f,1))
    control=float(np.linalg.norm(1.5j*(q0@q1-q1@q0)))
    assert det((1,0),mv(a,(1,0)))==3 and control<1e-10
    data={'status':'PASS','scope':'floating-point finite regression of a proved no-alias bound',
          'cases':len(rows),'maximum_relative_error':max(r['relative_error'] for r in rows),
          'aliasing_negative_control_norm':control,'records':rows,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='records'},indent=2))

if __name__=='__main__':main()
