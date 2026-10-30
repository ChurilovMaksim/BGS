"""Line F: lifted (lattice-of-discs) transfer operators, float prototype.
Vertex states k in [-K0,K0], disc D(k,r); edge states e in [-K0,K0-1] (pair (e,e+1)), disc D(e+1/2,rE).
(L_V Phi)_k(s) = sum_n w(n) e(c n s) Phi_{f_n(k)}((s+n)/lam),  f_n(k) = round((k+n)/lam)
(L_E Phi)_e(s) = sum_{n: f_n(e+1)=f_n(e)+1} w(n) e(c n s) Phi_{f_n(e)}((s+n)/lam)
Claim: sum_{w in A^m} prod w(n_j) e(c n_j s_j) = Tr L_V^m - Tr L_E^m."""
import numpy as np, math
from scipy.special import jv, gammaln
LAM=3+2*math.sqrt(2); C0=1/(LAM-1/LAM)
def rnd(x): return int(math.floor(x+0.5))
def blockmat(n,center_out,center_in,r_out,r_in,coef,K):
    # phi(u) = sum_l a_l ((u-cin)/rin)^l ; output in basis ((s-cout)/rout)^i ; u=(s+n)/lam
    # tau=(u-cin)/rin = (rout*sig + cout + n - lam*cin)/(lam*rin) = A*sig + B
    A=r_out/(LAM*r_in); B=(center_out+n-LAM*center_in)/(LAM*r_in)
    i=np.arange(K)[:,None]; l=np.arange(K)[None,:]; e=l-i; ee=np.where(e>=0,e,0)
    with np.errstate(divide='ignore'):
        logb=gammaln(l+1)-gammaln(i+1)-gammaln(ee+1)
        Cm=np.where(e>=0, np.exp(logb)*A**i*(B**ee if B!=0 else (ee==0)*1.0),0.0)
    z=2j*np.pi*coef*n*r_out
    d=i-l; dd=np.where(d>=0,d,0)
    M=np.where(d>=0, z**dd/np.exp(gammaln(dd+1)),0)
    return np.exp(2j*np.pi*coef*n*center_out)*(M@Cm)
def ops(wfun,N0,K0,r,rE,K,beta=0.0,coef=C0):
    nv=2*K0+1; ne=2*K0
    V=np.zeros((nv*K,nv*K),complex); E=np.zeros((ne*K,ne*K),complex)
    om=lambda k: math.exp(-beta*abs(k))
    for n in range(-N0,N0+1):
        wn=wfun(n)
        if wn==0: continue
        for k in range(-K0,K0+1):
            j=rnd((k+n)/LAM)
            if abs(j)>K0: continue
            V[(k+K0)*K:(k+K0+1)*K,(j+K0)*K:(j+K0+1)*K]+=wn*om(k)/om(j)*blockmat(n,k,j,r,r,coef,K)
        for e in range(-K0,K0):
            j=rnd((e+n)/LAM); j2=rnd((e+1+n)/LAM)
            if j2!=j+1 or j<-K0 or j>K0-1: continue
            E[(e+K0)*K:(e+K0+1)*K,(j+K0)*K:(j+K0+1)*K]+=wn*om(e)/om(j)*blockmat(n,e+.5,j+.5,rE,rE,coef,K)
    return V,E
def wk1(eta,a,L=None):
    x=0.9*eta
    def w(n):
        if L is not None and abs(n)>L: return 0
        return (1j)**(n%4)*jv(n,x)*np.exp(2j*np.pi*(C0*n*n/2+a*n/8))
    return w
def brute(wfun,L,m):
    import itertools
    tot=0
    for wd in itertools.product(range(-L,L+1),repeat=m):
        s0=sum(wd[(0-k)%m]*LAM**(-k) for k in range(1,40)) # s_0 = sum_{k>=1} n_{-k} lam^-k
        s=s0; p=1
        for j in range(m):
            p*=wfun(wd[j])*np.exp(2j*np.pi*C0*wd[j]*s); s=(s+wd[j])/LAM
        tot+=p
    return tot
if __name__=='__main__':
    import sys
    for a in (4,2):
        w=wk1(2.0,a,L=3)
        V,E=ops(w,3,3,1.2,0.8,40)
        ev=np.linalg.eigvals(V); ee=np.linalg.eigvals(E)
        for m in range(1,6):
            b=brute(w,3,m); t=np.sum(ev**m)-np.sum(ee**m)
            print(a,m,b,t,abs(b-t)/abs(b))
