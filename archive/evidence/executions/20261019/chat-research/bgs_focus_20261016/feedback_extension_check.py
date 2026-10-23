#!/usr/bin/env python3
"""Exact finite Green/reversal identities and leading trace-cycle counts."""
from __future__ import annotations

from collections import Counter
from fractions import Fraction as F
from itertools import permutations
from math import factorial, prod
import json
import sys

from feedback_covariance_check import Q, adj, eye, kernel, mul, rational_unitary


def inverse(a):
    n = len(a)
    c = [list(a[i]) + eye(n)[i] for i in range(n)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if c[i][j] != Q()), None)
        if pivot is None:
            raise ZeroDivisionError("exact singular matrix")
        c[j], c[pivot] = c[pivot], c[j]
        q = c[j][j]
        c[j] = [z / q for z in c[j]]
        for i in range(n):
            if i != j:
                z = c[i][j]
                c[i] = [x - z * y for x, y in zip(c[i], c[j])]
    return [row[n:] for row in c]


def add(a, b, sign=1):
    return [[x + sign * y for x, y in zip(r, s)] for r, s in zip(a, b)]


def reversal(s):
    n = len(s)
    return [[s[i][j] * s[j][i].conj() for j in range(n)] for i in range(n)]


def subset(a, keep):
    return [[a[i][j] for j in keep] for i in keep]


def green_checks():
    result = []
    phases = (Q(F(-1)), Q(F(0), F(1)), Q(F(3, 5), F(4, 5)))
    for n in range(2, 6):
        s = rational_unitary(n)
        b = reversal(s)
        c = kernel(s)
        p = [[z.abs2() for z in row] for row in s]
        energy = sum(z * z for row in p for z in row)
        # Four independent sums used for all three-label off-diagonal patterns.
        lhs = [sum(c[i*n+j][i*n+l].abs2() for i in range(n)
                   for j in range(n) for l in range(n)),
               sum(c[i*n+j][k*n+j].abs2() for i in range(n)
                   for k in range(n) for j in range(n)),
               sum(c[i*n+j][j*n+l].abs2() for i in range(n)
                   for j in range(n) for l in range(n)),
               sum(c[i*n+j][k*n+i].abs2() for i in range(n)
                   for j in range(n) for k in range(n))]
        b_energy = sum(z.abs2() for row in b for z in row)
        assert lhs == [energy, energy, b_energy, b_energy]
        assert sum(c[i*n+i][k*n+l].abs2() for i in range(n)
                   for k in range(n) for l in range(n)) == b_energy
        try:
            g = inverse(add(eye(n), b, -1))
        except ZeroDivisionError:
            g = None
        compression, inverse_expansions = 0, 0
        excluded = []
        for e in range(n):
            keep = [i for i in range(n) if i != e]
            den = 1 - b[e][e]
            bc = [[b[i][j] + b[i][e] * b[e][j] / den
                   for j in keep] for i in keep]
            gc = inverse(add(eye(n-1), bc, -1)) if g is not None else None
            if g is not None:
                assert gc == subset(g, keep)
                compression += 1
            for w in phases:
                q = w / (1 - s[e][e] * w)
                sp = [[s[i][j] + q * s[i][e] * s[e][j]
                       for j in keep] for i in keep]
                bp = reversal(sp)
                v = [s[i][e] * s[e][i].conj() for i in keep]
                c0 = [[s[i][e] * s[j][i].conj() * s[e][j]
                       for j in keep] for i in keep]
                explicit = [[b[i][j] + q*c0[a][z] + q.conj()*c0[z][a].conj()
                             + q.abs2()*v[a]*v[z].conj()
                             for z, j in enumerate(keep)] for a, i in enumerate(keep)]
                assert bp == explicit
                mean_formula = [[b[i][j] + v[a]*v[z].conj()/den
                                 for z, j in enumerate(keep)] for a, i in enumerate(keep)]
                assert mean_formula == bc
                if gc is not None:
                    try:
                        gp = inverse(add(eye(n-1), bp, -1))
                    except ZeroDivisionError:
                        excluded.append({"port": e, "reason": "I-Bprime singular; outside inverse-identity domain"})
                        continue
                    xi = add(bp, bc, -1)
                    lin = mul(mul(gc, xi), gc)
                    rem = mul(mul(mul(mul(gc, xi), gc), xi), gp)
                    assert gp == add(add(gc, lin), rem)
                    inverse_expansions += 1
        result.append({"n": n, "three_label_frobenius_identities": 4,
                       "diagonal_projector_identity": 1,
                       "reversal_feedback_identities": n*len(phases),
                       "old_green_exists": g is not None,
                       "green_compressions": compression,
                       "ordered_inverse_expansions": inverse_expansions,
                       "excluded_inverse_cases": excluded})
    return result


def partitions(n, lo=1):
    if n == 0:
        yield ()
    else:
        for j in range(lo, n+1):
            for tail in partitions(n-j, j):
                yield (j,) + tail


def edges(lengths, labels):
    out, offset = [], 0
    for m in lengths:
        word = labels[offset:offset+m]
        out.extend((word[j], word[(j+1) % m]) for j in range(m))
        offset += m
    assert offset == len(labels)
    return Counter(out)


def cycle_checks():
    cases, permutations_checked, nonzero = 0, 0, 0
    for k in range(1, 7):
        for ret in partitions(k):
            target_edges = edges(ret, tuple(range(k)))
            for adv in partitions(k):
                count = 0
                for labels in permutations(range(k)):
                    count += edges(adv, labels) == target_edges
                    permutations_checked += 1
                want = (prod(factorial(p) * m**p for m, p in Counter(ret).items())
                        if ret == adv else 0)
                assert count == want, (ret, adv, count, want)
                nonzero += count > 0
                cases += 1
    return {"K_range": [1, 6], "partition_pair_cases": cases,
            "advanced_label_permutations_checked": permutations_checked,
            "nonzero_matching_partition_cases": nonzero,
            "coverage": "all integer partition pairs at each K, all K! advanced labelings"}


def main():
    result = {"status": "passed", "green": green_checks(), "cycles": cycle_checks(),
              "arithmetic": "exact Q(i) and integer enumeration",
              "non_claims": ["No asymptotic proof by computation.",
                             "Inverse identities tested only where exact inverses exist.",
                             "Trace-cycle count concerns leading Gaussian model, not Heisenberg powers."]}
    with open(sys.argv[1], "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
