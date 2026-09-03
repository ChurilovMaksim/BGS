#!/usr/bin/env python3
"""Finite-sample nearest-neighbour spacing experiment against a GOE control law."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))

from bgs.jacobi import annihilator_indices, dlog_table, jacobi_matrix
from bgs.twisted_jacobi import primitive_root

OUTPUT = ROOT / "results" / "numerical" / "goe_spacing.json"


def unfold_polynomial(eigenvalues: np.ndarray, degree: int = 11) -> np.ndarray:
    """Unfold one finite spectrum by a smooth polynomial counting fit."""
    ordered = np.sort(eigenvalues)
    count = len(ordered)
    empirical_cdf = np.arange(1, count + 1) / (count + 1)
    coefficients = np.polyfit(ordered, empirical_cdf, degree)
    return count * np.polyval(coefficients, ordered)


def normalized_gaps(eigenvalues: np.ndarray) -> np.ndarray:
    unfolded = np.sort(unfold_polynomial(eigenvalues))
    gaps = np.diff(unfolded)
    return gaps / gaps.mean()


def goe_wigner_cdf(spacing: np.ndarray) -> np.ndarray:
    """CDF of the GOE Wigner surmise used as the finite reference law."""
    return 1.0 - np.exp(-np.pi * spacing**2 / 4.0)


def kolmogorov_smirnov_statistic(gaps: np.ndarray) -> tuple[float, float]:
    ordered = np.sort(gaps)
    sample_size = len(ordered)
    empirical = np.arange(1, sample_size + 1) / sample_size
    statistic = float(np.max(np.abs(empirical - goe_wigner_cdf(ordered))))
    critical_5pct = float(1.358 / np.sqrt(sample_size))
    return statistic, critical_5pct


def chi_squared_statistic(gaps: np.ndarray) -> tuple[float, int]:
    bins = np.linspace(0.0, 4.0, 21)
    observed, _ = np.histogram(gaps, bins=bins)
    centers = (bins[:-1] + bins[1:]) / 2.0
    density = (np.pi * centers / 2.0) * np.exp(-np.pi * centers**2 / 4.0)
    expected = density * np.diff(bins) * len(gaps)
    usable = expected >= 5.0
    statistic = float(
        np.sum((observed[usable] - expected[usable]) ** 2 / expected[usable])
    )
    degrees_of_freedom = int(usable.sum()) - 1
    return statistic, degrees_of_freedom


def run_design(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    q_step: int,
    q_stop: int,
) -> dict[str, object]:
    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)
    character_indices = annihilator_indices(
        prime, subgroup_order, eigenvalue, dlog
    )
    odd_sector = character_indices[character_indices % 2 == 1]

    all_gaps: list[float] = []
    inverse_two = pow(2, prime - 2, prime)
    q_values = list(range(1, q_stop, q_step))

    for q in q_values:
        jacobi = jacobi_matrix(
            prime,
            subgroup_order,
            eigenvalue,
            dlog,
            odd_sector,
            q,
        )
        normalized = (
            np.exp(-2j * np.pi * (inverse_two * q % prime) / prime)
            * jacobi
            / (prime - 1)
        )
        hermitian = (normalized + normalized.conj().T).real
        all_gaps.extend(normalized_gaps(np.linalg.eigvalsh(hermitian)))

    gaps = np.asarray(all_gaps)
    ks_value, ks_critical = kolmogorov_smirnov_statistic(gaps)
    chi2_value, degrees_of_freedom = chi_squared_statistic(gaps)

    return {
        "N": prime,
        "K": subgroup_order,
        "a": eigenvalue,
        "matrix_dimension": int(len(odd_sector)),
        "q_values_used": len(q_values),
        "gap_count": int(len(gaps)),
        "mean_normalized_gap": float(gaps.mean()),
        "ks_D": ks_value,
        "ks_critical_5pct": ks_critical,
        "ks_pass": bool(ks_value < ks_critical),
        "chi_squared": chi2_value,
        "degrees_of_freedom": degrees_of_freedom,
        "chi_squared_per_dof": chi2_value / degrees_of_freedom,
    }


def main() -> None:
    started = time.time()
    rows = [
        run_design(3571, 17, 2469, q_step=5, q_stop=200),
        run_design(19489, 29, 4523, q_step=7, q_stop=300),
    ]
    result = {
        "producer": "experiments/spectral/goe_spacing.py",
        "interpretation": "finite numerical evidence only",
        "reference": "GOE Wigner surmise P(s)=(pi*s/2) exp(-pi*s^2/4)",
        "designs": rows,
        "finite_sample_criterion_pass": all(
            row["ks_pass"] and row["chi_squared_per_dof"] < 1.5 for row in rows
        ),
        "wall_seconds": time.time() - started,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
