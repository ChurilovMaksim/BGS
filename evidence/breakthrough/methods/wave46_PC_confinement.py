#!/usr/bin/env python3
"""Wave 46, task 7, step 10: confinement sweep.

For EVERY non-dihedral pair at 81 and at 512, sample one sigma and
compute V_q(sigma) at 25, 49, 121, 289 and dim_1153. If all are trivial
(V = {0} / dim 0), then no sigma realizing a non-dihedral pair can
carry a nonzero component outside (81, 512): non-dihedral pairs are
confined to the (81, 512) subsystem (whose compatibility is settled
by the exhaustive joint search).
"""
import random

D24 = []
for k in range(24):
    D24.append(tuple((i + k) % 24 for i in range(24)))
    D24.append(tuple((-i + k) % 24 for i in range(24)))

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

K = {q: kernel_small(q) for q in [25, 49, 121, 289]}
Kset = {q: set(K[q]) for q in K}
for q0 in [81, 512]:
    K0 = kernel_small(q0)
    by_mult = {}
    for y in K0:
        by_mult.setdefault(tuple(sorted(y)), []).append(y)
    npairs = 0
    bad = 0
    for ys in by_mult.values():
        for ii in range(len(ys)):
            for jj in range(ii + 1, len(ys)):
                if is_dihedral_pair(ys[ii], ys[jj]):
                    continue
                npairs += 1
                for trial in range(3):
                    sigma = sample_sigma(ys[ii], ys[jj],
                                         1000 + 10 * npairs + trial)
                    Vs = {q: sum(1 for v in K[q]
                                 if compose(v, sigma) in Kset[q])
                          for q in [25, 49, 121, 289]}
                    d1153 = V_1153_dim(sigma)
                    if (any(v > 1 for v in Vs.values()) or d1153 > 0):
                        bad += 1
                        print(f"  LEAK q0={q0} pair#{npairs} trial{trial}: "
                              f"|V|={Vs} dim1153={d1153}")
    print(f"q0={q0}: non-dihedral pairs={npairs}, leaks={bad}")
