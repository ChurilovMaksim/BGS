"""Independent small-matrix checks of angular transfer, the gap window and Fourier normalization."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import json
from fractions import Fraction
from pathlib import Path
import sys
import numpy as np
import scipy.linalg as la
from scipy.integrate import quad
from scipy.optimize import linear_sum_assignment
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'research'))
from coefficients import raw_symbol

def one(n):
    x=np.arange(n);q=x/n
    def e(v):return np.exp(2j*np.pi*(v % n)/n)
    def r(z):return (1-np.cos(14*np.pi*z))*(1+np.cos(2*np.pi*z))
    A=np.diag(np.cos(14*np.pi*q)-.1+r(q)*(.1+.01*np.sin(2*np.pi*q))).astype(complex)
    link=(-3-4j)*r(((x+pow(2,-1,n))%n)/n)/1000
    A[x,(x+1)%n]+=link; A[(x+1)%n,x]+=link.conj()
    X,Y=np.meshgrid(x,x,indexing='ij')
    M=e(-pow(8,-1,n)*(3*X**2-2*X*Y+3*Y**2))/np.sqrt(n)
    t=.24/n
    U=la.expm(1j*t*A)@M
    z=np.linalg.eigvals(U);mu=np.linalg.eigvals(M)
    dist=abs(np.angle(z[:,None]/mu[None,:]))/(2*np.pi)
    # Optimize the maximum circular distance over the finite list of candidate thresholds.
    for threshold in np.unique(dist):
        cost=(dist>threshold).astype(float);a,b=linear_sum_assignment(cost)
        if not cost[a,b].any():break
    assert threshold<1.186*t/(2*np.pi)+1e-12
    unfolded=n*abs(np.angle(z[:,None]/z[None,:]))/(2*np.pi)
    assert not np.any((unfolded>.1)&(unfolded<.65))
    # Check formula for the squared norm of the averaged pure observable, directly and in its orbit expansion.
    T=9;Y=np.zeros_like(A);Z=A.copy()
    for _ in range(T):Y+=Z;Z=M@Z@M.conj().T
    sums={}
    for (a,b),(u,v) in raw_symbol().items():
        for _ in range(T):
            d=(a%n,b%n);s=sums.setdefault(d,[0,0]);s[0]+=u;s[1]+=v
            a,b=(3*a+4*b)%n,(2*a+3*b)%n
    exact=Fraction(sum(u*u+v*v for u,v in sums.values()),(4000*T)**2)
    err=abs(la.norm(Y/T,'fro')**2/n-float(exact))
    assert err<2e-13
    # Construct periodized b in Fourier space, and compare time-domain variance with positive-frequency sum.
    phi=lambda u: np.exp(-1/(1-u*u)) if abs(u)<1 else 0.
    I=quad(phi,-1,1,epsabs=1e-12)[0]
    def conv(s):
        return quad(lambda u:phi(u)*phi(s-u),max(-1,s-1),min(1,s+1),epsabs=1e-12)[0]/(2*I*I)
    c=np.array([conv(j/n)*sum(z**j)/n for j in range(2*n)])
    k=4*len(c);positions=np.arange(k)/k
    B=c[0].real+2*(np.exp(-2j*np.pi*positions[:,None]*np.arange(1,len(c)))@c[1:]).real
    mismatch=abs(np.var(B)-2*np.sum(abs(c[1:])**2))
    assert mismatch<1e-12
    return dict(N=n, matched_unfolded_shift=float(n*threshold), covariance_error=err, parseval_error=mismatch)

print(json.dumps([one(n) for n in (5,7,9,15,21)],indent=2))
