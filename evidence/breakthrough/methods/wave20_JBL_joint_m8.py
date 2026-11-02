"""Wave 20, task 2: test the JOINT version of 2-vs-odd compatibility at m=8.

For y in Fix_8 (D=1331712, q2=512, odd qs 9, 289, P=8, t=4), define the
joint pair at position i: (p_i, y_i mod q), p_i = y_i mod 512 (the
2-pattern, here the whole 2-component since m=P=8). Per-class joint
multiset J^{(q)}_r = multiset of pairs over i ≡ r (mod 4).
Question: for fiber pairs (y, y') with the same sorted exact multiset,
does there exist a single pi in D_4 with J'^{(q)}_r = J^{(q)}_{pi(r)}
for all r and all odd q? (This implies marginal compatibility by
taking marginals; failure would show the joint route is dead.)
Also record whether joint-pi, when it exists, agrees with Pi_2 ∩ Pi_odd.
Exhaustive over full Fix_8, reusing wave-19 enumeration.
Repository untouched; no Lean build.
"""
import math
import numpy as np
from collections import Counter


def Dm(m):
    s0, s1 = 2, 6
    if m == 1:
        return 4
    for _ in range(2, m + 1):
        s0, s1 = s1, 6 * s1 - s0
    return s1 - 2


def kernel_mod(m, mod):
    a, b = np.meshgrid(np.arange(mod), np.arange(mod), indexing="ij")
    a = a.ravel().astype(np.int64)
    b = b.ravel().astype(np.int64)
    seqs = [a, b]
    for _ in range(m):
        seqs.append((6 * seqs[-1] - seqs[-2]) % mod)
    ok = (seqs[m] == a) & (seqs[m + 1] == b)
    return np.stack([s[ok] for s in seqs[:m]], axis=1)


def crt_combine(A, mod_a, B, mod_b):
    inv = pow(int(mod_a), -1, int(mod_b))
    diff = (B[None, :, :] - A[:, None, :]) % mod_b
    t = (diff * inv) % mod_b
    return (A[:, None, :] + mod_a * t).reshape(-1, A.shape[1])


def d_perms(t):
    perms = []
    for b in range(t):
        perms.append(tuple((r + b) % t for r in range(t)))
        perms.append(tuple((-r + b) % t for r in range(t)))
    return list(dict.fromkeys(perms))


def main():
    m, t = 8, 4
    D = Dm(m)
    mods = [(2, 512), (3, 9), (17, 289)]
    q2, odd_qs = 512, [9, 289]
    kernels = []
    for p, q in mods:
        k = kernel_mod(m, q)
        assert len(k) == q, (m, q, len(k))
        kernels.append((q, k))
    pts = kernels[0][1]
    cur = kernels[0][0]
    for q, k in kernels[1:]:
        pts = crt_combine(pts, cur, k, q)
        cur *= q
    assert len(pts) == D
    print(f"Fix points: {len(pts)}", flush=True)

    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
    order = np.argsort(inv, kind="stable")
    inv_sorted = inv[order]
    bounds = np.concatenate([[0], np.cumsum(counts)])
    print(f"fibers: {len(counts)}", flush=True)

    perms = d_perms(t)
    nperms = len(perms)

    # marginal per-class keys per modulus (as in wave 19)
    marg = {}
    for _, q in mods:
        v = pts % q
        kk = np.empty((len(pts), t), dtype=np.int64)
        for r in range(t):
            cols = np.sort(v[:, r::t], axis=1)
            key = np.zeros(len(pts), dtype=np.int64)
            for j in range(cols.shape[1]):
                key = key * q + cols[:, j]
            kk[:, r] = key
        marg[q] = kk

    # joint per-class keys per odd q: pairs (p_i, y_i mod q), i in class r
    pat = pts % q2  # (N, 8)
    joint = {}
    for q in odd_qs:
        v = pts % q
        pair = pat * q + v  # (N, 8), values < 512*q
        kk = np.empty((len(pts), t), dtype=np.int64)
        for r in range(t):
            cols = np.sort(pair[:, r::t], axis=1)
            key = np.zeros(len(pts), dtype=np.int64)
            for j in range(cols.shape[1]):
                key = key * (512 * q) + cols[:, j]
            kk[:, r] = key
        joint[q] = kk

    stat = Counter()
    joint_fail_examples = []
    total_pairs = 0
    for fi in range(len(counts)):
        idx = order[bounds[fi]:bounds[fi + 1]]
        if len(idx) < 2:
            continue
        base = idx[0]
        others = idx[1:]
        # marginal masks
        eq = {}
        for _, q in mods:
            kb = marg[q][base]
            ko = marg[q][others]
            e = np.empty((len(others), nperms), dtype=bool)
            for pi, p in enumerate(perms):
                e[:, pi] = (ko == kb[list(p)]).all(axis=1)
            eq[q] = e
        eq2 = eq[q2]
        eqodd = np.ones_like(eq2)
        for q in odd_qs:
            eqodd &= eq[q]
        common = eq2 & eqodd
        # joint masks
        jeq = np.ones_like(eq2)
        for q in odd_qs:
            kb = joint[q][base]
            ko = joint[q][others]
            e = np.empty((len(others), nperms), dtype=bool)
            for pi, p in enumerate(perms):
                e[:, pi] = (ko == kb[list(p)]).all(axis=1)
            jeq &= e
        total_pairs += len(others)
        stat["pairs"] += len(others)
        stat["marg_compat"] += int(common.any(axis=1).sum())
        stat["joint_exists"] += int(jeq.any(axis=1).sum())
        stat["joint_subset_of_marg"] += int((jeq & ~common).sum() == 0)
        # joint pi must be among common pi? check per pair
        stat["joint_implies_marg_violations"] += int((jeq & ~common).any(axis=1).sum())
        stat["marg_but_no_joint"] += int((common.any(axis=1) & ~jeq.any(axis=1)).sum())
        if (~jeq.any(axis=1)).any() and len(joint_fail_examples) < 5:
            for j in np.where(~jeq.any(axis=1))[0]:
                if common[j].any():
                    joint_fail_examples.append(
                        (pts[base].tolist(), pts[others[j]].tolist(),
                         common[j].tolist(), jeq[j].tolist()))
                    if len(joint_fail_examples) >= 5:
                        break
    print(f"total fiber pairs: {total_pairs}")
    print(f"stats: {dict(stat)}")
    print("marg-but-no-joint examples (base, other, common_mask, joint_mask):")
    for e in joint_fail_examples:
        print(f"  base={e[0]} other={e[1]} common={e[2]} joint={e[3]}")


if __name__ == "__main__":
    main()
