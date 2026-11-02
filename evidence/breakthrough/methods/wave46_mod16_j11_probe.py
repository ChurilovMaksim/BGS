import numpy as np
from collections import Counter

# j = 11: m = p = 2048. Probe class geometry on sampled points.
m, p = 2048, 2048
Q = 8*m*m
step0 = Q//(8*p)
mod = 8*p
rng = np.random.default_rng(11)
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
mu = Q//64  # Q/2^{j-5}, j = 11
diff_d = (W[8:8+pj] - W[0:pj]) % Q
print('D_nondiv:', int(((diff_d % mu) != 0).sum()))
E64 = (diff_d // mu) % 64
eps = ((W[q:2*q] - W[0:q]) % Q)//(Q//2)
phi = (((W[pj:2*pj] - W[0:pj]) % Q)//(Q//4)) % 4
v = W[0:q] % (Q//2)
tt = W[0:q] // (Q//2)
stats = Counter()
for idx in range(W.shape[1]):
    reps = [j for j in range(pj) if eps[j, idx] == 0 and phi[j, idx] == 0]
    stats['reps_%d' % len(reps)] += 1
    if len(reps) != 32:
        continue
    if any(reps[i+1]-reps[i] != 4 for i in range(31)):
        stats['spacing_bad'] += 1
        continue
    Ej = E64[:, idx]
    # AP check along reps: diffs constant mod 64?
    diffs = [(int(Ej[reps[i+1]]) - int(Ej[reps[i]])) % 64 for i in range(31)]
    if len(set(diffs)) != 1:
        stats['ap_bad'] += 1
        continue
    d = diffs[0]
    if d % 4 != 0:
        stats['diff_non4'] += 1
        continue
    dE = (d//4) % 16  # delta_E mod 16 from rep diffs
    if dE % 2 == 0:
        stats['delta_even'] += 1
    if any(int(Ej[j]) % 4 != 0 for j in reps):
        stats['E_non0mod4'] += 1
    # full-k AP check: E_{j+1}-E_j constant over all j < pj?
    dd = [(int(Ej[j+1]) - int(Ej[j])) % 64 for j in range(pj-1)]
    if len(set(dd)) != 1:
        stats['full_ap_bad'] += 1
    # witness reps: S = E + 4*delta_E == 0 mod 32 (delta mod 8 suffices)
    dE8 = dE % 8
    S = [(int(Ej[j]) + 4*dE8) % 32 for j in reps]
    wit = [j for j, s in zip(reps, S) if s == 0]
    stats['wit_%d' % len(wit)] += 1
    # sharing reps: S == 0 mod 16
    stats['share_%d' % sum(1 for s in S if s % 16 == 0)] += 1
    classes = {}
    for j in reps:
        classes.setdefault(int(v[j, idx]), []).append(j)
    sizes = tuple(sorted(len(c) for c in classes.values()))
    stats['sizes_' + str(sizes)] += 1
    contribs = tuple(sorted(sum(2*(1-2*int(tt[j, idx])) for j in js) for js in classes.values()))
    stats['contribs_' + str(contribs)] += 1
    # is there a nonzero class? and does a witness rep sit in one?
    witset = set(wit)
    stats['nonzero_class' if any(c != 0 for c in contribs) else 'all_zero'] += 1
    for c, js in classes.items():
        contrib = sum(2*(1-2*int(tt[j, idx])) for j in js)
        if contrib != 0 and witset & set(js):
            stats['witness_in_nonzero'] += 1
            break
for k in sorted(stats):
    print(k, stats[k])
# detailed print for first 3 good points
shown = 0
for idx in range(W.shape[1]):
    if shown >= 3:
        break
    reps = [j for j in range(pj) if eps[j, idx] == 0 and phi[j, idx] == 0]
    if len(reps) != 32 or any(reps[i+1]-reps[i] != 4 for i in range(31)):
        continue
    Ej = E64[:, idx]
    d = (int(Ej[reps[1]]) - int(Ej[reps[0]])) % 64
    dE8 = (d//4) % 8
    print('--- point', idx, 'reps0=', reps[0], 'delta_E mod8=', dE8)
    print('  E64 along reps:', [int(Ej[j]) for j in reps])
    print('  S mod32 along reps:', [(int(Ej[j]) + 4*dE8) % 32 for j in reps])
    classes = {}
    for j in reps:
        classes.setdefault(int(v[j, idx]), []).append(j)
    for c, js in classes.items():
        print('  class members=%s E64=%s t=%s contrib=%d' % (
            js, [int(Ej[j]) for j in js], [int(tt[j, idx]) for j in js],
            sum(2*(1-2*int(tt[j, idx])) for j in js)))
    shown += 1
