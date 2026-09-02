"""
run46_symmetry.py -- WHY does the Dyson class of the compression depend on the
observable when A^k = -I mod p (K = 2k even)?

SETUP.  Theta_R = U_M o conj is an anti-unitary symmetry of U_A for every
reversing involution R (T3).  For sign = -1 we have U_A^k = -1, so the
half-period unitary J := U_A^{k/2} satisfies

    Theta_J := J o Theta :  X -> J Theta(X) J^{-1}

and a direct computation gives

    Theta_J U_A Theta_J^{-1} = J U_A^{-1} J^{-1} = U_A^{-1},
    Theta_J^2 = J Theta(J) = J U_A^{-k/2} ... = (+1),        (*)

so Theta_J is ANOTHER time-reversal symmetry, distinct from Theta whenever J
is not scalar on the multiplet.  An observable V has [Theta_J, V] = 0 iff

    V = J (Theta V Theta^{-1}) J^{-1},                      (**)

a linear condition on the coefficients of V that a generic V does NOT satisfy.
If it does, the compression V_lam is real symmetric in the Theta_J-real
structure => GOE; otherwise no anti-unitary symmetry survives and the class
is GUE.  For sign = +1 (K odd) U_A^k = +1 and J = U_A^{-k/2} does not exist
as an element of <U_A>; there is only one reversing anti-unitary per R, and
the classical dichotomy holds.

This script:
  W1  verifies (*) at small N;
  W2  computes the coefficient-level action n -> M^T E^{-?}... explicitly:
      Theta V Theta^{-1} has coefficients c'_n = conj(c_{E_M^T n}) with
      E_M the Egorov matrix of M (= M^T); conjugation by J shifts by E^{k/2}.
      So (**) reads:  c_n = conj( c_{ E_M^T E^{-k/2}... } ) -- implement as
      orbit condition and test which seeds satisfy it;
  W3  measures <r> separately over seeds satisfying/not satisfying (**);
  W4  checks the run-45 flip (small freq set -> GOE, big -> GUE at t3/p=2207)
      against this criterion.
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bgs_core as bc                                            # noqa: E402
from run43_parity import build_coeffs, close_labels              # noqa: E402
from run44_class import bulk_rtilde, control                     # noqa: E402

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
SMALL = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 0), (0, 2)]
BIG = [(a, b) for a in range(-3, 4) for b in range(-3, 4) if (a, b) != (0, 0)]

CONFIGS = [
    ("t3", (2, 1, 1, 1), 2207),
    ("t4", (3, 1, 2, 1), 2131),
    ("t7", (3, 1, 5, 2), 2089),
    ("t3", (2, 1, 1, 1), 3571),
    ("t4", (3, 1, 2, 1), 2017),
]


def theta_j_violation(coeffs, E, MT, Ej, N):
    """max_n |c_n - conj(c_{MT^T applied after Ej ... })| -- implemented via
    the label map of the composed operator.  The composed anti-unitary acts on
    frequency labels by n -> Ej^T . (M^T n)  where M^T is the Egorov matrix of
    U_M and Ej = E^{k/2} (mod N).  Violation measured on shared labels."""
    G = (np.array(MT, dtype=np.int64) @ np.array(Ej, dtype=np.int64)) % N
    worst = 0.0
    for n, c in coeffs.items():
        v = np.array(n, dtype=np.int64)
        w = tuple(int(t) % N for t in (G @ v) % N)
        if w in coeffs:
            worst = max(worst, abs(c - np.conj(coeffs[w])))
        else:
            worst = math.inf
            break
    return worst


def main():
    rows = []
    for (name, A, N) in CONFIGS:
        k, sign, K = bc.mat_order(A, N)
        chi, tres = bc.torsion_certificate_fft(A, N, K)
        E = np.array([[A[0], A[2]], [A[1], A[3]]], dtype=np.int64)
        Rs = [Rx for Rx in bc.reversing_involution(A) if (-int(Rx[2])) % N != 0]
        R = Rs[0]
        RT = np.array([[R[0], R[2]], [R[1], R[3]]], dtype=np.int64)
        negI = -np.eye(2, dtype=np.int64)
        M = (R[0], R[1], -R[2], -R[3])
        MT = np.array([[M[0], M[2]], [M[1], M[3]]], dtype=np.int64)
        out = dict(name=name, A=list(A), N=N, k=k, sign=int(sign), K=K,
                   chi=[chi.real, chi.imag], torsion_res=tres,
                   R=list(R), M=list(M))
        print(f"\n=== {name} p={N} k={k} sign={sign} K={K} chi={chi:.6f}")

        # W1: matrix-level verification of the Theta_J reversal at small N
        if N <= 700 and k % 2 == 0:
            U = bc.U_cat(A, N)
            UM = bc.U_cat(M, N)
            Uh = np.linalg.matrix_power(U, k // 2)

            def apply_anti(L, X):          # L o conj as operator conjugation
                return L @ np.conj(X) @ np.conj(np.linalg.inv(L))
            lhs = apply_anti(Uh @ UM, U)
            num = np.vdot(U.conj().T.ravel(), lhs.ravel()) / N
            z = num / abs(num)
            out["thJ_reversal_res"] = float(np.max(np.abs(lhs - z * U.conj().T)))
            sq = Uh @ UM @ np.conj(Uh @ UM)
            c2 = sq[0, 0]
            out["thJ_theta2"] = [float(c2.real), float(c2.imag)]
            out["thJ_theta2_res"] = float(np.max(
                np.abs(sq - c2 * np.eye(N))))
            print(f"  Theta_J reversal res {out['thJ_reversal_res']:.2e} "
                  f"Theta_J^2 = {c2:.6f} (res {out['thJ_theta2_res']:.1e})")

        bases = [bc.multiplet_basis_fft(A, N, K, chi, s) for s in range(K)]
        m = bases[0][2]
        out["m"] = int(m)
        Ej = (np.linalg.matrix_power(E.astype(object), k // 2)
              if k % 2 == 0 else None)
        Ej = np.array(Ej, dtype=np.int64) % N if Ej is not None else None

        for tag, freqs in (("small", SMALL), ("big", BIG)):
            labels = close_labels(freqs, [RT, negI], N)
            acc_sym, acc_gen = [], []
            viol_sym, viol_gen = [], []
            for sd in range(8):
                rng = np.random.default_rng(2000 + sd)
                gens = [(negI, True)]
                mode_seed = {}
                for mode in ("sym", "gen"):
                    rng_m = np.random.default_rng(3000 * sd + hash(tag) % 97 +
                                                  {"sym": 0, "gen": 1}[mode])
                    g = [(negI, True)]
                    if mode == "sym":
                        g.append((RT, True))
                    co = build_coeffs(labels, N, rng_m, g)
                    v = theta_j_violation(co, E, MT.tolist(), Ej.tolist(), N) \
                        if Ej is not None else float("inf")
                    acc = []
                    for (lam, B, mm, cert) in bases:
                        VL = B.conj().T @ bc.weyl_sum_operator(co, N, B)
                        VL = 0.5 * (VL + VL.conj().T)
                        acc.append(bulk_rtilde(np.linalg.eigvalsh(VL)))
                    rr = np.concatenate([a for a in acc if len(a)])
                    rec = dict(seed=sd, mean=float(rr.mean()), n=int(len(rr)),
                               violation=v)
                    (acc_sym if mode == "sym" else acc_gen).append(rec)
                    (viol_sym if mode == "sym" else viol_gen).append(v)
            def pool(recs):
                if not recs:
                    return None
                num = sum(r["mean"] * r["n"] for r in recs)
                den = sum(r["n"] for r in recs)
                sem = recs[0]["sem"] / math.sqrt(len(recs))
                return round(num / den, 4), den, round(sem, 4)
            out[f"{tag}_sym"] = pool(acc_sym)
            out[f"{tag}_gen"] = pool(acc_gen)
            out[f"{tag}_viol_sym"] = ([round(v, 3) if v != math.inf else None
                                       for v in viol_sym])
            out[f"{tag}_viol_gen"] = ([round(v, 3) if v != math.inf else None
                                       for v in viol_gen])
            g_c = control(m, K, "goe")["mean"]
            u_c = control(m, K, "gue")["mean"]
            out[f"{tag}_ctrl"] = [round(g_c, 4), round(u_c, 4)]
            print(f"  {tag:>5}: sym {out[f'{tag}_sym']} gen {out[f'{tag}_gen']}"
                  f"  ctrl {g_c:.4f}/{u_c:.4f}")
            print(f"         violations sym {out[f'{tag}_viol_sym']} "
                  f"gen {out[f'{tag}_viol_gen']}")
        rows.append(out)
        with open(os.path.join(ART, "run46_wip.json"), "w") as f:
            json.dump(rows, f, indent=1, default=float)
    os.replace(os.path.join(ART, "run46_wip.json"),
               os.path.join(ART, "run46_symmetry.json"))
    print("\nwrote artifacts/run46_symmetry.json")


if __name__ == "__main__":
    main()
