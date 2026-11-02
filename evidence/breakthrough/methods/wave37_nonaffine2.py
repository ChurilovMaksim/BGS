"""Wave 37, task 5, stage 2: dissect the 2 exceptional fibers.

Loads stage-1 intermediates, identifies the 2 fibers with 5 affine
orbits each, and reports: member (i1,i2) structure, component orbits,
orbit contents (shifts? dihedral?), stabilizers, and what the 5
orbits have in common / what separates them.
"""
import numpy as np
from collections import Counter, defaultdict
import importlib.util

spec = importlib.util.spec_from_file_location(
    "w37", "/home/hatch/workspace/bgs-breakthrough/methods/wave37_nonaffine.py")
w37 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w37)

M, N1, N2 = 30, 625, 841
K1 = w37.kernel_mod_np(M, N1)
K2 = w37.kernel_mod_np(M, N2)
d = np.load("/tmp/w37_stage1.npz")
gfib, canon = d["gfib"], d["canon"]
can1, can2 = d["can1"], d["can2"]
f1id, f2id = d["f1id"], d["f2id"]
i1_all, i2_all = d["i1_all"], d["i2_all"]
N = N1 * N2

# the 2 multi-orbit fibers
uk, uk_counts = np.unique(np.stack([gfib, canon], axis=1), axis=0,
                           return_counts=True)
fib_orbits = defaultdict(list)
for (f_, _), s_ in zip(uk.tolist(), uk_counts.tolist()):
    fib_orbits[f_].append(s_)
multi = {f_: s for f_, s in fib_orbits.items() if len(s) > 1}
print("multi-orbit fibers:", multi, flush=True)

# rebuild PA/PB for stabilizer/orbit inspection
d1, d2 = w37.row_index_map(K1), w37.row_index_map(K2)
units = [u for u in range(M) if np.gcd(u, M) == 1]
PA, PB = [], []
for u in units:
    for c in range(M):
        perm = [(u * j + c) % M for j in range(M)]
        PA.append(np.array([d1.get(K1[i, perm].tobytes(), -1)
                            for i in range(N1)], dtype=np.int64))
        PB.append(np.array([d2.get(K2[i, perm].tobytes(), -1)
                            for i in range(N2)], dtype=np.int64))
PA = np.array(PA)
PB = np.array(PB)
map_names = [(u, c) for u in units for c in range(M)]
P = (K1[:, None, :].astype(np.int64) * N2 +
     K2[None, :, :].astype(np.int64)).astype(np.int32)

for f_ in sorted(multi):
    members = np.where(gfib == f_)[0]
    print(f"\n=== fiber {f_}: {len(members)} members, orbits "
          f"{sorted(multi[f_])}", flush=True)
    i1m, i2m = i1_all[members], i2_all[members]
    print("  distinct i1:", len(set(i1m.tolist())),
          "distinct i2:", len(set(i2m.tolist())), flush=True)
    print("  i1 values:", sorted(set(i1m.tolist())), flush=True)
    print("  i2 count dist:", Counter(Counter(i2m.tolist()).values()),
          flush=True)
    print("  F1 ids:", sorted(set(f1id[i1m].tolist())),
          "F2 ids:", sorted(set(f2id[i2m].tolist())), flush=True)
    print("  comp orbits can1:", sorted(set(can1[i1m].tolist())),
          "can2:", sorted(set(can2[i2m].tolist())), flush=True)
    # orbit partition of this fiber
    cm = canon[members]
    orbs = defaultdict(list)
    for pt, co in zip(members.tolist(), cm.tolist()):
        orbs[co].append(pt)
    print("  orbit reps:", sorted(orbs.keys()), flush=True)
    for rep, pts in sorted(orbs.items()):
        # valid maps and stabilizer for rep
        a1, a2 = rep // N2, rep % N2
        valid = []
        stab = []
        for k in range(len(PA)):
            p1, p2 = PA[k][a1], PB[k][a2]
            if p1 >= 0 and p2 >= 0:
                valid.append(map_names[k])
                if p1 == a1 and p2 == a2:
                    stab.append(map_names[k])
        print(f"  orbit rep {rep} (i1={a1}, i2={a2}) size {len(pts)}: "
              f"valid maps {len(valid)}, stabilizer {stab}", flush=True)
        print(f"    valid (u,c): {valid}", flush=True)
        # are orbit members shifts of rep? check row rotations
        base_row = P[rep // N2, rep % N2]
        shifts = set()
        for pt in pts:
            r = P[pt // N2, pt % N2]
            # find rotation offsets taking base_row to r
            offs = [s for s in range(M)
                    if np.array_equal(np.roll(base_row, -s), r)]
            shifts.update(offs)
        print(f"    rotation offsets present in orbit: {sorted(shifts)}",
              flush=True)
        # value multiset of rep row, and repeated values?
        vals, cnts = np.unique(base_row, return_counts=True)
        print(f"    rep row distinct values: {len(vals)}, max mult: "
              f"{cnts.max()}, row: {base_row.tolist()}", flush=True)
    # cross-orbit pairing structure: for each pair of orbits, is there a
    # fixed component-orbit correspondence? print (can1, can2) per orbit
    for rep, pts in sorted(orbs.items()):
        pairs = Counter()
        for pt in pts:
            pairs[(int(can1[pt // N2]), int(can2[pt % N2]))] += 1
        print(f"  orbit {rep}: (can1,can2) cells: {dict(pairs)}", flush=True)
