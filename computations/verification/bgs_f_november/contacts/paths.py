"""Compare actual pairs of closed words with contact-generating transfer matrices."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from itertools import product
import json
import numpy as np
import scipy.linalg as la

def model(n,t):
    X,Y=np.indices((n,n))
    M=np.exp(2j*np.pi*((-pow(8,-1,n)*(3*X*X-2*X*Y+3*Y*Y))%n)/n)/np.sqrt(n)
    q=np.arange(n)/n
    r=lambda x:(1-np.cos(14*np.pi*x))*(1+np.cos(2*np.pi*x))
    A=np.diag(np.cos(14*np.pi*q)-.1+r(q)*(.1+.01*np.sin(2*np.pi*q))).astype(complex)
    x=np.arange(n); link=(-3-4j)*r(((x+pow(2,-1,n))%n)/n)/1000
    A[x,(x+1)%n]+=link
    A[(x+1)%n,x]+=link.conj()
    return la.expm(1j*t*A)@M

def test(n,m,t):
    U=model(n,t); words=np.array(list(product(range(n),repeat=m)))
    amplitude=U[np.roll(words,-1,axis=1),words].prod(axis=1)
    all_coeff=np.zeros(m+1,complex)
    near=0j; marked=0j; cyclic=0j; excess=0j
    h=(2*m)//3+1
    for x,amp in zip(words,amplitude):
        values=amp*amplitude.conj()
        hits=np.stack([np.sum(np.roll(words,k,axis=1)==x,axis=1) for k in range(m)])
        np.add.at(all_coeff,hits[0],values)
        mult=(hits>=h).sum(axis=0)
        near+=values[mult>0].sum()
        marked+=np.sum(mult*values)
        excess+=np.sum(np.maximum(mult-1,0)*values)
        cyclic+=values[np.max(hits,axis=0)==m].sum()
    V=np.kron(U,U.conj()); contact=(np.eye(n).reshape(-1)).astype(bool)
    check=0.
    for z in [0,.6+.25j,1,1.15-.2j]:
        Z=(np.where(contact,z,1))[:,None]*V
        check=max(check,abs(np.trace(np.linalg.matrix_power(Z,m))-sum(all_coeff[k]*z**k for k in range(m+1))))
    B=abs(U)**2
    check=max(check,abs(all_coeff[-1]-np.trace(np.linalg.matrix_power(B,m))),
              abs(marked-m*sum(all_coeff[h:])),abs(marked-near-excess),
              abs(sum(all_coeff)-abs(np.trace(np.linalg.matrix_power(U,m)))**2))
    cyc2=0.
    for x,amp in zip(words,amplitude):
        period=next(k for k in range(1,m+1) if np.all(np.roll(x,k)==x))
        cyc2+=period*abs(amp)**2
    check=max(check,abs(cyclic-cyc2))
    assert check<2e-10
    return dict(N=n,m=m,t=t,threshold=h,maximum_identity_error=float(check),
                near_real=float(near.real), marked_real=float(marked.real),
                duplicate_real=float(excess.real),cyclic_real=float(cyclic.real))
if __name__=='__main__':
    print(json.dumps([test(3,5,.37),test(5,4,.28),test(3,6,.42)],indent=2))
