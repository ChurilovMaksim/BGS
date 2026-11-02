import sys, json
sys.path.insert(0, ".")
import numpy as np, sympy as sp
from collections import Counter
from wave16_d1a_targeted import Dm, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon

def lifts_of_point(y, m_hi, q_hi, q_lo):
    """All lifts of a level-(k-1) point y (length m_lo, mod q_lo) to level k:
    seeds (y0 + q_lo*a, y1 + q_lo*b), a,b in 0..3, kept if kernel point."""
    m_lo = len(y)
    out = []
    for a in range(4):
        for b in range(4):
            s = np.empty(m_hi, dtype=np.int64)
            s[0] = (int(y[0]) + q_lo * a) % q_hi
            s[1] = (int(y[1]) + q_lo * b) % q_hi
            for i in range(1, m_hi - 1):
                s[i + 1] = (6 * s[i] - s[i - 1]) % q_hi
            # kernel check: m_hi-periodic
            if s[0] == (6 * s[-1] - s[-2]) % q_hi and s[1] == (6 * s[0] - s[-1]) % q_hi:
                out.append(s)
    return out

def canon_of_seq(s, m, q):
    ba, bb = orbit_canon(np.array([[s[0], s[1]]], dtype=np.int64), m, q)
    return (int(ba[0]), int(bb[0]))

# --- m=64 fiber 5 (2-orbit, size 32): lifts to m=128
pts64 = snf_kernel_i32(64, 32768)
d64 = json.load(open("wave36_2part_m64.json"))
f5 = d64["fibers"][5]
print("m64 fiber5:", f5["size"], f5["n_orbits"], f5["orbit_sizes"])
# find a point of fiber 5: recompute fibers
fib64 = group_ids(np.sort(pts64, axis=1))
ba, bb = orbit_canon(pts64[:, :2].astype(np.int64), 64, 32768)
gam64 = group_ids(np.stack([ba, bb], axis=1))
own5 = {tuple(c) for c in f5["own_orbit_canons"]}
idx5 = [i for i in range(len(pts64)) if (int(ba[i]), int(bb[i])) in own5]
print("points in fiber5:", len(idx5))
y = pts64[idx5[0]]
print("rep sequence first 16:", y[:16].tolist())
print("period of rep:", next((p for p in [8, 16, 32, 64] if np.all(np.roll(y, -p) == y)), None))
lifts = lifts_of_point(y, 128, 131072, 32768)
print("n lifts:", len(lifts))
ms = Counter()
for s in lifts:
    ms[tuple(np.sort(s).tolist())] += 1
print("distinct lift multisets:", len(ms), "counts:", list(ms.values()))
# delta patterns of lifts
for s in lifts[:4]:
    d = ((s[:64] - y) // 32768) % 4
    print("  delta first 12:", d[:12].tolist(), "delta period:", next((p for p in [1,2,4,8,16,32,64] if np.all(np.roll(d, -p) == d)), None))
# --- m=32 fiber 0 (2-orbit, size 32): lifts to m=64
pts32 = snf_kernel_i32(32, 8192)
d32 = json.load(open("wave36_2part_m32.json"))
f0 = d32["fibers"][0]
ba32, bb32 = orbit_canon(pts32[:, :2].astype(np.int64), 32, 8192)
own0 = {tuple(c) for c in f0["own_orbit_canons"]}
idx0 = [i for i in range(len(pts32)) if (int(ba32[i]), int(bb32[i])) in own0]
y32 = pts32[idx0[0]]
print("m32 fiber0 rep first 16:", y32[:16].tolist(),
      "period:", next((p for p in [4, 8, 16, 32] if np.all(np.roll(y32, -p) == y32)), None))
lifts32 = lifts_of_point(y32, 64, 32768, 8192)
print("n lifts m32->m64:", len(lifts32))
ms32 = Counter(tuple(np.sort(s).tolist()) for s in lifts32)
print("distinct lift multisets:", len(ms32), "counts:", sorted(ms32.values(), reverse=True))
# orbit structure of lifts: do any two lifted orbits share a multiset?
canons = {}
for s in lifts32:
    canons.setdefault(canon_of_seq(s, 64, 32768), []).append(tuple(np.sort(s).tolist()))
print("lifted orbits:", len(canons), "orbit multiset counts:",
      Counter(len(set(v)) for v in canons.values()))
