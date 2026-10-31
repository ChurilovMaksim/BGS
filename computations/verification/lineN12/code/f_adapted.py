"""N12 (1e) ADAPTED NORM for the Line F sector-4 core operator A0 (Galerkin, dim 495) -- reusable artefact.
Norm: ||v||_H^2 = v^* H v,  H = omega * conj(psi) psi^T + Qt^* P Qt,  Qt = I - Phi psi^T,
P = Stein solution  P = I + kap^{-2} B^* P B,  B = Qt A0 Qt / s  (P = sum_j kap^{-2j} (B^j)^* B^j).
Properties (exact for exact Phi,psi; verified a posteriori in float with explicit error terms):
 (N1) ||A0/s||_H <= 1,   (N2) ||(A0/s)^n Qt||_H <= kap^n  (one-step contraction, constant 1),
 (N3) c_lo ||v||_2 <= ||v||_H <= c_hi ||v||_2,
 (N4) twist Lipschitz: ||(A(d)-A(0))/s||_H <= Lip_H |d|,  Lip_H = (2 pi/|s|) sum_n |n||w_4(n)| ||M_n||_H  (core Galerkin part).
Saves logs/adapted_norm.npz (T = Cholesky factor with ||v||_H = ||T v||_2, H, Phi, psi, s, kap, omega, constants)."""
import sys, json, numpy as np, scipy.linalg as sl
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
kap=float(sys.argv[1]) if len(sys.argv)>1 else 0.45
omega=float(sys.argv[2]) if len(sys.argv)>2 else 1.0
tau0=float(sys.argv[3]) if len(sys.argv)>3 else 0.0
A0,s,Phi,psi=A.spectral(tau0)
ev=np.sort(abs(np.linalg.eigvals(A0)))[::-1]; D=A.D; I=np.eye(D)
Qt=I-np.outer(Phi,psi); B=Qt@A0@Qt/s
# Stein: P - (B/kap)^* P (B/kap) = I
P=sl.solve_discrete_lyapunov((B/kap).conj().T, I)
P=(P+P.conj().T)/2
H=omega*np.outer(psi.conj(),psi)+Qt.conj().T@P@Qt
H=(H+H.conj().T)/2
T=np.linalg.cholesky(H).conj().T          # H = T^* T
Ti=np.linalg.inv(T)
def nH(M): return np.linalg.norm(T@M@Ti,2)
sv=np.linalg.svd(T,compute_uv=False)
res=dict(tau0=tau0,mu1=float(ev[0]),mu2=float(ev[1]),gap_ratio=float(ev[1]/ev[0]),kap=kap,omega=omega,s=[s.real,s.imag],c_lo=float(sv.min()),c_hi=float(sv.max()),cond=float(sv.max()/sv.min()))
res['norm_A0_over_s']=nH(A0/s)
res['norm_B']=nH(B)
pw=[]; M=Qt.copy()
for n in range(1,13):
    M=(A0/s)@M; pw.append(nH(M)/kap**n)
res['pow_ratio_n1_12']=pw
# residual of Stein eq and commutation (a-posteriori error inputs)
res['stein_resid']=float(np.linalg.norm(P-(B/kap).conj().T@P@(B/kap)-I,2))
res['comm_resid']=float(np.linalg.norm(A0@Qt-Qt@A0,2))
res['eig_resid']=[float(np.linalg.norm(A0@Phi-s*Phi)),float(np.linalg.norm(psi@A0-s*psi))]
# Lipschitz constants: core Galerkin part in H-norm vs 2-norm
Mn_H=np.array([nH(Mk) for Mk in A.MS]); Mn_2=np.array([np.linalg.norm(Mk,2) for Mk in A.MS])
w=np.abs(A.COEF0); n=np.abs(A.NS)
res['Lip_H']=float(2*np.pi/abs(s)*np.sum(n*w*Mn_H)); res['Lip_H_series']=[float(x) for x in 2*np.pi/abs(s)*n*w*Mn_H]; res['Lip_2']=float(2*np.pi/abs(s)*np.sum(n*w*Mn_2))
# twisted single-step norms at the four slow twists and a grid (for D1/D2 users)
res['norm_A_tw']={str(t):nH(A.Amat(tau0+t)/s) for t in [0,0.125,0.25,0.375,0.5,0.625,0.75,0.875]}
print(json.dumps(res,indent=1))
np.savez(f'/workspace/bgs-lineN/N12/logs/adapted_norm_t{tau0}_k{kap}.npz',T=T,H=H,P=P,Phi=Phi,psi=psi,s=s,kap=kap,omega=omega,Qt=Qt)
json.dump(res,open(f'/workspace/bgs-lineN/N12/logs/adapted_norm_t{tau0}_k{kap}.json','w'),indent=1)
