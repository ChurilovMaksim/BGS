"""Referee re-check of N14 rate certificate K(Y_c) <= rb*Y_c (rb=0.28): own block-sparse K in float64 AND in extended precision
(clongdouble, ~1e-19) to measure the actual rounding error vs N14's a-priori E_round; lambda_min(W) by eigvalsh and by a
Cholesky of W - sigma I with residual check (extended precision residual)."""
import os; os.environ['OMP_NUM_THREADS']='1'
import sys, json, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
z=np.load('/workspace/bgs-lineN/N12/logs/adapted_norm_t0.0_k0.45.npz'); s=complex(z['s'])
Yc=np.load('/workspace/bgs-lineN/N14/logs/b_cp2_Yc_0.28.npz')['Yc']; D=A.D; K=55; NB=D//K; rb=0.28
bl=[]
for k in range(len(A.NS)):
    for ib in range(NB):
        for jb in range(NB):
            B=A.MS[k][ib*K:(ib+1)*K,jb*K:(jb+1)*K]
            if np.abs(B).max()>0: bl.append((k,ib,jb,B))
def Kop(Y,dt):
    c=(np.array(A.COEF0)/s).astype(dt); Y=Y.astype(dt); out=np.zeros((D,D),dt)
    for k in range(len(A.NS)):
        bk=[(ib,jb,B.astype(dt)) for kk,ib,jb,B in bl if kk==k]
        if not bk: continue
        T=np.zeros((D,D),dt)
        for ib,jb,B in bk: T[ib*K:(ib+1)*K,:]+=B@Y[jb*K:(jb+1)*K,:]
        Z=np.zeros((D,D),dt)
        for ib,jb,B in bk: Z[:,ib*K:(ib+1)*K]+=T[:,jb*K:(jb+1)*K]@B.conj().T
        out+=(c[k]*np.conj(c[k]))*Z
    return (out+out.conj().T)/2
K64=Kop(Yc,np.complex128); W=rb*Yc-K64; W=(W+W.conj().T)/2
lmin=float(np.linalg.eigvalsh(W).min())
KL=Kop(Yc,np.clongdouble)
round_err=float(np.linalg.norm((K64.astype(np.clongdouble)-KL).astype(np.complex128),2))
WL=(rb*Yc.astype(np.clongdouble)-KL); WL=(WL+WL.conj().T)/2
sig=lmin/2; L=np.linalg.cholesky(W-sig*np.eye(D))
Rres=WL-sig*np.eye(D,dtype=np.clongdouble)-L.astype(np.clongdouble)@L.conj().T.astype(np.clongdouble)
resF=float(np.sqrt((np.abs(Rres)**2).sum()))
ev=np.linalg.eigvalsh((Yc+Yc.conj().T)/2)
out=dict(lmin_W=lmin,actual_round_err_K=round_err,N14_claim_lmin=3.49e-6,sigma=sig,chol_residual_frob_ext=resF,cert_by_chol=resF<sig,
         Yc_min_eig=float(ev.min()),Yc_posdef=bool(ev.min()>0),cond=float(ev.max()/ev.min()))
print(out); json.dump(out,open('logs/ref_cp_cert.json','w'),indent=1)
