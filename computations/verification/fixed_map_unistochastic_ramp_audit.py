#!/usr/bin/env python3
"""Regression for the repaired fixed-map unistochastic ramp skeleton.

Checks the corrected midpoint-symbol branch witness, all aliased non-pairing
quadruples, a certified Frobenius-gap margin, and the exact cyclic path
identity on finite unitary fixtures. Fixed-time FIO asymptotics are external.
"""
from __future__ import annotations
import itertools, json
import numpy as np
import sympy as sp

ROOTS=[1,1j,-1,-1j]
ALPHA_PHASE=(-3-4j)/5

def alias_audit():
    rows=[]; minimum=10.0
    for a,b,c,d in itertools.product(range(4),repeat=4):
        if (a+b-c-d)%4: continue
        if sorted((a,b))==sorted((c,d)): continue
        C=ROOTS[a]+ROOTS[b]-ROOTS[c]-ROOTS[d]
        val=(ALPHA_PHASE*C).real
        assert abs(C)>1e-12 and abs(val)>1e-12
        minimum=min(minimum,abs(val)); rows.append((a,b,c,d))
    assert len(rows)==36 and minimum>=0.4-1e-12
    return {"aliased_nonpairing":len(rows),"min_abs_Re":minimum}

def corrected_witness():
    r=2*(1-sp.cos(2*sp.pi/7))
    assert sp.N(r-sp.Rational(1,2),60)>0
    curvature=r*sp.pi**2/sp.Integer(2000)
    assert sp.N(curvature-sp.pi**2/sp.Integer(4000),60)>0
    return {"r_q0_plus_half":str(sp.N(r,30)),
            "safe_r_lower":"1/2",
            "safe_curvature_lower":"pi^2/4000"}

def gap_constants():
    eps=sp.Rational(1,100)
    upper=2*(sp.Rational(4)/(4-eps))**2-4*(sp.Rational(1)/(4+eps))**2
    assert upper<sp.Rational(881,500)
    s2=sp.sqrt(upper-1)
    assert s2<sp.Rational(7,8)
    return {"pairing_frobenius_upper":str(sp.N(upper,25)),
            "limiting_s2_upper":str(sp.N(s2,25)),
            "certified_eventual_s2_lt":"7/8"}

def dft(N):
    x=np.arange(N)
    return np.exp(2j*np.pi*np.outer(x,x)/N)/np.sqrt(N)

def haar(N,seed):
    rng=np.random.default_rng(seed)
    Z=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
    Q,R=np.linalg.qr(Z); d=np.diag(R)
    return Q*(d/np.abs(d)).conj()

def path_square_sum(V,m):
    N=V.shape[0]; total=0.0
    for path in itertools.product(range(N),repeat=m):
        amp=1+0j
        for j in range(m): amp*=V[path[(j+1)%m],path[j]]
        total+=abs(amp)**2
    P=np.abs(V)**2
    return total,np.trace(np.linalg.matrix_power(P,m))

def cyclic_checks():
    rows=[]
    for N,V in ((3,dft(3)),(4,haar(4,20260921))):
        for m in range(1,6):
            lhs,rhs=path_square_sum(V,m); err=abs(lhs-rhs)
            assert err<5e-12
            rows.append({"N":N,"m":m,"error":err})
    return {"fixtures":rows,"max_error":max(x["error"] for x in rows)}

def main():
    print(json.dumps({
      "status":"PASS",
      "scope":"Exact branch/cyclic regression only; fixed-time torus FIO asymptotics are an external analytic input.",
      "alias":alias_audit(),
      "corrected_midpoint_witness":corrected_witness(),
      "gap":gap_constants(),
      "cyclic_identity":cyclic_checks()
    },indent=2))
if __name__=="__main__":main()
