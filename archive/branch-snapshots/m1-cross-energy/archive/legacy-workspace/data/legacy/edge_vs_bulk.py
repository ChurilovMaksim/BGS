"""
Run 82e: EDGE OUTLIERS OR BULK SHAPE?  The decisive dissection of the
arithmetic even-moment excess.
=====================================================================
R82c leaves two candidate mechanisms for std(mu_4) ~ 0.23 (vs GOE 0.027):

  (E) a few OUTLIER eigenvalues.  V_n = P_+(T(n)+T(-n))P_+ has ||V_n|| <= 2
      while Tr(V_n^2)/m+ = N/(K^2 m+) ~ 0.118, so the bulk edge sits at
      sqrt(2 . 0.118) = 0.485 in raw units and a single eigenvalue anywhere up
      to 2 appears at 4.1 sigma in normalised units, contributing
      4.1^4 / m+ = 2.7 to mu_4 all by itself.  Under this mechanism mu_4 is an
      extreme-value statistic, not a shape statistic.
  (B) a genuine n-dependent modulation of the bulk density shape.

Discriminator: recompute every statistic after deleting the k largest-|lambda|
eigenvalues from BOTH the arithmetic samples and the matched GOE samples
(identical treatment -- the GOE reference absorbs the bias of trimming).
  * mechanism (E) => the arithmetic/GOE variance ratio collapses towards 1
    for small k, and the deleted eigenvalues sit far outside the GOE support;
  * mechanism (B) => the ratio survives trimming.

Also reported: the raw (un-normalised) extreme eigenvalue lambda_max(V_n),
its distance to the bulk edge, and the number of eigenvalues beyond the
semicircle edge, all against the matched GOE reference.

Output: artifacts/r82/edge_vs_bulk.json
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
NWIN = 12


def trim_and_normalise(ev, k):
    """delete the k largest-|lambda| eigenvalues, then centre and scale."""
    if k > 0:
        idx = np.argsort(-np.abs(ev - ev.mean()))
        ev = np.delete(ev, idx[:k])
    e = ev - ev.mean()
    return e / np.sqrt((e ** 2).mean())


def mu4_of(e):
    return float((e ** 4).mean())


def design(N, batch, nrep, rng):
    t0 = time.time()
    cm = CatMap(A, N)
    ordA, K = cm.orders()
    assert ordA == K
    B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
    assert res < 1e-9 and m in ((N - 1) // K, (N + 1) // K), (res, m)
    RB = B.conj().T @ apply_parity(B)
    w, Vv = np.linalg.eigh(RB)
    mp = int((w > 0).sum())
    Bp = B @ Vv[:, w > 0]
    reps = orbit_reps(cm, K, nrep, rng)
    print(f"=== N={N} K={K} m={m} m+={mp} nrep={nrep} ({time.time()-t0:.0f} s)",
          flush=True)

    raw = []
    for u in reps:
        H = Bp.conj().T @ cm.apply_T(u, Bp)
        H = H + H.conj().T
        raw.append(np.linalg.eigvalsh(H))
    raw = np.array(raw)
    gref = goe_samples(mp, 4 * nrep, rng)          # already normalised

    row = {"N": N, "K": int(K), "m_plus": mp, "nrep": nrep}

    # ---- raw edge diagnostics -----------------------------------------
    s2 = (raw - raw.mean(axis=1, keepdims=True)) ** 2
    s2 = s2.mean(axis=1)
    bulk_edge = np.sqrt(2 * s2)                     # semicircle edge, raw units
    lmax = np.abs(raw - raw.mean(axis=1, keepdims=True)).max(axis=1)
    row["raw_bulk_edge_mean"] = float(bulk_edge.mean())
    row["raw_lambda_max_mean"] = float(lmax.mean())
    row["raw_lambda_max_max"] = float(lmax.max())
    row["operator_norm_bound"] = 2.0
    ratio_edge = lmax / bulk_edge
    row["lambda_max_over_bulk_edge"] = [float(ratio_edge.mean()),
                                        float(ratio_edge.max())]
    gmax = np.abs(gref).max(axis=1) / np.sqrt(2.0)
    row["goe_lambda_max_over_edge"] = [float(gmax.mean()), float(gmax.max())]
    print(f"  |lambda|_max / bulk edge: arithmetic mean {ratio_edge.mean():.3f}"
          f" max {ratio_edge.max():.3f}  |  GOE mean {gmax.mean():.3f} max "
          f"{gmax.max():.3f}   (operator norm bound 2 = "
          f"{2/bulk_edge.mean():.2f} edges)", flush=True)
    # how many eigenvalues beyond the semicircle edge
    nb_a = [(np.abs(r - r.mean()) > be).sum() for r, be in zip(raw, bulk_edge)]
    nb_g = [(np.abs(g) > np.sqrt(2)).sum() for g in gref]
    row["n_beyond_edge_arith"] = [float(np.mean(nb_a)), int(np.max(nb_a))]
    row["n_beyond_edge_goe"] = [float(np.mean(nb_g)), int(np.max(nb_g))]
    print(f"  # eigenvalues beyond the semicircle edge: arithmetic "
          f"{np.mean(nb_a):.2f} (max {np.max(nb_a)}) | GOE {np.mean(nb_g):.2f}"
          f" (max {np.max(nb_g)})", flush=True)

    # ---- trimming ladder ----------------------------------------------
    ladder = []
    for k in (0, 1, 2, 4, 8):
        ea = np.array([trim_and_normalise(r, k) for r in raw])
        eg = np.array([trim_and_normalise(g, k) for g in gref])
        va = float(np.var([mu4_of(e) for e in ea], ddof=1))
        vg = float(np.var([mu4_of(e) for e in eg], ddof=1))
        quant = semicircle_quantiles(ea.shape[1], NWIN)
        lo, hi = NWIN // 4, NWIN - NWIN // 4
        ca = np.array([count_var(e, quant) for e in ea])
        cg = np.array([count_var(e, quant) for e in eg])
        cva = float(ca[:, lo:hi].var(axis=0, ddof=1).mean())
        cvg = float(cg[:, lo:hi].var(axis=0, ddof=1).mean())
        ladder.append({"k_trimmed": k, "var_mu4_arith": va, "var_mu4_goe": vg,
                       "ratio_mu4": va / vg, "count_var_arith": cva,
                       "count_var_goe": cvg, "ratio_count": cva / cvg,
                       "mu4_mean_arith": float(np.mean([mu4_of(e) for e in ea])),
                       "mu4_mean_goe": float(np.mean([mu4_of(e) for e in eg]))})
        print(f"  trim k={k}: Var(mu_4) ratio = {va/vg:8.2f}   bulk-count "
              f"variance ratio = {cva/cvg:6.3f}   mu_4 mean "
              f"{np.mean([mu4_of(e) for e in ea]):.4f} (GOE "
              f"{np.mean([mu4_of(e) for e in eg]):.4f})", flush=True)
    row["trim_ladder"] = ladder
    return row


def main():
    rng = np.random.default_rng(820004)
    out = {"script": "src/r82e_edge_vs_bulk.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    for N, batch, nrep in ((3571, 512, 192), (9349, 1024, 128)):
        try:
            out["designs"].append(design(N, batch, nrep, rng))
        except Exception as exc:                       # noqa: BLE001
            print(f"design N={N} FAILED: {exc!r}", flush=True)
            out["designs"].append({"N": N, "error": repr(exc)})
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "edge_vs_bulk.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
