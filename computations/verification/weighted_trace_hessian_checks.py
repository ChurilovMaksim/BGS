#!/usr/bin/env python3
"""Bounded independent checks of the degenerate-block Hessian identity.

Direct differentiation of matrix powers is compared with the eigenblock
formula. Artificial repeated clock spectra are algebra tests, not simulations
of the original fixed-coupling asymptotic problem. No eigenvalue branches or
finite differences are used. Assertions remain active under python -O.
"""
import json
import numpy as np

def require(ok, message):
    if not ok: raise RuntimeError(message)

def main():
    rng=np.random.default_rng(20261021); cases=[]
    for d, multiplicities in [(3,[2,1,3]), (4,[2,2,1,2]), (5,[1,2,1,3,1])]:
        labels=np.repeat(np.arange(d),multiplicities); n=len(labels)
        lam=np.exp(2j*np.pi*labels/d); U=np.diag(lam)
        Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        A=(Z+Z.conj().T)/(2*n)
        A-=np.trace(A).real/n*np.eye(n)
        # Diagonalize only the fixed A blocks; degeneracies of U are retained.
        V=np.zeros((n,n),dtype=complex)
        for j in range(d):
            ix=np.flatnonzero(labels==j); _,v=np.linalg.eigh(A[np.ix_(ix,ix)])
            V[np.ix_(ix,ix)]=v
        A=V.conj().T@A@V; q=np.diag(A).real
        p={m:np.sum(lam**m) for m in range(-4*n,4*n+1)}
        G=np.zeros((n,n),complex); direct=0.; weights={}
        for m in range(1,2*n):
            x=m/n; weights[m]=np.exp(-1/(1-(x/2)**2))
            Um=np.diag(lam**m)
            first=1j*n*m*np.trace(A@Um)
            second=-n*n*m*sum(np.trace(A@np.diag(lam**j)@A@np.diag(lam**(m-j))) for j in range(m))
            direct+=weights[m]*2*(abs(first)**2+(np.conj(p[m])*second).real)/(n*n)
            Zm=np.conj(p[m])*Um
            G+=m*weights[m]*(Zm-Zm.conj().T)/(2j)
        beta=np.zeros(n)
        for a in range(n):
            gamma=sum(abs(A[a,b])**2*(lam[a]+lam[b])/(lam[a]-lam[b])
                      for b in range(n) if labels[a]!=labels[b])
            require(abs(gamma.real)<1e-10,'Gamma not imaginary')
            beta[a]=gamma.imag
        block=2*np.sum(beta*np.diag(G).real)
        for a in range(n):
            for b in range(n):
                H=sum(m*m*wm*np.cos(2*np.pi*m*(labels[a]-labels[b])/d)
                      for m,wm in weights.items())
                block-=(q[a]-q[b])**2*H
        energy=sum(m*k*weights[m]*weights[k]*
                   (np.conj(p[m])*p[k]*p[m-k]-np.conj(p[m])*np.conj(p[k])*p[m+k]).real
                   for m in weights for k in weights)
        err=abs(direct-block); ge=abs(2*np.linalg.norm(G,'fro')**2-energy)
        require(err<1e-8*(1+abs(direct)),'Hessian formula mismatch')
        require(ge<1e-8*(1+abs(energy)),'Gradient energy mismatch')
        require(abs(np.trace(G))<1e-8,'Gradient not traceless')
        cases.append({'d':d,'N':n,'multiplicities':multiplicities,
                      'direct_hessian':float(direct),'block_hessian':float(block),
                      'absolute_error':float(err),'gradient_energy_error':float(ge)})
    print(json.dumps({'result':'PASS','scope':'Three artificial repeated-clock finite algebra cases; not an asymptotic proof',
                      'cases':cases},indent=2))

if __name__=='__main__':main()
