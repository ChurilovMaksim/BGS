#!/usr/bin/env python3
r"""Exact finite-N audit of the M1 twist-pair energy assembly.

This is research code, not a proof of an asymptotic theorem.

The key table is built directly from ordered pairs x,y in F_N\{0,1}:
    u = x/y,
    v = (x-1)/(y-1),
    d = x-y.
The map is one-to-one off x=y.  The diagonal x=y collapses to the
single key (u,v,d)=(1,1,0) with multiplicity N-2.  We keep that
multiplicity exactly.

If H=<a> has order K and m=(N-1)/K, let c(u) in Z/mZ denote the H-coset
of u.  W[c_u,c_v,d] is the exact key multiplicity.  Then

  B(t) = sum_{c_u,c_v,d1+d2=t}
           W[c_u,c_v,d1] W[-c_u,-c_v,d2]

is an integer count.  The quotient-character DFT gives A_tau(d), and

  B(t) = m^-2 sum_tau (A_tau * A_tau)(t)

is checked numerically against the integer count.  Crucially, the full
energy expands all cross-twist terms; no orthogonality is assumed.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import numpy as np


def prime_factors(n: int) -> list[int]:
    out: list[int] = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            out.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


def primitive_root(p: int) -> int:
    factors = prime_factors(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise ValueError(f"no primitive root found modulo {p}")


def multiplicative_order(a: int, p: int) -> int:
    x = 1
    for k in range(1, p):
        x = x * a % p
        if x == 1:
            return k
    raise ValueError(f"{a} is not a unit modulo {p}")


def dlog_table(p: int, g: int) -> np.ndarray:
    table = np.full(p, -1, dtype=np.int64)
    x = 1
    for e in range(p - 1):
        table[x] = e
        x = x * g % p
    if np.any(table[1:] < 0):
        raise AssertionError("primitive-root dlog table is incomplete")
    return table


def build_key_tensor(N: int, a: int, K: int) -> tuple[np.ndarray, dict]:
    if multiplicative_order(a, N) != K:
        raise ValueError(f"ord_{N}({a}) != K={K}")
    if (N - 1) % K:
        raise ValueError("K must divide N-1")
    m = (N - 1) // K
    g = primitive_root(N)
    dl = dlog_table(N, g)
    if int(dl[a]) % m != 0:
        raise AssertionError("H=<a> is not the exponent-m subgroup")

    inv = np.zeros(N, dtype=np.int64)
    for z in range(1, N):
        inv[z] = pow(z, N - 2, N)

    W = np.zeros((m, m, N), dtype=np.int64)
    for x in range(2, N):
        for y in range(2, N):
            u = x * int(inv[y]) % N
            v = (x - 1) * int(inv[y - 1]) % N
            d = (x - y) % N
            W[int(dl[u]) % m, int(dl[v]) % m, d] += 1

    expected = (N - 2) ** 2
    if int(W.sum()) != expected:
        raise AssertionError(f"key mass {int(W.sum())} != {expected}")
    singular = int(W[0, 0, 0])
    if singular != N - 2 or int(W[:, :, 0].sum()) != N - 2:
        raise AssertionError("d=0 singular fiber does not equal the x=y diagonal")

    meta = {
        "N": N,
        "a": a,
        "K": K,
        "m": m,
        "primitive_root": g,
        "dlog_a": int(dl[a]),
        "key_mass": int(W.sum()),
        "singular_multiplicity_d0": singular,
    }
    return W, meta


def cyclic_convolution(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return np.fft.ifft(np.fft.fft(a) * np.fft.fft(b))


def exact_direct_B(W: np.ndarray) -> np.ndarray:
    """Integer B(t) from quotient-coset subgroup constraints."""
    m, _, N = W.shape
    B = np.zeros(N, dtype=np.int64)
    for cu in range(m):
        for cv in range(m):
            conv = cyclic_convolution(W[cu, cv], W[-cu % m, -cv % m]).real
            B += np.rint(conv).astype(np.int64)
    return B


def expected_regular_coset_masses(m: int, K: int) -> np.ndarray:
    """Exact total regular key mass in each quotient-coset pair."""
    out = np.empty((m, m), dtype=np.int64)
    for cu in range(m):
        for cv in range(m):
            if cu == 0 and cv == 0:
                out[cu, cv] = (K - 1) * (K - 2)
            elif cu == cv or cu == 0 or cv == 0:
                out[cu, cv] = K * (K - 1)
            else:
                out[cu, cv] = K * K
    return out


def twist_data(W: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return A_tau(d), F_tau=A_tau*A_tau, and reconstructed B."""
    m = W.shape[0]
    A = np.fft.fft2(W.astype(np.complex128), axes=(0, 1))
    F = np.fft.ifft(np.fft.fft(A, axis=2) ** 2, axis=2)
    B = F.sum(axis=(0, 1)) / (m * m)
    return A, F, B


def energy_summary(W: np.ndarray, *, significance_rel: float = 1e-7, compute_gram: bool = True) -> dict:
    m, _, N = W.shape
    K = (N - 1) // m
    B_direct = exact_direct_B(W)
    A, F, B_twist = twist_data(W)
    recon_err = float(np.max(np.abs(B_twist - B_direct)))

    full_energy = float(np.sum(B_direct.astype(np.float64) ** 2))
    trivial_vec = F[0, 0] / (m * m)
    trivial_energy = float(np.sum(np.abs(trivial_vec) ** 2))
    delta_vs_trivial = (full_energy - trivial_energy) / trivial_energy

    diagonal_energy = float(np.sum(np.abs(F) ** 2) / (m**4))
    cross_energy = full_energy - diagonal_energy

    # The d=0 fiber is singular: all x=y collapse to (1,1,0), so every
    # quotient character has A_tau(0)=N-2.  Recompute after removing only
    # that exact singular fiber; this is a diagnostic, not a theorem step.
    W_regular = W.copy()
    W_regular[:, :, 0] = 0
    regular_mass = W_regular.sum(axis=2)
    expected_mass = expected_regular_coset_masses(m, K)
    coset_mass_error = int(np.max(np.abs(regular_mass - expected_mass)))

    B_regular_direct = exact_direct_B(W_regular)
    _, F_regular, B_regular = twist_data(W_regular)
    regular_recon_err = float(np.max(np.abs(B_regular - B_regular_direct)))
    regular_energy = float(np.sum(B_regular_direct.astype(np.float64) ** 2))
    regular_trivial = float(np.sum(np.abs(F_regular[0, 0] / (m * m)) ** 2))
    regular_diag = float(np.sum(np.abs(F_regular) ** 2) / (m**4))
    regular_cross = regular_energy - regular_diag

    c = N - 2
    singular_rhs = B_regular_direct + 2 * c * W_regular[0, 0].astype(np.int64)
    singular_rhs = singular_rhs.copy()
    singular_rhs[0] += c * c
    singular_decomp_error = int(np.max(np.abs(B_direct - singular_rhs)))

    nontrivial_mask = np.ones((m, m), dtype=bool)
    nontrivial_mask[0, 0] = False
    nontriv = np.abs(A[nontrivial_mask])
    nontriv_regular = np.abs(A[nontrivial_mask][:, 1:])
    max_all = float(nontriv.max()) if nontriv.size else 0.0
    max_regular = float(nontriv_regular.max()) if nontriv_regular.size else 0.0

    gram_diag = {
        "computed": False,
        "reason": "disabled for this run",
    }
    if compute_gram:
        # Cross-twist Gram matrix for small/medium falsifier cases only.
        flat = F.reshape(m * m, N)
        raw_gram = flat @ flat.conj().T
        gram_scale = float(np.max(np.abs(raw_gram)) / (m**4))
        gram = raw_gram / (m**4)
        np.fill_diagonal(gram, 0.0)
        threshold = significance_rel * max(1.0, gram_scale)
        significant = int(np.count_nonzero(np.abs(gram) > threshold))
        possible = m * m * (m * m - 1)
        gram_diag = {
            "computed": True,
            "significant_ordered_offdiag_entries": significant,
            "possible_ordered_offdiag_entries": possible,
            "significance_relative_threshold": significance_rel,
            "minimum_offdiag_abs": float(np.min(np.abs(gram)[~np.eye(m*m, dtype=bool)])) if possible else 0.0,
        }

    return {
        "projector_identity": {
            "max_abs_B_reconstruction_error": recon_err,
            "passed_1e-8": recon_err < 1e-8,
        },
        "counts": {
            "V4_count": int(B_direct.sum()),
            "B_l2_energy_exact_integer": int(np.dot(B_direct, B_direct)),
        },
        "full_twist_energy": {
            "energy": full_energy,
            "trivial_twist_energy": trivial_energy,
            "delta_vs_trivial": delta_vs_trivial,
            "diagonal_twist_energy": diagonal_energy,
            "cross_twist_energy": cross_energy,
            "cross_fraction_of_full": cross_energy / full_energy,
            "cross_gram": gram_diag,
        },
        "singular_fiber": {
            "A_tau_d0_expected": N - 2,
            "regular_coset_mass_identity_max_integer_error": coset_mass_error,
            "HH_regular_mass": int(W_regular[0, 0].sum()),
            "HH_regular_mass_expected": (K - 1) * (K - 2),
            "direct_singular_regular_decomposition_max_integer_error": singular_decomp_error,
            "regular_projector_max_abs_error": regular_recon_err,
            "max_nontrivial_abs_A_including_d0": max_all,
            "max_nontrivial_abs_A_regular_d_nonzero": max_regular,
            "weil_reference_3sqrtN": 3.0 * math.sqrt(N),
            "weil_reference_4sqrtN": 4.0 * math.sqrt(N),
            "regular_only_energy": regular_energy,
            "regular_only_trivial_energy": regular_trivial,
            "regular_only_delta_vs_trivial": (regular_energy - regular_trivial) / regular_trivial,
            "regular_only_diagonal_twist_energy": regular_diag,
            "regular_only_cross_twist_energy": regular_cross,
            "regular_only_cross_fraction_of_full": regular_cross / regular_energy,
        },
    }


def run_case(N: int, a: int, K: int) -> dict:
    W, meta = build_key_tensor(N, a, K)
    out = {
        "status": "RESEARCH_DIAGNOSTIC_NOT_A_PROOF",
        "definition": "weighted key table from all ordered x,y in F_N\\{0,1}",
        "meta": meta,
    }
    out.update(energy_summary(W))
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--N", type=int, required=True)
    parser.add_argument("--a", type=int, required=True)
    parser.add_argument("--K", type=int, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_case(args.N, args.a, args.K)
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
