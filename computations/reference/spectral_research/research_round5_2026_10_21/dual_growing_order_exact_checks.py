"""Exact finite checks for growing-order directed-arc cancellation.

These checks corroborate identities and uniqueness; the asymptotic theorem
is proved in dual_directed_encounter_growing_order_cancellation.md.
Only Python's standard library is used. No floating-point computation.
"""

from collections import Counter
from itertools import combinations, permutations, product
from math import comb, factorial, prod
from random import Random


def cycle_successor(order):
    successor = [None] * len(order)
    for i, v in enumerate(order):
        successor[v] = order[(i + 1) % len(order)]
    return tuple(successor)


def permitted_cycles(r):
    for tail in permutations(range(1, r)):
        order = (0,) + tail
        sigma = cycle_successor(order)
        if all(sigma[i] != (i + 1) % r for i in range(r)):
            yield order, sigma


def cycles_count(permutation):
    seen = set()
    count = 0
    for v in range(len(permutation)):
        if v not in seen:
            count += 1
            while v not in seen:
                seen.add(v)
                v = permutation[v]
    return count


def relative_permutation(sigma):
    r = len(sigma)
    inverse = [None] * r
    for i, v in enumerate(sigma):
        inverse[v] = i
    return tuple(inverse[(i + 1) % r] for i in range(r))


def literal_allowed(starts, sigma):
    r = len(starts)
    return all(starts[sigma[i]] != starts[(i + 1) % r]
               for i in range(r))


def permutation_checks():
    expected = {
        3: {1: 1}, 4: {2: 1}, 5: {1: 8}, 6: {2: 36},
        7: {1: 180, 3: 49}, 8: {2: 1604, 4: 21},
        9: {1: 8064, 3: 5144},
    }
    checked = 0
    for r, target in expected.items():
        found = Counter()
        for _, sigma in permitted_cycles(r):
            pi = relative_permutation(sigma)
            assert all(pi[i] != i for i in range(r))
            c = cycles_count(pi)
            assert (r - c) % 2 == 0
            found[c] += 1
            checked += 1
        assert dict(found) == target, (r, found)
        inclusion_exclusion = sum((-1)**j * comb(r, j) *
                                  factorial(r - j - 1)
                                  for j in range(r)) + (-1)**r
        assert sum(found.values()) == inclusion_exclusion
    return checked


def rotations(word):
    return [word[j:] + word[:j] for j in range(len(word))]


def canonical(word):
    return min(rotations(word))


def regular(word, k):
    n = len(word)
    return len({tuple(word[(j + u) % n] for u in range(k))
                for j in range(n)}) == n


def arcs_at(word, cuts, gaps):
    n = len(word)
    return [tuple(word[(i + u) % n] for u in range(gap))
            for i, gap in zip(cuts, gaps)]


def markings(n, r, lower):
    for cuts in combinations(range(n), r):
        gaps = tuple((cuts[(i + 1) % r] - cuts[i]) % n
                     for i in range(r))
        if min(gaps) >= lower + 1:
            yield cuts, gaps


def make_regular_word(rng, n, alphabet):
    for _ in range(10000):
        word = [rng.randrange(alphabet)]
        used = set()
        while len(word) < n:
            possible = [v for v in range(alphabet)
                        if (word[-1], v) not in used]
            if not possible:
                break
            v = rng.choice(possible)
            used.add((word[-1], v))
            word.append(v)
        if len(word) == n and (word[-1], word[0]) not in used:
            word = tuple(word)
            assert regular(word, 2)
            return word
    raise AssertionError("Deterministic finite construction exhausted")


def cross_order_unmarking_checks():
    # The same dictionary covers r=3,4,5. Repeated start labels are allowed.
    rng = Random(2026102105)
    n, k, lower = 35, 2, 6
    mark_by_r = {r: list(markings(n, r, lower)) for r in (3, 4, 5)}
    perm_by_r = {r: list(permitted_cycles(r)) for r in (3, 4, 5)}
    words = [make_regular_word(rng, n, 11) for _ in range(12)]
    # Also verifies the nonempty construction with distinct vertices.
    words.append(tuple(range(n)))
    checked = repeated_starts = 0
    checked_by_r = Counter()
    for word in words:
        seen = {}
        original = canonical(word)
        for r in (3, 4, 5):
            for cuts, gaps in mark_by_r[r]:
                arcs = arcs_at(word, cuts, gaps)
                starts = tuple(arc[0] for arc in arcs)
                for order, sigma in perm_by_r[r]:
                    if not literal_allowed(starts, sigma):
                        continue
                    partner = tuple(v for i in order for v in arcs[i])
                    if not regular(partner, k):
                        continue
                    cyclic_partner = canonical(partner)
                    assert cyclic_partner != original
                    representation = (r, cuts, sigma)
                    assert cyclic_partner not in seen, (
                        word, seen.get(cyclic_partner), representation)
                    seen[cyclic_partner] = representation
                    assert len(set(rotations(partner))) == n
                    checked += 1
                    checked_by_r[r] += 1
                    repeated_starts += len(set(starts)) < r
    assert all(checked_by_r[r] > 0 for r in (3, 4, 5))
    assert repeated_starts > 0
    return checked, repeated_starts, dict(checked_by_r)


def matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def matrix_power(a, n):
    out = [[int(i == j) for j in range(len(a))]
           for i in range(len(a))]
    for _ in range(n):
        out = matmul(out, a)
    return out


def endpoint_factorization_checks():
    # A nonflat exact orthogonal matrix U=B/25 from v=(1,2,2,4).
    v = (1, 2, 2, 4)
    b = [[25 * int(i == j) - 2 * v[i] * v[j] for j in range(4)]
         for i in range(4)]
    assert matmul(b, b) == [[625 * int(i == j) for j in range(4)]
                             for i in range(4)]
    pnum = [[a*a for a in row] for row in b]
    pows = {ell: matrix_power(pnum, ell) for ell in (2, 3)}
    rng = Random(715043)
    checked = repeated_starts = nonzero = 0
    for r in (3, 4, 5, 6):
        allowed_perms = list(permitted_cycles(r))
        if r == 6:
            allowed_perms = allowed_perms[:3]
        for _, sigma in allowed_perms:
            starts_list = [s for s in product(range(4), repeat=r)
                           if literal_allowed(s, sigma)]
            rng.shuffle(starts_list)
            for starts in starts_list[:12]:
                ells = tuple(2 + i % 2 for i in range(r))
                factors = []
                centered_factors = []
                for i, ell in enumerate(ells):
                    j, h = starts[(i + 1) % r], starts[sigma[i]]
                    assert sum(b[a][j]*b[a][h] for a in range(4)) == 0
                    factors.append(sum(pows[ell][starts[i]][a] *
                                       b[a][j]*b[a][h] for a in range(4)))
                    centered_factors.append(sum(
                        (4*pows[ell][starts[i]][a] - 625**ell) *
                        b[a][j]*b[a][h] for a in range(4)))
                direct = 0
                for ends in product(range(4), repeat=r):
                    term = 1
                    for i, a in enumerate(ends):
                        term *= pows[ells[i]][starts[i]][a]
                        term *= b[a][starts[(i + 1) % r]]
                        term *= b[a][starts[sigma[i]]]
                    direct += term
                assert direct == prod(factors)
                assert 4**r * direct == prod(centered_factors)
                checked += 1
                repeated_starts += len(set(starts)) < r
                nonzero += direct != 0
    assert repeated_starts > 0 and nonzero > 0
    return checked, repeated_starts, nonzero


def amplitude(word, b):
    return prod(b[x][word[(i + 1) % len(word)]]
                for i, x in enumerate(word))


def marked_count_checks():
    # U=B/5; N=2 forces repeated start labels in every r=4 presentation.
    b = [[3, -4], [-4, -3]]
    assert matmul(b, b) == [[25, 0], [0, 25]]
    pnum = [[v*v for v in row] for row in b]
    r = 4
    order, sigma = list(permitted_cycles(r))[0]
    checked = 0
    for n in (8, 9, 10):
        marked = 0
        for word in product(range(2), repeat=n):
            ax = amplitude(word, b)
            for cuts, gaps in markings(n, r, 1):
                arcs = arcs_at(word, cuts, gaps)
                starts = tuple(arc[0] for arc in arcs)
                if not literal_allowed(starts, sigma):
                    continue
                partner = tuple(v for i in order for v in arcs[i])
                marked += n * ax * amplitude(partner, b)
                checked += 1
        contraction = 0
        for ells in product(range(1, n-r+1), repeat=r):
            if sum(ells) != n-r:
                continue
            powers = [matrix_power(pnum, ell) for ell in ells]
            for starts in product(range(2), repeat=r):
                if not literal_allowed(starts, sigma):
                    continue
                for ends in product(range(2), repeat=r):
                    term = 1
                    for i, a in enumerate(ends):
                        term *= powers[i][starts[i]][a]
                        term *= b[a][starts[(i+1) % r]]
                        term *= b[a][starts[sigma[i]]]
                    contraction += term
        # Both sums have common denominator 5^(2n), including periodic words.
        assert r * marked == n*n * contraction
    assert checked > 0
    return checked


if __name__ == "__main__":
    print("Permitted permutations / cycle counts:", permutation_checks(),
          flush=True)
    print("Cross-order regular classes / repeated starts / by r:",
          cross_order_unmarking_checks(), flush=True)
    print("Exact endpoint factorizations / repeated starts / nonzero:",
          endpoint_factorization_checks(), flush=True)
    print("Exact r=4 marked-root counts:", marked_count_checks(), flush=True)
    print("All finite exact checks passed.", flush=True)
