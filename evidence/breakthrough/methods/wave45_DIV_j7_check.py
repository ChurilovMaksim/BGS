"""Wave 45, task 4 check: DIV at j=7 (p=128) directly, plus the key lemma.
For (m, p) = (128, 128) and (256, 128): select kernel points mod Q = 8m^2
with minimal period exactly 128 and nu = (1,0) (y_{i+64} - y_i = Q/2 for
even i, 0 for odd i). Check PAR, u = 11t mod 16, L_n = 3*yt_n - yt_{n-1}
= 0 mod 16 for all odd n, and DIV: w_{k+4} - w_k = 0 mod Q/8 and
w_{k+8} - w_k = 0 mod Q/4 for all k < 32 (w_k = y_{2k+1}).
"""
import numpy as np
from math import gcd


def matmul(A, B, Q):
    return [[(A[0][0]*B[0][0]+A[0][1]*B[1][0]) % Q, (A[0][0]*B[0][1]+A[0][1]*B[1][1]) % Q],
            [(A[1][0]*B[0][0]+A[1][1]*B[1][0]) % Q, (A[1][0]*B[0][1]+A[1][1]*B[1][1]) % Q]]


def matpow(M, n, Q):
    R = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            R = matmul(M, R, Q)
        M = matmul(M, M, Q)
        n >>= 1
    return R


def kernel_points(p, Q):
    M = [[6, Q-1], [1, 0]]
    Mp = matpow(M, p, Q)
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


def check(m, p):
    Q = 8 * m * m
    M = [[6, Q-1], [1, 0]]
    y0, y1 = kernel_points(p, Q)
    Mp2 = matpow(M, p // 2, Q)
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
    step0 = Q // (8 * p)
    par = bool(np.all(y0s % step0 == 0)) and bool(np.all((y0s // step0) % 2 == 1)) \
        and bool(np.all(y1s % step0 == 0))
    t = y0s // step0
    u = y1s // step0
    u_ok = bool(np.all((u - 11 * t) % 16 == 0))
    # full sequences mod Q via matrix powers, chunked
    Mpows = {0: [[1, 0], [0, 1]]}
    cur = [[1, 0], [0, 1]]
    for n in range(1, p + 1):
        cur = matmul(M, cur, Q)
        Mpows[n] = cur
    Lbad = DIV2bad = DIV3bad = 0
    CH = 65536
    for st in range(0, npts, CH):
        a0, a1 = y0s[st:st + CH], y1s[st:st + CH]
        Y = np.stack([(Mpows[n][1][0] * a1 + Mpows[n][1][1] * a0) % Q
                      for n in range(p)], axis=1)  # Y[:, n] = y_n
        yt = Y // step0  # reduced sequence mod 1024
        # L_n for odd n: 3*yt_n - yt_{n-1} mod 16 (n-1 wraps mod p)
        odd = np.arange(1, p, 2)
        Ln = (3 * yt[:, odd] - yt[:, odd - 1]) % 16
        Lbad += int(np.sum(Ln != 0))
        W = Y[:, 1::2]  # w_k = y_{2k+1}, k < 32
        D2 = (np.roll(W, -4, axis=1) - W) % Q
        D3 = (np.roll(W, -8, axis=1) - W) % Q
        DIV2bad += int(np.sum(D2 % (Q // 8) != 0))
        DIV3bad += int(np.sum(D3 % (Q // 4) != 0))
    print("m=%d p=128 npts=%d PAR=%s u=11t(mod16)=%s Lbad=%d DIV2bad=%d DIV3bad=%d"
          % (m, npts, par, u_ok, Lbad, DIV2bad, DIV3bad), flush=True)


check(128, 128)
check(256, 128)
print("DONE")
