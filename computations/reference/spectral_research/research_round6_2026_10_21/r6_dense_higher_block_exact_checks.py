#!/usr/bin/env python3
"""Exact finite checks of the higher-block involution and its connected defect.

These checks use integers and fractions. They test finite identities only;
they are not numerical evidence for H_diag or for its asymptotic negation.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations, product
from math import prod
import json


def trim(poly):
    return {key: value for key, value in poly.items() if value}


def add_poly(left, right, scale=1):
    out = defaultdict(int, left)
    for key, value in right.items():
        out[key] += scale * value
    return trim(out)


def cycle_count(selected, successor):
    seen = set()
    count = 0
    for start in selected:
        if start in seen:
            continue
        count += 1
        u = start
        while u not in seen:
            seen.add(u)
            u = successor[u]
        assert u == start
    assert seen == set(selected)
    return count


def swap_successors(successor, pair):
    other = dict(successor)
    u, v = pair
    other[u], other[v] = other[v], other[u]
    return other


def first_bad_pair(states, selected):
    for u, v in combinations(selected, 2):
        if states[u][1:] == states[v][1:]:
            return (u, v)
    return None


def object_key(selected, successor):
    return (tuple(selected), tuple(successor[u] for u in selected))


def edges_and_amplitude(U, states, selected, successor):
    N = len(U)
    edge_counts = [0] * (N * N)
    amplitude = 1
    for u in selected:
        v = successor[u]
        assert len(states[u]) == 1 or states[u][1:] == states[v][:-1]
        a, b = states[u][-1], states[v][-1]
        assert U[a][b] != 0
        edge_counts[N * a + b] += 1
        amplitude *= U[a][b]
    return tuple(edge_counts), amplitude


def all_objects(U, K):
    states = tuple(product(range(len(U)), repeat=K))
    D = len(states)
    allowed = {
        u: tuple(v for v in range(D)
                 if (K == 1 or states[u][1:] == states[v][:-1])
                 and U[states[u][-1]][states[v][-1]] != 0)
        for u in range(D)
    }
    objects = []
    for size in range(D + 1):
        for selected in combinations(range(D), size):
            pool = set(selected)
            successor = {}

            def recurse(index):
                if index == size:
                    objects.append((selected, dict(successor)))
                    return
                u = selected[index]
                for v in allowed[u]:
                    if v not in pool:
                        continue
                    successor[u] = v
                    pool.remove(v)
                    recurse(index + 1)
                    pool.add(v)
                    del successor[u]

            recurse(0)
    return states, objects


def verify_level(U, K, previous=None):
    states, objects = all_objects(U, K)
    Z = defaultdict(int)
    R = defaultdict(int)
    bad_single = defaultdict(int)
    all_keys = set()
    survivor_keys = set()
    bad_count = 0
    single_count = 0
    for selected, successor in objects:
        key = object_key(selected, successor)
        assert key not in all_keys
        all_keys.add(key)
        c = cycle_count(selected, successor)
        edge_counts, amplitude = edges_and_amplitude(U, states, selected, successor)
        Z[len(selected), c] += (-1) ** c * amplitude
        single_count += c == 1
        if K == 1:
            continue
        pair = first_bad_pair(states, selected)
        if pair is not None:
            bad_count += 1
            other = swap_successors(successor, pair)
            assert other != successor
            assert swap_successors(other, first_bad_pair(states, selected)) == successor
            other_c = cycle_count(selected, other)
            other_edges, other_amplitude = edges_and_amplitude(U, states, selected, other)
            assert abs(c - other_c) == 1
            assert other_edges == edge_counts
            assert other_amplitude == amplitude
            if c < other_c:
                R[len(selected), c - 1] += (-1) ** c * amplitude
            if c == 1:
                assert other_c == 2
                bad_single[len(selected)] += amplitude
        else:
            lower_states = previous["states"]
            lower_index = {state: i for i, state in enumerate(lower_states)}
            suffix = {u: lower_index[states[u][1:]] for u in selected}
            lower_selected = tuple(sorted(suffix.values()))
            rho = {suffix[u]: suffix[successor[u]] for u in selected}
            assert len(lower_selected) == len(set(lower_selected))
            assert cycle_count(lower_selected, rho) == c
            lower_edges, lower_amplitude = edges_and_amplitude(
                U, lower_states, lower_selected, rho)
            assert lower_edges == edge_counts
            assert lower_amplitude == amplitude
            lower_key = object_key(lower_selected, rho)
            assert lower_key not in survivor_keys
            survivor_keys.add(lower_key)
            predecessor = {v: u for u, v in rho.items()}
            upper_index = {state: i for i, state in enumerate(states)}
            restored = {
                a: upper_index[(lower_states[predecessor[a]][0],) + lower_states[a]]
                for a in lower_selected
            }
            restored_selected = tuple(sorted(restored.values()))
            restored_pi = {restored[a]: restored[rho[a]] for a in lower_selected}
            assert object_key(restored_selected, restored_pi) == key

    Z, R = trim(Z), trim(R)
    if K > 1:
        assert survivor_keys == previous["keys"]
        defect = defaultdict(int)
        for (n, power), coefficient in R.items():
            defect[n, power + 1] += coefficient
            defect[n, power + 2] -= coefficient
        assert add_poly(Z, previous["Z"], -1) == trim(defect)
        C = {n: -value for (n, c), value in Z.items() if c == 1}
        Cprev = {n: -value for (n, c), value in previous["Z"].items() if c == 1}
        assert add_poly(C, Cprev, -1) == trim(bad_single)
        assert {n: -value for (n, c), value in R.items() if c == 0} == trim(bad_single)
        at_one = defaultdict(int)
        lower_at_one = defaultdict(int)
        for (n, c), coefficient in Z.items():
            at_one[n] += coefficient
        for (n, c), coefficient in previous["Z"].items():
            lower_at_one[n] += coefficient
        assert trim(at_one) == trim(lower_at_one)
        assert all(n <= len(U) or coefficient == 0 for n, coefficient in at_one.items())

    return {"states": states, "keys": all_keys, "Z": Z, "R": R,
            "summary": {"N": len(U), "K": K, "objects": len(objects),
                        "bad_objects": bad_count,
                        "survivors": len(survivor_keys) if K > 1 else len(objects),
                        "single_cycles": single_count}}


def matmul(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


def verify_traces(U, K, max_n=9):
    states = tuple(product(range(len(U)), repeat=K))
    B = [[int(K == 1 or u[1:] == v[:-1]) * U[u[-1]][v[-1]]
          for v in states] for u in states]
    UB, BB = U, B
    for n in range(1, max_n + 1):
        assert sum(UB[i][i] for i in range(len(U))) == sum(BB[i][i] for i in range(len(B)))
        if n != max_n:
            UB, BB = matmul(UB, U), matmul(BB, B)


def canonical_rotation(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def blocks(word, K):
    n = len(word)
    return tuple(tuple(word[(i + j) % n] for j in range(K)) for i in range(n))


def verify_first_failure(U, max_n, K):
    seen_sources = set()
    seen_images = set()
    counts = defaultdict(int)
    for n in range(1, max_n + 1):
        for word in product(range(len(U)), repeat=n):
            if len(set(word)) == n or len(set(blocks(word, K))) != n:
                continue
            canon = canonical_rotation(word)
            if canon in seen_sources:
                continue
            seen_sources.add(canon)
            q = next(q for q in range(2, K + 1) if len(set(blocks(canon, q))) == n)
            states = tuple(product(range(len(U)), repeat=q))
            index = {state: i for i, state in enumerate(states)}
            ordered = tuple(index[state] for state in blocks(canon, q))
            selected = tuple(sorted(ordered))
            successor = {ordered[i]: ordered[(i + 1) % n] for i in range(n)}
            assert cycle_count(selected, successor) == 1
            pair = first_bad_pair(states, selected)
            assert pair is not None
            other = swap_successors(successor, pair)
            assert cycle_count(selected, other) == 2
            assert edges_and_amplitude(U, states, selected, successor) == edges_and_amplitude(
                U, states, selected, other)
            image = (q, object_key(selected, other))
            assert image not in seen_images
            seen_images.add(image)
            restored = swap_successors(other, pair)
            u = selected[0]
            recovered = []
            for _ in range(n):
                recovered.append(states[u][0])
                u = restored[u]
            assert canonical_rotation(tuple(recovered)) == canon
            counts[q] += 1
    assert len(seen_sources) == len(seen_images)
    return {"N": len(U), "max_n": max_n, "K": K,
            "injective_pairs": len(seen_images), "by_first_failure": dict(counts)}


def verify_identification_rank(max_n=75):
    count = 0
    for n in range(3, max_n + 1):
        for K in range(1, (n + 1) // 2):
            for offset in range(1, n):
                parent = list(range(n))

                def root(x):
                    while parent[x] != x:
                        parent[x] = parent[parent[x]]
                        x = parent[x]
                    return x

                rank = 0
                for u in range(K):
                    a, b = root(u), root((u + offset) % n)
                    if a != b:
                        parent[a] = b
                        rank += 1
                assert rank == K
                count += 1
    return count


def verify_positive_bounds(max_n=8):
    # P = [[9,16],[16,9]]/25 tensor J_2. It is unistochastic,
    # doubly stochastic, max P=(32/25)/4, ||P-J||=7/25 < 1/2.
    N, denominator, C, d = 4, 50, Fraction(32, 25), 3
    numerator = [[9 if a // 2 == b // 2 else 16 for b in range(N)] for a in range(N)]
    checked_events = 0
    checked_words = 0
    for n in range(3, max_n + 1):
        Ks = tuple(range(1, (n + 1) // 2))
        total = 0
        vertex_simple = 0
        collision = defaultdict(int)
        union_collision = defaultdict(int)
        for word in product(range(N), repeat=n):
            checked_words += 1
            weight = prod(numerator[word[i]][word[(i + 1) % n]] for i in range(n))
            total += weight
            if len(set(word)) == n:
                vertex_simple += weight
            for K in Ks:
                blocklist = blocks(word, K)
                if len(set(blocklist)) != n:
                    union_collision[K] += weight
                for offset in range(1, n):
                    if blocklist[0] == blocklist[offset]:
                        collision[K, offset] += weight
        assert Fraction(total, denominator ** n) == 1 + Fraction(-7, 25) ** n
        m = n // d
        vertex_bound = C * prod(1 - Fraction(j, 2 * N) for j in range(1, m))
        assert Fraction(vertex_simple, denominator ** n) <= vertex_bound
        if n > N:
            assert vertex_simple == 0
        for K in Ks:
            one_event_bound = C * (C / N) ** K
            for offset in range(1, n):
                assert Fraction(collision[K, offset], denominator ** n) <= one_event_bound
                checked_events += 1
            assert Fraction(union_collision[K], denominator ** n) <= n * (n - 1) // 2 * one_event_bound

    # Distinct-label sampling can also be checked by exact falling factorials
    # for P=J, at sizes where direct enumeration would be unnecessary.
    uniform_checks = 0
    for N in range(3, 101):
        for n in range(3, N + 1):
            mass = Fraction(prod(range(N - n + 1, N + 1)), N ** n)
            m = n // 3
            bound = prod(1 - Fraction(j, 2 * N) for j in range(1, m))
            assert mass <= bound
            uniform_checks += 1
    return {"nonuniform_words": checked_words, "individual_collision_events": checked_events,
            "uniform_vertex_simple_cases": uniform_checks}


def polynomial_json(poly):
    return {f"z^{n} t^{c}": str(value) if isinstance(value, Fraction) else value
            for (n, c), value in sorted(poly.items())}


def main():
    U2 = [[2, 3], [5, 7]]
    U3 = [[2, 3, 5], [7, 11, 13], [17, 19, 23]]
    summaries = []
    example = None
    for U, top in ((U2, 3), (U3, 2)):
        previous = None
        for K in range(1, top + 1):
            result = verify_level(U, K, previous)
            verify_traces(U, K)
            summaries.append(result["summary"])
            if len(U) == 2 and K == 2:
                example = {"Z2_minus_Z1": polynomial_json(add_poly(result["Z"], previous["Z"], -1)),
                           "R2": polynomial_json(result["R"])}
            previous = result
    orthogonal_numerator = [[7, -4, -4], [-4, 1, -8], [-4, -8, 1]]
    orthogonal = [[Fraction(value, 9) for value in row] for row in orthogonal_numerator]
    assert matmul(orthogonal, [list(col) for col in zip(*orthogonal)]) == [
        [int(i == j) for j in range(3)] for i in range(3)]
    orthogonal_lower = verify_level(orthogonal, 1)
    orthogonal_upper = verify_level(orthogonal, 2, orthogonal_lower)
    verify_traces(orthogonal, 2)
    assert orthogonal_upper["R"][3, 0] != 0
    output = {
        "status": "PASS: every assertion used exact integer or rational arithmetic",
        "pseudoorbit_cases": summaries,
        "nonzero_connected_defect_example_U": U2,
        "nonzero_connected_defect_example": example,
        "exact_orthogonal_3_by_3_check": {
            "matrix_numerator": orthogonal_numerator, "matrix_denominator": 9,
            "lower": orthogonal_lower["summary"], "upper": orthogonal_upper["summary"],
            "z3_coefficient_of_R_at_t_zero": str(orthogonal_upper["R"][3, 0])},
        "first_failure_checks": [verify_first_failure(U2, 11, 4), verify_first_failure(U3, 7, 3)],
        "collision_rank_cases": verify_identification_rank(),
        "positive_mass_checks": verify_positive_bounds(),
        "scope": "Finite identity verification only; no asymptotic H_diag conclusion."
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
