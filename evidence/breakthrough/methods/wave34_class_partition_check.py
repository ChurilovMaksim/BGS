"""Wave 34, task 1: exhaustive JOINT class-partition check at m=4 and m=6.

For y in Fix_m, group by sorted exact multiset (the joint global
multiset, since CRT over q2 and odd q gives residues mod D_m).
For each fiber pair (y, y'), test whether one pi in D_t matches the
per-class JOINT multisets J^(q)_r = {(y_i mod q2, y_i mod q) : i = r mod t}
for every odd q. This is exactly the existence reading of the
class-partition lemma (equivalently JBL at these m). Distinct from
wave 19, which tested marginal (per-q) compatibility only.
Exact integer arithmetic via numpy CRT enumeration, as in wave 20.
"""
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


def check(m, t, mods):
    D = Dm(m)
    q2 = mods[0][1]
    odd_qs = [q for _, q in mods[1:]]
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
    assert len(pts) == D, (len(pts), D)
    print(f"m={m} t={t} D={D} Fix points: {len(pts)}", flush=True)

    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True,
                               return_counts=True)
    order = np.argsort(inv, kind="stable")
    inv_sorted = inv[order]
    bounds = np.concatenate([[0], np.cumsum(counts)])
    print(f"  fibers: {len(counts)}", flush=True)

    perms = d_perms(t)
    nperms = len(perms)
    pat = pts % q2
    joint = {}
    for q in odd_qs:
        v = pts % q
        pair = pat * q + v
        kk = np.empty((len(pts), t), dtype=np.int64)
        for r in range(t):
            cols = np.sort(pair[:, r::t], axis=1)
            key = np.zeros(len(pts), dtype=np.int64)
            for j in range(cols.shape[1]):
                key = key * (q2 * q) + cols[:, j]
            kk[:, r] = key
        joint[q] = kk

    total_pairs = 0
    joint_fail = 0
    fail_examples = []
    for fi in range(len(counts)):
        idx = order[bounds[fi]:bounds[fi + 1]]
        if len(idx) < 2:
            continue
        base = idx[0]
        others = idx[1:]
        jeq = np.ones((len(others), nperms), dtype=bool)
        for q in odd_qs:
            kb = joint[q][base]
            ko = joint[q][others]
            e = np.empty((len(others), nperms), dtype=bool)
            for pi, p in enumerate(perms):
                e[:, pi] = (ko == kb[list(p)]).all(axis=1)
            jeq &= e
        total_pairs += len(others)
        bad = ~jeq.any(axis=1)
        joint_fail += int(bad.sum())
        if bad.any() and len(fail_examples) < 3:
            for j in np.where(bad)[0][:3 - len(fail_examples)]:
                fail_examples.append((pts[base].tolist(),
                                      pts[others[j]].tolist()))
    print(f"  fiber pairs: {total_pairs}, joint-pi failures: {joint_fail}")
    for b, o in fail_examples:
        print(f"    FAIL base={b} other={o}")
    return total_pairs, joint_fail


if __name__ == "__main__":
    # m=4: D=1152 = 128 * 9, t=4, q2=128
    check(4, 4, [(2, 128), (3, 9)])
    # m=6: D=39200 = 32 * 25 * 49, t=2, q2=32
    check(6, 2, [(2, 32), (5, 25), (7, 49)])
    print("DONE")
