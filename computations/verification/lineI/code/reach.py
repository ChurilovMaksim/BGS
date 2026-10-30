import numpy as np
from law import kick_ghat
from twist import build
gh=kick_ghat('k1',2.0,10)
def krylov(v,mats):
    Q=(v/np.linalg.norm(v))[:,None]; k=0
    while True:
        W=np.column_stack([P@Q for P in mats])
        Qn,_=np.linalg.qr(np.column_stack([Q,W]))
        s=np.linalg.svd(np.column_stack([Q,W]),compute_uv=False); r=int((s>1e-8*s[0]).sum())
        if r==Q.shape[1]: return r
        U,sv,_=np.linalg.svd(np.column_stack([Q,W]),full_matrices=False); Q=U[:,:r]
for m in (9,15):
  for ab in ((2,8),(-2,8)):
    parts,nu,S=build(m,*ab,gh,2.6,4)
    Ps=[P for n,(Mn,P) in parts.items()]
    e0=np.zeros(S,complex); e0[0]=1; one=np.ones(S,complex)
    print(m,ab,'reachable',krylov(e0,Ps),'coreachable',krylov(one,[P.conj().T for P in Ps]),flush=True)
