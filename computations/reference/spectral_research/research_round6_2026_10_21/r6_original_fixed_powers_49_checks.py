#!/usr/bin/env python3
"""Exact integer/rational checks for r6_original_fixed_powers_49.md."""

from fractions import Fraction as F
import json
from r6_original_twostep_exact_checks import Poly, symbol_checks


def build_powers(maximum):
    powers = [(1, 0, 0)]
    for j in range(maximum):
        a, b, c = powers[-1]
        powers.append((3 * a + 2 * b, 4 * a + 3 * b, 2 * a + 3 * c))
    return powers


def main():
    fourier = symbol_checks()
    assert fourier["rational_coefficient_l1_upper_bound"] == "593/500"
    gradient = F(593, 500) * F(44, 7) * F(15, 14)
    hessian = gradient * F(44, 7)
    assert gradient == F(19569, 2450) < 8
    assert hessian == F(430518, 8575) < 64
    assert F(22, 350) < F(1, 15)
    powers = build_powers(50)
    sigma = 0
    square_sum = 0
    q, s, m = [Poly.variable(i) for i in range(3)]
    polynomial_identities = 0
    summaries = []
    for R in range(1, 51):
        a, b, c = powers[R]
        assert a * a - b * c == 1
        assert b == 2 * c
        assert a % 2 == 1 and b % 2 == c % 2 == 0
        assert 0 < a < b
        ap, bp, cp = powers[R - 1]
        Lj = 9 * (ap + bp)
        sigma += Lj
        square_sum += Lj * Lj
        assert 2 * sigma == 9 * (a - 1)
        assert square_sum <= sigma * sigma
        upper = F(51200 * sigma * sigma, 6 * 10 ** 80)
        lower = F(51200 * sigma * sigma, 7 * 10 ** 80)
        if R <= 49:
            assert upper < 1
        else:
            assert lower > 1
        if R in (1, 2, 3, 4, 48, 49, 50):
            summaries.append({
                "R": R,
                "a_R": a,
                "b_R": b,
                "Sigma_R": sigma,
                "Lambda_R": square_sum,
                "certified": R <= 49,
                "criterion_upper": str(upper),
                "probability_norm_upper_coefficient": 256 * square_sum,
            })
        if R == 3:
            assert (a, b, sigma, square_sum) == (99, 140, 441, 140211)
            assert 256 * square_sum == 35894016
        if R == 49:
            assert sigma == 73147532610169123199386258094868594249
            assert sigma < 74 * 10 ** 36
            assert upper < F(1, 2)
        if R == 50:
            assert sigma == 426335063173366200380428859644050080712
            assert sigma > 426 * 10 ** 36
        # Exact deck polynomials, evaluated symbolically over Q.
        theta = lambda mm, qq=q, ss=s: -(
            a * qq ** 2 - 2 * qq * (ss + mm) + a * (ss + mm) ** 2
        ) / (2 * b)
        identities = [
            theta(m + b) - theta(m) - q + a * (s + m) + F(a * b, 2),
            theta(m, q + 1, s) - theta(m - a) + c * (s + m) - F(a * c, 2),
            theta(m, q, s + 1) - theta(m + 1),
        ]
        for expr in identities:
            assert expr.terms == {}
            polynomial_identities += 1
        # Endpoint preimages and the unique marked Fourier source.
        p = (-a * q + s + m) / b
        for j in range(R):
            aj, bj, cj = powers[j]
            arj, brj, crj = powers[R - j]
            qj = aj * q + bj * p
            pj = cj * q + aj * p
            assert (qj - (brj * q + bj * (s + m)) / b).terms == {}
            assert (pj - (-arj * q + aj * (s + m)) / b).terms == {}
            polynomial_identities += 2
            k, ell = 7 * aj - cj, aj - 7 * bj
            assert aj * k + cj * ell == 7
            assert bj * k + aj * ell == 1
            if j == 0:
                assert (k, ell) == (7, 1)
            else:
                assert ell <= -25  # impossible for the original |l|<=1 support
    assert F(51200 * 74 ** 2, 6 * 10 ** 8) < F(1, 2)
    assert F(51200 * 426 ** 2, 7 * 10 ** 8) > 1
    print(json.dumps({
        "status": "all exact checks passed",
        "rational_gradient_factor": str(gradient),
        "rational_hessian_factor": str(hessian),
        "exact_polynomial_identities": polynomial_identities,
        "all_powers_1_through_49_certified": True,
        "criterion_fails_at_50_even_using_lower_bound_on_t": True,
        "selected_power_data": summaries,
    }, indent=2))


if __name__ == "__main__":
    main()
