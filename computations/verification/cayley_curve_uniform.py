#!/usr/bin/env python3
"""Exact regression for the global Corvaja--Zannier Cayley curve bound.

The continuum theorem is proved in mathematics/cayley_curve_uniform.md.
This script checks the algebraic geometry identities symbolically and exact
finite-field bookkeeping on many odd/even subgroup designs. Enumeration is
finite evidence, not the proof of the theorem.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse, hashlib, json
from collections import Counter
from math import gcd
from pathlib import Path
import sympy as sp


def icbrt(n: int) -> int:
    lo, hi = 0, 1
    while hi**3 <= n: hi *= 2
    while lo + 1 < hi:
        m=(lo+hi)//2
        if m**3 <= n: lo=m
        else: hi=m
    return lo


def symbolic_checks() -> dict:
    x,y,r,s=sp.symbols('x y r s')
    F=(1-s)*y*(r*x-1)*(x-1)-(1-r)*x*(s*y-1)*(y-1)
    dy=sp.factor(sp.discriminant(F,y))
    dd=sp.factor(sp.discriminant(dy,x))
    target=4096*r**2*s**2*(r-1)**6*(r-s)**2*(s-1)**6
    diag=sp.factor(F.subs(s,r))
    diag_target=-(r-1)*(x-y)*(r*x*y-1)
    X,Y=sp.symbols('X Y')
    charts={
      '00': F,
      '0inf': sp.expand(Y**2*F.subs(y,1/Y)),
      'inf0': sp.expand(X**2*F.subs(x,1/X)),
      'infinf': sp.expand(X**2*Y**2*F.subs({x:1/X,y:1/Y})),
    }
    grads={
      '00':[sp.factor(sp.diff(charts['00'],x).subs({x:0,y:0})),sp.factor(sp.diff(charts['00'],y).subs({x:0,y:0}))],
      '0inf':[sp.factor(sp.diff(charts['0inf'],x).subs({x:0,Y:0})),sp.factor(sp.diff(charts['0inf'],Y).subs({x:0,Y:0}))],
      'inf0':[sp.factor(sp.diff(charts['inf0'],X).subs({X:0,y:0})),sp.factor(sp.diff(charts['inf0'],y).subs({X:0,y:0}))],
      'infinf':[sp.factor(sp.diff(charts['infinf'],X).subs({X:0,Y:0})),sp.factor(sp.diff(charts['infinf'],Y).subs({X:0,Y:0}))],
    }
    expected={
      '00':[r-1,1-s],
      '0inf':[s*(r-1),1-s],
      'inf0':[r-1,r*(1-s)],
      'infinf':[s*(r-1),r*(1-s)],
    }
    return {
      'bidegree':[int(sp.degree(F,x)),int(sp.degree(F,y))],
      'discriminant_of_discriminant':str(dd),
      'disc_identity':bool(sp.expand(dd-target)==0),
      'diagonal_factorization':str(diag),
      'diagonal_identity':bool(sp.expand(diag-diag_target)==0),
      'boundary_gradients':{k:[str(z) for z in v] for k,v in grads.items()},
      'boundary_gradient_identity':all(all(sp.expand(a-b)==0 for a,b in zip(grads[k],expected[k])) for k in grads),
    }


def subgroup(p: int, k: int) -> list[int]:
    g=int(sp.primitive_root(p)); h=pow(g,(p-1)//k,p)
    return [pow(h,j,p) for j in range(k)]

def dval(p: int, rho: int, x: int) -> int:
    return ((rho*x-1)%p)*((x-1)%p)*pow(((1-rho)*x)%p,p-2,p)%p

def design(p: int, k: int) -> dict:
    H=subgroup(p,k)
    rows={rho:Counter(dval(p,rho,x) for x in H) for rho in H if rho!=1}
    total=diag=0; off_max=0; off_min=None
    for rho,a in rows.items():
      for sig,b in rows.items():
        n=sum(a[t]*b[t] for t in a.keys() & b.keys())
        total+=n
        if rho==sig: diag+=n
        else:
          off_max=max(off_max,n); off_min=n if off_min is None else min(off_min,n)
          assert 4 <= n <= 2*k
    C=Counter()
    for u in H:
      if u==1: continue
      for v in H:
        if v==1 or u==v: continue
        C[((u-1)*(v-1)*pow((v-u)%p,p-2,p))%p]+=1
    energy=sum(n*n for n in C.values())
    d=gcd(2,k)
    diag_formula=2*k*(k-1)-k+d
    admissible_diag=2*k*k-7*k+4+d
    assert total-energy==4*(k-1)**2
    assert diag==diag_formula
    b_int=min(2*k,max(4,icbrt(864*k*k),(48*k*k)//p))
    upper=admissible_diag+(k-1)*(k-2)*(b_int-4)
    assert energy <= upper
    return {'p':p,'K':k,'energy':energy,'extended':total,'diagonal_extended':diag,
            'offdiag_min':off_min,'offdiag_max':off_max,'B_integer':b_int,'energy_upper':upper}


def main() -> None:
    if not __debug__: raise RuntimeError('Do not run with python -O')
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--prime-limit',type=int,default=257)
    ap.add_argument('--max-order',type=int,default=32)
    ap.add_argument('--output',type=Path)
    args=ap.parse_args()
    if args.prime_limit<7 or args.max_order<3: ap.error('limits too small')
    sym=symbolic_checks()
    rows=[]
    for p in list(sp.primerange(3,args.prime_limit+1)):
      for k in sp.divisors(p-1):
        if 3 <= k <= args.max_order:
          rows.append(design(int(p),int(k)))
    passed=(sym['bidegree']==[2,2] and sym['disc_identity'] and sym['diagonal_identity']
            and sym['boundary_gradient_identity'] and bool(rows))
    result={'status':'PASS' if passed else 'FAIL',
            'scope':'symbolic identities plus finite exact field regression; Corvaja--Zannier is the external theorem input',
            'prime_limit':args.prime_limit,'max_order':args.max_order,
            'finite_designs':len(rows),'odd_orders':sum(r['K']%2 for r in rows),
            'even_orders':sum(r['K']%2==0 for r in rows),
            'max_tested_order':max(r['K'] for r in rows),
            'symbolic':sym,'anchors':rows[:8]+rows[-8:],
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
      args.output.parent.mkdir(parents=True,exist_ok=True)
      args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in {'anchors','symbolic'}},indent=2))
    if not passed: raise SystemExit(1)

if __name__=='__main__': main()
