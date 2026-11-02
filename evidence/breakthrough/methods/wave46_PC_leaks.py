#!/usr/bin/env python3
"""Wave 46, task 7, step 11: triple Pi analysis for leaking sigmas.

For each non-dihedral 512-pair (and 81-pair) sigma with V nontrivial
outside (81, 512), check ALL combinations (v25, v81, v512) in the
V-sets: if Pi_25 ∩ Pi_81 ∩ Pi_512 = empty for some combination, that
combination is an exact full-PC counterexample (mate = base o sigma).
Otherwise the leaks are harmless (49 is always full, 121/289/1153
never leak).
"""
import random
from collections import Counter

D4 = []
for b in range(4):
    D4.append(tuple((r + b) % 4 for r in range(4)))
    D4.append(tuple((-r + b) % 4 for r in range(4)))
D4 = sorted(set(D4))

def name(pi):
    if all(pi[r] == (r + pi[0]) % 4 for r in range(4)):
        return f"s{pi[0]}"
    return f"f{pi[0] % 4}"

def kernel_small(q):
    out = []
    for y0 in range(q):
        for y1 in range(q):
            y = [0] * 26
            y[0], y[1] = y0, y1
            for n in range(24):
                y[n + 2] = (6 * y[n + 1] - y[n]) % q
            if y[24] == y0 and y[25] == y1:
                out.append(tuple(y[:24]))
    return out

def compose(y, sigma):
    return tuple(y[sigma[i]] for i in range(24))

def prof(y):
    return tuple(tuple(sorted(y[i] for i in range(24) if i % 4 == r))
                  for r in range(4))

def pi_set(p, pp):
    return frozenset(name(pi) for pi in D4
                     if all(pp[r] == p[pi[r]] for r in range(4)))

D24 = []
for k in range(24):
    D24.append(tuple((i + k) % 24 for i in range(24)))
    D24.append(tuple((-i + k) % 24 for i in range(24)))

def is_dihedral_pair(y, yp):
    return any(compose(y, d) == yp for d in D24)

def sample_sigma(y, yp, seed):
    rng = random.Random(seed)
    valpos_y = {}
    for j, v in enumerate(y):
        valpos_y.setdefault(v, []).append(j)
    idxs_by_val = {}
    for i, v in enumerate(yp):
        idxs_by_val.setdefault(v, []).append(i)
    sigma = [0] * 24
    for v, idxs in idxs_by_val.items():
        js = valpos_y[v][:]
        rng.shuffle(js)
        for i, j in zip(idxs, js):
            sigma[i] = j
    return tuple(sigma)

def trace_seq(a, b, p):
    s = []
    ca, cb = a, b
    for _ in range(24):
        s.append((2 * ca) % p)
        ca, cb = (3 * ca + 4 * cb) % p, (2 * ca + 3 * cb) % p
    return tuple(s)

def V_1153_dim(sigma):
    p = 1153
    s1 = trace_seq(1, 0, p)
    s2 = trace_seq(0, 1, p)
    eqs = []
    for n in range(24):
        ca = (s1[sigma[(n + 2) % 24]] - 6 * s1[sigma[(n + 1) % 24]]
              + s1[sigma[n]]) % p
        cb = (s2[sigma[(n + 2) % 24]] - 6 * s2[sigma[(n + 1) % 24]]
              + s2[sigma[n]]) % p
        if ca or cb:
            eqs.append((ca, cb))
    if not eqs:
        return 2
    ca1, cb1 = eqs[0]
    for (ca, cb) in eqs[1:]:
        if (ca * cb1 - cb * ca1) % p != 0:
            return 0
    return 1

K = {q: kernel_small(q) for q in [25, 49, 81, 121, 289, 512]}
Kset = {q: set(K[q]) for q in K}
P = {q: {y: prof(y) for y in K[q]} for q in K}

for q0 in [81, 512]:
    by_mult = {}
    for y in K[q0]:
        by_mult.setdefault(tuple(sorted(y)), []).append(y)
    npairs = 0
    leaks = 0
    for ys in by_mult.values():
        for ii in range(len(ys)):
            for jj in range(ii + 1, len(ys)):
                if is_dihedral_pair(ys[ii], ys[jj]):
                    continue
                npairs += 1
                for trial in range(3):
                    sigma = sample_sigma(ys[ii], ys[jj],
                                         1000 + 10 * npairs + trial)
                    Vs = {q: [v for v in K[q]
                              if compose(v, sigma) in Kset[q]]
                          for q in [25, 49, 81, 121, 289, 512]}
                    d1153 = V_1153_dim(sigma)
                    if not (any(len(Vs[q]) > 1
                                 for q in [25, 49, 121, 289])
                            or d1153 > 0):
                        continue
                    leaks += 1
                    print(f"LEAK q0={q0} pair#{npairs} trial{trial}: "
                          f"|V|={ {q: len(Vs[q]) for q in Vs} } "
                          f"dim1153={d1153}")
                    # triple Pi analysis over (25, 81, 512)
                    pis = {}
                    for q in [25, 81, 512]:
                        s = Counter()
                        for v in Vs[q]:
                            s[pi_set(P[q][v], P[q][compose(v, sigma)])] += 1
                        pis[q] = s
                    print(f"  Pi25 sets: {dict(pis[25])}")
                    print(f"  Pi81 sets: {dict(pis[81])}")
                    print(f"  Pi512 distinct: {len(pis[512])} sets")
                    bad = 0
                    for a, na in pis[25].items():
                        for b, nb in pis[81].items():
                            for c, nc in pis[512].items():
                                if not (a & b & c):
                                    bad += na * nb * nc
                    print(f"  triple-empty combinations: {bad}")
                    if bad:
                        # print one explicit counterexample
                        for v25 in Vs[25]:
                            p25 = pi_set(P[25][v25],
                                         P[25][compose(v25, sigma)])
                            for v81 in Vs[81]:
                                p81 = pi_set(P[81][v81],
                                             P[81][compose(v81, sigma)])
                                for v512 in Vs[512]:
                                    p512 = pi_set(
                                        P[512][v512],
                                        P[512][compose(v512, sigma)])
                                    if not (p25 & p81 & p512):
                                        print("  COUNTEREXAMPLE:")
                                        print(f"    sigma={sigma}")
                                        print(f"    v25={v25} Pi={sorted(p25)}")
                                        print(f"    v81={v81} Pi={sorted(p81)}")
                                        print(f"    v512={v512} Pi={sorted(p512)}")
                                        raise SystemExit
    print(f"q0={q0}: pairs={npairs} leaks={leaks} (triple analysis done)")
