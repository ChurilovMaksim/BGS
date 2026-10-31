"""[N] precision check: double vs longdouble twisted traces, and K=32 vs K=40."""
import sys; sys.path.insert(0,'/workspace/audit/lineL/L2rerun/code'); from twlaw import *
import numpy as np
m=int(sys.argv[1]); q=int(sys.argv[2])
d=mdata(m); M=2*d['h']; x0=pow(4,-1,M//2); nu0=min(x for x in (x0,x0+M//2) if x%2==1)
pw=lam_pows(m,q); s=next(x for x in range(q) if (x*x-2)%q==0)
betas=[(s,1),((3*s)%q,3),(1,0),(5,7)]
for K in (32,40):
    tw=TW(m,nu0,L=8,K=K)
    out=[]
    for b in betas: out.append(tw.Z(taus_of(b,pw,q)))
    # longdouble
    tw.Mn={n:v.astype(np.clongdouble) for n,v in tw.Mn.items()}
    tw.ph={n:v.astype(np.clongdouble) for n,v in tw.ph.items()}
    out2=[]
    for b in betas:
        tau=taus_of(b,pw,q)
        X=np.zeros((tw.S,K,K),np.clongdouble); X[0]=np.eye(K)
        for step in range(m):
            Y=np.zeros_like(X); t=np.longdouble(tau[step])
            for n in tw.ns:
                c=np.exp(np.clongdouble(2j)*np.pi*n*t)
                Y[tw.tgt[n]]+=np.einsum('ij,sjk->sik',tw.Mn[n],X)*(tw.ph[n]*c)[:,None,None]
            X=Y
        out2.append((1-LAM**(-m))*np.trace(X.sum(axis=0)))
    for b,z,z2 in zip(betas,out,out2): print(m,q,K,b,'dbl %.6e'%abs(z),'ld %.6e'%abs(z2),'rel %.1e'%(abs(z-z2)/max(abs(z2),1e-300)),flush=True)
