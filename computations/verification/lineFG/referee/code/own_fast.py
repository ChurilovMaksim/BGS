"""vectorised version of own_lift.build (same math)."""
import numpy as np, math
from scipy.special import jv, gammaln
LAM=3+2*math.sqrt(2); C=1/(LAM-1/LAM)
def mk(K):
    i=np.arange(K)[:,None]; l=np.arange(K)[None,:]
    lb=np.where(l>=i, gammaln(l+1)-gammaln(i+1)-gammaln(np.maximum(l-i,0)+1), -np.inf)
    return i,l,np.exp(lb)
def block(n,c,cp,rho,K,Cc,pre):
    i,l,Bn=pre
    d=((c+n)/LAM-cp)/rho
    e=np.maximum(l-i,0)
    Cm=np.where(l>=i, Bn*LAM**(-i.astype(float))*(d**e if d!=0 else (e==0)*1.0),0)
    z=2j*math.pi*Cc*n*rho; e2=np.maximum(i-l,0)
    Mm=np.where(i>=l, z**e2/np.exp(gammaln(e2+1)),0)
    return np.exp(2j*math.pi*Cc*n*c)*(Mm@Cm)
def build(w,N0,K0,rhoV,rhoE,K,Cc=C):
    pre=mk(K); vs=list(range(-K0,K0+1)); es=list(range(-K0,K0))
    V=np.zeros((len(vs)*K,)*2,complex); E=np.zeros((len(es)*K,)*2,complex)
    r=lambda x: math.floor(x+0.5)
    for n in range(-N0,N0+1):
        wn=w(n)
        for ii,k in enumerate(vs):
            j=r((k+n)/LAM)
            if -K0<=j<=K0:
                jj=j+K0; V[ii*K:(ii+1)*K,jj*K:(jj+1)*K]+=wn*block(n,k,j,rhoV,K,Cc,pre)
        for ii,e in enumerate(es):
            j=r((e+n)/LAM)
            if r((e+1+n)/LAM)!=j+1 or not (-K0<=j<K0): continue
            jj=j+K0; E[ii*K:(ii+1)*K,jj*K:(jj+1)*K]+=wn*block(n,e+.5,j+.5,rhoE,K,Cc,pre)
    return V,E
def wk1(eta,a,Cc=C):
    x=0.9*eta
    return lambda n: (1j)**(n%4)*jv(n,x)*np.exp(2j*math.pi*(Cc*n*n/2+a*n/8))
def ca(kappa):
    return {a: sum(np.exp(2j*math.pi*(kappa*b*b-a*b)/8) for b in range(8))/8 for a in range(8)}
