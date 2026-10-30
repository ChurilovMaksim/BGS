"""Numerical check of Theorem E1 in Line B conventions: Z_m(nu*) = sum_a c_a Tr T_a^m (range-R, alphabet L truncation)."""
import os; os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np, itertools, sys
from scipy.special import jv
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from resid import nustar, G, check
from pell import data
def ghat_k1(eta,L):  # g = exp(i*0.9*eta*cos 2 pi q): ghat(n) = i^n J_n(0.9 eta)
    n=np.arange(-L,L+1); return n,(1j)**n*jv(n,0.9*eta)
def cvec(kap):
    return np.array([np.mean([np.exp(2j*np.pi*(kap*b*b-a*b)/8) for b in range(8)]) for a in range(8)])
def ZTM(m,eta,R=2,L=6,limit=False,sign=1):
    n,w=ghat_k1(eta,L); K=len(n)
    c=check(m); kap=c['kap8']
    lam=3+2*2**.5
    Gd=[(1/(lam-1/lam))*lam**(-d) for d in range(R+1)] if limit else [float(G(m,d)) for d in range(R+1)]
    if limit: Gd[0]=1/(lam-1/lam)
    if sign==-1: Gd=[-g for g in Gd]; kap=(-kap)%8
    states=list(itertools.product(range(K),repeat=R)); idx={s:i for i,s in enumerate(states)}
    cs=cvec(kap); Z=0; rhos=[]
    for a in range(8):
        T=np.zeros((len(states),)*2,complex)
        for s in states:
            for q in range(K):
                x=n[q]; ph=Gd[0]*x*x/2+a*x/8+sum(Gd[d]*x*n[s[-d]] for d in range(1,R+1))
                T[idx[s],idx[s[1:]+(q,)]]=w[q]*np.exp(2j*np.pi*ph)
        ev=np.linalg.eigvals(T); rhos.append(float(max(abs(ev))))
        Z+=cs[a]*np.sum(ev**m)
    return Z,rhos,cs
if __name__=='__main__':
    for m in map(int,sys.argv[1].split(',')):
        Z,rh,cs=ZTM(m,2.0,R=int(sys.argv[2]),L=int(sys.argv[3]))
        print(f'm={m} |Z_TM(nu*)|^2={abs(Z)**2:.5g}  rho_a={np.round(rh,4).tolist()}  |c_a|={np.round(abs(cs),3).tolist()}',flush=True)
