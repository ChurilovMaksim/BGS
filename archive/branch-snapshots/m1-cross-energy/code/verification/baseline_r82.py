"""Reproduce the load-bearing R82 twisted-Jacobi fourth-moment baseline.

This check compares the current closed-form kernel against the preserved R82
q-curve inputs at N=199 and N=3571. It is a reproducibility check, not a proof
of a limiting spectral law.
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from code.math.twisted_jacobi import (  # noqa: E402
    build_closed_form,
    find_design_eigenvalue,
)

LEGACY_DIR = os.path.join(ROOT, "inputs", "r82-legacy", "theorems", "I_torus_rigidity")
LEGACY_CF = os.path.join(
    ROOT,
    "inputs",
    "r82-legacy",
    "theorems",
    "II_twisted_jacobi",
    "closed_form.json",
)
OUT = os.path.join(ROOT, "results", "verified", "baseline_r82.json")


def reproduce_one(N: int, K: int) -> dict:
    t0 = time.time()
    a = find_design_eigenvalue(N, K)
    q_path = os.path.join(LEGACY_DIR, f"q_curve_N{N}.npz")
    if not os.path.exists(q_path):
        raise FileNotFoundError(q_path)

    data = np.load(q_path)
    q_measured = data["q"].astype(int)
    mu4_measured = data["mu4"]
    measured = dict(zip(q_measured.tolist(), mu4_measured.tolist()))

    probes = [1, 2, 3, 5, 7]
    best = None
    for parity_odd in (True, False):
        for k0 in range(K):
            closed, m = build_closed_form(N, K, a, k0, parity_odd, probes)
            expected_m = len(
                [
                    1
                    for k in range(N - 1)
                    if k % K == k0 % K and (k % 2 == 1) == parity_odd
                ]
            )
            if m != expected_m:
                continue
            v0 = closed[probes[0]]["mu4"]
            candidates = [q for q, value in measured.items() if abs(value - v0) < 1e-8]
            for scale in candidates:
                if all(
                    abs(closed[p]["mu4"] - measured.get((scale * p) % N, np.nan)) < 1e-8
                    for p in probes
                ):
                    best = (parity_odd, k0, scale, m)
                    break
            if best:
                break
        if best:
            break

    if best is None:
        return {"N": N, "K": K, "match": False, "wall_s": round(time.time() - t0, 1)}

    parity_odd, k0, scale, m = best
    all_q = sorted(measured)
    inv_scale = pow(scale, N - 2, N)
    closed, _ = build_closed_form(
        N, K, a, k0, parity_odd, [(inv_scale * q) % N for q in all_q]
    )
    deviations = np.array(
        [abs(closed[(inv_scale * q) % N]["mu4"] - measured[q]) for q in all_q]
    )
    return {
        "N": N,
        "K": K,
        "a": int(a),
        "match": True,
        "parity_odd": bool(parity_odd),
        "k0": int(k0),
        "scale_c": int(scale),
        "m_plus": int(m),
        "levels_checked": len(all_q),
        "max_abs_dev_mu4": float(deviations.max()),
        "mean_abs_dev_mu4": float(deviations.mean()),
        "wall_s": round(time.time() - t0, 1),
    }


def main() -> None:
    out = {
        "script": "code/verification/baseline_r82.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "phase": "canonical-rebuild/R82",
        "designs": [],
    }
    for N, K in ((199, 11), (3571, 17)):
        try:
            row = reproduce_one(N, K)
        except Exception as exc:  # explicit failure is recorded in the result
            row = {"N": N, "K": K, "match": False, "error": repr(exc)}
        out["designs"].append(row)
        print(f"N={N} K={K} -> {row}", flush=True)

    if os.path.exists(LEGACY_CF):
        with open(LEGACY_CF, encoding="utf-8") as handle:
            legacy = json.load(handle)
        out["legacy_R82_reference"] = legacy.get("designs", [])

    out["verdict"] = {}
    for row in out["designs"]:
        key = f"N={row.get('N')}"
        if not row.get("match"):
            out["verdict"][key] = "FAIL"
            continue
        reference = next(
            (r for r in out.get("legacy_R82_reference", []) if r.get("N") == row["N"]),
            None,
        )
        if reference is None:
            out["verdict"][key] = "NO_REFERENCE"
        elif row["max_abs_dev_mu4"] <= 10.0 * reference.get("max_abs_dev_mu4", 1.0):
            out["verdict"][key] = "PASS"
        else:
            out["verdict"][key] = "REGRESSION"

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
    print("artifact ->", OUT, flush=True)
    print("verdict ->", out["verdict"], flush=True)


if __name__ == "__main__":
    main()
