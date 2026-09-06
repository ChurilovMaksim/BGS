"""
Run 82u: the Catalan law in the HONEST /N^k normalisation (referee D3 fix).
=========================================================================
The R82.16 table's k >= 2 columns were empirically normalised
(<|J|^{2k}>/<|J|^2>^k * k!).  This script computes the raw
<|J|^{2k}>/N^k directly and tests the Catalan law  <|J|^{2k}> = C_k N^k
in that convention, which is the one any sheaf-theoretic statement (vertical
Sato-Tate) would use.

Output: artifacts/r82/catalan_honest.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r82j_closed_form import primitive_root  # noqa: E402
from r82k_bgs_large_m import design_params  # noqa: E402

CATALAN = [1, 1, 2, 5, 14, 42, 132]
FACT = [1, 1, 2, 6, 24, 120, 720]


def J_matrix(N, K, a, q, block=16384):
    m = (N - 1) // (2 * K)
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    ks = np.array([k for k in range(N - 1)
                   if k % K == 1 % K and (k % 2 == 0)], dtype=np.int64)
    assert len(ks) == m
    J = np.zeros((m, m), dtype=complex)
    xs = np.arange(2, N, dtype=np.int64)
    for s in range(0, len(xs), block):
        xb = xs[s:s + block]
        W = np.exp(-2j * np.pi * np.outer(ks, dlog[xb]) / (N - 1)) * \
            np.exp(2j * np.pi * (q * xb % N) / N)
        Vv = np.exp(2j * np.pi * np.outer(ks, dlog[(xb - 1) % N]) / (N - 1))
        J += W @ Vv.T
    return J, m


def main():
    out = {"script": "src/r82u_catalan_honest.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "normalisation": "raw <|J|^{2k}>/N^k", "designs": []}
    for N, K, qs in ((199, 11, (1, 2, 3, 5, 7, 11)),
                     (3571, 17, (1, 2, 3, 5, 7, 11)),
                     (95419, 57, (1, 2))):
        t0 = time.time()
        a = design_params(N, K)
        rows = []
        for q in qs:
            J, m = J_matrix(N, K, a, q)
            A2 = np.abs(J) ** 2
            r = {"q": q}
            vals = []
            for k in range(1, 6):
                v = float((A2 ** k).mean()) / N ** k
                r[f"k{k}"] = v
                vals.append(v - CATALAN[k])
            r["dev_from_catalan"] = vals
            rows.append(r)
            print(f"N={N} q={q:2d}: " + "  ".join(
                f"<|J|^{2*k}>/N^{k} = {r[f'k{k}']:.5f}" for k in (2, 3, 4, 5)),
                flush=True)
        print(f"  N={N}: Catalan targets 2, 5, 14, 42; factorial would be "
              f"6, 24, 120", flush=True)
        for k in (2, 3, 4, 5):
            v = np.array([r[f"k{k}"] for r in rows])
            print(f"    k={k}: mean {v.mean():.5f}  dev from C_{k} "
                  f"{v.mean()-CATALAN[k]:+.5f}  (1/sqrt(N) = {N**-0.5:.5f})",
                  flush=True)
        out["designs"].append({"N": N, "K": K, "m_plus": (N - 1) // (2 * K),
                               "rows": rows})
        print(f"  ({time.time()-t0:.0f} s)", flush=True)
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "catalan_honest.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
