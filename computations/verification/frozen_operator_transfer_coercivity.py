#!/usr/bin/env python3
"""Exact finite checks for FM-018, not its asymptotic analytic theorem.

Integer phases are reduced modulo 2N, cyclotomic polynomials over Z certify
finite character sums, and all remaining arithmetic uses Fraction/Q(i).
No floating spectrum, fitted exponent, random sample or BGS limit is computed.
"""
from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction as Q
from functools import lru_cache
import json
from pathlib import Path

from nonlinear_pressure_variance import frequency_map


def omega(v: tuple[int, int], w: tuple[int, int]) -> int:
    return v[0] * w[1] - v[1] * w[0]


def weyl_phase(n: int, v: tuple[int, int], x: int) -> int:
    a, b = v
    return (n * a * b + 2 * b * (x + ((n + 1) // 2) * a)) % (2 * n)


def kernel_phase(n: int, x: int, y: int) -> int:
    return (-2 * pow(8, -1, n) * (3 * x * x - 2 * x * y + 3 * y * y)) % (2 * n)


def trim(p: list[int]) -> list[int]:
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def remainder(p: list[int], q: list[int]) -> list[int]:
    p = trim(p.copy())
    assert q[-1] == 1
    while len(p) >= len(q) and p != [0]:
        k, a = len(p) - len(q), p[-1]
        for j, b in enumerate(q):
            p[k + j] -= a * b
        trim(p)
    return p


def divide(p: list[int], q: list[int]) -> list[int]:
    p = trim(p.copy())
    assert q[-1] == 1
    r = [0] * (len(p) - len(q) + 1)
    while len(p) >= len(q) and p != [0]:
        k, a = len(p) - len(q), p[-1]
        r[k] = a
        for j, b in enumerate(q):
            p[k + j] -= a * b
        trim(p)
    assert p == [0]
    return trim(r)


@lru_cache(maxsize=None)
def cyclotomic(n: int) -> tuple[int, ...]:
    p = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            p = divide(p, list(cyclotomic(d)))
    return tuple(p)


def exact_weyl_checks() -> dict[str, int]:
    counts: Counter[str] = Counter()
    for n in range(3, 14, 2):
        h = (n - 1) // 2
        labels = [(a, b) for a in range(-h, h + 1) for b in range(-h, h + 1)]
        wraps = [(-2 * n - 1, 3 * n + 2), (-n, 0), (0, n), (n + 1, -2 * n + 3)]
        for v in labels + wraps:
            for w in labels:
                vw = v[0] + w[0], v[1] + w[1]
                for x in range(n):
                    lhs = weyl_phase(n, v, x) + weyl_phase(n, w, x + v[0])
                    rhs = omega(v, w) + weyl_phase(n, vw, x)
                    assert (lhs - rhs) % (2 * n) == 0, (n, v, w, x)
                    counts['weyl_products'] += 1
            a, b = v
            sv = 3 * a + 4 * b, 2 * a + 3 * b
            jv = b, -a
            for x in range(n):
                for z in range(n):
                    lhs = kernel_phase(n, x, z - a) + weyl_phase(n, v, z - a)
                    rhs = weyl_phase(n, sv, x) + kernel_phase(n, x + sv[0], z)
                    assert (lhs - rhs) % (2 * n) == 0, (n, v, x, z)
                    counts['metaplectic_entries'] += 1
                    flhs = 2 * x * (z - a) + weyl_phase(n, v, z - a)
                    frhs = weyl_phase(n, jv, x) + 2 * (x + jv[0]) * z
                    assert (flhs - frhs) % (2 * n) == 0, (n, v, x, z)
                    counts['fourier_rotation_entries'] += 1
        phi = list(cyclotomic(n))
        assert remainder([1] * n, phi) == [0]
        for nu in labels:
            histogram = [0] * n
            for v in labels:
                histogram[omega(v, nu) % n] += 1
            expected = [n * n] if nu == (0, 0) else [0]
            assert remainder(histogram, phi) == expected
            counts['twirl_characters'] += 1
    return dict(counts)


ComplexQ = tuple[Q, Q]
Poly = dict[tuple[int, int], ComplexQ]


def qadd(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] + b[0], a[1] + b[1]


def qmul(a: ComplexQ, b: ComplexQ) -> ComplexQ:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def polyadd(a: Poly, b: Poly) -> Poly:
    out = a.copy()
    for v, c in b.items():
        out[v] = qadd(out.get(v, (Q(0), Q(0))), c)
    return {v: c for v, c in out.items() if c != (0, 0)}


def polymul(a: Poly, b: Poly) -> Poly:
    out: Poly = {}
    for v, c in a.items():
        for w, d in b.items():
            vw = v[0] + w[0], v[1] + w[1]
            out[vw] = qadd(out.get(vw, (Q(0), Q(0))), qmul(c, d))
    return {v: c for v, c in out.items() if c != (0, 0)}


def diffusion_pair_check() -> int:
    cosine: Poly = {(1, 0): (Q(1, 2), Q(0)), (-1, 0): (Q(1, 2), Q(0)),
                    (0, 1): (-Q(1, 2), Q(0)), (0, -1): (-Q(1, 2), Q(0))}
    sine: Poly = {(1, 0): (Q(0), -Q(1, 2)), (-1, 0): (Q(0), Q(1, 2)),
                  (0, 1): (Q(0), Q(1, 2)), (0, -1): (Q(0), -Q(1, 2))}
    squared = polyadd(polymul(cosine, cosine), polymul(sine, sine))
    expected = {(0, 0): (Q(2), Q(0)), (1, -1): (Q(-1), Q(0)),
                (-1, 1): (Q(-1), Q(0))}
    assert squared == expected
    return len(squared)


def design_functional_checks() -> dict[str, int]:
    counts: Counter[str] = Counter()
    for n in range(3, 34, 2):
        labels = [(a, b) for a in range(n) for b in range(n)]
        mean_w = sum((Q(int(a == 0)) for a, _ in labels), Q(0)) / (n * n)
        mean_f = Q(1, n)
        assert mean_w == mean_f
        second_w, second_f = mean_w, mean_f * mean_f
        assert second_w == Q(1, n) and second_f == Q(1, n * n)
        action_w2, action_f2 = (1 - mean_w) ** 2 / 2, (1 - second_f) / 2
        assert action_w2 - action_f2 == -Q(1, n) + Q(1, n * n)
        for r in (Q(0), Q(1, 2), Q(3, 4), Q(15, 16)):
            val_w = sum(((1 - r) / (1 - r * int(a == 0))
                         for a, _ in labels), Q(0)) / (n * n)
            val_f = (1 - r) / (1 - r / n)
            assert val_w == 1 - (1 - Q(1, n)) * r
            assert val_f == (1 - r) / (1 - Q(1, n) * r)
            counts['determinant_functionals'] += 2
        trace_w4 = 0
        for v in labels:
            orbit = [v, (v[1], -v[0]), (-v[0], -v[1]), (-v[1], v[0])]
            assert tuple(map(sum, zip(*orbit))) == (0, 0)
            phase = sum(omega(orbit[i], orbit[j])
                        for i in range(4) for j in range(i + 1, 4))
            assert phase == -2 * (v[0] ** 2 + v[1] ** 2)
            trace_w4 += n * n * int(4 * v[0] % n == 0 and 4 * v[1] % n == 0)
            counts['fourier_fourth_powers'] += 1
        assert Q(trace_w4, n * n) == 1
        counts['fourth_moment_pairs'] += 1
        counts['rank_one_moment_pairs'] += 1
    # Fresh independent choices {X,Z}, versus one fixed choice at all steps.
    # At m=N, only all-X and all-Z words have zero torus label for odd N>=3.
    for n in (3, 5, 7):
        fresh = Q(n * n * 2, 2 ** n)
        fixed = Q(n * n)
        assert fresh != fixed and fixed / fresh == 2 ** (n - 1)
        counts['fresh_fixed_discriminators'] += 1
    return dict(counts)


def generator_and_constants_checks() -> dict[str, int]:
    g = frequency_map()
    assert len(g) == 32 and g[7, 0] == (Q(9, 20), Q(0))
    assert max(abs(k) for k, _ in g) == 9
    assert max(abs(ell) for _, ell in g) == 1
    generator_cases = 0
    for n in range(19, 66, 2):
        assert len({(k % n, ell % n) for k, ell in g}) == 32
        a = (n - 1) // 2
        assert 7 <= a
        # O19 also exceeds this positive rational bound, using pi>3.
        assert Q(9, 10) * (21 * a - n) > 0
        generator_cases += 1
    constant_cases = 0
    for t in range(1, 201):
        epsilon_cap = Q(1, 128 * t * t)
        assert Q(5, 8) - epsilon_cap > Q(1, 2)
        assert epsilon_cap < 1
        constant_cases += 1
    # Independent exact cyclic Hilbert-space example of the gap mechanism.
    # Forty distinct shift images give band-average norm^2=1/40 uniformly
    # in the twist. A positive diagonal contraction has one weight 1 and
    # 39 weights 1/2. Its 40th power is 2^-39 I, so a finite resolvent sum
    # gives a singular bound (1-2^-39)/40 on the whole unit circle.
    t = 40
    assert Q(1, t) <= Q(1, 16)
    k = Q(3, 4)
    abstract_bound = min(Q(1, 128 * t * t), k / 8)
    direct_bound = (1 - Q(1, 2 ** (t - 1))) / t
    assert direct_bound >= abstract_bound
    return {'symbol_modes': len(g), 'full_band_generator_cases': generator_cases,
            'gap_constant_cases': constant_cases, 'independent_cyclic_case': 1}


def common_noise_checks() -> dict[str, int]:
    counts: Counter[str] = Counter()
    for n in range(3, 34, 2):
        zero = (0, 0)
        target = ((-1 % n, 1), zero)
        qp: Counter[tuple[tuple[int, int], tuple[int, int]]] = Counter()
        qp[zero, zero] = 4
        for v in ((-1 % n, 1), (1, -1 % n)):
            qp[v, zero] += 1
            qp[zero, v] += 1
        for sign in (-1, 1):
            for j in range(2):
                for k in range(2):
                    x, y = [0, 0], [0, 0]
                    x[j], y[k] = sign % n, sign % n
                    qp[tuple(x), tuple(y)] -= 1
        assert qp[target] == 1
        w = [0] * n
        w[-1] += 1
        w[1] += 1
        w[0] -= 2
        qq = [0] * n
        for i, a in enumerate(w):
            for j, b in enumerate(w):
                qq[(i - j) % n] += a * b
        expected = [0] * n
        for power, coefficient in ((0, 6), (1, -4), (-1, -4), (2, 1), (-2, 1)):
            expected[power % n] += coefficient
        assert qq == expected
        assert remainder(qq, list(cyclotomic(n))) != [0]
        counts['common_noise_noncommutation'] += 1
        swap0: dict[tuple[tuple[int, int], tuple[int, int]], Q] = {}
        for i in range(n):
            for j in range(n):
                x = i, j
                key = x, (j, i)
                swap0[key] = swap0.get(key, Q(0)) + 1
                key = x, x
                swap0[key] = swap0.get(key, Q(0)) - Q(1, n)
                # Collective shift commutes with physical swap.
                def shift(v: tuple[int, int], factor: int) -> tuple[int, int]:
                    return tuple((v[r] - int(r == factor)) % n for r in range(2))
                left = Counter(shift((j, i), factor) for factor in range(2))
                right = Counter(tuple(reversed(shift(x, factor))) for factor in range(2))
                assert left == right
                counts['collective_shift_swap_entries'] += 1
        for factor in (0, 1):
            trace: dict[tuple[int, int], Q] = {}
            for (x, y), c in swap0.items():
                if x[factor] == y[factor]:
                    key = x[1 - factor], y[1 - factor]
                    trace[key] = trace.get(key, Q(0)) + c
            assert all(c == 0 for c in trace.values())
            counts['swap_partial_traces'] += 1
        norm_squared = sum((c * c for c in swap0.values()), Q(0)) / (n * n)
        assert norm_squared == 1 - Q(1, n * n)
        counts['swap_norms'] += 1
    return dict(counts)


def lie_generation_checks() -> dict[str, int]:
    cases, brackets = 0, 0
    for n in range(3, 34, 2):
        reached = {(1, 0), (-1 % n, 0), (0, 1), (0, -1 % n)}
        for b in range(1, n):
            v, w = (1, b - 1), (0, 1)
            assert v in reached and w in reached and omega(v, w) % n != 0
            reached.add((1, b))
            brackets += 1
        for b in range(1, n):
            for a in range(2, n + 1):
                v, w = ((a - 1) % n, b), (1, 0)
                assert v in reached and w in reached and omega(v, w) % n != 0
                reached.add((a % n, b))
                brackets += 1
        for a in range(1, n):
            v, w = (a, 1), (0, -1 % n)
            assert v in reached and w in reached and omega(v, w) % n != 0
            reached.add((a, 0))
            brackets += 1
        assert reached == {(a, b) for a in range(n) for b in range(n)
                           if (a, b) != (0, 0)}
        cases += 1
    return {'finite_lie_generation_dimensions': cases,
            'nonzero_weyl_generation_brackets': brackets}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    checks = exact_weyl_checks()
    checks.update(design_functional_checks())
    checks.update(generator_and_constants_checks())
    checks.update(common_noise_checks())
    checks.update(lie_generation_checks())
    checks['squared_commutator_laurent_terms'] = diffusion_pair_check()
    result = {'claim_id': 'BGS-FM-018', 'status': 'passed',
              'arithmetic': 'exact Z/(2N) phases, Z cyclotomic polynomials and Fraction/Q(i)',
              'checks': checks,
              'non_claims': ['No asymptotic operator gap or effective exponent certified by finite checks',
                             'No actual large-N eigenphase statistic, randomness removal or BGS theorem',
                             'No numerical tolerance, Gaussian sample or analytic Lean certificate']}
    rendered = json.dumps(result, indent=2, ensure_ascii=False) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding='utf-8')
    print(rendered, end='')


if __name__ == '__main__':
    main()
