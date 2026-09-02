"""
Run 80: THE J-WEIGHTED RELATION AUTOMATON — the exact generating function of
the ensemble excess (R77.1 finally evaluated), census validation, ceiling
tables, and the uncapped shape growth S(R).
===========================================================================

Background.  R79 solved op:sofic_automaton: the support-normalised multiples
of m_t(x) = x^2 - t x + 1 (top-down normalised-tail automaton, states
sigma = a + b*lambda in Z[lambda], transition (a,b) --c--> (-b, a-c+3b),
a-priori bound |sigma| <= remaining L1) form a FINITE reachable set at every
budget, and the accepting walks are exactly the primitive shapes.

This script attaches the BESSEL WEIGHTS.  For a collected vector c in Z^K,

    wc(c, r) = r! * [y^r] prod_{j<K} I_{|c_j|}(2y)          (exact word count)

and Theorem H (cyclic shape decomposition, eps = +1) gives, with the shapes
summed over widths w <= K (K prime: the (sig, a, sign) parametrisation is
injective),

    X^Z_r(K)   = 2 r! [y^r] I_0(2y)^K * ( (K+1) Psi(y) - WPsi(y) ),
    X_full_r(K)= 2 K r! [y^r] I_0(2y)^K * Psi(y),
    wrap_r(K)  = X_full - X^Z = 2 r! [y^r] I_0(2y)^K * ( WPsi(y) - Psi(y) ),

where
    Psi(y)  = sum_{accepting walks} prod_{letters} J_{|c|}(2y),  J_c = I_c(2y)/I_0(2y),
    WPsi(y) = sum_{accepting walks} width * prod_{letters} J_{|c|}(2y),

and the walk letters INCLUDE internal zero gaps (J_0 = 1).  The identity
I_0(2y)^K * prod_letters J = prod_{j<K} I_{|c_j|}(2y) (the dense K-window
product) is what makes the [y^r] reading exact, cancelled pairs included.

Everything is exact rational arithmetic (fractions.Fraction).  Validations
built in:
  (V1) X^Z / full / wrap at K=17, r = 5,6,8,10,12 vs the r74-r77 census,
  (V2) X_full_5(19) = 760, X_full_6(19) = 6840,
  (V3) S_win(R;17) vs the R79 automaton counts (30,28,26,76,200,...),
  (V4) D_5(N) = X_full_5(17) = 680 = 2K*20 (Theorem H corollary),
  (V5) triv(r,K) = r! [y^{2s}] I_0(2y)^K at (6,17) = 538900 (R77.4 table).

New outputs (the point of the run):
  (N1) the ceiling table X_full_r(K)/triv(r,K) for r <= rmax, K in a design
       list -- the analytic uniformity ceiling (empirical target: the
       1.136/4.664/12.152/25.886 percent table at K=17),
  (N2) S(R) shape counts and the width distribution up to (rmax, Kmax),
  (N3) new exact excess values X_r(K) at r = 7, 9, 11 (never censused).

Output: artifacts/r80/jweight_dp.json
"""

from __future__ import annotations

import json
import math
import os
import sys
import time
from fractions import Fraction

T = 3
LAM_FLOAT = (3 + math.sqrt(5.0)) / 2  # 2.618...

F0 = Fraction(0)
F1 = Fraction(1)


# ----------------------------------------------------------------------
# truncated series in y (lists of Fraction, length L, index = degree)
# ----------------------------------------------------------------------
def ser_mul(a, b, L):
    out = [F0] * L
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if i + j >= L:
                break
            if bj == 0:
                continue
            out[i + j] += ai * bj
    return out


def ser_add(a, b):
    return [x + y for x, y in zip(a, b)]


def I_series(a, L):
    """I_a(2y) = sum_k y^{2k+a} / (k! (k+a)!)."""
    s = [F0] * L
    k = 0
    while 2 * k + a < L:
        s[2 * k + a] = F1 / (math.factorial(k) * math.factorial(k + a))
        k += 1
    return s


_I_CACHE = {}


def I_ser(a, L):
    key = (a, L)
    if key not in _I_CACHE:
        _I_CACHE[key] = I_series(a, L)
    return _I_CACHE[key]


def J_series(c, L):
    """J_c = I_c / I_0 (I_0 has constant term 1)."""
    num = I_ser(abs(c), L)
    den = I_ser(0, L)
    out = [F0] * L
    for d in range(L):
        acc = num[d]
        for e in range(1, d + 1):
            if den[e] != 0 and out[d - e] != 0:
                acc -= den[e] * out[d - e]
        out[d] = acc
    return out


_J_CACHE = {}


def J_ser(c, L):
    key = (c, L)
    if key not in _J_CACHE:
        _J_CACHE[key] = J_series(c, L)
    return _J_CACHE[key]


def I0_pow(K, L):
    """I_0(2y)^K by repeated squaring."""
    result = [F0] * L
    result[0] = F1
    base = I_ser(0, L)
    e = K
    while e > 0:
        if e & 1:
            result = ser_mul(result, base, L)
        base = ser_mul(base, base, L)
        e >>= 1
    return result


_I0P_CACHE = {}


def I0_pow_cached(K, L):
    key = (K, L)
    if key not in _I0P_CACHE:
        _I0P_CACHE[key] = I0_pow(K, L)
    return _I0P_CACHE[key]


# ----------------------------------------------------------------------
# automaton
# ----------------------------------------------------------------------
def trans(s, c):
    a, b = s
    return (-b, a - c + T * b)


def val_ok(s, rem):
    """|a + b*lambda| <= rem, float with safe slack (over-inclusive)."""
    return abs(s[0] + s[1] * LAM_FLOAT) <= rem * (1 + 1e-12) + 1e-9


# ----------------------------------------------------------------------
# the weighted DP over accepting walks
# ----------------------------------------------------------------------
def run_dp(rmax, Kmax, collect_counts=True):
    """
    DP over positions p = 0..Kmax-1 (the shape's digits read TOP-DOWN:
    the first letter is the TOP coefficient, normalised positive; the walk
    ends at its last nonzero letter, where sigma must be back to 0).

    State cell: (sigma=(a,b), u=L1 used, w=width so far) ->
        (weight series = prod_letters J, count)

    Accepting transitions: a nonzero digit landing on sigma = (0,0); the
    accepted walk is recorded AND the walk continues (concatenations).
    """
    L = rmax + 1
    t0 = time.time()
    # dp: dict (a,b,u,w) -> [weight series, count]
    dp = {}
    # position 0: first letter, nonzero, positive (support normalisation)
    for c in range(1, rmax + 1):
        u2 = c
        s2 = trans((0, 0), c)
        if not val_ok(s2, rmax - u2):
            continue
        key = (s2[0], s2[1], u2, 1)
        cell = dp.get(key)
        wt = J_ser(c, L)
        if cell is None:
            dp[key] = [wt, 1]
        else:
            cell[0] = ser_add(cell[0], wt)
            cell[1] += 1

    # per-width accumulators of ACCEPTED walks
    A_w = [None] * (Kmax + 1)      # A_w[w] = weight series
    cnt_wR = {}                    # (w, R) -> count of accepted walks

    for p in range(1, Kmax):
        ndp = {}
        w2 = p + 1
        for (a, b, u, w), (wt, cnt) in dp.items():
            s = (a, b)
            # zero letter (internal gap; also the closed-block gap at (0,0))
            s2 = trans(s, 0)
            if val_ok(s2, rmax - u):
                key = (s2[0], s2[1], u, w)
                cell = ndp.get(key)
                if cell is None:
                    ndp[key] = [wt, cnt]
                else:
                    cell[0] = ser_add(cell[0], wt)
                    cell[1] += cnt
            # nonzero letters
            rem = rmax - u
            for c in range(-rem, rem + 1):
                if c == 0:
                    continue
                u2 = u + abs(c)
                s2 = trans(s, c)
                if not val_ok(s2, rmax - u2):
                    continue
                Jc = J_ser(abs(c), L)
                wt2 = ser_mul(wt, Jc, L)
                cnt2 = cnt
                if s2 == (0, 0):
                    # ACCEPT: a shape of width w2, L1 u2 -- and continue
                    if A_w[w2] is None:
                        A_w[w2] = [F0] * L
                        cnt_wR[(w2, u2)] = 0
                    A_w[w2] = ser_add(A_w[w2], wt2)
                    cnt_wR[(w2, u2)] = cnt_wR.get((w2, u2), 0) + cnt2
                key = (s2[0], s2[1], u2, w2)
                cell = ndp.get(key)
                if cell is None:
                    ndp[key] = [wt2, cnt2]
                else:
                    cell[0] = ser_add(cell[0], wt2)
                    cell[1] += cnt2
        dp = ndp
        if not dp:
            break
    stats = {"rmax": rmax, "Kmax": Kmax, "seconds": round(time.time() - t0, 1)}
    return A_w, cnt_wR, stats


# ----------------------------------------------------------------------
# aggregation
# ----------------------------------------------------------------------
def excess_from_Aw(Aw, rmax, Kmax, K, r):
    """returns (X_Z, X_full, wrap) exact integers for order r.

    Only shapes with width w <= K contribute: a placement in the cyclic
    window needs w <= K, and shapes with w > K reduce to MERGED vectors
    that are not clean placements (they are the M_r bookkeeping, not here).
    """
    L = rmax + 1
    I0K = I0_pow_cached(K, L)
    Psi = [F0] * L
    WPsi = [F0] * L
    for w in range(1, min(Kmax, K) + 1):
        aw = Aw[w]
        if aw is None:
            continue
        Psi = ser_add(Psi, aw)
        WPsi = ser_add(WPsi, [x * w for x in aw])
    def grab(G):
        s = F0
        for d in range(r + 1):
            if I0K[d] != 0 and G[r - d] != 0:
                s += I0K[d] * G[r - d]
        return s * math.factorial(r)
    xz = grab([(K + 1) * p - q for p, q in zip(Psi, WPsi)]) * 2
    xf = grab(Psi) * 2 * K
    return xz, xf, xf - xz


def triv_count(r, K, rmax):
    """rank-0 word count r! [y^{2s}] I_0(2y)^K (r = 2s; 0 for odd r)."""
    if r % 2 == 1:
        return 0
    L = rmax + 1
    I0K = I0_pow_cached(K, L)
    return I0K[r] * math.factorial(r)


def s_win(cnt_wR, R, K):
    """2 * sum_w (K+1-w) * #shapes(L1=R, width=w)  (translate-inclusive)."""
    tot = 0
    for (w, rr), c in cnt_wR.items():
        if rr == R and w <= K:
            tot += 2 * (K + 1 - w) * c
    return tot


# ----------------------------------------------------------------------
# main
# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    rmax = 12
    Kmax = 41
    out = {"meta": {
        "script": "src/r80_jweight_dp.py",
        "date": "2026-08-29",
        "t": T,
        "rmax": rmax, "Kmax": Kmax,
        "description": "J-weighted relation automaton: exact Psi(y), census "
                       "validation, ceiling tables, shape growth",
    }}

    print(f"[r80] DP rmax={rmax} Kmax={Kmax} (exact rationals) ...")
    Aw, cnt_wR, stats = run_dp(rmax, Kmax)
    out["dp_stats"] = stats
    print(f"      done in {stats['seconds']} s")

    # ---- validations -------------------------------------------------
    val = {}
    targets = {  # r -> (K, X_Z, X_full, wrap) from the r74-r77 censuses
        5:  (17, 600, 680, 80),
        6:  (17, 5040, 6120, 1080),
        8:  (17, 4454240, 5464480, 1010240),
        10: (17, 3107822760, 3860398080, 752575320),
        12: (17, 2093152388976, 2642357918376, 549205529400),
    }
    ok_all = True
    for r, (K, xz_t, xf_t, wr_t) in sorted(targets.items()):
        xz, xf, wr = excess_from_Aw(Aw, rmax, Kmax, K, r)
        ok = (xz == xz_t and xf == xf_t and wr == wr_t)
        ok_all &= ok
        val[f"r{r}_K{K}"] = {"X_Z": str(xz), "X_Z_target": str(xz_t),
                             "X_full": str(xf), "X_full_target": str(xf_t),
                             "wrap": str(wr), "wrap_target": str(wr_t),
                             "ok": ok}
        print(f"  V1 r={r} K={K}: X_Z={xz} (target {xz_t}) "
              f"X_full={xf} (target {xf_t}) wrap={wr} (target {wr_t}) "
              f"{'OK' if ok else '*** MISMATCH ***'}")
    # K=19
    for r, xf_t in ((5, 760), (6, 6840)):
        _, xf, _ = excess_from_Aw(Aw, rmax, Kmax, 19, r)
        ok = xf == xf_t
        ok_all &= ok
        val[f"r{r}_K19_full"] = {"X_full": str(xf), "target": str(xf_t), "ok": ok}
        print(f"  V2 r={r} K=19: X_full={xf} (target {xf_t}) "
              f"{'OK' if ok else '*** MISMATCH ***'}")
    # S_win vs R79
    r79 = {5: 30, 6: 28, 7: 26, 8: 76, 9: 200, 10: 624,
           11: 1064, 12: 1760}
    for R, target in r79.items():
        got = s_win(cnt_wR, R, 17)
        ok = got == target
        ok_all &= ok
        val[f"swin_R{R}_K17"] = {"got": got, "target": target, "ok": ok}
        print(f"  V3 S_win({R};17) = {got} (target {target}) "
              f"{'OK' if ok else '*** MISMATCH ***'}")
    # triv(6,17)
    tv = triv_count(6, 17, rmax)
    ok = tv == 538900
    ok_all &= ok
    val["triv_6_17"] = {"got": str(tv), "target": "538900", "ok": ok}
    print(f"  V5 triv(6,17) = {tv} (target 538900) {'OK' if ok else '*** MISMATCH ***'}")
    out["validations"] = val
    out["validations_all_ok"] = ok_all

    # ---- new exact values: r = 7, 9, 11 at K = 17 --------------------
    new = {}
    for r in (7, 9, 11):
        xz, xf, wr = excess_from_Aw(Aw, rmax, Kmax, 17, r)
        new[f"r{r}_K17"] = {"X_Z": str(xz), "X_full": str(xf), "wrap": str(wr)}
        print(f"  N3 r={r} K=17: X_Z={xz} X_full={xf} wrap={wr}")
    out["new_exact_values"] = new

    # ---- ceiling table ----------------------------------------------
    Ks = [17, 19, 23, 25, 29, 31, 35, 37, 41]
    ceil_tab = {}
    for K in Ks:
        row = {}
        for r in range(5, rmax + 1):
            _, xf, _ = excess_from_Aw(Aw, rmax, Kmax, K, r)
            tv = triv_count(r, K, rmax)
            row[f"r{r}"] = {
                "X_full": str(xf), "triv": str(tv),
                "ratio": (float(xf) / float(tv)) if tv else None,
            }
        ceil_tab[f"K{K}"] = row
    out["ceiling_table"] = ceil_tab
    print("  N1 ceiling table (X_full/triv):")
    for K in Ks:
        cells = []
        for r in range(6, rmax + 1, 2):
            ratio = ceil_tab[f"K{K}"][f"r{r}"]["ratio"]
            cells.append(f"r{r}:{'--' if ratio is None else format(ratio, '.4f')}")
        print(f"    K={K}: " + "  ".join(cells))

    # ---- shape counts S(R) and the width distribution -----------------
    SR = {}
    for (w, R), c in cnt_wR.items():
        SR[R] = SR.get(R, 0) + c
    out["S_R_uncapped_at_Kmax"] = {str(r): SR.get(r, 0) for r in sorted(SR)}
    width_dist = {}
    for R in sorted({rr for (_, rr) in cnt_wR}):
        width_dist[f"L1={R}"] = {str(w): c
                                 for (w, rr), c in sorted(cnt_wR.items())
                                 if rr == R}
    out["width_distribution"] = width_dist
    print("  N2 S(R) (width <= Kmax):",
          {r: SR.get(r, 0) for r in sorted(SR)})

    # growth fit S(R)^(1/R)
    fit = {}
    for R in sorted(SR):
        if SR[R] > 0 and R >= 6:
            fit[R] = round(SR[R] ** (1.0 / R), 4)
    out["growth_constant_S_R"] = fit
    print("  N2b S(R)^(1/R):", fit)

    dest = os.path.join("artifacts", "r80")
    os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "jweight_dp.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(f"[r80] artifact -> {os.path.join(dest, 'jwidth_dp.json')}"
          if False else f"[r80] artifact -> {os.path.join(dest, 'jweight_dp.json')}")
    print(f"[r80] total {round(time.time()-t0,1)} s; ALL VALIDATIONS "
          f"{'PASS' if ok_all else 'FAIL'}")


if __name__ == "__main__":
    main()
