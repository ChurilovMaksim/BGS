"""Exact finite checks for the long-three-arc cancellation theorem.

No asymptotic conclusion is drawn from these checks.  The proof is in
dual_directed_encounter_marked_unitarity_resummation.md.
"""

from collections import Counter
from itertools import combinations, permutations, product
from random import Random


def rotations(word):
    return [word[j:] + word[:j] for j in range(len(word))]


def canonical(word):
    return min(rotations(word))


def reversed_canonical(word):
    return canonical(tuple(reversed(word)))


def regular(word, k):
    n = len(word)
    strings = {tuple(word[(j + t) % n] for t in range(k))
               for j in range(n)}
    return len(strings) == n


def edge_counts(word):
    return Counter((word[j], word[(j + 1) % len(word)])
                   for j in range(len(word)))


def markings(n, lower):
    for cuts in combinations(range(n), 3):
        gaps = tuple((cuts[(j + 1) % 3] - cuts[j]) % n
                     for j in range(3))
        if min(gaps) >= lower + 1:
            yield cuts, gaps


def arcs_at(word, cuts, gaps):
    return [tuple(word[(pos + t) % len(word)] for t in range(gap))
            for pos, gap in zip(cuts, gaps)]


def partner(arcs):
    return arcs[0] + arcs[2] + arcs[1]


def int_matmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b))] for i in range(len(a))]


def int_power(a, n):
    out = [[int(i == j) for j in range(len(a))] for i in range(len(a))]
    for _ in range(n):
        out = int_matmul(out, a)
    return out


def amplitude_numerator(word, b):
    ans = 1
    for j, x in enumerate(word):
        ans *= b[x][word[(j + 1) % len(word)]]
    return ans


def exact_endpoint_count_checks():
    # U=B/7 is an exact rational orthogonal matrix:
    # I - 2 vv^T/(v^Tv), v=(1,2,3).
    b = [[6, -2, -3], [-2, 3, -6], [-3, -6, -2]]
    assert int_matmul(b, b) == [[49 * int(i == j) for j in range(3)]
                               for i in range(3)]
    p_num = [[x*x for x in row] for row in b]
    checked = 0
    for n, lower in ((6, 1), (7, 1), (8, 1), (9, 2)):
        cuts_all = list(markings(n, lower))
        marked = 0
        coalesced = 0
        for word in product(range(3), repeat=n):
            ax = amplitude_numerator(word, b)
            for cuts, gaps in cuts_all:
                if len({word[pos] for pos in cuts}) != 3:
                    continue
                arcs = arcs_at(word, cuts, gaps)
                y = partner(arcs)
                term = n * ax * amplitude_numerator(y, b)
                marked += term
                ends_equal = len({arc[-1] for arc in arcs}) == 1
                assert (edge_counts(word) == edge_counts(y)) == ends_equal
                if ends_equal:
                    assert term >= 0
                    coalesced += term
                checked += 1
        contraction = 0
        coalesced_contraction = 0
        for lengths in product(range(lower, n), repeat=3):
            if sum(lengths) != n - 3:
                continue
            powers = [int_power(p_num, length) for length in lengths]
            for starts in permutations(range(3)):
                for ends in product(range(3), repeat=3):
                    term = 1
                    for i in range(3):
                        term *= powers[i][starts[i]][ends[i]]
                        term *= b[ends[i]][starts[(i + 1) % 3]]
                        term *= b[ends[i]][starts[(i - 1) % 3]]
                    contraction += term
                    if len(set(ends)) == 1:
                        coalesced_contraction += term
        # Every summand has the common denominator 7^(2n).
        assert 3 * marked == n*n * contraction
        assert 3 * coalesced == n*n * coalesced_contraction
    return checked


def flat_unitarity_checks():
    # Integer Walsh matrix divided by 2; P is exactly J.
    h = [[1, 1, 1, 1],
         [1, -1, 1, -1],
         [1, 1, -1, -1],
         [1, -1, -1, 1]]
    assert int_matmul(h, h) == [[4 * int(i == j) for j in range(4)]
                               for i in range(4)]
    for starts in permutations(range(4), 3):
        total = 0
        for ends in product(range(4), repeat=3):
            term = 1
            for i in range(3):
                term *= h[ends[i]][starts[(i + 1) % 3]]
                term *= h[ends[i]][starts[(i - 1) % 3]]
            total += term
        assert total == 0
    return 24


def make_edge_unique_word(rng, n, alphabet):
    for _ in range(10000):
        word = [rng.randrange(alphabet)]
        used = set()
        for _ in range(n - 1):
            options = [z for z in range(alphabet)
                       if (word[-1], z) not in used]
            if not options:
                break
            z = rng.choice(options)
            used.add((word[-1], z))
            word.append(z)
        if len(word) == n and (word[-1], word[0]) not in used:
            ans = tuple(word)
            assert regular(ans, 2)
            return ans
    raise AssertionError("Finite construction failed")


def unmarking_checks():
    rng = Random(20261021)
    words = [make_edge_unique_word(rng, 40, 10) for _ in range(12)]
    # A regular word with three equal arc endpoints and private interiors.
    words.append(tuple(v for i in range(3)
                       for v in tuple(range(1 + 12*i, 12 + 12*i)) + (0,)))
    checked = 0
    equal_count = 0
    for word in words:
        k = 2
        lower = 4*k + 2
        assert regular(word, k)
        seen = {}
        original = canonical(word)
        original_edges = edge_counts(word)
        for cuts, gaps in markings(len(word), lower):
            if len({word[pos] for pos in cuts}) != 3:
                continue
            arcs = arcs_at(word, cuts, gaps)
            y = partner(arcs)
            if not regular(y, k):
                continue
            cy = canonical(y)
            assert cy != original
            assert cy not in seen, (word, seen.get(cy), cuts)
            seen[cy] = cuts
            assert len(set(rotations(y))) == len(y)
            equal = len({arc[-1] for arc in arcs}) == 1
            assert (edge_counts(y) == original_edges) == equal
            equal_count += equal
            checked += 1
    assert equal_count > 0
    return checked, equal_count


def identification_rank_checks():
    checked = 0
    for n in range(3, 31):
        for k in range(1, n):
            for delta in range(1, n):
                parent = list(range(n))
                def find(x):
                    while parent[x] != x:
                        parent[x] = parent[parent[x]]
                        x = parent[x]
                    return x
                for u in range(k):
                    a, b = find(u), find((u + delta) % n)
                    parent[a] = b
                rank = n - len({find(x) for x in range(n)})
                assert 2*rank >= k
                checked += 1
    return checked


if __name__ == "__main__":
    print("Exact marked pair / edge-count checks:",
          exact_endpoint_count_checks())
    print("Exact flat-phase endpoint cancellations:", flat_unitarity_checks())
    print("Regular partner classes / coalesced examples:", unmarking_checks())
    print("Cyclic substring identification-rank checks:",
          identification_rank_checks())
    print("All finite exact checks passed.")
