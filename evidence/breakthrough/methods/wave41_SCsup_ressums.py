"""Wave 41, task 4: are the residue-class sums S_r(y) = sum_{i=r mod 4} y_i
fiber-constant? If yes (mod q), and support is a condition on the S_r,
that would explain SC-sup at the 2-part. Prints, per split fiber, the
S_r tuples (mod q) of one representative per orbit.
"""
import sys

import numpy as np

sys.path.insert(0, ".")
from wave16_d1a_targeted import (  # noqa: E402
    Dm, comp_supported, gamma_perms, group_ids, lex_canon, snf_kernel,
    torsion_data,
)


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
    print(f"== m={m} q={q}", flush=True)
    n_const = n_var = 0
    for f in np.where(opf > 1)[0]:
        idx = np.where(fib == f)[0]
        orbits = sorted(set(gam[idx].tolist()))
        reps = [idx[gam[idx] == g][0] for g in orbits]
        tuples = []
        for rep in reps:
            y = pts[rep]
            s = tuple(int(y[r::4].sum() % q) for r in range(4))
            tuples.append(s)
        const = len(set(tuples)) == 1
        n_const += const
        n_var += (not const)
        print(f"  fiber {int(f)} supp={int(sup[idx].sum())}/{len(idx)} "
              f"S_r_const={const} tuples={tuples}", flush=True)
    print(f"  split fibers: S_r constant {n_const}, varying {n_var}", flush=True)


if __name__ == "__main__":
    explore(16, 2048)
    explore(32, 8192)
