"""
Run 81: THE LOCAL-LAW PILOT (op:local) — the first direct empirical attack
on the resolvent scale for the compressed observable.
==========================================================================
For each design (A=Arnold, N; K = quantum period; m = dim of the lambda
eigenspace) and each of ~10 orbit representatives n:

  * build the parity blocks B_pm of H_lam (Theorems C/E: the comparison
    class is GOE, beta = 1);
  * build the compressed observable H = B_pm^dag (T(n) + T(-n)) B_pm
    (self-adjoint, m_pm x m_pm);
  * rescale the eigenvalues to unit second moment;
  * measure, against a MATCHED GOE MONTE-CARLO REFERENCE (same m, same
    number of samples — no asymptotic formula needed):
      (a) the RIGIDITY signature: Var over samples of the level counts in
          semicircle-quantile windows covering the bulk;
      (b) the STIELTJES deviation: |G(z) - G_GOE(z)| with
          G = (1/m) Tr (H - z)^{-1} at z = i*eta for eta = c/m-scaled
          positions (c = 3, 10, 30 — the local-law window).

The local law for this family predicts: the deviation from the matched GOE
reference stays O(small) as eta -> mean-spacing scale, with the m-scaling
of the systematic part readable from the design ladder.  Any arithmetic
spike/repulsion would show as an excess rigidity or a Stieltjes bias.

Designs: (199, K=11, m=18), (3001, K=25, m=120), (3571, K=17, m=210),
(9349, K=?, m~450-700) — the m-ladder of the pilot.

Output: artifacts/r81/local_law_pilot.json
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

A = [[2, 1], [1, 1]]


def goe_samples(m, nrep, rng):
    """nrep samples of GOE(m) with unit second moment, eigenvalues."""
    out = np.empty((nrep, m))
    for i in range(nrep):
        X = rng.standard_normal((m, m))
        H = (X + X.T) / 2
        ev = np.linalg.eigvalsh(H)
        ev = ev - ev.mean()
        s2 = (ev ** 2).mean()
        out[i] = ev / np.sqrt(s2)
    return out


def stieltjes(ev, eta):
    m = len(ev)
    return complex(np.mean(1.0 / (ev - 1j * eta)))


def count_var(ev_s, quantiles):
    """level counts in the quantile windows; returns the per-window counts."""
    counts = []
    for a, b in zip(quantiles[:-1], quantiles[1:]):
        counts.append(int(((ev_s >= a) & (ev_s < b)).sum()))
    return np.array(counts)


def semicircle_quantiles(m, nwin):
    """quantiles of the semicircle on [-sqrt2, sqrt2] (unit 2nd moment)."""
    xs = np.linspace(-np.sqrt(2), np.sqrt(2), 4001)
    rho = np.sqrt(np.maximum(0.0, 2 - xs ** 2))
    cdf = np.cumsum(rho)
    cdf /= cdf[-1]
    lv = np.linspace(0, 1, nwin + 1)[1:-1]
    return np.interp(lv, cdf, xs)


def main():
    out = {"script": "src/r81_local_law_pilot.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "designs": []}
    rng = np.random.default_rng(810810)
    designs = [(199, 64), (8969, 512), (3571, 512), (9349, 1024)]
    nrep = 10
    nwin = 12

    for N, batch in designs:
        t0 = time.time()
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        assert ordA == K
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        RB = B.conj().T @ apply_parity(B)
        w, Vv = np.linalg.eigh(RB)
        mp, mm = int((w > 0).sum()), int((w <= 0).sum())
        Bp = B @ Vv[:, w > 0]
        Bm = B @ Vv[:, w <= 0]
        reps = orbit_reps(cm, K, nrep, rng)
        row = {"N": N, "K": int(K), "m": int(m), "m_plus": mp, "m_minus": mm,
               "eig_resid": res, "blocks": {}}
        print(f"=== N={N} K={K} m={m} (m+={mp}, m-={mm}) resid={res:.1e} "
              f"({time.time()-t0:.0f} s)", flush=True)
        if min(mp, mm) < 12:
            print("  blocks too small, skipped", flush=True)
            out["designs"].append(row)
            continue

        for name, Bb, mpm in (("plus", Bp, mp), ("minus", Bm, mm)):
            t1 = time.time()
            evs = []
            for u in reps:
                H = Bb.conj().T @ cm.apply_T(u, Bb)
                H = H + H.conj().T
                ev = np.linalg.eigvalsh(H)
                ev = ev - ev.mean()
                s2 = (ev ** 2).mean()
                evs.append(ev / np.sqrt(s2))
            evs = np.array(evs)

            # matched GOE reference
            gref = goe_samples(mpm, nrep, rng)

            # (a) rigidity: variance of window counts (center windows)
            quant = semicircle_quantiles(mpm, nwin)
            lo = nwin // 4
            hi = nwin - lo
            cnt_a = np.array([count_var(e, quant) for e in evs])
            cnt_g = np.array([count_var(e, quant) for e in gref])
            var_a = cnt_a[:, lo:hi].var(axis=0, ddof=1).mean()
            var_g = cnt_g[:, lo:hi].var(axis=0, ddof=1).mean()
            ratio_rig = var_a / var_g if var_g > 0 else np.inf

            # (b) Stieltjes deviation at eta = c/m in the scaled units
            st = {}
            for c in (3.0, 10.0, 30.0):
                eta = c / mpm
                da = np.array([stieltjes(e, eta) for e in evs])
                dg = np.array([stieltjes(e, eta) for e in gref])
                # systematic part: |mean(G_arith) - mean(G_GOE)|
                sysdev = abs(da.mean() - dg.mean())
                # noise floor: the sample spread of the GOE statistic
                noise = dg.std().real
                st[f"eta{int(c)}"] = {
                    "sys_dev": sysdev, "goe_spread": noise,
                    "ratio": sysdev / noise if noise > 0 else np.inf,
                    "mean_arith": da.mean().real,
                    "mean_goe": dg.mean().real}
            print(f"  {name}: rigidity var ratio = {ratio_rig:.3f} "
                  f"(1 = GOE); stieltjes sys/noise: "
                  + " ".join(f"eta{int(c)}={st[f'eta{int(c)}']['ratio']:.2f}"
                             for c in (3.0, 10.0, 30.0))
                  + f"  ({time.time()-t1:.0f} s)", flush=True)
            row["blocks"][name] = {
                "rigidity_var_ratio": ratio_rig,
                "rigidity_var_arith": var_a, "rigidity_var_goe": var_g,
                "stieltjes": st}
        out["designs"].append(row)

    dest = os.path.join("artifacts", "r81", "local_law_pilot.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", os.path.normpath(dest), flush=True)


if __name__ == "__main__":
    main()
