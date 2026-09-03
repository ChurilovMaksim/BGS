"""
run47_seedinv.py -- the seed-invariance phenomenon at sign = -1.

Run-46 finding: for A = (2,1,1,1), p = 2207 (A^k = -1), a SINGLE-E-orbit
observable has compressed spectra whose <r> is identical across coefficient
seeds to 4+ decimals, although the spectra themselves differ.  Also all frame
matrices {B^dag T(E^j n) B}_j of one orbit commute and are simultaneously
diagonalisable.

This script pins down the algebra:
  P1  For each multiplet: eigen-decompose H_0 (Hermitian part); express every
      other frame matrix in that basis; check diagonal vs off-diagonal.
  P2  Compute the spectrum of W(a,b) as an explicit linear image and test
      whether the SPACING PATTERN is independent of (a,b): i.e. whether the
      map (a,b) -> spectrum is via a FIXED matrix with row-scaling.
  P3  Test whether the same holds for TWO orbits (does seed-dependence return?
      run45 said yes for big supports).
"""
import sys, os, json, math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bgs_core as bc                                            # noqa: E402
from run44_class import bulk_rtilde                              # noqa: E402


def orbit(root, E, N):
    cur = np.array(root, dtype=np.int64) % N
    out = []
    for _ in range(4 * N):
        key = (int(cur[0]) % N, int(cur[1]) % N)
        out.append(key)
        cur = (E @ cur) % N
        if (int(cur[0]) % N, int(cur[1]) % N) == (root[0] % N, root[1] % N):
            break
    return out


def main():
    A = (2, 1, 1, 1)
    N = 2207
    k, sgn, K = bc.mat_order(A, N)
    chi, res = bc.torsion_certificate_fft(A, N, K)
    E = np.array([[A[0], A[2]], [A[1], A[3]]], dtype=np.int64)
    lam, B, m, cert = bc.multiplet_basis_fft(A, N, K, chi, 0)

    orb0 = orbit((1, 0), E, N)
    frames = []
    for lab in orb0:
        H = B.conj().T @ bc.apply_T(lab[0], lab[1], B, N)
        frames.append(H)

    # P1: simultaneous diagonalisation over the full family incl. adjoints
    S = sum(h.real for h in frames[:1])
    Hc = sum((h + h.conj().T) * complex(0.3 + 0.11 * i, -0.07 * i)
             for i, h in enumerate(frames))     # generic member
    evH, QH = np.linalg.eigh(Hc)
    offd = max(float(np.max(np.abs(QH.conj().T @ h @ QH -
                                   np.diag(np.diag(QH.conj().T @ h @ QH)))))
               for h in frames[::5] + [h.conj().T for h in frames[::5]])
    print("simultaneous-diagonalisation residual over frames+adjoints:",
          f"{offd:.2e}")

    # diagonal entries of each frame in the common basis:
    D = np.array([np.diag(QH.conj().T @ h @ QH).real for h in frames])  # K x m
    # P2: W(g) has eigenvalues = D^T g (complex!) -- but W must be Hermitian:
    # Hermitian completion makes W = sum_j [a_j Re-part + b_j Im-part], so
    # eigenvalues are mu_i = sum_j alpha_j D[j,i] + beta_j E[j,i] where E is
    # the diagonal of the adjoint frames.  Both real.  So the eigenvalue
    # VECTOR is a random projection of a fixed 2K-dim vector family!
    Dadj = np.array([np.diag(QH.conj().T @ h.conj().T @ QH).real
                     for h in frames])
    rng = np.random.default_rng(0)
    mus = []
    for sd in range(6):
        r = np.random.default_rng(sd)
        al = r.standard_normal(K)
        be = r.standard_normal(K)
        mus.append(D.T @ al + Dadj.T @ be)
    mus = np.array(mus)                       # 6 x m
    # spacings pattern correlation across draws:
    sp0 = np.diff(np.sort(mus[0]))
    cors = []
    for i in range(1, 6):
        spi = np.diff(np.sort(mus[i]))
        if len(spi) == len(sp0):
            cors.append(float(np.corrcoef(
                sp0 / sp0.mean(), spi / spi.mean())[0, 1]))
    print("spacing-pattern correlations across coefficient draws:",
          [round(c, 4) for c in cors])

    # but wait: the ACTUAL compression also mixes multiplets? No: it is block
    # per multiplet; we did only s=0. The observed <r> pooled over ALL K
    # multiplets equal across seeds. Verify the same structure holds in
    # another multiplet and then pool.
    print("\nP3: two-orbit observables")
    acc_single, acc_double = [], []
    for sd in range(6):
        r = np.random.default_rng(sd)
        co = {}
        for lab in orbit((1, 0), E, N):
            c = complex(r.standard_normal(), r.standard_normal()) / math.sqrt(2)
            co[lab] = c
            co[((-lab[0]) % N, (-lab[1]) % N)] = np.conj(c)
        vals = []
        for s0 in range(K):
            lam2, B2, m2, c2 = bc.multiplet_basis_fft(A, N, K, chi, s0)
            VL = B2.conj().T @ bc.weyl_sum_operator(co, N, B2)
            VL = 0.5 * (VL + VL.conj().T)
            vals.append(bulk_rtilde(np.linalg.eigvalsh(VL)))
        rr = np.concatenate(vals)
        acc_single.append(rr.mean())
    print("single-orbit <r> per seed:", [round(x, 4) for x in acc_single])


if __name__ == "__main__":
    main()
