#!/usr/bin/env python3
"""Finite arithmetic and independent matrix controls for the harmonic law.

Exact integer checks and floating matrix checks are reported separately.
Neither verifies the asymptotic phase argument or microscopic BGS.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import platform
import time

import numpy as np

ROOT = Path(__file__).resolve().parents[2]


def pell(k: int) -> tuple[int, int]:
    if k < 0:
        raise ValueError("nonnegative Pell index required")
    n, f = 1, 0
    for _ in range(k):
        n, f = n + 2*f, n + f
    return n, f


def prime(k: int) -> bool:
    return k >= 2 and all(k % j for j in range(2, math.isqrt(k)+1))


def design(k: int) -> tuple[int, int, int, int]:
    if k < 3 or not prime(k):
        raise ValueError("odd prime K required")
    n, f = pell(k)
    s = pow(f, -1, n)
    h = (3+2*s) % n
    assert n*n-2*f*f == -1
    assert pow(h, k, n) == 1
    assert all(math.gcd(pow(h, j, n)-1, n) == 1 for j in range(1, k))
    assert all(math.gcd(pow(h, j, n)+1, n) == 1 for j in range(k))
    return n, f, s, h


def signed(d: int, k: int) -> int:
    return (d + k//2) % k - k//2


def pell_phase(d: int, k: int) -> int:
    delta = signed(d, k)
    return (-2 if delta >= 0 else 2)*pell(2*abs(delta))[1]


def pairings(positions: tuple[int, ...]):
    if not positions:
        yield ()
        return
    first = positions[0]
    for j in range(1, len(positions)):
        for tail in pairings(positions[1:j]+positions[j+1:]):
            yield ((first, positions[j]),)+tail


def edges(pi: tuple[tuple[int, int], ...]) -> tuple[tuple[int, int], ...]:
    return tuple((i, j) for i in range(len(pi)) for j in range(i+1, len(pi))
                 if pi[i][0] < pi[j][0] < pi[i][1] < pi[j][1])


def exact_phase_checks() -> dict:
    count = 0
    for k in (3, 5, 7, 11, 19, 31, 61, 127):
        n, f, s, h = design(k)
        for d in range(k):
            assert (-f*(pow(h, d, n)-pow(h, -d, n))-pell_phase(d, k)) % n == 0
        for a in range(1, 13):
            if math.gcd(a, n) == 1:
                # S_(a^-1) sends the real harmonic index to (a^2*q0,1).
                u = pow(a, -1, n)
                assert (a*(-f)*pow(u, -1, n)) % n == (-a*a*f) % n
                assert u*a % n == 1
        if k != 11:
            continue
        for r in range(1, 6):
            label_sets = (tuple(0 for _ in range(r)),
                          tuple(j % k for j in range(r)),
                          tuple(j*j % k for j in range(r)))
            for pi in pairings(tuple(range(2*r))):
                cross = edges(pi)
                for sig in itertools.product((-1, 1), repeat=r):
                    for labels in label_sets:
                        for a in (1, 2):
                            v = [None]*(2*r)
                            for j, (left, right) in enumerate(pi):
                                x = (sig[j]*a*(-f)*pow(h, -labels[j], n)) % n
                                y = (sig[j]*a*pow(h, labels[j], n)) % n
                                v[left], v[right] = (x, y), (-x % n, -y % n)
                            # Direct ordered Weyl multiplication, no crossing formula.
                            total_x = total_y = phase = 0
                            for x, y in v:
                                phase += (total_x*y-total_y*x)*pow(2, -1, n)
                                total_x, total_y = (total_x+x) % n, (total_y+y) % n
                            assert total_x == total_y == 0
                            predicted = a*a*sum(
                                sig[i]*sig[j]*pell_phase(labels[j]-labels[i], k)
                                for i, j in cross)
                            assert (phase-predicted) % n == 0
                            count += 1
    histogram = Counter(len(edges(pi)) for pi in pairings(tuple(range(6))))
    assert histogram == {0: 5, 1: 6, 2: 3, 3: 1}
    return {"oriented_word_identities": count,
            "K_values": [3, 5, 7, 11, 19, 31, 61, 127],
            "six_position_crossing_histogram": dict(sorted(histogram.items()))}


def exact_geometry_checks() -> dict:
    tests = 0
    for m in (5, 7, 11, 19, 31, 51):
        for radius in range((m+1)//2):
            allowed = [x for x in range(m) if min(x, m-x) <= radius]
            direct = sum(min((x-y) % m, (y-x) % m) <= radius
                         for x in allowed for y in allowed)
            wrap = max(0, 3*radius-m+1)
            expected = 3*radius*radius+3*radius+1+wrap*(wrap+1)
            assert direct == expected
            tests += 1
    rho = Fraction(1, 2)
    triangle = 3*rho*rho/4 + max(Fraction(0), 3*rho/2-1)**2
    m6 = 5+6*rho+3*rho*rho+triangle
    q_m6 = 5+6*rho+3*rho*rho+rho**3
    assert triangle == Fraction(3, 16)
    assert m6 == Fraction(143, 16) and q_m6 == Fraction(71, 8)
    # Rational symbolic checks of both pieces and the strict discrepancy.
    for j in range(1, 120):
        rho = Fraction(j, 120)
        triangle = 3*rho*rho/4 + max(Fraction(0), 3*rho/2-1)**2
        discrepancy = (rho*rho*(Fraction(3, 4)-rho) if rho <= Fraction(2, 3)
                       else (1-rho)**3)
        assert triangle-rho**3 == discrepancy > 0
        beta = (1-rho)/2
        assert 2*(1-rho*rho) == 8*beta*(1-beta)
    return {"integer_circle_triangle_designs": tests,
            "rational_interior_parameters": 119,
            "beta_quarter_sixth_moment": str(m6),
            "independent_crossing_sixth_moment": str(q_m6)}


def orbit_basis(k: int, sector: int) -> np.ndarray:
    n, _f, _s, h = design(k)
    dim = (n-1)//(2*k)
    basis = np.zeros((n, dim), dtype=complex)
    occupied = set()
    column = 0
    for rep in range(1, n):
        if rep in occupied:
            continue
        for j in range(k):
            x = rep*pow(h, j, n) % n
            z = np.exp(-2j*np.pi*sector*j/k)/math.sqrt(2*k)
            basis[x, column], basis[-x % n, column] = z, -z
            occupied.update((x, -x % n))
        column += 1
    assert column == dim
    assert np.max(abs(basis.conj().T@basis-np.eye(dim))) < 1e-12
    return basis


def chirp(n: int, t: int) -> np.ndarray:
    return np.array([np.exp(2j*np.pi*((t*x*x*pow(2, -1, n)) % n)/n)
                     for x in range(n)])


def dilation_rows(matrix: np.ndarray, u: int) -> np.ndarray:
    n = len(matrix)
    return matrix[(pow(u, -1, n)*np.arange(n)) % n]


def physical_basis(k: int, sector: int) -> np.ndarray:
    n, _f, s, _h = design(k)
    base = dilation_rows(orbit_basis(k, sector), pow(2, -1, n))
    # V = C_(s^-1) S_(1/2) F_N C_(2s), then V S_(1/2).
    base = chirp(n, 2*s)[:, None]*base
    x = np.arange(n)
    fourier = np.exp(2j*np.pi*((x[:, None]*x[None, :]) % n)/n)/math.sqrt(n)
    base = fourier@base
    base = dilation_rows(base, pow(2, -1, n))
    return chirp(n, pow(s, -1, n))[:, None]*base


def compressed_weyl(k: int, sector: int, a: int, squared: bool = True) -> np.ndarray:
    n, f, _s, _h = design(k)
    base = orbit_basis(k, sector)
    q = (-f*(a*a if squared else a)) % n
    x = np.arange(n)
    phase = np.exp(2j*np.pi*((q*(x-pow(2, -1, n))) % n)/n)
    action = phase[:, None]*base[(x-1) % n]
    matrix = base.conj().T@action
    return math.sqrt(k/2)*(matrix+matrix.conj().T)


def matrix_checks() -> dict:
    results, wrong_gaps = [], []
    for k in (3, 5, 7):
        n = pell(k)[0]
        for sector in sorted({0, 1, k-1}):
            base = physical_basis(k, sector)
            for a in (1, 2, 3, 4):
                if math.gcd(a, n) != 1:
                    continue
                potential = 2*np.cos(2*np.pi*a*np.arange(n)/n)
                physical = math.sqrt(k/2)*(base.conj().T@(potential[:, None]*base))
                actual = np.linalg.eigvalsh(physical)
                correct = np.linalg.eigvalsh(compressed_weyl(k, sector, a))
                error = float(np.max(abs(actual-correct)))
                assert error < 2e-10
                if a > 1:
                    wrong = np.linalg.eigvalsh(compressed_weyl(k, sector, a, False))
                    wrong_gaps.append(float(np.max(abs(actual-wrong))))
                results.append({"K": k, "N": n, "sector": sector, "harmonic": a,
                                "dimension": len(actual), "spectral_error": error})
    assert max(wrong_gaps) > 0.1
    return {"scope": "floating physical-potential spectrum versus squared-parameter Weyl block",
            "checks": results, "max_correct_error": max(x["spectral_error"] for x in results),
            "max_linear_parameter_negative_control_error": max(wrong_gaps)}


def quadratic_sum_checks() -> dict:
    tests, worst = 0, 0.0
    for exponent in (6, 8, 10, 12, 14):
        u = 2.0**(-exponent)
        h = math.floor(1/(4*math.sqrt(u)))
        if h < 2:
            continue
        for factor in (1, 4, 16):
            length = factor*math.ceil(1/math.sqrt(u))
            a = np.arange(1, length+1, dtype=float)
            observed = abs(np.mean(np.exp(2j*np.pi*u*a*a)))**2
            bound = 2/h + 4/(h*length)*sum(
                min(length, 1/(4*u*j)) for j in range(1, h))
            assert observed <= bound+1e-12
            tests += 1
            worst = max(worst, float(observed/max(bound, 1e-300)))
    return {"scope": "floating checks of the finite differencing inequality, rational phases",
            "designs": tests, "maximum_observed_to_bound_ratio": worst}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    start = time.monotonic()
    output = {
        "status": "PASS",
        "scope": "Exact finite algebra plus floating independent matrix regressions; no asymptotic or BGS certification",
        "software": {"python": platform.python_version(), "numpy": np.__version__},
        "exact_phase": exact_phase_checks(),
        "exact_geometry": exact_geometry_checks(),
        "matrix": matrix_checks(),
        "quadratic_sum": quadratic_sum_checks(),
    }
    paths = [Path(__file__), ROOT/"mathematics/pell_harmonic_transition.md"]
    output["source_sha256"] = {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in paths}
    output["runtime_seconds"] = time.monotonic()-start
    text = json.dumps(output, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
