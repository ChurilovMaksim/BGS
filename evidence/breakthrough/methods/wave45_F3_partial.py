"""Wave 45, task 6, part 2: dissect partial sums and e_i for top-digit pairs.

For a top-digit pair (j, j') at 729: T[:,j'] - T[:,j] = 243*e_i,
e_i in {0,1,2}. S[j] = A+B+C (partial sums over e-classes),
S[j'] = A + w^c B + w^{2c} C, w = exp(2pi i/3), c = ci mod 3.
Questions: (1) what are A,B,C and their ratios? (2) is e_i a function
of C_i (the kernel point's parameter) mod something small?
(3) what happens for the phase-degenerate fiber-1 pair at m=252?
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

def setup(m):
    q = 729
    D = Dm_big(m)
    perms = gamma_perms(m)
    K = np.array(kernel_points(m, q), dtype=np.int64)
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
    # orbit reps with C labels
    reps = {}
    for f in splits:
        idxf = np.where(fib == f)[0]
        for g in sorted(set(gam[idxf].tolist())):
            oo = idxf[gam[idxf] == g]
            rep = int(oo[0])
            C = recover_C(tuple(K[rep].tolist()), q)
            reps[rep] = (int(f), C)
    return K, T, ci, reps

def analyse(m, c0_target, pairs):
    K, T, ci, reps = setup(m)
    q = 729
    print(f"===== m={m} ci mod 3 = {ci % 3} =====")
    # map (C0, k) -> rep for orbits with first coord c0_target
    by_k = {}
    for rep, (f, C) in reps.items():
        if C[0] == c0_target and C[1] % 27 == 0:
            by_k[C[1] // 27] = rep
    print(f"  orbits with C0={c0_target}: k values {sorted(by_k)}")
    for (k_hi, k_lo) in pairs:
        if k_hi not in by_k or k_lo not in by_k:
            print(f"  pair {k_hi}<->{k_lo}: not both present"); continue
        j1, j2 = by_k[k_hi], by_k[k_lo]
        d = (T[:, j2] - T[:, j1]) % q
        assert np.all(d % 243 == 0), "diff not multiple of 243!"
        e = (d // 243) % 3
        cnt = np.bincount(e, minlength=3)
        zeta = np.exp(2j * np.pi * ((ci * T[:, j1]) % q) / q)
        parts = [complex(zeta[e == r].sum()) for r in range(3)]
        S1 = sum(parts)
        w = np.exp(2j * np.pi / 3)
        c = ci % 3
        S2pred = parts[0] + w**c * parts[1] + w**(2 * c) * parts[2]
        S2 = complex(np.exp(2j * np.pi * ((ci * T[:, j2]) % q) / q).sum())
        print(f"  pair k={k_hi}<->{k_lo}: e-counts={cnt.tolist()} "
              f"|S1|={abs(S1):.4f} ratio S2/S1={S2/S1:.6f} pred={S2pred/S1:.6f}")
        print(f"    partials A={parts[0]:.6f} B={parts[1]:.6f} C={parts[2]:.6f}")
        print(f"    A/C={parts[0]/parts[2] if abs(parts[2])>1e-9 else float('nan'):.6f} "
              f"B/A={parts[1]/parts[0] if abs(parts[0])>1e-9 else float('nan'):.6f} "
              f"C/B={parts[2]/parts[1] if abs(parts[1])>1e-9 else float('nan'):.6f}")
        # e_i vs C_i: C_i = recover_C of kernel point i; x,y divisible by 27?
        # sample: tabulate e by (xbar mod 3, ybar mod 3), xbar=x//27 etc.
        tab = defaultdict(set)
        for i in range(q):
            Ci = recover_C(tuple(K[i].tolist()), q)
            xb, yb = Ci[0] // 27, Ci[1] // 27
            tab[(xb % 3, yb % 3)].add(int(e[i]))
        pure = all(len(v) == 1 for v in tab.values())
        print(f"    e determined by (xbar mod 3, ybar mod 3)? {pure}")
        for key in sorted(tab):
            print(f"      (xbar%3,ybar%3)={key}: e values {sorted(tab[key])}")

analyse(180, 378, [(20, 11), (10, 1), (14, 5)])
analyse(252, 405, [(15, 6)])  # fiber-1 pair: C=(405,405)<->(405,162): k=15<->6
