"""Wave 41, task 4: mechanism probe for SC-sup at 2-part components.

For each split fiber at (m, q=2-part): take one representative per
dihedral orbit and compare across orbits:
  - t = H y / q (exact integer vector),
  - v.t mod 4 for every torsion rep v (the support conditions),
  - sorted multiset of t, residue-class sums of t mod 4, sum t.
Question: what is equal across orbits of one fiber, and does it
explain why support is constant on the fiber?
"""
import sys

import numpy as np
import sympy as sp

sys.path.insert(0, ".")
from wave16_d1a_targeted import (  # noqa: E402
    Dm, comp_supported, gamma_perms, group_ids, lex_canon, snf_kernel,
    torsion_data,
)


def Hvec(y):
    return 6 * y - np.roll(y, 1) - np.roll(y, -1)


def explore(m, q):
    D = Dm(m)
    Z, Qmod = torsion_data(m, D)
    perms = gamma_perms(m)
    pts = snf_kernel(m, q)
    fib = group_ids(np.sort(pts, axis=1))
    gam = group_ids(lex_canon(pts, perms))
    sup = comp_supported(pts, Z, Qmod, q)
    n_fib = int(fib.max()) + 1
    n_gam = int(gam.max()) + 1
    gam_fiber = np.empty(n_gam, dtype=np.int64)
    gam_fiber[gam] = fib
    opf = np.bincount(gam_fiber, minlength=n_fib)
    print(f"== m={m} q={q} |V4|={len(Z)}", flush=True)
    for f in np.where(opf > 1)[0]:
        idx = np.where(fib == f)[0]
        orbits = sorted(set(gam[idx].tolist()))
        reps = [idx[gam[idx] == g][0] for g in orbits]
        print(f"  fiber {int(f)} size={len(idx)} orbits={len(orbits)} "
              f"supp={int(sup[idx].sum())}/{len(idx)}", flush=True)
        for r, rep in enumerate(reps):
            y = pts[rep]
            Hy = Hvec(y)
            assert np.all(Hy % q == 0)
            t = Hy // q
            vt = [int((Z[k] @ t) % 4) for k in range(len(Z))]
            # RHS values R(v) = 2*(z.v) mod 4, from Qmod: need z.v;
            # recompute z = Hv/4 from torsion_data internals is not
            # exported, so just report vt vector and t statistics.
            rsums = [int(t[i::4].sum() % 4) for i in range(4)]
            print(f"    orbit{r} y0={int(y[0])} y1={int(y[1])} "
                  f"sup={bool(sup[rep])} vt_mod4={vt} "
                  f"t_ressums_mod4={rsums} sum_t={int(t.sum())} "
                  f"t_multiset_sorted={sorted(t.tolist())[:12]}...",
                  flush=True)


if __name__ == "__main__":
    for m, q in [(16, 2048), (32, 8192)]:
        explore(m, q)
