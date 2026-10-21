"""Finite combinatorial discriminator, not an asymptotic spectral test.

Look for multiple valid three-cut reconnections of the same cyclic word.
All checks concern exact words; no numerical U_N is substituted.
"""
from itertools import combinations
from random import Random


def canon(x):
    return min(x[j:] + x[:j] for j in range(len(x)))


def unique_blocks(x, q):
    xx = x + x
    return len({xx[j:j+q] for j in range(len(x))}) == len(x)


def partners(x, internal_min):
    n = len(x)
    out = {}
    for i, j, k in combinations(range(n), 3):
        if min(j-i, k-j, n+i-k) < internal_min+1:
            continue
        if len({x[i], x[j], x[k]}) != 3:
            continue
        aa, bb, cc = x[i:j], x[j:k], x[k:]+x[:i]
        y = canon(aa+cc+bb)
        out.setdefault(y, []).append((i, j, k))
    return out


def main():
    rng = Random(2026102105)
    checked = 0
    multi = 0
    for n, alphabet, internal_min in [(9, 5, 1), (12, 5, 2),
                                      (15, 7, 3), (18, 9, 4)]:
        for _ in range(2000):
            x = tuple(rng.randrange(alphabet) for _ in range(n))
            if not unique_blocks(x, internal_min+1):
                continue
            checked += 1
            for y, cuts in partners(x, internal_min).items():
                if len(cuts) > 1:
                    multi += 1
                    print({"counterexample": True, "n": n,
                           "alphabet": alphabet, "L": internal_min,
                           "x": x, "y": y, "cuts": cuts,
                           "unique_L_plus_1_blocks": True})
                    return
    print({"tested_words_with_unique_blocks": checked,
           "multiple_markings_found": multi,
           "status": "finite search only; no uniqueness theorem"})


if __name__ == "__main__":
    main()
