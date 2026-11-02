import sys, json
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave36_lift import lifts_of_point

def analyze(m_lo, q_lo, m_hi, q_hi, fiber_idx, jsonfile):
    d = json.load(open(jsonfile))
    f = d["fibers"][fiber_idx]
    pts = snf_kernel_i32(m_lo, q_lo)
    ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m_lo, q_lo)
    own = {tuple(c) for c in f["own_orbit_canons"]}
    idx = [i for i in range(len(pts)) if (int(ba[i]), int(bb[i])) in own]
    print(f"== m={m_lo} fiber {fiber_idx}: size={f['size']} orbits={f['n_orbits']} "
          f"orbit_sizes={f['orbit_sizes']}")
    # reps of each orbit
    reps = {}
    for i in idx:
        reps.setdefault((int(ba[i]), int(bb[i])), pts[i])
    for oc, r in reps.items():
        per = next((p for p in [4, 8, 16, 32, 64] if p <= m_lo and np.all(np.roll(r, -p) == r)), m_lo)
        print(f"   orbit canon={oc} period={per} rep[:16]={r[:16].tolist()}")
    # preimage: all lifts of all points
    all_lifts = []
    for i in idx:
        all_lifts.extend(lifts_of_point(pts[i], m_hi, q_hi, q_lo))
    print(f"   preimage points: {len(all_lifts)} (expect {len(idx)*16})")
    arr = np.array(all_lifts, dtype=np.int64)
    ms = group_ids(np.sort(arr, axis=1))
    ba2, bb2 = orbit_canon(arr[:, :2], m_hi, q_hi)
    gam2 = group_ids(np.stack([ba2, bb2], axis=1))
    # per multiset: orbit count, size
    by_ms = defaultdict(set); sz_ms = Counter()
    for j in range(len(arr)):
        by_ms[int(ms[j])].add(int(gam2[j])); sz_ms[int(ms[j])] += 1
    print(f"   distinct lift multisets: {len(by_ms)}; "
          f"(size, n_orbits) per multiset: {sorted((sz_ms[k], len(v)) for k, v in by_ms.items())}")

analyze(64, 32768, 128, 131072, 5, "wave36_2part_m64.json")
analyze(32, 8192, 64, 32768, 0, "wave36_2part_m32.json")
