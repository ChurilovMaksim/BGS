"""Wave 38 (c): period<=4 points scaling, e-image, collision stability.

1. Period<=4 kernel points at level j are (Q/32)*Y for fixed Y mod 32 (SNF).
2. Support condition for them: sum_r Y_r z_r = 0 mod 4 (j=5), mod 2 (j=6),
   automatic (j>=7). Check all Y satisfy it.
3. e in image(L|4-periodic): e_0==e_2, e_1==e_3 (mod 2), alternating sum 0 mod 4.
4. Full-collision per Y-orbit, compared across levels j=5,6,7 (sources at
   m=32,64,128): same Y-types collide?
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32, orbit_canon
from wave38_helpers import period_of, lifts_of_point


def z_patterns(m):
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
    pats = []
    for r in range(Z.shape[0]):
        pat = tuple(int(Z[r, i]) for i in range(4))
        pats.append(pat)
    return pats


def period_le4_points(m, q):
    pts = snf_kernel_i32(m, q)
    out = []
    for y in pts:
        if period_of(y) <= 4:
            out.append(y)
    return np.array(out)


for m, q in [(32, 8192), (64, 32768)]:
    pts4 = period_le4_points(m, q)
    print(f"== m={m} q={q}: period<=4 points: {len(pts4)}")
    # scaling: all values divisible by q//32?
    assert np.all(pts4 % (q // 32) == 0), "not all divisible by Q/32"
    Y = (pts4[:, :4] // (q // 32)) % 32
    Yset = {tuple(row.tolist()) for row in Y}
    print(f"   distinct Y (first 4 values mod 32): {len(Yset)}")
    if m == 32:
        Y32 = Yset
    else:
        print(f"   Y-set == m=32 Y-set: {Yset == Y32}")
    # support condition: sum_r Y_r z_r mod 4 / mod 2
    pats = z_patterns(m)
    bad4, bad2 = 0, 0
    for yy in Yset:
        for pat in pats:
            s = sum(yy[r] * pat[r] for r in range(4))
            if s % 4 != 0:
                bad4 += 1
            if s % 2 != 0:
                bad2 += 1
    print(f"   support violations: mod4: {bad4} (of {len(Yset)*16}), mod2: {bad2}")
    # e for period<=4 points: e_i = (Y_{i+1}-6Y_i+Y_{i-1})/32 mod 4 (j-independent?)
    # compute e from actual y (mod q) and from Y (mod 32), compare
    e_img_fail = 0
    for y in pts4[:200]:
        yy = y.astype(np.int64)
        num = np.roll(yy, -1) - 6 * yy + np.roll(yy, 1)
        e = (num // q) % 4
        # e should be 4-periodic (period<=4 point)
        assert np.all(e == np.tile(e[:4], m // 4)), "e not 4-periodic"
        e4 = e[:4]
        # image(L|4-per) conditions: e0==e2, e1==e3 mod 2; e0-e1+e2-e3 == 0 mod 4
        if not (e4[0] % 2 == e4[2] % 2 and e4[1] % 2 == e4[3] % 2
                and (e4[0] - e4[1] + e4[2] - e4[3]) % 4 == 0):
            e_img_fail += 1
    print(f"   e-image failures (first 200 pts): {e_img_fail}")
