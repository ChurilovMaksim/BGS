#!/usr/bin/env python3
"""Wave 46, task 7, step 9: on V(sigma) vectors, does sigma act dihedrally?

For the first non-dihedral 81-pair and a sampled sigma, for each
y in V_81(sigma) and V_512(sigma): find all dihedral d with y o sigma =
y o d, and their class maps. If every V-vector is acted on dihedrally,
then pairs built from V(sigma) are dihedral pairs (Pi contains the
class map) -- the mechanism behind compatibility.
"""
import random

D24 = []
for k in range(24):
    D24.append(tuple((i + k) % 24 for i in range(24)))
    D24.append(tuple((-i + k) % 24 for i in range(24)))

def dname(d):
    # d as tuple; recover shift/reflection + k
    if all(d[i] == (i + d[0]) % 24 for i in range(24)):
        return f"shift{d[0]}"
    return f"refl{d[0]}"

def classmap(d):
    # class map on residues mod 4 induced by position map d
    if all(d[i] == (i + d[0]) % 24 for i in range(24)):
        b = d[0] % 4
        return f"s{b}"
    b = d[0] % 4
    return f"f{b}"

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

K81 = kernel_small(81)
K512 = kernel_small(512)
S81, S512 = set(K81), set(K512)
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
sigma = sample_sigma(y, yp, 1)
for q, K, S in [(81, K81, S81), (512, K512, S512)]:
    V = [v for v in K if compose(v, sigma) in S]
    print(f"q={q}: |V|={len(V)}")
    for v in V:
        if all(x == 0 for x in v):
            print("  zero vector: trivial")
            continue
        ds = [d for d in D24 if compose(v, sigma) == compose(v, d)]
        cms = sorted(set(classmap(d) for d in ds))
        print(f"  v={v[:8]}...: sigma acts via {len(ds)} dihedral maps, "
              f"class maps {cms}")
