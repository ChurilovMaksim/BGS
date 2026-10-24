"""Odd twisted-Jacobi blocks: orbit matrices and exact all-order Weyl traces.

The global-law proof and its strong arithmetic restrictions are recorded in
mathematics/spectral-obstructions/magnetic_quotient_semicircle.md. No microscopic law is assumed.
"""
from __future__ import annotations
from collections import Counter
from fractions import Fraction
from itertools import product
import math
import numpy as np
from .finite_field import require_integer, require_odd_prime, multiplicative_order
from .jacobi import _checked_dlog, require_supported_prime


# Scalar parameters and residue sequences require exact integers. Convert
# NumPy scalars to Python ints
# before scalar modular arithmetic; reduce residues before vectorized products.
def _prime(p: int) -> int:
    p = require_integer(p, "p")
    require_odd_prime(p)
    return p


def _positive_integer(value: int, name: str) -> int:
    value = require_integer(value, name)
    if value < 1:
        raise ValueError(f"{name} must be positive")
    return value


def _residues(values, modulus: int, name: str) -> tuple[int, ...]:
    try:
        entries = tuple(values)
    except TypeError as exc:
        raise ValueError(f"{name} must be a one-dimensional integer sequence") from exc
    # Inspect original entries, not np.asarray(values): mixed booleans/integers
    # would otherwise be coerced to integers before validation.
    return tuple(require_integer(value, f"{name} entry") % modulus
                 for value in entries)


def _subgroup_residues(p: int, H) -> tuple[int, ...]:
    H = _residues(H, p, "H")
    if not H or 0 in H or p - 1 in H:
        raise ValueError("H must be nonempty and exclude zero and -1")
    return H


def subgroup(p: int, K: int, h: int) -> tuple[int, ...]:
    p = _prime(p)
    K = require_integer(K, "K")
    h = require_integer(h, "h") % p
    if K < 1 or K % 2 == 0 or (p-1) % K:
        raise ValueError("K must be a positive odd divisor of p-1")
    if multiplicative_order(h % p, p) != K:
        raise ValueError("incorrect subgroup generator order")
    return tuple(pow(h, j, p) for j in range(K))


def orbit_coordinates(p: int, H: tuple[int, ...]):
    """Signed H-orbits; callers supply a subgroup with exact integer entries."""
    p = require_supported_prime(p)
    H = _subgroup_residues(p, H)
    index = np.full(p, -1, dtype=np.int64)
    sign = np.zeros(p, dtype=np.int64)
    reps = []
    for r in range(1, p):
        if index[r] >= 0:
            continue
        i = len(reps)
        reps.append(r)
        for h in H:
            x = r*h % p
            for y, s in ((x, 1), ((-x) % p, -1)):
                if index[y] >= 0:
                    raise ValueError("invalid subgroup: signed orbit overlap")
                index[y], sign[y] = i, s
    if len(reps)*2*len(H) != p-1:
        raise ValueError("invalid orbit dimension")
    return index, sign, tuple(reps)


def orbit_matrix(p: int, H: tuple[int, ...], q: int) -> np.ndarray:
    """O(p) contributions, but a dense n-by-n return array (O(n^2) storage)."""
    p = require_supported_prime(p)
    H = _subgroup_residues(p, H)
    q = require_integer(q, "q") % p
    if q == 0:
        raise ValueError("q must be nonzero")
    index, sign, reps = orbit_coordinates(p, H)
    x = np.arange(2, p, dtype=np.int64)
    phase = np.exp(2j*np.pi*((q*(x-pow(2, -1, p))) % p)/p)
    M = np.zeros((len(reps), len(reps)), dtype=complex)
    np.add.at(M, (index[x], index[x-1]), sign[x]*sign[x-1]*phase/(2*len(H)))
    return M+M.conj().T


def orbit_basis(p: int, H: tuple[int, ...]) -> np.ndarray:
    p = require_supported_prime(p)
    H = _subgroup_residues(p, H)
    index, sign, reps = orbit_coordinates(p, H)
    V = np.zeros((p, len(reps)))
    V[np.arange(1, p), index[1:]] = sign[1:]/math.sqrt(2*len(H))
    return V


def gauss_real_gauge(p: int, dlog: np.ndarray, indices: np.ndarray, q: int):
    """D* A D is real; this is not the non-isospectral operation A.real."""
    p = require_supported_prime(p)
    q = require_integer(q, "q") % p
    dlog = _checked_dlog(dlog, p)
    indices = np.asarray(_residues(indices, p-1, "indices"), dtype=np.int64)
    if q == 0 or np.any(indices == 0):
        raise ValueError("nonzero q and nontrivial characters are required")
    chars = np.exp(2j*np.pi*np.outer(indices, dlog[1:])/(p-1))
    additive = np.exp(2j*np.pi*(np.arange(1, p)*q % p)/p)
    a = chars.conj()@additive/math.sqrt(p)
    return np.exp(0.5j*np.angle(a)), a


def word_histogram(p: int, H: tuple[int, ...], m: int) -> Counter:
    """Signed integer coefficients: Tr A_q^m=sum C[t] e_p(qt)/(2K^m).

    Reference enumeration costs (2K)^m. Restricted to q!=0; m>=1.
    """
    p = _prime(p)
    H = _subgroup_residues(p, H)
    m = _positive_integer(m, "m")
    if (2*len(H))**m > 10_000_000:
        raise ValueError("positive m and at most ten million reference words required")
    inv2 = pow(2, -1, p)
    choices = tuple(product((-1, 1), H))
    C = Counter()
    def visit(depth, g, A, B, c):
        if depth == m:
            if g == 1:
                if A == B == 0:
                    C[c] += p
            else:
                C[(c+A*B*(1+g)*inv2*pow(1-g, -1, p)) % p] += 1
            C[(c+A*B*(1-g)*inv2*pow(1+g, -1, p)) % p] -= 1
            return
        ig = pow(g, -1, p)
        for eps, h in choices:
            visit(depth+1, g*h % p, (A+eps*ig) % p, (B+eps*g) % p,
                  (c+eps*(A*g-B*ig)*inv2) % p)
    visit(0, 1, 0, 0, 0)
    # Unary +Counter would wrongly delete negative coefficients.
    return Counter({t:v for t,v in C.items() if v})


def canonical_histogram(p: int, C: Counter) -> list[int]:
    """Canonicalize coefficients; C must have canonical integer residue keys.

    C is a caller-supplied exact signed-integer histogram, e.g. word_histogram
    output. Its keys/counts are assumed, not validated, by histogram helpers.
    """
    p = _prime(p)
    return [C.get(t, 0)-C.get(p-1, 0) for t in range(p)]


def histogram_trace(p: int, K: int, m: int, q: int, C: Counter) -> complex:
    """Evaluate the trace from caller-supplied canonical exact histogram C."""
    p = _prime(p)
    K = _positive_integer(K, "K")
    m = _positive_integer(m, "m")
    q = require_integer(q, "q") % p
    if q == 0:
        raise ValueError("this trace formula excludes q=0")
    return sum(v*np.exp(2j*np.pi*(q*t % p)/p) for t,v in C.items())/(2*K**m)


def mean_trace(p: int, K: int, m: int, C: Counter) -> Fraction:
    """Mean nonzero-q trace; C has the canonical exact histogram contract."""
    p = _prime(p)
    K = _positive_integer(K, "K")
    m = _positive_integer(m, "m")
    return Fraction(p*C.get(0, 0)-sum(C.values()), 2*K**m*(p-1))
