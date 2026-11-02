#!/usr/bin/env python3
"""Wave 46, task 7, step 2: which Pi sets occur at each component?

Maps named: s_b = shift r -> r+b; f_b = reflection r -> -r+b (mod 4).
Pi_q(y, y') = {pi : prof'[r] == prof[pi(r)] forall r}.
Also samples Pi at 1153^2 via the p*Tr(C alpha^i) parametrization.
"""
from collections import Counter

M = 24

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

def prof(y):
    return tuple(tuple(sorted(y[i] for i in range(24) if i % 4 == r))
                  for r in range(4))

def name(pi):
    # pi as tuple pi[r]
    if all(pi[r] == (r + pi[0]) % 4 for r in range(4)):
        return f"s{pi[0]}"
    # reflection: pi[r] = -r + b
    b = pi[0] % 4
    if all(pi[r] == (-r + b) % 4 for r in range(4)):
        return f"f{b}"
    return str(pi)

D4 = []
for b in range(4):
    D4.append(tuple((r + b) % 4 for r in range(4)))
    D4.append(tuple((-r + b) % 4 for r in range(4)))
D4 = sorted(set(D4))

def pi_set(p, pp):
    return tuple(sorted(name(pi) for pi in D4
                        if all(pp[r] == p[pi[r]] for r in range(4))))

for q in [25, 49, 81, 121, 289, 512]:
    K = kernel_small(q)
    profs = [prof(y) for y in K]
    by_mult = {}
    for idx, y in enumerate(K):
        by_mult.setdefault(tuple(sorted(y)), []).append(idx)
    dist = Counter()
    for idxs in by_mult.values():
        for ii in range(len(idxs)):
            for jj in range(ii + 1, len(idxs)):
                dist[pi_set(profs[idxs[ii]], profs[idxs[jj]])] += 1
    print(f"q={q}: distinct Pi sets: {len(dist)}")
    for ps, c in dist.most_common():
        print(f"   {ps}: {c}")

# ---- 1153^2 sampling ----
import random
p = 1153
random.seed(42)

def seq_1153(C):
    # C = (a, b) in R/p; values p * Tr(C alpha^i) mod p^2, reported as Tr mod p
    a, b = C
    vals = []
    ca, cb = a, b
    for _ in range(24):
        vals.append((2 * ca) % p)
        ca, cb = (3 * ca + 4 * cb) % p, (2 * ca + 3 * cb) % p
    return tuple(vals)

N = 300000
groups = {}
for _ in range(N):
    C = (random.randrange(p), random.randrange(p))
    s = seq_1153(C)
    groups.setdefault(tuple(sorted(s)), []).append(s)
dist = Counter()
npairs = 0
for ss in groups.values():
    if len(ss) < 2:
        continue
    # profs from s (x1153 injective, so Pi identical)
    ps_list = [prof(s) for s in ss]
    for ii in range(len(ss)):
        for jj in range(ii + 1, len(ss)):
            dist[pi_set(ps_list[ii], ps_list[jj])] += 1
            npairs += 1
print(f"1153^2 sample: {N} seqs, {npairs} colliding pairs")
for ps, c in dist.most_common():
    print(f"   {ps}: {c}")
