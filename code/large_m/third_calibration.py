r"""RUN 93.2 -- Third calibration of the coupled energy at N=3571 via the
permutation-gather trick.

**RETRACTED IN R108 (2026-09-02).**  The class-1 loop below originally
used INNER fancy-indexing (Dp = dg_flat[U2-1, V2-1]), which pairs the
partner's u-coordinate with the COLUMN index (v1) instead of the row
index (u1) -- producing a wrong coupled energy (3.545e15 instead of the
true 4.459482e15; delta = -6.9% instead of +17.65%).  The bug is fixed
below (outer indexing via np.ix_, as the docstring always intended),
but the R93/R95 papers and tables citing the old number are corrected
separately (see docs/REVIEW_R108.md and HISTORY RUN 108).  This script
is kept for provenance; the certified values come from
code/referee/r108_k4_independent.py and r108b_direct3571.py.

B(t) = sum over coupled key pairs (p1,p2): u1*u2 in H, v1*v2 in H,
d(p1)+d(p2) = t of n1*n2.  For each (t1,t2) in H^2, the partner of the
grid point (u1,v1) is (t1/u1, t2/v1) -- a PERMUTATION of the grid.  So the
contribution of the (t1,t2) class to B is the histogram of
(d(p1) + d(perm(p1))) over valid grid points, computed by fancy-indexing
the 2D difference grid.  H^2 = 289 classes, each O(N^2) numpy work.

Weights: all grid points have n=1 EXCEPT the diagonal key (1,1) which
carries n = N-2 (pairs x=y).  The diagonal point (u=v=1) is excluded from
the grid (u=v masked); handle its couplings separately: coupling of (1,1)
with (u2,v2) requires u2 in H AND v2 in H (since 1*u2 = u2 must lie in
H, and likewise v2).  Class-2/3 below implement this correctly.

Output: artifacts/r93/sigma4_third_calibration.json
"""
import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "src", "large_m"))
sys.path.insert(0, os.path.join(ROOT, "src", "theorems"))

from theorem_ii_twisted_jacobi import (  # noqa: E402
    primitive_root, sqrt_mod, multiplicative_order,
)

OUT_DIR = os.path.join(ROOT, "artifacts", "r93")


def main():
    t00 = time.time()
    N = 3571
    K = 17
    roots = [r for r in sqrt_mod(5, N)]
    inv2 = pow(2, N - 2, N)
    a = None
    for r in roots:
        cnd = (3 + r) * inv2 % N
        if multiplicative_order(cnd, N) == K:
            a = cnd
            break
    g = primitive_root(N)
    h = pow(g, (N - 1) // K, N)
    H = sorted(pow(h, i, N) for i in range(K))
    Hset = set(H)

    Dgrid = np.load(os.path.join(OUT_DIR, "Dgrid_N3571.npy"))
    valid = np.load(os.path.join(OUT_DIR, "valid_N3571.npy"))
    uu = np.arange(1, N, dtype=np.int64)
    inv_arr = np.array([0] + [int(pow(i, N - 2, N)) for i in range(1, N)],
                       dtype=np.int64)

    # weights grid: n = 1 everywhere valid; the key (1,1) is NOT on the grid
    # (u=v masked) — it represents the N-2 diagonal pairs (x,x), all with
    # d=0, and couples with every key (u2,v2) [1*u2=u2, 1*v2=v2 — need
    # u2 in H? NO: coupling of (1,1) with (u2,v2) is u1u2 = u2 in H and
    # v1v2 = v2 in H — requires u2, v2 in H individually!]
    # Correct: (1,1)-(u2,v2) coupled iff u2 in H AND v2 in H.
    # (1,1)-(1,1): coupled, contributes (N-2)^2 at t=0.
    # Off-grid-diagonal couplings (u1=v1 i.e. u1=v1 != 1): no pair exists.

    # Precompute the H-subgrid mask: points (u,v) with u in H and v in H.
    hmask = np.zeros((N - 1, N - 1), dtype=bool)
    hidx = {hh: i for i, hh in enumerate(H)}
    hh_arr = np.array(H, dtype=np.int64)
    umask = np.zeros(N, dtype=bool)
    for hh in H:
        umask[hh] = True
    HM = umask[uu][:, None] & umask[uu][None, :] & valid

    B = np.zeros(N, dtype=np.int64)

    # --- class 1: both keys off-diagonal (u1 != v1, u2 != v2) ---
    # iterate (t1,t2) in H^2: partner of (u1,v1) is (t1/u1, t2/v1)
    print("class 1: H^2 permutation classes", flush=True)
    dsum_hist = np.zeros(N, dtype=np.int64)
    dg_flat = Dgrid
    val_flat = valid
    for t1 in H:
        for t2 in H:
            # partner u2 = t1 * inv(u1), v2 = t2 * inv(v1); grid is indexed
            # by 1..N-1 -> shift by -1.  OUTER indexing (np.ix_) so that
            # Dp[i, j] = d(t1/uu[i], t2/uu[j]) -- the partner of the grid
            # point (u1,v1) = (uu[i], uu[j]) takes u2 from the ROW index
            # and v2 from the COLUMN index.  (R108 fix: the original
            # inner indexing Dp = dg_flat[U2-1, V2-1] wrongly used the
            # column index for both coordinates.)
            U2 = (t1 * inv_arr[uu]) % N   # values in 1..N-1
            V2 = (t2 * inv_arr[uu]) % N
            ix = np.ix_(U2 - 1, V2 - 1)
            Dp = dg_flat[ix]
            Vp = val_flat[ix]
            both = valid & Vp
            if not both.any():
                continue
            dsum = (dg_flat + Dp) % N
            idx = dsum[both]
            np.add.at(B, idx, 1)
    print(f"  class-1 done t={time.time()-t00:.0f}s", flush=True)

    # --- class 2: diagonal key (1,1) with off-diagonal partners ---
    # coupled iff u2 in H and v2 in H; d1 = 0; contribution (N-2) * 1
    # at t = d2 for each HxH point (u2,v2) valid.
    diag_d = Dgrid[HM]
    np.add.at(B, diag_d % N, N - 2)
    # --- class 3: (1,1) with itself ---
    B[0] += (N - 2) ** 2
    # deduplicate: class-1 counted (1,1) pairs? (1,1) is not on the grid
    # (u=v), so no double counting. But class-2 added each HxH point once,
    # and class-3 once. Good.

    V4 = int(B.sum())
    Z0 = int(B[0])
    second = int((B.astype(np.int64) ** 2).sum())
    mean = (N * Z0 - V4) / (N - 1)
    var_excl0 = (N * second - V4 ** 2) / (N - 1) - mean ** 2
    std = math.sqrt(max(var_excl0, 0))

    print(f"|V4| = {V4}")
    print(f"Z0 = {Z0}")
    print(f"mean Sigma_4 (q=1..N-1) = {mean:.2f}")
    print(f"std Sigma_4 = {std:.1f}")
    print(f"rel std = {std/mean:.4f}")
    print(f"wall = {time.time()-t00:.0f}s")

    out = {
        "run": "93.2",
        "design": {"N": N, "a": a, "K": K,
                   "m": (N - 1) // K},
        "V4": V4, "Z0": Z0,
        "mean_Sigma4": mean, "std_Sigma4": std,
        "rel_std": std / mean,
        "E_coupled": second,
        "E_over_N3": second / N ** 3,
        "wall_s": time.time() - t00,
    }
    with open(os.path.join(OUT_DIR, "sigma4_third_calibration.json"), "w",
              encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact written")


if __name__ == "__main__":
    main()
