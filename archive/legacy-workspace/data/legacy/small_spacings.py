"""
Run 82r: SYMMETRIC-SQUARE vs EXTERIOR-SQUARE TEST -- a symmetry-class check
that does not need the eigenvector phases.
==========================================================================
The programme's claim is beta = 1 (GOE class) for the parity blocks (Theorems
C/D/E: Theta^2 = +1, the block is unitarily a real symmetric matrix).  The
standard model-independent test of the symmetry class -- the Dyson-Mehta
three-level cluster function, or the symmetric-square statistic -- avoids
eigenvector phase conventions entirely:

For a beta = 1 (orthogonal) ensemble the two-level correlation in the bulk is

    R_2(s) = 1 - (sin pi s / (pi s))^2 - (Si(pi s) + ... )' (the GOE kernel),

and a sharp, model-free discriminator between beta = 1 and beta = 2 is the
number of eigenvalue PAIRS at spacings below the mean level spacing:

    N_pairs(t) = #{(i<j): |lam_i - lam_j| < t * <spacing>},  t < 1,

which is O(1) per spectrum for a random-matrix spectrum (level repulsion) and
grows linearly for a spectrum with coincidences.  This is exactly the statistic
that distinguishes GOE (strong repulsion) from the degenerate/arithmetic case.

Even sharper and fully canonical: compare the SECOND moment of the spectrum
against the second moment of the symmetric square of a GOE sample in the same
scaling, or the "min-spacing" distribution.

For the arithmetic family the interesting question is whether V_q -- known to be
GOE at the NN and L <= 50 scale (R82.14/R82.18) -- also shows GOE-level
repulsion at the smallest scales, i.e. no exceptional near-degeneracies beyond
what GOE itself produces.  Any EXCESS of tiny spacings would be the signature of
hidden degeneracies (e.g. the T(n) and T(-n) blocks sharing spectra), which
would be the one structural way BGS could fail here while all the aggregate
statistics still look GOE.

Measured: the distribution of normalised near-zero spacings
s_min, s_{2nd smallest}, and N_pairs(t) for t in {0.05, 0.1, 0.2} over many
systems, against matched GOE.

Output: artifacts/r82/small_spacings.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r82k_bgs_large_m import build_M, design_params, goe_reference  # noqa: E402


def bulk_spacings(ev, cut=0.15):
    ev = np.sort(ev)
    n = len(ev)
    lo, hi = int(cut * n), int((1 - cut) * n)
    s = np.diff(ev[lo:hi])
    return s / s.mean()


def small_spacing_stats(sp, ts=(0.02, 0.05, 0.1, 0.2)):
    sp = np.sort(sp)
    return {"min": float(sp[0]), "second": float(sp[1]),
            "third": float(sp[2]),
            "n_below": {str(t): int((sp < t).sum()) for t in ts}}


def main():
    rng = np.random.default_rng(820016)
    out = {"script": "src/r82r_small_spacings.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, K, nq in ((3571, 17, 96), (95419, 57, 48), (144481, 43, 16)):
        t0 = time.time()
        a = design_params(N, K)
        m = (N - 1) // (2 * K)
        stats_a, mins_a, secs_a = [], [], []
        for i in range(nq):
            q = int(rng.integers(1, N))
            M, _ = build_M(N, K, a, q)
            sp = bulk_spacings(np.linalg.eigvalsh(M))
            st = small_spacing_stats(sp)
            stats_a.append(st)
            mins_a.append(st["min"])
            secs_a.append(st["second"])
        gref = goe_reference(m, nq, rng)
        stats_g, mins_g, secs_g = [], [], []
        for ev in gref:
            sp = bulk_spacings(ev)
            st = small_spacing_stats(sp)
            stats_g.append(st)
            mins_g.append(st["min"])
            secs_g.append(st["second"])
        row = {"N": N, "K": K, "m_plus": m, "nq": nq, "n_goe": nq}
        for key, va, vg in (("min", mins_a, mins_g), ("second", secs_a, secs_g)):
            ma, sa = float(np.mean(va)), float(np.std(va, ddof=1) / np.sqrt(nq))
            mg, sg = float(np.mean(vg)), float(np.std(vg, ddof=1) / np.sqrt(nq))
            row[key] = {"arith": ma, "arith_se": sa, "goe": mg, "goe_se": sg,
                        "z": (ma - mg) / np.hypot(sa, sg)}
            print(f"  N={N} {key:6s} spacing: arith {ma:.5f} +- {sa:.5f} | "
                  f"GOE {mg:.5f} +- {sg:.5f} | z = {row[key]['z']:+.2f}",
                  flush=True)
        for t in ("0.02", "0.05", "0.1", "0.2"):
            va = [s["n_below"][t] for s in stats_a]
            vg = [s["n_below"][t] for s in stats_g]
            ma, sa = float(np.mean(va)), float(np.std(va, ddof=1) / np.sqrt(nq))
            mg, sg = float(np.mean(vg)), float(np.std(vg, ddof=1) / np.sqrt(nq))
            row[f"n_below_{t}"] = {"arith": ma, "goe": mg,
                                   "z": (ma - mg) / np.hypot(sa, sg)}
            print(f"  N={N} #spacings<{t}: arith {ma:.2f} +- {sa:.2f} | GOE "
                  f"{mg:.2f} +- {sg:.2f} | z = {row[f'n_below_{t}']['z']:+.2f}",
                  flush=True)
        # extreme-value check: the smallest spacing ever seen vs GOE's
        row["min_ever_arith"] = float(min(mins_a))
        row["min_ever_goe"] = float(min(mins_g))
        print(f"  N={N} smallest spacing ever: arith {min(mins_a):.5f} | GOE "
              f"{min(mins_g):.5f}   [{time.time()-t0:.0f} s]", flush=True)
        out["designs"].append(row)
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "small_spacings.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
