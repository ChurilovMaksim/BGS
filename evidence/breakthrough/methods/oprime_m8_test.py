"""O' test at m=8, from main definitions only (band_limited_kick_bridge.md D3,
LineDOrbitPairFull phihat/torsion, HEAD 6dbcc7a via connector; local M08 file
used only for the bad-fiber count cross-check, not as source of definitions).

Fix_8 = ker(H_8 mod D), D=1331712=9*289*512. Enumerate ker mod each prime
power by recurrence (y0,y1) fixed by M^8, combine by CRT.
Gamma = dihedral permutations j -> +-j+k on positions.
Support: phihat_s != 0  <=>  for all torsion gamma, phiSummand_s(w,gamma)=1,
i.e. (2*s*Qnum(z_gamma) - pairNum(z_gamma,w)) == 0 mod D, s=1,
w = (H*lift(y))/D, z_gamma = (H*v_lift)/4 for v in V4 = ker(H mod 4).
"""
import json
import numpy as np
import sympy as sp

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
    print(f"ker mod {mod}: {len(k)}")

# CRT combine, vectorised in stages
def crt_combine(A, mod_a, B, mod_b):
    # A: (n,8) mod mod_a, B: (k,8) mod mod_b -> (n*k,8) mod mod_a*mod_b
    inv = pow(mod_a, -1, mod_b)
    # x = a + mod_a * ((b-a)*inv mod mod_b)
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    out = A[:, None, :] + mod_a * t
    return out.reshape(-1, 8)

pts = crt_combine(kernels[0], 9, kernels[1], 289)
print("combined 9*289:", pts.shape)
pts = crt_combine(pts, 9*289, kernels[2], 512)
print("Fix_8 points:", pts.shape)
assert pts.shape[0] == D

# sorted key + Gamma-orbit canonical, in chunks
perms = []
for k in range(8):
    perms.append([(j + k) % 8 for j in range(8)])       # rotation
    perms.append([(k - j) % 8 for j in range(8)])       # reflection
perms = np.array(perms, dtype=np.int64)
assert len(np.unique(perms, axis=0)) == 16

sorted_keys = np.sort(pts, axis=1)
orbit_canon = np.empty_like(pts)
CH = 50000
for s in range(0, len(pts), CH):
    chunk = pts[s:s+CH]
    # permuted: (chunk, perm, coord)
    permuted = np.stack([chunk[:, p] for p in perms], axis=1)
    # lexicographic minimum permuted tuple (elementwise min is NOT a canon:
    # dihedral action is transitive, so it collapses to the global min)
    mask = np.ones((len(chunk), 16), dtype=bool)
    for c in range(8):
        vals = np.where(mask, permuted[:, :, c], np.iinfo(np.int64).max)
        mask &= (permuted[:, :, c] == vals.min(axis=1, keepdims=True))
    chosen = mask.argmax(axis=1)
    orbit_canon[s:s+CH] = permuted[np.arange(len(chunk)), chosen]
    if s % 500000 == 0:
        print(f"  orbit canon chunk {s}")

# fibers: distinct sorted keys; bad = >1 orbit canon inside one sorted key
combo = np.concatenate([sorted_keys, orbit_canon], axis=1)
uniq_combo, combo_counts = np.unique(combo, axis=0, return_counts=True)
uniq_sorted, sorted_counts = np.unique(sorted_keys, axis=0, return_counts=True)
print(f"fibers: {len(uniq_sorted)}, max fiber size: {sorted_counts.max()}")
# orbits per fiber: count distinct combo rows per sorted key
# combo rows are sorted lexicographically by (sorted, canon), so group by first 8 cols
from collections import Counter
# use dict on combo rows (1.3M rows -> acceptable)
orbit_per_fiber = Counter()
fiber_size = {}
for row in uniq_combo:
    key = tuple(row[:8].tolist())
    orbit_per_fiber[key] += 1
bad_keys = [k for k, c in orbit_per_fiber.items() if c > 1]
print(f"bad fibers: {len(bad_keys)} (M08 reported 39)")
bad_set = set(bad_keys)

# support test for points in bad fibers only
H = sp.zeros(m)
for i in range(m):
    H[i, i] = 6; H[i, (i-1) % m] -= 1; H[i, (i+1) % m] -= 1
X = H.adjugate()
# V4
V4 = []
for code in range(4**m):
    v = []; c = code
    for i in range(m):
        v.append(c % 4); c //= 4
    if all(sum(int(H[i, j])*v[j] for j in range(m)) % 4 == 0 for i in range(m)):
        V4.append(v)
assert len(V4) == 16
tors = []
for v in V4:
    hv = [sum(int(H[i, j])*v[j] for j in range(m)) for i in range(m)]
    assert all(x % 4 == 0 for x in hv)
    tors.append([x // 4 for x in hv])

def pair(z, w):
    Xz = [sum(int(X[i, j])*z[j] for j in range(m)) for i in range(m)]
    return sum(Xz[i]*w[i] for i in range(m))
def Q(z):
    return pair(z, z)
tors_Q = [Q(z) for z in tors]

def in_support(y):
    Hy = [6*y[i]-y[(i-1) % m]-y[(i+1) % m] for i in range(m)]
    assert all(x % D == 0 for x in Hy)
    w = [x // D for x in Hy]
    for z, q in zip(tors, tors_Q):
        if (2*q - pair(z, w)) % D != 0:
            return False
    return True

# map sorted key -> points (bad only), using boolean mask via dict lookup on sorted rows
bad_mask = np.array([tuple(r.tolist()) in bad_set for r in sorted_keys])
bad_pts = pts[bad_mask]
bad_sorted = sorted_keys[bad_mask]
bad_orbit = orbit_canon[bad_mask]
print(f"points in bad fibers: {len(bad_pts)}")
results = []
support_hits = 0
killed = []
for key in bad_keys:
    idx = [i for i, r in enumerate(bad_sorted) if tuple(r.tolist()) == key]
    # group support points by orbit canon
    sup_orbits = {}
    for i in idx:
        y = tuple(bad_pts[i].tolist())
        if in_support(y):
            support_hits += 1
            sup_orbits.setdefault(tuple(bad_orbit[i].tolist()), []).append(y)
    if len(sup_orbits) > 1:
        killed.append({"sorted": key, "support_orbits": len(sup_orbits),
                       "examples": {str(k): v[0] for k, v in list(sup_orbits.items())[:2]}})
    results.append({"sorted": key, "fiber_size": len(idx),
                    "n_orbits": orbit_per_fiber[key],
                    "support_points": sum(len(v) for v in sup_orbits.values()),
                    "support_orbits": len(sup_orbits)})
print(f"support points inside bad fibers: {support_hits}")
print(f"bad fibers with support in >=2 orbits (O' killed): {len(killed)}")
for k in killed[:5]:
    print(k)
out = {"m": 8, "D": D, "n_fix": int(pts.shape[0]), "n_fibers": int(len(uniq_sorted)),
       "bad_fibers": int(len(bad_keys)), "points_in_bad_fibers": int(len(bad_pts)),
       "support_points_in_bad_fibers": int(support_hits),
       "oprim_killed": len(killed) > 0, "killed_examples": killed[:5],
       "bad_fiber_summary": results}
json.dump(out, open("/home/hatch/workspace/bgs-breakthrough/methods/oprime_m8_result.json", "w"), indent=1)
print("written oprime_m8_result.json")
