"""Exact small occupation-stabilizer checks and seeded large-N illustrations.

No fit, no use of numerical evidence as proof of a limit.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import permutations, product
from math import exp, factorial, sqrt
from pathlib import Path
from random import Random
import json

from independent_checks import cycle_difference, quadratic_normal_form

ROOT = Path(__file__).resolve().parent


def groups(word):
    result = defaultdict(list)
    for i,label in enumerate(word):
        result[label].append(i)
    return list(result.values())


def inactive_and_triples(h):
    n = len(h)
    inverse = [0]*n
    for i,j in enumerate(h):
        inverse[j] = i
    inactive, triples = [],[]
    for i in range(n):
        j = inverse[i]
        left,right = h[(j-1)%n],h[(j+1)%n]
        unchanged = ((left==(i-1)%n and right==(i+1)%n) or
                     (right==(i-1)%n and left==(i+1)%n))
        triple = all(h[v]==v for v in ((i-1)%n,i,(i+1)%n))
        assert not triple or unchanged
        inactive.append(unchanged)
        triples.append(triple)
    return inactive,triples


def occupation_stabilizers(blocks,n):
    for images in product(*(permutations(block) for block in blocks)):
        h = list(range(n))
        for block,targets in zip(blocks,images):
            for i,j in zip(block,targets):
                h[i] = j
        yield tuple(h)


def direct_case(N,n,rank_cache):
    active, triples, fixed, joint_three = (Fraction(0) for _ in range(4))
    independent_joint = Fraction(0)
    permutations_checked = 0
    for word in product(range(N),repeat=n):
        blocks = groups(word)
        f = 1
        for block in blocks:
            f *= factorial(len(block))
        sums = [0,0,0,0]
        for h in occupation_stabilizers(blocks,n):
            assert all(word[h[i]]==word[i] for i in range(n))
            inactive,ts = inactive_and_triples(h)
            k = n-sum(inactive)
            if h not in rank_cache:
                ranks = [quadratic_normal_form(cycle_difference(h,p),p)[0]
                         for p in (3,5,7)]
                rank_cache[h] = ranks
            assert all(k<=4*r for r in rank_cache[h])
            sums[0] += k
            sums[1] += sum(ts)
            sums[2] += sum(h[i]==i for i in range(n))
            sums[3] += all(h[i]==i for i in (0,1,2))
            permutations_checked += 1
        active += Fraction(sums[0],f)
        triples += Fraction(sums[1],f)
        fixed += Fraction(sums[2],f)
        joint_three += Fraction(sums[3],f)
        totals = Counter(word)
        selected = Counter(word[:3])
        conditional = Fraction(1)
        for label,t in selected.items():
            conditional *= Fraction(factorial(totals[label]-t),factorial(totals[label]))
        independent_joint += conditional
    expected_fixed_fraction = Fraction(N,n)*(1-Fraction(N-1,N)**n)
    assert fixed/(n*N**n) == expected_fixed_fraction
    assert triples/(n*N**n) == joint_three/N**n == independent_joint/N**n
    excess_inactive = 1-active/(n*N**n)-triples/(n*N**n)
    assert excess_inactive >= 0
    return {'N':N,'n':n,'words':N**n,
            'stabilizer_permutations_checked':permutations_checked,
            'mean_active_fraction':str(active/(n*N**n)),
            'mean_fixed_triple_fraction':str(triples/(n*N**n)),
            'mean_fixed_fraction':str(fixed/(n*N**n)),
            'inactive_without_fixed_triple_fraction':str(excess_inactive)}


def illustrate(N,tau,samples,rng):
    n = int(N*tau)
    fractions,exceptions = [],[]
    for _ in range(samples):
        word = [rng.randrange(N) for _ in range(n)]
        h = list(range(n))
        for block in groups(word):
            targets = block[:]
            rng.shuffle(targets)
            for i,j in zip(block,targets):
                h[i] = j
        inactive,triples = inactive_and_triples(h)
        fractions.append(1-sum(inactive)/n)
        exceptions.append((sum(inactive)-sum(triples))/n)
    average = sum(fractions)/samples
    stdev = sqrt(sum((v-average)**2 for v in fractions)/(samples-1))
    q = (1-exp(-tau))/tau
    return {'N':N,'n':n,'tau':tau,'samples':samples,
            'mean_active_fraction':average,'sample_standard_deviation':stdev,
            'proved_limit_active_fraction':1-q**3,
            'mean_inactive_without_fixed_triple':sum(exceptions)/samples,
            'analytic_upper_bound_exception_mean':9/N+2*n/N**3,
            'status':'Seeded illustration only; not an error certificate or proof.'}


def main():
    rank_cache = {}
    exact = [direct_case(N,n,rank_cache) for N in (2,3,4) for n in range(3,7)]
    seed = 20261010
    rng = Random(seed)
    illustrations = [illustrate(N,tau,40,rng)
                     for tau in (0.5,1.0,2.0) for N in (256,1024,4096)]
    result = {'all_passed':True,'exact_cases':exact,'seed':seed,
              'large_N_illustrations':illustrations,
              'scope':'Finite identities checked exactly. The limit and diagonal-rank '
                      'conclusion rely on the proof in occupation_rank_law.md.'}
    (ROOT/'occupation_rank_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'all_passed':True,'exact_cases':len(exact),
          'exact_stabilizer_permutations':sum(c['stabilizer_permutations_checked'] for c in exact),
          'unique_permutations_rank_checked':len(rank_cache),
          'large_N_cases':len(illustrations),'seed':seed}))


if __name__ == '__main__':
    main()
