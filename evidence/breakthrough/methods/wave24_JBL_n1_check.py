"""Wave 24, task 1: n=1 case of JBL — exact checks.
R = Z[sqrt(2)] as pairs (x, y); all arithmetic exact integers.
Repository untouched; no Lean build.
"""

def add(a, b): return (a[0]+b[0], a[1]+b[1])
def mul(a, b): return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
def mod(a, n): return (a[0] % n, a[1] % n)
def tr(a): return 2*a[0]
def conj(a): return (a[0], -a[1])
def pw(a, e):
    r = (1, 0)
    for _ in range(e): r = mul(r, a)
    return r

ALPHA = (3, 2)
BETA = pw(ALPHA, 4)  # alpha^4 = 577 + 408 sqrt(2)

# 1. beta mod 9 and beta^s mod 9
assert mod(BETA, 9) == (1, 3), mod(BETA, 9)
for s in range(8):
    assert mod(pw(BETA, s), 9) == (1, (3*s) % 9), s
print("1. beta^s mod 9 = 1 + 3s sqrt(2): OK")

# 2. Fix condition mod 9 forces 3 | B; then trace collapses.
# alpha^m - 1 = 3(m/4) sqrt(2) mod 9, so (alpha^m-1)B = 0 mod 9
# forces 3 | x, 3 | y; brute force over all B mod 9 at m=8, 12, 20.
import random
random.seed(24)
for m in (4, 8, 20, 28):
    k = m // 4
    am1 = (0, (3*k) % 9)  # alpha^m - 1 mod 9
    for x in range(9):
        for y in range(9):
            prod = mul(am1, (x, y))
            if prod[0] % 9 == 0 and prod[1] % 9 == 0:
                assert x % 3 == 0 and y % 3 == 0, (m, x, y)
print("2a. Fix condition mod 9 forces 3 | B (brute force, m=4,8,20,28): OK")
for _ in range(200):
    B = (3*random.randrange(-10**6, 10**6), 3*random.randrange(-10**6, 10**6))
    vals = {tr(mul(B, pw(BETA, s))) % 9 for s in range(6)}
    assert vals == {(2*B[0]) % 9}, (B, vals)
print("2b. Tr(B beta^s) mod 9 constant = 2 Re(B) mod 9 (genuine B): OK")

# 3. c_r formula: c_r(A) = 2 Re(A alpha^r) mod 9 = (2a, 6a+8b, 7a+3b, b)
for _ in range(200):
    A = (random.randrange(-10**6, 10**6), random.randrange(-10**6, 10**6))
    a, b = A
    expect = [(2*a) % 9, (6*a+8*b) % 9, (7*a+3*b) % 9, b % 9]
    got = [tr(mul(A, pw(ALPHA, r))) % 9 for r in range(4)]
    assert got == expect, (A, got, expect)
print("3. c_r(A) formula (2a, 6a+8b, 7a+3b, b) mod 9 (200 random A): OK")

# 4. Transport (genuine A only: alpha^4 = 1+3 sqrt(2) mod 9, so the
# alpha^{4q} correction 3qy vanishes mod 9 iff 3 | y, i.e. iff genuine):
# A' = A alpha^j -> c'_r = c_{r+j}; A' = conj(A) alpha^j -> c'_r = c_{-(r+j)}
def cvec(A):
    return [tr(mul(A, pw(ALPHA, r))) % 9 for r in range(4)]
for _ in range(200):
    A = (3*random.randrange(-10**6, 10**6), 3*random.randrange(-10**6, 10**6))
    j = random.randrange(4)
    c = cvec(A)
    assert cvec(mul(A, pw(ALPHA, j))) == [c[(r+j) % 4] for r in range(4)]
    assert cvec(mul(conj(A), pw(ALPHA, j))) == [c[(-(r+j)) % 4] for r in range(4)]
print("4. Transport c'_r = c_{r+j} (shift) / c_{-(r+j)} (reflection), genuine A: OK")

# 5. Wave-23 counterexample reproduction: m=8, p=3, q=9
D8 = 1331712
B = (887808, 1040400)
Bp = (887808, 596496)
a8m1 = add(pw(ALPHA, 8), (-1, 0))
for X in (B, Bp):
    prod = mul(a8m1, X)
    assert prod[0] % D8 == 0 and prod[1] % D8 == 0, X
assert mod(B, 512) == mod(Bp, 512) == (0, 16)
assert mod(B, 289) == mod(Bp, 289) == (0, 0)
assert mod(B, 9) == (3, 0) and mod(Bp, 9) == (3, 3)
def joint_class(X):
    return sorted((tr(mul(X, pw(BETA, s))) % 512,
                   tr(mul(X, pw(BETA, s))) % 9) for s in range(2))
assert joint_class(B) == joint_class(Bp) == [(0, 6), (0, 6)]
# B' not D-related to B mod 9: beta-orbit of B mod 9 under beta^j and conjugation
orbit = set()
for j in range(3):
    orbit.add(mod(mul(mod(B, 9), mod(pw(BETA, j), 9)), 9))
    orbit.add(mod(mul(mod(conj(B), 9), mod(pw(BETA, j), 9)), 9))
assert orbit == {(3, 0)} and (3, 3) not in orbit
print("5. Wave-23 counterexample reproduced; J equal [(0,6),(0,6)]; "
      "B' not D-related mod 9: OK")

# 6. Wave-22 slack example: m=6 vector identical from A=35 and A'=19635
D6 = 39200
def vec(A, m, D):
    return [tr(mul(A, pw(ALPHA, i))) % D for i in range(m)]
assert vec((35, 0), 6, D6) == vec((19635, 0), 6, D6) == [70, 210, 1190, 6930, 1190, 210]
assert (19635 - 17*35) % 32 == 0 and (19635 - 35) % 1225 == 0
print("6. m=6 slack example: identical vector; A' = 17*A mod 32, A' = A mod 1225: OK")

# 3b. For genuine A = 3(a'+b' sqrt(2)) mod 9: c-tuple = (6a', 6b', 3a', 3b') mod 9
for _ in range(200):
    ap, bp = random.randrange(3), random.randrange(3)
    A = (3*ap, 3*bp)
    assert cvec(A) == [(6*ap) % 9, (6*bp) % 9, (3*ap) % 9, (3*bp) % 9], A
print("3b. Genuine c-tuple = (6a', 6b', 3a', 3b') mod 9: OK")

# 7. Class-level n=1 collapse at m=8, 12, 20 (t=4): values mod 9 constant in class
for m in (4, 8, 20, 28):
    for _ in range(50):
        A = (3*random.randrange(-10**5, 10**5), 3*random.randrange(-10**5, 10**5))
        for r in range(4):
            vals = {tr(mul(A, pw(ALPHA, r+4*s))) % 9 for s in range(m//4)}
            assert len(vals) == 1, (m, A, r, vals)
print("7. Class mod-9 values constant at m=4, 8, 20, 28 (genuine A): OK")
print("ALL CHECKS PASS")
