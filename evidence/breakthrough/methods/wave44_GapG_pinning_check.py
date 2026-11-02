"""Wave 44, task 3 check: (B1), (B2), tower identity, pinning values, parametrisation.
For (m, p): Q = 8 m^2, j = log2 p, w_k = y_{2k+1}, k < p/4.
  phi_k   = (w_{k+2^{j-4}} - w_k)/(Q/4) mod 4
  Op_s(k) = (w_{k+2^s} - w_k)/(Q/2^{j-2-s}) mod 4, 2 <= s <= j-4
  (B1): Op_2 == phi + 2 (mod 4); (B2): Op_3 == phi (mod 4)
  Tower: Op_{s+1}(k) = (Op_s(k) + Op_s(k+2^s))/2 exactly (integer reps mod Q/mu)
  Pinning: D_0 = D_1 = 2 where D_k = Op_2(k) - phi_k (mod 4);
           E_0 = E_1 = 0 where E_k = Op_3(k) - phi_k (mod 4).
  Param: y0 = step0*t, t odd; u = y1/step0 integer; u == 11*t (mod 16).
"""
import sys
from math import gcd
import numpy as np


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


def check(m, p, maxpts=None):
    Q = 8 * m * m
    j = p.bit_length() - 1
    M = [[6, Q-1], [1, 0]]
    Mpows = {0: [[1, 0], [0, 1]]}
    cur = [[1, 0], [0, 1]]
    for n in range(1, p // 2 + 2):
        cur = matmul(M, cur, Q)
        Mpows[n] = cur
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
    if maxpts:
        y0s, y1s = y0s[:maxpts], y1s[:maxpts]
    npts = len(y0s)
    step0 = Q // (8 * p)
    step1 = Q // p
    q8 = p // 8
    # parametrisation
    par_ok = bool(np.all(y0s % step0 == 0)) and bool(np.all((y0s // step0) % 2 == 1)) \
        and bool(np.all(y1s % step0 == 0))
    t = y0s // step0
    u = y1s // step0
    u_ok = bool(np.all((u - 11 * t) % 16 == 0))
    # operators, chunked
    B1bad = B2bad = towbad = 0
    D0bad = D1bad = E0bad = E1bad = 0
    CH = 65536
    for st in range(0, npts, CH):
        y0c, y1c = y0s[st:st + CH], y1s[st:st + CH]
        wcols = []
        for k in range(p // 4):
            Mn = Mpows[2 * k + 1]
            wcols.append((Mn[1][0] * y1c + Mn[1][1] * y0c) % Q)
        W = np.stack(wcols, axis=1)
        # phi: shift 2^{j-4}, divisor Q/4
        sh_phi = 2 ** (j - 4)
        f = (W[:, sh_phi:sh_phi + q8] - W[:, :q8]) % Q
        assert np.all(f % (Q // 4) == 0), "phi divisibility fails"
        phi = (f // (Q // 4)) % 4
        ops = {}
        for s in range(2, j - 3):
            sh = 2 ** s
            ncol = p // 4 - sh
            mod = Q // (2 ** (j - 2 - s))
            dd = (W[:, sh:sh + ncol] - W[:, :ncol]) % Q
            assert np.all(dd % mod == 0), "Op_%d divisibility fails" % s
            ops[s] = (dd // mod)  # exact integer reps (not mod 4) for tower check
        op2 = ops[2][:, :q8] % 4
        if not np.all((op2 - phi) % 4 == 2):
            B1bad += int(np.sum((op2 - phi) % 4 != 2))
        if j - 4 >= 3:
            op3 = ops[3][:, :q8] % 4
            if not np.all((op3 - phi) % 4 == 0):
                B2bad += int(np.sum((op3 - phi) % 4 != 0))
            E = (op3 - phi) % 4
            E0bad += int(np.sum(E[:, 0] != 0))
            E1bad += int(np.sum(E[:, 1] != 0))
        D = (op2 - phi) % 4
        D0bad += int(np.sum(D[:, 0] != 2))
        D1bad += int(np.sum(D[:, 1] != 2))
        # tower identity: Op_{s+1}(k) = (Op_s(k)+Op_s(k+2^s))/2, exact reps
        for s in range(2, j - 4):
            lhs = ops[s + 1][:, :q8]
            rhs_num = ops[s][:, :q8] + ops[s][:, 2 ** s:2 ** s + q8]
            # rhs must be even and half must equal lhs mod (Q/mu_{s+1}); compare mod 4 and mod 8
            if not np.all(rhs_num % 2 == 0):
                towbad += int(np.sum(rhs_num % 2 != 0))
            elif not np.all((rhs_num // 2) % 4 == lhs % 4):
                towbad += int(np.sum((rhs_num // 2) % 4 != lhs % 4))
    print("m=%d p=%d j=%d npts=%d par=%s u=11tmod16=%s B1bad=%d B2bad=%d towbad=%d D0bad=%d D1bad=%d E0bad=%d E1bad=%d"
          % (m, p, j, npts, par_ok, u_ok, B1bad, B2bad, towbad, D0bad, D1bad, E0bad, E1bad), flush=True)


for (m, p, mx) in [(128, 128, None), (256, 256, None), (256, 128, None),
                   (512, 512, None), (512, 256, 200000)]:
    check(m, p, mx)
print("DONE")
