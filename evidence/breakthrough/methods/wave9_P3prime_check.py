"""Wave 9 task 3: checks for the P3' (3-adic) digit induction.

1. v3(D_m) = 2*f0, f0 = 1+v3(m/4), for 4|m.
2. SNF of M^m-I: v3(d1) = f0 (balanced), hence scaling.
3. Fix mod 3^e (e=2*f0): every entry divisible by 3^f0.
4. Component Lemma Y mod 3^e: per multiset, Y mod 3^e in one D4-orbit.
5. Top-digit formula for exponent f0: for y' mod 3^f0,
   Z' = Y'/3^(f0-1) mod 3  equals  n0 * v  (mod 3),
   where v = (y0', y1', -y0', -y1') mod 3, n0 = (m/4)/3^(f0-1) mod 3.
   (This is the heart of P3': Z' is determined by the mod-3 multiset
   up to D4, via the 3-type classification of v.)
Uses the SNF parametrisation from wave8_lemmaY_snf.py.
"""
import math
from collections import defaultdict
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c

def D_of_m(m):
    s_prev, s_cur = 2, 6
    if m == 1:
        return 4
    for _ in range(2, m + 1):
        s_prev, s_cur = s_cur, 6 * s_cur - s_prev
    return s_cur - 2

def fix_mod_q_snf(m, q, p):
    M = sp.Matrix([[6, -1], [1, 0]])
    A = M**m - sp.eye(2)
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    d1 = int(S[0, 0]); d2 = int(S[1, 1])
    e = vp(q, p); a = vp(d1, p)
    Vlist = [[int(V[i, j]) for j in range(2)] for i in range(2)]
    pts = []
    for Xp in range(p ** a):
        X = (p ** (e - a) * Xp) % q
        for Yp in range(p ** (e - a)):
            Y = (p ** a * Yp) % q
            y0 = (Vlist[0][0] * X + Vlist[0][1] * Y) % q
            y1 = (Vlist[1][0] * X + Vlist[1][1] * Y) % q
            seq = [y0, y1]
            for _ in range(m):
                seq.append((6 * seq[-1] - seq[-2]) % q)
            assert seq[m] == y0 and seq[m + 1] == y1
            pts.append(tuple(seq[:m]))
    assert len(pts) == q, (len(pts), q)
    return pts, (d1, d2, a, e)

def d4_orbit(vec):
    t = 4
    out = set()
    for b in range(t):
        out.add(tuple(vec[(r + b) % t] for r in range(t)))
        out.add(tuple(vec[(-r + b) % t] for r in range(t)))
    return out

def class_sums(vec, m, q):
    t = 4
    return tuple(sum(vec[i] for i in range(m) if i % t == r) % q for r in range(t))

def test_component(m):
    n = m // 4
    f0 = 1 + vp(n, 3)
    e = 2 * f0
    q = 3 ** e
    pts, (d1, d2, a, ee) = fix_mod_q_snf(m, q, 3)
    assert ee == e
    balanced = (a == f0)
    scaling = all(v % (3 ** f0) == 0 for vec in pts for v in vec)
    # component Lemma Y mod q
    by_ms = defaultdict(set)
    for vec in pts:
        ms = tuple(sorted(vec))
        Y = class_sums(vec, m, q)
        by_ms[ms].add(min(d4_orbit(Y)))
    bad = {ms: v for ms, v in by_ms.items() if len(v) > 1}
    print(f"m={m} f0={f0} e={e} q={q} SNF_a={a} balanced={balanced} "
          f"scaling={scaling} npts={len(pts)} nmultisets={len(by_ms)} bad={len(bad)}", flush=True)
    assert balanced and scaling and not bad
    return True

def test_top_digit(m):
    """Check Z' = n0 * v (mod 3) for all Fix mod 3^f0 points.

    NOTE (fixed vs first version): for exponent f0 < e = v3(D_m) the
    SNF parametrisation of fix_mod_q_snf does NOT apply (it assumes
    q || D). Here the period condition is automatic mod 3^f0, because
    v3(d1) = v3(d2) = f0, so M^m = I mod 3^f0 and Fix = ALL recurrence
    sequences: enumerate all (y0, y1) in (Z/q)^2 directly.
    """
    n = m // 4
    f0 = 1 + vp(n, 3)
    q = 3 ** f0
    n0 = (n // (3 ** (f0 - 1))) % 3
    pts = []
    for y0 in range(q):
        for y1 in range(q):
            seq = [y0, y1]
            for _ in range(m):
                seq.append((6 * seq[-1] - seq[-2]) % q)
            assert seq[m] == y0 and seq[m + 1] == y1, (m, y0, y1, seq[m], seq[m + 1])
            pts.append(tuple(seq[:m]))
    # v classification: group mod-3 multisets -> v up to D4
    by_ms_v = defaultdict(set)
    bad_top = 0
    for vec in pts:
        Y = class_sums(vec, m, q)
        # Y divisible by 3^(f0-1)?
        assert all(y % (3 ** (f0 - 1)) == 0 for y in Y), (m, vec, Y)
        Z = tuple((y // (3 ** (f0 - 1))) % 3 for y in Y)
        v = tuple([vec[0] % 3, vec[1] % 3, (-vec[0]) % 3, (-vec[1]) % 3])
        expect = tuple((n0 * x) % 3 for x in v)
        if Z != expect:
            bad_top += 1
            if bad_top <= 3:
                print("  TOP-DIGIT MISMATCH", m, vec, "Y", Y, "Z", Z, "expect", expect)
        ms3 = tuple(sorted(x % 3 for x in vec))
        by_ms_v[ms3].add(min(d4_orbit(v)))
    bad_v = {ms: v for ms, v in by_ms_v.items() if len(v) > 1}
    print(f"  top-digit m={m} f0={f0} q={q} n0={n0} bad_top={bad_top} "
          f"mod3-multisets={len(by_ms_v)} bad_v={len(bad_v)}", flush=True)
    assert bad_top == 0 and not bad_v
    return True

if __name__ == "__main__":
    for m in [4, 8, 12, 16, 20, 24, 28, 32, 36]:
        test_component(m)
        test_top_digit(m)
    print("ALL P3' CHECKS PASS")
