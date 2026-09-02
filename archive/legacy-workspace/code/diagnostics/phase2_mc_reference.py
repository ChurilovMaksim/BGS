"""PHASE 2b: beta-discrimination vs MC reference ensembles built at
the SAME multiplet dimensions as the data (m~70 and m~213)."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import os, json
import numpy as np

ART = _BGS_ROOT + r"\artifacts"
DATA_DIMS = [70, 213]          # observed multiplet sizes
TRIALS = {70: 3000, 213: 900}  # trials per ensemble per dim


def pool(ens, m, trials, rng):
    out = np.empty(trials * (m - 1), dtype=np.float64)
    buf = np.empty(m - 1)
    for t in range(trials):
        X = rng.standard_normal((m, m))
        if ens == "GOE":
            M = (X + X.T) / 2.0
        else:
            Y = rng.standard_normal((m, m))
            M = (X + X.T) / 2.0 + 1j * (Y - Y.T) / 2.0  # Hermitian by construction
        ev = np.linalg.eigvalsh(M)
        d = np.diff(ev)
        d /= d.mean()
        out[t * (m - 1):(t + 1) * (m - 1)] = d
    return np.sort(out)


def ks2(s_sorted, r_sorted):
    grid = np.concatenate([r_sorted[::max(1, len(r_sorted)//200000)],
                           s_sorted])
    grid = np.sort(grid)
    cr = np.searchsorted(r_sorted, grid, side="right") / len(r_sorted)
    cs = np.searchsorted(s_sorted, grid, side="right") / len(s_sorted)
    return float(np.max(np.abs(cr - cs)))


def main():
    s = np.load(os.path.join(ART, "phase2_spacings.npy"))
    s = np.sort(s)
    rng = np.random.default_rng(20260827)
    refs = {}
    for ens in ("GOE", "GUE"):
        parts = [pool(ens, m, TRIALS[m], rng) for m in DATA_DIMS]
        refs[ens] = np.sort(np.concatenate(parts))
        print(f"{ens} reference: {len(refs[ens])} spacings")
    k_goe = ks2(s, refs["GOE"])
    k_gue = ks2(s, refs["GUE"])
    n_ref = min(len(refs["GOE"]), len(refs["GUE"]))
    crit = 1.36 * float(np.sqrt(1.0 / len(s) + 1.0 / n_ref))
    gap = abs(k_goe - k_gue)
    closer = "GOE" if k_goe < k_gue else "GUE"
    print(f"\nDATA n={len(s)}: KS_vs_GOE={k_goe:.5f} "
          f"KS_vs_GUE={k_gue:.5f}")
    print(f"gap={gap:.5f}  crit(5%)={crit:.5f}  -> closer={closer}; "
          f"{'RESOLVED' if gap > crit else 'not resolved'}")
    json.dump(dict(data_n=int(len(s)),
                   ref_sizes={e: int(len(refs[e])) for e in refs},
                   ks_vs_goe=k_goe, ks_vs_gue=k_gue,
                   gap=gap, crit=crit, closer=closer,
                   resolved=bool(gap > crit)),
              open(os.path.join(ART, "phase2_beta.json"), "w"),
              indent=1)
    print("saved artifacts/phase2_beta.json")


if __name__ == "__main__":
    main()
