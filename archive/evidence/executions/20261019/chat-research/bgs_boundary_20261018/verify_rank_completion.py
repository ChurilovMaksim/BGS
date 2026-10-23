"""New strengthened-count checks; previous executed checkers stay unchanged."""
import itertools
import json
import math
import sys
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

from verify_generic_window import partitions, signature
from verify_polynomial_window import canonical, cycle_type, evaluate, rank, skew


def inverse(a, p):
    n = len(a)
    rows = [[x % p for x in row] + [int(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for i in range(n):
        pivot = next((j for j in range(i, n) if rows[j][i]), None)
        if pivot is None:
            return None
        rows[i], rows[pivot] = rows[pivot], rows[i]
        inv = pow(rows[i][i], -1, p)
        rows[i] = [(x * inv) % p for x in rows[i]]
        for j in range(n):
            if i != j:
                factor = rows[j][i]
                rows[j] = [(x - factor * y) % p for x, y in zip(rows[j], rows[i])]
    return [row[n:] for row in rows]


def certificate(a, p):
    n = len(a)
    r = rank(a, p)
    for index in itertools.combinations(range(n), r):
        minor = [[a[i][j] for j in index] for i in index]
        inv = inverse(minor, p)
        if inv is not None:
            for i in range(n):
                for j in range(n):
                    value = sum(a[i][v] * inv[k][h] * a[w][j]
                                for k, v in enumerate(index) for h, w in enumerate(index))
                    assert (value - a[i][j]) % p == 0
            return index
    raise AssertionError("no full-rank principal minor")


def matching(vertices, a, p):
    if not vertices:
        return ()
    i = vertices[0]
    for j in vertices[1:]:
        if a[i][j] % p:
            rest = tuple(v for v in vertices if v not in (i, j))
            tail = matching(rest, a, p)
            if tail is not None:
                return ((i, j),) + tail
    return None


def inverse_perm(tau):
    out = [0] * len(tau)
    for i, j in enumerate(tau):
        out[j] = i
    return out


def skew_checks():
    earlier = json.loads(Path('run/result.json').read_text())
    cache = {}
    checked = 0
    bounds = 0
    for row in earlier['permutation_cases']:
        p = row['p']
        parts = tuple(row['parts'])
        length = sum(parts)
        if parts not in cache:
            cache[parts] = [tau for tau in itertools.permutations(range(length)) if cycle_type(tau) == parts]
        sigma = canonical(parts)
        a = skew(sigma)
        encodings = set()
        counts = Counter()
        for tau in cache[parts]:
            b = skew(tau)
            k = [[x - y for x, y in zip(ar, br)] for ar, br in zip(a, b)]
            index = certificate(k, p)
            r = len(index)
            pairs = matching(index, k, p)
            assert pairs is not None
            inv_tau = inverse_perm(tau)
            encoding = []
            for i, j in pairs:
                if sigma[i] == j:
                    kind, u, v = 'sigma', i, j
                elif sigma[j] == i:
                    kind, u, v = 'sigma', j, i
                elif tau[i] == j:
                    kind, u, v = 'tau', i, j
                else:
                    assert tau[j] == i
                    kind, u, v = 'tau', j, i
                encoding.append((kind, u, v, tau[u], inv_tau[u], tau[v], inv_tau[v]))
            key = tuple(encoding)
            assert key not in encodings
            encodings.add(key)
            counts[r] += 1
            checked += 1
        for r, count in counts.items():
            assert count <= (length ** 5 + length ** 4) ** (r // 2)
        for d in range(1, 13):
            n = p ** (2 * d)
            x = F(length ** 5 + length ** 4, n)
            if x >= 1:
                continue
            aa = x / (1 - x)
            bb = F(math.comb(length, 2), n)
            ww = bb * (1 + aa) + 32 * x * (1 + x) / (1 - x) ** 3
            factor = math.prod(m ** c * math.factorial(c) for m, c in Counter(parts).items())
            gp = {int(k): v for k, v in row['gaussian_polynomial'].items()}
            wp = {int(k): v for k, v in row['collision_polynomial'].items()}
            assert abs(evaluate(gp, n) / factor - 1) <= aa
            assert evaluate(wp, n) / factor <= ww
            bounds += 1
    return checked, bounds


def generic_checks():
    count = 0
    for p in (3, 5):
        for length in range(1, 5):
            perms = list(itertools.permutations(range(length)))
            for parts in partitions(length):
                sigma = canonical(parts)
                encodings = set()
                rank_counts = Counter()
                for tau in perms:
                    q = signature(sigma, tau, p)
                    index = certificate(q, p)
                    inv_tau = inverse_perm(tau)
                    key = (index, tuple((tau[i // 2], inv_tau[i // 2]) for i in index))
                    assert key not in encodings
                    encodings.add(key)
                    rank_counts[len(index)] += 1
                    count += 1
                for r, number in rank_counts.items():
                    assert number <= math.comb(2 * length, r) * length ** (2 * r)
    return count


def main(destination):
    skew_count, bound_count = skew_checks()
    generic_count = generic_checks()
    result = {"status":"passed", "skew_reconstruction_and_matching_encodings":skew_count,
              "generic_reconstruction_and_row_encodings":generic_count,
              "stronger_geometric_bound_checks":bound_count,
              "scope":"Exact finite witnesses; the universal counting argument is a separate proof"}
    Path(destination).parent.mkdir(parents=True, exist_ok=True)
    Path(destination).write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main(sys.argv[1])
