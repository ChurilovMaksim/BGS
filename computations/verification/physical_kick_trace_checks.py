#!/usr/bin/env python3
"""Finite checks for TRACE-106/107, not a certificate of asymptotic decay.

Standard library only. Exact rational Fourier algebra and modular exponents;
bounded Pell enumeration; a small floating-point Fourier clock identity.
Explicit exceptions remain active under python -O. No files are overwritten.
"""
from fractions import Fraction as F
from collections import defaultdict
import cmath
import json
import math


def require(value, label):
    if not value:
        raise RuntimeError(label)


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def mul(z, w):
    return z[0]*w[0]-z[1]*w[1], z[0]*w[1]+z[1]*w[0]


def scale(z, c):
    return z[0]*c, z[1]*c


def polyadd(*ps):
    d = defaultdict(lambda: (F(0), F(0)))
    for p in ps:
        for v, z in p.items():
            d[v] = add(d[v], z)
    return {v: z for v, z in d.items() if z != (0, 0)}


def polymul(p, q):
    d = defaultdict(lambda: (F(0), F(0)))
    for v, z in p.items():
        for w, t in q.items():
            u = (v[0]+w[0], v[1]+w[1])
            d[u] = add(d[u], mul(z, t))
    return {v: z for v, z in d.items() if z != (0, 0)}


def scaled(p, a):
    return {v: scale(z, a) for v, z in p.items()}


def cosine(k):
    return {(k, 0): (F(1, 2), F(0)), (-k, 0): (F(1, 2), F(0))}


def coefficient_checks():
    one = {(0, 0): (F(1), F(0))}
    r = polymul(polyadd(one, scaled(cosine(7), -1)), polyadd(one, cosine(1)))
    sinq = {(1, 0): (F(0), F(-1, 2)), (-1, 0): (F(0), F(1, 2))}
    cosp = {(0, 1): (F(-3, 10), F(-2, 5)),
            (0, -1): (F(-3, 10), F(2, 5))}
    a = polyadd(cosine(7), scaled(r, F(1, 10)),
                scaled(polymul(r, sinq), F(1, 100)),
                scaled(polymul(r, cosp), F(1, 100)), scaled(one, F(-1, 10)))
    require(len(a) == 32 and (0, 0) not in a, 'Fourier support')
    require(all(a[(-k, -l)] == (z[0], -z[1]) for (k, l), z in a.items()),
            'Hermitian Fourier symmetry')
    ordinary = {(k, l): scale(z, -1 if (k*l) % 2 else 1) for (k, l), z in a.items()}
    expected = {-1: (F(-3, 125), F(4, 125)),
                0: (F(-784, 5), F(0)), 1: (F(-3, 125), F(-4, 125))}
    for l in (-1, 0, 1):
        sums = []
        for degree in range(3):
            val = (F(0), F(0))
            for (k, ell), z in ordinary.items():
                if ell == l:
                    val = add(val, scale(z, k**degree))
            sums.append(val)
        require(sums[0] == ((F(9, 10), F(0)) if l == 0 else (0, 0)), 'critical value')
        require(sums[1] == (0, 0), 'critical first derivative')
        require(scale(sums[2], -4) == expected[l], 'critical Hessian')
    require(7*F(19, 25)/4-2*F(7, 50) == F(21, 20), 'first derivative margin')
    require(49*F(19, 25)*F(19, 20)-14*F(7, 50)/4-F(8, 25)
            == F(4321, 125), 'second derivative margin')
    beta = F(1, 2)
    alpha = 1/(4+beta)
    require(alpha*beta == 1-4*alpha == F(1, 9), 'balanced exponents')
    require(2-8*alpha == F(2, 9), 'positive square remainder exponent')
    return {'support': 32, 'critical_hessian': {str(k): [str(x) for x in v]
            for k, v in expected.items()}, 'new_exponent': '1/9'}


def weyl_checks():
    count = 0
    moduli = [3, 5, 7, 9, 15, 21]
    for n in moduli:
        labels = [(0, 0), (1, -1), (n+2, -2*n-1), (-3*n, n+1), (7, 8)]
        inv2 = pow(2, -1, n)
        for k, l in labels:
            for x in range(n):
                # Compare exponents in e_{2N}; includes integer-label alias signs.
                modular = 2*k*(x+inv2*l)+k*l*n
                ordinary = 2*k*x+k*l
                require((modular-ordinary) % (2*n) == 0, 'ordinary-half conversion')
            for kp, lp in labels:
                for x in range(n):
                    lhs = 2*k*x+k*l+2*kp*((x+l) % n)+kp*lp
                    rhs = 2*(k+kp)*x+(k+kp)*(l+lp)+l*kp-k*lp
                    require((lhs-rhs) % (2*n) == 0, 'integer-label Weyl product')
                    count += 1
    return {'odd_moduli': moduli, 'exact_product_instances': count}


def pell_checks():
    rows = []
    x, y = 1, 0
    for r in range(1, 104):
        x, y = x+2*y, x+y
        if r < 3 or r % 2 == 0:
            continue
        n, c = x*y, x*x+2*y*y
        require(x*x-2*y*y == -1 and math.gcd(x, y) == 1, 'Pell primitive')
        require(c % x == 1 and c % y == y-1, 'CRT signs')
        v, w = (x+y)//2, (x-y)//2
        require(v+c*w == n*(2*y-x) and v+w == x, 'short alias witness')
        for p in range(-8, 9):
            for q in range(-8, 9):
                if (p-q) % 2:
                    continue
                vv, ww = (x*p+y*q)//2, (x*p-y*q)//2
                require((vv+c*ww) % n == 0, 'CRT parameterization')
                require(abs(vv)+abs(ww) == max(x*abs(p), y*abs(q)), 'l1 formula')
        if r <= 9:
            aliases = []
            for ww in range(-x, x+1):
                bound = x-abs(ww)
                for k in range(-((-c*ww+bound)//n), (c*ww+bound)//n+1):
                    vv = -c*ww+k*n
                    if vv or ww:
                        aliases.append((vv, ww))
            require(sorted(aliases) == sorted([(v,w),(w,v),(-v,-w),(-w,-v)]),
                    'exhaustive shortest aliases')
        rows.append(r)
    return {'odd_indices': rows, 'exhaustive_l1_search_indices': [3, 5, 7, 9]}


def clock_check():
    n, m = 17, 4
    cs = [complex(F(j, 1000), F(-j, 2000)) for j in range(1, m+1)]
    zs = [cmath.exp(2j*math.pi*l/n) for l in range(n)]
    weights = [(1+sum(c*z**(-j)+c.conjugate()*z**j
                for j,c in enumerate(cs,1)))/n for z in zs]
    require(min(w.real for w in weights)>0, 'positive clock weights')
    err = max(abs(sum(w*z**j for w,z in zip(weights,zs))-c)
              for j,c in enumerate(cs,1))
    require(err < 1e-12 and abs(sum(weights)-1)<1e-12, 'clock prefix identity')
    return {'N': n, 'm': m, 'arithmetic': 'complex binary64', 'max_error': err}


if __name__ == '__main__':
    print(json.dumps({'status': 'passed', 'asymptotics_computationally_verified': False,
        'coefficients': coefficient_checks(), 'weyl': weyl_checks(),
        'pell': pell_checks(), 'clock': clock_check()}, indent=2))
