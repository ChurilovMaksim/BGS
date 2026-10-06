#!/usr/bin/env python3
"""Portable exact controls for the four-block analytic proof.
This does NOT duplicate the separately owned rank-two classification kernel.
It does not certify the asymptotic theorem or its universal compression.
"""
from fractions import Fraction as F
from itertools import combinations, product
import argparse
import json


def check(condition, message):
    if not condition:
        raise RuntimeError(message)


def rotate_to(word, value):
    i = word.index(value)
    return word[i:] + word[:i]


def placement_checks():
    report = {}
    for case in ('U', 'V'):
        count = 0
        for lengths in product(range(3), repeat=6):
            pieces = [[(name, i) for i in range(n)] for name, n in
                      zip(('p1', 'p2', 'q1', 'q2', 'r1', 'r2'), lengths)]
            p1, p2, q1, q2, r1, r2 = pieces
            for e in range(1, 4):
                E = [('E', i) for i in range(e)]
                B, C, D = r2 + ['X'] + p1, p2 + ['Y'] + q1, q2 + ['Z'] + r1
                blocks = [B, E, C, D] if case == 'U' else [B, C, E, D]
                direct = rotate_to(blocks[0] + blocks[3] + blocks[2] + blocks[1], 'X')
                U = ['X'] + p1 + q2 + ['Z'] + r1 + p2 + ['Y'] + q1 + E + r2
                V = ['X'] + p1 + q2 + ['Z'] + r1 + E + p2 + ['Y'] + q1 + r2
                correct, wrong = (U, V) if case == 'U' else (V, U)
                check(direct == correct, f'correct {case} placement mismatch')
                check(direct != wrong, f'old {case} placement not detected')
                count += 1
        report[case] = {'cases': count, 'old_error_rejected': count, 'empty_pieces': True}
    return report


def matmul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def matrix_power(P, length):
    n = len(P)
    result = [[F(i == j) for j in range(n)] for i in range(n)]
    for _ in range(length):
        result = matmul(result, P)
    return result


def local_contraction_checks():
    n = 4
    v = list(range(1, n + 1))
    den = sum(t * t for t in v)
    U = [[F(i == j) - F(2 * v[i] * v[j], den) for j in range(n)] for i in range(n)]
    P = [[z * z for z in row] for row in U]
    J = [[F(1, n) for _ in range(n)] for _ in range(n)]
    check(matmul(U, U) == matrix_power(P, 0), 'Householder unitarity failed')
    count = 0
    def local(C, D):
        total = F(0)
        for a, b, c, d in product(range(n), repeat=4):
            if len({a, b, c, d}) != 4:
                continue
            fixed = P[b][a] * P[a][b] * U[a][b] * U[a][d] * U[b][c] * U[b][a]
            for u, vv in product(range(n), repeat=2):
                total += fixed * C[c][u] * D[d][vv] * U[u][d] * U[u][b] * U[vv][a] * U[vv][c]
        return total
    for length in range(5):
        M = matrix_power(P, length)
        check(local(J, M) == 0, 'uniform C local contraction failed')
        check(local(M, J) == 0, 'uniform D local contraction failed')
        count += 2
    return {'arithmetic': 'exact rational', 'N': n, 'uniform_link_checks': count, 'lengths': [0, 4]}


def local_flip(n, s):
    p = list(range(n))
    for a, b in ((s % n, (s + 2) % n), ((s + 1) % n, (s + 3) % n)):
        p[a], p[b] = p[b], p[a]
    return p


def nontrivial_cycles(p):
    seen, result = set(), []
    for i in range(len(p)):
        if i in seen:
            continue
        cycle, j = [], i
        while j not in seen:
            seen.add(j)
            cycle.append(j)
            j = p[j]
        if len(cycle) > 1:
            result.append(cycle)
    return result


def flip_graph_checks():
    count = 0
    for n in range(9, 31):
        for s, t in combinations(range(n), 2):
            a, b = local_flip(n, s), local_flip(n, t)
            cycles = nontrivial_cycles([a[b[j]] for j in range(n)])
            rank = sum(len(c) - 1 for c in cycles)
            distance = min((s - t) % n, (t - s) % n)
            if distance == 1:
                check(sorted(map(len, cycles)) == [3], 'neighboring flips not a three-cycle')
            else:
                check(rank == 4, 'nonneighboring flips not rank four')
            count += 1
    return {'m_range': [9, 30], 'flip_pairs': count}


def graph_budget_checks():
    checked = 0
    for r in range(1, 7):
        edges = list(combinations(range(r), 2))
        for mask in range(1 << len(edges)):
            adjacency = [[False] * r for _ in range(r)]
            e = 0
            for k, (a, b) in enumerate(edges):
                if (mask >> k) & 1:
                    adjacency[a][b] = adjacency[b][a] = True
                    e += 1
            if any(adjacency[a][b] and adjacency[b][c] and adjacency[a][c]
                   for a, b, c in combinations(range(r), 3)):
                continue
            bad = e != len(edges)
            if not bad:
                check(r <= 2 and r - e == 1, 'good graph correction failed')
            else:
                high_vertices = sum(any(j != i and not adjacency[i][j] for j in range(r)) for i in range(r))
                check(2 * high_vertices >= r, 'bad graph incident budget failed')
            check(abs(1 - r + e) <= 1 + r + r * (r - 1) // 2, 'coefficient budget failed')
            checked += 1
    return {'vertices_range': [1, 6], 'triangle_free_graphs': checked}


def canonical(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def concrete_overlap_check():
    x = (0, 1, 0, 1, 2, 3, 4, 5, 6, 7)
    target = canonical((0, 5, 6, 7, 2, 3, 4, 1, 0, 1))
    found = []
    for a, b, c, d in combinations(range(len(x)), 4):
        if len({x[a], x[b], x[c], x[d]}) != 4:
            continue
        y = x[a:b] + x[d:] + x[:a] + x[c:d] + x[b:c]
        if canonical(y) == target:
            found.append((a, b, c, d))
    check(found == [(0, 1, 4, 7), (0, 3, 4, 7)], 'concrete overlap cut sets differ')
    check(len({target[i:] + target[:i] for i in range(len(target))}) == len(target), 'output is not primitive')
    return {'m': len(x), 'cut_sets': found, 'unordered_local_edges': 1, 'r_minus_e': len(found) - 1}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fault-injection', action='store_true')
    args = parser.parse_args(argv)
    if args.fault_injection:
        check(False, 'INJECTED_FAILURE')
    report = {
        'corrected_placement': placement_checks(),
        'local_contraction': local_contraction_checks(),
        'flip_algebra': flip_graph_checks(),
        'graph_budget': graph_budget_checks(),
        'concrete_overlap': concrete_overlap_check(),
        'scope': 'finite exact controls only; rank-two classification kernel is separately owned',
    }
    print(json.dumps(report, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
