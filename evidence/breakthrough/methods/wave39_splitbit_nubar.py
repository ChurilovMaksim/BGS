"""Wave 39, task 3: verify the nu-bar lemma at m=32.
For each point with minimal period p>=8: ybar = y mod (Q/2) has minimal
period exactly p/2, and nu-bar (w.r.t. Q/2) equals nu (p>=16) or swap(nu)
(p=8). Also verify the quarter-defect formula.
"""
import sys
sys.path.insert(0, ".")
import numpy as np
from collections import Counter
from wave36_2part import snf_kernel_i32


def period_of_row(y):
    m = len(y)
    for p in range(1, m + 1):
        if m % p == 0 and all(y[i] == y[i % p] for i in range(m)):
            return p
    return m


m, q = 32, 8192
pts = snf_kernel_i32(m, q)
half = q // 2
cnt = Counter()
bad = []
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
    yb = y % half
    pb = period_of_row(yb)
    if pb != p // 2:
        bad.append((i, p, pb))
        continue
    # nu-bar w.r.t. modulus half: defect (Q/4)*nu-bar
    q4 = half // 2
    e0 = int(yb[pb // 2] - yb[0]) % half
    e1 = int(yb[pb // 2 + 1] - yb[1]) % half
    if e0 % q4 or e1 % q4:
        bad.append((i, p, "nubar-div", e0, e1))
        continue
    nub = ((e0 // q4) % 2, (e1 // q4) % 2)
    if p >= 16:
        cnt[("p>=16", "nubar==nu" if nub == nu else "OTHER")] += 1
    else:
        cnt[("p==8", "nubar==swap" if nub == (nu[1], nu[0]) else "OTHER")] += 1
    # quarter-defect formula: y[i+p/4] - y[i] == 2^{k-1} * nu_{i mod 2} (mod half)
    # for p>=16; swapped parity for p==8
    qd = half // 2  # 2^{k-1} with Q=2^{k+1}: half=2^k, qd=2^{k-1}
    ok = True
    for ii in range(p):
        diff = int(y[(ii + p // 4) % p] - y[ii]) % half
        if p >= 16:
            want = (qd * nu[ii % 2]) % half
        else:
            want = (qd * nu[(ii + 1) % 2]) % half
        if diff != want:
            ok = False
            break
    cnt[("quarter-defect", "ok" if ok else "FAIL")] += 1
print(dict(cnt))
print("bad:", len(bad), bad[:5])
