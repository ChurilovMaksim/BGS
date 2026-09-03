"""Twisted-Jacobi kernel used by the current rank-1 verification line.

This module intentionally exposes only the small load-bearing API needed by
current checks. Historical command-line drivers and theorem-status prose are
preserved in ``archive/legacy-workspace`` rather than mixed into this library.
"""
from __future__ import annotations

import numpy as np

T_TRACE = 3


def sqrt_mod(a: int, p: int) -> list[int]:
    """Return all square roots of ``a`` modulo an odd prime ``p``."""
    a %= p
    if a == 0:
        return [0]
    if pow(a, (p - 1) // 2, p) != 1:
        return []
    if p % 4 == 3:
        r = pow(a, (p + 1) // 4, p)
        return sorted({r, (-r) % p})

    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    m, c, t, r = s, pow(z, q, p), pow(a, q, p), pow(a, (q + 1) // 2, p)
    while t != 1:
        i, t2 = 0, t
        while t2 != 1:
            t2 = t2 * t2 % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        m, c = i, b * b % p
        t = t * c % p
        r = r * b % p
    return sorted({r, (-r) % p})


def multiplicative_order(a: int, p: int) -> int | None:
    """Return the multiplicative order of ``a`` modulo prime ``p``."""
    x, k = a % p, 1
    while x != 1:
        x = x * a % p
        k += 1
        if k > p:
            return None
    return k


def primitive_root(p: int) -> int:
    """Return the least primitive root modulo prime ``p``."""
    from sympy import factorint

    factors = list(factorint(p - 1))
    g = 2
    while True:
        if all(pow(g, (p - 1) // f, p) != 1 for f in factors):
            return g
        g += 1


def find_design_eigenvalue(N: int, K: int, trace: int = T_TRACE) -> int:
    """Find a root of x^2-trace*x+1 with multiplicative order K modulo N."""
    roots = sqrt_mod(trace * trace - 4, N)
    if not roots:
        raise ValueError(f"N={N} is not split for trace={trace}")
    inv2 = pow(2, N - 2, N)
    for root in roots:
        candidate = (trace + root) * inv2 % N
        if multiplicative_order(candidate, N) == K:
            return candidate
    raise ValueError(f"no eigenvalue of order K={K} at N={N}")


def build_closed_form(
    N: int,
    K: int,
    a: int,
    k0: int,
    parity_odd: bool,
    qs,
):
    """Build standardized spectral moments of the twisted-Jacobi matrix M_q.

    Characters are indexed by k with k == k0 (mod K), then filtered by parity.
    The returned dictionary is keyed by q and contains m, s2, mu4, mu6 and tr2.
    """
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N

    ks = np.array(
        [
            k
            for k in range(N - 1)
            if k % K == k0 % K and (k % 2 == 1) == parity_odd
        ],
        dtype=np.int64,
    )
    m = len(ks)
    xs = np.array([x for x in range(N) if x not in (0, 1)], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))

    out = {}
    inv2 = pow(2, N - 2, N)
    for q in qs:
        q = int(q)
        phase = np.exp(2j * np.pi * (q * xs % N) / N)
        J = (W * phase) @ V.T
        C = np.exp(-2j * np.pi * (inv2 * q % N) / N) * J / (N - 1)
        M = C + C.conj().T
        ev = np.linalg.eigvalsh(M)
        centered = ev - ev.mean()
        s2 = float((centered**2).mean())
        standardized = centered / np.sqrt(s2)
        out[q] = {
            "m": m,
            "s2": s2,
            "mu4": float((standardized**4).mean()),
            "mu6": float((standardized**6).mean()),
            "tr2": float((ev**2).sum()),
        }
    return out, m
