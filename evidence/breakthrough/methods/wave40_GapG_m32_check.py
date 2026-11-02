"""Wave 40, task 1: verify the computations behind wave40_GapG_m32.md.
1. M^32, M^16 mod 8192 values used in the note.
2. Parametrisation: kernel points are exactly (y0,y1) = (32t, 96t+256s).
3. nu=(1,0) at p=32 iff s,t odd.
4. Direct Gap G: odd sub-multiset never 4096-symmetric (all 2688 points).
"""
import numpy as np
import sympy as sp
from wave36_2part import snf_kernel_i32

M = sp.Matrix([[6, -1], [1, 0]])
M32 = (M**32).applyfunc(lambda x: int(x) % 8192)
M16 = (M**16).applyfunc(lambda x: int(x) % 8192)
assert M32.tolist() == [[2849, 416], [7776, 5345]], M32.tolist()
assert M16.tolist() == [[401, 208], [7984, 1649]], M16.tolist()
print("1. matrix values OK")

pts = snf_kernel_i32(32, 8192)
assert len(pts) == 8192
# parametrisation: every kernel point's seed (y0,y1) = (32t, 96t+256s)
param = set()
for t in range(256):
    for s in range(32):
        param.add((32 * t, (96 * t + 256 * s) % 8192))
seeds = set((int(r[0]), int(r[1])) for r in pts)
assert seeds == param, (len(seeds), len(param))
print("2. parametrisation OK (8192 points)")

q, half = 8192, 4096


def period_of_row(y):
    for p in range(1, 33):
        if 32 % p == 0 and all(y[i] == y[i % p] for i in range(32)):
            return p
    return 32


n_nu10 = n_sym = 0
st_odd_ok = True
for r in pts:
    y = r.astype(np.int64)
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
    n_nu10 += 1
    # direct Gap G: odd sub-multiset symmetry
    from collections import Counter
    O = Counter(int(y[i]) for i in range(1, p, 2))
    if all(O[(v + half) % q] == O[v] for v in O):
        n_sym += 1
    if p == 32:
        t = (int(y[0]) // 32) % 256
        s = ((int(y[1]) - 96 * t) // 256) % 32
        if not (s % 2 == 1 and t % 2 == 1):
            st_odd_ok = False
print("3. nu=(1,0) p=32 iff s,t odd:", st_odd_ok)
print("4. nu=(1,0) points:", n_nu10, "symmetric O:", n_sym)
assert n_nu10 == 2688 and n_sym == 0 and st_odd_ok
print("ALL CHECKS PASS")
