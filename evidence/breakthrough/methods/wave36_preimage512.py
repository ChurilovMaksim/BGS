import sys, json
sys.path.insert(0, ".")
import numpy as np
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave36_lift import lifts_of_point

d = json.load(open("wave36_2part_m256.json"))
pts = snf_kernel_i32(256, 524288)
ba, bb = orbit_canon(pts[:, :2].astype(np.int64), 256, 524288)
D512 = Dm(512); Z, Qmod = torsion_data(512, D512)
Qm = np.array([qq % 2097152 for qq in Qmod], dtype=np.int64)
Z64 = Z.astype(np.int64)
print("== m=256 fibers -> preimage at m=512:")
for fi, f in enumerate(d["fibers"]):
    own = {tuple(c) for c in f["own_orbit_canons"]}
    idx = [i for i in range(len(pts)) if (int(ba[i]), int(bb[i])) in own]
    all_lifts = []
    for i in idx:
        all_lifts.extend(lifts_of_point(pts[i], 512, 2097152, 524288))
    arr = np.array(all_lifts, dtype=np.int64)
    ms = group_ids(np.sort(arr, axis=1))
    dots = arr[::max(1, len(arr)//8)].astype(np.int64) @ Z64.T
    sups = ((2 * Qm[None, :] - dots) % 2097152 == 0).all(axis=1)
    print(f"  fiber {fi} size={f['size']} orbits={f['n_orbits']} "
          f"preimage={len(arr)} distinct_multisets={len(set(ms.tolist()))} "
          f"supported={sups.sum()}/{len(sups)}")
