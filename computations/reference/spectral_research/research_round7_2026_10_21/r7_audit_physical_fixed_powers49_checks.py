#!/usr/bin/env python3
"""Independent exact checks for the fixed-power physical-kernel audit.

This file was written from the matrix definitions and the identities derived in
the audit. It does not import or execute any earlier author's/auditor's code.
The finite checks supplement, and do not replace, the analytic proof.
Only Python's standard library is used; no floating-point kick is evaluated.
"""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from math import comb, gcd
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).with_suffix(".md")
counts = Counter()


def require(condition, group):
    if not condition:
        raise AssertionError(group)
    counts[group] += 1


# A minimal exact polynomial ring. All coefficient comparisons are symbolic.
NAMES = ("a", "b", "c", "x", "Y", "N", "q", "s", "m")
ZERO_MON = (0,) * len(NAMES)


class Poly:
    def __init__(self, value=0):
        if isinstance(value, Poly):
            self.d = value.d.copy()
        elif isinstance(value, dict):
            self.d = {k: F(v) for k, v in value.items() if v}
        else:
            self.d = {ZERO_MON: F(value)} if value else {}

    def __add__(self, other):
        result = self.d.copy()
        for mon, value in Poly(other).d.items():
            result[mon] = result.get(mon, F(0)) + value
        return Poly(result)

    __radd__ = __add__

    def __neg__(self):
        return Poly({mon: -value for mon, value in self.d.items()})

    def __sub__(self, other):
        return self + (-Poly(other))

    def __rsub__(self, other):
        return Poly(other) - self

    def __mul__(self, other):
        result = Counter()
        for left, lv in self.d.items():
            for right, rv in Poly(other).d.items():
                mon = tuple(u + v for u, v in zip(left, right))
                result[mon] += lv * rv
        return Poly(result)

    __rmul__ = __mul__

    def __pow__(self, power):
        answer = Poly(1)
        for _ in range(power):
            answer *= self
        return answer

    def __truediv__(self, scalar):
        return self * (F(1) / F(scalar))

    def determinant_reduce(self):
        # Exact normal form modulo a^2 - b*c - 1, monic in a.
        result = Counter()
        for mon, value in self.d.items():
            exponent = mon[0]
            half, odd = divmod(exponent, 2)
            for j in range(half + 1):
                new = list(mon)
                new[0] = odd
                new[1] += j
                new[2] += j
                result[tuple(new)] += value * comb(half, j)
        return Poly(result)


def variable(name):
    mon = [0] * len(NAMES)
    mon[NAMES.index(name)] = 1
    return Poly({tuple(mon): F(1)})


a, b, c, x, Y, N, q, s, m = (variable(name) for name in NAMES)
quadratic = lambda xx, yy: a * xx**2 - 2 * xx * yy + a * yy**2
phase_numerator = lambda qq, ss, mm: -quadratic(qq, ss + mm)

polynomial_identities = {
    "shift covariance": quadratic(x + a, Y) - quadratic(x, Y - 1)
    - b * c * (2 * x + a),
    "multiplication covariance": quadratic(x + b, Y) - quadratic(x, Y)
    - 2 * b * (a * (x + b / 2) - Y),
    "x boundary": quadratic(x + N, Y + a * N) - quadratic(x, Y)
    - b * c * (2 * Y * N + a * N**2),
    "image-index boundary": phase_numerator(q, s, m + b)
    - phase_numerator(q, s, m) - 2 * b * (q - a * (s + m) - a * b / 2),
    "q deck": phase_numerator(q + 1, s, m)
    - phase_numerator(q, s, m - a) - 2 * b * (-c * (s + m) + a * c / 2),
    "s deck": phase_numerator(q, s + 1, m) - phase_numerator(q, s, m + 1),
}
for name, polynomial in polynomial_identities.items():
    require(not polynomial.determinant_reduce().d, "symbolic polynomial identities")


# Reconstruct the exact corrected Fourier coefficients using Gaussian rationals.
def zadd(left, right):
    return (left[0] + right[0], left[1] + right[1])


def zmul(left, right):
    return (left[0] * right[0] - left[1] * right[1],
            left[0] * right[1] + left[1] * right[0])


def fs_add(*terms):
    result = {}
    for term in terms:
        for label, value in term.items():
            result[label] = zadd(result.get(label, (F(0), F(0))), value)
    return {label: value for label, value in result.items() if value != (0, 0)}


def fs_scale(poly, scalar):
    return {label: (scalar * value[0], scalar * value[1])
            for label, value in poly.items() if scalar}


def fs_mul(left, right):
    result = {}
    for (k, l), lv in left.items():
        for (kk, ll), rv in right.items():
            label = (k + kk, l + ll)
            result[label] = zadd(result.get(label, (F(0), F(0))), zmul(lv, rv))
    return {label: value for label, value in result.items() if value != (0, 0)}


def cosine(k):
    return {(k, 0): (F(1, 2), F(0)), (-k, 0): (F(1, 2), F(0))}


one = {(0, 0): (F(1), F(0))}
sin1 = {(1, 0): (F(0), F(-1, 2)), (-1, 0): (F(0), F(1, 2))}
cos_p = {(0, 1): (F(-3, 10), F(-4, 10)),
         (0, -1): (F(-3, 10), F(4, 10))}
r = fs_mul(fs_add(one, fs_scale(cosine(7), -1)), fs_add(one, cosine(1)))
q_real = fs_add(cosine(7), fs_scale(r, F(1, 10)), fs_scale(one, F(-1, 10)))
q_sine = fs_scale(fs_mul(r, sin1), F(1, 100))
p_original = fs_scale(fs_mul(r, cos_p), F(1, 100))
original = fs_add(q_real, q_sine, p_original)
parity_sign = lambda integer: 1 if integer % 2 == 0 else -1
corrected = {label: (parity_sign(label[0] * label[1]) * v[0],
                     parity_sign(label[0] * label[1]) * v[1])
             for label, v in original.items()}
shifted_r = {label: (parity_sign(label[0]) * v[0], parity_sign(label[0]) * v[1])
             for label, v in r.items()}
explicit_corrected = fs_add(q_real, q_sine,
                           fs_scale(fs_mul(shifted_r, cos_p), F(1, 100)))
require(corrected == explicit_corrected, "modular-half symbol correction")
require(corrected[(7, 1)] == (F(-3, 2000), F(-4, 2000)), "marked coefficient")
require(all(abs(k) + abs(l) <= 9 and abs(l) <= 1 for k, l in corrected),
        "Fourier support")
coordinate_norm = lambda poly: sum(abs(v[0]) + abs(v[1]) for v in poly.values())
require(coordinate_norm(r) == 4, "Fourier majorants")
require(coordinate_norm(q_real) == F(11, 10), "Fourier majorants")
require(coordinate_norm(q_sine) == F(3, 100), "Fourier majorants")
require(coordinate_norm(p_original) == F(7, 125), "Fourier majorants")
require(coordinate_norm(corrected) == F(593, 500), "Fourier majorants")


# Exact original modular kernel checks; raw labels are not reduced for parity.
raw_labels = (-41, -8, -7, -1, 0, 1, 7, 8, 41)
for dim in range(3, 102, 2):
    inv2, inv8 = pow(2, -1, dim), pow(8, -1, dim)
    quad = lambda xx, yy: 3 * xx * xx - 2 * xx * yy + 3 * yy * yy
    for xx in range(dim):
        for yy in range(dim):
            left_l = -inv8 * quad(xx, yy - 1)
            right_l = 2 * (xx + inv2 * 3) - inv8 * quad(xx + 3, yy)
            require((left_l - right_l) % dim == 0, "modular generator covariance")
            left_d = yy - inv8 * quad(xx, yy)
            right_d = 3 * (xx + inv2 * 4) - inv8 * quad(xx + 4, yy)
            require((left_d - right_d) % dim == 0, "modular generator covariance")
    sample_coordinates = sorted({0, 1, dim // 2, dim - 1})
    for l in raw_labels:
        for k in raw_labels:
            require((2 * k * inv2 * l - k * l - dim * k * l) % (2 * dim) == 0,
                    "raw ordinary-half phase identity")
            ll, kk = 3 * l + 4 * k, 2 * l + 3 * k
            require((kk * ll - k * l) % 2 == 0, "raw covariance parity")
            for xx in sample_coordinates:
                for yy in sample_coordinates:
                    left = -inv8 * quad(xx, yy - l) + k * (yy - inv2 * l)
                    right = kk * (xx + inv2 * ll) - inv8 * quad(xx + ll, yy)
                    require((left - right) % dim == 0, "general modular covariance")


# Integer recurrence, support separation, all-odd Gauss parity, exact thresholds.
powers = [(1, 0, 0)]
for step in range(1, 51):
    aa, bb, cc = powers[-1]
    powers.append((3 * aa + 2 * bb, 4 * aa + 3 * bb, 2 * aa + 3 * cc))
sigmas, lambdas = {}, {}
for R in range(1, 51):
    aa, bb, cc = powers[R]
    require(aa * aa - bb * cc == 1 and bb == 2 * cc and 0 < aa < bb,
            "power arithmetic")
    require(aa % 2 == 1 and bb % 2 == 0 and cc % 2 == 0, "power parities")
    lengths = [9 * (aj + bj) for aj, bj, _ in powers[:R]]
    sigmas[R], lambdas[R] = sum(lengths), sum(ell * ell for ell in lengths)
    require(2 * sigmas[R] == 9 * (aa - 1), "Sigma closed formula")
    target, hits = (7 * bb - aa, 1), []
    for j, (aj, bj, cj) in enumerate(powers[:R]):
        for (k, l), value in corrected.items():
            kk, ll = aj * k + cj * l, bj * k + aj * l
            require((kk - k) % 2 == 0 and (ll - l) % 2 == 0,
                    "all-power raw label parities")
            require(abs(kk) + abs(ll) <= 9 * (aj + bj), "all-power support bound")
            if (bb * kk - aa * ll, ll) == target:
                hits.append((j, k, l, value))
        if j:
            require(aj - 7 * bj < -24, "inverse-label exclusion")
    require(hits == [(0, 7, 1, corrected[(7, 1)])], "marked frequency noncollision")
    for dim in range(3, 302, 2):
        common = gcd(dim, bb)
        require(common % 2 == 1 and (bb // common) % 2 == 0,
                "all-odd Gauss parity")
        for rr in range(common):
            require((aa * (dim // common) * (bb // common) * rr * rr) % 2 == 0,
                    "remaining Gauss quadratic phase")

t_lower, t_upper = F(1, 7 * 10**80), F(1, 6 * 10**80)
for R in range(1, 50):
    require(51200 * t_upper * sigmas[R] ** 2 < 1, "fixed-kick sufficient range")
require(51200 * t_lower * sigmas[50] ** 2 > 1, "fixed-kick failure at 50")
require(sigmas[49] == 73147532610169123199386258094868594249,
        "printed Sigma49")
require(sigmas[50] == 426335063173366200380428859644050080712,
        "printed Sigma50")
require(lambdas[3] == 140211 and sigmas[3] == 441, "printed R3 constants")
require(F(593, 500) * F(44, 7) * F(15, 14) < 8, "complex derivative majorants")
require(F(593, 500) * F(44, 7) ** 2 * F(15, 14) < 64,
        "complex derivative majorants")


# Direct root-of-unity arithmetic for |G|^2, including gcd(N,b)>1.
# Polynomials are reduced exactly modulo Phi_{2b}; no trigonometric numerics.
def trim(poly):
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def divide(poly, divisor):
    dividend = list(poly)
    quotient = [0] * max(1, len(dividend) - len(divisor) + 1)
    while len(dividend) >= len(divisor) and any(dividend):
        shift = len(dividend) - len(divisor)
        lead = dividend[-1] // divisor[-1]
        require(lead * divisor[-1] == dividend[-1], "cyclotomic exact division")
        quotient[shift] += lead
        for j, coeff in enumerate(divisor):
            dividend[j + shift] -= lead * coeff
        trim(dividend)
    return trim(quotient), trim(dividend)


@lru_cache(None)
def cyclotomic(order):
    answer = [-1] + [0] * (order - 1) + [1]
    for divisor in range(1, order):
        if order % divisor == 0:
            answer, remainder = divide(answer, cyclotomic(divisor))
            require(remainder == [0], "cyclotomic construction")
    return tuple(answer)


gauss_cases = []
for R in range(1, 4):
    aa, bb, _ = powers[R]
    modulus, phi = 2 * bb, cyclotomic(2 * bb)
    for dim in (3, 5, 7, 9, 15, 21, 25, 35):
        common = gcd(dim, bb)
        residues = range(bb) if R <= 2 else sorted(
            {value % bb for value in (0, 1, 2, common - 1, common, common + 1, bb // 2, bb - 1)})
        for linear in residues:
            raw_sum = Counter((-aa * dim * mm * mm + 2 * linear * mm) % modulus
                              for mm in range(bb))
            square = [0] * modulus
            for ee, weight in raw_sum.items():
                for ff, other_weight in raw_sum.items():
                    square[(ee - ff) % modulus] += weight * other_weight
            expected = bb * common if linear % common == 0 else 0
            square[0] -= expected
            _, remainder = divide(trim(square), phi)
            require(remainder == [0], "direct finite Gauss norm")
            gauss_cases.append((R, dim, linear, common))


sources = [
    "Spectral_research_master.md",
    "research_round6_2026_10_21/round6_main_report.md",
    "research_round6_2026_10_21/r6_original_fixed_powers_49.md",
    "research_round6_2026_10_21/r6_original_twostep_physical_mixing.md",
    "research_round5_2026_10_21/root_oscillatory_matrix_cancellation.md",
]
hashes = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in sources}
require(hashes["Spectral_research_master.md"] ==
        "3534e4d7aa97c2f8621050248652363c639aeedf723f8b7fe7a971dc01ac2302",
        "base master SHA256")

lines = [
    "# Independent exact checks: physical powers through 49",
    "",
    "**Result: all checks passed.** These finite computations check exact algebra and constants; the asymptotic conclusion is audited analytically in the companion report.",
    "",
    "The script uses only integer/rational arithmetic and cyclotomic polynomial reduction. It never represents the fixed kick by floating point, imports an earlier checker, or samples an asymptotic limit.",
    "",
    "## Check counts", "", "| Check | Assertions |", "| --- | ---: |",
]
lines += [f"| {name} | {count} |" for name, count in sorted(counts.items())]
lines += ["", "## Exact constants", "", "| R | Sigma_R | Lambda_R |", "| ---: | ---: | ---: |"]
lines += [f"| {R} | {sigmas[R]} | {lambdas[R]} |" for R in (1, 2, 3, 49, 50)]
lines += [
    "", "The range proof uses the rational enclosure `1/(7*10^80) < t < 1/(6*10^80)`.",
    "The upper enclosure certifies every R from 1 through 49. The lower enclosure excludes R = 50 from this sufficient criterion.",
    "", f"Direct finite Gauss computations: {len(gauss_cases)} cases; powers 1, 2, 3; odd dimensions 3, 5, 7, 9, 15, 21, 25, 35. This includes gcd(N,b_R) equal to 3, 5, 7, and 35.",
    "", "## Source revisions", "", "| File | SHA-256 |", "| --- | --- |",
]
lines += [f"| `{name}` | `{digest}` |" for name, digest in hashes.items()]
lines += ["", "## Reproduction", "", "```bash", "python research_round7_2026_10_21/r7_audit_physical_fixed_powers49_checks.py", "```", ""]
OUT.write_text("\n".join(lines))
print(json.dumps({"status": "passed", "assertions": sum(counts.values()),
                  "direct_gauss_cases": len(gauss_cases), "output": str(OUT),
                  "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()},
                 indent=2))
