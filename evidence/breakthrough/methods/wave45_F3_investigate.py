"""Wave 45, task 6: investigate the uniform phase gap F3 at 729.

For each m on the 9t line (v3(m)=2, so 729 is the full 3-component):
- enumerate 729 kernel points, fibers, dihedral orbits;
- find the fiber-0 orbits (C[0]=378) and their C=(378,27k) labels;
- compute S_729 phases via the wave-34 formula;
- print phase gaps for top-digit pairs k -> k-9;
- analyse T-columns of a top-digit pair: is one a translate of the other?
"""
import math
import numpy as np
from collections import defaultdict

exec(open("wave38_blind_explore.py").read().split("m = 60")[0])

def gamma_perms(m):
    perms, seen = [], set()
    for k in range(m):
        for p in (tuple((j + k) % m for j in range(m)),
                  tuple((k - j) % m for j in range(m))):
            if p not in seen:
                seen.add(p); perms.append(p)
    return np.array(perms, dtype=np.int64)

def lex_canon(arr, perms, chunk=10000):
    out = np.empty_like(arr)
    for st in range(0, len(arr), chunk):
        ch = arr[st:st + chunk]
        permuted = np.stack([ch[:, p] for p in perms], axis=1)
        mask = np.ones((len(ch), len(perms)), dtype=bool)
        for cc in range(arr.shape[1]):
            vals = np.where(mask, permuted[:, :, cc], np.iinfo(arr.dtype).max)
            mask &= (permuted[:, :, cc] == vals.min(axis=1, keepdims=True))
        chosen = mask.argmax(axis=1)
        out[st:st + chunk] = permuted[np.arange(len(ch)), chosen]
    return out

def group_ids(keys):
    _, ids = np.unique(keys, axis=0, return_inverse=True)
    return np.asarray(ids).reshape(-1)

def Dm_big(m):
    e0, e1 = 2, 6
    for _ in range(2, m + 1):
        e0, e1 = e1, 6 * e1 - e0
    return e1 - 2

def phases_729(m):
    """Return (info, T, ci, q): info maps orbit rep index -> (fiber, C, phase, size)."""
    q = 729
    D = Dm_big(m)
    perms = gamma_perms(m)
    K = np.array(kernel_points(m, q), dtype=np.int64)
    assert len(K) == q
    fib = group_ids(np.sort(K, axis=1))
    canon = lex_canon(K, perms)
    gam = group_ids(canon)
    gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
    gam_fiber[gam] = fib
    opf = np.bincount(gam_fiber, minlength=int(fib.max()) + 1)
    splits = [f for f in np.where(opf > 1)[0]]
    H = lambda v: 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)
    HK = H(K)
    assert np.all(HK % q == 0)
    W = HK // q
    dqm = (D // q) % q
    Qv = (dqm * np.einsum("ij,ij->i", W, K)) % q
    P = (dqm * (W @ K.T)) % q
    u = (D // q) % q
    inv_u2 = pow((u * u) % q, -1, q)
    T = (inv_u2 * (2 * Qv[:, None] - P)) % q
    ci = pow(D // q, -1, q)
    info = {}
    for f in splits:
        idxf = np.where(fib == f)[0]
        for g in sorted(set(gam[idxf].tolist())):
            oo = idxf[gam[idxf] == g]
            E = np.exp(2j * np.pi * ((ci * T[:, oo]) % q) / q)
            vals = E.sum(axis=0)
            spread = float(np.abs(vals - vals[0]).max())
            rep = int(oo[0])
            C = recover_C(tuple(K[rep].tolist()), q)
            info[rep] = (int(f), C, float(np.angle(vals[0])), spread, len(oo),
                         complex(vals[0]))
    return info, T, ci, K, gam, fib

for m in [36, 72, 144, 180, 252]:
    info, T, ci, K, gam, fib = phases_729(m)
    print(f"===== m={m} =====", flush=True)
    # fiber-0 = orbits with C[0] == 378
    f0 = {r: v for r, v in info.items() if v[1][0] == 378}
    print(f"  fiber-0 orbits (C=(378,27k)): {len(f0)}")
    by_k = {}
    for r, (f, C, ph, sp, sz, val) in sorted(f0.items(), key=lambda kv: kv[1][1][1]):
        k = C[1] // 27
        by_k[k] = (r, ph, sz, val)
        print(f"    k={k:2d} C={C} phase={ph:+.6f} size={sz} |S|={abs(val):.4f} spread={sp:.1e}")
    for k in sorted(by_k):
        if k - 9 in by_k:
            r1, ph1, _, _ = by_k[k]
            r2, ph2, _, _ = by_k[k - 9]
            dth = abs((ph1 - ph2 + math.pi) % (2 * math.pi) - math.pi)
            print(f"    pair k={k}<->{k-9}: gap={dth:.6f} (2pi/3={2*math.pi/3:.6f})")
    # T-column analysis for the first top-digit pair found
    pair = None
    for k in sorted(by_k):
        if k - 9 in by_k:
            pair = (by_k[k][0], by_k[k - 9][0]); break
    if pair:
        j1, j2 = pair
        col1 = np.sort(T[:, j1]); col2 = np.sort(T[:, j2])
        diffs = (col2 - col1) % 729
        uq, cnt = np.unique(diffs, return_counts=True)
        print(f"    T-column sorted-diff for pair: unique diffs={list(zip(uq.tolist(), cnt.tolist()))[:10]}")
        # pointwise: is T[:,j2] - T[:,j1] constant?
        pd = (T[:, j2] - T[:, j1]) % 729
        uq2, cnt2 = np.unique(pd, return_counts=True)
        print(f"    T-column pointwise-diff: unique={list(zip(uq2.tolist(), cnt2.tolist()))[:10]}")
        # S ratio
        S1 = complex(np.exp(2j * np.pi * ((ci * T[:, j1]) % 729) / 729).sum())
        S2 = complex(np.exp(2j * np.pi * ((ci * T[:, j2]) % 729) / 729).sum())
        print(f"    S ratio S2/S1 = {S2/S1:.6f}  (omega={complex(np.exp(2j*np.pi/3)):.6f})")
print("DONE")
