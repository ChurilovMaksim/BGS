"""Independent dense checks of the frozen-symbol conventions and Duhamel bound.

Epsilon here is a test parameter, not 10^-80*N. The actual giant-N results
are rational certificates in frozen_sharp_return.py, not matrix simulations.
"""
import json
import numpy as np
from frozen_sharp_return import coefficients
from sparse_orbit_checks import pell


def expi(a,t):
    e,v=np.linalg.eigh(a)
    return (v*np.exp(1j*t*e))@v.conj().T


def run(k):
    n,_=pell(k);den,coeff=coefficients()
    x=np.arange(n);X=x[:,None];Y=x[None,:]
    M=np.exp(2j*np.pi*((-pow(8,-1,n)*(3*X*X-2*X*Y+3*Y*Y))%n)/n)/np.sqrt(n)
    def T(a,b):
        out=np.zeros((n,n),complex)
        out[x,(x+a)%n]=np.exp(2j*np.pi*((b*(x+a*pow(2,-1,n)))%n)/n)
        return out
    def r(q):return (1-np.cos(14*np.pi*q))*(1+np.cos(2*np.pi*q))
    def g(q):return np.cos(14*np.pi*q)+r(q)/10+r(q)*np.sin(2*np.pi*q)/100
    def hs(a):return np.linalg.norm(a,'fro')/np.sqrt(n)
    rows=[]
    for gauge in (False,True):
        A=.1*np.eye(n,dtype=complex)
        for (a,b),(re,im) in coeff.items():
            sign=-1 if gauge and (a*b)%2 else 1
            A+=sign*(re+1j*im)*T(a,b)/den
        jac=np.diag(g(x/n)).astype(complex)
        midpoint=.5 if gauge else pow(2,-1,n)
        hop=(-3-4j)*r((x+midpoint)/n)/1000
        jac[x,(x+1)%n]+=hop
        jac[(x+1)%n,x]+=hop.conj()
        jac_error=hs(A-jac)
        assert jac_error<1e-12
        seq=[A]
        for _ in range(k-1):seq.append(M@seq[-1]@M.conj().T)
        c=(k-1-2*np.arange(k))/(2*k)
        G=sum(t*a for t,a in zip(c,seq));bar=sum(seq)/k
        homological=hs(G-M@G@M.conj().T-A+bar)
        assert homological<1e-11
        error_coefficient=(hs(G@A-A@G)+hs((-G+A)@bar-bar@(-G+A)))/2
        cases=[]
        for eps in (.01,.1):
            V=expi(G,-eps);U=expi(A,eps)@M
            residual=hs(V@U@V.conj().T-expi(bar,eps)@M)
            bound=eps*eps*error_coefficient
            assert residual<bound+1e-11
            cases.append(dict(epsilon=eps,one_step_error=float(residual),
                              direct_commutator_bound=float(bound)))
        rows.append(dict(gauge='ordinary midpoint' if gauge else 'raw modular',
                         jacobi_assembly_error=float(jac_error),
                         homological_error=float(homological),
                         K_times_average_HS_squared=float(k*hs(bar-.1*np.eye(n))**2),
                         cases=cases))
    return dict(K=k,N=n,quantizations=rows)


if __name__=='__main__':print(json.dumps([run(k) for k in (5,7)],indent=2))
