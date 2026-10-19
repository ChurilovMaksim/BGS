"""Independent exact finite controls; see contract.json for scope."""
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


def permutations_with_sign(k):
    for perm in itertools.permutations(range(k)):
        inversions = sum(perm[i] > perm[j] for i in range(k) for j in range(i + 1, k))
        yield perm, (-1 if inversions % 2 else 1)


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def canonical_permutation(parts):
    perm = []
    start = 0
    for length in parts:
        perm.extend(list(range(start + 1, start + length)) + [start])
        start += length
    return tuple(perm)


def skew_matrix(perm):
    k = len(perm)
    result = [[0] * k for _ in range(k)]
    for i, j in enumerate(perm):
        result[i][j] += 1
        result[j][i] -= 1
    return result


def rank_mod(matrix, p):
    rows = [[x % p for x in row] for row in matrix]
    rank = 0
    for col in range(len(rows)):
        pivot = next((r for r in range(rank, len(rows)) if rows[r][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][col], -1, p)
        rows[rank] = [(x * inverse) % p for x in rows[rank]]
        for r in range(rank + 1, len(rows)):
            factor = rows[r][col]
            if factor:
                rows[r] = [(x - factor * y) % p for x, y in zip(rows[r], rows[rank])]
        rank += 1
    return rank


def rank_polynomial(k, p):
    """Conjugacy reduction in sigma, direct sum over every tau."""
    permutations = [(perm, sign, skew_matrix(perm)) for perm, sign in permutations_with_sign(k)]
    polynomial = Counter()
    rank_calls = 0
    for parts in partitions(k):
        sigma = canonical_permutation(parts)
        a_sigma = skew_matrix(sigma)
        z_parts = math.prod(length ** count * math.factorial(count) for length, count in Counter(parts).items())
        class_size = math.factorial(k) // z_parts
        sign_sigma = -1 if (k - len(parts)) % 2 else 1
        for _, sign_tau, a_tau in permutations:
            difference = [[x - y for x, y in zip(row_s, row_t)] for row_s, row_t in zip(a_sigma, a_tau)]
            rank = rank_mod(difference, p)
            assert rank % 2 == 0
            polynomial[rank // 2] += class_size * sign_sigma * sign_tau
            rank_calls += 1
    return {degree: F(value, math.factorial(k)) for degree, value in polynomial.items() if value}, rank_calls


def signature_second_moment(k):
    """Direct L2 of a Hermitian random-phase determinant; no rank formula."""
    edges = [(i, j) for i in range(k) for j in range(i + 1, k)]
    edge_index = {edge: q for q, edge in enumerate(edges)}
    coefficients = Counter()
    count = 0
    for perm, sign in permutations_with_sign(k):
        signature = [0] * len(edges)
        for i, j in enumerate(perm):
            if i < j:
                signature[edge_index[i, j]] += 1
            elif j < i:
                signature[edge_index[j, i]] -= 1
        coefficients[tuple(signature)] += sign
        count += 1
    return F(sum(value * value for value in coefficients.values()), math.factorial(k)), count


def limiting_series(bound):
    """ODE (1+z-z^2-z^3) C'=(1+2z^2+2z^3+z^4) C."""
    den = [1, 1, -1, -1]
    num = [1, 0, 2, 2, 1]
    coefficients = [F(1)]
    for n in range(bound):
        right = sum(F(num[j]) * coefficients[n - j] for j in range(min(n, 4) + 1))
        known_left = sum(F(den[j]) * (n - j + 1) * coefficients[n - j + 1] for j in range(1, min(n, 3) + 1))
        coefficients.append((right - known_left) / (n + 1))
    return coefficients


def independent_cycle_series(bound):
    """Two involution sums times sets of common long cycles."""
    hermite = [1, 1]
    for n in range(1, bound):
        hermite.append(hermite[n] - n * hermite[n - 1])
    involutions = [F(h * h, math.factorial(n)) for n, h in enumerate(hermite)]
    long_cycles = [F(1)] + [F(0)] * bound
    for n in range(1, bound + 1):
        long_cycles[n] = sum((long_cycles[n - length] for length in range(3, n + 1)), F(0)) / n
    return [sum(involutions[j] * long_cycles[n - j] for j in range(n + 1)) for n in range(bound + 1)]


def omega_table(p, d):
    vertices = list(itertools.product(range(p), repeat=2 * d))
    return [[sum(x[2 * j] * y[2 * j + 1] - x[2 * j + 1] * y[2 * j] for j in range(d)) % p for y in vertices] for x in vertices]


def cyclotomic_norm_coefficients(coefficients, p):
    """Absolute square in Z[omega], still represented by p coefficients."""
    result = [0] * p
    for i, x in enumerate(coefficients):
        for j, y in enumerate(coefficients):
            result[(i - j) % p] += x * y
    return result


def physical_coefficient(table, p, k):
    n = len(table)
    permutations = list(permutations_with_sign(k))
    total = [0] * p
    subset_count = 0
    for subset in itertools.combinations(range(n), k):
        det = [0] * p
        for perm, sign in permutations:
            phase = sum(table[subset[i]][subset[j]] for i, j in enumerate(perm)) % p
            det[phase] += sign
        square = cyclotomic_norm_coefficients(det, p)
        total = [x + y for x, y in zip(total, square)]
        subset_count += 1
    reduced = [x - total[-1] for x in total[:-1]]
    assert all(x == 0 for x in reduced[1:]), (p, n, k, reduced)
    return F(reduced[0], n ** k), subset_count


def physical_unitarity(table, p):
    n = len(table)
    checked = 0
    for x in range(n):
        for z in range(n):
            counts = [0] * p
            counts_b = [0] * p
            for y in range(n):
                exponent = (table[x][y] + table[y][z]) % p
                counts[exponent] += 1
                counts_b[(2 * exponent) % p] += 1
            target = n if x == z else 0
            for values in (counts, counts_b):
                reduced = [value - values[-1] for value in values[:-1]]
                assert reduced[0] == target and all(value == 0 for value in reduced[1:])
            checked += 1
    return checked


def evaluate(polynomial, n):
    return sum(coefficient / n ** degree for degree, coefficient in polynomial.items())


def main(destination):
    series = limiting_series(40)
    assert series == independent_cycle_series(40)
    assert series[:7] == [F(1), F(1), F(0), F(1), F(3, 4), F(3, 4), F(1)]
    signature_checks = []
    for k in range(9):
        value, count = signature_second_moment(k)
        assert value == series[k]
        signature_checks.append({"k": k, "value": str(value), "permutations": count})
    polynomials = {}
    calls = 0
    for p in (3, 5):
        for k in range(8):
            polynomial, count = rank_polynomial(k, p)
            calls += count
            assert polynomial.get(0, F(0)) == series[k]
            polynomials[p, k] = polynomial
    physical = []
    for p, d, degrees in [(3, 1, range(6)), (5, 1, range(4)), (3, 2, [3])]:
        table = omega_table(p, d)
        n = len(table)
        unitarity_checks = physical_unitarity(table, p)
        for k in degrees:
            value, count = physical_coefficient(table, p, k)
            target = evaluate(polynomials[p, k], n)
            assert value == target, (p, d, k, value, target)
            if k == 3:
                assert value == F(n - 1, n)
            physical.append({"p": p, "d": d, "N": n, "k": k, "value": str(value), "subsets": count, "unitarity_coordinates": unitarity_checks})
    assert evaluate(polynomials[3, 3], 9) != F(0), "negative control must separate replacing every rank by zero"
    result = {
        "status": "passed",
        "scope": "Exact finite checks only; asymptotic theorem is proved separately in secular_hierarchy_ru.md",
        "rank_polynomials": [{"p": p, "k": k, "coefficients_in_N_inverse": {str(degree): str(coefficient) for degree, coefficient in sorted(poly.items())}} for (p, k), poly in polynomials.items()],
        "rank_calls": calls,
        "signature_checks": signature_checks,
        "series_through_40": [str(x) for x in series],
        "physical_checks": physical,
        "negative_control": "all-zero ranks would give c_N,3=0 and is rejected by the physical c_9,3=8/9",
        "software": {"python": sys.version.split()[0]},
    }
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    Path(destination).write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": result["status"], "rank_calls": calls, "physical_cases": len(physical), "signature_permutations": sum(x["permutations"] for x in signature_checks)}))


if __name__ == "__main__":
    main(sys.argv[1])
