"""New seed-classification controls; see seed_contract_v2.json."""
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

from verify_secular import canonical_permutation, partitions, rank_mod
from verify_trace_hierarchy import cycle_type, monomial, root_inner, trace_polynomial, z_type


SEEDS = [
    ('symmetric', [[1, 0], [0, 1]]),
    ('antisymmetric', [[0, 1], [-1, 0]]),
    ('generic', [[1, 1], [0, 1]]),
]


def quadratic_signature(perm, seed, p):
    length = len(perm)
    b = len(seed)
    q = [[0] * (b * length) for _ in range(b * length)]
    for i, j in enumerate(perm):
        for a in range(b):
            for c in range(b):
                q[b * i + a][b * j + c] += seed[a][c]
                q[b * j + c][b * i + a] += seed[a][c]
    return tuple(tuple(x % p for x in row) for row in q)


def expected(kind, retarded, advanced):
    if sum(retarded) != sum(advanced):
        return 0
    if kind == 'antisymmetric':
        if tuple(x for x in retarded if x >= 3) != tuple(x for x in advanced if x >= 3):
            return 0
        return math.factorial(sum(x for x in retarded if x <= 2)) * z_type(tuple(x for x in retarded if x >= 3))
    if retarded != advanced:
        return 0
    if kind == 'symmetric':
        return z_type(retarded) * 2 ** sum(x >= 3 for x in retarded)
    return z_type(retarded)


def count_checks():
    rows = []
    for kind, seed in SEEDS:
        for length in range(7):
            signatures = Counter((cycle_type(perm), quadratic_signature(perm, seed, 3)) for perm in itertools.permutations(range(length)))
            cases = 0
            for retarded in partitions(length):
                signature = quadratic_signature(canonical_permutation(retarded), seed, 3)
                for advanced in partitions(length):
                    actual = signatures[advanced, signature] * z_type(advanced)
                    assert actual == expected(kind, retarded, advanced)
                    cases += 1
            rows.append({'kind': kind, 'L': length, 'partition_pairs': cases})
    return rows


def seed_table(seed, p):
    b = len(seed)
    points = list(itertools.product(range(p), repeat=b))
    return [[sum(x[a] * seed[a][c] * y[c] for a in range(b) for c in range(b)) % p for y in points] for x in points]


def finite_moment(kind, seed, retarded, advanced, p, table, traces):
    n = len(table)
    left = monomial(traces, retarded, p, n)
    right = monomial(traces, advanced, p, n)
    coefficients = [0] * p
    for occupation, a in left.items():
        if occupation in right:
            vector = root_inner(a, right[occupation], p)
            coefficients = [x + y for x, y in zip(coefficients, vector)]
    reduced = [x - coefficients[-1] for x in coefficients[:-1]]
    value = [F(x, n ** sum(retarded)) for x in reduced]
    if retarded == advanced:
        assert all(x == 0 for x in value[1:])
        assert value[0] >= 0
    limit = expected(kind, retarded, advanced)
    return {'retarded': retarded, 'advanced': advanced, 'exact_coefficients_in_omega_basis': [str(x) for x in value], 'limit': limit}


def main(destination):
    counts = count_checks()
    physical = []
    controls = [((1,), (1,)), ((2,), (2,)), ((1, 1), (2,)), ((3,), (3,)), ((1, 1, 1), (3,))]
    seeds = SEEDS + [('generic', [[1, 1, 0], [0, 1, 1], [0, 0, 1]])]
    for kind, seed in seeds:
        p = 3
        b = len(seed)
        assert rank_mod(seed, p) == b
        reversal_rank = rank_mod([[seed[i][j] - seed[j][i] for j in range(b)] for i in range(b)], p)
        assert (reversal_rank == 0) == (kind == 'symmetric')
        table = seed_table(seed, p)
        traces = {power: trace_polynomial(table, p, power) for power in (1, 2, 3)}
        checks = [finite_moment(kind, seed, a, c, p, table, traces) for a, c in controls]
        physical.append({'kind': kind, 'seed': seed, 'N': len(table), 'rank_A_minus_AT': reversal_rank, 'admissible_B_gap': reversal_rank > 0, 'checks': checks})
    assert physical[0]['admissible_B_gap'] is False
    assert physical[2]['checks'][2]['exact_coefficients_in_omega_basis'] != physical[1]['checks'][2]['exact_coefficients_in_omega_basis']
    result = {'status': 'passed', 'zero_signature_counts': counts, 'physical': physical, 'negative_control': 'symmetric seed excluded because B norm is exactly one', 'scope': 'Finite checks; general classification proved in bilinear_seed_classification_ru.md'}
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    Path(destination).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'status': 'passed', 'partition_pairs': sum(x['partition_pairs'] for x in counts), 'physical_seeds': len(physical)}))


if __name__ == '__main__':
    main(sys.argv[1])
