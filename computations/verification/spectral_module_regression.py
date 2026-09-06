#!/usr/bin/env python3
"""Exact translate-Gram lower bounds and filtered Gram/symbol diagnostics.

The growth-classification proof is analytic; finite floating-point eigenvalues
are not certificates of its asymptotic exponent.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import sympy as s
from extremal_resonance import (bracket,transport,gm,gc,norm,witness,check_witness,
                                determinant,filter_apply,orbit_sums,mv,det,power)


def gram(rows):
    return [[sum(gm(z,gc(q.get(k,(0,0))))[0] for k,z in p.items()) for q in rows] for p in rows]

def riesz(a,g,m,times):
    h=[bracket(g,transport(a,g,r)) for r in range(1,m+1)]
    L=sum(sum(abs(z[0])+abs(z[1]) for z in f.values())**2 for f in h)
    D=1
    for r in range(1,m+1):
        u,v=witness(a,list(g),r);d=check_witness(a,list(g),r,u,v)
        D*=2*d*d*norm(g[u])*norm(g[v])
    rows=[transport(a,f,j) for f in h for j in times];G=gram(rows);den=L**(m-1)
    B=[[den*x-(D if i==j else 0) for j,x in enumerate(row)] for i,row in enumerate(G)]
    # Positive definiteness of this difference is stronger than semidefiniteness
    # required by the theorem, and holds for these test configurations.
    for k in range(1,len(B)+1):assert determinant([row[:k] for row in B[:k]])>0
    return {'A':a,'lags':m,'times':times,'dimension':len(B),'lower_numerator':str(D),'lower_denominator':str(den)}


def filter_gram(a,p):
    d=len(p)-1;v=(1,0);g0={v:(1,0),(-1,0):(1,0)};g=filter_apply(a,g0,p)
    b={k:sum(p[i]*p[i+abs(k)] for i in range(len(p)-abs(k))) for k in range(-d,d+1)}
    lags=list(range(d+1,d+6));rows=[orbit_sums(a,bracket(g,transport(a,g,r))) for r in lags]
    G=gram(rows)
    for i,r in enumerate(lags):
        for j,t in enumerate(lags):
            expect=sum(4*det(v,mv(power(a,k),v))**2*b.get(k-r,0)*b.get(k-t,0)
                       for k in range(1,max(lags)+d+1))
            assert G[i][j]==expect
    return len(lags)**2


def toeplitz_from_weights(w,n):
    ks=list(w);c={j:sum(w[k]*w.get(k-j,0) for k in ks) for j in range(-max(ks)+min(ks),max(ks)-min(ks)+1)}
    return np.array([[c.get(i-j,0.) for j in range(n)] for i in range(n)])


def main():
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);args=ap.parse_args()
    g={(1,0):(2,3),(-1,0):(2,-3),(0,1):(1,2),(0,-1):(1,-2)}
    checked=[riesz(a,g,m,[-2,0,1,4]) for a in [(2,1,1,1),(-2,-1,-1,-1),(3,2,4,3)] for m in [1,2,3]]
    entries=sum(filter_gram(a,p) for a in [(2,1,1,1),(-2,-1,-1,-1)]
                for p in [[1],[1,2],[1,-3,1],[1,3,1],[2,0,-1,2],[0,1,5,6]])
    z,lam=s.symbols('z lam',nonzero=True);t=lam+1/lam
    Pplus=z*z-t*z+1;Pminus=z*z+t*z+1
    assert s.factor(Pplus-(z-lam)*(z-1/lam))==0
    assert s.factor(Pminus-(z+lam)*(z+1/lam))==0
    # Root multiplicities for single, reciprocal-double and off-axis roots.
    examples=[((z-lam),lam,1),((z-lam)*(z-1/lam),lam,2),
              ((z-lam)**2*(z-1/lam),lam,3),((z*z+lam*lam),s.I*lam,1)]
    for P,root,m in examples:
        B=s.cancel(P*P.subs(z,1/z))
        for j in range(m):assert s.simplify(s.diff(B,z,j).subs(z,root))==0
        assert s.simplify(s.diff(B,z,m).subs(z,root))!=0
    lf=(3+5**.5)/2;T=[]
    for p in [[1,-3,1],[1,3,1]]:
        b={k:sum(p[i]*p[i+abs(k)] for i in range(len(p)-abs(k))) for k in range(-2,3)}
        T.append({k:b[k]*lf**k for k in b})
    sample=[];lower=8*25 # q=1, t=3: 2^(2q+1)*(t^2-4)^(2q)
    for n in [8,16,32,64,128]:
        A=toeplitz_from_weights(T[0],n);B=toeplitz_from_weights(T[1],n)
        eplus=float(np.linalg.eigvalsh(A)[0]);eminus=float(np.linalg.eigvalsh(B)[0]);ejoint=float(np.linalg.eigvalsh(A+B)[0])
        assert min(eplus,eminus)>0 and ejoint>=lower-1e-8
        sample.append({'n':n,'soft_plus_min':eplus,'soft_minus_min':eminus,'joint_min':ejoint,'proved_symbol_lower':lower})
    data={'status':'PASS','scope':'exact integer Riesz and Gram tests; numerical Toeplitz diagnostics separately labelled',
          'exact_riesz_configurations':len(checked),'exact_riesz_principal_minors':sum(x['dimension'] for x in checked),
          'exact_filter_gram_entries':entries,'symbolic_root_examples':len(examples),
          'riesz_records':checked,'numerical_complementary_filter_records':sample,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if not k.endswith('_records')},indent=2))
if __name__=='__main__':main()
