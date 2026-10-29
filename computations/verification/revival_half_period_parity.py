#!/usr/bin/env python3
"""Checks for BGS-TRACE-135 (half-period parity reduction) and diagnostics for
the open free-with-parity revival law (diagonal kick only).

Proved and checked here: at an odd prime with even order t, S^(t/2) = -I;
M^(t/2) = c P with P the parity; R = Tr U^t / Tr M^t = N^-1 Tr(A P A P).
The Monte Carlo rows are diagnostics of an open conjecture and do not prove it.
"""
from __future__ import annotations

import math

import numpy as np
from scipy.special import i0

from revival_closure_law import DIAG, SIGMA_D, cat, diag_kick, order, require, spow_mod

SEED = 20261030


def is_prime(n: int) -> bool:
    return n > 1 and all(n % p for p in range(2, math.isqrt(n) + 1))


def check_half_period() -> None:
    primes = [p for p in range(3, 400) if is_prime(p)]
    even = 0
    for p in primes:
        t = order(p)
        if t % 2 == 0:
            even += 1
            require(spow_mod(t // 2, p) == (p - 1, 0, 0, p - 1), f"S^(t/2) = -I at p={p}")
    print(f"S^(t/2) = -I at all {even} odd primes < 400 with even order  ok")
    expect = {201: 200, 401: 400, 801: 800, 203: 57, 205: 124, 1001: 274}
    for n, h in expect.items():
        t = order(n)
        require(t % 2 == 0 and spow_mod(t // 2, n) == (h, 0, 0, h), f"half return at {n}")
    print("composite half returns:", expect, " ok")


def check_parity_reduction() -> None:
    rng = np.random.default_rng(SEED)
    for n in (61, 101):
        t = order(n)
        mm = cat(n)
        par = np.zeros((n, n))
        par[np.arange(n), (-np.arange(n)) % n] = 1
        half = np.linalg.matrix_power(mm, t // 2)
        c = half[0, 0]
        require(abs(abs(c) - 1) < 1e-9 and np.abs(half - c * par).max() < 1e-9, f"M^(t/2)=cP at {n}")
        require(np.abs(par @ mm - mm @ par).max() < 1e-12, f"[P,M]=0 at {n}")
        d = diag_kick(n, rng.uniform(0, 2 * np.pi, len(DIAG)), 0.6)
        trmt = np.sum(np.linalg.eigvals(mm) ** t)
        r = np.sum(np.linalg.eigvals(d[:, None] * mm) ** t) / trmt
        a = np.eye(n, dtype=complex)
        mj = np.eye(n, dtype=complex)
        for _ in range(t // 2):
            a = a @ (mj @ np.diag(d) @ mj.conj().T)
            mj = mm @ mj
        red = np.trace(a @ par @ a @ par) / n
        require(abs(r - red) < 1e-9, f"parity reduction at {n}")
    print("M^(t/2) = cP, [P,M] = 0 and R = N^-1 Tr(A P A P) at N=61, 101  ok")


def diagnostics() -> None:
    c4 = sum(abs(c) ** 4 for _, c in DIAG)
    sig = float(SIGMA_D)
    coef = c4 / (2 * sig ** 2)
    print(f"derived constant sum|c|^4/(2 sigma_d^2) = {coef:.7f} (from the heuristic F2)")
    require(abs(coef - 0.1204622) < 1e-6, "constant")
    rng = np.random.default_rng(SEED + 1)
    print("diagnostic (open conjecture): N t lam | E|R|^2 +- se | F2 | classical orbit | e^-lam  free-parity limit  classical limit")
    for n in (61, 101):
        t = order(n)
        nh = t // 2
        mm = cat(n)
        trmt = np.sum(np.linalg.eigvals(mm) ** t)
        x = np.arange(n)
        for lam in (1.0, 2.0, 3.0):
            eta = math.sqrt(lam / (sig * t))
            r2, f2, cl = [], [], []
            for _ in range(1000):
                d = diag_kick(n, rng.uniform(0, 2 * np.pi, len(DIAG)), eta)
                r = np.sum(np.linalg.eigvals(d[:, None] * mm) ** t) / trmt
                mu = d.mean()
                dp = d[(-x) % n]
                mup = dp.mean()
                f = (mu * mup) ** (nh - 1) * (mu * mup + nh * ((d * dp).mean() - mu * mup))
                z0 = np.repeat(x, n)
                z1 = np.tile(x, n)
                pr = np.ones(n * n, complex)
                for _ in range(t):
                    pr *= d[z0]
                    z0, z1 = (3 * z0 + 4 * z1) % n, (2 * z0 + 3 * z1) % n
                r2.append(abs(r) ** 2)
                f2.append(abs(f) ** 2)
                cl.append(abs(pr.mean()) ** 2)
            r2 = np.array(r2)
            se = r2.std() / math.sqrt(len(r2))
            lim = math.exp(-lam) * (1 + coef * lam ** 2)
            clim = math.exp(-lam) * float(np.prod([i0(2 * lam * abs(c) ** 2 / sig) for _, c in DIAG]))
            print(f"  {n} {t} {lam} | {r2.mean():.4f} +- {se:.4f} | {np.mean(f2):.4f} | {np.mean(cl):.4f} | "
                  f"{math.exp(-lam):.4f} {lim:.4f} {clim:.4f}")
            require(abs(r2.mean() - np.mean(f2)) < 4 * se, "diagnostic: F2 within 4 se")
            if lam >= 2:
                require(np.mean(cl) - r2.mean() > 5 * se, "diagnostic: classical orbit law above data by > 5 se")


def main() -> None:
    check_half_period()
    check_parity_reduction()
    diagnostics()
    print("PASS")


if __name__ == "__main__":
    main()
