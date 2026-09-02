"""
Run 73: how much slack is there in the T18 barrier?
==================================================

By Lemma F the moment error is

    theta_r = (m K)^{-1} sum_{J != 0} lam^{-J} Tr(U^J) . S_J(r),
    S_J(r)  = sum_v  a_v  w^{Q_J(v)},        a = Weyl coefficients of Vbar^r,

and T8's bound comes from |S_J| <= ||a||_1 <= C^r.  The question that decides
whether the barrier is breakable is: how large is |S_J| ACTUALLY?

Three reference sizes are compared:
    ||a||_1                     -- the T8 bound (no cancellation at all)
    ||a||_2 sqrt(|supp a|)      -- Cauchy-Schwarz (no cancellation either)
    ||a||_2                     -- full square-root cancellation
If |S_J| tracks ||a||_2 the barrier is soft and the moment method can be pushed;
if it tracks ||a||_1 the barrier is hard.

Weyl transform.  With T(-v)_{x,y} = w^{-v_2 x - v_1 v_2 / 2} [y = x + v_1],
    a_v = N^{-1} Tr(T(-v) X) = N^{-1} w^{-v_1 v_2/2} sum_x w^{-v_2 x} X[x+v_1, x],
so for each shift v_1 the v_2-dependence is a DFT: the whole transform costs
O(N^2 log N).
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                     # noqa: E402
from lemmaF_quadratic_phase import inv2, sigma, qval      # noqa: E402


def weyl_coeffs(X, N, two_inv):
    """a[v1, v2] = N^{-1} Tr(T(-v) X)."""
    idx = np.arange(N)
    D = np.empty((N, N), dtype=complex)
    for v1 in range(N):
        D[v1, :] = X[(idx + v1) % N, idx]
    F = np.fft.fft(D, axis=1)                     # sum_x w^{-v2 x} D[v1, x]
    ph = np.exp(-2j * np.pi * ((np.outer(idx, idx) * two_inv) % N) / N)
    return F * ph / N


def main():
    rng = np.random.default_rng(7355608)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}
    for A, N in [([[2, 1], [1, 1]], 41), ([[2, 1], [1, 1]], 101),
                 ([[5, 2], [2, 1]], 71)]:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        U = cm.U_matrix()
        two_inv = pow(2, -1, N)
        Am = np.array(A, dtype=np.int64) % N
        Upow = [np.eye(N, dtype=complex)]
        for _ in range(K):
            Upow.append(Upow[-1] @ U)
        # observable: a single Weyl orbit (real symbol), the T20 object
        u = (int(rng.integers(1, N)), int(rng.integers(1, N)))
        Vfull = cm.T_matrix(u) + cm.T_matrix(((-u[0]) % N, (-u[1]) % N))
        Vbar = sum(Upow[j] @ Vfull @ Upow[j].conj().T for j in range(K)) / K
        # precompute the quadratic phases Q_J
        QJ = {}
        for J in range(1, K):
            BJ = (np.linalg.matrix_power(Am, J) % N).T % N
            BJi = inv2(BJ, N)
            D = (BJi - np.eye(2, dtype=np.int64)) % N
            det = (int(D[0, 0]) * int(D[1, 1]) - int(D[0, 1]) * int(D[1, 0])) % N
            if det == 0:
                continue
            di = pow(det, -1, N)
            Di = np.array([[int(D[1, 1]) * di % N, -int(D[0, 1]) * di % N],
                           [-int(D[1, 0]) * di % N, int(D[0, 0]) * di % N]],
                          dtype=np.int64) % N
            v1 = np.repeat(np.arange(N), N)
            v2 = np.tile(np.arange(N), N)
            mv0 = (-(Di[0, 0] * v1 + Di[0, 1] * v2)) % N
            mv1 = (-(Di[1, 0] * v1 + Di[1, 1] * v2)) % N
            s1 = (mv1 * v1 - mv0 * v2) % N
            b0 = (BJi[0, 0] * mv0 + BJi[0, 1] * mv1) % N
            b1 = (BJi[1, 0] * mv0 + BJi[1, 1] * mv1) % N
            s2 = (b1 * mv0 - b0 * mv1) % N
            Q = (s1 - two_inv * s2) % N
            QJ[J] = np.exp(2j * np.pi * Q.reshape(N, N) / N)
        rows = []
        X = np.eye(N, dtype=complex)
        for r in range(1, 9):
            X = X @ Vbar
            a = weyl_coeffs(X, N, two_inv)
            l1 = float(np.abs(a).sum())
            l2 = float(np.sqrt((np.abs(a) ** 2).sum()))
            supp = int((np.abs(a) > 1e-12 * max(np.abs(a).max(), 1e-300)).sum())
            best = 0.0
            SJ = []
            for J, ph in QJ.items():
                S = complex((a * ph).sum())
                SJ.append(abs(S))
                best = max(best, abs(S))
            SJ = np.array(SJ)
            rows.append({"r": r, "l1": l1, "l2": l2, "support": supp,
                         "cs_bound": l2 * np.sqrt(max(supp, 1)),
                         "max_abs_S_J": float(SJ.max()),
                         "mean_abs_S_J": float(SJ.mean()),
                         "ratio_to_l1": float(SJ.max() / l1) if l1 else None,
                         "ratio_to_cs": float(SJ.max()
                                              / (l2 * np.sqrt(max(supp, 1)))),
                         "ratio_to_l2": float(SJ.max() / l2) if l2 else None})
            rr = rows[-1]
            print(f"  A={A} N={N} r={r}: |supp|={supp:>6}  ||a||_1={l1:.4e}  "
                  f"||a||_2={l2:.4e}  max_J|S_J|={SJ.max():.4e}   "
                  f"S/l1={rr['ratio_to_l1']:.3e}  S/(l2 sqrt|supp|)="
                  f"{rr['ratio_to_cs']:.3f}  S/l2={rr['ratio_to_l2']:.3f}")
            sys.stdout.flush()
        out["rows"].append({"A": A, "N": N, "K": K, "u": list(u), "data": rows})

    # verdict: does |S_J| behave like l1 (hard barrier) or l2 (soft)?
    rr = []
    for row in out["rows"]:
        for d in row["data"]:
            if d["r"] >= 4:
                rr.append((d["ratio_to_l1"], d["ratio_to_l2"]))
    rr = np.array(rr)
    out["verdict"] = {
        "mean_S_over_l1_for_r_ge_4": float(rr[:, 0].mean()),
        "mean_S_over_l2_for_r_ge_4": float(rr[:, 1].mean()),
        "reading": ("|S_J| is far below the l^1 bound and of the order of "
                    "||a||_2, i.e. the T8 bound is very lossy and the barrier is "
                    "soft in this diagnostic"
                    if rr[:, 0].mean() < 0.1 else
                    "|S_J| is comparable to the l^1 bound: the barrier is hard"),
    }
    print()
    print("VERDICT:", json.dumps(out["verdict"], indent=1))
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r73", "barrier_slack.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
