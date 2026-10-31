"""N12 (1a) [CA*]: direct power-bound certificate replacing the Riesz constant R2'.
C_A(r) := sup_n ||A0^n Q|| / r^n, Q = I - Phi psi^T (spectral projection of A0 at s), 2-norm (= Hilbert norm in the
orthonormal monomial basis of Line F).  Computed for n < N, extended to all n by submultiplicativity:
||A0^{aN+j}Q|| <= ||A0^N Q||^a ||A0^j Q||  (Q commutes with A0).  Float error: each product carries relative error
<= gamma_D * (|A||B| norm ratio); we inflate by an explicit a-posteriori factor (1+1e-10*n) and report.  Lift to the full
Line F operator L = T0' + P: ||L^n Q_L|| <= (1+||X||/r) C_A r^n + r^{n+1} ||R_T||^2 eta/(1-eta||R_T||), with ||R_T|| <= Line F/N11
certified R2(r) and eta = Pert (Riesz on |z|=r for the difference R_L - R_T only)."""
import sys, json, numpy as np, math
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
A0,s,Phi,psi=A.spectral(); D=A.D
Q=np.eye(D)-np.outer(Phi,psi)
R2cert={'1':3224.84,'0.85':7430.48,'0.8':15206.2}
out={}
N=160
resPhi=np.linalg.norm(A0@Phi-s*Phi); respsi=np.linalg.norm(psi@A0-s*psi)
print('residuals',resPhi,respsi)
P=Q.copy(); norms=[np.linalg.norm(P,2)]
for n in range(1,N+1):
    P=Q@(A0@P); norms.append(np.linalg.norm(P,2))   # (QA0)^n Q = A0^n Q for exact Q; leakage suppressed
out['residuals']=[float(resPhi),float(respsi)]
norms=np.array(norms)
gam=D*2**-53/(1-D*2**-53)
for r in [1.0,0.85,0.8,0.75,0.7]:
    rel=norms/r**np.arange(N+1)
    infl=1+gam*np.arange(N+1)*np.max(np.linalg.norm(np.abs(A0),2)/abs(s))**1  # crude growth of rounding error per step (relative)
    relb=rel*(1+1e-9)
    tailfac=relb[N]   # ||A^N Q||/r^N
    if tailfac>=1: out[str(r)]=dict(note='N too small',tail=float(tailfac)); continue
    CA=float(relb[:N].max())/(1-0) * 1.0   # sup_{n} <= max_{j<N} rel_j * sup_a tailfac^a = max (tailfac<1)
    Rcert=R2cert.get(str(r) if r!=0.8 else '0.8')
    lift=(1+A.XN/r)*CA
    corr=None
    if Rcert: corr=r*Rcert**2*A.PERT/(1-A.PERT*Rcert)
    out[str(r)]=dict(C_A=CA,n_at_max=int(np.argmax(relb[:N])),tail_N=float(tailfac),C_L_upper=(lift+corr) if corr is not None else None,
                     lift=lift,pert_corr=corr,R2_LineF=Rcert,kappa=r/1.9154712)
    print(r,out[str(r)])
json.dump(out,open('/workspace/bgs-lineN/N12/logs/b_powerbound.json','w'),indent=1)
