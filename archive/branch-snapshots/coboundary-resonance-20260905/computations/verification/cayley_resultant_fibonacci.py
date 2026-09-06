#!/usr/bin/env python3
"""Exact regression for the square-resultant and Fibonacci Cayley slice.

This producer checks finite consequences of the proofs in
mathematics/cayley_resultant_structure.md.  It does NOT replace the general
proofs: bounded resultant checks and the K=131 computation are finite exact
certificates only.
"""
from __future__ import annotations

import itertools
import json
import math
from collections import Counter
from fractions import Fraction

import sympy as sp

X = sp.Symbol("X")


def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def lucas(n: int) -> int:
    if n == 0:
        return 2
    a, b = 2, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def collision_polynomial(k: int, i: int, j: int, r: int, s: int) -> sp.Poly:
    """Collision polynomial with exponents reduced mod k after collection."""
    terms = [
        (1, r + s + i),
        (-1, r + s + j),
        (-1, r + i + j),
        (2, r + j),
        (-1, r),
        (1, s + i + j),
        (-2, s + i),
        (1, s),
        (1, i),
        (-1, j),
    ]
    coeffs: Counter[int] = Counter()
    for coefficient, exponent in terms:
        coeffs[exponent % k] += coefficient
    return sp.Poly(
        sum(c * X**e for e, c in coeffs.items() if c), X, domain=sp.ZZ
    )


def forced(k: int, i: int, j: int, r: int, s: int) -> bool:
    return (r % k == i % k and s % k == j % k) or (
        r % k == (-j) % k and s % k == (-i) % k
    )


def resultant_square_audit(k: int) -> dict[str, int]:
    """Exhaust normalized quadruples and check R/K^3 is a perfect square."""
    phi = sp.Poly(sp.cyclotomic_poly(k, X), X, domain=sp.ZZ)
    checked = 0
    distinct_m: set[int] = set()
    max_m = 0
    i = 1
    for j in range(1, k):
        if j == i:
            continue
        for r in range(1, k):
            for s in range(1, k):
                if r == s or forced(k, i, j, r, s):
                    continue
                polynomial = collision_polynomial(k, i, j, r, s)
                resultant = abs(
                    int(sp.resultant(phi.as_expr(), polynomial.as_expr(), X))
                )
                if resultant == 0:
                    raise AssertionError(
                        f"unexpected zero non-forced resultant at K={k}, {(i,j,r,s)}"
                    )
                k3 = k**3
                if resultant % k3:
                    raise AssertionError("resultant is not divisible by K^3")
                square = resultant // k3
                root = math.isqrt(square)
                if root * root != square:
                    raise AssertionError(
                        f"R/K^3 is not square at K={k}, {(i,j,r,s)}: {resultant}"
                    )
                checked += 1
                distinct_m.add(root)
                max_m = max(max_m, root)
    return {
        "K": k,
        "normalized_nonforced_quadruples": checked,
        "distinct_square_factors_M": len(distinct_m),
        "max_M": max_m,
    }


def fibonacci_resultant_audit() -> list[dict[str, int]]:
    q = X**2 + 3 * X + 1
    rows: list[dict[str, int]] = []
    for k in (3, 5, 7, 11, 13, 17, 19, 23, 29):
        phi = sp.cyclotomic_poly(k, X)
        resultant = abs(int(sp.resultant(phi, q, X)))
        expected = fib(k) ** 2
        if resultant != expected:
            raise AssertionError(
                f"Fibonacci resultant mismatch K={k}: {resultant} != {expected}"
            )
        rows.append({"K": k, "F_K": fib(k), "resultant": resultant})
    return rows


def rational_ratio_energy(n: int) -> tuple[int, int, int, Counter[int]]:
    values: list[Fraction] = []
    for index in range(1, n + 1):
        x = Fraction(lucas(index), fib(index))
        values.extend((x, -x))
    counts = Counter(x - y for x in values for y in values if x != y)
    energy = sum(m * m for m in counts.values())
    return energy, max(counts.values()), len(counts), Counter(counts.values())


def rational_almost_sidon_audit() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for n in range(3, 13):
        energy, max_mult, distinct, histogram = rational_ratio_energy(n)
        baseline = 2 * n * (4 * n - 3)
        expected = baseline + 32
        if energy != expected or max_mult != 4:
            raise AssertionError(
                f"ratio energy mismatch N={n}: energy={energy}, max={max_mult}"
            )
        if histogram.get(4) != 2 or histogram.get(3) != 4:
            raise AssertionError(
                f"unexpected high-multiplicity histogram N={n}: {histogram}"
            )
        rows.append(
            {
                "N": n,
                "set_size": 2 * n,
                "energy": energy,
                "forced_baseline": baseline,
                "excess": energy - baseline,
                "max_multiplicity": max_mult,
                "distinct_nonzero_differences": distinct,
                "multiplicity_histogram": dict(sorted(histogram.items())),
            }
        )
    return rows


def trial_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def lucas_primality_certificate(n: int, factors: dict[int, int], base: int) -> dict:
    product = math.prod(q**e for q, e in factors.items())
    if product != n - 1:
        raise AssertionError("claimed p-1 factorization is incomplete")
    if not all(trial_prime(q) for q in factors):
        raise AssertionError("a claimed p-1 factor is not prime")
    if pow(base, n - 1, n) != 1:
        raise AssertionError("Lucas certificate Fermat condition failed")
    gcd_rows = []
    for q in sorted(factors):
        residue = pow(base, (n - 1) // q, n)
        g = math.gcd(residue - 1, n)
        if g != 1:
            raise AssertionError(f"Lucas certificate gcd failed for q={q}")
        gcd_rows.append({"q": q, "gcd": g})
    return {
        "criterion": "Lucas primality criterion with complete factorization of p-1",
        "base": base,
        "p_minus_1_factorization": {str(q): e for q, e in sorted(factors.items())},
        "fermat_condition": True,
        "prime_factor_gcd_conditions": gcd_rows,
    }


def giant_fibonacci_witness() -> dict[str, object]:
    k = 131
    p = fib(k)
    expected_p = 1066340417491710595814572169
    if p != expected_p:
        raise AssertionError("F_131 literal mismatch")
    factors = {
        2: 3,
        11: 1,
        89: 1,
        131: 1,
        199: 1,
        521: 1,
        2081: 1,
        9901: 1,
        19801: 1,
        24571: 1,
    }
    primality = lucas_primality_certificate(p, factors, 3)
    if (p - 1) % k:
        raise AssertionError("K does not divide p-1")

    h = 188706367382658195937453923
    if (h * h + 3 * h + 1) % p:
        raise AssertionError("quadratic Fibonacci collision root failed")
    if pow(h, k, p) != 1 or h == 1:
        raise AssertionError("h does not have exact prime order K")

    def cayley(z: int) -> int:
        return (z + 1) * pow((z - 1) % p, -1, p) % p

    subgroup = [pow(h, e, p) for e in range(k)]
    values = [cayley(z) for z in subgroup if z != 1]
    if len(values) != k - 1 or len(set(values)) != k - 1:
        raise AssertionError("Cayley set size/injectivity failure")

    counts: Counter[int] = Counter()
    for x in values:
        for y in values:
            if x != y:
                counts[(x - y) % p] += 1
    energy = sum(m * m for m in counts.values())
    baseline = (k - 1) * (2 * k - 5)
    histogram = Counter(counts.values())
    if (energy, baseline, energy - baseline, max(counts.values())) != (
        33442,
        33410,
        32,
        4,
    ):
        raise AssertionError("K=131 giant energy witness changed")

    target = (cayley(h) - cayley(pow(h, k - 1, p))) % p
    exponent_pairs = []
    cayley_by_exp = {e: cayley(pow(h, e, p)) for e in range(1, k)}
    for a, b in itertools.permutations(range(1, k), 2):
        if (cayley_by_exp[a] - cayley_by_exp[b]) % p == target:
            exponent_pairs.append([a, b])
    expected_pairs = [[1, 130], [2, 1], [130, 129]]
    if exponent_pairs != expected_pairs:
        raise AssertionError(
            f"explicit Fibonacci collision class changed: {exponent_pairs}"
        )

    return {
        "K": k,
        "p": p,
        "p_equals_F_K": True,
        "p_mod_K": p % k,
        "primality_certificate": primality,
        "h": h,
        "h_quadratic_relation": True,
        "h_exact_order_K": True,
        "explicit_difference": target,
        "explicit_collision_exponent_pairs": exponent_pairs,
        "cayley_set_size": len(values),
        "nonzero_difference_classes": len(counts),
        "energy": energy,
        "forced_baseline": baseline,
        "excess": energy - baseline,
        "max_multiplicity": max(counts.values()),
        "multiplicity_histogram": dict(sorted(histogram.items())),
    }


def main() -> None:
    square_rows = [resultant_square_audit(k) for k in (3, 5, 7, 11)]
    result = {
        "producer": "computations/verification/cayley_resultant_fibonacci.py",
        "scope": (
            "Finite exact regressions for the general K^3-square theorem, "
            "Fibonacci resultant identity, rational almost-Sidon energy, and "
            "the explicit K=131 exceptional-prime witness. General proofs live "
            "in mathematics/cayley_resultant_structure.md."
        ),
        "square_resultant_finite_audits": square_rows,
        "fibonacci_resultant_audits": fibonacci_resultant_audit(),
        "rational_almost_sidon_audits": rational_almost_sidon_audit(),
        "giant_fibonacci_witness": giant_fibonacci_witness(),
        "verdict": "PASS",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
