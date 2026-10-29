#!/usr/bin/env python3
"""Checks for BGS-TRACE-133 (twisted closure formula) and BGS-TRACE-134
(pointwise revival bound on the minimal-period sequence), diagonal kick only.

Exact integer checks (orders, kappa, closure counts, norm-lemma boxes) and
float64 checks of the trace identities. The Monte Carlo rows on the family are
diagnostics of the limit theorem; the explicit bound gives no information at
these dimensions. A pass does not prove BGS-TRACE-005 or BGS-BGS-001.
"""
from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np

SEED = 20261029
LAM = 3 + 2 * math.sqrt(2)


def require(cond: bool, msg: str) -> None:
    if not cond:
        print("FAIL:", msg)
        raise SystemExit(1)


# ---------- exact symbol of the kick (BGS-TRACE-126), diagonal rows ----------
def r_coeff(k: int) -> Fraction:
    return {0: Fraction(1), 1: Fraction(1, 2), -1: Fraction(1, 2), 7: Fraction(-1, 2), -7: Fraction(-1, 2),
            6: Fraction(-1, 4), -6: Fraction(-1, 4), 8: Fraction(-1, 4), -8: Fraction(-1, 4)}.get(k, Fraction(0))


def diag_coeff(k: int) -> tuple[Fraction, Fraction]:
    re = (Fraction(1, 2) if abs(k) == 7 else 0) + r_coeff(k) / 10 - (Fraction(1, 10) if k == 0 else 0)
    im = -(r_coeff(k - 1) - r_coeff(k + 1)) / 200
    return Fraction(re), Fraction(im)


DIAG = [(k, complex(float(diag_coeff(k)[0]), float(diag_coeff(k)[1]))) for k in range(1, 10)
        if diag_coeff(k) != (0, 0)]
SIGMA_D = sum(2 * (diag_coeff(k)[0] ** 2 + diag_coeff(k)[1] ** 2) for k in range(1, 10))
K_MAX = max(k for k, _ in DIAG)


# ---------- cat map, Weyl operators ----------
def e_n(n: int, t) -> np.ndarray:
    return np.exp(2j * np.pi * (np.asarray(t) % n) / n)


def cat(n: int) -> np.ndarray:
    x = np.arange(n)[:, None]
    y = np.arange(n)[None, :]
    inv8 = pow(8, -1, n)
    return e_n(n, (-inv8 * (3 * x * x - 2 * x * y + 3 * y * y)) % n) / np.sqrt(n)


def weyl(n: int, a: int, b: int) -> np.ndarray:
    inv2 = pow(2, -1, n)
    t = np.zeros((n, n), complex)
    x = np.arange(n)
    t[x, (x + a) % n] = e_n(n, b * (x + inv2 * a))
    return t


def spow(d: int) -> tuple[int, int, int, int]:
    a, b, c, e = 1, 0, 0, 1
    for _ in range(d):
        a, b, c, e = 3 * a + 2 * b, 4 * a + 3 * b, 3 * c + 2 * e, 4 * c + 3 * e
    return a, b, c, e  # rows (a,b),(c,e): S^d = [[a,b],[c,e]]


def spow_mod(d: int, n: int) -> tuple[int, int, int, int]:
    a, b, c, e = 1, 0, 0, 1
    for _ in range(d):
        a, b, c, e = (3 * a + 2 * b) % n, (4 * a + 3 * b) % n, (3 * c + 2 * e) % n, (4 * c + 3 * e) % n
    return a % n, b % n, c % n, e % n


def order(n: int) -> int:
    a, b, c, e = 1, 0, 0, 1
    for t in range(1, 6 * n * n):
        a, b, c, e = (3 * a + 2 * b) % n, (4 * a + 3 * b) % n, (3 * c + 2 * e) % n, (4 * c + 3 * e) % n
        if (a, b, c, e) == (1 % n, 0, 0, 1 % n):
            return t
    raise ValueError(n)


def diag_kick(n: int, phi: np.ndarray, eta: float) -> np.ndarray:
    x = np.arange(n)
    f = np.zeros(n)
    for (k, c), p in zip(DIAG, phi):
        f += 2 * np.real(c * np.exp(1j * p) * e_n(n, k * x))
    return np.exp(1j * eta * f)


# ---------- Theorem A ----------
def orbit_vectors(n: int, m: int) -> list[tuple[int, int]]:
    return [(spow(j)[1] % n, spow(j)[3] % n) for j in range(m)]  # S^j e2 = (4y_j, x_j)


def lambda_set(n: int, m: int) -> list[tuple[int, ...]]:
    v = orbit_vectors(n, m)
    p, q = v[m - 2], v[m - 1]
    det_inv = pow((p[0] * q[1] - p[1] * q[0]) % n, -1, n)
    out = []
    for head in itertools.product(range(n), repeat=m - 2):
        r0 = -sum(a * v[j][0] for j, a in enumerate(head)) % n
        r1 = -sum(a * v[j][1] for j, a in enumerate(head)) % n
        x = det_inv * (r0 * q[1] - r1 * q[0]) % n
        y = det_inv * (p[0] * r1 - p[1] * r0) % n
        out.append(head + (x, y))
    return out


def beta(a: tuple[int, ...], n: int) -> int:
    y = [spow(d)[2] // 2 for d in range(len(a))]
    return (-2 * sum(a[i] * a[j] * y[j - i] for i in range(len(a)) for j in range(i + 1, len(a)))) % n


def check_conventions() -> None:
    rng = np.random.default_rng(SEED)
    for n in (5, 7, 11):
        m = cat(n)
        for _ in range(4):
            a, b = (int(z) for z in rng.integers(0, n, 2))
            sv = ((3 * a + 4 * b) % n, (2 * a + 3 * b) % n)
            err = np.abs(m @ weyl(n, a, b) @ m.conj().T - weyl(n, *sv)).max()
            require(err < 1e-12, f"Egorov N={n}")
    print("conventions: Egorov M T(v) M^-1 = T(Sv) at N=5,7,11  ok")


def check_theorem_a() -> None:
    rng = np.random.default_rng(SEED + 1)
    worst = 0.0
    for n, m in ((5, 3), (7, 3), (7, 4), (9, 3), (11, 3), (11, 4), (13, 3), (15, 3), (25, 3), (41, 3), (5, 5), (41, 4)):
        lam = lambda_set(n, m)
        require(len(lam) == n ** (m - 2) and len(set(lam)) == len(lam), f"|Lambda| N={n} m={m}")
        d = np.exp(1j * rng.uniform(0, 2 * np.pi, n))
        dh = np.fft.fft(d) / n
        mm = cat(n)
        prod = np.eye(n, dtype=complex)
        mj = np.eye(n, dtype=complex)
        for _ in range(m):
            prod = prod @ (mj @ np.diag(d) @ mj.conj().T)
            mj = mm @ mj
        lhs = np.trace(prod)
        rhs = n * sum(e_n(n, beta(a, n)) * np.prod([dh[x] for x in a]) for a in lam)
        rel = abs(lhs - rhs) / max(abs(lhs), 1e-300)
        worst = max(worst, rel)
        require(rel < 1e-10, f"Theorem A N={n} m={m} rel={rel}")
        # classical counterpart: N^-2 sum_z prod_j D(q(S^j z)) = sum_Lambda prod dhat (no phase)
        z0 = np.repeat(np.arange(n), n)
        z1 = np.tile(np.arange(n), n)
        pr = np.ones(n * n, complex)
        for _ in range(m):
            pr *= d[z0]
            z0, z1 = (3 * z0 + 4 * z1) % n, (2 * z0 + 3 * z1) % n
        cl = sum(np.prod([dh[x] for x in a]) for a in lam)
        require(abs(pr.mean() - cl) < 1e-10, f"classical counterpart N={n} m={m}")
    print(f"Theorem A: 12 (N,m) cases, |Lambda_m|=N^(m-2), max rel err {worst:.1e}  ok")
    # scalar return
    for n in (7, 41, 35, 239):
        t = order(n)
        ev = np.linalg.eigvals(cat(n))
        trmt = np.sum(ev ** t)
        require(abs(abs(trmt) - n) < 1e-8, f"|Tr M^t|=N at {n}")
        d = diag_kick(n, rng.uniform(0, 2 * np.pi, len(DIAG)), 0.7)
        u_tr = np.sum(np.linalg.eigvals(d[:, None] * cat(n)) ** t)
        mm = cat(n)
        prod = np.eye(n, dtype=complex)
        mj = np.eye(n, dtype=complex)
        for _ in range(t):
            prod = prod @ (mj @ np.diag(d) @ mj.conj().T)
            mj = mm @ mj
        require(abs(u_tr - trmt / n * np.trace(prod)) < 1e-8 * n, f"scalar return {n}")
    print("scalar return: |Tr M^t| = N and Tr U^t = (Tr M^t/N) Tr(prod D_j) at N=7,41,35,239  ok")


def check_phase_average() -> None:
    """Lemma (standard Kluyver/Jacobi-Anger average): exact J0 path sum vs product trapezoid in phi (2 modes)."""
    from scipy.special import j0
    modes = [DIAG[4], DIAG[0]]  # k=7 (|c|=0.45) and k=1
    for n, m, eta in ((7, 2, 1.3), (7, 3, 1.3), (11, 2, 2.0)):
        mm = cat(n)
        xs = list(itertools.product(range(n), repeat=m))
        kern = np.array([np.prod([mm[x[j], x[(j + 1) % m]] for j in range(m)]) for x in xs])
        vr = [np.array([np.sum(e_n(n, k * np.array(x))) for x in xs]) for k, _ in modes]
        tot = 0j
        for i in range(len(xs)):
            w = np.ones(len(xs))
            for (k, c), v in zip(modes, vr):
                w = w * j0(2 * eta * abs(c) * np.abs(v[i] - v))
            tot += kern[i] * np.sum(np.conj(kern) * w)
        g = 64
        grid = 2 * np.pi * np.arange(g) / g
        quad = 0.0
        for p1 in grid:
            for p2 in grid:
                x = np.arange(n)
                f = sum(2 * np.real(c * np.exp(1j * p) * e_n(n, k * x)) for (k, c), p in zip(modes, (p1, p2)))
                quad += abs(np.sum(np.linalg.eigvals(np.exp(1j * eta * f)[:, None] * mm) ** m)) ** 2
        quad /= g * g
        require(abs(tot.real - quad) < 1e-9 * max(1, quad), f"J0 identity N={n} m={m}")
    print("phase average: J0 path sum = trapezoid quadrature (N=7 m=2,3; N=11 m=2)  ok")


# ---------- norm lemma and dichotomy ----------
def is_relation(c) -> bool:
    a = b = 0
    pa, pb = 1, 0
    for cj in c:
        a += cj * pa
        b += cj * pb
        pa, pb = -pb, pa + 6 * pb
    return a == 0 and b == 0


def closes_mod(c, n: int) -> bool:
    a = b = 0
    pa, pb = 1, 0
    for cj in c:
        a += cj * pa
        b += cj * pb
        pa, pb = -pb, pa + 6 * pb
    return a % n == 0 and b % n == 0


def check_norm_lemma() -> None:
    rows = []
    for n, length, amax in ((41, 3, 5), (239, 4, 6), (239, 5, 5), (1189, 5, 8)):
        require(amax * amax * LAM ** length <= 4 * n * n, f"window hypothesis {n}")
        nz = rel = 0
        for c in itertools.product(range(-amax, amax + 1), repeat=length):
            if any(c) and closes_mod(c, n):
                nz += 1
                require(is_relation(c), f"Lemma 1 violated at N={n}: {c}")
                rel += 1
        rows.append((n, length, amax, nz))
    require(not is_relation((-7, 1, -7)) and closes_mod((-7, 1, -7), 41), "near-sharpness witness")
    print("Lemma 1 exhaustive (N,L,A,closures):", rows, " ok; witness (-7,1,-7) at N=41 outside the window")


def check_dichotomy(n: int, amax: int, expect_case1: int) -> None:
    t = order(n)
    v = orbit_vectors(n, t)
    gthr = t - math.log(4 * n * n / amax ** 2) / math.log(LAM)
    ga = int(math.floor(2 * math.log(amax / 2) / math.log(LAM))) if amax > 2 else 0
    p, q = v[t - 2], v[t - 1]
    det_inv = pow((p[0] * q[1] - p[1] * q[0]) % n, -1, n)
    case1 = total = 0
    for head in itertools.product(range(-amax, amax + 1), repeat=t - 2):
        r0 = -sum(a * v[j][0] for j, a in enumerate(head)) % n
        r1 = -sum(a * v[j][1] for j, a in enumerate(head)) % n
        x = det_inv * (r0 * q[1] - r1 * q[0]) % n
        y = det_inv * (p[0] * r1 - p[1] * r0) % n
        x = x - n if x > n // 2 else x
        y = y - n if y > n // 2 else y
        if abs(x) > amax or abs(y) > amax:
            continue
        a = head + (x, y)
        if not any(a):
            continue
        total += 1
        nzi = [j for j in range(t) if a[j]]
        gaps = [(nzi[(i + 1) % len(nzi)] - nzi[i] - 1) % t if len(nzi) > 1 else t - 1 for i in range(len(nzi))]
        gi = max(range(len(nzi)), key=lambda i: gaps[i])
        if gaps[gi] < gthr:
            continue
        case1 += 1
        start = nzi[(gi + 1) % len(nzi)]
        rot = [a[(start + j) % t] for j in range(t)]
        require(is_relation(rot), f"Case 1 not a relation {a}")
        nzr = [j for j in range(t) if rot[j]]
        blocks = [[nzr[0]]]
        for j in nzr[1:]:
            if j - blocks[-1][-1] - 1 <= ga:
                blocks[-1].append(j)
            else:
                blocks.append([j])
        for b in blocks:
            seg = [0] * (b[-1] + 1)
            for j in b:
                seg[j] = rot[j]
            require(len(b) >= 3 and is_relation(seg), f"run lemma {a}")
    require(case1 == expect_case1, f"Case-1 count N={n} A={amax}: {case1}")
    print(f"dichotomy N={n} t={t} A={amax}: elements={total} case1={case1} (runs checked) case2={total - case1}  ok")


# ---------- Theorem C bound ----------
def explicit_bound(n: int, t: int, eta: float) -> float:
    w_r = [2 * eta * abs(c) for _, c in DIAG]
    big_w = sum(w_r)
    from scipy.special import j0
    jprod = float(np.prod([j0(w) for w in w_r]))
    rho = math.expm1(big_w)
    best = math.inf
    tail = [0.0] * 6002
    terms = [math.exp(d * math.log(big_w) - math.lgamma(d + 1)) for d in range(6001)]
    for d in range(6000, -1, -1):
        tail[d] = tail[d + 1] + terms[d]
    a = 2
    while a <= min(n // 2 - 1, 9 * 5000):
        tau = tail[min(a // K_MAX + 1, 6000)]
        e_t = t * tau * math.exp(big_w * (t - 1))
        thr = t - (math.log(4) + 2 * math.log(n) - 2 * math.log(a)) / math.log(LAM)
        gstar = max(math.ceil(thr) - 1, 0)
        s0 = max(math.ceil(t / (gstar + 1)), 1)
        e_d = sum(math.exp(math.lgamma(t + 1) - math.lgamma(s + 1) - math.lgamma(t - s + 1) + s * math.log(rho))
                  for s in range(s0, t + 1))
        ga = math.floor(2 * math.log(a / 2) / math.log(LAM)) if a > 2 else 0
        q = (ga + 1) * rho
        e_r = math.inf if q >= 1 else math.expm1(t * math.log1p((ga + 1) ** 2 * rho ** 3 / (1 - q)))
        best = min(best, e_t + e_d + e_r)
        a = a + 1 if a < 64 else int(a * 1.1)
    require(jprod > 0, "J positive")
    return best


def family_member(t: int, kappa: int) -> int:
    x = spow(t)[0]
    n2 = (2 * x - 2) // kappa
    n = math.isqrt(n2)
    require(n * n == n2 and (2 * x - 2) % kappa == 0, f"family t={t}")
    return n


def check_theorem_c() -> None:
    require(SIGMA_D == Fraction(13203, 32000), "sigma_d")
    fam4 = [family_member(t, 4) for t in (3, 5, 7, 9, 11, 13, 15)]
    fam32 = [family_member(t, 32) for t in (6, 10, 14)]
    require(fam4 == [7, 41, 239, 1393, 8119, 47321, 275807] and fam32 == [35, 1189, 40391], "families")
    for n, t in zip(fam4[:5] + fam32[:2], (3, 5, 7, 9, 11, 6, 10)):
        require(order(n) == t, f"order {n}")
    print("families (kappa=4):", fam4, " (kappa=32):", fam32, " orders ok; sigma_d = 13203/32000")
    b41 = explicit_bound(41, 5, math.sqrt(0.25 / (float(SIGMA_D) * 5)))
    n501 = family_member(501, 4)
    b501 = explicit_bound(n501, 501, math.sqrt(0.25 / (float(SIGMA_D) * 501)))
    print(f"explicit bound lam=1/4: N=41 -> {b41:.3g} (no information); t=501, log10 N={math.log10(n501):.0f} -> {b501:.3g}")
    require(b41 > 1 and b501 < 1, "bound regime")
    # diagnostics of the limit theorem (not implied by the bound at these N)
    rng = np.random.default_rng(SEED + 2)
    prev = math.inf
    for n in (41, 239):
        t = order(n)
        eta = math.sqrt(1.0 / (float(SIGMA_D) * t))
        mm = cat(n)
        trmt = np.sum(np.linalg.eigvals(mm) ** t)
        dev = 0.0
        for _ in range(100):
            d = diag_kick(n, rng.uniform(0, 2 * np.pi, len(DIAG)), eta)
            r = np.sum(np.linalg.eigvals(d[:, None] * mm) ** t) / trmt
            dev = max(dev, abs(r - d.mean() ** t))
        print(f"diagnostic N={n} t={t} lam=1: max_phi |R - dhat0^t| = {dev:.3e} (100 draws)")
        require(dev < prev, "deviation should decrease along the family (diagnostic)")
        prev = dev


def main() -> None:
    check_conventions()
    check_theorem_a()
    check_phase_average()
    check_norm_lemma()
    check_dichotomy(239, 5, 28)
    check_dichotomy(1393, 5, 108)
    check_theorem_c()
    print("PASS")


if __name__ == "__main__":
    main()
