"""Exact Fourier certificate for rationally split affine antiunitary exclusion.

The uniform-N and normalizer arguments are mathematical proofs in the
accompanying manuscript. This script checks the finite coefficient algebra
and solves every possible coefficient collision as an exact linear equation.
"""
from fractions import Fraction as F
import json


ZERO = (F(0), F(0))


def addc(a, b):
    return a[0] + b[0], a[1] + b[1]


def scalec(a, s):
    return a[0] * s, a[1] * s


def conj(a):
    return a[0], -a[1]


def add(*polys):
    out = {}
    for poly in polys:
        for v, z in poly.items():
            out[v] = addc(out.get(v, ZERO), z)
    return {v: z for v, z in out.items() if z != ZERO}


def scale(poly, s):
    return {v: scalec(z, s) for v, z in poly.items()}


def mulc(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def product(a, b):
    out = {}
    for (k, l), ca in a.items():
        for (u, v), cb in b.items():
            w = k + u, l + v
            out[w] = addc(out.get(w, ZERO), mulc(ca, cb))
    return {v: z for v, z in out.items() if z != ZERO}


one = {(0, 0): (F(1), F(0))}
cos1 = {(1, 0): (F(1, 2), F(0)), (-1, 0): (F(1, 2), F(0))}
cos7 = {(7, 0): (F(1, 2), F(0)), (-7, 0): (F(1, 2), F(0))}
sin1 = {(1, 0): (F(0), F(-1, 2)), (-1, 0): (F(0), F(1, 2))}
cos_p_alpha = {(0, 1): (F(-3, 10), F(-2, 5)),
               (0, -1): (F(-3, 10), F(2, 5))}
r = product(add(one, scale(cos7, -1)), add(one, cos1))

# Original modular-Weyl symbol. There is no real-half sign conversion here.
a = add(cos7, scale(r, F(1, 10)),
        scale(product(r, sin1), F(1, 100)),
        scale(product(r, cos_p_alpha), F(1, 100)),
        scale(one, F(-1, 10)))
assert len(a) == 32
assert (0, 0) not in a
for v, z in a.items():
    assert a[(-v[0], -v[1])] == conj(z)


def S(v):
    k, l = v
    return 3 * k + 2 * l, 4 * k + 3 * l


b = {S(v): z for v, z in a.items()}
support = set(a) | set(b)
assert set(a) & set(b) == {(-1, -1), (1, 1)}
assert len(support) == 62
assert max(abs(v[0]) for v in support) == 27
assert max(abs(v[1]) for v in support) == 36

u = (F(1, 20), F(-1, 200))
gamma = (F(-3, 1000), F(-4, 1000))
assert a[(1, 0)] == u
assert a[(0, 1)] == gamma
assert b.get((1, 0), ZERO) == b.get((0, 1), ZERO) == ZERO


def target_collisions(target):
    """Solve b_v+c(a_v-b_v)=c*conjugate(target), exactly for 0<c<1."""
    all_c = []
    isolated = {}
    ct = conj(target)
    for v in sorted(support):
        alpha = b.get(v, ZERO)
        beta = addc(addc(a.get(v, ZERO), scalec(alpha, -1)), scalec(ct, -1))
        if beta == ZERO:
            if alpha == ZERO:
                all_c.append(v)
            continue
        component = 0 if beta[0] else 1
        c = -alpha[component] / beta[component]
        if F(0) < c < F(1) and addc(alpha, scalec(beta, c)) == ZERO:
            isolated[v] = c
    return all_c, isolated


u_all, u_special = target_collisions(u)
g_all, g_special = target_collisions(gamma)
assert u_all == [(-1, 0)]
assert u_special == {(-3, -4): F(1, 2)}
assert g_all == [(0, -1)]
assert g_special == {(-5, -7): F(1, 3), (-2, -3): F(1, 2)}

half = add(scale(a, F(1, 2)), scale(b, F(1, 2)))
assert half[(1, 1)] == half[(-1, -1)] == (F(-3, 2000), F(0))


def det(v, w):
    return v[0] * w[1] - v[1] * w[0]


half_determinants = sorted({
    det(v, w)
    for v in [(-1, 0), (-3, -4)]
    for w in [(0, -1), (-2, -3)]
})
third_determinants = sorted({
    det((-1, 0), w) for w in [(0, -1), (-5, -7)]
})
assert half_determinants == [1, 3]
assert third_determinants == [1, 7]

result = {
    "original_frequency_count": len(a),
    "combined_frequency_count": len(support),
    "combined_support_max_abs": [27, 36],
    "overlap": sorted(set(a) & set(b)),
    "u_target_always": u_all,
    "u_target_exceptional": {str(v): str(c) for v, c in u_special.items()},
    "gamma_target_always": g_all,
    "gamma_target_exceptional": {str(v): str(c) for v, c in g_special.items()},
    "determinants_at_c_half": half_determinants,
    "determinants_at_c_third": third_determinants,
    "status": "All exact Fraction coefficient identities and collision equations passed.",
}
print(json.dumps(result, indent=2))
