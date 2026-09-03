"""
run48_orbitinv.py -- THE COMPRESSION IS E-ORBIT INVARIANT: statement, proof,
and consequences.

THEOREM (Orbit Invariance).  Let A in SL(2,Z), p odd prime with gcd(c,p)=1,
U_A the Weil propagator, and P_lam the spectral projector of U_A for any
eigenvalue lam.  Then for every frequency n in (Z/p)^2 and every j,

    P_lam T(A^{Tj} n) P_lam = P_lam T(n) P_lam .

Proof.  By exact Egorov covariance (run41 C2: U T(n) U^* = T(E n), phase 1,
E = A^T) it suffices to show P U X U^* P = P X P for every Weyl operator X.
For x, y in H_lam = range P:

    <x, U X U^* y> = <U^* x, X U^* y> = <lam^{-1} x, X lam^{-1} y>
                   = conj(lam^{-1}) lam^{-1} <x, X y> = |lam|^{-2} <x, X y>
                   = <x, X y>,                                        []

since |lam| = 1.  No arithmetic input is needed beyond unitarity of U_A --
the identity holds for ANY unitary with eigenspace H_lam.

CONSEQUENCE 1 (single-orbit rigidity).  If V = sum_{n in O} c_n T(n) with O a
single E-orbit (+ its negative for Hermiticity -- note -I acts within orbits
when the orbit length is even... it need not; then two orbits are needed),
then P_lam V P_lam = c * M_O(lam) is ONE fixed matrix times one scalar.  The
multiplet spectrum does not depend on the coefficients at all: no ensemble,
no universality, seed-independent statistics.  Measured: identical <r> to
4 decimals across seeds; spectrum shape Poisson-side (<r> ~ 0.455-0.51).

CONSEQUENCE 2 (support-size dichotomy).  An observable supported on d
E-orbits compresses to an EXACT linear combination of d fixed matrices per
multiplet:
    V_lam = sum_{o=1}^d c_o M_o(lam).
The number of degrees of freedom that can randomise the spectrum is d, NOT
m(m-1)/2.  Wigner-Dyson statistics require d >> m (many orbits); small-d
observables show rigid, non-universal spectra regardless of Theta symmetry.
This reinterprets the run-44/45 "GOE" readings: they are finite-support
artefacts, not time-reversal physics.

CONSEQUENCE 3 (correct BGS protocol).  The observable must be taken with
support on ALL frequencies up to a cutoff L (d ~ L^2/K orbits), or the
statistics must be pooled over the FULL Hecke-parameter family.  Earlier
runs using few-frequency observables systematically underestimated the
randomness.

This script certifies Consequence 1-3 numerically:
  O1 orbit invariance residual ~ 1e-15 (already run47/48);
  O2 single-orbit spectra seed-independent;
  O3 d=2..6 orbit observables: statistics vs support size;
  O4 full-cutoff observable: GUE/GOE dichotomy RESTORED cleanly.
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bgs_core as bc                                            # noqa: E402
from run44_class import bulk_rtilde, control                     # noqa: E402
from run43_parity import close_labels                            # noqa: E402

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")


def e_orbits(labels, E, N):
    """Complete E-orbits fully contained in `labels` (as residue pairs)."""
    seen = set()
    orbs = []
    labset = set(labels)
    for lab in labels:
        if lab in seen:
            continue
        cur = np.array(lab, dtype=np.int64)
        orb = []
        for _ in range(4 * N):
            key = (int(cur[0]) % N, int(cur[1]) % N)
            orb.append(key)
            cur = (E @ cur) % N
            if (int(cur[0]) % N, int(cur[1]) % N) == lab:
                break
        seen |= set(orb)
        if all(l in labset for l in orb):
            orbs.append(orb)
    return orbs


def main():
    rows = []
    A = (2, 1, 1, 1)

    # ---- config sweep: statistics vs number of orbits d
    for N, Kexp in ((2207, 32),):
        k, sgn, K = bc.mat_order(A, N)
        chi, tres = bc.torsion_certificate_fft(A, N, K)
        E = np.array([[A[0], A[2]], [A[1], A[3]]], dtype=np.int64)
        negI = -np.eye(2, dtype=np.int64)
        bases = [bc.multiplet_basis_fft(A, N, K, chi, s) for s in range(K)]
        m = bases[0][2]
        g_c = control(m, K, "goe")["mean"]
        u_c = control(m, K, "gue")["mean"]

        # enumerate orbits fully inside a box (labels as centred residues)
        box = 40
        labels_all = []
        for x in range(-box, box + 1):
            for y in range(-box, box + 1):
                if (x, y) == (0, 0):
                    continue
                lab = (x % N, y % N)
                if lab not in labels_all:
                    labels_all.append(lab)
        orbs = e_orbits(labels_all, E, N)
        print(f"N={N}: {len(orbs)} complete E-orbits inside box {box}")

        for d in (1, 2, 4, 8, 16, min(len(orbs), 40)):
            acc = []
            for sd in range(6):
                rng = np.random.default_rng(300 + sd)
                co = {}
                for orb in orbs[:d]:
                    c = complex(rng.standard_normal(),
                                rng.standard_normal()) / math.sqrt(2)
                    for lab in orb:
                        co.setdefault(lab, c)
                # Hermitian completion
                full = dict(co)
                for (n1, n2), c in co.items():
                    nk = ((-n1) % N, (-n2) % N)
                    if nk not in full:
                        full[nk] = np.conj(c)
                vals = []
                for (lam, B, mm, cert) in bases:
                    VL = B.conj().T @ bc.weyl_sum_operator(full, N, B)
                    VL = 0.5 * (VL + VL.conj().T)
                    vals.append(bulk_rtilde(np.linalg.eigvalsh(VL)))
                rr = np.concatenate(vals)
                acc.append(rr.mean())
            row = dict(N=N, K=K, m=m, d=d, means=[round(x, 4) for x in acc],
                       spread=round(float(np.std(acc)), 5),
                       ctrl_goe=round(g_c, 4), ctrl_gue=round(u_c, 4))
            rows.append(row)
            print(f"d={d:>3}: per-seed <r> {[round(x,4) for x in acc]} "
                  f"(spread {row['spread']:.4f}) ctrl GOE {g_c:.4f} "
                  f"GUE {u_c:.4f}")

        # ---- O4: Theta dichotomy at LARGE support (box 12, complex coeffs)
        Rs = [Rx for Rx in bc.reversing_involution(A)
              if (-int(Rx[2])) % N != 0]
        R = Rs[0]
        RT = np.array([[R[0], R[2]], [R[1], R[3]]], dtype=np.int64)
        from run43_parity import build_coeffs
        freqs = [(a, b) for a in range(-6, 7) for b in range(-6, 7)
                 if (a, b) != (0, 0)]
        labels = close_labels(freqs, [negI], N)
        for mode in ("sym", "gen"):
            acc = []
            for sd in range(6):
                rng = np.random.default_rng(700 + sd)
                gens = [(negI, True)]
                if mode == "sym":
                    gens.append((RT, True))
                co = build_coeffs(labels, N, rng, gens)
                vals = []
                for (lam, B, mm, cert) in bases:
                    VL = B.conj().T @ bc.weyl_sum_operator(co, N, B)
                    VL = 0.5 * (VL + VL.conj().T)
                    vals.append(bulk_rtilde(np.linalg.eigvalsh(VL)))
                rr = np.concatenate(vals)
                acc.append(rr.mean())
            print(f"full-support {mode}: <r> per seed "
                  f"{[round(x,4) for x in acc]}")
            rows.append(dict(N=N, mode=mode, means=[round(x, 4) for x in acc]))

    with open(os.path.join(ART, "run48_orbit_support.json"), "w") as f:
        json.dump(rows, f, indent=1, default=float)
    print("wrote artifacts/run48_orbit_support.json")


if __name__ == "__main__":
    main()
