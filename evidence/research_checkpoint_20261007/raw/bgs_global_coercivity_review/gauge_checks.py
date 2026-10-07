#!/usr/bin/env python3
"""Independent exact ordinary-real Jacobian controls and bounded Mobius tests."""
import sympy as sp
import numpy as np
from scipy.optimize import least_squares
import json,hashlib,time
from pathlib import Path
start=time.perf_counter()
I=sp.I
exact=[]
for n in [1,2,3,4]:
    q=sp.symbols('q:'+str(2*n),real=True)
    aa=q[0]+I*q[1]
    ws=[q[2+2*k]+I*q[3+2*k] for k in range(n-1)]
    ws.append(-sum(ws,sp.S.Zero))
    zs=[(aa+w)/(1+sp.conjugate(aa)*w) for w in ws]
    coords=[]
    for z in zs: coords.extend([sp.re(z).expand(complex=True),sp.im(z).expand(complex=True)])
    vals=[sp.Rational(1,5),sp.Rational(-1,7)]
    for k in range(n-1): vals.extend([sp.Rational(k+1,11*n),sp.Rational((-1)**k,13*n)])
    sub=dict(zip(q,vals))
    jac=sp.Matrix(coords).jacobian(q).subs(sub)
    det=sp.factor(jac.det())
    aaa=aa.subs(sub);www=[sp.simplify(w.subs(sub)) for w in ws]
    abs2=lambda z:sp.expand(z*sp.conjugate(z))
    expected=(n*n-abs2(sum(w*w for w in www)))*(1-abs2(aaa))**(2*n-2)
    for w in www: expected/=abs2(1+sp.conjugate(aaa)*w)**2
    err=sp.factor(det-expected)
    assert err==0
    exact.append({'N':n,'jacobian_identity':str(err),'determinant':str(det)})

# Exact F4 sharpness and negative centering witness.
u=sp.Matrix([[I**(j*k)/2 for k in range(4)] for j in range(4)])
v=sp.diag(1,-1,1,-1)
q=sp.simplify(u*v*u.conjugate().T*v.conjugate().T)
assert q**2==sp.eye(4) and sp.trace(q)==0
r=sp.symbols('r',real=True)
assert sp.factor((sp.eye(4)-r*r*q).det()-(1-r*r)**2*(1+r*r)**2)==0

rng=np.random.default_rng(194861)
float_checks=[]
def mob(a,z):return (z-a)/(1-a.conjugate()*z)
def action(u,z):
 n=len(z);d=np.diag(z)
 return np.linalg.slogdet(np.eye(n)-u@d@u.conj().T@d.conj().T)[1]-np.log1p(-abs(z)**2).sum()
for n in [1,2,3,4,8]:
 for k in range(20):
    aa=.85*np.sqrt(rng.random())*np.exp(2j*np.pi*rng.random())
    z=.95*np.sqrt(rng.random(n))*np.exp(2j*np.pi*rng.random(n))
    mat=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
    u,_=np.linalg.qr(mat)
    defect=abs(action(u,z)-action(u,mob(aa,z)))
    assert defect<2e-10
    # Parametrize a in open disk by a=y/sqrt(1+|y|²); no clipping of residual.
    def afrom(x): return complex(x[0],x[1])/np.sqrt(1+x@x)
    def residual(x):
      zsum=mob(afrom(x),z).sum()
      return [zsum.real,zsum.imag]
    guesses=[np.zeros(2),np.array([1.,-.7]),np.array([-.8,1.2])]
    roots=[]
    for guess in guesses:
      fit=least_squares(residual,guess,xtol=1e-13,ftol=1e-13,gtol=1e-13,max_nfev=2000)
      rr=afrom(fit.x)
      assert np.linalg.norm(residual(fit.x))<1e-9,(n,k,fit)
      roots.append(rr)
    mismatch=max(abs(root-roots[0]) for root in roots)
    assert mismatch<1e-8
    a=roots[0];w=mob(a,z)
    reconstruction=max(abs((a+w)/(1+a.conjugate()*w)-z))
    hessian_min_lower=2*np.sum(1-abs(w)**2)
    assert reconstruction<1e-12 and hessian_min_lower>0
    float_checks.append({'N':n,'action_invariance_error':float(defect),'center_root_spread':float(mismatch),'reconstruction_error':float(reconstruction),'Hessian_lower_bound':float(hessian_min_lower)})

# Noncommuting full-matrix Mobius cocycle, only an algebra control for scalar gauge.
noncommuting=[]
for k in range(20):
 n=3
 a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));a*=.7/np.linalg.norm(a,2)
 b=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));b*=.8/np.linalg.norm(b,2)
 aa=.4+.2j;eye=np.eye(n)
 ma=(a-aa*eye)@np.linalg.inv(eye-aa.conjugate()*a)
 mb=(b-aa*eye)@np.linalg.inv(eye-aa.conjugate()*b)
 left=eye-ma@mb.conj().T
 right=(1-abs(aa)**2)*np.linalg.inv(eye-aa.conjugate()*a)@(eye-a@b.conj().T)@np.linalg.inv(eye-aa*b.conj().T)
 err=np.linalg.norm(left-right)
 assert err<1e-12
 noncommuting.append(float(err))

print(json.dumps({'status':'all_bounded_controls_passed','exact_jacobian':exact,'exact_F4_sharpness':True,'float_count':len(float_checks),'float_checks':float_checks,'noncommuting_cocycle_count':len(noncommuting),'max_noncommuting_cocycle_error':max(noncommuting),'seed':194861,'sympy':sp.__version__,'elapsed_seconds':time.perf_counter()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'nonclaims':['Finite roots do not prove global uniqueness','Ordinary bosonic real Jacobian only, not a super-Berezinian','No block-matrix field theorem or asymptotic conclusion']},indent=2))
