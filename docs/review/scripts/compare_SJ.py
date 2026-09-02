"""Compare S_J between old hardcoded r=4 and new iterative version."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))))
import sys, os, math
import numpy as np
sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import ord_pm
from master_formula import cocycle, rho_tables, weyl_matrix
from master_general import build_terms, precompute, psi_matrix, SJ_iterative

A, N, F = [2, 1, 1, 1], 101, [(1, 0)]
k, sg = ord_pm(A, N); K = k if sg > 0 else 2 * k
info, Bm, SIG, U = cocycle(A, N, K)
RH, _ = rho_tables(N, K, U)
rng = np.random.default_rng(1)
cs = {n: (rng.normal() + 1j*rng.normal())/math.sqrt(2) for n in F}

terms = build_terms(F, cs)
G, SPH, CO = precompute(N, K, Bm, SIG, terms)
PSI = psi_matrix(N, G)
gg = G
n = len(CO)

# Brute-force quadruple loop (reference)
def S_J_brute(J):
    rho = RH[J]
    tot = 0+0j
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    ph = (int(SPH[a])+int(SPH[b])+int(SPH[c])+int(SPH[d])
                          + int(PSI[a,b])+int(PSI[a,c])+int(PSI[a,d])
                          + int(PSI[b,c])+int(PSI[b,d])+int(PSI[c,d])) % (2*N)
                    gv = (gg[a]+gg[b]+gg[c]+gg[d]) % N
                    tot += (CO[a]*CO[b]*CO[c]*CO[d]
                            * np.exp(1j*np.pi*ph/N)
                            * np.exp(1j*np.pi*float(rho[gv[0],gv[1]])/N))
    return tot / K**4

for J in [1, 2]:
    sj_ref = S_J_brute(J)
    sj_new = SJ_iterative(N, K, G, SPH, CO, PSI, RH[J], 4)
    print(f"J={J}: |ref|={abs(sj_ref):.6e}  |new|={abs(sj_new):.6e}  "
          f"|diff|={abs(sj_ref-sj_new):.3e}")
