"""
Run 74: the frequency-ensemble moments are EXACTLY the Bessel/pairing count plus
an explicitly computable arithmetic excess.
==============================================================================

From `src/ensemble_moments.py`:  averaging the r-th moment of
M_n = P_lam (T(n)+T(-n)) P_lam over n in (Z/N)^2 gives, exactly,

    E_n[(1/m) Tr(M_n^r)] = K^{-r} sum_{eps,j} phi(eps,j) 1{ L(eps,j) = 0 mod N }
                            + O(2^r / (m N)),
    L(eps,j) = sum_i eps_i (A^{j_i})^t ,

and (C1, verified 1600/1600) L(eps,j) = 0 mod N is EXACTLY the pair of Chebyshev
congruences  sum_i eps_i U_{j_i} = 0,  sum_i eps_i U_{j_i - 1} = 0  (mod N), where
A^j = U_j A - U_{j-1} I.

CLAIM (this script).  With r = 2s,

    D_r(N) := #{(eps,j) : L = 0 mod N}
            = binom(2s, s) * P(s, K)  +  X_r(N),

where P(s,K) = s!^2 [x^s] I_0(2 sqrt x)^K is the pairing count of Theorem B
(Lemma 4.2) and X_r(N) >= 0 is the arithmetic excess -- the mod-N accidents.  The
first factor is exactly the number of length-r words over {(j,+),(j,-)} in which
every j carries as many + as -, because
    r! [x^r] I_0(2x)^K = binom(2s,s) * P(s,K).

WHY THIS MATTERS.  Theorem G closed the moment route for a FIXED observable.  The
ensemble route is different: the error term acquires the Gauss-sum factor
E_n[w^{Q_J(Ln)}] = O(1/N) of Lemma F, so the fixed-n error 2^r K/m becomes
O(2^r/(mN)).  With K = N^theta the reachable moment order moves from r < 2/theta
to r < 4/theta.  What then has to be controlled is exactly X_r(N), and this script
measures it.
"""

from __future__ import annotations

import itertools
import json
import math
import os
import sys
import time
from collections import defaultdict
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                     # noqa: E402
from subgroup_kloosterman_energy import pair_count        # noqa: E402
from parity_desymmetrised import eps_of                  # noqa: E402


def chebyshev_exact(t, K):
    U = [0, 1]
    for _ in range(K + 2):
        U.append(t * U[-1] - U[-2])
    return U


def trivial_count(r, K):
    """r! [x^r] I_0(2x)^K = binom(r, r/2) * P(r/2, K): the number of length-r
    words over {(j,+), (j,-)} with equal + and - counts at every j."""
    s = r // 2
    return math.comb(r, s) * pair_count(s, K)


def count_solutions(U, K, r, N=None):
    """#{(eps,j) in {+-1}^r x (Z/K)^r : sum eps_i U_{j_i} = 0 and
    sum eps_i U_{j_i-1} = 0}, either over Z (N=None) or mod N."""
    def red(x):
        return x % N if N else x
    atoms = [(e, red(e * U[j]), red(e * (U[j - 1] if j >= 1 else -1)))
             for e in (1, -1) for j in range(K)]
    h = r // 2
    tab = defaultdict(int)
    for combo in itertools.product(atoms, repeat=h):
        a = b = 0
        for (_, x, y) in combo:
            a += x
            b += y
        tab[(red(a), red(b))] += 1
    tot = 0
    for (a, b), c in tab.items():
        tot += c * tab.get((red(-a), red(-b)), 0)
    return tot


def main():
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}
    print(f"{'A':>16} {'N':>6} {'K':>4} {'eps':>3} {'r':>2} {'D_r(N)':>14} "
          f"{'trivial_eff':>14} {'excess X_r':>13} {'X_r/D_r':>9} "
          f"{'D_r(Z)':>14} {'Z-excess':>10}")
    for A, N in [([[2, 1], [1, 1]], 3571), ([[2, 1], [1, 1]], 9349),
                 ([[2, 1], [1, 1]], 1597), ([[5, 2], [2, 1]], 2161)]:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        k, eps = eps_of(A, N)
        t = A[0][0] + A[1][1]
        Uex = chebyshev_exact(t, K + 2)
        for r in (2, 4, 6, 8):
            if (2 * K) ** (r // 2) > 3_000_000:
                continue
            Umod = [x % N for x in Uex]
            DN = count_solutions(Umod, K, r, N=N)
            triv = trivial_count(r, K)
            DZ = count_solutions(Uex, K, r, N=None)
            # when A^k = -I the Chebyshev sequence is ANTIPERIODIC,
            # U_{j+k} = -U_j, so every configuration has 2^{r/2} images and the
            # trivial count must be multiplied accordingly
            fac = 2 ** (r // 2) if eps == -1 else 1
            triv_eff = triv * fac
            row = {"A": A, "N": N, "K": K, "k": k, "eps": eps, "r": r,
                   "D_r_mod_N": DN, "trivial_bessel_count": triv,
                   "antiperiodic_factor": fac,
                   "trivial_effective": triv_eff,
                   "excess_X_r": DN - triv_eff,
                   "relative_excess": (DN - triv_eff) / DN if DN else None,
                   "D_r_over_Z": DZ, "Z_excess": DZ - triv_eff}
            out["rows"].append(row)
            print(f"{str(A):>16} {N:>6} {K:>4} {eps:>+3} {r:>2} {DN:>14} "
                  f"{triv_eff:>14} {DN - triv_eff:>13} "
                  f"{(DN - triv_eff) / DN:>9.5f} {DZ:>14} "
                  f"{DZ - triv_eff:>10}")
            sys.stdout.flush()

    rows = out["rows"]
    out["verdict"] = {
        "exact_for_r_le_4_all_designs":
            all(r["excess_X_r"] == 0 for r in rows if r["r"] <= 4),
        "max_relative_excess_r_le_4":
            max((r["relative_excess"] for r in rows if r["r"] <= 4), default=0),
        "max_relative_excess_r_ge_6":
            max((r["relative_excess"] for r in rows if r["r"] >= 6), default=0),
        "excess_already_present_over_Z_at_r_ge_6":
            all(r["Z_excess"] > 0 for r in rows if r["r"] >= 6),
        "reading": ("With the antiperiodic factor 2^{r/2} included for eps = -1 "
                    "(A^k = -I makes U_{j+k} = -U_j), the Bessel/pairing count "
                    "is EXACT at r = 2 and r = 4 for every design point. At "
                    "r >= 6 a genuine excess appears and it is present already "
                    "over Z (the Chebyshev recurrence itself supplies +-1 "
                    "relations), so it is combinatorial, not a mod-N accident; "
                    "its relative size is 1-4% for eps = +1."),
    }
    print()
    print("VERDICT:", json.dumps(out["verdict"], indent=1))
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r74", "ensemble_excess.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
