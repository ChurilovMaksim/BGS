"""Wave 43, task 2 exploration part 3: 2B-A at phi=0 classes, t-signs, Op^(3) mod 8."""
import sys
from math import gcd
import numpy as np
from collections import Counter

m = 256
Q = 8 * m * m


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


def kernel_points(p):
    Mp = matpow(M, p)
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


for p in (128, 256):
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
    wcols = []
    for k in range(p // 4):
        Mn = Mpows[2 * k + 1]
        wcols.append((Mn[1][0] * y1s + Mn[1][1] * y0s) % Q)
    W = np.stack(wcols, axis=1)
    q8 = p // 8
    p16 = p // 16
    v = W % (Q // 2)
    t = W // (Q // 2)
    f = (W[:, p16:p16 + q8] - W[:, :q8]) % Q
    phi = (f // (Q // 4)) % 4
    eps = ((W[:, q8:2 * q8] - W[:, :q8]) % Q) // (Q // 2)
    # Op^(3): shift 8 in w, modulus Q/8; also mod 8 version
    dd8 = (W[:, 8:8 + q8] - W[:, :q8]) % Q
    op3mod4 = (dd8 // (Q // 8)) % 4
    op3mod8 = (dd8 // (Q // 8)) % 8
    twoBA = Counter()
    tpat = Counter()
    op3pat = Counter()
    bad = 0
    for r in range(npts):
        f0 = [jj for jj in range(p16) if eps[r, jj] == 0 and phi[r, jj] == 0]
        # group f0 by class
        groups = {}
        for jj in f0:
            groups.setdefault(v[r, jj], []).append(jj)
        for c, members in groups.items():
            A = sum(1 for k in range(q8) if v[r, k] == c and eps[r, k] == 0)
            B = sum(1 - t[r, k] for k in range(q8) if v[r, k] == c and eps[r, k] == 0)
            twoBA[2 * B - A] += 1
            if 2 * B - A == 0:
                bad += 1
        tpat[tuple(t[r, jj] for jj in f0)] += 1
        op3pat[tuple(op3mod8[r, jj] for jj in f0)] += 1
    print("p=%d npts=%d 2B-A at phi0 classes: %s  points with a zero class: %d" % (p, npts, dict(twoBA), bad))
    print("   t-patterns at f0 reps: %s" % tpat.most_common(4))
    print("   Op^(3) mod 8 at f0 reps: %s" % op3pat.most_common(4))
print("DONE")
