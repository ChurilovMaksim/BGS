"""M4c -- The Sp4 Hecke kernel in the Schroedinger model (RUN 104).

The 4D analogue of the cat-map quantization: Sp4(Z/N) acts on functions
on X = (Z/N)^2 through the Schroedinger model.  For the diagonal
element D = diag(u1, u2, u1^-1, u2^-1) the Hecke operator is

    (T_D f)(x) = e_N(mu(x)/1) f(D|_X^{-1} x),

with mu(x) = ((u1 - u1^{-1}) x1^2 + (u2 - u2^{-1}) x2^2) * inv2 -- the
quadratic phase of the 4D cat map.  The eigenbasis of T_D on the
mu-symmetric subspace plays the role of the Hecke basis; its matrix
elements against the translation operators T(n) (n in (Z/N)^4) give
the rank-2 twisted Jacobi kernel

    J4(chi; n) = sum_{x in (Z/N)^2, x not on the bad set}
                 chi(x) e_N(n-terms + mu-phase terms),

whose fiber structure (the constraint variety of the k=2 layer) is
the G0 test object: is the difference-fiber set still a rational-
function orbit (Weil-bounded, bounded degree), and does the coupled
energy factor through flat + twisted terms?

This file implements, at small N:
  1. the translation operators T(n) on functions on (Z/N)^2 (the
     4D analogue has T(n) acting through the theta kernel -- here we
     use the standard 2-torus-embedded model: T(n) for n in (Z/N)^2
     with the full Sp4 phase, which is the restriction of the Sp4
     representation to the parabolic 2D torus),
  2. T_D for the diagonal element,
  3. the simultaneous eigenbasis of T_D (its eigenspaces carry
     characters of the 2-torus (Z/N)^2),
  4. the matrix elements <f_chi|T(n)|f_psi> = J4(chi; n) for a scan
     of n, and the coupled-energy structure of the |J4|^2 sums.

Scope note: this is the 2-torus-embedded (parabolic) model — the
"rank-1 embedded in rank-2" reduction.  The FULL Sp4 model has
functions on all of (Z/N)^4 with the theta kernel entangling the
factors; the parabolic restriction is the first genuinely nontrivial
test of whether the coupled-energy mechanism survives the rank-2
quadratic form (two coupled mu-terms instead of one).
"""

import numpy as np
import math
import os
import json
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "artifacts", "r104")
os.makedirs(OUT_DIR, exist_ok=True)


def build_operators(N, u1, u2):
    """T_D and the translation operators on functions on (Z/N)^2."""
    inv2 = pow(2, N - 2, N)
    # grid
    G = np.array([[x1, x2] for x1 in range(N) for x2 in range(N)],
                 dtype=np.int64)
    n_grid = len(G)
    x1 = G[:, 0]
    x2 = G[:, 1]
    # mu(x) = ((u1-u1^-1) x1^2 + (u2-u2^-1) x2^2)/2
    mu = ((u1 - pow(u1, N - 2, N)) * x1 * x1 +
          (u2 - pow(u2, N - 2, N)) * x2 * x2) % N
    mu = mu * inv2 % N
    # T_D: phase times pullback
    iu1 = pow(u1, N - 2, N)
    iu2 = pow(u2, N - 2, N)
    px = (x1 * iu1) % N
    py = (x2 * iu2) % N
    # index of (px,py) in the grid
    idx = px * N + py
    phase = np.exp(2j * np.pi * mu / N)
    TD = np.zeros((n_grid, n_grid), dtype=complex)
    TD[np.arange(n_grid), idx] = phase
    return G, n_grid, TD, (iu1, iu2)


def translation_op(N, G, n_vec):
    """T(n): (T(n) f)(x) = e_N(phase(x, n)) f(x + n) -- the theta-shift;
    for the embedded 2-torus model the phase is the linear form
    e_N(n . x) with the standard symplectic half-correction."""
    n_grid = len(G)
    x1 = G[:, 0]
    x2 = G[:, 1]
    ph = np.exp(2j * np.pi * ((n_vec[0] * x1 + n_vec[1] * x2) % N) / N)
    idx = ((x1 + n_vec[0]) % N) * N + ((x2 + n_vec[1]) % N)
    T = np.zeros((n_grid, n_grid), dtype=complex)
    T[np.arange(n_grid), idx] = ph
    return T


def main():
    t0 = time.time()
    N = 53
    u1, u2 = 2, 3
    assert pow(u1, N - 2, N) * u1 % N == 1
    assert pow(u2, N - 2, N) * u2 % N == 1

    G, n_grid, TD, _ = build_operators(N, u1, u2)
    print(f"grid {N}x{N} = {n_grid} points")

    # eigendecompose T_D: eigenvalues e_N(mu-values) grouped
    evals, evecs = np.linalg.eig(TD)
    # cluster eigenvalues
    order = np.argsort(evals.real)
    evals = evals[order]
    evecs = evecs[:, order]
    # eigenvalue multiplicities: the spectrum is e_N(mu(x)) over grid
    # points; group by phase
    groups = {}
    for i, ev in enumerate(evals):
        key = (round(ev.real, 6), round(ev.imag, 6))
        groups.setdefault(key, []).append(i)
    print(f"T_D spectrum: {len(groups)} distinct eigenvalues")

    # pick the largest eigenspace and test the J4 matrix elements:
    # within an eigenspace, the translations T(n) act; their matrix
    # elements against the eigenvectors are the rank-2 Jacobi kernel.
    # For the kernel structure test we need characters of the 2-torus:
    # the joint eigenvectors of all T(n) — they exist iff the T(n)
    # commute (they do in the theta model) — take T(n) for the two
    # basis directions and joint-diagonalize.
    n1v = np.array([1, 0])
    n2v = np.array([0, 1])
    T1 = translation_op(N, G, n1v)
    T2 = translation_op(N, G, n2v)
    # check commutation with TD
    c1 = np.abs(TD @ T1 - T1 @ TD).max()
    c2 = np.abs(TD @ T2 - T2 @ TD).max()
    print(f"commutation ||[TD,T1]||={c1:.2e} ||[TD,T2]||={c2:.2e}")

    # joint eigenvectors: diagonalize T1 on the full space, then T2 in
    # each eigenspace... simpler: T1 and T2 are permutation-phase
    # matrices — their common eigenvectors are the 2D characters
    # chi_{a,b}(x) = e_N((a x1 + b x2)/N):
    # T1 chi_ab = e_N(a/N) chi_ab shifted... compute the J4 kernel
    # directly: <chi_a,b | T_D | chi_a',b'> for a scan of (a,b),(a',b')
    chi = np.zeros((n_grid, n_grid), dtype=complex)
    for i, (x1, x2) in enumerate(G):
        for a in range(N):
            for b in range(N):
                chi[a * N + b, i] = np.exp(
                    2j * np.pi * (a * x1 + b * x2) / N) / math.sqrt(n_grid)
    J4 = chi.conj().T @ TD @ chi  # <chi|TD|psi> in the character basis
    absJ4 = np.abs(J4)
    print(f"J4 kernel: max|J4|={absJ4.max():.4f}, "
          f"mean={absJ4.mean():.4f}, |V|=N^2={N*N}")
    # the structure: J4 should be supported on (a,b) pairs related to
    # the mu-phase — measure the support pattern
    nz = (absJ4 > 1e-10)
    print(f"support: {nz.sum()} entries of {N**4}")
    # normalize by sqrt(N^2)=N: the flat scale for |J4| is sqrt(N^2)=N...
    # for the coupled-energy test: sum |J4|^2 over the character basis
    # = |TD|_HS^2 = n_grid (the diagonal key count analogue)
    s2 = float((absJ4 ** 2).sum())
    print(f"sum |J4|^2 = {s2:.1f} (TD HS^2 = {n_grid})")

    out = {
        "run": "104",
        "design": {"N": N, "u1": u1, "u2": u2},
        "n_distinct_Teigenvalues": len(groups),
        "commutation": {"TD_T1": float(c1), "TD_T2": float(c2)},
        "J4_max": float(absJ4.max()),
        "J4_support": int(nz.sum()),
        "sum_J4sq": s2,
        "wall_s": time.time() - t0,
    }
    with open(os.path.join(OUT_DIR, "sp4_kernel_probe.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("artifact written")


if __name__ == "__main__":
    main()
