"""Wave 37, task 5, stage 4: scaling action on the 5 orbits, and
stabilizer sizes for all 300 members of the exceptional fibers.
"""
import numpy as np
from collections import defaultdict
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
i1_all, i2_all = d["i1_all"], d["i2_all"]
d1 = w37.row_index_map(K1)

# PA/PB for stabilizer sizes
d2 = w37.row_index_map(K2)
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

for f_ in (45, 186):
    members = np.where(gfib == f_)[0]
    # stabilizer size per member
    stabs = []
    for pt in members.tolist():
        a1, a2 = pt // N2, pt % N2
        stabs.append(int(((PA[:, a1] == a1) & (PB[:, a2] == a2)).sum()))
    print(f"fiber {f_}: stabilizer sizes over members: "
          f"{sorted(set(stabs))} (all 2: {all(s == 2 for s in stabs)})",
          flush=True)
    # scaling action of U_S = {u mod 25: u mod 5 in {1,4}} on orbits
    cm = canon[members]
    orbs = defaultdict(list)
    for pt, co in zip(members.tolist(), cm.tolist()):
        orbs[co].append(pt)
    reps = sorted(orbs.keys())
    rep_of = {}
    for rep, pts in orbs.items():
        for pt in pts:
            rep_of[pt] = rep
    U_S = [u for u in range(1, 25) if np.gcd(u, 25) == 1
           and u % 5 in (1, 4)]
    print(f"  U_S = {U_S}", flush=True)
    for rep in reps:
        a1 = rep // N2
        row = {}
        for u in U_S:
            scaled = (u * K1[a1]) % 625
            i1p = d1.get(scaled.tobytes(), -1)
            assert i1p >= 0, "scaled row not a kernel row!"
            ptp = i1p * N2 + 0
            assert gfib[ptp] == f_, "scaling left the fiber!"
            row[u] = rep_of[ptp]
        print(f"  orbit {rep}: scaling action {row}", flush=True)
