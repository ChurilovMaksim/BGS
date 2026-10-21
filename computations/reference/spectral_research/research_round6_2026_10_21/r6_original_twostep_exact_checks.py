#!/usr/bin/env python3
"""Exact algebra checks for r6_original_twostep_physical_mixing.md.

Small explicit rational polynomial and Gaussian-rational classes are used.
The 24-sheet Gauss-square check is integer arithmetic
in Z[x]/(x^16-x^8+1); there are no floating-point spectral experiments.
"""

from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from math import factorial, gcd
import json


@dataclass(frozen=True)
class G:
    """A Gaussian rational, with no floating-point coercion."""
    re: F = F(0)
    im: F = F(0)

    def __post_init__(self):
        object.__setattr__(self, "re", F(self.re))
        object.__setattr__(self, "im", F(self.im))

    @staticmethod
    def coerce(value):
        return value if isinstance(value, G) else G(value)

    def __add__(self, other):
        other = G.coerce(other)
        return G(self.re + other.re, self.im + other.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, other):
        return self + -G.coerce(other)

    def __mul__(self, other):
        other = G.coerce(other)
        return G(self.re * other.re - self.im * other.im,
                 self.re * other.im + self.im * other.re)

    __rmul__ = __mul__

    def __truediv__(self, other):
        other = G.coerce(other)
        denominator = other.re ** 2 + other.im ** 2
        numerator = self * other.conjugate()
        return G(numerator.re / denominator, numerator.im / denominator)

    def conjugate(self):
        return G(self.re, -self.im)

    def __bool__(self):
        return bool(self.re or self.im)

    def __str__(self):
        return f"{self.re}+({self.im})i"


class Poly:
    """A sparse polynomial in exactly three variables over Q."""

    def __init__(self, terms=None):
        self.terms = {key: F(value) for key, value in (terms or {}).items()
                      if value}

    @staticmethod
    def coerce(value):
        return value if isinstance(value, Poly) else Poly({(0, 0, 0): F(value)})

    @staticmethod
    def variable(i):
        key = [0, 0, 0]
        key[i] = 1
        return Poly({tuple(key): F(1)})

    def __add__(self, other):
        other = Poly.coerce(other)
        out = defaultdict(F, self.terms)
        for key, value in other.terms.items():
            out[key] += value
        return Poly(out)

    __radd__ = __add__

    def __neg__(self):
        return Poly({key: -value for key, value in self.terms.items()})

    def __sub__(self, other):
        return self + -Poly.coerce(other)

    def __rsub__(self, other):
        return Poly.coerce(other) + -self

    def __mul__(self, other):
        other = Poly.coerce(other)
        out = defaultdict(F)
        for ka, va in self.terms.items():
            for kb, vb in other.terms.items():
                out[tuple(x + y for x, y in zip(ka, kb))] += va * vb
        return Poly(out)

    __rmul__ = __mul__

    def __truediv__(self, denominator):
        return Poly({key: value / F(denominator)
                     for key, value in self.terms.items()})

    def __pow__(self, power):
        assert power >= 0
        out = Poly.coerce(1)
        for _ in range(power):
            out = out * self
        return out


def add(*terms):
    out = defaultdict(G)
    for term in terms:
        for key, value in term.items():
            out[key] += value
    return {key: value for key, value in out.items() if value}


def scale(a, c):
    return {key: c * value for key, value in a.items() if c * value}


def mul(a, b):
    out = defaultdict(G)
    for (ka, la), va in a.items():
        for (kb, lb), vb in b.items():
            out[(ka + kb, la + lb)] += va * vb
    return {key: value for key, value in out.items() if value}


def symbol_checks():
    one = {(0, 0): G(1)}
    cos1 = {(1, 0): G(F(1, 2)), (-1, 0): G(F(1, 2))}
    sin1 = {(1, 0): G(0, -F(1, 2)), (-1, 0): G(0, F(1, 2))}
    cos7 = {(7, 0): G(F(1, 2)), (-7, 0): G(F(1, 2))}
    r = mul(add(one, scale(cos7, -1)), add(one, cos1))
    shifted_r = {key: (-1 if key[0] % 2 else 1) * value
                 for key, value in r.items()}
    e_alpha = G(-3, 4) / 5
    cos_p_alpha = {(0, 1): e_alpha.conjugate() / 2, (0, -1): e_alpha / 2}
    a = add(cos7, scale(r, F(1, 10)),
            scale(mul(r, sin1), F(1, 100)),
            scale(one, -F(1, 10)),
            scale(mul(shifted_r, cos_p_alpha), F(1, 100)))
    assert max(abs(k) + abs(l) for k, l in a) <= 9
    assert max(abs(l) for k, l in a) <= 1
    coefficient_bound = sum(
        abs(value.re) + abs(value.im) for value in a.values()
    )
    assert coefficient_bound < 2
    am = {(3 * k + 2 * l, 4 * k + 3 * l): value
          for (k, l), value in a.items()}
    assert len(am) == len(a)
    assert max(abs(k) + abs(l) for k, l in am) <= 63
    assert all((3 * k + 2 * l) % 2 == k % 2
               and (4 * k + 3 * l) % 2 == l % 2 for k, l in a)
    marked = (F(151, 24), F(1, 24))
    first_sources = [
        (k, l) for k, l in a
        if (k - F(17 * l, 24), F(l, 24)) == marked
    ]
    second_sources = [
        (k, l) for k, l in a
        if (F(4 * k - 3 * l, 24), F(4 * k + 3 * l, 24)) == marked
    ]
    assert first_sources == [(7, 1)]
    assert second_sources == []
    assert a[(7, 1)] == e_alpha.conjugate() / 400
    assert a[(7, 1)] * a[(7, 1)].conjugate() == G(F(1, 160000))
    return {
        "original_fourier_modes": len(a),
        "transformed_fourier_modes": len(am),
        "rational_coefficient_l1_upper_bound": str(coefficient_bound),
        "transformed_max_l1_frequency": max(abs(k) + abs(l) for k, l in am),
        "marked_first_sources": first_sources,
        "marked_second_sources": second_sources,
        "marked_coefficient": str(a[(7, 1)]),
    }


def polynomial_checks():
    q, r, m = [Poly.variable(i) for i in range(3)]
    theta = lambda mm, qq=q, rr=r: -(
        17 * qq ** 2 - 2 * qq * (rr + mm) + 17 * (rr + mm) ** 2
    ) / 48
    identities = [
        theta(m + 24) - theta(m) - q + 17 * (r + m) + 204,
        theta(m, q + 1, r) - theta(m - 17) + 12 * (r + m) - 102,
        theta(m, q, r + 1) - theta(m + 1),
    ]
    p = (-17 * q + r + m) / 24
    identities += [
        3 * q + 4 * p - (q + r + m) / 6,
        2 * q + 3 * p - (-q + r + m) / 8,
    ]
    a, b, c = 17, 24, 12
    x, big_y, n = [Poly.variable(i) for i in range(3)]
    Q = lambda xx, yy: a * xx ** 2 - 2 * xx * yy + a * yy ** 2
    identities += [
        Q(x + a, big_y) - Q(x, big_y - 1) - b * c * (2 * x + a),
        Q(x + b, big_y) - Q(x, big_y) - 2 * b * (a * (x + F(b, 2)) - big_y),
        Q(x + n, big_y + a * n) - Q(x, big_y)
        - b * c * (2 * big_y * n + a * n ** 2),
        Q(x, big_y + b * n) - Q(x, big_y)
        - 2 * b * n * (-x + a * big_y + a * b * n / 2),
    ]
    for expr in identities:
        assert expr.terms == {}
    return len(identities)


def reduce_cyclotomic_48(coefficients):
    """Reduce using z^16-z^8+1=0, satisfied by every primitive 48th root."""
    c = list(coefficients)
    c += [0] * max(0, 16 - len(c))
    for k in range(len(c) - 1, 15, -1):
        value = c[k]
        c[k] = 0
        c[k - 8] += value
        c[k - 16] -= value
    return tuple(c[:16])


def gauss_square_checks():
    # G = sum_m zeta_48^(-17*N*m^2 + 2*L*m).
    # N mod48 and L mod24 exhaust all possible original integer parameters.
    checks = 0
    for n in range(1, 48, 2):
        g = gcd(n, 24)
        assert g in (1, 3)
        for ell in range(24):
            coefficients = [0] * 48
            for m in range(24):
                coefficients[(-17 * n * m * m + 2 * ell * m) % 48] += 1
            squared = [0] * 48
            for i, ci in enumerate(coefficients):
                for j, cj in enumerate(coefficients):
                    squared[(i - j) % 48] += ci * cj
            reduced = reduce_cyclotomic_48(squared)
            expected = 24 * g if ell % g == 0 else 0
            assert reduced == (expected,) + (0,) * 15
            checks += 1
    return checks


def margin_checks():
    # Exact positive Taylor tail bound for exp(4/5).
    u = F(4, 5)
    exp_upper = sum((u ** k / factorial(k) for k in range(7)), F(0))
    exp_upper += (u ** 7 / factorial(7)) / (1 - u / 8)
    assert exp_upper < F(9, 4)
    exponent_upper = F(44, 7) * F(2, 1000) * 63
    assert exponent_upper < F(4, 5)
    gradient = 2 * F(44, 7) * 63 * F(9, 4)
    hessian = 2 * F(44, 7) ** 2 * 63 ** 2 * F(9, 4)
    assert gradient == 1782 < 2000
    assert hessian == 705672 < 10 ** 6
    tstar = F(1, 10 ** 12)
    assert 4 * 10 ** 6 * tstar < F(1, 2)
    assert 32 * 10 ** 6 * tstar <= F(1, 4800)
    assert 32000 * tstar < F(1, 48)
    assert 24 * (1 + 8 * 10 ** 6 * tstar) < 25
    q = d = F(1, 4)
    z_sum = d * (2 - q) / ((1 - q - d) * (1 - q))
    assert z_sum == F(7, 6)
    assert z_sum - 2 * d == F(2, 3)
    total = 72 + 784 * (z_sum - 2 * d)
    assert total == F(1784, 3) < 600
    assert 17 < F(13, 3) ** 2  # (1+sqrt17)/8 < 2/3
    assert 8 * 10 ** 6 * F(1, 10 ** 80) + (
        40000 * F(1, 10 ** 80)
    ) ** 2 < F(1, 4)
    return {
        "gradient_upper_bound": str(gradient),
        "hessian_upper_bound": str(hessian),
        "construction_tstar": str(tstar),
        "all_time_signed_class_bound": str(total),
    }


def main():
    print(json.dumps({
        "fourier_symbols": symbol_checks(),
        "exact_deck_covariance_polynomials": polynomial_checks(),
        "all_residue_gauss_square_checks": gauss_square_checks(),
        "rational_margins": margin_checks(),
        "status": "all exact checks passed",
    }, indent=2))


if __name__ == "__main__":
    main()
