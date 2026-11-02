"""Wave 47, task 10, script D: level-parametric checks (no full census).

1. NEW at levels j = 5..10: the 10 fully-colliding source Y-types are
   fixed (wave38 c2, script C). The level-j source point is
   y_i = (Q_j/32) * Y_{i mod 4}, Q_j = 2^(2j+3), length N = 2^j.
   Lift it to level j+1 (16 candidates) and record lift periods and
   lift Gamma-orbit counts. Expect (q=4 -> p'=16, 4 orbits),
   (q<=2 -> p'=8, 2 orbits) at every level.

2. OLD step 256 -> 512: for one canon seed per m=256 on-support split
   fiber (wave36 JSON), lift to level 512 and record lift periods and
   lift orbit counts. Expect p' = 4p, 4 orbits per point.
"""
import sys
sys.path.insert(0, ".")
import json
import numpy as np
from wave36_2part import orbit_canon
from wave38_helpers import period_of, lifts_of_point

SOURCES = [
    ((0, 8, 16, 24), 4), ((2, 14, 18, 30), 4), ((6, 26, 22, 10), 4),
    ((4, 20, 20, 4), 4), ((12, 12, 28, 28), 4),
    ((0, 16, 0, 16), 2), ((4, 28, 4, 28), 2), ((12, 20, 12, 20), 2),
    ((8, 8, 8, 8), 1), ((24, 24, 24, 24), 1),
]

print("== NEW, levels j=5..10 (parametric construction)")
for j in range(5, 11):
    N, Q = 2**j, 2**(2*j + 3)
    unit = Q // 32
    rows = []
    for Yt, q in SOURCES:
        base = np.array([unit * Yt[i % 4] for i in range(N)], dtype=np.int64)
        lifts = lifts_of_point(base, 2 * N, 4 * Q, Q)
        assert len(lifts) == 16, (j, Yt, len(lifts))
        lpers = sorted({period_of(lft) for lft in lifts})
        seeds_hi = np.array([lft[:2] for lft in lifts], dtype=np.int64)
        ca, cb = orbit_canon(seeds_hi, 2 * N, 4 * Q)
        lorbs = len({(int(a), int(b)) for a, b in zip(ca, cb)})
        rows.append((q, tuple(lpers), lorbs))
    ok = all((q == 4 and lp == (16,) and lo == 4) or
             (q <= 2 and lp == (8,) and lo == 2)
             for q, lp, lo in rows)
    print(f"   j={j} m={N}: NEW profile as predicted: {ok}; "
          f"rows={sorted(set(rows))}")

print("== OLD step 256 -> 512 (one canon seed per m=256 fiber)")
d = json.load(open("wave36_2part_m256.json"))
q256 = d["q2"]


def seq_from_seed(a, b, m, q):
    y = [a % q, b % q]
    for i in range(1, m - 1):
        y.append((6*y[i] - y[i-1]) % q)
    return np.array(y, dtype=np.int64)


def period_of_np(y):
    m = len(y)
    p = 1
    while p <= m:
        if np.all(y == np.roll(y, -p)):
            return p
        p *= 2
    return None


allok = True
for f in d["fibers"]:
    a, b = f["own_orbit_canons"][0]
    y = seq_from_seed(a, b, 256, q256)
    p = period_of_np(y)
    lifts = lifts_of_point(y, 512, 4 * q256, q256)
    lpers = sorted({period_of(lft) for lft in lifts})
    seeds_hi = np.array([lft[:2] for lft in lifts], dtype=np.int64)
    ca, cb = orbit_canon(seeds_hi, 512, 4 * q256)
    lorbs = len({(int(x), int(z)) for x, z in zip(ca, cb)})
    ok = (lpers == [4 * p] and lorbs == 4)
    allok &= ok
    print(f"   fiber o={f['n_orbits']} p={p} -> lift periods={lpers} "
          f"lift orbits={lorbs} (expect {[4*p]}, 4): {ok}")
print("   OLD step 256->512 all OK:", allok)
