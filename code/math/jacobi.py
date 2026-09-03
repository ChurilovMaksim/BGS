"""Character-coset and twisted-Jacobi matrix primitives."""
from __future__ import annotations

import math
import numpy as np


def dlog_table(N: int, g: int) -> np.ndarray:
    """Discrete logarithm table for a primitive root g modulo prime N."""
    table = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        table[x] = s
        x = x * g % N
    return table


def index_coset(N: int, K: int, a: int, dlog: np.ndarray) -> np.ndarray:
    """Return character indices k satisfying chi_k(a)=1."""
    del K  # K documents the design; the annihilator is determined by a.
    ell = int(dlog[a])
    step = (N - 1) // math.gcd(ell, N - 1)
    return np.array([k for k in range(N - 1) if k % step == 0], dtype=np.int64)


def jacobi_matrix(
    N: int,
    K: int,
    a: int,
    dlog: np.ndarray,
    ks: np.ndarray,
    q: int,
) -> np.ndarray:
    """Return J[i,j;q] for the supplied character-index set ``ks``."""
    del K, a  # kept in the signature to make design provenance explicit.
    xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))
    phase = np.exp(2j * np.pi * (q * xs % N) / N)
    return (W * phase) @ V.T
