"""Wave 37, task 1 (retry), part 3: nonzero sequences at large components.

For q = p^2 with all kernel seeds divisible by p, the kernel equals
p*(Z/p^2)^2 as a set (sizes match), so every nonzero seed is a unit
multiple of one of p+1 direction reps (p, p*t), (0, p); unit scaling
preserves blindness both ways, so testing the reps is EXACT.
For q = 31^4, batched exhaustive test over all seeds.
"""
import math, sys
import numpy as np
sys.path.insert(0, ".")
exec(open("wave37_Blindness_m60.py").read().split("# ---------- small components")[0])

# ---------- e=2 components: direction reps ----------
for q, p in [(1681, 41), (3481, 59), (72361, 269), (361201, 601), (5202961, 2281)]:
    reps = [(p % q, (p*t) % q) for t in range(p)] + [(0, p % q)]
    n625 = n81 = 0
    for (s0, s1) in reps:
        o = seq_from(s0, s1, M, q)
        if any(triple_collides(a, fib, o, q, 625) for a in a_reps for fib in reps625):
            n625 += 1
        if any(triple_collides(b, reps81[0], o, q, 81) for b in b_reps):
            n81 += 1
    print(f"q={q} (p={p}): direction reps={len(reps)} blind625 reps={n625} blind81 reps={n81}", flush=True)
print("DIRECTION DONE", flush=True)

# ---------- 923521 = 31^4: batched exhaustive ----------
q, p = 923521, 31
Mm = mat_pow([6, q-1, 1, 0], M, q)
a = (Mm[0]-1) % q; b = Mm[1] % q; c = Mm[2] % q; d = (Mm[3]-1) % q
y0 = np.arange(q, dtype=np.int64)
g = math.gcd(a, q)
mask = (b*y0) % g == 0
y0m = y0[mask]
a1, q1 = a//g, q//g
inv = pow(a1, -1, q1) if q1 > 1 else 0
y1_0 = ((-(b*y0m)//g) * inv) % q1
step = q//g
S0, S1 = [], []
for k in range(g):
    y1 = y1_0 + k*step
    ok = np.nonzero((c*y1 + d*y0m) % q == 0)[0]
    S0.append(y0m[ok]); S1.append(y1[ok])
S0 = np.concatenate(S0); S1 = np.concatenate(S1)
print(f"923521 seeds: {len(S0)} (expect {q})", flush=True)

def batch_blind(S0, S1, fixed, orbreps, qfree, batch=20000):
    """Count seeds (excluding zero) with a triple-multiset collision."""
    cnt = 0
    for s in range(0, len(S0), batch):
        y0b = S0[s:s+batch]; y1b = S1[s:s+batch]
        B = len(y0b)
        seq = np.empty((B, M), dtype=np.int64)
        seq[:, 0] = y0b; seq[:, 1] = y1b
        for i in range(2, M):
            seq[:, i] = (6*seq[:, i-1] - seq[:, i-2]) % q
        fixed_arr = np.array(fixed, dtype=np.int64)
        packed = np.empty((B, len(orbreps), M), dtype=np.int64)
        for j, orb in enumerate(orbreps):
            orb_arr = np.array(orb, dtype=np.int64)
            packed[:, j, :] = fixed_arr[None, :]*(qfree*q) + orb_arr[None, :]*q + seq
        packed.sort(axis=2)
        blind = np.zeros(B, dtype=bool)
        for i in range(len(orbreps)):
            for j in range(i+1, len(orbreps)):
                blind |= (packed[:, i, :] == packed[:, j, :]).all(axis=1)
        nz = ~((y0b == 0) & (y1b == 0))
        cnt += int((blind & nz).sum())
    return cnt

for ai, a in enumerate(a_reps):
    for fi, fib in enumerate(reps625):
        c = batch_blind(S0, S1, a, fib, 625)
        print(f"923521 blind625 nonzero: a-rep {ai} fiber {fi} -> {c}", flush=True)
for bi, b in enumerate(b_reps):
    c = batch_blind(S0, S1, b, reps81[0], 81)
    print(f"923521 blind81 nonzero: b-rep {bi} -> {c}", flush=True)
print("PART3 DONE", flush=True)
