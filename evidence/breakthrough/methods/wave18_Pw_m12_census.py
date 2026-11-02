"""Wave 18, task 2: P_w census on support at m=12 (EXACT, no full enumeration).

Question: do (fiber,w)-classes coincide with Gamma-orbits on all of supp?
Gamma-orbit subset (fiber,w)-class subset fiber, so failure needs a split
fiber ( >1 Gamma-orbit ) whose orbits share the same sorted(w).

Method: Gamma_121-normalized representatives.
  - Global point = CRT tuple of component points (q = 128,81,25,49,121).
  - Every Gamma-orbit has a representative with 121-component equal to a
    fixed base point a_121 of its 121-fiber (diagonal action; 121-fibers
    are single orbits). So enumerating, per super-combo of component
    fibers (128 supported only; all others), all tuples (b_128, b_81,
    b_25, b_49) with 121-component fixed to a_121 covers one
    representative of EVERY orbit of EVERY fiber meeting support.
  - Fiber of a point = sorted global values = sorted column multiset M.
    Group representatives by (M, dihedral canon): distinct canons per M
    = number of Gamma-orbits in that fiber. Split fibers are M's with
    >= 2 canons. For each split fiber, sorted(w) per orbit decides P_w.
  - Support: global supp = AND of component supports (wave 16, exact
    factorization); component support is constant on component fibers
    (verified), and odd components are fully supported, so super-combos
    with 128-fibers supported cover exactly the fibers meeting support.
Total representatives: 8 * 81 * 25 * 49 * 11 = 8,731,800 (expected).
Repository untouched; no Lean build.
"""
import json
import sys

import numpy as np

sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 comp_supported, global_supported,
                                 gamma_perms, lex_canon, group_ids)

m = 12
D = Dm(m)
QS = [128, 81, 25, 49, 121]
Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
assert len(perms) == 24

# K_q CRT idempotents: global value = sum_q K_q * comp_q (mod D)
K = {}
for q in QS:
    dq = D // q
    K[q] = (dq * pow(dq % q, -1, q)) % D

# Component data: points, fiber ids, support mask; fibers as index lists
comp = {}
for q in QS:
    pts = snf_kernel(m, q)
    assert len(pts) == q
    fib = group_ids(np.sort(pts, axis=1))
    sup = comp_supported(pts, Z, Qmod, q)
    fibers = {}
    for f in range(int(fib.max()) + 1):
        idx = np.where(fib == f)[0]
        fibers[f] = idx
    comp[q] = {"pts": pts, "fib": fib, "sup": sup, "fibers": fibers}

supp_fibers_128 = sorted(set(comp[128]["fib"][comp[128]["sup"]].tolist()))
print(f"128 supported fibers: {supp_fibers_128}", flush=True)


def H_np(v):
    return 6 * v - np.roll(v, 1, axis=1) - np.roll(v, -1, axis=1)


total_delta = 0
total_fibers = 0
split_groups = []  # dicts: combo, M, orbits: [(rep, orbit_size, sorted_w)]
n_super = 0
for f128 in supp_fibers_128:
    I128 = comp[128]["fibers"][f128]
    P128 = comp[128]["pts"][I128]
    for f81, I81 in comp[81]["fibers"].items():
        P81 = comp[81]["pts"][I81]
        for f25, I25 in comp[25]["fibers"].items():
            P25 = comp[25]["pts"][I25]
            for f49, I49 in comp[49]["fibers"].items():
                P49 = comp[49]["pts"][I49]
                for f121, I121 in comp[121]["fibers"].items():
                    a121 = comp[121]["pts"][I121[0]]
                    B = (K[121] * a121) % D
                    n128, n81, n25, n49 = len(I128), len(I81), len(I25), len(I49)
                    N = n128 * n81 * n25 * n49
                    # multi-index decomposition
                    ii = np.arange(N, dtype=np.int64)
                    i49 = ii % n49; ii //= n49
                    i25 = ii % n25; ii //= n25
                    i81 = ii % n81; ii //= n81
                    i128 = ii
                    col = (B[None, :]
                           + K[128] * P128[i128]
                           + K[81] * P81[i81]
                           + K[25] * P25[i25]
                           + K[49] * P49[i49]) % D
                    total_delta += N
                    n_super += 1
                    scol = np.sort(col, axis=1)
                    canon = lex_canon(col, perms)
                    keys = np.concatenate([scol, canon], axis=1)
                    ukeys, inv = np.unique(keys, axis=0, return_inverse=True)
                    # distinct M's in this super-combo
                    mkeys, minv = np.unique(ukeys[:, :12], axis=0,
                                            return_inverse=True)
                    total_fibers += len(mkeys)
                    # orbits per M: count ukeys per M
                    cnts = np.bincount(minv, minlength=len(mkeys))
                    for mi in np.where(cnts >= 2)[0]:
                        # representative rows: first ukey row per orbit
                        orbit_rows = ukeys[minv == mi]
                        # recover one point per orbit: find a delta row
                        # whose (sorted, canon) equals this ukey row
                        orbits = []
                        for orow in orbit_rows:
                            # find first delta index with this key
                            match = np.where((keys == orow).all(axis=1))[0][0]
                            rep = col[match]
                            # orbit size via stabilizer bitmask
                            stab = sum(1 for p in perms
                                       if (rep[p] == rep).all())
                            assert 24 % stab == 0
                            w = H_np(rep[None, :])[0] // D
                            orbits.append({
                                "rep": rep.tolist(),
                                "orbit_size": 24 // stab,
                                "sorted_w": sorted(w.tolist()),
                            })
                        split_groups.append({
                            "combo": [int(f128), int(f81), int(f25),
                                      int(f49), int(f121)],
                            "M": mkeys[mi].tolist(),
                            "orbits": orbits,
                        })
                    if n_super % 5000 == 0:
                        print(f"  super-combos={n_super} delta={total_delta} "
                              f"fibers={total_fibers} "
                              f"split_groups={len(split_groups)}", flush=True)

print(f"DONE: super-combos={n_super} total_delta={total_delta} "
      f"(expected 8731800) total_fibers_meeting_support={total_fibers} "
      f"split_groups={len(split_groups)}", flush=True)

# Verdicts
n_pw_fail = 0
for g in split_groups:
    sws = [tuple(o["sorted_w"]) for o in g["orbits"]]
    g["pw_ok"] = len(set(sws)) == len(sws)
    g["fiber_size"] = sum(o["orbit_size"] for o in g["orbits"])
    if not g["pw_ok"]:
        n_pw_fail += 1
    # sanity: all representative points in support
    reps = np.array([o["rep"] for o in g["orbits"]], dtype=np.int64)
    assert bool(global_supported(reps, Z, Qmod, D).all()), \
        f"split group off support! {g['combo']}"
print(f"P_w-failing split fibers on support: {n_pw_fail} "
      f"out of {len(split_groups)} split fibers", flush=True)
for g in split_groups:
    print(f"  SPLIT combo={g['combo']} fiber_size={g['fiber_size']} "
          f"n_orbits={len(g['orbits'])} "
          f"orbit_sizes={[o['orbit_size'] for o in g['orbits']]} "
          f"pw_ok={g['pw_ok']}", flush=True)

with open("/home/hatch/workspace/bgs-breakthrough/methods/"
          "wave18_Pw_m12_census.json", "w") as fh:
    json.dump({"total_delta": int(total_delta),
               "total_fibers": int(total_fibers),
               "split_groups": split_groups,
               "n_pw_fail": int(n_pw_fail)}, fh, indent=1)
print("wrote wave18_Pw_m12_census.json", flush=True)
