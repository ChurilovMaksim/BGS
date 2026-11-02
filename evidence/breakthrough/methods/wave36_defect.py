import sys, json
sys.path.insert(0, ".")
import numpy as np
from wave16_d1a_targeted import Dm, torsion_data
from wave36_2part import snf_kernel_i32, orbit_canon
from wave36_lift import lifts_of_point

# m=64 fibers 0 (4-orbit, preimage unsupported) and 5 (2-orbit, preimage supported)
pts64 = snf_kernel_i32(64, 32768)
d64 = json.load(open("wave36_2part_m64.json"))
ba, bb = orbit_canon(pts64[:, :2].astype(np.int64), 64, 32768)
D128 = Dm(128); Z, Qmod = torsion_data(128, D128)
Qm = np.array([qq % 131072 for qq in Qmod], dtype=np.int64)
Z64 = Z.astype(np.int64)
for fi in (0, 5):
    f = d64["fibers"][fi]
    own = {tuple(c) for c in f["own_orbit_canons"]}
    idx = [i for i in range(len(pts64)) if (int(ba[i]), int(bb[i])) in own]
    y = pts64[idx[0]]
    lifts = lifts_of_point(y, 128, 131072, 32768)
    print(f"== m64 fiber {fi} (orbits={f['n_orbits']}, size={f['size']}): lifts={len(lifts)}")
    for s in lifts[:3]:
        dot = s.astype(np.int64) @ Z64.T
        defect = (2 * Qm[None, :] - dot) % 131072
        print("   defect vector (16 z's):", defect[0].tolist())
    # defect of the base point at m=64 (for comparison)
    D64 = Dm(64); Z64lo, Qmod64 = torsion_data(64, D64)
    Qm64 = np.array([qq % 32768 for qq in Qmod64], dtype=np.int64)
    dot = y.astype(np.int64) @ Z64lo.astype(np.int64).T
    print("   base defect at m=64:", ((2 * Qm64[None, :] - dot) % 32768)[0].tolist())
