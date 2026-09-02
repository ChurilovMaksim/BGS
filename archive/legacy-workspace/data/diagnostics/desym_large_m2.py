"""
Run 73, Priority 1 (memory-lean rewrite): the parity-desymmetrised ratio
statistic at large m.
=======================================================================

The first attempt died at 1280/1674 columns from memory pressure.  Two changes:

 * the parity blocks are never materialised in the big space.  We compute the
   m x m matrices  H = B^* (T(u)+T(u)^*) B  and  R_B = B^* R_par B  once, and
   then rotate inside the small space: with R_B = V diag(+-1) V^*, the blocks of
   H are the corresponding sub-blocks of V^* H V.  This removes two N x (m/2)
   arrays (about 1.5 GB at m = 1280).
 * no Haar arm at this size; the matched Haar comparison is already recorded at
   m = 673 in artifacts/r72/desym_ratio_statistic.json.

Peak memory is then basis (N x m) plus one temporary of the same shape.
"""

from __future__ import annotations

import gc
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                     # noqa: E402
from desym_ratio_statistic import RTILDE, r_tilde, ref_rtilde   # noqa: E402
from desym_large_m import projector_basis_chunked         # noqa: E402
from parity_desymmetrised import apply_parity             # noqa: E402

P = 95419
A = [[2, 1], [1, 1]]
M_TARGET = 1674  # = p//K: the FULL eigenspace (run 75; RAM re-probed at 16 GB)
NU = 6


def main():
    rng = np.random.default_rng(7391)
    t0 = time.time()
    cm = CatMap(A, P)
    ordA, K = cm.orders()
    e0 = np.zeros((P, 1), dtype=complex)
    e0[0, 0] = 1.0
    v = e0
    for _ in range(K):
        v = cm.apply_U(v)
    chi = v[0, 0]
    lam = np.exp(np.log(chi + 0j) / K)
    del e0, v
    print(f"p={P} K={K}  target m={M_TARGET}  "
          f"basis {P * M_TARGET * 16 / 2**30:.2f} GB", flush=True)
    B = projector_basis_chunked(cm, K, lam, M_TARGET, blk=64, rng=rng)
    m = B.shape[1]
    res = float(np.abs(cm.apply_U(B[:, :48]) - lam * B[:, :48]).max())
    m_true = P // K
    is_full = abs(m - m_true) <= 1
    print(f"   TARGET CHECK: m={m}, dim H_lam = p//K = {m_true} -> "
          f"{'FULL eigenspace' if is_full else 'PROPER SUBSPACE of the eigenspace'}",
          flush=True)
    if not is_full:
        print("   WARNING: a proper subspace of H_lam is NOT parity invariant, so "
              "the parity split below is NOT the desymmetrisation of Theorem D; "
              "this run is the 'random subspace inside the eigenspace' CONTROL.",
              flush=True)
    RB = B.conj().T @ apply_parity(B)
    w, V = np.linalg.eigh(RB)
    par_dev = float(np.abs(np.abs(w) - 1).max())
    print(f"   parity eigenvalues within {par_dev:.2e} of +-1 "
          f"({'involution, subspace is parity invariant' if par_dev < 1e-8 else 'NOT an involution on this subspace'})",
          flush=True)
    plus = w > 0
    mp, mm_ = int(plus.sum()), int((~plus).sum())
    print(f"   m={m}  |U B - lam B|={res:.2e}   parity split m+={mp} m-={mm_}",
          flush=True)
    del RB
    gc.collect()

    nrep = 6
    refs_full = {kk: ref_rtilde(kk, m, nrep, rng)
                 for kk in ("GOE", "GUE", "Poisson", "SUP_GUE")}
    refs_blk = {kk: ref_rtilde(kk, mp, nrep, rng)
                for kk in ("GOE", "GUE", "Poisson")}
    print("   refs full :", "  ".join(f"{a}={b[0]:.4f}+-{b[1]:.4f}"
                                      for a, b in refs_full.items()), flush=True)
    print("   refs block:", "  ".join(f"{a}={b[0]:.4f}+-{b[1]:.4f}"
                                      for a, b in refs_blk.items()), flush=True)

    vals = {kk: [] for kk in ("full", "plus", "minus")}
    for t in range(NU):
        u = (int(rng.integers(1, P)), int(rng.integers(1, P)))
        Tb = cm.apply_T(u, B)
        H = B.conj().T @ Tb
        del Tb
        gc.collect()
        H = H + H.conj().T
        vals["full"].append(r_tilde(np.linalg.eigvalsh(H))[0])
        Hr = V.conj().T @ H @ V                 # rotate into the parity basis
        del H
        Hp = Hr[np.ix_(plus, plus)]
        Hm = Hr[np.ix_(~plus, ~plus)]
        offblock = float(np.abs(Hr[np.ix_(plus, ~plus)]).max())
        del Hr
        vals["plus"].append(r_tilde(np.linalg.eigvalsh(Hp))[0])
        vals["minus"].append(r_tilde(np.linalg.eigvalsh(Hm))[0])
        del Hp, Hm
        gc.collect()
        print(f"      u#{t+1}: full={vals['full'][-1]:.4f} "
              f"plus={vals['plus'][-1]:.4f} minus={vals['minus'][-1]:.4f}   "
              f"max |off-parity block| = {offblock:.2e}", flush=True)

    row = {"p": P, "A": A, "K": K, "m": m, "dim_H_lam": m_true,
           "is_full_eigenspace": bool(is_full),
           "parity_eigenvalue_deviation_from_pm1": par_dev,
           "interpretation": ("desymmetrised measurement" if is_full else
                              "CONTROL: random subspace inside the eigenspace, "
                              "not parity invariant"),
           "m_plus": mp, "m_minus": mm_,
           "proj_res": res, "n_orbits": NU,
           "refs_full": {a: list(b) for a, b in refs_full.items()},
           "refs_block": {a: list(b) for a, b in refs_blk.items()},
           "measured": {}, "secs": round(time.time() - t0, 1)}
    for kk, vv in vals.items():
        a = np.array([x for x in vv if np.isfinite(x)])
        Rf = refs_full if kk == "full" else refs_blk
        row["measured"][kk] = {
            "rtilde_mean": float(a.mean()),
            "rtilde_sem": float(a.std(ddof=1) / math.sqrt(len(a))),
            "z": {nm: float((a.mean() - mu) / sd) for nm, (mu, sd) in Rf.items()}}
        z = row["measured"][kk]["z"]
        print(f"   {kk:<6} <r~>={a.mean():.4f}+-"
              f"{a.std(ddof=1)/math.sqrt(len(a)):.4f}   z: "
              + "  ".join(f"{nm}={zz:+.2f}" for nm, zz in z.items()), flush=True)

    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "rtilde_reference_values": RTILDE, "rows": [row],
           "note": "no Haar arm at this size; the matched Haar comparison is in "
                   "artifacts/r72/desym_ratio_statistic.json at m = 673"}
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r73", "desym_large_m.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
