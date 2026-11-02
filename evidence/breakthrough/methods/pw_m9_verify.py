"""Independent cross-check of pw_m9.cpp at m=9, via numpy (sep_m8_test.py style).

Uses gluing_components.fix_mod (Python, not the C++ port) + numpy CRT,
lex-min Gamma canon, np.unique fiber/orbit counts. No w here: if bad=0,
P_w failure is impossible, so the check that matters is fibers vs orbits.
"""
import json
import sys
import numpy as np
sys.path.insert(0, '/home/hatch/workspace/bgs-breakthrough/methods')
from gluing_components import fix_mod

m, D = 9, 7761796
MODS = (4, 49, 39601)
kernels = []
for q in MODS:
    vecs = fix_mod(m, q)
    print(f"q={q} n_fix={len(vecs)}", flush=True)
    assert len(vecs) == q
    kernels.append(np.array(vecs, dtype=np.int64))

def crt_combine(A, mod_a, B, mod_b):
    inv = pow(mod_a, -1, mod_b)
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    out = A[:, None, :] + mod_a * t
    return out.reshape(-1, m)

pts = crt_combine(kernels[0], 4, kernels[1], 49)
print("after 4x49:", pts.shape, flush=True)
pts = crt_combine(pts, 4 * 49, kernels[2], 39601)
print("Fix_9 points:", pts.shape, flush=True)
assert pts.shape[0] == D
chk = (6 * pts - np.roll(pts, 1, axis=1) - np.roll(pts, -1, axis=1)) % D
assert np.all(chk == 0)
print("H check passed", flush=True)

gam_perms = []
for k in range(m):
    gam_perms.append([(j + k) % m for j in range(m)])
    gam_perms.append([(k - j) % m for j in range(m)])
gam_perms = np.array(gam_perms, dtype=np.int64)
assert len(np.unique(gam_perms, axis=0)) == 18

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
del pts
uniq_fib, fib_id = np.unique(sorted_keys, axis=0, return_inverse=True)
fib_id = np.asarray(fib_id).reshape(-1)
del sorted_keys
uniq_gam, gam_id = np.unique(gam_canon, axis=0, return_inverse=True)
gam_id = np.asarray(gam_id).reshape(-1)
del gam_canon
n_fib, n_gam = len(uniq_fib), len(uniq_gam)
gam_fiber = np.empty(n_gam, dtype=np.int64)
gam_fiber[gam_id] = fib_id
orbits_per_fiber = np.bincount(gam_fiber, minlength=n_fib)
bad = int(np.sum(orbits_per_fiber > 1))
print(f"fibers={n_fib} gamma_orbits={n_gam} bad_fibers={bad}", flush=True)
json.dump({"m": m, "D": D, "n_points": int(len(fib_id)),
           "n_fibers": int(n_fib), "n_gamma_orbits": int(n_gam),
           "n_bad_fibers": bad},
          open('/home/hatch/workspace/bgs-breakthrough/methods/pw_m9_verify_result.json', 'w'), indent=1)
print("written pw_m9_verify_result.json", flush=True)
