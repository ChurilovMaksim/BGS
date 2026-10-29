"""Independent core for the audit (written from the definitions of phase-1 Thm 3 / Prop R; no project code used).
G = H^{-1}Z^m/Z^m, V = Z^m/HZ^m, Q(beta) = 2 beta^T H^{-1} beta mod 1, k_nu(xi) = D^{-1} sum_beta e(-nu Q(beta) - <beta,xi>),
Z(nu;eta) = sum_xi k_nu(xi) e^{i eta S(xi)},  S(xi) = sum_j f(xi_j),  f(t) = sum_k c_k e(k t)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, cypari2, math
from fractions import Fraction as Fr
pari = cypari2.Pari()
# exact l=0 kick coefficients (c_k for k>0; c_{-k}=conj)
CK = {1:(Fr(1,20),Fr(-1,200)), 2:(Fr(0),Fr(-1,400)), 5:(Fr(0),Fr(-1,800)), 6:(Fr(-1,40),Fr(-1,400)),
      7:(Fr(9,20),Fr(0)), 8:(Fr(-1,40),Fr(1,400)), 9:(Fr(0),Fr(1,800))}
def ck_complex():
    d={}
    for k,(a,b) in CK.items():
        d[k]=complex(a,b); d[-k]=complex(a,-b)
    return d
def ftab(M):
    """f(n/M), n=0..M-1 (real)"""
    n=np.arange(M); out=np.zeros(M)
    for k,c in ck_complex().items(): out+= (c*np.exp(2j*np.pi*k*n/M)).real
    return out
def uodd_tab(M):
    """u(t)=f(t)-f(-t) on n/M"""
    t=ftab(M); return t-t[(-np.arange(M))%M]
def Hmat(m):
    H=[[0]*m for _ in range(m)]
    for i in range(m):
        H[i][i]+=6; H[i][(i+1)%m]-=1; H[i][(i-1)%m]-=1
    return H
def hm(m):
    a,b,c,d=1,0,0,1
    for _ in range(m): a,b,c,d=3*a+2*b,4*a+3*b,3*c+2*d,4*c+3*d
    return a+d-2   # D_m = Tr S^m - 2
class Model:
    def __init__(self,m):
        self.m=m; H=pari.matrix(m,m,[x for r in Hmat(m) for x in r])
        D=int(pari.matdet(H)); self.D=abs(D)
        U,Vt,Dg=pari.matsnf(H,1)   # U*H*V = Dg
        diag=[int(Dg[i,i]) for i in range(m)]
        idx=[i for i in range(m) if abs(diag[i])!=1]
        self.e=[abs(diag[i]) for i in idx]; self.idx=idx
        assert np.prod(self.e)==self.D
        Vm=[[int(Vt[i,j]) for j in range(m)] for i in range(m)]
        # xi = V (s/e) ; beta = V^{-T} b  =>  beta.xi = sum b_i s_i/e_i  (H symmetric)
        Vinv=pari.matsolve(Vt,pari.matid(m))
        VinvT=[[int(Vinv[j,i]) for j in range(m)] for i in range(m)]
        adj=pari.matadjoint(H)*(1 if D>0 else -1)   # adj with H^{-1} = adj/Dabs
        self.cols=[[VinvT[r][i] for r in range(m)] for i in idx]   # beta = sum b_i * col_i
        adjl=[[int(adj[i,j]) for j in range(m)] for i in range(m)]
        A=[[sum(self.cols[a][i]*adjl[i][j]*self.cols[b][j] for i in range(m) for j in range(m)) for b in range(len(idx))] for a in range(len(idx))]
        self.A=A   # Q(b) = 2 b^T A b / D mod 1
        self.Vxi=[[Vm[j][i] for i in idx] for j in range(m)]  # xi_j = sum_i Vxi[j][i] s_i/e_i
        x,y=1,0
        for _ in range(m): x,y=3*x+8*y,x+3*y
        g=math.gcd(y,x-1); self.gp=(x-1)//g; self.yp=y//g
        self.units=[v for v in range(1,self.gp) if math.gcd(v,self.gp)==1]
    def grids(self):
        e=self.e; L=math.lcm(*e)
        assert all(L%ei==0 for ei in e)
        S=np.meshgrid(*[np.arange(ei,dtype=np.int64) for ei in e],indexing='ij')
        seq=np.zeros((self.m,)+tuple(e),dtype=np.int64)   # numerator of xi_j over L
        for j in range(self.m):
            acc=np.zeros(tuple(e),dtype=np.int64)
            for i,ei in enumerate(e): acc=(acc+ (self.Vxi[j][i]%L)*(L//ei)%L*S[i])%L
            seq[j]=acc
        Q=np.zeros(tuple(e),dtype=np.int64); D=self.D
        for a in range(len(e)):
            for b in range(len(e)):
                Q=(Q+ (S[a]*S[b]%D)*(2*self.A[a][b]%D))%D
        return seq,Q,L
