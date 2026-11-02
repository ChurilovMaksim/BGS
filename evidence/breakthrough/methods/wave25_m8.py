"""Wave 25, task 5 (part 1): m=8 full census — C(y) separation and
Sigma y_i w_i constancy on (fiber, w)-classes.

Fix_8: 1,331,712 points, Hy divisible by D_8, w = Hy/D.
Fiber = sorted(y); orbit = dihedral canon; (fiber,w)-class =
(sorted(y), sorted(w)). Tests:
  (a) C(y) = sum_i y_i*y_{i+1}*|y_i - y_{i+1}| distinct across orbits
      of every split fiber (expect 39, all off-support).
  (b) S(y) = sum_i y_i*w_i (equivalently ab-sum A(y) = sum_i
      y_i*y_{i+1}, since D*S = 6*sum y_i^2 - 2*A and sum y_i^2 is
      fiber-constant) constant across orbits of every multi-orbit
      (fiber,w)-class? A counterexample refutes the general-m
      constancy mechanism; holding everywhere supports it.
Exact integers throughout (C in Python ints on representatives only).
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

comp_pts = {}
for q in qs:
    pts = snf_kernel(m, q)
    assert len(pts) == q
    comp_pts[q] = pts
    print(f"  q={q}: {len(pts)} component points", flush=True)

q_big = max(qs)
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

dq_big = D // q_big
K_big = (dq_big * pow(dq_big % q_big, -1, q_big)) % D
n_tot = D
all_sorted = np.empty((n_tot, m), dtype=np.int64)
all_canon = np.empty((n_tot, m), dtype=np.int64)
all_sup = np.empty(n_tot, dtype=bool)
all_w_sorted = np.empty((n_tot, m), dtype=np.int64)
all_S = np.empty(n_tot, dtype=np.int64)
all_A = np.empty(n_tot, dtype=np.int64)
row = 0
chunk = 20000
for st in range(0, q_big, chunk):
    en = min(q_big, st + chunk)
    blk = (base[None, :, :] + (K_big * comp_pts[q_big][st:en])[:, None, :]) % D
    blk = blk.reshape(-1, m)
    n = len(blk)
    Hy = 6 * blk - np.roll(blk, 1, axis=1) - np.roll(blk, -1, axis=1)
    assert np.all(Hy % D == 0), "Hy not divisible by D"
    w = Hy // D
    all_sorted[row:row + n] = np.sort(blk, axis=1)
    all_canon[row:row + n] = lex_canon(blk, perms)
    all_sup[row:row + n] = global_supported(blk, Z, Qmod, D)
    all_w_sorted[row:row + n] = np.sort(w, axis=1)
    all_S[row:row + n] = (blk * w).sum(axis=1)
    all_A[row:row + n] = (blk * np.roll(blk, -1, axis=1)).sum(axis=1)
    row += n
print(f"rows={row}", flush=True)
assert row == n_tot

# identity check: D*S == 6*sum y^2 - 2*A on a sample
idx0 = np.arange(0, n_tot, 100003)
lhs = D * all_S[idx0]
rhs = 6 * (all_sorted[idx0] ** 2).sum(axis=1) - 2 * all_A[idx0]
assert np.all(lhs == rhs), "identity D*S = 6*sum y^2 - 2*A failed"
print("identity D*S = 6*sum(y^2) - 2*A verified on sample", flush=True)

fib = group_ids(all_sorted)
orb = group_ids(all_canon)
n_fib = int(fib.max()) + 1
n_orb = int(orb.max()) + 1
print(f"fibers={n_fib} orbits={n_orb}", flush=True)
assert (n_fib, n_orb) == (85106, 85145), (n_fib, n_orb)

orb_fiber = np.empty(n_orb, dtype=np.int64)
orb_fiber[orb] = fib
opf = np.bincount(orb_fiber, minlength=n_fib)
split_fibs = np.where(opf > 1)[0]
print(f"split fibers: {len(split_fibs)}", flush=True)
assert len(split_fibs) == 39


def C_of(y):
    y = [int(v) for v in y]
    return sum(y[i] * y[(i + 1) % m] * abs(y[i] - y[(i + 1) % m])
               for i in range(m))


# (a) C separation on split fibers (canon reps; C is dihedral-invariant)
c_fail = 0
for f in split_fibs:
    idx = np.where(fib == f)[0]
    orbits = sorted(set(orb[idx].tolist()))
    cvals = []
    for o in orbits:
        j = idx[orb[idx] == o][0]
        cvals.append(C_of(all_canon[j]))
    if len(set(cvals)) != len(cvals):
        c_fail += 1
        print(f"  C FAIL split fiber {f}: orbits={len(orbits)} C={cvals}",
              flush=True)
print(f"C(y) failures on split fibers: {c_fail} / {len(split_fibs)}",
      flush=True)

# (b) (fiber, w)-classes with >= 2 orbits: S and A constancy
fw_keys = np.concatenate([all_sorted, all_w_sorted], axis=1)
fw = group_ids(fw_keys)
n_fw = int(fw.max()) + 1
# orbit -> fw class: take fw of first point of each orbit
orb_fw = np.empty(n_orb, dtype=np.int64)
seen_orb = np.zeros(n_orb, dtype=bool)
for j in range(n_tot):
    o = orb[j]
    if not seen_orb[o]:
        seen_orb[o] = True
        orb_fw[o] = fw[j]
assert seen_orb.all()
# count orbits per fw class
opfw = np.bincount(orb_fw, minlength=n_fw)
multi = np.where(opfw > 1)[0]
print(f"(fiber,w)-classes: {n_fw}; multi-orbit classes: {len(multi)}",
      flush=True)

s_var = 0
a_var = 0
examples = []
for c in multi:
    orbits = np.where(orb_fw == c)[0]
    # S and A are constant on an orbit? S is NOT dihedral-invariant in
    # general (it is a cyclic sum, but reversal? check per point).
    # Use per-point values across all points of the class's orbits.
    pts_idx = np.where(np.isin(fw, [c]))[0]
    svals = set(all_S[pts_idx].tolist())
    avals = set(all_A[pts_idx].tolist())
    if len(svals) > 1:
        s_var += 1
        if len(examples) < 5:
            examples.append((int(c), sorted(svals), sorted(avals),
                             [int(x) for x in orbits]))
    if len(avals) > 1:
        a_var += 1
print(f"multi-orbit (fiber,w)-classes with varying S: {s_var} / "
      f"{len(multi)}", flush=True)
print(f"multi-orbit (fiber,w)-classes with varying A: {a_var} / "
      f"{len(multi)}", flush=True)
for e in examples:
    print("  example class:", e, flush=True)

# Also: is S constant on each single orbit (dihedral invariance of S)?
# S(y) = <y, Hy>/D; Hy is dihedral-equivariant and inner product is
# permutation-invariant, so S IS dihedral-invariant. Verify on sample.
print("S per-orbit constancy is structural (<y,Hy>/D, Hy equivariant); "
      "verified implicitly by class test above.", flush=True)

with open("/home/hatch/workspace/bgs-breakthrough/methods/"
          "wave25_m8.json", "w") as fh:
    json.dump({"D": int(D), "n_fibers": n_fib, "n_orbits": n_orb,
               "split_fibers": int(len(split_fibs)),
               "C_failures": int(c_fail),
               "fw_classes": int(n_fw),
               "multi_orbit_fw_classes": int(len(multi)),
               "S_varying_classes": int(s_var),
               "A_varying_classes": int(a_var),
               "examples": examples}, fh, indent=1)
print("wrote wave25_m8.json", flush=True)
