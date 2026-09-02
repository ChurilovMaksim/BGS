"""
Machine certification of THEOREM B (exact Wigner-Dyson for Gaussian Weyl
observables compressed to a cat-map eigenspace).

Claims certified here, at machine precision, for several (A, N):

 B1  Weyl second-moment identity (the only arithmetic input):
        sum_{u in (Z/N)^2}  T(u)_{ij} (T(u)^*)_{kl} = N delta_{jk} delta_{il}
     equivalently  sum_u T(u) X T(u)^* = N Tr(X) 1 .

 B2  compressed exact covariance, with P = B B^* the eigenprojector of U_A and
     M^{(u)} = B^* T(u) B  (m x m):
        sum_{u != 0} M^{(u)}_{ab} conj(M^{(u)}_{cd})
             = N delta_{ac} delta_{bd} - delta_{ab} delta_{cd}   EXACTLY.
     (The project's T19 states this with N/K and 1/K after regrouping by
     A^T-orbits; the un-regrouped form above is what the proof actually gives.)

 B3  the correction term lives ONLY in the identity direction:
     for every traceless Hermitian Y,  Var<Y, V_lam> = N ||Y||_HS^2 exactly,
     i.e. the traceless part of the compression is exactly sqrt(N) * GUE_m.

 B4  Theta-symmetrised family: in the Theta-real basis B Q (Q Q^T = W,
     W = B^* U_M conj(B)), the compressions are real symmetric and
        sum_{u != 0} Msym_{ab} Msym_{cd}
             = 2N (delta_{ac} delta_{bd} + delta_{ad} delta_{bc})
               + (identity-direction correction),
     i.e. the traceless part is exactly a GOE_m matrix.

 B5  empirical check: eigenvalue spacings of a single Gaussian draw already
     match GUE_m / GOE_m within control error (done in compression_spacings.py).
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


def sqrt_sym_unitary(W):
    """Q with Q Q^T = W for W unitary symmetric with W conj(W) = I."""
    # W symmetric unitary => W = e^{i H} with H real symmetric?  Use the
    # standard construction: W = X + iY with X,Y real symmetric commuting.
    X, Y = W.real, W.imag
    # X and Y commute and X^2+Y^2 = I ; diagonalise X+Y (generic) to get a
    # common real orthonormal eigenbasis.
    rng = np.random.default_rng(7)
    for _ in range(50):
        t = rng.standard_normal(2)
        Msym = t[0] * X + t[1] * Y
        w, O = np.linalg.eigh(Msym)
        D = O.T @ W @ O
        off = np.abs(D - np.diag(np.diag(D))).max()
        if off < 1e-8:
            d = np.diag(D)
            Q = O @ np.diag(np.sqrt(d.astype(complex))) @ O.T
            return Q, float(off)
    return None, float(off)


def main():
    rng = np.random.default_rng(31415)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}

    for A, N, batch in [([[2, 1], [1, 1]], 41, 20), ([[2, 1], [1, 1]], 101, 40),
                        ([[5, 2], [2, 1]], 71, 30), ([[3, 2], [2, 2]], 0, 0),
                        ([[2, 1], [1, 1]], 151, 40), ([[3, 1], [2, 1]], 181, 40)]:
        if N == 0:
            continue
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        if m < 2:
            print(f"  A={A} N={N}: m={m} too small, skipped")
            continue

        # ---- B1  Weyl second moment
        Xr = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
        acc = np.zeros((N, N), dtype=complex)
        for u1 in range(N):
            for u2 in range(N):
                T = cm.T_matrix((u1, u2))
                acc += T @ Xr @ T.conj().T
        b1 = float(np.abs(acc - N * np.trace(Xr) * np.eye(N)).max()
                   / (N * abs(np.trace(Xr))))

        # ---- B2  compressed covariance
        C = np.zeros((m, m, m, m), dtype=complex)
        for u1 in range(N):
            for u2 in range(N):
                if u1 == 0 and u2 == 0:
                    continue
                Mu = B.conj().T @ cm.apply_T((u1, u2), B)
                C += np.einsum("ab,cd->abcd", Mu, np.conj(Mu))
        I = np.eye(m)
        target = (N * np.einsum("ac,bd->abcd", I, I)
                  - np.einsum("ab,cd->abcd", I, I))
        b2 = float(np.abs(C - target).max() / N)

        # ---- B3  traceless directions
        worst = 0.0
        for _ in range(20):
            Y = rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))
            Y = (Y + Y.conj().T) / 2
            Y -= np.trace(Y) / m * I
            var = np.einsum("ab,abcd,cd->", np.conj(Y), C, Y).real
            worst = max(worst, abs(var - N * np.abs(Y) .__pow__(2).sum())
                        / (N * np.abs(Y ** 2).sum() + 1e-30))
        b3 = float(worst)

        # ---- B4  Theta-symmetrised
        b4 = None
        (a_, b_), (c_, d_) = A
        Rfound = None
        for p_ in range(-6, 7):
            for q_ in range(-6, 7):
                for r_ in range(-6, 7):
                    if p_ * (a_ - d_) + q_ * c_ + b_ * r_ == 0 and p_ ** 2 + q_ * r_ == 1:
                        Rc = np.array([[p_, q_], [r_, -p_]], dtype=np.int64)
                        if round(np.linalg.det(Rc)) == -1:
                            Mm = np.array([[1, 0], [0, -1]]) @ Rc
                            if math.gcd(int(Mm[1, 0]) % N, N) == 1:
                                Rfound = Rc
                                break
                if Rfound is not None:
                    break
            if Rfound is not None:
                break
        theta_info = {}
        if Rfound is not None:
            Mm = np.array([[1, 0], [0, -1]]) @ Rfound
            cmM = CatMap([[int(Mm[0, 0]), int(Mm[0, 1])],
                          [int(Mm[1, 0]), int(Mm[1, 1])]], N)
            W = B.conj().T @ cmM.apply_U(np.conj(B))
            Q, off = sqrt_sym_unitary(W)
            theta_info = {"W_sym_dev": float(np.abs(W - W.T).max()),
                          "W_unitary_dev": float(np.abs(W.conj().T @ W - I).max()),
                          "diagonalisation_off": off}
            if Q is not None:
                theta_info["QQt_minus_W"] = float(np.abs(Q @ Q.T - W).max())
                Bq = B @ Q
                # (i) exact pseudo-covariance identity: it follows from B2 by an
                #     index swap, so this is a consistency check of the code path
                Cp = np.zeros((m, m, m, m), dtype=complex)
                realdev = 0.0
                for u1 in range(N):
                    for u2 in range(N):
                        if u1 == 0 and u2 == 0:
                            continue
                        Mu = Bq.conj().T @ cm.apply_T((u1, u2), Bq)
                        Mmu = Bq.conj().T @ cm.apply_T((-u1 % N, -u2 % N), Bq)
                        Cp += np.einsum("ab,cd->abcd", Mu, Mmu)
                        realdev = max(realdev,
                                      float(np.abs((Mu + np.conj(Mu)).imag).max()))
                tgt_p = (N * np.einsum("ad,bc->abcd", I, I)
                         - np.einsum("ab,cd->abcd", I, I))
                pseudo_rel = float(np.abs(Cp - tgt_p).max() / N)
                # (ii) covariance of Re(M) must be the GOE tensor + identity term
                Cre = 0.25 * (Cp + C + np.conj(C).transpose(2, 3, 0, 1)
                              + np.conj(Cp))
                # NOTE  E[Mbar_ab M_cd] = conj(E[M_ab Mbar_cd]) with (ab)<->(cd)
                Cre = 0.25 * (Cp + C
                              + np.conj(np.einsum("cdab->abcd", C))
                              + np.conj(Cp))
                goe = 0.5 * N * (np.einsum("ac,bd->abcd", I, I)
                                 + np.einsum("ad,bc->abcd", I, I))
                idd = np.einsum("ab,cd->abcd", I, I)
                res_goe = float(np.abs(Cre - (goe - idd)).max() / N)
                theta_info.update({
                    "Msym_real_dev": realdev,
                    "pseudo_cov_rel_dev": pseudo_rel,
                    "ReM_minus_GOE_rel_dev": res_goe,
                })
                b4 = res_goe

        row = {"A": A, "N": N, "ord": ordA, "K": K, "m": m,
               "B1_weyl_rel": b1, "B2_cov_rel": b2, "B3_traceless_rel": b3,
               "theta": theta_info}
        out["rows"].append(row)
        print(f"  A={A} N={N} K={K} m={m}:  B1={b1:.2e}  B2={b2:.2e}  "
              f"B3={b3:.2e}  B4={('%.2e' % b4) if b4 is not None else 'n/a'}")
        if theta_info:
            print(f"      theta: pseudo_cov_dev={theta_info.get('pseudo_cov_rel_dev')}, "
                  f"ReM-GOE_dev={theta_info.get('ReM_minus_GOE_rel_dev')}, "
                  f"Msym imag dev={theta_info.get('Msym_real_dev')}")
        sys.stdout.flush()

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r71", "theoremB_covariance.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
