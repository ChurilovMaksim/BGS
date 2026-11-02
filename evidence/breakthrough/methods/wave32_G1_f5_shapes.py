# Wave 32, task 1: (2,3) orbit-shape check at p=13, P=13^5, m=14*13^3.
# gamma = alpha^14, k=2. Tiers by v_13(Tr(Cu)), u=(gamma-1)/169 mod 13^3:
#  v=0 non-collapsed: 13^2 mod-13^4 fibers, top digit constant per fiber.
#  v=1 tier-1: 13 mod-13^4 fibers, top digit constant per fiber.
#  v=2 tier-2: 1 fiber, top digits = a*T1'' + C(a,2)*T2 (a in F_13), x13^2.
#  v>=3 tier-3: 1 fiber, top digits = C(a,2)*T2, x13^2.
from collections import Counter
p = 13; P = p**5; P4 = p**4; P3 = p**3

def add(x, y, M): return ((x[0]+y[0]) % M, (x[1]+y[1]) % M)
def mul(x, y, M): return ((x[0]*y[0]+2*x[1]*y[1]) % M, (x[0]*y[1]+x[1]*y[0]) % M)
def tr(x, M): return (2*x[0]) % M
def pw(x, n, M):
    r = (1, 0)
    while n:
        if n & 1: r = mul(r, x, M)
        x = mul(x, x, M); n >>= 1
    return r
def vp(n):
    v = 0
    while n % p == 0 and n != 0:
        n //= p; v += 1
    return v

ALPHA = (3, 2)
# order of alpha mod 13
cur = (1, 0); L0 = None
for n in range(1, 200):
    cur = mul(cur, (3 % p, 2 % p), p)
    if cur == (1, 0): L0 = n; break
print(f"L0 = {L0}")
assert L0 == 14
m = L0 * p**3
am = pw(ALPHA, m, P)
print(f"alpha^{m} mod {P} = {am} (need (1,0))")
assert am == (1, 0)
g = pw(ALPHA, L0, P)
d = ((g[0]-1) % P, g[1] % P)
print(f"gamma-1 valuations: {vp(d[0])}, {vp(d[1])} (need min 2)")
assert min(vp(d[0]), vp(d[1])) == 2
# u mod 13^3: gamma mod P*169, divide by 169
Pbig = P * p**2
gb = pw(ALPHA, L0, Pbig)
u = (((gb[0]-1) % Pbig)//p**2 % P3, (gb[1] % Pbig)//p**2 % P3)
print(f"u mod 13^3 = {u}, u mod 13 = {(u[0] % p, u[1] % p)}")
ubar = (u[0] % p, u[1] % p)

def T1(C):
    # Tr(C*u) mod 13^3; C mod P, u mod 13^3
    Cu = mul((C[0] % P3, C[1] % P3), u, P3)
    return tr(Cu, P3)

def lin_form(Cmod13):
    # Tr(C * ubar) mod 13
    return tr(mul(Cmod13, ubar, p), p)

# kernel of lin_form mod 13 (nonzero solutions)
ker = [(a, b) for a in range(p) for b in range(p) if (a, b) != (0, 0) and lin_form((a, b)) == 0]
print(f"nonzero kernel size mod 13: {len(ker)} (need 12)")
assert len(ker) == 12

def solve_lift(target):
    # X mod 13 with Tr(X*ubar) == target mod 13
    for X in [(a, b) for a in range(p) for b in range(p)]:
        if lin_form(X) == target % p:
            return X
    raise AssertionError

import random
random.seed(32)

def make_tier(tier):
    # returns C mod P with v_13(T1) == tier (tier 3 means >=3)
    C0 = random.choice([k for k in ker])
    # lift C0 (as reps 0..12) to mod 13^3: C = C0 + 13X + 169Y
    # Tr(C0*u) mod 13^3: C0 reps mod 13^3
    t0 = T1(C0)
    assert t0 % p == 0
    w1 = (t0 // p) % p  # Tr(C0*u) = 13*w1 mod 13^2 (w1 as element mod 13^2? careful)
    # Actually t0 in [0,13^3); t0 = 13*w1' with w1' in [0,13^2). Work mod 13^2 first.
    if tier == 1:
        # need w1' + Tr(X*ubar) != 0 mod 13, where w1' mod 13 = (t0//p) % 13
        need = (-(t0 // p) % p + 1) % p  # Tr(X*ubar) = need -> sum != 0
        X = solve_lift(need)
        C = (C0[0] + p*X[0], C0[1] + p*X[1])
    elif tier == 2:
        # kill mod 13^2: Tr(X*ubar) == -(t0//p) mod 13
        X = solve_lift(-(t0 // p) % p)
        C = (C0[0] + p*X[0], C0[1] + p*X[1])
        t = T1(C)
        assert t % p**2 == 0
        if t % p**3 == 0:
            # push to exactly v=2: add 169*Y with Tr(Y*ubar)=1
            Y = solve_lift(1)
            C = (C[0] + p**2*Y[0], C[1] + p**2*Y[1])
            t = T1(C)
        assert t % p**2 == 0 and t % p**3 != 0
    elif tier == 3:
        X = solve_lift(-(t0 // p) % p)
        C = (C0[0] + p*X[0], C0[1] + p*X[1])
        t = T1(C)
        assert t % p**2 == 0
        # kill mod 13^3: add 169*Y with Tr(Y*ubar) == -(t//169) mod 13
        Y = solve_lift(-(t // p**2) % p)
        C = (C[0] + p**2*Y[0], C[1] + p**2*Y[1])
        t = T1(C)
        assert t % p**3 == 0
    # random higher digits mod P (do not affect T1 mod 13^3)
    C = (C[0] + p**3*random.randrange(p**2), C[1] + p**3*random.randrange(p**2))
    C = (C[0] % P, C[1] % P)
    assert vp(T1(C)) == tier if tier < 3 else T1(C) % p**3 == 0
    return C

def orbit(C):
    gps = []
    cur = (1, 0)
    for j in range(p**3):
        gps.append(cur)
        cur = mul(cur, g, P)
    return [tr(mul(C, gj, P), P) for gj in gps]

def check_C(C, tier):
    # CORRECTED structure (debug 2026-11-02): the j*T1 term contributes
    # t*T1 to the top digit within a fiber, so non-collapsed/tier-1
    # fibers have FULL F_13 top-digit lines, not constants. Only
    # tier-2/3 orbits (single fiber, quadratic top digits) constrain.
    F = orbit(C)
    assert len(F) == p**3
    fib = {}
    for v in F:
        fib.setdefault(v % P4, []).append(v // P4)
    nfib = len(fib)
    # T2 = Tr(C*u^2) mod 13
    u2 = mul(u, u, P3)
    T2 = tr(mul((C[0] % P3, C[1] % P3), u2, P3), P3) % p
    res = f"tier {tier}: C={C} T1={T1(C)} nfib={nfib} T2={T2}"
    if tier == 0:
        # 169 fibers of size 13; each fiber's top digits = all of F_13 once
        assert nfib == p**2
        assert all(len(tops) == p and len(set(tops)) == p for tops in fib.values())
        res += " full-line fibers OK"
    elif tier == 1:
        # 13 fibers of size 169; each fiber's top digits = all of F_13 x13
        assert nfib == p
        assert all(len(tops) == p**2 and Counter(tops) == Counter({d: p for d in range(p)})
                   for tops in fib.values())
        res += " full-line fibers OK"
    elif tier in (2, 3):
        assert nfib == 1
        tops = list(fib.values())[0]
        cnt = Counter(tops)
        c4 = (tr(C, P) // P4) % p  # Tr(C)'s own top digit: constant offset
        if tier == 3:
            pred = Counter()
            for a in range(p):
                d = (c4 + a*(a-1)//2 * T2) % p
                pred[d] += p**2
        else:
            T1pp = (T1(C) // p**2) % p
            pred = Counter()
            for a in range(p):
                d = (c4 + a*T1pp + a*(a-1)//2 * T2) % p
                pred[d] += p**2
        assert cnt == pred, (cnt, pred)
        res += f" quadratic topdist OK"
    print(res)

# non-collapsed samples
for _ in range(5):
    while True:
        C = (random.randrange(P), random.randrange(P))
        if T1(C) % p != 0:
            break
    check_C(C, 0)
for tier, n in [(1, 5), (2, 5), (3, 3)]:
    for _ in range(n):
        check_C(make_tier(tier), tier)
print("ALL SHAPE CHECKS PASS")
