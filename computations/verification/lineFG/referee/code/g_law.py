"""Referee check of Line G's G1/G1'/G2 law, own code. Finite alphabet |n|<=L, random complex weights.
Z(nu) = sum_n Phi(n) e(-nu P(n)/(2h)), P = 4h n^T H^-1 n (checked integer); law: Z = (1-lam^-m) Tr_H[(I x <1|) Lop^m (I x |d0>)]."""
import numpy as np, math, itertools, sys
from math import gcd
LAM=3+2*math.sqrt(2); C=1/(4*math.sqrt(2))
rng=np.random.default_rng(1)
def nsw(m): # h_m = Re (1+sqrt2)^m
    a,b=1,0
    for _ in range(m): a,b=a+2*b,a+b
    return a
def run(m,L,ntest=12):
    h=nsw(m); yp=math.isqrt((h*h+1)//2); assert h*h+1==2*yp*yp
    Cy=np.roll(np.eye(m),1,axis=1); Hi=np.linalg.inv(6*np.eye(m)-Cy-Cy.T)
    # psi(d) = 4h Hinv_{0d}; compare with y' x_d - 2h y_d
    x,y=1,0; ok=True
    for d in range(m):
        ok&= abs(4*h*Hi[0,d]-(yp*x-2*h*y))<1e-6; x,y=3*x+8*y,x+3*y
    g=rng.normal(size=2*L+1)+1j*rng.normal(size=2*L+1); g/=np.abs(g).sum()
    ns=np.arange(-L,L+1)
    words=np.array(list(itertools.product(ns,repeat=m)),float)
    amp=np.prod(g[(words+L).astype(int)],axis=1)
    P=4*h*np.einsum('ki,ij,kj->k',words,Hi,words); Pi=np.rint(P); assert abs(P-Pi).max()<1e-6
    Pi=Pi.astype(np.int64)
    units=[v for v in range(2*h) if gcd(v,2*h)==1]
    Zb={v:np.sum(amp*np.exp(-2j*np.pi*((v*Pi)%(2*h))/(2*h))) for v in units}
    psi0=yp; psi1=3*yp-2*h
    K=28; rho=1.2; assert rho>L/(LAM-1)
    i=np.arange(K)[:,None]; l=np.arange(K)[None,:]
    from scipy.special import comb, gammaln
    out=[]
    tested=0
    for v in rng.permutation(units):
        # shortest (a,b): smallest b with |a|<=b-ish
        best=None
        for b in range(1,25):
            a=(b*v)%(2*h);  a=a-2*h if a>h else a
            if best is None or abs(a)+b<abs(best[0])+best[1]: best=(a,b)
        a,b=best; k=(b*v-a)//(2*h); assert b*v-a==2*h*k
        coef=-4*a*C/b
        # H-part operator R_n: phi -> e(coef(n^2/2+ns)) phi((s+n)/lam) on H^2(D_rho), basis (s/rho)^i
        R={}
        for n in ns:
            d=n/(LAM*rho)  # (u)/rho = s/(lam rho)... u=(s+n)/lam, u/rho = sig/lam + n/(lam rho)
            e=np.maximum(l-i,0); Cm=np.where(l>=i, comb(l,i)*LAM**(-i*1.0)*d**e,0)
            z=2j*np.pi*coef*n*rho; e2=np.maximum(i-l,0); Mm=np.where(i>=l, z**e2/np.exp(gammaln(e2+1)),0)
            R[n]=np.exp(2j*np.pi*coef*n*n/2)*(Mm@Cm)
        # automaton on (u,w) mod b: state index u*b+w
        S=b*b
        A={}
        for n in ns:
            M=np.zeros((S,S),complex)
            for u in range(b):
                for w in range(b):
                    u2=(6*u-w+n*psi1)%b; w2=(u+n*psi0)%b
                    M[u2*b+w2,u*b+w]=np.exp(-2j*np.pi*k*((psi0*n*n+2*n*u)%b)/b)
            A[n]=M
        Lop=sum(g[n+L]*np.kron(R[n],A[n]) for n in ns)
        # columns e_i x delta0
        X=np.zeros((K*S,K),complex)
        for ii in range(K): X[ii*S+0,ii]=1
        for _ in range(m): X=Lop@X
        Z=(1-LAM**-m)*sum(X[ii*S:(ii+1)*S,ii].sum() for ii in range(K))
        rel=abs(Z-Zb[v])/max(abs(Zb[v]),1e-12)
        out.append((int(v),a,b,rel)); tested+=1
        if tested>=ntest: break
    return h,ok,out
for m,L in ((5,2),(7,2)):
    h,ok,out=run(m,L)
    print('m',m,'h',h,'psi(d)=yp x_d-2h y_d:',ok)
    for o in out: print('  nu=%d (a,b)=(%d,%d) rel=%.2e'%o)
    print('  max rel',max(o[3] for o in out),flush=True)
