from __future__ import annotations

import argparse
import json
import math

import numpy as np


def factorint(n: int) -> list[int]:
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
    factors = factorint(p - 1)
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in factors):
            return g
    raise RuntimeError("primitive root not found")


def dlog_table(p: int, g: int) -> np.ndarray:
    dlog = np.full(p, -1, dtype=np.int64)
    x = 1
    for s in range(p - 1):
        dlog[x] = s
        x = x * g % p
    return dlog


def annihilator_characters(p: int, K: int) -> tuple[np.ndarray, np.ndarray, int]:
    g = primitive_root(p)
    dlog = dlog_table(p, g)
    ks = np.arange(0, p - 1, K, dtype=np.int64)
    psi = np.zeros((len(ks), p), dtype=np.complex128)
    nz = np.arange(1, p, dtype=np.int64)
    psi[:, nz] = np.exp(2j * np.pi * np.outer(ks, dlog[nz]) / (p - 1))
    return psi, ks, g


def build_fiber_sums(p: int, K: int) -> tuple[np.ndarray, int, np.ndarray, int]:
    """Build the historical Mobius-fiber sums A_(psi1,psi2)(d).

    This reproduces the object stated in paper/final/mobius_fiber_theorem.tex:
        v(u) = (u(d-1)+1)/(d-u+1).
    u and v are restricted to F_p^*, and the pole is omitted.

    This is an audit of that historical assembly. It is not yet a proof that
    the assembly equals the full current k=4 coupled-energy object.
    """
    psi, ks, g = annihilator_characters(p, K)
    m = len(ks)
    A = np.zeros((m * m, p), dtype=np.complex128)
    us = np.arange(1, p, dtype=np.int64)

    for d in range(p):
        den = (d - us + 1) % p
        valid = den != 0
        u = us[valid]
        num = (u * ((d - 1) % p) + 1) % p
        inv = np.array([pow(int(x), p - 2, p) for x in den[valid]], dtype=np.int64)
        v = num * inv % p
        valid_v = v != 0
        u = u[valid_v]
        v = v[valid_v]
        A[:, d] = (psi[:, u] @ psi[:, v].T).reshape(-1)
    return A, m, ks, g


def analyse(p: int, K: int) -> dict[str, object]:
    if (p - 1) % K:
        raise ValueError("K must divide p-1")

    A, m, ks, g = build_fiber_sums(p, K)
    # Circular convolution F_tau = A_tau * A_tau.
    F = np.fft.ifft(np.fft.fft(A, axis=1) ** 2, axis=1)

    summed = F.sum(axis=0)
    total_raw = float(np.vdot(summed, summed).real)
    diag_raw = float(np.sum(np.abs(F) ** 2).real)
    cross_raw = total_raw - diag_raw

    trivial_diag_raw = float(np.vdot(F[0], F[0]).real)
    nontrivial_diag_raw = diag_raw - trivial_diag_raw
    nontrivial_sum = F[1:].sum(axis=0)
    trivial_nontrivial_cross_raw = float(2 * np.real(np.vdot(F[0], nontrivial_sum)))
    nontrivial_total_raw = float(np.vdot(nontrivial_sum, nontrivial_sum).real)
    nontrivial_cross_raw = nontrivial_total_raw - nontrivial_diag_raw

    bound = 4 * math.sqrt(p)
    abs_A = np.abs(A[1:])
    violations = np.argwhere(abs_A > bound + 1e-8)
    violation_rows = []
    for flat_minus_one, d in violations:
        flat = int(flat_minus_one) + 1
        r, s = divmod(flat, m)
        violation_rows.append(
            {
                "twist_indices": [r, s],
                "character_exponents": [int(ks[r]), int(ks[s])],
                "d": int(d),
                "abs_A": float(abs(A[flat, d])),
            }
        )

    energy = total_raw / (m**4)
    reconstructed = (diag_raw + cross_raw) / (m**4)
    return {
        "N": p,
        "K": K,
        "m": m,
        "primitive_root": g,
        "num_twist_pairs": m * m,
        "normalization": "psi_k(x)=exp(2pi i k log_g(x)/(N-1)); k multiple of K; psi(0)=0",
        "fiber_model": "historical Mobius graph v=(u(d-1)+1)/(d-u+1), u,v nonzero, pole excluded",
        "energy_total": energy,
        "energy_reconstructed": reconstructed,
        "reconstruction_abs_error": abs(energy - reconstructed),
        "diag_raw": diag_raw,
        "cross_raw": cross_raw,
        "cross_over_total_raw": cross_raw / total_raw,
        "cross_over_diag_raw": cross_raw / diag_raw,
        "trivial_diag_raw": trivial_diag_raw,
        "nontrivial_diag_raw": nontrivial_diag_raw,
        "trivial_nontrivial_cross_raw": trivial_nontrivial_cross_raw,
        "nontrivial_cross_raw": nontrivial_cross_raw,
        "max_abs_nontrivial_A": float(abs_A.max()),
        "weil_4sqrtN": bound,
        "weil_violations": violation_rows,
        "special_fiber_d0": "For psi1=1 and psi2 nontrivial, d=0 has v(u)=1 for every admissible u!=1, hence A(0)=N-2 exactly.",
        "cross_terms_nonzero": abs(cross_raw) > 1e-8 * max(1.0, total_raw),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--design", action="append", default=[])
    parser.add_argument("--out")
    args = parser.parse_args()
    designs = args.design or ["53,13", "199,11"]
    results = [analyse(*map(int, spec.split(","))) for spec in designs]
    payload = {
        "status": "EXPERIMENTAL EXACT-AS-IMPLEMENTED",
        "claim": "Audits the historical Mobius-fiber twist assembly; does not yet certify equivalence to the full current k=4 object.",
        "results": results,
    }
    text = json.dumps(payload, indent=2, sort_keys=True)
    print(text)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(text + "\n")


if __name__ == "__main__":
    main()
