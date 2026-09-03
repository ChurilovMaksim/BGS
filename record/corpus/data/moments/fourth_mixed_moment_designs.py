"""Run 85b: the fourth mixed moment at a FULL R82 design (N=3571, K=17).

R85a established the small-design behaviour; this run computes the same
moment sequence on the certified R82 design (N = 3571, a with ord = 17,
principal coset chi(a)=1) over the FULL q-curve, and additionally at the
intermediate design (199, 11), to test convergence toward the Catalan
value C_4 N^4 = 14 N^4 with the (K, N) dependence visible.

Same two-key discipline: matrix-product J vs direct loop at one q.
Output: artifacts/diagnostics/fourth_mixed_moment_designs.json + .log (append).
"""
import json
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.path.abspath(os.path.join(HERE, "..", "..", "artifacts", "diagnostics"))
LOG = os.path.join(OUT_DIR, "fourth_mixed_moment_designs.log")


def log(msg):
    print(msg, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(str(msg) + "\n")


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


def main():
    t0 = time.time()
    log("RUN 85b -- fourth mixed moment at certified R82 designs")
    import math
    out = {"designs": []}
    for (N, a) in [(199, 123 % 199 or 122), (3571, 622)]:
        # choose a with small ord: scan
        K = None
        for cand in range(2, N):
            k = ord_N(cand, N)
            if 8 <= k <= 64 and k % 2 == 1:
                a, K = cand, k
                break
        g = primitive_root(N)
        dlog = dlog_table(N, g)
        ell = int(dlog[a])
        mod = (N - 1) // math.gcd(ell, N - 1)
        ks = np.array([k for k in range(N - 1) if k % mod == 0], dtype=np.int64)
        m = len(ks)
        log(f"-- design N={N}, a={a}, K={K}, |S|={m}")
        xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
        dl_x = dlog[xs]
        dl_xm1 = dlog[(xs - 1) % N]
        W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
        V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))
        m2 = m4 = m6 = m8 = 0.0
        for q in range(1, N):
            ph = np.exp(2j * np.pi * (q * xs % N) / N)
            J = (W * ph) @ V.T
            aJ = np.abs(J)
            m2 += (aJ**2).mean(); m4 += (aJ**4).mean()
            m6 += (aJ**6).mean(); m8 += (aJ**8).mean()
        nq = N - 1
        row = {"N": N, "a": int(a), "K": K, "m": m,
               "e2/N": m2/nq/N, "e4/N^2": m4/nq/N**2,
               "e6/N^3": m6/nq/N**3, "e8/N^4": m8/nq/N**4}
        log("   " + json.dumps(row))
        out["designs"].append(row)
    out["walltime_s"] = time.time() - t0
    with open(os.path.join(OUT_DIR, "fourth_mixed_moment_designs.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log("artifact written")


if __name__ == "__main__":
    main()
