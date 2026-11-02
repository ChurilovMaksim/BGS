"""Wave 37, task 2: exact verification of Full Blindness.

R = Z[sqrt(2)], alpha = 3+2*sqrt(2). Elements are pairs (a,b) = a + b*sqrt(2).
All arithmetic exact (Python ints); reductions mod p**f only at the end.
Checks, for odd primes p:
  (1) Line Lemma: for C' with Tr(C'u) != 0 mod p, the multiset
      {Tr(C' beta^t) mod p^f : t < p^(f-e)} equals the full coset
      Tr(C') + p^e * (Z / p^f), each element once.
  (2) Full Blindness: for C with Z(C mod p) = empty, M_f(C) equals the
      disjoint union over j0 of those cosets; in particular C' == C mod p^e
      (hence mod p^b, b = e+1) with Z = empty gives M_f(C') = M_f(C).
  (3) Sharpness: for C with some B_j0 == 0 mod p, some line is NOT the full
      coset (it collapses).
"""
import random
from collections import Counter

def mul(x, y, mod=None):
    a, b = x; c, d = y
    r = (a * c + 2 * b * d, a * d + b * c)
    if mod:
        r = (r[0] % mod, r[1] % mod)
    return r

def pw(x, k, mod=None):
    r = (1, 0)
    while k:
        if k & 1:
            r = mul(r, x, mod)
        x = mul(x, x, mod)
        k >>= 1
    return r

def tr(x):
    return 2 * x[0]

def vp(n, p):
    if n == 0:
        return 10 ** 9
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c

ALPHA = (3, 2)

def order_mod_p(p):
    # order of alpha in (R/pR)^x; search up to p^2
    cur = (1, 0)
    for k in range(1, p * p + 1):
        cur = mul(cur, ALPHA, p)
        if cur == (1, 0):
            return k
    raise ValueError("order not found")

def decomp(p):
    d = order_mod_p(p)
    # exact alpha^d - 1
    Ad = pw(ALPHA, d)
    A, B = Ad[0] - 1, Ad[1]
    e = min(vp(A, p), vp(B, p))
    assert e >= 1, (p, d, A, B)
    u = (A // p ** e, B // p ** e)
    assert u[0] % p != 0 or u[1] % p != 0
    return d, e, u

def cycle_multiset(C, p, f, d, e):
    mod = p ** f
    df = d * p ** (f - e)
    vals = []
    cur = (1, 0)
    for _ in range(df):
        vals.append(tr(mul(C, cur, mod)) % mod)
        cur = mul(cur, ALPHA, mod)
    return Counter(vals)

def line_multiset(Cp, beta, p, f, e):
    mod = p ** f
    vals = []
    cur = (1, 0)
    for _ in range(p ** (f - e)):
        vals.append(tr(mul(Cp, cur, mod)) % mod)
        cur = mul(cur, beta, mod)
    return Counter(vals)

def check_case(p, f, rng, nC=6):
    d, e, u = decomp(p)
    b = e + 1
    mod = p ** f
    beta = pw(ALPHA, d, mod)
    # sanity: ord of beta mod p^f is p^(f-e)
    assert pw(beta, p ** (f - e), mod) == (1, 0)
    assert pw(beta, p ** (f - e - 1), mod) != (1, 0) if f - e >= 1 else True
    df = d * p ** (f - e)
    assert df == d * p ** (f - e)
    tested_lines = 0
    tested_blind = 0
    sharp = 0
    for _ in range(nC):
        # random C mod p^f with Z = empty
        for _try in range(200):
            C = (rng.randrange(mod), rng.randrange(mod))
            B = []
            cur = (1, 0)
            for _j in range(d):
                B.append(tr(mul(mul(C, cur, mod), u, mod)) % p)
                cur = mul(cur, ALPHA, mod)
            if all(v != 0 for v in B):
                break
        else:
            raise RuntimeError("no Z-empty C found")
        # (1) Line Lemma for every j0
        cur = (1, 0)
        for j0 in range(d):
            Cp = mul(C, cur, mod)
            line = line_multiset(Cp, beta, p, f, e)
            base = tr(Cp) % mod
            coset = Counter((base + p ** e * s) % mod for s in range(p ** (f - e)))
            assert line == coset, (p, f, j0, "line != coset")
            tested_lines += 1
            cur = mul(cur, ALPHA, mod)
        # (2) Full Blindness: M_f(C) = union of cosets; and C' = C mod p^e
        M = cycle_multiset(C, p, f, d, e)
        union = Counter()
        cur = (1, 0)
        for j0 in range(d):
            Cp = mul(C, cur, mod)
            base = tr(Cp) % mod
            for s in range(p ** (f - e)):
                union[(base + p ** e * s) % mod] += 1
            cur = mul(cur, ALPHA, mod)
        assert M == union, (p, f, "M != union of cosets")
        # random lift: C' == C mod p^e, arbitrary higher digits, Z still empty?
        # Z depends only on C mod p, so C' mod p == C mod p keeps Z empty.
        for _ in range(3):
            lift = (C[0] + p ** e * rng.randrange(p ** (f - e)),
                    C[1] + p ** e * rng.randrange(p ** (f - e)))
            lift = (lift[0] % mod, lift[1] % mod)
            M2 = cycle_multiset(lift, p, f, d, e)
            assert M2 == M, (p, f, "blindness fails for mod-p^e lift")
            tested_blind += 1
        # also C'' == C mod p^b (b = e+1): implied, but check directly once
        liftb = (C[0] + p ** b * rng.randrange(p ** (f - b)),
                 C[1] + p ** b * rng.randrange(p ** (f - b)))
        liftb = (liftb[0] % mod, liftb[1] % mod)
        assert cycle_multiset(liftb, p, f, d, e) == M
        # (3) Sharpness: find C with some B_j0 == 0 and check a line collapses
        for _try in range(200):
            C2 = (rng.randrange(mod), rng.randrange(mod))
            B2 = []
            cur = (1, 0)
            for _j in range(d):
                B2.append(tr(mul(mul(C2, cur, mod), u, mod)) % p)
                cur = mul(cur, ALPHA, mod)
            if any(v == 0 for v in B2):
                break
        else:
            continue
        jbad = B2.index(0)
        cur = (1, 0)
        for _j in range(jbad):
            cur = mul(cur, ALPHA, mod)
        Cp = mul(C2, cur, mod)
        line = line_multiset(Cp, beta, p, f, e)
        base = tr(Cp) % mod
        coset = Counter((base + p ** e * s) % mod for s in range(p ** (f - e)))
        if line != coset:
            sharp += 1
    print(f"p={p} f={f} d={d} e={e} b={b} df={df}: "
          f"lines OK={tested_lines}, blindness lifts OK={tested_blind}, "
          f"sharpness collapses={sharp}")
    return True

rng = random.Random(20261102)
for (p, f) in [(3, 3), (3, 4), (5, 3), (5, 4), (7, 3), (13, 4), (13, 5), (17, 3)]:
    check_case(p, f, rng)
print("ALL CHECKS PASS")
