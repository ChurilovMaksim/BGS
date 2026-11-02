"""Wave 39, task 3: support-mixing and flip-support checks at m=32.
(1) Do fibers mix on/off-support points?
(2) For on-support nu=(1,0) y, is the odd-flip Phi(y) off-support?
    For on-support nu=(0,1) y, is the even-flip Psi(y) off-support?
(3) Torsion rows: odd-position sums (parity of sum over odd i).
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter, defaultdict
from wave16_d1a_targeted import Dm, torsion_data, group_ids
from wave36_2part import snf_kernel_i32


def period_of_row(y):
    m = len(y)
    for p in range(1, m + 1):
        if m % p == 0 and all(y[i] == y[i % p] for i in range(m)):
            return p
    return m


m, q = 32, 8192
pts = snf_kernel_i32(m, q)
D = Dm(m)
Z, Qmod = torsion_data(m, D)
print("Z shape:", Z.shape, "Qmod len:", len(Qmod))
print("Z rows (first 4 rows, first 16 entries):")
for r in range(min(4, len(Z))):
    print("  row", r, list(Z[r][:16]), "Qmod", int(Qmod[r]) % q)
Qm = np.array([qq % q for qq in Qmod], dtype=np.int64)
Z64 = Z.astype(np.int64)
sup = ((2 * Qm[None, :] - pts.astype(np.int64) @ Z64.T) % q == 0).all(axis=1)
fib = group_ids(np.sort(pts, axis=1))
fib_sup = defaultdict(lambda: [0, 0])
for i in range(len(pts)):
    fib_sup[int(fib[i])][0] += int(sup[i])
    fib_sup[int(fib[i])][1] += 1
mixed = [f for f in fib_sup if 0 < fib_sup[f][0] < fib_sup[f][1]]
print("\nfibers:", len(fib_sup), "mixed-support fibers:", len(mixed))
for f in mixed[:10]:
    print("  mixed fiber", f, fib_sup[f])

# (2) flip support
half = q // 2
idx = np.arange(m)
cnt = Counter()
for i in range(len(pts)):
    if not sup[i]:
        continue
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
        s = ((2 * Qm[None, :] - od.astype(np.int64) @ Z64.T) % q == 0).all()
        cnt[("nu10", "Phi_on_support", bool(s))] += 1
    elif nu == (0, 1):
        ev = y.copy(); ev[idx % 2 == 0] = (ev[idx % 2 == 0] + half) % q
        s = ((2 * Qm[None, :] - ev.astype(np.int64) @ Z64.T) % q == 0).all()
        cnt[("nu01", "Psi_on_support", bool(s))] += 1
print("\nflip-support for on-support points:", dict(cnt))

# (3) torsion row odd-position sums mod 2
print("\ntorsion row odd-position sums (sum over odd i, mod 2) and even sums:")
for r in range(len(Z)):
    z = Z[r].astype(np.int64)
    so = int(z[1::2].sum()) % 2
    se = int(z[0::2].sum()) % 2
    print(f"  row {r}: odd-sum%2={so} even-sum%2={se} pattern[:8]={list(z[:8])}")
