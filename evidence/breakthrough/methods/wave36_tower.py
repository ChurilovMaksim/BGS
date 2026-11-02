"""Wave 36, task 2: tower census for the Lift-Tower Lemma.

For (m, p) with trace levels f = 1..F (p^(2f) | D_m), compute at each
level f the fibers of C in R/p^f (fiber key = sorted d_f-cycle of
Tr(C alpha^j), d_f = ord_{p^f}(alpha); Gamma-orbit canon = lex-min of
{C alpha^j, conj(C) alpha^j}), with the wave-16 support flag, and the
reduction maps of fibers (and orbits) to lower levels.

Usage: python3 wave36_tower.py m p
"""
import sys, hashlib
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave16_d1a_targeted import Dm, torsion_data


def alpha_powers(m, mod):
    A = [(1, 0)]
    for _ in range(m):
        a, b = A[-1]
        A.append(((3 * a + 4 * b) % mod, (2 * a + 3 * b) % mod))
    return A


def census_level(m, p, f):
    mod = p ** f
    A = alpha_powers(m, mod)
    d = next((j for j in range(1, m + 1) if A[j] == (1, 0)), None)
    assert d is not None and A[m] == (1, 0), f"trace model N/A m={m} p={p} f={f}"
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
    reps = m // d
    conds = []
    for z, Q in zip(Z, Qmod):
        zbar = np.array([sum(z[r * d + j] for r in range(reps))
                         for j in range(d)], dtype=np.int64)
        rhs = (2 * Q // (p ** f)) % mod
        conds.append((zbar, rhs))
    nC = mod * mod
    chunk = 20000
    hashes = np.empty(nC, dtype='S16')
    ca_all = np.empty(nC, dtype=np.int64)
    cb_all = np.empty(nC, dtype=np.int64)
    sup_all = np.ones(nC, dtype=bool)
    Aarr = np.array(A[:d], dtype=np.int64)
    for st in range(0, nC, chunk):
        en = min(st + chunk, nC)
        idx = np.arange(st, en, dtype=np.int64)
        a = (idx // mod).astype(np.int64)
        b = (idx % mod).astype(np.int64)
        cyc = np.empty((en - st, d), dtype=np.int64)
        ca, cb = a.copy(), b.copy()
        ba, bb = a.copy(), b.copy()
        for j in range(d):
            aj, bj = Aarr[j]
            cyc[:, j] = (2 * ca) % mod
            x1, y1 = ca, cb
            x2 = (a * aj - 2 * b * bj) % mod
            y2 = (a * bj - b * aj) % mod
            upd = (x1 < ba) | ((x1 == ba) & (y1 < bb))
            ba = np.where(upd, x1, ba); bb = np.where(upd, y1, bb)
            upd2 = (x2 < ba) | ((x2 == ba) & (y2 < bb))
            ba = np.where(upd2, x2, ba); bb = np.where(upd2, y2, bb)
            ca, cb = (3 * ca + 4 * cb) % mod, (2 * ca + 3 * cb) % mod
        srt = np.sort(cyc, axis=1)
        for i in range(en - st):
            hashes[st + i] = hashlib.blake2b(
                srt[i].tobytes(), digest_size=16).digest()
        ca_all[st:en] = ba; cb_all[st:en] = bb
        sup = np.ones(en - st, dtype=bool)
        for zbar, rhs in conds:
            dot = (cyc @ zbar) % mod
            sup &= (dot == rhs)
        sup_all[st:en] = sup
    # group by hash: fiber id, orbit canons, support
    uh, inv, cnt = np.unique(hashes, return_inverse=True, return_counts=True)
    trip = np.empty(nC, dtype=[('h', 'S16'), ('a', np.int64), ('b', np.int64)])
    trip['h'] = hashes; trip['a'] = ca_all; trip['b'] = cb_all
    ut = np.unique(trip)
    canon_count = defaultdict(int)
    canon_by_fiber = defaultdict(set)
    for t in ut:
        canon_count[t['h']] += 1
        canon_by_fiber[t['h']].add((int(t['a']), int(t['b'])))
    sup_cnt = np.zeros(len(uh), dtype=np.int64)
    np.add.at(sup_cnt, inv, sup_all.astype(np.int64))
    fibers = []  # (hash, size, norbits, allsup, anysup, canons)
    for hi, h in enumerate(uh):
        nc = canon_count[h]
        fibers.append((h, int(cnt[hi]), nc,
                       bool(sup_cnt[hi] == cnt[hi]),
                       bool(sup_cnt[hi] > 0),
                       canon_by_fiber[h]))
    return {'mod': mod, 'd': d, 'fibers': fibers,
            'hashes': hashes, 'ca': ca_all, 'cb': cb_all, 'sup': sup_all}


def main():
    m, p = int(sys.argv[1]), int(sys.argv[2])
    D = Dm(m)
    v = 0
    while D % p == 0:
        D //= p; v += 1
    F = v // 2
    print(f"m={m} p={p} v_p(D_m)={v} trace levels 1..{F}")
    levels = {}
    for f in range(1, F + 1):
        lv = census_level(m, p, f)
        levels[f] = lv
        split = [x for x in lv['fibers'] if x[2] >= 2]
        onsup = [x for x in split if x[3]]
        mixed = [x for x in split if x[4] and not x[3]]
        print(f" level f={f} (mod {lv['mod']}, d'={lv['d']}): "
              f"split={len(split)} on-support={len(onsup)} mixed={len(mixed)}")
        for (h, sz, nc, allsup, anysup, canons) in sorted(split, key=lambda x: -x[1]):
            print(f"   size={sz} orbits={nc} allsup={allsup} anysup={anysup}")
    # refined analysis: separate DEGENERATE fibers (all elements divisible
    # by p: then F_f = p * F_{f-1}) from GENUINE ones, and test:
    # (LT1) every genuine split fiber at level f reduces mod p^2 to a
    # split fiber at level 2; (LT2) at most one genuine split fiber per
    # base split fiber; (LT3) degenerate fibers are exactly p * (level
    # f-1 split fibers).
    if F >= 2:
        mod2 = p ** 2
        lv2 = levels[2]
        l2info = {h: (nc, allsup) for (h, sz, nc, allsup, anysup, _) in lv2['fibers']}
        d2 = lv2['d']

        def hash_at_level(a, b, mod, d):
            ca, cb = a % mod, b % mod
            cyc = []
            for j in range(d):
                cyc.append((2 * ca) % mod)
                ca, cb = (3 * ca + 4 * cb) % mod, (2 * ca + 3 * cb) % mod
            return hashlib.blake2b(
                np.sort(np.array(cyc, dtype=np.int64)).tobytes(),
                digest_size=16).digest()

        for f in range(2, F + 1):
            lv = levels[f]
            split = [x for x in lv['fibers'] if x[2] >= 2 and x[3]]  # on-support
            degen, genuine = [], []
            for x in split:
                ca, cb = next(iter(x[5]))
                (degen if (ca % p == 0 and cb % p == 0) else genuine).append(x)
            print(f" level f={f}: on-support split={len(split)} "
                  f"genuine={len(genuine)} degenerate={len(degen)}")
            if f >= 3:
                # LT1/LT2 for genuine fibers
                per_base = defaultdict(int)
                bad = []
                for (h, sz, nc, allsup, anysup, canons) in genuine:
                    ca, cb = next(iter(canons))
                    h2 = hash_at_level(ca, cb, mod2, d2)
                    info = l2info.get(h2)
                    if info is None or info[0] < 2:
                        bad.append((sz, nc, info))
                    else:
                        per_base[h2] += 1
                print(f"   genuine -> level 2: {len(genuine)} fibers, "
                      f"{len(per_base)} base fibers, per-base counts="
                      f"{sorted(per_base.values())}, bad={bad}")
                # LT3: degenerate fibers should be p * (level f-1 split fibers);
                # check ALL canons divide into a single level f-1 fiber
                # with matching size and orbit count.
                lvm1 = levels[f - 1]
                m1info = {h: (sz, nc) for (h, sz, nc, a, an, _) in lvm1['fibers']}
                bad3 = []
                for (h, sz, nc, allsup, anysup, canons) in degen:
                    h1s = {hash_at_level(ca // p, cb // p, lvm1['mod'], lvm1['d'])
                           for (ca, cb) in canons}
                    if len(h1s) != 1:
                        bad3.append((sz, nc, 'multi-parent'))
                        continue
                    info = m1info.get(next(iter(h1s)))
                    if info is None or info != (sz, nc):
                        bad3.append((sz, nc, info))
                print(f"   degenerate = p*(level {f-1} split fiber): "
                      f"{len(degen)} fibers, bad={bad3}")


if __name__ == "__main__":
    main()
