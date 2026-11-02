"""Wave 22, task 4 (part 1): Adj separator test at m=8 (FULL census).

m=8: D_8 = 1331712 = 512 * 9 * 289, so full Fix_8 enumeration is cheap
(1,331,712 points). Group into fibers (sorted values) and Gamma-orbits
(dihedral canon, 16 perms); for every split fiber, check that Adj(y) =
sorted multiset of unordered cyclic adjacent pairs {y_i, y_{i+1}}
takes distinct values on distinct orbits. Also split by support
(global torsion criterion s=1). Expected (wave 14): 85,106 fibers,
85,145 orbits, 39 split fibers, all off-support.
Repository untouched; no Lean build.
"""
import json
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data,
                                 global_supported, gamma_perms,
                                 lex_canon, group_ids, crt_combine)

m = 8
D = Dm(m)
fac = sp.factorint(D)
qs = [p ** e for p, e in fac.items()]
print(f"m={m} D={D} prime powers={qs}", flush=True)
assert D == 1331712 and sorted(qs) == [9, 289, 512]

Z, Qmod = torsion_data(m, D)
perms = gamma_perms(m)
print(f"|V4|={len(Z)} perms={len(perms)}", flush=True)

comp_pts = {}
for q in qs:
    pts = snf_kernel(m, q)
    assert len(pts) == q
    comp_pts[q] = pts
    print(f"  q={q}: {len(pts)} component points", flush=True)

# CRT combine all triples: iterate over the smallest components outer
# to keep memory bounded; accumulate sorted/canon in chunks.
q_big = max(qs)
others = [q for q in qs if q != q_big]
# Build full array in blocks over the big component.
n_tot = D
print(f"total global points: {n_tot}", flush=True)

all_sorted = np.empty((n_tot, m), dtype=np.int64)
all_canon = np.empty((n_tot, m), dtype=np.int64)
all_sup = np.empty(n_tot, dtype=bool)
row = 0
# CRT base over the two smaller components (mixed-radix indexing),
# then loop over the big component in chunks.
small = {q: comp_pts[q] for q in qs if q != q_big}
qs_small = list(small.keys())
n_small = 1
for q in qs_small:
    n_small *= q
base = np.zeros((n_small, m), dtype=np.int64)
div = n_small
for q in qs_small:
    div //= q
    sel = (np.arange(n_small) // div) % q
    dq = D // q
    K = (dq * pow(dq % q, -1, q)) % D
    base = (base + K * small[q][sel]) % D
print(f"small-component base: {base.shape}", flush=True)

dq_big = D // q_big
K_big = (dq_big * pow(dq_big % q_big, -1, q_big)) % D
chunk = 20000
for st in range(0, q_big, chunk):
    en = min(q_big, st + chunk)
    blk = (base[None, :, :] + (K_big * comp_pts[q_big][st:en])[:, None, :]) % D
    blk = blk.reshape(-1, m)
    n = len(blk)
    all_sorted[row:row + n] = np.sort(blk, axis=1)
    all_canon[row:row + n] = lex_canon(blk, perms)
    all_sup[row:row + n] = global_supported(blk, Z, Qmod, D)
    row += n
    print(f"  big chunk {st}..{en}: rows={row}", flush=True)
assert row == n_tot

fib = group_ids(all_sorted)
orb = group_ids(all_canon)
n_fib = int(fib.max()) + 1
n_orb = int(orb.max()) + 1
print(f"fibers={n_fib} orbits={n_orb}", flush=True)
assert n_fib == 85106, n_fib
assert n_orb == 85145, n_orb

# orbits per fiber
orb_fiber = np.empty(n_orb, dtype=np.int64)
orb_fiber[orb] = fib
opf = np.bincount(orb_fiber, minlength=n_fib)
split_fibs = np.where(opf > 1)[0]
print(f"split fibers: {len(split_fibs)}", flush=True)
assert len(split_fibs) == 39, len(split_fibs)


def adj_of(y):
    return tuple(sorted(tuple(sorted((int(y[i]), int(y[(i + 1) % m]))))
                        for i in range(m)))


results = []
n_adj_fail = 0
n_on_sup = 0
for f in split_fibs:
    idx = np.where(fib == f)[0]
    orbits = sorted(set(orb[idx].tolist()))
    # Use canon rows as orbit representatives: a canon is a dihedral
    # perm of a point in the orbit, and Adj is Gamma-invariant, so
    # Adj(canon) = Adj(point). (Global points themselves were not kept
    # to save memory; sorted rows and canons were.)
    adj_vals = []
    for o in orbits:
        j = idx[orb[idx] == o][0]
        adj_vals.append(adj_of(all_canon[j]))
    ok = len(set(adj_vals)) == len(adj_vals)
    if not ok:
        n_adj_fail += 1
    sup_pat = all_sup[idx]
    n_sup = int(sup_pat.sum())
    pat = "FULL" if n_sup == len(idx) else "PARTIAL" if n_sup > 0 else "EMPTY"
    if pat != "EMPTY":
        n_on_sup += 1
    results.append({
        "fiber": int(f), "size": int(len(idx)), "n_orbits": len(orbits),
        "orbit_sizes": [int((orb[idx] == o).sum()) for o in orbits],
        "n_supp": n_sup, "pattern": pat, "adj_separates": bool(ok),
    })
    print(f"  split fiber {f}: size={len(idx)} orbits={len(orbits)} "
          f"supp={n_sup} -> {pat} adj_ok={ok}", flush=True)

print(f"Adj failures: {n_adj_fail} / {len(split_fibs)}; "
      f"split fibers meeting support: {n_on_sup}", flush=True)
assert n_adj_fail == 0
assert n_on_sup == 0

with open("/home/hatch/workspace/bgs-breakthrough/methods/"
          "wave22_Adj_m8.json", "w") as fh:
    json.dump({"D": int(D), "n_fibers": n_fib, "n_orbits": n_orb,
               "split_fibers": results}, fh, indent=1)
print("wrote wave22_Adj_m8.json", flush=True)
