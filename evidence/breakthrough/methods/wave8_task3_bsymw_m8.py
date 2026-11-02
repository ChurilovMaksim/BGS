"""Wave 8, task 3: Bsym_w at m=8, computed from scratch (exact integers).

Definitions (M08 / sep note / oprime note):
  Fix_8 = ker(H_8 mod D), H = 6I - C - C^T, D = 1331712 = 9*289*512.
  fiber = sorted(y) class; Gamma = dihedral perms j -> +-j+k on positions.
  w_y = (H y)/D (integer vector); (fiber,w)-class = (sorted(y), sorted(w_y)) class.
  supp phihat = {y : (2*Qnum(z_g) - pairNum(z_g, w_y)) == 0 mod D for all g in V4},
  V4 = ker(H mod 4), z_g = (H v)/4, pairNum(z,w_y) = z.y (since X w_y = y).
  Bsym_Gamma(X) = (1/|X|) * sum_{x in X} |Gamma x|
                = (1/|X|) * sum_{orbits O subset X} |O|^2   (when X is a union of orbits)
  Bsym_w(X)    = (1/|X|) * sum_{classes C subset X} |C|^2  (same form, w-classes)
  Bsym_fiber(X)= (1/|X|) * sum_{fibers F subset X} |F|^2.

Output: JSON with counts, distributions, and all three Bsym values on supp
and on the whole Fix_8, plus partition-coincidence checks.
"""
import json
import numpy as np
import sympy as sp
from fractions import Fraction

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
    return (A[:, None, :] + mod_a * t).reshape(-1, m)


pts = crt_combine(kernels[0], 9, kernels[1], 289)
pts = crt_combine(pts, 9 * 289, kernels[2], 512)
assert pts.shape[0] == D
chk = (6 * pts - np.roll(pts, 1, axis=1) - np.roll(pts, -1, axis=1)) % D
assert np.all(chk == 0)
print("Fix_8 points:", pts.shape, flush=True)

gam_perms = []
for k in range(8):
    gam_perms.append([(j + k) % 8 for j in range(8)])
    gam_perms.append([(k - j) % 8 for j in range(8)])
gam_perms = np.array(gam_perms, dtype=np.int64)
assert len(np.unique(gam_perms, axis=0)) == 16


def lex_canon(arr, perms):
    out = np.empty_like(arr)
    CH = 50000
    for s in range(0, len(arr), CH):
        chunk = arr[s:s + CH]
        permuted = np.stack([chunk[:, p] for p in perms], axis=1)
        mask = np.ones((len(chunk), len(perms)), dtype=bool)
        for c in range(arr.shape[1]):
            vals = np.where(mask, permuted[:, :, c], np.iinfo(np.int64).max)
            mask &= (permuted[:, :, c] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        out[s:s + CH] = permuted[np.arange(len(chunk)), chosen]
    return out


sorted_keys = np.sort(pts, axis=1)
gam_canon = lex_canon(pts, gam_perms)
print("canons done", flush=True)

Hy = 6 * pts - np.roll(pts, 1, axis=1) - np.roll(pts, -1, axis=1)
assert np.all(Hy % D == 0)
w = Hy // D
w_sorted = np.sort(w, axis=1)
print("w range:", int(w.min()), int(w.max()), flush=True)

uniq_fib, fib_id = np.unique(sorted_keys, axis=0, return_inverse=True)
fib_id = np.asarray(fib_id).reshape(-1)
uniq_gam, gam_id = np.unique(gam_canon, axis=0, return_inverse=True)
gam_id = np.asarray(gam_id).reshape(-1)
uniq_w, w_id = np.unique(w_sorted, axis=0, return_inverse=True)
w_id = np.asarray(w_id).reshape(-1)
n_fib, n_gam, n_w = len(uniq_fib), len(uniq_gam), len(uniq_w)
print(f"fibers={n_fib} gamma-orbits={n_gam} distinct w_sorted={n_w}", flush=True)

# (fiber,w)-classes: unique (fib_id, w_id) pairs
fw_pair = np.stack([fib_id, w_id], axis=1)
uniq_fw, fw_id = np.unique(fw_pair, axis=0, return_inverse=True)
fw_id = np.asarray(fw_id).reshape(-1)
n_fw = len(uniq_fw)
print(f"(fiber,w)-classes={n_fw}", flush=True)

# Partition coincidence: each w-class contains exactly one Gamma-orbit and vice versa?
# gam per fw-class
pair_gf = gam_id.astype(np.int64) * n_fw + fw_id
n_gf = len(np.unique(pair_gf))
# fw per gam-orbit
pair_fg = fw_id.astype(np.int64) * n_gam + gam_id
n_fg = len(np.unique(pair_fg))
print(f"distinct (gam, fw) pairs={n_gf}  distinct (fw, gam) pairs={n_fg}", flush=True)
print(f"partitions coincide: {n_gf == n_gam and n_fg == n_fw and n_fw == n_gam}", flush=True)

fib_size = np.bincount(fib_id, minlength=n_fib)
gam_size = np.bincount(gam_id, minlength=n_gam)
fw_size = np.bincount(fw_id, minlength=n_fw)
gam_fiber = np.empty(n_gam, dtype=np.int64)
gam_fiber[gam_id] = fib_id
orbits_per_fiber = np.bincount(gam_fiber, minlength=n_fib)
bad_fib = np.where(orbits_per_fiber > 1)[0]
print(f"bad fibers={len(bad_fib)}", flush=True)

# --- support via torsion criterion (exact, sympy solve for Qnum) ---
V4 = []
for code in range(4 ** m):
    v = []
    c = code
    for i in range(m):
        v.append(c % 4)
        c //= 4
    hv = [6 * v[i] - v[(i - 1) % m] - v[(i + 1) % m] for i in range(m)]
    if all(x % 4 == 0 for x in hv):
        V4.append(v)
assert len(V4) == 16
tors = [[x // 4 for x in [6 * v[i] - v[(i - 1) % m] - v[(i + 1) % m] for i in range(m)]]
        for v in V4]
Z = np.array(tors, dtype=np.int64)
Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6
    Hsp[i, (i - 1) % m] -= 1
    Hsp[i, (i + 1) % m] -= 1
Qnum = []
for z in tors:
    t = Hsp.LUsolve(sp.Matrix([D * zz for zz in z]))
    assert all(x.q == 1 for x in t)
    t = tuple(int(x) for x in t)
    Qnum.append(sum(zz * tt for zz, tt in zip(z, t)))
Qnum = np.array(Qnum, dtype=np.int64)
print("2*Qnum mod D:", (2 * Qnum % D).tolist(), flush=True)
pair = pts @ Z.T
passcount = (((2 * Qnum[None, :] - pair) % D) == 0).sum(axis=1)
print("passcount distribution:", np.bincount(passcount).tolist(), flush=True)
del pair
supp = passcount == 16
n_supp = int(supp.sum())
print("support size:", n_supp, flush=True)
assert n_supp == 83232

# Support composition: fibers / orbits / w-classes fully in or out?
def composition(ids, n_ids, sizes):
    in_supp = np.bincount(ids[supp], minlength=n_ids)
    full = np.where(in_supp == sizes)[0]
    empty = np.where(in_supp == 0)[0]
    partial = np.where((in_supp > 0) & (in_supp < sizes))[0]
    return {
        "n_in_supp": int(len(full)),
        "n_partial": int(len(partial)),
        "size_dist_in_supp": {str(int(s)): int(((sizes[full] == s).sum())) for s in sorted(set(sizes[full].tolist()))},
        "sum_sq_in_supp": int((sizes[full].astype(object) ** 2).sum()) if len(full) else 0,
    }


comp_fib = composition(fib_id, n_fib, fib_size)
comp_gam = composition(gam_id, n_gam, gam_size)
comp_fw = composition(fw_id, n_fw, fw_size)
print("fibers in supp:", comp_fib, flush=True)
print("orbits in supp:", comp_gam, flush=True)
print("w-classes in supp:", comp_fw, flush=True)

# Bsym values as exact fractions
def bsym(sum_sq, denom):
    return str(Fraction(sum_sq, denom))


out = {
    "m": 8, "D": D, "n_fix": int(D),
    "n_fibers": int(n_fib), "n_gamma_orbits": int(n_gam),
    "n_distinct_w_sorted": int(n_w), "n_fiber_w_classes": int(n_fw),
    "partitions_coincide": bool(n_gf == n_gam and n_fg == n_fw and n_fw == n_gam),
    "distinct_gam_fw_pairs": int(n_gf), "distinct_fw_gam_pairs": int(n_fg),
    "fiber_size_dist": {str(int(s)): int((fib_size == s).sum()) for s in sorted(set(fib_size.tolist()))},
    "gamma_orbit_size_dist": {str(int(s)): int((gam_size == s).sum()) for s in sorted(set(gam_size.tolist()))},
    "bad_fibers": int(len(bad_fib)),
    "support_size": n_supp,
    "passcount_dist": {str(i): int(c) for i, c in enumerate(np.bincount(passcount).tolist())},
    "support_fibers": comp_fib, "support_orbits": comp_gam, "support_w_classes": comp_fw,
    "Bsym_gamma_supp": bsym(comp_gam["sum_sq_in_supp"], n_supp),
    "Bsym_w_supp": bsym(comp_fw["sum_sq_in_supp"], n_supp),
    "Bsym_fiber_supp": bsym(comp_fib["sum_sq_in_supp"], n_supp),
    "Bsym_gamma_fix": bsym(int((gam_size.astype(object) ** 2).sum()), D),
    "Bsym_w_fix": bsym(int((fw_size.astype(object) ** 2).sum()), D),
    "Bsym_fiber_fix": bsym(int((fib_size.astype(object) ** 2).sum()), D),
}
# first bad fiber detail: M08 example sorted key
target = np.array([0, 55488, 332928, 610368, 665856, 721344, 998784, 1276224])
match = np.where(np.all(sorted_keys == target, axis=1))[0]
if len(match):
    f = int(fib_id[match[0]])
    sub = np.where(fib_id == f)[0]
    out["first_bad_fiber"] = {
        "fiber_size": int(len(sub)),
        "gamma_orbits": sorted([int((gam_id[sub] == g).sum()) for g in set(gam_id[sub].tolist())]),
        "w_sorted_values": [sorted(w_sorted[i].tolist()) for i in sub[:1]] + [sorted(w_sorted[j].tolist()) for j in sub if list(w_sorted[j]) != list(w_sorted[sub[0]])],
        "n_distinct_w_sorted": int(len(set(tuple(x) for x in w_sorted[sub].tolist()))),
    }
    print("first bad fiber:", json.dumps(out["first_bad_fiber"]), flush=True)

print(json.dumps(out, indent=1))
with open("/home/hatch/workspace/bgs-breakthrough/methods/wave8_task3_bsymw_m8_result.json", "w") as fh:
    json.dump(out, fh, indent=1)
print("written wave8_task3_bsymw_m8_result.json")
