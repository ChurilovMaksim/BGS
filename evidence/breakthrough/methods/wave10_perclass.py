"""Wave 10, task 2, experiment D: per-class multiset condition.
For P in {4,8,16}, enumerate Fix_P mod q, group by sorted multiset.
For each ordered pair (p,p') in a group, check whether the 4 per-class
multisets of p' are a D4 permutation of those of p (this is exactly the
condition for a class-permuting matching tau to exist).
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

def per_class(p, P):
    return tuple(tuple(sorted(p[j] for j in range(P) if j % 4 == r)) for r in range(4))

def d4_perms():
    out = []
    for b in range(4):
        out.append(tuple((i+b) % 4 for i in range(4)))
        out.append(tuple((-i+b) % 4 for i in range(4)))
    return list(dict.fromkeys(out))

PIS = d4_perms()
for P in [4, 8, 16]:
    a = 2*(P.bit_length()-1) + 3
    q = 2**a
    vecs = fix_mod_q(P, q)
    groups = defaultdict(list)
    for v in vecs:
        groups[tuple(sorted(v))].append(v)
    pcs = {v: per_class(v, P) for v in vecs}
    total = 0
    fail = 0
    examples = []
    for ms, vs in groups.items():
        for p in vs:
            for pp in vs:
                if p == pp:
                    continue
                total += 1
                cp, cpp = pcs[p], pcs[pp]
                # exists pi in D4 with cpp[r] == cp[pi[r]] for all r
                ok = any(all(cpp[r] == cp[pi[r]] for r in range(4)) for pi in PIS)
                if not ok:
                    fail += 1
                    if len(examples) < 3:
                        examples.append((p, pp, cp, cpp))
    print(f"P={P} q={q} groups={len(groups)} pairs={total} perclass-fail={fail}", flush=True)
    for p, pp, cp, cpp in examples:
        print(f"  FAIL p={p} pp={pp}\n    cp={cp}\n    cpp={cpp}")
