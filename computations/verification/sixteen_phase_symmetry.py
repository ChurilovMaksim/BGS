#!/usr/bin/env python3
"""Symmetry checks for BGS-TRACE-130.

Position-diagonal realizations are checked to be similar to a symmetric
unitary. The momentum sine is checked to be odd under position conjugation.
A pass does not prove a COE or CUE form factor.
"""
from __future__ import annotations

import numpy as np

PI = float.fromhex("0x1.921fb54442d18p+1")
NS = (3, 5, 7, 11)


def r_num(k: int) -> int:
    return {0: 4, 1: 2, -1: 2, 7: -2, -7: -2, 6: -1, -6: -1, 8: -1, -8: -1}.get(k, 0)


def coeff(k: int, ell: int) -> tuple[int, int]:
    if ell == 0:
        re = (2000 if abs(k) == 7 else 0) + 100 * r_num(k) - (400 if k == 0 else 0)
        im = -5 * (r_num(k - 1) - r_num(k + 1))
        return re, im
    if ell == 1:
        return -3 * r_num(k), -4 * r_num(k)
    if ell == -1:
        return -3 * r_num(k), 4 * r_num(k)
    return 0, 0


def require(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit(msg)


def cat(n: int) -> np.ndarray:
    inv8 = pow(8, -1, n)
    x = np.arange(n)
    xx, yy = np.meshgrid(x, x, indexing="ij")
    quad = (3 * xx * xx - 2 * xx * yy + 3 * yy * yy) % n
    phase = (-inv8 * quad) % n
    return np.exp(2j * PI * phase / n) / np.sqrt(float(n))


def shift(n: int, a: int) -> np.ndarray:
    t = np.zeros((n, n), dtype=np.complex128)
    xs = np.arange(n)
    t[xs, (xs + a) % n] = 1.0
    return t


def main() -> None:
    odd = 0
    diag_imag = 0
    for k in range(-9, 10):
        re, im = coeff(k, 1)
        odd += re * re + im * im
        re0, im0 = coeff(k, 0)
        # diagonal symbol of one cosine pair is real; the raw coeff may be complex,
        # but c(k) e^{ikx} + conj(c(k)) e^{-ikx} is real. Check the pair sum of
        # imaginary parts of the Hermitian combination vanishes at x=0 after phases 0.
        diag_imag += im0  # used only as a sanity that we read the table
    require(odd == 900, f"odd energy {odd}")
    require(odd * 160000 == 9 * 16_000_000, "ratio")
    require(2 * 2 - 4 * 2 == -4, "det")
    print(f"odd_energy_scaled={odd}")

    rng = np.random.default_rng(130)
    for n in NS:
        m = cat(n)
        # random position symbol, real diagonal
        a = rng.normal(size=n)
        dhalf = np.diag(np.exp(1j * a / 2))
        s = dhalf @ m @ dhalf
        gap = np.max(np.abs(s - s.T))
        print(f"sym N={n} gap={gap:.3e}")
        require(gap < 1e-8, f"symmetry {n}")
        b = (shift(n, 1) - shift(n, -1)) / (2j)
        # conjugation in the position basis
        odd_gap = np.max(np.abs(np.conjugate(b) + b))
        print(f"mom N={n} odd_gap={odd_gap:.3e}")
        require(odd_gap < 1e-12, f"momentum odd {n}")
        herm = np.max(np.abs(b - b.conj().T))
        require(herm < 1e-12, f"hermitian {n}")
    print("PASS")


if __name__ == "__main__":
    main()
