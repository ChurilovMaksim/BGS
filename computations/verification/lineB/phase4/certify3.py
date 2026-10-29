"""Rigorous certificate v3 (resolvent test vector).  For eta in [e0,e1] and a in {0,1,2,3}:
   find v>0 on Z^2 with (A_a v)(s) <= rho v(s) for all s, A_a the tilted majorant (REPORT4 §1); then for odd m
   Tr(A_a^m) <= rho^(m-1) * sum_s (A_a v)(s)/v(s) <= Cst*rho^(m-1),   |chi_m(eta)| <= sum_a Tr(A_a^m).
 v on box S_K2: solution of (rho_t I - A_in) v = rho_t*phi + b_out (+dropped mass), phi = theta e^{-kappa N};
 v = C e^{-kappa N} outside S_K2.  All inequalities re-verified a posteriori in rigorous float (SAFE)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, math, time, json; sys.path.insert(0,'.')
import numpy as np, scipy.sparse as sp, scipy.sparse.linalg as spl
from wcoef import BETA, what_arb
from transfer import *
from certify import bounds, remainder_mass, lattice_tail, SAFE
def build_box(K2,a,nn,ww,beta,C,kappa):
    P,Q,Nv,R=box_states(K2); S=len(P); W=2*R+1
    idx=-np.ones((W,W),np.int64); idx[P+R,Q+R]=np.arange(S)
    damp=np.exp(-beta*G0_SAFE*Nv); rows=[];cols=[];vals=[]; bout=np.zeros(S)
    for nv,w in zip(nn,ww):
        p2=Q; q2=6*Q-P+a-nv
        ok=(np.abs(p2)<=R)&(np.abs(q2)<=R)
        j=np.full(S,-1); j[ok]=idx[p2[ok]+R,q2[ok]+R]; inb=j>=0
        rows.append(np.flatnonzero(inb)); cols.append(j[inb]); vals.append(damp[inb]*w)
        if (~inb).any():
            N2=Ncoord(p2[~inb].astype(float),q2[~inb].astype(float))-1e-9
            bout[~inb]+=damp[~inb]*w*C*np.exp(-kappa*N2)
    A=sp.csr_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(S,S))
    return A,bout,damp,(P,Q,Nv)
def cert_one(e0,e1,a,n,b,rem,beta,kappa,Kmid,x2,theta=1e-2,Cfac=3.0,Vg=50.0,delta=None,iters=80,pit=400,rfloor=0.0,dbg=False):
    tilt=np.exp(beta*CC_SAFE*np.abs(n-a)); ww_all=b*tilt
    keep=ww_all>1e-40; drop=float(ww_all[~keep].sum())+rem*math.exp(3*(beta+kappa)*CC_SAFE)
    nn,ww=n[keep],ww_all[keep]
    K2=LAM*(Kmid+CC_SAFE*x2)+1
    A,bunit,damp,(P,Q,Nv)=build_box(K2,a,nn,ww,beta,1.0,kappa)
    # float Perron estimate on the whole box: power iteration from padded core vector
    core=np.flatnonzero(Nv<=Kmid); Ac=A[core][:,core].toarray()
    ev,evec=np.linalg.eig(Ac); i=np.argmax(ev.real); vc=np.abs(evec[:,i].real)
    v0=np.zeros(len(P)); v0[core]=vc/vc.max(); v0+=1e-9
    ev,evv=spl.eigs(A,k=1,which='LM',v0=v0,tol=1e-14,maxiter=5000)
    v=np.abs(evv[:,0].real); v/=v.max(); r0=float(abs(ev[0]))
    if delta is None: delta=max(2e-6,0.03*(1-r0))
    rt=max(r0*(1+delta),rfloor)
    phi=theta*np.exp(-kappa*Nv); rin=np.inf; vp=v.copy()
    C=max(theta*Cfac,1.5*float(np.max((np.maximum(phi,vp)*np.exp(kappa*(Nv+1e-9)))[Nv>=Kmid])))
    for rnd in range(30):
        extra=C*bunit+damp*drop*Vg
        v=np.maximum(phi,vp)
        for it in range(iters): v=np.maximum(phi,(A@v+extra)/rt)
        Vmax=float(v.max()); Cact=float(np.max((v*np.exp(kappa*(Nv+1e-9)))[Nv>=Kmid]))
        if Cact<=C and Vmax<=Vg: break
        C=1.5*Cact
    Av=(A@v+C*bunit+damp*drop*Vg)*SAFE
    ratio=Av/v; rin=float(ratio.max())
    if dbg:
        j=int(np.argmax(ratio)); print('argmax N',Nv[j],'P,Q',P[j],Q[j],'v',v[j],'phi',phi[j],'Av',(A@v)[j],'bout',C*bunit[j],'dropterm',damp[j]*drop*Vg,'drop',drop,'iscore',v[j]>phi[j]*1.0000001)
    ok_V=Vmax<=Vg; ok_C=Cact<=C; info=rnd
    tau=(beta+kappa)*CC_SAFE
    Wp=float(np.sum(b*np.exp(tau*(np.abs(n)+3))))+drop
    big=np.abs(n-a)>=x2; Tx=float(np.sum(ww_all[big]))+drop
    xo=min((beta-kappa)*G0_SAFE,beta*G0_SAFE-kappa)
    rout=(math.exp(-(beta-kappa)*G0_SAFE*K2)*Wp+math.exp(-(beta*G0_SAFE-kappa)*K2)*Tx*Vg/C)*SAFE
    rho=max(rin,rout)
    const=float(ratio.sum())+(Wp+Tx*Vg/C)*lattice_tail(K2,xo)
    return dict(e0=e0,e1=e1,a=a,beta=beta,kappa=kappa,Kmid=Kmid,K2=K2,states=len(P),rho_float=r0,rho_t=rt,gmres=info,
                rho_in=rin,rho_out=rout,rho=rho,C=const,Vmax=Vmax,Cact=Cact,C_used=C,valid=bool(ok_V and ok_C))
def run(e0,e1,beta,kappa,Kmid,x2,**kw):
    n,b,b0,eps,tl=bounds(e0,e1); tau=(beta+kappa)*CC_SAFE
    rem=remainder_mass(b0,n,eps,tau)+tl*1e40
    r=[cert_one(e0,e1,0,n,b,rem,beta,kappa,Kmid,x2,**kw)]
    kw2=dict(kw); kw2['rfloor']=min(0.9,r[0]['rho_t'])
    return r+[cert_one(e0,e1,a,n,b,rem,beta,kappa,Kmid,x2,**kw2) for a in (1,2,3)]
if __name__=='__main__':
    for (e0,e1,Kmid,x2) in [(1,1.1,8,25),(10,10.5,12,40)]:
        t0=time.time(); res=run(e0,e1,0.1,0.05,Kmid,x2)
        for r in res: print({k:(float(f'{v:.7g}') if isinstance(v,float) else v) for k,v in r.items()},flush=True)
        print('time',round(time.time()-t0),flush=True)
