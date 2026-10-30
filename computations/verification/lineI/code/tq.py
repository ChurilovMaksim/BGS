import numpy as np, time, scipy.sparse.linalg as ssl
from law import kick_ghat
from twist import build
gh=kick_ghat('k1',2.0,10); K=40
parts,nu,S=build(9,2,8,gh,2.6,K)
items=[(n,Mn,P) for n,(Mn,P) in parts.items()]
tg={n:(P!=0).argmax(axis=0) for n,Mn,P in items}; ph={n:P[tg[n],np.arange(S)] for n,Mn,P in items}
cnt=[0]
def apply(v,tau):
    X=v.reshape(K,S); Y=np.zeros_like(X)
    for n,Mn,P in items: Y[:,tg[n]]+=np.exp(2j*np.pi*n*tau)*(Mn@X)*ph[n][None,:]
    return Y.ravel()
t=time.time()
A=ssl.LinearOperator((K*S,K*S),matvec=lambda v:(cnt.__setitem__(0,cnt[0]+1),apply(v,0))[1],dtype=complex)
ev=ssl.eigs(A,k=6,which='LM',tol=1e-8,maxiter=3000,return_eigenvectors=False,ncv=40)
print(sorted(abs(ev))[::-1],cnt,time.time()-t)
