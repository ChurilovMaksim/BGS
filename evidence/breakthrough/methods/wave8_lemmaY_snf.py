"""Wave 8 task 1: component Lemma Y test for large prime powers via SNF.

M^m - I = U^{-1} diag(d1,d2) V^{-1} (sympy smith_normal_decomp: U*A*V=diag).
Kernel mod q (q = p^e || D): V^{-1} v = (X,Y) with d1*X=0, d2*Y=0 mod q,
i.e. X = p^{e-a} X', X' in Z/p^a; Y = p^a Y', Y' in Z/p^{e-a},
where a = v_p(d1). Then v = V*(X,Y) mod q, sequence by recurrence.
Check: multiset of sequence -> class-sum vector mod q up to D_t ?
"""
import math
import sympy as sp
from collections import defaultdict

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
    from sympy.matrices.normalforms import smith_normal_decomp
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    d1 = int(S[0, 0]); d2 = int(S[1, 1])
    assert d1 * d2 == int(A.det()) or d1 * d2 == -int(A.det()), (d1, d2, A.det())
    # valuations
    def vp(n):
        c = 0
        while n % p == 0:
            n //= p; c += 1
        return c
    e = vp(q)
    a = vp(d1)
    assert vp(d2) == e - a or True  # d1*d2 may have extra primes, but p-adic sum = e
    # V as list
    Vlist = [[int(V[i, j]) for j in range(2)] for i in range(2)]
    pts = []
    mod_a = p ** a
    mod_b = p ** (e - a)
    for Xp in range(mod_a):
        X = (p ** (e - a) * Xp) % q
        for Yp in range(mod_b):
            Y = (p ** a * Yp) % q
            y0 = (Vlist[0][0] * X + Vlist[0][1] * Y) % q
            y1 = (Vlist[1][0] * X + Vlist[1][1] * Y) % q
            seq = [y0, y1]
            for _ in range(m):
                seq.append((6 * seq[-1] - seq[-2]) % q)
            assert seq[m] == y0 and seq[m + 1] == y1, (m, q, y0, y1, seq[m], seq[m+1])
            pts.append(tuple(seq[:m]))
    assert len(pts) == q, (len(pts), q)
    return pts, (d1, d2, a, e)

def d_t_orbit(vec, t):
    out = set()
    for b in range(t):
        out.add(tuple(vec[(r + b) % t] for r in range(t)))
        out.add(tuple(vec[(-r + b) % t] for r in range(t)))
    return out

def test(m, q, p):
    pts, info = fix_mod_q_snf(m, q, p)
    t = math.gcd(m, 4)
    by_ms = defaultdict(set)
    for vec in pts:
        ms = tuple(sorted(vec))
        Y = tuple(sum(vec[i] for i in range(m) if i % t == r) % q for r in range(t))
        by_ms[ms].add(min(d_t_orbit(Y, t)))
    bad = {ms: v for ms, v in by_ms.items() if len(v) > 1}
    print(f"m={m} q={q} p={p} SNF={info} n={len(pts)} n_multisets={len(by_ms)} bad={len(bad)}", flush=True)
    if bad:
        ms, v = next(iter(bad.items()))
        print("  BAD", ms, v, flush=True)
    return len(bad) == 0

for (m, q, p) in [(14, 28561, 13), (14, 57121, 239), (18, 38809, 197), (18, 39601, 199), (16, 332929, 577)]:
    test(m, q, p)
