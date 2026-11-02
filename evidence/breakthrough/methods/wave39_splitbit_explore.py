"""Wave 39, task 3: mechanism exploration at m=32.
(a) split fibers: orbit counts, periods, nu values; where do the 4 flips land?
(b) lift classification: kernel points reducing to y mod Q/2 == exactly
    {y, even-flip, odd-flip, both-flip}?
(c) parity/mod-4 separation of even/odd positions for nu!=(1,1) points.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon


def period_of_row(y):
    m = len(y)
    for p in range(1, m + 1):
        if m % p == 0 and all(y[i] == y[i % p] for i in range(m)):
            return p
    return m


m, q = 32, 8192
pts = snf_kernel_i32(m, q)
D = Dm(m)
Z, Qmod = torsion_data(m, D)
Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
sup = ((2 * Qm[None, :] - pts.astype(np.int64) @ Z.astype(np.int64).T) % q == 0).all(axis=1)
fib = group_ids(np.sort(pts, axis=1))
ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
gam = group_ids(np.stack([ba, bb], axis=1))
fib_orbits = defaultdict(set)
for i in range(len(pts)):
    fib_orbits[int(fib[i])].add(int(gam[i]))
split_ids = {f for f in fib_orbits if len(fib_orbits[f]) > 1}
print("split fibers:", len(split_ids),
      "orbit-count dist:", Counter(len(fib_orbits[f]) for f in split_ids))

# index points by seed for flip lookup
seed_to_idx = {}
for i in range(len(pts)):
    seed_to_idx[(int(pts[i, 0]), int(pts[i, 1]))] = i


def flips(y):
    """y as np array length m; returns dict name->sequence (length m)."""
    half = q // 2
    idx = np.arange(m)
    ev = y.copy(); ev[idx % 2 == 0] = (ev[idx % 2 == 0] + half) % q
    od = y.copy(); od[idx % 2 == 1] = (od[idx % 2 == 1] + half) % q
    bo = y.copy(); bo[:] = (bo + half) % q
    return {"even": ev, "odd": od, "both": bo}


# (a) for each split fiber, pick a point, locate its flips' orbits
print("\n(a) split fibers: flip landing (orbit id relative: 0=same orbit as y)")
for f in sorted(split_ids)[:15]:
    members = [i for i in range(len(pts)) if fib[i] == f]
    y = pts[members[0]].astype(np.int64)
    yorb = int(gam[members[0]])
    p = period_of_row(y)
    fl = flips(y)
    land = {}
    for name, z in fl.items():
        # z is a kernel sequence? find a point with this sequence (seed = z[:2])
        j = seed_to_idx.get((int(z[0]), int(z[1])))
        if j is None:
            land[name] = "NOT-A-POINT"
        else:
            # verify full sequence matches
            ok = np.array_equal(pts[j].astype(np.int64), z)
            land[name] = ("same-orbit" if int(gam[j]) == yorb else "other-orbit") + ("" if ok else "?SEQ")
    print(f"  fiber {f} size={len(members)} period={p} orbits={len(fib_orbits[f])} flips={land}")

# (b) lift classification for a sample of points (all periods>=8)
print("\n(b) lift classification: #kernel points reducing to y mod Q/2")
half = q // 2
red_to_pts = defaultdict(list)
for i in range(len(pts)):
    key = tuple(int(v) % half for v in pts[i])
    red_to_pts[key].append(i)
bad = 0
for i in range(len(pts)):
    y = pts[i].astype(np.int64)
    p = period_of_row(y)
    if p < 8:
        continue
    key = tuple(int(v) % half for v in y)
    cands = red_to_pts[key]
    fl = flips(y)
    fl_seeds = {(int(y[0]), int(y[1]))}
    for z in fl.values():
        fl_seeds.add((int(z[0]), int(z[1])))
    cand_seeds = {(int(pts[j, 0]), int(pts[j, 1])) for j in cands}
    if cand_seeds != fl_seeds:
        bad += 1
        if bad <= 5:
            print("   MISMATCH point", i, "period", p, "cands", len(cands), "flips", len(fl_seeds))
print("  points p>=8 with lift-set != 4 flips:", bad)

# (c) separation: y0 mod 2 vs y1 mod 2; mod-4 even/odd value sets
print("\n(c) separation stats for nu!=(1,1), p>=8 points")
nu_cache = {}
for i in range(len(pts)):
    y = pts[i].astype(np.int64)
    p = period_of_row(y)
    if p < 8 or p % 2:
        continue
    d0 = int(y[p // 2] - y[0]) % q
    d1 = int(y[p // 2 + 1] - y[1]) % q
    nu = ((d0 // half) % 2, (d1 // half) % 2) if d0 % half == 0 and d1 % half == 0 else None
    nu_cache[i] = nu
cnt = Counter()
for i, nu in nu_cache.items():
    if nu in ((1, 0), (0, 1)):
        y = pts[i].astype(np.int64)
        p = period_of_row(y)
        ev4 = {int(v) % 4 for v in y[:p:2]}
        od4 = {int(v) % 4 for v in y[1:p:2]}
        cnt[("parity_sep", int(y[0]) % 2 != int(y[1]) % 2)] += 1
        cnt[("mod4_disjoint", ev4.isdisjoint(od4))] += 1
        cnt[("mod4_ev", tuple(sorted(ev4)), "od", tuple(sorted(od4)))] += 0  # placeholder
print("  parity separation (y0%2 != y1%2):", cnt[("parity_sep", True)], "vs not:",
      cnt[("parity_sep", False)])
print("  mod-4 even/odd value sets disjoint:", cnt[("mod4_disjoint", True)], "vs not:",
      cnt[("mod4_disjoint", False)])
# distribution of mod-4 patterns for nu!=(1,1)
pat = Counter()
for i, nu in nu_cache.items():
    if nu in ((1, 0), (0, 1)):
        y = pts[i].astype(np.int64)
        p = period_of_row(y)
        ev4 = tuple(sorted({int(v) % 4 for v in y[:p:2]}))
        od4 = tuple(sorted({int(v) % 4 for v in y[1:p:2]}))
        pat[(ev4, od4)] += 1
print("  mod-4 (ev,od) patterns:", dict(pat))
