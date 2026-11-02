# Wave 33, task 4: test Q5 at p=13, P=13^5, m=14*13^3=30758.
# Q5 as stated: vertex equations + level-4 constraints force the
# level-5 twist to vanish (eta2 = 0). We test the single-tier-3-orbit
# case: eta0 = eta1 = 0, eta2 != 0 with Tr(C*eta2) = 0 for the unique
# tier-3 orbit C. If per-class multisets still match, Q5-as-stated
# is FALSE (vanishing is not forced), though G1 survives.
from collections import Counter
import random

p = 13
P = p ** 5
P3 = p ** 3


def add(x, y, M):
    return ((x[0] + y[0]) % M, (x[1] + y[1]) % M)


def mul(x, y, M):
    return ((x[0] * y[0] + 2 * x[1] * y[1]) % M, (x[0] * y[1] + x[1] * y[0]) % M)


def tr(x, M):
    return (2 * x[0]) % M


def pw(x, n, M):
    r = (1, 0)
    while n:
        if n & 1:
            r = mul(r, x, M)
        x = mul(x, x, M)
        n >>= 1
    return r


def vp(n):
    if n == 0:
        return 3  # 0 mod 13^3 means v >= 3, capped at 3
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


ALPHA = (3, 2)
# L0 = ord(alpha mod 13) = 14
cur = (1, 0)
L0 = None
for n in range(1, 200):
    cur = mul(cur, ALPHA, p)
    if cur == (1, 0):
        L0 = n
        break
assert L0 == 14
m = L0 * p ** 3
assert pw(ALPHA, m, P) == (1, 0)
g = pw(ALPHA, L0, P)
# u mod 13^3: gamma mod 13^7, divide by 169
Pbig = P * p ** 2
gb = pw(ALPHA, L0, Pbig)
u = (((gb[0] - 1) % Pbig) // p ** 2 % P3, (gb[1] % Pbig) // p ** 2 % P3)
u2 = mul(u, u, P3)
print(f"u mod 13^3 = {u}, u mod 13 = {(u[0] % p, u[1] % p)}")

APOW = [(1, 0)]
for _ in range(L0):
    APOW.append(mul(APOW[-1], ALPHA, P))


def tier_of(C):
    # v_13(Tr(C*u)) mod 13^3, capped: >=3 -> 3
    Cu = mul((C[0] % P3, C[1] % P3), u, P3)
    t = tr(Cu, P3)
    v = vp(t)
    return min(v, 3)


def T2_of(C):
    Cu2 = mul((C[0] % P3, C[1] % P3), u2, P3)
    return tr(Cu2, P3) % p


def orbits_of(A):
    # list of (i0, C, tier, T2) for the 14 gamma-orbits
    out = []
    for i0 in range(L0):
        C = mul(A, APOW[i0], P)
        t = tier_of(C)
        out.append((i0, C, t, T2_of(C) if t >= 2 else None))
    return out


def is_unit(A):
    return (A[0] * A[0] - 2 * A[1] * A[1]) % p != 0


random.seed(33)
found = []
tries = 0
while len(found) < 2 and tries < 5000:
    tries += 1
    A = (random.randrange(P), random.randrange(P))
    if not is_unit(A):
        continue
    obs = orbits_of(A)
    n3 = sum(1 for o in obs if o[2] == 3)
    n2 = sum(1 for o in obs if o[2] == 2)
    if n3 == 1 and n2 == 0:
        found.append((A, obs))
print(f"search tries: {tries}, found: {len(found)}")
for A, obs in found:
    print(f"A = {A}")
    for i0, C, t, T2 in obs:
        if t >= 2:
            print(f"  tier-{t} orbit i0={i0} C={C} T2={T2}")


def per_class(A):
    # classes i mod t, t = gcd(m,4) = 2
    cnt = [Counter(), Counter()]
    cur = A
    for i in range(m):
        cnt[i & 1][tr(cur, P)] += 1
        cur = mul(cur, ALPHA, P)
    return cnt


def solve_eta2(C):
    # nonzero eta2 in R/13 with Tr(C*eta2) = 0 mod 13; C mod 13 = (c0,c1)
    c0, c1 = C[0] % p, C[1] % p
    # Tr((c0+c1 s)(x+y s)) = 2(c0 x + 2 c1 y) = 0
    for x in range(p):
        for y in range(p):
            if (x, y) != (0, 0) and (c0 * x + 2 * c1 * y) % p == 0:
                return (x, y)
    raise AssertionError


for A, obs in found:
    (i0, C, t, T2) = [o for o in obs if o[2] == 3][0]
    eta2 = solve_eta2(C)
    print(f"\nA={A}: tier-3 orbit i0={i0}, C={C}, T2={T2}, eta2={eta2}")
    print(f"  Tr(C*eta2) mod 13 = {(2 * ((C[0] % p) * eta2[0] + 2 * (C[1] % p) * eta2[1])) % p} (need 0)")
    twist = (1 + p ** 4 * eta2[0], p ** 4 * eta2[1])  # 1 + p^4*eta2 mod P
    Ap = mul(A, twist, P)
    cA = per_class(A)
    cAp = per_class(Ap)
    match = all(cA[r] == cAp[r] for r in (0, 1))
    print(f"  per-class multisets match with eta2 != 0: {match}")
    # control: eta2' with Tr(C*eta2') != 0
    eta2b = None
    for x in range(p):
        for y in range(p):
            if (2 * ((C[0] % p) * x + 2 * (C[1] % p) * y)) % p != 0:
                eta2b = (x, y)
                break
        if eta2b:
            break
    twistb = (1 + p ** 4 * eta2b[0], p ** 4 * eta2b[1])
    Apb = mul(A, twistb, P)
    cApb = per_class(Apb)
    matchb = all(cA[r] == cApb[r] for r in (0, 1))
    print(f"  control eta2'={eta2b} (Tr != 0): per-class match: {matchb} (expect False)")
print("DONE")
