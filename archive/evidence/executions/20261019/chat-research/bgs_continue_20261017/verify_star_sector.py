#!/usr/bin/env python3
"""Exact finite controls of rare_star_heisenberg.md; not an asymptotic proof."""
from collections import Counter
from fractions import Fraction as F
from itertools import product
from math import factorial, comb, prod, lgamma, log
from pathlib import Path
import json
import platform
import sys


def tables(n, m):
    counts = Counter()
    for word in product(range(n), repeat=m):
        edges = [0] * (n*n)
        for i, a in enumerate(word):
            edges[n*a + word[(i+1) % m]] += 1
        counts[tuple(edges)] += 1
    assert sum(counts.values()) == n**m
    return counts


def gaussian_formula(n, m):
    rising = prod(n+j for j in range(m+1))
    falling = prod(n-j for j in range(m+1)) if m < n else 0
    assert (rising-falling) % (m+1) == 0
    return (rising-falling)//(m+1)


def is_star(n, nu, k, s):
    for a in range(n):
        leaves = [b for b in range(n) if b != a and nu[n*a+b] == s]
        if len(leaves) != k:
            continue
        expected = [0]*(n*n)
        for b in leaves:
            expected[n*a+b] = expected[n*b+a] = s
        if tuple(expected) == nu:
            return True
    return False


def verify(n, m, star=None):
    counts = tables(n, m)
    h = sum(c*c*prod(factorial(v) for v in nu) for nu,c in counts.items())
    assert h == gaussian_formula(n, m), (n,m,h)
    record = {'N':n,'m':m,'words':n**m,'tables':len(counts),'h':str(h)}
    if star:
        k,s = star
        selected = [(nu,c) for nu,c in counts.items() if is_star(n,nu,k,s)]
        expected_c = 2*factorial(s*k)//factorial(s)**k
        assert len(selected) == n*comb(n-1,k)
        assert all(c == expected_c for nu,c in selected)
        mass = sum(c*c*prod(factorial(v) for v in nu) for nu,c in selected)
        assert mass == 4*n*comb(n-1,k)*factorial(s*k)**2
        assert all(sum(v>=2 for v in nu) == 2*k for nu,c in selected)
        assert all(max(nu) == s for nu,c in selected)
        record.update(star_tables=len(selected), words_per_star=expected_c,
                      unnormalized_star_mass=str(mass), multiplicity=s)
    return record


records = []
for n in (2,3,4):
    for m in range(1,9):
        records.append(verify(n,m,(2,2) if n>=3 and m==8 else None))
records.append(verify(3,12,(2,3)))

# The excluded k=1 case really double-counts the hub.
n,s,k = 3,2,1
actual_two_cycle_tables = comb(n,2)
assert n*comb(n-1,k) == 2*actual_two_cycle_tables

# Circular laws are specified by the exact law of R=|xi|^2.
law32 = [(F(0),F(31,32)),(F(32),F(1,32))]
law4match = [(F(254,255),F(65025,65026)),(F(256),F(1,65026))]
def moments(law, degree):
    return [sum(p*r**j for r,p in law) for j in range(degree+1)]
mu32 = moments(law32,3)
mu = moments(law4match,4)
assert mu32[:3] == [1,1,32]
assert mu[:4] == [1,1,2,F(66044,255)]
q3=mu[3]/6
assert q3*q3*5**5 > 12**6  # exact sign of the positive alpha=5 exponent
assert 3**9 > 2**12        # exact sign of the alpha=3, kappa=32 exponent

# Exact finite ratio lower bounds; logarithms are only descriptive output.
rates=[]
for n in (12,24,60,120,300,600):
    for s,alpha,q in ((2,3,F(16)),(3,5,q3)):
        k=(alpha*n)//(2*s)
        m=2*s*k
        lower=F(4*n*comb(n-1,k)*factorial(s*k)**2,
                gaussian_formula(n,m))*q**(2*k)
        log_ratio=log(lower.numerator)-log(lower.denominator)
        rates.append({'N':n,'m':m,'s':s,'log_ratio_lower_per_N':log_ratio/n})

output={
 'status':'passed','arithmetic':'exact integers and fractions; floats only rate illustration',
 'python':platform.python_version(),
 'finite_enumeration':records,
 'total_words_enumerated':sum(r['words'] for r in records),
 'excluded_k1_negative_control':'passed: naive hub count is twice the table count',
 'radial_moments_32':[str(x) for x in mu32],
 'radial_moments_4matched':[str(x) for x in mu],
 'exact_sign_tests':{'kappa32_alpha3':True,'fourth_matched_alpha5':True},
 'finite_ratio_bounds':rates,
 'non_claims':['No exhaustive asymptotic check','No unitary/BGS counterexample',
               'No full tilted-Wick free-energy formula']
}
Path(sys.argv[1]).write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({'status':'passed','cases':len(records),
                  'words':output['total_words_enumerated'],
                  'exact_sign_tests':output['exact_sign_tests']}))
