"""Exact independent finite trace controls; see trace_contract.json."""
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

from verify_secular import canonical_permutation, omega_table, partitions, permutations_with_sign, skew_matrix


def cycle_type(perm):
    unseen = set(range(len(perm)))
    lengths = []
    while unseen:
        first = next(iter(unseen))
        current = first
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = perm[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths))


def skew_signature(perm):
    return tuple(tuple(row) for row in skew_matrix(perm))


def z_type(parts):
    return math.prod(length ** count * math.factorial(count) for length, count in Counter(parts).items())


def proposed_moment(retarded, advanced):
    if sum(retarded) != sum(advanced):
        return 0
    if tuple(x for x in retarded if x >= 3) != tuple(x for x in advanced if x >= 3):
        return 0
    short_length = sum(x for x in retarded if x <= 2)
    return math.factorial(short_length) * z_type(tuple(x for x in retarded if x >= 3))


def rank_zero_checks(bound):
    records = []
    for length in range(bound + 1):
        counts = Counter()
        permutation_count = 0
        for perm in itertools.permutations(range(length)):
            counts[cycle_type(perm), skew_signature(perm)] += 1
            permutation_count += 1
        cases = 0
        for retarded in partitions(length):
            signature = skew_signature(canonical_permutation(retarded))
            for advanced in partitions(length):
                actual = z_type(advanced) * counts[advanced, signature]
                assert actual == proposed_moment(retarded, advanced), (retarded, advanced, actual)
                cases += 1
        records.append({"L": length, "partition_pairs": cases, "permutations": permutation_count})
    return records


def root_multiply(a, b, p):
    out = [0] * p
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if y:
                out[(i + j) % p] += x * y
    return out


def root_inner(a, b, p):
    out = [0] * p
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[(i - j) % p] += x * y
    return out


def trace_polynomial(table, p, power):
    n = len(table)
    result = {}
    for word in itertools.product(range(n), repeat=power):
        occupation = [0] * n
        for vertex in word:
            occupation[vertex] += 1
        phase = sum(table[word[i]][word[(i + 1) % power]] for i in range(power)) % p
        vector = result.setdefault(tuple(occupation), [0] * p)
        vector[phase] += 1
    return result


def polynomial_product(left, right, p):
    result = {}
    for alpha, a in left.items():
        for beta, b in right.items():
            occupation = tuple(x + y for x, y in zip(alpha, beta))
            target = result.setdefault(occupation, [0] * p)
            product = root_multiply(a, b, p)
            for j in range(p):
                target[j] += product[j]
    return result


def monomial(polynomials, powers, p, n):
    result = {(0,) * n: [1] + [0] * (p - 1)}
    for power in powers:
        result = polynomial_product(result, polynomials[power], p)
    return result


def physical_moment(retarded, advanced, p, d, table, polynomials):
    n = len(table)
    left = monomial(polynomials, retarded, p, n)
    right = monomial(polynomials, advanced, p, n)
    coefficients = [0] * p
    for alpha, a in left.items():
        if alpha in right:
            vector = root_inner(a, right[alpha], p)
            for j in range(p):
                coefficients[j] += vector[j]
    reduced = [x - coefficients[-1] for x in coefficients[:-1]]
    assert all(x == 0 for x in reduced[1:])
    total_length = sum(retarded) + sum(advanced)
    assert total_length % 2 == 0
    return F(reduced[0], (p ** d) ** total_length)


def run_physical():
    records = []
    controls = [((1,), (1,)), ((2,), (2,)), ((1, 1), (2,)), ((3,), (3,)), ((1, 1, 1), (3,)), ((4,), (4,)), ((1, 3), (4,)), ((2, 2), (4,)), ((2, 2), (2, 2)), ((1, 3), (1, 3))]
    for p, d, maximum in ((3, 1, 4), (5, 1, 3)):
        table = omega_table(p, d)
        n = len(table)
        polynomials = {power: trace_polynomial(table, p, power) for power in range(1, maximum + 1)}
        square = polynomial_product(polynomials[1], polynomials[1], p)
        assert square == polynomials[2], "exact trace-two identity failed"
        for retarded, advanced in controls:
            if max(retarded + advanced) > maximum:
                continue
            actual = physical_moment(retarded, advanced, p, d, table, polynomials)
            limit = proposed_moment(retarded, advanced)
            length = sum(retarded)
            error_bound = F(math.factorial(length) * (1 + math.comb(length, 2)), n)
            assert abs(actual - limit) <= error_bound
            if retarded == (1,) and advanced == (1,):
                assert actual == 1
            if retarded in ((2,), (1, 1)) and advanced == (2,):
                assert actual == 2 - F(1, n)
            records.append({"N": n, "retarded": retarded, "advanced": advanced, "exact_moment": str(actual), "limit": limit, "proven_error_bound": str(error_bound)})
    return records


def main(destination):
    counts = rank_zero_checks(8)
    physical = run_physical()
    negative = next(row for row in physical if row['N'] == 9 and row['retarded'] == (1, 1) and row['advanced'] == (2,))
    assert F(negative['exact_moment']) != 0
    result = {"status": "passed", "rank_zero_counts": counts, "physical_controls": physical, "negative_control": "Independent centered Gaussian trace two would predict zero, but exact E[t1^2 conjugate(t2)]=17/9 at N=9", "scope": "Finite verification only; universal proof is separate"}
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    Path(destination).write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "passed", "rank_zero_partition_pairs": sum(x['partition_pairs'] for x in counts), "physical_moment_cases": len(physical)}))


if __name__ == '__main__':
    main(sys.argv[1])
