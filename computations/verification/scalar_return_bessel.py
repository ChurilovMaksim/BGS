#!/usr/bin/env python3
"""Integer orbit counts and floating Bessel sums for BGS-TRACE-129.

The Bessel identity is the classical orbit sum of a position-diagonal kick.
A pass does not identify that sum with the quantum trace, and it does not
prove BGS-TRACE-005 or BGS-BGS-001.
"""
from __future__ import annotations

import numpy as np

PI = float.fromhex("0x1.921fb54442d18p+1")
PRIMES = (5, 7, 11, 13, 17, 19, 31, 41, 47)
EXCESS_ZERO = (7, 31, 41, 47)
QUAD_EXPECT = {5: (6, 90, 66), 7: (3, 15, 15), 11: (12, 396, 276),
               31: (15, 435, 435), 41: (5, 45, 45), 47: (23, 1035, 1035)}


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


def modes():
    out = []
    for k in range(-9, 10):
        for ell in range(-1, 2):
            re, im = coeff(k, ell)
            if re or im:
                out.append((ell, k, re, im))
    return out


MODES = modes()


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise SystemExit(msg)


def order_and_rows(n: int) -> tuple[int, list[tuple[int, int]]]:
    a = b = d = 0
    c = 1  # placeholder, overwritten
    aa, bb, cc, dd = 1, 0, 0, 1
    rows = []
    for t in range(0, n * n + 3):
        rows.append((aa % n, bb % n))
        if t > 0 and (aa % n, bb % n, cc % n, dd % n) == (1, 0, 0, 1):
            return t, rows[:-1]
        aa, bb, cc, dd = (
            (3 * aa + 2 * bb) % n,
            (4 * aa + 3 * bb) % n,
            (3 * cc + 2 * dd) % n,
            (4 * cc + 3 * dd) % n,
        )
        a, b, c, d = aa, bb, cc, dd
    raise SystemExit(f"order not found at {n}")


def quadruples(rows: list[tuple[int, int]], n: int) -> int:
    sums: dict[tuple[int, int], int] = {}
    for u in rows:
        for v in rows:
            key = ((u[0] + v[0]) % n, (u[1] + v[1]) % n)
            sums[key] = sums.get(key, 0) + 1
    return sum(v * v for v in sums.values())


def bessel_j0(z: np.ndarray) -> np.ndarray:
    z = np.asarray(z, dtype=float)
    term = np.ones_like(z)
    total = np.ones_like(z)
    y = (z / 2.0) ** 2
    for k in range(1, 40):
        term *= -y / (k * k)
        total += term
    return total


def diagonal_pairs() -> list[tuple[int, float]]:
    """Representative frequency and modulus of each diagonal pair."""
    found = {}
    for ell, k, re, im in MODES:
        if ell != 0:
            continue
        other = -k
        rep = k if k > other else other
        if rep not in found:
            found[rep] = (re / 4000.0) ** 2 + (im / 4000.0) ** 2
    return [(k, found[k] ** 0.5) for k in sorted(found)]


PAIRS = diagonal_pairs()


def phasors(n: int, m: int, k: int) -> np.ndarray:
    out = np.zeros(n * n, dtype=np.complex128)
    idx = 0
    for q in range(n):
        for p in range(n):
            acc = 0j
            qq, pp = q, p
            for _ in range(m):
                acc += np.exp(2j * PI * ((k % n) * qq % n) / n)
                qq, pp = (3 * qq + 4 * pp) % n, (2 * qq + 3 * pp) % n
            out[idx] = acc
            idx += 1
    return out


def bessel_average(n: int, m: int, eta: float) -> float:
    active = [(k, amp) for k, amp in PAIRS if k % n != 0]
    vs = [(amp, phasors(n, m, k)) for k, amp in active]
    # Accumulate the mean of the product by streaming pairs in blocks.
    total = 0.0
    block = 64
    idx = np.arange(n * n)
    for i0 in range(0, n * n, block):
        ii = idx[i0:i0 + block]
        delta = None
        prod = np.ones((ii.size, n * n), dtype=float)
        for amp, vec in vs:
            diff = np.abs(vec[ii, None] - vec[None, :])
            prod *= bessel_j0(2.0 * eta * amp * diff)
        total += float(prod.sum())
        del delta
    return total / (n ** 4)


def sigma_diag(n: int) -> float:
    return sum(2.0 * amp * amp for k, amp in PAIRS if k % n != 0)


def orbit_monte_carlo(n: int, m: int, eta: float, draws: int, seed: int) -> float:
    rng = np.random.default_rng(seed)
    active = [(k, amp) for k, amp in PAIRS if k % n != 0]
    # fixed arguments alpha are irrelevant for |V-V'| and for one orbit's |V|
    acc = 0.0
    for _ in range(draws):
        phases = rng.uniform(0.0, 2.0 * PI, size=len(active))
        total = 0j
        for q in range(n):
            for p in range(n):
                qq, pp = q, p
                phase_sum = 0.0
                # recompute positions
                positions = []
                for _j in range(m):
                    positions.append(qq)
                    qq, pp = (3 * qq + 4 * pp) % n, (2 * qq + 3 * pp) % n
                for (k, amp), phi in zip(active, phases):
                    acc_c = 0.0
                    for x in positions:
                        acc_c += np.cos(phi + 2.0 * PI * ((k % n) * x % n) / n)
                    phase_sum += 2.0 * amp * acc_c
                total += np.exp(1j * eta * phase_sum)
        acc += abs(total / (n * n)) ** 2
    return acc / draws


def odd_energy_scaled() -> int:
    total = 0
    for ell, k, re, im in MODES:
        if ell == 1:
            total += re * re + im * im
    return total


def main() -> None:
    require(len(MODES) == 32, "mode count")
    energy = sum(re * re + im * im for *_, re, im in MODES)
    require(energy == 6603300, f"energy {energy}")
    odd = odd_energy_scaled()
    require(odd == 900, f"odd energy {odd}")
    require(odd * 160000 == 9 * 16000000, "9/160000")
    require((2 * 2 - 4 * 2) == -4, "det")

    for n in PRIMES:
        m, rows = order_and_rows(n)
        require(len(rows) == m and len(set(rows)) == m, f"rows {n}")
        quads = quadruples(rows, n)
        perm = 2 * m * m - m
        print(f"quad N={n} m={m} quads={quads} perm={perm} excess={quads - perm}")
        if n in QUAD_EXPECT:
            em, eq, ep = QUAD_EXPECT[n]
            require((m, quads, perm) == (em, eq, ep), f"quad table {n}")
        if n in EXCESS_ZERO:
            require(quads == perm, f"excess {n}")
        if n >= 11:
            # no diagonal frequency is 0 mod n
            require(all(k % n != 0 for k, _ in PAIRS), f"sigma0 {n}")

    # Bessel versus the exponential, and versus a Monte Carlo of the orbit sum.
    for n, lams in ((11, (1.0,)), (31, (0.3, 1.0)), (47, (1.0,))):
        m, _rows = order_and_rows(n)
        sig = sigma_diag(n)
        for lam in lams:
            eta = (lam / (sig * m)) ** 0.5
            avg = bessel_average(n, m, eta)
            ratio = avg / np.exp(-lam)
            print(f"bessel N={n} m={m} lam={lam:.1f} avg={avg:.6f} ratio={ratio:.4f}")
            if n == 11 and lam == 1.0:
                require(ratio > 1.10, "p=11 should sit above the exponential")
            if n in (31, 47) and lam == 1.0:
                require(abs(ratio - 1.0) < 0.03, f"free orbit ratio {n}")
            if n == 31 and lam == 0.3:
                require(abs(ratio - 1.0) < 0.01, "small lambda")

    for n, draws in ((7, 400), (11, 200)):
        m, _ = order_and_rows(n)
        sig = sigma_diag(n)
        eta = (0.3 / (sig * m)) ** 0.5 if sig > 0 else 0.2
        exact = bessel_average(n, m, eta)
        sample = orbit_monte_carlo(n, m, eta, draws, seed=100 + n)
        print(f"orbit N={n} eta={eta:.4f} bessel={exact:.6f} mc={sample:.6f}")
        require(abs(exact - sample) < 0.02, f"orbit monte carlo {n}")
    print("PASS")


if __name__ == "__main__":
    main()
