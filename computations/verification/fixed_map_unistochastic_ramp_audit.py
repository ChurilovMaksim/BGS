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


def variational_bounds():
    pi=math.pi; t=1e-6
    M1=2*(20*pi)
    M2=2*(20*pi)**2
    M3=2*(20*pi)**3
    M4=2*(20*pi)**4
    d1=math.exp(M2*t)
    d2=t*M3*math.exp(3*M2*t)
    d3=t*math.exp(M2*t)*(3*M3*1.01*0.52+M4*1.01**3)
    assert M1<126 and M2<7.90e3 and M3<4.97e5 and M4<3.12e7
    assert d1<1.01 and d2<0.52 and d3<34
    hp=4-7*(d1-1)
    hk=7*M1
    hkp=7*M2*1.01
    hkpp=7*(M3*1.01**2+M2*0.52)
    hpp=7*0.52
    hppp=7*34
    assert hp>3.94 and hk<9e2 and hkp<6e4 and hkpp<4e6 and hpp<4 and hppp<2.5e2
    pQ=1/hp
    pQQ=hpp/hp**3
    pk=hk/hp
    pkQ=hkp/hp**2+hk*hpp/hp**3
    pkQQ=hkpp/hp**3+3*hkp*hpp/hp**4+hk*hppp/hp**4+3*hk*hpp**2/hp**5
    assert pQ<0.26 and pQQ<0.07 and pk<2.3e2 and pkQ<4e3 and pkQQ<7e4
    w2=M3*pQ**2*pk + M2*pQQ*pk + 2*M2*pQ*pkQ + M1*pkQQ
    assert w2<4e7
    return {'M':[M1,M2,M3,M4],'flow':[d1,d2,d3],'Hp_lower':hp,
            'implicit':[pQ,pQQ,pk,pkQ,pkQQ],'one_branch_second_kappa_bound':w2}

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
          'alias':alias_audit(),'corrected_midpoint_witness':corrected_witness(),'gap':gap_constants(),'variational':variational_bounds(),'cyclic_identity':cyclic_checks()}
    print(json.dumps(data,indent=2))
if __name__=='__main__':main()
