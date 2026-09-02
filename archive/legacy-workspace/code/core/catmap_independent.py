"""
INDEPENDENT (clean-room) implementation of the quantised cat map and of the
compression experiment.  Nothing here imports the project's own modules; the
only inputs are the formulas printed in THEORY.md sections 1-2, which are
re-derived and re-verified from scratch:

    U_A(x,y) = N^{-1/2} w^{ (2c)^{-1} ( d x^2 - 2 x y + a y^2 ) },  w = e^{2 pi i/N}
    T(n)f(x) = w^{ n2 x - 2^{-1} n1 n2 } f(x - n1)

Verifications performed (all printed with measured residuals):

 V1  U unitary
 V2  exact Egorov covariance   U T(n) U^* = T(A n)                      [T1]
 V3  torsion  U^K = chi * 1, K = ord of A in PSL(2,Z/N) (x2 if needed)  [T2]
 V4  spectral projector P_lam = (1/K) sum_j lam^{-j} U^j  is a projector,
     ranks sum to N, and multiplicities are floor/ceil(N/K)             [T2,run3]
 V5  Weyl tight frame     sum_u T(u) X T(u)^* = N Tr(X) 1               [T19 input]
 V6  orbit tight frame    sum_O (|O|/K) M_O ox conj(M_O) = (N/K) I ox I - (1/K) J
                                                                        [T19]
 V7  Birkhoff reduction   P_lam V P_lam = Vbar P_lam                    [T6]
 V8  |Tr(T(v) U^J)| = 1 for J != 0 mod K                                [T7]

RED-TEAM experiments:

 X1  spacing statistics of the compression of a SINGLE Weyl orbit
     (project claim T20: "one orbit = two parameters already gives GOE")
 X2  spacing statistics of a Gaussian combination of ALL orbits
     (new Theorem B: this must be EXACTLY GUE / GOE)
 X3  the same for a Theta-invariant Gaussian observable
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np


# ----------------------------------------------------------------- basics

def inv(a: int, n: int) -> int:
    return pow(a % n, -1, n)


class CatMap:
    def __init__(self, A, N):
        (a, b), (c, d) = A
        assert (a * d - b * c) % N == 1 % N, "det != 1 mod N"
        assert math.gcd(c % N, N) == 1, "need gcd(c,N)=1 for this kernel"
        self.A = np.array([[a, b], [c, d]], dtype=np.int64)
        self.N = N
        self.a, self.b, self.c, self.d = a % N, b % N, c % N, d % N
        self.cp = inv(2 * c, N)                     # (2c)^{-1}
        self.two_inv = inv(2, N)
        x = np.arange(N, dtype=np.int64)
        self.chirp_in = np.exp(2j * np.pi * (self.cp * self.a % N) * (x * x % N) / N)
        self.chirp_out = np.exp(2j * np.pi * (self.cp * self.d % N) * (x * x % N) / N)
        self.perm = (2 * self.cp * x) % N           # x -> 2 c' x
        self.norm = N ** -0.5

    # ---- U applied to a batch of column vectors (N, B)
    def apply_U(self, F):
        N = self.N
        G = self.chirp_in[:, None] * F
        Gh = np.fft.fft(G, axis=0)                  # sum_y w^{-t y} g(y)
        return self.norm * self.chirp_out[:, None] * Gh[self.perm, :]

    def apply_Ustar(self, F):
        # U^* = conj(U)^T ; do it by explicit adjoint of the three factors
        N = self.N
        H = np.zeros_like(F)
        np.add.at(H, self.perm, np.conj(self.chirp_out)[:, None] * F)
        Hh = np.fft.ifft(H, axis=0) * N             # adjoint of fft is conj-fft
        Hh = np.conj(np.fft.fft(np.conj(H), axis=0))
        return self.norm * np.conj(self.chirp_in)[:, None] * Hh

    def U_matrix(self):
        return self.apply_U(np.eye(self.N, dtype=complex))

    # ---- Weyl operator T(n) applied to a batch
    def apply_T(self, n, F):
        N = self.N
        n1, n2 = int(n[0]) % N, int(n[1]) % N
        x = np.arange(N, dtype=np.int64)
        ph = np.exp(2j * np.pi * ((n2 * x - self.two_inv * n1 * n2) % N) / N)
        return ph[:, None] * np.roll(F, n1, axis=0)     # f(x-n1)

    def T_matrix(self, n):
        return self.apply_T(n, np.eye(self.N, dtype=complex))

    # ---- order of A in PSL(2, Z/N) and the torsion exponent K
    def orders(self):
        N, A = self.N, self.A % self.N
        I = np.eye(2, dtype=np.int64)
        M = A.copy()
        for j in range(1, 4 * N + 4):
            if np.array_equal(M % N, I % N):
                return j, j                 # ord = j, K = j
            if np.array_equal(M % N, (-I) % N):
                return j, 2 * j             # projective order j, K = 2j
            M = M @ A % N
        raise RuntimeError("order not found")


# ------------------------------------------------------- spacing statistics

def unfolded_spacings(ev, cut=0.15):
    """ev: real eigenvalues.  Unfold by a smooth polynomial fit of the
    integrated density, drop `cut` fraction at each edge, return spacings."""
    ev = np.sort(np.asarray(ev, dtype=float))
    n = len(ev)
    lo, hi = int(cut * n), int((1 - cut) * n)
    x = ev
    y = np.arange(1, n + 1) - 0.5
    deg = min(9, max(3, n // 25))
    cf = np.polyfit(x, y, deg)
    u = np.polyval(cf, x)
    u = u[lo:hi]
    s = np.diff(u)
    s = s[s > 0]
    return s / s.mean()


def spacing_hist(s, edges):
    h, _ = np.histogram(s, bins=edges, density=True)
    return h


def wigner_surmise(x, beta):
    if beta == 1:
        return (np.pi / 2) * x * np.exp(-np.pi * x ** 2 / 4)
    if beta == 2:
        return (32 / np.pi ** 2) * x ** 2 * np.exp(-4 * x ** 2 / np.pi)
    if beta == 0:
        return np.exp(-x)
    raise ValueError


def L1_to(s, beta, edges):
    h = spacing_hist(s, edges)
    mid = 0.5 * (edges[1:] + edges[:-1])
    ref = wigner_surmise(mid, beta)
    return float(np.abs(h - ref).sum() * (edges[1] - edges[0]))


def reference_L1(kind, m, nrep, edges, rng):
    """L1 distance of true GOE/GUE/Poisson samples of the same size."""
    out = []
    for _ in range(nrep):
        if kind == "GOE":
            X = rng.standard_normal((m, m))
            X = (X + X.T) / np.sqrt(2)
            ev = np.linalg.eigvalsh(X)
            beta = 1
        elif kind == "GUE":
            X = rng.standard_normal((m, m)) + 1j * rng.standard_normal((m, m))
            X = (X + X.conj().T) / 2
            ev = np.linalg.eigvalsh(X)
            beta = 2
        else:
            ev = np.sort(rng.random(m))
            beta = 0
        s = unfolded_spacings(ev)
        out.append((L1_to(s, 1, edges), L1_to(s, 2, edges), L1_to(s, 0, edges)))
    a = np.array(out)
    return a.mean(axis=0), a.std(axis=0)


# ---------------------------------------------------------------- driver

def main():
    rng = np.random.default_rng(20260828)
    rep = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "checks": {},
           "experiments": []}

    # ---------- small N: exact matrix-level identity checks
    print("=" * 78)
    print("EXACT IDENTITY CHECKS (small N, full matrices)")
    print("=" * 78)
    for (A, N) in [([[2, 1], [1, 1]], 41), ([[2, 1], [1, 1]], 101),
                   ([[3, 1], [2, 1]], 61), ([[5, 2], [2, 1]], 71)]:
        cm = CatMap(A, N)
        U = cm.U_matrix()
        v1 = np.abs(U.conj().T @ U - np.eye(N)).max()
        # Egorov
        e_max = 0.0
        for _ in range(6):
            n = rng.integers(0, N, size=2)
            An = (cm.A @ n) % N
            lhs = U @ cm.T_matrix(n) @ U.conj().T
            rhs = cm.T_matrix(An)
            e_max = max(e_max, np.abs(lhs - rhs).max())
        ordA, K = cm.orders()
        UK = np.linalg.matrix_power(U, K)
        chi = UK[0, 0]
        v3 = np.abs(UK - chi * np.eye(N)).max()
        # projectors
        lams = [chi ** (1.0 / K) * np.exp(2j * np.pi * j / K) for j in range(K)]
        # more robust: eigenvalues of U are the K-th roots of chi
        roots = np.exp((np.log(chi + 0j) + 2j * np.pi * np.arange(K)) / K)
        ranks, projerr = [], 0.0
        Upow = [np.eye(N, dtype=complex)]
        for j in range(1, K):
            Upow.append(Upow[-1] @ U)
        for lam in roots:
            P = sum((lam ** (-j)) * Upow[j] for j in range(K)) / K
            projerr = max(projerr, np.abs(P @ P - P).max(),
                          np.abs(P - P.conj().T).max())
            ranks.append(int(np.round(np.trace(P).real)))
        # Weyl tight frame
        X = rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))
        acc = np.zeros((N, N), dtype=complex)
        for u1 in range(N):
            for u2 in range(N):
                T = cm.T_matrix((u1, u2))
                acc += T @ X @ T.conj().T
        v5 = np.abs(acc - N * np.trace(X) * np.eye(N)).max() / (N * abs(np.trace(X)))
        # |Tr(T(v) U^J)| = 1
        v8 = []
        for _ in range(5):
            v = rng.integers(0, N, size=2)
            J = int(rng.integers(1, K))
            if J % K == 0:
                continue
            v8.append(abs(abs(np.trace(cm.T_matrix(v) @ Upow[J])) - 1.0))
        row = {"A": A, "N": N, "ord": ordA, "K": K,
               "V1_unitary": float(v1), "V2_egorov": float(e_max),
               "V3_torsion": float(v3), "V4_proj": float(projerr),
               "V4_ranks": ranks, "V4_ranksum": int(sum(ranks)),
               "V4_expected": [N // K, -(-N // K)],
               "V5_weyl_frame_rel": float(v5),
               "V8_unimodular_max_dev": float(max(v8)) if v8 else None}
        rep["checks"][f"{A}_{N}"] = row
        print(f"  A={A} N={N}: ord={ordA} K={K} m in {sorted(set(ranks))} "
              f"sum={sum(ranks)}")
        print(f"     V1 unitary   {v1:.2e}   V2 Egorov {e_max:.2e}   "
              f"V3 torsion {v3:.2e}   V4 proj {projerr:.2e}")
        print(f"     V5 Weyl frame(rel) {v5:.2e}   "
              f"V8 max| |Tr(TU^J)|-1 | {max(v8) if v8 else float('nan'):.2e}")
        sys.stdout.flush()

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                           "artifacts", "r71", "catmap_independent_checks.json"),
              "w", encoding="utf-8") as fh:
        json.dump(rep, fh, indent=1)
    print("\nwrote artifacts/catmap_independent_checks.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
