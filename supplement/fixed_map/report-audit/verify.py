"""Exact and finite diagnostic checks; no fixed-map BGS claim.

Run from the repository root with the project's supplemental SymPy path:
PYTHONPATH=../dependencies/python OPENBLAS_NUM_THREADS=1 python build/report-audit-20260919/verify.py
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations, product
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from sympy.polys.domains import QQ


@lru_cache(None)
def partitions(n):
    if n == 0:
        return ((),)
    answer = []
    for p in partitions(n - 1):
        answer.append(p + ((n - 1,),))
        for j in range(len(p)):
            answer.append(p[:j] + (p[j] + (n - 1,),) + p[j + 1:])
    return tuple(answer)


@lru_cache(None)
def cue_cumulant(N, modes):
    if sum(modes):
        return Fraction(0)
    answer = Fraction(0)
    for p in partitions(len(modes)):
        ell = len(p)
        sign = (-1) ** (ell - 1)
        for ordered in permutations(p):
            position = 0
            positions = [0]
            for block in ordered:
                position += sum(modes[j] for j in block)
                positions.append(position)
            span = max(positions) - min(positions)
            answer += Fraction(sign * max(N - span, 0), ell)
    return answer


def cue_moment(N, modes):
    answer = Fraction(0)
    for p in partitions(len(modes)):
        term = Fraction(1)
        for block in p:
            term *= cue_cumulant(N, tuple(modes[j] for j in block))
        answer += term
    return answer


def permutation_sign(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))


def vandermonde_moment(N, modes):
    """Independent constant-term integral of the CUE joint density.

    Symmetry fixes one Vandermonde permutation to the identity; its N!
    choices cancel 1/N! in the density. No cumulant identities are used.
    """
    answer = 0
    for assignment in product(range(N), repeat=len(modes)):
        exponents = list(range(N))
        for j, mode in zip(assignment, modes):
            exponents[j] += mode
        if sorted(exponents) == list(range(N)):
            answer += permutation_sign(exponents)
    return answer


def cubic_formula(N, a, b):
    return N - max(N - a, 0) - max(N - b, 0) + max(N - a - b, 0)


def check_cue():
    cases = 0
    for N in range(1, 7):
        for a in range(1, 2 * N + 1):
            for b in range(1, 2 * N + 1):
                modes = (a, b, -a - b)
                value = cubic_formula(N, a, b)
                assert cue_cumulant(N, modes) == value
                assert vandermonde_moment(N, modes) == value
                cases += 1
    rng = np.random.default_rng(20260919)
    mixed_cases = []
    for N in (2, 3, 4):
        for r in (2, 3, 4, 5, 6):
            for trial in range(3):
                modes = [int(x) for x in rng.integers(-2 * N, 2 * N + 1, size=r - 1)]
                modes.append(-sum(modes) if trial != 2 else 1)
                modes = tuple(modes)
                got = cue_moment(N, modes)
                expected = vandermonde_moment(N, modes)
                assert got == expected, (N, modes, got, expected)
                mixed_cases.append([N, list(modes), expected])
    for N in range(1, 8):
        for r in range(3, 7):
            modes = (N,) * (r - 1) + (-(r - 1) * N,)
            assert cue_cumulant(N, modes) == N
    # Normalized positive smooth amplitude near (3/4,3/4).
    # The entire support is in a,b<N and a+b>N, where H=x+y-1.
    # Symmetry then gives limiting integral H=1/2 times the amplitude mass.
    bump_results = []
    for N in (64, 128, 256, 512):
        t = np.arange(1, N, dtype=float) / N
        v = (t - 0.75) / 0.04
        bump = np.zeros_like(t)
        inside = abs(v) < 1
        bump[inside] = np.exp(-1 / (1 - v[inside] ** 2))
        weights = bump[:, None] * bump[None, :]
        H = np.maximum(t[:, None] + t[None, :] - 1, 0)
        ratio = np.sum(weights * H) / np.sum(weights)
        assert abs(ratio - 0.5) < 1e-12
        bump_results.append([N, float(ratio)])
    return {"exhaustive_positive_cubic_cases": cases,
            "general_exact_moment_cases": mixed_cases,
            "smooth_cubic_normalized_reference": bump_results}


def check_symbol():
    # Q=2pi(q+1/5), P=2pi p. Coefficients in Q(zeta_24) are exact.
    field = QQ.algebraic_field(sp.exp(sp.I * sp.pi / 12))
    zeta = field.unit
    ii = zeta ** 6
    sqrt3 = zeta ** 2 + zeta ** -2
    quarter = field.convert(Fraction(1, 4))
    half = field.convert(Fraction(1, 2))
    f = {(1, 0): half, (-1, 0): half,
         (2, 0): -quarter + sqrt3 / (4 * ii),
         (-2, 0): -quarter - sqrt3 / (4 * ii)}
    # sin(Q) sin(P+pi/4)
    for a, ca in ((1, -ii / 2), (-1, ii / 2)):
        for b, cb in ((1, zeta ** 3 / (2 * ii)), (-1, -zeta ** -3 / (2 * ii))):
            f[a, b] = ca * cb
    # cos(2Q) sin(2P)
    for a in (2, -2):
        f[a, 2] = -ii / 4
        f[a, -2] = ii / 4
    powers = [{(0, 0): field.one}]
    for _ in range(4):
        new = defaultdict(lambda: field.zero)
        for (a, b), c in powers[-1].items():
            for (d, e), h in f.items():
                new[a + d, b + e] += c * h
        powers.append({v: c for v, c in new.items() if c != field.zero})
    expected = {0: field.convert(Fraction(53, 256)),
                2: 9 * ii / 256, -2: -9 * ii / 256,
                4: field.convert(Fraction(-33, 1024)),
                -4: field.convert(Fraction(-33, 1024)),
                8: field.convert(Fraction(1, 1024)),
                -8: field.convert(Fraction(1, 1024))}
    actual = {b: c / 24 for (a, b), c in powers[4].items() if a == 0}
    assert actual == expected
    assert powers[3].get((0, 3), field.zero) == field.zero
    assert powers[3].get((0, -3), field.zero) == field.zero
    assert powers[4].get((0, 6), field.zero) == field.zero
    # The entire cubic vertical polynomial is NOT zero.
    cubic = {b: str(field.to_sympy(c / 6))
             for (a, b), c in powers[3].items() if a == 0}
    assert cubic
    x = sp.symbols('x', real=True)
    polynomial = sp.expand((((3 + x) / 2) ** 2 + (x*x - x + 1) ** 2
                            + 4 * ((3 + x) / 2) * (x*x - x + 1)) / 64)
    q, p = sp.symbols('q p', real=True)
    original = (sp.cos(2*sp.pi*(q+sp.Rational(1, 5)))
                + sp.cos(2*sp.pi*(2*q+sp.Rational(1, 15)))
                + sp.sin(2*sp.pi*(q+sp.Rational(1, 5))) * sp.sin(2*sp.pi*(p+sp.Rational(1, 8)))
                + sp.sin(2*sp.pi*(2*q-sp.Rational(7, 20))) * sp.sin(4*sp.pi*p))
    derivative = (2 * sp.diff(original, p, 2) - 4 * sp.diff(original, q, 2)).subs({q: 0, p: 0})
    expected_derivative = sp.pi**2 * (16*sp.cos(2*sp.pi/5) + 64*sp.cos(2*sp.pi/15)
                                     + 4*sp.sqrt(2)*sp.sin(2*sp.pi/5))
    assert sp.simplify(derivative - expected_derivative) == 0
    return {"quartic_polynomial_in_sin4pip": str(polynomial),
            "vertical_fourier_coefficients": {str(k): str(field.to_sympy(v)) for k, v in actual.items()},
            "nonzero_cubic_vertical_coefficients_div6": cubic,
            "fixed_point_trace_derivative": float(derivative.evalf()),
            "field": "Q(zeta_24), exact; q coordinate translated before convolution"}, f, field


def check_quantum_quartic(f, field):
    # Weyl W(a,b)=exp(pi i a b/N) Z^b X^a, in the ordinary midpoint gauge.
    # N>16 excludes all Fourier aliases of the fourth power.
    results = []
    for N in (17, 23, 25, 31, 33, 65):
        j = np.arange(N)
        def W(a, b):
            result = np.zeros((N, N), dtype=complex)
            result[j, (j + a) % N] = np.exp(2j * np.pi * b * (j + a / 2) / N)
            return result
        A = sum(complex(field.to_sympy(c).evalf()) * W(a, b) for (a, b), c in f.items())
        assert np.linalg.norm(A - A.conj().T) < 1e-12
        actual = np.trace(W(0, 8).conj().T @ (A @ A @ A @ A)) / (24 * N)
        expected = (1 + math.cos(16*math.pi/N) + math.cos(32*math.pi/N)) / 3072
        assert abs(actual - expected) < 1e-13, (N, actual, expected)
        results.append({"N": N, "matrix_coefficient": [actual.real, actual.imag],
                        "formula": expected})
    return results


def check_resonances():
    lam = 3 + 2 * math.sqrt(2)
    tested = 0
    samples = []
    for N in range(3, 302, 2):
        a, b, period = 1, 0, 0
        while True:
            a, b = (3*a + 4*b) % N, (2*a + 3*b) % N
            period += 1
            if b == 0 and a in (1, N-1):
                break
            assert period < 100000
        lower = 2 * math.acosh(N / 2) / math.log(lam)
        assert period + 1e-12 >= lower
        tested += 1
        if N in (7, 17, 41, 239, 301):
            samples.append([N, period, lower])
    pell = []
    n, f = 1, 0
    for K in range(1, 40):
        n, f = n + 2*f, n + f
        if K >= 3 and K % 2:
            S = sp.Matrix([[3, 4], [2, 3]])
            assert (S**K - sp.eye(2)).applyfunc(lambda x: x % n) == sp.zeros(2)
            if K in (3, 5, 7, 9, 19, 39):
                # On either parity block M^K is scalar, so every return
                # amplitude has modulus one. Sharp box window |m|<=d.
                d = (n + 1) // 2
                count = 2 * (d // K)
                pell.append({"K": K, "N": n, "plus_block_dimension": d,
                             "positive_trace_square_sum_at_multiples_K": count,
                             "putative_1_over_K": 1 / K})
    return {"all_odd_dimensions_checked": tested, "samples_N_rho_lower_bound": samples,
            "unperturbed_cat_normalization_counterexamples": pell}


def main():
    symbols, f, field = check_symbol()
    result = {"cue": check_cue(), "symbol": symbols,
              "quantum_quartic": check_quantum_quartic(f, field),
              "resonances": check_resonances(),
              "status": "Finite diagnostics and exact algebra; no BGS theorem"}
    target = Path(__file__).with_suffix('.json')
    target.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({"output": str(target), "cue_cubic_cases": result['cue']['exhaustive_positive_cubic_cases'],
                      "general_moment_cases": len(result['cue']['general_exact_moment_cases']),
                      "quartic_exact": True, "resonant_dimensions": result['resonances']['all_odd_dimensions_checked']}, indent=2))


if __name__ == '__main__':
    main()
