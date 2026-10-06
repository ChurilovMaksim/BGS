#!/usr/bin/env python3
"""Exact regressions for analytic_coboundary_regularization.md.

Standard library only. Finite Chebyshev and Laurent checks protect the scalar
algebra, not a numerical proof of the universal estimate. Orbit enumeration
for the symmetric test matrices has a proved norm-growth stopping criterion.
Fourier coefficients below are rational multiples of i.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from fractions import Fraction as F
import json
from pathlib import Path

Vec = tuple[int, int]
Mat = tuple[tuple[int, int], tuple[int, int]]
Laurent = dict[int, F]


def mv(a: Mat, v: Vec) -> Vec:
    return (a[0][0]*v[0] + a[0][1]*v[1],
            a[1][0]*v[0] + a[1][1]*v[1])


def norm2(v: Vec) -> int:
    return v[0]*v[0] + v[1]*v[1]


def combine(*terms: tuple[F | int, Laurent]) -> Laurent:
    out: Laurent = {}
    for factor, poly in terms:
        for exponent, coefficient in poly.items():
            out[exponent] = out.get(exponent, F(0)) + factor*coefficient
    return {k: v for k, v in out.items() if v}


def a_poly(n: int) -> Laurent:
    return combine((F(1, 2), {n: F(1)}),
                   (F(1, 2), {-n: F(1)}))


def scalar_checks(max_trace: int, max_order: int) -> dict:
    # Q_n(t)=lambda^n+lambda^-n, where lambda+lambda^-1=t.
    chebyshev_cases = 0
    for t in range(3, max_trace + 1):
        q = [2, t]
        for n in range(2, max_order + 1):
            q.append(t*q[-1] - q[-2])
        for n in range(max_order + 1):
            assert q[n] >= 2 + n*(t-2)
            chebyshev_cases += 1
        for n in range(max_order - 1):
            assert q[n+2] - 2*q[n+1] + q[n] >= 0

    # Exact formal Laurent identity for the second difference of a_n.
    for n in range(max_order + 1):
        lhs = combine((1, a_poly(n+2)), (-2, a_poly(n+1)),
                      (1, a_poly(n)))
        rhs = combine(
            (F(1, 2), {n+2: F(1), n+1: F(-2), n: F(1)}),
            (F(1, 2), {-n-2: F(1), -n-1: F(-2), -n: F(1)}))
        assert lhs == rhs

    ratio_cases = 0
    for lam in (F(3, 2), F(2), F(5, 2), F(3)):
        for x, y in ((F(1), F(1)), (F(3, 2), F(1)),
                     (F(7), F(2, 3))):
            for n in range(max_order + 1):
                average = (lam**n + lam**(-n))/2
                ratio = (lam**n*x + lam**(-n)*y)/(x+y)
                difference = (x-y)*(lam**n-lam**(-n))/(2*(x+y))
                assert ratio-average == difference >= 0
                assert average >= 1+n*((lam+1/lam)/2-1)
                ratio_cases += 1
    return {"trace_range": [3, max_trace], "order_range": [0, max_order],
            "chebyshev_cases": chebyshev_cases,
            "laurent_identities": max_order+1,
            "rational_ratio_cases": ratio_cases}


def orbit_intersection(a: Mat, seed: Vec, support: set[Vec]) -> set[Vec]:
    """All intersections, without an arbitrary orbit cutoff.

    For symmetric hyperbolic a, orthogonal diagonalization expresses
    ||a^n seed||^2 as alpha*lambda^(2n)+beta*lambda^(-2n), alpha,beta>=0.
    This sequence is strictly convex. Once above the support bound and
    increasing, it cannot return to the support in that direction.
    """
    assert a[0][1] == a[1][0]
    assert a[0][0]*a[1][1] - a[0][1]*a[1][0] == 1
    assert abs(a[0][0]+a[1][1]) > 2
    inv: Mat = ((a[1][1], -a[0][1]), (-a[1][0], a[0][0]))
    bound = max(map(norm2, support))
    found = {seed} & support
    for step in (a, inv):
        previous, current = seed, mv(step, seed)
        while True:
            if current in support:
                found.add(current)
            if norm2(current) > bound and norm2(current) > norm2(previous):
                break
            previous, current = current, mv(step, current)
    return found


def negative_trace_check() -> dict:
    b: Mat = ((2, 1), (1, 1))
    a: Mat = ((-2, -1), (-1, -1))
    k, bk = (1, 0), (2, 1)
    assert mv(b, k) == bk and mv(a, k) == (-2, -1)
    # h=sin(2*pi*k.x)-sin(2*pi*(Bk).x); values multiply i.
    h = {k: F(-1, 2), (-1, 0): F(1, 2),
         bk: F(1, 2), (-2, -1): F(-1, 2)}
    sums = {}
    for label, matrix in (("B", b), ("A", a)):
        remaining = set(h)
        totals = []
        while remaining:
            seed = min(remaining)
            intersection = orbit_intersection(matrix, seed, set(h))
            totals.append(sum((h[v] for v in intersection), F(0)))
            remaining -= intersection
        sums[label] = sorted(totals)
    assert sums["B"] == [F(0), F(0)]
    assert sums["A"] == [F(-1), F(1)]
    return {"B": b, "A": a,
            "B_orbit_sums_divided_by_i": list(map(str, sums["B"])),
            "A_orbit_sums_divided_by_i": list(map(str, sums["A"]))}


def transfer_check() -> int:
    cases = 0
    for width in range(1, 17):
        forcing = {j: F((-1)**abs(j)*(j*j+1), abs(j)+1)
                   for j in range(-width, width+1)}
        forcing[width+1] = -sum(forcing.values(), F(0))
        previous = F(0)
        for j in range(-width-1, width+3):
            backward = sum((v for ell, v in forcing.items() if ell <= j), F(0))
            forward = -sum((v for ell, v in forcing.items() if ell > j), F(0))
            assert backward == forward
            assert backward-previous == forcing.get(j, F(0))
            previous = backward
        assert previous == 0
        cases += 1
    return cases


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-trace", type=int, default=32)
    parser.add_argument("--max-order", type=int, default=64)
    parser.add_argument("--output", type=Path, nargs="?",
                        const=Path("build/analytic_coboundary.json"),
                        help="write JSON; omitted path defaults to build/analytic_coboundary.json")
    args = parser.parse_args()
    if args.max_trace < 3 or args.max_order < 2:
        parser.error("require --max-trace >= 3 and --max-order >= 2")
    result = {"status": "PASS", "arithmetic": "exact integers and rationals",
              "scope": "finite algebra regressions; universal proof is in mathematics/",
              "scalar": scalar_checks(args.max_trace, args.max_order),
              "negative_trace": negative_trace_check(),
              "transfer_cases": transfer_check()}
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    print("PASS analytic coboundary exact regressions")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
