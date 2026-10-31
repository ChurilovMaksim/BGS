"""N12 shared: float sector-4 twisted operator A(d) = sum_n w_4(n) e(n d) M_n from Line F/N6 cert_core arb blocks (mid->float,
max entry radius recorded). Imported by other N12 scripts. Caches to logs/a_ops.npz."""
import sys, os, numpy as np, math
CACHE='/workspace/bgs-lineN/N12/logs/a_ops.npz'
if os.path.exists(CACHE):
    z=np.load(CACHE,allow_pickle=True); NS=z['NS']; MS=z['MS']; COEF0=z['COEF0']; D=int(z['D']); RAD=float(z['RAD']); XN=float(z['XN']); PERT=float(z['PERT'])
else:
    sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
    import cert_core as C
    from flint import arb
    import json
    nc=json.load(open('/workspace/bgs-lineN/N6/logs/n_cert.json'))
    D=C.D; K=C.K; ns=sorted(set(n for (c2,n) in C.blocks)); NS=np.array(ns)
    MS=np.zeros((len(ns),D,D),complex); COEF0=np.zeros(len(ns),complex); RAD=0.0
    for (c2,n),(j2,Mx) in C.blocks.items():
        k=ns.index(n); i0=C.idx[c2]*K; j0=C.idx[j2]*K
        for i in range(K):
            for j in range(K):
                z=Mx[i,j]; MS[k,i0+i,j0+j]+=complex(float(z.real.mid()),float(z.imag.mid()))
                RAD=max(RAD,float(z.real.rad())+float(z.imag.rad()))
    for k,n in enumerate(ns):
        w=C.wa(4,n); COEF0[k]=complex(float(w.real.mid()),float(w.imag.mid()))
    XN=float(C.Xn.upper()); PERT=float(nc['Pert'])
    np.savez(CACHE,NS=NS,MS=MS,COEF0=COEF0,D=D,RAD=RAD,XN=XN,PERT=PERT)
def Amat(d):
    c=COEF0*np.exp(2j*np.pi*NS*d)
    return np.tensordot(c,MS,1)
def spectral(d=0.0):
    A0=Amat(d); ev,R=np.linalg.eig(A0); i=np.argmax(abs(ev)); s=ev[i]; Phi=R[:,i]
    evl,Lv=np.linalg.eig(A0.T); psi=Lv[:,np.argmin(abs(evl-s))]
    # refine by inverse iteration (shift slightly off s) and Rayleigh quotient
    M=A0-(s+1e-7)*np.eye(A0.shape[0])
    for _ in range(3):
        Phi=np.linalg.solve(M,Phi); Phi/=np.linalg.norm(Phi)
        psi=np.linalg.solve(M.T,psi); psi/=np.linalg.norm(psi)
    s=(psi@A0@Phi)/(psi@Phi)
    Phi=Phi/np.linalg.norm(Phi); psi=psi/(psi@Phi)
    return A0,s,Phi,psi
