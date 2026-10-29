"""D1 pathwise and in expectation: brute-force matrix traces vs n-sum formula (independent code)."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np, itertools
from math import gcd
import core
from scipy.special import jv

def ghat(modes, amps, thetas, eta, L=1024, Nt=20):
    y = np.arange(L)/L
    V = sum(a*np.cos(2*np.pi*k*y + th) for k, a, th in zip(modes, amps, thetas))
    c = np.fft.fft(np.exp(1j*eta*V))/L          # c[n] = int g(y) e(-n y) dy
    n = np.arange(-Nt, Nt+1)
    return n, c[n % L]

def Aform(dat, Nt):
    m = dat['m']; X = np.array(dat['X'], dtype=np.int64)
    n = np.arange(-Nt, Nt+1)
    grids = np.meshgrid(*([n]*m), indexing='ij')
    N = np.stack([g.ravel() for g in grids], axis=1)
    A = 2*np.einsum('bi,ij,bj->b', N, X, N)
    return N, A

def nsum(dat, gh, Nt, t, NA=None):
    m = dat['m']
    if NA is None: NA = Aform(dat, Nt)
    N, A = NA
    G = np.ones(len(N), dtype=complex)
    for j in range(m): G *= gh[N[:, j] + Nt]
    # e(t A) with t = r/q exact rational reduction
    return (G*np.exp(2j*np.pi*t*A)).sum()

def tp(dat, p):
    D = dat['D']; return (pow(D, -1, p) % p)/p

def run(m, p, modes, amps, eta, ntheta=6, Nt=None, seed=1):
    dat = core.data(m); D = dat['D']
    assert gcd(p, D) == 1
    if Nt is None: Nt = {3: 30, 4: 14, 5: 9}[m]
    NA = Aform(dat, Nt)
    M = core.Mp(p); trM = core.trace_powers(M, m)[m]
    rng = np.random.default_rng(seed)
    x = np.arange(p)
    t = tp(dat, p)
    worst = 0
    for it in range(ntheta):
        th = rng.uniform(0, 2*np.pi, len(modes))
        V = sum(a*np.cos(2*np.pi*k*x/p + h) for k, a, h in zip(modes, amps, th))
        U = np.exp(1j*eta*V)[:, None]*M
        tr = core.trace_powers(U, m)[m]
        n, gh = ghat(modes, amps, th, eta, Nt=Nt)
        f = trM*nsum(dat, gh, Nt, t, NA)
        worst = max(worst, abs(tr - f))
    print(f"m={m} p={p} modes={modes} amps={amps} eta={eta}: |TrM^m|={abs(trM):.15f}  max_theta |TrU^m - TrM^m*nsum| = {worst:.2e} (Nt={Nt})", flush=True)

if __name__ == '__main__':
    for m, ps in [(3, [5, 11, 13, 29, 101]), (4, [5, 7, 11, 13, 29]), (5, [3, 7, 11, 13])]:
        for p in ps:
            run(m, p, [1], [1.0], 1.0)
            run(m, p, [1, 2], [1.0, 0.7], 0.8)
    # p | D_m: formula hypothesis violated
    for m, p in [(3, 7), (4, 3)]:
        M = core.Mp(p); print(f"p | D_m case m={m} p={p}: |Tr M^m| = {abs(core.trace_powers(M, m)[m]):.6f}")
