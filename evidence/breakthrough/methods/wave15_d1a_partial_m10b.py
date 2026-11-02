"""Wave 15, task 3 (m=10, low-memory retry): hash-grouped scan for a split
fiber partially in supp(phihat).  Stage A computes fib_id, supp, orbit
hashes and checkpoints them; stage B groups orbits and reports.
Grouping uses lexsort (no np.unique axis=0 on huge arrays).
"""
import json
import os
import sys

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

sys.path.insert(0, "methods")
from wave15_d1a_partial_scan import Dm, torsion_data, support_mask, gamma_perms

m = 10
D = Dm(m)
CKPT = "/home/hatch/workspace/bgs-breakthrough/methods/wave15_m10_ckpt.npz"

P1 = np.uint64(1099511628211)
P2 = np.uint64(14029467366897019727)


def rowhash(rows):
    h1 = np.zeros(len(rows), dtype=np.uint64)
    h2 = np.zeros(len(rows), dtype=np.uint64)
    for c in range(rows.shape[1]):
        v = rows[:, c].astype(np.uint64) + np.uint64(1)
        h1 = h1 * P1 + v
        h2 = h2 * P2 + v
    return h1, h2


def group_by_hash(h1, h2):
    order = np.lexsort((h2, h1))
    s1, s2 = h1[order], h2[order]
    boundary = np.empty(len(h1), dtype=bool)
    boundary[0] = True
    boundary[1:] = (s1[1:] != s1[:-1]) | (s2[1:] != s2[:-1])
    ids = np.cumsum(boundary) - 1
    out = np.empty(len(h1), dtype=np.int32)
    out[order] = ids.astype(np.int32)
    return out, int(ids[-1]) + 1


if not os.path.exists(CKPT):
    print("D_10 =", D, flush=True)
    M = sp.Matrix([[6, -1], [1, 0]])
    A = M**m - sp.eye(2)
    S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
    assert U * A * V == S
    d1, d2 = int(S[0, 0]), int(S[1, 1])
    import math
    g1, g2 = math.gcd(abs(d1), D), math.gcd(abs(d2), D)
    assert g1 * g2 == D
    Vnp = np.array(V.tolist(), dtype=np.int64)
    y0s = np.arange(0, D, D // g1, dtype=np.int64)
    y1s = np.arange(0, D, D // g2, dtype=np.int64)
    pts = np.empty((D, m), dtype=np.int32)
    CH = 5_000_000
    for st in range(0, D, CH):
        idx = np.arange(st, min(st + CH, D))
        i0, i1 = np.divmod(idx, len(y1s))
        y0, y1 = y0s[i0], y1s[i1]
        k0 = (Vnp[0, 0] * y0 + Vnp[0, 1] * y1) % D
        k1 = (Vnp[1, 0] * y0 + Vnp[1, 1] * y1) % D
        blk = np.empty((len(idx), m), dtype=np.int32)
        blk[:, 0] = k1.astype(np.int32)
        blk[:, 1] = k0.astype(np.int32)
        for i in range(1, m - 1):
            blk[:, i + 1] = ((6 * blk[:, i].astype(np.int64)
                              - blk[:, i - 1]) % D).astype(np.int32)
        pts[st:st + len(idx)] = blk
    for st in range(0, D, CH):
        ch = pts[st:st + CH].astype(np.int64)
        Hy = (6 * ch - np.roll(ch, 1, axis=1) - np.roll(ch, -1, axis=1)) % D
        assert np.all(Hy == 0)
    print("Fix points built:", pts.shape, flush=True)

    Z, Q = torsion_data(m, D)
    supp = support_mask(pts, Z, Q, D, chunk=1_000_000)
    print(f"V4_size={len(Z)} support_size={int(supp.sum())} "
          f"D/V4={D // len(Z)}", flush=True)
    assert D % len(Z) == 0 and int(supp.sum()) == D // len(Z)

    # fiber hashes, chunked (no full sorted matrix stored)
    fh1 = np.empty(D, dtype=np.uint64)
    fh2 = np.empty(D, dtype=np.uint64)
    for st in range(0, D, CH):
        a, b = rowhash(np.sort(pts[st:st + CH], axis=1))
        fh1[st:st + CH] = a
        fh2[st:st + CH] = b
    fib_id, n_fib = group_by_hash(fh1, fh2)
    del fh1, fh2
    print("n_fibers =", n_fib, flush=True)

    # orbit hashes, chunked
    perms = gamma_perms(m)
    oh1 = np.empty(D, dtype=np.uint64)
    oh2 = np.empty(D, dtype=np.uint64)
    CH2 = 200_000
    for st in range(0, D, CH2):
        ch = pts[st:st + CH2]
        permuted = np.stack([ch[:, p] for p in perms], axis=1)
        mask = np.ones((len(ch), len(perms)), dtype=bool)
        for cc in range(m):
            vals = np.where(mask, permuted[:, :, cc], np.iinfo(np.int32).max)
            mask &= (permuted[:, :, cc] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        canon = permuted[np.arange(len(ch)), chosen]
        a, b = rowhash(canon)
        oh1[st:st + CH2] = a
        oh2[st:st + CH2] = b
    print("canon done", flush=True)
    rng = np.random.default_rng(7)
    sample_idx = rng.choice(D, size=20000, replace=False)
    sample_pts = pts[sample_idx].copy()
    np.savez(CKPT, fib_id=fib_id, supp=supp, oh1=oh1, oh2=oh2,
             sample_idx=sample_idx, sample_pts=sample_pts,
             V4_size=len(Z))
    print("checkpoint saved", flush=True)
else:
    print("loading checkpoint", flush=True)
    z = np.load(CKPT)
    fib_id, supp, oh1, oh2 = z["fib_id"], z["supp"], z["oh1"], z["oh2"]
    sample_idx, sample_pts = z["sample_idx"], z["sample_pts"]
    n_fib = int(fib_id.max()) + 1
    print("n_fibers =", n_fib, flush=True)

gam_id, n_gam = group_by_hash(oh1, oh2)
del oh1, oh2
print("n_gamma_orbits =", n_gam, flush=True)
fib_size = np.bincount(fib_id, minlength=n_fib)
gam_fiber = np.empty(n_gam, dtype=np.int64)
gam_fiber[gam_id] = fib_id
orbits_per_fiber = np.bincount(gam_fiber, minlength=n_fib)
bad = np.where(orbits_per_fiber > 1)[0]
in_supp = np.bincount(fib_id[supp], minlength=n_fib)
full = np.where(in_supp == fib_size)[0]
empty = np.where(in_supp == 0)[0]
partial = np.where((in_supp > 0) & (in_supp < fib_size))[0]
rep = {"m": m, "D": D, "n_points": D, "V4_size": int(np.load(CKPT)["V4_size"]),
       "support_size": int(supp.sum()), "n_fibers": int(n_fib),
       "n_gamma_orbits": int(n_gam), "n_split_fibers": int(len(bad)),
       "fibers_full_in_supp": int(len(full)), "fibers_empty": int(len(empty)),
       "fibers_partial": int(len(partial)),
       "split_fibers_meeting_supp": int(len(np.intersect1d(bad, full))),
       "split_fibers_partial": int(len(np.intersect1d(bad, partial)))}
print(json.dumps(rep), flush=True)

# sample validation of hash grouping (direct row comparison)
perms = gamma_perms(m)
s_sorted = np.sort(sample_pts, axis=1)
sh1, sh2 = rowhash(s_sorted)
_, s_fib = np.unique(np.stack([sh1, sh2], axis=1), axis=0,
                     return_inverse=True)
s_fib = np.asarray(s_fib).reshape(-1)
ok = all(np.all(s_sorted[s_fib == g] == s_sorted[s_fib == g][0])
         for g in np.unique(s_fib))
print("sample fiber-hash validation:", ok, flush=True)
canon_s = np.array([min(tuple(row[p]) for p in perms)
                    for row in sample_pts], dtype=np.int32)
oh1s, oh2s = rowhash(canon_s)
_, s_gam = np.unique(np.stack([oh1s, oh2s], axis=1), axis=0,
                     return_inverse=True)
s_gam = np.asarray(s_gam).reshape(-1)
ok2 = all(np.all(canon_s[s_gam == g] == canon_s[s_gam == g][0])
          for g in np.unique(s_gam))
print("sample orbit-hash validation:", ok2, flush=True)
agree = all(len(set(fib_id[sample_idx][s_fib == g].tolist())) == 1
            for g in np.unique(s_fib))
print("sample fiber ids consistent with global ids:", agree, flush=True)

if len(partial):
    f0 = int(partial[0])
    sub = np.where(fib_id == f0)[0]
    orbits = {}
    for g in sorted(set(gam_id[sub].tolist())):
        oo = sub[gam_id[sub] == g]
        orbits[int(g)] = {"size": int(len(oo)),
                          "n_in_supp": int(supp[oo].sum())}
    print("PARTIAL DETAIL:", json.dumps(
        {"first_partial_fiber": f0, "fiber_size": int(len(sub)),
         "n_orbits": len(orbits), "orbits": orbits}), flush=True)

with open("/home/hatch/workspace/bgs-breakthrough/methods/wave15_scan_10.json", "w") as fh:
    json.dump(rep, fh, indent=1)
