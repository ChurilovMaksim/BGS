"""Independent rational construction; no floating transcendence test."""
from fractions import Fraction as F


def add(*polys):
    out = {}
    for poly in polys:
        for v, (a, b) in poly.items():
            x, y = out.get(v, (F(0), F(0)))
            out[v] = x+a, y+b
    return {v: z for v, z in out.items() if z != (0, 0)}


def scale(poly, c):
    return {v: (c*a, c*b) for v, (a, b) in poly.items()}


def multiply(left, right):
    out = {}
    for (a, b), (x, y) in left.items():
        for (c, d), (u, v) in right.items():
            z = a+c, b+d
            re, im = out.get(z, (F(0), F(0)))
            out[z] = re+x*u-y*v, im+x*v+y*u
    return {v: z for v, z in out.items() if z != (0, 0)}


def frozen_coefficients():
    one = {(0, 0): (F(1), F(0))}
    cosine = lambda n: {(n, 0): (F(1, 2), F(0)),
                        (-n, 0): (F(1, 2), F(0))}
    sinq = {(1, 0): (F(0), F(-1, 2)), (-1, 0): (F(0), F(1, 2))}
    cosp = {(0, 1): (F(-3, 10), F(-2, 5)),
            (0, -1): (F(-3, 10), F(2, 5))}
    r = multiply(add(one, scale(cosine(7), -1)), add(one, cosine(1)))
    f = add(cosine(7), scale(r, F(1, 10)),
            scale(multiply(r, sinq), F(1, 100)),
            scale(multiply(r, cosp), F(1, 100)))
    # Position convention e(kq+lp) -> T(l,k).
    return {(l, k): z for (k, l), z in f.items()}


def gauge_coefficients(ordinary=False):
    return {v: tuple((-1 if ordinary and v[0]*v[1] % 2 else 1)*x for x in z)
            for v, z in frozen_coefficients().items()}


def act(v, n):
    a, b = v
    return (3*a+4*b) % n, (2*a+3*b) % n


def orbit(v, n):
    start = v[0] % n, v[1] % n
    result = []
    current = start
    while not result or current != start:
        result.append(current)
        current = act(current, n)
        assert len(result) <= n*n
    return result


def period(n):
    left, right = (1, 0), (0, 1)
    for r in range(1, n**3+1):
        left, right = act(left, n), act(right, n)
        if (left, right) == ((1, 0), (0, 1)):
            return r
    raise AssertionError('finite group period bound failed')


def average_coefficients(n, ordinary=False):
    r = period(n)
    out = {}
    for label, value in gauge_coefficients(ordinary).items():
        v = label[0] % n, label[1] % n
        for _ in range(r):
            re, im = out.get(v, (F(0), F(0)))
            out[v] = re+value[0]/r, im+value[1]/r
            v = act(v, n)
    return r, {v: z for v, z in out.items() if z != (0, 0)}


def check_coefficients():
    from pathlib import Path
    import importlib.util
    # Compare with the older, differently assembled frozen-symbol input.
    prior = Path(__file__).resolve().parents[1]/'design-return/frozen_sharp_return.py'
    import sys
    sys.path.insert(0, str(prior.parent))
    spec = importlib.util.spec_from_file_location('prior_frozen_coefficients', prior)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    den, old = module.coefficients()
    current = frozen_coefficients()
    assert current.pop((0, 0)) == (F(1, 10), F(0))
    assert current == {v: (F(a, den), F(b, den)) for v, (a, b) in old.items()}
    rows = []
    for ordinary in (False, True):
        coeff = gauge_coefficients(ordinary)
        assert coeff[(0, 7)] == coeff[(0, -7)] == (F(9, 20), F(0))
        neg = sum(max(-z[0], F(0)) for v, z in coeff.items()
                  if v not in ((0, 0), (0, 7), (0, -7)))
        assert neg == F(14, 125)
        for n in (3, 5, 7, 9, 15, 21, 25, 35, 41, 49, 63, 105, 239, 1393):
            r, bar = average_coefficients(n, ordinary)
            if n == 7 and not ordinary:
                assert bar == {(0, 0): (F(1), F(0))}
                reduced = {}
                for (a, b), (x, y) in coeff.items():
                    key = a % n, b % n
                    u, v = reduced.get(key, (F(0), F(0)))
                    reduced[key] = u+x, v+y
                assert {v: z for v, z in reduced.items() if z != (0, 0)} == bar
                assert r == 3
            if n != 7:
                labels = set(orbit((0, 7), n))
                witness = sum(z[0] for (a, b), z in coeff.items()
                              if (a % n, b % n) in labels)
                assert witness >= F(169, 500)
                assert sum(bar.get(v, (F(0), F(0)))[0] for v in labels) == witness
            else:
                witness = None
            rows.append({'N': n, 'ordinary_midpoint': ordinary, 'period': r,
                         'dominant_orbit_witness': str(witness),
                         'average_nonscalar': any(v != (0, 0) for v in bar)})
    return {'independent_frozen_coefficients_match': True,
            'negative_real_mass_both_gauges': '14/125',
            'uniform_witness_margin': '169/500', 'rows': rows}
