"""Self-contained exact checks for contract.json; no imported prior checker."""
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path


def canonical(parts):
    out = []
    start = 0
    for length in parts:
        out.extend(list(range(start + 1, start + length)) + [start])
        start += length
    return tuple(out)


def cycle_type(perm):
    unseen = set(range(len(perm)))
    lengths = []
    while unseen:
        current = next(iter(unseen))
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = perm[current]
            length += 1
        lengths.append(length)
    return tuple(sorted(lengths))


def class_factor(parts):
    return math.prod(m ** count * math.factorial(count)
                     for m, count in Counter(parts).items())


def skew(perm):
    n = len(perm)
    a = [[0] * n for _ in range(n)]
    for i, j in enumerate(perm):
        a[i][j] += 1
        a[j][i] -= 1
    return a


def rank(matrix, p):
    a = [[x % p for x in row] for row in matrix]
    height = len(a)
    width = len(a[0]) if height else 0
    pivots = 0
    for col in range(width):
        pivot = next((j for j in range(pivots, height) if a[j][col]), None)
        if pivot is None:
            continue
        a[pivots], a[pivot] = a[pivot], a[pivots]
        inv = pow(a[pivots][col], -1, p)
        a[pivots] = [(x * inv) % p for x in a[pivots]]
        for j in range(pivots + 1, height):
            factor = a[j][col]
            if factor:
                a[j] = [(x - factor * y) % p
                        for x, y in zip(a[j], a[pivots])]
        pivots += 1
    return pivots


def identify(matrix, left, right):
    """H^T K H with x_right=x_left; both row and column are summed."""
    n = len(matrix)
    labels = [i for i in range(n) if i != right]
    position = {i: j for j, i in enumerate(labels)}
    mapping = [position[left if i == right else i] for i in range(n)]
    out = [[0] * (n - 1) for _ in range(n - 1)]
    for i in range(n):
        for j in range(n):
            out[mapping[i]][mapping[j]] += matrix[i][j]
    return out


def evaluate(poly, n):
    return sum((F(value, n ** degree) for degree, value in poly.items()), F(0))


def serialize(poly):
    return {str(k): v for k, v in sorted(poly.items()) if v}


def all_rank_cases():
    types = [(3,), (4,), (5,), (6,), (7,), (8,), (3, 3), (3, 4), (4, 4)]
    classes = {}
    for length in sorted(set(map(sum, types))):
        wanted = {t for t in types if sum(t) == length}
        for perm in itertools.permutations(range(length)):
            kind = cycle_type(perm)
            if kind in wanted:
                classes.setdefault(kind, []).append(perm)
        for kind in wanted:
            assert len(classes[kind]) == math.factorial(length) // class_factor(kind)
    records = []
    lookup = {}
    rank_calls = 0
    pair_calls = 0
    for p in (3, 5):
        for parts in types:
            length = sum(parts)
            sigma = canonical(parts)
            a = skew(sigma)
            factor = class_factor(parts)
            g_poly = Counter()
            w_poly = Counter()
            rank_counts = Counter()
            max_support_by_rank = {}
            for tau in classes[parts]:
                b = skew(tau)
                k = [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]
                r = rank(k, p)
                rank_calls += 1
                support = {i for i, row in enumerate(k) if any(x % p for x in row)}
                assert r % 2 == 0
                assert len(support) <= 4 * r
                assert all(tau[i] == sigma[i] for i in range(length) if i not in support)
                if r == 0:
                    assert tau == sigma
                rank_counts[r] += 1
                max_support_by_rank[r] = max(max_support_by_rank.get(r, 0), len(support))
                g_poly[r // 2] += factor
                for i in range(length):
                    for j in range(i + 1, length):
                        restricted = rank(identify(k, i, j), p)
                        pair_calls += 1
                        assert restricted % 2 == 0
                        assert r - 2 <= restricted <= r
                        if i not in support or j not in support:
                            assert restricted == r
                        w_poly[1 + restricted // 2] += factor
            assert rank_counts[0] == 1
            for r, count in rank_counts.items():
                if r:
                    assert count <= sum(math.comb(length, q) * math.factorial(q)
                                        for q in range(min(4 * r, length) + 1))
                    assert count <= 2 * length ** (4 * r)
            bounded_n = []
            for d in range(1, 13):
                n = p ** (2 * d)
                x = F(length ** 8, n)
                if x >= 1:
                    continue
                a_bound = 2 * x / (1 - x)
                b_bound = F(math.comb(length, 2), n)
                w_bound = b_bound * (1 + a_bound) + 64 * x * (1 + x) / (1 - x) ** 3
                g_value = evaluate(g_poly, n) / factor
                w_value = evaluate(w_poly, n) / factor
                assert 1 <= g_value <= 1 + a_bound
                assert 0 <= w_value <= w_bound
                bounded_n.append(n)
            row = {"p": p, "parts": parts, "tau_count": len(classes[parts]),
                   "rank_counts": dict(sorted(rank_counts.items())),
                   "max_support_by_rank": dict(sorted(max_support_by_rank.items())),
                   "gaussian_polynomial": serialize(g_poly),
                   "collision_polynomial": serialize(w_poly),
                   "geometric_bound_N": bounded_n}
            records.append(row)
            lookup[p, parts] = (g_poly, w_poly)
    # Negative control: zero skew signature does NOT determine short cycles.
    short = (2, 2)
    a = skew(canonical(short))
    zeros = sum(skew(tau) == a for tau in itertools.permutations(range(4))
                if cycle_type(tau) == short)
    assert zeros == 3 and zeros != 1
    return records, lookup, rank_calls, pair_calls


def omega_table(p, d):
    vertices = list(itertools.product(range(p), repeat=2 * d))
    return [[sum(x[2 * j] * y[2 * j + 1] - x[2 * j + 1] * y[2 * j]
                 for j in range(d)) % p for y in vertices] for x in vertices]


def trace_poly(table, p, m):
    n = len(table)
    out = {}
    for word in itertools.product(range(n), repeat=m):
        occupation = [0] * n
        for v in word:
            occupation[v] += 1
        phase = sum(table[word[i]][word[(i + 1) % m]] for i in range(m)) % p
        out.setdefault(tuple(occupation), [0] * p)[phase] += 1
    return out


def multiply(a, b, p):
    out = {}
    for alpha, left in a.items():
        for beta, right in b.items():
            occupation = tuple(x + y for x, y in zip(alpha, beta))
            row = out.setdefault(occupation, [0] * p)
            for i, x in enumerate(left):
                if x:
                    for j, y in enumerate(right):
                        if y:
                            row[(i + j) % p] += x * y
    return out


def weighted_norm(poly, p, n, length, kind):
    total = [0] * p
    for alpha, row in poly.items():
        weight = 1 if kind == 'circle' else math.prod(math.factorial(x) for x in alpha)
        if kind == 'collision':
            weight *= sum(math.comb(x, 2) for x in alpha)
        for i, x in enumerate(row):
            if x:
                for j, y in enumerate(row):
                    if y:
                        total[(i - j) % p] += weight * x * y
    reduced = [x - total[-1] for x in total[:-1]]
    assert all(x == 0 for x in reduced[1:]), (p, kind, reduced)
    return F(reduced[0], n ** length)


def physical_checks(lookup):
    rows = []
    for p, maximum, types in [(3, 5, [(3,), (4,), (5,), (3, 3), (3, 4), (4, 4)]),
                              (5, 4, [(3,), (4,)])]:
        table = omega_table(p, 1)
        n = len(table)
        traces = {m: trace_poly(table, p, m) for m in range(3, maximum + 1)}
        for parts in types:
            polynomial = traces[parts[0]]
            for m in parts[1:]:
                polynomial = multiply(polynomial, traces[m], p)
            actual = {kind: weighted_norm(polynomial, p, n, sum(parts), kind)
                      for kind in ('circle', 'gaussian', 'collision')}
            g_poly, w_poly = lookup[p, parts]
            assert actual['gaussian'] == evaluate(g_poly, n)
            assert actual['collision'] == evaluate(w_poly, n)
            assert 0 <= actual['gaussian'] - actual['circle'] <= actual['collision']
            rows.append({"N": n, "parts": parts,
                         **{key: str(value) for key, value in actual.items()},
                         "occupation_count": len(polynomial)})
    control = next(row for row in rows if row['N'] == 9 and row['parts'] == (3,))
    assert control['gaussian'] != control['circle']
    return rows


def main(destination):
    rows, lookup, ranks, pairs = all_rank_cases()
    physical = physical_checks(lookup)
    result = {"status": "passed", "permutation_cases": rows,
              "rank_calls": ranks, "identified_pair_rank_calls": pairs,
              "physical_cases": physical,
              "negative_controls": ["Gaussian and physical circle t3 norms differ at N=9",
                                    "Three zero-skew-signature permutations for type (2,2), not one"],
              "scope": "Exact finite verification; analytic convergence and uniform asymptotics are established only by the accompanying proof"}
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    Path(destination).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({"status": "passed", "permutation_cases": len(rows),
                      "rank_calls": ranks, "pair_calls": pairs,
                      "physical_cases": len(physical)}))


if __name__ == '__main__':
    main(sys.argv[1])
