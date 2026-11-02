"""Wave 39 task 5: below-base checks.
A: all-fiber level-2 census for the e>=2 primes p=13,31 (d_f=d since
   f=2<=e): split fibers would refute below-base vanishing.
B: good-position check: for C mod p, C!=0, do the mod-p trace values
   have two consecutive positions with unique values? (Lemma hypothesis.)
"""
import hashlib
import numpy as np
from collections import defaultdict


def alpha_powers(mod, n):
    A = [(1, 0)]
    for _ in range(n):
        a, b = A[-1]
        A.append(((3 * a + 4 * b) % mod, (2 * a + 3 * b) % mod))
    return A


def ord_alpha(p):
    mod = p
    a, b = 1, 0
    for j in range(1, 5000):
        a, b = (3 * a + 4 * b) % mod, (2 * a + 3 * b) % mod
        if (a, b) == (1, 0):
            return j
    return None


def level2_census(p):
    mod = p * p
    d = ord_alpha(p)
    A = alpha_powers(mod, d)
    Aarr = np.array(A[:d], dtype=np.int64)
    nC = mod * mod
    hashes = []
    canons = []
    chunk = 50000
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
            x2, y2 = ca, (-cb) % mod
            upd = (x1 < ba) | ((x1 == ba) & (y1 < bb))
            ba = np.where(upd, x1, ba); bb = np.where(upd, y1, bb)
            upd2 = (x2 < ba) | ((x2 == ba) & (y2 < bb))
            ba = np.where(upd2, x2, ba); bb = np.where(upd2, y2, bb)
            ca, cb = (3 * ca + 4 * cb) % mod, (2 * ca + 3 * cb) % mod
        srt = np.sort(cyc, axis=1)
        for i in range(en - st):
            hashes.append(hashlib.blake2b(
                srt[i].tobytes(), digest_size=16).digest())
            canons.append((int(ba[i]), int(bb[i])))
    fib = defaultdict(set)
    for h, c in zip(hashes, canons):
        fib[h].add(c)
    split = [(h, s) for h, s in fib.items() if len(s) >= 2]
    print(f"p={p} level2: classes={nC} fibers={len(fib)} "
          f"split={len(split)}")
    for h, s in sorted(split, key=lambda x: -len(x[1]))[:10]:
        print(f"   SPLIT orbits={len(s)}")
    return split


def good_position_check(p):
    d = ord_alpha(p)
    mod = p
    A = alpha_powers(mod, d)
    Aarr = np.array(A[:d], dtype=np.int64)
    nC = mod * mod
    bad = []  # (a,b,pattern) with no two consecutive good positions
    nrep = 0
    chunk = 50000
    for st in range(0, nC, chunk):
        en = min(st + chunk, nC)
        idx = np.arange(st, en, dtype=np.int64)
        a = (idx // mod).astype(np.int64)
        b = (idx % mod).astype(np.int64)
        cyc = np.empty((en - st, d), dtype=np.int64)
        ca, cb = a.copy(), b.copy()
        for j in range(d):
            cyc[:, j] = (2 * ca) % mod
            ca, cb = (3 * ca + 4 * cb) % mod, (2 * ca + 3 * cb) % mod
        for i in range(en - st):
            if a[i] == 0 and b[i] == 0:
                continue
            vals, cnts = np.unique(cyc[i], return_counts=True)
            if np.all(cnts == 1):
                continue
            nrep += 1
            good = np.zeros(d, dtype=bool)
            for v, c in zip(vals, cnts):
                if c == 1:
                    good[np.where(cyc[i] == v)[0][0]] = True
            ok = any(good[j] and good[(j + 1) % d] for j in range(d))
            if not ok:
                bad.append((int(a[i]), int(b[i]),
                            tuple(int(x) for x in cyc[i])))
    print(f"p={p} d={d}: C!=0 with a repeat={nrep}, "
          f"no-two-consecutive-good={len(bad)}")
    for a, b, pat in bad[:5]:
        print(f"   C=({a},{b}) cycle={pat}")
    return bad


if __name__ == "__main__":
    for p in (13, 31):
        level2_census(p)
    for p in (13, 31):
        good_position_check(p)
