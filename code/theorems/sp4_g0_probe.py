"""M4c — Sp4 diagonal Hecke kernel and the G0 coupled-energy test (RUN 105).

The Sp4 diagonal element D = diag(u1, u2, iu1, iu2) acts in the
Schroedinger model as the DILATION (x1,x2) -> (u1 x1, u2 x2) with NO
phase, and satisfies the exact covariance

    U_D T(n) = T(D n) U_D,  D n = (u1 n1, u2 n2, iu1 n3, iu2 n4),

where T(n) is the 4D Heisenberg translation with the cocycle
e_N((c x1 + d x2) - (a c + b d)/2) in the Schroedinger model on (Z/N)^2.
(Verified: 0.00e+00 error on all four basis shifts at N = 53.)

The G0 TEST: the characters chi of the torus (Z/N)^2 are the joint
eigenvectors of the translations; the Hecke kernel of U_D in the
character basis is the rank-2 analogue of the twisted Jacobi sums.
The coupled-energy structure: is the k=2 moment sum over the annihilator
coset again EXACTLY flat + Weil?  Specifically: for the character
coset S (characters of the diagonal torus), the sum
    A_S(n) = sum_{chi in S} |<chi | U_D T(n) | chi>|^2
is computed for all n; its dependence on n (the q-curve analogue) is
the G0 fluctuation.  For the cat map this sum was constant; here the
two-torus introduces the coupled quadratic form.

Implementation: build U_D (N^2 x N^2), the translations T(n), the
character basis chi_{k,l}, the Hecke kernel J4(k,l;n) = <chi_kl|T(n)|...>
and measure A_S(n) for a scan of n.
"""
import numpy as np
import math
import os
import json
import time

N = 53
u1, u2 = 2, 3
iu1, iu2 = pow(u1, -1, N), pow(u2, -1, N)
w = np.exp(2j * np.pi / N)
b2 = pow(2, -1, N)
G = N * N


def T4(a, b, c, d):
    T = np.zeros((G, G), dtype=complex)
    for x1 in range(N):
        for x2 in range(N):
            nx1 = (x1 - a) % N
            nx2 = (x2 - b) % N
            ph = np.exp(2j * np.pi * ((c * x1 + d * x2 - b2 * (a * c + b * d)) % N) / N)
            T[nx1 * N + nx2, x1 * N + x2] = ph
    return T


def UD():
    U = np.zeros((G, G), dtype=complex)
    for x1 in range(N):
        for x2 in range(N):
            nx1 = (u1 * x1) % N
            nx2 = (u2 * x2) % N
            U[nx1 * N + nx2, x1 * N + x2] = 1.0
    return U


def char_basis():
    """chi_{k,l}(x1,x2) = e_N(k x1 + l x2)/N."""
    C = np.zeros((G, G), dtype=complex)
    idx = 0
    for k in range(N):
        for l in range(N):
            for x1 in range(N):
                for x2 in range(N):
                    C[idx, x1 * N + x2] = np.exp(
                        2j * np.pi * (k * x1 + l * x2) / N) / N
            idx += 1
    return C


def main():
    t0 = time.time()
    # covariance certificate first
    Ud = UD()
    max_err = 0.0
    for n in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]:
        Tn = T4(*n)
        m = ((u1 * n[0]) % N, (u2 * n[1]) % N,
             (iu1 * n[2]) % N, (iu2 * n[3]) % N)
        err = float(np.abs(Ud @ Tn - T4(*m) @ Ud).max())
        max_err = max(max_err, err)
    print(f"Sp4 diagonal covariance: max err = {max_err:.2e}")

    # The G0 probe: the Hecke kernel in the character basis.
    # <chi_kl | T(n) U_D | chi_kl'> — but for the coupled-energy test
    # we need the analog of the Jacobi kernel: the matrix element
    # between characters under the diagonal element D.  The character
    # chi_kl is an eigenvector of U_D?  Check: U_D chi_kl (x) =
    # chi_kl(u1 x1, u2 x2) = e_N(k u1 x1 + l u2 x2) = chi_{(k u1, l u2)}.
    # So U_D does NOT preserve the character eigenspaces unless u_i = 1.
    # The genuine Hecke basis: joint eigenvectors of U_D and the
    # translations commuting with it — the characters of the D-FIXED
    # subtorus.  The fixed characters: chi_kl with k u1 = k, l u2 = l
    # mod N, i.e. k(u1-1) = 0, l(u2-1) = 0: k, l multiples of
    # N/gcd(u_i-1, N).  With u1 = 2, u2 = 3 at N = 53 (prime):
    # gcd(1,53)=1 and gcd(2,53)=1: only k=l=0.  So U_D has NO
    # nontrivial character eigenvectors: it mixes all characters.
    # This is the rank-2 phenomenon: the diagonal element is NOT
    # diagonal in the product character basis — the coupling is real.
    # The Hecke matrix in the character basis: H_kl,k'l' = <chi_kl |
    # U_D | chi_k'l'> — its structure is the G0 object.  Compute it
    # (G x G = 53^4 = 7.9M entries — manageable).
    C = char_basis()
    H = C.conj().T @ Ud @ C
    absH = np.abs(H)
    print(f"Hecke matrix in char basis: max|H|={absH.max():.4f} "
          f"support={int((absH>1e-9).sum())}/{G*G}")
    # The G0 coupled-energy probe: the "annihilator coset" analogue —
    # sum over characters of |<chi|U_D T(n)|chi>|^2 as a function of n.
    # (the rank-2 "level-set" analogue).  Scan n over the first few.
    A = {}
    for n in [(0,0,0,0),(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1),(1,1,0,0)]:
        Tn = T4(*n)
        M = Ud @ Tn
        # diagonal matrix elements in the character basis
        diag = np.einsum('ij,ji->i', C.conj().T @ M, C)
        A[str(n)] = float((np.abs(diag) ** 2).sum())  # R108 bracket fix
    print("A_S(n) = sum_chi |<chi|U_D T(n)|chi>|^2:")
    for k, v in A.items():
        print(f"  n={k}: {v:.2f}")
    # For the cat map this A was CONSTANT in n (q-independence).  Here:
    print(f"A spread: max/min = {max(A.values())/min(A.values()):.4f}")

    out = {
        "run": "105",
        "design": {"N": N, "u1": u1, "u2": u2},
        "covariance_err": max_err,
        "hecke_max": float(absH.max()),
        "hecke_support": int((absH > 1e-9).sum()),
        "A_S_scan": A,
        "A_spread": float(max(A.values()) / min(A.values())),
        "wall_s": time.time() - t0,
    }
    out_dir = os.path.join(os.path.dirname(__file__), "..", "..",
                           "artifacts", "r105")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "sp4_g0_probe.json"), "w") as fh:
        json.dump(out, fh, indent=1)
    print("artifact written")


if __name__ == "__main__":
    main()
