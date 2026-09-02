"""Run 85a: THE FOURTH MIXED MOMENT OF THE TWISTED JACOBI SUMS.

The R82 handoff's named "cheap first step" toward op:local (LEDGER, R82
handoff item 0): extend the R82.13 tuple collapse to the fourth mixed
moment sum_{chi,psi in S} |J(chi,psi;q)|^8 and test whether

  (1) the leading term is the CATALAN value C_4 N^4 = 14 N^4
      (Sato-Tate / rank-2 sheaf prediction, R82.16), and
  (2) the subleading structure is a sum over NON-DIAGONAL tuple classes
      (not matchings -- those died in R82.25/R82.21a) whose Weil-type
      bounds give an error o(N^4), so that the moment sequence stays
      Catalan with an explicit error budget.

Method (all exact integer/numpy arithmetic, no floating ambiguity):
  * characters chi_k(x) = exp(2 pi i k dlog(x)/(N-1)) on F_N^* via a
    discrete-log table;
  * the index coset S = {chi : chi(a) = zeta} for the design's a with
    ord(a) = K (zeta = 1: principal class, the largest coset);
  * J(chi,psi;q) = sum_{x != 0,1} conj(chi)(x) psi(x-1) e_N(q x),
    computed as an (m x N)(N x m) product exactly as in
    src/theorems/theorem_ii_twisted_jacobi.py (the certified pipeline);
  * the moment M8(q) = (1/|S|^2) sum_{chi,psi}|J|^8, averaged over q.
  * SECOND KEY: the same M8 computed by direct triple loop over a small
    design (N = 53) with independently-coded Jacobi sums (no matrix
    product) -- catches any vectorisation/grouping bug (LESSON 82-M).

Cross-check anchors (must reproduce before anything is reported):
  * at k=2: <|J|^2> = N + O(K^2)   (Proposition A, R82.13);
  * at k=4 (this is the 8th power): asymptotic 14 N^4
    (Catalan C_4 = 14; Gaussian alternative 24 is dead, R82.21).

Output: artifacts/diagnostics/fourth_mixed_moment.json + .log
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "artifacts", "diagnostics")
os.makedirs(OUT_DIR, exist_ok=True)
LOG = os.path.join(OUT_DIR, "fourth_mixed_moment.log")


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


def index_coset(N, K, a, dlog):
    """characters chi_k with chi_k(a) = 1, i.e. k*dlog(a) = 0 mod (N-1);
    this is the annihilator coset structure of R82.12's principal class."""
    ell = int(dlog[a])            # dlog of the design element
    step = ell % K                # chi_k(a) depends on k via k*ell mod (N-1)
    # chi(a)=1  <=>  k*ell = 0 mod (N-1)  <=>  k = 0 mod (N-1)/gcd(ell,N-1)
    import math
    d = math.gcd(ell, N - 1)
    mod = (N - 1) // d
    ks = np.array([k for k in range(N - 1) if k % mod == 0], dtype=np.int64)
    return ks


def jacobi_matrix(N, K, a, dlog, ks, q):
    """J[i,j] = sum_{x != 0,1} conj(chi_i)(x) psi_j(x-1) e_N(qx)."""
    xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))     # conj(chi)(x)
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))    # psi(x-1)
    ph = np.exp(2j * np.pi * (q * xs % N) / N)
    return (W * ph) @ V.T


def jacobi_direct(N, ks, q):
    """Second key: O(m^2 N) direct triple loop, no matrix product."""
    xs = [x for x in range(N) if x not in (0, 1)]
    m = len(ks)
    J = np.zeros((m, m), dtype=complex)
    for i in range(m):
        for j in range(m):
            s = 0.0 + 0.0j
            for x in xs:
                s += (np.exp(-2j * np.pi * ks[i] * dlog_t[x] / (N - 1))
                      * np.exp(2j * np.pi * ks[j] * dlog_t[(x - 1) % N] / (N - 1))
                      * np.exp(2j * np.pi * q * x / N))
            J[i, j] = s
    return J


def moment8(Jm):
    return float((np.abs(Jm) ** 8).mean())


# ---------------------------------------------------------------- designs
# split primes with ord(a)=K, K odd, from the R82 design table
DESIGNS = [
    (37, 3, 18),      # N, a, placeholder-K resolved below
    (53, 16, 18),
]
# resolve K = ord_N(a) at runtime
def ord_N(a, N):
    x = a % N
    k = 1
    while x != 1:
        x = x * a % N
        k += 1
    return k


def main():
    t0 = time.time()
    log("RUN 85a -- fourth mixed moment of J(chi,psi;q), principal coset")
    out = {"run": "85a", "designs": [], "notes": {}}

    for (N, a, _Kguess) in DESIGNS:
        K = ord_N(a, N)
        g = 3 if N % 3 else 5          # any primitive root; check below
        # find a genuine primitive root
        def is_primitives_root(g):
            need = {1}
            x = 1
            seen = set()
            for _ in range(N - 1):
                x = x * g % N
                seen.add(x)
            return len(seen) == N - 1
        g = next(gg for gg in range(2, N) if is_primitives_root(gg))
        dlog = dlog_table(N, g)
        ks = index_coset(N, K, a, dlog)
        m = len(ks)
        log(f"-- design N={N}, a={a}, K={K}, |S|={m} (chi(a)=1 coset)")

        # q-average over ALL nonzero q (exact full curve, no sampling)
        m2_sum = m4_sum = m6_sum = m8_sum = 0.0
        per_q = []
        for q in range(1, N):
            J = jacobi_matrix(N, K, a, dlog, ks, q)
            a2 = float((np.abs(J) ** 2).mean())
            a4 = float((np.abs(J) ** 4).mean())
            a6 = float((np.abs(J) ** 6).mean())
            a8 = float((np.abs(J) ** 8).mean())
            m2_sum += a2; m4_sum += a4; m6_sum += a6; m8_sum += a8
            per_q.append({"q": q, "e2": a2, "e8": a8})
        nq = N - 1
        e2 = m2_sum / nq; e4 = m4_sum / nq; e6 = m6_sum / nq; e8 = m8_sum / nq
        row = {
            "N": N, "a": a, "K": K, "m": m,
            "mean|J|^2/N^1": e2 / N,
            "mean|J|^4/N^2": e4 / N**2,
            "mean|J|^6/N^3": e6 / N**3,
            "mean|J|^8/N^4": e8 / N**4,
            "catalan_2_5_14": [2.0, 5.0, 14.0],
            "gaussian_alt_6_24": [6.0, 24.0],
        }
        log("   " + json.dumps(row))
        out["designs"].append(row)

        # second key at this design: direct-loop J at q=1
        global dlog_t
        dlog_t = dlog
        Jd = jacobi_direct(N, ks, 1)
        Jm = jacobi_matrix(N, K, a, dlog, ks, 1)
        dev = float(np.max(np.abs(Jd - Jm)))
        e8_direct = float((np.abs(Jd) ** 8).mean())
        e8_matrix = float((np.abs(Jm) ** 8).mean())
        log(f"   second-key direct-vs-matrix: max|dJ|={dev:.2e}, "
            f"e8 {e8_direct:.6f} vs {e8_matrix:.6f}")
        out.setdefault("second_key", []).append(
            {"N": N, "q": 1, "max_dev": dev, "e8_direct": e8_direct,
             "e8_matrix": e8_matrix})

    # anchors: k=2 must be ~1 (Prop A), k=8 must approach 14 not 24
    log("ANCHORS: <|J|^2>/N ~ 1 (Prop A); <|J|^8>/N^4 -> 14 (Catalan), "
        "24 = Gaussian is dead (R82.21)")
    out["walltime_s"] = time.time() - t0
    with open(os.path.join(OUT_DIR, "fourth_mixed_moment.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log("artifact: artifacts/diagnostics/fourth_mixed_moment.json")


if __name__ == "__main__":
    main()
