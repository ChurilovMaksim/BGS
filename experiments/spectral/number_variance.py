#!/usr/bin/env python3
"""Compare finite cat-map number variance with a matched GOE simulation."""
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

OUTPUT = ROOT / "results" / "numerical" / "goe_number_variance.json"


def unfold_polynomial(eigenvalues: np.ndarray, degree: int = 11) -> np.ndarray:
    ordered = np.sort(eigenvalues)
    count = len(ordered)
    empirical_cdf = np.arange(1, count + 1) / (count + 1)
    coefficients = np.polyfit(ordered, empirical_cdf, degree)
    return count * np.polyval(coefficients, ordered)


def number_variance(unfolded: np.ndarray, windows: list[int]) -> dict[int, float]:
    ordered = np.sort(unfolded)
    count = len(ordered)
    output: dict[int, float] = {}

    for width in windows:
        occupation_counts: list[int] = []
        for left_index in range(count):
            right_index = left_index
            while (
                right_index < count
                and ordered[right_index] < ordered[left_index] + width
            ):
                right_index += 1
            occupation_counts.append(right_index - left_index)
        output[width] = float(np.var(occupation_counts))
    return output


def main() -> None:
    started = time.time()
    prime, subgroup_order, eigenvalue = 19489, 29, 4523
    windows = [1, 2, 3, 5, 8, 12]
    q_values = list(range(1, 300, 12))
    goe_simulations = 60
    rng = np.random.default_rng(20260901)

    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)
    character_indices = annihilator_indices(
        prime, subgroup_order, eigenvalue, dlog
    )
    odd_sector = character_indices[character_indices % 2 == 1]
    dimension = len(odd_sector)
    inverse_two = pow(2, prime - 2, prime)

    cat_map_samples = {width: [] for width in windows}
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
        statistics = number_variance(
            unfold_polynomial(np.linalg.eigvalsh(hermitian)), windows
        )
        for width in windows:
            cat_map_samples[width].append(statistics[width])

    goe_samples = {width: [] for width in windows}
    for _ in range(goe_simulations):
        random_matrix = rng.normal(size=(dimension, dimension))
        goe_matrix = (random_matrix + random_matrix.T) / 2.0
        statistics = number_variance(
            unfold_polynomial(np.linalg.eigvalsh(goe_matrix)), windows
        )
        for width in windows:
            goe_samples[width].append(statistics[width])

    rows: list[dict[str, object]] = []
    for width in windows:
        cat_mean = float(np.mean(cat_map_samples[width]))
        goe_mean = float(np.mean(goe_samples[width]))
        cat_sem = float(
            np.std(cat_map_samples[width]) / np.sqrt(len(cat_map_samples[width]))
        )
        goe_sem = float(
            np.std(goe_samples[width]) / np.sqrt(goe_simulations)
        )
        combined_sem = np.sqrt(cat_sem**2 + goe_sem**2)
        z_score = abs(cat_mean - goe_mean) / combined_sem
        rows.append(
            {
                "window": width,
                "cat_map_mean": cat_mean,
                "cat_map_sem": cat_sem,
                "goe_mean": goe_mean,
                "goe_sem": goe_sem,
                "absolute_z_score": float(z_score),
                "within_two_sigma": bool(z_score < 2.0),
            }
        )

    result = {
        "producer": "experiments/spectral/number_variance.py",
        "interpretation": "finite numerical evidence only",
        "design": {
            "N": prime,
            "K": subgroup_order,
            "a": eigenvalue,
            "matrix_dimension": int(dimension),
            "q_values_used": len(q_values),
            "goe_simulations": goe_simulations,
        },
        "rows": rows,
        "finite_sample_criterion_pass": all(
            row["within_two_sigma"] for row in rows
        ),
        "wall_seconds": time.time() - started,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
