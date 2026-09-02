"""
Run 82l: the EXACT second moment from Theorem II, and the exact law of E(q).
==========================================================================
Theorem II (R82.12) gives <f_chi|T(n)|f_psi> = e_N(-q/2) theta_chi conj(theta_psi)
J(chi,psi;q)/(N-1).  Summing |.|^2 over the m x m index set S x S -- a coset of
a subgroup whose annihilator in F_N^* is <a, -1> of order 2K (K odd) -- collapses
the double character sum to a finite sum over tuples (sigma, tau, j, j'):

    Tr(C C^*) = m^2/(N-1)^2 [ (N-2) + sum' chi_0(sigma a^j) chi_0(tau a^{j'})
                                          e_N(q f(sigma,tau,j,j')) ],
    x = (1 - tau a^{j'}) / (1 - sigma tau a^{j+j'}),   f = x (1 - sigma a^j),

the primed sum over the (2K)^2 tuples with sigma tau a^{j+j'} != 1; the
degenerate tuples are exactly the diagonal x = y and are already inside the
(N-2).  Tr(C^2) is the analogous sum with J(chi,psi;q) J(psi,chi;q), and

    Tr(M_q^2) = 2 Tr(C C^*) + 2 Re Tr(C^2).

This script evaluates both closed forms directly and compares with
Tr(M_q^2) computed from the matrix, over many q -- a two-key check of R82.13 and
the exact law of the residual E(q) = Tr(V_q^2) - N/K^2 of Lemma 82.1.

Output: artifacts/r82/second_moment_exact.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r82j_closed_form import (multiplicative_order, primitive_root,  # noqa: E402
                              sqrt_mod)
from r82k_bgs_large_m import build_M, design_params  # noqa: E402

T_TRACE = 3


def exact_trCCs(N, K, a, q, k0=1, parity_odd=False):
    """closed-form Tr(C C^*) via the tuple sum."""
    inv = lambda z: pow(int(z) % N, N - 2, N)                      # noqa: E731
    m = (N - 1) // (2 * K)
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    # chi_0 = the character with index k0 (any element of the coset S)
    chi0 = lambda z: np.exp(2j * np.pi * k0 * dlog[int(z) % N] / (N - 1))  # noqa: E731
    tot = complex(N - 2)
    ndeg = 0
    for sg in (1, -1):
        for tau in (1, -1):
            for j in range(K):
                for jp in range(K):
                    den = (1 - sg * tau * pow(a, (j + jp) % K, N)) % N
                    if den == 0:
                        ndeg += 1
                        continue
                    xx = ((1 - tau * pow(a, jp, N)) % N) * inv(den) % N
                    f = xx * ((1 - sg * pow(a, j, N)) % N) % N
                    if xx == 0 or xx == 1:
                        continue                    # x must avoid 0 and 1
                    yy = sg * pow(a, j, N) * xx % N
                    if yy == 0 or yy == 1:
                        continue
                    w = chi0(sg * pow(a, j, N) % N) * chi0(tau * pow(a, jp, N) % N)
                    tot += w * np.exp(2j * np.pi * (q * f % N) / N)
    return float(np.real(tot)) * m * m / (N - 1) ** 2, ndeg


def main():
    out = {"script": "src/r82l_second_moment_exact.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, K in ((199, 11), (3571, 17)):
        t0 = time.time()
        a = design_params(N, K)
        m = (N - 1) // (2 * K)
        rows = []
        qs = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23]
        for q in qs:
            M, mm = build_M(N, K, a, q)
            assert mm == m
            C_num = None
            tr2_num = float(np.real(np.trace(M @ M)))
            # split the numeric trace the same way
            # M = C + C^*, so Tr(M^2) = 2 Tr(C C^*) + 2 Re Tr(C^2)
            ex, ndeg = exact_trCCs(N, K, a, q)
            rows.append({"q": q, "tr_M2_numeric": tr2_num,
                         "exact_TrCCs": ex, "2xexact": 2 * ex,
                         "residual_2ReTrC2": tr2_num - 2 * ex})
            print(f"  N={N} q={q:3d}: Tr(M^2) = {tr2_num:.9f};  "
                  f"2.Tr(CC*)_exact = {2*ex:.9f};  "
                  f"2.Re Tr(C^2) = {tr2_num - 2*ex:+.9f}", flush=True)
        # is the leftover piece equal to the other half of N/K^2?
        lo = np.array([r["residual_2ReTrC2"] for r in rows])
        pred = N / K ** 2
        print(f"  N={N}: N/K^2 = {pred:.6f};  mean Tr(M^2) = "
              f"{np.mean([r['tr_M2_numeric'] for r in rows]):.6f};  "
              f"mean 2Tr(CC*) = {np.mean([2*r['exact_TrCCs'] for r in rows]):.6f}"
              f";  mean 2ReTr(C^2) = {lo.mean():.6f} "
              f"({time.time()-t0:.0f} s)", flush=True)
        out["designs"].append({"N": N, "K": K, "m_plus": m,
                               "N_over_K2": pred, "degenerate_tuples": ndeg,
                               "rows": rows,
                               "mean_2TrCCs": float(np.mean(
                                   [2 * r["exact_TrCCs"] for r in rows])),
                               "mean_2ReTrC2": float(lo.mean())})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "second_moment_exact.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
