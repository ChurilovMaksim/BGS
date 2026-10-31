"""N6: batched version of the L2 TW twisted transfer law (identical arithmetic, batch over beta)."""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineL/L2/code'); from twlaw import TW, mdata, lam_pows, taus_of, LAM
def Zbatch(tw,T):
    T=np.asarray(T,float); B,m=T.shape; K,S=tw.K,tw.S
    X=np.zeros((B,S,K,K),complex); X[:,0]=np.eye(K)
    for step in range(m):
        Y=np.zeros_like(X); t=T[:,step]
        for n in tw.ns:
            c=np.exp(2j*np.pi*n*t)                       # (B,)
            contrib=np.matmul(tw.Mn[n][None],X)*(tw.ph[n][None,:,None,None]*c[:,None,None,None])
            Y[:,tw.tgt[n]]+=contrib
        X=Y
    return (1-LAM**(-m))*np.einsum('bsii->b',X)
def nu_rho(m,sg=1):
    d=mdata(m); h=d['h']; M=2*h
    x0=(sg*pow(4,-1,M//2))%(M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1); assert (8*nu0-2*sg)%M==0
    return h,nu0
