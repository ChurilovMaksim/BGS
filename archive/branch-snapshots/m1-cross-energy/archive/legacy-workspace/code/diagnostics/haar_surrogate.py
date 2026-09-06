"""
THE DISCRIMINATING EXPERIMENT for op:local_deterministic (run 72).
=================================================================

Question.  A single Weyl-orbit compression  M_O = P_lam (T(u)+T(u)^*) P_lam  was
claimed (T20) to be GOE; run 71 measured a systematic +0.05..+5.3 sigma
deviation.  Is ANY of that behaviour arithmetic?

Matched surrogate.  Replace the cat-map eigenprojector by a Haar-random
m-dimensional frame Q and compress the SAME Weyl operator:
        M_R = Q^* (T(u)+T(u)^*) Q .
Both are single m x m compressions of the same fixed operator, with the same
Hilbert-Schmidt scale (m^2/N versus m/K, equal because N = mK + O(K)), and the
surrogate has no arithmetic content whatsoever.  Q^* X Q with Haar Q is a
unitarily invariant ensemble (a free/MANOVA-type compression), so its local
statistics are expected to be GUE (resp. GOE for a real Haar frame).

Arms measured, per (A, p) and per random frequency u:
  arm1  eigenspace,          raw            T(u)+T(u)^*
  arm2  eigenspace,          Theta-symmetrised
  arm3  complex Haar frame,  raw            (surrogate for arm1)
  arm4  real    Haar frame,  raw            (surrogate for arm2)

Read-out: L1 distance of the unfolded nearest-neighbour spacings to the beta=1
and beta=2 curves, and z against size-matched true GOE/GUE controls run through
the identical pipeline.

Interpretation key.
  * If arm1 ~ arm3 and arm2 ~ arm4 then the single-orbit statistics carry NO
    arithmetic information beyond the dimension m: the cat-map eigenspace acts
    exactly like a pseudorandom subspace and BGS-in-this-family is a statement
    about subspace equidistribution, not about the arithmetic of the orbit.
  * If arm1 deviates MORE than arm3, the orbit structure genuinely correlates
    the entries and the deviation is arithmetic - a real obstruction to BGS.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import (                     # noqa: E402
    CatMap, L1_to, reference_L1, unfolded_spacings,
)
from compression_spacings import EDGES, eigen_basis, orbit_reps   # noqa: E402
from theoremB_covariance import sqrt_sym_unitary     # noqa: E402


def haar_frame(N, m, rng, real=False):
    if real:
        Z = rng.standard_normal((N, m))
    else:
        Z = rng.standard_normal((N, m)) + 1j * rng.standard_normal((N, m))
    Q, _ = np.linalg.qr(Z)
    return Q.astype(complex)


def theta_block(cm, B, N, A, rng):
    """W = B^* U_M conj(B) and Q with Q Q^T = W, so that in the basis B Q the
    antiunitary Theta acts as complex conjugation."""
    (a, b), (c, d) = A
    for p_ in range(-8, 9):
        for q_ in range(-8, 9):
            for r_ in range(-8, 9):
                if p_ * (a - d) + q_ * c + b * r_ != 0 or p_ ** 2 + q_ * r_ != 1:
                    continue
                M = np.array([[p_, q_], [-r_, p_]], dtype=np.int64)
                if math.gcd(abs(int(M[1, 0])) % N, N) != 1:
                    continue
                cmM = CatMap([[int(M[0, 0]), int(M[0, 1])],
                              [int(M[1, 0]), int(M[1, 1])]], N)
                W = B.conj().T @ cmM.apply_U(np.conj(B))
                Qs, off = sqrt_sym_unitary(W)
                if Qs is None:
                    continue
                return Qs, float(np.abs(Qs @ Qs.T - W).max())
    return None, None


def measure(H, refs):
    ev = np.linalg.eigvalsh(H)
    s = unfolded_spacings(ev)
    l1g, l1u = L1_to(s, 1, EDGES), L1_to(s, 2, EDGES)
    mg, sg = refs["GOE"]
    mu, su = refs["GUE"]
    return {"L1_GOE": l1g, "L1_GUE": l1u,
            "z_GOE": float((l1g - mg[0]) / sg[0]),
            "z_GUE": float((l1u - mu[1]) / su[1]),
            "n_spacings": int(len(s))}


def main():
    rng = np.random.default_rng(20260828)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}
    designs = [([[2, 1], [1, 1]], 1597, 120), ([[2, 1], [1, 1]], 3571, 400),
               ([[2, 1], [1, 1]], 9349, 800)]
    NU = 8

    for A, N, batch in designs:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        nrep = 24 if m <= 260 else 12
        refs = {k: reference_L1(k, m, nrep, EDGES, rng)
                for k in ("GOE", "GUE", "Poisson")}
        Qth, qerr = theta_block(cm, B, N, A, rng)
        Bq = B @ Qth if Qth is not None else None
        print("=" * 78)
        print(f"A={A} N={N} K={K} m={m}  proj-res {res:.1e}  "
              f"|QQ^T-W| {qerr if qerr is None else format(qerr, '.1e')}")
        print(f"  controls: GOE {refs['GOE'][0][0]:.4f}+-{refs['GOE'][1][0]:.4f}"
              f"   GUE {refs['GUE'][0][1]:.4f}+-{refs['GUE'][1][1]:.4f}"
              f"   (nrep={nrep})")
        reps = orbit_reps(cm, K, NU, rng)
        arms = {k: [] for k in ("eig_raw", "eig_theta", "haar_C", "haar_R")}
        hs = {k: [] for k in arms}
        for t, u in enumerate(reps):
            Tu = cm.apply_T(u, B)
            H1 = B.conj().T @ Tu
            H1 = H1 + H1.conj().T
            arms["eig_raw"].append(measure(H1, refs))
            hs["eig_raw"].append(float(np.linalg.norm(H1)))

            if Bq is not None:
                Tq = cm.apply_T(u, Bq)
                X = Bq.conj().T @ Tq
                X = X + X.conj().T
                X = (X + np.conj(X)) / 2          # Theta-symmetrisation
                arms["eig_theta"].append(measure(X, refs))
                hs["eig_theta"].append(float(np.linalg.norm(X)))

            for key, real in (("haar_C", False), ("haar_R", True)):
                Qf = haar_frame(N, m, rng, real=real)
                Tq = cm.apply_T(u, Qf)
                Y = Qf.conj().T @ Tq
                Y = Y + Y.conj().T
                arms[key].append(measure(Y, refs))
                hs[key].append(float(np.linalg.norm(Y)))

        row = {"A": A, "N": N, "K": K, "m": m, "proj_res": res,
               "controls": {k: {"mean": list(map(float, v[0])),
                                "std": list(map(float, v[1]))}
                            for k, v in refs.items()},
               "arms": {}}
        for k, v in arms.items():
            if not v:
                continue
            zg = np.array([d["z_GOE"] for d in v])
            zu = np.array([d["z_GUE"] for d in v])
            row["arms"][k] = {
                "n": len(v),
                "L1_GOE_mean": float(np.mean([d["L1_GOE"] for d in v])),
                "L1_GUE_mean": float(np.mean([d["L1_GUE"] for d in v])),
                "z_GOE_mean": float(zg.mean()),
                "z_GOE_sem": float(zg.std(ddof=1) / math.sqrt(len(zg))),
                "z_GUE_mean": float(zu.mean()),
                "z_GUE_sem": float(zu.std(ddof=1) / math.sqrt(len(zu))),
                "HS_norm_mean": float(np.mean(hs[k])),
                "per_u": v}
            r = row["arms"][k]
            print(f"    {k:<10} L1(GOE)={r['L1_GOE_mean']:.4f} "
                  f"L1(GUE)={r['L1_GUE_mean']:.4f}  "
                  f"z_GOE={r['z_GOE_mean']:+.2f}+-{r['z_GOE_sem']:.2f}  "
                  f"z_GUE={r['z_GUE_mean']:+.2f}+-{r['z_GUE_sem']:.2f}  "
                  f"||.||_F={r['HS_norm_mean']:.3f}")
        out["rows"].append(row)
        sys.stdout.flush()

    print()
    print("SUMMARY  (arithmetic content = eigenspace arm minus Haar arm)")
    for r in out["rows"]:
        a = r["arms"]
        if "haar_C" in a and "eig_raw" in a:
            d = a["eig_raw"]["z_GUE_mean"] - a["haar_C"]["z_GUE_mean"]
            e = math.hypot(a["eig_raw"]["z_GUE_sem"], a["haar_C"]["z_GUE_sem"])
            print(f"  N={r['N']:>5} m={r['m']:>4}: complex arm  "
                  f"z_GUE(eig) - z_GUE(haar) = {d:+.2f} +- {e:.2f}")
        if "haar_R" in a and "eig_theta" in a:
            d = a["eig_theta"]["z_GOE_mean"] - a["haar_R"]["z_GOE_mean"]
            e = math.hypot(a["eig_theta"]["z_GOE_sem"], a["haar_R"]["z_GOE_sem"])
            print(f"  N={r['N']:>5} m={r['m']:>4}: real arm     "
                  f"z_GOE(eig) - z_GOE(haar) = {d:+.2f} +- {e:.2f}")

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r72", "haar_surrogate.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
