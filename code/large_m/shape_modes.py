"""
Run 82: WHAT CARRIES THE COHERENT MODE?  Chebyshev-mode decomposition of the
arithmetic fluctuation excess (op:local, the R81.4 phenomenon).
============================================================================
R81.4/R81.5 established, for the family {V_n = P_+(T(n)+T(-n))P_+} over
A^T-orbit representatives n:
  * per-sample spectra are GOE-rigid (D1: every per-sample <r~> inside the
    matched GOE band);
  * the ENSEMBLE across n fluctuates 1.8-4.2x more than GOE in bulk level
    counts, through ONE coherent mode with positively correlated neighbour
    windows;
  * the rank-0 quadratic-phase scalar theta(n) does NOT drive it (D2, R^2
    <= 0.11).
The driver was left open.  Note that each sample is already normalised to
zero mean and unit second moment in that pipeline, so a global width
("breathing") fluctuation is ALREADY divided out -- the surviving modulation
must live in the SHAPE of the density.

THIS RUN tests the shape-modulation hypothesis in the basis that diagonalises
linear eigenvalue statistics of a beta-ensemble: the Chebyshev modes

    L_k(n) = sum_i T_k(lambda_i(n)/sqrt 2),    k = 1, 2, 3, ...

(for the unit-second-moment semicircle supported on [-sqrt2, sqrt2]).  For a
beta-ensemble Var(L_k) = O(1) uniformly in m -- no growth with m -- and the
modes are asymptotically independent.  Hence:

PRE-REGISTERED PREDICTIONS (written before the run; see LEDGER RUN 82)
  P1  the arithmetic/GOE variance ratio is >= 2 for the LOW modes
      (k = 2, 3, 4) and decays towards 1 for large k.               [~70%]
  P2  after projecting the window-count vectors on the low modes
      (k <= 4) and removing that component, the arithmetic/GOE
      count-variance ratio drops to <= 1.3.                          [~60%]
  P3  the Haar control shows ratios 0.6-0.8 at every k (no excess).  [~85%]
  P4  the A-invariant quadratic form Q(n) = n1^2 - n1 n2 - n2^2 (mod N),
      an exact orbit invariant, explains a nontrivial part of the
      leading arithmetic mode (R^2 >= 0.2).                          [~35%]
A result that surprises is treated first as a bug signal (numeric evidence
standard): every ratio is reported with its Monte-Carlo error bar, and the
GOE reference uses 4x the sample count of the arithmetic family.

Output: artifacts/r82/shape_modes.json
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
from r81_local_law_pilot import (count_var, goe_samples,  # noqa: E402
                                 semicircle_quantiles)

A = [[2, 1], [1, 1]]
KMAX = 12          # Chebyshev modes tracked
NWIN = 12          # bulk windows (as in R81)


def cheb_stats(ev_s, kmax=KMAX):
    """L_k = sum_i T_k(lambda_i / sqrt 2) via the stable recurrence."""
    x = ev_s / np.sqrt(2.0)
    t_prev = np.ones_like(x)
    t_cur = x.copy()
    out = np.empty(kmax)
    out[0] = t_cur.sum()
    for k in range(2, kmax + 1):
        t_next = 2.0 * x * t_cur - t_prev
        t_prev, t_cur = t_cur, t_next
        out[k - 1] = t_cur.sum()
    return out


def moments(ev_s, rmax=8):
    """normalised spectral moments mu_r = (1/m) sum lambda^r, r = 3..rmax."""
    m = len(ev_s)
    return np.array([(ev_s ** r).sum() / m for r in range(3, rmax + 1)])


def var_with_err(x):
    """sample variance and its own relative MC error (~sqrt(2/(n-1)))."""
    n = len(x)
    v = float(np.var(x, ddof=1))
    return v, v * np.sqrt(2.0 / (n - 1))


def ratio_err(v1, e1, v2, e2):
    r = v1 / v2
    return r, r * np.hypot(e1 / v1, e2 / v2)


def residual_after_projection(counts, feats):
    """Variance of the count vectors after removing the component explained
    linearly by `feats` (per-window OLS across samples).  Returns the mean
    per-window residual variance."""
    c = counts - counts.mean(axis=0, keepdims=True)
    X = np.column_stack([np.ones(len(feats)), feats - feats.mean(axis=0)])
    coef, *_ = np.linalg.lstsq(X, c, rcond=None)
    resid = c - X @ coef
    dof = max(1, len(c) - X.shape[1])
    return float((resid ** 2).sum(axis=0).mean() / dof)


def design_run(N, batch, nrep, rng, nrep_goe_mult=4):
    t0 = time.time()
    cm = CatMap(A, N)
    ordA, K = cm.orders()
    assert ordA == K, (ordA, K)
    B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
    assert m == (N - 1) // K or m == (N + 1) // K, (m, N, K)
    assert res < 1e-9, res
    RB = B.conj().T @ apply_parity(B)
    w, Vv = np.linalg.eigh(RB)
    mp = int((w > 0).sum())
    Bp = B @ Vv[:, w > 0]
    reps = orbit_reps(cm, K, nrep, rng)
    print(f"=== N={N} K={K} m={m} m+={mp} resid={res:.1e} nrep={nrep} "
          f"({time.time()-t0:.0f} s)", flush=True)

    quant = semicircle_quantiles(mp, NWIN)

    def harvest(ev_list):
        evs = np.array(ev_list)
        L = np.array([cheb_stats(e) for e in evs])
        M = np.array([moments(e) for e in evs])
        C = np.array([count_var(e, quant) for e in evs])
        return L, M, C

    # ---- (a) the arithmetic family -------------------------------------
    ev_a, s2raw, Qs = [], [], []
    for u in reps:
        H = Bp.conj().T @ cm.apply_T(u, Bp)
        H = H + H.conj().T
        ev = np.linalg.eigvalsh(H)
        ev = ev - ev.mean()
        s2 = (ev ** 2).mean()
        s2raw.append(float(s2))
        ev_a.append(ev / np.sqrt(s2))
        n1, n2 = int(u[0]), int(u[1])
        Qs.append((n1 * n1 - n1 * n2 - n2 * n2) % N)
    La, Ma, Ca = harvest(ev_a)

    # ---- (b) matched GOE reference (4x samples) ------------------------
    gref = goe_samples(mp, nrep * nrep_goe_mult, rng)
    Lg, Mg, Cg = harvest(list(gref))

    # ---- (c) Haar control: same operators, random subspaces -----------
    ev_h = []
    for u in reps:
        Z = rng.standard_normal((N, mp)) + 1j * rng.standard_normal((N, mp))
        Q, _ = np.linalg.qr(Z)
        Y = Q.conj().T @ (cm.apply_T(u, Q) +
                          cm.apply_T((-u[0], -u[1]), Q))
        Y = (Y + Y.conj().T) / 2
        ev = np.linalg.eigvalsh(Y)
        ev = ev - ev.mean()
        ev_h.append(ev / np.sqrt((ev ** 2).mean()))
    Lh, Mh, Ch = harvest(ev_h)

    row = {"N": N, "K": int(K), "m": int(m), "m_plus": mp, "nrep": nrep,
           "nrep_goe": nrep * nrep_goe_mult, "eig_resid": res,
           "width_rel_spread": float(np.std(s2raw) / np.mean(s2raw))}

    # ---- P1: per-mode variance ratios ---------------------------------
    modes = []
    for k in range(1, KMAX + 1):
        va, ea = var_with_err(La[:, k - 1])
        vg, eg = var_with_err(Lg[:, k - 1])
        vh, eh = var_with_err(Lh[:, k - 1])
        ra, era = ratio_err(va, ea, vg, eg)
        rh, erh = ratio_err(vh, eh, vg, eg)
        modes.append({"k": k, "var_arith": va, "var_goe": vg, "var_haar": vh,
                      "ratio_arith": ra, "ratio_arith_err": era,
                      "ratio_haar": rh, "ratio_haar_err": erh})
        print(f"  k={k:2d}  Var_arith={va:9.3f}  Var_GOE={vg:7.3f}  "
              f"ratio={ra:8.2f} +- {era:5.2f}   haar={rh:5.2f}", flush=True)
    row["cheb_modes"] = modes

    # ---- reproduce the R81.4 window-count ratio ------------------------
    lo, hi = NWIN // 4, NWIN - NWIN // 4
    va_c = float(Ca[:, lo:hi].var(axis=0, ddof=1).mean())
    vg_c = float(Cg[:, lo:hi].var(axis=0, ddof=1).mean())
    vh_c = float(Ch[:, lo:hi].var(axis=0, ddof=1).mean())
    row["count_var_ratio_arith"] = va_c / vg_c
    row["count_var_ratio_haar"] = vh_c / vg_c
    print(f"  bulk count-variance ratio: arith/GOE = {va_c/vg_c:.2f}, "
          f"haar/GOE = {vh_c/vg_c:.2f}   [R81.4 reproduction]", flush=True)

    # ---- P2: residual count variance after removing low modes ---------
    proj = []
    for k0 in (2, 3, 4, 6, 8):
        ra_res = residual_after_projection(Ca[:, lo:hi], La[:, :k0])
        rg_res = residual_after_projection(Cg[:, lo:hi], Lg[:, :k0])
        proj.append({"k0": k0, "resid_arith": ra_res, "resid_goe": rg_res,
                     "resid_ratio": ra_res / rg_res})
        print(f"  project out k<={k0}: residual ratio arith/GOE = "
              f"{ra_res/rg_res:.3f}", flush=True)
    row["projection"] = proj

    # ---- P4: does the orbit invariant Q(n) drive the leading mode? ----
    Qs = np.array(Qs, dtype=float)
    qr = Qs / N
    leg = np.array([pow(int(q), (N - 1) // 2, N) if q % N else 0
                    for q in Qs], dtype=float)
    leg = np.where(leg > 1, -1.0, leg)          # Legendre symbol in {-1,0,1}
    feats = np.column_stack([qr, np.cos(2 * np.pi * qr), np.sin(2 * np.pi * qr),
                             leg])
    qtests = {}
    for k in (1, 2, 3, 4):
        y = La[:, k - 1]
        X = np.column_stack([np.ones(len(y)), feats - feats.mean(axis=0)])
        coef, *_ = np.linalg.lstsq(X, y, rcond=None)
        r2 = 1.0 - float(((y - X @ coef) ** 2).sum() /
                         ((y - y.mean()) ** 2).sum())
        qtests[f"L{k}"] = r2
        print(f"  Q(n)-regression on L_{k}: R^2 = {r2:.3f}", flush=True)
    row["Q_regression_R2"] = qtests

    # moment variance ratios (interpretable form of P1)
    mom = []
    for i, r in enumerate(range(3, 9)):
        va, ea = var_with_err(Ma[:, i])
        vg, eg = var_with_err(Mg[:, i])
        rr, er = ratio_err(va, ea, vg, eg)
        mom.append({"r": r, "ratio": rr, "err": er})
    row["moment_ratios"] = mom
    print("  moment-variance ratios (r=3..8): "
          + " ".join(f"{d['r']}:{d['ratio']:.1f}" for d in mom), flush=True)
    return row


def main():
    rng = np.random.default_rng(820001)
    out = {"script": "src/r82_shape_modes.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "kmax": KMAX, "nwin": NWIN, "designs": []}
    for N, batch, nrep in ((199, 64, 96), (3571, 512, 96), (9349, 1024, 64)):
        try:
            out["designs"].append(design_run(N, batch, nrep, rng))
        except Exception as exc:                      # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "shape_modes.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
