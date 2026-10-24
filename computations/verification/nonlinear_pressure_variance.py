#!/usr/bin/env python3
"""Exact Fourier check for BGS-FM-006; no thermodynamic limit is computed.

All coefficients lie in Q(i). The script constructs the ordinary-midpoint
symbol directly from its trigonometric formula, independently of the
coefficient table in mathematics/resonance-cohomology/frozen_full_lag_resonance.md.
"""

from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import defaultdict
from fractions import Fraction as Q
import json
from pathlib import Path

ComplexQ = tuple[Q, Q]
ZERO: ComplexQ = (Q(0), Q(0))


def add(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] + b[0], a[1] + b[1]


def mul(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def scaled(a: ComplexQ, c: Q | int) -> ComplexQ:
    return c * a[0], c * a[1]


def parity(n: int) -> int:
    return 1 if n % 2 == 0 else -1


def frequency_map() -> dict[tuple[int, int], ComplexQ]:
    # r(q)=(1-cos(14 pi q))(1+cos(2 pi q)).
    r = {0: Q(1), 1: Q(1, 2), -1: Q(1, 2),
         7: -Q(1, 2), -7: -Q(1, 2),
         6: -Q(1, 4), -6: -Q(1, 4),
         8: -Q(1, 4), -8: -Q(1, 4)}
    coeff: defaultdict[tuple[int, int], ComplexQ] = defaultdict(lambda: ZERO)
    for k, value in r.items():
        coeff[k, 0] = add(coeff[k, 0], (value / 10, Q(0)))
        for m, sine in ((1, (Q(0), -Q(1, 2))),
                        (-1, (Q(0), Q(1, 2)))):
            coeff[k + m, 0] = add(coeff[k + m, 0], scaled(sine, value / 100))
        # r(q+1/2) contributes the (-1)^k ordinary-Weyl correction.
        for ell, phase in ((1, (-Q(3, 10), -Q(2, 5))),
                           (-1, (-Q(3, 10), Q(2, 5)))):
            coeff[k, ell] = add(coeff[k, ell],
                                scaled(phase, parity(k) * value / 100))
    for k in (-7, 7):
        coeff[k, 0] = add(coeff[k, 0], (Q(1, 2), Q(0)))
    coeff[0, 0] = add(coeff[0, 0], (-Q(1, 10), Q(0)))
    return {v: c for v, c in coeff.items() if c != ZERO}


def cat_dual(v: tuple[int, int]) -> tuple[int, int]:
    k, ell = v
    return 3 * k + 2 * ell, 4 * k + 3 * ell


def quadratic(v: tuple[int, int]) -> int:
    k, ell = v
    return 4 * k * k - 2 * ell * ell


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    g = frequency_map()
    assert len(g) == 32 and (0, 0) not in g
    assert g[7, 0] == g[-7, 0] == (Q(9, 20), Q(0))
    assert all(g.get((-k, -ell)) == (a, -b)
               for (k, ell), (a, b) in g.items())
    assert all(quadratic(cat_dual(v)) == quadratic(v) for v in g)

    # All supported p-frequencies have |ell| <= 1. The second dual iterate
    # has both coordinates of the same sign and |ell| >= 7, which then
    # increases strictly at every further positive iterate. This certifies
    # the absence of every covariance beyond lag 1, not a sampled cutoff.
    assert all(abs(v[1]) <= 1 for v in g)
    second = {v: cat_dual(cat_dual(v)) for v in g}
    assert all(k * ell > 0 and abs(ell) >= 7
               for k, ell in second.values())

    # b=(g_pp-2g_qq)/(2 sqrt(2)), so b_v=(pi^2/sqrt(2)) q(v) g_v.
    # The returned correlations are exactly 2/pi^4 times integral b(x)b(S^n x) dx.
    covariances: list[Q] = []
    for n in (0, 1):
        value = ZERO
        for v, coefficient in g.items():
            image = v if n == 0 else cat_dual(v)
            target = g.get((-image[0], -image[1]), ZERO)
            value = add(value, scaled(mul(coefficient, target), quadratic(v) ** 2))
        assert value[1] == 0
        covariances.append(value[0])
    assert covariances == [Q(313386243, 20000), -Q(7, 500000)]
    variance = covariances[0] + 2 * covariances[1]
    assert variance == Q(7834656061, 500000) > 0

    # At these four fixed points g_pp=0. The sums are sqrt(2)b/pi^2,
    # equivalently minus the source's Hessian b_x/pi^2.
    fixed: dict[str, str] = {}
    expected = {(0, 0): Q(19606, 125), (0, 1): Q(19594, 125),
                (1, 0): -Q(24306, 125), (1, 1): -Q(24894, 125)}
    for (i, j), target in expected.items():
        value = ZERO
        for (k, ell), coefficient in g.items():
            value = add(value, scaled(coefficient,
                                      parity(k * i + ell * j) * quadratic((k, ell))))
        assert value == (target, Q(0)), (i, j, value)
        fixed[f"({i}/2,{j}/2)"] = str(value[0])

    result = {
        "claim_id": "BGS-FM-006",
        "arithmetic": "exact rational pairs representing Q(i)",
        "scope": "32 Fourier modes, complete covariance support by a proved cone argument; no pressure-limit or BGS proof",
        "fourier_modes": len(g),
        "two_over_pi4_times_covariance": {"0": str(covariances[0]), "1": str(covariances[1]), "all_n_ge_2": "0"},
        "two_over_pi4_times_asymptotic_variance": str(variance),
        "fixed_points_sqrt2_b_over_pi2": fixed,
    }
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
