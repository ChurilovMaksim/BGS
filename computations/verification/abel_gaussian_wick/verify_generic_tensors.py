#!/usr/bin/env python3
"""Independent exact checks of the Hessian sphere contractions.

These inputs are generic complex tensors symmetric only under exchange of
the two matrix slots. They are deliberately not trace Hessians. The checker
uses integer real/imaginary pairs throughout, not floating point or NumPy.
Finite tests support the written permutation classification; they are not
a proof over all N or a test of BGS.
"""

from itertools import product, permutations
from collections import Counter
from pathlib import Path
import hashlib
import json


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul_conj(x, y):
    return (x[0] * y[0] + x[1] * y[1], x[1] * y[0] - x[0] * y[1])


def norm(values):
    return sum(x*x + y*y for x, y in values)


def check(ok, description):
    if not ok:
        raise RuntimeError(description)


def tensor(n, seed, symmetric=True):
    result = {}
    for a, b, c, d in product(range(n), repeat=4):
        i, j = a*n+b, c*n+d
        if symmetric:
            i, j = sorted((i, j))
        result[a, b, c, d] = ((7*i + 11*j + seed*3 + i*j) % 13 - 6,
                              (5*i - 9*j + seed*7 + i*j*j) % 11 - 5)
    return result


def pairing_value(H, n, sigma):
    pos = (0, 2, 5, 7)
    neg = (1, 3, 4, 6)
    label = [None]*8
    for i, j in enumerate(sigma):
        label[pos[i]] = i
        label[neg[j]] = i
    total = (0, 0)
    for vals in product(range(n), repeat=4):
        a, b, c, d, e, f, g, h = [vals[i] for i in label]
        total = add(total, mul_conj(H[a, b, c, d], H[e, f, g, h]))
    # Count links from an index of the first H to one of the conjugate H.
    cross = 2*sum(j >= 2 for j in sigma[:2])
    return cross, total


def sixth_pairing_value(H, n, sigma):
    # H_abcd conjugate(H_ebgh), positive u=(a,c,h), negative=(d,e,g).
    pos = (0,2,7)
    neg = (3,4,6)
    label = [None]*8
    for i,j in enumerate(sigma):
        label[pos[i]] = i
        label[neg[j]] = i
    label[1] = label[5] = 3
    total = (0,0)
    for vals in product(range(n),repeat=4):
        a,b,c,d,e,f,g,h = [vals[i] for i in label]
        total = add(total,mul_conj(H[a,b,c,d],H[e,f,g,h]))
    return total


def run(n, seed):
    H = tensor(n, seed)
    check(all(H[a,b,c,d] == H[c,d,a,b] for a,b,c,d in H), 'pair symmetry')
    check(any(H[a,b,c,d] != H[c,b,a,d] for a,b,c,d in H), 'not upper symmetric')
    check(any(H[a,b,c,d] != H[a,d,c,b] for a,b,c,d in H), 'not lower symmetric')
    T, S, A, BH = {}, {}, (0,0), (0,0)
    for c, d in product(range(n), repeat=2):
        T[c,d] = (0,0)
        S[c,d] = (0,0)
        for a in range(n):
            T[c,d] = add(T[c,d], H[a,a,c,d])
            S[c,d] = add(S[c,d], H[a,c,d,a])
    for a,c in product(range(n), repeat=2):
        A = add(A, H[a,a,c,c])
        BH = add(BH, H[a,c,c,a])
    hnorm = norm(H.values())
    partial = (0,0)
    for a,b,c,d in H:
        partial = add(partial, mul_conj(H[a,b,c,d], H[a,d,c,b]))
    check(partial[1] == 0, 'partial swap is self-adjoint')
    bins = {0:(0,0), 2:(0,0), 4:(0,0)}
    counts = Counter()
    for sigma in permutations(range(4)):
        cross, value = pairing_value(H,n,sigma)
        bins[cross] = add(bins[cross], value)
        counts[cross] += 1
    check(counts == {0:4, 2:16, 4:4}, 'all 24 pairings')
    check(bins[4] == (2*hnorm + 2*partial[0],0), 'exact four-cross identity')
    joint = [add(T[c,d], S[d,c]) for c,d in product(range(n), repeat=2)]
    check(bins[2] == (4*norm(joint),0), 'exact sixteen two-cross identity')
    check(bins[0] == (norm([add(A,BH)]),0), 'exact four zero-cross identity')
    check(bins[4][0] <= 4*hnorm, 'four-cross bound')
    check(bins[2][0] <= 8*(norm(T.values())+norm(S.values())), 'two-cross bound')
    check(bins[0][0] <= 2*norm([A,BH]), 'zero-cross bound')
    sixth = (0,0)
    for sigma in permutations(range(3)):
        sixth = add(sixth,sixth_pairing_value(H,n,sigma))
    check(sixth == (hnorm + partial[0] + norm(joint),0),
          'exact six sixth-moment contractions')
    return {'N':n,'seed':seed,'pairing_counts':dict(counts),
            'norm_squared':hnorm,'partial_swap_inner_product':partial[0],
            'T_norm_squared':norm(T.values()),'S_norm_squared':norm(S.values()),
            'pairing_group_sums':{k:v[0] for k,v in bins.items()},
            'sixth_pairing_sum':sixth[0]}


def main():
    cases = [run(n,seed) for n in range(2,6) for seed in range(3)]
    print(json.dumps({'status':'PASS','arithmetic':'integer real/imaginary pairs',
        'cases':cases,'total_eighth_pairings':24*len(cases),
        'total_sixth_pairings':6*len(cases),
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'boundary':'Finite generic tensors; the written classification supplies the all-N proof.'},indent=2))


if __name__ == '__main__':
    main()
