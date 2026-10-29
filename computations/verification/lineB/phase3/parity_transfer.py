"""Exact transfer-operator formula for the parity characteristic function (odd m):
chi_m(eta) := (1/D_eff) sum_{xi in supp} prod_j u(xi_j),  u(th)=exp(i eta (f(th)-f(-th))),   supp = 1/2*1 + V^_odd.
Poisson over the annihilator of V_2=<1>:  chi_m = sum_{a=0..3} sum_{k in Z^m} prod_j uhat(6k_j-k_{j-1}-k_{j+1}+a) * sign
=> chi_m = sum_a s_a Tr(M_a^m),  M_a[(p,q),(q,r)] = uhat(6q-p-r+a).   (states truncated |k|<=K; |k_j|<=max|n|/4).
Compare with direct sum over the support (m<=9) and give leading eigenvalues mu_a(eta)."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys; sys.path.insert(0,__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'..','phase2'))
from p2lib import *
def uhat(eta,L=1<<12):
    th=np.arange(L)/L; u=np.exp(1j*eta*(f_diag(th)-f_diag(-th))); c=np.fft.fft(u)/L
    return lambda n: c[np.asarray(n)%L]*(np.abs(np.asarray(n))<L//2)
def Mats(eta,K):
    uh=uhat(eta); ks=np.arange(-K,K+1); P,Q,R=np.meshgrid(ks,ks,ks,indexing='ij'); n0=6*Q-P-R
    S=len(ks); out=[]
    for a in range(4):
        M=np.zeros((S*S,S*S),complex); w=uh(n0+a)
        idx_from=(P+K)*S+(Q+K); idx_to=(Q+K)*S+(R+K)
        M[idx_from.ravel(),idx_to.ravel()]=w.ravel(); out.append(M)
    return out
def chi_transfer(eta,m,K,signs):
    return sum(s*np.trace(np.linalg.matrix_power(M,m)) for s,M in zip(signs,Mats(eta,K)))
def chi_direct(eta,m):
    O,supp=support_data(m); d1,d2=O.d1,O.d2
    i1=(-np.arange(d1))%d1; i2=(-np.arange(d2))%d2; Sn=O.S[i1][:,i2]
    return np.mean(np.exp(1j*eta*(O.S-Sn))[supp])
if __name__=='__main__':
    for sg in [(1,1,1,1),(1,-1,1,-1)]:
        e1=chi_transfer(3.0,3,6,sg); print('sign pattern',sg,'m=3 eta=3 transfer',e1,'direct',chi_direct(3.0,3))
