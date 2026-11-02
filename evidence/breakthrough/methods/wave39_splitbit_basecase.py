"""Wave 39, task 3: period-4 base case, reduced mod 32 (k-independent).

Period-4 kernel sequences mod 2^{k+1}: y0 = 2^{k-4} U, y1 = 2^{k-4}(a+8t)
with U in Z/32, t in Z/4, a = (3U) mod 8. Reduced tuple (divide by 2^{k-4},
mod 32): r = (U, a+8t, 6a+16t-U, 3a+24t-6U) mod 32.
nu^(4) (census convention): nu0 = ((3a+8t-U)/8) mod 2,
nu1 = ((a+8t-3U)/8) mod 2.
Gamma-orbit of reduced tuple: rotations of r and rotations of (r0,r3,r2,r1).
Check: any two (U,t) with equal multiset and nu != (1,1) share an orbit.
Also report: nu=(1,1) tuples in split fibers (multiset shared, orbits >1)?
"""
from collections import defaultdict


def orbit_canon(r):
    rots = [tuple(r[(i + s) % 4] for i in range(4)) for s in range(4)]
    rev = [r[0], r[3], r[2], r[1]]
    rots += [tuple(rev[(i + s) % 4] for i in range(4)) for s in range(4)]
    return min(rots)


cases = {}
for U in range(32):
    a = (3 * U) % 8
    for t in range(4):
        r = (U % 32, (a + 8 * t) % 32, (6 * a + 16 * t - U) % 32,
             (3 * a + 24 * t - 6 * U) % 32)
        nu0 = ((3 * a + 8 * t - U) // 8) % 2
        nu1 = ((a + 8 * t - 3 * U) // 8) % 2
        assert (3 * a + 8 * t - U) % 8 == 0 and (a + 8 * t - 3 * U) % 8 == 0
        cases[(U, t)] = (r, (nu0, nu1))
print("cases:", len(cases))
by_multi = defaultdict(list)
for key, (r, nu) in cases.items():
    by_multi[tuple(sorted(r))].append((key, nu, orbit_canon(r)))
viol = []
split11 = []
for multi, lst in by_multi.items():
    orbits = {o for _, _, o in lst}
    nus = {nu for _, nu, _ in lst}
    if len(orbits) > 1:
        # split reduced fiber: check whether some member has nu != (1,1)
        bad = [x for x in lst if x[1] != (1, 1)]
        if bad:
            viol.append((multi, lst))
        if nus == {(1, 1)}:
            split11.append((multi, lst))
print("reduced fibers:", len(by_multi))
print("VIOLATIONS (split fiber containing nu!=(1,1)):", len(viol))
for v in viol[:10]:
    print("  ", v)
print("split reduced fibers with all nu=(1,1):", len(split11))
for multi, lst in split11[:10]:
    print("   multi", multi, "members", [(k, o) for k, _, o in lst])
# nu distribution
from collections import Counter
print("nu dist:", Counter(nu for _, nu in cases.values()))
# period breakdown: period exactly 4 vs dividing 2 vs 1 (reduced: period 2 iff
# r0==r2 and r1==r3; period 1 iff all equal)
per = Counter()
for (U, t), (r, nu) in cases.items():
    if r[0] == r[1] == r[2] == r[3]:
        per[1] += 1
    elif r[0] == r[2] and r[1] == r[3]:
        per[2] += 1
    else:
        per[4] += 1
print("reduced periods:", dict(per))
