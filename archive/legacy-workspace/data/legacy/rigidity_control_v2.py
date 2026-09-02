"""
Run 82p: IS THE LONG-RANGE EXCESS RIGIDITY REAL, OR AN UNFOLDING ARTIFACT?
========================================================================
R82.18 (src/r82o_rigidity_long_range.py) found, at m_+ = 837 over 48 systems
against 192 matched GOE samples, that the arithmetic spectra are systematically
MORE rigid than GOE at long range:

    Sigma^2(L):  z = -1.5 (L=5), -2.3 (L=12), -2.5 (L=20), -2.6 (L=30), -2.2 (L=50)
    Delta_3(L):  z = +0.9 (L=5), -1.7 (L=12), -2.4 (L=20), -3.3 (L=30), -3.6 (L=50)

This is the OPPOSITE sign from the arithmetic-chaos scenario (where long-range
rigidity is LOST towards Poisson), so it would be a genuinely new phenomenon --
which is exactly why it must be attacked as a suspected artifact first.

The suspect is the unfolding.  Both families are unfolded by a per-sample
polynomial fit of the integrated density; a fit of degree `d` can absorb
fluctuations on scales `~n/d` levels, so at `L` comparable to that it suppresses
`Sigma^2` -- visibly so, since the GOE Monte Carlo itself falls below the GOE
asymptote at L = 50 (1.1446 vs 1.2348).  If the arithmetic spectra are better
fitted by a low-degree polynomial than GOE spectra are -- plausible, since the
arithmetic macroscopic density is a smooth function of `q` (18.5) whereas a GOE
sample's density has its own random wiggle -- the arithmetic `Sigma^2` is
suppressed MORE, producing exactly this signature with no physics behind it.

DISCRIMINATOR: sweep the unfolding degree `d = 4, 6, 8, 11, 15` on the SAME
spectra.  An artifact must weaken as `d` decreases (less absorption); a real
excess rigidity must survive, and its `z` should be roughly `d`-independent.
Also reported: the per-sample residual of the fit for both families, which
measures the absorption directly.

Output: artifacts/r82/rigidity_control.json  (+ spectra cached to
artifacts/r82/rigidity_spectra.npz for any further analysis)
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r82k_bgs_large_m import build_M, design_params, goe_reference  # noqa: E402

LS = (5, 12, 20, 30, 50)
DEGS = (4, 6, 8, 11, 15)


def unfold_deg(ev, deg):
    ev = np.sort(np.asarray(ev, dtype=float))
    n = len(ev)
    y = np.arange(1, n + 1) - 0.5
    cf = np.polyfit(ev, y, deg)
    u = np.polyval(cf, ev)
    resid = float(np.sqrt(((y - u) ** 2).mean()))
    return u, resid


def sigma2_delta3(u, cut=0.15, nwin=600, rng=None):
    n = len(u)
    lo, hi = int(cut * n), int((1 - cut) * n)
    x = u[lo:hi]
    s2, d3 = {}, {}
    for L in LS:
        a, b = x.min(), x.max()
        if b - a <= 2 * L:
            s2[L] = d3[L] = np.nan
            continue
        cs = rng.uniform(a + L / 2, b - L / 2, nwin)
        cnt = np.empty(nwin)
        dev = np.empty(nwin)
        for i, c in enumerate(cs):
            sel = x[(x >= c - L / 2) & (x < c + L / 2)]
            cnt[i] = len(sel)
            if len(sel) >= 3:
                t = sel - (c - L / 2)
                yy = np.arange(1, len(sel) + 1) - 0.5
                A = np.column_stack([np.ones_like(t), t])
                coef, *_ = np.linalg.lstsq(A, yy, rcond=None)
                dev[i] = ((yy - A @ coef) ** 2).mean()
            else:
                dev[i] = np.nan
        s2[L] = float(cnt.var(ddof=1))
        d3[L] = float(np.nanmean(dev))
    return s2, d3


def main():
    rng = np.random.default_rng(820015)
    N, K, nq, goe_mult = 95419, 57, 48, 4
    a = design_params(N, K)
    m = (N - 1) // (2 * K)
    t0 = time.time()
    print(f"=== N={N} K={K} m+={m}: building {nq} arithmetic spectra", flush=True)
    EA = []
    for i in range(nq):
        q = int(rng.integers(1, N))
        M, _ = build_M(N, K, a, q)
        EA.append(np.linalg.eigvalsh(M))
        if (i + 1) % 12 == 0:
            print(f"   {i+1}/{nq} ({time.time()-t0:.0f} s)", flush=True)
    EG = goe_reference(m, nq * goe_mult, rng)
    print(f"   GOE reference built ({time.time()-t0:.0f} s)", flush=True)
    np.savez_compressed(
        os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                     "artifacts", "r82", "rigidity_spectra.npz"),
        arith=np.array(EA), goe=np.array(EG))

    out = {"script": "src/r82p_rigidity_control.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "N": N, "K": K, "m_plus": m, "nq": nq, "n_goe": nq * goe_mult,
           "degrees": list(DEGS), "L": list(LS), "sweep": []}
    for deg in DEGS:
        ua = [unfold_deg(e, deg) for e in EA]
        ug = [unfold_deg(e, deg) for e in EG]
        ra = float(np.mean([r for _, r in ua]))
        rg = float(np.mean([r for _, r in ug]))
        SA = [sigma2_delta3(u, rng=rng) for u, _ in ua]
        SG = [sigma2_delta3(u, rng=rng) for u, _ in ug]

        def agg(lst, idx, L):
            v = np.array([d[idx][L] for d in lst], dtype=float)
            v = v[np.isfinite(v)]
            return float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v)))

        row = {"degree": deg, "fit_resid_arith": ra, "fit_resid_goe": rg,
               "sigma2": {}, "delta3": {}}
        line2, line3 = [], []
        for L in LS:
            ma, sa = agg(SA, 0, L)
            mg, sg = agg(SG, 0, L)
            z = (ma - mg) / np.hypot(sa, sg)
            row["sigma2"][str(L)] = {"arith": ma, "goe": mg, "z": float(z)}
            line2.append(f"L={L}: {z:+.2f}")
            ma, sa = agg(SA, 1, L)
            mg, sg = agg(SG, 1, L)
            z = (ma - mg) / np.hypot(sa, sg)
            row["delta3"][str(L)] = {"arith": ma, "goe": mg, "z": float(z)}
            line3.append(f"L={L}: {z:+.2f}")
        out["sweep"].append(row)
        print(f"  deg={deg:2d}  fit resid arith {ra:.4f} / GOE {rg:.4f}   "
              f"Sigma^2 z: " + "  ".join(line2), flush=True)
        print(f"           " + " " * 32 + "Delta_3 z: " + "  ".join(line3),
              flush=True)
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "rigidity_control.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
