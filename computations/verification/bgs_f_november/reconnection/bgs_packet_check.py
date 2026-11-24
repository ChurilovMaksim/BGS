"""Exact integer checks for permutation cylinders and the Pell counterexample."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import Counter, defaultdict
from itertools import permutations, product
from math import gcd, prod
from pathlib import Path
import json
import sys

def mul(a, b):
    n = len(a)
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(n))
                       for j in range(n)) for i in range(n))

def matrix_powers(a, m):
    n = len(a)
    powers = [tuple(tuple(int(i == j) for j in range(n)) for i in range(n))]
    for _ in range(m):
        powers.append(mul(powers[-1], a))
    return powers

def permutations_of_order(r):
    yield from ((0, *tail) for tail in permutations(range(1, r)))

def cycle_count(order):
    r = len(order)
    connection = {order[(i + 1) % r]: (order[i] + 1) % r for i in range(r)}
    seen = set()
    count = 0
    for i in range(r):
        if i not in seen:
            count += 1
            while i not in seen:
                seen.add(i)
                i = connection[i]
    return count

def count_polynomial(r):
    counts = Counter(cycle_count(order) for order in permutations_of_order(r))
    for n in (1,2,3,5,11,r+1):
        expected = prod(n+j for j in range(r+1))-prod(n-j for j in range(r+1))
        assert r*(r+1)*sum(a*n**c for c,a in counts.items()) == expected
    assert all((r-c)%2==0 for c in counts)
    return dict(r=r, cycles=dict(sorted(counts.items())))

def check_paths(u, scale, ell, r, m):
    n = len(u)
    assert mul(u, tuple(zip(*u))) == tuple(
        tuple(scale**2*int(i==j) for j in range(n)) for i in range(n))
    short = m//r-ell
    assert short>=1
    gaps = [short + m%r] + [short]*(r-1)
    starts = [sum(ell+g for g in gaps[:i]) for i in range(r)]
    groups = defaultdict(int)
    root_groups = defaultdict(int)
    words = []
    for x in product(range(n), repeat=m):
        ax = prod(u[x[(j+1)%m]][x[j]] for j in range(m))
        corridors = tuple(x[i:i+ell+1] for i in starts)
        groups[corridors] += ax
        root_groups[corridors[0]] += ax
        words.append((x,ax))
    bp = matrix_powers(tuple(tuple(v*v for v in row) for row in u),m)
    up = matrix_powers(u,m)
    root_mass = sum(a*a for a in root_groups.values())
    assert root_mass == sum(bp[ell][i][j]*up[m-ell][j][i]**2
                            for i in range(n) for j in range(n))
    marked_mass = distinct_mass = 0
    for order in permutations_of_order(r):
        successor = {i: order[(j+1)%r] for j,i in enumerate(order)}
        actual = sum(a*groups.get(tuple(x[i] for i in order),0) for x,a in groups.items())
        contracted = 0
        for a in product(range(n),repeat=r):
            contracted += prod(sum(bp[ell][b][a[i]]
                                   *up[gaps[i]][a[(i+1)%r]][b]
                                   *up[gaps[i]][a[successor[i]]][b]
                                   for b in range(n)) for i in range(r))
        assert actual == contracted
        marked_mass += actual
        distinct_mass += sum(ax*groups.get(tuple(x[i] for i in order),0)
                             for x,ax in groups.items() if len(set(x))==r)
    orbit_groups = defaultdict(int)
    orbit_counts = {}
    for x,a in groups.items():
        key = (x[0], tuple(sorted(x[1:])))
        orbit_groups[key] += a
        orbit_counts[key] = prod(prod(range(1,k+1)) for k in Counter(x[1:]).values())
    unmarked_mass = sum(a*a for a in orbit_groups.values())
    assert marked_mass == sum(a*a*orbit_counts[x] for x,a in orbit_groups.items())
    assert distinct_mass <= unmarked_mass <= marked_mass
    # Exact inclusion-exclusion for maximal common runs in a fixed alignment.
    direct, mobius = 0,0
    for x,ax in words:
        for y,ay in words:
            same = tuple(a==b for a,b in zip(x,y))
            if all(same):
                direct += ax*ay
                mobius += ax*ay
                continue
            hit = any(all(same[(i+j)%m] for j in range(ell+1)) for i in range(m))
            starts_count = sum(not same[(i-1)%m] and all(
                same[(i+j)%m] for j in range(ell+1)) for i in range(m))
            direct += ax*ay*hit
            mobius += ax*ay*(1-(1-1)**starts_count)
    assert direct == mobius
    return dict(N=n,m=m,ell=ell,r=r,denominator=scale**(2*m),root=root_mass,
                marked=marked_mass,unmarked=unmarked_mass,distinct=distinct_mass,
                common_run=direct,comparisons=len(words)**2)

def pell_checks():
    h, v = [1], [0]
    for _ in range(71):
        h.append(h[-1]+2*v[-1])
        v.append(h[-2]+v[-1])
    rows = []
    for k in (3,5,7,11,13,17,23,31,41,53,71):
        n = h[k]
        assert n%2==1
        assert (h[k]**2+2*v[k]**2-1)%n == (4*h[k]*v[k])%n == 0
        for j in range(1,k):
            diagonal = h[j]**2+2*v[j]**2
            assert gcd(4*h[j]*v[j],n)==1 and gcd(2*(1-diagonal),n)==1
        rows.append(dict(k=k,N=str(n),powers_checked=k-1))
    return rows

def main():
    output = dict(polynomials=[count_polynomial(r) for r in range(1,10)],
                  paths=[check_paths(((3,-4),(4,3)),5,1,3,7),
                         check_paths(((3,-4),(4,3)),5,1,4,9),
                         check_paths(((1,2,2),(2,1,-2),(2,-2,1)),3,1,3,6)],
                  pell=pell_checks())
    if '--verify' in sys.argv:
        expected = json.loads((Path(__file__).resolve().parent/'data/check.json').read_text())
        assert json.loads(json.dumps(output)) == expected
        print("Exact checks passed.")
    else:
        print(json.dumps(output,indent=2))
if __name__ == "__main__":
    main()
