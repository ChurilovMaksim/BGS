"""Auditor's independent transfer-operator code (collocation/FFT construction, NOT the author's binomial Galerkin).
(L_a phi)(s) = sum_{|n|<=L} ghat(n) e(c n^2/2 + a n/8) e(c n s) phi((s+n)/lam) on H^2(D_rho).
Matrix in basis (s/rho)^k, k<K, built by evaluating L_a e_k on M points of |s|=rho and FFT -> Taylor coefficients."""
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import numpy as np, math, cmath, sys
sys.path.insert(0,'.')
from aud import data, nustar, ghat, K1
LAM=3+2*math.sqrt(2); C0=1/(LAM-1/LAM)
def kappa(m):
    d=data(m); h=d['h']; nu=nustar(m); k=(-4*nu-1)//h; return (k*d['yp'])%8
def ca(kap,a): return sum(cmath.exp(2j*math.pi*(kap*b*b-a*b)/8) for b in range(8))/8
def build(G,a,L,rho,K,c=C0,M=None):
    M=M or 2*K+64
    s=rho*np.exp(2j*np.pi*np.arange(M)/M)
    vals=np.zeros((M,K),complex)
    for n in range(-L,L+1):
        w=G.get(n,0)*np.exp(2j*np.pi*(c*n*n/2+a*n/8))
        if w==0: continue
        t=(s+n)/(LAM*rho)                       # e_k((s+n)/lam) = t^k
        vals+=(w*np.exp(2j*np.pi*c*n*s))[:,None]*t[:,None]**np.arange(K)[None,:]
    coef=np.fft.fft(vals,axis=0)/M              # coefficient of s^j * rho^j  -> basis e_j
    return coef[:K,:]
def spectra(G,L,rho,K,c=C0):
    return {a:np.linalg.eigvals(build(G,a,L,rho,K,c)) for a in range(0,8,2)}
def Zpred(m,sp,kap=None):
    kap=kappa(m) if kap is None else kap
    return (1-LAM**(-m))*sum(ca(kap,a)*np.sum(sp[a]**m) for a in sp)
if __name__=='__main__':
    eta=float(sys.argv[1]); L=int(sys.argv[2]); rho=float(sys.argv[3]); K=int(sys.argv[4])
    G=ghat(K1,eta); sp=spectra(G,L,rho,K)
    for a in sp:
        e=sp[a][np.argsort(-abs(sp[a]))]; print('a',a,'top |mu|',np.round(abs(e[:5]),8).tolist(),'mu0',complex(np.round(e[0],8)))
