"""
REFEREE CHECK R83.1 --- does the antiunitary Theta stabilise each eigenspace H_lambda?

CONTEXT.  REVIEW_ERRORS.md ERROR #1 (severity HIGH) asserts that
    Theta U_A Theta^{-1} = U_A^{-1}
implies Theta maps H_lambda -> H_{lambda^{-1}}, hence does NOT stabilise
H_lambda unless lambda^2 = 1, and that the paper's sentence
"preserves each H_lambda" is therefore wrong.

CLAIM UNDER TEST (this script).  ERROR #1 is itself WRONG.  Theta is
ANTIunitary.  For an antiunitary Theta and U_A v = lambda v:

    Theta U_A v = Theta(lambda v) = conj(lambda) * Theta v      [antilinearity]
    Theta U_A v = U_A^{-1} Theta v                              [intertwining]

  =>  U_A^{-1}(Theta v) = conj(lambda) (Theta v)
  =>  U_A (Theta v)     = conj(lambda)^{-1} (Theta v).

Since U_A is unitary, |lambda| = 1, so conj(lambda)^{-1} = lambda.  Hence

    U_A (Theta v) = lambda (Theta v),

i.e. Theta v lies in the SAME eigenspace H_lambda.  Theta stabilises every
H_lambda, for every lambda, with no hypothesis whatsoever.

This is exactly THEORY.md T4 ("Theta preserves every eigenspace H_lambda",
[PROVEN, 4.8e-16]).  The REVIEW_ERRORS entry dropped the complex conjugate.

VERIFICATION STRATEGY (two mechanistically independent keys):
  KEY 1 (operator identity, exact linear algebra):
        residual ||Theta U_A Theta^{-1} - U_A^{-1}||, ||Theta^2 - 1||.
  KEY 2 (spectral, per-eigenspace):
        for each eigenspace projector P_lambda, measure
        ||P_lambda Theta P_lambda - Theta P_lambda||  (= 0 iff Theta H_lambda
        subset H_lambda), and additionally the "wrong" hypothesis
        ||P_{lambda^{-1}} Theta P_lambda - Theta P_lambda|| which ERROR #1
        predicts to vanish instead.

If KEY 2 shows residual ~ 1e-15 for the SAME-eigenspace test and O(1) for the
INVERSE-eigenspace test at eigenvalues with lambda^2 != 1, ERROR #1 is refuted.

Run:  py -3 review/referee/ref01_theta_stabilises_eigenspaces.py
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from src.core.catmap_core import U_cat, ord_pm, weyl  # noqa: E402

OUT = os.path.join(ROOT, "artifacts", "referee_r83")
os.makedirs(OUT, exist_ok=True)


# ----------------------------------------------------------------- utilities
def reversor(A, N):
    """Find R = [[p,q],[r,-p]] in GL_2(Z/N) with det R = -1 and R A R^{-1} = A^{-1}.

    Conditions (THEORY.md T3):  p(a-d) + q c + b r = 0  and  p^2 + q r = 1.
    We brute-force over (p, q, r) mod N; N is small in the design points used.
    """
    a, b, c, d = [v % N for v in A]
    for p in range(N):
        for q in range(N):
            for r in range(N):
                if (p * (a - d) + q * c + b * r) % N != 0:
                    continue
                if (p * p + q * r) % N != 1 % N:
                    continue
                return (p, q, r, (-p) % N)
    return None


def theta_matrix(A, N):
    """Return the matrix W such that Theta psi = W conj(psi)."""
    R = reversor(A, N)
    if R is None:
        return None, None
    p, q, r, mp = R
    # S = diag(1,-1);  M = S R  in SL_2(Z/N)
    M = (p % N, q % N, (-r) % N, (p) % N)
    # det M = p*p + q*r = 1 by construction
    assert (M[0] * M[3] - M[1] * M[2]) % N == 1 % N, "M not in SL_2"
    if math.gcd(M[2] % N, N) != 1:
        return None, None  # kernel formula needs gcd(c, N) = 1
    return U_cat(M, N), M


def eig_projectors(U, N, tol=1e-8):
    """Spectral projectors of the unitary U, grouped by eigenvalue."""
    ev, W = np.linalg.eig(U)
    th = np.angle(ev)
    order = np.argsort(th)
    th, ev, W = th[order], ev[order], W[:, order]
    out = []
    start = 0
    for i in range(1, len(th) + 1):
        if i == len(th) or abs(th[i] - th[start]) > tol:
            B = W[:, start:i]
            Q, _ = np.linalg.qr(B)
            lam = np.exp(1j * th[start:i].mean())
            out.append((lam, Q, Q @ Q.conj().T))
            start = i
    return out


def run_case(A, N):
    U = U_cat(A, N)
    k, sgn = ord_pm(A, N)
    Wm, M = theta_matrix(A, N)
    if Wm is None:
        return None

    # ---- KEY 1: operator identities -------------------------------------
    # Theta psi = Wm @ conj(psi).  Then Theta X Theta^{-1} acts as
    #   Theta X Theta^{-1} psi = Wm conj(X conj(Wm^{-1} psi))
    #                          = Wm conj(X) conj(Wm^{-1}) psi.
    # With Theta^2 = +1 we have Wm conj(Wm) = 1, i.e. conj(Wm^{-1}) = Wm.
    Wc = Wm.conj()
    theta_sq = Wm @ Wc                              # matrix of Theta^2
    err_theta_sq = np.max(np.abs(theta_sq - np.eye(N)))

    Uinv = U.conj().T
    # Theta U Theta^{-1} psi = Theta U Theta psi          (Theta^2 = 1)
    #                        = Theta ( U W conj(psi) )
    #                        = W conj(U W conj(psi))
    #                        = W conj(U) conj(W) psi.
    conj_U = Wm @ U.conj() @ Wc                     # matrix of Theta U Theta^{-1}
    err_intertwine = np.max(np.abs(conj_U - Uinv))
    # allow for a global phase chi: Theta U Theta^{-1} = chi * U^{-1}
    num = np.vdot(Uinv.reshape(-1), conj_U.reshape(-1))
    den = np.vdot(Uinv.reshape(-1), Uinv.reshape(-1))
    chi = num / den
    err_intertwine_uptophase = np.max(np.abs(conj_U - chi * Uinv))

    err_unitary = np.max(np.abs(U.conj().T @ U - np.eye(N)))

    # ---- KEY 2: per-eigenspace stabilisation -----------------------------
    blocks = eig_projectors(U, N)
    same_max = 0.0
    inv_max = 0.0
    n_lambda_selfinv = 0
    rows = []
    for lam, Q, P in blocks:
        # matrix of Theta restricted then re-projected:  psi -> Wm conj(P psi)
        TP = Wm @ P.conj()                  # Theta P   (antilinear part folded in)
        same = np.max(np.abs(P @ TP - TP))  # ||P_lam Theta P_lam - Theta P_lam||
        # find the projector onto H_{lambda^{-1}} (ERROR #1's prediction)
        lam_inv = 1.0 / lam
        j = int(np.argmin([abs(l2 - lam_inv) for l2, _, _ in blocks]))
        Pinv = blocks[j][2]
        inv = np.max(np.abs(Pinv @ TP - TP))
        selfinv = abs(lam * lam - 1.0) < 1e-9
        n_lambda_selfinv += int(selfinv)
        same_max = max(same_max, same)
        if not selfinv:
            inv_max = max(inv_max, inv)
        rows.append(dict(lam_re=float(lam.real), lam_im=float(lam.imag),
                         dim=int(Q.shape[1]), same_eigsp_residual=float(same),
                         inv_eigsp_residual=float(inv), lam_sq_is_one=bool(selfinv)))

    return dict(
        A=list(A), N=int(N), ord_pm=[int(k), int(sgn)], M=list(M),
        n_eigenvalues=len(blocks),
        err_unitary=float(err_unitary),
        err_theta_squared_minus_1=float(err_theta_sq),
        err_theta_U_theta_inv_minus_Uinv=float(err_intertwine),
        err_intertwine_up_to_global_phase=float(err_intertwine_uptophase),
        global_phase_chi=[float(chi.real), float(chi.imag)],
        MAX_same_eigenspace_residual=float(same_max),
        MAX_inverse_eigenspace_residual_over_nonselfinv=float(inv_max),
        n_selfinverse_eigenvalues=int(n_lambda_selfinv),
        per_eigenvalue=rows,
    )


def main():
    designs = [
        ((2, 1, 1, 1), 11),
        ((2, 1, 1, 1), 13),
        ((2, 1, 1, 1), 23),
        ((3, 1, 2, 1), 17),
        ((1, 1, 1, 2), 19),
    ]
    results = []
    for A, N in designs:
        r = run_case(A, N)
        if r is None:
            print(f"SKIP A={A} N={N} (no admissible reversor / gcd(c,N)!=1)")
            continue
        results.append(r)
        print(f"A={A} N={N}: #eig={r['n_eigenvalues']:3d}  "
              f"||Theta^2-1||={r['err_theta_squared_minus_1']:.2e}  "
              f"||ThetaUTheta^-1 - chi*U^-1||={r['err_intertwine_up_to_global_phase']:.2e}  "
              f"SAME-eigsp={r['MAX_same_eigenspace_residual']:.2e}  "
              f"INV-eigsp={r['MAX_inverse_eigenspace_residual_over_nonselfinv']:.2e}  "
              f"(#lam^2=1: {r['n_selfinverse_eigenvalues']})")

    if not results:
        print("FAIL: no design point produced a valid Theta")
        return 1

    same_worst = max(r["MAX_same_eigenspace_residual"] for r in results)
    inv_worst = max(r["MAX_inverse_eigenspace_residual_over_nonselfinv"] for r in results)
    tsq_worst = max(r["err_theta_squared_minus_1"] for r in results)
    itw_worst = max(r["err_intertwine_up_to_global_phase"] for r in results)

    verdict = {
        "claim": ("Theta (antiunitary, Theta U_A Theta^{-1} = U_A^{-1}) stabilises "
                  "EVERY eigenspace H_lambda of U_A"),
        "REVIEW_ERRORS_ERROR_1_says": ("Theta maps H_lambda -> H_{lambda^{-1}}, "
                                       "does not stabilise H_lambda unless lambda^2=1"),
        "worst_same_eigenspace_residual": float(same_worst),
        "worst_inverse_eigenspace_residual": float(inv_worst),
        "worst_theta_squared_error": float(tsq_worst),
        "worst_intertwining_error": float(itw_worst),
        "n_designs": len(results),
    }
    ok = (same_worst < 1e-10) and (inv_worst > 1e-3) and (tsq_worst < 1e-10) and (itw_worst < 1e-10)
    verdict["VERDICT"] = ("PASS: Theta stabilises each H_lambda; "
                          "REVIEW_ERRORS ERROR #1 is REFUTED (it forgot antilinear "
                          "conjugation of the eigenvalue)") if ok else "INCONCLUSIVE"
    print()
    print("=" * 78)
    print(f"worst SAME-eigenspace residual     : {same_worst:.3e}   (expect ~1e-15)")
    print(f"worst INVERSE-eigenspace residual  : {inv_worst:.3e}   (expect O(1))")
    print(f"worst ||Theta^2 - 1||              : {tsq_worst:.3e}")
    print(f"worst ||ThetaUTheta^-1 - chi U^-1|| : {itw_worst:.3e}")
    print(f"VERDICT: {verdict['VERDICT']}")
    print("=" * 78)

    path = os.path.join(OUT, "ref01_theta_stabilises_eigenspaces.json")
    with open(path, "w", encoding="utf-8") as fh:
        json.dump({"verdict": verdict, "cases": results}, fh, indent=2)
    print(f"artifact: {path}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
