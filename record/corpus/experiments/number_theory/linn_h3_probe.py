#!/usr/bin/env python3
"""Deterministic replacement for the historical Julia Linn H^3 probe.

This is a numerical discriminator only. It does not promote the historical
"Linn transfer" heuristic to a theorem. Coefficients are seeded so runs are
reproducible, unlike the unseeded Julia script.
"""
from __future__ import annotations

import cmath
import random
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src" / "python"))
from bgs.finite_field import primitive_root  # noqa: E402


def subgroup(p: int, k: int) -> list[int]:
    if (p - 1) % k:
        raise ValueError("k must divide p-1")
    alpha = pow(primitive_root(p), (p - 1) // k, p)
    out, h = [], 1
    for _ in range(k):
        out.append(h)
        h = h * alpha % p
    return out


def linn_h3_sum(p: int, H: list[int], coeffs: tuple[int, ...]) -> complex:
    a, b, c, d, e, f = coeffs
    total = 0j
    scale = 2j * cmath.pi / p
    for u1 in H:
        for u2 in H:
            for u3 in H:
                phase = (a*u1 + b*u2 + c*u3 + d*u1*u2 + e*u2*u3 + f*u1*u2*u3) % p
                total += cmath.exp(scale * phase)
    return total


def main(seed: int = 20260903) -> None:
    rng = random.Random(seed)
    designs = [(101,5),(101,10),(211,7),(401,8),(401,16),(401,20),
               (1009,4),(1009,8),(2003,7),(2003,11),(3571,17),(3571,34)]
    print(f"deterministic Linn H^3 numerical probe; seed={seed}")
    for p, k in designs:
        H = subgroup(p, k)
        coeffs = tuple(rng.randrange(1, p) for _ in range(6))
        mag = abs(linn_h3_sum(p, H, coeffs))
        print(f"p={p:4d} k={k:2d} |sum|={mag:12.6f}  /k^(2/3)={mag/k**(2/3):9.5f}")


if __name__ == "__main__":
    main()
