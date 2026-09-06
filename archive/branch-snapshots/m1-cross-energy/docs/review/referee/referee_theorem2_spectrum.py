"""Referee spectrum-level check of Theorem II (Claim 2) at N=199.
The canonical r82j verification compared mu_4 only.  Here the FULL sorted
spectrum of the closed-form M_{q'} (twisted Jacobi sums, q' = q/c) is
compared with the full sorted spectrum of the pipeline V_q (exact-projector
eigenbasis + parity block), for several level sets.  Agreement to ~1e-13
would confirm Theorem II at spectrum level, not just at the level of one
normalised moment.
"""
import os
import sys

import numpy as np

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC)
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402
from r82g_q_curve import rep_for_each_q  # noqa: E402
from r82k_bgs_large_m import build_M, design_params  # noqa: E402

A = [[2, 1], [1, 1]]
N, K = 199, 11

cm = CatMap(A, N)
ordA, K = cm.orders()
rng = np.random.default_rng(820005)
B, lam, m, res, chi = eigen_basis(cm, K, 0, 64, rng)
RB = B.conj().T @ apply_parity(B)
w, Vv = np.linalg.eigh(RB)
Bp = B @ Vv[:, w > 0]
reps = rep_for_each_q(N)
a = design_params(N, K)
c = 123
cinv = pow(c, N - 2, N)

for q in (1, 2, 3, 5, 7, 11, 13, 50, 100, 198):
    H = Bp.conj().T @ cm.apply_T(reps[q], Bp)
    H = H + H.conj().T
    ev_pipe = np.sort(np.linalg.eigvalsh(H))
    M, mc = build_M(N, K, a, (cinv * q) % N)
    ev_cf = np.sort(np.linalg.eigvalsh(M))
    dev = float(np.abs(ev_pipe - ev_cf).max())
    scale = float(np.abs(ev_pipe).max())
    print(f"q={q:4d}: max|ev_pipeline - ev_closedform| = {dev:.3e} "
          f"(spectral radius {scale:.3f}, m+ = {mc})", flush=True)
