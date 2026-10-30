"""Referee's independent float implementation of Line F's vertex/edge lift (written from the prose, not from lift.py).
Basis: Taylor coefficients at disc centre, scaled by rho (orthonormal in H^2(D(c,rho))).
Operator block (letter n, output state centre c, input centre c'): f -> w(n) e(C n s) f((s+n)/lam)."""
import numpy as np, math, itertools, sys
from scipy.special import jv, comb, factorial
LAM=3+2*math.sqrt(2); C=1/(LAM-1/LAM)
def block(n,c,cp,rho,K,Cc):
    # g(sig)= exp(2 pi i Cc n (c+rho sig)) * f(((c+rho sig)+n)/lam), f(u)=sum_l a_l ((u-cp)/rho)^l
    # (u-cp)/rho = sig/lam + d, d=((c+n)/lam-cp)/rho
    d=((c+n)/LAM-cp)/rho
    Cm=np.zeros((K,K),complex)
    for l in range(K):
        for i in range(l+1): Cm[i,l]=comb(l,i)*LAM**(-i)*d**(l-i)
    z=2j*math.pi*Cc*n*rho
    Mm=np.zeros((K,K),complex)
    for i in range(K):
        for j in range(i+1): Mm[i,j]=z**(i-j)/math.factorial(i-j)
    return np.exp(2j*math.pi*Cc*n*c)*Mm@Cm
def build(w,N0,K0,rhoV,rhoE,K,Cc=C):
    vs=list(range(-K0,K0+1)); es=list(range(-K0,K0))
    V=np.zeros((len(vs)*K,)*2,complex); E=np.zeros((len(es)*K,)*2,complex)
    r=lambda x: math.floor(x+0.5)
    for n in range(-N0,N0+1):
        wn=w(n)
        for i,k in enumerate(vs):
            j=r((k+n)/LAM)
            if -K0<=j<=K0:
                jj=vs.index(j); V[i*K:(i+1)*K,jj*K:(jj+1)*K]+=wn*block(n,k,j,rhoV,K,Cc)
        for i,e in enumerate(es):
            j=r((e+n)/LAM)
            if r((e+1+n)/LAM)!=j+1 or not (-K0<=j<K0): continue
            jj=es.index(j); E[i*K:(i+1)*K,jj*K:(jj+1)*K]+=wn*block(n,e+.5,j+.5,rhoE,K,Cc)
    return V,E
def wk1(eta,a,Cc=C):
    x=0.9*eta
    return lambda n: (1j)**(n%4)*jv(n,x)*np.exp(2j*math.pi*(Cc*n*n/2+a*n/8))
def ca(kappa):
    return {a: sum(np.exp(2j*math.pi*(kappa*b*b-a*b)/8) for b in range(8))/8 for a in range(8)}
def Hinv(m):
    Cy=np.roll(np.eye(m),1,axis=1); H=6*np.eye(m)-Cy-Cy.T; return np.linalg.inv(H)
def brute_Z(m,eta,kappa,L):
    x=0.9*eta; G=Hinv(m)
    ns=np.arange(-L,L+1); gh=(1j)**(ns%4)*jv(ns,x)
    tot=0
    for wd in itertools.product(range(2*L+1),repeat=m):
        n=ns[list(wd)]; amp=np.prod(gh[list(wd)])
        if abs(amp)<1e-22: continue
        tot+=amp*np.exp(2j*math.pi*(0.5*n@G@n+kappa*(n.sum())**2/8))
    return tot
