#!/usr/bin/env python3
"""Finite controls for BGS-FLOW-001/002; no fixed-map or BGS claim.

Float64 dense Hermitian samples, N=15,31, t=+/-0.25,+/-1.5,
T=1,3,7, deterministic seed 20260925. Exact scalar 2x2
sharpness formula is checked for m=5,11,23,47,95,511.
The ensemble completeness identity is checked in dimensions 3,4,7.
These checks do not prove a uniform-in-N or stochastic limit.
"""

from __future__ import annotations

import math

import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment


def op_norm(x: np.ndarray) -> float:
    return float(np.linalg.norm(x, ord=2))


def hs_norm(x: np.ndarray) -> float:
    return float(np.linalg.norm(x, ord="fro") / math.sqrt(len(x)))


def check_flow() -> int:
    rng = np.random.default_rng(20260925)
    trials = 0
    for n in (15, 31):
        angles = (2 * math.pi * np.arange(n) / n
                  + rng.uniform(-.12, .12, n) / n)
        u = np.diag(np.exp(1j * angles))
        z = rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))
        g = (z + z.conj().T) / (2 * n)
        b = u @ g @ u.conj().T
        c = g @ b - b @ g
        h = 1j * n * c
        eta = (op_norm(g @ c - c @ g)
               + .5 * op_norm((g - b) @ c - c @ (g - b)))
        power = h.copy()
        for tmax in (1, 3, 7):
            if tmax > 1:
                power = sum(np.linalg.matrix_power(u.conj().T, r) @ h
                            @ np.linalg.matrix_power(u, r)
                            for r in range(tmax)) / tmax
            v = hs_norm(power)
            for t in (-1.5, -.25, .25, 1.5):
                evolved = expm(1j * t * (g - b)) @ u
                got_angles = np.angle(np.linalg.eigvals(evolved))
                differences = np.angle(
                    np.exp(1j * (got_angles[:, None] - angles[None, :]))
                )
                row, col = linear_sum_assignment(differences**2)
                q = (n / (2 * math.pi)
                     * float(np.sqrt(np.mean(differences[row, col] ** 2))))
                bound = (t*t*v/(4*math.pi)
                         + t**4*(tmax-1)*op_norm(h)**2/(16*math.pi*n)
                         + n*abs(t)**3*eta/(6*math.pi))
                assert q <= bound + 1e-10, (n, tmax, t, q, bound)
                trials += 1
    return trials


def check_sharpness() -> None:
    c = .5
    target = c*c / math.sqrt(2)
    errors = []
    for m in (5, 11, 23, 47, 95, 511):
        n = 2*m*m
        alpha = math.pi/(2*m)
        t = c*n**.25
        beta = math.acos(
            math.cos(alpha) * math.cos(2*t*math.sin(alpha)/math.sqrt(n))
        )
        displacement = n*(beta-alpha)/(2*math.pi)
        leading = t*t*(2*math.sin(2*alpha))/(4*math.pi)
        errors.append(abs(displacement - target))
        assert abs(displacement - leading) < .1
    assert errors[-1] < errors[0] and errors[-1] < .002


def check_gue_covariance() -> None:
    for n in (3, 4, 7):
        angles = np.linspace(.13, 5.8, n)
        u = np.diag(np.exp(1j*angles))
        matrices = []
        for j in range(n):
            g = np.zeros((n,n), complex)
            g[j,j] = 1/math.sqrt(n)
            matrices.append(g)
        for j in range(n):
            for k in range(j+1, n):
                g = np.zeros((n,n), complex)
                g[j,k] = g[k,j] = 1/math.sqrt(2*n)
                matrices.append(g)
                g = np.zeros((n,n), complex)
                g[j,k] = 1j/math.sqrt(2*n)
                g[k,j] = -1j/math.sqrt(2*n)
                matrices.append(g)
        actual = sum((g @ (u@g@u.conj().T) - (u@g@u.conj().T) @ g
                      for g in matrices), np.zeros_like(u))
        predicted = (np.trace(u)*u.conj().T
                     - np.trace(u.conj().T)*u) / n
        assert op_norm(actual - predicted) < 1e-12
        # At Tr U=0, the radial drift in (7) vanishes identically.
        root = np.diag(np.exp(2j*math.pi*np.arange(n)/n))
        assert abs(np.trace(root)) < 1e-12
        assert max(abs(sum(math.sin(2*math.pi*(j-k)/n)
                           for k in range(n))) for j in range(n)) < 1e-12


def main() -> None:
    cases = check_flow()
    check_sharpness()
    check_gue_covariance()
    print(f"coboundary-flow: PASS ({cases} finite bound cases; "
          "sharpness scalar limits and GUE basis checks)")


if __name__ == "__main__":
    main()
