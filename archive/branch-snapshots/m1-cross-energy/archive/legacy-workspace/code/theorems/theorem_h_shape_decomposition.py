"""
Run 75: STRUCTURE THEORY OF THE ENSEMBLE EXCESS X_r.
=====================================================

R74.5 named the whole remaining gap as "control X_r, the Chebyshev +-1 relation
count".  This script establishes its structure.  The exact identity underlying
everything: a word (eps_i, j_i)_{i<=r} with j in [0,K) has collected coefficient
vector c_j = sum_{i: j_i = j} eps_i, and

    L(eps,j) = 0 over Z   <=>   p_c(A) = 0,  p_c(x) = sum_j c_j x^j
                          <=>   m_t | p_c   in Z[x],   m_t(x) = x^2 - t x + 1,

because {A, I} spans Q[A] and A^j = U_j A - U_{j-1} I (U_{-1} = -1), and the
word signature depends only on c.  Grouping D_r by c (exact identity):

    D_r = sum_{c : m_t | p_c over Z} wc(c, r)           (the Z-part)
        + sum_{c : p_c not 0, p_c(A) = 0 mod N} wc(c, r) (the mod-N accidents),

    wc(c, r) = r! * sum_{c_j = c_j^+ - c_j^-, sum (c_j^+ + c_j^-) = r}
               prod_j 1/(c_j^+! c_j^-!)                  (exact rational).

The Z-part is FINITE-SCALE: p_c is a multiple of m_t with ||c||_1 <= r, hence a
translate of one of finitely many PRIMITIVE SHAPES (support-normalised multiples
of m_t).  This script:

  (S1) enumerates all primitive shapes of m_t for t=3 and t=6 (exact
       meet-in-the-middle on the lattice coordinates of p(lambda) = 0);
  (S2) predicts D_r(Z) and X_r(Z) from shapes at K=17,19 and validates against
       the measured r74 values -- exact match required;
  (S3) enumerates ALL collected vectors with ||c||_1 <= 6 at K=17,19, splits
       D_6(N) = Z-part + accidents, and classifies the accident patterns;
  (S4) counts the (1,1,-2) "midpoint class"  A^a + A^b = 2 A^c (mod N);
  (S5) measures the shape growth S(R) = #{primitive shapes, ||p||_1 = R};
  (S6) measures D_5 over Z (odd order) and validates the m-shape prediction.

Output: artifacts/r75/multiples_structure.json
"""

from __future__ import annotations

import itertools
import json
import math
import os
import sys
import time
from fractions import Fraction

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402


def chebyshev_exact(t, count):
    """Returns [U_{-1}, U_0, U_1, ..., ] of length count+2:
    index i holds U_{i-1}.  So U_j = Ue[j+1], U_{-1} = Ue[0] = -1."""
    U = [-1, 0, 1]
    for _ in range(count):
        U.append(t * U[-1] - U[-2])
    return U


# ----------------------------------------------------------------------
# S1+S5  primitive shapes: meet-in-the-middle over Z[lambda]^2
# ----------------------------------------------------------------------
def enumerate_shapes(t, R_max, width_max):
    """All p with m_t | p, 0 < ||p||_1 <= R_max, support-normalised (p(0) != 0,
    leading coefficient positive), width <= width_max.  Exact: the relation
    p(lambda) = 0 is the pair of integer equations
        sum_j c_j U_j = 0,   sum_j c_j U_{j-1} = 0,
    split by position at h = width_max//2 (every support splits uniquely, so
    joins never double count).  Returns dict R -> sorted list of coefficient
    tuples (c_0, ..., c_w), c_0 > 0."""
    Ue = chebyshev_exact(t, width_max + 4)
    atoms = [(Ue[j + 1], Ue[j]) for j in range(width_max)]  # (U_j, U_{j-1})
    h = width_max // 2
    left_pos = range(h)
    right_pos = range(h, width_max)

    cache = {}

    def half_configs(positions, R_half):
        """dict (vx, vy) -> list of (support, coeffs) with L1 exactly R_half."""
        key = (positions[0], len(positions), R_half)
        if key in cache:
            return cache[key]
        d = {}
        for k in range(1, min(len(positions), R_half) + 1):
            for support in itertools.combinations(positions, k):
                for coeffs in signed_compositions(R_half, k):
                    vx = 0
                    vy = 0
                    for j, c in zip(support, coeffs):
                        vx += c * atoms[j][0]
                        vy += c * atoms[j][1]
                    d.setdefault((vx, vy), []).append(
                        (tuple(support), tuple(coeffs)))
        cache[key] = d
        return d

    found = {R: set() for R in range(1, R_max + 1)}
    for R in range(1, R_max + 1):
        for Rl in range(0, R + 1):
            Rr = R - Rl
            if Rl == 0:
                left = {(0, 0): [((), ())]}
            else:
                left = half_configs(left_pos, Rl)
            if Rr == 0:
                right = {(0, 0): [((), ())]}
            else:
                right = half_configs(right_pos, Rr)
            for (vx, vy), cfgs in left.items():
                match = right.get((-vx, -vy))
                if not match:
                    continue
                for (sup_l, cf_l) in cfgs:
                    for (sup_r, cf_r) in match:
                        if not sup_l and not sup_r:
                            continue
                        support = sup_l + sup_r
                        coeffs = cf_l + cf_r
                        if support[0] != 0:
                            continue  # keep only support-normalised shapes
                        # expand the support to a DENSE coefficient vector
                        # (gaps are real zero coefficients, not compressions)
                        dense = [0] * (support[-1] + 1)
                        for j, c in zip(support, coeffs):
                            dense[j] = c
                        tup = tuple(dense)
                        if tup[0] < 0:
                            tup = tuple(-x for x in tup)
                        found[R].add(tup)
    out = {R: sorted(found[R]) for R in range(1, R_max + 1)}
    return out


def signed_compositions(total, k):
    """All (a_1..a_k), a_i != 0 integers, sum |a_i| = total."""
    out = []

    def rec(rem, left, cur):
        if left == 1:
            if rem != 0:
                out.append(cur + [rem])
                out.append(cur + [-rem])
            return
        for v in range(-rem + 1, rem):
            if v == 0:
                continue
            rec(rem - abs(v), left - 1, cur + [v])

    rec(total, k, [])
    return out


# ----------------------------------------------------------------------
# exact word counts for a collected vector
# ----------------------------------------------------------------------
def wc_exact(cvec, r):
    """#words of length r over atoms (e, j) with collected vector cvec
    (dict position -> int, all positions with c_j != 0 listed), when
    sum |c_j| = r (no room for extra cancelled pairs).  Exact integer."""
    positions = sorted(cvec.keys())

    def rec(idx, slots_left, prod):
        if idx == len(positions):
            return prod if slots_left == 0 else Fraction(0)
        cj = cvec[positions[idx]]
        tot = Fraction(0)
        for cp in range(0, slots_left + 1):
            cm = cp - cj
            if cm < 0:
                continue
            use = cp + cm
            if use > slots_left:
                continue
            tot += rec(idx + 1, slots_left - use,
                       prod / (math.factorial(cp) * math.factorial(cm)))
        return tot

    val = rec(0, r, Fraction(1)) * math.factorial(r)
    assert val.denominator == 1, (cvec, r, val)
    return int(val)


def wc_full(sig, K, r):
    """#words of length r over atoms (e,j), j in [0,K), whose collected vector
    equals sig on its support (tuple aligned at 0..w) and 0 elsewhere.
    Exact:  wc = r! [y^{r-S}] prod_{j<K} I_{|c_j|}(2y),  S = sum |c_j|,
    where [y^{2k}] I_a(2y) = 1/(k! (k+a)!).  Zero if r - S is odd."""
    S = sum(abs(v) for v in sig if v != 0)
    deg = r - S
    if deg < 0 or deg % 2 == 1:
        return 0
    h = deg // 2
    # P[k] = coefficient of y^{2k} in the product over all K positions
    P = [Fraction(1)] + [Fraction(0)] * h
    coeffs = [abs(v) for v in sig if v != 0] + [0] * (K - sum(1 for v in sig if v != 0))
    for a in coeffs:
        new = [Fraction(0)] * (h + 1)
        for i in range(h + 1):
            if P[i] == 0:
                continue
            for k in range(h + 1 - i):
                new[i + k] += P[i] * Fraction(1, math.factorial(k)
                                               * math.factorial(k + a))
        P = new
    val = P[h] * math.factorial(r)
    assert val.denominator == 1, (sig, K, r, val)
    return int(val)


# ----------------------------------------------------------------------
# S2  shape prediction of D_r(Z), X_r(Z)
# ----------------------------------------------------------------------
def predict_Z(shapes, K, r):
    """(triv, D_pred): D_r(Z) from the shape decomposition,
    triv = r![y^r] I_0(2y)^K = binom(r, r/2) P(s, K) for even r."""
    triv = 0
    if r % 2 == 0:
        s = r // 2
        base = [Fraction(1) / math.factorial(i) ** 2 for i in range(s + 1)]
        poly = [Fraction(1)] + [Fraction(0)] * s
        for _ in range(K):
            new = [Fraction(0)] * (s + 1)
            for i in range(s + 1):
                if poly[i] == 0:
                    continue
                for j in range(s - i + 1):
                    new[i + j] += poly[i] * base[j]
            poly = new
        P = poly[s] * math.factorial(s) ** 2
        assert P.denominator == 1
        triv = math.comb(r, s) * int(P)
    D = triv
    for R in range(1, min(len(shapes), r) + 1):
        if (r - R) % 2 == 1:
            continue
        for sig in shapes.get(R, []):
            width = len(sig) - 1
            if width > K - 1:
                continue
            ntr = K - width
            w = wc_full(sig, K, r)
            D += 2 * ntr * w
    return triv, D


# ----------------------------------------------------------------------
# S2b  cyclic shape prediction of D_r(N)  (eps = +1 designs)
# ----------------------------------------------------------------------
def predict_N_cyclic(shapes, K, r):
    """D_r(N) = triv + 2 sum_{sig} sum_{a in Z/K} wc(dense(a.sig mod K), K, r).

    Justification: the atom signatures are K-periodic mod N (A^K = I), and the
    Chebyshev shift identity U_{i+a} = U_a U_{i+1} - U_{a-1} U_i shows every
    cyclic shift of a solution is again a solution.  Shifts that stay inside
    the window give the Z-multiples; shifts that wrap give the mod-N
    accidents.  The map (sig, a, +-sign) -> dense cyclic vector is injective
    on support-normalised shapes."""
    triv, _ = predict_Z({i: [] for i in range(r + 1)}, K, r)
    D = triv
    for R in range(1, min(len(shapes), r) + 1):
        if (r - R) % 2 == 1:
            continue
        for sig in shapes.get(R, []):
            if len(sig) - 1 > K - 1:
                continue
            for a in range(K):
                dense = [0] * K
                for i, c in enumerate(sig):
                    dense[(a + i) % K] += c
                D += 2 * wc_full(tuple(dense), K, r)
    return D


# ----------------------------------------------------------------------
# S3  full collected-vector census at fixed (K, N, r)
# ----------------------------------------------------------------------
def census(t, K, N, r):
    """All collected vectors over positions 0..K-1 with 0 < ||c||_1 <= r
    (||c||_1 = r mod 2), classified by their signature mod N.  Returns
    (D_N, D_Z, accidents); D_N includes the trivial pairing count only when
    r is even and ||c||_1 = 0 is added by the caller."""
    Ue = chebyshev_exact(t, K + 3)
    sig1m = np.array([Ue[j + 1] % N for j in range(K)], dtype=np.int64)
    sig2m = np.array([Ue[j] % N for j in range(K)], dtype=np.int64)
    Uex = Ue[1:]  # U_0, U_1, ...

    D_N = 0
    D_Z = 0
    accidents = []

    for S in range((r % 2) or 2, r + 1, 2):  # S = ||c||_1: even, 0 < S <= r
        for k in range(1, min(K, S) + 1):
            for support in itertools.combinations(range(K), k):
                for coeffs in signed_compositions(S, k):
                    s1 = 0
                    s2 = 0
                    z1 = 0
                    z2 = 0
                    for j, c in zip(support, coeffs):
                        s1 += c * sig1m[j]
                        s2 += c * sig2m[j]
                        z1 += c * Uex[j]
                        z2 += c * (Uex[j - 1] if j >= 1 else -1)
                    if s1 % N == 0 and s2 % N == 0:
                        cvec = {j: c for j, c in zip(support, coeffs)}
                        w = wc_full(tuple(
                            cvec.get(j, 0) for j in range(
                                max(cvec) + 1)), K, r)
                        D_N += w
                        if z1 == 0 and z2 == 0:
                            D_Z += w
                        else:
                            accidents.append((tuple(cvec.values()), w))
    return D_N, D_Z, accidents


# ----------------------------------------------------------------------
# S4  midpoint class
# ----------------------------------------------------------------------
def midpoint_class(A, N, K):
    """#{nontrivial (a,b,c) in [0,K)^3 : A^a + A^b = 2 A^c mod N}, a,b ordered.
    N odd: 2 is invertible, so c is found from h = (A^a + A^b)/2 mod N.
    Diagonal triples (a,a,a) give the zero collected vector and are excluded."""
    inv2 = (N + 1) // 2
    Am = np.array(A, dtype=object)
    pows = [np.eye(2, dtype=object)]
    for _ in range(K):
        pows.append((pows[-1] @ Am) % N)
    cnt = 0
    tri = []
    for a in range(K):
        for b in range(K):
            s = (pows[a] + pows[b]) % N
            h = (s * inv2) % N
            for c in range(K):
                if np.array_equal(h, pows[c]):
                    if a == b == c:
                        continue
                    cnt += 1
                    tri.append((a, b, c))
    return cnt, tri


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "R75": "structure of X_r", "S1": {}, "S2": [], "S3": [], "S4": [],
           "S5": {}, "S6": [], "verdict": {}}

    # ---------------- S1+S5: shapes -----------------------------------
    shapes3 = enumerate_shapes(3, 8, 16)      # full width for the K=17 window
    shapes3_growth = enumerate_shapes(3, 12, 14)  # growth study, width capped
    shapes6 = enumerate_shapes(6, 10, 14)
    out["S1"]["t=3"] = {R: [list(s) for s in shapes3[R]]
                        for R in sorted(shapes3) if shapes3[R]}
    out["S1"]["t=3_growth_w14"] = {R: [list(s) for s in shapes3_growth[R]]
                                   for R in sorted(shapes3_growth)
                                   if shapes3_growth[R]}
    out["S1"]["t=6"] = {R: [list(s) for s in shapes6[R]]
                        for R in sorted(shapes6) if shapes6[R]}
    out["S5"]["t=3"] = {R: len(shapes3_growth[R]) for R in sorted(shapes3_growth)}
    out["S5"]["t=6"] = {R: len(shapes6[R]) for R in sorted(shapes6)}
    print("[S1] t=3 shapes (width<=16):",
          {R: len(shapes3[R]) for R in sorted(shapes3) if shapes3[R]})
    for R in sorted(shapes3):
        if shapes3[R] and R <= 8:
            print(f"      L1={R}: {shapes3[R]}")
    print("[S1] t=6 shapes (width<=14):",
          {R: len(shapes6[R]) for R in sorted(shapes6) if shapes6[R]})
    for R in sorted(shapes6):
        if shapes6[R] and R <= 10:
            print(f"      L1={R}: {shapes6[R]}")
    sys.stdout.flush()

    # ---------------- S2: validate against r74 ------------------------
    targets = [  # (N, K, r, D_Z_measured, X_Z_measured)  from r74 artifact
        (3571, 17, 6, 543940, 5040),
        (9349, 19, 6, 765380, 5760),
        (3571, 17, 8, 121627590, 4454240),
        (9349, 19, 8, 192140410, 5742240),
    ]
    print("\n[S2] shape prediction of the Z-part (t=3):")
    ok_all = True
    for N, K, r, DZ_meas, XZ_meas in targets:
        triv, Dpred = predict_Z(shapes3, K, r)
        Xpred = Dpred - triv
        ok = (Dpred == DZ_meas) and (Xpred == XZ_meas)
        ok_all &= ok
        print(f"  K={K} r={r}: D_Z pred {Dpred:>12} meas {DZ_meas:>12}"
              f"  X_Z pred {Xpred:>9} meas {XZ_meas:>9}  {'PASS' if ok else 'FAIL'}")
        out["S2"].append({"K": K, "r": r, "D_Z_pred": Dpred,
                          "D_Z_measured": DZ_meas, "X_Z_pred": Xpred,
                          "X_Z_measured": XZ_meas, "match": ok})
        sys.stdout.flush()
    out["verdict"]["S2_shape_prediction_exact"] = ok_all

    # ---------------- S2b: cyclic prediction of D_r(N) -----------------
    targets_N = [  # (N, K, r, D_N_measured, X_N_measured) from r74
        (3571, 17, 6, 545020, 6120),
        (9349, 19, 6, 766460, 6840),
        (3571, 17, 8, 122637830, 5464480),
        (9349, 19, 8, 193271610, 6873440),
    ]
    print("\n[S2b] cyclic shape prediction of D_r(N) (eps = +1):")
    ok_cyc = True
    for N, K, r, DN_meas, XN_meas in targets_N:
        Dpred = predict_N_cyclic(shapes3, K, r)
        Xpred = Dpred - predict_Z({i: [] for i in range(r + 1)}, K, r)[0]
        ok = (Dpred == DN_meas) and (Xpred == XN_meas)
        ok_cyc &= ok
        print(f"  K={K} r={r}: D_N pred {Dpred:>12} meas {DN_meas:>12}"
              f"  X_N pred {Xpred:>9} meas {XN_meas:>9}  {'PASS' if ok else 'FAIL'}")
        out["S2"].append({"K": K, "r": r, "D_N_cyclic_pred": Dpred,
                          "D_N_measured": DN_meas, "X_N_cyclic_pred": Xpred,
                          "X_N_measured": XN_meas, "match": ok})
        sys.stdout.flush()
    out["verdict"]["S2b_cyclic_prediction_exact"] = ok_cyc

    # ---------------- S3: census at r=6 -------------------------------
    print("\n[S3] collected-vector census at r=6 (0 < ||c||_1 <= 6):")
    from collections import Counter
    r74 = {(17, 6): (545020, 543940, 5040), (19, 6): (766460, 765380, 5760)}
    for A, N in [([[2, 1], [1, 1]], 3571), ([[2, 1], [1, 1]], 9349)]:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        if K not in (17, 19):
            continue
        DN, DZ, acc = census(A[0][0] + A[1][1], K, N, 6)
        triv, _ = predict_Z({i: [] for i in range(7)}, K, 6)
        DN_total = triv + DN
        DZ_total = triv + DZ
        pat = Counter()
        for c, w in acc:
            nz = sorted((abs(v) for v in c if v != 0))
            pat[tuple(nz)] += w
        Xacc = sum(w for _, w in acc)
        DN_meas, DZ_meas, XZ_meas = r74[(K, 6)]
        ok = (DN_total == DN_meas) and (DZ_total == DZ_meas)
        print(f"  A={A} N={N} K={K}: D_N(census)={DN_total} (r74 {DN_meas}) "
              f"D_Z(census)={DZ_total} (r74 {DZ_meas})  {'PASS' if ok else 'FAIL'}")
        print(f"     X_accidents={Xacc} (r74 X_N - X_Z = {DN_meas - DZ_meas}), "
              f"X_Z r74 = {XZ_meas}")
        print(f"     accident |coeff|-patterns -> total wc: {dict(pat)}")
        out["S3"].append({"A": A, "N": N, "K": K, "D_N_census": DN_total,
                          "D_Z_census": DZ_total, "X_accidents": Xacc,
                          "match_r74": ok,
                          "patterns": {str(k): v for k, v in pat.items()}})
        sys.stdout.flush()

    # ---------------- S4: midpoint class ------------------------------
    print("\n[S4] nontrivial midpoint class A^a + A^b = 2 A^c mod N:")
    for A, N in [([[2, 1], [1, 1]], 3571), ([[2, 1], [1, 1]], 9349)]:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        cnt, tri = midpoint_class(A, N, K)
        print(f"  N={N} K={K}: nontrivial ordered triples = {cnt} {tri[:12]}")
        out["S4"].append({"N": N, "K": K, "midpoint_triples": cnt,
                          "list": tri})

    # ---------------- S6: odd order D_5(Z) ----------------------------
    print("\n[S6] D_5 (odd order; Z-part = m-shape, cyclic D_5(N) = 2K*20):")
    t = 3
    Ue = chebyshev_exact(t, 40)
    for K, N in ((17, 3571), (19, 9349)):
        atomsZ = []
        for e in (1, -1):
            for j in range(K):
                atomsZ.append((e * Ue[j + 1], e * Ue[j]))
        tab = {}
        for combo in itertools.product(atomsZ, repeat=2):
            key = (combo[0][0] + combo[1][0], combo[0][1] + combo[1][1])
            tab[key] = tab.get(key, 0) + 1
        D5Z = 0
        for combo in itertools.product(atomsZ, repeat=3):
            key = (-(combo[0][0] + combo[1][0] + combo[2][0]),
                   -(combo[0][1] + combo[1][1] + combo[2][1]))
            D5Z += tab.get(key, 0)
        predZ = 2 * (K - 2) * wc_full((1, -3, 1), K, 5)
        # cyclic (mod N) count: atoms with U reduced mod N
        atomsN = [(a % N, b % N) for (a, b) in atomsZ]
        tab = {}
        for combo in itertools.product(atomsN, repeat=2):
            key = ((combo[0][0] + combo[1][0]) % N,
                   (combo[0][1] + combo[1][1]) % N)
            tab[key] = tab.get(key, 0) + 1
        D5N = 0
        for combo in itertools.product(atomsN, repeat=3):
            key = (-(combo[0][0] + combo[1][0] + combo[2][0]) % N,
                   -(combo[0][1] + combo[1][1] + combo[2][1]) % N)
            D5N += tab.get(key, 0)
        predN = 2 * K * wc_full((1, -3, 1), K, 5)
        ok = (D5Z == predZ) and (D5N == predN)
        print(f"  K={K}: D_5(Z) = {D5Z} (pred {predZ})   D_5(N) = {D5N} "
              f"(pred {predN})  {'PASS' if ok else 'FAIL'}")
        out["S6"].append({"K": K, "D5_Z": D5Z, "pred_Z": predZ,
                          "D5_N": D5N, "pred_N": predN, "match": ok})
        sys.stdout.flush()

    out["verdict"]["S6_odd_order_m_shape"] = all(s["match"] for s in out["S6"])

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r75", "multiples_structure.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("\nartifact ->", os.path.normpath(dest))
    print(f"total time {time.time() - t0:.1f} s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
