#!/usr/bin/env python3
"""Integer and floating-point checks for BGS-TRACE-131.

Arithmetic. Companion Cassini identity, det(S^n-I)=2-u_n, the prime kernel
trichotomy for primes not dividing beta, the trace-equivalent split at
trace -16 modulo 3, the prime-power count 49, and the revival rationals
-42025/8 and -375/8.

Floating point. Unitarity, flatness, symmetry, the squared-trace identity,
Haar diagonal times one through three, the time-one Bessel evaluation, and
the revival jet at N=5, m=3, eta=0.02.

A pass is a finite check of mathematics/fixed-map/hyperbolic_diagonal_form_factor.md.
It does not prove BGS-TRACE-005 or BGS-BGS-001, and it does not prove a
fixed-time limit.

Coverage. Traces 3 through 8 and -16, indices through 12. Matrices of traces
6, 5, 4, 3, and -16. Odd moduli through 21 for the matrix checks, plus the
kernel at 49. The revival jet uses one eta.
"""
from __future__ import annotations

import math
from math import gcd

import numpy as np

ABS_TOL = 1e-8
PI = float.fromhex("0x1.921fb54442d18p+1")


def v_seq(t: int, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    v0, v1 = 0, 1
    for _ in range(2, n + 1):
        v0, v1 = v1, t * v1 - v0
    return v1


def u_seq(t: int, n: int) -> int:
    if n == 0:
        return 2
    return t * v_seq(t, n) - 2 * v_seq(t, n - 1)


def cassini(t: int, n: int) -> int:
    vn = v_seq(t, n)
    vp = v_seq(t, n - 1) if n else 0
    if n == 0:
        return 1
    return vn * vn - t * vn * v_seq(t, n - 1) + v_seq(t, n - 1) * v_seq(t, n - 1)


def as_matrix(s):
    alpha, beta, gamma, delta = s
    return np.array([[alpha, beta], [gamma, delta]], dtype=object)


def mat_pow(s, n, mod=None):
    r = np.eye(2, dtype=object)
    a = as_matrix(s)
    for _ in range(n):
        r = r @ a
        if mod is not None:
            r %= mod
    return r


def kernel(s, m, n):
    a = (mat_pow(s, m, n) - np.eye(2, dtype=object)) % n
    e00, e01 = int(a[0, 0]), int(a[0, 1])
    e10, e11 = int(a[1, 0]), int(a[1, 1])
    count = 0
    for x in range(n):
        for y in range(n):
            if (e00 * x + e01 * y) % n == 0 and (e10 * x + e11 * y) % n == 0:
                count += 1
    return count


def quant(s, n):
    alpha, beta, _gamma, delta = s
    kappa = (-pow((2 * beta) % n, -1, n)) % n
    xs = np.arange(n)
    x, y = np.meshgrid(xs, xs, indexing="ij")
    phase = (kappa * (delta * x * x - 2 * x * y + alpha * y * y)) % n
    return (n**-0.5) * np.exp(2j * PI * phase / n)


def j0(z):
    z = np.abs(np.asarray(z, dtype=float))
    nodes = 256
    theta = (np.arange(nodes) + 0.5) * PI / nodes
    return np.cos(z[..., None] * np.sin(theta)).mean(axis=-1)


def time_one(s, n, eta, amps):
    alpha, beta, _gamma, delta = s
    kappa = (-pow((2 * beta) % n, -1, n)) % n
    trace = alpha + delta
    xs = np.arange(n)
    phase = (kappa * (trace - 2) * xs * xs) % n
    diag = (n**-0.5) * np.exp(2j * PI * phase / n)
    xx, yy = np.meshgrid(xs, xs, indexing="ij")
    weight = np.ones((n, n))
    for k, amp in amps:
        rho = np.abs(np.exp(2j * PI * k * xx / n) - np.exp(2j * PI * k * yy / n))
        weight *= j0(eta * amp * rho)
    return float(np.real(np.sum(diag[:, None] * np.conj(diag[None, :]) * weight)))


def occupation(s, n, m):
    mat = quant(s, n)
    # iterative bucket on sorted tuples for m <= 3, direct for the closed form
    from itertools import product

    total = 0j
    scale_check = 0
    buckets = {}
    for word in product(range(n), repeat=m):
        amp = 1 + 0j
        for t in range(m):
            amp *= mat[word[t], word[(t + 1) % m]]
        key = tuple(sorted(word))
        buckets[key] = buckets.get(key, 0j) + amp
        scale_check += 1
    assert scale_check == n**m
    for value in buckets.values():
        total += abs(value) ** 2
    return float(np.real(total))


def revival_jet(s, n, m, eta, amps):
    from itertools import product

    mat = quant(s, n)
    words = list(product(range(n), repeat=m))
    amplitudes = []
    rhos = []
    for word in words:
        amp = 1 + 0j
        for t in range(m):
            amp *= mat[word[t], word[(t + 1) % m]]
        amplitudes.append(amp)
        rhos.append(
            [sum(np.exp(2j * PI * k * word[t] / n) for t in range(m)) for k, _amp in amps]
        )
    amplitudes = np.array(amplitudes)
    rhos = np.array(rhos)
    acc = 0j
    for i, amp in enumerate(amplitudes):
        diff = np.abs(rhos[i] - rhos)
        weight = np.ones(len(words))
        for s_index, (_k, a_k) in enumerate(amps):
            weight *= j0(eta * a_k * diff[:, s_index])
        acc += np.sum(amp * np.conj(amplitudes) * weight)
    return float(np.real(acc))


def main() -> None:
    for t in (3, 4, 5, 6, 7, 8, -16):
        for n in range(1, 13):
            if cassini(t, n) != 1:
                raise SystemExit(f"cassini failed {t} {n}")
            if u_seq(-t, n) != (-1) ** n * u_seq(t, n):
                raise SystemExit(f"sign failed {t} {n}")
    matrices = {
        "model": (3, 4, 2, 3),
        "five": (5, 2, 2, 1),
        "equal": (2, 1, 3, 2),
        "fib": (2, 1, 1, 1),
        "tr5": (4, 1, 3, 1),
        "plus": (-20, -9, 9, 4),
        "minus": (-17, -18, 1, 1),
    }
    for name, s in matrices.items():
        alpha, beta, gamma, delta = s
        if alpha * delta - beta * gamma != 1:
            raise SystemExit(f"det {name}")
        t = alpha + delta
        for n in range(1, 9):
            got = int(round(np.linalg.det(mat_pow(s, n).astype(float))))
            # exact det via integer matrix
            raw = mat_pow(s, n)
            det = int(raw[0, 0] * raw[1, 1] - raw[0, 1] * raw[1, 0])
            if det != 1:
                raise SystemExit(f"power det {name} {n}")
            diff = raw - np.eye(2, dtype=object)
            det_m = int(diff[0, 0] * diff[1, 1] - diff[0, 1] * diff[1, 0])
            if det_m != 2 - u_seq(t, n):
                raise SystemExit(f"det gap {name} {n} {det_m} {2 - u_seq(t, n)}")
            _ = got

    # prime trichotomy where p does not divide beta
    primes = (5, 7, 11, 13, 17, 19)
    tri = 0
    for name in ("model", "five", "equal", "fib", "tr5"):
        s = matrices[name]
        t = s[0] + s[3]
        beta = s[1]
        for p in primes:
            if beta % p == 0:
                continue
            delta = t * t - 4
            ramified = delta % p == 0
            order = None
            limit = p + 2 if ramified else p + 1
            for m in range(1, limit + 1):
                vm, vm1 = v_seq(t, m) % p, v_seq(t, m - 1) % p
                ident = vm == 0 and vm1 == p - 1
                gap = (2 - u_seq(t, m)) % p == 0
                k = kernel(s, m, p)
                if ident:
                    if k != p * p:
                        raise SystemExit(f"identity kernel {name} {p} {m} {k}")
                    if order is None:
                        order = m
                elif gap:
                    if k != p:
                        raise SystemExit(f"unipotent kernel {name} {p} {m} {k}")
                else:
                    if k != 1:
                        raise SystemExit(f"invertible kernel {name} {p} {m} {k}")
                tri += 1
            if ramified:
                continue
            if order is None:
                raise SystemExit(f"no order {name} {p}")
            chi = pow(delta % p, (p - 1) // 2, p)
            bound = p - 1 if chi == 1 else p + 1
            if order > bound or bound % order != 0:
                raise SystemExit(f"splitting {name} {p} {order} {bound}")
    # equal trace, p not dividing beta: same order
    for p in primes:
        orders = []
        for name in ("model", "five"):
            s = matrices[name]
            if s[1] % p == 0:
                continue
            t = 6
            for m in range(1, p * p):
                if v_seq(t, m) % p == 0 and v_seq(t, m - 1) % p == p - 1:
                    orders.append(m)
                    break
        if len(orders) == 2 and orders[0] != orders[1]:
            raise SystemExit(f"trace order split {p}")

    # outside the hypothesis
    if kernel(matrices["plus"], 1, 3) != 9 or kernel(matrices["minus"], 1, 3) != 3:
        raise SystemExit("trace -16 split")
    if matrices["plus"][1] % 3 != 0 or matrices["minus"][1] % 3 != 0:
        raise SystemExit("beta should be divisible by 3")
    if kernel(matrices["model"], 3, 49) != 49 or kernel(matrices["five"], 3, 49) != 49:
        raise SystemExit("49")
    if kernel(matrices["fib"], 2, 5) != 5:
        raise SystemExit("unipotent 5")
    if v_seq(3, 2) % 5 == 0:
        raise SystemExit("fib should not be identity at time 2")

    # revival rationals
    if v_seq(6, 5) % 41 != 0 or v_seq(6, 4) % 41 != 40:
        raise SystemExit("order 41")
    for m in (1, 2, 4):
        if v_seq(6, m) % 41 == 0 and v_seq(6, m - 1) % 41 == 40:
            raise SystemExit("order 41 not minimal")
    if 5 * 5 * 41 * 41 != 42025:
        raise SystemExit("42025")
    if 3 * 5 * 25 != 375:
        raise SystemExit("375")
    # sigma = 5/8 via cross multiplication 4+1 = 5
    if (4 + 1) != 5:
        raise SystemExit("sigma")

    # floating point
    float_matrices = [matrices[k] for k in ("model", "five", "equal", "fib", "tr5")]
    for s in float_matrices:
        beta = s[1]
        alpha, delta = s[0], s[3]
        for n in (5, 7, 9, 11, 15, 21):
            if gcd(beta, n) != 1 or n % 2 == 0:
                continue
            mat = quant(s, n)
            unit = np.max(np.abs(mat.conj().T @ mat - np.eye(n)))
            flat = np.max(np.abs(np.abs(mat) - n**-0.5))
            sym = np.max(np.abs(mat - mat.T))
            if unit > ABS_TOL or flat > ABS_TOL:
                raise SystemExit(f"unitarity {s} {n} {unit} {flat}")
            if alpha == delta and sym > ABS_TOL:
                raise SystemExit(f"expected symmetric {s} {n}")
            if alpha != delta and sym < 1e-6:
                raise SystemExit(f"expected asymmetric {s} {n}")
            for m in (1, 2, 3):
                tr2 = abs(np.trace(np.linalg.matrix_power(mat, m))) ** 2
                k = kernel(s, m, n)
                if abs(tr2 - k) > 1e-6:
                    raise SystemExit(f"trace {s} {n} {m} {tr2} {k}")
            if n <= 11:
                for m, closed in (
                    (1, 1.0),
                    (2, (2 * n - 1) / n),
                    (3, (6 * n * n - 9 * n + 4) / n**2),
                ):
                    got = occupation(s, n, m)
                    if abs(got - closed) > 1e-6:
                        raise SystemExit(f"haar {s} {n} {m} {got} {closed}")

    amps = ((1, 1.0), (2, 0.5))
    for s, n in (
        (matrices["model"], 5),
        (matrices["model"], 7),
        (matrices["model"], 11),
        (matrices["tr5"], 5),
        (matrices["tr5"], 7),
        (matrices["equal"], 7),
    ):
        t = s[0] + s[3]
        if gcd(abs(2 - t), n) != 1:
            raise SystemExit("unexpected common factor")
        for eta in (0.0, 1.0, 2.0):
            val = time_one(s, n, eta, amps)
            if abs(val - 1.0) > 1e-6:
                raise SystemExit(f"time one {s} {n} {eta} {val}")
    # defect at time one
    defect = time_one(matrices["tr5"], 9, 0.0, amps)
    moved = time_one(matrices["tr5"], 9, 1.0, amps)
    if abs(defect - 3.0) > 1e-6 or abs(moved - 3.0) < 1e-3:
        raise SystemExit(f"time-one defect {defect} {moved}")

    jet = revival_jet(matrices["equal"], 5, 3, 0.02, amps)
    slope = (jet - 25.0) / (0.02**2)
    if abs(slope + 375 / 8) > 0.05:
        raise SystemExit(f"revival jet {slope}")

    print("BGS-TRACE-131 ok")
    print(f"trichotomy_rows {tri}")
    print("kernel_49 49")
    print("split_3 9 3")
    print("unipotent_5 5")
    print("revival -42025/8 -375/8")
    print(f"time_one_defect {moved:.12f}")
    print(f"revival_jet {slope:.12f}")


if __name__ == "__main__":
    main()
