"""Strong-kick limit (D4/D5) and 1/p coefficient (D6) from the orbit-pair formula; own derivations."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np
from math import gcd
from scipy.special import jv
import core

def setup(m):
    dat = core.data(m); D = dat['D']
    W = core.enum_fix(dat); B = core.enum_V(dat)
    return dat, W, B

def units_lifts(dat):
    D, gp = dat['D'], dat['gp']; out = []
    for u in range(1, gp):
        if gcd(u, gp) != 1: continue
        s = u
        while gcd(s, D) != 1: s += gp
        out.append(s)
    return out

def supp_data(dat, s, W, B):
    ph = core.phihat(dat, s, W, B); sel = np.abs(ph) > 1e-9
    return ph[sel], W[sel]

def psi(ph, Ws, D, Ks, amps, eta, ens):
    w = np.ones((len(ph), len(ph)))
    for k, a in zip(Ks, amps):
        S = core.Sk(Ws, D, k); d = np.abs(S[:, None]-S[None, :])
        w *= jv(0, eta*a*d) if ens == 'J0' else np.exp(-(eta*a*d)**2/4)
    return np.real(ph.conj() @ w @ ph)

def psi_inf(ph, Ws, D, Ks, tol=1e-8):
    P = np.stack([core.Sk(Ws, D, k) for k in Ks], axis=1)
    lab = -np.ones(len(ph), dtype=int); c = 0
    for i in range(len(ph)):
        if lab[i] >= 0: continue
        same = np.sqrt((np.abs(P - P[i])**2).sum(axis=1)) < tol
        lab[same & (lab < 0)] = c; c += 1
    return sum(abs(ph[lab == j].sum())**2 for j in range(c))

def c1_gauss(dat, ph, Ws, Ks, amps, eta, split=False):
    """c1 = (2/pi) Im sum phi(xi) conj phi(xi') E[G(xi) conj G(xi') beta(xi)], G ensemble, Gaussian identities."""
    D, m = dat['D'], dat['m']
    Hinv = np.array(dat['X'], dtype=float)/D; h0 = Hinv[0, 0]
    n = len(ph)
    hat = lambda u: np.stack([u.real, -u.imag], axis=-1)
    logf = np.zeros((n, n)); mvec = np.zeros((n, n, m), dtype=complex); Ev2 = np.zeros((n, n), dtype=complex)
    C = np.zeros((n, m, m))
    for k, a in zip(Ks, amps):
        sig2 = a*a/2
        S = core.Sk(Ws, D, k); dS = S[:, None]-S[None, :]
        zeta = eta*hat(dS)                                   # (n,n,2)
        logf += -sig2*(zeta**2).sum(-1)/2
        e = np.exp(2j*np.pi*k*Ws/D)                          # (n,m)
        mu = hat(2j*np.pi*k*e)                               # (n,m,2)
        nu = hat((2j*np.pi*k)**2*e)
        mvec += 1j*sig2*np.einsum('abx,aix->abi', zeta, mu)
        Ev2 += 1j*sig2*np.einsum('abx,aix->ab', zeta, nu)
        C += sig2*np.einsum('aix,ajx->aij', mu, mu)
    f = np.exp(logf)
    quad = np.einsum('aij,ij->a', C, Hinv)[:, None] + np.einsum('abi,ij,abj->ab', mvec, Hinv, mvec)
    b = 1j*eta*h0*Ev2 - eta**2*quad
    assert np.abs(b.imag).max() < 1e-8*max(1, np.abs(b).max())
    T = np.imag(ph[:, None]*ph.conj()[None, :])*f*b.real
    if split:
        canon, _ = core.gamma_canon(Ws, D)
        same = np.array([[canon[i] == canon[j] for j in range(n)] for i in range(n)])
        return 2/np.pi*T.sum(), 2/np.pi*T[same].sum(), np.abs(b.real[~same]).max()
    return 2/np.pi*T.sum()
