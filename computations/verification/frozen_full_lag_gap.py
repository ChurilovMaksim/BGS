#!/usr/bin/env python3
"""Exact finite symbol/constant audit for BGS-RES-005; not its infinite-lag proof."""
from __future__ import annotations

import argparse
from collections import defaultdict
from fractions import Fraction as F
import json
from pathlib import Path

ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def plus(*terms):
    out = defaultdict(lambda: ZERO)
    for term in terms:
        for key, value in term.items():
            out[key] = add(out[key], value)
    return {k: v for k, v in out.items() if v != ZERO}


def scale(p, a):
    return {key: mul(a, value) for key, value in p.items()}


def product(p, q):
    out = defaultdict(lambda: ZERO)
    for (k, l), a in p.items():
        for (m, n), b in q.items():
            out[k + m, l + n] = add(out[k + m, l + n], mul(a, b))
    return {k: v for k, v in out.items() if v != ZERO}


def cosine(k, l=0):
    return {(k, l): (F(1, 2), F(0)), (-k, -l): (F(1, 2), F(0))}


def sine(k, l=0):
    return {(k, l): (F(0), F(-1, 2)), (-k, -l): (F(0), F(1, 2))}


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def q(v):
    x, y = v
    return cross(v, (3*x + 2*y, 4*x + 3*y))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    unit = {(0, 0): ONE}
    r = product(plus(unit, scale(cosine(7), (F(-1), F(0)))),
                plus(unit, cosine(1)))
    shifted = {key: ((1 if key[0] % 2 == 0 else -1) * value[0],
                     (1 if key[0] % 2 == 0 else -1) * value[1])
               for key, value in r.items()}
    phase_cos = {(0, 1): (F(-3, 10), F(-2, 5)),
                 (0, -1): (F(-3, 10), F(2, 5))}
    g = plus(cosine(7), scale(r, (F(1, 10), F(0))),
             scale(product(r, sine(1)), (F(1, 100), F(0))),
             scale(product(shifted, phase_cos), (F(1, 100), F(0))),
             {(0, 0): (F(-1, 10), F(0))})
    assert (0, 0) not in g
    assert g[7, 0] == (F(9, 20), F(0)) == g[-7, 0]
    assert len(g) == 32, len(g)
    assert all((k and abs(l) <= abs(k)) or (k == 0 and l)
               for k, l in g)
    moment = sum((abs(a)+abs(b))*(k*k+l*l)
                 for (k, l), (a, b) in g.items())
    assert moment == F(51451, 1000), moment

    # The two irrational bounds are established by rational squaring.
    assert F(201, 20)**2 > 101
    assert F(283, 200)**2 > 2
    assert F(7, 5)**2 < 2
    assert (3+2*F(7, 5))**2 > F(100, 3)  # lambda^(-2)<3/100
    e_bound = 2*F(201, 20)/25 + (39+F(283, 200))/200
    assert e_bound < F(101, 100)
    assert F(583, 100)**2 > 6*F(583, 100)-1  # lambda<5.83
    assert F(3969, 50)/F(583, 100) > F(68, 5)
    pert_bound = F(103, 100)*F(177, 250)*(
        F(63, 5)*F(101, 100) + F(101, 100)**2)
    assert F(177, 250)**2 > F(1, 2)
    assert pert_bound < F(401, 40), pert_bound
    assert F(103, 100)*F(177, 250)*(F(63, 10)+F(101, 100))**2 < 40
    assert F(68, 5)-F(401, 40) == F(143, 40) > F(7, 2)
    assert F(7, 2)-F(10401, 5000) > 1
    assert 40+F(10401, 5000) < 43

    # These finitely many samples check implementation/sign conventions only.
    keys = tuple(g)
    visited = 0
    for u in keys:
        for v in keys:
            z = v
            values = []
            for lag in range(1, 13):
                z = (3*z[0]+2*z[1], 4*z[0]+3*z[1])
                if cross(u, z) and u != (-z[0], -z[1]):
                    values.append(q((u[0]+z[0], u[1]+z[1])))
            assert len(values) == len(set(values))
            visited += 1
    result = {'status': 'passed', 'arithmetic': 'fractions and exact integer lattice',
              'frequencies': len(g), 'ordered_frequency_pairs': visited,
              'sampled_lags_per_pair': 12, 'M2_real_imag': str(moment),
              'perturbation_bound_over_pi': str(pert_bound),
              'nonclaim': 'Finite orbit sampling does not prove the infinite-lag theorem; see the maintained proof.'}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
