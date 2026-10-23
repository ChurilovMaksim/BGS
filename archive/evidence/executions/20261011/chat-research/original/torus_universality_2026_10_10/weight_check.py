"""Exact finite weight-multiplicity controls; not a universal proof.

Integer Gelfand--Tsetlin recursion, with an independent C++ implementation.
All selected dominant integer weights are enumerated, not sampled.
"""
from functools import lru_cache
from itertools import product
from math import prod
from fractions import Fraction
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def lower_rows(top):
    return product(*(range(top[i + 1], top[i] + 1) for i in range(len(top) - 1)))


@lru_cache(None)
def multiplicity(top, content):
    if len(top) != len(content) or sum(top) != sum(content):
        return 0
    if len(top) == 1:
        return int(top[0] == content[0])
    target = sum(content[:-1])
    return sum(multiplicity(tuple(row), content[:-1])
               for row in lower_rows(top) if sum(row) == target)


def dimension(lam):
    return prod(Fraction(lam[i] - lam[j] + j - i, j - i)
                for i in range(len(lam)) for j in range(i + 1, len(lam)))


def dominant_weights(n, bound, prefix=()):
    if len(prefix) == n:
        if sum(prefix) == 0 and any(prefix):
            yield prefix
        return
    upper = prefix[-1] if prefix else bound
    for value in range(-bound, upper + 1):
        partial = prefix + (value,)
        remaining = n - len(partial)
        if sum(partial) - remaining * bound <= 0 <= sum(partial) + remaining * value:
            yield from dominant_weights(n, bound, partial)


def run():
    rows = []
    seen = set()
    ranges = [(n, 2) for n in range(2, 8)] + [(n, 4) for n in range(2, 6)]
    for n, bound in ranges:
        for lam in dominant_weights(n, bound):
            if lam in seen:
                continue
            seen.add(lam)
            k = -lam[-1]
            top = tuple(v + k for v in lam)
            zero = multiplicity(top, (k,) * n)
            # Choose the last simple root: all root multiplicities coincide.
            root_content = (k,) * (n - 2) + (k + 1, k - 1)
            root = multiplicity(top, root_content)
            dim = dimension(lam)
            assert dim.denominator == 1
            dim = dim.numerator
            assert zero <= (n - 1) * root, (lam, zero, root)
            assert dim >= zero + n * (n - 1) * root, (lam, dim, zero, root)
            assert dim >= (n + 1) * zero
            rows.append({'N': n, 'lambda': list(lam), 'dimension': dim,
                         'm_zero': zero, 'm_root': root})
    rows.sort(key=lambda r: (r['N'], r['lambda']))
    equality = [r for r in rows if r['dimension'] == (r['N'] + 1) * r['m_zero']]
    for n in range(2, 8):
        adj = (1,) + (0,) * (n - 2) + (-1,)
        hit = next(r for r in rows if tuple(r['lambda']) == adj)
        assert hit['dimension'] == n * n - 1 and hit['m_zero'] == n - 1
    result = {'all_passed': True, 'exact_cases': len(rows), 'cases': rows,
              'equality_cases': equality,
              'enumeration': {'N_2_to_7': 'all dominant lambda in [-2,2]^N, sum=0, lambda!=0',
                              'N_2_to_5_extra': 'all dominant lambda in [-4,4]^N, sum=0, lambda!=0'},
              'arithmetic': 'Python arbitrary-size integers and Fraction',
              'cache': str(multiplicity.cache_info())}
    (ROOT / 'weight_check_results.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: v for k, v in result.items() if k not in ['cases', 'equality_cases']}))
    return result


if __name__ == '__main__':
    run()
