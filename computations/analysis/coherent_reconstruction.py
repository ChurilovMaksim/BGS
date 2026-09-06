#!/usr/bin/env python3
"""High-precision one-mode reference for the finite Chebyshev reconstruction.

Proofs cover any fixed number of modes; this implementation intentionally
implements one mode only. Input probabilities are for normalized projectors,
not Husimi densities (multiply a Husimi Q value by pi first). No Fock cutoff
is assumed for the input probability callable. The output is a finite matrix.

The theorem's L=128*K is conservative; smaller L can be supplied for numerical
experiments, but do not inherit its asymptotic bias bound. Use adequate decimal
precision: the inverse problem is severely ill-conditioned.
"""
from __future__ import annotations
from dataclasses import dataclass
from functools import lru_cache
from math import comb, factorial
from typing import Callable, Sequence
import mpmath as mp


@lru_cache(maxsize=None)
def chebyshev_coefficients(n: int) -> tuple[int, ...]:
    """Integer monomial coefficients of T_n, in increasing order."""
    if not isinstance(n, int) or n < 0:
        raise ValueError('n must be a nonnegative integer')
    if n == 0:
        return (1,)
    if n == 1:
        return (0, 1)
    previous, current = [1], [0, 1]
    for _ in range(1, n):
        nxt = [0] * (len(current) + 1)
        for j, value in enumerate(current):
            nxt[j+1] += 2*value
        for j, value in enumerate(previous):
            nxt[j] -= value
        previous, current = current, nxt
    return tuple(current)


def trace_norm_hermitian(matrix: mp.matrix) -> mp.mpf:
    if matrix.rows != matrix.cols:
        raise ValueError('square matrix required')
    h = (matrix + matrix.H) / 2
    eigenvalues = mp.eigsy(h, eigvals_only=True) if not any(
        mp.im(x) for x in h
    ) else mp.eighe(h, eigvals_only=True)
    return mp.fsum(abs(x) for x in eigenvalues)


def density_from_positive_part(matrix: mp.matrix) -> mp.matrix:
    """Hermitian symmetrization, positive part, trace normalization."""
    if matrix.rows != matrix.cols or matrix.rows == 0:
        raise ValueError('nonempty square matrix required')
    h = (matrix + matrix.H) / 2
    values, vectors = mp.eighe(h)
    positive = [max(mp.mpf(0), value) for value in values]
    total = mp.fsum(positive)
    if total == 0:
        out = mp.zeros(h.rows)
        out[0, 0] = 1
        return out
    return vectors * mp.diag([value/total for value in positive]) * vectors.H


def fock_probability(rho: mp.matrix, z: mp.mpc) -> mp.mpf:
    """Probability for a finite Fock matrix, embedded in the full Hilbert space."""
    if rho.rows != rho.cols:
        raise ValueError('square matrix required')
    v = mp.matrix([z**j/mp.sqrt(factorial(j)) for j in range(rho.rows)])
    return mp.re(mp.exp(-abs(z)**2) * (v.H*rho*v)[0])


def _complex_monomial_coefficient(p: int, q: int, j: int) -> mp.mpc:
    """Coefficient of w^j z^(p+q-j) in ((z+w)/2)^p ((z-w)/(2i))^q."""
    signed_sum = sum(comb(p, ell)*comb(q, j-ell)*(-1)**(j-ell)
                     for ell in range(max(0, j-q), min(p, j)+1))
    return mp.mpc(signed_sum) * (1j)**(-q) / (2**(p+q))


@dataclass
class Reconstruction:
    raw: mp.matrix
    density: mp.matrix
    nodes: tuple[mp.mpf, ...]
    degree: int
    cutoff: int
    squared_radius: mp.mpf
    decimal_precision: int


def reconstruct(probability: Callable[[mp.mpc], object], cutoff: int, degree: int,
                squared_radius: object, *, decimal_precision: int = 100,
                observations: Sequence[Sequence[object]] | None = None) -> Reconstruction:
    """Reconstruct low matrix entries from tensor Gauss-Chebyshev nodes.

    observations, when supplied, are a (degree+1)^2 array of measured
    probabilities, ordered as real-coordinate index then imaginary-coordinate
    index. The callable is ignored in that case. The grid is inside |z|^2<=S.
    Returned mpmath numbers retain the precision at which they were formed;
    callers should use a compatible workdps context for subsequent arithmetic.
    """
    if not isinstance(cutoff, int) or cutoff < 0:
        raise ValueError('nonnegative integer cutoff required')
    if not isinstance(degree, int) or degree < max(1, 2*cutoff):
        raise ValueError('degree must be an integer at least max(1,2*cutoff)')
    if decimal_precision < 30:
        raise ValueError('at least 30 decimal digits required')
    with mp.workdps(decimal_precision):
        S = mp.mpf(squared_radius)
        if not mp.isfinite(S) or S <= 0:
            raise ValueError('positive finite squared radius required')
        a = mp.sqrt(S/2)
        count = degree+1
        angles = [mp.pi*(j+mp.mpf('0.5'))/count for j in range(count)]
        nodes = tuple(a*mp.cos(theta) for theta in angles)
        if observations is not None and (len(observations) != count or
                any(len(row) != count for row in observations)):
            raise ValueError('observation grid has wrong dimensions')
        data = mp.zeros(count)
        for j, x in enumerate(nodes):
            for k, y in enumerate(nodes):
                z = mp.mpc(x, y)
                value = mp.mpf(observations[j][k] if observations is not None else probability(z))
                if not mp.isfinite(value):
                    raise ValueError('non-finite observed probability')
                data[j, k] = mp.exp(abs(z)**2)*value
        transform = mp.matrix(count, count)
        for ell in range(count):
            weight = mp.mpf(1 if ell == 0 else 2)/count
            for j in range(count):
                transform[ell, j] = weight*mp.cos(ell*angles[j])
        coefficients = transform*data*transform.T
        # Convert retained Chebyshev coefficients to low real monomials.
        max_degree = 2*cutoff
        real_coeff = [[mp.mpf(0) for _ in range(max_degree+1)]
                      for _ in range(max_degree+1)]
        polys = [chebyshev_coefficients(j) for j in range(count)]
        for alpha in range(count):
            for beta in range(count-alpha):
                value = coefficients[alpha, beta]
                for p, cp in enumerate(polys[alpha][:max_degree+1]):
                    if cp == 0:
                        continue
                    for q, cq in enumerate(polys[beta][:max_degree-p+1]):
                        if cq:
                            real_coeff[p][q] += value*cp*cq/a**(p+q)
        raw = mp.zeros(cutoff+1)
        for j in range(cutoff+1):
            for k in range(cutoff+1):
                d = j+k
                value = mp.fsum(real_coeff[p][d-p] *
                               _complex_monomial_coefficient(p, d-p, j)
                               for p in range(d+1))
                raw[j, k] = value*mp.sqrt(factorial(j)*factorial(k))
        raw = (raw+raw.H)/2
        return Reconstruction(raw, density_from_positive_part(raw), nodes,
                              degree, cutoff, S, decimal_precision)


def coefficient_bound(cutoff: int, degree: int, squared_radius: object,
                      noise: object, modes: int = 1) -> mp.mpf:
    """Explicit theorem bound, not an error estimate fitted to a test."""
    if modes < 1 or cutoff < 0:
        raise ValueError('invalid dimension or cutoff')
    S, eta = mp.mpf(squared_radius), mp.mpf(noise)
    if S <= 0 or eta < 0 or degree < max(2*cutoff, 2*modes, 16*S):
        raise ValueError('the coefficient-lemma hypotheses are not satisfied')
    A = max(mp.mpf(1), factorial(cutoff)*(2*modes/S)**cutoff)
    C = 4**modes*(degree+1)**(2*modes)*mp.mpf(3)**degree
    tail = 4*mp.sqrt(comb(degree+2*modes, 2*modes-1))*mp.power(2*S, (degree+1)/2)/mp.sqrt(factorial(degree+1))
    return C*A*(mp.exp(S)*eta+tail)
