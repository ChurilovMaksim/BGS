import sys, json
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave36_lift import lifts_of_point

def check(m_lo, q_lo, m_hi, q_hi, jsonfile):
    d = json.load(open(jsonfile))
    pts = snf_kernel_i32(m_lo, q_lo)
    ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m_lo, q_lo)
    # support at hi level
    Dh = Dm(m_hi)
    Zh, Qmodh = torsion_data(m_hi, Dh)
    Qmh = np.array([qq % q_hi for qq in Qmodh], dtype=np.int64)
    Zh64 = Zh.astype(np.int64)
    print(f"== level {m_lo} -> {m_hi}:")
    for fi, f in enumerate(d["fibers"]):
        own = {tuple(c) for c in f["own_orbit_canons"]}
        idx = [i for i in range(len(pts)) if (int(ba[i]), int(bb[i])) in own]
        all_lifts = []
        for i in idx:
            all_lifts.extend(lifts_of_point(pts[i], m_hi, q_hi, q_lo))
        arr = np.array(all_lifts, dtype=np.int64)
        ms = group_ids(np.sort(arr, axis=1))
        # support of first lift point
        dot = arr[:1].astype(np.int64) @ Zh64.T
        sup = bool(((2 * Qmh[None, :] - dot) % q_hi == 0).all(axis=1)[0])
        # support constant on the preimage fiber? check a few points
        dots = arr[::max(1, len(arr)//8)].astype(np.int64) @ Zh64.T
        sups = ((2 * Qmh[None, :] - dots) % q_hi == 0).all(axis=1)
        print(f"  fiber {fi} size={f['size']} orbits={f['n_orbits']} "
              f"preimage={len(arr)} distinct_multisets={len(set(ms.tolist()))} "
              f"supported={sup} (sample {sups.sum()}/{len(sups)} supported)")

check(64, 32768, 128, 131072, "wave36_2part_m64.json")
check(128, 131072, 256, 524288, "wave36_2part_m128.json")
