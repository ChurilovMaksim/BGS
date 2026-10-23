#!/usr/bin/env python3
"""Independent finite controls for the BGS audit. No asymptotic claim is certified by tests."""
from __future__ import annotations
from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import math, json, itertools, importlib.util
import numpy as np
from scipy.linalg import expm, eigvalsh

OUT=Path(__file__).parent
Z=(F(0),F(0)); ONE=(F(1),F(0)); I=(F(0),F(1))
def ca(z,w):return z[0]+w[0],z[1]+w[1]
def cm(z,w):return z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0]
def cs(z,s):return z[0]*s,z[1]*s
def cc(z):return z[0],-z[1]
def add(*ds):
    out={}
    for d in ds:
        for k,v in d.items():out[k]=ca(out.get(k,Z),v)
    return {k:v for k,v in out.items() if v!=Z}
def scale(d,s):return {k:cs(v,s) for k,v in d.items() if cs(v,s)!=Z}
def mul(a,b):
    out={}
    for k,v in a.items():
        for l,w in b.items():
            kl=(k[0]+l[0],k[1]+l[1]);out[kl]=ca(out.get(kl,Z),cm(v,w))
    return {k:v for k,v in out.items() if v!=Z}
def cos(k,l=0):return {(k,l):(F(1,2),F(0)),(-k,-l):(F(1,2),F(0))}
def sin(k,l=0):return {(k,l):(F(0),F(-1,2)),(-k,-l):(F(0),F(1,2))}
def shifted_q(d):return {k:cs(v,F((-1)**k[0])) for k,v in d.items()}
one={(0,0):ONE}
rpoly=mul(add(one,scale(cos(7),-1)),add(one,cos(1)))
phase=add(scale(cos(0,1),F(-3,5)),scale(sin(0,1),F(4,5)))
g=add(cos(7),scale(rpoly,F(1,10)),scale(mul(rpoly,sin(1)),F(1,100)),scale(mul(shifted_q(rpoly),phase),F(1,100)),scale(one,F(-1,10)))
T=((3,2),(4,3))
def tv(v):return 3*v[0]+2*v[1],4*v[0]+3*v[1]
def push(d):return {tv(k):v for k,v in d.items()}
def cov(a,b):
    ans=Z
    for k,v in a.items():ans=ca(ans,cm(v,b.get((-k[0],-k[1]),Z)))
    return ans

def need(b,s):
    if not b:raise AssertionError(s)
need(len(g)==32,'32 modes')
need((0,0) not in g,'mean zero')
need(all(g.get((-k,-l))==cc(v) for (k,l),v in g.items()),'reality')
raw={(l,k):cs(v,F((-1)**(k*l))) for (k,l),v in g.items()}
covs=[];gn=g
for lag in range(7):
    covs.append(cov(g,gn));gn=push(gn)
need(covs[0]==(F(66033,160000),F(0)),'norm')
need(covs[1]==(F(-7,2000000),F(0)),'lag one')
need(all(v==Z for v in covs[2:]),'sample later covariances')
second=[tv(tv(k)) for k in g]
need(all(k*l>0 and abs(l)>=7 for k,l in second),'all-lag cone certificate')
variance=covs[0][0]+2*covs[1][0]
need(variance==F(1650797,4000000),'variance')
# h/pi^2 = {g,g o S}/pi^2. All coefficients exact Gaussian rationals.
h={}
for u,a in g.items():
    for v,b in push(g).items():
        det=u[0]*v[1]-u[1]*v[0]
        k=(u[0]+v[0],u[1]+v[1])
        h[k]=ca(h.get(k,Z),cs(cm(a,b),F(-4*det)))
h={k:v for k,v in h.items() if v!=Z}
hcov=[];hn=h
for lag in range(8):hcov.append(cov(h,hn));hn=push(hn)
hvar=hcov[0][0]+2*sum(v[0] for v in hcov[1:])
need(hvar==F(102203970585164681,10**12),'bracket variance candidate')
# Prove covariance tail n>=4 by an explicit finite escape into a cone.
h4=list(h)
for _ in range(4):h4=[tv(k) for k in h4]
maxl=max(abs(k[1]) for k in h)
cone_tail=all(k*l>0 and abs(l)>maxl for k,l in h4)
# Some short stable preimages can delay escape, so certify by direct orbits to cone.
def no_future_hits(start,forbidden,first):
    v=start
    for _ in range(first):v=tv(v)
    for _ in range(80):
        if v in forbidden:return False
        if v[0]*v[1]>0 and abs(v[1])>maxl:return True
        v=tv(v)
    return False
need(all(no_future_hits(v,set(h),4) for v in h),'all bracket covariance lags >=4')
# Exact phases at rational points with denominators dividing 8: symbolic only here.
import sympy as sy
def eval_exact(d,q,p):
    ans=0
    for (k,l),(a,b) in d.items():
        f=sy.Rational(k)*q+sy.Rational(l)*p
        ans+=(sy.Rational(a.numerator,a.denominator)+sy.I*sy.Rational(b.numerator,b.denominator))*sy.expand_complex(sy.exp(2*sy.pi*sy.I*f))
    return sy.simplify(sy.expand_complex(ans))
s1=eval_exact(h,sy.Rational(1,4),sy.Rational(1,4))+eval_exact(h,sy.Rational(3,4),sy.Rational(1,4))
s2=eval_exact(h,sy.Rational(3,4),sy.Rational(3,8))+eval_exact(h,sy.Rational(3,4),sy.Rational(5,8))
need(sy.simplify(s1+sy.Rational(19615657,15625))==0,'period 2 certificate A')
need(sy.simplify(s2-sy.Rational(39437497,31250)-sy.Rational(30144,3125)*sy.sqrt(2))==0,'period 2 certificate B')

# Rebuild actual matrices directly from the stated quantization, not from prior checkers.
def W(N,k,l):
    x=np.arange(N);out=np.zeros((N,N),complex)
    out[x,(x+l)%N]=np.exp(2j*np.pi*k*(x+l/2)/N)
    return out

def Raw(N,a,b):
    x=np.arange(N);out=np.zeros((N,N),complex);h2=pow(2,-1,N)
    out[x,(x+a)%N]=np.exp(2j*np.pi*((b*(x+h2*a))%N)/N)
    return out

def M(N):
    x=np.arange(N)[:,None];y=np.arange(N)[None,:]
    expo=(-pow(8,-1,N)*(3*x*x-2*x*y+3*y*y))%N
    return np.exp(2j*np.pi*expo/N)/np.sqrt(N)
def A(N):return sum((float(v[0])+1j*float(v[1]))*W(N,k,l) for (k,l),v in g.items())
def adj(X):return X.conj().T
matrix_checks=[]
for N in (3,5,7,9,11,13,19,21,29,31,35,61):
    an=A(N);mn=M(N)
    herm=np.linalg.norm(an-adj(an));uni=np.linalg.norm(mn@adj(mn)-np.eye(N))
    need(herm<1e-10 and uni<1e-10,'Hermiticity and unitarity')
    min_eig_gap=float(np.min(np.diff(eigvalsh(an))))
    signerr=0.;egerr=0.;rawerr=0.
    for k,l,k2,l2 in [(1,0,0,1),(2,-3,-4,1),(N-1,2,1,N-2)]:
        omega=k*l2-l*k2
        signerr=max(signerr,np.linalg.norm(W(N,k,l)@W(N,k2,l2)-np.exp(-1j*np.pi*omega/N)*W(N,k+k2,l+l2)))
    for k,l in [(1,0),(0,1),(2,-1),(9,1)]:
        egerr=max(egerr,np.linalg.norm(mn@W(N,k,l)@adj(mn)-W(N,3*k+2*l,4*k+3*l)))
        rawerr=max(rawerr,np.linalg.norm(W(N,k,l)-(-1)**(k*l)*Raw(N,l,k)))
    need(signerr<1e-9 and egerr<1e-9 and rawerr<1e-9,'quantization signs')
    if N>=19:need(abs(np.trace(an@an).real/N-float(covs[0][0]))<1e-11,'matrix norm matches exact')
    if N==7:need(np.linalg.norm(an-.9*np.eye(N))<1e-11,'N7 exception')
    matrix_checks.append(dict(N=N,hermiticity=herm,unitarity=uni,weyl_product=signerr,egorov=egerr,raw_midpoint=rawerr,min_A_gap=min_eig_gap))

# Newly found invalid decimal lower bound in earlier prose: log-scale time.
# Test a stronger claim in the external paper's orbit lemma against all primes <300.
# Check the older exact scalar return phase against the actual matrix.
trace_tests=[]
for p in (3,5,7,11,13,19,29,31):
    mat=M(p);eps=1 if p%4==1 else 1j
    leg=lambda x:1 if pow(x%p,(p-1)//2,p)==1 else -1
    exact=leg(-2)*eps
    got=np.trace(mat)
    need(abs(got-exact)<1e-10,'Gauss trace')
    trace_tests.append(dict(p=p,actual=[got.real,got.imag],correct=[complex(exact).real,complex(exact).imag]))

# A universal all-frequency periodization identity is checked independently.
# Shell modes: DPP kernel comparison not asserted by numerics.
report={
 'scope':'finite/exact controls; not a proof of BGS',
 'mode_count':len(g),'norm_A_squared':str(covs[0][0]),
 'g_temporal_covariances':[str(a)+(' + i*'+str(b) if b else '') for a,b in covs],
 'g_CLT_variance':str(variance),'h_mode_count':len(h),
 'h_covariances_over_pi4':[str(a) for a,b in hcov],
 'h_variance_over_pi4':str(hvar),'h_period_sums_over_pi2':[str(s1),str(s2)],
 'matrix_checks':matrix_checks,'metaplectic_trace_checks':trace_tests}
(OUT/'independent_checks.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
