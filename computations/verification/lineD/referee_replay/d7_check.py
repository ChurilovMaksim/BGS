if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, itertools
from fractions import Fraction
from scipy.special import j0
import core
def classes(p, m):
    M = core.Mp(p); Z = {}
    for x in itertools.product(range(p), repeat=m):
        K = np.prod([M[x[j], x[(j+1) % m]] for j in range(m)])
        key = tuple(sorted(x)); Z[key] = Z.get(key, 0) + K
    keys = list(Z); N = np.zeros((len(keys), p))
    for i, k in enumerate(keys):
        for z in k: N[i, z] += 1
    return keys, np.array([Z[k] for k in keys]), N
def E_band(p, Zc, N, eta, a, ens, Ks=None):
    if Ks is None: Ks = range(1, (p-1)//2+1)
    w = np.ones((len(Zc), len(Zc)))
    for k in Ks:
        S = N @ np.exp(2j*np.pi*k*np.arange(p)/p); d = np.abs(S[:, None]-S[None, :])
        w *= np.exp(-(eta*a*d)**2/4) if ens == 'G' else j0(eta*a*d)
    return np.real(Zc.conj() @ w @ Zc)
rng = np.random.default_rng(7)
for p, m, ref in [(5, 3, None), (7, 3, Fraction(235, 49)), (11, 3, Fraction(631, 121)), (13, 3, Fraction(901, 169)), (7, 4, Fraction(1829, 343)), (5, 4, None)]:
    keys, Zc, N = classes(p, m)
    ELC = np.real((np.abs(Zc)**2).sum())
    line = f"p={p} m={m}: E_LineC(enum)={ELC:.12f}" + (f" ref={float(ref):.12f} diff={ELC-float(ref):.1e}" if ref else "")
    print(line, flush=True)
    for eta_a in (0.5, 1.0, 2.0, 4.0):
        EG = E_band(p, Zc, N, eta_a, 1.0, 'G'); EJ = E_band(p, Zc, N, eta_a, 1.0, 'J0')
        X = 2*m*eta_a; beta = min(0.2, 0.2676/X**2)
        bG = p**m*np.exp(-eta_a**2*p/4); bJ = p**m*np.exp(-beta*eta_a**2*p)
        print(f"   eta*a={eta_a}: |E_G-E_LC|={abs(EG-ELC):.3e} (bound {bG:.2e}, ok={abs(EG-ELC)<=bG})  |E_J0-E_LC|={abs(EJ-ELC):.3e} (bound {bJ:.2e}, ok={abs(EJ-ELC)<=bJ})", flush=True)
    if p == 7 and m == 3:
        # brute-force Monte Carlo with the literal band-limited kick, J0 ensemble, eta*a = 1
        M = core.Mp(p); x = np.arange(p); K = (p-1)//2; S = 40000; vals = np.empty(S)
        for i in range(S):
            th = rng.uniform(0, 2*np.pi, K)
            V = sum(np.cos(2*np.pi*k*x/p + th[k-1]) for k in range(1, K+1))
            U = np.exp(1j*1.0*V)[:, None]*M
            vals[i] = abs(np.trace(U @ U @ U))**2
        print(f"   MC literal kick J0 eta*a=1: {vals.mean():.4f} +- {vals.std()/np.sqrt(S):.4f} vs formula {E_band(p, Zc, N, 1.0, 1.0, 'J0'):.4f}")
