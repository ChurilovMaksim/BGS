#!/usr/bin/env python3
"""Wave 46, task 7: scan random slice base points for non-dihedral mates.

For base (C, D), enumerate (d, e) in D_24^2 with pair-multiset equality
(wave 12 s3a: every mate arises this way). Report hits, distinct mates,
and non-dihedral mates. Goal: a generic base with non-dihedral mates.
"""
import random

def trace_seq(a, b, p):
    s = []
    ca, cb = a, b
    for _ in range(24):
        s.append((2 * ca) % p)
        ca, cb = (3 * ca + 4 * cb) % p, (2 * ca + 3 * cb) % p
    return tuple(s)

D24 = []
for k in range(24):
    D24.append((0, k))
    D24.append((1, k))

def apply(d, i):
    kind, k = d
    return (i + k) % 24 if kind == 0 else (-i + k) % 24

rng = random.Random(7)
good = 0
for trial in range(60):
    C = (rng.randrange(17), rng.randrange(17))
    D = (rng.randrange(1153), rng.randrange(1153))
    if C == (0, 0) or D == (0, 0):
        continue
    t0 = trace_seq(*C, 17)
    s0 = trace_seq(*D, 1153)
    base_pairs = sorted(zip(t0, s0))
    t_by_d = {d: tuple(t0[apply(d, i)] for i in range(24)) for d in D24}
    s_by_e = {e: tuple(s0[apply(e, i)] for i in range(24)) for e in D24}
    mates = {}
    for d in D24:
        td = t_by_d[d]
        for e in D24:
            se = s_by_e[e]
            if sorted(zip(td, se)) == base_pairs:
                mates.setdefault((td, se), []).append((d, e))
    nondih = 0
    for (td, se) in mates:
        if not any(t_by_d[dp] == td and s_by_e[dp] == se for dp in D24):
            nondih += 1
    # periods of t0, s0 (smallest p>0 with seq o shift_p == seq)
    def period(seq):
        for p in range(1, 25):
            if all(seq[(i + p) % 24] == seq[i] for i in range(24)):
                return p
        return 24
    print(f"base C={C} D={D}: mates={len(mates)} nondih={nondih} "
          f"per_t={period(t0)} per_s={period(s0)}")
    if nondih > 0:
        good += 1
        if good >= 5:
            break
