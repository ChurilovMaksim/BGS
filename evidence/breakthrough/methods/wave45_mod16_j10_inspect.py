import numpy as np

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
for nn in range(1, p+1):
    y_next = (6*y_curr - y_prev) % Q
    y_prev, y_curr = y_curr, y_next
    if nn % 2 == 0 and nn//2 < 256:
        W[nn//2] = y_curr
q, pj = 128, 64
mu = Q//32
eps = ((W[q:2*q] - W[0:q]) % Q)//(Q//2)
phi = (((W[pj:2*pj] - W[0:pj]) % Q)//(Q//4)) % 4
E32 = (((W[8:8+pj] - W[0:pj]) % Q)//mu)  # mod 32
v = W[0:q] % (Q//2)
tt = W[0:q] // (Q//2)
for idx in [0, 1, 2]:
    reps = [j for j in range(pj) if eps[j, idx] == 0 and phi[j, idx] == 0]
    print('point', idx, 't=', t[idx], 'u=', u[idx], 'reps:', reps)
    for j in reps:
        print('  rep j=%2d v=%d E32=%2d (mod16=%2d) t=%d' % (
            j, int(v[j, idx]), int(E32[j, idx]), int(E32[j, idx]) % 16, int(tt[j, idx])))
    classes = {}
    for j in reps:
        classes.setdefault(int(v[j, idx]), []).append(j)
    for c, js in classes.items():
        print('  class v=%d members=%s t=%s contrib=%d' % (
            c, js, [int(tt[j, idx]) for j in js],
            sum(2*(1-2*int(tt[j, idx])) for j in js)))
