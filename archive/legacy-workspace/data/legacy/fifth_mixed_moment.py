"""RUN 86.1 -- THE FIFTH MIXED MOMENT OF THE TWISTED JACOBI SUMS at the
CERTIFIED DESIGN (N=3571, K=17, m=210).

R85 handoff item (a): extend e_{2k} = <|J|^{2k}>/N^k to k = 5 at (3571)
to complete the honest table against the 95419 anchor (R82.21(b), k=5).

Catalan targets:
    C_1 = 1,  C_2 = 2,  C_3 = 5,  C_4 = 14,  C_5 = 42,  C_6 = 132, ...
Gaussian alternative at k=5: 5! = 120 (DEAD at every k >= 3, R82.21).

Two-key discipline (LESSON 82-M): the matrix-product J implementation
(the certified pipeline, identical to R82.12 / R85) is cross-checked
against a direct triple loop on a SMALL design where memory allows.

Output: artifacts/diagnostics/fifth_mixed_moment.json + .log
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
LOG = os.path.join(OUT_DIR, "fifth_mixed_moment.log")


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


def index_coset(N, K, a, dlog):
    """chi_k(a) = 1: k*dlog(a) = 0 mod (N-1), principal class."""
    ell = int(dlog[a])
    d = math.gcd(ell, N - 1)
    mod = (N - 1) // d
    return np.array([k for k in range(N - 1) if k % mod == 0], dtype=np.int64)


def jacobi_matrix_q(N, K, a, dlog, ks, q, W, V, xs, dl_x, dl_xm1):
    """J[i,j] = sum_{x != 0,1} conj(chi_i)(x) psi_j(x-1) e_N(qx)."""
    ph = np.exp(2j * np.pi * (q * xs % N) / N)
    return (W * ph) @ V.T


def jacobi_direct_q(N, ks, q, dlog):
    """Second key: O(m^2 N) direct triple loop, no matrix product."""
    xs = [x for x in range(N) if x not in (0, 1)]
    m = len(ks)
    J = np.zeros((m, m), dtype=complex)
    for i in range(m):
        for j in range(m):
            s = 0.0 + 0.0j
            for x in xs:
                s += (np.exp(-2j * np.pi * ks[i] * dlog[x] / (N - 1))
                      * np.exp(2j * np.pi * ks[j] * dlog[(x - 1) % N] / (N - 1))
                      * np.exp(2j * np.pi * q * x / N))
            J[i, j] = s
    return J


def main():
    t0 = time.time()
    log("RUN 86.1 -- fifth mixed moment <|J|^{10}>/N^5 at (3571, 17)")
    out = {"run": "86.1", "designs": [], "anchors": {}}

    # ---------- CERTIFIED DESIGN (3571, K=17, m=210) ----------
    N = 3571
    K = 17
    a = 47     # same a as R85b / certified R82.12
    log(f"-- certified design: N={N}, a={a}, K={K}, m=(N-1)/K=210")
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ks = index_coset(N, K, a, dlog)
    m = len(ks)
    assert m == 210, f"m = {m} != 210"

    xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    # precompute W and V (independent of q)
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))     # conj(chi)(x)
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))    # psi(x-1)

    # honest Catalan / Gaussian targets
    targets = {
        "k=1": ("catalan 1", 1.0, "gaussian 1", 1.0),
        "k=2": ("catalan 2", 2.0, "gaussian 2", 2.0),
        "k=3": ("catalan 5", 5.0, "gaussian 6", 6.0),
        "k=4": ("catalan 14", 14.0, "gaussian 24", 24.0),
        "k=5": ("catalan 42", 42.0, "gaussian 120", 120.0),
    }

    sums = {f"k{k}": 0.0 for k in range(1, 6)}
    nq = N - 1
    # chunked progress: write intermediate result every 500 q so a crash loses
    # at most one chunk
    CHUNK = 500
    chunk_partial = {f"k{k}": 0.0 for k in range(1, 6)}
    for q in range(1, N):
        ph = np.exp(2j * np.pi * (q * xs % N) / N)
        J = (W * ph) @ V.T
        aJ = np.abs(J)
        for k in range(1, 6):
            chunk_partial[f"k{k}"] += (aJ ** (2*k)).mean()
        if q % CHUNK == 0:
            log(f"   q={q}/{N-1} ({(q/(N-1))*100:.1f}%)")
            for k in range(1, 6):
                sums[f"k{k}"] += chunk_partial[f"k{k}"]
                chunk_partial[f"k{k}"] = 0.0
            # interim write for crash safety
            interim = {"partial_q": q, "sums": {k: sums[f"k{k}"] for k in range(1, 6)}}
            with open(os.path.join(OUT_DIR, "fifth_mixed_moment_partial.json"), "w",
                      encoding="utf-8") as fh:
                json.dump(interim, fh)
    # remainder
    for k in range(1, 6):
        sums[f"k{k}"] += chunk_partial[f"k{k}"]
    row = {"N": N, "a": int(a), "K": K, "m": m}
    for k in range(1, 6):
        row[f"e_{2*k}/N^{k}"] = sums[f"k{k}"] / nq / N**k
    log("   " + json.dumps(row))
    out["designs"].append({"label": "certified_3571_17", **row})

    # SECOND KEY: direct-loop J at q=1 on a SMALL design (N=53, K=13) where
    # the triple loop is tractable.  Compare to matrix-product at same N,q.
    # Per LESSON 82-M: this catches grouping/vectorisation bugs; the certified
    # design (3571) is too large for a triple loop.
    log("   second-key at SMALL design (N=53, K=13)")
    N2 = 53
    g2 = primitive_root(N2)
    dlog2 = dlog_table(N2, g2)
    # find a with small ord: scan
    a2 = None
    K2 = None
    for cand in range(2, N2):
        kk = ord_N(cand, N2)
        if 8 <= kk <= 64 and kk % 2 == 1:
            a2, K2 = cand, kk
            break
    assert a2 is not None
    ks2 = index_coset(N2, K2, a2, dlog2)
    m2 = len(ks2)
    xs2 = np.array([x for x in range(N2) if x not in (0, 1)], dtype=np.int64)
    dl2x = dlog2[xs2]
    dl2xm1 = dlog2[(xs2 - 1) % N2]
    W2 = np.exp(-2j * np.pi * np.outer(ks2, dl2x) / (N2 - 1))
    V2 = np.exp(2j * np.pi * np.outer(ks2, dl2xm1) / (N2 - 1))
    Jd2 = jacobi_direct_q(N2, ks2, 1, dlog2)
    ph1_2 = np.exp(2j * np.pi * (1 * xs2 % N2) / N2)
    Jm2 = (W2 * ph1_2) @ V2.T
    dev2 = float(np.max(np.abs(Jd2 - Jm2)))
    e10_d = float((np.abs(Jd2) ** 10).mean())
    e10_m = float((np.abs(Jm2) ** 10).mean())
    log(f"   second-key N=53,q=1: max|dJ|={dev2:.2e}, "
        f"e10 direct {e10_d:.6f} vs matrix {e10_m:.6f}")
    out["second_key"] = {"N": N2, "K": K2, "q": 1, "max_dev": dev2,
                         "e10_direct": e10_d, "e10_matrix": e10_m}

    # comparison vs targets
    for k in range(1, 6):
        v = row[f"e_{2*k}/N^{k}"]
        c = [1.0, 2.0, 5.0, 14.0, 42.0][k - 1]
        g_v = [1.0, 2.0, 6.0, 24.0, 120.0][k - 1]
        log(f"   k={k}: measured {v:.6f}, Catalan {c}, Gaussian {g_v}, "
            f"dev/cat={v-c:.4f}, dev/gauss={v-g_v:.4f}")

    out["catalan_targets"] = [1.0, 2.0, 5.0, 14.0, 42.0]
    out["gaussian_targets"] = [1.0, 2.0, 6.0, 24.0, 120.0]
    out["walltime_s"] = time.time() - t0
    with open(os.path.join(OUT_DIR, "fifth_mixed_moment.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log("artifact written")


if __name__ == "__main__":
    main()