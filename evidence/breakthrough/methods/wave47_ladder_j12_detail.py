import numpy as np

# j = 12 detail: class anatomy of first 3 valid points.
m, p = 4096, 4096
Q = 8*m*m
step0 = Q//(8*p)
mod = 8*p
rng = np.random.default_rng(12)
t = rng.choice(np.arange(1, mod, 2), size=64)
U0 = rng.integers(0, mod//16, size=64)
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
good = ((snap[p] == y0) & (snap[p+1] == y1)
        & ~((snap[p//2] == y0) & (snap[p//2+1] == y1))
        & ((snap[p//2] - y0) % Q == Q//2) & ((snap[p//2+1] - y1) % Q == 0))
W = W[:, good]
q, pj = p//8, p//16
mu = Q//128
E128 = (((W[8:8+pj] - W[0:pj]) % Q) // mu) % 128
eps = ((W[q:2*q] - W[0:q]) % Q)//(Q//2)
phi = (((W[pj:2*pj] - W[0:pj]) % Q)//(Q//4)) % 4
v = W[0:q] % (Q//2)
tt = W[0:q] // (Q//2)
shown = 0
for idx in range(W.shape[1]):
    if shown >= 3:
        break
    reps = [j for j in range(pj) if eps[j, idx] == 0 and phi[j, idx] == 0]
    if len(reps) != 64 or any(reps[i+1]-reps[i] != 4 for i in range(63)):
        continue
    Ej = E128[:, idx]
    d = (int(Ej[reps[1]]) - int(Ej[reps[0]])) % 128
    dE = (d//4) % 32
    dE8 = dE % 8
    S = [(int(Ej[j]) + 4*(dE % 16)) % 64 for j in reps]
    wit_ords = [i for i, s in enumerate(S) if s == 0]
    conds = [c for c in range(8) if (int(Ej[reps[c]]) + 12*dE8) % 32 == 0]
    print('--- point', idx, 'delta_E mod32 =', dE, 'wit ordinals =', wit_ords,
          'cond32 chain residues =', conds)
    classes = {}
    for j in reps:
        classes.setdefault(int(v[j, idx]), []).append(j)
    for cval, js in classes.items():
        ords = [reps.index(j) for j in js]
        contrib = sum(2*(1-2*int(tt[j, idx])) for j in js)
        tag = ''
        if any(o in wit_ords for o in ords):
            tag += ' WITNESS'
        if len(ords) == 8 and all(ords[a+1]-ords[a] == 8 for a in range(7)) \
                and ords[0] % 8 in conds:
            tag += ' COND32'
        print('  class size=%d ords=%s t=%s contrib=%d%s' % (
            len(js), ords, [int(tt[j, idx]) for j in js], contrib, tag))
    shown += 1
