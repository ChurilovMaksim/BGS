"""Exact rational checks for the fourth-commutator gauge discriminator.

This verifies finite algebra only. The uniform remainder and asymptotic
scope are proved in audit_quantitative_gauge_reversal_obstruction.md.
"""

from fractions import Fraction as F


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1],
            z[0] * w[1] + z[1] * w[0])


def scale(z, x):
    return (z[0] * x, z[1] * x)


def put(poly, key, value):
    z = add(poly.get(key, (F(0), F(0))), value)
    if z == (0, 0):
        poly.pop(key, None)
    else:
        poly[key] = z


def product(a, b):
    c = {}
    for (k, l), z in a.items():
        for (r, s), w in b.items():
            put(c, (k + r, l + s), mul(z, w))
    return c


one = {(0, 0): (F(1), F(0))}
cos1 = {(1, 0): (F(1, 2), F(0)), (-1, 0): (F(1, 2), F(0))}
cos7 = {(7, 0): (F(1, 2), F(0)), (-7, 0): (F(1, 2), F(0))}
sin1 = {(1, 0): (F(0), F(-1, 2)), (-1, 0): (F(0), F(1, 2))}

rleft, rright = dict(one), dict(one)
for key, value in cos7.items():
    put(rleft, key, scale(value, -1))
for key, value in cos1.items():
    put(rright, key, value)
r = product(rleft, rright)

a = dict(cos7)
for key, value in r.items():
    put(a, key, scale(value, F(1, 10)))
for key, value in product(r, sin1).items():
    put(a, key, scale(value, F(1, 100)))
put(a, (0, 0), (F(-1, 10), F(0)))

gamma = (F(-3, 1000), F(-4, 1000))
gammabar = (gamma[0], -gamma[1])
R = {}
for (k, l), value in r.items():
    assert l == 0 and value[1] == 0
    R[k] = value[0] * (-1 if k % 2 else 1)
    put(a, (k, 1), scale(gamma, R[k]))
    put(a, (k, -1), scale(gammabar, R[k]))

assert len(a) == 32
assert sum(abs(x) for x in R.values()) == 4

# Remove the common (4*pi**2) factor from each classical bracket.
v = {(3, 4): (F(1), F(0))}
for order in range(5):
    target = v.get((1, 0), (F(0), F(0)))
    if order < 4:
        assert target == (0, 0)
    else:
        gb4 = mul(mul(gammabar, gammabar), mul(gammabar, gammabar))
        assert target == scale(gb4, F(245, 32))
        assert target[1] * F(4**4, 24) == F(343, 12500000000)
        print("Full-symbol fourth coefficient / (4*pi^2)^4:", target)
        print("Imaginary t^4 coefficient / pi^8:", F(343, 12500000000))
        break
    out = {}
    for (k, l), au in a.items():
        for (K, L), bv in v.items():
            omega = l * K - k * L
            put(out, (K + k, L + l), scale(mul(au, bv), -omega))
    v = out

# Independent scalar R^4 check.
rp = {0: F(1)}
for _ in range(4):
    out = {}
    for k, x in rp.items():
        for l, y in R.items():
            out[k + l] = out.get(k + l, F(0)) + x * y
    rp = out
assert rp[-2] == rp[2] == F(245, 32)
assert F(35, 8) * F(7, 4) == rp[-2]

# Conservative numerical constants are rational/integer comparisons.
assert F(32 * 35**2 * 140**4, 3) < 10**13
assert F(245, 32) - F(1, 10) > 7
assert 14208**5 < 10**21
assert F(7 * 36**4 * 336, 24 * 10**12) > F(1, 10**4)
assert F(1, 10**59) < F(1, 20000)
assert 20000 * 8**4 < 10**8
print("All exact coefficient and constant checks passed.")
