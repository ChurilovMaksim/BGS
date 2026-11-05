"""Fast batched evaluation of the L2/N6 twisted transfer law Zhat(beta) (same arithmetic as twb.Zbatch:
one GEMM over all letters + permutation scatter). Validated against twb.Zbatch in selftest()."""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineN/N6/code')
from twb import TW, Zbatch, nu_rho, mdata, lam_pows, taus_of, LAM
class Fast:
    def __init__(s,tw):
        s.tw=tw; s.K=tw.K; s.S=tw.S; s.ns=list(tw.ns); s.m=tw.m
        s.Mall=np.concatenate([tw.Mn[n] for n in s.ns],axis=0)       # (nL*K, K)
        s.inv=[np.argsort(tw.tgt[n]) for n in s.ns]                  # Y[tgt[s]] += f(s)  <=> Y[s'] += f(inv[s'])
        s.ph=np.array([tw.ph[n][s.inv[i]] for i,n in enumerate(s.ns)]) # (nL,S) phase at source state, indexed by target
        s.nar=np.array(s.ns,float)
    def Z(s,T):
        T=np.asarray(T,float); B,m=T.shape; K,S,nL=s.K,s.S,len(s.ns)
        X=np.zeros((K,B,S,K),complex); X[:,:,0,:]=np.eye(K)[:,None,:]
        for step in range(m):
            G=(s.Mall@X.reshape(K,-1)).reshape(nL,K,B,S,K)
            c=np.exp(2j*np.pi*s.nar[:,None]*T[None,:,step])            # (nL,B)
            Y=np.zeros_like(X)
            for i in range(nL):
                Y+=G[i][:,:,s.inv[i],:]*(s.ph[i][None,None,:,None]*c[i][None,:,None,None])
            X=Y
        return (1-LAM**(-m))*np.einsum('ibsi->b',X)
def selftest(m=15,B=8,K=16):
    h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=K); f=Fast(tw)
    T=np.random.default_rng(1).random((B,m)); T[0]=0
    a=Zbatch(tw,T); b=f.Z(T)
    return float(np.max(np.abs(a-b))/np.max(np.abs(a)))
if __name__=='__main__':
    import time
    print('selftest rel err',selftest())
    m=int(sys.argv[1]); B=int(sys.argv[2])
    h,nu0=nu_rho(m,1); tw=TW(m,nu0,L=8,K=16); f=Fast(tw)
    T=np.random.rand(B,m); t=time.time(); f.Z(T); print('fast sec/beta',(time.time()-t)/B)
