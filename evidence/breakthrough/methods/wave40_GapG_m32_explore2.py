"""Wave 40, task 1, step 2: structure of nu=(1,0) points at m=32.
Check: (a) p=8 swapped quarter-defect; (b) p=16 epsilon alternation and
bad-case analysis; (c) p=32 epsilon alternation and the bad case
(eps0=0 & u2=u0) or (eps0=1 & u3=u1)."""
from collections import Counter

import numpy as np
from wave36_2part import snf_kernel_i32

m, q = 32, 8192
half = q // 2
pts = snf_kernel_i32(m, q)


def period_of_row(y):
    for p in range(1, m + 1):
        if m % p == 0 and all(y[i] == y[i % p] for i in range(m)):
            return p
    return m


c8 = Counter()
c16 = Counter()
c32 = Counter()
for i in range(len(pts)):
    y = pts[i].astype(np.int64)
    p = period_of_row(y)
    if p < 8:
        continue
    d0 = int(y[p // 2] - y[0]) % q
    d1 = int(y[p // 2 + 1] - y[1]) % q
    if d0 % half or d1 % half:
        continue
    nu = ((d0 // half) % 2, (d1 // half) % 2)
    if nu != (1, 0):
        continue
    if p == 8:
        # swapped quarter defect: y3 - y1 should be 2048 mod 4096
        c8[("y3-y1 mod 4096", int(y[3] - y[1]) % 4096)] += 1
        c8[("w1-w0", int(y[3] - y[1]) % q)] += 1
    elif p == 16:
        # S=4: eps_k = (y_{2k+1+4} - y_{2k+1})/4096 for k=0,1
        e0 = (int(y[5]) - int(y[1])) % q // half
        e1 = (int(y[7]) - int(y[3])) % q // half
        # check these are 0/1 (i.e. diff in {0,4096})
        ok = (int(y[5]) - int(y[1])) % q in (0, half) and \
             (int(y[7]) - int(y[3])) % q in (0, half)
        c16[("eps", e0, e1, "ok", ok)] += 1
        u = [int(y[2 * k + 1]) % 4096 for k in range(4)]
        c16[("u2==u0", u[2] == u[0], "u3==u1", u[3] == u[1])] += 1
    elif p == 32:
        # S=8: eps_k = (y_{2k+1+8} - y_{2k+1})/4096 for k=0..3
        eps = []
        ok = True
        for k in range(4):
            d = (int(y[2 * k + 1 + 8]) - int(y[2 * k + 1])) % q
            if d not in (0, half):
                ok = False
            eps.append(d // half)
        c32[("eps", tuple(eps), "ok", ok)] += 1
        u = [int(y[2 * k + 1]) % 4096 for k in range(4)]
        bad = (eps[0] == 0 and u[2] == u[0]) or (eps[0] == 1 and u[3] == u[1])
        c32[("bad", bad, "u2==u0", u[2] == u[0], "u3==u1", u[3] == u[1],
             "eps0", eps[0])] += 1

print("p=8:", dict(c8))
print("p=16 eps:", {k: v for k, v in c16.items() if k[0] == "eps"})
print("p=16 u-eq:", {k: v for k, v in c16.items() if k[0] == "u2==u0"})
print("p=32 eps:", {k: v for k, v in c32.items() if k[0] == "eps"})
print("p=32 bad:", {k: v for k, v in c32.items() if k[0] == "bad"})
