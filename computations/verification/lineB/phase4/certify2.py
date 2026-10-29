"""Rigorous certificate (v2):  for eta in [e0,e1], odd m:  |chi_m(eta)| <= sum_{a=0..3} Tr(A_a^m) <= sum_a Cst_a * rho_a^(m-1).
Test vector: v = max(v_perron, theta e^{-kappa N}) for N<Kc, v = theta e^{-kappa N} for N>=Kc; ratio (Av)/v checked EXACTLY
(rigorous float, nonnegative sums, SAFE factor) on the big box S_K2; analytic bound outside S_K2 (successors landing in the core
N<Kc need |n-a| >= (N(s)/lam - Kc)/c).  See REPORT4 §1 for the proof."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, math, time, json; sys.path.insert(0,'.')
import numpy as np, flint
from wcoef import BETA, what_arb
from transfer import *
from certify import bounds, remainder_mass, lattice_tail, SAFE
def Av_matfree(P,Q,Nv,idxmap,R,a,nn,ww,beta,v,theta,kappa,K2):
    """(A v)(s) for all box states, successors outside the box bounded by theta e^{-kappa N(s')}."""
    damp=np.exp(-beta*G0_SAFE*Nv); acc=np.zeros(len(P))
    for nv,w in zip(nn,ww):
        p2=Q; q2=6*Q-P+a-nv
        ok=(np.abs(p2)<=R)&(np.abs(q2)<=R)
        j=np.full(len(P),-1); j[ok]=idxmap[p2[ok]+R,q2[ok]+R]
        val=np.empty(len(P)); inb=j>=0; val[inb]=v[j[inb]]
        if (~inb).any():
            N2=Ncoord(p2[~inb].astype(float),q2[~inb].astype(float))-1e-9
            val[~inb]=theta*np.exp(-kappa*N2)
        acc+=w*val
    return damp*acc
def cert_one(e0,e1,a,n,b,rem,beta,kappa,Kc,x2,log,theta_in=1e-3):
    tau=(beta+kappa)*CC_SAFE
    tilt=np.exp(beta*CC_SAFE*np.abs(n-a)); ww_all=b*tilt
    keep=ww_all>1e-40; drop=float(ww_all[~keep].sum())+rem*math.exp(3*tau)
    nn,ww=n[keep],ww_all[keep]
    K=Kc
    A,om,(Pk,Qk,Nk)=build(K,a,nn,b[keep],beta); r0,vp=perron(A); vp=vp/vp.max()
    K2=LAM*(Kc+CC_SAFE*x2)+1
    P,Q,Nv,R=box_states(K2); W=2*R+1; idx=-np.ones((W,W),np.int64); idx[P+R,Q+R]=np.arange(len(P))
    v=theta_in*np.exp(-kappa*Nv); theta=theta_in
    jk=idx[Pk+R,Qk+R]; v[jk]=np.maximum(v[jk],vp)
    Vc=1.0  # v_p normalised to max 1; v<=max(v_p 1[N<=K], theta e^{-kappa N})
    Av=Av_matfree(P,Q,Nv,idx,R,a,nn,ww,beta,v,theta,kappa,K2)
    Av+=np.exp(-beta*G0_SAFE*Nv)*drop*max(Vc,theta)
    ratio=Av*SAFE/v; rin=float(ratio.max())
    Wp=float(ww_all.sum()*math.exp(kappa*CC_SAFE*3)) # >= sum b e^{(beta+kappa)c|n-a|}, |n-a|<=|n|+3 handled below
    Wp=float(np.sum(b*np.exp(tau*(np.abs(n)+3))))+drop
    big=np.abs(n-a)>=x2
    Tx=float(np.sum((b*np.exp(beta*CC_SAFE*np.abs(n-a)))[big]))+drop
    rout=(math.exp(-(beta-kappa)*G0_SAFE*K2)*Wp+math.exp(-(beta*G0_SAFE-kappa)*K2)*Tx*Vc/theta)*SAFE
    rho=max(rin,rout)
    const=float(ratio.sum())+(Wp+Tx*Vc/theta)*lattice_tail(K2,min((beta-kappa)*G0_SAFE,beta*G0_SAFE-kappa))
    return dict(e0=e0,e1=e1,a=a,beta=beta,kappa=kappa,Kc=Kc,K2=K2,states=len(P),rho_float=r0,rho_in=rin,rho_out=rout,rho=rho,C=const,theta=theta)
def run(e0,e1,beta,kappa,Kc_list,x2,theta=1e-3):
    n,b,b0,eps,tl=bounds(e0,e1); tau=(beta+kappa)*CC_SAFE
    rem=remainder_mass(b0,n,eps,tau)+tl*1e40
    return [cert_one(e0,e1,a,n,b,rem,beta,kappa,Kc_list[a],x2,None,theta) for a in range(4)]
if __name__=='__main__':
    for th in [1e-2,1e-3,1e-4,1e-6]:
        t0=time.time(); res=run(1,1.1,0.1,0.05,[16]*4,40,th)
        print('theta',th,' '.join(f"a={r['a']}:rho_in={r['rho_in']:.6f},out={r['rho_out']:.2e},float={r['rho_float']:.6f},C={r['C']:.1e}" for r in res),f'{time.time()-t0:.0f}s',flush=True)
