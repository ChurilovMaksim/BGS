import sympy as s, numpy as np, json, time
from scipy.linalg import block_diag, expm, svdvals
start=time.time();I=s.I;u=s.eye(3)-s.Rational(1,7)*s.Matrix([1,2,3])*s.Matrix([[1,2,3]]);U=s.kronecker_product(u,s.eye(2))
z1=s.Matrix([[s.Rational(1,8),I/10],[0,-s.Rational(1,9)]]);z2=s.Matrix([[0,s.Rational(1,11)],[I/12,s.Rational(1,13)]]);zs=[z1,z2,-z1-z2];Z=s.diag(*zs);E=s.eye(6);DL=E-Z*Z.conjugate().T;DR=E-Z.conjugate().T*Z
# Norm <1 follows the exact Frobenius-square upper bound, separately for each block.
assert all(s.simplify(s.trace(z*z.conjugate().T))<1 for z in zs)
A=U-Z*U*Z.conjugate().T;B=U*Z-Z*U
assert s.simplify(A*DL.inv()*A.conjugate().T-B*DR.inv()*B.conjugate().T-DL)==s.zeros(6)
det=(E-U*Z*U.conjugate().T*Z.conjugate().T).det()
assert s.simplify(det*s.conjugate(det)/DL.det()**2-(E+DL.inv()*B*DR.inv()*B.conjugate().T).det())==0
assert z1*z1.conjugate().T!=z1.conjugate().T*z1
rng=np.random.default_rng(2847);cnt=0;minmargin=1e4;minintermediate=1e4;maxgradient=0
lc=lambda x:np.logaddexp(x,-x)-np.log(2)
for n in [2,3,4,5]:
 for k in [1,2,3]:
  u=np.exp(2j*np.pi*np.outer(np.arange(n),np.arange(n))/n)/np.sqrt(n);U=np.kron(u,np.eye(k));P=abs(u)**2;K=1.;nn=n*k
  for trial in range(25):
   zz=rng.normal(size=(n,k,k))+1j*rng.normal(size=(n,k,k));zz-=zz.mean(0);zz*=rng.uniform(.1,.995)/max(np.linalg.norm(z,2) for z in zz)
   ww=[]
   for z in zz:
    L,ss,R=np.linalg.svd(z);ww.append((L*np.arctanh(ss))@R)
   Z=block_diag(*zz);W=block_diag(*ww);I0=np.eye(nn);D=I0-Z@Z.conj().T
   HH=-np.linalg.slogdet(D)[1];SS=np.linalg.slogdet(I0-U@Z@U.conj().T@Z.conj().T)[1]+HH
   mean=sum(ww)/n;Fmean=sum(lc(svdvals(w-mean)).sum() for w in ww);Fzero=sum(lc(svdvals(w)).sum() for w in ww)
   v=[ww[j]-sum(P[j,l]*ww[l] for l in range(n)) for j in range(n)];FM=sum(lc(svdvals(vv)).sum() for vv in v)
   assert Fmean>=Fzero-1e-10 and SS>=FM-1e-10 and SS>=HH/2-1e-10
   minmargin=min(minmargin,SS-HH/2);minintermediate=min(minintermediate,SS-FM);cnt+=1
print(json.dumps({'exact':{'N':3,'block_size':2,'rational_complex_nonnormal':True,'strict_contractions':True,'normalized_J_unitary_identity':True,'determinant_identity':True},'floating':{'N':[2,3,4,5],'k':[1,2,3],'trials_per_pair':25,'samples':cnt,'seed':2847,'unitaries':'Fourier only, hence P=J and K=1','min_coercivity_margin':float(minmargin),'min_intermediate_margin':float(minintermediate),'arithmetic':'float64; diagnostic only'},'runtime_seconds':time.time()-start,'non_claims':['No block Mobius gauge or Jacobian','No supersymmetry','No asymptotic theorem inferred from samples']},indent=2))
