#!/usr/bin/env python3
"""Independent bounded floating controls for global bosonic coercivity.
No canonical implementation imported. The checks are diagnostics, not a proof.
"""
import json, time, sys, hashlib
from pathlib import Path
import numpy as np
from scipy.linalg import expm
import scipy
import mpmath as mp

rng=np.random.default_rng(732046)
start=time.perf_counter()
checks=[]
def lc(x):
    x=np.abs(x)
    return x+np.log1p(np.exp(-2*x))-np.log(2.)
def haar(n):
    q,r=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))
    return q @ np.diag(np.diag(r)/np.abs(np.diag(r)))
def fourier(n):
    j=np.arange(n)
    return np.exp(2j*np.pi*np.outer(j,j)/n)/np.sqrt(n)
def check(u,z,label):
    n=len(z);eye=np.eye(n);j=np.ones((n,n))/n
    p=np.abs(u)**2
    c=max(1.,n*np.max(p));rho=np.linalg.norm(p-j,2)
    if rho>=1.-1e-12: raise AssertionError(('gap',label,rho))
    k=1+np.sqrt(c-1)/(1-rho)
    zmat=np.diag(z);b=u@zmat@u.conj().T
    h=-np.log1p(-np.abs(z)**2).sum()
    s=np.linalg.slogdet(eye-b@zmat.conj().T)[1]+h
    radius=np.abs(z)
    w=np.divide(np.arctanh(radius)*z,radius,out=np.zeros(n,complex),where=radius>0)
    v=(eye-p)@w
    diff=np.diag(w)-u@np.diag(w)@u.conj().T
    sv=np.linalg.svd(diff,compute_uv=False)
    inv=np.linalg.inv(eye-p+j)
    row=max(np.abs(inv).sum(1));col=max(np.abs(inv).sum(0))
    # Build g(z) directly from scalar coefficients; not from expm.
    a=1/np.sqrt(1-radius**2)
    az=np.diag(a);bz=np.diag(a*z)
    ga=np.block([[az,bz],[bz.conj().T,az]])
    uu=np.block([[u,np.zeros_like(u)],[np.zeros_like(u),u]])
    gb=uu@ga@uu.conj().T
    eta=np.diag(np.r_[np.ones(n),-np.ones(n)])
    gg=(eta@gb.conj().T@eta)@ga
    # Cartan values from off-diagonal singular values, avoiding tiny reciprocal SVs.
    tt=np.arcsinh(np.linalg.svd(gg[:n,n:],compute_uv=False))
    ds=np.linalg.slogdet(gg[n:,n:])[1]
    variances={
      'coercivity_margin':s-h/(2*k*k),
      'cartan_determinant_error':abs(s-ds)/(1+abs(s)),
      'cartan_logcosh_error':abs(s-lc(tt).sum())/(1+abs(s)),
      'emi_partial_sum_margin':np.min(np.cumsum(tt)-np.cumsum(sv)),
      'pinching_margin':lc(sv).sum()-lc(v).sum(),
      'inverse_row_margin':k-row,
      'inverse_col_margin':k-col,
      'centering_margin':lc(w-w.mean()).sum()-lc(w).sum(),
      'modular_margin':k*k*lc(v).sum()-lc(w-w.mean()).sum(),
      'mean_z_residual':abs(z.sum()),
      'unitarity_residual':np.linalg.norm(u@u.conj().T-eye),
      'cartan_sv_pairing_error':None,
      'max_radius':float(radius.max()),
      'N':n,'family':label,'S':s,'H':h,'C':c,'rho':rho,'K':k,
    }
    # Direct SVD only away from high condition numbers.
    if radius.max()<.999:
      lgs=np.log(np.linalg.svd(gg,compute_uv=False))
      variances['cartan_sv_pairing_error']=float(max(abs(lgs+lgs[::-1])))
      assert np.max(abs(lgs[:n]-tt))<1e-7
    for key in ['coercivity_margin','emi_partial_sum_margin','pinching_margin','inverse_row_margin','inverse_col_margin','centering_margin','modular_margin']:
      assert variances[key]>-1e-7*(1+h+k*k), (label,key,variances[key])
    assert variances['cartan_determinant_error']<1e-7,(label,variances)
    assert variances['cartan_logcosh_error']<1e-7,(label,variances)
    checks.append({key:float(val) if isinstance(val,np.floating) else val for key,val in variances.items()})

check(np.ones((1,1)),np.array([0j]),'N1_zero')
for n in [2,3,4,5,8,12,20]:
    us=[('fourier',fourier(n)),('haar0',haar(n)),('haar1',haar(n))]
    a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));a=(a+a.conj().T)/(2*np.sqrt(n))
    us.extend([('near_identity_03',expm(.3j*a)),('near_identity_10',expm(1j*a))])
    for uname,u in us:
      for sample in range(15):
        raw=rng.normal(size=n)+1j*rng.normal(size=n);raw-=raw.mean()
        r=[.001,.1,.5,.9,.99][sample%5]
        z=raw/max(abs(raw))*r
        check(u,z,f'{uname}_random_{sample}')
      for r in [.9,.999,1-1e-7,1-1e-10]:
        # Exact geometric balancing analytically; FP mean residual recorded.
        z=r*np.exp(2j*np.pi*np.arange(n)/n)
        check(u,z,f'{uname}_polygon_{r}')
      if n>=3:
        for r in [.9,1-1e-10]:
          z=np.zeros(n,complex);z[0]=r;z[1:]=-r/(n-1)
          check(u,z,f'{uname}_unbalanced_radii_{r}')

# Explicit 2x2 analytic benchmark: Hadamard and z=(r,-r) imply S=-log(1-r^2)*2+log(1+r^4).
# Check high precision without double linear algebra, radii approaching boundary.
mp.mp.dps=100
bench=[]
for exponent in [1,3,10,30,60]:
    r=1-mp.mpf(10)**(-exponent)
    u=mp.matrix([[1,1],[1,-1]])/mp.sqrt(2);z=mp.diag([r,-r])
    h=-2*mp.log(1-r*r)
    s=mp.log(abs(mp.det(mp.eye(2)-u*z*u.T*z)))+h
    claimed=h+mp.log(1+r**4)
    assert abs(s-claimed)<mp.mpf('1e-90')
    assert s>=h/2
    bench.append({'boundary_exponent':exponent,'formula_error':str(abs(s-claimed)),'S_over_H':str(s/h)})

# Essential-hypothesis negative control: constant nonzero z has S=0 and H>0.
u=fourier(4);r=.4;z=np.eye(4)*r
s_constant=np.linalg.slogdet(np.eye(4)-u@z@u.conj().T@z)[1]-4*np.log1p(-r*r)
assert abs(s_constant)<1e-12

# Flatness scaling lemma scalar scan; includes x=0, tiny x and large x.
# Use high precision to avoid cancellation at x~0.
scaling=[]
for x in ['0','0.000000000001','.1','1','10','1000']:
 for k in ['1','1.00001','2','100']:
    xx=mp.mpf(x);kk=mp.mpf(k)
    gap=mp.log(mp.cosh(xx/kk))-mp.log(mp.cosh(xx))/kk**2
    assert gap>=-mp.mpf('1e-95')
    scaling.append(str(gap))

result={'status':'all_bounded_controls_passed','arithmetic':'NumPy complex128/float64, plus mpmath 100 decimal digits for declared scalar/2x2 controls','seed':732046,'count':len(checks),'dimensions':sorted(set(x['N'] for x in checks)),
'checks':checks,'high_precision_2x2':bench,'constant_z_negative_control_S':float(s_constant),'scalar_scaling_count':len(scaling),
'nonclaims':['No exhaustive coverage of unitary matrices or disk vectors','No asymptotic or universality conclusion','No proof from floating tests','No Grassmann variables, source terms, or super-Jacobian tested'],
'python':sys.version,'numpy':np.__version__,'scipy':scipy.__version__,'mpmath':mp.__version__,'elapsed_seconds':time.perf_counter()-start,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
print(json.dumps(result,indent=2))
