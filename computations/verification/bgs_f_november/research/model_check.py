"""Independently assemble A by its three diagonals, then test (4) using all symbol frequencies."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from pathlib import Path
import json
import numpy as np
from coefficients import pell,raw_symbol

def check(k):
    n=pell(k);x=np.arange(n);xx,yy=np.meshgrid(x,x,indexing="ij")
    def e(t):return np.exp(2j*np.pi*(np.asarray(t)%n)/n)
    def r(q):return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
    q=x/n
    A=np.diag(np.cos(14*np.pi*q)+r(q)*(.1+np.sin(2*np.pi*q)/100)-.1).astype(complex)
    off=(-3-4j)*r(((x+pow(2,-1,n))%n)/n)/1000
    A[x,(x+1)%n]+=off;A[(x+1)%n,x]+=off.conj()
    M=e(-pow(8,-1,n)*(3*xx*xx-2*xx*yy+3*yy*yy))/np.sqrt(n)
    D={(a,b):complex(re,im)/4000 for (a,b),(re,im) in raw_symbol().items()}
    Araw=np.zeros_like(A)
    for (a,b),z in D.items():
        Araw[x,(x+a)%n]+=z*e(b*(x+pow(2,-1,n)*a))
    adiff=float(np.max(abs(A-Araw)))
    # Use a moderate test of all mixed Fourier terms, a finite polynomial V.
    strength=.375
    V=np.eye(n)+1j*strength*A
    digits={d:1j*strength*z for d,z in D.items()};digits[0,0]=digits.get((0,0),0)+1
    direct=np.trace(np.linalg.matrix_power(V@M,k))/np.trace(np.linalg.matrix_power(M,k))
    # Any periodic state obeys (5); the square [-24,24]^2 contains all doubled coordinates.
    # rad <= 1+9 sqrt(2); hence u+v < 20. Four parity classes are invariant.
    tot=0j
    for i in range(2):
        for j in range(2):
            states=[(a,b) for a in range(-24,25) for b in range(-24,25)
                    if a%2==i and b%2==j and abs(a+np.sqrt(2)*b)<6.0
                    and abs(a-np.sqrt(2)*b)<34.0]
            index={d:s for s,d in enumerate(states)};H=np.zeros((len(states),)*2,complex)
            for col,(X,Y) in enumerate(states):
                P,Q=3*X+4*Y,2*X+3*Y
                for (a,b),z in digits.items():
                    row=index.get((P+2*a,Q+2*b))
                    if row is not None:H[row,col]+=z*e(pow(4,-1,n)*(a*Q-b*P))
            tot+=np.trace(np.linalg.matrix_power(H,k))
    err=float(abs(tot-direct))
    assert adiff<1e-12 and err<1e-12
    return {"k":k,"N":n,"raw_vs_jacobi":adiff,"dual_vs_direct":err}
if __name__=="__main__":print(json.dumps([check(k) for k in (3,5,7)],indent=2))
