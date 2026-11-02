import math, sys
from sympy import factorint
def beta_pow(m):
    u, v = 1, 0
    for _ in range(m):
        u, v = 3*u + 4*v, 2*u + 3*v
    return u, v
def Dm(m):
    u, _ = beta_pow(m)
    return abs(2 - 2*u)
def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c
for m in (72, 108, 144):
    d = Dm(m)
    v2 = vp(d, 2)
    rest = d // (2**v2)
    s = math.isqrt(rest)
    assert s*s == rest, f"D_{m}: non-square odd part!"
    fac = factorint(s)
    full = {2: v2}
    for p, e in fac.items():
        full[p] = 2*e
    print(f"D_{m} = " + " * ".join(f"{p}^{e}" for p, e in sorted(full.items())), flush=True)
    # sanity: product check
    pr = 1
    for p, e in full.items(): pr *= p**e
    assert pr == d
    print(f"  product check OK; odd primes: {sorted(p for p in full if p != 2)}", flush=True)
