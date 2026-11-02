"""Wave 35, task 3, stage 2: trace-model census of on-support split fibers.

For odd p, component q = p^(2f) of D_m: kernel rows mod q are
p^f * Tr(C alpha^j) mod q, C in R/p^f. Trace sequence is (m/d') repeats
of the d'-cycle (d' = ord_{p^f}(alpha)). Fiber key = sorted d'-cycle
(hashed); orbit canon = lex-min of {C alpha^j, conj(C) alpha^j}.
Support: c . Zbar == 2Q/p^f (mod p^f) for all torsion data, where
Zbar_j = sum_r z_{r d' + j} (folded torsion vector).
A fiber is split iff >= 2 distinct orbit canons; on-support iff every
C in it is supported. Support constancy on fibers is also checked.
"""
import sys, math, hashlib
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from wave16_d1a_targeted import Dm, torsion_data

def alpha_powers(m, mod):
    A = [(1, 0)]
    for _ in range(m):
        a, b = A[-1]
        A.append(((3 * a + 4 * b) % mod, (2 * a + 3 * b) % mod))
    return A

def ord_alpha(mod, m):
    A = alpha_powers(m, mod)
    for j in range(1, m + 1):
        if A[j] == (1, 0):
            return j, A
    return None, A

def tm_census(m, p, f, verbose=True):
    mod = p ** f
    d, A = ord_alpha(mod, m)
    if d is None or A[m] != (1, 0):
        print(f"  m={m} p={p} f={f}: trace model N/A (alpha^{m} != 1 mod {mod})")
        return None
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
    # folded torsion vectors + RHS values
    reps = m // d
    conds = []
    for z, Q in zip(Z, Qmod):
        zbar = np.array([sum(z[r * d + j] for r in range(reps))
                         for j in range(d)], dtype=np.int64)
        rhs = (2 * Q // (p ** f)) % mod
        conds.append((zbar, rhs))
    # enumerate C in chunks
    nC = mod * mod
    chunk = 20000
    hashes = np.empty(nC, dtype='S16')
    ca_all = np.empty(nC, dtype=np.int64)
    cb_all = np.empty(nC, dtype=np.int64)
    sup_all = np.ones(nC, dtype=bool)
    Aarr = np.array(A[:d], dtype=np.int64)  # (d,2)
    for st in range(0, nC, chunk):
        en = min(st + chunk, nC)
        idx = np.arange(st, en, dtype=np.int64)
        a = (idx // mod).astype(np.int64)
        b = (idx % mod).astype(np.int64)
        # cycles: (chunk, d) traces
        ca, cb = a.copy(), b.copy()
        cyc = np.empty((en - st, d), dtype=np.int64)
        ba, bb = a.copy(), b.copy()  # orbit canon trackers
        for j in range(d):
            aj, bj = Aarr[j]
            cyc[:, j] = (2 * ca) % mod
            # orbit candidates: C*alpha^j = (ca,cb); conj(C)*alpha^j
            x1, y1 = ca, cb
            x2 = (a * aj - 2 * b * bj) % mod
            y2 = (a * bj - b * aj) % mod
            upd = (x1 < ba) | ((x1 == ba) & (y1 < bb))
            ba = np.where(upd, x1, ba); bb = np.where(upd, y1, bb)
            upd2 = (x2 < ba) | ((x2 == ba) & (y2 < bb))
            ba = np.where(upd2, x2, ba); bb = np.where(upd2, y2, bb)
            # advance C*alpha^j -> C*alpha^(j+1)
            ca, cb = (3 * ca + 4 * cb) % mod, (2 * ca + 3 * cb) % mod
        # hash sorted cycles
        srt = np.sort(cyc, axis=1)
        for i in range(en - st):
            hashes[st + i] = hashlib.blake2b(
                srt[i].tobytes(), digest_size=16).digest()
        ca_all[st:en] = ba; cb_all[st:en] = bb
        # support: c . Zbar == rhs (mod mod) for all conds
        sup = np.ones(en - st, dtype=bool)
        for zbar, rhs in conds:
            dot = (cyc @ zbar) % mod
            sup &= (dot == rhs)
        sup_all[st:en] = sup
    # group by hash
    uh, inv, cnt = np.unique(hashes, return_inverse=True, return_counts=True)
    # distinct orbit canons per hash: unique (hash, ca, cb) triples
    trip = np.empty(nC, dtype=[('h', 'S16'), ('a', np.int64), ('b', np.int64)])
    trip['h'] = hashes; trip['a'] = ca_all; trip['b'] = cb_all
    ut = np.unique(trip)
    # count distinct canons per hash + support info per hash
    from collections import defaultdict
    canon_count = defaultdict(int)
    for t in ut:
        canon_count[t['h']] += 1
    # support per hash: all supported?
    sup_cnt = np.zeros(len(uh), dtype=np.int64)
    np.add.at(sup_cnt, inv, sup_all.astype(np.int64))
    res = []
    for hi, h in enumerate(uh):
        nc = canon_count[h]
        if nc >= 2:
            res.append((int(cnt[hi]), nc,
                        bool(sup_cnt[hi] == cnt[hi]),
                        bool(sup_cnt[hi] > 0)))
    onsup = [r for r in res if r[2]]
    mixed = [r for r in res if r[3] and not r[2]]
    if verbose:
        print(f"  m={m} p={p} f={f} (mod {mod}, d'={d}): "
              f"split={len(res)} on-support={len(onsup)} mixed-support={len(mixed)}")
        for (sz, nc, allsup, anysup) in sorted(res, reverse=True):
            print(f"    size={sz} orbits={nc} allsup={allsup} anysup={anysup}")
    return res

if __name__ == "__main__":
    cases = [(816, 17, 2), (465, 31, 2), (147, 7, 3), (108, 3, 4),
             (150, 5, 3), (36, 3, 3), (60, 5, 2), (48, 577, 1),
             (30, 31, 2), (42, 7, 2), (63, 7, 2)]
    for (m, p, f) in cases:
        # sanity: q = p^(2f) must divide D_m
        D = Dm(m)
        if D % (p ** (2 * f)) != 0:
            print(f"  m={m} p={p} f={f}: SKIP (p^(2f) does not divide D_m)")
            continue
        tm_census(m, p, f)
