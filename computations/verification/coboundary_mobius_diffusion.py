#!/usr/bin/env python3
"""Finite controls for BGS-FLOW-008 and BGS-FLOW-009.

Exact rational noncommutative BCH/Wick reduction; complex128 full GUE-basis
contractions at N=2..5; independent nonlinear-projection Hessians at N=4,5,7,9.
No stochastic-limit simulation, BGS experiment or asymptotic certificate.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.linalg import expm, logm
from scipy.optimize import root
from quadratic_coboundary_noise import hermitian_basis

def add(*polys):
 out=defaultdict(F)
 for p in polys:
  for w,c in p.items():out[w]+=c
 return {w:c for w,c in out.items() if c}
def scale(p,c):return {w:v*c for w,v in p.items()}
def mul(p,q):
 out=defaultdict(F)
 for a,c in p.items():
  for b,d in q.items():
   if len(a+b)<=4:out[a+b]+=c*d
 return dict(out)
def exp(p):
 ans={():F(1)}; power=ans
 for k in range(1,5):
  power=mul(power,p);ans=add(ans,scale(power,F(1,factorial(k))))
 return ans
A={('G',):F(1)};B={('B',):F(1)}
w=mul(mul(exp(scale(A,-1)),exp(add(A,scale(B,-1)))),exp(B))
y=add(w,{():F(-1)})
log=add(y,scale(mul(y,y),F(-1,2)))

def exact_mean():
    out=defaultdict(F)
    for word,c in log.items():
     if len(word)!=4:continue
     b=[int(x=='B') for x in word]
     a=[b[i+1]-b[i] for i in range(3)]
     terms=[(b[0]+a[1]-b[3],(a[0],a[2])),(b[0]-b[3],(a[1],a[0]+a[2]))]
     for power,ms in terms:out[(power,tuple(sorted(j for j in ms if j)))]+=c
    expected={(-1,(1,)):F(3,8),(1,(-1,)):F(-3,8),
     (-2,(1,1)):F(1,12),(-1,(-1,2)):F(1,12),
     (2,(-1,-1)):F(-1,12),(1,(-2,1)):F(-1,12)}
    assert {k:v for k,v in out.items() if v}==expected
    assert sum(v for w,v in log.items() if len(w)==4)==0
    return {str(k):str(v) for k,v in expected.items()}

def check_wick():
    worst=0.; ratios=[]
    for n in (2,3,4,5):
     theta=np.linspace(.17,5.3,n)**1.13
     f=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
     u=f@np.diag(np.exp(1j*theta))@f.conj().T;us=u.conj().T
     basis=hermitian_basis(n)/np.sqrt(n)
     tb=u@basis@us
     vals={'G':basis,'B':tb}
     total=np.zeros((n,n),complex)
     for w,c in log.items():
      if len(w)!=4:continue
      for r in range(n*n):
       for s in range(n*n):
        for ids in ((r,r,s,s),(r,s,r,s),(r,s,s,r)):
         term=np.eye(n,dtype=complex)
         for j,a in enumerate(w):term=term@vals[a][ids[j]]
         total+=float(c)*term
     m1=np.trace(u)/n;m2=np.trace(u@u)/n
     b=1.5*((m1*us-(m1*us).conj().T)/(2j))
     x=m1*m1*(us@us)+m2*m1.conjugate()*us
     b+=(x-x.conj().T)/(6j)
     err=np.max(abs(total-1j*b/2));worst=max(worst,float(err));assert err<2e-12
     rng=np.random.default_rng(n)
     g=sum(x*a for x,a in zip(rng.normal(size=n*n),basis));bb=u@g@us
     scaled=[]
     for eps in (.08,.04,.02):
      w=expm(-1j*eps*g)@expm(1j*eps*(g-bb))@expm(1j*eps*bb)
      pred=np.zeros((n,n),complex)
      for word,c in log.items():
       term=np.eye(n,dtype=complex)
       for a in word:term=term@({'G':g,'B':bb}[a])
       pred+=float(c)*(1j*eps)**len(word)*term
      scaled.append(float(np.linalg.norm(logm(w)-pred)/eps**5))
     ratios.append((n,scaled))
    return {'quartic_Wick_max_error':worst,'fifth_order_scaled_remainders':ratios}

def center(u):
 n=len(u); eye=np.eye(n)
 def ff(v):
  w=v[0]+1j*v[1]
  z=(u-w*eye)@np.linalg.inv(eye-w.conjugate()*u)
  m=np.trace(z)/n
  return [m.real,m.imag]
 fit=root(ff,[0.,0.],tol=1e-11)
 w=fit.x[0]+1j*fit.x[1]
 assert np.linalg.norm(ff(fit.x))<1e-11
 return (u-w*eye)@np.linalg.inv(eye-w.conjugate()*u)

def cov(u,bs):
 n=len(u);q=np.trace(u@u)/n;us=u.conj().T
 tr=np.einsum('jk,akj->a',u@u,bs)
 v=bs/n-(q*(us@bs@us)+q.conjugate()*(u@bs@u))/(2*n)
 v+=(tr[:,None,None]*(us@us)+tr.conj()[:,None,None]*(u@u))/(2*n*n)
 return np.einsum('ajk,bkj->ab',bs,v).real


def check_projection():
    errs=[]
    for n in (4,5,7,9):
     bs=hermitian_basis(n,traceless=True)
     theta=2*np.pi*np.arange(n)/n+.11*np.sin(4*np.pi*np.arange(n)/n)+.05*np.cos(6*np.pi*np.arange(n)/n)
     dft=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
     y=center(dft@np.diag(np.exp(1j*theta))@dft.conj().T);ys=y.conj().T
     q=np.trace(y@y)/n;r=np.trace(y@y@y)/n;d=1-abs(q)**2
     c=cov(y,bs);ev,vec=np.linalg.eigh((c+c.T)/2)
     ks=np.einsum('ab,ajk->bjk',(vec*np.sqrt(np.maximum(ev,0)))@vec.T,bs)
     fa=1j*np.einsum('ajk,kj->a',ks,y)/n
     wa=(fa+q*fa.conj())/d
     ja=1j*wa[:,None,None]*ys-1j*wa.conj()[:,None,None]*y
     la=ks+ja
     v=float(np.vdot(wa,wa).real);zeta=np.dot(wa,wa)
     dm2=2j*np.einsum('ajk,kj->a',ks,y@y)/n
     h=np.dot(wa.conj(),dm2)+r*zeta.conjugate()
     bw=(h+q*h.conjugate())/d
     tt=np.einsum('a,ajk->jk',wa.conj(),ks)
     ac=1j*bw*ys-1j*bw.conjugate()*y+tt@y+tt.conj().T@ys+0.5j*zeta*ys@ys-0.5j*zeta.conjugate()*y@y
     ql=np.einsum('ajk,akl->jl',la,la)
     analytic=-.5*ql@y+1j*ac@y
     # Generator of Pi(exp(i*s*K)Y): independent centered finite difference.
     step=2e-4
     numeric=np.zeros_like(y)
     for k in ks:
      numeric+=(center(expm(1j*step*k)@y)+center(expm(-1j*step*k)@y)-2*y)/(2*step**2)
     assert v<=5/n**2+1e-12
     assert np.linalg.norm(ac,2)<=80/n**2+1e-12
     assert abs(np.trace(analytic))<1e-10
     p2=np.trace(y@y)
     p2drift=2*np.trace(y@analytic)-sum(np.trace(a@y@a@y) for a in la)
     assert abs(p2drift+.5*(1-abs(q)**2)*p2)<=150/n
     p2bracket=sum(abs(2j*np.trace(a@y@y))**2 for a in la)
     assert p2bracket<=64+1e-10
     # Local Möbius orbit invariance of the centered spectrum, modulo rotation.
     shift=.003+.005j
     moved=(y-shift*np.eye(n))@np.linalg.inv(np.eye(n)-shift.conjugate()*y)
     centered=center(moved)
     phase=np.trace(centered@ys)/n;phase=phase/abs(phase)
     assert np.max(abs(centered-phase*y))<2e-12
     err=float(np.max(abs(numeric-analytic)));assert err<3e-7
     comm=np.einsum('ajk,akl->jl',bs/np.sqrt(n),la-bs/np.sqrt(n))
     assert np.max(abs(comm-comm.conj().T))<1e-12
     assert np.linalg.norm(np.trace(la@y,axis1=1,axis2=2))<1e-11
     assert np.linalg.norm(ac-ac.conj().T)<1e-11
     errs.append({'N':n,'projection_drift_error':err,'scaled_drift_op':float(n*n*np.linalg.norm(ac,2)),'m2':float(abs(q))})
    return errs

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    report={'status':'PASS','date':'2026-09-29',
      'arithmetic':'Fraction exact algebra; numpy complex128 finite matrices',
      'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,
      'exact_quartic_mean':exact_mean(),'wick_and_remainder':check_wick(),
      'projection':check_projection(),
      'resource_caps':{'Wick_N':[2,3,4,5],'projection_N':[4,5,7,9],
          'projection_step':2e-4,'BCH_steps':[.08,.04,.02]},
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'exclusions':['No diffusion-limit simulation','No limit theorem certified by finite tests',
                    'No deterministic noise removal','No Lean certificate']}
    data=json.dumps(report,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(data)
    print(data,end='')

if __name__=='__main__':
    main()
