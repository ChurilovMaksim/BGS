"""Finite high-precision checks; not an asymptotic proof or formal certificate."""

import json
import random
from fractions import Fraction
from pathlib import Path

import mpmath as mp


mp.mp.dps = 60


def require(condition, details="finite check failed"):
    if not condition:
        raise AssertionError(details)


def mpr(x):
    if isinstance(x, Fraction):
        return mp.mpf(x.numerator) / x.denominator
    return mp.mpf(x)


def q(s, x):
    if not x:
        return s / mp.sinh(s) ** 2
    return s**3 / mp.sinh(s) ** 2 * (mp.sin(mp.pi * x) / (mp.pi * x)) ** 2 / (
        s**2 + mp.pi**2 * x**2
    )


def qper(s, N, x):
    # Independently sum partial fractions using the elementary cotangent sum.
    x %= N
    if abs(x - mp.nint(x)) < mp.mpf("1e-50"):
        return s / mp.sinh(s) ** 2 if abs(x) < mp.mpf("1e-50") else mp.mpf(0)
    fper = mp.sinh(2 * s / N) / (
        N * (mp.cosh(2 * s / N) - mp.cos(2 * mp.pi * x / N))
    )
    return mp.sin(mp.pi * x) ** 2 / mp.sinh(s) ** 2 * (
        s / (N**2 * mp.sin(mp.pi * x / N) ** 2) - fper
    )


def hhat(s, u):
    u = abs(u)
    if u >= 1:
        return mp.mpf(0)
    return (mp.sinh(2 * s * (1 - u)) - 2 * s * (1 - u)) / (2 * mp.sinh(s) ** 2)


def check(theta, s):
    N = len(theta)
    theta = list(map(mpr, theta))
    radial = mp.exp(-2 * s / N)
    lhs = mp.mpf(0)
    for a in theta:
        for b in theta:
            z = radial * mp.exp(2j * mp.pi * (a - b))
            lhs += (z / (1 - z)).real / N**2
    delta = lhs - 1 / mp.expm1(2 * s)
    spectral = mp.mpf(0)
    for m in range(1, N):
        trace = sum(mp.exp(2j * mp.pi * m * a) for a in theta)
        spectral += hhat(s, mp.mpf(m) / N) * abs(trace) ** 2 / N**2
    positional = sum(
        qper(s, N, N * (theta[j] - theta[k]))
        for j in range(N)
        for k in range(N)
        if j != k
    ) / (2 * N)
    err = abs(delta - spectral - positional)
    require(err < mp.mpf("1e-45"), (N, s, err))
    require(delta >= -mp.mpf("1e-45"), (N, s, delta))
    return err


def main():
    rng = random.Random(20261016)
    maxerr = mp.mpf(0)
    finite = 0
    ss = list(map(mp.mpf, ["0.15", "1", "3"]))
    for N in [1, 2, 3, 4, 7, 8, 9, 12]:
        spectra = [
            [Fraction(j, N) for j in range(N)],
            [Fraction(1, 7)] * N,
            [Fraction(j % 2, 3) for j in range(N)],
            [Fraction(rng.randrange(997), 997) for _ in range(N)],
            [Fraction(j + 1, N + 1) for j in range(N)],
            [Fraction(j, N) + Fraction(rng.randrange(-5, 6), 997 * N) for j in range(N)],
        ]
        for theta in spectra:
            for s in ss:
                maxerr = max(maxerr, check(theta, s))
                finite += 1

    ftmax = mp.mpf(0)
    ftcases = 0
    for s in ss:
        for u in map(mp.mpf, ["0", "0.2", "0.75", "1", "1.2", "2"]):
            cuts = sorted(set([-mp.mpf(1), mp.mpf(0), mp.mpf(1)] + ([u] if u < 1 else [])))
            qhat = s**2 / mp.sinh(s)**2 * mp.quad(
                lambda t: (1-abs(t)) * mp.exp(-2*s*abs(u-t)), cuts
            )
            err = abs(mp.exp(-2*s*abs(u)) - qhat - hhat(s, u))
            require(err < mp.mpf("1e-50"), (s, u, err))
            ftmax = max(ftmax, err)
            ftcases += 1

    tailcases = 0
    tailmax = mp.mpf(0)
    K = 1000
    for s in ss:
        for N in [1, 2, 7, 12]:
            x = mp.mpf("0.371") * N
            finite_qsum = sum(q(s, x+l*N) for l in range(-K, K+1))
            positive_tail = qper(s,N,x) - finite_qsum
            bound = 2 * s**3 / (3*mp.pi**4*mp.sinh(s)**2*N**4*(K-1)**3)
            require(positive_tail >= -mp.mpf("1e-50"), (s,N,x,positive_tail))
            require(positive_tail <= bound, (s,N,x,positive_tail,bound))
            tailmax = max(tailmax, positive_tail/bound)
            tailcases += 1

    report = {
        "arithmetic": "mpmath 60 decimal digits; numerical checks only",
        "finite_identity_cases": finite,
        "max_finite_identity_absolute_error": mp.nstr(maxerr, 12),
        "fourier_compact_convolution_quadratures": ftcases,
        "max_fourier_absolute_error": mp.nstr(ftmax, 12),
        "direct_periodization_checks": tailcases,
        "periodization_cutoff": K,
        "largest_observed_tail_to_analytic_upper_bound_ratio": mp.nstr(tailmax, 12),
        "includes": ["N=1", "even and odd N", "repeated eigenvalues", "clock", "deleted clock", "rational random phases"],
        "nonclaims": ["no asymptotic numerical proof", "no proof of physical Abel limit", "no BGS universality", "no claim of optimal rate"],
    }
    Path(__file__).with_name("receipt.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
