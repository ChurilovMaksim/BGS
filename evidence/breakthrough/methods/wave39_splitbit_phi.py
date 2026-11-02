"""Wave 39, task 3: is Phi(y) ever in Gamma(y) for nu=(1,0) points (m=32)?
(If never, then since F(y) is a single orbit, Phi(y) is not in F(y),
i.e. the odd sub-multiset is never Q/2-symmetric -- confirmed directly too.)
Also: Psi(y) in Gamma(y) for nu=(0,1)? (expect: never, by symmetry)
And direct: Phi(y) multiset == y multiset? (expect: never for nu=(1,0))
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter
from wave36_2part import snf_kernel_i32, orbit_canon
from wave16_d1a_targeted import group_ids


def period_of_row(y):
    m = len(y)
    for p in range(1, m + 1):
        if m % p == 0 and all(y[i] == y[i % p] for i in range(m)):
            return p
    return m


m, q = 32, 8192
pts = snf_kernel_i32(m, q)
ba, bb = orbit_canon(pts[:, :2].astype(np.int64), m, q)
gam = group_ids(np.stack([ba, bb], axis=1))
fib = group_ids(np.sort(pts, axis=1))
seed_to_idx = {(int(pts[i, 0]), int(pts[i, 1])): i for i in range(len(pts))}
half = q // 2
idx = np.arange(m)
cnt = Counter()
for i in range(len(pts)):
    y = pts[i].astype(np.int64)
    p = period_of_row(y)
    if p < 8 or p % 2:
        continue
    d0 = int(y[p // 2] - y[0]) % q
    d1 = int(y[p // 2 + 1] - y[1]) % q
    if d0 % half or d1 % half:
        continue
    nu = ((d0 // half) % 2, (d1 // half) % 2)
    if nu == (1, 0):
        od = y.copy(); od[idx % 2 == 1] = (od[idx % 2 == 1] + half) % q
        j = seed_to_idx.get((int(od[0]), int(od[1])))
        in_orbit = (j is not None and int(gam[j]) == int(gam[i]))
        in_fiber = (j is not None and int(fib[j]) == int(fib[i]))
        cnt[("nu10", "Phi_in_orbit", in_orbit)] += 1
        cnt[("nu10", "Phi_in_fiber", in_fiber)] += 1
    elif nu == (0, 1):
        ev = y.copy(); ev[idx % 2 == 0] = (ev[idx % 2 == 0] + half) % q
        j = seed_to_idx.get((int(ev[0]), int(ev[1])))
        in_orbit = (j is not None and int(gam[j]) == int(gam[i]))
        in_fiber = (j is not None and int(fib[j]) == int(fib[i]))
        cnt[("nu01", "Psi_in_orbit", in_orbit)] += 1
        cnt[("nu01", "Psi_in_fiber", in_fiber)] += 1
print(dict(cnt))
