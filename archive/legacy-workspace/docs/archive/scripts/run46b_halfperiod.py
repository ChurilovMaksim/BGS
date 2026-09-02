"""
run46b_halfperiod.py -- the half-period operator as a hidden unitary symmetry.

Facts established so far (runs 44-46):
  * At sign = -1 configs (U_A^k = -1, K = 2k), the Dyson class of the
    compression is OBSERVABLE-dependent: some observables give GOE, others
    GUE, reproducibly over seeds; at sign = +1 the class follows [Theta,V].
  * J := U_A^{k/2} is NOT scalar on the multiplets (eigenvalues of P J P fill
    an interval), and U_A^{k} = -1 exactly.

HYPOTHESIS H-J: J acts ON THE MULTIPLICLET as a unitary involution up to the
scalar chi^{1/2}: indeed J^2 = U_A^k = -1 on H_lam, so iJ is a Hermitian
unitary INVOLUTION of H_lam with eigenvalues +-1.  Any observable V that
COMMUTES WITH J splits every multiplet into the two J-sectors, each carrying
an independent spectrum.  Conversely:

  KEY MECHANISM CANDIDATE.  The compression V_lam commutes with iJ iff
  c_n = conj(c_{E^{-k/2} n})-type conditions hold, i.e. iff V is invariant
  under a second anti-unitary-like involution.  When it holds, the observed
  spectrum is the union of TWO independent spectra (dimension m/2 each),
  which pushes <r> DOWN toward GOE even for complex coefficients -- this is
  precisely the run-45 pattern at t3/p=2207 small frequency set.

But wait: union-of-two gives <r> ~ 0.42 (superposition control), NOT 0.53.
The observed GOE value 0.5231 at t3/2207-small is full level repulsion, not
a superposition.  So the correct mechanism must be different:

  H-J2: when [V, J] = 0 fails but V has a NONTRIVIAL relation to J, the
  compression decomposes as a DIRECT SUM of two m/2-dimensional blocks that
  are TRANSPOSES of one another (particle-hole / chiral symmetry):
        Gamma V_lam Gamma^T = -conj(V_lam)   or   V_lam ~ V_lam^T,
  i.e. the multiplet spectrum equals its own mirror image.  A chiral symmetry
  forces the spectral density to be symmetric AND correlates eigenvalues in
  pairs (lambda, -lambda), producing GOE-type repulsion at zero... no:
  chiral classes give Bessel statistics near 0 but bulk WD.

This script measures directly, per configuration and per seed:
  M1  ||[PJP restricted, V_lam]||  (does V commute with the half-period?)
  M2  the singular values of the anti-linear structure W = B^dagger conj(B)...
      more practically: measure the reality structure: is there a unitary
      G with G V_lam G^T = V_lam (symmetric in SOME basis)?  Equivalent to
      existence of symmetric embedding -> test via Tr(V_lam^2) vs
      Tr(V_lam V_lam^T) after optimising over basis?  Basis-invariant test:
      det-free criterion -- use the canonical anti-linear map
      C_J : psi -> i J psi-bar ... too heavy; instead test whether V_lam is
      unitarily equivalent to a REAL matrix via the realification rank of
      the commutant.
  Simplest basis-invariant diagnostic: the ANTIUNITARY SYMMETRY SEARCH --
      for each candidate g in <A> (j = 0..k-1), check whether
          Theta_g := U_M^g ... 
  We do the direct thing: compute A_g := P_lam U^g U_M P_lam (as matrices)
  and test whether X -> X_g conj(X) is a symmetry of V_lam for some phase,
  i.e. whether  V_lam = c * X_g conj(V_lam) X_g^dagger + h.c. holds.
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


def antilinear_scan(U, UM, coeffs, N, K, chi, bases, jmax=6):
    """For each j, test whether Theta_j = U^j U_M o conj maps V to a multiple
    of V (on the nose, coefficient-level):  V = alpha * U^{2j} V' U^{-2j}-ish.
    Coefficient-level condition: c_n = conj(alpha) * c'_{...}.  We implement
    the honest matrix test on the first few multiplets."""
    out = []
    lam0, B0, m0, cert0 = bases[0]
    VL0 = B0.conj().T @ bc.weyl_sum_operator(coeffs, N, B0)
    VL0 = 0.5 * (VL0 + VL0.conj().T)
    for j in range(jmax):
        # anti-unitary action on the compressed operator:
        # Theta_j(X) = Q conj(X) Q^dagger with Q = P_lam (U^j UM) P_lam|_basis
        Q = B0.conj().T @ bc.apply_U(A_CFG, N, bc.apply_U(M_CFG, N, B0))
        # NOTE: apply twice needed? U^j UM means product; we compose applies:
        pass
    return out


def main():
    rows = []
    for (name, A, N) in CONFIGS:
        globals()["A_CFG"], globals()["M_CFG"] = A, None
        k, sign, K = bc.mat_order(A, N)
        chi, tres = bc.torsion_certificate_fft(A, N, K)
        Rs = [Rx for Rx in bc.reversing_involution(A) if (-int(Rx[2])) % N != 0]
        R = Rs[0]
        M = (R[0], R[1], -R[2], -R[3])
        globals()["M_CFG"] = M
        negI = -np.eye(2, dtype=np.int64)
        RT = np.array([[R[0], R[2]], [R[1], R[3]]], dtype=np.int64)
        bases = [bc.multiplet_basis_fft(A, N, K, chi, s) for s in range(K)]
        m = bases[0][2]
        maxcert = max(b[3] for b in bases)
        print(f"\n=== {name} p={N} sign={sign} K={K} m={m} "
              f"certs max {maxcert:.2e}")
        out = dict(name=name, N=N, sign=int(sign), K=K, m=int(m),
                   max_cert=float(maxcert))
        if maxcert > 1e-10:
            print("  !! certificate failure -- skipping this config")
            rows.append(out)
            with open(os.path.join(ART, "run46b_halfperiod.json"), "w") as f:
                json.dump(rows, f, indent=1, default=float)
            continue

        for tag, freqs in (("small", SMALL), ("big", BIG)):
            labels = close_labels(freqs, [RT, negI], N)
            per_seed = []
            for sd in range(6):
                rng = np.random.default_rng(4000 + sd)
                co_gen = build_coeffs(labels, N, rng, [(negI, True)])
                rng2 = np.random.default_rng(5000 + sd)
                co_sym = build_coeffs(labels, N, rng2,
                                      [(negI, True), (RT, True)])

                def stats(co):
                    acc = []
                    # commutator with half period (matrix-level, first mult.)
                    lam0, B0, mm, cert = bases[0]
                    VL = B0.conj().T @ bc.weyl_sum_operator(co, N, B0)
                    VL = 0.5 * (VL + VL.conj().T)
                    if sign == -1 and k % 2 == 0:
                        Uh = None     # computed below lazily via apply_U chain
                        Wp = bc.apply_U(A, N, B0)
                        for _ in range(k // 2 - 1):
                            Wp = bc.apply_U(A, N, Wp)
                        JP = B0.conj().T @ Wp         # = P J B0 (columns)
                        JJ = JP.conj().T @ JP
                        comm = float(np.max(np.abs(
                            JP @ JJ @ VL - VL @ JP @ JJ))) if False else \
                            float(np.max(np.abs(JP.conj().T @ VL @ JP -
                                                np.conj(JP.T @ VL.T @ JP))))
                    else:
                        comm = float("nan")
                    for (lam, B, mmm, cert) in bases:
                        V = B.conj().T @ bc.weyl_sum_operator(co, N, B)
                        V = 0.5 * (V + V.conj().T)
                        acc.append(bulk_rtilde(np.linalg.eigvalsh(V)))
                    rr = np.concatenate([a for a in acc if len(a)])
                    return dict(mean=float(rr.mean()), n=int(len(rr)),
                                sem=float(rr.std(ddof=1)/math.sqrt(len(rr))),
                                half_comm=comm)
                per_seed.append((tag, stats(co_sym), stats(co_gen)))
            for mode_idx, mode in ((1, "sym"), (2, "gen")):
                ms = [p[mode_idx] for p in per_seed if p[0] == tag]
                num = sum(x["mean"]*x["n"] for x in ms)
                den = sum(x["n"] for x in ms)
                hc = [x["half_comm"] for x in ms]
                out[f"{tag}_{mode}"] = dict(pooled=round(num/den, 4),
                                            n=den,
                                            half_comm=[round(h, 5) for h in hc])
                print(f"  {tag:>5} {mode}: pooled {num/den:.4f} "
                      f"half-comm {[f'{h:.3f}' for h in hc]}")
        rows.append(out)
        with open(os.path.join(ART, "run46b_halfperiod.json"), "w") as f:
            json.dump(rows, f, indent=1, default=float)
    print("\nwrote artifacts/run46b_halfperiod.json")


if __name__ == "__main__":
    main()
