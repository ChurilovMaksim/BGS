"""Wave 32, task 2: RB2 census.

For each m, for each prime-power component q || D_m with q <= CAP,
enumerate ker(H_m mod q) (SNF), group into sorted-multiset fibers
and dihedral Gamma-orbits, compute component support, and report:
  - split fibers ( >1 orbit ) and whether fully on support
  - mixed-support fibers (should be 0: support constant on fibers)
  - on-support split fibers OUTSIDE q3 = 3**(2*v3(m)+2)  -> RB2 violation
  - split fibers at q3 with size > 4*m^2                 -> size-bound violation
Reuses wave16_d1a_targeted (Dm, snf_kernel, torsion_data,
comp_supported, gamma_perms, lex_canon, group_ids).
"""
import sys, math
sys.path.insert(0, ".")
import numpy as np
import sympy as sp
from wave16_d1a_targeted import (Dm, snf_kernel, torsion_data, comp_supported,
                                 gamma_perms, lex_canon, group_ids)

CAP = 400_000

def v_p(n, p):
    c = 0
    while n % p == 0:
        n //= p; c += 1
    return c

def analyze(m):
    D = Dm(m)
    fac = sp.factorint(D)
    qs = sorted([p ** e for p, e in fac.items()])
    Z, Qmod = torsion_data(m, D)
    perms = gamma_perms(m)
    v3 = v_p(m, 3)
    q3 = 3 ** (2 * v3 + 2) if m % 4 == 0 else None
    print(f"== m={m} D={D} v3={v3} q3={q3}", flush=True)
    violations = []
    for q in qs:
        if q > CAP:
            print(f"   q={q}: SKIPPED (>CAP)", flush=True)
            continue
        pts = snf_kernel(m, q)
        assert len(pts) == q, (m, q, len(pts))
        fib = group_ids(np.sort(pts, axis=1))
        canon = lex_canon(pts, perms)
        gam = group_ids(canon)
        n_fib = int(fib.max()) + 1
        gam_fiber = np.empty(int(gam.max()) + 1, dtype=np.int64)
        gam_fiber[gam] = fib
        opf = np.bincount(gam_fiber, minlength=n_fib)
        split_fibs = np.where(opf > 1)[0]
        sup = comp_supported(pts, Z, Qmod, q)
        mixed = 0
        onsup_splits = []
        for f in split_fibs:
            idx = np.where(fib == f)[0]
            s = int(sup[idx].sum())
            if s == len(idx):
                onsup_splits.append((int(len(idx)), int(len(set(gam[idx].tolist())))))
            if 0 < s < len(idx):
                mixed += 1
        # also count partial-support fibers overall
        n_partial = 0
        for f in range(n_fib):
            idx = np.where(fib == f)[0]
            s = int(sup[idx].sum())
            if 0 < s < len(idx):
                n_partial += 1
        print(f"   q={q}: fibers={n_fib} split={len(split_fibs)} "
              f"on-support splits={onsup_splits} partial={n_partial} mixed_split={mixed}",
              flush=True)
        for (sz, no) in onsup_splits:
            if q != q3:
                violations.append(f"m={m} q={q} on-support split outside q3: size={sz} orbits={no}")
            if q == q3 and sz > 4 * m * m:
                violations.append(f"m={m} q=q3={q} split size {sz} > 4m^2={4*m*m}")
            if q == q3 and no > m:
                violations.append(f"m={m} q=q3={q} orbit count {no} > m={m}")
        if n_partial:
            violations.append(f"m={m} q={q}: {n_partial} partial-support fibers (support not constant!)")
    return violations

all_v = []
for m in [12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 6, 10, 18, 30]:
    all_v += analyze(m)
print("VIOLATIONS:", all_v if all_v else "NONE", flush=True)
