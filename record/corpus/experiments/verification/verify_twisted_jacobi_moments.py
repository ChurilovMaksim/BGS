#!/usr/bin/env python3
"""Reproduce the audited twisted-Jacobi fourth-moment reference curves."""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))

from bgs.twisted_jacobi import build_closed_form, find_design_eigenvalue

REFERENCE = ROOT / "results" / "reference" / "r82"
OUTPUT = ROOT / "results" / "verified" / "twisted_jacobi_moments.json"


def reproduce_design(prime: int, subgroup_order: int) -> dict[str, object]:
    started = time.time()
    eigenvalue = find_design_eigenvalue(prime, subgroup_order)

    curve_path = REFERENCE / f"q_curve_N{prime}.npz"
    curve = np.load(curve_path)
    measured = dict(zip(curve["q"].astype(int).tolist(), curve["mu4"].tolist()))

    probes = [1, 2, 3, 5, 7]
    matching_sector: tuple[bool, int, int, int] | None = None

    for odd_parity in (True, False):
        for residue_class in range(subgroup_order):
            closed, dimension = build_closed_form(
                prime,
                subgroup_order,
                eigenvalue,
                residue_class,
                odd_parity,
                probes,
            )
            first_value = closed[probes[0]]["mu4"]
            scale_candidates = [
                q for q, value in measured.items() if abs(value - first_value) < 1e-8
            ]
            for scale in scale_candidates:
                if all(
                    abs(closed[q]["mu4"] - measured.get(scale * q % prime, np.nan))
                    < 1e-8
                    for q in probes
                ):
                    matching_sector = (
                        odd_parity,
                        residue_class,
                        scale,
                        dimension,
                    )
                    break
            if matching_sector is not None:
                break
        if matching_sector is not None:
            break

    if matching_sector is None:
        return {
            "N": prime,
            "K": subgroup_order,
            "match": False,
            "wall_seconds": round(time.time() - started, 1),
        }

    odd_parity, residue_class, scale, dimension = matching_sector
    inverse_scale = pow(scale, prime - 2, prime)
    all_q = sorted(measured)
    closed, _ = build_closed_form(
        prime,
        subgroup_order,
        eigenvalue,
        residue_class,
        odd_parity,
        [inverse_scale * q % prime for q in all_q],
    )
    deviations = np.array(
        [
            abs(closed[inverse_scale * q % prime]["mu4"] - measured[q])
            for q in all_q
        ]
    )

    return {
        "N": prime,
        "K": subgroup_order,
        "a": int(eigenvalue),
        "match": True,
        "odd_parity": bool(odd_parity),
        "residue_class": int(residue_class),
        "q_scale": int(scale),
        "matrix_dimension": int(dimension),
        "levels_checked": len(all_q),
        "max_abs_mu4_deviation": float(deviations.max()),
        "mean_abs_mu4_deviation": float(deviations.mean()),
        "wall_seconds": round(time.time() - started, 1),
    }


def main() -> None:
    rows = [reproduce_design(199, 11), reproduce_design(3571, 17)]
    legacy = json.loads(
        (REFERENCE / "closed_form.json").read_text(
            encoding="utf-8"
        )
    )

    verdict: dict[str, str] = {}
    for row in rows:
        reference = next(item for item in legacy["designs"] if item["N"] == row["N"])
        threshold = 10.0 * reference["max_abs_dev_mu4"]
        passed = row["match"] and row["max_abs_mu4_deviation"] <= threshold
        verdict[f"N={row['N']}"] = "PASS" if passed else "REGRESSION"

    result = {
        "producer": "experiments/verification/verify_twisted_jacobi_moments.py",
        "scope": "finite reproducibility regression against preserved R82 inputs",
        "interpretation": "implementation anchor only; not an asymptotic theorem",
        "designs": rows,
        "legacy_R82_reference": legacy["designs"],
        "verdict": verdict,
    }
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
