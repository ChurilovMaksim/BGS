import numpy as np
from collections import Counter

# j = 12: m = p = 4096. Probe the ladder prediction on sampled points:
# exactly one step-32 chain of 8, contribution +-16, per point.
m, p = 4096, 4096
Q = 8*m*m
step0 = Q//(8*p)
mod = 8*p
rng = np.random.default_rng(12)
t = rng.choice(np.arange(1, mod, 2), size=4096)
U0 = rng.integers(0, mod//16, size=4096)
u = (11*t + 16*U0) % mod
y_prev = (step0*t) % Q
y_curr = (step0*u) % Q
W = np.zeros((p//4, len(t)), dtype=np.int64)
W[0] = y_curr
snap = {}
for nn in range(1, p+1):
    y_next = (6*y_curr - y_prev) % Q
    y_prev, y_curr = y_curr, y_next
    if nn % 2 == 0 and nn//2 < p//4:
        W[nn//2] = y_curr
    if nn+1 in (p//2, p//2+1, p, p+1):
        snap[nn+1] = y_curr.copy()
y0 = (step0*t) % Q
y1 = (step0*u) % Q
per_ok = (snap[p] == y0) & (snap[p+1] == y1)
min_ok = ~((snap[p//2] == y0) & (snap[p//2+1] == y1))
nu_ok = ((snap[p//2] - y0) % Q == Q//2) & ((snap[p//2+1] - y1) % Q == 0)
good = per_ok & min_ok & nu_ok
print('valid:', int(good.sum()), 'of', len(t))
W = W[:, good]
q, pj = p//8, p//16
mu = Q//128  # Q/2^{j-5}, j = 12
diff_d = (W[8:8+pj] - W[0:pj]) % Q
print('D_nondiv:', int(((diff_d % mu) != 0).sum()))
E128 = (diff_d // mu) % 128
eps = ((W[q:2*q] - W[0:q]) % Q)//(Q//2)
phi = (((W[pj:2*pj] - W[0:pj]) % Q)//(Q//4)) % 4
v = W[0:q] % (Q//2)
tt = W[0:q] // (Q//2)
stats = Counter()
for idx in range(W.shape[1]):
    reps = [j for j in range(pj) if eps[j, idx] == 0 and phi[j, idx] == 0]
    stats['reps_%d' % len(reps)] += 1
    if len(reps) != 64:
        continue
    if any(reps[i+1]-reps[i] != 4 for i in range(63)):
        stats['spacing_bad'] += 1
        continue
    Ej = E128[:, idx]
    diffs = [(int(Ej[reps[i+1]]) - int(Ej[reps[i]])) % 128 for i in range(63)]
    if len(set(diffs)) != 1:
        stats['ap_bad'] += 1
        continue
    d = diffs[0]
    if d % 4 != 0:
        stats['diff_non4'] += 1
        continue
    dE = (d//4) % 32  # delta_E mod 32
    if dE % 2 == 0:
        stats['delta_even'] += 1
    if any(int(Ej[j]) % 4 != 0 for j in reps):
        stats['E_non0mod4'] += 1
    # step-16 witness: S = E + 4*delta_E == 0 mod 64
    dE16 = dE % 16
    S = [(int(Ej[j]) + 4*dE16) % 64 for j in reps]
    stats['wit_%d' % sum(1 for s in S if s == 0)] += 1
    stats['share_%d' % sum(1 for s in S if s % 32 == 0)] += 1
    # step-32 chains: ordinals c mod 8, condition E + 12*delta_E == 0 mod 32
    dE8 = dE % 8
    conds = [c for c in range(8)
             if (int(Ej[reps[c]]) + 12*dE8) % 32 == 0]
    stats['cond32_%d' % len(conds)] += 1
    classes = {}
    for j in reps:
        classes.setdefault(int(v[j, idx]), []).append(j)
    sizes = tuple(sorted(len(c) for c in classes.values()))
    stats['sizes_' + str(sizes)] += 1
    contribs = tuple(sorted(sum(2*(1-2*int(tt[j, idx])) for j in js)
                            for js in classes.values()))
    stats['contribs_' + str(contribs)] += 1
    # chain geometry: each cond chain exactly a class with constant t?
    for c in conds:
        members = [reps[c + 8*a] for a in range(8)]
        vs = set(int(v[j, idx]) for j in members)
        ts = set(int(tt[j, idx]) for j in members)
        cls = classes[int(v[members[0], idx])]
        if len(vs) == 1 and len(ts) == 1 and sorted(cls) == sorted(members):
            stats['chain_exact_class_const_t'] += 1
            stats['chain_contrib_%d' % sum(2*(1-2*int(tt[j, idx]))
                                            for j in members)] += 1
        else:
            stats['chain_BAD'] += 1
    # nonzero classes: exactly the cond chains?
    for js in classes.values():
        contrib = sum(2*(1-2*int(tt[j, idx])) for j in js)
        if contrib == 0:
            continue
        ords = sorted(reps.index(j) for j in js)
        iscond = (len(ords) == 8 and all(ords[a+1]-ords[a] == 8 for a in range(7))
                  and (int(Ej[reps[ords[0]]]) + 12*dE8) % 32 == 0)
        if not iscond:
            stats['nonzero_not_cond32'] += 1
for k in sorted(stats):
    print(k, stats[k])
