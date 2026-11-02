"""Separation invariants within fibers at m=8 (exact integer arithmetic).

Question: is there a computable invariant I(y), Gamma-invariant but NOT
fully symmetric, that separates distinct Gamma-orbits inside one fiber
(sorted(y) class)?  Symmetric invariants (power sums sum y_j^k, ANY symmetric
polynomial) are constant on a fiber BY DEFINITION, so they cannot separate
anything -- this is proved in the note, not tested.

Candidates tested here on ALL of Fix_8 (1,331,712 points, CRT enumeration
as in oprime_m8_test.py):
  * w_sorted : sorted(w), w = (H y)/D  (integer vector; H y is a multiple of D)
  * pair_sorted : sorted over gamma in V4 of z_gamma . y  (exact integers;
                   pairNum(z_gamma, w_y) = z_gamma . y, since X w_y = y)
  * pair_mod_sorted : same, mod D (the support-criterion values)
  * support_pass_count : #{gamma : (2 Qnum(z_gamma) - pairNum) == 0 mod D}
  * S1, S1+S2, S1+S2+S3 : nearest / next-nearest / opposite neighbour sums
  * w_gamma_canon : lex-min Gamma-orbit canonical of w (sanity: must be a
                    PERFECT separator, by H commuting with Gamma and H
                    invertible over Q -- see note)
  * (bad fibers only, 1152 points) adjacency pair multiset and adjacency
    difference multiset.

For each invariant we report: #distinct (fiber, invariant) classes,
#fibers where invariant classes < Gamma-orbits (separation failures),
same restricted to the 39 Gamma-bad fibers, and whether the invariant is
constant on Gamma-orbits (distinct (gamma, invariant) pairs == #orbits).
"""
import json, gc
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
            for _ in range(m):
                seq.append((6*seq[-1] - seq[-2]) % mod)
            if seq[m] == a and seq[m+1] == b:
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
pts = crt_combine(pts, 9*289, kernels[2], 512)
print("Fix_8 points:", pts.shape, flush=True)
assert pts.shape[0] == D
chk = (6*pts - np.roll(pts, 1, axis=1) - np.roll(pts, -1, axis=1)) % D
assert np.all(chk == 0)

gam_perms = []
for k in range(8):
    gam_perms.append([(j + k) % 8 for j in range(8)])
    gam_perms.append([(k - j) % 8 for j in range(8)])
gam_perms = np.array(gam_perms, dtype=np.int64)
assert len(np.unique(gam_perms, axis=0)) == 16

def lex_canon(arr, perms):
    """Lexicographic minimum over perms, chunked (elementwise min is NOT a canon)."""
    out = np.empty_like(arr)
    CH = 50000
    for s in range(0, len(arr), CH):
        chunk = arr[s:s+CH]
        permuted = np.stack([chunk[:, p] for p in perms], axis=1)
        mask = np.ones((len(chunk), len(perms)), dtype=bool)
        for c in range(arr.shape[1]):
            vals = np.where(mask, permuted[:, :, c], np.iinfo(np.int64).max)
            mask &= (permuted[:, :, c] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        out[s:s+CH] = permuted[np.arange(len(chunk)), chosen]
    return out

sorted_keys = np.sort(pts, axis=1)
gam_canon = lex_canon(pts, gam_perms)
print("canons done", flush=True)

# --- w = (H y)/D ---
Hy = 6*pts - np.roll(pts, 1, axis=1) - np.roll(pts, -1, axis=1)
assert np.all(Hy % D == 0)
w = Hy // D
print("w range:", int(w.min()), int(w.max()), flush=True)
w_sorted = np.sort(w, axis=1)

# --- fiber / gamma ids (reused for every invariant) ---
uniq_fib, fib_id = np.unique(sorted_keys, axis=0, return_inverse=True)
fib_id = np.asarray(fib_id).reshape(-1)
uniq_gam, gam_id = np.unique(gam_canon, axis=0, return_inverse=True)
gam_id = np.asarray(gam_id).reshape(-1)
n_fib, n_gam = len(uniq_fib), len(uniq_gam)
print(f"fibers={n_fib} gamma-orbits={n_gam}", flush=True)
gam_fiber = np.empty(n_gam, dtype=np.int64)
gam_fiber[gam_id] = fib_id
orbits_per_fiber = np.bincount(gam_fiber, minlength=n_fib)
bad_fib = np.where(orbits_per_fiber > 1)[0]
print(f"bad fibers={len(bad_fib)} (expect 39)", flush=True)
assert len(bad_fib) == 39

def analyse(name, inv):
    """inv: (N, k) int64 array. Returns dict; frees nothing (caller dels)."""
    if inv.ndim == 1:
        inv = inv.reshape(-1, 1)
    uniq_inv, inv_id = np.unique(inv, axis=0, return_inverse=True)
    inv_id = np.asarray(inv_id).reshape(-1)
    n_inv = len(uniq_inv)
    # invariant constant on gamma orbits?
    pair_gi = gam_id.astype(np.int64) * n_inv + inv_id
    n_gi = len(np.unique(pair_gi))
    # classes per fiber
    pair_fi = fib_id.astype(np.int64) * n_inv + inv_id
    uniq_fi = np.unique(pair_fi)
    fib_of_pair = (uniq_fi // n_inv).astype(np.int64)
    classes_per_fiber = np.bincount(fib_of_pair, minlength=n_fib)
    fail = np.where(classes_per_fiber < orbits_per_fiber)[0]
    fail_bad = [int(f) for f in fail if f in set(bad_fib.tolist())]
    res = {
        "name": name, "n_distinct_invariant": int(n_inv),
        "n_fiber_invariant_classes": int(len(uniq_fi)),
        "constant_on_gamma_orbits": bool(n_gi == n_gam),
        "distinct_gamma_invariant_pairs": int(n_gi),
        "n_fail_fibers": int(len(fail)),
        "n_fail_bad_fibers": int(len(fail_bad)),
        "fail_bad_fiber_ids": fail_bad,
    }
    print(json.dumps(res), flush=True)
    return res

results = {}
results["w_sorted"] = analyse("w_sorted", w_sorted)
del w_sorted; gc.collect()

# --- V4, torsion z, Qnum (sympy adjugate-free: solve H t = D z) ---
V4 = []
for code in range(4**m):
    v = []; c = code
    for i in range(m):
        v.append(c % 4); c //= 4
    hv = [6*v[i] - v[(i-1) % m] - v[(i+1) % m] for i in range(m)]
    if all(x % 4 == 0 for x in hv):
        V4.append(v)
assert len(V4) == 16
tors = [[x // 4 for x in [6*v[i] - v[(i-1) % m] - v[(i+1) % m] for i in range(m)]]
        for v in V4]
Z = np.array(tors, dtype=np.int64)
print("V4 size:", len(V4), "z max abs:", int(np.abs(Z).max()), flush=True)
Hsp = sp.zeros(m)
for i in range(m):
    Hsp[i, i] = 6; Hsp[i, (i-1) % m] -= 1; Hsp[i, (i+1) % m] -= 1
Qnum = []
for z in tors:
    t = Hsp.LUsolve(sp.Matrix([D*zz for zz in z]))
    assert all(x.q == 1 for x in t)
    t = tuple(int(x) for x in t)
    Qnum.append(sum(zz*tt for zz, tt in zip(z, t)))
Qnum = np.array(Qnum, dtype=np.int64)
print("Qnum:", Qnum.tolist(), flush=True)
print("2*Qnum mod D:", (2*Qnum % D).tolist(), flush=True)

pair = pts @ Z.T   # (N,16) exact: pairNum(z_gamma, w_y) = z_gamma . y
print("pair range:", int(pair.min()), int(pair.max()), flush=True)
results["pair_sorted"] = analyse("pair_sorted", np.sort(pair, axis=1))
pair_mod = np.sort(pair % D, axis=1)
results["pair_mod_sorted"] = analyse("pair_mod_sorted", pair_mod)
del pair_mod; gc.collect()
# support pass count: (2Q - pair) % D == 0
passmask = ((2*Qnum[None, :] - pair) % D == 0)
passcount = passmask.sum(axis=1)
print("passcount distribution:", np.bincount(passcount).tolist(), flush=True)
results["support_passcount"] = analyse("support_passcount", passcount)
del pair; gc.collect()

# --- neighbour sums ---
S1 = (pts * np.roll(pts, -1, axis=1)).sum(axis=1)
S2 = (pts * np.roll(pts, -2, axis=1)).sum(axis=1)
S3 = (pts * np.roll(pts, -4, axis=1)).sum(axis=1)
results["S1"] = analyse("S1", S1)
results["S1_S2"] = analyse("S1_S2", np.stack([S1, S2], axis=1))
results["S1_S2_S3"] = analyse("S1_S2_S3", np.stack([S1, S2, S3], axis=1))
del S1, S2, S3; gc.collect()

# --- w gamma canon: perfect-separator sanity ---
w_canon = lex_canon(w, gam_perms)
results["w_gamma_canon"] = analyse("w_gamma_canon", w_canon)
del w_canon, w; gc.collect()

# --- bad fibers only: adjacency multisets ---
bad_mask = np.isin(fib_id, bad_fib)
bad_pts = pts[bad_mask]; bad_fib_id = fib_id[bad_mask]; bad_gam_id = gam_id[bad_mask]
print("bad points:", len(bad_pts), flush=True)
def adj_classes(keyfn):
    # keyfn(point) -> hashable invariant; returns #fibers where classes < orbits
    from collections import defaultdict
    per_fiber = defaultdict(dict)  # fiber -> {inv: set(gam)}
    for y, f, g in zip(bad_pts, bad_fib_id, bad_gam_id):
        inv = keyfn(y)
        per_fiber[int(f)].setdefault(inv, set()).add(int(g))
    fail = [f for f, d in per_fiber.items()
            if len(d) < len({g for s in d.values() for g in s})]
    return {"n_bad_fibers": len(per_fiber), "n_fail": len(fail), "fail": fail}
adj_pair = adj_classes(lambda y: tuple(sorted(zip(y.tolist(), np.roll(y, -1).tolist()))))
adj_diff = adj_classes(lambda y: tuple(sorted(((np.roll(y, -1) - y) % D).tolist())))
print("adj_pair_multiset (bad only):", json.dumps(adj_pair), flush=True)
print("adj_diff_multiset (bad only):", json.dumps(adj_diff), flush=True)
results["adj_pair_multiset_badonly"] = adj_pair
results["adj_diff_multiset_badonly"] = adj_diff

# --- M08 three examples: exact candidate values for y vs y' ---
examples = json.load(open('/home/hatch/workspace/bgs-breakthrough/methods/M08_BAD_M8.json'))['examples']
def cand(y):
    y = np.array(y, dtype=np.int64)
    hy = 6*y - np.roll(y, 1) - np.roll(y, -1)
    assert np.all(hy % D == 0)
    wy = hy // D
    pr = Z @ y
    return {
        "w_sorted": sorted(wy.tolist()),
        "pair_sorted": sorted(pr.tolist()),
        "pair_mod_sorted": sorted((pr % D).tolist()),
        "support_passcount": int((((2*Qnum - pr) % D) == 0).sum()),
        "S1": int((y * np.roll(y, -1)).sum()),
        "adj_pair": sorted(zip(y.tolist(), np.roll(y, -1).tolist())),
    }
ex_out = []
for e in examples:
    cy, cyp = cand(e['y']), cand(e['y_prime'])
    ex_out.append({"key": e['key'],
                   "y": cy, "y_prime": cyp,
                   "separates": {k: cy[k] != cyp[k] for k in cy}})
    print("example separates:", ex_out[-1]["separates"], flush=True)
results["m08_examples"] = ex_out

json.dump(results, open('/home/hatch/workspace/bgs-breakthrough/methods/sep_m8_result.json', 'w'), indent=1, default=str)
print("written sep_m8_result.json", flush=True)
