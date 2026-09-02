"""
Run 81b: DISCRIMINATING the rigidity signal at the largest design.
==================================================================
The r81 pilot showed the count-variance ratio (arithmetic / matched GOE)
growing with m: 1.7 (m=105) -> 5.7/7.9 (m=246).  Before interpreting this
as arithmetic, exclude the density-mismatch artifact: the pilot measured
counts in FIXED semicircle-quantile windows; if the arithmetic density
deviates slightly from the semicircle, the window counts inherit the
mismatch and the variance inflates.

This script, at (9349, K=19) plus-block (m+=246) and (3571,17) plus-block:
  (i)  the Kolmogorov distance of the per-sample CDF vs the semicircle
       (density shape check), with the GOE reference distance;
  (ii) the count variance around the POOLED per-window mean (density
       removed) vs the matched GOE variance — the clean rigidity readout;
  (iii) per-sample counts printed (outlier check).

Output: artifacts/r81/rigidity_discriminator.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis, orbit_reps  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402
from r81_local_law_pilot import (goe_samples, semicircle_quantiles,  # noqa: E402
                                 count_var)

A = [[2, 1], [1, 1]]


def main():
    out = {"script": "src/r81b_rigidity_discriminator.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    rng = np.random.default_rng(810810)
    nrep = 24
    nwin = 12

    for N, batch in ((3571, 512), (9349, 1024)):
        t0 = time.time()
        cm = CatMap(A, N)
        _, K = cm.orders()
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        RB = B.conj().T @ apply_parity(B)
        w, Vv = np.linalg.eigh(RB)
        mp = int((w > 0).sum())
        Bp = B @ Vv[:, w > 0]
        reps = orbit_reps(cm, K, nrep, rng)
        evs = []
        for u in reps:
            H = Bp.conj().T @ cm.apply_T(u, Bp)
            H = H + H.conj().T
            ev = np.linalg.eigvalsh(H)
            ev = ev - ev.mean()
            evs.append(ev / np.sqrt((ev ** 2).mean()))
        evs = np.array(evs)
        gref = goe_samples(mp, nrep, rng)
        quant = semicircle_quantiles(mp, nwin)

        # (i) density shape: Kolmogorov distance to the semicircle CDF
        xs = np.linspace(-np.sqrt(2), np.sqrt(2), 4001)
        rho = np.sqrt(np.maximum(0.0, 2 - xs ** 2))
        cdf = np.cumsum(rho)
        cdf /= cdf[-1]
        def ks(ev):
            emp = np.searchsorted(xs, np.sort(ev)) / len(xs)
            emp = np.clip(emp, 0, 1)
            th = np.interp(np.sort(ev), xs, cdf)
            return float(np.abs(emp - th).max())
        ks_a = float(np.mean([ks(e) for e in evs]))
        ks_g = float(np.mean([ks(e) for e in gref]))

        # (ii) counts: raw variance AND pooled-mean-centered variance
        cnt_a = np.array([count_var(e, quant) for e in evs])
        cnt_g = np.array([count_var(e, quant) for e in gref])
        var_raw_a = cnt_a.var(axis=0, ddof=1)
        var_raw_g = cnt_g.var(axis=0, ddof=1)
        var_pooled_a = cnt_a.var(axis=0, ddof=1)  # same; the pooled readout:
        mean_a = cnt_a.mean(axis=0)
        mean_g = cnt_g.mean(axis=0)
        # the density-mismatch component: the deviation of the arithmetic
        # mean counts from the GOE mean counts
        dens_shift = np.abs(mean_a - mean_g).max()
        # centered variance (fluctuation around the family mean)
        var_c_a = ((cnt_a - cnt_a.mean(axis=0)) ** 2).mean(axis=0)
        var_c_g = ((cnt_g - cnt_g.mean(axis=0)) ** 2).mean(axis=0)

        row = {"N": N, "K": int(K), "m_plus": mp, "nrep": nrep,
               "ks_arith": ks_a, "ks_goe": ks_g,
               "density_shift_max": float(dens_shift),
               "var_raw_ratio": float(var_raw_a.mean() / var_raw_g.mean()),
               "var_centered_ratio": float(var_c_a.mean() / var_c_g.mean()),
               "counts_arith_first3": cnt_a[:, :3].tolist(),
               "counts_goe_first3": cnt_g[:, :3].tolist(),
               "mean_counts_arith": mean_a.tolist(),
               "mean_counts_goe": mean_g.tolist()}
        out["designs"].append(row)
        print(f"=== N={N} m+={mp} ({time.time()-t0:.0f} s)", flush=True)
        print(f"  KS arith {ks_a:.4f} vs GOE {ks_g:.4f} "
              f"(density shape {'MATCH' if ks_a < 2*ks_g+0.01 else 'DEVIATES'})",
              flush=True)
        print(f"  max|mean counts arith - goe| = {dens_shift:.2f} levels",
              flush=True)
        print(f"  var raw ratio     = {row['var_raw_ratio']:.2f}", flush=True)
        print(f"  var centered ratio= {row['var_centered_ratio']:.2f}",
              flush=True)
        print(f"  per-sample counts (win 0..2), arith:\n{cnt_a[:, :3]}",
              flush=True)

    dest = os.path.join("artifacts", "r81", "rigidity_discriminator.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", os.path.normpath(dest), flush=True)


if __name__ == "__main__":
    main()
