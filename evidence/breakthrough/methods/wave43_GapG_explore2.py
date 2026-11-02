"""Wave 43, task 2 exploration part 2: tower operators + phi=0 class analysis at m=256."""
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
    j = p.bit_length() - 1
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
    # tower operators Op^(s), s=2..j-4, modulus Q/2^{j-s-2}, shift 2^s in w
    print("=== p=%d j=%d npts=%d" % (p, j, npts))
    for s in range(2, j - 3):
        sh = 2 ** s
        mod = Q // (2 ** (j - s - 2))
        dd = (W[:, sh:sh + q8] - W[:, :q8]) % Q
        divok = bool(np.all(dd % mod == 0))
        op = (dd // mod) % 4 if divok else None
        rel = None
        if divok:
            rel = {
                "op==phi": bool(np.all(op == phi)),
                "op==phi+2": bool(np.all(op == (phi + 2) % 4)),
                "op-phi values": Counter(((op - phi) % 4).ravel().tolist()),
            }
        print("  s=%d shift=%d mod=Q/%d divok=%s %s" % (s, sh, 2 ** (j - s - 2), divok, rel))
    # phi=0 pair class analysis: for each point, f0 reps, their classes, 2B-A per class
    distinct_fail = 0
    cancel_fail = 0
    f0count = Counter()
    for r in range(npts):
        f0 = [jj for jj in range(p16) if eps[r, jj] == 0 and phi[r, jj] == 0]
        f0count[len(f0)] += 1
        cls = [v[r, jj] for jj in f0]
        if len(set(cls)) != len(cls):
            distinct_fail += 1
        for jj in f0:
            c = v[r, jj]
            A = sum(1 for k in range(q8) if v[r, k] == c and eps[r, k] == 0)
            B = sum(1 - t[r, k] for k in range(q8) if v[r, k] == c and eps[r, k] == 0)
            if 2 * B - A not in (2, -2):
                cancel_fail += 1
                break
    print("  f0 count dist=%s distinct_fail=%d cancel_fail=%d" % (dict(f0count), distinct_fail, cancel_fail))
    # sample point: phi, G, v at f0 reps, differences v_{j+4}-v_j mod Q/2
    r = 0
    f0 = [jj for jj in range(p16) if eps[r, jj] == 0 and phi[r, jj] == 0]
    modG = Q // (2 ** (j - 4))
    gdiff = (W[r, 4:4 + q8] - W[r, :q8]) % Q
    G = (gdiff // modG) % 4
    print("  sample0 f0=%s phi_f0=%s G_f0=%s v_f0=%s" % (
        f0, [phi[r, jj] for jj in f0], [G[jj] for jj in f0], [v[r, jj] for jj in f0]))
    print("  sample0 v_{j+4}-v_j (mod Q/2) at f0: %s" % [
        (v[r, jj + 4] - v[r, jj]) % (Q // 2) for jj in f0])
    print("  sample0 (w_{j+4}-w_j) mod Q at f0: %s  (Q/8=%d)" % (
        [(W[r, jj + 4] - W[r, jj]) % Q for jj in f0], Q // 8))
print("DONE")
