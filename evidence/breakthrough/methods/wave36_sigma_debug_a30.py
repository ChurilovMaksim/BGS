"""Debug/definitive test (a) at m=30: brute-force per-fiber
signature counting (the composite-grouping code in the main
script undercounts; this direct method is the one reported)."""
import numpy as np
from collections import Counter
from wave36_sigma_structure import kernel_mod_np

m = 30
K1 = kernel_mod_np(m, 625)
K2 = kernel_mod_np(m, 841)
n1, n2 = len(K1), len(K2)
N = n1 * n2
MOD2 = 841
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
tot_with = 0
tot = 0
bad = 0
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
        bad += 1
print(f"m=30 (a) brute-force: total {tot}, with {tot_with}, "
      f"WITHOUT {tot - tot_with}, bad fibers: {bad}")
print("DONE")
