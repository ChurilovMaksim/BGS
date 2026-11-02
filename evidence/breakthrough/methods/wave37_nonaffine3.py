"""Wave 37, task 5, stage 3: mechanism of the 2 exceptional fibers.

Checks: K2[0] is the zero row; all members sigma-symmetric for
sigma(i) = -i+15 mod 30; K1 rows divisible by 25 and their value
sets; unordered cyclic adjacent-pair multisets per orbit (do they
separate the 5 orbits?); scaling relations between orbit reps
(within a fiber and between the two fibers by x2).
"""
import numpy as np
from collections import defaultdict
import importlib.util

spec = importlib.util.spec_from_file_location(
    "w37", "/home/hatch/workspace/bgs-breakthrough/methods/wave37_nonaffine.py")
w37 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(w37)

M, N1, N2 = 30, 625, 841
K1 = w37.kernel_mod_np(M, N1)
K2 = w37.kernel_mod_np(M, N2)
d = np.load("/tmp/w37_stage1.npz")
gfib, canon = d["gfib"], d["canon"]
i1_all, i2_all = d["i1_all"], d["i2_all"]
print("K2[0] is zero row:", bool((K2[0] == 0).all()), flush=True)

uk, uk_counts = np.unique(np.stack([gfib, canon], axis=1), axis=0,
                           return_counts=True)
fib_orbits = defaultdict(list)
for (f_, _), s_ in zip(uk.tolist(), uk_counts.tolist()):
    fib_orbits[f_].append(s_)
multi = sorted(f_ for f_, s in fib_orbits.items() if len(s) > 1)
print("multi-orbit fiber ids:", multi, flush=True)

P = (K1[:, None, :].astype(np.int64) * N2 +
     K2[None, :, :].astype(np.int64)).astype(np.int32)
SIG = [(-i + 15) % M for i in range(M)]

for f_ in multi:
    members = np.where(gfib == f_)[0]
    rows = P[members // N2, members % N2]
    # sigma-symmetry
    sig_ok = all(np.array_equal(r, r[SIG]) for r in rows)
    # divisibility by 25 of K1 component
    k1rows = K1[members // N2]
    div25 = bool((k1rows % 25 == 0).all())
    vset = sorted(set((k1rows[0] // 25).tolist()))
    print(f"\nfiber {f_}: members {len(members)}, all sigma-symmetric: "
          f"{sig_ok}, K1 rows all div by 25: {div25}", flush=True)
    print(f"  K1 value set (/25) of rep: {vset}", flush=True)
    print(f"  mod-5 reductions of value set: "
          f"{sorted(set(v % 5 for v in vset))}", flush=True)
    # per-orbit adjacent-pair multisets
    cm = canon[members]
    orbs = defaultdict(list)
    for pt, co in zip(members.tolist(), cm.tolist()):
        orbs[co].append(pt)
    adj_sets = {}
    for rep, pts in sorted(orbs.items()):
        r = P[rep // N2, rep % N2]
        pairs = tuple(sorted(tuple(sorted((int(r[i]), int(r[(i + 1) % M]))))
                             for i in range(M)))
        adj_sets[rep] = pairs
        print(f"  orbit {rep}: adj-pair multiset hash {hash(pairs) % 10**8}, "
              f"first pairs {pairs[:4]}", flush=True)
    print("  adj multisets pairwise distinct:",
          len(set(adj_sets.values())) == len(adj_sets), flush=True)
    # scaling relations between orbit reps (K1 rows, mod 625)
    reps = sorted(orbs.keys())
    k1reps = {rep: K1[rep // N2] for rep in reps}
    print("  scaling between orbit reps (u with r_j = u*r_1 mod 625):",
          flush=True)
    base = k1reps[reps[0]]
    for rep in reps[1:]:
        found = []
        for u in range(1, 625):
            if np.gcd(u, 625) != 1:
                continue
            if np.array_equal((u * base) % 625, k1reps[rep]):
                found.append(u)
                break
        print(f"    rep {rep}: u = {found}", flush=True)

# scaling by 2 between the two fibers' K1 row sets
f_a, f_b = multi
rows_a = set()
for pt in np.where(gfib == f_a)[0].tolist():
    rows_a.add(K1[pt // N2].tobytes())
rows_b = set()
for pt in np.where(gfib == f_b)[0].tolist():
    rows_b.add(K1[pt // N2].tobytes())
scaled = set(((2 * np.frombuffer(r, dtype=np.int32)) % 625).tobytes()
             for r in rows_a)
print("\nfiber", f_a, "x2 == fiber", f_b, "K1 row sets:", scaled == rows_b,
      flush=True)
# and the reverse: is fiber b x13 (2^-1 mod 625 = 313?) -- 2*313=626=1 mod 625
inv2 = pow(2, -1, 625)
scaled_back = set(((inv2 * np.frombuffer(r, dtype=np.int32)) % 625).tobytes()
                  for r in rows_b)
print("fiber", f_b, "x inv2 == fiber", f_a, ":", scaled_back == rows_a,
      flush=True)
