#!/usr/bin/env python3
"""Wave 46, task 7, step 8: inspect V_81(sigma), V_512(sigma) explicitly.

Take the first non-dihedral pair at 81, sample two sigmas, print the
V-sets and test whether they are identical across sigma choices
(invariance) and what structure the vectors have (periods).
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

def period(y):
    for p in range(1, 25):
        if all(y[(i + p) % 24] == y[i] for i in range(24)):
            return p
    return 24

K81 = kernel_small(81)
K512 = kernel_small(512)
S81 = set(K81)
S512 = set(K512)
by_mult = {}
for y in K81:
    by_mult.setdefault(tuple(sorted(y)), []).append(y)
pair = None
for ys in by_mult.values():
    for ii in range(len(ys)):
        for jj in range(ii + 1, len(ys)):
            if not is_dihedral_pair(ys[ii], ys[jj]):
                pair = (ys[ii], ys[jj])
                break
        if pair:
            break
    if pair:
        break
y, yp = pair
print(f"pair y={y}")
print(f"     yp={yp}")
for seed in [1, 2]:
    sigma = sample_sigma(y, yp, seed)
    V81 = [v for v in K81 if compose(v, sigma) in S81]
    V512 = [v for v in K512 if compose(v, sigma) in S512]
    print(f"seed {seed}: sigma={sigma}")
    print(f"  |V81|={len(V81)} periods: {[period(v) for v in V81]}")
    print(f"  |V512|={len(V512)} periods: {[period(v) for v in V512]}")
    for v in V81:
        print(f"    V81 vec: {v}")
    for v in V512:
        print(f"    V512 vec: {v}")
