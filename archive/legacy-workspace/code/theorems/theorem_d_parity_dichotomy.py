"""
THEOREM D (exact parity dichotomy) and the DESYMMETRISED experiment.  Run 72.
============================================================================

Let R be the parity operator (R f)(x) = f(-x) on C^{Z/N}, and let k be the
projective order of A mod N, so that A^k = eps I with eps in {+1,-1} and the
torsion exponent is K = k if eps = +1, K = 2k if eps = -1.

THEOREM D.
 (D1)  R U_A = U_A R exactly: the kernel
       U_A(x,y) = N^{-1/2} w^{(2c)^{-1}(d x^2 - 2xy + a y^2)} is even in (x,y).
       Hence R preserves every eigenspace H_lam, and R^2 = 1.
 (D2)  R T(u) R^{-1} = T(-u).  A Weyl observable V = sum_u g_u T(u) is
       Hermitian iff g_{-u} = conj(g_u) and parity invariant iff g_{-u} = g_u;
       both together say exactly that all g_u are REAL, i.e. that the Weyl
       symbol of V is an EVEN function on the torus.  For such V,
       [R, P_lam V P_lam] = 0.
 (D3)  DICHOTOMY.  R = U_{-I} and -I is a power of A mod N precisely when
       eps = -1, in which case U_A^{k} = (phase) R and therefore R acts on each
       eigenspace H_lam as a SCALAR: parity carries no information.  When
       eps = +1 (K = k odd or even but A^k = +I), R is an independent
       involution, H_lam = H_lam^+ + H_lam^- with both blocks nonempty, and
       every real-symbol compression is BLOCK DIAGONAL.
 (D4)  A block-diagonal matrix has the spacing statistics of a SUPERPOSITION of
       two spectra: P(0) > 0, no level repulsion between levels of opposite
       parity.  So for eps = +1 a real-symbol compression - in particular the
       single-Weyl-orbit observable T(u) + T(u)^* used in T20 - can NEVER be
       Wigner-Dyson, whatever the arithmetic.
 (D5)  A generic Gaussian Weyl observable has complex g_u, is not parity
       invariant, and is exactly GUE by Theorem A.  Sharp dichotomy:
       REAL symbol  => parity superposition, never WD;
       COMPLEX symbol => exactly GUE.

This explains the whole run-71 measurement.  Design points with eps = +1
(K = 17, 19, 59) gave z = +2.8, +5.3, +2.4; design points with eps = -1
(K = 34, 46, 56) gave z = -0.1, +0.6, +0.1.  The correlation is with eps,
not with m or with the size of K.

DESYMMETRISED EXPERIMENT: restrict to one parity block and re-ask BGS there.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import (                      # noqa: E402
    CatMap, L1_to, reference_L1, unfolded_spacings,
)
from compression_spacings import EDGES, eigen_basis, orbit_reps   # noqa: E402


def apply_parity(F):
    """(R f)(x) = f(-x) on a batch of columns, indices mod N."""
    N = F.shape[0]
    idx = (-np.arange(N)) % N
    return F[idx, :]


def eps_of(A, N):
    """A^k = eps I mod N; return (k, eps)."""
    A = np.array(A, dtype=np.int64) % N
    I = np.eye(2, dtype=np.int64)
    M = A.copy()
    for j in range(1, 4 * N + 4):
        if np.array_equal(M % N, I):
            return j, +1
        if np.array_equal(M % N, (-I) % N):
            return j, -1
        M = M @ A % N
    raise RuntimeError


def superposition_L1(m, nrep, edges, rng, kind="GUE"):
    out = []
    for _ in range(nrep):
        parts = []
        for mm in (m - m // 2, m // 2):
            if mm < 3:
                continue
            if kind == "GUE":
                X = rng.standard_normal((mm, mm)) + 1j * rng.standard_normal((mm, mm))
                X = (X + X.conj().T) / 2
            else:
                X = rng.standard_normal((mm, mm))
                X = (X + X.T) / np.sqrt(2)
            parts.append(np.linalg.eigvalsh(X) / np.sqrt(mm))
        ev = np.sort(np.concatenate(parts))
        s = unfolded_spacings(ev)
        out.append((L1_to(s, 1, edges), L1_to(s, 2, edges), L1_to(s, 0, edges)))
    a = np.array(out)
    return a.mean(axis=0), a.std(axis=0)


def stats(ev, refs):
    s = unfolded_spacings(ev)
    l1 = (L1_to(s, 1, EDGES), L1_to(s, 2, EDGES), L1_to(s, 0, EDGES))
    d = {"L1_GOE": l1[0], "L1_GUE": l1[1], "L1_Poisson": l1[2],
         "n_spacings": int(len(s)), "frac_small": float(np.mean(s < 0.1))}
    for name, (mu, sd) in refs.items():
        d[f"z_{name}"] = [float((l1[i] - mu[i]) / sd[i]) if sd[i] > 0 else None
                          for i in range(3)]
    return d


def main():
    rng = np.random.default_rng(720720)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}

    designs = [([[2, 1], [1, 1]], 1597, 120),    # eps = -1 expected
               ([[2, 1], [1, 1]], 3571, 400),    # eps = +1 expected
               ([[2, 1], [1, 1]], 8969, 300),    # eps = +1 expected
               ([[2, 1], [1, 1]], 9349, 800),    # eps = +1 expected
               ([[2, 1], [1, 1]], 14503, 500)]   # eps = -1 expected

    for A, N, batch in designs:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        k, eps = eps_of(A, N)

        E = np.zeros((N, min(N, 48)), dtype=complex)
        E[:min(N, 48), :min(N, 48)] = np.eye(min(N, 48))
        d1 = float(np.abs(apply_parity(cm.apply_U(E))
                          - cm.apply_U(apply_parity(E))).max())

        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        RB = B.conj().T @ apply_parity(B)
        herm = float(np.abs(RB - RB.conj().T).max())
        invol = float(np.abs(RB @ RB - np.eye(m)).max())
        w, Vv = np.linalg.eigh(RB)
        mp, mm_ = int((w > 0).sum()), int((w <= 0).sum())
        scalar = float(np.abs(RB - np.trace(RB) / m * np.eye(m)).max())

        print("=" * 78)
        print(f"A={A} N={N}: k={k} eps={eps:+d} K={K} m={m}   "
              f"|[R,U_A]|={d1:.1e}  |R_B^2-1|={invol:.1e}")
        print(f"   R on H_lam: m+={mp} m-={mm_}   "
              f"|R_B - scalar|={scalar:.1e}   "
              f"-> {'SCALAR (no parity info)' if scalar < 1e-9 else 'NONTRIVIAL SPLIT'}")
        row = {"A": A, "N": N, "k": k, "eps": eps, "K": K, "m": m,
               "m_plus": mp, "m_minus": mm_,
               "D1_commutator_R_UA": d1, "RB_involution_dev": invol,
               "RB_distance_to_scalar": scalar,
               "parity_is_scalar": bool(scalar < 1e-9),
               "predicted_scalar_from_eps": bool(eps == -1),
               "D3_dichotomy_holds": bool((scalar < 1e-9) == (eps == -1)),
               "arms": {}}

        refs_full = {kk: reference_L1(kk, m, 12, EDGES, rng)
                     for kk in ("GOE", "GUE", "Poisson")}
        refs_full["SUPGUE"] = superposition_L1(m, 12, EDGES, rng, "GUE")
        reps = orbit_reps(cm, K, 8, rng)

        arms = {"full": []}
        for u in reps:
            H = B.conj().T @ cm.apply_T(u, B)
            H = H + H.conj().T
            st = stats(np.linalg.eigvalsh(H), refs_full)
            st["commutator_with_parity"] = float(np.abs(RB @ H - H @ RB).max())
            arms["full"].append(st)

        if not row["parity_is_scalar"] and min(mp, mm_) >= 12:
            Bp, Bm = B @ Vv[:, w > 0], B @ Vv[:, w <= 0]
            refs_p = {kk: reference_L1(kk, mp, 12, EDGES, rng)
                      for kk in ("GOE", "GUE", "Poisson")}
            refs_m = {kk: reference_L1(kk, mm_, 12, EDGES, rng)
                      for kk in ("GOE", "GUE", "Poisson")}
            arms["plus"], arms["minus"], arms["haar_plus"] = [], [], []
            for u in reps:
                Hp = Bp.conj().T @ cm.apply_T(u, Bp)
                Hp = Hp + Hp.conj().T
                arms["plus"].append(stats(np.linalg.eigvalsh(Hp), refs_p))
                Hm = Bm.conj().T @ cm.apply_T(u, Bm)
                Hm = Hm + Hm.conj().T
                arms["minus"].append(stats(np.linalg.eigvalsh(Hm), refs_m))
                Z = (rng.standard_normal((N, mp))
                     + 1j * rng.standard_normal((N, mp)))
                Q, _ = np.linalg.qr(Z)
                Y = Q.conj().T @ cm.apply_T(u, Q)
                Y = Y + Y.conj().T
                arms["haar_plus"].append(stats(np.linalg.eigvalsh(Y), refs_p))

        for kk, v in arms.items():
            if not v:
                continue
            g = lambda key: float(np.mean([d[key] for d in v]))          # noqa: E731
            zg = np.array([d["z_GOE"][0] for d in v])
            zu = np.array([d["z_GUE"][1] for d in v])
            e = {"n": len(v), "L1_GOE": g("L1_GOE"), "L1_GUE": g("L1_GUE"),
                 "L1_Poisson": g("L1_Poisson"),
                 "frac_spacings_below_0.1": g("frac_small"),
                 "z_GOE_mean": float(zg.mean()),
                 "z_GOE_sem": float(zg.std(ddof=1) / math.sqrt(len(zg))),
                 "z_GUE_mean": float(zu.mean()),
                 "z_GUE_sem": float(zu.std(ddof=1) / math.sqrt(len(zu)))}
            if kk == "full":
                e["z_vs_superposition_GUE"] = float(
                    np.mean([d["z_SUPGUE"][1] for d in v]))
                e["max_commutator_with_parity"] = max(
                    d["commutator_with_parity"] for d in v)
            row["arms"][kk] = e
            msg = (f"    {kk:<10} L1: GOE={e['L1_GOE']:.4f} GUE={e['L1_GUE']:.4f} "
                   f"Poi={e['L1_Poisson']:.4f}  P(s<.1)="
                   f"{e['frac_spacings_below_0.1']:.3f}  "
                   f"z_GUE={e['z_GUE_mean']:+.2f}+-{e['z_GUE_sem']:.2f}  "
                   f"z_GOE={e['z_GOE_mean']:+.2f}+-{e['z_GOE_sem']:.2f}")
            if kk == "full":
                msg += (f"  | z vs 2-fold superposition ="
                        f" {e['z_vs_superposition_GUE']:+.2f}"
                        f"  |[R,H]|<={e['max_commutator_with_parity']:.1e}")
            print(msg)
        out["rows"].append(row)
        sys.stdout.flush()

    print()
    print("VERDICT: dichotomy eps = -1  <=>  parity acts as a scalar")
    ok = True
    for r in out["rows"]:
        ok &= r["D3_dichotomy_holds"]
        print(f"  N={r['N']:>6} eps={r['eps']:+d} K={r['K']:>3} m={r['m']:>4}: "
              f"parity scalar={r['parity_is_scalar']!s:>5} "
              f"(predicted {r['predicted_scalar_from_eps']!s:>5})  "
              f"m+={r['m_plus']:>4} m-={r['m_minus']:>4}  "
              f"full z_GUE={r['arms']['full']['z_GUE_mean']:+6.2f}"
              + (f"   plus z_GUE={r['arms']['plus']['z_GUE_mean']:+6.2f}"
                 f"   haar z_GUE={r['arms']['haar_plus']['z_GUE_mean']:+6.2f}"
                 if "plus" in r["arms"] else ""))
    out["verdict"] = {"D3_dichotomy_holds_everywhere": bool(ok)}
    print(f"  D3 dichotomy holds at every design point: {ok}")
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r72", "parity_desymmetrised.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
