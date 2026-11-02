"""Follow-up to ostar_m8_test.py: exact structure of the 39 Gamma-bad fibers,
Gamma-orbit size distribution, and strict-good fiber breakdown by size.
Reuses the same enumeration (CRT over 9, 289, 512) and lex-min canon."""
import json
import numpy as np
from collections import Counter

m = 8
D = 1331712


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


kernels = [kernel_mod(mod) for mod in (9, 289, 512)]


def crt_combine(A, mod_a, B, mod_b):
    inv = pow(mod_a, -1, mod_b)
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    return (A[:, None, :] + mod_a * t).reshape(-1, m)


pts = crt_combine(crt_combine(kernels[0], 9, kernels[1], 289), 9 * 289,
                  kernels[2], 512)
assert len(pts) == D

gam_perms = np.array(
    [[(j + k) % 8 for j in range(8)] for k in range(8)] +
    [[(k - j) % 8 for j in range(8)] for k in range(8)], dtype=np.int64)
aff_perms = np.array(
    [[(a * j + b) % 8 for j in range(8)] for a in (1, 3, 5, 7)
     for b in range(8)], dtype=np.int64)


def canon(pts, perms, chunk=40000):
    out = np.empty_like(pts)
    for s in range(0, len(pts), chunk):
        ch = pts[s:s + chunk]
        permuted = np.stack([ch[:, p] for p in perms], axis=1)
        mask = np.ones((len(ch), len(perms)), dtype=bool)
        for c in range(8):
            vals = np.where(mask, permuted[:, :, c], np.iinfo(np.int64).max)
            mask &= (permuted[:, :, c] == vals.min(axis=1, keepdims=True))
        out[s:s + chunk] = permuted[np.arange(len(ch)), mask.argmax(axis=1)]
    return out


sorted_keys = np.sort(pts, axis=1)
gam_canon = canon(pts, gam_perms)
aff_canon = canon(pts, aff_perms)

# per fiber: size, gamma-orbit sizes, aff-canonical count
combo_g = np.concatenate([sorted_keys, gam_canon], axis=1)
uniq_g, cnt_g = np.unique(combo_g, axis=0, return_counts=True)
combo_a = np.concatenate([sorted_keys, aff_canon], axis=1)
uniq_a, cnt_a = np.unique(combo_a, axis=0, return_counts=True)

fib = {}
for row, c in zip(uniq_g, cnt_g):
    fib.setdefault(tuple(row[:8].tolist()), {"gamma_orbits": []})["gamma_orbits"].append(int(c))
for row, c in zip(uniq_a, cnt_a):
    fib.setdefault(tuple(row[:8].tolist()), {})["aff_orbits"] = int(len([1]))  # placeholder
# count distinct aff canons per fiber properly:
aff_per = Counter(tuple(r[:8].tolist()) for r in uniq_a)
for k in fib:
    fib[k]["aff_orbits"] = aff_per[k]
    fib[k]["fiber_size"] = sum(fib[k]["gamma_orbits"])

bad = {k: v for k, v in fib.items() if len(v["gamma_orbits"]) > 1}
print("gamma-bad fibers:", len(bad))
print("bad fiber (size -> orbit sizes) distribution:",
      Counter((v["fiber_size"], tuple(sorted(v["gamma_orbits"]))) for v in bad.values()))
print("total gamma orbits:", sum(len(v["gamma_orbits"]) for v in fib.values()))
print("gamma orbit size distribution:",
      Counter(s for v in fib.values() for s in v["gamma_orbits"]))
print("fiber size distribution:",
      Counter(v["fiber_size"] for v in fib.values()))
print("aff orbits per fiber distribution:",
      Counter(v["aff_orbits"] for v in fib.values()))

# strict-good fibers by size
fix_set = set(map(tuple, pts.tolist()))
fiber_members = {}
for idx, row in enumerate(sorted_keys):
    fiber_members.setdefault(tuple(row.tolist()), []).append(idx)
strict_good_by_size = Counter()
strict_good_examples = []
for key, idxs in fiber_members.items():
    rep = pts[idxs[0]]
    orbit = set(tuple(rep[p].tolist()) for p in aff_perms)
    if orbit == set(tuple(pts[i].tolist()) for i in idxs):
        strict_good_by_size[len(idxs)] += 1
        if len(strict_good_examples) < 3:
            strict_good_examples.append({"sorted": list(key), "size": len(idxs),
                                         "rep": rep.tolist()})
print("strict-good fibers by size:", dict(strict_good_by_size),
      "total:", sum(strict_good_by_size.values()))
# one explicit strict-failure example: a generic size-16 fiber
for key, idxs in fiber_members.items():
    if len(idxs) == 16:
        rep = pts[idxs[0]]
        orbit = [tuple(rep[p].tolist()) for p in aff_perms]
        outside = [t for t in orbit if t not in fix_set]
        print("generic size-16 fiber rep:", rep.tolist())
        print("  aff orbit size:", len(set(orbit)), "of which outside Fix:",
              len(outside), "example outside:", outside[0] if outside else None)
        break

json.dump({
    "gamma_bad_count": len(bad),
    "bad_fiber_structure": {str(k): v for k, v in
                            Counter((v["fiber_size"], tuple(sorted(v["gamma_orbits"])))
                                    for v in bad.values()).items()},
    "gamma_orbit_size_distribution": {str(k): v for k, v in
        Counter(s for v in fib.values() for s in v["gamma_orbits"]).items()},
    "strict_good_by_size": {str(k): v for k, v in strict_good_by_size.items()},
}, open("/home/hatch/workspace/bgs-breakthrough/methods/ostar_m8_followup.json", "w"), indent=1)
print("written ostar_m8_followup.json")
