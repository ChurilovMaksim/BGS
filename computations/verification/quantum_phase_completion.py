#!/usr/bin/env python3
"""Exact sparse Gram tests for the phase-completed quantum cyclic module.

The four-label Weyl coefficients are Gaussian integers after dividing each
commutator by its nonzero real sine factor. No floating-point phase is used in
these structural tests. Dense Weyl matrix checks are reported separately.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as sp
from quantum_cyclic_module import order,mv,det,normalized_h,orbit,dense_case
from extremal_resonance import ga,gm,gc,norm


def sparse_gram(a,p,c):
    K=order(a,p);m=(K-1)//2;v=(1,0);arv=v;incidence=defaultdict(list)
    for r in range(1,m+1):
        arv=mv(a,arv,p);h=normalized_h(v,arv,p,c)
        assert len(h)==4
        for w,co in h.items():
            ob=orbit(a,w,p);assert len(ob)==K
            for j,k in enumerate(ob):incidence[k].append(((r-1)*K+j,co))
    G={}
    for group in incidence.values():
        for i,x in group:
            for j,y in group:
                key=(i,j);G[key]=ga(G.get(key,(0,0)),gm(gc(x),y))
    G={k:x for k,x in G.items() if x!=(0,0)}
    assert all(i==j or x[1]==0 for (i,j),x in G.items())
    return K,m,G


def components(G,dimension):
    adj=defaultdict(set)
    for i,j in G:
        if i!=j:adj[i].add(j);adj[j].add(i)
    remaining=set(range(dimension));out=[]
    while remaining:
        seed=min(remaining);todo=[seed];remaining.remove(seed);block=[]
        while todo:
            i=todo.pop();block.append(i)
            for j in adj[i]:
                if j in remaining:remaining.remove(j);todo.append(j)
        out.append(sorted(block))
    return out


def main():
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prime-limit',type=int,default=61)
    ap.add_argument('--output',type=Path);args=ap.parse_args()
    if args.prime_limit<7:ap.error('prime-limit must be at least 7')
    rows=[];generic_blocks=0;rank_checks=0;dense=[]
    for pp in sp.primerange(3,args.prime_limit+1):
        p=int(pp)
        for t in [3,4,6,-3]:
            a=(t%p,(-1)%p,1,0)
            if (t*t-4)%p==0:continue
            K=order(a,p)
            if K<3:continue
            K,m,G=sparse_gram(a,p,(1,1))
            assert len(G)==K*m
            assert all(i==j and x==(16,0) for (i,j),x in G.items())
            rows.append({'p':p,'trace_parameter':t,'K':K,'dimension':K*m})
            if K%2==0 and p<=31:
                _,_,H=sparse_gram(a,p,(2,3))
                for block in components(H,K*m):
                    assert len(block)<=4
                    M=sp.Matrix([[H.get((i,j),(0,0))[0] for j in block] for i in block])
                    eig=M.eigenvals()
                    assert all(x in [256,576,1296] for x in eig)
                    generic_blocks+=1
                _,_,Hreal=sparse_gram(a,p,(1,0))
                rank=0
                for block in components(Hreal,K*m):
                    M=sp.Matrix([[Hreal.get((i,j),(0,0))[0] for j in block] for i in block])
                    rank+=M.rank()
                assert rank==K*(K-2)//8
                rank_checks+=1
                if len(dense)<20:
                    for r in sorted({1,m,K//4}):
                        if 1<=r<=m:
                            dense.append(dense_case(a,p,2*p+1,r=r,c=1+1j))
    data={'status':'PASS','scope':'exact Gaussian-integer sparse Gram identities; dense checks numerical',
          'configurations':len(rows),'even_order_configurations':sum(x['K']%2==0 for x in rows),
          'orthogonal_operators':sum(x['dimension'] for x in rows),
          'generic_phase_exact_blocks':generic_blocks,'real_phase_rank_checks':rank_checks,'dense_checks':len(dense),
          'maximum_dense_relative_error':max(x['relative_error'] for x in dense),
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'configuration_records':rows,'dense_records':dense}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if not k.endswith('_records')},indent=2))
if __name__=='__main__':main()
