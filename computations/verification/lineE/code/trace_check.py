"""Check: brute-force n-sum Z_L(m) at nu* (Line B phase, exact integers mod g')  ==  sum_a c_a (1-lam^-m) sum_k mu_{a,k}^m (Galerkin eigenvalues)."""
import numpy as np, itertools, sys
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from scipy.special import jv
from pell import data, xy
from resid import nustar, check
from ifs_explore import build
lam=3+2*np.sqrt(2)
def brute(m,eta,L):
    d=data(m); gp,yp=d['gp'],d['yp']; nu,_=nustar(m)
    vals=np.arange(-L,L+1); g=(1j)**vals*jv(vals,0.9*eta)
    X=np.array([[xy(abs(i-j))[0] for j in range(m)] for i in range(m)],dtype=np.int64)
    grid=np.array(list(itertools.product(range(2*L+1),repeat=m)),dtype=np.int64); nv=vals[grid]
    Nm=np.einsum('ki,ij,kj->k',nv,X,nv)   # exact in int64 for these sizes
    ph=((-nu*yp*Nm)%gp)/gp
    return np.sum(np.prod(g[grid],axis=1)*np.exp(2j*np.pi*ph))
def galerkin(m,eta,L,rho=2.0,K=80):
    kap=check(m)['kap8']
    cs=[np.mean([np.exp(2j*np.pi*(kap*b*b-a*b)/8) for b in range(8)]) for a in range(8)]
    Z=0
    for a in range(8):
        if abs(cs[a])<1e-12: continue
        ev=np.linalg.eigvals(build(a,eta,L,max(rho,1.05*L/(lam-1)),K))
        Z+=cs[a]*(1-lam**(-m))*np.sum(ev**m)
    return Z
for (m,L) in ((5,4),(5,6),(7,3),(7,4)):
    zb=brute(m,2.0,L); zg=galerkin(m,2.0,L)
    print(f'm={m} L={L} brute={zb:.10f} galerkin={zg:.10f} |diff|={abs(zb-zg):.2e}',flush=True)
