"""Finite normalization check for BGS-TRACE-008 and BGS-RES-006.

Inputs: deterministic diagonal spectra at N=10, 11, 20, 21; s=1.3, 2.5.
Arithmetic: Python double-precision complex arithmetic. The 700-term Abel
sum has a geometric tail bounded by q**701/(1-q), since |p_m|/N <= 1.
Scope: checks separate finite matrix and Poisson-kernel representations,
and the even-dimensional CUE *expected* Gram benchmark. Does not certify
an asymptotic limit, transcendence, model realization, or BGS universality.
"""

from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import cmath
import math


def phases(n: int) -> list[float]:
    half = n // 2
    phi = math.acos(-1 / 3) if n % 2 else 2 * math.acos(
        math.sqrt(1 / 3 - 1 / (3 * n * n))
    )
    vals = [2 * math.pi * j / half for j in range(half)]
    vals += [(2 * math.pi * j + phi) / half for j in range(half)]
    if n % 2:
        vals.append(0.21374)  # only a finite normalization check
    return vals


def check(n: int, s: float) -> None:
    angles = phases(n)
    assert len(angles) == n
    ordered = sorted(angles)
    gaps = [
        (ordered[(j + 1) % n] - ordered[j]) % (2 * math.pi) * n / (2 * math.pi)
        for j in range(n)
    ]
    half = n // 2
    phi = angles[half] * half
    base_gaps = (n * phi / (2 * math.pi * half),
                 n * (2 * math.pi - phi) / (2 * math.pi * half))
    expected_unchanged = n if n % 2 == 0 else n - 2
    assert sum(min(abs(g - h) for h in base_gaps) < 2e-12 for g in gaps) \
        >= expected_unchanged
    eig = [cmath.exp(1j * x) for x in angles]
    powers = [n + 0j]
    cur = [1 + 0j] * n
    q = math.exp(-2 * s / n)
    abel = 0.0
    # Powers are obtained by repeated multiplication, not by the clock formula.
    for m in range(1, 701):
        cur = [v * z for v, z in zip(cur, eig)]
        trace = sum(cur)
        if m < n:
            powers.append(trace)
        abel += q**m * abs(trace) ** 2 / (n * n)

    # Explicit Toeplitz matrix: independent of the lag-count derivation.
    gram = sum(
        abs(powers[abs(a - b)] / n) ** 2 for a in range(n) for b in range(n)
    ) / n
    lag_gram = 1 + 2 * sum(
        (n - m) * abs(powers[m]) ** 2 for m in range(1, n)
    ) / n**3
    assert abs(gram - lag_gram) < 2e-12
    if n % 2 == 0:
        cue_expected_gram = 4 / 3 - 1 / (3 * n * n)
        assert abs(gram - cue_expected_gram) < 2e-12
        x = math.exp(-s)
        phi = 2 * math.acos(math.sqrt(1 / 3 - 1 / (3 * n * n)))
        two_clock_abel = 0.5 * (
            x / (1 - x)
            + ((x * cmath.exp(1j * phi)) / (1 - x * cmath.exp(1j * phi))).real
        )
        assert abs(abel - two_clock_abel) < 2e-12

    # Pair Poisson kernel is computed directly from the eigenphase gaps.
    poisson = sum(
        (1 - q * q) / (1 - 2 * q * math.cos(a - b) + q * q)
        for a in angles for b in angles
    ) / n**2
    assert abs(abel - (poisson - 1) / 2) < 3e-11

    hyper = n * math.sinh(s / n)
    resolvent = sum(
        1 / (n * n * math.sin((a - b) / 2) ** 2 + hyper**2)
        for a in angles for b in angles
    ) / n
    assert abs(poisson - n * math.sinh(s / n) * math.cosh(s / n) * resolvent) < 3e-11


def main() -> None:
    for n in (10, 11, 20, 21):
        for s in (1.3, 2.5):
            check(n, s)
    print("gram-resolvent-normalization: PASS (8 finite cases; no asymptotic claim)")


if __name__ == "__main__":
    main()
