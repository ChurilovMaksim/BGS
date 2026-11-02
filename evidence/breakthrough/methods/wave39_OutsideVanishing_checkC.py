"""Wave 39 task 5, part C: (182,13) level-4 tower check via Full Blindness.
- M_4/M_3 grouping over C mod 13^2 (canonical lifts): genuine fibers
  must give identical partitions.
- Genuine split correspondence vs level-3 census (census_level).
- Orbit lifting: 169 lifts of one element per level-3 split fiber must
  fall into exactly 13 level-4 orbits, each reducing to that element's
  level-3 orbit.
- Degenerate groups: must equal 13*(level-3 split fiber mod 13).
"""
import sys, hashlib
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave36_tower import census_level

P = 13
MOD4 = P ** 4
MOD3 = P ** 3
MOD2 = P ** 2
D4 = 14 * P ** 2  # 2366
D3 = 14 * P      # 182


def alpha_powers(mod, n):
    A = [(1, 0)]
    for _ in range(n):
        a, b = A[-1]
        A.append(((3 * a + 4 * b) % mod, (2 * a + 3 * b) % mod))
    return A


def cycle_hashes(mod, d, classes):
    """classes: array of (a,b) mod MOD2 (canonical lifts). Returns list
    of blake2b hashes of sorted cycles mod `mod`."""
    Aarr = np.array(alpha_powers(mod, d)[:d], dtype=np.int64)
    out = []
    chunk = 4000
    for st in range(0, len(classes), chunk):
        cc = classes[st:st + chunk]
        a = cc[:, 0].astype(np.int64)
        b = cc[:, 1].astype(np.int64)
        cyc = np.empty((len(cc), d), dtype=np.int64)
        ca, cb = a.copy(), b.copy()
        for j in range(d):
            cyc[:, j] = (2 * ca) % mod
            ca, cb = (3 * ca + 4 * cb) % mod, (2 * ca + 3 * cb) % mod
        srt = np.sort(cyc, axis=1)
        for i in range(len(cc)):
            out.append(hashlib.blake2b(
                srt[i].tobytes(), digest_size=16).digest())
    return out


def orbit_canons_l4(lifts):
    """lifts: array of (a,b) mod MOD4. Returns list of level-4 orbit
    canons (lex-min over {C alpha^j, Cbar alpha^j})."""
    Aarr = np.array(alpha_powers(MOD4, D4)[:D4], dtype=np.int64)
    a = lifts[:, 0].astype(np.int64)
    b = lifts[:, 1].astype(np.int64)
    ca, cb = a.copy(), b.copy()
    ba, bb = a.copy(), b.copy()
    for j in range(D4):
        x1, y1 = ca, cb
        x2, y2 = ca, (-cb) % MOD4
        upd = (x1 < ba) | ((x1 == ba) & (y1 < bb))
        ba = np.where(upd, x1, ba); bb = np.where(upd, y1, bb)
        upd2 = (x2 < ba) | ((x2 == ba) & (y2 < bb))
        ba = np.where(upd2, x2, ba); bb = np.where(upd2, y2, bb)
        ca, cb = (3 * ca + 4 * cb) % MOD4, (2 * ca + 3 * cb) % MOD4
    return list(zip(ba.tolist(), bb.tolist()))


def main():
    print("== level-3 census (182,13) ==")
    lv3 = census_level(182, P, 3)
    print(f"mod={lv3['mod']} d={lv3['d']}")
    fib3 = defaultdict(list)   # hash -> indices
    for idx, h in enumerate(lv3['hashes']):
        fib3[h].append(idx)
    canon3 = {}
    for h, idxs in fib3.items():
        canon3[h] = {(int(lv3['ca'][i]), int(lv3['cb'][i])) for i in idxs}
    split3 = {h: canon3[h] for h in fib3 if len(canon3[h]) >= 2}
    sup3 = {}
    for h, idxs in fib3.items():
        s = [bool(lv3['sup'][i]) for i in idxs]
        sup3[h] = (all(s), any(s))
    onsup3 = {h: c for h, c in split3.items() if sup3[h][0]}
    mixed3 = [h for h in fib3 if sup3[h][1] and not sup3[h][0]]
    print(f"level3 fibers={len(fib3)} split={len(split3)} "
          f"on-support split={len(onsup3)} mixed={len(mixed3)}")

    print("== M4/M3 grouping over C mod 169 ==")
    classes = np.array([(a, b) for a in range(MOD2) for b in range(MOD2)],
                       dtype=np.int64)
    h4 = cycle_hashes(MOD4, D4, classes)
    h3 = cycle_hashes(MOD3, D3, classes)
    g4 = defaultdict(set)
    g3 = defaultdict(set)
    for i, (a, b) in enumerate(classes):
        g4[h4[i]].add((int(a), int(b)))
        g3[h3[i]].add((int(a), int(b)))
    # Genuine fibers contain no element divisible by 13 (fiber property);
    # restrict the partition comparison to non-divisible classes.
    # (Degenerate classes group by small-lift fibers instead, expected.)
    def is_degen_class(c):
        return c[0] % P == 0 and c[1] % P == 0
    s4 = {frozenset(v - {c for c in v if is_degen_class(c)})
          for v in g4.values()}
    s3 = {frozenset(v - {c for c in v if is_degen_class(c)})
          for v in g3.values()}
    s4.discard(frozenset())
    s3.discard(frozenset())
    print(f"M4 groups={len(g4)} M3 groups={len(g3)}; "
          f"non-divisible classes: M4 groups={len(s4)} "
          f"M3 groups={len(s3)} identical partitions: {s4 == s3}")
    if s4 != s3:
        print(f"  M4-only={len(s4 - s3)} M3-only={len(s3 - s4)}")

    print("== genuine split correspondence ==")
    # map each M4 group to a level-3 fiber via representative lift
    def idx3(a, b):
        return a * MOD3 + b
    grp_to_fib = {}
    for h, grp in g4.items():
        a, b = next(iter(grp))
        grp_to_fib[h] = lv3['hashes'][idx3(a, b)]
    fib_to_grp = defaultdict(list)
    for h, fh in grp_to_fib.items():
        fib_to_grp[fh].append(h)
    multi = {fh: v for fh, v in fib_to_grp.items() if len(v) > 1}
    print(f"groups mapping to >1 level-3 fiber per group: n/a; "
          f"level-3 fibers hit by >1 group: {len(multi)}")
    hit_split = [fh for fh in fib_to_grp if fh in split3]
    print(f"M4 groups hitting level-3 split fibers: {len(hit_split)} "
          f"of {len(split3)} level-3 split fibers")
    missed = [fh for fh in split3 if fh not in fib_to_grp]
    print(f"level-3 split fibers missed by M4 grouping: {len(missed)}")

    print("== orbit lifting (169 lifts per level-3 split fiber) ==")
    bad_count = []
    bad_red = []
    for fh, canons in onsup3.items():
        idxs = fib3[fh]
        x = idxs[0]
        xa, xb = x // MOD3, x % MOD3
        lifts = np.array(
            [(xa + MOD3 * ea, xb + MOD3 * eb)
             for ea in range(P) for eb in range(P)], dtype=np.int64)
        can4 = orbit_canons_l4(lifts)
        ncan = len(set(can4))
        if ncan != P:
            bad_count.append((fh, ncan))
        # reduction check: orbit of first canon reduces to O3(x)
        ca0, cb0 = can4[0]
        orb3 = set()
        Aarr = np.array(alpha_powers(MOD3, D3)[:D3], dtype=np.int64)
        ca, cb = ca0 % MOD3, cb0 % MOD3
        for j in range(D3):
            orb3.add((int(ca), int(cb)))
            orb3.add((int(ca), int((-cb) % MOD3)))
            ca, cb = (3 * ca + 4 * cb) % MOD3, (2 * ca + 3 * cb) % MOD3
        # O3(x): elements with same canon as x
        cx = (int(lv3['ca'][x]), int(lv3['cb'][x]))
        o3x = set()
        for i in idxs:
            if (int(lv3['ca'][i]), int(lv3['cb'][i])) == cx:
                o3x.add((i // MOD3, i % MOD3))
        if orb3 != o3x:
            bad_red.append(fh)
    print(f"on-support split fibers tested: {len(onsup3)}; "
          f"orbit-count != 13: {len(bad_count)} {bad_count[:5]}; "
          f"reduction mismatches: {len(bad_red)}")

    print("== degenerate fibers at level 3 (census) ==")
    def is_degen_fiber(h):
        ca, cb = next(iter(canon3[h]))
        return ca % P == 0 and cb % P == 0
    degen_split3 = [h for h in split3 if is_degen_fiber(h)]
    print(f"level-3 split fibers: {len(split3)}, of which degenerate: "
          f"{len(degen_split3)} (expect 0: level-2 splits = 0)")
    print("== sampled LT3 check at level 4 ==")
    # For sampled level-3 split fibers: 13*F3' must be a level-4 fiber
    # with matching orbit count (orbits 13*O, same count).
    Aarr4 = np.array(alpha_powers(MOD4, D4)[:D4], dtype=np.int64)
    sample = list(onsup3.items())[:20]
    bad_lt3 = []
    for fh, canons in sample:
        idxs = fib3[fh]
        by_canon = defaultdict(list)
        for i in idxs:
            by_canon[(int(lv3['ca'][i]), int(lv3['cb'][i]))].append(i)
        orbits = list(by_canon.values())
        if len(orbits) < 2:
            continue
        reps = [o[0] for o in orbits[:2]]
        l4canons = []
        m4hashes = []
        for r in reps:
            ra, rb = r // MOD3, r % MOD3
            ca, cb = (P * ra) % MOD4, (P * rb) % MOD4
            ba, bb = ca, cb
            cyc = []
            for j in range(D4):
                cyc.append((2 * ca) % MOD4)
                x2, y2 = ca, (-cb) % MOD4
                upd = (ca < ba) | ((ca == ba) & (cb < bb))
                ba, bb = (ca if upd else ba, cb if upd else bb)
                upd2 = (x2 < ba) | ((x2 == ba) & (y2 < bb))
                ba, bb = (x2 if upd2 else ba, y2 if upd2 else bb)
                ca, cb = (3 * ca + 4 * cb) % MOD4, (2 * ca + 3 * cb) % MOD4
            l4canons.append((int(ba), int(bb)))
            m4hashes.append(hashlib.blake2b(
                np.sort(np.array(cyc, dtype=np.int64)).tobytes(),
                digest_size=16).digest())
        if m4hashes[0] != m4hashes[1]:
            bad_lt3.append(("m4-mismatch",))
        if l4canons[0] == l4canons[1]:
            bad_lt3.append(("canon-collision",))
    print(f"sampled fibers: {len(sample)}, LT3 failures: {len(bad_lt3)} "
          f"{bad_lt3[:5]}")


if __name__ == "__main__":
    main()
