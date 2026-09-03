"""
Run 82o: LONG-RANGE RIGIDITY -- the statistic where arithmetic systems are
known to break from GOE.
========================================================================
For arithmetic hyperbolic surfaces the spectral statistics are POISSON-like
rather than GOE (Bogomolny-Georgeot-Giannoni-Schmit; Bolte-Steil-Steiner), the
mechanism being exponentially degenerate length spectra -- the standard
counterexample to a naive reading of BGS.  Whether the desymmetrised quantum cat
map belongs with the generic chaotic systems or with the arithmetic exceptions is
therefore decided by the LONG-RANGE statistics, not by nearest neighbours: a
system can have Wigner-Dyson spacings and still lose rigidity at larger L.

This run measures, at `m_+ = 837` (48 systems, so ~40 000 levels) and
`m_+ = 1680` (16 systems):

  * the number variance `Sigma^2(L)` for `L` up to 50, against a matched GOE
    Monte Carlo at 4x the sample count AND against the GOE asymptotic form
        Sigma^2_GOE(L) = (2/pi^2)[ln(2 pi L) + gamma + 1 - pi^2/8] + O(1/L),
    with the Poisson value `Sigma^2 = L` as the opposite reference;
  * the Dyson-Mehta rigidity `Delta_3(L)`, whose GOE asymptote is
        Delta_3(L) = (1/pi^2)[ln(2 pi L) + gamma - 5/4 - pi^2/8].
A Poisson-like breakdown would show as `Sigma^2(L)` turning UP towards `L/…`
(saturation) instead of staying logarithmic.

Unfolding: each spectrum is unfolded by its own smooth integrated density
(polynomial fit), which is the standard procedure and is applied identically to
the arithmetic and GOE samples.

Output: artifacts/r82/rigidity_long_range.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from r82k_bgs_large_m import build_M, design_params, goe_reference  # noqa: E402

GAMMA = 0.5772156649015329
LS = (1, 2, 3, 5, 8, 12, 20, 30, 50)


def sigma2_goe_asymptotic(L):
    return (2 / np.pi ** 2) * (np.log(2 * np.pi * L) + GAMMA + 1 - np.pi ** 2 / 8)


def delta3_goe_asymptotic(L):
    return (1 / np.pi ** 2) * (np.log(2 * np.pi * L) + GAMMA - 5 / 4 - np.pi ** 2 / 8)


def unfold(ev, deg=None):
    ev = np.sort(np.asarray(ev, dtype=float))
    n = len(ev)
    if deg is None:
        deg = min(11, max(4, n // 60))
    cf = np.polyfit(ev, np.arange(1, n + 1) - 0.5, deg)
    return np.polyval(cf, ev)


def stats_from_unfolded(u, cut=0.15, nwin=600, rng=None):
    """Sigma^2(L) and Delta_3(L) on the bulk of one unfolded spectrum."""
    n = len(u)
    lo, hi = int(cut * n), int((1 - cut) * n)
    x = u[lo:hi]
    s2, d3 = {}, {}
    for L in LS:
        a, b = x.min(), x.max()
        if b - a <= 2 * L:
            s2[L] = np.nan
            d3[L] = np.nan
            continue
        cs = rng.uniform(a + L / 2, b - L / 2, nwin)
        cnt = np.empty(nwin)
        dev = np.empty(nwin)
        for i, c in enumerate(cs):
            sel = x[(x >= c - L / 2) & (x < c + L / 2)]
            cnt[i] = len(sel)
            if len(sel) >= 3:
                t = (sel - (c - L / 2))
                y = np.arange(1, len(sel) + 1) - 0.5
                A = np.column_stack([np.ones_like(t), t])
                coef, *_ = np.linalg.lstsq(A, y, rcond=None)
                dev[i] = ((y - A @ coef) ** 2).mean()
            else:
                dev[i] = np.nan
        s2[L] = float(cnt.var(ddof=1))
        d3[L] = float(np.nanmean(dev))
    return s2, d3


def design(N, K, nq, rng, goe_mult=4, block=8192):
    t0 = time.time()
    a = design_params(N, K)
    m = (N - 1) // (2 * K)
    print(f"=== N={N} K={K} m+={m}  nq={nq}", flush=True)
    S2a, D3a = [], []
    for i in range(nq):
        q = int(rng.integers(1, N))
        M, _ = build_M(N, K, a, q, block=block)
        u = unfold(np.linalg.eigvalsh(M))
        s2, d3 = stats_from_unfolded(u, rng=rng)
        S2a.append(s2)
        D3a.append(d3)
        if (i + 1) % 8 == 0 or i == 0:
            print(f"   {i+1}/{nq} systems ({time.time()-t0:.0f} s)", flush=True)
    S2g, D3g = [], []
    for ev in goe_reference(m, nq * goe_mult, rng):
        u = unfold(ev)
        s2, d3 = stats_from_unfolded(u, rng=rng)
        S2g.append(s2)
        D3g.append(d3)
    print(f"   GOE reference done ({time.time()-t0:.0f} s)", flush=True)

    def agg(dicts, L):
        v = np.array([d[L] for d in dicts], dtype=float)
        v = v[np.isfinite(v)]
        return float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v)))

    row = {"N": N, "K": K, "m_plus": m, "nq": nq, "n_goe": nq * goe_mult,
           "L": list(LS), "sigma2": {}, "delta3": {}}
    print("     L   Sigma2 arith        Sigma2 GOE MC       GOE asympt  Poisson"
          "   z", flush=True)
    for L in LS:
        ma, sa = agg(S2a, L)
        mg, sg = agg(S2g, L)
        z = (ma - mg) / np.hypot(sa, sg) if np.isfinite(ma) else float("nan")
        row["sigma2"][str(L)] = {"arith": ma, "arith_se": sa, "goe": mg,
                                 "goe_se": sg, "goe_asymptote":
                                 float(sigma2_goe_asymptotic(L)),
                                 "poisson": float(L), "z": float(z)}
        print(f"   {L:3d}   {ma:7.4f} +- {sa:6.4f}   {mg:7.4f} +- {sg:6.4f}   "
              f"{sigma2_goe_asymptotic(L):7.4f}   {L:6.1f}  {z:+6.2f}", flush=True)
    print("     L   Delta3 arith        Delta3 GOE MC       GOE asympt    z",
          flush=True)
    for L in LS:
        ma, sa = agg(D3a, L)
        mg, sg = agg(D3g, L)
        z = (ma - mg) / np.hypot(sa, sg) if np.isfinite(ma) else float("nan")
        row["delta3"][str(L)] = {"arith": ma, "arith_se": sa, "goe": mg,
                                 "goe_se": sg, "goe_asymptote":
                                 float(delta3_goe_asymptotic(L)), "z": float(z)}
        print(f"   {L:3d}   {ma:7.4f} +- {sa:6.4f}   {mg:7.4f} +- {sg:6.4f}   "
              f"{delta3_goe_asymptotic(L):7.4f}   {z:+6.2f}", flush=True)
    row["seconds"] = time.time() - t0
    return row


def main():
    rng = np.random.default_rng(820014)
    out = {"script": "src/r82o_rigidity_long_range.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    plan = [(95419, 57, 48), (144481, 43, 16)]
    for N, K, nq in plan:
        try:
            out["designs"].append(design(N, K, nq, rng))
        except Exception as exc:                       # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "rigidity_long_range.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
