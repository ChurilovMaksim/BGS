"""RUN 92.1 -- Exact reduction of the k=2 layer of H3 (Sub-Weyl) to
combinatorics.

BACKGROUND.  The trace-fluctuation lemma (R86) needs the variance across q
of the coset second moment A_S(q) = sum_{i,j in S} |J(chi_i,chi_j;q)|^2.
R91.5 found A_S(q) = m^2 (N-2) + fluctuation.  This run closes the k=2
layer EXACTLY:

THEOREM 92.1.  Let S be the character coset trivial on H = <a> (|H| = K),
m = |S| = (N-1)/K.  Then for every q != 0,

    A_S(q) = m^2 [ (N-2) + S_off(q) ],

where

    S_off(q) = sum_{(x,y) in P} e_N(q(x-y)),
    P = {(x,y) in (F_N^*)^2 : x != 1, y != 1, x/y in H, (x-1)/(y-1) in H,
         x != y},

and |P| = (K-1)(K-2) exactly: the constraint set is parametrized by
(u, v) in H^2 with u != v, u != 1, v != 1 via y = (1-v)/(u-v), x = u y
(the diagonal x = y corresponds to u = v = 1 and contributes the constant
(N-2)).

Corollaries:
  mean_q S_off = -|P|/(N-1)                    (geometric sum over q)
  Var_q S_off  = |P| (1 + o(1))                (equidistribution of phases)
  std_q A_S    = m^2 sqrt((K-1)(K-2)) = m(N-1)(1+o(1)).

In particular the k=2 fluctuation is pure combinatorics: no Katz, no Weil.
Relative to the GOE normalization of M_q^S the fluctuation vanishes as
K/sqrt(N) -> 0 along the design scaling.

VERIFICATION (this script):
  1. Exact identity A_S(q) = m^2[(N-2) + S_off(q)] at N=53 for q=1,2,3
     (machine precision).
  2. |P| = (K-1)(K-2) by direct enumeration.
  3. std and mean of S_off over the full q-curve vs the formulas,
     at N=53 and N=199.

Output: data/proof/h3_k2_exact_reduction.json + .log
"""
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "data", "proof")
os.makedirs(OUT_DIR, exist_ok=True)
LOG = os.path.join(OUT_DIR, "h3_k2_exact_reduction.log")

sys.path.insert(0, os.path.join(ROOT, "code", "large_m"))
sys.path.insert(0, os.path.join(ROOT, "code", "theorems"))

from fourth_mixed_moment import dlog_table  # noqa: E402
from theorem_ii_twisted_jacobi import primitive_root  # noqa: E402


def log(msg):
    line = str(msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def subgroup(N, K, g):
    h = pow(g, (N - 1) // K, N)
    H, x = [], 1
    for _ in range(K):
        H.append(x)
        x = x * h % N
    return H


def constraint_pairs(N, H):
    """P = {(x,y): x != y, x/y in H, (x-1)/(y-1) in H}, x,y not in {0,1}."""
    Hset = set(H)
    pairs = []
    for x in range(2, N):
        for y in range(2, N):
            if x == y:
                continue
            if (x * pow(y, N - 2, N)) % N in Hset and \
               ((x - 1) * pow(y - 1, N - 2, N)) % N in Hset:
                pairs.append((x, y))
    return pairs


def run_design(N, a, K):
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    H = subgroup(N, K, g)
    P = constraint_pairs(N, H)
    np_pairs = len(P)
    expected = (K - 1) * (K - 2)
    log(f"N={N} a={a} K={K}: |P|={np_pairs} expected (K-1)(K-2)={expected} "
        f"{'OK' if np_pairs == expected else 'MISMATCH'}")

    xs_arr = np.array([p[0] for p in P], dtype=np.int64)
    ys_arr = np.array([p[1] for p in P], dtype=np.int64)

    ell = int(dlog[a])
    d = math.gcd(ell, N - 1)
    mod = (N - 1) // d
    ks = np.array([k for k in range(N - 1) if k % mod == 0], dtype=np.int64)
    m = len(ks)
    xs_full = np.array([x for x in range(1, N) if x != 1], dtype=np.int64)
    dl_x = dlog[xs_full]
    dl_xm1 = dlog[(xs_full - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))

    dxy = (xs_arr - ys_arr) % N
    S_off = np.array([
        np.exp(2j * np.pi * (q * dxy % N) / N).sum() for q in range(1, N)
    ])
    mean_S = float(S_off.real.mean())
    std_S = float(S_off.real.std())
    pred_mean = -np_pairs / (N - 1)
    pred_std = math.sqrt(np_pairs)

    max_dev = 0.0
    for q in [1, 2, 3]:
        ph = np.exp(2j * np.pi * (q * xs_full % N) / N)
        J = (W * ph) @ V.T
        A = float((np.abs(J) ** 2).sum())
        dev = abs(A - m * m * ((N - 2) + S_off[q - 1].real))
        max_dev = max(max_dev, dev)

    A_vals = m * m * ((N - 2) + S_off.real)
    std_A = float(A_vals.std())
    pred_stdA = m * m * pred_std

    row = {
        "N": N, "a": a, "K": K, "m": m, "n_pairs": np_pairs,
        "identity_max_dev": max_dev,
        "mean_S_off": mean_S, "pred_mean_S_off": pred_mean,
        "std_S_off": std_S, "pred_std_S_off": pred_std,
        "std_A": std_A, "pred_std_A": pred_stdA,
        "std_A_over_mN": std_A / (m * (N - 1)),
    }
    log(f"  identity dev {max_dev:.2e}; mean S {mean_S:.4f} "
        f"(pred {pred_mean:.4f}); std S {std_S:.2f} (pred {pred_std:.2f}); "
        f"std_A/(mN) = {row['std_A_over_mN']:.4f}")
    return row


def main():
    t0 = time.time()
    log("RUN 92.1 -- H3(k=2) exact combinatorial reduction")
    out = {
        "script": "code/verification/h3_k2_exact_reduction.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "designs": [],
    }
    a = 10
    x, kk = a % 53, 1
    while x != 1:
        x = x * a % 53
        kk += 1
    out["designs"].append(run_design(53, a, kk))
    out["designs"].append(run_design(199, 139, 11))
    out["walltime_s"] = time.time() - t0
    with open(os.path.join(OUT_DIR, "h3_k2_exact_reduction.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log("artifact written")


if __name__ == "__main__":
    main()
