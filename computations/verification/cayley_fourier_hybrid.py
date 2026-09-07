#!/usr/bin/env python3
"""Exact finite regression for the Cayley centered-energy Fourier/Weil bound.

The growing-parameter theorem uses the classical mixed Weil estimate externally.
This script verifies the exact finite-field identities and the simplified integer
consequence p E_+(A)-|A|^4 <= 4 p |A|(p-|A|) on all tested subgroups.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path


def primes_upto(n: int):
    sieve=[True]*(n+1); sieve[:2]=[False,False]
    for q in range(2,int(n**0.5)+1):
        if sieve[q]:
            sieve[q*q:n+1:q]=[False]*(((n-q*q)//q)+1)
    return [q for q in range(3,n+1) if sieve[q]]
def factor(n:int):
    out=[]; d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:n//=d;e+=1
            out.append((d,e))
        d+=1
    if n>1:out.append((n,1))
    return out
def divisors(n:int):
    ds=[1]
    for q,e in factor(n):
        ds=[d*q**j for d in ds for j in range(e+1)]
    return sorted(ds)
def primitive_root(p:int):
    qs=[q for q,_ in factor(p-1)]
    for g in range(2,p):
        if all(pow(g,(p-1)//q,p)!=1 for q in qs):return g
    raise RuntimeError('primitive root')
def inv(a,p): return pow(a,p-2,p)
def cayley(h,p): return ((h+1)*inv(h-1,p))%p

def energy(A,p):
    r=[0]*p
    for a in A:
        for b in A:r[(a+b)%p]+=1
    return sum(x*x for x in r),r

def check(p,K,g):
    step=(p-1)//K
    H={pow(g,step*j,p) for j in range(K)}
    assert len(H)==K and 1 in H
    A={cayley(h,p) for h in H if h!=1}
    n=K-1
    assert len(A)==n and all((-a)%p in A for a in A)
    E,r=energy(A,p)
    assert sum(r)==n*n
    centered_num=p*E-n**4
    assert centered_num>=0
    rhs=4*p*n*(p-n)
    assert centered_num<=rhs,(p,K,centered_num,rhs)
    rd=[0]*p
    for a in A:
        for b in A:rd[(a-b)%p]+=1
    assert sum(x*x for x in rd)==E
    return {'p':p,'K':K,'index':(p-1)//K,'size_A':n,'energy':E,
            'centered_numerator':centered_num,'integer_rhs':rhs,
            'max_sum_fiber':max(r)}
def main():
    if not __debug__:raise RuntimeError('assertions required')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prime-limit',type=int,default=257)
    ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    if a.prime_limit<5:ap.error('prime limit >=5')
    rows=[]; dense=0
    for p in primes_upto(a.prime_limit):
        g=primitive_root(p)
        for K in divisors(p-1):
            if K<2:continue
            row=check(p,K,g); rows.append(row)
            if K**5>p**3:dense+=1
    result={'status':'PASS','scope':'exact finite regression; mixed Weil estimate is external',
            'prime_limit':a.prime_limit,'designs':len(rows),
            'dense_hybrid_designs':dense,'max_order':max(r['K'] for r in rows),
            'anchors':rows[:4]+rows[-4:],
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
