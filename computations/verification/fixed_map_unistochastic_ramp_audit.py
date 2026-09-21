#!/usr/bin/env python3
import itertools, json, math
from fractions import Fraction
import numpy as np
import sympy as sp

roots=[1,1j,-1,-1j]
alpha_phase=(-3-4j)/5

def alias_audit():
    rows=[]; min_re=10
    for a,b,c,d in itertools.product(range(4),repeat=4):
        pairing=sorted((a,b))==sorted((c,d))
        delta=a+b-c-d
        if delta%4 or pairing: continue
        C=roots[a]+roots[b]-roots[c]-roots[d]
        val=(alpha_phase*C).real
        assert abs(C)>1e-12
        assert abs(val)>1e-12
        min_re=min(min_re,abs(val)); rows.append((a,b,c,d,val))
    assert len(rows)==36
    assert min_re >= 0.4-1e-12
    return {'aliased_nonpairing':len(rows),'min_abs_Re_e_minus_ialpha_C':min_re}

def corrected_witness():
    # q0=1/7; corrected midpoint coefficient is r(q+1/2)
    r=2*(1-sp.cos(2*sp.pi/7))
    # easy rigorous lower bound: 2pi/7 > pi/4 => cos < sqrt(2)/2 < 3/4
    assert sp.N(r-sp.Rational(1,2),50)>0
    # safe nonpairing Re lower is 1/5; Q curvature contributes (pi/2)^2
    curv=r*sp.pi**2/sp.Integer(2000)
    assert sp.N(curv-sp.pi**2/sp.Integer(4000),50)>0
    return {'r_shift':str(sp.N(r,30)),'safe_r_lower':'1/2','safe_curvature_lower':'pi^2/4000'}

def gap_constants():
    eps=sp.Rational(1,100)
    upper=2*(sp.Rational(4)/(4-eps))**2-4*(sp.Rational(1)/(4+eps))**2
    assert upper < sp.Rational(881,500) # 1.762
    s2=sp.sqrt(upper-1)
    assert s2 < sp.Rational(7,8)
    return {'frobenius_upper_at_eps_0p01':str(sp.N(upper,25)), 's2_upper':str(sp.N(s2,25)), 'certified_s2_lt':'7/8'}

def dft(N):
    x=np.arange(N); return np.exp(2j*np.pi*np.outer(x,x)/N)/np.sqrt(N)

def haar(N,seed):
    rng=np.random.default_rng(seed); Z=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N));Q,R=np.linalg.qr(Z);d=np.diag(R);return Q*(d/np.abs(d)).conj()

def path_sum(V,m):
    N=V.shape[0]; total=0j; sq=0.0
    for path in itertools.product(range(N),repeat=m):
        amp=1+0j
        for j in range(m): amp*=V[path[(j+1)%m],path[j]]
        sq+=abs(amp)**2
    P=np.abs(V)**2
    target=np.trace(np.linalg.matrix_power(P,m))
    return sq,target

def cyclic_checks():
    checks=[]
    for N,V in [(3,dft(3)),(4,haar(4,20260921))]:
      for m in range(1,6):
        sq,tr=path_sum(V,m)
        err=abs(sq-tr)
        assert err<2e-12,(N,m,sq,tr)
        checks.append({'N':N,'m':m,'error':err})
    return {'checks':checks,'max_error':max(x['error'] for x in checks)}

def main():
    data={'status':'PASS','scope':'Exact branch-alias/gap/cyclic-skeleton regression; fixed-time FIO asymptotics remain an external analytic input.',
          'alias':alias_audit(),'corrected_midpoint_witness':corrected_witness(),'gap':gap_constants(),'cyclic_identity':cyclic_checks()}
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
