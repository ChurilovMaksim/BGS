"""Wave 20, task 2: sampled test of marginal 2-vs-odd compatibility AND the
joint version at m=12 (t=4), where full enumeration (D=1536796800) is
infeasible. Random global Fix points via CRT of prime-power kernels,
grouped by sorted exact multiset; for each repeat pair check:
  (a) Pi_2 ∩ Pi_odd != empty (marginal compatibility),
  (b) a single joint pi with J'^{(q)}_r = J^{(q)}_{pi(r)} for all odd q,
      where J^{(q)}_r = multiset of pairs (p_{i mod P}, y_i mod q) over
      i ≡ r (mod 4), P = 2^{v2(m)} = 4, p = y mod 128.
A single failure of (a) refutes compatibility; a failure of (b) with (a)
holding kills the joint route. Repository untouched; no Lean build.
"""
import math
import numpy as np
from collections import Counter

rng = np.random.default_rng(20261101)


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
    # row-wise CRT: A (N,m) mod mod_a, B (N,m) mod mod_b -> (N,m) mod mod_a*mod_b
    inv = pow(int(mod_a), -1, int(mod_b))
    t = (((B - A) % mod_b) * inv) % mod_b
    return A + mod_a * t


def d_perms(t):
    perms = []
    for b in range(t):
        perms.append(tuple((r + b) % t for r in range(t)))
        perms.append(tuple((-r + b) % t for r in range(t)))
    return list(dict.fromkeys(perms))


def main():
    m, t = 12, 4
    D = Dm(m)
    print(f"m={m} D={D}", flush=True)
    mods = [(2, 128), (3, 81), (5, 25), (7, 49), (11, 121)]
    assert math.prod(q for _, q in mods) == D
    q2, odd_qs = 128, [81, 25, 49, 121]
    P = 4
    kernels = []
    for p, q in mods:
        k = kernel_mod(m, q)
        assert len(k) == q, (m, q, len(k))
        kernels.append((q, k))
        print(f"  ker mod {q}: {len(k)}", flush=True)

    N = 1000000
    pts = kernels[0][1][rng.integers(0, kernels[0][0], size=N)]
    cur = kernels[0][0]
    for q, k in kernels[1:]:
        pts = crt_combine(pts, cur, k[rng.integers(0, q, size=N)], q)
        cur *= q
    assert pts.shape == (N, m)
    print(f"sampled points: {N}", flush=True)

    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
    order = np.argsort(inv, kind="stable")
    bounds = np.concatenate([[0], np.cumsum(counts)])
    nrep = int((counts[counts >= 2]).sum())
    print(f"fibers hit: {len(counts)}, repeat samples: {nrep}", flush=True)

    perms = d_perms(t)
    nperms = len(perms)

    marg = {}
    for _, q in mods:
        v = pts % q
        kk = np.empty((N, t), dtype=np.int64)
        for r in range(t):
            cols = np.sort(v[:, r::t], axis=1)
            key = np.zeros(N, dtype=np.int64)
            for j in range(cols.shape[1]):
                key = key * q + cols[:, j]
            kk[:, r] = key
        marg[q] = kk

    # pattern values: y mod 128, P-periodic with P=4: p_{i mod 4}
    pat = pts % q2  # (N, 12); pattern value at position i is pat[:, i]
    joint = {}
    for q in odd_qs:
        v = pts % q
        pair = pat * q + v
        kk = np.empty((N, t), dtype=np.int64)
        for r in range(t):
            cols = np.sort(pair[:, r::t], axis=1)
            key = np.zeros(N, dtype=np.int64)
            for j in range(cols.shape[1]):
                key = key * (128 * q) + cols[:, j]
            kk[:, r] = key
        joint[q] = kk

    stat = Counter()
    marg_fail, joint_fail = [], []
    for fi in range(len(counts)):
        if counts[fi] < 2:
            continue
        idx = order[bounds[fi]:bounds[fi + 1]]
        base = idx[0]
        others = idx[1:]
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
        jeq = np.ones_like(eq2)
        for q in odd_qs:
            kb = joint[q][base]
            ko = joint[q][others]
            e = np.empty((len(others), nperms), dtype=bool)
            for pi, p in enumerate(perms):
                e[:, pi] = (ko == kb[list(p)]).all(axis=1)
            jeq &= e
        stat["pairs"] += len(others)
        stat["marg_compat"] += int(common.any(axis=1).sum())
        stat["joint_exists"] += int(jeq.any(axis=1).sum())
        stat["joint_violations"] += int((jeq & ~common).any(axis=1).sum())
        if not common.all(axis=1).all():
            for j in np.where(~common.any(axis=1))[0]:
                marg_fail.append((pts[base].tolist(), pts[others[j]].tolist()))
        if (common.any(axis=1) & ~jeq.any(axis=1)).any():
            for j in np.where(common.any(axis=1) & ~jeq.any(axis=1))[0]:
                joint_fail.append((pts[base].tolist(), pts[others[j]].tolist()))
        if len(marg_fail) >= 5 and len(joint_fail) >= 5:
            break
    print(f"stats: {dict(stat)}")
    print(f"marginal failures: {len(marg_fail)}")
    for b in marg_fail[:3]:
        print(f"  base={b[0]} other={b[1]}")
    print(f"joint failures (marginal holds): {len(joint_fail)}")
    for b in joint_fail[:3]:
        print(f"  base={b[0]} other={b[1]}")


if __name__ == "__main__":
    main()
