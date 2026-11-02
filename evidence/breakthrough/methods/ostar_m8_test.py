"""O* test at m=8: are fibers of mu(y)=sorted(y) on Fix_8 exactly affine orbits?

Definitions (from M08_GAMMA_ORBITS.md, which itself cites the project replay):
  H_8 y = 0 mod D, D = 1331712, (H y)_i = 6 y_i - y_{i+1} - y_{i-1} (mod 8).
  Gamma = dihedral perms j -> +-j+k (16 perms).
  Aff   = affine perms p[j] = a*j + b mod 8, a in (Z/8)^x = {1,3,5,7}, b in 0..7
          (32 perms), acting by y'_j = y_{p[j]} (precomposition, as in M08).
  Fiber = { y' in Fix_8 : sorted(y') = sorted(y) }.

Two readings, both tested (affine perms do NOT preserve Fix_8 setwise in
general: sigma H sigma^-1 = 6I - C^3 - C^-3 != H for a=3, so the strict
reading can fail even where the separation reading holds):
  (S) STRICT: fiber == full Aff-orbit of y (all 32 permuted tuples in Fix,
      and the orbit equals the fiber).
  (R) SEPARATION: every y' in the fiber is an Aff-permutation of y
      (equivalently: all points in a fiber share one Aff-canonical form,
      the lex-min over the 32 aff perms). This is the reading that would
      salvage the hSep separation step with Aff in place of Gamma.

Enumeration: ker mod prime powers 9, 289, 512 by recurrence, CRT combine
(same method as oprime_m8_test.py). Canonical forms by lex-min with a
running mask (elementwise min is NOT canonical, cf. oprime note).
Exact integer arithmetic via numpy int64 (values < D, products for CRT
stay < D; no floats anywhere).
"""
import json
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
            for _ in range(m):
                seq.append((6 * seq[-1] - seq[-2]) % mod)
            if seq[m] == a and seq[m + 1] == b:
                res.append(seq[:m])
    return np.array(res, dtype=np.int64)


kernels = [kernel_mod(mod) for mod in MODS]
for mod, k in zip(MODS, kernels):
    print(f"ker mod {mod}: {len(k)}", flush=True)


def crt_combine(A, mod_a, B, mod_b):
    inv = pow(mod_a, -1, mod_b)
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    out = A[:, None, :] + mod_a * t
    return out.reshape(-1, m)


pts = crt_combine(kernels[0], 9, kernels[1], 289)
print("combined 9*289:", pts.shape, flush=True)
pts = crt_combine(pts, 9 * 289, kernels[2], 512)
print("Fix_8 points:", pts.shape, flush=True)
assert pts.shape[0] == D
# sanity: all points in kernel
chk = (6 * pts - np.roll(pts, 1, axis=1) - np.roll(pts, -1, axis=1)) % D
assert np.all(chk == 0), "kernel check failed"

# permutations
aff_perms = []
for a in (1, 3, 5, 7):
    for b in range(8):
        aff_perms.append([(a * j + b) % 8 for j in range(8)])
aff_perms = np.array(aff_perms, dtype=np.int64)
assert len(np.unique(aff_perms, axis=0)) == 32
gam_perms = []
for k in range(8):
    gam_perms.append([(j + k) % 8 for j in range(8)])
    gam_perms.append([(k - j) % 8 for j in range(8)])
gam_perms = np.array(gam_perms, dtype=np.int64)
assert len(np.unique(gam_perms, axis=0)) == 16


def canon(pts, perms, chunk=40000):
    """Lexicographic minimum permuted tuple per point, via running mask."""
    out = np.empty_like(pts)
    P = len(perms)
    for s in range(0, len(pts), chunk):
        ch = pts[s:s + chunk]
        permuted = np.stack([ch[:, p] for p in perms], axis=1)  # (n,P,8)
        mask = np.ones((len(ch), P), dtype=bool)
        for c in range(8):
            vals = np.where(mask, permuted[:, :, c], np.iinfo(np.int64).max)
            mask &= (permuted[:, :, c] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        out[s:s + chunk] = permuted[np.arange(len(ch)), chosen]
        if s % 400000 == 0:
            print(f"  canon chunk {s}", flush=True)
    return out


sorted_keys = np.sort(pts, axis=1)
print("computing Gamma canon...", flush=True)
gam_canon = canon(pts, gam_perms)
print("computing Aff canon...", flush=True)
aff_canon = canon(pts, aff_perms)

uniq_sorted, sorted_counts = np.unique(sorted_keys, axis=0, return_counts=True)
print(f"fibers: {len(uniq_sorted)}, max fiber size: {sorted_counts.max()}")

# per-fiber counts of distinct Gamma / Aff canons
def orbits_per_fiber(canon_arr):
    combo = np.concatenate([sorted_keys, canon_arr], axis=1)
    uniq_combo = np.unique(combo, axis=0)
    cnt = Counter()
    for row in uniq_combo:
        cnt[tuple(row[:8].tolist())] += 1
    return cnt

gam_per_fiber = orbits_per_fiber(gam_canon)
aff_per_fiber = orbits_per_fiber(aff_canon)
gam_bad = [k for k, c in gam_per_fiber.items() if c > 1]
aff_bad = [k for k, c in aff_per_fiber.items() if c > 1]
print(f"Gamma-bad fibers: {len(gam_bad)} (M08 reported 39)")
print(f"Aff-bad fibers (separation reading R): {len(aff_bad)}")

fiber_size = {tuple(r.tolist()): int(c) for r, c in zip(uniq_sorted, sorted_counts)}

# strict reading (S): full Aff-orbit of each point must lie in Fix and equal fiber.
# Check via a set of Fix points: for each point, all 32 aff perms in Fix-set?
fix_set = set(map(tuple, pts.tolist()))
print("building strict-reading check (32 perms x 1.33M points, chunked)...", flush=True)
strict_bad_points = 0
strict_examples = []
# group by fiber: strict holds for a fiber iff aff-orbit of rep == fiber set.
# Equivalent per-point test: aff orbit (as tuple set) subset of fix_set and
# its size == fiber size. We test per fiber using representative + orbit set.
fiber_members = {}
for idx, row in enumerate(sorted_keys):
    fiber_members.setdefault(tuple(row.tolist()), []).append(idx)
n_strict_bad_fibers = 0
strict_fiber_examples = []
for key, idxs in fiber_members.items():
    rep = tuple(pts[idxs[0]].tolist())
    orbit = set(tuple(pts[idxs[0]][p].tolist()) for p in aff_perms)
    if orbit != set(tuple(pts[i].tolist()) for i in idxs):
        n_strict_bad_fibers += 1
        if len(strict_fiber_examples) < 5:
            in_fix = sum(1 for t in orbit if t in fix_set)
            strict_fiber_examples.append({
                "sorted": list(key), "fiber_size": len(idxs),
                "aff_orbit_size": len(orbit),
                "aff_orbit_points_in_fix": in_fix,
                "representative": list(rep),
            })
print(f"Strict-bad fibers (S): {n_strict_bad_fibers}")

# Aff-orbit size distribution vs fiber size (for fibers where orbit in Fix?)
# For the M08 examples, verify aff orbit size 32 and equality.
bad_json = json.load(open("/home/hatch/workspace/bgs-breakthrough/methods/M08_BAD_M8.json"))
m08_check = []
for ex in bad_json["examples"]:
    y = np.array(ex["y"], dtype=np.int64)
    orbit = set(tuple(y[p].tolist()) for p in aff_perms)
    key = tuple(sorted(ex["y"]))
    fib = set(tuple(pts[i].tolist()) for i in fiber_members[key])
    m08_check.append({
        "fiber_size": len(fib), "aff_orbit_size": len(orbit),
        "orbit_in_fix": sum(1 for t in orbit if t in fix_set),
        "orbit_equals_fiber": orbit == fib,
    })
print("M08 examples check:", m08_check)

# Per-component (CRT) test of reading (R): ker mod q, fibers, aff canon.
def component_test(mod):
    K = kernel_mod(mod)
    sk = np.sort(K, axis=1)
    ac = canon(K, aff_perms, chunk=100000)
    combo = np.concatenate([sk, ac], axis=1)
    uc = np.unique(combo, axis=0)
    cnt = Counter(tuple(r[:8].tolist()) for r in uc)
    bad = [k for k, c in cnt.items() if c > 1]
    us, sc = np.unique(sk, axis=0, return_counts=True)
    return {"mod": mod, "n_points": len(K), "n_fibers": len(us),
            "max_fiber": int(sc.max()), "aff_bad_fibers": len(bad),
            "bad_examples": [list(k) for k in bad[:3]]}

comp = [component_test(mod) for mod in MODS]
for c in comp:
    print("component:", c)

out = {
    "m": 8, "D": D, "n_fix": int(len(pts)), "n_fibers": int(len(uniq_sorted)),
    "max_fiber_size": int(sorted_counts.max()),
    "gamma_bad_fibers": int(len(gam_bad)),
    "aff_bad_fibers_separation_R": int(len(aff_bad)),
    "aff_bad_examples_R": [list(k) for k in aff_bad[:5]],
    "strict_bad_fibers_S": int(n_strict_bad_fibers),
    "strict_examples_S": strict_fiber_examples,
    "m08_examples_check": m08_check,
    "components": comp,
    "fiber_size_distribution": {str(k): int(v) for k, v in
                                Counter(sorted_counts.tolist()).items()},
}
json.dump(out, open("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m8_result.json", "w"), indent=1)
print("written ostar_m8_result.json")
print(json.dumps({k: v for k, v in out.items() if k not in
                  ("aff_bad_examples_R", "strict_examples_S")}, indent=1))
