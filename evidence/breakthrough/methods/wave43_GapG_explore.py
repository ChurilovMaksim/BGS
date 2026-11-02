"""Wave 43, task 2 exploration: Gap G induction step.
For m = 2^k, Q = 8 m^2, periods p = 2^j:
- enumerate nu=(1,0) minimal-period kernel points directly,
- direct Gap G check (O symmetric <=> low/up counters match),
- phi_k (shift p/16 in w), G_k (shift 4 in w),
- intermediate operators Op^(s) (shift 2^s in w),
- parametrisation pattern (y0, y1) for nu=(1,0) points.
Usage: python3 wave43_GapG_explore.py [m] [pmax]
"""
import sys
from math import gcd
import numpy as np
from collections import Counter

m = int(sys.argv[1]) if len(sys.argv) > 1 else 256
Q = 8 * m * m
print("m=%d Q=%d" % (m, Q))


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
# precompute M^n rows for y_n = Mn[1][0]*y1 + Mn[1][1]*y0
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


def seq_vals(y0, y1, ns):
    """y_n for n in ns (list), vectorized over points."""
    out = []
    for n in ns:
        Mn = Mpows[n]
        out.append((Mn[1][0] * y1 + Mn[1][1] * y0) % Q)
    return out  # list of arrays, index = position in ns


for p in [2**j for j in range(3, 10) if 2**j <= m]:
    j = p.bit_length() - 1
    y0, y1 = kernel_points(p)
    # minimal period: y_{p/2}... use sequence period via M^{p/2}: point has
    # period dividing p/2 iff (y0,y1) is fixed by M^{p/2}
    Mp2 = matpow(M, p // 2)
    yhalf0 = (Mp2[1][0] * y1 + Mp2[1][1] * y0) % Q  # y_{p/2}
    yhalf1 = (Mp2[0][0] * y1 + Mp2[0][1] * y0) % Q  # y_{p/2+1}
    minper = (yhalf0 != y0) | (yhalf1 != y1)
    # nu: y_{p/2}-y0 and y_{p/2+1}-y1 divisible by Q/2?
    d0 = (yhalf0 - y0) % Q
    d1 = (yhalf1 - y1) % Q
    div = (d0 % (Q // 2) == 0) & (d1 % (Q // 2) == 0)
    nu0 = (d0 // (Q // 2)) % 2
    nu1 = (d1 // (Q // 2)) % 2
    sel = minper & div & (nu0 == 1) & (nu1 == 0)
    y0s, y1s = y0[sel], y1[sel]
    npts = len(y0s)
    # w_k = y_{2k+1}, k < p/4
    wcols = seq_vals(y0s, y1s, [2 * k + 1 for k in range(p // 4)])
    W = np.stack(wcols, axis=1)  # (npts, p/4)
    # direct Gap G: low/up counters on w-cycle
    sym = 0
    for row in W:
        v = row % (Q // 2)
        t = row // (Q // 2)
        low = Counter(v[t == 0])
        up = Counter(v[t == 1])
        if low == up:
            sym += 1
    # phi_k, k < p/8: f = w_{k+p/16} - w_k, divisible by Q/4?
    q8 = p // 8
    p16 = p // 16
    phi_div_ok = True
    phi = None
    if p >= 16:
        f = (W[:, p16:p16 + q8] - W[:, :q8]) % Q
        phi_div_ok = bool(np.all(f % (Q // 4) == 0))
        phi = (f // (Q // 4)) % 4
    # eps over quarter indices
    eps = ((W[:, q8:2 * q8] - W[:, :q8]) % Q) // (Q // 2) if p >= 16 else None
    # G_k, shift 4 in w, modulus Q/2^{j-4} (p>=32)
    G = None
    G_div_ok = None
    if p >= 32:
        modG = Q // (2 ** (j - 4))
        gdiff = (W[:, 4:4 + q8] - W[:, :q8]) % Q
        G_div_ok = bool(np.all(gdiff % modG == 0))
        G = (gdiff // modG) % 4
    # G == phi + 2 ?
    Geq = None
    if G is not None:
        Geq = bool(np.all((G - phi) % 4 == 2))
    # phi=0 pair representatives: j < p/16, eps[j]==0, phi[j]==0
    f0info = None
    if p >= 64:
        z0 = [jj for jj in range(p16) if True]
        # eps over pair reps: eps index j (quarter indices), phi index j
        eps_rep = eps[:, :p16]
        phi_rep = phi[:, :p16]
        f0sets = []
        for r in range(npts):
            f0 = [jj for jj in range(p16) if eps_rep[r, jj] == 0 and phi_rep[r, jj] == 0]
            f0sets.append(tuple(f0))
        cc = Counter(f0sets)
        f0info = (len(cc), cc.most_common(3))
    # parametrisation pattern for nu points
    step0 = Q // (8 * p)
    step1 = Q // p
    tvals = y0s // step0 if npts else y0s
    pat = None
    if npts:
        rem0 = np.all(y0s % step0 == 0)
        # y1 = a*step0*t + step1*s ; solve a from a sample with t odd?
        # find a mod 8p: use first point with t odd: (y1 - step1*s) ...
        # instead: check y1 mod step1 vs step0*t mod step1
        # step1/step0 = 8, so y1 mod step1 = a*step0*t mod step1 -> a*t mod 8
        a_mod8 = Counter(((y1s % step1) // step0 % 8).tolist())
        pat = (bool(rem0), bool(np.all(tvals % 2 == 1)), a_mod8.most_common(3))
    print("p=%d j=%d ker=%d nu10=%d symO=%d phi_div=%s G_div=%s G=phi+2:%s f0sets=%s pat(y0mult,todd,amod8)=%s"
          % (p, j, len(y0), npts, sym, phi_div_ok, G_div_ok, Geq, f0info, pat))
    # intermediate operators on first point: Op^(s) vs phi
    if p >= 64 and npts:
        w0 = W[0]
        ph0 = phi[0]
        ops = {}
        for s in range(2, j - 3):
            sh = 2 ** s
            mod = Q // (2 ** (j - 3 - s))
            dd = (w0[sh:sh + q8] - w0[:q8]) % Q
            ok = bool(np.all(dd % mod == 0))
            ops[s] = (ok, ((dd // mod) % 4)[:8].tolist() if ok else None)
        print("   sample0 phi[:8]=%s eps[:8]=%s ops=%s" % (ph0[:8].tolist(), eps[0, :8].tolist(), ops))
print("DONE")
