"""Exact local probe of the first confluent coefficient, N=49, at 1+2i.

This is a finite diagnostic, not an asymptotic spectral theorem.
All arithmetic is in F_5[x]/Phi_49(x), an actual field because
ord_49(5)=42. No external library or floating point is used.
"""

from functools import lru_cache
import json

P = 5
DEG = 42
WIDTH = 16
MASK = (1 << WIDTH) - 1


def norm(a):
    a = [v % P for v in a]
    while a and a[-1] == 0:
        a.pop()
    return tuple(a)


ZERO = ()
ONE = (1,)


def add(a, b):
    return norm([
        (a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
        for i in range(max(len(a), len(b)))
    ])


def neg(a):
    return norm([-x for x in a])


def sub(a, b):
    return add(a, neg(b))


def scale(a, n):
    return norm([n * x for x in a])


def mul(a, b):
    if not a or not b:
        return ZERO
    # Every convolution coefficient is <= 42*4*4 < 2**16.
    x = sum(v << (WIDTH * i) for i, v in enumerate(a))
    y = sum(v << (WIDTH * i) for i, v in enumerate(b))
    z = x * y
    c = [
        ((z >> (WIDTH * i)) & MASK) % P
        for i in range(len(a) + len(b) - 1)
    ]
    # Phi_49 = 1 + x^7 + x^14 + ... + x^42.
    for j in range(len(c) - 1, DEG - 1, -1):
        q = c[j] % P
        if q:
            c[j] = 0
            for r in range(6):
                c[j - DEG + 7 * r] = (c[j - DEG + 7 * r] - q) % P
    return norm(c[:DEG])


def power(a, n):
    z = ONE
    while n:
        if n & 1:
            z = mul(z, a)
        a = mul(a, a)
        n //= 2
    return z


@lru_cache(None)
def inv(a):
    if not a:
        raise ZeroDivisionError
    result = power(a, P**DEG - 2)
    assert mul(a, result) == ONE
    return result


def poly_norm(a):
    a = list(a)
    while a and not a[-1]:
        a.pop()
    return a


def poly_add(a, b):
    return poly_norm([
        add(a[i] if i < len(a) else ZERO, b[i] if i < len(b) else ZERO)
        for i in range(max(len(a), len(b)))
    ])


def poly_scale(a, c):
    return poly_norm([mul(x, c) for x in a])


def poly_sub(a, b):
    return poly_add(a, [neg(x) for x in b])


def poly_mul(a, b):
    if not a or not b:
        return []
    c = [ZERO] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i + j] = add(c[i + j], mul(x, y))
    return poly_norm(c)


def remainder(a, b):
    a = poly_norm(a)
    b = poly_norm(b)
    q = inv(b[-1])
    while len(a) >= len(b):
        d = len(a) - len(b)
        c = mul(a[-1], q)
        for j, x in enumerate(b):
            a[d + j] = sub(a[d + j], mul(c, x))
        a = poly_norm(a)
    return a


def gcd(a, b):
    while b:
        a, b = b, remainder(a, b)
    return poly_scale(a, inv(a[-1]))


def linear_composition(poly, u, v):
    """Return poly(u*x+v)."""
    result = []
    for coefficient in reversed(poly):
        result = poly_add(poly_mul(result, [v, u]), [coefficient])
    return result


def main():
    residue = 1
    order = None
    for k in range(1, 43):
        residue = residue * P % 49
        if residue == 1:
            order = k
            break
    assert order == DEG
    root = (0, 1)
    assert power(root, 49) == ONE and power(root, 7) != ONE
    roots = [power(root, k) for k in range(49)]

    def cos(k):
        return scale(add(roots[k % 49], roots[-k % 49]), 3)

    def r(k):
        return mul(sub(ONE, cos(7 * k)), add(ONE, cos(k)))

    def diagonal(x):
        # 200 V = 2 r sin mod 5, and i=2 at 1+2i, so 2/(2i)=3.
        return scale(mul(r(x), sub(roots[x % 49], roots[-x % 49])), 3)

    polys = []
    endpoints = []
    squarefree = []
    for s in range(7):
        start = 25 + 7 * s
        end = start + 6
        previous = [ONE]
        current = []
        for j in range(7):
            x = (start + j) % 49
            d = diagonal(x)
            if j == 0:
                current = [neg(d), ONE]
            else:
                b = r(x - 1 + 25)
                following = poly_sub(
                    poly_add([ZERO] + current, poly_scale(current, neg(d))),
                    poly_scale(previous, mul(b, b)),
                )
                previous, current = current, following
        polys.append(current)
        endpoints.append({
            "d_start": diagonal(start),
            "d_end": diagonal(end),
            "b_start": r(start + 25),
            "b_end": r(end - 1 + 25),
        })
        derivative = [scale(current[k], k) for k in range(1, len(current))]
        squarefree.append(len(gcd(current, derivative)) - 1)

    shared = []
    for s in range(7):
        for t in range(s + 1, 7):
            d = len(gcd(polys[s], polys[t])) - 1
            if d:
                shared.append([s, t, d])
    assert squarefree == [0] * 7
    assert not shared

    eta_a = roots[35]
    eta_b = roots[7]
    z = [roots[(7 * 2 * s) % 49] for s in range(7)]
    coefficient_failures = []
    linear_coefficients = []
    for s in range(7):
        for t in range(s + 1, 7):
            es, et = endpoints[s], endpoints[t]
            denominator = mul(z[s], z[t])
            a_s = mul(eta_a, mul(power(z[s], 3), inv(denominator)))
            a_t = mul(eta_a, mul(power(z[t], 3), inv(denominator)))
            b_s = mul(eta_b, inv(power(z[s], 3)))
            b_t = mul(eta_b, inv(power(z[t], 3)))
            # F/(z_s-z_t) = a*mu_s + b*mu_t + c.
            a = sub(mul(b_s, inv(es["b_start"])), mul(a_s, inv(es["b_end"])))
            b = sub(mul(a_t, inv(et["b_end"])), mul(b_t, inv(et["b_start"])))
            c = add(
                sub(
                    mul(a_s, mul(es["d_end"], inv(es["b_end"]))),
                    mul(b_s, mul(es["d_start"], inv(es["b_start"]))),
                ),
                sub(
                    mul(b_t, mul(et["d_start"], inv(et["b_start"]))),
                    mul(a_t, mul(et["d_end"], inv(et["b_end"]))),
                ),
            )
            if t == 6 - s:
                assert a == b and a and not c
                assert linear_composition(polys[t], neg(ONE), ZERO) == poly_scale(polys[s], neg(ONE))
            if b:
                u = neg(mul(a, inv(b)))
                v = neg(mul(c, inv(b)))
                composed = linear_composition(polys[t], u, v)
                common = gcd(polys[s], composed)
                degree = len(common) - 1
            elif a:
                common = gcd(polys[s], [c, a])
                degree = (len(common) - 1) * 7
            else:
                degree = 49 if not c else 0
                common = []
            linear_coefficients.append({"s": s, "t": t, "degree": degree})
            if degree:
                coefficient_failures.append({
                    "s": s, "t": t, "degree": degree,
                    "gcd_coefficients": common,
                    "a": a, "b": b, "c": c,
                })

    report = {
        "N": 49,
        "prime": 5,
        "root_order": 49,
        "field_degree": DEG,
        "i_reduction": 2,
        "squarefree_gcd_degrees": squarefree,
        "shared_chain_factors": shared,
        "first_confluent_pair_gcd_degrees": linear_coefficients,
        "first_confluent_coefficient_failures": coefficient_failures,
    }
    print(json.dumps(report, separators=(",", ":")))


if __name__ == "__main__":
    main()
