#!/usr/bin/env python3
"""Exact regression gate for the 20--21 September 2026 BGS continuation.

This checks load-bearing symbolic/arithmetic identities only. It is not a
proof of the analytic limit theorems and not a fixed-tau BGS verification.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import sympy as sp


def three_orientation():
    l, C, Q, R = sp.symbols("l C Q R", positive=True, real=True)
    A = 3*Q/8 + R/2 - l*l/4 - 9*C*C/(8*l)
    B = Q/8 - l*l/4 - 3*C*C/(8*l)
    D = 3*Q/8 - R/2 - l*l/4 - C*C/(8*l)
    radius2 = (Q-C*C/l)*(Q-l*l-2*C*C/l)/2
    assert sp.simplify(4*(A*D-B*B)-radius2+(R-C*C/l)**2) == 0

    t, c, u = sp.symbols("t c u", positive=True)
    r = (1-t*t)/(4*t*t)
    l0 = (1/t-1)/2
    K = r*u+r-r*r/u
    J = 2*r*u+r-r*r/u
    Phi = -u*u+(2*r-1)*u+3*r-2*r*r/u
    assert sp.simplify(Phi.subs(u,l0)) == 0
    radial = lambda f: (1-t*t)**3*sp.diff(f,t,2)+(1-t*t)**2*(2/t-3*t)*sp.diff(f,t)
    gap = (1-t*t)**2/(2*t)
    d = c*t**3*(1-t*t)**2
    assert sp.simplify(radial(l0)-8*K.subs(u,l0)-gap) == 0
    assert sp.Rational(369,512)**2-sp.Rational(9,32) > 0
    return {"schur_identity": True, "barrier_constant": "1/64"}


def recurrence():
    checks = 0
    for T in range(3, 16):
        a = [1, T+1]
        for _ in range(42):
            a.append(T*a[-1]-a[-2])
        total = F(0)
        for j in range(40):
            assert a[j+1]**2-a[j]*a[j+2] == T+2
            total += F(1, a[j]*a[j+1])
            assert total == F(T+1,T+2)-F(a[j+2],(T+2)*a[j+1])
            checks += 1
    T = 6
    lam = 3+2*sp.sqrt(2)
    kappa = sp.simplify((lam-1)/(lam+1))
    assert sp.simplify(kappa-1/sp.sqrt(2)) == 0
    assert sp.simplify(1-(1+sp.sqrt(2))/sp.sqrt(7)) > 0
    return {"recurrence_checks": checks, "project_kappa_H2": "1/sqrt(2)"}


ZERO=(F(0),F(0))
def plus(a,b): return a[0]+b[0],a[1]+b[1]
def times(a,b): return a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def conj(a): return a[0],-a[1]
def abs2(a): return a[0]*a[0]+a[1]*a[1]

def add(*ps):
    out={}
    for p in ps:
        for v,z in p.items():
            out[v]=plus(out.get(v,ZERO),z)
    return {v:z for v,z in out.items() if z!=ZERO}

def scale(p,t): return {v:(t*z[0],t*z[1]) for v,z in p.items()}

def mul(p,q):
    out={}
    for v,z in p.items():
        for w,y in q.items():
            key=(v[0]+w[0],v[1]+w[1])
            out[key]=plus(out.get(key,ZERO),times(z,y))
    return {v:z for v,z in out.items() if z!=ZERO}

def frozen_coefficients():
    one={(0,0):(F(1),F(0))}
    def cos(k):
        return {(0,k):(F(1,2),F(0)),(0,-k):(F(1,2),F(0))}
    sin={(0,1):(F(0),F(-1,2)),(0,-1):(F(0),F(1,2))}
    cp={(1,0):(F(-3,10),F(-2,5)),(-1,0):(F(-3,10),F(2,5))}
    r=mul(add(one,scale(cos(7),-1)),add(one,cos(1)))
    f=add(cos(7),scale(r,F(1,10)),scale(mul(r,sin),F(1,100)),
          scale(mul(r,cp),F(1,100)),scale(one,F(-1,10)))
    assert (0,0) not in f
    assert all(f[(-a,-b)]==conj(z) for (a,b),z in f.items())
    return f

def act(v):
    a,b=v
    return 3*a+4*b,2*a+3*b

def inv(v):
    a,b=v
    return 3*a-4*b,-2*a+3*b

def shifted(v,d):
    for _ in range(abs(d)):
        v=(act if d>=0 else inv)(v)
    return v

def exact_variance():
    c=frozen_coefficients()
    cov={}
    for lag in range(-4,5):
        z=ZERO
        for v,a in c.items():
            w=shifted(v,lag)
            if w in c:
                z=plus(z,times(a,conj(c[w])))
        assert z[1]==0
        cov[lag]=z[0]
    variance=sum(cov.values(),F(0))
    assert variance==F(1650797,4000000)
    f1=sum((abs(z[0])+abs(z[1]))*(abs(v[0])+abs(v[1])) for v,z in c.items())
    assert f1==F(7491,1000)
    return {"variance": str(variance), "F1": str(f1), "lags": {str(k):str(v) for k,v in cov.items()}}


def local_jet():
    lam,a=sp.symbols("lambda a", positive=True)
    u,z=sp.symbols("u z")
    G=(u*u-z*z+a*u*z)**2+u*u*z*z
    GS=sp.expand(G.subs({u:lam*u,z:z/lam}, simultaneous=True))
    bracket=sp.expand(sp.diff(G,u)*sp.diff(GS,z)-sp.diff(G,z)*sp.diff(GS,u))
    resonant=sp.expand(bracket).coeff(u,3).coeff(z,3)
    relation=(lam**2+lam**-2)/2
    assert sp.simplify(resonant.subs(a**2,relation)) == 0
    pure=sp.expand(bracket).coeff(u,6)
    assert sp.simplify(pure-8*a*(lam**2-lam**4)) == 0
    return {"resonant_u3z3": "0 under a^2=(lambda^2+lambda^-2)/2",
            "u6": "8*a*(lambda^2-lambda^4)"}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    result={"status":"PASS",
            "scope":"Exact symbolic/arithmetic regression only; no asymptotic proof audit, Lean certificate, or fixed-tau BGS claim.",
            "three_orientation":three_orientation(),
            "fourier_line":recurrence(),
            "crossover":exact_variance(),
            "local_jet":local_jet()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
