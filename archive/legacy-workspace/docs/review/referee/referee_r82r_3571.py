"""Referee reproduction of src/r82r_small_spacings.py, design 1 only
(N=3571, K=17, nq=96).  Same seed (820016) and same draw order as the
canonical main(), so the numbers must match the canonical artifact's first
design row exactly.  Imports the canonical functions; no logic re-implemented.
"""
import json
import os
import sys
import time

import numpy as np

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC)
from r82r_small_spacings import bulk_spacings, small_spacing_stats  # noqa: E402
from r82k_bgs_large_m import build_M, design_params, goe_reference  # noqa: E402


def main():
    rng = np.random.default_rng(820016)
    N, K, nq = 3571, 17, 96
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
              f"GOE {mg:.5f} +- {sg:.5f} | z = {row[key]['z']:+.2f}", flush=True)
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
    row["min_ever_arith"] = float(min(mins_a))
    row["min_ever_goe"] = float(min(mins_g))
    print(f"  N={N} smallest spacing ever: arith {min(mins_a):.5f} | GOE "
          f"{min(mins_g):.5f}   [{time.time()-t0:.0f} s]", flush=True)
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "referee_small_spacings_3571.json")
    with open(dest, "w") as fh:
        json.dump(row, fh, indent=1)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
