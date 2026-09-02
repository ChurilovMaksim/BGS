"""RUN 91.19 -- Third GOE spacing design: N=95419, K=57, principal coset m=1674.

The R82 certified design at the largest available prime.  The full coset
has m = (N-1)/K = 1674 characters (the parity-odd half is 837; we use the
FULL principal coset, matching the R87.4 design set).  Per-q cost is
dominated by the J build (~90 s wall on this box); we run 8 q values in
separate chunks with incremental artifact writes.

Output: artifacts/r91/bgs_spacing_N95419.json + .log
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "artifacts", "r91")
os.makedirs(OUT_DIR, exist_ok=True)
LOG = os.path.join(OUT_DIR, "bgs_spacing_N95419.log")

sys.path.insert(0, os.path.join(ROOT, "src", "large_m"))
sys.path.insert(0, os.path.join(ROOT, "src", "theorems"))

from fourth_mixed_moment import (  # noqa: E402
    dlog_table, index_coset, jacobi_matrix,
)
from theorem_ii_twisted_jacobi import (  # noqa: E402
    primitive_root, sqrt_mod, multiplicative_order,
)


def log(msg):
    line = str(msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def unfold_poly(ev, deg=11):
    ev = np.sort(ev)
    n = len(ev)
    y = np.arange(1, n + 1) / (n + 1)
    return n * np.polyval(np.polyfit(ev, y, deg), ev)


def ratios_of(u):
    u = np.sort(u)
    gaps = np.diff(u)
    gaps = gaps / np.mean(gaps)
    if len(gaps) < 3:
        return np.array([])
    return np.array([min(gaps[i], gaps[i + 1]) / max(gaps[i], gaps[i + 1])
                     for i in range(len(gaps) - 1)])


def goe_cdf(s):
    return 1 - np.exp(-np.pi * s ** 2 / 4)


def main():
    t00 = time.time()
    log("RUN 91.19 -- GOE spacing at N=95419 K=57 m=1674")
    N, K = 95419, 57
    roots = [r for r in sqrt_mod(5, N)]
    inv2 = pow(2, N - 2, N)
    a = None
    for r in roots:
        c = (3 + r) * inv2 % N
        if multiplicative_order(c, N) == K:
            a = c
            break
    assert a is not None
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ks = index_coset(N, K, a, dlog)
    m = len(ks)
    log(f"a={a} m={m}")

    inv2N = pow(2, N - 2, N)
    q_list = [1, 5, 11, 19, 29, 43, 61, 89]
    all_gaps = []
    per_q = []
    artifact = {"N": N, "K": K, "a": int(a), "m": int(m), "per_q": [],
                "script": "src/large_m/bgs_spacing_N95419.py"}
    out_path = os.path.join(OUT_DIR, "bgs_spacing_N95419.json")

    for q in q_list:
        t0 = time.time()
        J = jacobi_matrix(N, K, a, dlog, ks, q)
        C = np.exp(-2j * np.pi * (inv2N * q % N) / N) * J / (N - 1)
        M = (C + C.conj().T).real
        ev = np.linalg.eigvalsh(M)
        u = unfold_poly(ev)
        g4 = ratios_of(u)
        all_gaps.extend(g4)
        row = {"q": int(q), "wall_s": time.time() - t0,
               "n_gaps": int(len(g4)),
               "mean_r": float(g4.mean()) if len(g4) else None}
        per_q.append(row)
        artifact["per_q"] = per_q
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump(artifact, fh, indent=1)
        log(f"q={q}: {row['wall_s']:.0f}s, <r>={row['mean_r']:.4f}")

    all_gaps = np.array(all_gaps)
    gs = np.sort(all_gaps)
    n = len(gs)
    D = float(np.max(np.abs(np.arange(1, n + 1) / n - goe_cdf(gs))))
    crit = float(1.358 / np.sqrt(n))
    artifact["n_gaps_total"] = int(n)
    artifact["mean_gap"] = float(all_gaps.mean())
    artifact["ks_D"] = D
    artifact["ks_crit_5pct"] = crit
    artifact["ks_pass"] = D < crit
    artifact["walltime_s"] = time.time() - t00
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(artifact, fh, indent=1)
    log(f"total gaps={n}, KS D={D:.4f} (crit {crit:.4f}) "
        f"{'PASS' if D < crit else 'REJECT'}")


if __name__ == "__main__":
    main()
