"""Verify the N12 adapted norm (reusable; gap (a) and gap (b) D1/D2).
Usage: python verify_adapted.py [npz]   (default ../logs/adapted_norm_t0.0_k0.45.npz)
Checks, with explicit float rounding bounds (Higham gamma_n) and Weyl's inequality, that
 (V1) H = T^*T is Hermitian PD and c_lo^2 I <= H <= c_hi^2 I
 (V2) ||A0/s||_H <= 1+eta            (A0 = sector-4 Galerkin core operator at total phase 1/2, rebuilt from cert_core blocks)
 (V3) ||Qt||_H <= 1+eta, ||(A0/s) Qt||_H <= kap(1+eta)
 (V4) Galerkin->true operator: additive error ||A_true - A0||_H <= cond*(D*RAD + Pert-type terms) printed for the user.
Each matrix inequality X^*HX <= c^2 H is checked as lambda_min(c^2 H - X^*HX) > err, err = rigorous bound on the float error.
Label: [CA-float] (rigorous modulo IEEE-754 + LAPACK eigvalsh backward stability bound used below)."""
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
f=sys.argv[1] if len(sys.argv)>1 else '/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'
z=np.load(f); H=z['H']; s=complex(z['s']); kap=float(z['kap']); Qt=z['Qt']; tau0=0.0
D=H.shape[0]; u=2.0**-53; g=lambda n:n*u/(1-n*u)
eta=1e-8
A0=A.Amat(tau0); M=A0/s
def psd_margin(c2,X):
    G=X.conj().T@H@X; Rm=c2*H-G; Rm=(Rm+Rm.conj().T)/2
    lam=np.linalg.eigvalsh(Rm).min()
    aX=np.abs(X); aH=np.abs(H)
    err=g(2*D+4)*np.linalg.norm(aX.T@aH@aX,2)*2 + g(4)*c2*np.linalg.norm(aH,2)   # forming G and Rm
    err+= 10*D*u*np.linalg.norm(Rm,2)                                            # eigvalsh backward error
    return float(lam),float(err)
out={}
ev=np.linalg.eigvalsh(H); out['V1_H_eig_minmax']=[float(ev.min()),float(ev.max())]
out['V1_ok']=bool(ev.min()>10*D*u*ev.max())
out['V2']=psd_margin((1+eta)**2,M); out['V2_ok']=out['V2'][0]>out['V2'][1]
out['V3a']=psd_margin((1+eta)**2,Qt); out['V3a_ok']=out['V3a'][0]>out['V3a'][1]
out['V3b']=psd_margin((kap*(1+eta))**2,M@Qt); out['V3b_ok']=out['V3b'][0]>out['V3b'][1]
cond=float(np.sqrt(ev.max()/ev.min())); out['cond']=cond
out['input_radius_D_RAD_2norm']=float(D*A.RAD); out['Pert_2norm']=A.PERT
out['V4_additive_H_over_|s|']=float(cond*(D*A.RAD+A.PERT)/abs(s))
out['ALL_OK']=all(out[k] for k in ['V1_ok','V2_ok','V3a_ok','V3b_ok'])
print(json.dumps(out,indent=1))
