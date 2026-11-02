"""Wave 28, task 5: complete check of Hypothesis H without factoring D_m.

H: every twin qt || D_m satisfies qt <= D_m / m^2 (for large m).
Cofactor reformulation: write D_m = 2^a * S_m^2 (S_m odd, a = v2(D_m)).
A prime power qt = p^{2f} || D_m has p^f || S_m; write c = S_m / p^f.
Then qt > D_m/m^2  <=>  2^a * c^2 < m^2.  So a violation is exactly a
prime-power divisor p^f of S_m with small cofactor c (and p not | c,
automatic from gcd(d,c)=1) that is TWIN (3 not | ord_{p^{2f}}(beta)).
Hence H at m is decidable by trial-dividing S_m by c < m/2^{a/2} only:
no factorisation of the huge S_m is needed.

Twin test: |G| = p^{2f-1} * (p - eps), eps = (2/p) = +/-1, is the order
of the norm-1 group in (Z/qt)[sqrt 2].  Let G3 = |G| with all factors
of 3 removed.  Then 3 | ord(beta)  <=>  beta^G3 != 1 mod qt.
(If 3 not | |G| this is automatic: beta^|G| = 1.)
"""
import sys
from math import isqrt, gcd

from sympy import isprime, perfect_power, integer_nthroot

# Pell pair: x_n + y_n*sqrt(2) = (3+2*sqrt(2))^n
xs = [1, 3]
ys = [0, 2]
NMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
for n in range(2, NMAX + 1):
    xs.append(6 * xs[-1] - xs[-2])
    ys.append(6 * ys[-1] - ys[-2])


def prime_power(d):
    """Return (p, f) if d = p^f with p prime, else None. d > 1."""
    if isprime(d):
        return (d, 1)
    pp = perfect_power(d)
    if pp is False:
        return None
    base, exp = pp
    if isprime(base):
        return (base, exp)
    return None


def ring_mul(u, v, qt):
    a, b = u
    c, d = v
    return ((a * c + 2 * b * d) % qt, (a * d + b * c) % qt)


def ring_pow(u, e, qt):
    r = (1, 0)
    while e:
        if e & 1:
            r = ring_mul(r, u, qt)
        u = ring_mul(u, u, qt)
        e >>= 1
    return r


def is_twin(p, f):
    """3 not | ord_{p^{2f}}(beta)?  beta = 17 + 12*sqrt(2)."""
    qt = p ** (2 * f)
    eps = 1 if pow(2, (p - 1) // 2, p) == 1 else -1
    G = p ** (2 * f - 1) * (p - eps)
    G3 = G
    while G3 % 3 == 0:
        G3 //= 3
    return ring_pow((17, 12), G3, qt) == (1, 0)


violations = []
near_misses = []  # prime-power divisors with cofactor < m (any twin status)
for m in range(1, NMAX + 1):
    Dm = 2 * (xs[m] - 1)
    a = (Dm & -Dm).bit_length() - 1  # v2, Dm > 0
    odd = Dm >> a
    S = isqrt(odd)
    assert S * S == odd, (m, "odd part not a square")
    # sanity: LTE for a
    if m % 2 == 1:
        assert a == 2, (m, a)
    else:
        v2m = (m & -m).bit_length() - 1
        assert a == 2 * v2m + 3, (m, a, v2m)
    c = 1
    while (1 << a) * c * c < m * m:  # violating-cofactor range
        if S % c == 0:
            d = S // c
            if d > 1 and gcd(d, c) == 1:
                pp = prime_power(d)
                if pp is not None:
                    p, f = pp
                    qt = p ** (2 * f)
                    tw = is_twin(p, f)
                    near_misses.append((m, c, p, f, qt, tw))
                    if tw:
                        violations.append((m, c, p, f, qt, Dm))
        c += 1
    if m % 100 == 0:
        print(f"... m={m} done, violations so far: {len(violations)}",
              flush=True)

print("VIOLATIONS (m, cofactor c, p, f, qt, D_m):")
for v in violations:
    m, c, p, f, qt, Dm = v
    print(f"  m={m} c={c} p={p} f={f} qt={qt} qt/D_m={qt/Dm:.6g}")
print(f"total violations: {len(violations)}")
print("NEAR MISSES (prime-power divisor, cofactor < m/2^(a/2), twin or not):")
for nm in near_misses:
    print(f"  m={nm[0]} c={nm[1]} p={nm[2]} f={nm[3]} qt={nm[4]} twin={nm[5]}")
