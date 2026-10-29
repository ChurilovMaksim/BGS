#!/usr/bin/env python3
"""Exact bucket checks for BGS-TRACE-140/141/142.

Recomputes the Haar momentum-phase form factor by occupation buckets at
the primes 5, 7 and 11, checks the error inequality, records the residue
27 mod 13, and checks the odd-symbol energy 9/125000.
A seeded Gaussian sample is a numerical check of the crossover constant,
not a proof of BGS-TRACE-142. A pass does not prove BGS-TRACE-005.
"""
from __future__ import annotations

import json
from fractions import Fraction
from itertools import product
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def r_coeff(k: int) -> Fraction:
    if k == 0:
        return Fraction(1)
    if abs(k) == 1:
        return Fraction(1, 2)
    if abs(k) == 7:
        return Fraction(-1, 2)
    if abs(k) in (6, 8):
        return Fraction(-1, 4)
    return Fraction(0)


def odd_energy() -> Fraction:
    """Energy of the part of r(q) cos(2 pi p - alpha_0) odd in p."""
    mom = Fraction(0)
    for k in range(-9, 10):
        rc = r_coeff(k)
        # coefficient of ell = +1 is rc * (-3 - 4i) / 1000
        re = rc * Fraction(-3, 1000)
        im = rc * Fraction(-4, 1000)
        mom += 2 * (re * re + im * im)  # ell = -1 has the same modulus
    # mom is the full ell=+-1 energy. Odd fraction is (4/5)^2 = 16/25.
    if mom != Fraction(9, 80000):
        raise SystemExit(f"momentum energy {mom}")
    odd = mom * Fraction(16, 25)
    if odd != Fraction(9, 125000):
        raise SystemExit(f"odd energy {odd}")
    return odd


def bucket(p: int, m: int, lam: int) -> float:
    """Haar expectation from the reduced phase Phi = sum s_t (x_t - lam x_{t+1})."""
    buckets: dict[tuple, complex] = {}
    coords = range(p)
    scale = 2j * np.pi / p
    for x in product(coords, repeat=m):
        ox = tuple(sorted(x))
        for s in product(coords, repeat=m):
            phase = 0
            for t in range(m):
                phase += s[t] * (x[t] - lam * x[(t + 1) % m])
            key = (ox, tuple(sorted(s)))
            buckets[key] = buckets.get(key, 0j) + np.exp(scale * (phase % p))
    return float(sum(abs(v) ** 2 for v in buckets.values()) / p ** (2 * m))


def falling(p: int, m: int) -> int:
    out = 1
    for i in range(m):
        out *= p - i
    return out


def fact(m: int) -> int:
    out = 1
    for i in range(1, m + 1):
        out *= i
    return out


def admissible(p: int, m: int, delta: int = 3) -> bool:
    """Theorem 1 needs only lambda not congruent to -1. The exponent m is unused."""
    del m
    lam = pow(delta, -1, p)
    return lam != p - 1


def main() -> None:
    odd = odd_energy()
    rows = []
    for p in (5, 7, 11, 13):
        for m in (2, 3):
            if not admissible(p, m):
                rows.append({"p": p, "m": m, "admissible": False, "reason": "lambda^t = 1"})
                continue
            lam = pow(3, -1, p)
            val = bucket(p, m, lam)
            main_term = m * falling(p, m) / p ** m if m >= 3 else 2.0
            # Theorem 1 compares m>=3 with m P/p^m and m=2 with 2.
            if m == 2:
                gap = abs(val - 2.0)
                bound = 20 / p
            else:
                gap = abs(val - main_term)
                bound = (fact(m) ** 2) * (1 + 2 * m * (m - 1)) / p
            if gap > bound + 1e-8:
                raise SystemExit(f"bound failed at p={p}, m={m}: {gap} > {bound}")
            rows.append({
                "p": p,
                "m": m,
                "admissible": True,
                "value": round(val, 10),
                "main": round(main_term, 10),
                "gap": round(gap, 10),
                "bound": round(bound, 10),
            })
            print(f"p={p} m={m} value={val:.6f} main={main_term:.6f} gap={gap:.6f} bound={bound:.6f}")

    # Seeded Gaussian sample. Not a proof of Theorem 3.
    rng = np.random.default_rng(20261029)
    p, m, v, samples = 29, 3, 0.4, 600
    lam = pow(3, -1, p)
    # Build U = D R M with Gaussian momentum phases and average |Tr|^2.
    kappa = (-pow(8, -1, p)) % p
    xs = np.arange(p)
    xx = xs[:, None]
    yy = xs[None, :]
    phase = (kappa * (3 * xx * xx - 2 * xx * yy + 3 * yy * yy)) % p
    M = np.exp(2j * np.pi * phase / p) / np.sqrt(p)
    F = np.exp(-2j * np.pi * np.outer(xs, xs) / p) / np.sqrt(p)
    acc = 0.0
    for _ in range(samples):
        D = np.exp(2j * np.pi * rng.random(p))
        xi = np.exp(1j * np.sqrt(v) * rng.normal(size=p))
        R = F.conj().T @ (xi[:, None] * F)
        U = (D[:, None] * R) @ M
        acc += abs(np.trace(np.linalg.matrix_power(U, m))) ** 2
    sample = acc / samples
    pred = m * (1 + np.exp(-v * m))
    print(f"gaussian sample={sample:.4f} prediction={pred:.4f}")

    payload = {
        "odd_energy": str(odd),
        "rows": rows,
        "gaussian_sample": {"p": p, "m": m, "v": v, "samples": samples, "mean": sample, "prediction": pred},
        "residue_t3": {"moduli": [5, 7, 11, 13], "value": 27, "residues": [27 % q for q in (5, 7, 11, 13)]},
    }
    out = ROOT / "evidence" / "executions" / "20261029" / "momentum-phase-cue"
    out.mkdir(parents=True, exist_ok=True)
    (out / "python_stdout.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print("odd_energy", odd)
    print("wrote", out / "python_stdout.json")


if __name__ == "__main__":
    main()
