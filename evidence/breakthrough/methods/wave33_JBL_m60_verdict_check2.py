"""Wave 33, task 1, follow-up verification (independent of the main script's
CRT-merge code path):
 (1) mod-128 window is 4-periodic, so (y_i mod 128, y_i mod q) pairs equal
     wave-20's (p_{i mod P}, y_i mod q) pairs with P = t = 4;
 (2) a dihedral parameter transform (conj + alpha^k) makes the pair
     pi=id signature-equal, i.e. (A*, A') has IDENTICAL signatures;
 (3) pairwise CRT incompatibility for c=conj: residue sets mod small
     moduli, and the first incompatible component pair.
"""
from math import gcd
from collections import Counter

M = 60
ALPHA = (3, 2)
PAIRS = {
    128: ((0, 8), (32, 8)),
    81: ((9, 18), (72, 63)),
    625: ((0, 0), (0, 0)),
    49: ((0, 7), (0, 42)),
    121: ((11, 77), (110, 44)),
    841: ((29, 435), (29, 406)),
    1681: ((41, 861), (41, 820)),
    361: ((0, 0), (0, 0)),
    923521: ((0, 0), (0, 0)),
    3481: ((0, 0), (0, 0)),
    72361: ((0, 0), (0, 0)),
    361201: ((0, 0), (0, 0)),
    5202961: ((0, 0), (0, 0)),
}
PE = {81: 9, 625: 25, 49: 7, 121: 11, 361: 19, 841: 29,
      923521: 961, 1681: 41, 3481: 59, 72361: 269, 361201: 601,
      5202961: 2281}


def mul(a, b, q):
    return ((a[0] * b[0] + 2 * a[1] * b[1]) % q,
            (a[0] * b[1] + a[1] * b[0]) % q)


def tr_seq(A, q):
    out, cur = [], A
    for _ in range(60):
        out.append((2 * cur[0]) % q)
        cur = mul(cur, ALPHA, q)
    return tuple(out)


def crt_pair(residues):
    x, Mprod = 0, 1
    for v, m in residues:
        g = gcd(Mprod, m)
        assert (v - x) % g == 0
        p, q_ = Mprod // g, m // g
        t = ((v - x) // g * pow(p, -1, q_)) % q_
        x += Mprod * t
        Mprod *= q_
        x %= Mprod
    return x, Mprod


def crt_param(d):
    ax, D = crt_pair([(d[q][0], q) for q in sorted(d)])
    bx, D2 = crt_pair([(d[q][1], q) for q in sorted(d)])
    assert D == D2
    return (ax, bx), D


Aglob, D = crt_param({q: A for q, (A, _) in PAIRS.items()})
Apglob, _ = crt_param({q: Ap for q, (_, Ap) in PAIRS.items()})

# (1) 4-periodicity of the mod-128 window
win = tr_seq(Aglob, D)
per4 = all(win[i + 4] % 128 == win[i] % 128 for i in range(56))
print(f"(1) mod-128 window 4-periodic: {per4}")
assert per4

# (2) dihedral transforms making signatures pi=id equal
def class_joint(A, q):
    w = tr_seq(A, D)
    return {r: Counter((w[i] % 128, w[i] % q)
                       for i in range(60) if i % 4 == r) for r in range(4)}


def alpha_pow(k, q):
    cur = (1, 0)
    for _ in range(k % 4):
        cur = mul(cur, ALPHA, q)
    return cur


print("(2) dihedral transforms A* = conj^e(A) * alpha^k with J(A*) = J(A') (pi=id):")
for e in (0, 1):
    for k in range(4):
        def transform(Aq, q, e=e, k=k):
            base = (Aq[0], -Aq[1]) if e else Aq
            return mul(base, alpha_pow(k, q), q)
        Astar = {q: transform(Aglob_q, q) for q, Aglob_q in
                 ((q, (0, 0)) for q in ())}  # placeholder, replaced below
        # build Astar per component from global A via CRT-free route:
        # transform acts componentwise, so apply to PAIRS' A components.
        Astar_c = {q: transform(PAIRS[q][0], q) for q in PAIRS}
        Astar_g, _ = crt_param(Astar_c)
        ok = True
        for q in sorted(PAIRS):
            if q == 128:
                continue
            if class_joint(Astar_g, q) != class_joint(Apglob, q):
                ok = False
                break
        print(f"    e={e} (conj), k={k}: {'SIGNATURES IDENTICAL (pi=id)' if ok else 'no'}")

# (3) pairwise CRT incompatibility, c=conj, with residue sets recomputed
#     by direct search over j mod ord_q (orders recomputed independently).
def alpha_order(q):
    cur = (1, 0)
    for j in range(1, 10_000_000):
        cur = mul(cur, ALPHA, q)
        if cur == (1, 0):
            return j
    raise RuntimeError("order cap")


ANN = set()
for x in range(128):
    for y in range(128):
        cur, ok = (x, y), True
        for _ in range(60):
            if (2 * cur[0]) % 128 != 0:
                ok = False
                break
            cur = mul(cur, ALPHA, 128)
        if ok:
            ANN.add((x, y))
assert len(ANN) == 16


def residues_conj(q):
    Aq, Apq = PAIRS[q]
    base = (Aq[0], -Aq[1])
    ordq = alpha_order(q)
    cur = base
    res = set()
    for j in range(ordq):
        diff = ((Apq[0] - cur[0]) % q, (Apq[1] - cur[1]) % q)
        good = (diff in ANN) if q == 128 else \
            (diff[0] % 27 == 0 and diff[1] % 27 == 0) if q == 81 else \
            (diff[0] % 125 == 0 and diff[1] % 125 == 0) if q == 625 else \
            (diff == (0, 0))
        if good:
            res.add(j)
        cur = mul(cur, ALPHA, q)
    return res, ordq


sets = {}
for q in (49, 81, 121, 128, 841, 1681):
    res, ordq = residues_conj(q)
    sets[q] = (res, ordq)
    print(f"(3) c=conj q={q}: residues mod {ordq}: {sorted(res)}")


def compatible(T1, m1, T2, m2):
    g = gcd(m1, m2)
    c1 = {r % g for r in T1}
    c2 = {s % g for s in T2}
    return bool(c1 & c2), c1, c2


qs = [49, 81, 121, 128, 841, 1681]
for i in range(len(qs)):
    for j in range(i + 1, len(qs)):
        q1, q2 = qs[i], qs[j]
        T1, m1 = sets[q1]
        T2, m2 = sets[q2]
        ok, c1, c2 = compatible(T1, m1, T2, m2)
        if not ok:
            print(f"(3) INCOMPATIBLE pair: q={q1} residues mod gcd({m1},{m2})="
                  f"{gcd(m1, m2)} are {sorted(c1)}, q={q2} are {sorted(c2)} "
                  f"-> NO common j for c=conj, confirmed independently")
            raise SystemExit(0)
print("(3) all pairs among {49,81,121,128,841,1681} pairwise compatible; "
      "incompatibility must involve a longer chain (see main script merge)")
print("DONE")
