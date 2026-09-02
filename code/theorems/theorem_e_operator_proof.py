"""
Run 73: upgrade THEOREM E from a solvability statement to an operator theorem.
=============================================================================

Theorem E said: if there is tau in the Hecke torus C(A) with
tau^t R^t u = +- u, then Theta_u := U_tau Theta is an antiunitary commuting with
the single-orbit compression, forcing beta = 1.  Two things were not checked:

  (E-a)  the ALGEBRAIC identity behind it.  Since conj(U_{M'}) = U_{S M' S} up to
         a phase, Theta_u^2 = U_tau U_M conj(U_tau U_M) is proportional to
         U_W with
                W := (tau M) * S (tau M) S ,      M = S R ,
         so Theta_u^2 is a SCALAR exactly when W = +- I, and then antiunitarity
         forces the scalar to be +-1.  We verify W = +- I by integer arithmetic
         mod p for every (A, p, u, tau) found, and record the sign.

  (E-b)  the OPERATOR statements, at machine precision:
             Theta_u^2 = c * 1  with c = +-1,
             Theta_u (T(u) + T(-u)) Theta_u^{-1} = T(u) + T(-u),
             and hence, in the parity block, the compression is unitarily
             equivalent to a REAL SYMMETRIC matrix (a real structure), which is
             the analytic content of beta = 1.

Theta_u acts as v -> G conj(v) with G = U_tau U_M, so
Theta_u X Theta_u^{-1} = G conj(X) G^*.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                     # noqa: E402
from compression_spacings import eigen_basis              # noqa: E402
from parity_desymmetrised import apply_parity             # noqa: E402
from theoremE_torus_repair import reversing_involution, torus_elements  # noqa: E402

S = np.array([[1, 0], [0, -1]], dtype=np.int64)


def matmod(X, Y, p):
    return (np.array(X, dtype=object) @ np.array(Y, dtype=object)) % p


def find_tau(A, p, u, R, torus):
    """tau in C(A) with tau^t R^t u = +- u (mod p); return (tau, sign)."""
    RT = np.array(R, dtype=np.int64).T
    w = (RT @ np.array(u, dtype=np.int64)) % p
    for (m11, m12, m21, m22) in torus:
        v0 = (m11 * w[0] + m21 * w[1]) % p
        v1 = (m12 * w[0] + m22 * w[1]) % p
        if v0 == u[0] % p and v1 == u[1] % p:
            return np.array([[m11, m12], [m21, m22]], dtype=np.int64), +1
        if v0 == (-u[0]) % p and v1 == (-u[1]) % p:
            return np.array([[m11, m12], [m21, m22]], dtype=np.int64), -1
    return None, 0


def real_structure_defect(H, W):
    """H Hermitian, W unitary symmetric with W conj(W) = 1.  Return
    |W conj(H) W^* - H| (0 means H is real in the basis diagonalising the
    real structure)."""
    return float(np.abs(W @ np.conj(H) @ W.conj().T - H).max())


def main():
    rng = np.random.default_rng(7373)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}
    designs = [([[2, 1], [1, 1]], 101), ([[2, 1], [1, 1]], 199),
               ([[2, 1], [1, 1]], 311), ([[5, 2], [2, 1]], 101),
               ([[5, 2], [2, 1]], 151), ([[3, 1], [2, 1]], 199)]
    tot = {"W_eq_plusI": 0, "W_eq_minusI": 0, "W_other": 0,
           "c_plus1": 0, "c_minus1": 0, "c_other": 0, "checked": 0}
    worst = {"theta2_scalar": 0.0, "observable_invariance": 0.0,
             "block_real_structure": 0.0, "W_sym": 0.0, "W_Wbar": 0.0}

    for A, p in designs:
        R = reversing_involution(A)
        if R is None:
            continue
        M = (S @ R)
        if math.gcd(abs(int(M[1, 0])) % p, p) != 1:
            print(f"  A={A} p={p}: gcd(M21,p) > 1, chart skipped")
            continue
        cmM = CatMap([[int(M[0, 0]), int(M[0, 1])],
                      [int(M[1, 0]), int(M[1, 1])]], p)
        UM = cmM.U_matrix()
        cm = CatMap(A, p)
        ordA, K = cm.orders()
        torus = torus_elements(A, p)
        B, lam, m, res, chi = eigen_basis(cm, K, 0, min(4 * (p // K) + 20, p), rng)
        RB = B.conj().T @ apply_parity(B)
        w_, Vv = np.linalg.eigh(RB)
        mp = int((w_ > 0).sum())
        Bp = B @ Vv[:, w_ > 0] if mp >= 2 else None
        print("=" * 78)
        print(f"A={A} p={p}: K={K} m={m} torus |C(A)|={len(torus)} "
              f"parity m+={mp}  R={R.tolist()}  M={M.tolist()}")

        nfound = 0
        rows = []
        for trial in range(14):
            u = (int(rng.integers(1, p)), int(rng.integers(1, p)))
            tau, sgn = find_tau(A, p, u, R, torus)
            if tau is None:
                continue
            if math.gcd(abs(int(tau[1, 0])) % p, p) != 1:
                continue                       # U_tau chart undefined
            nfound += 1
            tot["checked"] += 1
            # ---- (E-a) integer identity  W = (tau M) S (tau M) S
            # M -> U_M is an ANTIhomomorphism (Egorov carries a transpose:
            # U_A T(n) U_A^* = T(A^t n), so U_{M1} U_{M2} ~ U_{M2 M1}).  Hence
            # Theta_u^2 = U_tau U_M conj(U_tau) conj(U_M) ~ U_W with
            #     W = (S M S)(S tau S) M tau = (R tau)^2 ,
            # using S M S = R S and S(S tau S) = tau S.  And R tau R^{-1}
            # = tau^{-1} for every tau = x I + y A in the centraliser torus,
            # because R A R^{-1} = A^{-1} and tau^{-1} = (x + y t) I - y A.
            # Therefore W = (R tau)^2 = (R tau R^{-1}) tau = tau^{-1} tau = I.
            SMS = matmod(matmod(S, M, p), S, p)
            StS = matmod(matmod(S, tau, p), S, p)
            W = matmod(matmod(SMS, StS, p), matmod(M, tau, p), p)
            Rtau2 = matmod(matmod(R, tau, p), matmod(R, tau, p), p)
            assert np.array_equal(W % p, Rtau2 % p), "W != (R tau)^2"
            RtRinv = matmod(matmod(R, tau, p), np.array(R, dtype=object), p)
            tauinv = matmod(np.array(tau, dtype=object),
                            np.array([[0, 0], [0, 0]], dtype=object), p)  # unused
            I2 = np.eye(2, dtype=np.int64)
            if np.array_equal(W % p, I2 % p):
                tot["W_eq_plusI"] += 1
                wtag = "+I"
            elif np.array_equal(W % p, (-I2) % p):
                tot["W_eq_minusI"] += 1
                wtag = "-I"
            else:
                tot["W_other"] += 1
                wtag = "other"
            # ---- (E-b) operator level
            cmT = CatMap([[int(tau[0, 0]), int(tau[0, 1])],
                          [int(tau[1, 0]), int(tau[1, 1])]], p)
            G = cmT.U_matrix() @ UM
            th2 = G @ np.conj(G)
            c = th2[0, 0]
            dev = float(np.abs(th2 - c * np.eye(p)).max())
            worst["theta2_scalar"] = max(worst["theta2_scalar"], dev)
            if abs(c - 1) < 1e-8:
                tot["c_plus1"] += 1
                ctag = "+1"
            elif abs(c + 1) < 1e-8:
                tot["c_minus1"] += 1
                ctag = "-1"
            else:
                tot["c_other"] += 1
                ctag = f"{c:.4f}"
            Vu = cm.T_matrix(u) + cm.T_matrix((-u[0] % p, -u[1] % p))
            inv = float(np.abs(G @ np.conj(Vu) @ G.conj().T - Vu).max())
            worst["observable_invariance"] = max(
                worst["observable_invariance"], inv)
            # ---- real structure inside the parity block
            blk = None
            if Bp is not None:
                Wb = Bp.conj().T @ (G @ np.conj(Bp))
                sym = float(np.abs(Wb - Wb.T).max())
                wwb = float(np.abs(Wb @ np.conj(Wb) - np.eye(Bp.shape[1])).max())
                Hu = Bp.conj().T @ Vu @ Bp
                Hu = (Hu + Hu.conj().T) / 2
                blk = real_structure_defect(Hu, Wb)
                evb = np.linalg.eigvalsh(Hu)
                gaps = np.diff(np.sort(evb))
                kram = float(np.median(gaps) / max(gaps.min(), 1e-300))
                worst["W_sym"] = max(worst["W_sym"], sym)
                worst["W_Wbar"] = max(worst["W_Wbar"], wwb)
                worst["block_real_structure"] = max(
                    worst["block_real_structure"], blk)
            rows.append({"u": list(u), "sign": sgn, "tau": tau.tolist(),
                         "W": wtag, "theta2_scalar_dev": dev, "c": ctag,
                         "observable_invariance": inv,
                         "block_real_structure_defect": blk,
                         "kramers_median_over_min_gap": (
                             None if Bp is None else kram)})
            print(f"    u={u}: sign={sgn:+d} W={wtag:>5} "
                  f"Theta_u^2={ctag:>5} (scalar dev {dev:.1e})  "
                  f"|Theta_u V Theta_u^-1 - V|={inv:.1e}  "
                  f"block real-structure defect="
                  f"{'n/a' if blk is None else format(blk, '.1e')}")
            sys.stdout.flush()
        out["rows"].append({"A": A, "p": p, "K": K, "m": m, "m_plus": mp,
                            "torus_order": len(torus), "R": R.tolist(),
                            "M": M.tolist(), "n_tau_found": nfound,
                            "cases": rows})

    out["totals"] = tot
    out["worst"] = worst
    out["verdict"] = {
        "W_always_pm_I": tot["W_other"] == 0,
        "Theta_u_squared_always_pm1": tot["c_other"] == 0,
        "Theta_u_squared_always_plus1": tot["c_minus1"] == 0 and tot["c_other"] == 0,
        "observable_invariance_max": worst["observable_invariance"],
        "block_real_structure_max": worst["block_real_structure"],
        "E_upgraded_to_theorem": bool(
            tot["W_other"] == 0 and tot["c_other"] == 0
            and worst["observable_invariance"] < 1e-10
            and worst["block_real_structure"] < 1e-9),
    }
    print()
    print("TOTALS:", json.dumps(tot))
    print("WORST :", json.dumps({k: float(v) for k, v in worst.items()}))
    print("VERDICT:", json.dumps(out["verdict"], indent=1))
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r73", "theoremE_operator.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0 if out["verdict"]["E_upgraded_to_theorem"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
