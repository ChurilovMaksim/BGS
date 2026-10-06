#!/usr/bin/env python3
"""Finite checks for BGS-CUE-001; NOT an asymptotic proof.

Arithmetic: float64 quadrature and exact rational cumulants.
Inputs: N=2,3,7,20 for the CUE mean; N=2 and b=.01,.1,1 for
the tail bound; m,n=1..7 and N=1..14 for the fourth cumulant.
Optional --sample performs a seeded Haar diagnostic; the default does
not sample. No claim concerning the prescribed frozen map.
"""

from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from fractions import Fraction
from itertools import product
import math

import numpy as np
from scipy.integrate import quad


def rho2(n: int, angle: float) -> float:
    modes = np.arange(1, n)
    return float(4 * np.dot(n - modes, np.sin(modes * angle / 2) ** 2))


def check_mean() -> None:
    for n in (2, 3, 7, 20):
        integral = quad(
            lambda d: rho2(n, d) / (4 * math.sin(d / 2) ** 2) / math.pi,
            0, math.pi, epsabs=1e-9,
        )[0]
        exact = n * (n * n - 1) / 6
        assert abs(integral - exact) < 1e-8 * max(1, exact)


def check_tail_bound() -> None:
    # At N=2 both rho_3 and rho_4 vanish: exact variance = 2*I2 - M^2.
    n = 2
    for b in (.01, .1, 1.):
        kernel = lambda d: 1 / (4 * math.sin(d / 2) ** 2)
        m = quad(lambda d: kernel(d) * rho2(n, d) / math.pi,
                 b, math.pi)[0]
        i2 = quad(lambda d: kernel(d) ** 2 * rho2(n, d) / math.pi,
                  b, math.pi)[0]
        scaled = (2 * i2 - m * m) / n ** (16 / 3)
        r = b * n ** (4 / 3)
        upper = math.pi ** 3 / (96 * r) + n ** (-1 / 3) / 9
        assert 0 <= scaled <= upper


def exact_cumulant(n: int, m: int, k: int) -> Fraction:
    """DPP log-det fourth cumulant, independent of covariance shortcut."""
    frequencies = (m, -m, k, -k)
    ans = Fraction(0)
    for blocks in range(1, 5):
        for labels in product(range(blocks), repeat=4):
            if set(labels) != set(range(blocks)):
                continue
            partial = [0]
            for block in range(blocks):
                partial.append(
                    partial[-1] + sum(frequencies[j] for j in range(4)
                                      if labels[j] == block)
                )
            width = max(partial) - min(partial)
            ans += Fraction((-1) ** (blocks - 1), blocks) * max(n - width, 0)
    return ans


def check_cumulants() -> None:
    # Known fourth trace covariance; not needed for the energy theorem.
    for m in range(1, 8):
        for k in range(1, 8):
            for n in range(1, 15):
                expected = (2 * max(n - max(m, k), 0)
                            - max(n - m - k, 0)
                            - max(n - abs(m - k), 0))
                assert exact_cumulant(n, m, k) == expected


def check_levy_normalization() -> None:
    # Numerically integrates a regularized form of the stable exponent.
    # The omitted oscillatory tail after 1000 is O(1000**-5/2).
    cutoff = 1000.
    real = quad(lambda v: (math.cos(v) - 1) / v ** 2.5,
                0, cutoff, epsabs=1e-8, limit=1500)[0]
    imag = quad(lambda v: (math.sin(v) - v) / v ** 2.5,
                0, cutoff, epsabs=1e-8, limit=1500)[0]
    real -= 2 / (3 * cutoff ** 1.5)
    imag -= 2 / math.sqrt(cutoff)
    got = math.sqrt(2) / (24 * math.pi) * complex(real, imag)
    expected = -(1 + 1j) / (18 * math.sqrt(math.pi))
    assert abs(got - expected) < 1e-8


def sample_diagnostic() -> None:
    """Slowly converging empirical characteristic function, not an assertion."""
    rng = np.random.default_rng(20260925)
    limit = np.exp(-5 ** 1.5 * (1 + 1j) / (18 * np.sqrt(np.pi)))
    for n, draws in ((16, 3000), (32, 1800), (64, 800)):
        vals = []
        for _ in range(draws):
            z = ((rng.normal(size=(n, n))
                  + 1j * rng.normal(size=(n, n))) / np.sqrt(2))
            q, r = np.linalg.qr(z)
            phases = np.diag(r)
            q = q * (phases / np.abs(phases))[None, :]
            eig = np.linalg.eigvals(q)
            chord = np.abs(eig[:, None] - eig[None, :])
            np.fill_diagonal(chord, np.inf)
            energy = np.sum(chord ** -2) / n ** 3
            vals.append(n ** (1 / 3) * (energy - (1 - n ** -2) / 6))
        observed = np.mean(np.exp(5j * np.asarray(vals)))
        print(f"N={n}, draws={draws}, empirical CF={observed:.6f}, "
              f"limit={limit:.6f}, sampling SE <= {draws**-.5:.5f}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sample", action="store_true",
                        help="Print an exploratory Haar diagnostic; never assert convergence")
    args = parser.parse_args()
    check_mean()
    check_tail_bound()
    check_cumulants()
    check_levy_normalization()
    print("cue-singular-energy: PASS (finite normalizations; no limit theorem)")
    if args.sample:
        sample_diagnostic()


if __name__ == "__main__":
    main()
