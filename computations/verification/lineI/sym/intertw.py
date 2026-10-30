"""Search intertwiners between the finite monomial factors of different G2 (±2,8) cases (d=7 relevant m).
Linear:     X A_n(base) = A_n(case) X            for n mod 8   (same a: H-part identical)
Antilinear: X (-1)^n conj(A_n(base)) = A_n(case) X  (relates a=2 to a=-2 via complex conjugation of H-part)"""
import sys, numpy as np
sys.path.insert(0,'/workspace/bgs-lineI/cert')
from gstates import g2params, reach, finite
def mats(m,a):
    P=g2params(m,a,8); idx,tg=reach(P,8); A=[]
    for n in range(8):
        M=np.zeros((16,16),complex)
        for (o,i,ph8,tw) in finite(P,idx,tg,n,None): M[o,i]+=np.exp(-2j*np.pi*ph8/8)
        A.append(M)
    return A,P,idx
def nullsp(As,Bs):
    I=np.eye(16); rows=[np.kron(I,B)-np.kron(A.T,I) for A,B in zip(As,Bs)]  # vec(B X - X A) column-major: (I⊗B - A^T⊗I) vec X
    s,v=np.linalg.svd(np.vstack(rows))[1:]
    k=(s<1e-9).sum(); return k, v[-k:].conj() if k else None
base,P0,i0=mats(9,2)
for m in (9,15,21,27):
  for a in (2,-2):
    A,P,idx=mats(m,a)
    k1,_=nullsp(base,A)
    k2,_=nullsp([((-1)**n)*base[n].conj() for n in range(8)],A)
    print(m,a,P['k'],P['psi0'],P['psi1'],'linear intertwiner dim',k1,'antilinear dim',k2,flush=True)
