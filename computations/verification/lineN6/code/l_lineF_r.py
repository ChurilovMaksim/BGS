"""N6 (1) [N]: excursion factors r_A, r_B in the Line F lifted sector-4 vertex operator (float), to compare with the TW-law values of N5.
r = lim <psi| prod_k (L_{1/2+d_k}/mu) |Phi> / <psi|Phi>, Perron data of L_{1/2}.  Excursion A: d_k = -a lam^-(-k) (k<=0), +a lam^-(k-1) (k>=1),
a=(2-sqrt2)/4 ; B: d_k = -b lam^-|k|, b = sqrt2/4."""
import sys, math, numpy as np
sys.path.insert(0,'/workspace/bgs-lineF/code'); from lift import ops, LAM, C0
from scipy.special import jv
K0=int(sys.argv[1]) if len(sys.argv)>1 else 4; K=int(sys.argv[2]) if len(sys.argv)>2 else 40; N0=int(sys.argv[3]) if len(sys.argv)>3 else 30
r=1.2; beta=2.5
def w(t):
    return lambda n: (1j)**(n%4)*jv(n,1.8)*np.exp(2j*np.pi*(C0*n*n/2+n*t))
cache={}
def V(t):
    if t not in cache: cache[t]=ops(w(t),N0,K0,r,0.8,K,beta=beta)[0]
    return cache[t]
L=V(0.5); ev,R=np.linalg.eig(L); i=np.argmax(abs(ev)); mu=ev[i]; Phi=R[:,i]
evl,Lv=np.linalg.eig(L.T); j=np.argmin(abs(evl-mu)); psi=Lv[:,j]
srt=sorted(abs(ev))[::-1]
print('mu',mu,abs(mu),'second',srt[1])
a=(2-math.sqrt(2))/4; b=math.sqrt(2)/4; KK=14
dA=[-a*LAM**(-(-k)) for k in range(-KK,1)]+[a*LAM**(-(k-1)) for k in range(1,KK+1)]
dB=[-b*LAM**(-abs(k)) for k in range(-KK,KK+1)]
def fac(ds):
    v=Phi.copy()
    for dd in ds: v=V(0.5+dd)@v/mu
    return (psi@v)/(psi@Phi)
rA=fac(dA); rB=fac(dB)
print('rA',rA,abs(rA),'rB',rB,abs(rB),'-(rArB)^3',-(rA*rB)**3)
