#!/usr/bin/env python3
"""Descriptive finite spectral diagnostics for the arithmetic cat-map project.

The historical scripts used IID-KS and "number variance" language that was too
strong for their actual sampling scheme.  This replacement keeps the useful
computations but reports only descriptive quantities:

* an empirical CDF sup-distance to the GOE Wigner surmise;
* a matched GOE comparison for forward windows anchored at eigenvalues.

The latter is deliberately called ``forward_window_count_variance``.  It is not
the stationary number variance Sigma^2(L), and neither diagnostic is a
hypothesis test or a proof of a limiting BGS law.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.jacobi import annihilator_indices, dlog_table, jacobi_matrix  # noqa: E402
from bgs.finite_field import primitive_root  # noqa: E402


def unfold_polynomial(eigenvalues: np.ndarray, degree: int = 11) -> np.ndarray:
    ordered = np.sort(np.asarray(eigenvalues, dtype=float))
    if len(ordered) < 4:
        raise ValueError("at least four eigenvalues are required for unfolding")
    degree = min(degree, len(ordered) - 2)
    empirical_cdf = np.arange(1, len(ordered) + 1) / (len(ordered) + 1)
    coefficients = np.polyfit(ordered, empirical_cdf, degree)
    return len(ordered) * np.polyval(coefficients, ordered)


def normalized_gaps(eigenvalues: np.ndarray) -> np.ndarray:
    unfolded = np.sort(unfold_polynomial(eigenvalues))
    gaps = np.diff(unfolded)
    mean = float(gaps.mean())
    if not mean > 0.0:
        raise ValueError("non-positive mean unfolded gap")
    return gaps / mean


def goe_wigner_cdf(spacing: np.ndarray) -> np.ndarray:
    spacing = np.asarray(spacing, dtype=float)
    return 1.0 - np.exp(-np.pi * spacing**2 / 4.0)


def empirical_cdf_sup_distance(gaps: np.ndarray) -> float:
    ordered = np.sort(np.asarray(gaps, dtype=float))
    empirical = np.arange(1, len(ordered) + 1) / len(ordered)
    return float(np.max(np.abs(empirical - goe_wigner_cdf(ordered))))


def forward_window_count_variance(
    unfolded: np.ndarray, widths: list[int]
) -> dict[int, float]:
    """Historical edge-truncated forward-window statistic, named literally."""
    ordered = np.sort(np.asarray(unfolded, dtype=float))
    count = len(ordered)
    output: dict[int, float] = {}
    for width in widths:
        occupations: list[int] = []
        right = 0
        for left in range(count):
            right = max(right, left)
            while right < count and ordered[right] < ordered[left] + width:
                right += 1
            occupations.append(right - left)
        output[width] = float(np.var(occupations))
    return output


def sector_eigenvalues(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    q: int,
) -> np.ndarray:
    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)
    character_indices = annihilator_indices(
        prime, subgroup_order, eigenvalue, dlog
    )
    odd_sector = character_indices[character_indices % 2 == 1]
    if len(odd_sector) < 4:
        raise ValueError("odd character sector is too small for spectral diagnostics")

    jacobi = jacobi_matrix(
        prime,
        subgroup_order,
        eigenvalue,
        dlog,
        odd_sector,
        q,
    )
    inverse_two = pow(2, prime - 2, prime)
    normalized = (
        np.exp(-2j * np.pi * (inverse_two * q % prime) / prime)
        * jacobi
        / (prime - 1)
    )
    hermitian = (normalized + normalized.conj().T).real
    return np.linalg.eigvalsh(hermitian)


def spacing_design(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    q_values: list[int],
) -> dict[str, object]:
    gaps: list[float] = []
    dimension = 0
    for q in q_values:
        spectrum = sector_eigenvalues(prime, subgroup_order, eigenvalue, q)
        dimension = len(spectrum)
        gaps.extend(normalized_gaps(spectrum).tolist())
    array = np.asarray(gaps, dtype=float)
    return {
        "N": prime,
        "K": subgroup_order,
        "a": eigenvalue,
        "matrix_dimension": int(dimension),
        "q_values_used": len(q_values),
        "gap_count": int(len(array)),
        "mean_normalized_gap": float(array.mean()),
        "cdf_sup_distance_to_wigner_surmise": empirical_cdf_sup_distance(array),
    }


def matched_window_design(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    q_values: list[int],
    widths: list[int],
    goe_simulations: int,
    seed: int,
) -> dict[str, object]:
    cat_samples = {width: [] for width in widths}
    dimension = 0
    for q in q_values:
        spectrum = sector_eigenvalues(prime, subgroup_order, eigenvalue, q)
        dimension = len(spectrum)
        statistic = forward_window_count_variance(
            unfold_polynomial(spectrum), widths
        )
        for width in widths:
            cat_samples[width].append(statistic[width])

    rng = np.random.default_rng(seed)
    goe_samples = {width: [] for width in widths}
    for _ in range(goe_simulations):
        random_matrix = rng.normal(size=(dimension, dimension))
        goe_matrix = (random_matrix + random_matrix.T) / 2.0
        statistic = forward_window_count_variance(
            unfold_polynomial(np.linalg.eigvalsh(goe_matrix)), widths
        )
        for width in widths:
            goe_samples[width].append(statistic[width])

    rows = []
    for width in widths:
        cat = np.asarray(cat_samples[width], dtype=float)
        goe = np.asarray(goe_samples[width], dtype=float)
        cat_mean = float(cat.mean())
        goe_mean = float(goe.mean())
        # Retained only as a descriptive scale; no Gaussian/independence
        # inference is attached to this standardized difference.
        cat_sem = float(cat.std(ddof=0) / np.sqrt(len(cat)))
        goe_sem = float(goe.std(ddof=0) / np.sqrt(len(goe)))
        scale = float(np.hypot(cat_sem, goe_sem))
        standardized = abs(cat_mean - goe_mean) / scale if scale > 0 else 0.0
        rows.append(
            {
                "L": width,
                "catmap_mean": cat_mean,
                "goe_mean": goe_mean,
                "descriptive_standardized_difference": float(standardized),
            }
        )

    return {
        "N": prime,
        "K": subgroup_order,
        "a": eigenvalue,
        "matrix_dimension": int(dimension),
        "q_values_used": len(q_values),
        "goe_simulations": int(goe_simulations),
        "seed": int(seed),
        "rows": rows,
    }


def quick_smoke() -> dict[str, object]:
    spacing = spacing_design(199, 11, 139, [1, 7])
    if not np.isfinite(spacing["cdf_sup_distance_to_wigner_surmise"]):
        raise AssertionError("non-finite spacing diagnostic")
    toy = np.arange(16, dtype=float)
    counts = forward_window_count_variance(toy, [1, 2, 3])
    if any(value < 0.0 or not np.isfinite(value) for value in counts.values()):
        raise AssertionError("invalid forward-window variance")
    return {
        "producer": "computations/analysis/spectral_diagnostics.py",
        "mode": "quick-smoke",
        "spacing": spacing,
        "toy_forward_window_variance": counts,
        "verdict": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        choices=("quick", "spacing", "window"),
        nargs="?",
        default="quick",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.mode == "quick":
        result = quick_smoke()
    elif args.mode == "spacing":
        result = {
            "producer": "computations/analysis/spectral_diagnostics.py",
            "interpretation": (
                "Descriptive finite spacing comparison only; no IID-KS "
                "pass/fail semantics and no limiting-law claim."
            ),
            "reference": "GOE Wigner surmise P(s)=(pi s/2) exp(-pi s^2/4)",
            "designs": [
                spacing_design(3571, 17, 2469, list(range(1, 200, 5))),
                spacing_design(19489, 29, 4523, list(range(1, 300, 7))),
            ],
        }
    else:
        result = {
            "producer": "computations/analysis/spectral_diagnostics.py",
            "interpretation": (
                "Matched-GOE forward-window count variance; edge-truncated, "
                "not stationary Sigma^2(L), not a hypothesis test."
            ),
            "design": matched_window_design(
                19489,
                29,
                4523,
                list(range(1, 300, 12)),
                [1, 2, 3, 5, 8, 12],
                goe_simulations=60,
                seed=20260901,
            ),
        }

    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
