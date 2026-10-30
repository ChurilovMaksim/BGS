"""Tilted positive transfer matrix A_a (see REPORT4 §1):  state s=(p,q) in Z^2, transition s -> Ts+(0,a-n), T(p,q)=(q,6q-p),
weight  exp(-beta*g0*N(s)) * b(n) * exp(beta*c*|n-a|),  N(s)=|u|+|t| eigen-coordinates of T.
Cycle inequality: gamma0*sum N(s_j) <= c*sum |n_j-a|  (L=|u|-|t| Lyapunov),  gamma0=1-1/lam, c=1/(2 sqrt2)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, math, scipy.sparse as sp
LAM=3+2*math.sqrt(2); G0=1-1/LAM; CC=1/(2*math.sqrt(2))
G0_SAFE=0.8284; CC_SAFE=0.35356        # G0_SAFE < 1-1/lam = 0.828427..., CC_SAFE > 0.353553...
def Ncoord(p,q):
    den=LAM-1/LAM; u=(q-p/LAM)/den; t=(LAM*p-q)/den
    return np.abs(u)+np.abs(t)
def box_states(K):
    R=int(math.ceil(LAM*K))+2; P,Q=np.meshgrid(np.arange(-R,R+1),np.arange(-R,R+1),indexing='ij')
    Nv=Ncoord(P.astype(float),Q.astype(float))-1e-9      # lower bound on N(s) (float error << 1e-9)
    sel=Nv<=K; return P[sel],Q[sel],Nv[sel],R
def build(K, a, nvals, bvals, beta):
    """sparse A on box S_K (transitions leaving the box dropped; returned separately as out-mass)."""
    P,Q,Nv,R=box_states(K); S=len(P); W=2*R+1
    idx=-np.ones((W,W),np.int64); idx[P+R,Q+R]=np.arange(S)
    wt=bvals*np.exp(beta*CC_SAFE*np.abs(nvals-a))
    rows=[];cols=[];vals=[]; outmass=np.zeros(S)
    damp=np.exp(-beta*G0_SAFE*Nv)
    for n,w in zip(nvals,wt):
        p2=Q; q2=6*Q-P+a-n
        ok=(np.abs(p2)<=R)&(np.abs(q2)<=R)
        j=np.full(S,-1); j[ok]=idx[p2[ok]+R,q2[ok]+R]
        inb=j>=0
        rows.append(np.flatnonzero(inb)); cols.append(j[inb]); vals.append(damp[inb]*w)
        outmass[~inb]+=damp[~inb]*w
    A=sp.csr_matrix((np.concatenate(vals),(np.concatenate(rows),np.concatenate(cols))),shape=(S,S))
    return A,outmass,(P,Q,Nv)
def perron(A,it=5000,tol=1e-14):
    v=np.ones(A.shape[0])
    for i in range(it):
        w=A@v; w/=w.max()
        if np.max(np.abs(w-v))<tol: v=w; break
        v=w
    w=A@v; m=v>0; return float(np.max(w[m]/v[m])), v
