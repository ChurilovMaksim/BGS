"""c1 for the uniform-phase (J0) ensemble, single mode k=1, a=1: theta-quadrature of E[G(xi)conjG(xi')beta(xi)]; validated by d/dt of the n-sum."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import numpy as np, sys
from d4_d6 import *
from psi_check import psi_nsum
from d1_check import Aform
def c1_j0(dat, ph, Ws, eta, Q):
    D, m = dat['D'], dat['m']; Hinv = np.array(dat['X'], dtype=float)/D; h0 = Hinv[0, 0]
    S1 = core.Sk(Ws, D, 1); tot = 0
    for th in 2*np.pi*np.arange(Q)/Q:
        y = 2*np.pi*Ws/D + th
        vp = -2*np.pi*np.sin(y); vpp = -4*np.pi**2*np.cos(y)
        beta = 1j*eta*h0*vpp.sum(1) - eta**2*np.einsum('ai,ij,aj->a', vp, Hinv, vp)
        G = np.exp(1j*eta*np.real(np.exp(1j*th)*S1))
        tot = tot + (ph*G*beta)[:, None]*np.conj(ph*G)[None, :]
    return 2/np.pi*np.imag(tot.sum())/Q
m = 3; dat, W, B = setup(m); D = dat['D']
sd = [(s, *supp_data(dat, s, W, B)) for s in units_lifts(dat)]
for eta in (1, 4, 8):
    Nt = int(3*eta+25); NA = Aform(dat, Nt); s, ph, Ws = sd[1]; h = 1e-6
    num = (psi_nsum(dat, s/D+h, eta, Nt, NA) - psi_nsum(dat, s/D-h, eta, Nt, NA))/(2*h)/D
    print(f"validate eta={eta} s={s}: quadrature c1={c1_j0(dat, ph, Ws, eta, Q=max(64, 24*eta)):.6f}  numeric d/dt={num:.6f}", flush=True)
for eta in (1, 4, 16, 64, 256, 1024):
    vals = [c1_j0(dat, ph, Ws, eta, Q=max(64, 24*eta)) for s, ph, Ws in sd]
    print(f"J0 m=3 K=1 (separating, gap 0.753) eta={eta}: max_s|c1|={max(abs(v) for v in vals):.4f}   G-ensemble for comparison: {max(abs(c1_gauss(dat, ph, Ws, [1], [1.0], eta)) for s, ph, Ws in sd):.3e}", flush=True)
