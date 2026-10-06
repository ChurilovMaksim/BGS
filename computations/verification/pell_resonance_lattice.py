#!/usr/bin/env python3
"""Finite exact lattice/geometry checks and floating physical-matrix controls.

No finite run establishes growing-time phase cancellation, BGS, or priority.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from collections import Counter
from fractions import Fraction
from itertools import combinations, product
import json
import math
from pathlib import Path
import platform
import time
import numpy as np
from pell_harmonic_transition import pell, chirp, dilation_rows


def matrix(k):
    a = [[0]*k for _ in range(k)]
    for j in range(k):
        a[j][j] += 1
        a[j][(j-1) % k] -= 6
        a[j][(j-2) % k] += 1
    return a


def determinant(a):
    """Bareiss elimination with exact divisibility assertions."""
    a = [r[:] for r in a]
    size, previous, sign = len(a), 1, 1
    for k in range(size-1):
        if a[k][k] == 0:
            pivot = next((i for i in range(k+1, size) if a[i][k]), None)
            if pivot is None:
                return 0
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k+1, size):
            for j in range(k+1, size):
                value = pivot*a[i][j]-a[i][k]*a[k][j]
                assert value % previous == 0
                a[i][j] = value//previous
        for i in range(k+1, size):
            a[i][k] = 0
        previous = pivot
    return sign*a[-1][-1]


def inverse(a):
    n = len(a)
    aug = [[Fraction(x) for x in r]+[Fraction(i == j) for j in range(n)]
           for i, r in enumerate(a)]
    for j in range(n):
        p = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[p] = aug[p], aug[j]
        pivot = aug[j][j]
        aug[j] = [x/pivot for x in aug[j]]
        for i in range(n):
            if i != j:
                c = aug[i][j]
                aug[i] = [x-c*y for x, y in zip(aug[i], aug[j])]
    return [r[n:] for r in aug]


def arithmetic():
    determinants, smith = [], []
    for k in range(3, 32, 2):
        n, f = pell(k)
        h = (3+2*pow(f, -1, n)) % n
        assert n*n-2*f*f == -1 and pow(h, k, n) == 1
        assert math.gcd(h-1, n) == math.gcd(h-pow(h, -1, n), n) == 1
        det = determinant(matrix(k))
        assert abs(det) == 4*n*n
        determinants.append({"K": k, "N": n, "determinant": det})
        if k > 9:
            continue
        a = matrix(k)
        adj_gcd = 0
        for i in range(k):
            for j in range(k):
                minor = [[a[r][c] for c in range(k) if c != j]
                         for r in range(k) if r != i]
                adj_gcd = math.gcd(adj_gcd, determinant(minor))
        assert adj_gcd == n
        minor_gcd = checked = 0
        for rows in combinations(range(k), k-2):
            for cols in combinations(range(k), k-2):
                minor_gcd = math.gcd(minor_gcd,
                                    determinant([[a[r][c] for c in cols] for r in rows]))
                checked += 1
                if minor_gcd == 1:
                    break
            if minor_gcd == 1:
                break
        assert minor_gcd == 1
        smith.append({"K": k, "last_Smith_factors": [n, 4*n],
                      "codimension_two_minors_until_gcd_one": checked})

    checked = central = 0
    for k, values in ((3, range(28)), (5, range(-2, 3))):
        n, f = pell(k)
        h = (3+2*pow(f, -1, n)) % n
        inv = inverse(matrix(k))
        denominator = 4*n
        scaled = [[int(x*denominator) for x in row] for row in inv]
        assert all(x*denominator == y for row, r in zip(inv, scaled)
                   for x, y in zip(row, r))
        hp = [pow(h, j, n) for j in range(k)]
        hm = [pow(h, -j, n) for j in range(k)]
        for c in product(values, repeat=k):
            is_central = (sum(x*y for x, y in zip(c, hp)) % n == 0
                          and sum(x*y for x, y in zip(c, hm)) % n == 0)
            q = [sum(x*y for x, y in zip(row, c)) for row in scaled]
            integral = all(x % denominator == 0 for x in q)
            assert integral == (is_central and sum(c) % 4 == 0)
            if is_central:
                coset = sum(c)*pow(k, -1, 4) % 4
                assert all((x+coset*n) % denominator == 0 for x in q)
                threshold = k if coset in (1, 3) else 2*k if coset == 2 else 0
                assert sum(map(abs, c)) >= threshold
                central += 1
            checked += 1
    return {"determinants": determinants, "Smith_checks": smith,
            "rational_kernel_vectors": checked, "central_vectors": central}


def ordered_geometry():
    reciprocal_checks = strip_checks = 0
    for k in (5, 7, 11, 17):
        for ell in range(1, min(4, k//2)+1):
            sets = list(combinations(range(k), ell))
            upper = Fraction(ell, k-ell+1)
            for i in range(ell):
                total = Fraction(0)
                for x in sets:
                    left = x[i-1] if i else -1
                    right = x[i+1] if i+1 < ell else k
                    total += Fraction(1, right-left-1)
                assert total/len(sets) <= upper
                reciprocal_checks += 1
            forms = [tuple(1 if j == i else 0 for j in range(ell))
                     for i in range(ell)]
            forms += [tuple((-1)**j for j in range(ell)),
                      tuple(j+1 for j in range(ell))]
            if ell >= 3:
                forms.append((1, -2, 1)+(0,)*(ell-3))
            for form in forms:
                histogram = Counter(sum(a*b for a, b in zip(form, x)) for x in sets)
                lo, hi = min(histogram), max(histogram)
                for width in (0, 1, 2):
                    for start in range(lo-1, hi+1):
                        mass = sum(histogram[j] for j in range(start, start+width+1))
                        assert Fraction(mass, len(sets)) <= (width+1)*upper
                        strip_checks += 1
    # Exact rational constants used in the first-return bound.
    for j in range(1, 101):
        delta = Fraction(j, 1000)
        z = 2*delta
        assert 32*delta**4/(1-16*delta**4) <= delta**2/2
        assert (z+z**3)/(1-z**4) <= Fraction(5, 24)
        assert 2*z*z/(1-z**4) <= Fraction(25, 312)
    return {"conditional_reciprocal_checks": reciprocal_checks,
            "affine_strip_checks": strip_checks, "rational_kick_constants": 100}


def physical_unitary(k):
    n, f = pell(k)
    s = pow(f, -1, n)
    h = (3+2*s) % n
    x = np.arange(n)
    fourier = np.exp(2j*np.pi*((x[:, None]*x[None, :]) % n)/n)/math.sqrt(n)
    v = chirp(n, pow(s, -1, n))[:, None]*dilation_rows(
        fourier*chirp(n, 2*s)[None, :], pow(2, -1, n))
    u = v[:, (pow(h, -1, n)*x) % n] @ v.conj().T
    return u


def floating_matrices():
    rows, returns = [], []
    for k in (3, 5, 7, 9):
        n, _ = pell(k)
        d = (n-1)//2
        x = np.arange(1, d+1)
        p = 2/n*(1-np.cos(2*np.pi*((pow(2, -1, n)*x[:, None]*x[None, :]) % n)/n))
        gap_error = float(np.max(abs(p@p-(np.eye(d)+2*np.ones((d, d)))/n)))
        assert gap_error < 1e-12
        row = {"K": k, "N": n, "P_squared_error": gap_error}
        if k <= 7:
            u = physical_unitary(k)
            odd = u[1:d+1, 1:d+1]-u[1:d+1, (-x) % n]
            actual_error = float(np.max(abs(abs(odd)**2-p)))
            assert actual_error < 1e-12
            row["physical_modulus_error"] = actual_error
            full_x = np.arange(n)
            quadratic = ((3*full_x[:, None]**2-2*full_x[:, None]*full_x[None, :]
                          +3*full_x[None, :]**2)*pow(8, -1, n)) % n
            kernel = np.exp(2j*np.pi*quadratic/n)/math.sqrt(n)
            kernel_error = float(np.max(abs(u-(u[0, 0]/kernel[0, 0])*kernel)))
            assert kernel_error < 1e-12
            row["physical_kernel_error"] = kernel_error
            for a in (1, 2, n-1):
                for epsilon in (0., 0.05, 0.1, -0.1):
                    kicked = np.exp(2j*epsilon*np.cos(2*np.pi*a*x/n))[:, None]*odd
                    trace = np.trace(np.linalg.matrix_power(kicked, k))/d
                    bound = (math.exp(-k*epsilon*epsilon/2)+3*0.21**k
                             +math.exp(2*k*abs(epsilon))/(n-1))
                    assert abs(trace) <= bound+1e-12
                    assert np.max(abs(abs(kicked)**2-p)) < 1e-12
                    returns.append({"K": k, "a": a, "epsilon": epsilon,
                                    "trace_absolute_value": float(abs(trace)), "bound": bound})
        rows.append(row)
    return {"Markov_and_kernel_checks": rows, "first_return_controls": returns}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    result = {"scope": "Finite exact lattice/ordered-geometry and floating physical-matrix checks; no asymptotic or BGS certificate.",
              "python": platform.python_version(), "numpy": np.__version__,
              "arithmetic": arithmetic(), "ordered_geometry": ordered_geometry(),
              "floating_matrices": floating_matrices()}
    result["elapsed_seconds"] = time.monotonic()-start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2)+"\n")


if __name__ == "__main__":
    main()
