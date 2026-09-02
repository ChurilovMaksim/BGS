"""
Run 81d: THE TWO DISCRIMINATORS for the coherent-mode mechanism.
================================================================
R81.4 established: the arithmetic ensemble {V_n} has semicircle density
but 2-4x excess, growing-with-m variance of the bulk level counts across
n, carried by one coherent mode.  Two hypotheses:

  (H-breath) each sample is internally GOE-rigid; the FAMILY fluctuates
             through a low-dimensional arithmetic modulation;
  (H-broken) each sample is itself non-GOE at the local scale.

Discriminator 1: per-sample <r~> (the unfolding-free ratio statistic on
consecutive gaps) for every n-sample, against the matched GOE per-sample
distribution.  H-breath predicts: the arithmetic <r~> values lie INSIDE
the GOE sample spread.

Discriminator 2: the coherent mode scores regressed on the per-n
arithmetic phase scalar
    theta(n) = sum over rank-0 word classes mult_c * w^{sigma(n, C_c n)/2}
(the R76 phase family — computable per n from the few distinct C
matrices).  H-breath-with-arithmetics predicts a high R^2 of the top-mode
scores on {Re theta, Im theta}.

Designs: (3571, K=17) plus block m+=105; (9349, K=19) plus block m+=246.

Output: artifacts/r81/coherent_mode.json
"""

import json
import os
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from r76_phi_ensemble import powers_At  # noqa: E402
from compression_spacings import eigen_basis, orbit_reps  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402
from r81_local_law_pilot import (goe_samples, semicircle_quantiles,  # noqa: E402
                                 count_var)

A = [[2, 1], [1, 1]]


def rtilde(ev):
    """unfolding-free consecutive-gap ratio statistic."""
    s = np.diff(np.sort(ev))
    s = s[s > 0]
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(r.mean())


def theta_of(n, rank0_C, N, two_inv, P):
    """per-n rank-0 phase scalar theta(n) = sum_c mult_c w^{sigma(n, C n)/2}."""
    n1, n2 = int(n[0]) % N, int(n[1]) % N
    tot = 0.0 + 0.0j
    for ct, mult in rank0_C.items():
        C = np.array(ct, dtype=np.int64).reshape(2, 2)
        Cn1 = (C[0, 0] * n1 + C[0, 1] * n2) % N
        Cn2 = (C[1, 0] * n1 + C[1, 1] * n2) % N
        sig = (n1 * Cn2 - n2 * Cn1) % N
        tot += mult * np.exp(2j * np.pi * (two_inv * sig % N) / N)
    return tot


def rank0_classes(K, r, N, P, chunk=500_000):
    """distinct C matrices and multiplicities among words with L = 0."""
    lo = K - 1
    Psh = np.stack([P[d] for d in range(-(K - 1), K)])
    total = (2 * K) ** r
    pw = np.array([(2 * K) ** (r - 1 - t) for t in range(r)], dtype=np.int64)
    cls = defaultdict(int)
    for start in range(0, total, chunk):
        cnt = min(chunk, total - start)
        idx = np.arange(start, start + cnt, dtype=np.int64)
        g = np.stack([(idx // pw[t]) % (2 * K) for t in range(r)])
        eg = np.where(g < K, -1, 1)
        jg = g % K
        L = np.zeros((cnt, 2, 2), dtype=np.int64)
        Cacc = np.zeros((cnt, 2, 2), dtype=np.int64)
        for i in range(r):
            L += eg[i, :, None, None] * Psh[jg[i] + lo]
        L %= N
        for i in range(r):
            for k2 in range(i + 1, r):
                d = jg[k2] - jg[i] + lo
                Cacc += (eg[i] * eg[k2])[:, None, None] * Psh[d]
        Cacc %= N
        iszero = ~L.reshape(cnt, 4).any(axis=1)
        for w in np.nonzero(iszero)[0]:
            cls[tuple(Cacc[w].ravel())] += 1
    return dict(cls)


def main():
    out = {"script": "src/r81d_coherent_mode.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    rng = np.random.default_rng(810813)
    nrep = 24
    nwin = 12

    for N, batch in ((3571, 512), (9349, 1024)):
        t0 = time.time()
        cm = CatMap(A, N)
        _, K = cm.orders()
        two_inv = (N + 1) // 2
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        RB = B.conj().T @ apply_parity(B)
        w, Vv = np.linalg.eigh(RB)
        mp = int((w > 0).sum())
        Bp = B @ Vv[:, w > 0]
        reps = orbit_reps(cm, K, nrep, rng)

        # rank-0 phase classes (r = 5)
        P5 = powers_At(A, N, -(K - 1), K - 1)
        r0 = rank0_classes(K, 5, N, P5)
        ncls = len(r0)

        evs = []
        thetas = []
        for u in reps:
            H = Bp.conj().T @ cm.apply_T(u, Bp)
            H = H + H.conj().T
            ev = np.linalg.eigvalsh(H)
            ev = ev - ev.mean()
            ev = ev / np.sqrt((ev ** 2).mean())
            evs.append(ev)
            thetas.append(theta_of(u, r0, N, two_inv, P5))
        evs = np.array(evs)
        gref = goe_samples(mp, nrep, rng)

        # ---- discriminator 1: per-sample <r~> ----
        rt_a = [rtilde(e) for e in evs]
        rt_g = [rtilde(e) for e in gref]
        rt_a = np.array(rt_a)
        rt_g = np.array(rt_g)
        inside = float(np.mean(np.abs(rt_a - rt_g.mean()) <=
                               2 * rt_g.std(ddof=1)))
        z_mean = (rt_a.mean() - rt_g.mean()) / (rt_g.std(ddof=1) /
                                                np.sqrt(len(rt_g)))

        # ---- discriminator 2: top-mode scores vs theta(n) ----
        quant = semicircle_quantiles(mp, nwin)
        cnt = np.array([count_var(e, quant) for e in evs])
        X = cnt - cnt.mean(axis=0)
        U, s, Vt = np.linalg.svd(X, full_matrices=False)
        mode = Vt[0]                      # top coherent direction
        scores = X @ mode                 # per-sample scores
        frac = float(s[0] ** 2 / (s ** 2).sum())
        th = np.array([theta.real for theta in thetas])
        ti = np.array([theta.imag for theta in thetas])
        tmod = np.abs(np.array(thetas))
        M = np.stack([np.ones(nrep), th, ti, tmod], axis=1)
        # least squares fit of scores on the theta basis
        coef, res_, rank_, sv_ = np.linalg.lstsq(M, scores, rcond=None)
        pred = M @ coef
        ss_res = float(((scores - pred) ** 2).sum())
        ss_tot = float(((scores - scores.mean()) ** 2).sum())
        r2score = 1 - ss_res / ss_tot if ss_tot > 0 else np.nan

        row = {"N": N, "K": int(K), "m_plus": mp, "nrep": nrep,
               "rank0_classes": ncls,
               "rtilde_arith_mean": float(rt_a.mean()),
               "rtilde_arith_all": [float(x) for x in rt_a],
               "rtilde_goe_mean": float(rt_g.mean()),
               "rtilde_goe_std": float(rt_g.std(ddof=1)),
               "frac_inside_2sigma_goe": inside,
               "z_of_mean_vs_goe": float(z_mean),
               "top_mode_fraction": frac,
               "theta_regression_R2": r2score,
               "theta_coef": [float(c) for c in coef]}
        out["designs"].append(row)
        print(f"=== N={N} m+={mp} ({time.time()-t0:.0f} s)", flush=True)
        print(f"  D1 per-sample <r~>: arith mean {rt_a.mean():.4f} "
              f"(per-sample spread {rt_a.min():.4f}..{rt_a.max():.4f}); "
              f"GOE {rt_g.mean():.4f} +- {rt_g.std(ddof=1):.4f}", flush=True)
        print(f"     fraction of arithmetic samples inside GOE 2-sigma: "
              f"{inside:.2f};  z(mean vs GOE) = {z_mean:+.2f}", flush=True)
        print(f"  D2 top mode carries {frac:.2f} of count variance; "
              f"regression on theta(n) (const, Re, Im, |theta|): "
              f"R^2 = {r2score:.2f}", flush=True)
        print(f"     (rank-0 phase classes: {ncls})", flush=True)

    dest = os.path.join("artifacts", "r81", "coherent_mode.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", os.path.normpath(dest), flush=True)


if __name__ == "__main__":
    main()
