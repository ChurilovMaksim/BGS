#!/usr/bin/env python3
"""Wave 46, task 3 checks: valuation lemmas V1-V4, Cassini sign,
mod-4 period, divided-system enumeration at (128,128), DIV at new
levels (1024,1024), (1024,512), (2048,1024). Exit 0 iff all pass."""
import random

def v2(n):
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c

# --- Pell numbers exact ---
N = 2**12 + 2
P = [0, 1]
for i in range(1, N):
    P.append(6 * P[-1] - P[-2])

# --- 1. Valuation lemmas + residues ---
for s in range(1, 13):
    d = 2**s
    V = P[d + 1] - P[d - 1]
    assert v2(P[d]) == s, ("V1", s)
    assert v2(P[d + 1] - 1) == s, ("V2", s)
    assert v2(P[d - 1] + 1) == s, ("V3", s)
    assert v2(2 - V) == 2 * s + 3, ("V4", s)
    if s >= 2:
        assert (P[d] // d) % 16 == 3, ("e", s)
        assert ((P[d + 1] - 1) // d) % 16 == 9, ("c", s)
        assert ((P[d - 1] + 1) // d) % 16 == 9, ("f", s)
print("valuations V1-V4 + residues: OK for s=1..12")

# --- 2. Cassini sign: P_{n+1}P_{n-1} - P_n^2 = -1 (det T^n = 1) ---
for n in range(1, 201):
    assert P[n + 1] * P[n - 1] - P[n] ** 2 == -1, ("Cassini", n)
print("Cassini sign -1: OK for n=1..200")

# --- 3. P_n mod 4 cycles 0,1,2,3 ---
for n in range(0, 101):
    assert P[n] % 4 == [0, 1, 2, 3][n % 4], ("mod4", n)
print("P_n mod 4 period 4: OK for n=0..100")

# --- 4. Divided-system enumeration at (m,p)=(128,128) ---
K, j = 7, 7
Q = 2 ** (2 * K + 3)
step0 = Q // (8 * 2**j)
d = 2 ** (j - 1)
NN = 2 * K + 4 - j  # divided modulus 2^NN = 16*step0
mod = 2 ** NN
a = ((P[d + 1] - 1) // d) % mod
b = (P[d] // d) % mod
f = ((P[d - 1] + 1) // d) % mod
assert a % 2 == 1 and b % 2 == 1 and f % 2 == 1
binv = pow(b, -1, mod)
nsol = 0
bad = 0
for y0 in range(mod):
    y1 = (binv * (f * y0 + 2 ** (NN - 1))) % mod
    if (a * y1 - b * y0) % mod != 0:
        continue
    nsol += 1
    if y0 % step0 != 0 or (y0 // step0) % 2 == 0:
        bad += 1
    if y1 % step0 != 0 or (y1 // step0) % 2 == 0:
        bad += 1
print(f"divided system (128,128): solutions={nsol} odd-quotient violations={bad}")
assert nsol == 8 and bad == 0

# --- 5. DIV at new levels on PAR-style sequences ---
def check_DIV(m, p, trials):
    K = m.bit_length() - 1
    j = p.bit_length() - 1
    Q = 8 * m * m
    step0 = Q // (8 * p)
    assert m == 2**K and p == 2**j and step0 * 8 * p == Q
    rng = random.Random(46)
    viol = 0
    lviol = 0
    for _ in range(trials):
        t = rng.randrange(1, 8 * p, 2)  # odd
        u = (11 * t + 16 * rng.randrange(0, 8 * p)) % (8 * p)
        y = [0] * (2 * p + 2)
        y[0] = (step0 * t) % Q
        y[1] = (step0 * u) % Q
        for i in range(1, 2 * p + 1):
            y[i + 1] = (6 * y[i] - y[i - 1]) % Q
        # L_n = 0 mod 16 for odd n (reduced sequence)
        for n in range(1, 2 * p, 2):
            yn = y[n] // step0
            ynm = y[n - 1] // step0
            if (3 * yn - ynm) % 16 != 0:
                lviol += 1
        # DIV: w_{k+2^s} - w_k = 0 mod mu_s, w_k = y_{2k+1},
        # checked on unwrapped y (n = 2k+1, shift d = 2^{s+1}).
        for s in range(2, j - 3):
            mu = Q // 2 ** (j - 2 - s)
            dd = 2 ** (s + 1)
            for k in range(p // 4):
                n = 2 * k + 1
                if (y[n + dd] - y[n]) % mu != 0:
                    viol += 1
    print(f"DIV (m,p)=({m},{p}): trials={trials} DIV violations={viol} L violations={lviol}")
    assert viol == 0 and lviol == 0

check_DIV(1024, 1024, 200)
check_DIV(1024, 512, 200)
check_DIV(2048, 1024, 200)
print("ALL CHECKS PASS")
