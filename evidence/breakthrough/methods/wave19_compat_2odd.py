"""Wave 19, task 4: 2-vs-odd per-class compatibility at prime-power level.

For every fiber pair (y, y') in Fix_m (same sorted multiset), compute
  Pi_2   = {pi in D_t : per-class multisets mod 2^a of y' = those of y composed with pi}
  Pi_odd = intersection over odd q || D_m of the analogous pi-sets mod q
and check Pi_2 ∩ Pi_odd != empty. A pair with empty intersection is a
counterexample to 2-vs-odd compatibility. Exhaustive for m = 4, 6, 8
(CRT enumeration via prime-power kernels, as in wave 10).
Repository untouched; no Lean build.
"""
import sys
import numpy as np
from collections import Counter


def Dm(m):
    s0, s1 = 2, 6
    if m == 1:
        return 4
    for _ in range(2, m + 1):
        s0, s1 = s1, 6 * s1 - s0
    return s1 - 2


def prime_power_mods(D):
    # factor D by trial division (D <= 1.4e6 here)
    n, out, p = D, [], 2
    while p * p <= n:
        if n % p == 0:
            q = 1
            while n % p == 0:
                n //= p
                q *= p
            out.append((p, q))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, n))
    return out


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


def check_m(m):
    D = Dm(m)
    t = __import__("math").gcd(m, 4)
    mods = prime_power_mods(D)
    q2 = [q for p, q in mods if p == 2]
    assert len(q2) == 1, mods
    q2 = q2[0]
    odd_qs = [q for p, q in mods if p != 2]
    print(f"m={m} D={D} t={t} q2={q2} odd_qs={odd_qs}", flush=True)
    kernels = []
    for p, q in mods:
        k = kernel_mod(m, q)
        assert len(k) == q, (m, q, len(k))
        kernels.append((q, k))
        print(f"  ker mod {q}: {len(k)}", flush=True)
    pts = kernels[0][1]
    cur = kernels[0][0]
    for q, k in kernels[1:]:
        pts = crt_combine(pts, cur, k, q)
        cur *= q
    assert len(pts) == D, (len(pts), D)
    print(f"  Fix points: {len(pts)}", flush=True)

    # fibers: group by sorted row
    srt = np.sort(pts, axis=1)
    _, inv, counts = np.unique(srt, axis=0, return_inverse=True, return_counts=True)
    order = np.argsort(inv, kind="stable")
    inv_sorted = inv[order]
    bounds = np.concatenate([[0], np.cumsum(counts)])
    print(f"  fibers: {len(counts)}", flush=True)

    # per-class multiset keys per modulus: shape (N, t)
    perms = d_perms(t)
    nperms = len(perms)
    print(f"  D_t perms ({nperms}): {perms}", flush=True)
    keys = {}
    for _, q in mods:
        v = pts % q
        kk = np.empty((len(pts), t), dtype=np.int64)
        for r in range(t):
            cols = v[:, r::t]
            cols = np.sort(cols, axis=1)
            key = np.zeros(len(pts), dtype=np.int64)
            for j in range(cols.shape[1]):
                key = key * q + cols[:, j]
            kk[:, r] = key
        keys[q] = kk

    total_pairs = 0
    bad = []
    stat = Counter()
    for fi in range(len(counts)):
        idx = order[bounds[fi]:bounds[fi + 1]]
        if len(idx) < 2:
            continue
        base = idx[0]
        others = idx[1:]
        # eq masks per modulus: (n_other, nperms) bool
        eq = {}
        for _, q in mods:
            kb = keys[q][base]  # (t,)
            ko = keys[q][others]  # (n, t)
            e = np.empty((len(others), nperms), dtype=bool)
            for pi, p in enumerate(perms):
                e[:, pi] = (ko == kb[list(p)]).all(axis=1)
            eq[q] = e
        eq2 = eq[q2]
        eqodd = np.ones_like(eq2)
        for q in odd_qs:
            eqodd &= eq[q]
        common = eq2 & eqodd
        has = common.any(axis=1)
        total_pairs += len(others)
        stat["pairs"] += len(others)
        stat["both_singleton"] += int(((eq2.sum(axis=1) == 1) & (eqodd.sum(axis=1) == 1)).sum())
        stat["pi2_singleton"] += int((eq2.sum(axis=1) == 1).sum())
        stat["piodd_singleton"] += int((eqodd.sum(axis=1) == 1).sum())
        stat["pi2_full"] += int((eq2.sum(axis=1) == nperms).sum())
        stat["piodd_full"] += int((eqodd.sum(axis=1) == nperms).sum())
        if not has.all():
            for j in np.where(~has)[0]:
                bad.append((fi, pts[base].tolist(), pts[others[j]].tolist(),
                            eq2[j].tolist(), eqodd[j].tolist()))
                if len(bad) >= 5:
                    break
        if len(bad) >= 5:
            break
    print(f"  total fiber pairs: {total_pairs}", flush=True)
    print(f"  stats: {dict(stat)}", flush=True)
    print(f"  BAD (empty Pi2 ∩ Piodd): {len(bad)}", flush=True)
    for b in bad:
        print(f"    fiber {b[0]} base={b[1]} other={b[2]} pi2mask={b[3]} pioddmask={b[4]}", flush=True)
    return len(bad)


if __name__ == "__main__":
    ms = [int(x) for x in sys.argv[1:]] or [4, 6, 8]
    tot = 0
    for m in ms:
        tot += check_m(m)
    print(f"TOTAL BAD: {tot}")
