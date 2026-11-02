"""Wave 10, task 2, experiment A: strong pattern-dihedral lemma test.
For P in {4,8,16}, q=2^a with a=2*v2(P)+3, enumerate Fix_P mod q
(recurrence sequences of length P with M^P = I mod q), group by sorted
multiset, and check:
  (i) each group is a single dihedral orbit of patterns (strong claim);
  (ii) each group's pattern class sums (over j mod 4) lie in a single
       D4 orbit (Lemma Y mod q for the pattern itself, weaker claim).
Dihedral action on patterns: (p o delta)_j = p_{delta(j)},
delta(j) = j+b or -j+b mod P.
"""
import numpy as np
from collections import defaultdict
import sys

def fix_mod_q(P, q):
    # vectorised seed scan: y0 loop, y1 array
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
        # seq[k] = y_k for k=0..P+1 ; need seq[P]==y0 and seq[P+1]==y1
        ok = (seq[P] == y0) & (seq[P+1] == y1_all)
        idx = np.where(ok)[0]
        for j in idx:
            vecs.append(tuple(int(seq[k][j]) for k in range(P)))
    return vecs

def dihedral_orbit(p, P):
    out = set()
    for b in range(P):
        out.add(tuple(p[(j+b) % P] for j in range(P)))
        out.add(tuple(p[(-j+b) % P] for j in range(P)))
    return out

def d4_orbit(v):
    out = set()
    for b in range(4):
        out.add(tuple(v[(i+b) % 4] for i in range(4)))
        out.add(tuple(v[(-i+b) % 4] for i in range(4)))
    return out

def class_sums(p, P):
    Y = [0]*4
    for j, val in enumerate(p):
        Y[j % 4] += val
    return tuple(Y)

for P in [4, 8, 16]:
    a = 2*(P.bit_length()-1) + 3  # v2(P) for power of 2
    # P=4: v2=2 -> a=7; P=8: v2=3 -> a=9; P=16: v2=4 -> a=11
    q = 2**a
    vecs = fix_mod_q(P, q)
    print(f"P={P} q={q} |Fix|={len(vecs)} (expect {q})", flush=True)
    assert len(vecs) == q
    groups = defaultdict(list)
    for v in vecs:
        groups[tuple(sorted(v))].append(v)
    print(f"  groups (multisets): {len(groups)}", flush=True)
    strong_fail = 0
    weak_fail = 0
    strong_examples = []
    weak_examples = []
    repeat_groups = 0
    for ms, vs in groups.items():
        # (ii) weak: class sums in single D4 orbit?
        Ys = [class_sums(v, P) for v in vs]
        orb = d4_orbit(Ys[0])
        if any(y not in orb for y in Ys):
            weak_fail += 1
            if len(weak_examples) < 3:
                weak_examples.append((ms, Ys))
        # (i) strong: group == dihedral orbit of first element?
        orb_p = dihedral_orbit(vs[0], P)
        if set(vs) != orb_p:
            strong_fail += 1
            if len(strong_examples) < 3:
                strong_examples.append((ms, vs, orb_p))
        if len(set(ms)) < P:
            repeat_groups += 1
    print(f"  strong-fail groups: {strong_fail} / {len(groups)}; weak-fail groups: {weak_fail}; repeat-pattern groups: {repeat_groups}", flush=True)
    for ms, vs, orb_p in strong_examples:
        print(f"   STRONG FAIL multiset={ms}")
        print(f"     group size={len(vs)} dihedral orbit size={len(orb_p)}")
        print(f"     group[0]={vs[0]}")
        extra = [v for v in vs if v not in orb_p]
        print(f"     in group not in dihedral orbit (first): {extra[0] if extra else None}")
        print(f"     class sums group: {[class_sums(v,P) for v in vs]}")
    for ms, Ys in weak_examples:
        print(f"   WEAK FAIL multiset={ms} Ys={Ys}")
