"""Wave 10, task 2, experiment E: exact per-class multisets at m=8.
Enumerate Fix_8 via CRT (as in oprime_m8_test.py), group by sorted
multiset (fiber), and check whether the per-class pair multisets
({y_r, y_{r+4}} for r=0..3) of all points in a fiber are D4-related.
If yes for all fibers, exact Lemma Y follows from per-class multisets
(stronger than sums), and Pcarry is moot at m=8 in this stronger form.
"""
import numpy as np
from collections import Counter

m = 8
D = 1331712
MODS = (9, 289, 512)

def kernel_mod(mod):
    res = []
    for a in range(mod):
        for b in range(mod):
            seq = [a, b]
            for _ in range(8):
                seq.append((6*seq[-1] - seq[-2]) % mod)
            if seq[8] == a and seq[9] == b:
                res.append(seq[:8])
    return np.array(res, dtype=np.int64)

kernels = [kernel_mod(mod) for mod in MODS]
for mod, k in zip(MODS, kernels):
    print(f"ker mod {mod}: {len(k)}", flush=True)

def crt_combine(A, mod_a, B, mod_b):
    inv = pow(mod_a, -1, mod_b)
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    out = A[:, None, :] + mod_a * t
    return out.reshape(-1, 8)

pts = crt_combine(kernels[0], 9, kernels[1], 289)
pts = crt_combine(pts, 9*289, kernels[2], 512)
print(f"Fix_8 points: {pts.shape}", flush=True)
assert pts.shape[0] == D

# per-class pairs: pair_r = sorted (y_r, y_{r+4}) encoded as a*D + b
pair_keys = np.empty((len(pts), 4), dtype=np.int64)
for r in range(4):
    a = pts[:, r]; b = pts[:, r+4]
    lo = np.minimum(a, b); hi = np.maximum(a, b)
    pair_keys[:, r] = lo * D + hi

# D4 canonical key: lex-min over 8 dihedral perms of (k0,k1,k2,k3)
perms = []
for bb in range(4):
    perms.append(tuple((i+bb) % 4 for i in range(4)))
    perms.append(tuple((-i+bb) % 4 for i in range(4)))
perms = list(dict.fromkeys(perms))
print(f"D4 perms: {perms}", flush=True)
best = pair_keys[:, list(perms[0])]  # (N,4)
for pi in perms[1:]:
    cand = pair_keys[:, list(pi)]
    # lex compare cand < best
    lt = np.zeros(len(pts), dtype=bool)
    eq = np.ones(len(pts), dtype=bool)
    for c in range(4):
        lt |= eq & (cand[:, c] < best[:, c])
        eq &= (cand[:, c] == best[:, c])
    best[lt] = cand[lt]
canon = best  # (N,4)

# fibers: unique sorted rows
sorted_keys = np.sort(pts, axis=1)
uniq, inv = np.unique(sorted_keys, axis=0, return_inverse=True)
print(f"fibers: {len(uniq)}", flush=True)
# unique (fiber, canon) rows
combo = np.concatenate([inv[:, None], canon], axis=1)
uniq_combo = np.unique(combo, axis=0)
print(f"(fiber, canon) rows: {len(uniq_combo)}  (== fibers iff canon constant per fiber)", flush=True)
bad = len(uniq_combo) - len(uniq)
print(f"EXACT PER-CLASS FAILURES (extra rows): {bad}", flush=True)
if bad:
    # find a failing fiber example
    from collections import defaultdict
    # count per fiber via uniq_combo first column
    cnt = Counter(uniq_combo[:, 0].tolist())
    bad_fibers = [f for f, c in cnt.items() if c > 1][:3]
    for f in bad_fibers:
        idx = np.where(inv == f)[0][:6]
        print(f" fiber sorted={sorted_keys[idx[0]]}")
        for i in idx:
            print(f"   pt={pts[i]} pairs={pair_keys[i]} canon={canon[i]}")
