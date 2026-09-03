#!/usr/bin/env python3
"""Exact audit of the historical Julia sol6_closed_form.jl experiment.

The historical filename suggested a closed form. Its own preserved output
contains counterexamples. This replacement keeps the exact enumeration but
makes the p-dependence explicit and treats the old formula only as a falsifier.
"""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))
from bgs.finite_field import primitive_root  # noqa: E402


def subgroup(p: int, k: int) -> list[int]:
    if (p - 1) % k:
        raise ValueError("k must divide p-1")
    a = pow(primitive_root(p), (p - 1) // k, p)
    h = 1
    out: list[int] = []
    for _ in range(k):
        out.append(h)
        h = h * a % p
    if h != 1 or len(set(out)) != k:
        raise AssertionError("failed to construct exact-order subgroup")
    return out


def sol6_count(p: int, k: int) -> int:
    """Count h1+h3+h5=h2+h4+h6 and reciprocal-sum equality exactly."""
    H = subgroup(p, k)
    inv = {h: pow(h, p - 2, p) for h in H}
    triples: Counter[tuple[int, int]] = Counter()
    for h1 in H:
        for h3 in H:
            s13 = (h1 + h3) % p
            t13 = (inv[h1] + inv[h3]) % p
            for h5 in H:
                triples[((s13 + h5) % p, (t13 + inv[h5]) % p)] += 1
    return sum(m * m for m in triples.values())


def historical_prediction(k: int) -> int:
    return 15 * k**3 - 5 * k**2 - 170 * k


def verify() -> None:
    anchors = {
        (127, 6): 2040,
        (181, 12): 23160,
        (127, 18): 82800,
        (181, 30): 417000,
        (211, 30): 422400,
        (181, 36): 719640,
        (101, 4): 400,
        (113, 8): 5120,
        (181, 20): 103400,
        (353, 22): 138820,
    }
    for design, want in anchors.items():
        got = sol6_count(*design)
        if got != want:
            raise AssertionError(f"{design}: got {got}, want preserved Julia {want}")
    if sol6_count(211, 30) == historical_prediction(30):
        raise AssertionError("historical closed form unexpectedly survived falsifier")
    print("PASS sol6 exact enumeration; historical closed form FALSIFIED")


def main() -> None:
    verify()
    for p, k in [(127, 6), (181, 12), (127, 18), (181, 30), (211, 30), (181, 36)]:
        got = sol6_count(p, k)
        print(f"p={p:4d} k={k:2d} sol6={got:7d} historical_pred={historical_prediction(k):7d}")


if __name__ == "__main__":
    main()
