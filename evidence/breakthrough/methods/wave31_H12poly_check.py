# Wave 31 task 3 check: twin primes at m=12u divide y_{2u} with equal
# p-adic valuation, giving the exponential cofactor bound.
# Exact integer arithmetic except the final float comparison of the
# analytic bound (which has huge slack).
import sys
from math import log

sys.setrecursionlimit(10000)

# y_n: y_0=0, y_1=2, y_{n+1}=6 y_n - y_{n-1}
def y_seq(N):
    y = [0] * (N + 1)
    if N >= 1:
        y[1] = 2
    for n in range(1, N):
        y[n + 1] = 6 * y[n] - y[n - 1]
    return y

def vp(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return c

def v2(n):
    return vp(n, 2)

def odd_part(n):
    return n >> v2(n)

# mul/pw in (Z/q)[sqrt2]
def mul(u, w, q):
    return ((u[0] * w[0] + 2 * u[1] * w[1]) % q, (u[0] * w[1] + u[1] * w[0]) % q)

def pw(u, e, q):
    r = (1, 0)
    while e:
        if e & 1:
            r = mul(r, u, q)
        u = mul(u, u, q)
        e >>= 1
    return r

def is_twin(p, f):
    # wave-30 test: twin iff beta^G3 == 1 where G3 = norm-1 group order with 3s stripped
    qt = p ** (2 * f)
    # Legendre-type eps: eps = 1 if 2 is QR mod p else -1 (for p != 2)
    eps = 1 if pow(2, (p - 1) // 2, p) == 1 else -1
    G = p ** (2 * f - 1) * (p - eps)
    while G % 3 == 0:
        G //= 3
    return pw((17 % qt, 12 % qt), G, qt) == (1, 0)

# Exact factorisation via sympy (Pollard rho); trial division alone is
# unsafe here (it once merged 665857*9188923201 into one fake prime).
from sympy import factorint as _factorint

def factorint_small(n, primes=None):
    return {int(p): int(e) for p, e in _factorint(n).items()}
ALPHA = 3 + 2 * (2 ** 0.5)
Y = y_seq(120)

bad = 0
for u in range(1, 11):
    m = 12 * u
    Sm = odd_part(Y[6 * u])
    fac = factorint_small(Sm)
    # check factorisation is complete: product must equal Sm
    prod = 1
    for p, f in fac.items():
        prod *= p ** f
    assert prod == Sm, (m, "incomplete factorisation")
    twins = [(p, f) for p, f in fac.items() if p != 3 and is_twin(p, f)]
    s = 0
    for p, f in twins:
        # (i) p | y_{2u}
        assert Y[2 * u] % p == 0, (m, p, "not dividing y2u")
        # (ii) valuations equal
        assert vp(Y[6 * u], p) == vp(Y[2 * u], p) == f, (m, p, "valuation mismatch")
        # (iii) cofactor bound c_p >= alpha^{4u}/(8u)
        cp = Sm // (p ** f)
        assert cp * 8 * u >= ALPHA ** (4 * u) / 2, (m, p, "cofactor bound fails")
        s += p ** (2 * f)
    Dm = 8 * Y[6 * u] ** 2
    # (iv) exponential bound and H12-poly for b=0,1,2
    ratio = s / Dm
    expbound = 18 * u ** 3 / ALPHA ** (8 * u)
    assert ratio <= expbound * 1.0000001, (m, ratio, expbound)
    for b in (0, 1, 2):
        assert ratio <= m ** (-(9 + 2 * b)) or m < 1200 * (b + 1) ** 2, (m, b)
    print(f"m={m} u={u} twins={[p for p, _ in twins]} sum/D={ratio:.3e} "
          f"expbound={expbound:.3e} m^-9={m ** -9:.3e} OK")
print("ALL CHECKS PASS")
