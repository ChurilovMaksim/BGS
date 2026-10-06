#!/usr/bin/env python3
"""Descriptive finite spectral diagnostics for the arithmetic cat-map project.

The historical scripts used IID-KS and "number variance" language that was too
strong for their actual sampling scheme. This maintained implementation keeps
the useful finite computations but reports only descriptive quantities:

* an empirical CDF sup-distance to the GOE Wigner surmise;
* a matched GOE comparison for forward windows anchored at eigenvalues.

The spectral matrix is the *full complex Hermitian* matrix M + M^*. A
reconstruction-era implementation accidentally took its entrywise real part
before diagonalization; that changes the spectrum and is permanently guarded
against here.

Neither diagnostic is a hypothesis test or a proof of a limiting BGS law.
"""
from __future__ import annotations

import argparse
import json
import sys
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
from scipy.special import ndtr

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "computations" / "python"))

from bgs.finite_field import primitive_root  # noqa: E402
from bgs.jacobi import annihilator_indices, dlog_table  # noqa: E402

FLOAT_TOLERANCE = 1e-9


@dataclass(slots=True)
class SectorContext:
    """Precomputed character data for one finite spectral design."""

    prime: int
    subgroup_order: int
    eigenvalue: int
    character_indices: np.ndarray
    x_values: np.ndarray
    left: np.ndarray
    right: np.ndarray
    inverse_two: int


def unfold_polynomial(eigenvalues: np.ndarray, degree: int = 11) -> np.ndarray:
    """Polynomially unfold one finite spectrum.

    This is retained solely to reproduce the historical finite diagnostic.
    KNOWN DEFECT: this can reverse level order. Never use it for active
    diagnostics. Kept only for the explicit legacy-failure regression.
    """
    ordered = np.sort(np.asarray(eigenvalues, dtype=float))
    if len(ordered) < 4:
        raise ValueError("at least four eigenvalues are required for unfolding")
    degree = min(degree, len(ordered) - 2)
    empirical_cdf = np.arange(1, len(ordered) + 1) / (len(ordered) + 1)
    coefficients = np.polyfit(ordered, empirical_cdf, degree)
    return len(ordered) * np.polyval(coefficients, ordered)


def unfold_monotone(eigenvalues: np.ndarray, bandwidth_factor: float = 1.0,
                    edge_fraction: float = 0.0) -> np.ndarray:
    """Integrated Gaussian KDE, evaluated at sorted raw levels, never re-sorted.

    U(x) = sum_j Phi((x-lambda_j)/h), h = 1.06*s*n**(-1/5)*factor,
    where s is the sample standard deviation (ddof=1). Thus U'(x)>0
    for finite x and h>0 in exact arithmetic. This is a smoothed CDF,
    not the empirical CDF at its own nodes. Fit all levels before trimming
    floor(n*edge_fraction) levels at each edge. No universality is inferred.
    """
    raw = np.asarray(eigenvalues, dtype=float)
    if raw.ndim != 1 or len(raw) < 4 or not np.all(np.isfinite(raw)):
        raise ValueError("at least four finite one-dimensional eigenvalues required")
    if not np.isfinite(bandwidth_factor) or bandwidth_factor <= 0:
        raise ValueError("bandwidth_factor must be finite and positive")
    if not np.isfinite(edge_fraction) or not 0 <= edge_fraction < 0.5:
        raise ValueError("edge_fraction must be in [0, 0.5)")
    ordered = np.sort(raw)
    bandwidth = 1.06 * float(ordered.std(ddof=1)) * len(ordered)**(-0.2) * bandwidth_factor
    if not np.isfinite(bandwidth) or bandwidth <= 0:
        raise ValueError("spectrum must have positive finite spread")
    unfolded = ndtr((ordered[:, None] - ordered[None, :]) / bandwidth).sum(axis=1)
    if not np.all(np.isfinite(unfolded)) or np.any(np.diff(unfolded) < 0):
        raise ValueError("unfolding is nonfinite or reverses raw level order")
    trim = int(len(ordered) * edge_fraction)
    unfolded = unfolded[trim:len(ordered)-trim]
    if len(unfolded) < 4:
        raise ValueError("edge trimming must retain at least four levels")
    return unfolded


def normalized_gaps(eigenvalues: np.ndarray, bandwidth_factor: float = 1.0,
                    edge_fraction: float = 0.0) -> np.ndarray:
    unfolded = unfold_monotone(eigenvalues, bandwidth_factor, edge_fraction)
    gaps = np.diff(unfolded)
    if not np.all(np.isfinite(gaps)) or np.any(gaps < 0):
        raise ValueError("unfolded levels must preserve order")
    mean = float(gaps.mean())
    if not mean > 0.0:
        raise ValueError("non-positive mean unfolded gap")
    return gaps / mean


def goe_wigner_cdf(spacing: np.ndarray) -> np.ndarray:
    spacing = np.asarray(spacing, dtype=float)
    return 1.0 - np.exp(-np.pi * spacing**2 / 4.0)


def empirical_cdf_sup_distance(gaps: np.ndarray) -> float:
    """Supremum against the continuous Wigner-surmise CDF, both jump sides."""
    ordered = np.asarray(gaps, dtype=float)
    if ordered.ndim != 1 or len(ordered) == 0 or not np.all(np.isfinite(ordered)) or np.any(ordered < 0):
        raise ValueError("a nonempty one-dimensional finite nonnegative gap sample is required")
    ordered = np.sort(ordered)
    target = goe_wigner_cdf(ordered)
    right = np.arange(1, len(ordered) + 1) / len(ordered)
    left = np.arange(0, len(ordered)) / len(ordered)
    return float(max(np.max(right - target), np.max(target - left)))


def forward_window_count_variance(
    unfolded: np.ndarray, widths: list[int]
) -> dict[int, float]:
    """Historical edge-truncated forward-window statistic, named literally."""
    ordered = np.asarray(unfolded, dtype=float)
    if (ordered.ndim != 1 or len(ordered) < 2 or not np.all(np.isfinite(ordered))
            or np.any(np.diff(ordered) < 0)):
        raise ValueError("unfolded levels must be finite and already nondecreasing")
    if any(not np.isfinite(width) or width <= 0 for width in widths):
        raise ValueError("window widths must be finite and positive")
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


def build_sector_context(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
) -> SectorContext:
    """Precompute the odd annihilator sector for repeated q-values."""
    generator = primitive_root(prime)
    dlog = dlog_table(prime, generator)
    character_indices = annihilator_indices(
        prime, subgroup_order, eigenvalue, dlog
    )
    odd_sector = character_indices[character_indices % 2 == 1]
    if len(odd_sector) < 4:
        raise ValueError("odd character sector is too small for spectral diagnostics")

    x_values = np.arange(2, prime, dtype=np.int64)
    log_x = dlog[x_values]
    log_x_minus_one = dlog[(x_values - 1) % prime]
    left = np.exp(
        -2j * np.pi * np.outer(odd_sector, log_x) / (prime - 1)
    )
    right = np.exp(
        2j * np.pi * np.outer(odd_sector, log_x_minus_one) / (prime - 1)
    )
    return SectorContext(
        prime=prime,
        subgroup_order=subgroup_order,
        eigenvalue=eigenvalue,
        character_indices=odd_sector,
        x_values=x_values,
        left=left,
        right=right,
        inverse_two=pow(2, prime - 2, prime),
    )


def hermitian_matrix(context: SectorContext, q: int) -> np.ndarray:
    """Return the full complex Hermitian sector matrix at q."""
    prime = context.prime
    additive_phase = np.exp(
        2j * np.pi * (q * context.x_values % prime) / prime
    )
    jacobi = (context.left * additive_phase) @ context.right.T
    normalized = (
        np.exp(-2j * np.pi * (context.inverse_two * q % prime) / prime)
        * jacobi
        / (prime - 1)
    )
    hermitian = normalized + normalized.conj().T
    residual = float(np.max(np.abs(hermitian - hermitian.conj().T)))
    if residual > 5e-13:
        raise AssertionError(f"Hermitian residual too large: {residual}")
    return hermitian


def sector_eigenvalues(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    q: int,
) -> np.ndarray:
    """Convenience wrapper for a single q-value."""
    return np.linalg.eigvalsh(
        hermitian_matrix(build_sector_context(prime, subgroup_order, eigenvalue), q)
    )


def spacing_design(
    prime: int,
    subgroup_order: int,
    eigenvalue: int,
    q_values: list[int],
    bandwidth_factor: float = 1.0,
    edge_fraction: float = 0.0,
) -> dict[str, object]:
    context = build_sector_context(prime, subgroup_order, eigenvalue)
    if not q_values:
        raise ValueError("at least one q value is required")
    gaps: list[float] = []
    for q in q_values:
        spectrum = np.linalg.eigvalsh(hermitian_matrix(context, q))
        gaps.extend(normalized_gaps(spectrum, bandwidth_factor, edge_fraction).tolist())
    array = np.asarray(gaps, dtype=float)
    return {
        "N": prime,
        "K": subgroup_order,
        "a": eigenvalue,
        "matrix_dimension": int(len(context.character_indices)),
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
    bandwidth_factor: float = 1.0,
    edge_fraction: float = 0.0,
) -> dict[str, object]:
    if not q_values or goe_simulations < 1:
        raise ValueError("nonempty cat-map and GOE samples required")
    context = build_sector_context(prime, subgroup_order, eigenvalue)
    cat_samples = {width: [] for width in widths}
    dimension = len(context.character_indices)
    for q in q_values:
        spectrum = np.linalg.eigvalsh(hermitian_matrix(context, q))
        statistic = forward_window_count_variance(
            unfold_monotone(spectrum, bandwidth_factor, edge_fraction), widths
        )
        for width in widths:
            cat_samples[width].append(statistic[width])

    rng = np.random.default_rng(seed)
    goe_samples = {width: [] for width in widths}
    for _ in range(goe_simulations):
        random_matrix = rng.normal(size=(dimension, dimension))
        goe_matrix = (random_matrix + random_matrix.T) / 2.0
        statistic = forward_window_count_variance(
            unfold_monotone(np.linalg.eigvalsh(goe_matrix), bandwidth_factor, edge_fraction), widths
        )
        for width in widths:
            goe_samples[width].append(statistic[width])

    rows = []
    for width in widths:
        cat = np.asarray(cat_samples[width], dtype=float)
        goe = np.asarray(goe_samples[width], dtype=float)
        cat_mean = float(cat.mean())
        goe_mean = float(goe.mean())
        comparison = descriptive_difference(cat, goe)
        rows.append(
            {
                "L": width,
                "catmap_mean": cat_mean,
                "goe_mean": goe_mean,
                **comparison,
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


def descriptive_difference(cat: np.ndarray, goe: np.ndarray) -> dict[str, object]:
    """Descriptive SEM scaling only; q-values need not be independent.

    Use sample variance (ddof=1), requiring >=2 values in each group.
    Any zero denominator is undefined, including equal means. JSON null
    with an explicit status prevents absence of spread from implying agreement.
    """
    cat, goe = np.asarray(cat, dtype=float), np.asarray(goe, dtype=float)
    if any(a.ndim != 1 or not len(a) or not np.all(np.isfinite(a)) for a in (cat, goe)):
        raise ValueError("finite nonempty one-dimensional samples required")
    difference = abs(float(cat.mean()) - float(goe.mean()))
    status = "insufficient_replicates"
    scale = None
    standardized = None
    if min(len(cat), len(goe)) >= 2:
        scale = float(np.hypot(cat.std(ddof=1)/np.sqrt(len(cat)),
                               goe.std(ddof=1)/np.sqrt(len(goe))))
        status = "zero_spread" if scale == 0 else "defined"
        if scale > 0:
            standardized = difference / scale
    return {"absolute_mean_difference": difference,
            "descriptive_sem_scale": scale,
            "descriptive_standardized_difference": standardized,
            "standardized_difference_status": status}


def unfolding_metadata() -> dict[str, object]:
    return {"method": "integrated Gaussian KDE", "bandwidth": "1.06 * sample_std(ddof=1) * n**(-1/5)",
            "bandwidth_factor": 1.0, "edge_fraction": 0.0,
            "order_contract": "sort raw levels only; reject transformed inversions",
            "spread_contract": "ddof=1; fewer than two replicates or zero scale is null with status"}


def spacing_report() -> dict[str, object]:
    return {
        "producer": "computations/analysis/spectral_diagnostics.py",
        "producer_command": "python computations/analysis/spectral_diagnostics.py spacing",
        "unfolding": unfolding_metadata(),
        "interpretation": (
            "Descriptive finite spacing comparison only; not an IID KS test "
            "and not evidence for a limiting local law."
        ),
        "reference": "GOE Wigner surmise P(s)=(pi s/2) exp(-pi s^2/4)",
        "methodology_warning": (
            "Smoothed unfolding and pooled gaps induce dependence; no "
            "textbook IID-KS critical value or pass/fail label is justified."
        ),
        "matrix_convention": (
            "Eigenvalues are taken from the full complex Hermitian matrix "
            "M+M^*. Entrywise real projection is forbidden."
        ),
        "designs": [
            spacing_design(3571, 17, 2469, list(range(1, 200, 5))),
            spacing_design(19489, 29, 4523, list(range(1, 300, 7))),
        ],
    }


def window_report() -> dict[str, object]:
    return {
        "producer": "computations/analysis/spectral_diagnostics.py",
        "producer_command": "python computations/analysis/spectral_diagnostics.py window",
        "unfolding": unfolding_metadata(),
        "interpretation": (
            "Descriptive matched-GOE forward-window count variance; not "
            "stationary number variance Sigma^2(L) and not a hypothesis test."
        ),
        "methodology_warning": (
            "Windows start at eigenvalues and are edge-truncated. Cat-map and "
            "GOE samples use the same algorithm, so this is a matched diagnostic only."
        ),
        "matrix_convention": (
            "Cat-map eigenvalues are taken from the full complex Hermitian "
            "matrix M+M^*. Entrywise real projection is forbidden."
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


def _assert_close(actual: Any, expected: Any, path: str = "$") -> None:
    if isinstance(expected, dict):
        if not isinstance(actual, dict) or set(actual) != set(expected):
            raise AssertionError(f"{path}: dictionary keys differ")
        for key in expected:
            _assert_close(actual[key], expected[key], f"{path}.{key}")
        return
    if isinstance(expected, list):
        if not isinstance(actual, list) or len(actual) != len(expected):
            raise AssertionError(f"{path}: list shape differs")
        for index, (left, right) in enumerate(zip(actual, expected)):
            _assert_close(left, right, f"{path}[{index}]")
        return
    if isinstance(expected, float):
        if not np.isclose(float(actual), expected, rtol=FLOAT_TOLERANCE, atol=FLOAT_TOLERANCE):
            raise AssertionError(f"{path}: {actual!r} != {expected!r}")
        return
    if actual != expected:
        raise AssertionError(f"{path}: {actual!r} != {expected!r}")


def verify_committed_evidence() -> dict[str, object]:
    # Reproducing numbers alone cannot certify the transformation contract.
    subprocess.run([sys.executable, str(ROOT / "computations" / "verification" /
                                       "spectral_diagnostics_contracts.py")],
                   check=True, capture_output=True, text=True)
    spacing = spacing_report()
    window = window_report()
    spacing_expected = json.loads(
        (ROOT / "evidence" / "numerical" / "goe_spacing_monotone_v2.json").read_text(
            encoding="utf-8"
        )
    )
    window_expected = json.loads(
        (
            ROOT / "evidence" / "numerical" / "matched_window_count_variance_monotone_v2.json"
        ).read_text(encoding="utf-8")
    )
    _assert_close(spacing, spacing_expected, "$.spacing")
    _assert_close(window, window_expected, "$.window")
    return {
        "producer": "computations/analysis/spectral_diagnostics.py",
        "mode": "verify-corrected-descriptive-evidence",
        "interpretation": "Numerical regression only; historical polynomial outputs are superseded, not certified.",
        "verdict": "PASS",
    }


def quick_smoke() -> dict[str, object]:
    context = build_sector_context(199, 11, 139)
    full = hermitian_matrix(context, 1)
    correct = np.linalg.eigvalsh(full)
    real_projected = np.linalg.eigvalsh(full.real)
    bug_guard = float(np.max(np.abs(correct - real_projected)))
    if bug_guard < 1e-3:
        raise AssertionError("real-projection regression guard did not separate spectra")

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
        "real_projection_spectrum_difference_guard": bug_guard,
        "spacing": spacing,
        "toy_forward_window_variance": counts,
        "verdict": "PASS",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        choices=("quick", "spacing", "window", "verify"),
        nargs="?",
        default="quick",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.mode == "quick":
        result = quick_smoke()
    elif args.mode == "spacing":
        result = spacing_report()
    elif args.mode == "window":
        result = window_report()
    else:
        result = verify_committed_evidence()

    text = json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + "\n"
    if args.output is not None:
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
