"""N14 shared: block-sparse float version of the N12 sector-4 operator A(d)=sum_n c_n e(n d) M_n (same data as N12/code/a_ops.py).
Blocks: D=495 = 9 cores x K=55. Each M_n has a few nonzero KxK blocks. step(v,d) = A(d)v/s in ~10x fewer flops than dense."""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N12/code'); import a_ops as A
D=A.D; K=55; NB=D//K
A0,s,Phi,psi=A.spectral()
_bl=[]
for k in range(len(A.NS)):
    M=A.MS[k]
    for ib in range(NB):
        for jb in range(NB):
            B=M[ib*K:(ib+1)*K, jb*K:(jb+1)*K]
            if np.abs(B).max()>0: _bl.append((k,ib,jb,B))
BK=np.array([b[0] for b in _bl]); BI=np.array([b[1] for b in _bl]); BJ=np.array([b[2] for b in _bl]); BB=np.array([b[3] for b in _bl])
NSf=A.NS.astype(float); C0=A.COEF0/s
def step(v,d):
    """v: (D,) or (D,m) -> A(d) v / s"""
    c=C0*np.exp(2j*np.pi*NSf*d)
    vb=v.reshape(NB,K,-1)
    y=np.einsum('bij,bjm->bim',BB,vb[BJ])*c[BK][:,None,None]
    out=np.zeros((NB,K,y.shape[2]),complex); np.add.at(out,BI,y)
    return out.reshape(v.shape)
def stepT(u,d):
    """row vector u -> u A(d)/s"""
    c=C0*np.exp(2j*np.pi*NSf*d)
    ub=u.reshape(NB,K,-1)
    y=np.einsum('bij,bim->bjm',BB,ub[BI])*c[BK][:,None,None]
    out=np.zeros((NB,K,y.shape[2]),complex); np.add.at(out,BJ,y)
    return out.reshape(u.shape)
def weight(ds):
    v=Phi.astype(complex)
    for d in ds: v=step(v,d)
    return complex(psi@v)
if __name__=='__main__':
    import time
    print('blocks',len(_bl),'of',len(A.NS)*NB*NB)
    rng=np.random.default_rng(1); ds=rng.uniform(-.5,.5,30)
    t=time.time(); w1=weight(ds); t1=time.time()-t
    v=Phi.astype(complex); t=time.time()
    for d in ds: v=A.Amat(d)@v/s
    w2=complex(psi@v); t2=time.time()-t
    print(w1,w2,abs(w1-w2),t1,t2)
def step_batch(V,ds):
    """V: (D,m) columns, ds: (m,) twist per column -> column-wise A(d_m) V[:,m] / s"""
    c=C0[:,None]*np.exp(2j*np.pi*NSf[:,None]*ds[None,:])     # (nk,m)
    vb=V.reshape(NB,K,-1)
    y=np.einsum('bij,bjm->bim',BB,vb[BJ])*c[BK][:,None,:]
    out=np.zeros((NB,K,V.shape[1]),complex); np.add.at(out,BI,y)
    return out.reshape(V.shape)
def weights_batch(seqs):
    """list of twist sequences -> array of psi prod X Phi ; sequences right-aligned with d=0 left padding (X(0)Phi=Phi)."""
    L=max(len(q) for q in seqs); m=len(seqs)
    Dm=np.zeros((L,m))
    for i,q in enumerate(seqs): Dm[L-len(q):,i]=q
    V=np.repeat(Phi[:,None].astype(complex),m,axis=1)
    for t in range(L): V=step_batch(V,Dm[t])
    return psi@V
