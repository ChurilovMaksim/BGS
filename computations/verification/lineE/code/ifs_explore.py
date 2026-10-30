"""Galerkin sections of the IFS transfer operators L_a on H^2(D_rho) (exploration, double precision).
(L_a phi)(s) = sum_{|n|<=L} w_a(n) e(c n s) phi((s+n)/lam), w_a(n)=ghat(n) e(c n^2/2 + a n/8), c=1/(4 sqrt2)."""
import os; os.environ.setdefault('OPENBLAS_NUM_THREADS','2')
import numpy as np, sys
from scipy.special import jv, gammaln
lam=3+2*np.sqrt(2); c=1/(lam-1/lam)
def build(a,eta,L,rho,K):
    A=np.zeros((K,K),complex); l=np.arange(K)
    for n in range(-L,L+1):
        w=(1j)**n*jv(n,0.9*eta)*np.exp(2j*np.pi*(c*n*n/2+a*n/8))
        # M[l,j]=(2 pi i c n rho)^(l-j)/(l-j)!
        z=2j*np.pi*c*n*rho; d=l[:,None]-l[None,:]
        with np.errstate(all='ignore'):
            M=np.where(d>=0, np.exp(np.where(d>=0,d,0)*np.log(z+0j) if n!=0 else 0)-0, 0)
        if n==0: M=np.eye(K,dtype=complex)
        else:
            dd=np.where(d>=0,d,0); M=np.where(d>=0,np.exp(dd*np.log(z)-gammaln(dd+1)),0)
        # C[j,k]=binom(k,j) rho^j n^(k-j)/(lam rho)^k = binom(k,j) lam^-k (n/rho)^(k-j)
        kk=l[None,:]; jj=l[:,None]; e=kk-jj
        if n==0: C=np.diag(lam**(-l.astype(float))).astype(complex)
        else:
            ee=np.where(e>=0,e,0)
            logb=gammaln(kk+1)-gammaln(jj+1)-gammaln(ee+1)
            C=np.where(e>=0,np.exp(logb-kk*np.log(lam)+ee*np.log(abs(n)/rho))*np.sign(n)**ee,0)
        A+=w*(M@C)
    return A
if __name__=='__main__':
    eta=float(sys.argv[1]); L=int(sys.argv[2]); rho=float(sys.argv[3])
    for K in map(int,sys.argv[4].split(',')):
        out=[]
        for a in (0,2,4,6):
            ev=np.linalg.eigvals(build(a,eta,L,rho,K)); ev=ev[np.argsort(-abs(ev))]
            out.append((a,np.round(abs(ev[:4]),5).tolist(),complex(np.round(ev[0],6))))
        print('K',K,out,flush=True)
