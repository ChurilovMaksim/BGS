"""Wave 40, task 1, step 3: mod-64 / mod-128 structure of nu=(1,0) points,
and the e-sequence bit alternation used in the proof."""
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


c = Counter()
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
    # odd entries mod 64 / mod 128
    odd = [int(y[j]) for j in range(1, p, 2)]
    c[("p", p, "odd mod 64 set", tuple(sorted(set(v % 64 for v in odd))))] += 1
    c[("p", p, "odd mod 128 set size", len(set(v % 128 for v in odd)))] += 1
    # even entries mod 64
    ev = [int(y[j]) for j in range(0, p, 2)]
    c[("p", p, "even mod 64 set", tuple(sorted(set(v % 64 for v in ev))))] += 1
    if p == 32:
        # e-sequence: e_i = y_{i+4} - y_i; check e_odd = 0 mod 2048,
        # e_even = 1024 mod 2048, and f alternation at even positions
        e = [(int(y[(j + 4) % p]) - int(y[j])) % q for j in range(p)]
        ok_odd = all(v % 2048 == 0 for j, v in enumerate(e) if j % 2 == 1)
        ok_ev = all(v % 2048 == 1024 for j, v in enumerate(e) if j % 2 == 0)
        f = [(v // 1024) % 8 for v in e]
        # f at even positions alternates 1<->3 mod 4?
        alt = all((f[j] % 4) != (f[j + 2] % 4) for j in range(0, p - 2, 2))
        c[("p32 e-check", ok_odd, ok_ev, alt)] += 1
        # a,b bits: e2 = 1024 + 2048a (mod 4096), e4 likewise
        a = ((e[2] % 4096) - 1024) // 2048
        b = ((e[4] % 4096) - 1024) // 2048
        c[("p32 a!=b", a != b)] += 1

for k in sorted(c, key=str):
    print(k, c[k])
