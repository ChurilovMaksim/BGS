#!/usr/bin/env python3
"""Exact and floating checks for BGS-TRACE-126.

Arithmetic. Symbol coefficients, the Hilbert--Schmidt energy, the strict
majorant, the parity defect and the position-conjugation reversal defect are
exact `fractions.Fraction` values. The prime-revival coefficients at the
orders modulo 3, 5, 7 and 41 are exact rational identities, with the
zero-mode energy sigma_0(p) kept at the three small primes. The cyclotomic witness that the fixed-kick linear
coefficient is nonzero at N=11, m=3 is exact integer arithmetic in
Q(i)(zeta_11).

Floating point. Matrix traces of the cat map and of Weyl operators are
compared with the Gauss-sum closure in float64. A pass on that comparison is
a finite numerical check, not a proof of the trace formula. The formula is
proved in mathematics/fixed-map/interaction_phase_form_factor.md.

Coverage. Odd N in {3,5,7,9,11,15,21,25,27,35} and powers m=1..6 for the
trace closure, on every symbol mode and on the window [-2,2]^2. The
interaction picture, the order-two coefficient and a two-pair torus average
are checked at the dimensions named in the receipt. Symmetry defects are
folded for every odd N from 3 through 77.

Non-claims. A pass does not prove BGS-TRACE-005 or BGS-BGS-001, a revival
limit, or the absence of every N-dependent antiunitary.
"""
from __future__ import annotations

import math
from fractions import Fraction

import numpy as np

S = np.array([[3, 4], [2, 3]], dtype=object)
S_INV = np.array([[3, -4], [-2, 3]], dtype=object)
TRACE_NS = (3, 5, 7, 9, 11, 15, 21, 25, 27, 35)
TRACE_POWERS = range(1, 7)
FLOAT_ABS = 1e-8


def r_coeff(k: int) -> Fraction:
    if k == 0:
        return Fraction(1)
    if abs(k) == 1:
        return Fraction(1, 2)
    if abs(k) == 7:
        return Fraction(-1, 2)
    if abs(k) in (6, 8):
        return Fraction(-1, 4)
    return Fraction(0)


def f_coeff(k: int, ell: int) -> tuple[Fraction, Fraction]:
    """Fourier coefficient of f-1/10, matching fCoeff(k, ell) in TraceStatement."""
    re = im = Fraction(0)
    if ell == 0:
        if abs(k) == 7:
            re += Fraction(1, 2)
        re += r_coeff(k) / 10
        im += -(r_coeff(k - 1) - r_coeff(k + 1)) / 200
        if k == 0:
            re -= Fraction(1, 10)
    elif ell == 1:
        rc = r_coeff(k)
        re += rc * Fraction(-3, 1000)
        im += rc * Fraction(-4, 1000)
    elif ell == -1:
        rc = r_coeff(k)
        re += rc * Fraction(-3, 1000)
        im += rc * Fraction(4, 1000)
    return re, im


def modes() -> list[tuple[tuple[int, int], Fraction, Fraction]]:
    out = []
    for k in range(-9, 10):
        for ell in range(-1, 2):
            re, im = f_coeff(k, ell)
            if re == 0 and im == 0:
                continue
            # T(a,b) with a=ell, b=k.
            out.append(((ell, k), re, im))
    return out


MODES = modes()


def mat_pow(m: int, matrix=S):
    A = np.array([[1, 0], [0, 1]], dtype=object)
    base = matrix
    e = m
    # square-and-multiply, m nonnegative
    acc = np.array([[1, 0], [0, 1]], dtype=object)
    while e:
        if e & 1:
            acc = base @ acc
        base = base @ base
        e >>= 1
    return acc


def apply_int(A, v: tuple[int, int]) -> tuple[int, int]:
    return (
        int(A[0, 0] * v[0] + A[0, 1] * v[1]),
        int(A[1, 0] * v[0] + A[1, 1] * v[1]),
    )


def omega(u: tuple[int, int], v: tuple[int, int]) -> int:
    return u[0] * v[1] - u[1] * v[0]


def eN(N: int, t: int) -> complex:
    return np.exp(2j * np.pi * (int(t) % N) / N)


def weyl(N: int, a: int, b: int) -> np.ndarray:
    a %= N
    b %= N
    inv2 = pow(2, -1, N)
    T = np.zeros((N, N), dtype=np.complex128)
    xs = np.arange(N)
    phase = (b * ((xs + inv2 * a) % N)) % N
    T[xs, (xs + a) % N] = np.exp(2j * np.pi * phase / N)
    return T


def cat(N: int) -> np.ndarray:
    inv8 = pow(8, -1, N)
    x = np.arange(N)
    X, Y = np.meshgrid(x, x, indexing="ij")
    quad = (3 * X * X - 2 * X * Y + 3 * Y * Y) % N
    phase = (-inv8 * quad) % N
    return np.exp(2j * np.pi * phase / N) / np.sqrt(N)


def expm(B: np.ndarray) -> np.ndarray:
    n = B.shape[0]
    norm = np.linalg.norm(B, 1)
    s = max(0, int(np.ceil(np.log2(norm + 1e-16))))
    Bs = B / (2**s) if s else B
    term = np.eye(n, dtype=np.complex128)
    acc = term.copy()
    for k in range(1, 60):
        term = term @ Bs / k
        acc = acc + term
        if np.linalg.norm(term, 1) < 1e-18:
            break
    for _ in range(s):
        acc = acc @ acc
    return acc


def preimage_table(N: int, m: int) -> tuple[dict[tuple[int, int], tuple[int, int]], int]:
    A = mat_pow(m)
    table: dict[tuple[int, int], tuple[int, int]] = {}
    ker = 0
    for x in range(N):
        for y in range(N):
            img = apply_int(A, (x, y))
            v = ((x - img[0]) % N, (y - img[1]) % N)
            if v == (0, 0):
                ker += 1
            table.setdefault(v, (x, y))
    return table, ker


def psi_of(N: int, m: int, w: tuple[int, int]) -> int:
    Smw = apply_int(mat_pow(m), w)
    inv2 = pow(2, -1, N)
    return (inv2 * (omega(w, Smw) % N)) % N


def trace_formula(N: int, m: int, v: tuple[int, int], Z: complex, table) -> complex:
    w = table.get((v[0] % N, v[1] % N))
    if w is None:
        return 0j
    return eN(N, psi_of(N, m, w)) * Z


def mod_norm(v: tuple[int, int]) -> int:
    return max(abs(v[0]), abs(v[1]))


def isqrt_majorant(re: Fraction, im: Fraction) -> Fraction:
    mag2 = re * re + im * im
    p, q = mag2.numerator, mag2.denominator
    # sqrt(p/q) < (isqrt(p*q)+1)/q
    return Fraction(math.isqrt(p * q) + 1, q)


def symbol_certificate() -> dict:
    assert len(MODES) == 32
    coeff = {v: (re, im) for v, re, im in MODES}
    energy = Fraction(0)
    imag_energy = Fraction(0)
    scale = 4000
    squares = 0
    for re, im in coeff.values():
        energy += re * re + im * im
        imag_energy += im * im
        R = re * scale
        I = im * scale
        assert R.denominator == 1 and I.denominator == 1
        squares += int(R) * int(R) + int(I) * int(I)
    # Hermitian symmetry and the integer scale.
    for v, (re, im) in coeff.items():
        ore, oim = coeff[(-v[0], -v[1])]
        assert ore == re and oim == -im
    assert squares == 6603300
    assert energy == Fraction(66033, 160000)
    majorants = [isqrt_majorant(re, im) for _, re, im in MODES]
    majorant = sum(majorants, Fraction(0))
    assert majorant == Fraction(184981, 160000)
    assert energy < majorant * majorant
    # (7,0) in (k, ell) is T(a,b)=(0,7).
    re7, im7 = coeff[(0, 7)]
    assert re7 == Fraction(9, 20) and im7 == 0
    parity_fraction = imag_energy / energy
    # Reversal defect on Z^2. The position-basis conjugation sends the
    # coefficient of T(w) to the conjugate of the coefficient of T(sigma w),
    # sigma(a,b)=(a,-b). The cat-map reversal sends it to the coefficient of
    # T(S w). Both functions are extended by zero outside the 32 modes.
    labels = set()
    for a, b in coeff:
        labels.add((a, -b))
        labels.add(apply_int(S_INV, (a, b)))
    defect = Fraction(0)
    for w in labels:
        sr, si = coeff.get((w[0], -w[1]), (Fraction(0), Fraction(0)))
        sw = apply_int(S, w)
        tr, ti = coeff.get(sw, (Fraction(0), Fraction(0)))
        dr, di = sr - tr, -si - ti
        defect += dr * dr + di * di
    assert defect > 0 and imag_energy > 0
    return {
        "modes": 32,
        "energy": energy,
        "imag_energy": imag_energy,
        "parity_fraction": parity_fraction,
        "majorant": majorant,
        "reversal_defect": defect,
        "squares": squares,
        "majorant_terms": majorants,
    }


def fold_coeff(N: int) -> dict[tuple[int, int], tuple[Fraction, Fraction]]:
    acc: dict[tuple[int, int], tuple[Fraction, Fraction]] = {}
    for (a, b), re, im in MODES:
        key = (a % N, b % N)
        pr, pi = acc.get(key, (Fraction(0), Fraction(0)))
        acc[key] = (pr + re, pi + im)
    return acc


def parity_defect_mod(N: int) -> Fraction:
    """sum_w |c_{-w} - c_w|^2 after folding labels modulo N."""
    acc = fold_coeff(N)

    def get(a: int, b: int) -> tuple[Fraction, Fraction]:
        return acc.get((a % N, b % N), (Fraction(0), Fraction(0)))

    labels = set(acc)
    for a, b in list(acc):
        labels.add(((-a) % N, (-b) % N))
    total = Fraction(0)
    for a, b in labels:
        re, im = get(a, b)
        ore, oim = get(-a, -b)
        total += (ore - re) ** 2 + (oim - im) ** 2
    return total


def reversal_defect_mod(N: int) -> Fraction:
    acc = fold_coeff(N)

    def get(a: int, b: int) -> tuple[Fraction, Fraction]:
        return acc.get((a % N, b % N), (Fraction(0), Fraction(0)))

    total = Fraction(0)
    for a in range(N):
        for b in range(N):
            sr, si = get(a, -b)
            sw = apply_int(S, (a, b))
            tr, ti = get(sw[0], sw[1])
            # conj(c_sigma) - c_S
            total += (sr - tr) ** 2 + (-si - ti) ** 2
    return total


def check_symmetries(cert: dict) -> dict:
    # N > 18 separates the parity labels. N > 78 separates the reversal labels,
    # whose integer coordinates lie in [-39, 39].
    stable_parity = 4 * cert["imag_energy"]
    assert stable_parity == Fraction(663, 1000000)
    assert cert["reversal_defect"] == Fraction(66031, 80000)
    for N in range(3, 79, 2):
        parity = parity_defect_mod(N)
        reversal = reversal_defect_mod(N)
        if N == 7:
            assert parity == 0 and reversal == 0
            folded = fold_coeff(7)
            assert (0, 0) in folded
            for key, (re, im) in folded.items():
                if key == (0, 0):
                    assert re == Fraction(9, 10) and im == 0
                else:
                    assert re == 0 and im == 0, (key, re, im)
        else:
            assert parity > 0 and reversal > 0, N
        if N >= 19:
            assert parity == stable_parity
    for N in (79, 81, 105):
        assert parity_defect_mod(N) == stable_parity
        assert reversal_defect_mod(N) == cert["reversal_defect"]
    matrix_symmetry_spotcheck(cert)
    return {
        "parity_fraction": str(cert["parity_fraction"]),
        "imag_energy": str(cert["imag_energy"]),
        "stable_parity_defect": str(stable_parity),
        "reversal_defect": str(cert["reversal_defect"]),
        "only_classical_symmetry_dimension": 7,
    }


def matrix_symmetry_spotcheck(cert: dict) -> None:
    """Compare folded coefficient defects with literal matrix commutators."""
    for N in (7, 9, 11, 15):
        M = cat(N)
        P = np.zeros((N, N), dtype=np.complex128)
        for x in range(N):
            P[x, (-x) % N] = 1
        A = np.zeros((N, N), dtype=np.complex128)
        for (a, b), re, im in MODES:
            A += complex(float(re), float(im)) * weyl(N, a, b)
        parity_hs = np.linalg.norm(P @ A @ P - A) ** 2
        assert abs(parity_hs - N * float(parity_defect_mod(N))) < 1e-8
        assert np.linalg.norm(P @ M - M @ P) < 1e-8
        reversal_hs = np.linalg.norm(np.conjugate(A) - M.conj().T @ A @ M) ** 2
        assert abs(reversal_hs - N * float(reversal_defect_mod(N))) < 1e-8
        assert np.linalg.norm(np.conjugate(M) - M.conj().T) < 1e-8
        if N == 7:
            assert parity_hs < 1e-8 and reversal_hs < 1e-8
            assert np.linalg.norm(A - 0.9 * np.eye(N)) < 1e-8
            eta = 0.2
            U = expm(1j * eta * A) @ M
            assert np.linalg.norm(P @ U @ P - U) < 1e-8
            assert np.linalg.norm(np.conjugate(U) - np.linalg.inv(U)) < 1e-7


def check_cocycle_egorov_gauge() -> dict:
    worst = {"cocycle": 0.0, "egorov": 0.0, "gauge": 0.0, "unitary": 0.0}
    samples = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 3), (4, -1), (5, 6), (-2, 4)]
    for N in (5, 9, 11, 15, 21):
        M = cat(N)
        worst["unitary"] = max(worst["unitary"], float(np.linalg.norm(M.conj().T @ M - np.eye(N))))
        inv2 = pow(2, -1, N)
        for a, b in samples:
            for c, d in samples:
                left = weyl(N, a, b) @ weyl(N, c, d)
                phase = eN(N, (inv2 * ((a * d - b * c) % N)) % N)
                right = phase * weyl(N, a + c, b + d)
                worst["cocycle"] = max(worst["cocycle"], float(np.linalg.norm(left - right)))
            left = M @ weyl(N, a, b) @ M.conj().T
            na, nb = apply_int(S, (a, b))
            worst["egorov"] = max(worst["egorov"], float(np.linalg.norm(left - weyl(N, na, nb))))
            raw = weyl(N, a, b)
            aa, bb = a % N, b % N
            KR = np.zeros((N, N), dtype=np.complex128)
            xs = np.arange(N)
            # Integer-lift identity uses the unreduced product ab, then the
            # reduced operator. The checked samples have a,b already small.
            KR[xs, (xs + aa) % N] = np.exp(1j * np.pi * a * b / N) * np.exp(2j * np.pi * bb * xs / N)
            worst["gauge"] = max(worst["gauge"], float(np.linalg.norm(raw - ((-1) ** (a * b)) * KR)))
    for key, val in worst.items():
        assert val < 1e-8, (key, val)
    return worst


def check_trace_closure() -> dict:
    worst_trace = 0.0
    worst_ker = 0.0
    window = [(a, b) for a in range(-2, 3) for b in range(-2, 3)]
    for N in TRACE_NS:
        M = cat(N)
        for m in TRACE_POWERS:
            table, ker = preimage_table(N, m)
            Mm = np.linalg.matrix_power(M, m)
            Z = np.trace(Mm)
            worst_ker = max(worst_ker, abs(abs(Z) ** 2 - ker))
            vs = window + [v for v, _, _ in MODES]
            for v in vs:
                pred = trace_formula(N, m, v, Z, table)
                got = np.trace(weyl(N, v[0], v[1]) @ Mm)
                worst_trace = max(worst_trace, abs(pred - got))
    assert worst_trace < FLOAT_ABS
    assert worst_ker < FLOAT_ABS
    return {"trace_abs": worst_trace, "kernel_abs": worst_ker}


def order_two_coefficient(N: int, m: int, table, Z: complex) -> complex:
    sigma = 0.0
    image_sum = 0.0
    off = 0j
    inv2 = pow(2, -1, N)
    Sm = mat_pow(m)
    for (a, b), re, im in MODES:
        c2 = float(re * re + im * im)
        sigma += c2
        if (a % N, b % N) in table:
            image_sum += c2
        v = (a, b)
        for j in range(m):
            Sj = apply_int(mat_pow(j), v)
            for k in range(j + 1, m):
                Sk = apply_int(mat_pow(k), v)
                u = ((Sj[0] - Sk[0]) % N, (Sj[1] - Sk[1]) % N)
                w = table.get(u)
                if w is None:
                    continue
                delta = k - j
                Sd = apply_int(mat_pow(delta), v)
                coc = (-inv2 * (omega(v, Sd) % N)) % N
                theta = eN(N, coc) * eN(N, psi_of(N, m, w))
                off += c2 * theta
    return (abs(Z) ** 2) * (m**2 * image_sum - m * sigma - 2 * np.real(off))


def matrix_order_two(N: int, m: int, Mm: np.ndarray) -> complex:
    """Assemble D2 from literal matrix traces of balanced words."""
    Ts = {}

    def T(v):
        key = (v[0] % N, v[1] % N)
        if key not in Ts:
            Ts[key] = weyl(N, v[0], v[1])
        return Ts[key]

    sigma = 0.0
    image_part = 0.0
    off = 0j
    Z = np.trace(Mm)
    for (a, b), re, im in MODES:
        c2 = float(re * re + im * im)
        sigma += c2
        tr = np.trace(T((a, b)) @ Mm)
        image_part += c2 * abs(tr) ** 2
        v = (a, b)
        for j in range(m):
            Sj = apply_int(mat_pow(j), v)
            for k in range(j + 1, m):
                Sk = apply_int(mat_pow(k), v)
                prod = T(Sj) @ T((-Sk[0], -Sk[1]))
                off += c2 * np.trace(prod @ Mm)
    # E|t1|^2 / eta^2 = image_part * m^2, and the t2 contribution is
    # -| from the identity words and the off-diagonal traces.
    # Tr(E A_j^2 M^m) = sigma * Z, halved, times (i)^2 = -1, then 2 Re conj(Z).
    t2_trace = (m * sigma / 2) * Z + off
    e_t2 = -(t2_trace)  # coefficient of eta^2 in E Tr(W2 M^m), since (i)^2=-1
    # 2 Re(conj(Z) E f2) + E|f1|^2
    return m**2 * image_part + 2 * np.real(np.conjugate(Z) * e_t2)


def check_order_two() -> dict:
    points = [(3, 4), (5, 1), (5, 2), (5, 6), (7, 1), (7, 3), (9, 2), (11, 1), (11, 3), (15, 2)]
    worst = 0.0
    for N, m in points:
        table, ker = preimage_table(N, m)
        M = cat(N)
        Mm = np.linalg.matrix_power(M, m)
        Z = np.trace(Mm)
        closed = order_two_coefficient(N, m, table, Z)
        direct = matrix_order_two(N, m, Mm)
        worst = max(worst, abs(closed - direct))
        assert abs(abs(Z) ** 2 - ker) < FLOAT_ABS
    assert worst < 1e-6
    return {"order_two_abs": worst}


def check_interaction() -> dict:
    worst = 0.0
    for N, m, eta in ((9, 3, 0.07), (11, 3, 0.04), (11, 4, 0.02), (15, 2, 0.05)):
        M = cat(N)
        A = np.zeros((N, N), dtype=np.complex128)
        for (a, b), re, im in MODES:
            A += complex(float(re), float(im)) * weyl(N, a, b)
        assert np.linalg.norm(A - A.conj().T) < 1e-8
        U = expm(1j * eta * A) @ M
        W = np.eye(N, dtype=np.complex128)
        Aj = A.copy()
        for _ in range(m):
            W = W @ expm(1j * eta * Aj)
            Aj = M @ Aj @ M.conj().T
        got = np.linalg.matrix_power(U, m)
        worst = max(worst, float(np.linalg.norm(got - W @ np.linalg.matrix_power(M, m))))
    assert worst < 1e-8
    return {"interaction_abs": worst}


def check_fixed_linear() -> dict:
    N, m = 11, 3
    table, ker = preimage_table(N, m)
    M = cat(N)
    Mm = np.linalg.matrix_power(M, m)
    Z = np.trace(Mm)
    Sigma = 0j
    for (a, b), re, im in MODES:
        w = table.get((a % N, b % N))
        if w is None:
            continue
        Sigma += complex(float(re), float(im)) * eN(N, psi_of(N, m, w))
    lin = -2 * m * ker * float(np.imag(Sigma))
    A = sum(
        (complex(float(re), float(im)) * weyl(N, a, b) for (a, b), re, im in MODES),
        np.zeros((N, N), dtype=np.complex128),
    )

    def tr2(h: float) -> float:
        return abs(np.trace(np.linalg.matrix_power(expm(1j * h * A) @ M, m))) ** 2

    h = 1e-4
    num = (tr2(h) - tr2(-h)) / (2 * h)
    assert abs(num - lin) < 5e-3
    assert abs(lin) > 1.0
    witness = cyclotomic_witness(table)
    assert witness["nonzero"]
    return {"linear_coefficient": lin, "imag_sigma": float(np.imag(Sigma)), "ker": ker, **witness}


def mul_zeta(coeffs: list[int]) -> list[int]:
    # multiply by zeta, reduce by zeta^10 = -1 - zeta - ... - zeta^9
    out = [0] * 10
    for j in range(10):
        out[j] -= coeffs[9]
    for j in range(9):
        out[j + 1] += coeffs[j]
    return out


def zeta_power(k: int) -> list[int]:
    coeffs = [0] * 10
    coeffs[0] = 1
    k %= 11
    for _ in range(k):
        coeffs = mul_zeta(coeffs)
    return coeffs


def add_scaled(acc: list[int], coeffs: list[int], scale: int) -> None:
    for i in range(10):
        acc[i] += scale * coeffs[i]


def cyclotomic_witness(table) -> dict:
    """4000(Sigma - conjugate Sigma) as an element of Z[i][zeta_11]/(Phi_11)."""
    N, m = 11, 3
    re_c = [0] * 10
    im_c = [0] * 10
    for (a, b), re, im in MODES:
        w = table.get((a % N, b % N))
        if w is None:
            continue
        psi = psi_of(N, m, w)
        R = int(re * 4000)
        I = int(im * 4000)
        zp = zeta_power(psi)
        zm = zeta_power(-psi)
        # (R+i I) zeta^psi - (R-i I) zeta^{-psi}
        # real: R (zp - zm)  +  I (0 from i*(zp) wait)
        # (R+iI) zp = R zp + i I zp
        # (R-iI) zm = R zm - i I zm
        # difference real part: R(zp-zm) - (-I? )
        # real: R*zp - R*zm
        # imag: I*zp - (-I*zm) = I(zp+zm)
        # stored as real_poly + i * imag_poly
        add_scaled(re_c, zp, R)
        add_scaled(re_c, zm, -R)
        add_scaled(im_c, zp, I)
        add_scaled(im_c, zm, I)
    nonzero = any(re_c) or any(im_c)
    return {"nonzero": nonzero, "cyclotomic_re": re_c, "cyclotomic_im": im_c}


def two_pair_average() -> dict:
    """Exact 5-by-5 average of a degree-2 trigonometric polynomial, two pairs."""
    N, m = 11, 2
    # representatives: first two pairs in the mode list
    pairs = []
    seen = set()
    for (a, b), re, im in MODES:
        if (a, b) in seen or (-a, -b) in seen:
            continue
        pairs.append((a, b))
        seen.add((a, b))
        if len(pairs) == 2:
            break
    selected = set()
    for a, b in pairs:
        selected.add((a, b))
        selected.add((-a, -b))
    reduced = [(v, re, im) for v, re, im in MODES if v in selected]

    def build(phi: np.ndarray) -> np.ndarray:
        A = np.zeros((N, N), dtype=np.complex128)
        for (a, b), re, im in reduced:
            if (a, b) in pairs:
                sign = 1
                p = phi[pairs.index((a, b))]
            else:
                sign = -1
                p = phi[pairs.index((-a, -b))]
            A += complex(float(re), float(im)) * np.exp(1j * sign * p) * weyl(N, a, b)
        return A

    M = cat(N)
    h = 2e-3

    def second(phi: np.ndarray) -> float:
        A = build(phi)

        def tr2(t: float) -> float:
            return abs(np.trace(np.linalg.matrix_power(expm(1j * t * A) @ M, m))) ** 2

        return (tr2(h) + tr2(-h) - 2 * tr2(0.0)) / (2 * h * h)

    grid = np.linspace(0.0, 2 * np.pi, 5, endpoint=False)
    acc = 0.0
    for p0 in grid:
        for p1 in grid:
            acc += second(np.array([p0, p1]))
    acc /= 25.0
    # closed form on the reduced symbol
    table, _ker = preimage_table(N, m)
    Mm = np.linalg.matrix_power(M, m)
    Z = np.trace(Mm)
    # temporarily evaluate with the reduced modes by a local copy of the sum
    sigma = 0.0
    image_sum = 0.0
    off = 0j
    inv2 = pow(2, -1, N)
    for (a, b), re, im in reduced:
        c2 = float(re * re + im * im)
        sigma += c2
        if (a % N, b % N) in table:
            image_sum += c2
        v = (a, b)
        for j in range(m):
            Sj = apply_int(mat_pow(j), v)
            for k in range(j + 1, m):
                Sk = apply_int(mat_pow(k), v)
                u = ((Sj[0] - Sk[0]) % N, (Sj[1] - Sk[1]) % N)
                w = table.get(u)
                if w is None:
                    continue
                Sd = apply_int(mat_pow(k - j), v)
                coc = (-inv2 * (omega(v, Sd) % N)) % N
                off += c2 * eN(N, coc) * eN(N, psi_of(N, m, w))
    closed = (abs(Z) ** 2) * (m**2 * image_sum - m * sigma - 2 * np.real(off))
    err = abs(acc - closed)
    assert err < 2e-3
    return {"two_pair_abs": err, "two_pair_closed": float(np.real(closed)), "two_pair_grid": acc}


REVIVALS = (
    # N, order, sigma_0, modes (ell, k) congruent to 0, D2
    (3, 4, Fraction(81, 64000), {(0, 6), (0, -6), (0, 9), (0, -9)}, Fraction(-1184949, 80000)),
    (5, 6, Fraction(1, 320000), {(0, 5), (0, -5)}, Fraction(-79239, 1280)),
    (7, 3, Fraction(81, 200), {(0, 7), (0, -7)}, Fraction(-181251, 160000)),
    (41, 5, Fraction(0), set(), Fraction(-111001473, 32000)),
)


def sigma0_of(p: int) -> tuple[Fraction, set[tuple[int, int]]]:
    total = Fraction(0)
    found: set[tuple[int, int]] = set()
    for (a, b), re, im in MODES:
        if a % p == 0 and b % p == 0:
            total += re * re + im * im
            found.add((a, b))
    return total, found


def fixed_quadratic_difference(N: int, m: int) -> float:
    """Central difference of the fixed-kick squared trace. This estimates Q, not D2."""
    M = cat(N)
    A = np.zeros((N, N), dtype=np.complex128)
    for (a, b), re, im in MODES:
        A += complex(float(re), float(im)) * weyl(N, a, b)

    def tr2(h: float) -> float:
        return abs(np.trace(np.linalg.matrix_power(expm(1j * h * A) @ M, m))) ** 2

    h = 1e-4
    return (tr2(h) + tr2(-h) - 2.0 * tr2(0.0)) / (2.0 * h * h)


def prime_revival() -> dict:
    sigma = sum((re * re + im * im) for _, re, im in MODES)
    assert sigma == Fraction(66033, 160000)
    identity = np.array([[1, 0], [0, 1]], dtype=object)
    out: dict[str, object] = {"sigma": str(sigma)}
    worst = 0.0
    for N, m, sigma0, modes, D2 in REVIVALS:
        assert np.array_equal(mat_pow(m) % N, identity)
        for d in range(1, m):
            assert not np.array_equal(mat_pow(d) % N, identity)
            Ad = mat_pow(d) - identity
            det = int(Ad[0, 0] * Ad[1, 1] - Ad[0, 1] * Ad[1, 0]) % N
            assert det != 0, (N, d)
        got0, found = sigma0_of(N)
        assert got0 == sigma0, (N, got0, found)
        assert found == modes
        assert D2 == -m * (sigma - sigma0) * (N * N)
        table, ker = preimage_table(N, m)
        assert ker == N * N
        M = cat(N)
        Mm = np.linalg.matrix_power(M, m)
        Z = np.trace(Mm)
        closed = order_two_coefficient(N, m, table, Z)
        err = abs(closed - float(D2))
        assert err < 1e-4, (N, err, closed, float(D2))
        assert abs(abs(Z) ** 2 - N * N) < 1e-6
        if N == 7:
            # A_7 is scalar, so the fixed-kick trace square is independent of eta.
            # The phase-averaged coefficient D2 is a different, nonzero rational.
            diff = fixed_quadratic_difference(N, m)
            assert abs(diff) < 1e-3, diff
            out["fixed_Q_difference_7"] = diff
        worst = max(worst, err)
        out[f"D2_{N}"] = str(D2)
        out[f"sigma0_{N}"] = str(sigma0)
    for p in (11, 13, 17, 19, 41):
        got0, found = sigma0_of(p)
        assert got0 == 0 and found == set(), p
    out["float_abs"] = worst
    return out


def main() -> None:
    cert = symbol_certificate()
    out = {
        "status": "all exact and floating checks passed",
        "symbol": {
            "modes": cert["modes"],
            "energy": str(cert["energy"]),
            "majorant": str(cert["majorant"]),
            "imag_energy": str(cert["imag_energy"]),
            "parity_fraction": str(cert["parity_fraction"]),
            "reversal_defect": str(cert["reversal_defect"]),
            "squares": cert["squares"],
        },
        "symmetries": check_symmetries(cert),
        "algebra": check_cocycle_egorov_gauge(),
        "trace": check_trace_closure(),
        "order_two": check_order_two(),
        "interaction": check_interaction(),
        "two_pair": two_pair_average(),
        "revival": prime_revival(),
    }
    lin = check_fixed_linear()
    out["fixed_linear"] = {
        "linear_coefficient": lin["linear_coefficient"],
        "imag_sigma": lin["imag_sigma"],
        "ker": lin["ker"],
        "nonzero": lin["nonzero"],
        "cyclotomic_re": lin["cyclotomic_re"],
        "cyclotomic_im": lin["cyclotomic_im"],
    }
    print(out["status"])
    for key, val in out.items():
        if key == "status":
            continue
        print(key, val)


if __name__ == "__main__":
    main()
