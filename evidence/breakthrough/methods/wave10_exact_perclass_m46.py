"""Wave 10, task 2, experiment F: exact per-class multisets at m=4,6.
Enumerate Fix_m via CRT over prime-power moduli, group by sorted
multiset (fiber), check per-class multisets are D_t-related
(t=gcd(m,4); m=4: classes singletons, D4; m=6: classes parity, D2=S2).
"""
import numpy as np
import math
from collections import Counter

def run(m, mods):
    D = 1
    for q in mods:
        D *= q
    print(f"=== m={m} mods={mods} D={D}", flush=True)
    def kernel_mod(mod):
        res = []
        for a in range(mod):
            for b in range(mod):
                seq = [a, b]
                for _ in range(m):
                    seq.append((6*seq[-1] - seq[-2]) % mod)
                if seq[m] == a and seq[m+1] == b:
                    res.append(seq[:m])
        return np.array(res, dtype=np.int64)
    kernels = [kernel_mod(q) for q in mods]
    for q, k in zip(mods, kernels):
        print(f"  ker mod {q}: {len(k)}", flush=True)
    def crt_combine(A, mod_a, B, mod_b):
        inv = pow(mod_a, -1, mod_b)
        diff = (B[None, :, :] - A[:, None, :]) % mod_b
        t = (diff * inv) % mod_b
        out = A[:, None, :] + mod_a * t
        return out.reshape(-1, m)
    pts = kernels[0]; cur = mods[0]
    for k, q in zip(kernels[1:], mods[1:]):
        pts = crt_combine(pts, cur, k, q)
        cur *= q
    print(f"  Fix points: {pts.shape} (expect {D})", flush=True)
    assert pts.shape[0] == D
    t = math.gcd(m, 4)
    # per-class multisets: for class r, sorted values at positions r, r+t, ...
    # encode each class multiset as a tuple; canonical = min over D_t perms
    # D_t perms on Z/t: r -> r+b, r -> -r+b
    perms = []
    for b in range(t):
        perms.append(tuple((i+b) % t for i in range(t)))
        perms.append(tuple((-i+b) % t for i in range(t)))
    perms = list(dict.fromkeys(perms))
    # class multisets as arrays: class_vals[r] = sorted tuple per point
    # Represent each class multiset by a string key via sorted values tuple;
    # for canonicalisation, compare tuples lexicographically in numpy by
    # encoding: values < D, class size = m//t, encode as Python ints? Use
    # object arrays in a loop over points is too slow for m=6 (39200 ok actually).
    # 39200 points: pure python loop fine.
    pts_list = pts.tolist()
    canon_list = []
    for y in pts_list:
        classes = []
        for r in range(t):
            classes.append(tuple(sorted(y[i] for i in range(m) if i % t == r)))
        canon = min(tuple(classes[pi[i]] for i in range(t)) for pi in perms)
        canon_list.append(canon)
    sorted_keys = [tuple(sorted(y)) for y in pts_list]
    # group: (fiber, canon) distinct count vs fiber count
    fibers = set(sorted_keys)
    combos = set(zip(sorted_keys, canon_list))
    print(f"  fibers: {len(fibers)}  (fiber,canon) rows: {len(combos)}  extra: {len(combos)-len(fibers)}", flush=True)
    if len(combos) > len(fibers):
        cnt = Counter(f for f, _ in combos)
        bad = [f for f, c in cnt.items() if c > 1][:2]
        for f in bad:
            print(f"  FAIL fiber {f}")
            for y, cn in zip(pts_list, canon_list):
                if tuple(sorted(y)) == f:
                    print(f"    y={y} canon={cn}")

run(4, [128, 9])
run(6, [32, 25, 49])
