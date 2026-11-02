"""Wave 43, task 2: refined p=512 structure at m=512 (chunked)."""
from math import gcd
import numpy as np
from collections import Counter

m = 512
Q = 8 * m * m
p = 512
j = 9
print("m=%d p=%d Q=%d" % (m, p, Q), flush=True)


def matmul(A, B):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0]) % Q, (A[0][0]*B[0][1]+A[0][1]*B[1][1]) % Q],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0]) % Q, (A[1][0]*B[0][1]+A[1][1]*B[1][1]) % Q]]


def matpow(M, n):
    R = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            R = matmul(M, R)
        M = matmul(M, M)
        n >>= 1
    return R


M = [[6, Q-1], [1, 0]]
Mpows = {0: [[1, 0], [0, 1]]}
cur = [[1, 0], [0, 1]]
for n in range(1, m + 2):
    cur = matmul(M, cur)
    Mpows[n] = cur


def kernel_points(pp):
    Mp = matpow(M, pp)
    a = (Mp[0][0] - 1) % Q
    b = Mp[0][1] % Q
    c = Mp[1][0] % Q
    d = (Mp[1][1] - 1) % Q
    y0 = np.arange(Q, dtype=np.int64)
    rhs = (-b * y0) % Q
    g = gcd(a, Q)
    valid = (rhs % g == 0)
    y0v = y0[valid]
    rhsv = rhs[valid]
    a1 = a // g
    Q1 = Q // g
    inv = pow(a1, -1, Q1) if Q1 > 1 else 0
    y1_0 = ((inv * (rhsv // g)) % Q1) if Q1 > 1 else np.zeros_like(y0v)
    pts0, pts1 = [], []
    for k in range(g):
        y1 = y1_0 + k * Q1
        ok = (c * y1 + d * y0v) % Q == 0
        pts0.append(y0v[ok])
        pts1.append(y1[ok])
    return np.concatenate(pts0), np.concatenate(pts1)


y0, y1 = kernel_points(p)
Mp2 = matpow(M, p // 2)
yhalf0 = (Mp2[1][0] * y1 + Mp2[1][1] * y0) % Q
yhalf1 = (Mp2[0][0] * y1 + Mp2[0][1] * y0) % Q
minper = (yhalf0 != y0) | (yhalf1 != y1)
d0 = (yhalf0 - y0) % Q
d1 = (yhalf1 - y1) % Q
div = (d0 % (Q // 2) == 0) & (d1 % (Q // 2) == 0)
nu0 = (d0 // (Q // 2)) % 2
nu1 = (d1 // (Q // 2)) % 2
sel = minper & div & (nu0 == 1) & (nu1 == 0)
y0s, y1s = y0[sel], y1[sel]
npts = len(y0s)
print("nu10=%d" % npts, flush=True)
q8 = p // 8
p16 = p // 16
# parametrisation: y0 = (Q/8p) t, y1 = a (Q/8p) t + (Q/p) s
step0 = Q // (8 * p)
step1 = Q // p
print("y0 mult of step0: %s, t odd: %s" % (bool(np.all(y0s % step0 == 0)),
      bool(np.all((y0s // step0) % 2 == 1))), flush=True)
print("a mod 8 dist: %s" % Counter(((y1s % step1) // step0 % 8).tolist()), flush=True)
op2bad = 0
op3p8pat = Counter()
classpat = Counter()
CH = 65536
for st in range(0, npts, CH):
    y0c, y1c = y0s[st:st + CH], y1s[st:st + CH]
    wcols = []
    for k in range(p // 4):
        Mn = Mpows[2 * k + 1]
        wcols.append((Mn[1][0] * y1c + Mn[1][1] * y0c) % Q)
    W = np.stack(wcols, axis=1)
    v = W % (Q // 2)
    t = W // (Q // 2)
    f = (W[:, p16:p16 + q8] - W[:, :q8]) % Q
    phi = (f // (Q // 4)) % 4
    eps = ((W[:, q8:2 * q8] - W[:, :q8]) % Q) // (Q // 2)
    # Op^(2): shift 4, modulus Q/2^{j-4} = Q/32
    mod2 = Q // (2 ** (j - 4))
    dd4 = (W[:, 4:4 + q8] - W[:, :q8]) % Q
    assert np.all(dd4 % mod2 == 0)
    op2 = (dd4 // mod2) % 4
    if not np.all(op2 == (phi + 2) % 4):
        op2bad += len(y0c)
    # Op3': shift 8, modulus Q/16, values mod 8
    dd8 = (W[:, 8:8 + q8] - W[:, :q8]) % Q
    assert np.all(dd8 % (Q // 16) == 0)
    op3p = (dd8 // (Q // 16)) % 8
    for r in range(len(y0c)):
        f0 = [jj for jj in range(p16) if eps[r, jj] == 0 and phi[r, jj] == 0]
        op3p8pat[tuple(op3p[r, jj] for jj in f0)] += 1
        groups = {}
        for jj in f0:
            groups.setdefault(v[r, jj], []).append(jj)
        classpat[tuple(sorted(len(g) for g in groups.values()))] += 1
    print("  chunk %d done" % st, flush=True)
print("Op^(2)==phi+2 violations: %d" % op2bad)
print("Op3' mod 8 at f0 reps (top): %s" % op3p8pat.most_common(6))
print("f0 class-size patterns: %s" % classpat.most_common(6))
print("DONE")
