"""
REFEREE CHECK R83.2 --- Theorem G norm ratio:  is  ||cbar||_1/||cbar||_2  ~ sqrt(K)
or ~ 1/sqrt(K)?

CONTEXT.
Paper (thm:G, lines ~1037-1045) states
    ||cbar||_1 ~ ||c||_1 ,   ||cbar||_2 ~ K^{-1/2} ||c||_2 ,
  =>  ||cbar||_1 / ||cbar||_2  ~ sqrt(K) * ||c||_1/||c||_2 .

REVIEW_ERRORS.md ERROR #3 (severity MEDIUM-HIGH) claims this is a sign error:
it asserts ||cbar||_1 = K^{-1} ||c||_1 always, and concludes the true factor is
K^{-1/2}, i.e. the moment route OPENS UP for large K rather than closing.

THE ACTUAL MATHEMATICS (settled by this script).
Let the Birkhoff average of the observable be
    Vbar = K^{-1} sum_{j<K} U^j V U^{-j}.
By Egorov,  U^j T(n) U^{-j} = T(A^j n)  (up to phase; the phase is trivial for
the quantised propagator in the T-normalisation used here), so
    cbar_n = K^{-1} sum_{j<K} c_{A^{-j} n}.
Hence cbar is CONSTANT on each A^T-orbit, with value = the orbit mean of c.

CRUCIAL POINT missed by ERROR #3: whether ||cbar||_1 equals ||c||_1 or
K^{-1}||c||_1 depends on the SUPPORT of c relative to orbits.

Case (i)  c supported on ONE point n0 of a free orbit of size K:
    cbar takes value 1/K at each of the K orbit points.
    ||cbar||_1 = K * (1/K) = 1 = ||c||_1                 <-- paper is right
    ||cbar||_2 = sqrt(K * (1/K)^2) = K^{-1/2} = K^{-1/2}||c||_2
    ratio ||cbar||_1/||cbar||_2 = sqrt(K)                <-- paper is right

Case (ii) c already A^T-invariant (constant on the orbit, K points, value 1/K
so that ||c||_1 = 1):
    cbar = c, ratio unchanged.  No K-factor either way.

ERROR #3's assertion "||cbar||_1 = K^{-1}||c||_1 (not ~ ||c||_1)" is what you
get ONLY if you (wrongly) forget that the average redistributes the mass onto
K distinct frequencies rather than shrinking it at one frequency.  For a
delta-supported c, mass is preserved in l^1 and only l^2 collapses.

THIS SCRIPT computes cbar EXACTLY (no floating heuristics) for genuine cat maps
and genuine A^T-orbit structure, for several (A, N) with several support types,
and reports the measured exponent
    e := log( ||cbar||_1/||cbar||_2  /  (||c||_1/||c||_2) ) / log(K).
Paper predicts e = +1/2 for delta-supported c.  ERROR #3 predicts e = -1/2.

Run: py -3 review/referee/ref02_theoremG_norm_ratio.py
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT = os.path.join(ROOT, "artifacts", "referee_r83")
os.makedirs(OUT, exist_ok=True)


def mat_pow_mod(A, j, N):
    a, b, c, d = [v % N for v in A]
    P = (1, 0, 0, 1)
    M = (a, b, c, d)
    for _ in range(j):
        P = ((P[0] * M[0] + P[1] * M[2]) % N, (P[0] * M[1] + P[1] * M[3]) % N,
             (P[2] * M[0] + P[3] * M[2]) % N, (P[2] * M[1] + P[3] * M[3]) % N)
    return P


def order_mod(A, N):
    """least k >= 1 with A^k = +-I mod N; returns (k, K) with K = k or 2k."""
    a, b, c, d = [v % N for v in A]
    P = (1, 0, 0, 1)
    for k in range(1, 4 * N + 4):
        P = ((P[0] * a + P[1] * c) % N, (P[0] * b + P[1] * d) % N,
             (P[2] * a + P[3] * c) % N, (P[2] * b + P[3] * d) % N)
        if P == (1, 0, 0, 1):
            return k, k
        if P == ((N - 1) % N, 0, 0, (N - 1) % N):
            return k, 2 * k
    raise RuntimeError("order not found")


def orbit_of(n, AT, N, K):
    """A^T-orbit of the frequency n = (n1, n2) in (Z/N)^2."""
    pts = []
    cur = tuple(x % N for x in n)
    for _ in range(K):
        pts.append(cur)
        a, b, c, d = AT
        cur = ((a * cur[0] + b * cur[1]) % N, (c * cur[0] + d * cur[1]) % N)
    # de-duplicate preserving order
    seen, out = set(), []
    for p in pts:
        if p not in seen:
            seen.add(p)
            out.append(p)
    return out


def birkhoff_coeffs(c, AT, N, K):
    """cbar_n = K^{-1} sum_{j<K} c_{A^{-j} n}.  Equivalent: distribute each
    c_{n0} equally over the forward orbit of n0.  Computed exactly with
    Fraction-free float since all weights are 1/K."""
    cbar = {}
    for n0, val in c.items():
        orb = orbit_of(n0, AT, N, K)
        L = len(orb)
        # each of the K steps lands on orbit points; with orbit length L,
        # each point is hit K/L times.  Weight per hit = 1/K.
        w = val * (K / L) / K       # = val / L
        for p in orb:
            cbar[p] = cbar.get(p, 0.0) + w
    return cbar


def norms(d):
    vals = np.array(list(d.values()), dtype=float)
    return float(np.sum(np.abs(vals))), float(np.sqrt(np.sum(vals * vals)))


def transpose(A):
    a, b, c, d = A
    return (a, c, b, d)


def run(A, N):
    k, K = order_mod(A, N)
    AT = transpose(tuple(v % N for v in A))
    rows = []

    # ---- support type 1: single delta at a generic frequency --------------
    n0 = (1, 0)
    c1 = {n0: 1.0}
    orb = orbit_of(n0, AT, N, K)
    cb1 = birkhoff_coeffs(c1, AT, N, K)
    l1c, l2c = norms(c1)
    l1b, l2b = norms(cb1)
    ratio_c = l1c / l2c
    ratio_b = l1b / l2b
    e = math.log(ratio_b / ratio_c) / math.log(K) if K > 1 else float("nan")
    rows.append(dict(support="single delta (generic freq)", orbit_len=len(orb),
                     l1_c=l1c, l2_c=l2c, l1_cbar=l1b, l2_cbar=l2b,
                     l1_ratio_cbar_over_c=l1b / l1c,
                     l2_ratio_cbar_over_c=l2b / l2c,
                     ratio_c=ratio_c, ratio_cbar=ratio_b, exponent_in_K=e))

    # ---- support type 2: already orbit-invariant --------------------------
    c2 = {p: 1.0 / len(orb) for p in orb}
    cb2 = birkhoff_coeffs(c2, AT, N, K)
    l1c, l2c = norms(c2)
    l1b, l2b = norms(cb2)
    e2 = math.log((l1b / l2b) / (l1c / l2c)) / math.log(K) if K > 1 else float("nan")
    rows.append(dict(support="A^T-invariant (one full orbit)", orbit_len=len(orb),
                     l1_c=l1c, l2_c=l2c, l1_cbar=l1b, l2_cbar=l2b,
                     l1_ratio_cbar_over_c=l1b / l1c,
                     l2_ratio_cbar_over_c=l2b / l2c,
                     ratio_c=l1c / l2c, ratio_cbar=l1b / l2b, exponent_in_K=e2))

    # ---- support type 3: several random deltas, distinct orbits ----------
    rng = np.random.default_rng(20260831)
    picks, seen_orbits = [], set()
    tries = 0
    while len(picks) < 5 and tries < 400:
        tries += 1
        cand = (int(rng.integers(0, N)), int(rng.integers(0, N)))
        if cand == (0, 0):
            continue
        ob = frozenset(orbit_of(cand, AT, N, K))
        if ob in seen_orbits:
            continue
        seen_orbits.add(ob)
        picks.append(cand)
    c3 = {p: 1.0 for p in picks}
    cb3 = birkhoff_coeffs(c3, AT, N, K)
    l1c, l2c = norms(c3)
    l1b, l2b = norms(cb3)
    e3 = math.log((l1b / l2b) / (l1c / l2c)) / math.log(K) if K > 1 else float("nan")
    rows.append(dict(support=f"{len(picks)} deltas on distinct orbits", orbit_len=len(orb),
                     l1_c=l1c, l2_c=l2c, l1_cbar=l1b, l2_cbar=l2b,
                     l1_ratio_cbar_over_c=l1b / l1c,
                     l2_ratio_cbar_over_c=l2b / l2c,
                     ratio_c=l1c / l2c, ratio_cbar=l1b / l2b, exponent_in_K=e3))

    return dict(A=list(A), N=int(N), k=int(k), K=int(K), rows=rows)


def main():
    designs = [((2, 1, 1, 1), 11), ((2, 1, 1, 1), 29), ((2, 1, 1, 1), 41),
               ((2, 1, 1, 1), 71), ((3, 1, 2, 1), 31), ((1, 1, 1, 2), 101)]
    all_res = []
    print(f"{'A':<14}{'N':>5}{'K':>5}  {'support':<34}"
          f"{'l1bar/l1':>10}{'l2bar/l2':>10}{'exponent in K':>15}")
    print("-" * 96)
    for A, N in designs:
        r = run(A, N)
        all_res.append(r)
        for row in r["rows"]:
            print(f"{str(A):<14}{N:>5}{r['K']:>5}  {row['support']:<34}"
                  f"{row['l1_ratio_cbar_over_c']:>10.4f}"
                  f"{row['l2_ratio_cbar_over_c']:>10.4f}"
                  f"{row['exponent_in_K']:>15.4f}")

    # verdict on the delta-supported case, which is the one the paper's
    # corollary uses
    deltas = [row["exponent_in_K"] for r in all_res for row in r["rows"]
              if row["support"].startswith("single delta")]
    l1pres = [row["l1_ratio_cbar_over_c"] for r in all_res for row in r["rows"]
              if row["support"].startswith("single delta")]
    paper_ok = all(abs(e - 0.5) < 0.02 for e in deltas) and all(abs(x - 1.0) < 1e-9 for x in l1pres)
    err3_ok = all(abs(e + 0.5) < 0.02 for e in deltas)

    verdict = dict(
        measured_exponents_delta_case=deltas,
        measured_l1_preservation_delta_case=l1pres,
        paper_prediction="exponent = +0.5, ||cbar||_1 = ||c||_1",
        review_errors_3_prediction="exponent = -0.5, ||cbar||_1 = K^{-1}||c||_1",
        PAPER_CONFIRMED=bool(paper_ok),
        REVIEW_ERRORS_3_CONFIRMED=bool(err3_ok),
        VERDICT=("PASS: Theorem G as printed is CORRECT; REVIEW_ERRORS #3 is REFUTED "
                 "(it wrongly assumed the Birkhoff average shrinks l^1 mass instead "
                 "of redistributing it over the orbit)") if paper_ok else
                ("REVIEW_ERRORS #3 CONFIRMED" if err3_ok else "INCONCLUSIVE"),
    )
    print()
    print("=" * 96)
    print(f"delta-case exponents in K : {[round(e,4) for e in deltas]}")
    print(f"delta-case l1 preservation: {[round(x,6) for x in l1pres]}  (1.0 = paper, 1/K = ERROR#3)")
    print(f"VERDICT: {verdict['VERDICT']}")
    print("=" * 96)

    path = os.path.join(OUT, "ref02_theoremG_norm_ratio.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(dict(verdict=verdict, designs=all_res), fh, indent=2)
    print(f"artifact: {path}")
    return 0 if paper_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
