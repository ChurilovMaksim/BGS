"""RUN 98 -- k=6 layer at N=199: measure the coupled-energy fluctuation of
the sixth coset moment via the direct A6(q) computation (all q), and the
k=8 layer likewise, testing whether the relative cross-q fluctuation
decays with N at fixed layer (the H3 requirement per layer).

Design: N=199, a=139, K=11, m=18 (full principal coset).

The k-layer fluctuation statistic: rel_k = std_q(A_{k,S}) / mean_q(A_{k,S}).
Flat-scale context: the layer's uncoupled energy E_unc,k ~ N^{2k-3}
(c-distribution flat at ~N^{k-2}... measured directly below).

Output: artifacts/r98/k_layers_N199.json
"""
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "artifacts", "r98")
os.makedirs(OUT_DIR, exist_ok=True)

sys.path.insert(0, os.path.join(ROOT, "src", "large_m"))
sys.path.insert(0, os.path.join(ROOT, "src", "theorems"))

from fourth_mixed_moment import (  # noqa: E402
    dlog_table, index_coset, jacobi_matrix,
)
from theorem_ii_twisted_jacobi import primitive_root  # noqa: E402


def main():
    t0 = time.time()
    N, a = 199, 139
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    kk = 1
    x = a % N
    while x != 1:
        x = x * a % N
        kk += 1
    K = kk
    ks = index_coset(N, K, a, dlog)
    m = len(ks)
    xs = np.array([q for q in range(1, N) if q != 1], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))

    rows = []
    A = {k: [] for k in (2, 4, 6, 8, 10, 12)}
    for q in range(1, N):
        ph = np.exp(2j * np.pi * (q * xs % N) / N)
        J = (W * ph) @ V.T
        aJ2 = np.abs(J) ** 2
        s = float(aJ2.sum())
        A[2].append(s)
        for k in (4, 6, 8, 10, 12):
            s = float((aJ2 ** (k // 2)).sum())
            A[k].append(s)
    for k in (2, 4, 6, 8, 10, 12):
        arr = np.array(A[k])
        rel = float(arr.std() / arr.mean())
        rows.append({"k": k, "mean": float(arr.mean()),
                     "std": float(arr.std()), "rel": rel})
        print(f"k={k}: mean={arr.mean():.4e} std={arr.std():.4e} rel={rel:.4f}")

    out = {
        "run": "98",
        "design": {"N": N, "a": a, "K": K, "m": m},
        "layers": rows,
        "note": ("rel_k at m=18 across k=2..12; the H3 requirement is "
                 "rel_k -> 0 as N -> infinity for each fixed k"),
        "wall_s": time.time() - t0,
    }
    with open(os.path.join(OUT_DIR, "k_layers_N199.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact written")


if __name__ == "__main__":
    main()
