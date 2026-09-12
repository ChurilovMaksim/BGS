#!/usr/bin/env python3
"""Exact finite controls for the return-pressure proof; no BGS certificate.

The integer checks are exhaustive only on the stated finite domains.
The 80-digit transfer calculation has the explicit spin cutoff {-1,0,1};
it is a consistency experiment, not a certified infinite-spin computation.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from itertools import product
import json
import math
from pathlib import Path
import platform
import time

import mpmath as mp
import numpy as np
from pell_resonance_lattice import determinant


def modulus(t, k):
    previous, current = 0, 1
    for _ in range((k-1)//2):
        previous, current = current, t*current-previous
    return previous+current


def laplacian(p, t):
    return [p[(j-1) % len(p)]-t*p[j]+p[(j+1) % len(p)]
            for j in range(len(p))]


def arithmetic():
    counts = Counter()
    matrices = []
    for t in (4, 6, 8, 10, 12, 14, 20):
        for k in range(3, 20, 2):
            n = modulus(t, k)
            mat = [[int(i == (j-1) % k)+int(i == (j+1) % k)-t*int(i == j)
                    for j in range(k)] for i in range(k)]
            det = determinant(mat)
            assert abs(det) == (t-2)*n*n
            counts["determinants"] += 1
            w, orbit = (1, 0), []
            for _ in range(k):
                orbit.append(w)
                w = ((t*w[0]-w[1]) % n, w[0])
            assert w == (1, 0)
            assert all(sum(w[j] for w in orbit) % n == 0 for j in (0, 1))
            assert math.gcd(n, t-2) == math.gcd(k, t-2)
            counts["matrix_orbits"] += 1
            matrices.append({"T": t, "K": k, "N": n, "determinant": det})
            if k > 7 or math.gcd(k, t-2) != 1:
                continue
            inv2, invd = pow(2, -1, n), pow(t-2, -1, n)
            for p in product((-1, 0, 1), repeat=k):
                for r in (range(t-2) if k <= 5 else (0,)):
                    c = [x+r for x in laplacian(p, t)]
                    total, phase = [0, 0], 0
                    for cj, wj in zip(c, orbit):
                        wj = [cj*x for x in wj]
                        phase += (total[0]*wj[1]-total[1]*wj[0])*inv2
                        total = [(x+y) % n for x, y in zip(total, wj)]
                    assert total == [0, 0]
                    modp = [(x-r*invd) % n for x in p]
                    predicted = inv2*sum(x*y for x, y in zip(modp, c))
                    assert (phase-predicted) % n == 0
                    if r:
                        counts["affine_actions"] += 1
                    else:
                        action = sum(p[j]*p[(j+1) % k]-(t//2)*p[j]**2
                                     for j in range(k))
                        assert (phase-action) % n == 0
                        assert sum(c) % 4 == ((2-t)*sum(p)) % 4
                        counts["integer_actions"] += 1
    return {"counts": dict(counts), "determinants": matrices}


def poly_add(target, source, factor=1):
    for power, coefficient in source.items():
        target[power] += factor*coefficient
        if not target[power]:
            del target[power]


def poly_product(left, right):
    result = Counter()
    for a, x in left.items():
        for b, y in right.items():
            result[a+b] += x*y
    return Counter({k: v for k, v in result.items() if v})


def surrogate_weight(p, t, twist, cyclic):
    if cyclic:
        c = laplacian(p, t)
        pairs = sum(p[j]*p[(j+1) % len(p)] for j in range(len(p)))
    else:
        extended = (0, 0)+tuple(p)+(0, 0)
        c = [extended[j-1]-t*extended[j]+extended[j+1]
             for j in range(1, len(extended)-1)]
        pairs = sum(x*y for x, y in zip(p, p[1:]))
    action = pairs-(t//2)*sum(x*x for x in p)
    # J_{-n}=(-1)^n J_n; i^(sum c)=(-1)^((T/2-1)sum p).
    parity = ((t//2-1)*sum(p)+sum(max(-x, 0) for x in c)+twist*action)
    return sum(map(abs, c)), (-1 if parity % 2 else 1)


def cyclic_tilings():
    """Exact formal monomials, not an evaluation of Bessel functions."""
    maximum_k, checked, rows = 9, 0, []
    for t in (4, 6):
        for twist in (0, 1):  # theta=0 or 1/2, so every phase is an integer sign
            tiles = {1: Counter({0: 1})}
            for size in range(3, maximum_k+1):
                weight = Counter()
                for p in product((-1, 0, 1), repeat=size-2):
                    if not p[0] or not p[-1]:
                        continue
                    if any(x == y == 0 for x, y in zip(p, p[1:])):
                        continue
                    power, sign = surrogate_weight(p, t, twist, False)
                    weight[power] += sign
                tiles[size] = Counter({k: v for k, v in weight.items() if v})
            inverse = [Counter({0: 1})]
            for k in range(1, maximum_k+1):
                linear, cyclic = Counter(), Counter()
                for size, weight in tiles.items():
                    if size <= k:
                        contribution = poly_product(weight, inverse[k-size])
                        poly_add(linear, contribution)
                        poly_add(cyclic, contribution, size)
                inverse.append(linear)
                if k < 3:
                    continue
                direct = Counter()
                configurations = 0
                for p in product((-1, 0, 1), repeat=k):
                    if not any(p[j] == p[(j+1) % k] == 0 for j in range(k)):
                        continue
                    power, sign = surrogate_weight(p, t, twist, True)
                    direct[power] += sign
                    configurations += 1
                direct = Counter({k: v for k, v in direct.items() if v})
                assert direct == cyclic, (t, twist, k, direct-cyclic)
                checked += configurations
                rows.append({"T": t, "theta": str(Q(twist, 2)), "K": k,
                             "configurations": configurations,
                             "nonzero_polynomial_coefficients": len(direct)})
    return {"scope": "All cyclic spins in {-1,0,1} with an adjacent zero pair; exact signed monomials.",
            "configurations": checked, "rows": rows}


def multiply(a, b, degree):
    result = [Q(0) for _ in range(degree+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b[:degree+1-i]):
            result[i+j] += x*y
    return result


def bessel(n, degree):
    out = [Q(0) for _ in range(degree+1)]
    for j in range((degree-n)//2+1):
        out[n+2*j] = Q((-1)**j, math.factorial(j)*math.factorial(n+j))
    return out


def exact_series_and_constants():
    degree = 12
    j0 = bessel(0, degree)
    inverse = [Q(1)]
    for j in range(1, degree+1):
        inverse.append(-sum(j0[i]*inverse[j-i] for i in range(1, j+1)))
    derivative = [(j+1)*j0[j+1] for j in range(degree)]+[Q(0)]
    log_derivative = multiply(derivative, inverse, degree)
    log_j0 = [Q(0)]+[log_derivative[j-1]/j for j in range(1, degree+1)]
    assert [log_j0[j] for j in (2, 4, 6, 8, 10)] == [
        Q(-1), Q(-1, 4), Q(-1, 9), Q(-11, 192), Q(-19, 600)]
    w3 = multiply(multiply(bessel(1, degree), bessel(1, degree), degree),
                  bessel(6, degree), degree)
    for _ in range(3):
        w3 = multiply(w3, inverse, degree)
    w3 = [2*x for x in w3]
    assert [w3[j] for j in (8, 10, 12)] == [
        Q(1, 360), Q(13, 2520), Q(803, 120960)]
    v, r, a = Q(1, 12), Q(3, 2), Q(1, 5)
    bound = a**4*r*r*(2*v*r+4*v*v*r*r)/(1-4*v*r*r)
    assert bound == Q(9, 2000)
    cauchy = Q(4, 3)*(2+6*bound)/(Q(1, 3)-bound)
    assert cauchy < 9
    assert Q(9, 20)/(1-bound) < Q(1, 2)
    assert Q(100, 99)+Q(9, 20) < Q(3, 2)
    return {"log_J0_coefficients": {str(j): str(log_j0[j]) for j in (2, 4, 6, 8, 10)},
            "T6_single_site_coefficients": {str(j): str(w3[j]) for j in (8, 10, 12)},
            "rod_bound": str(bound), "Cauchy_remainder_constant": str(cauchy)}


def transfer_experiment():
    mp.mp.dps = 80
    states = tuple(product((-1, 0, 1), repeat=2))
    rows = []
    for t in (4, 6):
        for theta in (mp.mpf(0), mp.mpf("0.5"), mp.mpf("0.2")):
            previous_error = None
            target = (2*(-1)**(t//2-1)/mp.mpf(math.factorial(t))
                      *mp.exp(-mp.pi*1j*t*theta))
            for epsilon in (mp.mpf("0.02"), mp.mpf("0.01")):
                matrix = mp.matrix(len(states))
                for i, (p, q) in enumerate(states):
                    for j, (u, r) in enumerate(states):
                        if u == q:
                            matrix[i, j] = (
                                mp.besselj(p-t*q+r, 2*epsilon)/mp.besselj(0, 2*epsilon)
                                *(-1)**((t//2-1)*q)
                                *mp.exp(2j*mp.pi*theta*(q*r-(t//2)*q*q)))
                eigenvalues = mp.eig(matrix, left=False, right=False)
                leading = min(eigenvalues, key=lambda z: abs(z-1))
                coefficient = mp.log(leading)/epsilon**(t+2)
                error = abs(coefficient-target)
                if previous_error is not None:
                    assert error < mp.mpf("0.3")*previous_error
                previous_error = error
                rows.append({"T": t, "theta": str(theta), "epsilon": str(epsilon),
                             "rescaled_log_eigenvalue": mp.nstr(coefficient, 35),
                             "leading_theoretical_coefficient": mp.nstr(target, 35),
                             "absolute_error": mp.nstr(error, 15)})
    return {"scope": "Finite spin cutoff {-1,0,1}, 9 by 9 matrix; NOT a certified infinite-spin pressure.",
            "mpmath": mp.__version__, "decimal_precision": mp.mp.dps, "rows": rows}


def physical_controls():
    rows = []
    for t, k in ((4, 3), (4, 5), (4, 7), (6, 3), (6, 5), (6, 7)):
        n, a = modulus(t, k), 2
        x = np.arange(n)
        kernel_exponent = ((t*x[:, None]**2-2*x[:, None]*x[None, :])
                           *pow(2, -1, n)) % n
        u = np.exp(2j*np.pi*kernel_exponent/n)/math.sqrt(n)
        uk = np.linalg.matrix_power(u, k)
        scalar = np.trace(uk)/n
        error = float(np.max(abs(uk-scalar*np.eye(n))))
        assert error < 2e-12 and abs(abs(scalar)-1) < 2e-12
        u *= np.exp(-1j*np.angle(scalar)/k)
        # Direct Egorov check for W(a,0), whose image is W(Ta,a).
        clock = np.exp(2j*np.pi*(a*x % n)/n)
        evolved = (u*clock[None, :]) @ u.conj().T
        predicted = np.zeros((n, n), dtype=complex)
        predicted[x, (x-a) % n] = np.exp(
            2j*np.pi*((t*a*(x-a*pow(2, -1, n))) % n)/n)
        egorov = float(np.max(abs(evolved-predicted)))
        assert egorov < 2e-12
        d = (n-1)//2
        positive = np.arange(1, d+1)
        odd = u[1:d+1, 1:d+1]-u[1:d+1, (-positive) % n]
        kicked = np.exp(0.2j*np.cos(2*np.pi*a*positive/n))[:, None]*odd
        first_return = np.trace(np.linalg.matrix_power(kicked, k))/d
        rows.append({"T": t, "K": k, "N": n, "period_scalar_error": error,
                     "Egorov_error": egorov, "epsilon": 0.1, "a": a,
                     "normalized_return_real": float(first_return.real),
                     "normalized_return_imaginary": float(first_return.imag)})
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    start = time.monotonic()
    results = {
        "scope": "Exact finite action/tiling/series checks and explicitly truncated floating experiments; no asymptotic, priority, or BGS certificate.",
        "python": platform.python_version(), "numpy": np.__version__,
        "arithmetic": arithmetic(), "cyclic_tilings": cyclic_tilings(),
        "series_and_constants": exact_series_and_constants(),
        "finite_transfer_experiment": transfer_experiment(),
        "physical_controls": physical_controls(),
    }
    results["elapsed_seconds"] = time.monotonic()-start
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(results, indent=2)+"\n")
    print(json.dumps({"output": str(args.output), "elapsed_seconds": results["elapsed_seconds"],
                      "arithmetic": results["arithmetic"]["counts"],
                      "cyclic_configurations": results["cyclic_tilings"]["configurations"],
                      "transfer_experiments": len(results["finite_transfer_experiment"]["rows"]),
                      "physical_controls": len(results["physical_controls"])}))


if __name__ == "__main__":
    main()
