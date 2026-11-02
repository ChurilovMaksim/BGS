"""Wave 45, task 6, part 8: definitive quadratic-fit test at m=252, k=20.
Solve A x = b (mod 27) for the design [dx^2, dy^2, dx*dy, dx, dy, 1]
by brute-force mod 3 + Hensel lifts to mod 9 and mod 27.
"""
import numpy as np
import itertools

exec(open("wave45_F3_partial.py").read().split("analyse(180")[0])

m = 252
K, T, ci, reps = setup(m)
q = 729
by_k = {}
for rep, (f, C) in reps.items():
    if C[0] == 378 and C[1] % 27 == 0:
        by_k[C[1] // 27] = rep
j = by_k[20]
E = (ci * T[:, j]) % q
F = (E // 27) % 27
Cs = [recover_C(tuple(K[i].tolist()), q) for i in range(q)]
bars = [(c[0] // 27 % 27, c[1] // 27 % 27) for c in Cs]
xj, yj = bars[j]
A = np.zeros((q, 6), dtype=int)
b = np.array([int(v) for v in F], dtype=int)
for i in range(q):
    xb, yb = bars[i]
    dx, dy = (xb - xj) % 27, (yb - yj) % 27
    A[i] = [dx * dx % 27, dy * dy % 27, dx * dy % 27, dx, dy, 1]

def sols_mod(A, b, mod):
    """All x in (Z/mod)^6 with A x = b mod mod, by brute force."""
    out = []
    for x in itertools.product(range(mod), repeat=6):
        if np.all((A @ np.array(x)) % mod == b % mod):
            out.append(x)
    return out

# mod 3
s3 = sols_mod(A % 3, b % 3, 3)
print(f"mod-3 solutions: {len(s3)}")
# lift each to mod 9, then mod 27
def lift(sols, A, b, cur, nxt):
    factor = nxt // cur
    out = []
    for x0 in sols:
        r = (b - A @ np.array(x0)) % nxt
        if np.any(r % cur != 0):
            continue
        rhs = (r // cur) % factor
        for t in itertools.product(range(factor), repeat=6):
            if np.all((A @ np.array(t)) % factor == rhs):
                out.append(tuple((np.array(x0) + cur * np.array(t)) % nxt))
    return out

s9 = lift(s3, A, b, 3, 9)
print(f"mod-9 lifts: {len(s9)}")
s27 = lift(s9, A, b, 9, 27)
print(f"mod-27 solutions: {len(s27)}")
for x in s27[:10]:
    print(f"  coeffs (a,b,c,d,e,f) = {x}")
