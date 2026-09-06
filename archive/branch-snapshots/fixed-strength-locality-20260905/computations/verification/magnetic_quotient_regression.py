#!/usr/bin/env python3
"""Independent finite falsifiers for the magnetic-quotient spectral theorem.

Exact integer histograms and pairing polynomials are distinguished from
floating matrix checks. Neither type replaces the general written proof.
"""
from __future__ import annotations
import argparse
from collections import Counter
from itertools import product, combinations
import json
import math
from pathlib import Path
import subprocess
import sys
import numpy as np
import sympy as sp
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'computations/python'))
from bgs.magnetic_quotient import (subgroup,orbit_matrix,orbit_basis,gauss_real_gauge,
    word_histogram,canonical_histogram,histogram_trace,mean_trace)
from bgs.jacobi import dlog_table,annihilator_indices,jacobi_matrix


def matchings(items):
    if not items:
        yield ()
        return
    a=items[0]
    for j in range(1,len(items)):
        b=items[j]
        for rest in matchings(items[1:j]+items[j+1:]):
            yield ((a,b),)+rest


def pairing_audit(max_r=5):
    rows=[]
    for r in range(1,max_r+1):
        count=nc=orientations=0
        for pi in matchings(tuple(range(2*r))):
            count+=1
            crosses=[(i,j) for i in range(r) for j in range(i+1,r)
                     if pi[i][0]<pi[j][0]<pi[i][1]<pi[j][1]]
            nc+=not crosses
            for sig in product((-1,1),repeat=r):
                orientations+=1
                lab=[0]*(2*r); eps=[0]*(2*r)
                for i,(a,b) in enumerate(pi):
                    lab[a]=lab[b]=i;eps[a]=sig[i];eps[b]=-sig[i]
                def mon(i,j):
                    e=[0]*(r-1)
                    if i:e[i-1]-=1
                    if j:e[j-1]+=1
                    return tuple(e)
                twice=Counter()
                for a,b in combinations(range(2*r),2):
                    twice[mon(lab[a],lab[b])]+=eps[a]*eps[b]
                    twice[mon(lab[b],lab[a])]-=eps[a]*eps[b]
                assert all(c%2==0 for c in twice.values())
                direct={e:c//2 for e,c in twice.items() if c}
                formula=Counter()
                for i,j in crosses:
                    formula[mon(i,j)]+=sig[i]*sig[j]
                    formula[mon(j,i)]-=sig[i]*sig[j]
                formula={e:c for e,c in formula.items() if c}
                assert direct==formula
                assert bool(formula)==bool(crosses)
                if crosses:
                    assert any(any(e) for e in formula)
                    assert max(sum(a+1 for a in e) for e in formula)<=r
        catalan=math.comb(2*r,r)//(r+1)
        pairing_count=math.factorial(2*r)//(2**r*math.factorial(r))
        assert nc==catalan and count==pairing_count
        rows.append({'r':r,'matchings':count,'noncrossing':nc,'orientations':orientations})
    return rows


def matrix_audit():
    rows=[]
    for p,K in [(7,3),(31,5),(43,7),(67,11),(101,5),(199,11)]:
        g=int(sp.primitive_root(p));h=pow(g,(p-1)//K,p);H=subgroup(p,K,h)
        log=dlog_table(p,g);inds=annihilator_indices(p,K,h,log);inds=inds[inds%2==1]
        V=orbit_basis(p,H)
        chars=np.zeros((p,len(inds)),complex)
        chars[1:]=np.exp(2j*np.pi*np.outer(log[1:],inds)/(p-1))/math.sqrt(p-1)
        U=V.T@chars
        assert np.max(abs(U.conj().T@U-np.eye(len(inds))))<1e-10
        errors=[];wrong=[]
        for q in [1,2,p-1]:
            J=jacobi_matrix(p,K,h,log,inds,q)*np.exp(-2j*np.pi*(q*pow(2,-1,p)%p)/p)/(p-1)
            A=J+J.conj().T;B=orbit_matrix(p,H,q)
            W=np.zeros((p,p),complex)
            x=np.arange(p);W[x,(x-1)%p]=np.exp(2j*np.pi*(q*(x-pow(2,-1,p))%p)/p)
            D,a=gauss_real_gauge(p,log,inds,q)
            real=np.conj(D)[:,None]*A*D[None,:]
            err=max(np.max(abs(J-J.conj().T)),np.max(abs(U.conj().T@B@U-A)),
                    np.max(abs(V.T@(W+W.conj().T)@V-B)),np.max(abs(real.imag)),
                    np.max(abs(abs(a)-1)),np.max(abs(np.linalg.eigvalsh(A)-np.linalg.eigvalsh(real.real))))
            assert err<1e-10,(p,K,q,err)
            errors.append(float(err))
            wrong.append(float(np.max(abs(np.linalg.eigvalsh(A)-np.linalg.eigvalsh(A.real)))))
        rows.append({'p':p,'K':K,'n':len(inds),'maximum_residual':max(errors),'real_projection_gap':max(wrong)})
    assert rows[-1]['real_projection_gap']>1e-3
    return rows


def histogram_audit(cpp=None):
    rows=[]
    for p,K,max_m in [(7,3,6),(31,5,4),(43,7,4)]:
        g=int(sp.primitive_root(p));h=pow(g,(p-1)//K,p);H=subgroup(p,K,h)
        for m in range(1,max_m+1):
            C=word_histogram(p,H,m);can=canonical_histogram(p,C)
            if p==7 and m==1: assert can==[0,0,4,2,2,4,0], can
            if cpp:
                raw=subprocess.check_output([str(cpp),'--histogram',str(p),str(K),str(h),str(m)],text=True)
                assert list(map(int,raw.split()))==can,(p,K,m)
            values=[]
            for q in range(1,p):
                ev=np.linalg.eigvalsh(orbit_matrix(p,H,q))
                tr=np.sum(ev**m);z=histogram_trace(p,K,m,q,C)
                assert abs(tr-z)<1e-8,(p,K,m,q,tr,z)
                values.append(tr)
            mean=mean_trace(p,K,m,C)
            assert abs(np.mean(values)-float(mean))<1e-9
            rows.append({'p':p,'K':K,'m':m,'mean_trace':str(mean),'canonical_histogram':can})
    return rows


def reciprocal_audit():
    # Exhaustive signed tuples with first label fixed to 1; scaling covers all.
    rows=[]
    for p,K,m in [(31,5,4),(71,7,4),(67,11,2)]:
        assert m<K and p*p>m**(K-1)
        h=pow(int(sp.primitive_root(p)),(p-1)//K,p);H=subgroup(p,K,h)
        checked=0
        for tail in product(H,repeat=m-1):
            labels=(1,)+tail
            for eps in product((-1,1),repeat=m):
                if sum(e*t for e,t in zip(eps,labels))%p or sum(e*pow(t,-1,p) for e,t in zip(eps,labels))%p:
                    continue
                balance=Counter()
                for e,t in zip(eps,labels):balance[t]+=e
                assert all(c==0 for c in balance.values())
                checked+=1
        rows.append({'p':p,'K':K,'m':m,'balanced_solutions':checked})
    # Removing m<K is invalid even when reciprocal equations both hold.
    assert sum([1,2,4])%7==sum(pow(t,-1,7) for t in [1,2,4])%7==0
    return rows


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--cpp',type=Path);ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.cpp and not args.cpp.is_file():raise FileNotFoundError(args.cpp)
    result={'producer':'computations/verification/magnetic_quotient_regression.py',
            'scope':'Finite exact algebra and floating matrix agreement; not a formalization of the limiting theorem.',
            'cpp_comparison':bool(args.cpp),'pairings':pairing_audit(),
            'matrices':matrix_audit(),'histograms':histogram_audit(args.cpp),
            'reciprocal_cutoff':reciprocal_audit()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('magnetic quotient regression: PASS; exact C++ comparison =',bool(args.cpp))
    print('pairing orientations:',sum(x['orientations'] for x in result['pairings']))
    print('histograms:',len(result['histograms']))
if __name__=='__main__':main()
