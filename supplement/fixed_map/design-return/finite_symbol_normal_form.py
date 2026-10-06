"""Finite checks for the general finite-Fourier-symbol normal form.

The exponent epsilon is an independent test parameter here; these
moderate-size experiments do NOT simulate the frozen 10^-80 coupling.
"""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json
import numpy as np


def expi(a,t):
    w,v=np.linalg.eigh(a)
    return (v*np.exp(1j*t*w))@v.conj().T


def run(k):
    n,f=1,0
    for _ in range(k): n,f=n+2*f,n+f
    x=np.arange(n);X=x[:,None];Y=x[None,:]
    M=np.exp(2j*np.pi*((-pow(8,-1,n)*(3*X*X-2*X*Y+3*Y*Y))%n)/n)/np.sqrt(n)
    def T(a,b):
        out=np.zeros((n,n),complex)
        out[x,(x+a)%n]=np.exp(2j*np.pi*((b*(x+a*pow(2,-1,n)))%n)/n)
        return out
    # A genuinely two-dimensional, non-even real symbol.
    coeff={(1,0):.4+.1j,(0,1):.3-.2j,(1,2):.15+.07j}
    coeff.update({(-a,-b):z.conjugate() for (a,b),z in list(coeff.items())})
    A=sum(z*T(a,b) for (a,b),z in coeff.items())
    F0=sum(abs(z) for z in coeff.values())
    F1=sum(abs(z)*(abs(a)+abs(b)) for (a,b),z in coeff.items())
    seq=[A]
    for _ in range(k-1):seq.append(M@seq[-1]@M.conj().T)
    c=(k-1-2*np.arange(k))/(2*k)
    G=sum(cj*Aj for cj,Aj in zip(c,seq))
    avg=sum(seq)/k
    hs=lambda z:np.linalg.norm(z,'fro')/np.sqrt(n)
    homological=hs(G-M@G@M.conj().T-A+avg)
    assert homological<1e-11
    comm1=np.linalg.norm(G@A-A@G,2)
    comm2=hs(G@avg-avg@G)
    assert comm1<=15*np.pi*F1*F1/k
    assert comm2<=6*np.pi*F1*F1/np.sqrt(k)
    assert hs(avg)<=F0/np.sqrt(k)+1e-12
    rows=[]
    for eps in (.003,.01,.03):
        U=expi(A,eps)@M;V=expi(G,-eps)
        error=hs(V@U@V.conj().T-expi(avg,eps)@M)
        comm_actual=(comm1+hs((-G+A)@avg-avg@(-G+A)))/2
        assert error<=eps*eps*comm_actual+1e-11
        assert error<=17*np.pi*F1*F1*eps*eps/np.sqrt(k)
        rows.append(dict(epsilon=eps,error=float(error),
                         error_over_epsilon_squared=float(error/eps**2)))
    return dict(K=k,N=n,homological_error=float(homological),
                commutator_operator=float(comm1),commutator_hs=float(comm2),
                checks=rows)


if __name__=='__main__':
    print(json.dumps([run(k) for k in (5,7)],indent=2))
