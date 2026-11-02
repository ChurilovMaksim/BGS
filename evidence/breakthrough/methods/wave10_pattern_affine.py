"""Wave 10, task 2, experiment B: refined tau claim.
For P in {4,8,16}, q=2^a as before, enumerate Fix_P mod q, group by sorted
multiset. For each ordered pair (p,p') in a group, check:
  - exists dihedral delta (j -> +-j+b) with p' = p o delta;
  - exists affine tau (j -> a*j+b, a odd) with p' = p o tau.
Report per P: pairs total, dihedral-fail pairs, affine-fail pairs, and
examples of affine-fail pairs (with their class sums).
"""
import numpy as np
from collections import defaultdict

def fix_mod_q(P, q):
    vecs = []
    y1_all = np.arange(q, dtype=np.int64)
    for y0 in range(q):
        a = np.full(q, y0, dtype=np.int64)
        b = y1_all.copy()
        seq = [a.copy(), b.copy()]
        for _ in range(P):
            c = (6*b - a) % q
            a, b = b, c
            seq.append(b.copy())
        ok = (seq[P] == y0) & (seq[P+1] == y1_all)
        idx = np.where(ok)[0]
        for j in idx:
            vecs.append(tuple(int(seq[k][j]) for k in range(P)))
    return vecs

def class_sums(p, P):
    Y = [0]*4
    for j, val in enumerate(p):
        Y[j % 4] += val
    return tuple(Y)

for P in [4, 8, 16]:
    a = 2*(P.bit_length()-1) + 3
    q = 2**a
    vecs = fix_mod_q(P, q)
    groups = defaultdict(list)
    for v in vecs:
        groups[tuple(sorted(v))].append(v)
    total_pairs = 0
    dih_fail = 0
    aff_fail = 0
    aff_examples = []
    # precompute dihedral and affine maps as index tuples
    dih = []
    for b in range(P):
        dih.append(tuple((j+b) % P for j in range(P)))
        dih.append(tuple((-j+b) % P for j in range(P)))
    aff = []
    for aa in range(1, P, 2):
        for b in range(P):
            aff.append(tuple((aa*j+b) % P for j in range(P)))
    def exists(p, pp, maps):
        # p' = p o tau means pp[j] = p[tau[j]]
        for tau in maps:
            if all(pp[j] == p[tau[j]] for j in range(P)):
                return True
        return False
    for ms, vs in groups.items():
        for p in vs:
            for pp in vs:
                if p == pp:
                    continue
                total_pairs += 1
                if not exists(p, pp, dih):
                    dih_fail += 1
                    if not exists(p, pp, aff):
                        aff_fail += 1
                        if len(aff_examples) < 5:
                            aff_examples.append((p, pp, class_sums(p, P), class_sums(pp, P)))
    print(f"P={P} q={q} groups={len(groups)} ordered distinct pairs={total_pairs} dihedral-fail={dih_fail} affine-fail={aff_fail}", flush=True)
    for p, pp, Y, Yp in aff_examples:
        print(f"  AFFINE FAIL p={p} pp={pp} Y={Y} Yp={Yp}")
