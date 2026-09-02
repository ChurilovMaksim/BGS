"""
bgs_core.py -- canonical, independent core for the BGS/cat-map programme (run 41).

Written from scratch as a SECOND, mechanistically independent implementation of
the objects previously handled by `catmap_core.py` / `master_formula*.py`.
Nothing here imports the older modules; agreement between the two is used as an
independent verification key.

Conventions (N odd prime, gcd(c,N)=1, w = exp(2*pi*i/N)):

    Weil / Hannay-Berry propagator
        U_A(x,y) = N^{-1/2} w^{ (2c)^{-1} ( d x^2 - 2 x y + a y^2 ) }

    Weyl (finite Heisenberg) operators
        T(n1,n2) = w^{ 2^{-1} n1 n2 } X^{n1} Z^{n2},
        (X psi)(x) = psi(x-1),   (Z psi)(x) = w^{x} psi(x).

    Matrix form used throughout (no N x N storage needed):
        T(n1,n2)_{x,y} = w^{ 2^{-1} n1 n2 + n2 y } [ y = x - n1 ],
    hence for a block B (N x r):
        ( T(n1,n2) B )[x,:] = w^{ 2^{-1} n1 n2 + n2 (x-n1) } B[x-n1,:].

    Egorov covariance (verified, not assumed):
        U_A T(n) U_A^dagger = phase * T(E_A n),  E_A = A^T  (see `egorov_matrix`).

All heavy linear algebra is float64/complex128; every identity that the
programme relies on is checked here by an explicit residual that the caller can
assert on.
"""
from __future__ import annotations

import math
import numpy as np

__all__ = [
    "omega", "U_cat", "apply_T", "T_matrix", "egorov_matrix", "egorov_residual",
    "mat_order", "torsion_certificate", "multiplet_basis", "weyl_sum_operator",
    "orbit", "reversing_involution", "theta_operator", "theta_conjugate",
]


# ----------------------------------------------------------------- primitives
def omega(N: int) -> complex:
    return np.exp(2j * np.pi / N)


def _phase_pow(N: int, exps: np.ndarray) -> np.ndarray:
    """w^exps with exps an integer array, computed without accumulating error."""
    return np.exp((2j * np.pi / N) * (np.asarray(exps) % N))


def U_cat(A, N: int) -> np.ndarray:
    """Explicit N x N Weil propagator of A = (a,b,c,d), gcd(c,N) = 1."""
    a, b, c, d = [int(v) for v in A]
    if math.gcd(c % N, N) != 1:
        raise ValueError("gcd(c,N) must be 1 for this kernel")
    inv2c = pow((2 * c) % N, -1, N)
    x = np.arange(N)
    X, Y = np.meshgrid(x, x, indexing="ij")
    Q = (inv2c * (d * X * X - 2 * X * Y + a * Y * Y)) % N
    return _phase_pow(N, Q) / math.sqrt(N)


def apply_T(n1: int, n2: int, B: np.ndarray, N: int) -> np.ndarray:
    """T(n1,n2) @ B for B of shape (N, r) or (N,) -- O(N r), no N x N storage."""
    n1 %= N
    n2 %= N
    inv2 = pow(2, -1, N)
    x = np.arange(N)
    ph = _phase_pow(N, inv2 * n1 * n2 + n2 * ((x - n1) % N))
    rolled = np.roll(B, n1, axis=0)          # rolled[x] = B[x-n1]
    if B.ndim == 1:
        return ph * rolled
    return ph[:, None] * rolled


def T_matrix(n1: int, n2: int, N: int) -> np.ndarray:
    """Explicit N x N matrix of T(n1,n2) (for small N / cross-checks only)."""
    return apply_T(n1, n2, np.eye(N, dtype=complex), N)


def apply_U(A, N: int, block: np.ndarray) -> np.ndarray:
    """U_A @ block in O(N log N) per column, without ever forming U_A.

        U_A(x,y) = N^{-1/2} w^{(2c)^{-1} d x^2} w^{-c^{-1} x y} w^{(2c)^{-1} a y^2}

    so with phi(y) = w^{(2c)^{-1} a y^2} psi(y),
        (U psi)(x) = N^{-1/2} w^{(2c)^{-1} d x^2} * FFT[phi]( (c^{-1} x) mod N ),
    where FFT[phi](k) = sum_y phi(y) e^{-2 pi i k y / N} (numpy convention).
    """
    a, b, c, d = [int(v) for v in A]
    inv2c = pow((2 * c) % N, -1, N)
    invc = pow(c % N, -1, N)
    y = np.arange(N)
    pre = _phase_pow(N, inv2c * a * y * y)
    post = _phase_pow(N, inv2c * d * y * y)
    idx = (invc * y) % N
    if block.ndim == 1:
        F = np.fft.fft(pre * block)
        return post * F[idx] / math.sqrt(N)
    F = np.fft.fft(pre[:, None] * block, axis=0)
    return post[:, None] * F[idx, :] / math.sqrt(N)


def multiplet_basis_fft(A, N: int, K: int, chi: complex, s: int,
                        oversample: int = 24, seed: int = 0,
                        gap_tol: float = 1e-6):
    """Same as `multiplet_basis` but using `apply_U`; never forms U_A."""
    lam = (chi ** (1.0 / K)) * np.exp(2j * np.pi * s / K)
    rng = np.random.default_rng(seed)
    r = min(N, int(round(N / K)) + 2 + oversample)
    G = rng.standard_normal((N, r)) + 1j * rng.standard_normal((N, r))
    Y = np.zeros_like(G)
    W = G
    for J in range(K):
        Y += (lam ** (-J)) * W
        W = apply_U(A, N, W)
    Y /= K
    Q, S, _ = np.linalg.svd(Y, full_matrices=False)
    m = int(np.sum(S > gap_tol * S[0]))
    B = Q[:, :m]
    Z = np.zeros_like(B)
    W = B
    for J in range(K):
        Z += (lam ** (-J)) * W
        W = apply_U(A, N, W)
    Z /= K
    cert = float(np.linalg.norm(Z - B, 2))
    return lam, B, m, cert


def torsion_certificate_fft(A, N: int, K: int, seed: int = 0, r: int = 4):
    """chi and residual from U^K applied to a random block (no N x N storage)."""
    rng = np.random.default_rng(seed)
    G = rng.standard_normal((N, r)) + 1j * rng.standard_normal((N, r))
    W = G
    for _ in range(K):
        W = apply_U(A, N, W)
    chi = np.vdot(G.ravel(), W.ravel()) / np.vdot(G.ravel(), G.ravel())
    res = float(np.max(np.abs(W - chi * G)))
    return complex(chi), res



# ------------------------------------------------------------------- Egorov
def egorov_matrix(A) -> np.ndarray:
    """The matrix E_A acting on frequency labels in U T(n) U^* = phase*T(E_A n).

    Determined empirically in run 3 to be A^T for the kernel above; the caller
    should always confirm with `egorov_residual`.
    """
    a, b, c, d = [int(v) for v in A]
    return np.array([[a, c], [b, d]], dtype=np.int64)      # = A^T


def egorov_residual(A, N: int, E=None, nmax: int = 3):
    """max over |n| <= nmax of the phase-optimised residual

        min_{|z|=1} || U T(n) U^* - z T(E n) ||_max .

    Returns (residual, E) with E the label matrix actually used.
    """
    U = U_cat(A, N)
    Ud = U.conj().T
    E = egorov_matrix(A) if E is None else np.asarray(E, dtype=np.int64)
    worst = 0.0
    for n1 in range(-nmax, nmax + 1):
        for n2 in range(-nmax, nmax + 1):
            if n1 % N == 0 and n2 % N == 0:
                continue
            lhs = U @ apply_T(n1, n2, Ud, N)
            m1, m2 = (E @ np.array([n1, n2])) % N
            rhs = T_matrix(int(m1), int(m2), N)
            # optimal global phase
            num = np.vdot(rhs.ravel(), lhs.ravel())
            z = num / abs(num) if abs(num) > 0 else 1.0
            worst = max(worst, float(np.max(np.abs(lhs - z * rhs))))
    return worst, E


# ------------------------------------------------------- order / torsion / P_l
def mat_order(A, N: int):
    """Least k with A^k = +-I mod N; returns (k, sign, K) with K = k or 2k."""
    a, b, c, d = [int(v) % N for v in A]
    P = (1, 0, 0, 1)
    for k in range(1, 4 * N + 4):
        P = ((P[0] * a + P[1] * c) % N, (P[0] * b + P[1] * d) % N,
             (P[2] * a + P[3] * c) % N, (P[2] * b + P[3] * d) % N)
        if P == (1, 0, 0, 1):
            return k, +1, k
        if P == (N - 1, 0, 0, N - 1):
            return k, -1, 2 * k
    raise RuntimeError("order not found")


def torsion_certificate(U: np.ndarray, K: int):
    """Check U^K = chi * I; return (chi, residual)."""
    N = U.shape[0]
    P = np.linalg.matrix_power(U, K)
    chi = P[0, 0] if abs(P[0, 0]) > 1e-9 else np.trace(P) / N
    res = float(np.max(np.abs(P - chi * np.eye(N))))
    return complex(chi), res


def multiplet_basis(U: np.ndarray, K: int, chi: complex, s: int,
                    oversample: int = 24, seed: int = 0, gap_tol: float = 1e-6):
    """Orthonormal basis B (N x m) of the U-eigenspace with eigenvalue

        lam_s = chi^{1/K} * exp(2*pi*i*s/K),   s = 0..K-1,

    obtained by a randomised range finder applied to P_lam = K^{-1} sum_J
    lam^{-J} U^J.  Returns (lam, B, m, cert) with cert = ||P_lam B - B||_2,
    which the caller must check is ~1e-13.
    """
    N = U.shape[0]
    lam = (chi ** (1.0 / K)) * np.exp(2j * np.pi * s / K)
    rng = np.random.default_rng(seed)
    m_guess = int(round(N / K)) + 2
    r = min(N, m_guess + oversample)
    G = rng.standard_normal((N, r)) + 1j * rng.standard_normal((N, r))
    # Y = P_lam G  by Horner in U
    Y = np.zeros_like(G)
    W = G.copy()
    for J in range(K):
        Y += (lam ** (-J)) * W
        W = U @ W
    Y /= K
    Q, S, _ = np.linalg.svd(Y, full_matrices=False)
    m = int(np.sum(S > gap_tol * S[0]))
    B = Q[:, :m]
    # certificate: B must be P_lam-invariant
    Z = np.zeros_like(B)
    W = B.copy()
    for J in range(K):
        Z += (lam ** (-J)) * W
        W = U @ W
    Z /= K
    cert = float(np.linalg.norm(Z - B, 2))
    return lam, B, m, cert


# ------------------------------------------------------------ observables
def orbit(n, E, N: int):
    """A-orbit of the frequency label n under the Egorov matrix E, mod N."""
    n = np.asarray(n, dtype=np.int64) % N
    out, cur = [], n.copy()
    for _ in range(4 * N):
        out.append((int(cur[0]), int(cur[1])))
        cur = (E @ cur) % N
        if (int(cur[0]), int(cur[1])) == (int(n[0]), int(n[1])):
            break
    return out


def weyl_sum_operator(coeffs: dict, N: int, block: np.ndarray) -> np.ndarray:
    """(sum_n coeffs[n] T(n)) @ block, keys n = (n1,n2)."""
    out = np.zeros_like(block, dtype=complex)
    for (n1, n2), c in coeffs.items():
        if c == 0:
            continue
        out += c * apply_T(n1, n2, block, N)
    return out


def hermitian_observable(freqs, rng, N: int, real_symbol: bool = False):
    """Random Hermitian V = sum c_n T(n) with c_{-n} = conj(c_n).

    `freqs` is a list of labels n = (n1,n2); the returned dict contains both n
    and -n.  real_symbol=True forces real c_n (a *real, even* classical symbol).
    """
    coeffs = {}
    for (n1, n2) in freqs:
        key = (n1 % N, n2 % N)
        nkey = ((-n1) % N, (-n2) % N)
        if key in coeffs or nkey in coeffs:
            continue
        c = rng.standard_normal() if real_symbol else (
            rng.standard_normal() + 1j * rng.standard_normal()) / math.sqrt(2)
        coeffs[key] = c
        coeffs[nkey] = np.conj(c)
    return coeffs


def birkhoff_average(coeffs: dict, E, K: int, N: int) -> dict:
    """Coefficients of Vbar = K^{-1} sum_{j<K} U^j V U^{-j}, i.e. the K-step
    average of the frequency labels under E (valid when the Egorov phase is 1)."""
    out = {}
    E = np.asarray(E, dtype=np.int64)
    for (n1, n2), c in coeffs.items():
        v = np.array([n1, n2], dtype=np.int64)
        for _ in range(K):
            key = (int(v[0]) % N, int(v[1]) % N)
            out[key] = out.get(key, 0j) + c / K
            v = (E @ v) % N
    return out


def classical_symbol_values(coeffs: dict, N: int, grid: int = 0) -> np.ndarray:
    """Values of the classical symbol f(theta) = sum_n c_n e^{2 pi i n.theta}
    on the lattice theta = (x1,x2)/M, M = grid or N.  Returns a real array
    (the symbol is real for Hermitian V) flattened."""
    M = grid or N
    x = np.arange(M)
    X1, X2 = np.meshgrid(x, x, indexing="ij")
    val = np.zeros((M, M), dtype=complex)
    for (n1, n2), c in coeffs.items():
        e1 = ((n1 + N // 2) % N) - N // 2          # centred representatives
        e2 = ((n2 + N // 2) % N) - N // 2
        val += c * np.exp(2j * np.pi * (e1 * X1 + e2 * X2) / M)
    return np.real(val).ravel()


# --------------------------------------------------- time reversal (Theta)
def reversing_involution(A, box: int = 12):
    """All R = [[p,q],[r,-p]] in GL(2,Z), det R = -1, R A R = A^{-1}.

    Conditions (T3):  p(a-d) + q c + b r = 0,  p^2 + q r = 1.
    """
    a, b, c, d = [int(v) for v in A]
    sols = []
    for p in range(-box, box + 1):
        for q in range(-box, box + 1):
            for r in range(-box, box + 1):
                if p * (a - d) + q * c + b * r != 0:
                    continue
                if p * p + q * r != 1:
                    continue
                sols.append((p, q, r, -p))
    return sols


def theta_operator(A, N: int, R):
    """Return U_M with M = S R, S = diag(1,-1); Theta = U_M o (complex conj.)."""
    p, q, r, s = [int(v) for v in R]
    M = (p, q, -r, -s)                     # S @ R with S = diag(1,-1)
    return U_cat(M, N), M


def theta_conjugate(UM: np.ndarray, V: np.ndarray) -> np.ndarray:
    """Theta V Theta^{-1} = U_M conj(V) conj(U_M)  (valid when Theta^2 = 1)."""
    return UM @ np.conj(V) @ np.conj(UM)


def parity_operator(N: int) -> np.ndarray:
    """Pi = U_{-I}: (Pi psi)(x) = psi(-x).  Real symmetric involution with
    Pi T(n) Pi = T(-n) and Pi U_A Pi = U_A for every A (since -I is central).
    The kernel formula cannot be used for -I because c = 0."""
    P = np.zeros((N, N))
    for x in range(N):
        P[x, (-x) % N] = 1.0
    return P


def apply_parity(block: np.ndarray) -> np.ndarray:
    """Pi @ block, i.e. row index x -> -x mod N, without forming Pi."""
    N = block.shape[0]
    idx = (-np.arange(N)) % N
    return block[idx] if block.ndim == 1 else block[idx, :]


def theta_apply(M, N: int, coeffs: dict, block: np.ndarray) -> np.ndarray:
    """(Theta V Theta^{-1}) @ block = U_M conj(V) conj(U_M) @ block, with
    V = sum_n coeffs[n] T(n), computed with FFT propagators only."""
    W = apply_U(M, N, np.conj(block))                 # U_M conj(block)
    W = weyl_sum_operator(coeffs, N, W)               # V U_M conj(block)
    return apply_U(M, N, np.conj(W))






