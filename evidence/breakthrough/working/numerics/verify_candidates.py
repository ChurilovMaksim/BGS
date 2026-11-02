"""Independent exact checks for M09 C1/C2, M03 Ramanujan, M08 counterexample.
No Lean, no repo writes. Pure Python integers, except Ramanujan direct sum (float, tol 1e-9).
"""
from math import gcd
import cmath

def pell_uv(m):
    u, v = 1, 0  # (1+sqrt2)^0
    for _ in range(m):
        u, v = u + 2*v, u + v
    return u, v

def pell_xy(m):
    x, y = 1, 0
    for _ in range(m):
        x, y = 3*x + 8*y, x + 3*y
    return x, y

def D_gp(m):
    x, _ = pell_xy(m)
    D = 2*(x-1)
    u, v = pell_uv(m)
    gp = 2*u if m % 2 == 1 else 4*v
    return D, gp

# C1
print("C1 Pell/gp/D:")
for m in range(1, 21):
    D, gp = D_gp(m)
    ok = (D == gp*gp) if m % 2 == 1 else (2*D == gp*gp)
    print(f"  m={m} D={D} gp={gp} {'OK' if ok else 'FAIL'}")
    assert ok

# C2 window counts differ <= 1
print("C2 window counts (X up to 500):")
for m in range(3, 7):
    D, gp = D_gp(m)
    worst = 0
    for X in range(1, 501):
        counts = {}
        for N in range(X+1, 2*X+1):
            if gcd(N, D) == 1:
                nu = pow(N, -1, gp)
                counts[nu] = counts.get(nu, 0) + 1
        # units only; counts should cover all units present? check spread
        vals = list(counts.values())
        if vals:
            worst = max(worst, max(vals) - min(vals))
    print(f"  m={m} D={D} gp={gp} max_spread={worst}")
    assert worst <= 1

# Ramanujan: c_q(a) = sum_{u in (Z/q)^x} exp(2pi i a u / q) == mu(q/d)*phi(q)/phi(q/d), d=gcd(a,q)
def phi(n):
    r = n
    p = 2
    nn = n
    while p*p <= nn:
        if nn % p == 0:
            while nn % p == 0: nn //= p
            r -= r//p
        p += 1 if p == 2 else 2
    if nn > 1: r -= r//nn
    return r
def mu(n):
    if n == 1: return 1
    p = 2; nn = n; cnt = 0
    while p*p <= nn:
        if nn % p == 0:
            cnt += 1; nn //= p
            if nn % p == 0: return 0
        p += 1 if p == 2 else 2
    if nn > 1: cnt += 1
    return -1 if cnt % 2 else 1

print("Ramanujan direct vs formula:")
for q in (14, 82):
    for a in range(q):
        direct = sum(cmath.exp(2j*cmath.pi*a*u/q) for u in range(q) if gcd(u, q) == 1)
        d = gcd(a, q)
        formula = mu(q//d)*phi(q)//phi(q//d) if q//d else 0
        assert abs(direct - formula) < 1e-9, (q, a, direct, formula)
    print(f"  q={q} OK, resonance check: c_14(7)={sum(cmath.exp(2j*cmath.pi*7*u/14) for u in range(14) if gcd(u,14)==1):.3f}")

# M08 counterexample kernel check
print("M08 m=8 counterexample:")
D, gp = D_gp(8)
y = (0,1276224,998784,721344,665856,610368,332928,55488)
yp = (0,721344,332928,1276224,665856,55488,998784,610368)
def Hy(v):
    return tuple((6*v[i]-v[(i-1)%8]-v[(i+1)%8]) % D for i in range(8))
assert Hy(y) == (0,)*8 and Hy(yp) == (0,)*8
assert sorted(y) == sorted(yp)
assert all(yp[i] == y[(3*i) % 8] for i in range(8))
print(f"  D={D} kernel OK, sorted equal, p=3j mod 8 maps y to y'")
print("ALL CHECKS PASS")
