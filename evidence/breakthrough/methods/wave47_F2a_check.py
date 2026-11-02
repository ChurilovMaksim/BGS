"""Wave 47, task 5: F2a checks.
(1) gcd(delta, D_{3t}) is a 3-power, delta = 2*A_{3t}+1, alpha^{3t}=A+B sqrt2.
(2) Kernel equality ker(M^m - I) == ker(M^{3t} - I) mod q0 for q0 | D_{3t},
    3 not | q0; failure at q0 = 81 (3-part) at m = 252.
Kernel of a 2x2 matrix mod q: brute seed solve on (y0, y1).
"""
import math


def alpha_pow(n):
    """Return (A, B) with alpha^n = A + B sqrt2, exact ints."""
    # alpha^n via binary powering in Z[sqrt2]
    def mul(p, r):
        a, b = p
        c, d = r
        return (a * c + 2 * b * d, a * d + b * c)
    res = (1, 0)
    base = (3, 2)
    while n:
        if n & 1:
            res = mul(res, base)
        base = mul(base, base)
        n >>= 1
    return res


def mat_pow_mod(Mm, e, q):
    def mul(X, Y):
        return [(X[0] * Y[0] + X[1] * Y[2]) % q, (X[0] * Y[1] + X[1] * Y[3]) % q,
                (X[2] * Y[0] + X[3] * Y[2]) % q, (X[2] * Y[1] + X[3] * Y[3]) % q]
    R = [1, 0, 0, 1]
    B = Mm[:]
    while e:
        if e & 1:
            R = mul(R, B)
        B = mul(B, B)
        e >>= 1
    return R


def ker_seeds(Mm, e, q):
    """All (y0, y1) mod q with (Mm^e - I)(y0, y1) = 0."""
    P = mat_pow_mod(Mm, e, q)
    a = (P[0] - 1) % q
    b = P[1] % q
    c = P[2] % q
    d = (P[3] - 1) % q
    out = set()
    for y0 in range(q):
        # a*y1 = -b*y0 (mod q); solve by brute over gcd structure
        g = math.gcd(a, q)
        if (-b * y0) % g != 0:
            continue
        # find one solution via extended gcd on reduced equation
        a1, q1 = a // g, q // g
        rhs = ((-(b * y0)) // g) % q1
        if q1 == 1:
            y1s = range(q)
        else:
            inv = pow(a1, -1, q1)
            y1_0 = (inv * rhs) % q1
            step = q // g
            y1s = range(y1_0, q, step)
        for y1 in y1s:
            if (c * y1 + d * y0) % q == 0:
                out.add((y0, y1))
    return out


Mm = [6, -1, 1, 0]  # entries mod q handled inside (use q-1 for -1)
Mm = [6, 10 ** 18, 1, 0]  # placeholder, replaced per q below


def ker_seeds_q(e, q):
    Mq = [6 % q, (-1) % q, 1 % q, 0]
    return ker_seeds(Mq, e, q)


print("=== (1) gcd(delta, D_{3t}) ===")
for t in [4, 8, 12, 16, 20, 28, 40]:
    if t % 3 == 0:
        continue
    A, B = alpha_pow(3 * t)
    D = 2 * (A - 1)
    delta = 2 * A + 1
    g = math.gcd(delta, D)
    # strip factors of 3
    h = g
    while h % 3 == 0:
        h //= 3
    print(f"t={t}: gcd={g} 3-free part={h} (1 => pure 3-power)")

print("=== (2) kernel equality at m=252, 3t=84 ===")
for q0 in [25, 121, 81, 2401]:
    k252 = ker_seeds_q(252, q0)
    k84 = ker_seeds_q(84, q0)
    print(f"q0={q0}: |ker252|={len(k252)} |ker84|={len(k84)} equal={k252 == k84}")
