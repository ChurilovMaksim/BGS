#!/usr/bin/env python3
"""Exact large-lag covariance formula for multi-orbit Fourier symbols.

Integer/Gaussian-integer tests compare direct Fourier orbit sums with the
factorized pair-orbit formula. The growing-window theorem is proved in TeX,
not inferred from these finite tests.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
import hashlib
import json
from pathlib import Path
import sympy as sp
from extremal_resonance import (mv,power,det,neg,ga,gm,gc,accumulate,bracket,
                                transport,orbit_sums,geometry)


def make_symbol(a,filters):
    g={};orbits=[]
    for v,p in filters:
        for w,q in [(v,p),(neg(v),[gc(c) for c in p])]:
            orbits.append((w,q))
            for j,c in enumerate(q):accumulate(g,mv(power(a,j),w),c)
    return g,orbits


def correlation(p,q,k):
    out=(0,0)
    for i,c in enumerate(p):
        if 0<=i+k<len(q):out=ga(out,gm(c,q[i+k]))
    return out


def check(a,filters):
    g,orbs=make_symbol(a,filters);sg,b,_,_,_=geometry(a);t=abs(a[0]+a[3])
    M=max(2*abs(b[2])*abs(x)+(abs(t-2*b[0])+t)*abs(y) for x,y in g)
    G=(4*M*M).bit_length()+1;d=max(len(p)-1 for _,p in filters);R=3*G+2*d+4
    lags=list(range(R+1,R+5))
    hs=[orbit_sums(a,bracket(g,transport(a,g,r))) for r in lags]
    checked=0
    for ii,r in enumerate(lags):
        for jj,s in enumerate(lags):
            direct=(0,0)
            for v,c in hs[ii].items():direct=ga(direct,gm(c,gc(hs[jj].get(v,(0,0)))))
            predicted=(0,0)
            for wa,pa in orbs:
                for wb,pb in orbs:
                    for ell in range(max(1,r-d,s-d),min(r+d,s+d)+1):
                        D=det(wa,mv(power(a,ell),wb))
                        coef=gm(correlation(pa,pb,ell-r),gc(correlation(pa,pb,ell-s)))
                        predicted=ga(predicted,(D*D*coef[0],D*D*coef[1]))
            assert direct==predicted,(a,r,s,direct,predicted)
            assert direct[1]==0
            checked+=1
    return {'A':a,'fourier_support':len(g),'oriented_orbits':len(orbs),
            'integer_gap_bound':G,'starting_lag':R+1,'exact_gram_entries':checked}


def main():
    if not __debug__:raise RuntimeError('Assertions must be enabled')
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);args=ap.parse_args()
    rows=[]
    for a in [(2,1,1,1),(-2,-1,-1,-1),(3,2,4,3)]:
        for w in [(2,0),(1,1)]:
            assert det(w,mv(a,w))!=det((1,0),mv(a,(1,0)))
            filters=[((1,0),[(1,2),(-3,1),(1,-1)]),(w,[(2,1),(1,-2)])]
            rows.append(check(a,filters))
    z=sp.symbols('z');P=z*z-3*z+1
    tests=[([P,2*P],P),([P,P*(z+2)],P),([P,z*z+3*z+1],sp.Integer(1)),
           ([P,sp.Integer(1)],sp.Integer(1))]
    for polys,expected in tests:
        result=polys[0]
        for Q in polys[1:]:result=sp.gcd(result,Q)
        assert sp.Poly(result,z).monic().as_expr()==expected
    # Exact Fourier-symbol factorization for arbitrary orbit filters.
    pa=[1+sp.I,2-sp.I,3];pb=[2,1+2*sp.I]
    corr={k:sum(pa[i]*pb[i+k] for i in range(len(pa)) if 0<=i+k<len(pb))
          for k in range(-len(pa)+1,len(pb))}
    assert sp.expand(sum(v*z**k for k,v in corr.items())-
                     sum(v*z**(-i) for i,v in enumerate(pa))*
                     sum(v*z**i for i,v in enumerate(pb)))==0
    data={'status':'PASS','scope':'exact finite multi-orbit Fourier covariance and common-divisor tests',
          'configurations':len(rows),'exact_gram_entries':sum(r['exact_gram_entries'] for r in rows),
          'gcd_examples':len(tests),'bilinear_symbol_identity':True,'records':rows,
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps({k:v for k,v in data.items() if k!='records'},indent=2))
if __name__=='__main__':main()
