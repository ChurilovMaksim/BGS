"""Exact finite checks for dual_weyl_primitivity_and_quantitative_limits.md.

The all-N proof is in the accompanying manuscript. This script reconstructs
the original polynomial, checks every exceptional alias, and checks the
guaranteed support graph at finite composite moduli. No proxy kick is used.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction as F
import json


ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def mul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def scale(p, q):
    return {k: (v[0] * q, v[1] * q) for k, v in p.items()}


def polyadd(*polys):
    out = {}
    for p in polys:
        for k, v in p.items():
            out[k] = add(out.get(k, ZERO), v)
    return {k: v for k, v in out.items() if v != ZERO}


def polymul(p, q):
    out = {}
    for (k, l), a in p.items():
        for (j, h), b in q.items():
            v = (k + j, l + h)
            out[v] = add(out.get(v, ZERO), mul(a, b))
    return {k: v for k, v in out.items() if v != ZERO}


def cosq(n):
    return {(n, 0): (F(1, 2), F(0)), (-n, 0): (F(1, 2), F(0))}


def sinq(n):
    return {(n, 0): (F(0), F(-1, 2)), (-n, 0): (F(0), F(1, 2))}


unit = {(0, 0): ONE}
r = polymul(polyadd(unit, scale(cosq(7), F(-1))), polyadd(unit, cosq(1)))
cos_p_alpha = {(0, 1): (F(-3, 10), F(-2, 5)), (0, -1): (F(-3, 10), F(2, 5))}
coeff = polyadd(
    cosq(7), scale(r, F(1, 10)), scale(polymul(r, sinq(1)), F(1, 100)),
    scale(polymul(r, cos_p_alpha), F(1, 100)), scale(unit, F(-1, 10)),
)
assert len(coeff) == 32
assert max(abs(k) + abs(l) for k, l in coeff) == 9
assert all(coeff.get((-k, -l)) == (a, -b) for (k, l), (a, b) in coeff.items())
assert all((4000 * a).denominator == 1 and (4000 * b).denominator == 1 for a, b in coeff.values())


def aliases(n):
    out = {}
    for (k, l), v in coeff.items():
        point = (k % n, l % n)
        out[point] = add(out.get(point, ZERO), v)
    return {k: v for k, v in out.items() if v != ZERO}


gamma = (F(-3, 1000), F(-1, 250))
expected = {
    3: ((F(19, 40), F(-3, 800)), (gamma[0] / 2, gamma[1] / 2), (F(19, 40), F(3, 800))),
    5: ((F(1, 40), F(-7, 800)), gamma, (F(17, 40), F(-1, 200))),
    7: (ZERO, ZERO, ZERO),
    9: ((F(1, 40), F(-3, 400)), gamma, (F(9, 20), F(-1, 400))),
    11: ((F(1, 20), F(-1, 200)), gamma, (F(0), F(-3, 800))),
}
default = ((F(1, 20), F(-1, 200)), gamma, (F(0), F(-1, 400)))

for n in range(3, 202, 2):
    c = aliases(n)
    actual = (c.get((1, 0), ZERO), c.get((0, 1), ZERO), c.get((2 % n, 0), ZERO))
    assert actual == expected.get(n, default), (n, actual)
assert aliases(7) == {(0, 0): (F(9, 10), F(0))}


def transport(n, v):
    k, l = v
    return ((3 * k + 2 * l) % n, (4 * k + 3 * l) % n)


def reached(adjacency, start):
    seen = {start}
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w in adjacency[v]:
            if w not in seen:
                seen.add(w)
                queue.append(w)
    return seen


checked_graphs = []
for n in range(3, 66, 2):
    if n == 7:
        continue
    labels = [(k, l) for k in range(n) for l in range(n) if (k, l) != (0, 0)]
    adjacency = {v: set() for v in labels}
    for v in labels:
        w = transport(n, v)
        adjacency[v].add(w)
        k, l = w
        if l:
            adjacency[v].update([((k + 1) % n, l), ((k - 1) % n, l)])
        if k:
            adjacency[v].update([(k, (l + 1) % n), (k, (l - 1) % n)])
    anchor = (1, -2 % n)
    adjacency[anchor].add(anchor)  # Nonzero derivative proved from b_N and omega=4.
    reverse = {v: set() for v in labels}
    for v, neighbours in adjacency.items():
        for w in neighbours:
            reverse[w].add(v)
    assert len(reached(adjacency, anchor)) == n * n - 1
    assert len(reached(reverse, anchor)) == n * n - 1
    e1, e2 = (1, 0), (0, 1)
    a, b = transport(n, e1), transport(n, e2)
    order = 1
    while (a, b) != (e1, e2):
        a, b = transport(n, a), transport(n, b)
        order += 1
        assert order <= 4 * n // 3
    assert (4 * n - 4) * order < 6 * n * n
    checked_graphs.append(n)

print(json.dumps({
    "exact_original_fourier_terms": len(coeff),
    "alias_checks_odd_N": [3, 201],
    "graph_checks": checked_graphs,
    "N7_exact_scalar": "9/10",
    "all_checks_passed": True,
}))
