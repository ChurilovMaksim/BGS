"""E_theta|Tr U^m|^2 (brute force, single mode k=1, uniform phase) vs Psi_m(t_p) (n-sum, exact in theta)
   vs orbit-pair formula at t* ; and the 1/p coefficient."""

if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import sys, numpy as np
from math import gcd
from scipy.special import jv
import core
from d1_check import Aform, tp
from structure import rad_elems, supp_via_rad

def psi_nsum(dat, t, eta_a, Nt, NA=None):
    m = dat['m']
    N, A = NA if NA is not None else Aform(dat, Nt)
    n = np.arange(-Nt, Nt+1)
    gh = (1j**n)*jv(n, eta_a)                    # Fourier coeff of exp(i eta a cos(2 pi y + th)) at th=0
    G = np.ones(len(N), dtype=complex)
    for j in range(m): G *= gh[N[:, j]+Nt]
    tot = N.sum(axis=1)
    val = G*np.exp(2j*np.pi*t*A)
    CN = np.bincount(tot - tot.min(), weights=val.real) + 1j*np.bincount(tot - tot.min(), weights=val.imag)
    return (np.abs(CN)**2).sum()

def brute(m, p, eta_a, Q=96):
    M = core.Mp(p); x = np.arange(p); acc = 0
    for th in 2*np.pi*np.arange(Q)/Q:
        U = np.exp(1j*eta_a*np.cos(2*np.pi*x/p + th))[:, None]*M
        acc += abs(core.trace_powers(U, m)[m])**2
    return acc/Q

def psi_orbit(dat, s, eta_a, W, B, supp=None):
    D = dat['D']
    ph = core.phihat(dat, s, W, B)
    sel = np.abs(ph) > 1e-9
    ph = ph[sel]; S1 = core.Sk(W[sel], D, 1)
    K = jv(0, eta_a*np.abs(S1[:, None]-S1[None, :]))
    return np.real(ph.conj() @ K @ ph)

if __name__ == '__main__':
    eta_a = 1.0
    for m in (3, 4, 5):
        dat = core.data(m); D = dat['D']; Nt = {3: 25, 4: 13, 5: 9}[m]
        NA = Aform(dat, Nt)
        W = core.enum_fix(dat); B = core.enum_V(dat)
        print(f"== m={m} D={D} g'={dat['gp']}")
        for p in [5, 11, 13, 29, 31, 101]:
            if gcd(p, D) != 1: continue
            if m == 5 and p > 31: continue
            e = brute(m, p, eta_a); ps = psi_nsum(dat, tp(dat, p), eta_a, Nt, NA)
            print(f"  p={p}: brute E={e:.12f}  Psi(t_p)={ps:.12f}  diff={e-ps:.1e}", flush=True)
        for p in [101, 197, 401, 797, 1601, 3203]:
            if gcd(p, D) != 1: continue
            t = tp(dat, p); pbar = pow(p, -1, D); s = (-pbar) % D; tstar = s/D
            assert abs(((t - tstar - 1/(p*D)) + 0.5) % 1 - 0.5) < 1e-12
            P0 = psi_nsum(dat, tstar, eta_a, Nt, NA); Pp = psi_nsum(dat, t, eta_a, Nt, NA)
            Po = psi_orbit(dat, s, eta_a, W, B) if m <= 5 else float('nan')
            h = 1e-6
            dP = (psi_nsum(dat, tstar+h, eta_a, Nt, NA) - psi_nsum(dat, tstar-h, eta_a, Nt, NA))/(2*h)
            c1 = dP/D
            print(f"  p={p} (p mod g'={p % dat['gp']}): Psi(t*) nsum={P0:.10f} orbit={Po:.10f} | p(Psi(t_p)-Psi(t*))={p*(Pp-P0):.5f} | c1=Psi'(t*)/D={c1:.5f} | p^2*(E-Psi*-c1/p)={p*p*(Pp-P0-c1/p):.3f}", flush=True)
