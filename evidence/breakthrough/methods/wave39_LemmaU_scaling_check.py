"""Wave 39 task 2: scaling-degeneracy mechanism of Lemma U, exact checks.

R = Z[sqrt(2)], elements (a, b) = a + b*sqrt(2) mod N.
alpha = 3 + 2*sqrt(2), beta = alpha^2 = 17 + 12*sqrt(2), N(beta) = 1.
Constraining component: alpha^u == -1 mod p^f (u = m/2).
For pure-sqrt(2) parameter C = c*sqrt(2): Tr(C beta^k) = 4*c*B_k
where beta^k = A_k + B_k*sqrt(2).
block0 for (c*sqrt(2), 0) = {(4*c*B_k, 0) : k in Z/u}, block1 = -block0.
"""
from collections import Counter

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

def bseq(m, p, f):
    """B_k for k in Z/u, plus check beta^u == 1."""
    N = p ** f
    u = m // 2
    cur = (1, 0)
    Bs = []
    for _ in range(u):
        Bs.append(cur[1])
        cur = mul(cur, BETA, N)
    assert cur == (1, 0), f"beta^u != 1 at m={m}, p={p}, f={f}"
    return Bs

def saturation_report(Bs, p, f):
    """Check H2': {B_k} is a union of full mod-p fibers, each internally
    uniform. Returns (ok, S, mu_dict, detail)."""
    N = p ** f
    cnt = Counter(Bs)
    by = {}
    for x, c in cnt.items():
        by.setdefault(x % p, {})[x] = c
    ok = True
    S = sorted(by)
    mu = {}
    for r, d in by.items():
        if len(d) != p ** (f - 1):
            ok = False
        vals = set(d.values())
        if len(vals) != 1:
            ok = False
        else:
            mu[r] = vals.pop()
    # negation symmetry of multiplicities (should follow from B_{-k} = -B_k)
    for r in by:
        if mu.get(r) != mu.get((-r) % p):
            ok = False
    return ok, S, mu, {r: len(d) for r, d in by.items()}

def block_pair(c, Bs, N):
    b0 = Counter((4 * c * b % N, 0) for b in Bs)
    b1 = Counter(((-t) % N, 0) for (t, _) in b0.elements() for _ in [0])
    # block1 = -block0 as multiset: negate each pair
    b1 = Counter()
    for (t, s), n in b0.items():
        b1[((-t) % N, (-s) % N)] += n
    return b0, b1

print("=== (1) m=30 scaling group, component 25 (C^a), 29 (C^b = 0) ===")
Bs25 = bseq(30, 5, 2)
print("B_k mod 25:", Bs25)
ok, S, mu, det = saturation_report(Bs25, 5, 2)
print("H2' at (30,5,2):", ok, "S =", S, "mu =", mu, "lifts/class =", det)
# negation invariance of {B_k}
print("negation-invariant:", Counter(Bs25) == Counter((-b) % 25 for b in Bs25))
pairs = {}
for c in [1, 4, 6, 9, 11, 14, 16, 19, 21, 24]:
    b0, b1 = block_pair(c, Bs25, 25)
    pairs[c] = (b0, b1)
    print(f"c={c:2d}: block0==block1: {b0 == b1}, "
          f"distinct first coords: {len(b0)}")
ref = pairs[1]
print("all 10 values c = +-1 mod 5 give identical block pair:",
      all(v == ref for v in pairs.values()))
# scaling by lambda = 4 (== -1 mod 5) maps c=1 block to c=4 block
b0_1, _ = pairs[1]
b0_4, _ = pairs[4]
print("lambda=4 scales block0(c=1) to block0(c=4):",
      Counter((4 * t % 25, s) for (t, s) in b0_1.elements()) == b0_4)
# scaling by lambda = 2 (not +-1 mod 5) must FAIL
print("lambda=2 does NOT preserve block0(c=1):",
      Counter((2 * t % 25, s) for (t, s) in b0_1.elements()) != b0_1)
# G-orbit size of (c*sqrt(2), 0): rotations by beta (15 steps) x conjugation
def rot_orbit_size(c, m, p, f):
    N = p ** f
    C = (0, c)
    seen = set()
    cur = C
    for _ in range(m // 2):
        seen.add(cur)
        cur = mul(cur, BETA, N)
    conj = {(a, (-b) % N) for (a, b) in seen}
    return len(seen | conj), len(seen)
for c in [1, 4, 6, 9, 11]:
    tot, rot = rot_orbit_size(c, 30, 5, 2)
    print(f"c={c}: rotation orbit {rot}, G-orbit {tot}")
print("5 orbits x 30 =", 5 * 30, "(wave-37 scaling group size 150)")

print()
print("=== (2) H2' sweep: all constraining (m, p, f), p odd, p^f <= 10^5 ===")
def primes_upto(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, v in enumerate(sieve) if v]

fails = []
total = 0
for m in [12, 18, 24, 30, 36, 42, 48, 60]:
    for p in primes_upto(200):
        if p == 2:
            continue
        f = 1
        while p ** f <= 10 ** 5:
            if constraining(m, p, f):
                total += 1
                Bs = bseq(m, p, f)
                ok, S, mu, _ = saturation_report(Bs, p, f)
                if not ok:
                    fails.append((m, p, f, S, mu))
            f += 1
print(f"constraining components tested: {total}, H2' failures: {len(fails)}")
for row in fails[:20]:
    print("  FAIL:", row)
print()
print("=== (3) f=1 triviality + one more nontrivial case ===")
for (m, p, f) in [(30, 29, 1), (60, 5, 2), (12, 5, 2), (36, 5, 2)]:
    if constraining(m, p, f):
        Bs = bseq(m, p, f)
        ok, S, mu, _ = saturation_report(Bs, p, f)
        print(f"(m={m}, p={p}, f={f}): H2' = {ok}, S = {S}, mu = {mu}")
    else:
        print(f"(m={m}, p={p}, f={f}): not constraining")
