"""Wave 41, task 4: SC-sup check — is component support constant on
EVERY component fiber (not just split ones)?

For each (m, q) with q enumerable: enumerate ker(H mod q) via the
wave-16 SNF kernel, group points into component fibers (sorted
multiset), compute the component-support mask (wave-16 torsion
criterion), and report any PARTIAL fiber (0 < n_supp < size).
Also verifies support is constant on dihedral orbits (sanity:
partial unsplit fibers would refute Gamma-invariance of support).

Usage: python3 wave41_SCsup_check.py m1 m2 ... (each m checked at
every prime-power divisor q of D_m up to ENUM_CAP).
"""
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import (  # noqa: E402
    Dm, comp_supported, gamma_perms, group_ids, lex_canon, snf_kernel,
    torsion_data,
)

ENUM_CAP = 2_000_000


def check_m(m):
    D = Dm(m)
    fac = sp.factorint(D)
    qs = [p ** e for p, e in fac.items()]
    Z, Qmod = torsion_data(m, D)
    perms = gamma_perms(m)
    print(f"== m={m} D_digits={len(str(D))} qs={qs} |V4|={len(Z)}", flush=True)
    grand_partial = 0
    for q in qs:
        if q > ENUM_CAP:
            print(f"   q={q}: SKIP (too large)", flush=True)
            continue
        pts = snf_kernel(m, q)
        assert len(pts) == q
        fib = group_ids(np.sort(pts, axis=1))
        sup = comp_supported(pts, Z, Qmod, q)
        n_fib = int(fib.max()) + 1
        # per-fiber support counts
        sizes = np.bincount(fib, minlength=n_fib)
        supc = np.bincount(fib, weights=sup.astype(np.int64), minlength=n_fib)
        partial = np.where((supc > 0) & (supc < sizes))[0]
        # split fibers and orbit-constancy only when cheap
        if q <= 10000:
            gam = group_ids(lex_canon(pts, perms))
            n_gam = int(gam.max()) + 1
            gsizes = np.bincount(gam, minlength=n_gam)
            gsupc = np.bincount(gam, weights=sup.astype(np.int64), minlength=n_gam)
            bad_orbit = np.where((gsupc > 0) & (gsupc < gsizes))[0]
            gam_fiber = np.empty(n_gam, dtype=np.int64)
            gam_fiber[gam] = fib
            opf = np.bincount(gam_fiber, minlength=n_fib)
            n_split = int((opf > 1).sum())
            split_partial = [int(f) for f in partial if opf[f] > 1]
        else:
            bad_orbit, n_split, split_partial, opf = [], -1, [], None
        print(f"   q={q}: pts={q} fibers={n_fib} split={n_split} "
              f"supp={int(sup.sum())} PARTIAL={len(partial)} "
              f"(split-partial={len(split_partial)}) "
              f"bad_orbits={len(bad_orbit)}", flush=True)
        for f in partial[:20]:
            print(f"      PARTIAL fiber id={int(f)} size={int(sizes[f])} "
                  f"n_supp={int(supc[f])}",
                  flush=True)
        grand_partial += len(partial)
    print(f"== m={m}: TOTAL PARTIAL FIBERS = {grand_partial}", flush=True)
    return grand_partial


if __name__ == "__main__":
    total = 0
    for m in [int(a) for a in sys.argv[1:]]:
        total += check_m(m)
    print(f"GRAND TOTAL PARTIAL = {total}", flush=True)
