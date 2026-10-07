#!/usr/bin/env python3
"""Bounded controls only. Universal conclusions are in report.md, not inferred here."""
import json, hashlib, platform, time
import sympy as s
import numpy as np
from scipy.linalg import expm, svdvals
from scipy.optimize import root
start=time.time(); exact={}; floats={}
I=s.I
# Exact algebra: rational orthogonal and complex Fourier controls, all strict disks.
H=s.eye(3)-s.Rational(2,14)*s.Matrix([1,2,3])*s.Matrix([[1,2,3]])
F4=s.Matrix([[I**(i*j)/2 for j in range(4)] for i in range(4)])
fixtures=[(H,[s.Rational(1,3)+I/5,-s.Rational(1,4)+I/7,-s.Rational(1,12)-12*I/35]),(F4,[s.Rational(1,3),I/4,-s.Rational(1,5),-s.Rational(2,15)-I/4])]
for k,(U,z) in enumerate(fixtures):
 n=len(z); Z=s.diag(*z); D=s.eye(n)-Z*Z.conjugate().T; C=s.diag(*[s.sqrt(1/D[j,j]) for j in range(n)])
 F=C*(U-Z*U*Z.conjugate().T)*C; G=C*(U*Z-Z*U)*C
 assert s.simplify(U*U.conjugate().T-s.eye(n))==s.zeros(n)
 assert sum(z)==0 and all(bool(D[j,j]>0) for j in range(n))
 assert s.simplify(F*F.conjugate().T-G*G.conjugate().T-s.eye(n))==s.zeros(n)
 det=s.simplify((s.eye(n)-U*Z*U.conjugate().T*Z.conjugate().T).det())
 assert s.simplify(F.det()*s.conjugate(F.det())-det*s.conjugate(det)/D.det()**2)==0
 a=s.Rational(1,7)+I/9; zz=[s.cancel((q-a)/(1-s.conjugate(a)*q)) for q in z]; ZZ=s.diag(*zz);DD=s.eye(n)-ZZ*ZZ.conjugate().T
 det2=s.simplify((s.eye(n)-U*ZZ*U.conjugate().T*ZZ.conjugate().T).det())
 assert s.simplify(det2*s.conjugate(det2)/DD.det()**2-det*s.conjugate(det)/D.det()**2)==0
 exact[str(k)]={'N':n,'centered':True,'block_identity':True,'determinant_identity':True,'mobius_invariance':True}
# Exact common-radius sharpness and rank-one formula.
r=s.symbols('r',positive=True);V=s.diag(1,-1,1,-1);Q=s.simplify(F4*V*F4.conjugate().T*V)
assert Q.eigenvals()=={s.Integer(-1):2,s.Integer(1):2}
assert s.factor((s.eye(4)-r**2*Q).det())==(r-1)**2*(r+1)**2*(r**2+1)**2
for U,_ in fixtures:
 n=U.rows;Z=s.diag(r,*([0]*(n-1)))
 assert s.simplify((s.eye(n)-U*Z*U.conjugate().T*Z).det()-(1-r**2*U[0,0]*s.conjugate(U[0,0])))==0
exact['boundary']={'F4_Q_eigenvalues':{'-1':2,'1':2},'rank_one_identity':True}
# Symbolic N=1,2 Jacobian including arbitrary a and u, computed through Wirtinger derivatives.
for n in [1,2,3,4]:
 aa=s.Rational(1,7)+I/11
 ws=([s.Integer(0)] if n==1 else [s.Rational(j+1,5*n)+I*s.Rational(j+2,7*n) for j in range(n-1)])
 if n>1:ws.append(-sum(ws))
 da=s.symbols('da');db=s.symbols('db');ds=s.symbols('d0:'+str(2*(n-1)))
 diffs=[]
 for j,w in enumerate(ws):
  dw=(ds[2*j]+I*ds[2*j+1] if j<n-1 else -sum(ds[2*i]+I*ds[2*i+1] for i in range(n-1)))
  q=(1-aa*s.conjugate(aa))/(1+s.conjugate(aa)*w)**2
  dz=q*dw+(da+I*db)/(1+s.conjugate(aa)*w)-w*(aa+w)*(da-I*db)/(1+s.conjugate(aa)*w)**2
  # All differential symbols are real. Extract coefficients directly.
  coeff=[s.expand(dz).coeff(v) for v in [da,db,*ds]]
  diffs.extend([[s.re(c).expand(complex=True) for c in coeff],[s.im(c).expand(complex=True) for c in coeff]])
 jac=s.factor(s.Matrix(diffs).det()); predicted=s.factor((n*n-abs(sum(w*w for w in ws))**2)*(1-abs(aa)**2)**(2*n-2)/s.prod(abs(1+s.conjugate(aa)*w)**4 for w in ws))
 assert s.simplify(jac-predicted)==0
 exact['jacobian_'+str(n)]={'actual_equals_formula':True,'positive':bool(jac>0)}
# Bounded double-precision diagnostics. No root existence or theorem inferred.
rng=np.random.default_rng(732104);minmargin=1e3;maxerr=0.;counts=0;minratio=1e3;min_emi=1e3
for n in [2,3,4,5,7,8,12]:
 for kind in ['fourier','haar']:
  if kind=='fourier': U=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n)
  else:
   A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));U,_=np.linalg.qr(A)
  P=abs(U)**2;J=np.ones((n,n))/n;rho=np.linalg.norm(P-J,2);C=n*P.max();K=1+np.sqrt(max(C-1,0))/(1-rho)
  R=np.linalg.inv(np.eye(n)-P+J)
  assert max(np.abs(R).sum(0).max(),np.abs(R).sum(1).max())<=K+2e-12
  for k in range(60):
   z=(1-np.exp(-rng.uniform(.03,4,n)))*np.exp(2j*np.pi*rng.random(n))
   def fun(a):
    a=complex(*a);v=((z-a)/(1-a.conjugate()*z)).sum();return [v.real,v.imag]
   rr=root(fun,[0,0]);a=complex(*rr.x)
   if not rr.success or abs(a)>=1 or np.linalg.norm(fun(rr.x))>1e-8:continue
   z=(z-a)/(1-a.conjugate()*z);d=1-abs(z)**2
   assert min(d)>0
   Z=np.diag(z);CC=np.diag(1/np.sqrt(d));F=CC@(U-Z@U@Z.conj().T)@CC;G=CC@(U@Z-Z@U)@CC
   HH=-np.log(d).sum();SS=np.linalg.slogdet(np.eye(n)-U@Z@U.conj().T@Z.conj().T)[1]+HH
   x=np.arctanh(abs(z))*z/np.maximum(abs(z),1e-300);W=np.diag(x)
   X=np.block([[np.zeros((n,n)),W],[W.conj().T,np.zeros((n,n))]])
   g=expm(X);UU=np.block([[U,np.zeros((n,n))],[np.zeros((n,n)),U]])
   T=expm(-X)@UU@g;ts=np.log(svdvals(T)[:n]);ss=svdvals(W-U@W@U.conj().T)
   emi=np.min(np.cumsum(ts)-np.cumsum(ss));min_emi=min(min_emi,float(emi));assert emi>=-2e-9
   lc=lambda v:np.logaddexp(v,-v)-np.log(2)
   modular=lc(abs((np.eye(n)-P)@x)).sum()
   assert SS>=modular-2e-8
   assert SS>=HH/(2*K*K)-2e-8
   err=max(abs(SS-lc(ts).sum()),np.linalg.norm(F@F.conj().T-G@G.conj().T-np.eye(n),ord=np.inf))
   maxerr=max(maxerr,err);minmargin=min(minmargin,SS-HH/(2*K*K));minratio=min(minratio,SS/HH);counts+=1
floats={'arithmetic':'IEEE754 float64; scipy/numpy, no interval certification','seed':732104,'dimensions':[2,3,4,5,7,8,12],'unitaries':['Fourier','one seeded Haar sample per dimension'],'trials_per_family':60,'accepted_centered_samples':counts,'minimum_coercivity_margin':float(minmargin),'minimum_S_over_H':float(minratio),'minimum_Ky_Fan_margin':float(min_emi),'maximum_block_or_logcosh_residual':float(maxerr),'interpretation':'bounded diagnostics only'}
out={'exact':exact,'floating':floats,'runtime_seconds':time.time()-start,'python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'non_claims':['No actual U_N sampled','No growing-dimension theorem inferred from computation','No supersymmetric measure/source/tail verification']}
print(json.dumps(out,indent=2))
