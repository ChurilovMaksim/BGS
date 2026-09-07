#!/usr/bin/env python3
"""Independent exact/numerical checks for the Gaussian-input minimax section.

The analytic minimax proof is in the manuscript. This verifier checks the Weyl
matrix-unit inversion, pure-loss identities, Gaussian-noise factorization,
finite n=128 half-loss certificate, Kraus/characteristic-function consistency,
and amplifier cross-operator decay. Numerical checks are diagnostics only.
"""
from __future__ import annotations
import argparse, hashlib, importlib.util, json, random, sys
from fractions import Fraction as F
from math import comb, factorial
from pathlib import Path
import mpmath as mp

HERE=Path(__file__).resolve()
IMPL=HERE.parents[1]/'analysis'/'gaussian_inverse.py'
spec=importlib.util.spec_from_file_location('gaussian_inverse',IMPL)
gi=importlib.util.module_from_spec(spec);sys.modules[spec.name]=gi;spec.loader.exec_module(gi)


def poly(j,k,negative=False):
    out={}
    for ell in range(min(j,k)+1):
        p,q=j-ell,k-ell
        sign=(-1)**q*((-1)**(p+q) if negative else 1)
        out[p,q]=F(sign,factorial(p)*factorial(q)*factorial(ell))
    return out


def exact_weyl(dim):
    count=0
    for a in range(dim):
      for b in range(dim):
       p=poly(b,a)
       for j in range(dim):
        for k in range(dim):
         q=poly(j,k,True);value=F(0)
         for (pz,pw),pc in p.items():
          for (qz,qw),qc in q.items():
           if pz+qz==pw+qw:value+=pc*qc*factorial(pz+qz)
         target=F(1,factorial(a)*factorial(b)) if (j,k)==(a,b) else F(0)
         assert value==target,(a,b,j,k,value,target)
         count+=1
    return count


def exact_loss_and_factorization():
    checks=0
    for n in range(1,65):
      for eta in [F(1,5),F(1,2),F(9,10),F(99,100)]:
       u=F(1,2*n);a=1-u+u*(1-eta)**n;b=u*eta**n;c2=u*(1-u)*eta**n;s=a+b
       assert sum(F(comb(n,l))*eta**(n-l)*(1-eta)**l for l in range(n+1))==1
       assert a*b-c2==u*u*(eta*(1-eta))**n
       assert s>=1-u and 2*c2/s<=2*u*eta**n
       checks+=2
    factorizations=0
    for nu in [F(1,10),F(1),F(2),F(20)]:
      g=1+nu/2;eta=1/g
      assert g*eta==1
      assert g*(1-eta)+(g-1)==nu
      factorizations+=1
    return checks,factorizations


def finite_half_loss_certificate():
    n=128;u=F(1,n);h=F(1,2**n)
    a=1-u+u*h;b=u*h;c2=u*(1-u)*h;s=a+b;d=a*b-c2
    r2=(a-b)**2+4*c2;gap_upper=4*c2/(2*s-4*c2/s)
    lower=3*10**39;upper=4*10**39
    assert 2*lower*gap_upper/(1-gap_upper)<F(5,18)
    minimum=(9*upper*s.numerator)//(10*s.denominator)
    v=4*c2/r2
    assert minimum*v>F(8,25)
    assert upper*s*(1-s)/(upper*s-minimum)**2<F(1,1000)
    assert 4*upper*d/s<F(1,1000)
    x=F(8,25);assert 1+x+x*x/2+x**3/6>F(10000,7399)
    assert F(999,1000)*F(51,100)-F(1,1000)>F(1,2)
    return 6


def sqrt_matrix(a):
    vals,v=mp.eighe((a+a.H)/2)
    return v*mp.diag([mp.sqrt(max(0,x)) for x in vals])*v.H


def numerical_checks(dps,seed):
    rng=random.Random(seed); channels=fids=kernels=amps=0;anchors=[]
    with mp.workdps(dps):
      tol=mp.mpf(10)**(-dps//2)
      for eta in [mp.mpf('.2'),mp.mpf('.5'),mp.mpf('.9')]:
       dim=5;x=mp.matrix([[mp.mpc(rng.randint(-3,3),rng.randint(-3,3)) for _ in range(dim)] for _ in range(dim)])
       rho=x*x.H;rho/=mp.re(sum(rho[j,j] for j in range(dim)))
       out=gi.pure_loss(rho,eta)
       for z in [mp.mpc('.2','.4'),mp.mpc('1.2','-.7'),mp.mpc(0),mp.mpc(2),mp.mpc(0,2),mp.mpc('.01','.03')]:
        expected=gi.finite_characteristic(rho,mp.sqrt(eta)*z)*mp.exp(-(1-eta)*abs(z)**2/2)
        assert abs(expected-gi.finite_characteristic(out,z))<tol
        channels+=1
       for n in [2,4,6]:
        u=mp.mpf(1)/(2*n);v=mp.matrix([mp.sqrt(1-u)]+[0]*(n-1)+[mp.sqrt(u)])
        w=v.copy();w[n]=-w[n]
        plus=gi.pure_loss(v*v.H,eta);minus=gi.pure_loss(w*w.H,eta)
        sp=sqrt_matrix(plus);fid=mp.re(sum(sqrt_matrix(sp*minus*sp)[j,j] for j in range(n+1)))
        pred=gi.pair_loss_fidelity(n,u,eta)
        assert abs(fid-pred['root_fidelity'])<mp.sqrt(tol)*20
        fids+=1
       n=128;u=mp.mpf(1)/n;p=gi.pair_loss_fidelity(n,u,eta)
       anchors.append({'eta':str(eta),'root_fidelity_gap':mp.nstr(p['root_fidelity_gap'],22)})
      for K in [1,2,3,5,8]:
       for j in range(K+1):
        for k in range(K+1):
         z=mp.sqrt(16*K)*mp.exp(mp.mpc(0,'.31'))
         assert abs(gi.displacement_element(j,k,z))<=mp.exp(-abs(z)**2/4)*(1+tol)
         kernels+=1
      for g in [mp.mpf('1.2'),mp.mpf(2),mp.mpf(5),mp.mpf(10)]:
       q=1-1/g;v=q*(1+q)/2;theta=1/mp.sqrt(g*(1-v));C=1/(g*mp.sqrt((1-v)*(1-q*q/v)))
       assert 0<theta<1
       for n in [2,8,32,64]:
        term=g**(-mp.mpf(n)/2-1);total=term;ell=0
        while True:
         ratio=q*mp.sqrt(mp.mpf(n+ell+1)/(ell+1));term*=ratio;ell+=1;total+=term
         next_ratio=q*mp.sqrt(mp.mpf(n+ell+1)/(ell+1))
         if next_ratio<1 and term*next_ratio/(1-next_ratio)<mp.mpf('1e-45')*C*theta**n:break
         if ell>20000:raise RuntimeError('amplifier tail budget exceeded')
        assert total+term*next_ratio/(1-next_ratio)<=C*theta**n*(1+tol)
        amps+=1
    return {'dps':dps,'kraus_characteristic_checks':channels,'fidelity_checks':fids,
            'weyl_kernel_bounds':kernels,'amplifier_trace_norm_bounds':amps,'anchors':anchors}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--dimension',type=int,default=4);ap.add_argument('--dps',type=int,default=65)
    ap.add_argument('--seed',type=int,default=20260907);ap.add_argument('--output',type=Path)
    a=ap.parse_args()
    if not 2<=a.dimension<=8 or a.dps<50:ap.error('Require 2<=dimension<=8 and dps>=50')
    loss,factors=exact_loss_and_factorization()
    result={'status':'PASS','exact':{'matrix_unit_weyl_inversions':exact_weyl(a.dimension),
             'loss_identities':loss,'additive_noise_factorizations':factors,
             'finite_half_loss_inequalities':finite_half_loss_certificate()},
            'numerical':numerical_checks(a.dps,a.seed),
            'source_sha256':hashlib.sha256(HERE.read_bytes()).hexdigest(),
            'implementation_sha256':hashlib.sha256(IMPL.read_bytes()).hexdigest()}
    bad=0
    for g,v in [(0,1),(-1,2),('.5','.1'),(2,'.1')]:
      try:gi.physical_parameters(g,v)
      except ValueError:bad+=1
      else:raise AssertionError('nonphysical channel accepted')
    result['negative_controls']=bad
    if a.output:a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
