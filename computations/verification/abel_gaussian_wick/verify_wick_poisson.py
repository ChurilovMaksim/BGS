#!/usr/bin/env python3
"""Exact finite audits of the high-derivative collision proof.

Two representations: integer Gaussian monomial norms and directed contraction
graphs evaluated by hook characters. Exact Fraction Haar Gram inversion.
No Monte Carlo and no inference of an asymptotic theorem from finite cases.
"""
from collections import Counter
from functools import lru_cache
from fractions import Fraction
from itertools import combinations, permutations, product
from math import factorial, prod
from pathlib import Path
import argparse
import hashlib
import json

from verify_gaussian_hessian import check, hook_weight, inner, norm, trace_poly, times


def falling(n, k):
    return prod(range(n-k+1, n+1))


@lru_cache(None)
def compositions(total, slots):
    if slots == 1:
        return ((total,),)
    return tuple((v,)+rest for v in range(total+1)
                 for rest in compositions(total-v, slots-1))


def partial_matchings(k):
    for j in range(k+1):
        for aa in combinations(range(k), j):
            for bb in combinations(range(k), j):
                for image in permutations(bb):
                    yield tuple(zip(aa, image))


def derivative(p, edges):
    marks = Counter(edges)
    out = Counter()
    for nu, c in p.items():
        if all(nu[e] >= v for e, v in marks.items()):
            v = list(nu)
            weight = c
            for e, order in marks.items():
                weight *= falling(nu[e], order)
                v[e] -= order
            out[tuple(v)] += weight
    return dict(out)


def tensor(p, k):
    active = sorted({i for nu in p for i, v in enumerate(nu) if v})
    out = {}
    for edges in product(active, repeat=k):
        d = derivative(p, edges)
        if d:
            out[edges] = d
    return out


def contracted_norm(t, n, k, matching):
    aa, bb = {i for i, _ in matching}, {j for _, j in matching}
    out = {}
    for edges, polynomial in t.items():
        upper, lower = tuple(e//n for e in edges), tuple(e % n for e in edges)
        if any(upper[i] != lower[j] for i, j in matching):
            continue
        key = tuple(upper[i] for i in range(k) if i not in aa)
        key += tuple(lower[j] for j in range(k) if j not in bb)
        out.setdefault(key, Counter()).update(polynomial)
    return sum(norm(p) for p in out.values())


@lru_cache(None)
def contraction_cycles(k, matching, order):
    """Return (number of unit creation edges, tuple of gap indices) per cycle."""
    parent = list(range(4*k))

    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i

    def join(i, j):
        parent[root(i)] = root(j)

    aa, bb = {i for i, _ in matching}, {j for _, j in matching}
    for i, j in matching:
        join(i, k+j)
        join(2*k+i, 3*k+j)
    for i in range(k):
        if i not in aa:
            join(i, 2*k+i)
        if i not in bb:
            join(k+i, 3*k+i)
    edges = [(2*k+i, 3*k+i, 1, None) for i in range(k)]
    edges += [(k+order[i], order[(i+1) % k], 0, i) for i in range(k)]
    graph = {}
    incoming = Counter()
    for v, w, creation, gap in edges:
        v, w = root(v), root(w)
        check(v not in graph, 'not a directed cycle cover', k, matching, order)
        graph[v] = (w, creation, gap)
        incoming[w] += 1
    check(set(graph) == set(incoming) and all(v == 1 for v in incoming.values()),
          'unbalanced contraction graph', k, matching, order)
    seen, cycles = set(), []
    for start in graph:
        if start in seen:
            continue
        v, units, gaps = start, 0, []
        while v not in seen:
            seen.add(v)
            v, u, g = graph[v]
            units += u
            if g is not None:
                gaps.append(g)
        check(v == start, 'cycle traversal', k, matching, order)
        check(units or gaps, 'zero loop without any marked gap', k, matching, order)
        cycles.append((units, tuple(gaps)))
    all_gaps = [g for _, gaps in cycles for g in gaps]
    check(sorted(all_gaps) == list(range(k)), 'gap partition')
    check(sum(u for u, _ in cycles) == k, 'creation-edge partition')
    return tuple(cycles)


@lru_cache(None)
def trace_overlap(n, parts):
    zeros = parts.count(0)
    positive = tuple(v for v in parts if v)
    m = sum(positive)
    numerator = [0]*(m+1)
    numerator[0] = 1
    for v in positive:
        for j in range(m, v-1, -1):
            numerator[j] -= numerator[j-v]
    coefficients, s = [], 0
    for value in numerator[:m]:
        s += value
        coefficients.append(s)
    check(all(abs(v) <= 2**len(positive) for v in coefficients), 'hook character bound')
    value = n**zeros*sum(coefficients[j]*hook_weight(n, m, j)
                         for j in range(min(n, m)))
    hm = sum(hook_weight(n, m, j) for j in range(min(n, m)))
    check(0 <= value <= n**zeros*2**len(positive)*hm, 'positive trace overlap bound')
    return value


def graph_norm(n, m, k, matching):
    value = 0
    for tail in permutations(range(1, k)):
        cycles = contraction_cycles(k, matching, (0,)+tail)
        for gaps in compositions(m-k, k):
            parts = tuple(sorted(units+sum(gaps[g] for g in indices)
                                 for units, indices in cycles))
            value += trace_overlap(n, parts)
    return m*value


def partition_parts(total, minimum=1):
    if not total:
        yield ()
    for v in range(minimum, total+1):
        for tail in partition_parts(total-v, v):
            yield (v,)+tail


def permutation_cycles(p):
    seen, cycles = set(), 0
    for i in range(len(p)):
        if i not in seen:
            cycles += 1
            j = i
            while j not in seen:
                seen.add(j)
                j = p[j]
    return cycles


def inverse_matrix(a):
    size = len(a)
    a = [[Fraction(v) for v in row]+[Fraction(i == j) for j in range(size)]
         for i, row in enumerate(a)]
    for col in range(size):
        pivot = next(i for i in range(col, size) if a[i][col])
        a[col], a[pivot] = a[pivot], a[col]
        v = a[col][col]
        a[col] = [x/v for x in a[col]]
        for i in range(size):
            if i != col and a[i][col]:
                v = a[i][col]
                a[i] = [x-v*y for x, y in zip(a[i], a[col])]
    return [row[size:] for row in a]


def input_pairing(t, n, k, tau):
    inv = [tau.index(i) for i in range(2*k)]
    value = 0
    for z in product(range(n), repeat=2*k):
        aa, dd = z[:k], z[k:]
        bb = tuple(z[inv[i]] for i in range(k))
        cc = tuple(z[inv[k+i]] for i in range(k))
        e = tuple(a*n+b for a, b in zip(aa, bb))
        f = tuple(c*n+d for c, d in zip(cc, dd))
        value += inner(t.get(e, {}), t.get(f, {}))
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    cases, contraction_checks, swaps = [], 0, 0
    for n, m, maxk in ((2, 4, 3), (2, 5, 4), (2, 6, 4), (2, 7, 4),
                       (3, 4, 3), (3, 5, 3), (3, 6, 3)):
        p = trace_poly(n, m)
        hm = norm(p)
        w = [hook_weight(n, m, j) for j in range(min(n, m))]
        jbar = Fraction(sum(j*v for j, v in enumerate(w)), hm)
        for k in range(1, maxk+1):
            t = tensor(p, k)
            energy = falling(m, k)*hm
            check(sum(norm(v) for v in t.values()) == energy, 'total degree tensor norm', n,m,k)
            for matching in partial_matchings(k):
                direct = contracted_norm(t, n, k, matching)
                graphical = graph_norm(n, m, k, matching)
                check(direct == graphical, 'partial-contraction graph norm', n,m,k,matching,direct,graphical)
                contraction_checks += 1
            if k >= 2:
                overlap = 0
                for edges, polynomial in t.items():
                    a, b = divmod(edges[0], n)
                    c, d = divmod(edges[1], n)
                    swapped = (c*n+b, a*n+d)+edges[2:]
                    overlap += inner(polynomial, t.get(swapped, {}))
                check(Fraction(overlap, energy) == 1-2*jbar/(m-1), 'higher upper-swap identity',n,m,k)
                swaps += 1
            cases.append({'N':n,'m':m,'k':k,'nonzero_tensor_coordinates':len(t)})

    overlap_checks = 0
    for n in (2,3):
        for m in range(2,8):
            pm = trace_poly(n,m)
            for parts in partition_parts(m):
                pp = {(0,)*(n*n):1}
                for v in parts:
                    pp = times(pp,trace_poly(n,v))
                check(inner(pm,pp) == trace_overlap(n,parts), 'hook trace-product overlap',n,m,parts)
                overlap_checks += 1

    graph_checks = Counter()
    for k in range(1,6):
        for matching in partial_matchings(k):
            for tail in permutations(range(1,k)):
                contraction_cycles(k,matching,(0,)+tail)
                graph_checks[k] += 1

    haar_checks = 0
    for n, m, k, outputs in (
        (3,4,1, ((0,), (1,))),
        (4,4,2, ((1,1),(0,0),(1,4),(1,2),(1,11))),
    ):
        ps = list(permutations(range(2*k)))
        gram = [[n**permutation_cycles(tuple(s.index(tau[i]) for i in range(2*k)))
                 for tau in ps] for s in ps]
        inverse = inverse_matrix(gram)
        for i,row in enumerate(gram):
            for j in range(len(ps)):
                check(sum(row[l]*inverse[l][j] for l in range(len(ps))) == (i==j), 'exact Haar Gram inverse')
        t = tensor(trace_poly(n,m),k)
        pairings = [input_pairing(t,n,k,tau) for tau in ps]
        for edges in outputs:
            upper,lower = tuple(e//n for e in edges),tuple(e % n for e in edges)
            pos,neg = upper+lower,lower+upper
            value = 0
            for i,sigma in enumerate(ps):
                if all(pos[l] == neg[sigma[l]] for l in range(2*k)):
                    value += sum(inverse[i][j]*pairings[j] for j in range(len(ps)))
            check(value == norm(t.get(edges,{})), 'Haar input/output contraction dictionary',n,m,k,edges)
            haar_checks += 1

    moment_checks = 0
    row_checks = 0
    bounded_weight_checks = 0
    for n,m in ((2,4),(2,6),(3,5),(3,6)):
        p = trace_poly(n,m)
        hm = norm(p)
        for r in range(1,4):
            direct = sum(c*c*prod(factorial(v) for v in nu)*falling(sum(v>=2 for v in nu),r)
                         for nu,c in p.items())
            weighted = 0
            for edges in permutations(range(n*n),r):
                weighted += norm(derivative(p,tuple(e for e in edges for _ in range(2))))
            weighted = Fraction(weighted,2**r)
            difference_bound = 0
            for edges in permutations(range(n*n),r):
                for i in range(r):
                    orders = tuple(e for j,e in enumerate(edges) for _ in range(3 if i==j else 2))
                    difference_bound += norm(derivative(p,orders))
            difference_bound = Fraction(difference_bound,2**r)
            check(0 <= weighted-direct <= difference_bound, 'factorial indicator comparison',n,m,r)
            moment_checks += 1

        for rows in ((0,), (0,0), (0,0,0), (0,1), (0,0,1)):
            orders = Counter(rows)
            direct = sum(c*c*prod(factorial(v) for v in nu)*prod(
                         falling(sum(nu[a*n:(a+1)*n]),k) for a,k in orders.items())
                         for nu,c in p.items())
            via_derivatives = sum(norm(derivative(p,tuple(a*n+b for a,b in zip(rows,lower))))
                                  for lower in product(range(n),repeat=len(rows)))
            check(direct == via_derivatives,'row falling-factorial derivative identity',n,m,rows)
            row_checks += 1
        triple_mass = Fraction(sum(c*c*prod(factorial(v) for v in nu)
                                   for nu,c in p.items() if max(nu)>=3),hm)
        for family in ('phase','disk','gaussian'):
            def q(j):
                if family == 'phase': return Fraction(1,factorial(j))
                if family == 'disk': return Fraction(2**j,factorial(j+1))
                return Fraction(1)
            exact = Fraction(0)
            transform = Fraction(0)
            for nu,c in p.items():
                weight = Fraction(c*c*prod(factorial(v) for v in nu),hm)
                collisions = sum(v*(v-1)//2 for v in nu)
                exact += weight*prod(q(v) for v in nu)
                transform += weight*q(2)**collisions
            check(abs(exact-transform) <= triple_mass,'bounded radial-moment comparison',n,m,family)
            bounded_weight_checks += 1

    result = {'status':'PASS','arithmetic':'exact integers and Fraction rationals',
      'partial_contraction_norm_checks':contraction_checks,'higher_swap_checks':swaps,
      'trace_product_overlap_checks':overlap_checks,'abstract_directed_graph_checks':dict(graph_checks),
      'haar_dictionary_checks':haar_checks,'factorial_indicator_checks':moment_checks,
      'row_occupation_identity_checks':row_checks,'bounded_radial_weight_checks':bounded_weight_checks,
      'cases':cases,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'nonclaims':['No asymptotic conclusion follows from these finite cases.',
                   'No physical signed remainder, non-flat extension, or BGS verification.']}
    rendered = json.dumps(result,indent=2)+'\n'
    if args.output:
        args.output.write_text(rendered,encoding='utf-8')
    print(rendered,end='')


if __name__ == '__main__':
    main()
