#!/usr/bin/env python3
"""Finite diagnostics for the time-insertion criterion, not asymptotic evidence."""

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import json
import numpy as np


def cutoff(s):
    s=np.asarray(s); out=np.zeros(s.shape)
    inside=abs(s)<.4
    out[inside]=np.exp(1-1/(1-(s[inside]/.4)**2))
    return out


def diagnostic(phases):
    N=len(phases); L=2*N+1
    m=np.arange(L); m=np.where(m<=N,m,m-L)
    diffs=(phases[:,None]-phases[None,:]).ravel()
    traces=np.exp(2j*np.pi*m[:,None]*phases).sum(axis=1)
    main=np.minimum(abs(m),N).astype(float); main[m==0]=N*N
    residual=abs(traces)**2-main
    chi=cutoff(m/N)
    # A is diagonal in the eigenmatrix basis; this is the full canonical
    # insertion chi(m/N) R_m A^(-m)/N^2, not a stochastic trace estimator.
    E=(chi*residual/(N*N))[:,None]*np.exp(-2j*np.pi*m[:,None]*diffs)
    coeff=np.fft.fft(E,axis=0)/L
    inverse=np.fft.ifft(coeff*L,axis=0)
    assert np.max(abs(inverse-E))<1e-12
    # Reconstruct the trace of E_m A^m independently.
    inserted=(E*np.exp(2j*np.pi*m[:,None]*diffs)).sum(axis=1)
    assert np.max(abs(inserted-chi*residual))<1e-8
    return dict(N=N,wiener_budget=float(np.max(abs(coeff),axis=1).sum()),
                operator_sup=float(np.max(abs(E))),
                signed_weighted_residual=float(np.sum(chi*residual)/(N*N)))


def exact_obstruction_checks():
    rows=[]
    for N in [8,16,32,64]:
        eps=N**(-.5); m=np.arange(N); d=np.arange(N)/N
        E=eps*np.exp(-2j*np.pi*m[:,None]*d)
        coeff=np.fft.fft(E,axis=0)/N
        budget=np.max(abs(coeff),axis=1).sum()
        assert abs(budget-N*eps)<1e-10
        assert np.max(abs(np.fft.ifft(coeff*N,axis=0)-E))<1e-12
        rows.append(dict(N=N,operator_sup=eps,wiener_budget=float(budget)))
    return rows


def main():
    rng=np.random.default_rng(20260916); rows=[]
    for N in [15,31,63,127]:
        rows.append(dict(model='clock',**diagnostic(np.arange(N)/N)))
        x=np.arange(N); X=x[:,None]; Y=x[None,:]
        M=np.exp(2j*np.pi*((-pow(8,-1,N)*(3*X*X-2*X*Y+3*Y*Y))%N)/N)/np.sqrt(N)
        assert np.linalg.norm(M.conj().T@M-np.eye(N),2)<1e-12
        rows.append(dict(model='linear cat',**diagnostic(np.angle(np.linalg.eigvals(M))/(2*np.pi))))
        for seed_index in range(2):
            Z=rng.normal(size=(N,N))+1j*rng.normal(size=(N,N))
            Q,R=np.linalg.qr(Z); signs=np.diag(R)/abs(np.diag(R)); Q=Q*signs
            assert np.linalg.norm(Q.conj().T@Q-np.eye(N),2)<1e-12
            rows.append(dict(model='Haar control',sample=seed_index,
                             **diagnostic(np.angle(np.linalg.eigvals(Q))/(2*np.pi))))
    print(json.dumps(dict(scope='Finite diagnostic only; frozen nonlinear map not simulated',
                          obstructions=exact_obstruction_checks(),models=rows),indent=2))


if __name__=='__main__':
    main()
