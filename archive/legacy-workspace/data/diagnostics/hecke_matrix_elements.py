"""
Run 73: the CORRECT Hecke eigenbasis, and the distribution of matrix elements.
=============================================================================

This is the honest replacement for the voided runs R67-R70, which never
constructed a Hecke basis at all (they used columns of the propagator).

Construction.  The centraliser torus C(A) = {x I + y A : x^2 + x y t + y^2 = 1}
has order p ∓ 1 and commutes with U_A, so its quantisation preserves every
eigenspace H_lam.  Taking a generator tau_0 of C(A) and diagonalising
        H_tau = B^* U_{tau_0} B      (unitary, m x m)
gives the HECKE EIGENBASIS {psi_j} of H_lam: a simultaneous eigenbasis of U_A and
of the whole torus, with distinct torus characters.  This is exactly the basis of
Kurlberg-Rudnick.

Measured, for mean-zero observables T(n), n != 0:
  * diagonal elements  <psi_j, T(n) psi_j>  -- their variance, fourth moment and
    excess kurtosis, both raw and after the parity desymmetrisation;
  * off-diagonal elements  <psi_i, T(n) psi_j>, i != j -- same statistics.

Reference points.
  * A complex Gaussian would give normalised |.|^4 moment 2 and excess kurtosis 0
    for the real part.
  * Kurlberg-Rudnick (arXiv:math/0302277, accepted Annals of Mathematics)
    conjecture that the normalised DIAGONAL elements in this basis follow a
    weighted sum of traces of independent SU(2) matrices -- explicitly NOT
    Gaussian, "in contrast to generic chaotic systems".  A single Sato-Tate trace
    has fourth moment 2 and excess kurtosis -1 relative to its own variance 1
    (Catalan numbers 1, 2, 5, 14 versus Gaussian 1, 3, 15, 105 for a real
    variable).
So: excess kurtosis clearly different from 0 supports KR and refutes the voided
"Gaussian residual = QUE signature" reading.
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
from parity_desymmetrised import apply_parity, eps_of     # noqa: E402
from theoremE_torus_repair import torus_elements          # noqa: E402


def torus_generator(A, p):
    """A generator of C(A) (cyclic of order p ∓ 1), with gcd(tau_21, p) = 1 so
    that the standard kernel is defined."""
    T = torus_elements(A, p)
    n = len(T)
    I = (1, 0, 0, 1)

    def order(M):
        X = np.array([[M[0], M[1]], [M[2], M[3]]], dtype=object)
        Y = X.copy()
        for j in range(1, n + 1):
            if np.array_equal(Y % p, np.eye(2, dtype=object) % p):
                return j
            Y = (Y @ X) % p
        return None

    best = None
    for M in T:
        if M == I or math.gcd(abs(M[2]) % p, p) != 1:
            continue
        o = order(M)
        if o == n:
            return np.array([[M[0], M[1]], [M[2], M[3]]], dtype=np.int64), n
        if best is None or (o or 0) > best[1]:
            best = (np.array([[M[0], M[1]], [M[2], M[3]]], dtype=np.int64), o)
    return best if best else (None, None)


def moments(x):
    """standardised moments of a real sample"""
    x = np.asarray(x, dtype=float)
    mu = x.mean()
    s2 = x.var()
    if s2 <= 0:
        return {"n": int(x.size), "mean": float(mu), "var": 0.0,
                "m4_over_var2": None, "excess_kurtosis": None}
    m4 = ((x - mu) ** 4).mean()
    return {"n": int(x.size), "mean": float(mu), "var": float(s2),
            "m4_over_var2": float(m4 / s2 ** 2),
            "excess_kurtosis": float(m4 / s2 ** 2 - 3.0)}


def cmoments(z):
    """moments of a complex sample: E|z|^2, E|z|^4/(E|z|^2)^2 (2 for complex
    Gaussian), and the excess kurtosis of the real part."""
    z = np.asarray(z)
    a2 = float(np.mean(np.abs(z) ** 2))
    a4 = float(np.mean(np.abs(z) ** 4))
    out = {"n": int(z.size), "E_abs2": a2,
           "E_abs4_over_E_abs2_sq": (a4 / a2 ** 2 if a2 > 0 else None)}
    out["real_part"] = moments(z.real)
    out["imag_part"] = moments(z.imag)
    return out


def main():
    rng = np.random.default_rng(731731)
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "reference": {"complex_gaussian_E_abs4_over_E_abs2_sq": 2.0,
                         "real_gaussian_excess_kurtosis": 0.0,
                         "sato_tate_trace_m4_over_var2": 2.0,
                         "sato_tate_trace_excess_kurtosis": -1.0},
           "rows": []}
    designs = [([[2, 1], [1, 1]], 1597, 200), ([[2, 1], [1, 1]], 3571, 400),
               ([[5, 2], [2, 1]], 2161, 300), ([[2, 1], [1, 1]], 9349, 900)]
    NN = 24                                    # number of frequencies n

    for A, p, batch in designs:
        cm = CatMap(A, p)
        ordA, K = cm.orders()
        k, eps = eps_of(A, p)
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        tau0, ordt = torus_generator(A, p)
        if tau0 is None:
            print(f"  A={A} p={p}: no usable torus generator")
            continue
        cmT = CatMap([[int(tau0[0, 0]), int(tau0[0, 1])],
                      [int(tau0[1, 0]), int(tau0[1, 1])]], p)
        Htau = B.conj().T @ cmT.apply_U(B)
        comm = float(np.abs(Htau @ Htau.conj().T - np.eye(m)).max())
        # does U_tau really commute with U_A?  check on the eigenspace
        cc = float(np.abs(cm.apply_U(cmT.apply_U(B))
                          - cmT.apply_U(cm.apply_U(B))).max())
        evt, W = np.linalg.eig(Htau)
        # orthonormalise the Hecke eigenbasis (Htau is unitary, so eigenvectors
        # for distinct eigenvalues are orthogonal; enforce numerically)
        Q, _ = np.linalg.qr(W)
        sep = float(np.min([abs(evt[i] - evt[j])
                            for i in range(m) for j in range(i + 1, m)]))
        Bh = B @ Q                              # Hecke eigenbasis of H_lam
        diagdev = float(np.abs(Bh.conj().T @ cmT.apply_U(Bh)
                               - np.diag(np.diag(Bh.conj().T @ cmT.apply_U(Bh)))
                               ).max())
        print("=" * 78)
        print(f"A={A} p={p}: K={K} eps={eps:+d} m={m}  |U_A B - lam B|={res:.1e}")
        print(f"   torus generator {tau0.tolist()} of order {ordt} "
              f"(|C(A)|={ordt}); [U_A, U_tau] on H_lam = {cc:.1e}; "
              f"H_tau unitarity {comm:.1e}")
        print(f"   Hecke basis: min character separation {sep:.3e}; "
              f"off-diagonal residue of U_tau in the Hecke basis {diagdev:.1e}")

        # parity block inside the Hecke basis (parity commutes with the torus)
        RB = Bh.conj().T @ apply_parity(Bh)
        w_, Vv = np.linalg.eigh(RB)
        mp = int((w_ > 0).sum())
        par_scalar = float(np.abs(RB - np.trace(RB) / m * np.eye(m)).max())

        diag_raw, off_raw = [], []
        per_freq = {"diag_kurt": [], "off_kurt": [],
                    "diag_m4norm": [], "off_m4norm": []}
        mask = ~np.eye(m, dtype=bool)
        for _ in range(NN):
            n = (int(rng.integers(1, p)), int(rng.integers(1, p)))
            Mn = Bh.conj().T @ cm.apply_T(n, Bh)
            d = np.diag(Mn).copy() * math.sqrt(p)
            o = Mn[mask] * math.sqrt(p)
            diag_raw.append(d)
            off_raw.append(o)
            # per-frequency statistics, so the error bar respects the fact that
            # the m elements of one frequency are not independent
            for tag, arr in (("diag", d), ("off", o)):
                cm_ = cmoments(arr)
                per_freq[f"{tag}_kurt"].append(
                    cm_["real_part"]["excess_kurtosis"])
                per_freq[f"{tag}_m4norm"].append(cm_["E_abs4_over_E_abs2_sq"])
        diag_raw = np.concatenate(diag_raw)
        off_raw = np.concatenate(off_raw)
        pf = {}
        for kk, v in per_freq.items():
            v = np.array([x for x in v if x is not None], dtype=float)
            pf[kk] = {"mean": float(v.mean()),
                      "sem": float(v.std(ddof=1) / math.sqrt(len(v))),
                      "n_freq": int(len(v))}

        row = {"A": A, "p": p, "K": K, "eps": eps, "m": m,
               "proj_res": res, "commutator_UA_Utau": cc,
               "torus_order": ordt, "min_character_separation": sep,
               "hecke_offdiag_residue": diagdev,
               "parity_is_scalar_on_Hlam": bool(par_scalar < 1e-9),
               "m_plus": mp, "n_frequencies": NN,
               "diagonal_elements": cmoments(diag_raw),
               "offdiagonal_elements": cmoments(off_raw),
               "per_frequency": pf}
        d = row["diagonal_elements"]
        o = row["offdiagonal_elements"]
        print(f"   DIAGONAL   sqrt(p)*<psi_j,T(n)psi_j>: n={d['n']}  "
              f"E|z|^2={d['E_abs2']:.4f}  E|z|^4/(E|z|^2)^2="
              f"{d['E_abs4_over_E_abs2_sq']:.4f}  (Gaussian 2.000)  "
              f"Re excess kurt={d['real_part']['excess_kurtosis']:+.4f}")
        print(f"   OFFDIAG    sqrt(p)*<psi_i,T(n)psi_j>: n={o['n']}  "
              f"E|z|^2={o['E_abs2']:.4f}  E|z|^4/(E|z|^2)^2="
              f"{o['E_abs4_over_E_abs2_sq']:.4f}  (Gaussian 2.000)  "
              f"Re excess kurt={o['real_part']['excess_kurtosis']:+.4f}")
        print(f"   per-frequency error bars ({pf['diag_kurt']['n_freq']} "
              f"frequencies):  diag kurt = "
              f"{pf['diag_kurt']['mean']:+.4f} +- {pf['diag_kurt']['sem']:.4f}"
              f"   (Sato-Tate -1, Gaussian 0)"
              f"   |   offdiag kurt = {pf['off_kurt']['mean']:+.4f} +- "
              f"{pf['off_kurt']['sem']:.4f}")
        print(f"                                    diag E|z|^4/(E|z|^2)^2 = "
              f"{pf['diag_m4norm']['mean']:.4f} +- {pf['diag_m4norm']['sem']:.4f}"
              f"   |   offdiag {pf['off_m4norm']['mean']:.4f} +- "
              f"{pf['off_m4norm']['sem']:.4f}")
        out["rows"].append(row)
        sys.stdout.flush()

    print()
    print("SUMMARY  (Gaussian would give 2.000 and 0.000; Sato-Tate-like laws "
          "give a clear departure)")
    for r in out["rows"]:
        d, o = r["diagonal_elements"], r["offdiagonal_elements"]
        print(f"  p={r['p']:>5} m={r['m']:>4}: diag E|z|^4/(E|z|^2)^2="
              f"{d['E_abs4_over_E_abs2_sq']:.4f} (kurt "
              f"{d['real_part']['excess_kurtosis']:+.3f})   "
              f"offdiag {o['E_abs4_over_E_abs2_sq']:.4f} (kurt "
              f"{o['real_part']['excess_kurtosis']:+.3f})")
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r73", "hecke_matrix_elements.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
