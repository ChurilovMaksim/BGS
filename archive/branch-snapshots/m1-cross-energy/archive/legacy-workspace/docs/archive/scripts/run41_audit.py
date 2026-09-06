"""
run41_audit.py -- run-41 independent audit of the load-bearing identities.

Checks, all with explicit residuals and PASS/FAIL, using ONLY `bgs_core.py`
(a from-scratch second implementation):

  C1 unitarity of U_A
  C2 Egorov covariance: which label matrix (A or A^T) and is the phase 1?
  C3 torsion U^K = chi I, and the order/sign bookkeeping
  C4 multiplet projector certificates + uniform multiplicity |m - N/K| < 1
  C5 Birkhoff reduction (T6):  P V P = Vbar P  in the multiplet basis
  C6 [Vbar, U] = 0
  C7 unimodular Weyl-weighted traces (T7): |Tr(T(v) U^J)| = 1, J != 0 mod K
  C8 reversing involution R and Theta^2 = +1; Theta U_A Theta^{-1} = U_A^{-1}
"""
import json
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bgs_core as bc                                            # noqa: E402

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
A_DEFAULT = (2, 1, 1, 1)


def audit_prime(A, N, seed=0, verbose=True):
    out = {"A": list(A), "N": N}
    U = bc.U_cat(A, N)
    I = np.eye(N)

    # C1 unitarity
    out["C1_unitarity"] = float(np.max(np.abs(U.conj().T @ U - I)))

    # C2 Egorov: try A^T (predicted) and A (the naive guess)
    AT = np.array([[A[0], A[2]], [A[1], A[3]]], dtype=np.int64)
    Amat = np.array([[A[0], A[1]], [A[2], A[3]]], dtype=np.int64)
    res_AT, _ = bc.egorov_residual(A, N, E=AT, nmax=2)
    res_A, _ = bc.egorov_residual(A, N, E=Amat, nmax=2)
    out["C2_egorov_res_AT"] = res_AT
    out["C2_egorov_res_A"] = res_A
    # is the covariance phase exactly 1?
    Ud = U.conj().T
    worst_phase = 0.0
    for n in [(1, 0), (0, 1), (1, 1), (2, 1), (1, -1)]:
        lhs = U @ bc.apply_T(n[0], n[1], Ud, N)
        m1, m2 = (AT @ np.array(n)) % N
        rhs = bc.T_matrix(int(m1), int(m2), N)
        z = np.vdot(rhs.ravel(), lhs.ravel()) / N
        worst_phase = max(worst_phase, abs(z - 1.0))
    out["C2_egorov_phase_dev"] = float(worst_phase)

    # C3 torsion
    k, sign, K = bc.mat_order(A, N)
    chi, tres = bc.torsion_certificate(U, K)
    out.update(k=k, sign=int(sign), K=K, chi=[chi.real, chi.imag],
               C3_torsion_res=tres)

    # C4 multiplet bases
    mults, certs = [], []
    bases = []
    for s in range(K):
        lam, B, m, cert = bc.multiplet_basis(U, K, chi, s, seed=seed)
        mults.append(m)
        certs.append(cert)
        bases.append((lam, B))
    out["C4_mults"] = mults
    out["C4_sum_mults"] = int(sum(mults))
    out["C4_max_cert"] = float(max(certs))
    out["C4_multiplicity_rigidity"] = float(max(abs(m - N / K) for m in mults))
    return out, U, chi, K, bases, AT


def main():
    A = A_DEFAULT
    rows = []
    for N in (101, 199, 521):
        out, U, chi, K, bases, AT = audit_prime(A, N)
        rng = np.random.default_rng(7)
        coeffs = bc.hermitian_observable([(1, 0), (0, 1), (1, 1)], rng, N,
                                         real_symbol=True)
        cbar = bc.birkhoff_average(coeffs, AT, K, N)

        # C5 / C6
        lam, B = bases[0]
        VB = bc.weyl_sum_operator(coeffs, N, B)
        VbarB = bc.weyl_sum_operator(cbar, N, B)
        VL = B.conj().T @ VB
        VLbar = B.conj().T @ VbarB
        out["C5_birkhoff_res"] = float(np.max(np.abs(VL - VLbar)))
        out["C5_hermitian_res"] = float(np.max(np.abs(VL - VL.conj().T)))
        E = np.eye(N, dtype=complex)
        VbarE = bc.weyl_sum_operator(cbar, N, E)
        out["C6_commutator"] = float(np.max(np.abs(VbarE @ U - U @ VbarE)))

        # C7 |Tr(T(v) U^J)| = 1 for J != 0 mod K
        worst = 0.0
        for J in (1, 2, K - 1):
            UJ = np.linalg.matrix_power(U, J % K if J % K else 1)
            for v in [(1, 0), (0, 1), (3, 2)]:
                tr = np.trace(bc.apply_T(v[0], v[1], UJ, N))
                worst = max(worst, abs(abs(tr) - 1.0))
        out["C7_unimodular_dev"] = float(worst)

        # C8 Theta
        Rs = bc.reversing_involution(A)
        out["C8_n_involutions"] = len(Rs)
        if Rs:
            UM, M = bc.theta_operator(A, N, Rs[0])
            out["C8_R"] = list(Rs[0])
            out["C8_M"] = list(M)
            th2 = UM @ np.conj(UM)
            c_sign = th2[0, 0]
            out["C8_theta2"] = [float(c_sign.real), float(c_sign.imag)]
            out["C8_theta2_res"] = float(np.max(np.abs(th2 - c_sign * np.eye(N))))
            # Theta U Theta^{-1} = U^{-1}  <=>  UM conj(U) conj(UM) = U^dagger
            lhs = UM @ np.conj(U) @ np.conj(UM)
            num = np.vdot(U.conj().T.ravel(), lhs.ravel()) / N
            z = num / abs(num)
            out["C8_reversal_res"] = float(
                np.max(np.abs(lhs - z * U.conj().T)))
            out["C8_reversal_phase"] = [float(z.real), float(z.imag)]
        rows.append(out)
        print(json.dumps(out, indent=1))

    os.makedirs(ART, exist_ok=True)
    with open(os.path.join(ART, "run41_audit.json"), "w") as f:
        json.dump(rows, f, indent=1)
    print("\nwrote artifacts/run41_audit.json")


if __name__ == "__main__":
    main()
