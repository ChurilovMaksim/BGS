"""Exact finite Fourier checks for the fourth-difference comb argument.

These calculations audit coefficients and constants; the asymptotic operator
estimate is proved in the accompanying manuscript, not inferred from this code.
"""
from fractions import Fraction as F
import json


def addc(a, b):
    return a[0] + b[0], a[1] + b[1]


def mulc(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def add(*polys):
    out = {}
    for poly in polys:
        for key, value in poly.items():
            out[key] = addc(out.get(key, (F(0), F(0))), value)
    return {key: value for key, value in out.items() if value != (0, 0)}


def scale(poly, value):
    value = F(value), F(0)
    return {key: mulc(coef, value) for key, coef in poly.items()}


def product(a, b):
    out = {}
    for (k, l), ca in a.items():
        for (u, v), cb in b.items():
            key = k + u, l + v
            out[key] = addc(out.get(key, (F(0), F(0))), mulc(ca, cb))
    return {key: value for key, value in out.items() if value != (0, 0)}


def cosine_q(k):
    return {(k, 0): (F(1, 2), F(0)), (-k, 0): (F(1, 2), F(0))}


one = {(0, 0): (F(1), F(0))}
c1, c7 = cosine_q(1), cosine_q(7)
s1 = {(1, 0): (F(0), F(-1, 2)), (-1, 0): (F(0), F(1, 2))}
r = product(add(one, scale(c7, -1)), add(one, c1))
rshift = product(add(one, c7), add(one, scale(c1, -1)))
cos_p_alpha = {(0, 1): (F(-3, 10), F(-2, 5)),
               (0, -1): (F(-3, 10), F(2, 5))}
a = add(c7, scale(r, F(1, 10)), scale(product(r, s1), F(1, 100)),
        scale(one, F(-1, 10)), scale(product(rshift, cos_p_alpha), F(1, 100)))

assert max(abs(k) + abs(l) for k, l in a) == 9
assert a[(7, 0)] == a[(-7, 0)] == (F(9, 20), F(0))
for (k, l), (re, im) in a.items():
    assert a[(-k, -l)] == (re, -im)

sigma_scaled = sum(F(k**8) * (re * re + im * im)
                   for (k, l), (re, im) in a.items())
lower_scaled = F(81, 200) * 7**8
assert sigma_scaled >= lower_scaled
series_remainder_coefficient = 120 * 60**3 * 8 * 7000
assert series_remainder_coefficient < 2 * 10**12
exponential_remainder_coefficient = F((240 * 60**3)**2, 2)
assert exponential_remainder_coefficient + 10**12 < 10**16

result = {
    "frequency_count": len(a),
    "maximum_frequency_l1": 9,
    "a_plus7_0": [str(x) for x in a[(7, 0)]],
    "sigma_squared_divided_by_(2pi)^8": str(sigma_scaled),
    "lower_bound_divided_by_(2pi)^8": str(lower_scaled),
    "cubic_generator_remainder_coefficient": series_remainder_coefficient,
    "exponential_remainder_coefficient": str(exponential_remainder_coefficient),
    "status": "All exact coefficient and numerical-margin assertions passed.",
}
print(json.dumps(result, ensure_ascii=False, indent=2))
