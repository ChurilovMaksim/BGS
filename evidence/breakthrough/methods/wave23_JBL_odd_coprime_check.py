"""Wave 23, task 2 (retry): exact check of the counterexample to single-class
JBL rigidity in the coprime case. R = Z[sqrt2] as pairs (a,b) = a + b*sqrt2.
m = 8, p = 3, q = 9 || D_8, q2 = 512, t = 4. Coprime case: P = 8, m/P = 1,
3 does not divide 1. Repository untouched; no Lean build.
"""
import math

def mul(x, y, N):
    return ((x[0]*y[0] + 2*x[1]*y[1]) % N, (x[0]*y[1] + x[1]*y[0]) % N)

def tr(x):
    return 2*x[0]

N = 1331712  # D_8 = 512 * 9 * 289
assert 512*9*289 == N
alpha8 = (665857, 470832)  # alpha^8, alpha = 3 + 2*sqrt2
beta = (577, 408)           # alpha^4
assert alpha8[0]**2 - 2*alpha8[1]**2 == 1
B = (887808, 1040400)
Bp = (887808, 596496)

d = ((alpha8[0]-1) % N, alpha8[1] % N)
assert mul(d, B, N) == (0, 0) and mul(d, Bp, N) == (0, 0), "not Fix parameters"
assert (B[0] % 512, B[1] % 512) == (0, 16) == (Bp[0] % 512, Bp[1] % 512)
assert (B[0] % 9, B[1] % 9) == (3, 0) and (Bp[0] % 9, Bp[1] % 9) == (3, 3)

def joint(X):
    out, cur = [], (1, 0)
    for _ in range(2):  # s in Z/(m/t) = Z/2
        v = mul(X, cur, N)
        out.append((tr(v) % 512, tr(v) % 9))
        cur = mul(cur, beta, N)
    return sorted(out)

assert joint(B) == joint(Bp) == [(0, 6), (0, 6)], (joint(B), joint(Bp))
orbit, cur = set(), (1, 0)
for _ in range(12):
    orbit.add((mul(B, cur, 9)[0] % 9, mul(B, cur, 9)[1] % 9))
    orbit.add((mul((B[0], -B[1]), cur, 9)[0] % 9, mul((B[0], -B[1]), cur, 9)[1] % 9))
    cur = mul(cur, beta, 9)
assert orbit == {(3, 0)} and (Bp[0] % 9, Bp[1] % 9) == (3, 3) not in orbit
assert math.gcd(8, 4) == 4 and (8 // 8) % 3 != 0
print("ALL CHECKS PASS: joint multisets equal, Bp not D-related to B mod 9.")
