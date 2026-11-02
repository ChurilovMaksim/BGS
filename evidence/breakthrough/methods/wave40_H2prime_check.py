"""Wave 40 task 2: H2' lift-sweeping lemma — numerical verification.

Checks, for every constraining (m, p, f) in scope:
  d = ord_p(beta)                       (order of beta mod p)
  growth = (beta^d != 1 mod p^2)        (for f >= 2; vacuous for f = 1)
  fourdiv = (4 | d)
  H2' = saturation of {B_k} (wave-39 report)
Theorem to verify: (growth and not fourdiv) => H2'.
Also: order mod p^f equals d*p^(f-1) under growth (growth lemma),
the factorisation equivalence B_a == B_b  <=>  (beta^(td)-1)(beta^(a+b)+1) == 0,
and the dividing line (42,13,2).
"""
from collections import Counter
import random

def mul(x, y, N):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % N, (x[0]*y[1] + x[1]*y[0]) % N)

def pw(x, e, N):
    r = (1, 0)
    while e:
        if e & 1:
            r = mul(r, x, N)
        x = mul(x, x, N)
        e >>= 1
    return r

ALPHA = (3, 2)
BETA = (17, 12)

def constraining(m, p, f):
    N = p ** f
    return pw(ALPHA, m // 2, N) == (N - 1, 0)

def ord_p(p):
    cur = (1, 0)
    for k in range(1, p * p + 2):
        cur = mul(cur, BETA, p)
        if cur == (1, 0):
            return k
    raise RuntimeError(f"no order mod {p}")

def ord_pf(p, f):
    # order of BETA mod p^f by iteration (only used for tiny N)
    N = p ** f
    cur = (1, 0)
    for k in range(1, N * N + 2):
        cur = mul(cur, BETA, N)
        if cur == (1, 0):
            return k
    raise RuntimeError(f"no order mod {N}")

def bseq(m, p, f):
    N = p ** f
    u = m // 2
    cur = (1, 0)
    Bs = []
    for _ in range(u):
        Bs.append(cur[1])
        cur = mul(cur, BETA, N)
    assert cur == (1, 0), f"beta^u != 1 at m={m}, p={p}, f={f}"
    return Bs

def saturation(Bs, p, f):
    cnt = Counter(Bs)
    by = {}
    for x, c in cnt.items():
        by.setdefault(x % p, {})[x] = c
    ok = True
    for r, d in by.items():
        if len(d) != p ** (f - 1):
            ok = False
        if len(set(d.values())) != 1:
            ok = False
    return ok

def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

def sweep(ms, label):
    print(f"=== {label} ===")
    rows = []
    viol = []
    fourdiv_rows = []
    for m in ms:
        for p in primes_upto(200):
            if p == 2:
                continue
            f = 1
            while p ** f <= 10 ** 5:
                if constraining(m, p, f):
                    Bs = bseq(m, p, f)
                    h2 = saturation(Bs, p, f)
                    d = ord_p(p)
                    growth = True if f == 1 else (pw(BETA, d, p * p) != (1, 0))
                    fd = (d % 4 == 0)
                    rows.append((m, p, f, d, growth, fd, h2))
                    if growth and not fd and not h2:
                        viol.append((m, p, f, d))
                    if fd:
                        fourdiv_rows.append((m, p, f, d, growth, h2))
                f += 1
    print(f"components: {len(rows)}, theorem violations "
          f"(growth & 4∤d but H2' fails): {len(viol)}")
    for v in viol:
        print("  VIOLATION:", v)
    n_growth = sum(1 for r in rows if r[4])
    n_h2 = sum(1 for r in rows if r[6])
    n_both_fail = sum(1 for r in rows if not r[4] and not r[6])
    print(f"growth holds: {n_growth}, H2' holds: {n_h2}, "
          f"both fail: {n_both_fail}")
    print(f"4|d components: {len(fourdiv_rows)}")
    for r in fourdiv_rows:
        print(f"  4|d: m={r[0]}, p={r[1]}, f={r[2]}, d={r[3]}, "
              f"growth={r[4]}, H2'={r[5]}")
    return rows

rows_a = sweep([12, 18, 24, 30, 36, 42, 48, 60], "Sweep A (wave-39 scope)")
rows_b = sweep(list(range(6, 122, 2)), "Sweep B (all even m <= 120)")

print()
print("=== Growth lemma: ord mod p^f == d*p^(f-1) under growth ===")
# ord is a multiple of d (reduction mod p) and divides d*p^(f-1) iff
# beta^(d*p^(f-1)) == 1 mod p^f; it equals d*p^(f-1) iff additionally
# beta^(d*p^(f-2)) != 1 mod p^f (for f >= 2). Fast via pw.
bad_ord = 0
checked_ord = 0
for (m, p, f, d, growth, fd, h2) in rows_a + rows_b:
    if f >= 2 and growth:
        N = p ** f
        a = pw(BETA, d * p ** (f - 1), N) == (1, 0)
        b = pw(BETA, d * p ** (f - 2), N) != (1, 0)
        checked_ord += 1
        if not (a and b):
            bad_ord += 1
            print(f"  MISMATCH: m={m}, p={p}, f={f}, d={d}, "
                  f"beta^(d*p^(f-1))==1: {a}, beta^(d*p^(f-2))!=1: {b}")
print(f"growth-lemma order check: {checked_ord} components, "
      f"{bad_ord} mismatches")

print()
print("=== Dividing line (42,13,2) ===")
d13 = ord_p(13)
print(f"d = ord_13(beta) = {d13}")
print(f"beta^d mod 169 == 1: {pw(BETA, d13, 169) == (1, 0)}")
print(f"period mod 169 = {ord_pf(13, 2)}, fiber size p^(f-1) = 13")
Bs = bseq(42, 13, 2)
print(f"H2' at (42,13,2): {saturation(Bs, 13, 2)}, "
      f"distinct B values: {len(set(Bs))} (u=21)")

print()
print("=== Factorisation equivalence (random pairs) ===")
random.seed(40)
bad = 0
tested = 0
for (m, p, f) in [(30, 5, 2), (36, 3, 3), (12, 3, 2), (60, 11, 1)]:
    N = p ** f
    u = m // 2
    # beta powers mod N
    pws = [(1, 0)]
    for _ in range(u):
        pws.append(mul(pws[-1], BETA, N))
    assert pws[u] == (1, 0)
    for _ in range(300):
        a = random.randrange(u)
        b = random.randrange(u)
        Ba, Bb = pws[a][1], pws[b][1]
        t = a - b
        # (beta^(td)-1)(beta^(a+b)+1) mod N, with td = a-b directly
        y = pws[a % u]  # placeholder, recompute properly below
        # beta^(a-b) mod N:
        y = pw(BETA, a - b, N) if a >= b else pw(BETA, a - b + u, N)
        # beta^(a+b) mod N:
        s = pw(BETA, a + b, N)
        lhs = (Ba == Bb)
        prod = mul(((y[0] - 1) % N, y[1]),
                   ((s[0] + 1) % N, s[1]), N)
        rhs = (prod == (0, 0))
        tested += 1
        if lhs != rhs:
            bad += 1
            print(f"  MISMATCH at {(m, p, f)} a={a} b={b}")
print(f"factorisation equivalence: {tested} pairs, {bad} mismatches")
