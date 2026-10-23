"""Exact complex Gauss sums; imports only declared local combinatorics."""
import itertools
import json
import math
import sys
from fractions import Fraction as F
from pathlib import Path

from verify_polynomial_window import canonical, class_factor, cycle_type, multiply, rank, trace_poly


def partitions(n, minimum=1):
    if n == 0:
        yield ()
    for first in range(minimum, n + 1):
        for rest in partitions(n - first, first):
            yield (first,) + rest


def signature(sigma, tau, p):
    n = len(sigma)
    a = [[1, 1], [0, 1]]
    r = [[int(sigma[i] == j) - int(tau[i] == j) for j in range(n)] for i in range(n)]
    return [[(r[i][j] * a[u][v] + r[j][i] * a[v][u]) % p
             for j in range(n) for v in range(2)]
            for i in range(n) for u in range(2)]


def compress(q, i, j):
    n = len(q) // 2
    kept = [v for v in range(n) if v != j]
    index = {v: k for k, v in enumerate(kept)}
    mapping = [2 * index[i if v == j else v] + u for v in range(n) for u in range(2)]
    out = [[0] * (2 * n - 2) for _ in range(2 * n - 2)]
    for a in range(2 * n):
        for b in range(2 * n):
            out[mapping[a]][mapping[b]] += q[a][b]
    return out


def product_roots(a, b, p):
    return [sum(a[i] * b[(k - i) % p] for i in range(p)) for k in range(p)]


def reduced(a):
    return tuple(x - a[-1] for x in a[:-1])


def gauss(q, p):
    """Congruence elimination of a symmetric quadratic form, including 2x2 pivots."""
    a = [[x % p for x in row] for row in q]
    diagonal = []
    while a:
        n = len(a)
        pivot = next((i for i in range(n) if a[i][i]), None)
        if pivot is None:
            pair = next(((i, j) for i in range(n) for j in range(i + 1, n) if a[i][j]), None)
            if pair is None:
                break
            i, j = pair
            # New basis vector e_i+e_j creates a nonzero diagonal 2*a_ij.
            for k in range(n):
                a[i][k] = (a[i][k] + a[j][k]) % p
            for k in range(n):
                a[k][i] = (a[k][i] + a[k][j]) % p
            pivot = i
        order = [pivot] + [i for i in range(n) if i != pivot]
        a = [[a[i][j] for j in order] for i in order]
        value = a[0][0]
        diagonal.append(value)
        inv = pow(value, -1, p)
        a = [[(a[i][j] - a[i][0] * inv * a[0][j]) % p
              for j in range(1, n)] for i in range(1, n)]
    vector = [F(1)] + [F(0)] * (p - 1)
    half = pow(2, -1, p)
    for value in diagonal:
        factor = [F(0)] * p
        for x in range(p):
            factor[(half * value * x * x) % p] += F(1, p)
        vector = product_roots(vector, factor, p)
    return vector


def rank_checks():
    ranks = pairs = brute = 0
    for p in (3, 5):
        for length in range(1, 6):
            perms = list(itertools.permutations(range(length)))
            for parts in partitions(length):
                sigma = canonical(parts)
                for tau in perms:
                    q = signature(sigma, tau, p)
                    r = rank(q, p)
                    ranks += 1
                    support = {i for i in range(length)
                               if any(q[2 * i + u][j] % p
                                      for u in range(2) for j in range(2 * length))}
                    assert len(support) <= 4 * r
                    assert (r == 0) == (sigma == tau)
                    assert all(tau[i] == sigma[i] for i in range(length) if i not in support)
                    for i in range(length):
                        for j in range(i + 1, length):
                            rr = rank(compress(q, i, j), p)
                            pairs += 1
                            assert max(0, r - 4) <= rr <= r
                            if i not in support or j not in support:
                                assert rr == r
                    # Direct character enumeration independently tests all forms up to L=2.
                    if length <= 2:
                        counts = [F(0)] * p
                        dim = len(q)
                        for x in itertools.product(range(p), repeat=dim):
                            exponent = sum(x[i] * q[i][j] * x[j]
                                           for i in range(dim) for j in range(dim))
                            counts[(pow(2, -1, p) * exponent) % p] += F(1, p ** dim)
                        assert reduced(counts) == reduced(gauss(q, p))
                        brute += 1
    return ranks, pairs, brute


def bilinear_table(p):
    vertices = list(itertools.product(range(p), repeat=2))
    return [[(x[0] * y[0] + x[0] * y[1] + x[1] * y[1]) % p
             for y in vertices] for x in vertices]


def polynomial(parts, traces, n, p):
    out = {(0,) * n: [1] + [0] * (p - 1)}
    for m in parts:
        out = multiply(out, traces[m], p)
    return out


def phase_moment(left, right, p, n, length, kind):
    values = [F(0)] * p
    for alpha, a in left.items():
        if alpha not in right:
            continue
        b = right[alpha]
        weight = 1 if kind == 'circle' else math.prod(math.factorial(x) for x in alpha)
        if kind == 'collision':
            weight *= sum(math.comb(x, 2) for x in alpha)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                values[(i - j) % p] += F(weight * x * y, n ** length)
    return reduced(values)


def physical_checks():
    p = 3
    table = bilinear_table(p)
    n = len(table)
    traces = {m: trace_poly(table, p, m) for m in range(1, 5)}
    records = []
    for length in range(1, 5):
        kinds = list(partitions(length)) if length <= 3 else [(4,)]
        polys = {parts: polynomial(parts, traces, n, p) for parts in kinds}
        perms = list(itertools.permutations(range(length)))
        for a in kinds:
            sigma = canonical(a)
            for b in kinds:
                norm = [F(0)] * p
                collision = [F(0)] * p
                for tau in perms:
                    if cycle_type(tau) != b:
                        continue
                    q = signature(sigma, tau, p)
                    value = gauss(q, p)
                    for k in range(p):
                        norm[k] += class_factor(b) * value[k]
                    for i in range(length):
                        for j in range(i + 1, length):
                            value = gauss(compress(q, i, j), p)
                            for k in range(p):
                                collision[k] += F(class_factor(b), n) * value[k]
                actual_g = phase_moment(polys[a], polys[b], p, n, length, 'gaussian')
                actual_w = phase_moment(polys[a], polys[b], p, n, length, 'collision')
                actual_d = phase_moment(polys[a], polys[b], p, n, length, 'circle')
                assert actual_g == reduced(norm)
                assert actual_w == reduced(collision)
                if a == b:
                    assert actual_g[1] == actual_d[1] == actual_w[1] == 0
                    assert 0 <= actual_g[0] - actual_d[0] <= actual_w[0]
                records.append({"a": a, "b": b,
                                "circle": [str(x) for x in actual_d],
                                "gaussian": [str(x) for x in actual_g],
                                "collision": [str(x) for x in actual_w]})
    control = next(row for row in records if row['a'] == (1, 1) and row['b'] == (2,))
    assert F(control['circle'][1]) != 0
    # At p=3, a+b*omega is nonreal exactly when rational b!=0.
    assert control['circle'] == ['5/9', '4/3']
    return records


def main(destination):
    ranks, pairs, brute = rank_checks()
    physical = physical_checks()
    result = {"status": "passed", "rank_cases": ranks, "identified_pairs": pairs,
              "direct_character_checks": brute, "physical_cases": physical,
              "negative_control": "E[t1^2 conjugate(t2)]=5/9+(4/3)omega is nonreal; Gauss moduli cannot replace Gauss phases",
              "scope": "Finite exact verification of the stated generic seed; proof for all fixed b is separate"}
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    Path(destination).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({"status": "passed", "ranks": ranks, "pairs": pairs,
                      "brute_character_checks": brute, "physical_cases": len(physical)}))


if __name__ == '__main__':
    main(sys.argv[1])
