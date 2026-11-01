#!/usr/bin/env python3
"""Exact checks for BGS-TRACE-127, plus one shared sixteen-phase sample.

Arithmetic. Kernels of S^2-I and S^3-I, the 7-adic formula, and the symbol
energy 6603300 are exact integers. The closed forms (2N-1)/N and
(6N^2-9N+4)/N^2 are exact rationals.

Floating point. The occupation sum for the position-diagonal ensemble is
compared with those rationals. A pass is a finite check of the counting
argument in mathematics/fixed-map/diagonal_phase_form_factor.md, not a
substitute for it. The sixteen-phase block is one deterministic sample.
It is not an evaluation of the expectation and not a CUE limit.

Coverage. Odd N in {3,5,7,9,11,15,21,25,27,35,45,49,63,105} at times 1, 2
and 3, including N=3, 5 and 7. The sixteen-phase sample uses N in
{3,5,7,11,31}, eta=2, 24 draws, times 1..6, seed 20261029.

Non-claims. A pass does not prove BGS-TRACE-005 or BGS-BGS-001, a CUE or
COE limit, or a limit for the sixteen-phase ensemble.
"""
from __future__ import annotations
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import math

import numpy as np

CERT_N = (3, 5, 7, 9, 11, 15, 21, 25, 27, 35, 45, 49, 63, 105)
SAMPLE_N = (3, 5, 7, 11, 31)
SAMPLE_ETA = 2.0
SAMPLE_DRAWS = 24
SAMPLE_MMAX = 6
SAMPLE_SEED = 20261029
ABS_TOL = 1e-6
PI = float.fromhex("0x1.921fb54442d18p+1")
MASK = (1 << 64) - 1


def r_num(k: int) -> int:
    return {0: 4, 1: 2, -1: 2, 7: -2, -7: -2, 6: -1, -6: -1, 8: -1, -8: -1}.get(k, 0)


def coeff(k: int, ell: int) -> tuple[int, int]:
    """Scaled coefficient 4000 * fCoeff(k, ell), frequency-first, as in Lean."""
    if ell == 0:
        re = (2000 if k in (7, -7) else 0) + 100 * r_num(k) - (400 if k == 0 else 0)
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
            if re == 0 and im == 0:
                continue
            out.append((ell, k, re, im))
    return out


MODES = modes()


def pairs():
    remaining = {(a, b): (re, im) for a, b, re, im in MODES}
    assert len(remaining) == 32
    out = []
    for v in sorted(remaining):
        if v not in remaining:
            continue
        w = (-v[0], -v[1])
        rep, other = (v, w) if v > w else (w, v)
        out.append((rep, remaining[rep], other, remaining[other]))
        del remaining[v]
        del remaining[w]
    assert len(out) == 16 and not remaining
    return out


PAIRS = pairs()


def symbol_energy() -> int:
    return sum(re * re + im * im for _a, _b, re, im in MODES)


def pow_s(m: int) -> tuple[int, int, int, int]:
    a, b, c, d = 1, 0, 0, 1
    ea, eb, ec, ed = 3, 4, 2, 3
    e = m
    while e:
        if e & 1:
            a, b, c, d = a * ea + b * ec, a * eb + b * ed, c * ea + d * ec, c * eb + d * ed
        ea, eb, ec, ed = ea * ea + eb * ec, ea * eb + eb * ed, ec * ea + ed * ec, ec * eb + ed * ed
        e >>= 1
    return a, b, c, d


def ker(n: int, m: int) -> int:
    a, b, c, d = pow_s(m)
    a, d = a - 1, d - 1
    cnt = 0
    for x in range(n):
        for y in range(n):
            if (a * x + b * y) % n == 0 and (c * x + d * y) % n == 0:
                cnt += 1
    return cnt


def qpoly(x: int, y: int) -> int:
    return 3 * x * x - 2 * x * y + 3 * y * y


def phase_identity(n: int) -> None:
    for a in range(n):
        for b in range(n):
            for c in range(n):
                left = qpoly(a, b) + qpoly(b, c) + qpoly(c, a)
                right = qpoly(a, c) + qpoly(c, b) + qpoly(b, a)
                if left != right:
                    raise SystemExit(f"phase identity failed at N={n} {(a, b, c)}")


def cat(n: int) -> np.ndarray:
    inv8 = pow(8, -1, n)
    x = np.arange(n)
    xx, yy = np.meshgrid(x, x, indexing="ij")
    quad = (3 * xx * xx - 2 * xx * yy + 3 * yy * yy) % n
    phase = (-inv8 * quad) % n
    return np.exp(2j * PI * phase / n) / np.sqrt(float(n))


def occupation_sum(M: np.ndarray, m: int) -> float:
    n = M.shape[0]
    buckets: dict[tuple[int, ...], complex] = {}
    if m == 1:
        for a in range(n):
            buckets[(a,)] = M[a, a]
    elif m == 2:
        for a in range(n):
            for b in range(n):
                key = tuple(sorted((a, b)))
                buckets[key] = buckets.get(key, 0j) + M[a, b] * M[b, a]
    elif m == 3:
        for a in range(n):
            for b in range(n):
                mab = M[a, b]
                for c in range(n):
                    key = tuple(sorted((a, b, c)))
                    buckets[key] = buckets.get(key, 0j) + mab * M[b, c] * M[c, a]
    else:
        raise SystemExit("occupation sum is implemented for m=1,2,3")
    return float(sum(abs(v) ** 2 for v in buckets.values()))


def closed_form(n: int, m: int) -> float:
    if m == 1:
        return 1.0
    if m == 2:
        return (2 * n - 1) / n
    if m == 3:
        return (6 * n * n - 9 * n + 4) / (n * n)
    raise SystemExit(m)


def weyl(n: int, a: int, b: int) -> np.ndarray:
    a %= n
    b %= n
    inv2 = pow(2, -1, n)
    T = np.zeros((n, n), dtype=np.complex128)
    xs = np.arange(n)
    phase = (b * ((xs + inv2 * a) % n)) % n
    T[xs, (xs + a) % n] = np.exp(2j * PI * phase / n)
    return T


def cache_weyl(n: int):
    cache = {}
    for a, b, _re, _im in MODES:
        key = (a % n, b % n)
        if key not in cache:
            cache[key] = weyl(n, key[0], key[1])
    return cache


def matmul(A: np.ndarray, B: np.ndarray) -> np.ndarray:
    """Triple loop, matching the C++ verifier's addition order."""
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.complex128)
    for i in range(n):
        for k in range(n):
            aik = A[i, k]
            for j in range(n):
                C[i, j] += aik * B[k, j]
    return C


def expm(B: np.ndarray) -> np.ndarray:
    n = B.shape[0]
    norm = 0.0
    for j in range(n):
        col = float(np.sum(np.abs(B[:, j])))
        if col > norm:
            norm = col
    s = max(0, int(math.ceil(math.log2(norm)))) if norm > 1.0 else 0
    scale = 1.0 / (1 << s) if s else 1.0
    acc = np.eye(n, dtype=np.complex128)
    term = np.eye(n, dtype=np.complex128)
    Bs = B * scale
    for k in range(1, 100):
        term = matmul(term, Bs) / k
        acc = acc + term
        if float(np.linalg.norm(term, 1)) < 1e-16:
            break
    for _ in range(s):
        acc = matmul(acc, acc)
    return acc


def splitmix(x: int) -> tuple[int, int]:
    x = (x + 0x9E3779B97F4A7C15) & MASK
    z = x
    z = ((z ^ (z >> 30)) * 0xBF58476D1CE4E5B9) & MASK
    z = ((z ^ (z >> 27)) * 0x94D049BB133111EB) & MASK
    z = (z ^ (z >> 31)) & MASK
    return x, z


def sample_means(n: int) -> list[float]:
    state = SAMPLE_SEED
    cache = cache_weyl(n)
    M = cat(n)
    acc = np.zeros(SAMPLE_MMAX)
    for _draw in range(SAMPLE_DRAWS):
        phis = []
        for _r in range(16):
            state, z = splitmix(state)
            phis.append((z >> 11) * (1.0 / 9007199254740992.0) * 2.0 * PI)
        A = np.zeros((n, n), dtype=np.complex128)
        for r, (rep, (rre, rim), other, (ore, oim)) in enumerate(PAIRS):
            e = np.exp(1j * phis[r])
            crep = (rre + 1j * rim) / 4000.0
            cother = (ore + 1j * oim) / 4000.0
            A += (crep * e) * cache[(rep[0] % n, rep[1] % n)]
            A += (cother / e) * cache[(other[0] % n, other[1] % n)]
        A = 0.5 * (A + A.conj().T)
        K = expm(1j * SAMPLE_ETA * A)
        U = matmul(K, M)
        T = U
        for m in range(SAMPLE_MMAX):
            acc[m] += abs(np.trace(T)) ** 2
            T = matmul(T, U)
    return [float(v / SAMPLE_DRAWS) for v in acc]


def main() -> None:
    energy = symbol_energy()
    if energy != 6603300 or len(MODES) != 32:
        raise SystemExit(f"symbol energy {energy} modes {len(MODES)}")
    for n in (3, 5, 7, 9, 11, 15):
        phase_identity(n)
    max_err = 0.0
    for n in CERT_N:
        M = cat(n)
        flat = float(np.max(np.abs(np.abs(M) - n ** -0.5)))
        if flat > 1e-12:
            raise SystemExit(f"flatness N={n} err {flat}")
        k2 = ker(n, 2)
        k3 = ker(n, 3)
        expect3 = 49 if n % 7 == 0 else 1
        if k2 != 1 or k3 != expect3 or expect3 != math.gcd(14, n) ** 2:
            raise SystemExit(f"kernel N={n} ker2={k2} ker3={k3} expect {expect3}")
        for m, matrix_power in ((2, M @ M), (3, M @ M @ M)):
            pure = abs(np.trace(matrix_power)) ** 2
            expect = k2 if m == 2 else k3
            if abs(pure - expect) > 1e-6:
                raise SystemExit(f"trace closure N={n} m={m} {pure} vs {expect}")
        for m in (1, 2, 3):
            got = occupation_sum(M, m)
            want = closed_form(n, m)
            err = abs(got - want)
            max_err = max(max_err, err)
            if err > ABS_TOL:
                raise SystemExit(f"form N={n} m={m} got {got} want {want}")
        if (2 * n - 1) <= n or (6 * n * n - 9 * n + 4) <= n * n:
            raise SystemExit(f"gap failed at {n}")
        if n % 7 == 0 and not (6 * n * n - 9 * n + 4) < 6 * n * n:
            raise SystemExit(f"upper gap failed at {n}")
    print(f"occupation-max-abs-err {max_err:.3e}")
    if ker(31, 5) != 1:
        raise SystemExit("ker 31,5")
    print(f"kernels-ok odd-N {len(CERT_N)} including 3,5,7")
    for n in SAMPLE_N:
        means = sample_means(n)
        for m, val in enumerate(means, start=1):
            print(f"sample N={n} eta=2 m={m} mean={val:.12f}")
    print("diagonal-phase-form-factor: OK")


if __name__ == "__main__":
    main()
