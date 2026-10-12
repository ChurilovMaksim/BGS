#!/usr/bin/env python3
"""Finite controls for a static unitary obstruction, not Schur evolution."""

from __future__ import annotations

if not __debug__:
    raise RuntimeError(
        "Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE."
    )

import argparse
import json
from math import log, sqrt
from pathlib import Path

import numpy as np
import sympy as sp


def exact_unitary(dimension, seed):
    """Rational orthogonal fixtures using two explicit plane rotations."""
    matrix = sp.eye(dimension)
    for index in range(1, dimension):
        cosine, sine = (
            (sp.Rational(3, 5), sp.Rational(4, 5))
            if (index + seed) % 2
            else (sp.Rational(5, 13), sp.Rational(12, 13))
        )
        rotation = sp.eye(dimension)
        rotation[0, 0] = rotation[index, index] = cosine
        rotation[0, index] = sine
        rotation[index, 0] = -sine
        matrix = matrix * rotation
    return matrix * sp.diag(
        *[(-1) ** ((index + seed) % 2) for index in range(dimension)]
    )


def exact_correction(source, target):
    if source == target:
        return sp.eye(source.rows)
    difference = source - target
    denominator = 1 - (target.conjugate().T * source)[0]
    return (
        sp.eye(source.rows)
        - difference * difference.conjugate().T / denominator
    ).applyfunc(sp.simplify)


def exact_controls():
    cases = 0
    for dimension in (8, 12):
        for seed in (0, 1):
            original = exact_unitary(dimension, seed)
            identity = sp.eye(dimension)
            prescribed = sp.zeros(dimension, 1)
            prescribed[2:6, 0] = sp.ones(4, 1) / 2
            left = exact_correction(original[:, 1], prescribed)
            intermediate = (left * original).applyfunc(sp.simplify)
            row = intermediate.conjugate().T[:, 0]
            right = exact_correction(prescribed, row)
            matrix = (intermediate * right).applyfunc(sp.simplify)

            assert (original.conjugate().T * original).applyfunc(sp.simplify) == identity
            assert (matrix.conjugate().T * matrix).applyfunc(sp.simplify) == identity
            assert matrix[:, 1] == prescribed
            assert matrix.conjugate().T[:, 0] == prescribed
            assert (matrix - original).rank() <= 2
            intensity = matrix.applyfunc(
                lambda value: sp.simplify(value * sp.conjugate(value))
            )
            uniform = sp.ones(dimension) / dimension
            centered = intensity - uniform
            assert (intensity * intensity)[0, 1] == sp.Rational(1, 4)
            assert centered * centered == intensity * intensity - uniform
            assert centered**3 == intensity**3 - uniform
            row_square = sum(value**2 for value in centered.row(0))
            column_square = sum(value**2 for value in centered.col(1))
            assert row_square == column_square == sp.Rational(1, 4) - 1 / sp.Integer(dimension)
            assert (centered**2)[0, 1] == row_square
            cases += 1

    source = sp.Matrix([(3 + 4 * sp.I) / 5, 0])
    target = sp.Matrix([0, 1])
    correction = exact_correction(source, target)
    assert (correction.conjugate().T * correction).applyfunc(sp.simplify) == sp.eye(2)
    assert (correction * source).applyfunc(sp.simplify) == target
    assert (correction - sp.eye(2)).rank() == 1

    dimension = sp.symbols("n", positive=True)
    denominator = (dimension + 1) * (dimension + 2) * (dimension + 3)
    mean_square_sum = 2 / (dimension + 1)
    mean_cube_sum = 6 / ((dimension + 1) * (dimension + 2))
    mean_square_sum_squared = 4 * (dimension + 5) / denominator
    moment = sp.factor(
        dimension * mean_square_sum_squared
        + (1 - mean_square_sum - 2 * mean_cube_sum + 2 * mean_square_sum_squared)
        - 1
    )
    expected = 2 * (dimension - 1) * (dimension + 4) / denominator
    assert sp.cancel(moment - expected) == 0
    assert expected.subs(dimension, 2) == sp.Rational(1, 5)
    return {
        "rational_orthogonal_construction_fixtures": cases,
        "complex_rank_one_primitive_fixtures": 1,
        "dimensions": [8, 12],
        "support_size": 4,
        "exact_two_step_peak": "1/4",
        "exact_row_column_Cauchy_bound_saturated": True,
        "Haar_fourth_Schatten_polynomial": str(moment),
        "coverage": "Exact finite construction, rank, unitarity, centering and "
        "algebraic moment combination; no probability theorem is tested.",
    }


def floating_correction(source, target):
    difference = source - target
    if np.linalg.norm(difference) < 1e-14:
        return np.eye(source.size, dtype=complex)
    return np.eye(source.size) - np.outer(difference, difference.conj()) / (
        1 - np.vdot(target, source)
    )


def numerical_controls():
    generator = np.random.default_rng(20261011)
    rows = []
    for dimension in (32, 64, 128):
        for trial in range(2):
            gaussian = (
                generator.standard_normal((dimension, dimension))
                + 1j * generator.standard_normal((dimension, dimension))
            ) / sqrt(2)
            original, triangular = np.linalg.qr(gaussian)
            original = original * (
                np.diag(triangular) / np.abs(np.diag(triangular))
            )
            support_size = int(dimension / log(2 * dimension))
            prescribed = np.zeros(dimension, dtype=complex)
            prescribed[2 : 2 + support_size] = 1 / sqrt(support_size)
            intermediate = floating_correction(original[:, 1], prescribed) @ original
            matrix = intermediate @ floating_correction(
                prescribed, intermediate.conj().T[:, 0]
            )
            intensity = np.abs(matrix) ** 2
            centered = intensity - 1 / dimension
            operator_norm = np.linalg.norm(centered, ord=2)
            unitarity = np.linalg.norm(
                matrix.conj().T @ matrix - np.eye(dimension), ord=2
            )
            assert unitarity < 1e-11
            assert abs((intensity @ intensity)[0, 1] - 1 / support_size) < 1e-11
            singular_values = np.linalg.svd(matrix - original, compute_uv=False)
            assert singular_values[2] < 1e-11
            row_norms = np.linalg.norm(centered, axis=1)
            column_norms = np.linalg.norm(centered, axis=0)
            third_step = centered @ centered @ centered
            third_bound = np.outer(row_norms, column_norms) * operator_norm
            assert np.max(np.abs(third_step) - third_bound) < 1e-11
            rows.append(
                {
                    "n": dimension,
                    "trial": trial,
                    "support_size": support_size,
                    "max_intensity": float(intensity.max()),
                    "centered_intensity_operator_norm": float(operator_norm),
                    "n_times_two_step_peak": float(
                        dimension * (intensity @ intensity)[0, 1]
                    ),
                    "n_times_max_third_step_defect": float(
                        dimension * np.max(np.abs(third_step))
                    ),
                    "unitarity_error": float(unitarity),
                }
            )
    return {"arithmetic": "float64 diagnostic only", "seed": 20261011, "cases": rows}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    arguments = parser.parse_args()
    result = {
        "status": "PASS",
        "exact": exact_controls(),
        "numerical": numerical_controls(),
        "non_claims": [
            "No finite check proves the asymptotic existence theorem",
            "No random Schur trajectory or flatness probability is tested",
            "No chaotic quantizer or BGS counterexample is constructed",
            "No world priority claim",
        ],
    }
    serialized = json.dumps(result, indent=2) + "\n"
    if arguments.output:
        with arguments.output.open("x", encoding="utf-8") as output:
            output.write(serialized)
    print(serialized, end="")


if __name__ == "__main__":
    main()
