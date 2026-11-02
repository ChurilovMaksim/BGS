import numpy as np
from collections import Counter

m, p = 1024, 1024
Q = 8*m*m
step0 = Q//(8*p)
rng = np.random.default_rng(7)
t = rng.choice(np.arange(1, 8192, 2), size=4096)
U0 = rng.integers(0, 512, size=4096)
u = (11*t + 16*U0) % 8192
y_prev = (step0*t) % Q
y_curr = (step0*u) % Q
W = np.zeros((256, len(t)), dtype=np.int64)
W[0] = y_curr
snap = {}
for nn in range(1, p+1):
    y_next = (6*y_curr - y_prev) % Q
    y_prev, y_curr = y_curr, y_next
    if nn % 2 == 0 and nn//2 < 256:
        W[nn//2] = y_curr
    if nn+1 in (512, 513, 1024, 1025):
        snap[nn+1] = y_curr.copy()
y0 = (step0*t) % Q
y1 = (step0*u) % Q
per_ok = (snap[1024] == y0) & (snap[1025] == y1)
min_ok = ~((snap[512] == y0) & (snap[513] == y1))
nu_ok = ((snap[512] - y0) % Q == Q//2) & ((snap[513] - y1) % Q == 0)
good = per_ok & min_ok & nu_ok
print('valid:', int(good.sum()), 'of', len(t))
W = W[:, good]
q, pj = 128, 64
mu = Q//32  # Q/2^{10-5}
eps = ((W[q:2*q] - W[0:q]) % Q)//(Q//2)
phi = (((W[pj:2*pj] - W[0:pj]) % Q)//(Q//4)) % 4
D = (((W[8:8+pj] - W[0:pj]) % Q)//mu) % 16
v = W[0:q] % (Q//2)
tt = W[0:q] // (Q//2)
stats = Counter()
for idx in range(W.shape[1]):
    reps = [j for j in range(pj) if eps[j, idx] == 0 and phi[j, idx] == 0]
    stats['reps_%d' % len(reps)] += 1
    if len(reps) != 16:
        continue
    if any(reps[i+1]-reps[i] != 4 for i in range(15)):
        stats['spacing_bad'] += 1
        continue
    classes = {}
    for j in reps:
        classes.setdefault(int(v[j, idx]), []).append(j)
    sizes = tuple(sorted(len(c) for c in classes.values()))
    stats['sizes_' + str(sizes)] += 1
    contribs = tuple(sorted(sum(2*(1-2*int(tt[j, idx])) for j in js) for js in classes.values()))
    stats['contribs_' + str(contribs)] += 1
    for c, js in classes.items():
        dtup = tuple(int(D[j, idx]) for j in js)
        ttv = tuple(int(tt[j, idx]) for j in js)
        stats['class_len%d_D%s_t%s' % (len(js), dtup, ttv)] += 1
for k in sorted(stats):
    if k.startswith('class_len'):
        continue
    print(k, stats[k])
for L in (8, 4):
    print('--- size %d (top 12) ---' % L)
    items = [(k, val) for k, val in stats.items() if k.startswith('class_len%d_' % L)]
    items.sort(key=lambda kv: -kv[1])
    for k, val in items[:12]:
        print(k, val)
