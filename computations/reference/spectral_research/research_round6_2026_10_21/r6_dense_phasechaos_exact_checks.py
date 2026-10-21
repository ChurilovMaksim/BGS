#!/usr/bin/env python3
"""Exact finite audit for isolated substitutions and bounded differences.

Integers and fractions only. These computations validate finite algebra
and constants, and do not prove a limiting spectral statistic.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import comb, prod
import json


def trim(poly):
    return {key: value for key, value in poly.items() if value}


def padd(out, poly, multiplier=1):
    for key, value in poly.items():
        out[key] += multiplier * value


def pmul(left, right):
    out = defaultdict(int)
    for lkey, lvalue in left.items():
        for rkey, rvalue in right.items():
            key = tuple(a + b for a, b in zip(lkey, rkey))
            out[key] += lvalue * rvalue
    return trim(out)


def poly_matmul(A, B):
    out = [[defaultdict(int) for _ in B[0]] for _ in A]
    for i, row in enumerate(A):
        for k, left in enumerate(row):
            if not left:
                continue
            for j, right in enumerate(B[k]):
                if right:
                    padd(out[i][j], pmul(left, right))
    return [[trim(entry) for entry in row] for row in out]


def poly_trace(A):
    out = defaultdict(int)
    for i in range(len(A)):
        padd(out, A[i][i])
    return trim(out)


def imatmul(A, B):
    return [[sum(a * b for a, b in zip(row, column))
             for column in zip(*B)] for row in A]


def independent_sets(n):
    result = []
    for mask in range(1 << n):
        selected = tuple(i for i in range(n) if mask & (1 << i))
        if any((i + 1) % n in selected for i in selected):
            continue
        result.append(selected)
    return result


def word_amplitude(numerator, word):
    return prod(numerator[word[i]][word[(i + 1) % len(word)]]
                for i in range(len(word)))


def direct_rooted_pair_polynomial(numerator, n):
    N = len(numerator)
    out = defaultdict(int)
    counts = defaultdict(int)
    balanced_counts = defaultdict(int)
    sets = independent_sets(n)
    for x in product(range(N), repeat=n):
        ax = word_amplitude(numerator, x)
        for selected in sets:
            choices = [tuple(v for v in range(N) if v != x[i]) for i in selected]
            for replacement in product(*choices):
                y = list(x)
                exponent = [0] * N
                for i, v in zip(selected, replacement):
                    exponent[x[i]] += 1
                    exponent[v] -= 1
                    y[i] = v
                key = tuple(exponent) + (len(selected),)
                out[key] += ax * word_amplitude(numerator, y)
                counts[len(selected)] += 1
                if all(value == 0 for value in exponent):
                    balanced_counts[len(selected)] += 1
                assert selected == tuple(i for i in range(n) if x[i] != y[i])
    return trim(out), dict(counts), dict(balanced_counts)


def scaled_companion(numerator):
    # If U=H/d, this matrix is similar to d^2 times the actual
    # companion. Thus its nth trace numerator has denominator d^(2n).
    N = len(numerator)
    zero = (0,) * (N + 1)
    T = [[{} for _ in range(2 * N)] for _ in range(2 * N)]
    for a in range(N):
        for b in range(N):
            T[a][b] = {zero: numerator[a][b] ** 2}
            dpoly = defaultdict(int)
            for u in range(N):
                for v in range(N):
                    if u == v:
                        continue
                    key = [0] * (N + 1)
                    key[u], key[v], key[-1] = 1, -1, 1
                    dpoly[tuple(key)] += (numerator[a][u] * numerator[a][v]
                                          * numerator[u][b] * numerator[v][b])
            T[a][N + b] = trim(dpoly)
        T[N + a][a] = {zero: 1}
    return T


def verify_rooted_transfer(numerator, denominator, max_n):
    N = len(numerator)
    assert imatmul(numerator, [list(column) for column in zip(*numerator)]) == [
        [denominator ** 2 * int(i == j) for j in range(N)] for i in range(N)]
    T = scaled_companion(numerator)
    power = T
    examples = []
    total_pairs = 0
    total_balanced_nondiagonal_pairs = 0
    for n in range(1, max_n + 1):
        direct, counts, balanced_counts = direct_rooted_pair_polynomial(numerator, n)
        indirect = poly_trace(power)
        assert direct == indirect
        assert balanced_counts.get(1, 0) == 0
        total_pairs += sum(counts.values())
        total_balanced_nondiagonal_pairs += sum(value for r, value in balanced_counts.items() if r)
        h_by_order = {}
        for (key, value) in sorted(direct.items()):
            if all(v == 0 for v in key[:-1]) and key[-1] > 0:
                h_by_order[key[-1]] = str(Fraction(value, denominator ** (2 * n)))
        examples.append({"n": n, "all_rooted_pairs": sum(counts.values()),
                         "balanced_pairs_by_defect_count": balanced_counts,
                         "H_iso_by_defect_count": h_by_order})
        if n != max_n:
            power = poly_matmul(power, T)
    return {"N": N, "denominator": denominator, "numerator": numerator,
            "max_n": max_n, "all_rooted_pairs": total_pairs,
            "nonempty_balanced_rooted_pairs": total_balanced_nondiagonal_pairs,
            "cases": examples}


def psd_by_exact_elimination(A):
    work = [[Fraction(value) for value in row] for row in A]
    n = len(work)
    for i in range(n):
        pivot = work[i][i]
        assert pivot >= 0
        if pivot == 0:
            assert all(work[i][j] == 0 for j in range(i + 1, n))
            continue
        for j in range(i + 1, n):
            for k in range(j, n):
                value = work[j][k] - work[j][i] * work[i][k] / pivot
                work[j][k] = value
                work[k][j] = value


def hadamard(N):
    assert N > 0 and N & (N - 1) == 0
    H = [[1 if (i & j).bit_count() % 2 == 0 else -1
          for j in range(N)] for i in range(N)]
    assert imatmul(H, H) == [[N * int(i == j) for j in range(N)] for i in range(N)]
    return H


def R_numerator(H, phases):
    # Actual U=H/sqrt(N); V=H diag(z) H/N; R denominator is N^2.
    N = len(H)
    phase_values = ((1, 0), (0, 1), (-1, 0), (0, -1))
    out = []
    for a in range(N):
        row = []
        for b in range(N):
            real = sum(H[a][v] * H[v][b] * phase_values[phases[v]][0]
                       for v in range(N))
            imag = sum(H[a][v] * H[v][b] * phase_values[phases[v]][1]
                       for v in range(N))
            row.append(real * real + imag * imag)
        out.append(row)
    assert all(sum(row) == N * N for row in out)
    assert all(sum(column) == N * N for column in zip(*out))
    return out


def verify_bounded_difference():
    cases = 0
    for N in (4, 8):
        H = hadamard(N)
        phase_vectors = {
            tuple(((seed + 3) * v * v + (seed // 3 + 1) * v + seed // 2
                   + ((v + seed) % 3)) % 4 for v in range(N))
            for seed in range(40)
        }
        phase_vectors.add((0,) * N)
        for phases in sorted(phase_vectors):
            R = R_numerator(H, phases)
            for v in range(N):
                for replacement in range(4):
                    if replacement == phases[v]:
                        continue
                    other_phases = list(phases)
                    other_phases[v] = replacement
                    other = R_numerator(H, other_phases)
                    difference = [[other[a][b] - R[a][b] for b in range(N)] for a in range(N)]
                    square = imatmul([list(column) for column in zip(*difference)], difference)
                    certificate = [[16 * N * N * int(a == b) - square[a][b]
                                    for b in range(N)] for a in range(N)]
                    # R difference has denominator N^2. This proves exactly
                    # Delta R* Delta R <= (4/N)^2 I, the C=1 bound.
                    psd_by_exact_elimination(certificate)
                    cases += 1
    return cases


def scalar_trace_polynomial(n):
    return {r: Fraction(n, n - r) * comb(n - r, r)
            for r in range(n // 2 + 1)}


def scalar_F(n, q, d):
    if n == 0:
        return Fraction(2)
    return sum(coefficient * q ** (n - 2 * r) * d ** r
               for r, coefficient in scalar_trace_polynomial(n).items())


def verify_scalar_rare_phase_example(max_n=50):
    q = Fraction(41, 841)
    d0 = 1 - q * q
    checks = 0
    for n in range(2, max_n + 1):
        assert scalar_F(n, q, d0) == q * scalar_F(n - 1, q, d0) + d0 * scalar_F(n - 2, q, d0)
        expectation = sum(coefficient * q ** (n - 2 * r) * d0 ** r
                          * Fraction(comb(r, r // 2), 2 ** r)
                          for r, coefficient in scalar_trace_polynomial(n).items()
                          if r % 2 == 0)
        lower = (scalar_F(n, q, d0) + scalar_F(n, q, -d0)) / (2 * (n + 1))
        assert expectation >= lower
        checks += 1
    return checks


def verify_hs_and_cyclic_constants():
    matrices = [([[21, 20], [20, -21]], 29),
                ([[-4, 7, -4], [1, -4, -8], [-8, -4, 1]], 9)]
    hs_results = []
    for numerator, denominator in matrices:
        N = len(numerator)
        P = [[Fraction(x * x, denominator ** 2) for x in row] for row in numerator]
        C = N * max(value for row in P for value in row)
        e_hs_squared = sum(value * value for row in P for value in row) - 1
        d_expected_hs_squared = sum(
            sum(P[a][u] * P[a][v] for a in range(N))
            * sum(P[u][b] * P[v][b] for b in range(N))
            for u in range(N) for v in range(N) if u != v)
        assert e_hs_squared <= C - 1
        assert d_expected_hs_squared <= C
        hs_results.append({"N": N, "C": str(C),
                           "E_HS_squared": str(e_hs_squared),
                           "phase_mean_D_HS_squared": str(d_expected_hs_squared)})
    quarter = Fraction(1, 4)
    for n in range(1, 15):
        direct = sum(quarter ** (n - len(selected))
                     for selected in independent_sets(n) if selected)
        assert direct == scalar_F(n, quarter, quarter) - quarter ** n
    exact_infinite_sum = ((quarter + 2 * quarter) / (1 - 2 * quarter)
                          - quarter / (1 - quarter) - 2 * quarter)
    assert exact_infinite_sum == Fraction(2, 3)
    return {"hs_cases": hs_results, "cyclic_scalar_cases": 14,
            "exact_sum_of_nonempty_cyclic_weights_n_ge_3": str(exact_infinite_sum)}


def main():
    binary = [[21, 20], [20, -21]]
    ternary = [[-4, 7, -4], [1, -4, -8], [-8, -4, 1]]
    output = {
        "status": "PASS: exact integer/Fraction arithmetic in every assertion",
        "rooted_transfer_and_all_phase_coefficients": [
            verify_rooted_transfer(binary, 29, 10),
            verify_rooted_transfer(ternary, 9, 7)],
        "operator_bounded_difference_psd_certificates": verify_bounded_difference(),
        "scalar_high_time_lower_bound_cases": verify_scalar_rare_phase_example(),
        "hs_refinement_constants": verify_hs_and_cyclic_constants(),
        "scope": "Finite verification only. No asymptotic claim follows from these computations."
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
