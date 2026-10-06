#!/usr/bin/env python3
"""Finite exact controls for TRACE-015; no asymptotic numerical claim.
Run with Python 3 standard library only. Prints a deterministic JSON report.
Checks are explicit exceptions, so python -O cannot silently disable them.
"""
from fractions import Fraction as F
from itertools import product, combinations
from collections import Counter, defaultdict
import random, json

def check(condition, message="finite check failed"):
    if not condition:
        raise RuntimeError(message)

def mm(A, B):
    return [[sum((a * b for a, b in zip(row, col))) for col in zip(*B)] for row in A]

def power(A, k):
    R = [[F(i == j) for j in range(len(A))] for i in range(len(A))]
    for _ in range(k):
        R = mm(R, A)
    return R
out = {}
for n in (3, 4):
    v = list(range(1, n + 1))
    d = sum((t * t for t in v))
    U = [[F(i == j) - F(2 * v[i] * v[j], d) for j in range(n)] for i in range(n)]
    P = [[t * t for t in row] for row in U]
    J = [[F(1, n)] * n for _ in range(n)]
    L = (1, 2, 3)
    Ps = [power(P, l) for l in L]
    Ds = [[[Ps[k][i][j] - J[i][j] for j in range(n)] for i in range(n)] for k in range(3)]

    def contraction(M, restrict=lambda a: True):
        s = F(0)
        for a in product(range(n), repeat=3):
            if not restrict(a):
                continue
            for b in product(range(n), repeat=3):
                z = F(1)
                for i in range(3):
                    z *= M[i][a[i]][b[i]] * U[b[i]][a[(i + 1) % 3]] * U[b[i]][a[(i - 1) % 3]]
                s += z
        return s
    check(contraction([J] * 3) == F(1, n * n), 'finite check failed')
    for k in range(3):
        M = [J] * 3
        M[k] = Ds[k]
        check(contraction(M) == sum((Ds[k][a][b] * P[b][a] for a in range(n) for b in range(n))) / n ** 2, 'finite check failed')
    for i, j in ((0, 1), (0, 2), (1, 2)):
        M = [J] * 3
        M[i] = Ds[i]
        M[j] = Ds[j]
        check(contraction(M) == sum((Ds[i][a][b] * Ds[j][a][b] * P[b][a] for a in range(n) for b in range(n))) / n, 'finite check failed')
    E = contraction(Ps)
    eq = [contraction(Ps, lambda a, i=i, j=j: a[i] == a[j]) for i, j in ((0, 1), (0, 2), (1, 2))]
    tri = contraction(Ps, lambda a: a[0] == a[1] == a[2])
    dis = contraction(Ps, lambda a: len(set(a)) == 3)
    check(dis == E - sum(eq) + 2 * tri, 'finite check failed')
    Fm = [[[sum((Ps[i][a][b] * U[b][a] * U[b][c] for b in range(n))) for c in range(n)] for a in range(n)] for i in range(3)]
    check(eq[0] == sum((power(P, 4)[c][a] * Fm[0][a][c] * Fm[1][a][c] for a in range(n) for c in range(n))), 'finite check failed')
    target = sum((power(P, 2)[a][a] * power(P, 3)[a][a] * power(P, 4)[a][a] for a in range(n)))
    check(tri == target, 'finite check failed')
    out[str(n)] = {'unitary': 'rational Householder v=(1,...,N)', 'lengths': L, 'all_checks': True, 'distinct': str(dis)}
n = 3
m = 6
counts = Counter()
rot = lambda x, k: x[k:] + x[:k]
for x in product(range(n), repeat=m):
    for s in range(1, m - 1):
        for t in range(s + 1, m):
            if len({x[0], x[s], x[t]}) < 3:
                continue
            y = x[:s] + x[t:] + x[s:t]
            if any((y == rot(x, k) for k in range(m))):
                continue
            for i in range(m):
                for j in range(m):
                    counts[rot(x, i), rot(y, j)] += 1
hist = Counter(counts.values())
out['multiplicity'] = {'N': n, 'm': m, 'exclude_cyclic_pairs': True, 'histogram': dict(sorted(hist.items())), 'examples': {str(k): [list(a), list(b)] for k in (min(hist), max(hist)) for (a, b), c in counts.items() if c == k and (a, b) == next((p for p, v in counts.items() if v == k))}}
report = {'rational_and_multiplicity': out}
cycmin = lambda x: min((x[i:] + x[:i] for i in range(len(x))))
checked = 0
for m in range(4, 15):
    for p, q in combinations(range(m), 2):
        x = tuple((p if i == q else i for i in range(m)))
        groups = defaultdict(list)
        for a, b, c in combinations(range(m), 3):
            if len({x[a], x[b], x[c]}) < 3:
                continue
            y = cycmin(x[a:b] + x[c:] + x[:a] + x[b:c])
            if y != cycmin(x):
                groups[y].append((a, b, c))
        bad = next(((y, v) for y, v in groups.items() if len(v) > 1), None)
        if bad:
            raise RuntimeError(str({'counterexample': True, 'x': x, 'y': bad[0], 'cuts': bad[1]}))
        checked += 1
report['single_repeat'] = {'m_range': [4, 14], 'checked': checked}
rng = random.Random(20261006)

def cycmin(x):
    return min((x[i:] + x[:i] for i in range(len(x))))

def unique_k(x, k):
    return len({tuple((x[(i + j) % len(x)] for j in range(k))) for i in range(len(x))}) == len(x)

def cuts(x, y):
    target = cycmin(y)
    r = []
    for a, b, c in combinations(range(len(x)), 3):
        if len({x[a], x[b], x[c]}) < 3:
            continue
        z = x[a:b] + x[c:] + x[:a] + x[b:c]
        if cycmin(z) == target:
            r.append((a, b, c))
    return r
out = []
for k, n in ((1, 10), (2, 15), (3, 20)):
    for short in (1, 2, 3):
        if short >= 4 * k:
            continue
        m = 8 * k + short
        tested = 0
        attempts = 0
        while tested < 20:
            attempts += 1
            x = tuple((rng.randrange(n) for _ in range(m))) if k > 1 else tuple(rng.sample(range(m), m))
            if not unique_k(x, k) or len({x[0], x[short], x[short + 4 * k]}) < 3:
                continue
            y = x[:short] + x[short + 4 * k:] + x[short:short + 4 * k]
            cs = cuts(x, y)
            check(cs == [(0, short, short + 4 * k)], (k, x, cs))
            tested += 1
        out.append({'K': k, 'm': m, 'short_length': short, 'tested': tested, 'unique': True})
C = tuple(range(2, 52))
x = C + (0, 1, 0, 1)
y = C + (1, 0, 1, 0)
cs = cuts(x, y)
check(unique_k(x, 3), 'finite check failed')
check(cs == [(0, 50, 51), (0, 50, 53)], cs)
out.append({'K_unique_local_ambiguity': True, 'K': 3, 'm': 54, 'alphabet': 52, 'cuts': cs})
report['two_long_and_local_ambiguity'] = out
print(json.dumps(report, indent=2))
