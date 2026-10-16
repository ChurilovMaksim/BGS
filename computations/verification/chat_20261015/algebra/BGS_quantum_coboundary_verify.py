"""Independent exact-rational checks for the frozen BGS cyclic cohomology theorem.

Usage: python BGS_quantum_coboundary_verify.py
Dependencies: Python standard library only. Does not modify BGS/GitHub.
"""
from collections import defaultdict
from fractions import Fraction as F
from math import isqrt
ZERO = (F(0), F(0))

def add(z, w):
    return (z[0] + w[0], z[1] + w[1])

def scale(z, t):
    return (t * z[0], t * z[1])

def even_sign(n):
    return 1 if n % 2 == 0 else -1

def coefficients_raw():
    r = {0: F(1), 1: F(1, 2), -1: F(1, 2), 7: -F(1, 2), -7: -F(1, 2), 6: -F(1, 4), -6: -F(1, 4), 8: -F(1, 4), -8: -F(1, 4)}
    c = defaultdict(lambda: ZERO)
    for k, v in r.items():
        c[k, 0] = add(c[k, 0], (v / 10, F(0)))
        for m, s in ((1, (F(0), -F(1, 2))), (-1, (F(0), F(1, 2)))):
            c[k + m, 0] = add(c[k + m, 0], scale(s, v / 100))
        for ell, phase in ((1, (-F(3, 10), -F(2, 5))), (-1, (-F(3, 10), F(2, 5)))):
            c[k, ell] = add(c[k, ell], scale(phase, even_sign(k) * v / 100))
    for k in (-7, 7):
        c[k, 0] = add(c[k, 0], (F(1, 2), F(0)))
    c[0, 0] = add(c[0, 0], (-F(1, 10), F(0)))
    c = {v: z for v, z in c.items() if z != ZERO}
    if not (len(c) == 32 and (0, 0) not in c):
        raise AssertionError('verification failed')
    return {(ell, k): scale(z, even_sign(k * ell)) for (k, ell), z in c.items()}

def S(v, p):
    return ((3 * v[0] + 4 * v[1]) % p, (2 * v[0] + 3 * v[1]) % p)

def ord_S(p):
    v, w = ((1, 0), (0, 1))
    for d in range(1, p + 3):
        v, w = (S(v, p), S(w, p))
        if v == (1, 0) and w == (0, 1):
            return d
    raise RuntimeError(f'Unexpected order at {p}')

def check(p, coefficients):
    if not (p > 99 and all((p % a for a in range(2, isqrt(p) + 1)))):
        raise AssertionError('Require prime p>99')
    d = ord_S(p)
    support = {(v[0] % p, v[1] % p): z for v, z in coefficients.items()}
    if not len(support) == 32:
        raise AssertionError('verification failed')
    orbit_index = {}
    sums = []
    for v in support:
        if v in orbit_index:
            continue
        i = len(sums)
        w = v
        for j in range(d):
            if not w not in orbit_index:
                raise AssertionError('verification failed')
            orbit_index[w] = i
            w = S(w, p)
        if not w == v:
            raise AssertionError('verification failed')
        sums.append([F(0), F(0)])
    for v, z in support.items():
        mass = sums[orbit_index[v]]
        mass[0] += z[0]
        mass[1] += z[1]
    sigma = sum((x * x + y * y for x, y in sums))
    baseline = F(81, 100) if d % 2 == 0 else F(81, 200)
    if not baseline <= sigma <= baseline + F(143, 500) ** 2:
        raise AssertionError('verification failed')
    if p > 163:
        if not sigma <= baseline + F(37747, 2000000):
            raise AssertionError('verification failed')
    return (d, sigma)

def main():
    coefficients = coefficients_raw()
    norm_A_sq = sum((x * x + y * y for x, y in coefficients.values()))
    if not norm_A_sq == F(66033, 160000):
        raise AssertionError('verification failed')
    main_modes = {(0, 7), (0, -7)}
    if not coefficients[0, 7] == coefficients[0, -7] == (F(9, 20), F(0)):
        raise AssertionError('verification failed')
    tail = sum((abs(x) + abs(y) for v, (x, y) in coefficients.items() if v not in main_modes))
    if not tail == F(143, 500):
        raise AssertionError('verification failed')
    qclasses = defaultdict(lambda: [F(0), F(0)])
    for (u, v), (x, y) in coefficients.items():
        q = u * u - 2 * v * v
        qclasses[q][0] += x
        qclasses[q][1] += y
    maximal_inert_sigma = sum((x * x + y * y for x, y in qclasses.values()))
    if not maximal_inert_sigma == F(412563, 500000):
        raise AssertionError('verification failed')
    print('Raw Weyl modes:', len(coefficients), '||A||^2:', norm_A_sq)
    print('Tail coefficient l1 bound:', tail)
    print('Maximal inert order coefficient:', maximal_inert_sigma)
    for p in (101, 127, 199, 239, 509, 1009, 2003, 5003, 10007):
        d, s = check(p, coefficients)
        print(f'p={p:>5} d={d:>5} d||PA||^2={s} ={float(s):.9f}, Haar ratio={float(s / norm_A_sq):.7f}')
    print('All exact checks passed.')
if __name__ == '__main__':
    main()
