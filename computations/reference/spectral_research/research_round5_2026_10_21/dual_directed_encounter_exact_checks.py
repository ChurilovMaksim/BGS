"""Finite exact checks for the directed encounter note.

These checks do not establish the asymptotic theorem.  The mathematical
proof is in dual_directed_encounter_exact_visit_classes.md.
Only Python's standard library and exact rational arithmetic are used.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations, product


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def inverse(a):
    n = len(a)
    x = [list(row) + identity for row, identity in zip(a, eye(n))]
    for j in range(n):
        pivot = next(i for i in range(j, n) if x[i][j])
        x[j], x[pivot] = x[pivot], x[j]
        d = x[j][j]
        x[j] = [v / d for v in x[j]]
        for i in range(n):
            if i != j:
                d = x[i][j]
                x[i] = [u - d * v for u, v in zip(x[i], x[j])]
    return [row[n:] for row in x]


def determinant(a):
    a = [list(row) for row in a]
    ans = F(1)
    for j in range(len(a)):
        found = [i for i in range(j, len(a)) if a[i][j]]
        if not found:
            return F(0)
        pivot = found[0]
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            ans = -ans
        d = a[j][j]
        ans *= d
        for i in range(j + 1, len(a)):
            scale = a[i][j] / d
            a[i] = [u - scale * v for u, v in zip(a[i], a[j])]
    return ans


def minus_scalar_identity(a, lam):
    return [[lam * (i == j) - a[i][j] for j in range(len(a))]
            for i in range(len(a))]


def poly_add(a, b):
    out = [F(0)] * max(len(a), len(b))
    for j, x in enumerate(a):
        out[j] += x
    for j, x in enumerate(b):
        out[j] += x
    return out


def poly_mul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def poly_matmul(a, b):
    return [[sum_poly(poly_mul(a[i][k], b[k][j])
                      for k in range(len(b)))
             for j in range(len(b))] for i in range(len(a))]


def sum_poly(polys):
    ans = [F(0)]
    for p in polys:
        ans = poly_add(ans, p)
    return ans


def gf_checks():
    b = [[-1, 1, 0], [2, -1, -1], [-1, 0, 1]]
    count = 0
    for size in (3, 4):
        p = [[F(1, size) +
              (F(b[i][j], 100) if i < 3 and j < 3 else F(0))
              for j in range(size)] for i in range(size)]
        assert all(sum(row) == 1 for row in p)
        assert all(sum(p[i][j] for i in range(size)) == 1
                   for j in range(size))
        assert max(max(row) for row in p) <= F(2, size)
        a = [[p[i][j] - F(1, size) for j in range(size)]
             for i in range(size)]
        # Frobenius norm bounds the operator norm and is < 1/2 here.
        assert sum(x*x for row in a for x in row) < F(1, 4)
        # This is intentionally not a normal example.
        at = [list(col) for col in zip(*a)]
        assert matmul(a, at) != matmul(at, a)
        for v in range(size):
            dp = [[([F(0), p[i][j]] if i == v else [p[i][j]])
                   for j in range(size)] for i in range(size)]
            power = [[[F(i == j)] for j in range(size)]
                     for i in range(size)]
            for n in range(1, 7):
                power = poly_matmul(power, dp)
                trace_poly = sum_poly(power[i][i] for i in range(size))
                direct = [F(0)] * (n + 1)
                for word in product(range(size), repeat=n):
                    weight = F(1)
                    for j in range(n):
                        weight *= p[word[j]][word[(j + 1) % n]]
                    direct[word.count(v)] += weight
                trace_poly += [F(0)] * (n + 1 - len(trace_poly))
                assert trace_poly == direct
                count += 1
            for lam in (F(3, 4), F(1), F(5, 4), F(2)):
                resolvent = inverse(minus_scalar_identity(a, lam))
                r = matmul(a, resolvent)[v][v]
                det_perp = determinant(
                    minus_scalar_identity(a, lam)) / lam
                for z in (F(-1), F(0), F(1), F(2)):
                    tilted = [[p[i][j] * (z if i == v else 1)
                               for j in range(size)] for i in range(size)]
                    eta = z - 1
                    rhs = det_perp * (
                        (lam - 1) * (1 - eta * r) - eta / size)
                    assert determinant(
                        minus_scalar_identity(tilted, lam)) == rhs
                    count += 1
    return count


def rotations(word):
    return {word[j:] + word[:j] for j in range(len(word))}


def reversed_rotations(word):
    return rotations((word[0],) + tuple(reversed(word[1:])))


def edge_counts(word):
    return Counter((word[j], word[(j + 1) % len(word)])
                   for j in range(len(word)))


def trigram_counts(word):
    n = len(word)
    return Counter((word[(j - 1) % n], word[j], word[(j + 1) % n])
                   for j in range(n))


def good_hub(word, v):
    places = [j for j, w in enumerate(word) if w == v]
    n, m = len(word), len(places)
    if m < 3:
        return False
    gaps = [(places[(i + 1) % m] - places[i]) % n for i in range(m)]
    neighbors = [word[(j - 1) % n] for j in places]
    neighbors += [word[(j + 1) % n] for j in places]
    return min(gaps) >= 3 and len(set(neighbors)) == 2*m


def partner_classes(word, v):
    places = [j for j, w in enumerate(word) if w == v]
    n = len(word)
    pieces = []
    for i, pos in enumerate(places):
        end = places[(i + 1) % len(places)]
        length = (end - pos) % n
        pieces.append(tuple(word[(pos + j) % n] for j in range(length)))
    original = tuple(range(len(pieces)))
    for tail in permutations(range(1, len(pieces))):
        order = (0,) + tail
        if order != original:
            partner = tuple(w for i in order for w in pieces[i])
            yield partner


def inspect_word(word, hubs):
    n = len(word)
    old_rot = rotations(word)
    old_rev = reversed_rotations(word)
    old_edges = edge_counts(word)
    old_tri = trigram_counts(word)
    assert len(old_rot) == n
    seen = set()
    count = 0
    for v in hubs:
        assert good_hub(word, v)
        expected_classes = 1
        m = word.count(v)
        for k in range(1, m):
            expected_classes *= k
        expected_classes -= 1
        actual_classes = 0
        for y in partner_classes(word, v):
            actual_classes += 1
            assert edge_counts(y) == old_edges
            tri = trigram_counts(y)
            changed_centers = {u[1] for u in set(tri) | set(old_tri)
                               if tri[u] != old_tri[u]}
            assert changed_centers == {v}
            rot = rotations(y)
            assert len(rot) == n
            assert not (rot & old_rot)
            assert not (rot & old_rev)
            assert not (rot & seen)
            assert good_hub(y, v)
            # The partner relation is symmetric.
            assert any(word in rotations(back)
                       for back in partner_classes(y, v))
            seen.update(rot)
            count += n
        assert actual_classes == expected_classes
    return count


def encounter_checks():
    count = 0
    # Single hubs, every cyclic ordering through fixed order m=6.
    for m in range(3, 7):
        word = tuple(w for i in range(m) for w in (0, 2*i + 1, 2*i + 2))
        count += inspect_word(word, [0])
    # Every arrangement of 3 visits to hub 0 and 4 to hub 1.
    # Private neighbors make all 2m endpoints distinct.
    for zeros in combinations(range(7), 3):
        hubs = [0 if i in zeros else 1 for i in range(7)]
        word = tuple(w for i, v in enumerate(hubs)
                     for w in (v, 2 + 2*i, 3 + 2*i))
        count += inspect_word(word, [0, 1])
    return count


if __name__ == "__main__":
    print("Exact generating-function / rank-one checks:", gf_checks())
    print("Distinct directed partner pairs checked:", encounter_checks())
    print("All finite exact checks passed.")
