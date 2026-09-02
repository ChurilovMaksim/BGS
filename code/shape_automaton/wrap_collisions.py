"""
Run 80b: WRAP COINCIDENCES — the exact fibre structure of the shape-rotation
parametrisation of Theorem H.
=============================================================================

Run 80 (src/r80_jweight_dp.py) established, by exact Bessel-weighted automaton
DP:
  * X^Z_r(K)  (non-wrapping placements) matches the r74-r77 census EXACTLY
    through r = 12, padded shapes included;
  * the rotation-inclusive count 2K sum_sig wc  matches exactly through r = 8
    but OVERCOUNTS the census at r = 10 (by 41,126,400 at K=17) and
    r = 12 (by 97,037,740,800).

Mechanism claim to verify here: the map (sig, a, sign) -> collected vector
c = dense(a.sig mod K) is NOT injective once padded shapes exist.  A wrapping
rotation of a shape can equal another shape as a vector: this happens iff the
WRAPPED SUFFIX of sig is itself a multiple of m_t over Z.  Algebraically,

    sig_A = x^a sig_B - (x^K - 1) h(x),   m_t | h,   h = wrapped suffix,

because m_t | x^a sig_B and m_t | sig_A force m_t | (x^K-1)h, and
gcd(m_t, x^K - 1) = 1 over Q (the roots of m_t are not roots of unity).

This script DFS-enumerates all primitive shapes (L1 <= 12, width <= 17,
t = 3), builds the full preimage multiset of vectors, computes the collision
excess per order r, and checks it against the census deltas:

    collision_excess(r) = 2 sum_{c} (mult(c) - 1) wc(c, r)

    target r=10, K=17: 41,126,400
    target r=12, K=17: 97,037,740,800

It also emits the structure of the colliding preimages (families, rotation
offsets, wrapped suffixes) and the corrected X_full table.

Output: artifacts/r80/wrap_collisions.json
"""

from __future__ import annotations

import json
import math
import os
import time
from fractions import Fraction

T = 3
K = 17
RMAX = 12
WMAX = 17
F0 = Fraction(0)
F1 = Fraction(1)


# ---------------- series helpers (identical conventions to r80) ----------
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


_I_CACHE = {}


def I_ser(a, L):
    key = (a, L)
    if key not in _I_CACHE:
        s = [F0] * L
        k = 0
        while 2 * k + a < L:
            s[2 * k + a] = F1 / (math.factorial(k) * math.factorial(k + a))
            k += 1
        _I_CACHE[key] = s
    return _I_CACHE[key]


def wc_exact(cvec, r):
    """r! [y^r] prod_{j<K} I_{|c_j|}(2y) for the K-window vector (exact)."""
    L = r + 1
    prod = [F0] * L
    prod[0] = F1
    for c in cvec:
        if c:
            prod = ser_mul(prod, I_ser(abs(c), L), L)
        else:
            prod = ser_mul(prod, I_ser(0, L), L)
    return prod[r] * math.factorial(r)


# ---------------- automaton DFS: enumerate shapes -------------------------
LAM = (3 + math.sqrt(5.0)) / 2


def val_ok(a, b, rem):
    return abs(a + b * LAM) <= rem * (1 + 1e-12) + 1e-9


def trans(a, b, c):
    return (-b, a - c + T * b)


def enumerate_shapes(rmax, wmax):
    """All support-normalised multiples: digits (c_0..c_{w-1}) read TOP-DOWN
    with first (top) digit > 0; returned as tuples in TOP-DOWN order with
    width w = len.  The bottom digit c_0 of the polynomial is the LAST entry.
    """
    shapes = []  # list of (tuple_top_down, L1, width)

    def dfs(p, a, b, u, digits):
        if p >= wmax:
            return
        rem = rmax - u
        for c in range(-rem, rem + 1):
            if c == 0:
                continue
            u2 = u + abs(c)
            a2, b2 = trans(a, b, c)
            if not val_ok(a2, b2, rmax - u2):
                continue
            d2 = digits + [c]
            if (a2, b2) == (0, 0):
                shapes.append((tuple(d2), u2, p + 1))
            # continue (concatenations and beyond)
            if p + 1 < wmax:
                dfs(p + 1, a2, b2, u2, d2)
        # zero letter (internal gap) after the walk has started
        a2, b2 = trans(a, b, 0)
        if val_ok(a2, b2, rmax - u) and p + 1 < wmax:
            dfs(p + 1, a2, b2, u, digits + [0])

    # first letter positive
    for c in range(1, rmax + 1):
        a2, b2 = trans(0, 0, c)
        if not val_ok(a2, b2, rmax - c):
            continue
        if (a2, b2) == (0, 0):
            shapes.append(((c,), c, 1))
        if 1 < wmax:
            dfs(1, a2, b2, c, [c])
    return shapes


# ---------------- main ----------------------------------------------------
def main():
    t0 = time.time()
    shapes = enumerate_shapes(RMAX, WMAX)
    print(f"[r80b] shapes enumerated: {len(shapes)} "
          f"({round(time.time()-t0,1)} s)")
    by_R = {}
    for _, u, w in shapes:
        by_R[u] = by_R.get(u, 0) + 1
    print("  S(R) per L1:", {r: by_R.get(r, 0) for r in sorted(by_R)})

    # ---- vector preimage multiset (SIGNED vectors, no abs merging) ------
    # The census counts SIGNED vectors c (each once); wc depends on |c_j|
    # but distinct sign patterns are DISTINCT census vectors.  The
    # rotation-inclusive formula counts every (sig, a) of every shape AND of
    # its negation (the +- sign class): register signed vectors
    #     { rot_a(s) : s in shapes +- , a in [0,K) },
    # then  sum_v mult(v) wc(v) == 2K sum_sig wc   (exact consistency check),
    #       census vector count  == #distinct signed vectors,
    #       collision excess(r)  == sum_v (mult(v)-1) wc(v, r).
    from collections import defaultdict
    pre = defaultdict(list)
    for sig, u, w in shapes:
        vec = [0] * K
        for i, c in enumerate(sig):
            vec[w - 1 - i] = c
        for sgn in (1, -1):
            for a in range(K):
                v = [0] * K
                for j in range(K):
                    v[(j + a) % K] = sgn * vec[j]
                pre[tuple(v)].append((sig, sgn, a))

    n_vec = len(pre)
    n_pre = sum(len(v) for v in pre.values())
    print(f"  signed vectors: {n_vec}; preimage terms: {n_pre}")
    print(f"  consistency: n_pre == 2 * n_shapes * K: "
          f"{n_pre == 2 * len(shapes) * K} ({n_pre} vs {2*len(shapes)*K})")

    # internal consistency: sum mult*wc == 2K sum wc  at r=10
    from fractions import Fraction as _Fr
    chk = sum(len(plist) * wc_exact(key, 10)
              for key, plist in pre.items())
    tot_direct = _Fr(0)
    for sig, u, w in shapes:
        vec = [0] * K
        for i, c in enumerate(sig):
            vec[w - 1 - i] = c
        tot_direct += 2 * K * wc_exact(tuple(abs(x) for x in vec), 10)
    print(f"  consistency r=10: sum mult*wc = {chk} vs 2K*sum wc = {tot_direct}"
          f"  {'OK' if chk == tot_direct else '*** MISMATCH ***'}")

    # ---- collision excess per order r -----------------------------------
    L = RMAX + 1
    excess = {}
    over_vectors = {}
    for r in range(5, RMAX + 1):
        tot = 0
        overs = []
        for key, plist in pre.items():
            mult = len(plist)
            if mult > 1:
                wcv = wc_exact(key, r)
                tot += (mult - 1) * wcv
                overs.append((key, mult, str(wcv), plist))
        excess[r] = str(tot)
        if overs:
            over_vectors[r] = overs
        print(f"  r={r}: collision excess = {tot}")

    # ---- targets ---------------------------------------------------------
    ok10 = excess[10] == "41126400"
    ok12 = excess[12] == "97037740800"
    print(f"  TARGET r=10: 41,126,400 -> got {excess[10]} "
          f"{'OK' if ok10 else '*** MISMATCH ***'}")
    print(f"  TARGET r=12: 97,037,740,800 -> got {excess[12]} "
          f"{'OK' if ok12 else '*** MISMATCH ***'}")

    # ---- structure of the collisions -------------------------------------
    struct = []
    for key, mult, wcv, plist in over_vectors.get(10, []):
        struct.append({
            "vector_nonzero": {i: int(x) for i, x in enumerate(key) if x},
            "mult": mult,
            "wc_r10": wcv,
            "preimages": [
                {"shape_topdown": [int(x) for x in p[0]],
                 "sign": int(p[1]), "rotation": int(p[2])}
                for p in plist],
        })
    print(f"  r=10 over-counted classes: {len(struct)}")
    for s in struct[:12]:
        nz = s["vector_nonzero"]
        tags = [f"{'+' if p['sign']>0 else '-'}{p['shape_topdown']}@{p['rotation']}"
                for p in s["preimages"]]
        print(f"    mult={s['mult']} wc={s['wc_r10']} vec={nz}")
        for tg in tags:
            print(f"       {tg}")
    if len(struct) > 12:
        print(f"    ... and {len(struct)-12} more")

    out = {
        "meta": {
            "script": "src/r80_wrap_collisions.py",
            "date": "2026-08-29", "t": T, "K": K,
            "rmax": RMAX, "wmax": WMAX,
        },
        "n_shapes": len(shapes),
        "S_R": {str(r): by_R.get(r, 0) for r in sorted(by_R)},
        "n_abs_vectors": n_vec,
        "collision_excess": excess,
        "target_r10_ok": ok10,
        "target_r12_ok": ok12,
        "overcounted_classes_r10": struct,
        "n_overcounted_classes": {str(r): len(over_vectors.get(r, []))
                                  for r in range(5, RMAX + 1)},
    }
    dest = os.path.join("artifacts", "r80")
    os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "wrap_collisions.json"), "w") as f:
        json.dump(out, f, indent=1, default=str)
    print(f"[r80b] artifact -> {os.path.join(dest, 'wrap_collisions.json')}")
    print(f"[r80b] total {round(time.time()-t0,1)} s")


if __name__ == "__main__":
    main()
