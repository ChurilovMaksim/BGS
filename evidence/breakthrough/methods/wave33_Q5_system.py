# Wave 33, task 4: solve the Q5 system for a paired tier-3/tier-2
# sequence at p=13, and test a nonzero-eta2 solution directly.
# System on (eta0, eta2) in (R/13)^2:
#   Tr(eta0) = 0;  Tr(D*eta0) = 0 per tier-2/3 orbit (D = 13-digit of C);
#   vertex eq per tier-2/3 orbit (s = Tr(C*eta0*u), r = Tr(C*eta2)):
#     tier-3, T2 != 0: 2*T2*r = s*(s-T2);  tier-3, T2 == 0: s = r = 0;
#     tier-2, T2 != 0: 2*T2*r = s*(s+2*T1pp-T2); tier-2, T2 == 0: none.
from collections import Counter
import random

p = 13
P = p ** 5
P3 = p ** 3
P4 = p ** 4


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


def vp3(n):
    # v_13(n) for n mod 13^3, capped at 3 (n==0 -> 3)
    if n == 0:
        return 3
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


ALPHA = (3, 2)
L0 = 14
m = L0 * p ** 3
assert pw(ALPHA, m, P) == (1, 0)
g = pw(ALPHA, L0, P)
Pbig = P * p ** 2
gb = pw(ALPHA, L0, Pbig)
u = (((gb[0] - 1) % Pbig) // p ** 2 % P3, (gb[1] % Pbig) // p ** 2 % P3)
u2 = mul(u, u, P3)
ubar = (u[0] % p, u[1] % p)
APOW = [(1, 0)]
for _ in range(L0):
    APOW.append(mul(APOW[-1], ALPHA, P))


def orbit_data(A):
    # per gamma-orbit: (i0, C, tier, D, T1pp, T2)
    out = []
    for i0 in range(L0):
        C = mul(A, APOW[i0], P)
        Cu = mul((C[0] % P3, C[1] % P3), u, P3)
        t1 = tr(Cu, P3)
        tier = vp3(t1)
        Cm13 = (C[0] % p, C[1] % p)
        D = ((C[0] % p ** 2) // p, (C[1] % p ** 2) // p)  # 13-digit of C
        Cu2 = mul((C[0] % P3, C[1] % P3), u2, P3)
        T2 = tr(Cu2, P3) % p
        T1pp = (t1 // p ** 2) % p if tier == 2 else None
        out.append((i0, C, tier, D, T1pp, T2, Cm13))
    return out


def is_unit(A):
    return (A[0] * A[0] - 2 * A[1] * A[1]) % p != 0


def tr13(X, Y):
    # Tr(X*Y) mod 13, X,Y in R/13
    return (2 * (X[0] * Y[0] + 2 * X[1] * Y[1])) % p


random.seed(33)
A = None
obs = None
for trial in range(5000):
    Ac = (random.randrange(P), random.randrange(P))
    if not is_unit(Ac):
        continue
    ob = orbit_data(Ac)
    ts = [o[2] for o in ob]
    if ts.count(3) == 1 and ts.count(2) == 1:
        A, obs = Ac, ob
        break
assert A is not None
print(f"A = {A}")
hi = [o for o in obs if o[2] >= 2]
for o in hi:
    print(f"  i0={o[0]} tier={o[2]} C={o[1]} Cmod13={o[6]} D={o[3]} T1pp={o[4]} T2={o[5]}")
# pairing check: tier-3 i0 vs tier-2 i0 differ by 7 mod 14?
i3 = [o[0] for o in hi if o[2] == 3][0]
i2 = [o[0] for o in hi if o[2] == 2][0]
print(f"  pairing: i3={i3}, i2={i2}, diff mod 14 = {(i2 - i3) % 14} (expect 7)")

# solve the system over (eta0, eta2)
sols = []
for e0a in range(p):
    for e0b in range(p):
        eta0 = (e0a, e0b)
        if tr13((1, 0), eta0) != 0:  # Tr(eta0) = 0
            continue
        ok0 = True
        for o in hi:
            if tr13(o[3], eta0) != 0:  # Tr(D*eta0) = 0
                ok0 = False
                break
        if not ok0:
            continue
        for e2a in range(p):
            for e2b in range(p):
                eta2 = (e2a, e2b)
                ok = True
                for o in hi:
                    i0, C, tier, D, T1pp, T2, Cm13 = o
                    s = tr13(mul(Cm13, ubar, p), eta0)
                    r = tr13(Cm13, eta2)
                    if tier == 3:
                        if T2 == 0:
                            if s != 0 or r != 0:
                                ok = False
                        elif (2 * T2 * r - s * (s - T2)) % p != 0:
                            ok = False
                    else:  # tier 2
                        if T2 != 0 and (2 * T2 * r - s * (s + 2 * T1pp - T2)) % p != 0:
                            ok = False
                    if not ok:
                        break
                if ok:
                    sols.append((eta0, eta2))
nz = [s for s in sols if s[1] != (0, 0)]
print(f"system solutions: {len(sols)}; with eta2 != 0: {len(nz)}")
print(f"  sample nonzero-eta2 solutions: {nz[:5]}")


def per_class(Ax):
    cnt = [Counter(), Counter()]
    cur = Ax
    for i in range(m):
        cnt[i & 1][tr(cur, P)] += 1
        cur = mul(cur, ALPHA, P)
    return cnt


cA = per_class(A)
for eta0, eta2 in nz[:3]:
    # twist = 1 + 13^2*eta0 + 13^4*eta2 (eta1 = 0), mod P
    tw = ((1 + p ** 2 * eta0[0] + p ** 4 * eta2[0]) % P,
          (p ** 2 * eta0[1] + p ** 4 * eta2[1]) % P)
    Ap = mul(A, tw, P)
    cAp = per_class(Ap)
    print(f"  twist eta0={eta0} eta2={eta2}: per-class match = "
          f"{all(cA[r] == cAp[r] for r in (0, 1))} (Q5-as-stated says eta2 must be 0)")
# control: eta0 = 0, eta2 with Tr(C3*eta2) != 0 -> vertex eq violated -> mismatch expected
o3 = [o for o in hi if o[2] == 3][0]
eta2c = None
for x in range(p):
    for y in range(p):
        if tr13(o3[6], (x, y)) != 0:
            eta2c = (x, y)
            break
    if eta2c:
        break
twc = ((1 + p ** 4 * eta2c[0]) % P, (p ** 4 * eta2c[1]) % P)
cApc = per_class(mul(A, twc, P))
print(f"  control eta2={eta2c} (violates tier-3 vertex eq): per-class match = "
      f"{all(cA[r] == cApc[r] for r in (0, 1))} (expect False)")
print("DONE")
