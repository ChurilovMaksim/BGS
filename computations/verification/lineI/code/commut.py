import numpy as np
from law import kick_ghat
from twist import build
gh=kick_ghat('k1',2.0,10)
for m in (9,15,21,27):
  for ab in ((2,8),(-2,8)):
    parts,nu,S=build(m,*ab,gh,2.6,4)
    Ps=[P for n,(Mn,P) in parts.items()]
    # commutant: X P = P X  -> (I kron P^T ... ) solve via vec
    I=np.eye(S); rows=[np.kron(I,P)-np.kron(P.T,I) for P in Ps]  # vec(PX - XP) with column-major
    A=np.vstack(rows); sv=np.linalg.svd(A,compute_uv=False); cdim=int((sv<1e-9).sum())
    # reachable subspace from e0 and co-reachable from 1
    def krylov(v,mats):
        B=[v/np.linalg.norm(v)]; Q=np.array(B).T
        changed=True
        while changed:
            changed=False
            for P in mats:
                W=P@Q
                for w in W.T:
                    w=w-Q@(Q.conj().T@w)
                    if np.linalg.norm(w)>1e-9: Q=np.column_stack([Q,w/np.linalg.norm(w)]); changed=True
        return Q.shape[1]
    e0=np.zeros(S,complex); e0[0]=1; one=np.ones(S,complex)
    r=krylov(e0,Ps); c=krylov(one,[P.conj().T for P in Ps])
    print(m,ab,'commutant dim',cdim,'reachable',r,'coreachable',c,flush=True)
