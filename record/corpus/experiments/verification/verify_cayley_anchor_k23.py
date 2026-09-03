#!/usr/bin/env python3
"""Exact negative-control regression for the Cayley mixed-energy formula.

The fixed-K theorem says that the forced energy (K-1)(2K-5) holds only
outside a finite exceptional set E_K. This test prevents an accidental
promotion to a uniform formula: N=461, K=23 is an exact exceptional design.
"""
from __future__ import annotations

import json
from pathlib import Path

N = 461
K = 23
GENERATOR = 23
OUTPUT = Path(__file__).resolve().parents[2] / "results" / "verified" / "cayley_exception_k23.json"


def subgroup() -> list[int]:
    values: list[int] = []
    value = 1
    for _ in range(K):
        if value in values:
            raise AssertionError("generator order is smaller than K")
        values.append(value)
        value = value * GENERATOR % N
    if value != 1 or len(values) != K:
        raise AssertionError("generator does not have exact order K")
    return values


def main() -> None:
    H = subgroup()
    counts = [0] * N
    for u in H:
        if u == 1:
            continue
        for v in H:
            if v == 1 or v == u:
                continue
            d = (u - 1) * (v - 1) * pow((v - u) % N, N - 2, N) % N
            counts[d] += 1

    pair_count = sum(counts)
    energy = sum(c * c for c in counts)
    baseline = (K - 1) * (2 * K - 5)
    result = {
        "producer": "experiments/verification/verify_cayley_anchor_k23.py",
        "scope": "Exact finite negative control; establishes only that (N,K)=(461,23) is exceptional.",
        "N": N,
        "K": K,
        "subgroup_generator": GENERATOR,
        "pair_count": pair_count,
        "expected_pair_count": (K - 1) * (K - 2),
        "collision_energy": energy,
        "forced_baseline": baseline,
        "excess_collision_energy": energy - baseline,
        "max_nonzero_difference_multiplicity": max(counts[1:]),
        "is_exceptional": energy != baseline,
        "verdict": "PASS" if pair_count == 462 and energy == 1190 and baseline == 902 else "FAIL",
    }
    if result["verdict"] != "PASS":
        raise AssertionError(result)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
