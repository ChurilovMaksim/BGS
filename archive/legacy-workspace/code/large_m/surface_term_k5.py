"""RUN 86.2 -- O(K^2/N) SURFACE-TERM COEFFICIENT FROM e_{2k} ACROSS DESIGNS.

R85 handoff item (b): extract the leading O(K^2/N) surface-term coefficient
from the deviation columns at fixed-K N-sweep.

Key observation from R86.1: e_{2k}/N^k = C_k (1 - delta_k) where delta_k grows
slowly with k.  The R82.35 picture predicts delta_k ~ c_k * K^2 / N + O(K^4/N^2)
for the cubic-surface family second moment (k=4) and a Katz-suppressed analog
for higher k.

Strategy: compute e_{2k}/N^k for k = 1..5 on as many (N, K) designs as possible,
then fit delta_k = C * K^2 / N against the data and report the leading
coefficient C.

Two-key discipline preserved: matrix-product pipeline (R82.12/R85/R86.1).

Output: artifacts/diagnostics/surface_term_k5.json + .log
"""
import json
import math
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "artifacts", "diagnostics")
os.makedirs(OUT_DIR, exist_ok=True)
LOG = os.path.join(OUT_DIR, "surface_term_k5.log")


def log(msg):
    line = str(msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def dlog_table(N, g):
    tab = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        tab[x] = s
        x = x * g % N
    return tab


def primitive_root(N):
    for g in range(2, N):
        x, seen = 1, set()
        for _ in range(N - 1):
            x = x * g % N
            seen.add(x)
            if len(seen) < _ + 1:
                break
        if len(seen) == N - 1:
            return g
    raise RuntimeError


def ord_N(a, N):
    x, k = a % N, 1
    while x != 1:
        x = x * a % N
        k += 1
    return k


def find_a_with_ord(N, target_K):
    """Find a with ord_N(a) = target_K, scanning primes 2..N-1."""
    for cand in range(2, N):
        if ord_N(cand, N) == target_K:
            return cand
    return None


def measure_moments(N, a, K):
    """Return dict e_{2k}/N^k for k=1..5 over the full q-curve.

    Cost: ~ (N-1) * m^2 * N exp.
    """
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ell = int(dlog[a])
    d = math.gcd(ell, N - 1)
    mod = (N - 1) // d
    ks = np.array([k for k in range(N - 1) if k % mod == 0], dtype=np.int64)
    m = len(ks)
    xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))
    sums = {f"k{k}": 0.0 for k in range(1, 6)}
    nq = N - 1
    for q in range(1, N):
        ph = np.exp(2j * np.pi * (q * xs % N) / N)
        J = (W * ph) @ V.T
        aJ = np.abs(J)
        for k in range(1, 6):
            sums[f"k{k}"] += (aJ ** (2*k)).mean()
    res = {"N": N, "a": int(a), "K": K, "m": m}
    for k in range(1, 6):
        res[f"e_{2*k}/N^{k}"] = sums[f"k{k}"] / nq / N**k
    return res


# design set: primes with small odd K; we want a wide range of K^2/N ratios
# so the K^2/N slope is fit-able.
# N=37,K=18; N=53,K=13; N=199,K=33; N=3571,K=17; N=14281,K=??
# Let me build a script that searches for split primes with K odd, 8<=K<=60
DESIGN_CANDIDATES = [37, 53, 199, 521, 3571, 14281]


def main():
    t0 = time.time()
    log("RUN 86.2 -- surface-term coefficient from e_{2k} across designs")
    out = {"designs": []}
    catalan = [1.0, 2.0, 5.0, 14.0, 42.0]
    for N in DESIGN_CANDIDATES:
        # find a with small odd ord; we want m as large as feasible
        best_K = None
        best_m = 0
        best_a = None
        for cand in range(2, N):
            K = ord_N(cand, N)
            if K % 2 == 0 or K < 8 or K > 80:
                continue
            g = primitive_root(N)
            dlog = dlog_table(N, g)
            ell = int(dlog[cand])
            d = math.gcd(ell, N - 1)
            m = d
            if m > best_m:
                best_K, best_m, best_a = K, m, cand
        if best_a is None:
            log(f"   N={N}: no suitable K, skipping")
            continue
        log(f"   design: N={N}, a={best_a}, K={best_K}, m={best_m}")
        # compute moments; budget: at m=210 N=3571 took 60s; at m=6 N=199 should be fast
        # at m=N/2-ish (K=2) too expensive on full N; skip if m*(N-1)*N > 1e9
        cost = best_m * best_m * (N - 1)
        if cost > 5e8:
            log(f"   skipping (cost {cost:.2e} > 5e8)")
            continue
        row = measure_moments(N, best_a, best_K)
        # deviations from Catalan
        devs = []
        for k in range(1, 6):
            v = row[f"e_{2*k}/N^{k}"]
            c = catalan[k - 1]
            devs.append(v - c)
        row["dev_catalan"] = devs
        row["K2_over_N"] = best_K**2 / N
        log("   " + json.dumps(row))
        out["designs"].append(row)
    # fit delta_k = c_k * K^2 / N + O(K^4 / N^2)
    # simple linear fit: delta_k = c_k * (K^2/N)
    log("--- surface-term fit: delta_k = c_k * K^2/N + O(K^4/N^2) ---")
    if len(out["designs"]) >= 2:
        ks = np.array([d["K2_over_N"] for d in out["designs"]])
        # for each k, fit delta = c * k2/n
        coefs = {}
        for k_idx in range(5):
            deltas = np.array([d["dev_catalan"][k_idx] for d in out["designs"]])
            # linear regression without intercept: c = sum(d*k2n) / sum(k2n^2)
            num = float((deltas * ks).sum())
            den = float((ks * ks).sum())
            c = num / den if den > 0 else float('nan')
            coefs[f"k={k_idx+1}"] = c
            log(f"   k={k_idx+1}: c_k = {c:.4f}")
        out["surface_term_coefs"] = coefs
    out["walltime_s"] = time.time() - t0
    with open(os.path.join(OUT_DIR, "surface_term_k5.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log("artifact written")


if __name__ == "__main__":
    main()