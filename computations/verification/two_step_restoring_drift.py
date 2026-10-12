#!/usr/bin/env python3
"""Exact phase-residue and finite two-step drift controls."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")

import argparse
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np
import sympy as sp


def phase_product_controls():
    variable = sp.symbols("w")
    original_1, original_2 = sp.Rational(2, 5) + sp.I / 7, -sp.Rational(1, 9) + 2 * sp.I / 11
    feedback_1, feedback_2 = sp.Rational(3, 13) - sp.I / 3, sp.Rational(1, 8) + sp.I / 4
    cases = []
    for diagonal in [sp.Integer(0), sp.Rational(1, 3) + sp.I / 4, sp.Rational(2, 7) - sp.I / 5]:
        q = variable / (1 - diagonal * variable)
        qbar = 1 / (variable - sp.conjugate(diagonal))
        product = ((original_1 + q * feedback_1) * (sp.conjugate(original_1) + qbar * sp.conjugate(feedback_1))
                   * (original_2 + q * feedback_2) * (sp.conjugate(original_2) + qbar * sp.conjugate(feedback_2)))
        integrand = sp.cancel(product / variable)
        if diagonal == 0:
            integral = sp.residue(integrand, variable, 0)
        else:
            conjugate = sp.conjugate(diagonal)
            pole_free = sp.cancel((variable - conjugate)**2 * integrand)
            second_pole_residue = sp.diff(pole_free, variable).subs(variable, conjugate)
            zero_residue = original_1 * (sp.conjugate(original_1) - sp.conjugate(feedback_1) / conjugate)
            zero_residue *= original_2 * (sp.conjugate(original_2) - sp.conjugate(feedback_2) / conjugate)
            integral = zero_residue + second_pole_residue
        real = lambda value: sp.simplify((value + sp.conjugate(value)) / 2)
        square = lambda value: sp.simplify(value * sp.conjugate(value))
        a1, a2 = feedback_1 * sp.conjugate(original_1), feedback_2 * sp.conjugate(original_2)
        b1, b2 = square(feedback_1), square(feedback_2)
        p1, p2, diagonal_square = square(original_1), square(original_2), square(diagonal)
        defect = 1 - diagonal_square
        prediction = (p1 * p2 + (p1 * b2 + p2 * b1) / defect
                      + 2 * real(a1 * sp.conjugate(a2)) / defect
                      + 2 * real(sp.conjugate(diagonal) * (a1 * b2 + a2 * b1)) / defect**2
                      + (1 + diagonal_square) * b1 * b2 / defect**3)
        assert sp.cancel(sp.expand(integral - prediction)) == 0
        cases.append(str(diagonal))
    return {"complex_rational_phase_product_cases": cases,
            "independent_method": "Unit-circle constant term from residues at zero and conjugate(a); direct Laurent residue for a=0."}


def drift_controls():
    hadamard = np.array([[1]], dtype=np.int64)
    for _ in range(5):
        hadamard = np.block([[hadamard, hadamard], [hadamard, -hadamard]])
    coefficients = np.kron(np.array([[3, 4], [-4, 3]], dtype=np.int64), hadamard)
    dimension, denominator = 64, 800
    assert np.array_equal(coefficients.T @ coefficients, denominator * np.eye(dimension, dtype=np.int64))
    squares = coefficients**2
    assert np.all(squares.sum(axis=0) == denominator) and np.all(squares.sum(axis=1) == denominator)
    square_kernel = squares @ squares
    cube_kernel = square_kernel @ squares
    delta = F(int(squares.max()), denominator)
    assert delta <= F(1, 16)
    d = 1 - F(9, denominator)
    c_delta = 2 * delta / (1 - delta)**2 + delta * (1 + delta) / (1 - delta)**3
    d_delta = 4 / (1 - delta) + 2 * delta / (1 - delta)**2
    assert c_delta < F(1, 2) and d_delta < 5
    cases = []
    for i, j in [(0, 1), (0, 33), (7, 40), (31, 63)]:
        linear = coherent = cubic_ad = cubic_cb = quartic = forward_square = reverse_square = 0
        for e in range(dimension):
            if e in (i, j):
                continue
            assert int(coefficients[e, e])**2 == 9
            for k in range(dimension):
                if k == e:
                    continue
                ie, ek, ik, ke, ej, kj, ee = map(int, [coefficients[i, e], coefficients[e, k], coefficients[i, k],
                                                     coefficients[k, e], coefficients[e, j], coefficients[k, j],
                                                     coefficients[e, e]])
                forward, reverse = ie * ek * kj, ik * ke * ej
                linear += ik**2 * ke**2 * ej**2 + kj**2 * ie**2 * ek**2
                coherent += forward * reverse
                forward_square += forward**2
                reverse_square += reverse**2
                cubic_ad += abs(ee * ie * ek * ik * ke**2 * ej**2)
                cubic_cb += abs(ee * ke * ej * kj * ie**2 * ek**2)
                quartic += ie**2 * ek**2 * ke**2 * ej**2
        # Signed cubic sums are computed independently; the bounds use absolute sums.
        signed_cubic = 0
        for e in range(dimension):
            if e in (i, j):
                continue
            for k in range(dimension):
                if k == e:
                    continue
                ie, ek, ik, ke, ej, kj, ee = map(int, [coefficients[i, e], coefficients[e, k], coefficients[i, k],
                                                     coefficients[k, e], coefficients[e, j], coefficients[k, j],
                                                     coefficients[e, e]])
                signed_cubic += ee * (ie * ek * ik * ke**2 * ej**2 + ke * ej * kj * ie**2 * ek**2)
        kernel_2, kernel_3 = F(int(square_kernel[i, j]), denominator**2), F(int(cube_kernel[i, j]), denominator**3)
        entry = F(int(squares[i, j]), denominator)
        loss = -kernel_2 + F(int((squares[i, i] + squares[j, j]) * squares[i, j]), denominator**2)
        drift_times_dimension = (loss + F(linear + 2 * coherent, denominator**3) / d
                                + 2 * F(signed_cubic, denominator**4) / d**2
                                + (2 - d) * F(quartic, denominator**4) / d**3)
        assert coherent**2 <= forward_square * reverse_square
        assert forward_square <= int(cube_kernel[i, j]) and reverse_square <= int(cube_kernel[i, j])
        assert F(cubic_ad, denominator**4) <= delta * (kernel_2 + kernel_3) / 2
        assert F(cubic_cb, denominator**4) <= delta * (kernel_2 + kernel_3) / 2
        assert F(quartic, denominator**4) <= delta * kernel_2
        full_upper = -(1 - c_delta) * kernel_2 + 2 * delta * entry + d_delta * kernel_3
        simplified_upper = -kernel_2 / 2 + 5 * kernel_3 + 2 * delta * entry
        assert drift_times_dimension <= full_upper <= simplified_upper
        cases.append({"i": i, "j": j, "u_times_exact_mean_drift": str(drift_times_dimension),
                      "u_times_simplified_upper_bound": str(simplified_upper)})
    return {"arithmetic": "exact Python integers and Fraction; S has entries coefficient*sqrt(2)/40",
            "dimension": dimension, "max_intensity": str(delta), "ordered_pairs": cases}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = {"status": "PASS", "phase_products": phase_product_controls(), "drift": drift_controls(),
              "non_claims": ["Finite controls are not the general analytic theorem",
                            "No higher moments, trajectory concentration, all-time flatness or BGS theorem",
                            "No world-priority claim"]}
    serialized = json.dumps(result, indent=2) + "\n"
    if arguments.output:
        with arguments.output.open("x", encoding="utf-8") as stream:
            stream.write(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
