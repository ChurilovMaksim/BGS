#!/usr/bin/env python3
"""Floating-point checks for BGS-TRACE-128.

The symmetric inequality and the inversion inequality are finite checks of
the counting argument in mathematics/fixed-map/diagonal_phase_short_time.md.
They are not a substitute for it. The Kloosterman quadruple count is an
integer census at p=5 and p=7. Unitarity is a floating-point check on the
certificate dimensions.

Coverage. Symmetric: odd N from 3 through 15 at times 3, 4 and 5, and N in
{21, 31, 41, 49} at time 4, including N=3, 5 and 7. Inversion: primes from
3 through 31 at times 3 and 4. Times 1 and 2 use the flat-matrix formulae.
At p=3 the inversion permutation is the identity.

Non-claims. A pass does not prove BGS-TRACE-005 or BGS-BGS-001, a window
m <= N^alpha, or a limit for the sixteen-phase ensemble.
"""
from __future__ import annotations

import cmath
import math

PI = float.fromhex("0x1.921fb54442d18p+1")
ABS_TOL = 1e-8
UNIT_TOL = 1e-8

SYM_ODD = (3, 5, 7, 9, 11, 13, 15)
SYM_M4 = (21, 31, 41, 49)
PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31)


def factorial(m: int) -> int:
    out = 1
    for k in range(2, m + 1):
        out *= k
    return out


def falling(n: int, m: int) -> int:
    if m > n:
        return 0
    out = 1
    for k in range(m):
        out *= n - k
    return out


def mod_inverse(a: int, n: int) -> int:
    return pow(a, -1, n)


def pi_table(n: int, invert: bool) -> list[int]:
    table = list(range(n))
    if invert:
        for x in range(1, n):
            table[x] = mod_inverse(x, n)
    return table


def occupation(n: int, m: int, invert: bool) -> float:
    inv8 = mod_inverse(8, n)
    pi = pi_table(n, invert)
    buckets: dict[tuple[int, ...], complex] = {}
    xs = [0] * m
    scale = n ** (-0.5 * m)
    twopi = 2.0 * PI
    for _ in range(n**m):
        phase = 0
        for t in range(m):
            u = pi[xs[t]]
            v = xs[0] if t + 1 == m else xs[t + 1]
            quad = (3 * u * u - 2 * u * v + 3 * v * v) % n
            phase += (-inv8 * quad) % n
        phase %= n
        amp = cmath.exp(1j * twopi * phase / n) * scale
        key = tuple(sorted(xs))
        buckets[key] = buckets.get(key, 0j) + amp
        for i in range(m):
            xs[i] += 1
            if xs[i] < n:
                break
            xs[i] = 0
    return float(sum(abs(value) ** 2 for value in buckets.values()))


def entry_phase(n: int, x: int, y: int, invert: bool) -> int:
    inv8 = mod_inverse(8, n)
    u = mod_inverse(x, n) if invert and x else x
    quad = (3 * u * u - 2 * u * y + 3 * y * y) % n
    return (-inv8 * quad) % n


def unitary_deviation(n: int, invert: bool) -> float:
    inv8 = mod_inverse(8, n)
    pi = pi_table(n, invert)
    scale = n ** -0.5
    twopi = 2.0 * PI
    cols = []
    for y in range(n):
        col = []
        for x in range(n):
            quad = (3 * pi[x] * pi[x] - 2 * pi[x] * y + 3 * y * y) % n
            phase = (-inv8 * quad) % n
            col.append(cmath.exp(1j * twopi * phase / n) * scale)
        cols.append(col)
    worst = 0.0
    for i in range(n):
        for j in range(i, n):
            inner = 0j
            for y in range(n):
                inner += cols[y][i] * cols[y][j].conjugate()
            target = 1.0 if i == j else 0.0
            worst = max(worst, abs(inner - target))
    return worst


def quad_count(p: int) -> int:
    count = 0
    for n1 in range(1, p):
        inv1 = mod_inverse(n1, p)
        for n2 in range(1, p):
            inv2 = mod_inverse(n2, p)
            sum12 = (n1 + n2) % p
            inv12 = (inv1 + inv2) % p
            for n3 in range(1, p):
                inv3 = mod_inverse(n3, p)
                for n4 in range(1, p):
                    if (sum12 - n3 - n4) % p:
                        continue
                    if (inv12 - inv3 - mod_inverse(n4, p)) % p:
                        continue
                    count += 1
    return count


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)


def check_low_times(n: int, invert: bool, label: str) -> None:
    for m, closed in ((1, 1.0), (2, (2 * n - 1) / n)):
        got = occupation(n, m, invert)
        err = abs(got - closed)
        print(f"{label} N={n} m={m} E={got:.12f} closed={closed:.12f} err={err:.3e}")
        require(err <= ABS_TOL, f"low time failed {label} N={n} m={m}")


def check_symmetric(n: int, m: int) -> float:
    got = occupation(n, m, False)
    main = 2 * m * falling(n, m) / n**m
    bound = factorial(m) * (1 + m * (m - 1)) / n
    diff = abs(got - main)
    slack = bound - diff
    print(
        f"sym N={n} m={m} E={got:.12f} D={main:.12f} "
        f"diff={diff:.6e} bound={bound:.6f} slack={slack:.6e}"
    )
    require(slack >= -ABS_TOL, f"symmetric inequality failed N={n} m={m}")
    if m == 3:
        closed = (6 * n * n - 9 * n + 4) / (n * n)
        exact = (9 * n - 8) / (n * n)
        require(abs(got - closed) <= ABS_TOL, f"time-three closed form failed N={n}")
        require(abs((got - main) - exact) <= ABS_TOL, f"time-three gap failed N={n}")
    return got


def check_inversion(p: int, m: int) -> float:
    got = occupation(p, m, True)
    main = m * falling(p, m) / p**m
    bound = factorial(m) * (3**0.25 * p ** (-0.25) + (m * (m - 1) + 2) / p)
    diff = abs(got - main)
    slack = bound - diff
    print(
        f"inv p={p} m={m} E={got:.12f} main={main:.12f} "
        f"diff={diff:.6e} bound={bound:.6f} slack={slack:.6e}"
    )
    require(slack >= -ABS_TOL, f"inversion inequality failed p={p} m={m}")
    return got


def main() -> None:
    for n in SYM_ODD:
        check_low_times(n, False, "sym")
        for m in (3, 4, 5):
            check_symmetric(n, m)
        dev = unitary_deviation(n, False)
        print(f"unit sym N={n} dev={dev:.3e}")
        require(dev <= UNIT_TOL, f"symmetric unitarity failed N={n}")
    for n in SYM_M4:
        check_symmetric(n, 4)
        dev = unitary_deviation(n, False)
        print(f"unit sym N={n} dev={dev:.3e}")
        require(dev <= UNIT_TOL, f"symmetric unitarity failed N={n}")

    for p in PRIMES:
        check_low_times(p, True, "inv")
        sym3 = occupation(p, 3, False) if p == 3 else None
        sym4 = occupation(p, 4, False) if p == 3 else None
        for m in (3, 4):
            got = check_inversion(p, m)
            if p == 3:
                other = sym3 if m == 3 else sym4
                err = abs(got - other)
                print(f"id p=3 m={m} err={err:.3e}")
                require(err <= ABS_TOL, f"p=3 identity failed m={m}")
        if p >= 5:
            x, y = (2, 0) if p == 11 else (1, 2)
            delta = (entry_phase(p, x, y, True) - entry_phase(p, y, x, True)) % p
            print(f"nonsym p={p} pair={x},{y} delta={delta}")
            require(delta != 0, f"inversion still symmetric at p={p}")
        dev = unitary_deviation(p, True)
        print(f"unit inv p={p} dev={dev:.3e}")
        require(dev <= UNIT_TOL, f"inversion unitarity failed p={p}")

    for p, expected, cap in ((5, 36, 48), (7, 90, 108)):
        got = quad_count(p)
        print(f"kloosterman p={p} count={got} cap={cap}")
        require(got == expected, f"quadruple census failed p={p}")
        require(got <= cap, f"quadruple cap failed p={p}")
    print("PASS")


if __name__ == "__main__":
    main()
