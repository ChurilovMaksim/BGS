"""
RED TEAM: refutation of the "Hecke-centring collapse" (project runs R67-R70).
============================================================================

The claim under test (LEDGER R67-R70, THEORY 8.0.4-8.0.7, HANDOFF "the main
empirical discovery of this run"):

    for 11 design points, the residual  R_n = V_lam - A_n, where A_n is the
    "Hecke mean over 64 Haar-orthogonal rotations", has off-diagonal excess
    kurtosis <= 0.25, a reduction of 5x-7842x from the RAW value; this is
    "the empirical signature of Quantum Unique Ergodicity in the Hecke basis".

Two defects are tested here.

F1  In `tools/hecke_real_centraliser_v6.jl` (and v7-v10, which inherit it) the
    multiplet basis is built as

        ev_U   = eigvals(U)                    # eigenVALUES only
        idx    = [i for i in 1:N if angle(ev_U[i]) in window]
        U_sub  = U[:, idx]                     # <-- COLUMNS OF THE PROPAGATOR

    `U[:, idx]` are columns of the unitary propagator selected by *eigenvalue
    index*.  They are an orthonormal frame, but they span the image under U of
    the coordinate subspace spanned by {e_i : i in idx}, which has nothing to do
    with the eigenspace of U for the chosen eigenvalue.  There is no call to
    `eigen`/`eigvecs` anywhere in the file.  Hence `V_lam` is not a compression
    to a multiplet, and no Hecke operator occurs anywhere in the computation.

F2  For Haar-distributed Q on C^m,   E_Q[ Q V Q^* ] = (Tr V / m) * I .
    So the population "Hecke mean" is a multiple of the identity, and
    subtracting it CANNOT change a single off-diagonal entry.  With n_hecke = 64
    samples the procedure instead subtracts
        (Tr V/m) I  +  (a Gaussian-like fluctuation of size ~ sigma_V/sqrt(m*n)),
    i.e. it INJECTS approximately Gaussian noise into the off-diagonal entries.
    Whenever that noise floor exceeds the true off-diagonal scale, the excess
    kurtosis of the sum is driven to 0 by construction, and the "reduction
    factor" is just the noise-to-signal ratio.

PREDICTIONS (pre-registered before running):
    P1  the collapse occurs identically for a basis with NO arithmetic content
        (a Haar-random orthonormal m-frame);
    P2  the collapse WEAKENS monotonically as n_hecke grows, and
        kurt(R_n) -> kurt(RAW) as n_hecke -> infinity;
    P3  the "reduction factor" scales like n_hecke (variance of the injected
        noise ~ 1/n_hecke), not like any spectral invariant.
If P1-P3 hold, the R67-R70 claim is an artifact and must be retracted.
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                    # noqa: E402
from compression_spacings import eigen_basis             # noqa: E402


def V_arith_cycles(N: int, C: int, seed: int) -> np.ndarray:
    """Faithful port of the project's Julia V_arith_cycles (sum of C random
    Weyl operators with unit coefficients, Hermitised)."""
    rng = np.random.RandomState(seed)
    V = np.zeros((N, N), dtype=complex)
    b2 = pow(2, -1, N)
    j = np.arange(N)
    for _ in range(C):
        n_shift = int(rng.randint(0, N))
        m_phase = int(rng.randint(0, N))
        phase = np.exp(2j * np.pi * ((b2 * n_shift * m_phase) % N) / N)
        col = (j + n_shift) % N
        V[j, col] += phase * np.exp(2j * np.pi * ((m_phase * j) % N) / N)
    V /= C
    return (V + V.conj().T) / 2


def kurt_offdiag(M: np.ndarray) -> float:
    n = M.shape[0]
    mask = ~np.eye(n, dtype=bool)
    x = M[mask].real
    mu = x.mean()
    s2 = ((x - mu) ** 2).mean()
    if s2 ** 2 < 1e-30:
        return 0.0
    return float(((x - mu) ** 4).mean() / s2 ** 2 - 3.0)


def haar_centre(Vl: np.ndarray, n_hecke: int, rng) -> np.ndarray:
    m = Vl.shape[0]
    acc = np.zeros((m, m), dtype=complex)
    for _ in range(n_hecke):
        Z = (rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m)))
        Q, R = np.linalg.qr(Z)
        Q = Q * (np.diag(R) / np.abs(np.diag(R)))          # Haar fix-up
        acc += Q @ Vl @ Q.conj().T
    acc /= n_hecke
    acc = (acc + acc.conj().T) / 2
    return Vl - acc


def churilov_tail(M):
    s = np.linalg.svd(M, compute_uv=False)
    return float(s.max() / np.median(s))


def main():
    rng = np.random.default_rng(2718281828)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "predictions": ["P1 arithmetic-free basis shows the same collapse",
                           "P2 collapse vanishes as n_hecke grows",
                           "P3 reduction factor ~ n_hecke"],
           "rows": []}

    for A, N, batch in [([[2, 1], [1, 1]], 1597, 120),
                        ([[2, 1], [1, 1]], 2161, 120)]:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        Bc, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        V = V_arith_cycles(N, 100, 42)

        # --- three bases of the same dimension m
        bases = {}
        bases["correct_eigenspace"] = Bc
        # the project's buggy basis: m columns of the propagator, chosen by
        # (arbitrary) eigenvalue index -> emulate with m arbitrary columns of U
        Ucols = cm.apply_U(np.eye(N, dtype=complex)[:, :m])
        bases["project_bug_U_columns"] = Ucols
        # arithmetic-free control: Haar-random orthonormal m-frame
        Z = rng.standard_normal((N, m)) + 1j * rng.standard_normal((N, m))
        Qr, _ = np.linalg.qr(Z)
        bases["random_frame_control"] = Qr

        print("=" * 78)
        print(f"A={A} N={N} K={K} m={m}  (eigenbasis residual {res:.1e})")
        for name, Bm in bases.items():
            orth = float(np.abs(Bm.conj().T @ Bm - np.eye(m)).max())
            Vl = Bm.conj().T @ V @ Bm
            Vl = (Vl + Vl.conj().T) / 2
            kr = kurt_offdiag(Vl)
            offscale = float(np.abs(Vl - np.diag(np.diag(Vl))).std())
            row = {"A": A, "N": N, "m": m, "basis": name,
                   "orthonormality_dev": orth, "RAW_kurt": kr,
                   "offdiag_std": offscale, "sweep": {}}
            print(f"  basis={name:<24} |B*B-I|={orth:.1e}  RAW kurt={kr:+.4f}  "
                  f"offdiag std={offscale:.3e}")
            for n_hecke in (8, 64, 512, 4096, 32768):
                t0 = time.time()
                R = haar_centre(Vl, n_hecke, rng)
                kR = kurt_offdiag(R)
                noise = float(np.abs(R - Vl).std())
                red = (kr / kR) if abs(kR) > 1e-12 else float("inf")
                row["sweep"][n_hecke] = {"kurt_R": kR, "reduction": red,
                                         "injected_noise_std": noise,
                                         "churilov": churilov_tail(R),
                                         "secs": round(time.time() - t0, 1)}
                print(f"      n_hecke={n_hecke:>6}: kurt(R_n)={kR:+.4f}  "
                      f"reduction={red:>9.1f}x  injected noise std="
                      f"{noise:.3e}  ratio noise/offdiag="
                      f"{noise/offscale:6.3f}  churilov={churilov_tail(R):.2f}")
                sys.stdout.flush()
            out["rows"].append(row)

    # ---- verdict
    v = {}
    for row in out["rows"]:
        ks = [(n, d["kurt_R"]) for n, d in row["sweep"].items()]
        v[f"{row['N']}_{row['basis']}"] = {
            "RAW": row["RAW_kurt"],
            "kurt_R_by_n_hecke": {str(n): k for n, k in ks},
            "monotone_recovery": all(abs(ks[i][1]) <= abs(ks[i + 1][1]) + 1e-9
                                     for i in range(len(ks) - 1)),
        }
    out["verdict"] = v
    print("\nVERDICT (kurt(R_n) as a function of n_hecke; RAW in brackets)")
    for kk, vv in v.items():
        print(f"  {kk}: RAW={vv['RAW']:+.3f}  " +
              " ".join(f"n={n}:{val:+.3f}" for n, val in
                       vv["kurt_R_by_n_hecke"].items()))
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r71", "hecke_centring_refutation.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__" and "--exact" not in sys.argv:
    raise SystemExit(main())


# ---------------------------------------------------------------------------
# ADDENDUM (run separately as `python hecke_centring_refutation.py --exact`):
# faithful reproduction of the project's code path, INCLUDING the missing
# division by n_hecke.  In the Julia source the accumulator is
#
#     A_n_haar = zeros(...); for _ in 1:n_hecke  A_n_haar += Q*V_lam*Q'  end
#     A_n_haar = Hermitian((A_n_haar + A_n_haar')/2)      # <-- never /= n_hecke
#
# so the subtracted "Hecke mean" is n_hecke times too large and the residual is
# dominated by  sqrt(n_hecke) x  the single-sample Haar fluctuation.
# ---------------------------------------------------------------------------

def haar_centre_undivided(Vl, n_hecke, rng):
    m = Vl.shape[0]
    acc = np.zeros((m, m), dtype=complex)
    for _ in range(n_hecke):
        Z = (rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m)))
        Q, R = np.linalg.qr(Z)
        Q = Q * (np.diag(R) / np.abs(np.diag(R)))
        acc += Q @ Vl @ Q.conj().T
    acc = (acc + acc.conj().T) / 2          # NO division by n_hecke
    return Vl - acc


def addendum():
    rng = np.random.default_rng(4242)
    res = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}
    print("=" * 78)
    print("ADDENDUM: project code path reproduced WITH the missing /n_hecke")
    print("=" * 78)
    for A, N, batch in [([[2, 1], [1, 1]], 1597, 120),
                        ([[2, 1], [1, 1]], 2161, 120)]:
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        Bc, lam, m, r0, chi = eigen_basis(cm, K, 0, batch, rng)
        V = V_arith_cycles(N, 100, 42)
        Ucols = cm.apply_U(np.eye(N, dtype=complex)[:, :m])
        for name, Bm in (("correct_eigenspace", Bc),
                         ("project_bug_U_columns", Ucols)):
            Vl = Bm.conj().T @ V @ Bm
            Vl = (Vl + Vl.conj().T) / 2
            kr = kurt_offdiag(Vl)
            print(f"  N={N} m={m} basis={name}: RAW kurt={kr:+.4f}")
            for n_hecke in (8, 64, 512):
                R = haar_centre_undivided(Vl, n_hecke, rng)
                kR = kurt_offdiag(R)
                red = (kr / kR) if abs(kR) > 1e-12 else float("inf")
                noise = float(np.abs(R - Vl).std())
                offs = float(np.abs(Vl - np.diag(np.diag(Vl))).std())
                print(f"      n_hecke={n_hecke:>4} (undivided): "
                      f"kurt(R_n)={kR:+.4f}  reduction={red:>10.1f}x  "
                      f"noise/offdiag={noise/offs:8.2f}  "
                      f"churilov={churilov_tail(R):.2f}")
                res["rows"].append({"N": N, "m": m, "basis": name,
                                    "RAW_kurt": kr, "n_hecke": n_hecke,
                                    "kurt_R": kR, "reduction": red,
                                    "noise_over_offdiag": noise / offs,
                                    "churilov": churilov_tail(R)})
            sys.stdout.flush()
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r71", "hecke_centring_undivided.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))


if __name__ == "__main__" and "--exact" in sys.argv:
    raise SystemExit(addendum())
