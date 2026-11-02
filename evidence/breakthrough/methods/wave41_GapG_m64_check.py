"""Wave 41, task 1 checks: Gap G at m=64 (Q=32768).
Verifies matrices, parametrisations, nu-formulas, parity lemma,
phi-recurrence, and Gap G directly on all nu=(1,0) points (p=8,16,32,64).
"""
from collections import Counter

Q = 32768
H = Q // 2
Q4 = Q // 4
a = [0, 1]
for _ in range(100):
    a.append((6 * a[-1] - a[-2]) % Q)


def matmul(A, B):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % Q,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % Q],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % Q,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % Q]]


def matpow(n):
    M = [[6, Q - 1], [1, 0]]
    P = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            P = matmul(P, M)
        M = matmul(M, M)
        n >>= 1
    return P


def seq(y1, y0, n):
    y = [y0, y1]
    for _ in range(n):
        y.append((6 * y[-1] - y[-2]) % Q)
    return y


def sym_O(ys, p):
    O = Counter(ys[i] for i in range(1, p, 2))
    return all(O[v] == O[(v + H) % Q] for v in O)


# 1. Matrices by squaring vs a_n formula
for n in (8, 16, 32, 64):
    P = matpow(n)
    assert P == [[a[n + 1] % Q, (-a[n]) % Q], [a[n] % Q, (-a[n - 1]) % Q]], n
    print(f"M^{n} ok:", P)

# 2. Parametrisations are kernel points, and nu-formulas
for t in range(512):
    y0 = (64 * t) % Q
    for s in range(64):
        y1 = (27328 * t + 512 * s) % Q
        ys = seq(y1, y0, 66)
        assert ys[64] == y0 and ys[65] == y1
        assert (ys[32] - y0) % Q == H * ((t + s) % 2)
        assert (ys[33] - y1) % Q == H * (s % 2)
print("64-param: 32768 kernel points, nu-formula ok")
for t in range(256):
    y0 = (128 * t) % Q
    for s in range(32):
        y1 = (5504 * t + 1024 * s) % Q
        ys = seq(y1, y0, 34)
        assert ys[32] == y0 and ys[33] == y1
        assert (ys[16] - y0) % Q == H * ((t + s) % 2)
        assert (ys[17] - y1) % Q == H * (s % 2)
print("32-param: 8192 kernel points, nu-formula ok")


def nu_points(period):
    """All nu=(1,0) points of exact minimal period `period`, via param or solve."""
    out = []
    if period == 64:
        for t in range(1, 512, 2):
            y0 = (64 * t) % Q
            for s in range(0, 64, 2):
                out.append(((27328 * t + 512 * s) % Q, y0))
    elif period == 32:
        for t in range(1, 256, 2):
            y0 = (128 * t) % Q
            for s in range(0, 32, 2):
                out.append(((5504 * t + 1024 * s) % Q, y0))
    else:
        # solve (M^p - I) s = 0 by iterating y0 and solving the first equation
        import math
        P = matpow(period)
        A = (P[0][0] - 1) % Q
        B = P[0][1] % Q
        C = P[1][0] % Q
        D = (P[1][1] - 1) % Q
        g = math.gcd(A, Q)
        step = Q // g
        for y0 in range(Q):
            rhs = (-B * y0) % Q
            if rhs % g:
                continue
            y1_0 = (pow(A // g, -1, step) * (rhs // g)) % step
            for r in range(g):
                y1 = y1_0 + r * step
                if (C * y1 + D * y0) % Q:
                    continue
                ys = seq(y1, y0, period + period // 2 + 1)
                hp = period // 2
                if (ys[hp] - y0) % Q == H and (ys[hp + 1] - y1) % Q == 0:
                    out.append((y1, y0))
    return out


for p in (8, 16, 32, 64):
    pts = nu_points(p)
    bad = sum(1 for (y1, y0) in pts if sym_O(seq(y1, y0, p), p))
    print(f"p={p}: nu points {len(pts)}, symmetric O: {bad}")
    assert bad == 0

# 3. Parity lemma + phi-recurrence on all p=64 nu points
for (y1, y0) in nu_points(64):
    ys = seq(y1, y0, 64)
    eps = [((ys[2 * k + 1 + 16] - ys[2 * k + 1]) % Q) // H for k in range(8)]
    phi = [((ys[2 * k + 1 + 8] - ys[2 * k + 1]) % Q) // Q4 for k in range(16)]
    assert all(phi[k] % 2 == eps[k % 8] for k in range(8))
    assert all((phi[k + 1] - (2 * phi[k] - phi[k - 1])) % 4 == 0
               for k in range(1, 15))
    # exactly one phi=0 among the eps=0 pairs j<4
    z = [phi[k] for k in range(4) if eps[k] == 0]
    assert sorted(z) == [0, 2]
print("parity lemma, phi-recurrence, unique phi=0: ok on 8192 points")
print("ALL CHECKS PASS")
