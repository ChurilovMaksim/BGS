"""Wave 15, task 3 (m=10): hash-grouped scan for a split fiber partially
in supp(phihat).  Full 45,239,074-point enumeration; fibers and
Gamma-orbits grouped by 128-bit row hashes (collision probability
~ N^2 / 2^129 ~ 1e-21; verified on a random sample by direct row
comparison).  Reuses definitions from wave15_d1a_partial_scan.py.
"""
import json

import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_decomp

import sys
sys.path.insert(0, "methods")
from wave15_d1a_partial_scan import Dm, torsion_data, support_mask, gamma_perms

m = 10
D = Dm(m)
print("D_10 =", D, flush=True)

# --- Fix points, chunked SNF seed generation ---
M = sp.Matrix([[6, -1], [1, 0]])
A = M**m - sp.eye(2)
S, U, V = smith_normal_decomp(A, domain=sp.ZZ)
assert U * A * V == S
d1, d2 = int(S[0, 0]), int(S[1, 1])
import math
g1, g2 = math.gcd(abs(d1), D), math.gcd(abs(d2), D)
assert g1 * g2 == D, (g1, g2, D)
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
    print(f"  seeds {st + len(idx)}/{D}", flush=True)
for st in range(0, D, CH):
    ch = pts[st:st + CH].astype(np.int64)
    Hy = (6 * ch - np.roll(ch, 1, axis=1) - np.roll(ch, -1, axis=1)) % D
    assert np.all(Hy == 0)
print("Fix points built:", pts.shape, flush=True)

# --- support ---
Z, Q = torsion_data(m, D)
supp = support_mask(pts, Z, Q, D, chunk=1_000_000)
print(f"V4_size={len(Z)} support_size={int(supp.sum())} "
      f"D/V4={D // len(Z) if D % len(Z) == 0 else 'non-integer'}", flush=True)
assert D % len(Z) == 0 and int(supp.sum()) == D // len(Z)

# --- 128-bit row hashes ---
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
    arr = np.empty((len(h1), 2), dtype=np.uint64)
    arr[:, 0] = h1
    arr[:, 1] = h2
    _, ids = np.unique(arr, axis=0, return_inverse=True)
    return np.asarray(ids).reshape(-1).astype(np.int32), int(ids.max()) + 1


print("sorting rows for fibers...", flush=True)
srt = np.sort(pts, axis=1)
h1, h2 = rowhash(srt)
del srt
fib_id, n_fib = group_by_hash(h1, h2)
del h1, h2
print("n_fibers =", n_fib, flush=True)

# --- Gamma canon hashes, chunked (canon rows not stored) ---
perms = gamma_perms(m)
print(f"gamma perms: {len(perms)}", flush=True)
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
    if (st // CH2) % 50 == 0:
        print(f"  canon {st + len(ch)}/{D}", flush=True)
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
rep = {"m": m, "D": D, "n_points": D, "V4_size": int(len(Z)),
       "support_size": int(supp.sum()), "n_fibers": int(n_fib),
       "n_gamma_orbits": int(n_gam), "n_split_fibers": int(len(bad)),
       "fibers_full_in_supp": int(len(full)), "fibers_empty": int(len(empty)),
       "fibers_partial": int(len(partial)),
       "split_fibers_meeting_supp": int(len(np.intersect1d(bad, full))),
       "split_fibers_partial": int(len(np.intersect1d(bad, partial)))}
print(json.dumps(rep), flush=True)

# --- sample validation of hash grouping (direct row comparison) ---
rng = np.random.default_rng(7)
sample = rng.choice(D, size=20000, replace=False)
s_sorted = np.sort(pts[sample], axis=1)
sh1, sh2 = rowhash(s_sorted)
_, s_fib = np.unique(np.stack([sh1, sh2], axis=1), axis=0,
                     return_inverse=True)
s_fib = np.asarray(s_fib).reshape(-1)
ok = True
for g in np.unique(s_fib):
    rows = s_sorted[s_fib == g]
    if not np.all(rows == rows[0]):
        ok = False
print("sample fiber-hash validation (equal hash => equal sorted row):",
      ok, flush=True)
# orbit sample check: canon equality within hash groups
perms_np = perms
canon_s = []
for row in pts[sample]:
    cands = [tuple(row[p]) for p in perms_np]
    canon_s.append(min(cands))
canon_s = np.array(canon_s, dtype=np.int32)
oh1s, oh2s = rowhash(canon_s)
_, s_gam = np.unique(np.stack([oh1s, oh2s], axis=1), axis=0,
                     return_inverse=True)
s_gam = np.asarray(s_gam).reshape(-1)
ok2 = True
for g in np.unique(s_gam):
    rows = canon_s[s_gam == g]
    if not np.all(rows == rows[0]):
        ok2 = False
print("sample orbit-hash validation (equal hash => equal canon):",
      ok2, flush=True)
# cross-check: sample fiber ids agree with global fiber ids up to relabel
agree = True
for g in np.unique(s_fib):
    gl = set(fib_id[sample][s_fib == g].tolist())
    if len(gl) != 1:
        agree = False
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
         "n_orbits": len(orbits), "orbits": orbits,
         "example_point": pts[sub[0]].tolist()}), flush=True)

with open("/tmp/wave15_scan_10.json", "w") as fh:
    json.dump(rep, fh, indent=1)
