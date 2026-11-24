"""Integer checks on rational orthogonal matrices. All sums use one common denominator."""

# Repository-wide fail-closed verification guard.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

from collections import defaultdict
from itertools import product
from math import gcd, prod
import json

def power(a, k):
    n = len(a)
    b = [[int(i == j) for j in range(n)] for i in range(n)]
    for _ in range(k):
        b = [[sum(b[i][j] * a[j][v] for j in range(n))
              for v in range(n)] for i in range(n)]
    return b

def check(u, den, m):
    n = len(u)
    assert all(sum(a*b for a,b in zip(u[i],u[j])) == den**2 * (i == j)
               for i in range(n) for j in range(n))
    words = list(product(range(n), repeat=m))
    def key(x):
        return tuple(sorted(zip(x, x[1:] + x[:1])))
    keys = [key(w) for w in words]
    amps = [prod(u[w[(i+1)%m]][w[i]] for i in range(m)) for w in words]
    z = sum(a*a for a in amps)
    max_l = (m-1)//2
    # For each mismatch pattern use the definition at every possible beginning.
    info = {}
    for mask in range(1 << m):
        allowed = []
        for l in range(max_l+1):
            inner = ((1 << max(0,l-1))-1) << 1
            fixed = mask & ~inner == 0
            count = 0
            for a in range(m):
                free = ((inner << a) | (inner >> (m-a))) & ((1<<m)-1)
                count += mask & ~free == 0
            allowed.append((fixed, count))
        if mask:
            for l in range(2,max_l+1):
                assert allowed[l][1]-allowed[l-1][1] == int(allowed[l][1]>0)
        info[mask] = allowed
    totals = [[0,0,0] for _ in range(1<<m)]
    for i,x in enumerate(words):
        for j,y in enumerate(words):
            mask = sum((a!=b)<<h for h,(a,b) in enumerate(zip(x,y)))
            row = totals[mask]
            val = amps[i]*amps[j]
            row[0] += val
            if keys[i] == keys[j]:
                row[1] += val
                row[2] += 1
    b = [[v*v for v in row] for row in u]
    prev = [z,z]
    report = []
    for l in range(1,max_l+1):
        fixed = [sum(totals[mask][j] for mask in info if info[mask][l][0]) for j in (0,1)]
        union = [sum(totals[mask][j] for mask in info if info[mask][l][1]) for j in (0,1)]
        c, exterior = power(u,l),power(b,m-l)
        assert fixed[0] == sum(c[i][j]**2*exterior[j][i] for i in range(n) for j in range(n))
        assert all(union[j] == z + m*(fixed[j]-prev[j]) for j in (0,1))
        prev = fixed
        report.append(dict(L=l,aligned_total=union[0],aligned_equal_edges=union[1]))
    assert report[-1]['aligned_equal_edges']>z
    return dict(N=n,m=m,denominator=den**(2*m),pairs_compared=len(words)**2,windows=report)

def interval_rank():
    cases=0
    for m in range(3,21):
        for step in range(1,m):
            g=gcd(m,step)
            for k in range(m//2+1,m+1):
                for start in range(m):
                    first=set(range(k))
                    other={(start+i)%m for i in range(k)}
                    # A complete component requires all x-positions in both matchings.
                    complete=sum(all(i in first and i in other for i in range(h,m,g))
                                 for h in range(g))
                    assert complete<=max(0,g-m+k) and 2*complete<=2*k-m
                    cases+=1
    return cases

print(json.dumps(dict(checks=[check([[3,-4],[4,3]],5,9),
                              check([[1,2,2],[2,1,-2],[2,-2,1]],3,7)],
                      interval_rank_cases=interval_rank()),indent=2))
