"""Wave 39, task 3: structure of the extra orbits in a split fiber (m=32).
Take a period-32 split fiber with 8 orbits; print orbit representatives
and test relations between them:
  - same even/odd sub-multisets?
  - related by independent even/odd shifts?
  - related by quarter-flips (add Q/2 on positions = r mod 4)?
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import defaultdict
from wave16_d1a_targeted import group_ids
from wave36_2part import snf_kernel_i32, orbit_canon


def period_of_row(y):
    m = len(y)
    for p in range(1, m + 1):
        if m % p == 0 and all(y[i] == y[i % p] for i in range(m)):
            return p
    return m


m, q = 32, 8192
pts = snf_kernel_i32(m, q)
fib = group_ids(np.sort(pts, axis=1))
ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
gam = group_ids(np.stack([ba, bb], axis=1))
fib_orbits = defaultdict(set)
fib_members = defaultdict(list)
for i in range(len(pts)):
    fib_orbits[int(fib[i])].add(int(gam[i]))
    fib_members[int(fib[i])].append(i)

# find a period-32 split fiber with 8 orbits
target = None
for f in sorted(fib_orbits):
    if len(fib_orbits[f]) == 8:
        y0 = pts[fib_members[f][0]].astype(np.int64)
        if period_of_row(y0) == 32:
            target = f
            break
print("target fiber:", target)
members = fib_members[target]
# orbit representatives: first member of each orbit
reps = {}
for i in members:
    g = int(gam[i])
    if g not in reps:
        reps[g] = pts[i].astype(np.int64)
print("num orbits:", len(reps))
y = list(reps.values())[0]
print("base seq:", list(y))
for g, z in reps.items():
    print("orbit seed", (int(z[0]), int(z[1])), "seq[:8]", list(z[:8]))
# relation tests: for each pair of reps, check
#  (i) even sub-multiset equal? odd sub-multiset equal?
#  (ii) z even part == shift of y even part? (and odd part shift?)
print("\nrelations vs base:")
for g, z in reps.items():
    ev_y = sorted(int(v) for v in y[0::2])
    od_y = sorted(int(v) for v in y[1::2])
    ev_z = sorted(int(v) for v in z[0::2])
    od_z = sorted(int(v) for v in z[1::2])
    # shifts of even/odd subsequences (period 16 in k, but sequences 32-long)
    ev_y_seq = list(y[0::2])
    od_y_seq = list(y[1::2])
    ev_z_seq = list(z[0::2])
    od_z_seq = list(z[1::2])
    sev = None
    for s in range(16):
        if ev_z_seq == ev_y_seq[s:] + ev_y_seq[:s]:
            sev = s
            break
    sod = None
    for s in range(16):
        if od_z_seq == od_y_seq[s:] + od_y_seq[:s]:
            sod = s
            break
    print(f"  orbit seed=({int(z[0])},{int(z[1])}) evMulti={ev_z == ev_y} "
          f"odMulti={od_z == od_y} evShift={sev} odShift={sod}")
