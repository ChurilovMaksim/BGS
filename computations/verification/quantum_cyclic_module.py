#!/usr/bin/env python3
"""Exact finite-field orbit/cyclic-module tests and independent dense checks.

No long-time/no-alias cutoff is used. Algebraic label checks are exact;
NumPy matrix comparisons are explicitly floating-point diagnostics.
"""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import random
import numpy as np
import sympy as sp
from extremal_resonance import ga,gm,gc,norm


def mv(a, v, p): return ((a[0]*v[0]+a[1]*v[1])%p,(a[2]*v[0]+a[3]*v[1])%p)
def det(u,v,p): return (u[0]*v[1]-u[1]*v[0])%p
def minus(v,p): return ((-v[0])%p,(-v[1])%p)
def add(u,v,p): return ((u[0]+v[0])%p,(u[1]+v[1])%p)
def mm(a,b,p):
    return tuple(x%p for x in (a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))
def order(a,p):
    b=(1,0,0,1)
    for k in range(1,2*p+2):
        b=mm(b,a,p)
        if b==(1,0,0,1):return k
    raise ValueError('Order bound exceeded')
def orbit(a,v,p):
    out=[];w=v
    while not out or w!=v:
        if w in out:raise AssertionError('Orbit failed to close at initial point')
        out.append(w);w=mv(a,w,p)
        if len(out)>2*p+2:raise AssertionError('Orbit too long')
    return out

def plus_coeff(out,k,z):
    zz=ga(out.get(k,(0,0)),z)
    if zz==(0,0):out.pop(k,None)
    else:out[k]=zz

def normalized_h(v,arv,p,c=(2,3)):
    """H divided by p*sin(2*pi*(1/2)*d/p); Gaussian-integer coefficients."""
    g={v:c,minus(v,p):gc(c)};q={arv:c,minus(arv,p):gc(c)};out={}
    d=det(v,arv,p)
    if not d:raise ValueError('Zero base determinant')
    for u,z in g.items():
        for w,y in q.items():
            dw=det(u,w,p)
            sg=-1 if dw==d else 1
            assert dw==d or dw==(-d)%p
            vxy=gm(z,y);plus_coeff(out,add(u,w,p),(sg*vxy[0],sg*vxy[1]))
    return out

def exact_case(a,p,rng):
    K=order(a,p)
    assert K>=3 and K%2 and ((a[0]+a[3])**2-4)%p
    v=(1,0);assert det(v,mv(a,v,p),p)
    used=set();arv=v;fields=[];time_checks=0
    for r in range(1,(K+1)//2):
        arv=mv(a,arv,p);h=normalized_h(v,arv,p);assert len(h)==4
        orbs={w:orbit(a,w,p) for w in h}
        for ob in orbs.values():
            assert len(ob)==K and not used.intersection(ob)
            used.update(ob)
        b={j:(rng.randrange(-3,4),rng.randrange(-3,4)) for j in range(-K,2*K+3)}
        direct={};fibres={i:(0,0) for i in range(K)}
        for j,z in b.items():
            fibres[j%K]=ga(fibres[j%K],z)
            for w,c in h.items():plus_coeff(direct,orbs[w][j%K],gm(z,c))
        lhs=sum(norm(z) for z in direct.values())
        rhs=4*norm((2,3))**2*sum(norm(z) for z in fibres.values())
        assert lhs==rhs
        # Exactly the temporal polynomial z^K-1 is a zero.
        for w,c in h.items(): assert orbs[w][K%K]==w
        for n in sorted({1,K-1,K,K+1,2*K+3,p,3*p+1}):
            counts=Counter(j%K for j in range(n))
            q,s=divmod(n,K)
            assert sum(x*x for x in counts.values())==K*q*q+(2*q+1)*s
            assert K*(K*q*q+(2*q+1)*s)==n*n+s*(K-s)
            time_checks+=1
        fields.append(det(v,arv,p))
    return {'p':p,'A':a,'K':K,'lags':len(fields),'disjoint_label_orbits':4*len(fields),
            'time_checks':time_checks,'nonzero_determinants':len(fields)}

def W(p,v):
    a,b=v;out=np.zeros((p,p),complex);x=np.arange(p,dtype=np.int64)
    out[x,(x-b)%p]=np.exp(2j*np.pi*((a*(x-((p+1)//2)*b))%p)/p)
    return out

def dense_case(a,p,n,r=1,c=2+3j):
    K=order(a,p);v=(1,0);vectors=[v]
    for j in range(n+r):vectors.append(mv(a,vectors[-1],p))
    mats=[c*W(p,w)+c.conjugate()*W(p,minus(w,p)) for w in vectors]
    T=np.zeros((p,p),complex)
    for j in range(n):T+=(0.5j*p)*(mats[j]@mats[j+r]-mats[j+r]@mats[j])
    value=float(np.vdot(T,T).real/p)
    d=det(v,vectors[r],p);q,s=divmod(n,K)
    expected=4*p*p*abs(c)**4*np.sin(np.pi*d/p)**2*(K*q*q+(2*q+1)*s)
    rel=abs(value-expected)/max(1,abs(expected))
    assert rel<5e-12,(p,n,value,expected,rel)
    return {'p':p,'K':K,'r':r,'n':n,'variance':value,'formula':float(expected),'relative_error':rel}

def main():
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path)
    ap.add_argument('--prime-limit',type=int,default=101);args=ap.parse_args()
    if args.prime_limit<11:ap.error('prime-limit must be >=11')
    rng=random.Random(20260906);rows=[];dense=[]
    for pp in sp.primerange(5,args.prime_limit+1):
        p=int(pp)
        for t in [3,4,6,-3]:
            a=(t%p,(-1)%p,1,0)
            if (t*t-4)%p==0:continue
            K=order(a,p)
            if K>=3 and K%2:
                rows.append(exact_case(a,p,rng))
                if p<=31 and len(dense)<15:
                    for n in [1,K+1,p,2*p+1]:dense.append(dense_case(a,p,n))
    # Even order: opposite frequencies share an orbit, so the odd-K formula fails.
    p=7;a=(3,6,1,0);K=order(a,p);assert K==8
    h=normalized_h((1,0),mv(a,(1,0),p),p,c=(1,0));out={}
    for w,c in h.items():
        for k in orbit(a,w,p):plus_coeff(out,k,c)
    measured=sum(norm(z) for z in out.values());wrong=4*K
    assert measured!=wrong
    data={'status':'PASS','scope':'exact modular orbit and Gaussian-integer identities; dense checks numerical',
          'configurations':len(rows),'lag_modules':sum(r['lags'] for r in rows),
          'all_time_count_checks':sum(r['time_checks'] for r in rows),
          'dense_checks':len(dense),'max_dense_relative_error':max(x['relative_error'] for x in dense),
          'even_order_negative_control':{'p':p,'K':K,'measured_normalized_squared_norm':measured,'inapplicable_odd_order_value':wrong},
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'configurations_detail':rows,'dense_detail':dense}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if not k.endswith('_detail')},indent=2))
if __name__=='__main__':main()
