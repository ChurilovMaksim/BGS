"""Debug test (a) at m=18: per-fiber brute-force signature counting
vs the sorted-composite grouping. Also prints one failing fiber
(if any) in full detail."""
import numpy as np
from collections import Counter
from wave36_sigma_structure import kernel_mod_np, kernel_mod_38809

m = 18
K1 = kernel_mod_np(m, 25)
K2 = kernel_mod_38809(m)
n1, n2 = len(K1), len(K2)
N = n1 * n2
MOD2 = 38809
P = (K1[:, None, :].astype(np.int64) * MOD2 +
     K2[None, :, :].astype(np.int64)).astype(np.int32)
flat = P.reshape(N, m)
srt = np.sort(flat, axis=1)
_, inv, counts = np.unique(srt, axis=0, return_inverse=True,
                           return_counts=True)
order = np.argsort(inv, kind="stable")
bounds = np.concatenate([[0], np.cumsum(counts)])
nfib = len(counts)
ev = np.sort(flat[:, 0::2], axis=1)
od = np.sort(flat[:, 1::2], axis=1)
evod = np.concatenate([ev, od], axis=0)
_, uids = np.unique(evod, axis=0, return_inverse=True)
ev_id, od_id = uids[:N], uids[N:]
B = 2 * N
sig = ev_id.astype(np.int64) * B + od_id.astype(np.int64)

# brute-force per fiber via Counters
tot_with = 0
tot = 0
bad_fibers = []
for fi in range(nfib):
    if counts[fi] < 2:
        continue
    idx = order[bounds[fi]:bounds[fi + 1]]
    cs = Counter()
    for p in idx.tolist():
        cs[(int(ev_id[p]), int(od_id[p]))] += 1
    k = len(idx)
    tot += k * (k - 1) // 2
    w = 0
    for (e_, o_), c_ in cs.items():
        w += c_ * (c_ - 1) // 2
        if (o_, e_) > (e_, o_):
            w += c_ * cs.get((o_, e_), 0)
    tot_with += w
    if w != k * (k - 1) // 2:
        bad_fibers.append((fi, k, dict(cs)))
print(f"brute-force per-fiber: total {tot}, with {tot_with}, "
      f"without {tot - tot_with}, bad fibers: {len(bad_fibers)}")
for fi, k, cs in bad_fibers[:3]:
    print(f"  fiber {fi} size {k} signatures {cs}")
    idx = order[bounds[fi]:bounds[fi + 1]]
    print(f"  base pt {idx[0]}: {flat[idx[0]].tolist()}")
    for p in idx[1:4].tolist():
        print(f"  other pt {p}: {flat[p].tolist()} "
              f"sig=({int(ev_id[p])},{int(od_id[p])})")
print("DONE")
