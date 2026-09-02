"""Exact k=2 fluctuation-layer reduction and direct numerical identity check.

For the annihilator character coset S, the checked identity is

    A_S(q) = m^2 * ((N-2) + S_off(q)),

with |P|=(K-1)(K-2) for the off-diagonal constraint set P. The two canonical
checks are N=53,K=13 and N=199,K=11. This statement is independent of the
later, currently open, M1/Möbius-fiber asymptotic step.
"""
from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from code.math.jacobi import dlog_table  # noqa: E402
from code.math.twisted_jacobi import primitive_root  # noqa: E402

OUT = os.path.join(ROOT, "results", "verified", "h3_k2_exact_reduction.json")
LOG = os.path.join(ROOT, "results", "verified", "h3_k2_exact_reduction.log")


def log(message) -> None:
    line = str(message)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as handle:
        handle.write(line + "\n")


def subgroup(N: int, K: int, g: int) -> list[int]:
    h = pow(g, (N - 1) // K, N)
    values, x = [], 1
    for _ in range(K):
        values.append(x)
        x = x * h % N
    return values


def constraint_pairs(N: int, H: list[int]) -> list[tuple[int, int]]:
    Hset = set(H)
    pairs = []
    for x in range(2, N):
        for y in range(2, N):
            if x == y:
                continue
            if (x * pow(y, N - 2, N)) % N not in Hset:
                continue
            if ((x - 1) * pow(y - 1, N - 2, N)) % N not in Hset:
                continue
            pairs.append((x, y))
    return pairs


def run_design(N: int, a: int, K: int) -> dict:
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    H = subgroup(N, K, g)
    pairs = constraint_pairs(N, H)
    n_pairs = len(pairs)
    expected = (K - 1) * (K - 2)
    log(f"N={N} a={a} K={K}: |P|={n_pairs}, expected={expected}")
    if n_pairs != expected:
        raise AssertionError((N, K, n_pairs, expected))

    xs_pair = np.array([x for x, _ in pairs], dtype=np.int64)
    ys_pair = np.array([y for _, y in pairs], dtype=np.int64)

    ell = int(dlog[a])
    divisor = math.gcd(ell, N - 1)
    modulus = (N - 1) // divisor
    ks = np.array([k for k in range(N - 1) if k % modulus == 0], dtype=np.int64)
    m = len(ks)

    xs = np.array([x for x in range(1, N) if x != 1], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))

    differences = (xs_pair - ys_pair) % N
    s_off = np.array(
        [
            np.exp(2j * np.pi * (q * differences % N) / N).sum()
            for q in range(1, N)
        ]
    )

    max_dev = 0.0
    for q in (1, 2, 3):
        phase = np.exp(2j * np.pi * (q * xs % N) / N)
        J = (W * phase) @ V.T
        energy = float((np.abs(J) ** 2).sum())
        predicted = m * m * ((N - 2) + s_off[q - 1].real)
        max_dev = max(max_dev, abs(energy - predicted))

    A_values = m * m * ((N - 2) + s_off.real)
    predicted_mean = -n_pairs / (N - 1)
    predicted_std = math.sqrt(n_pairs)
    return {
        "N": N,
        "a": a,
        "K": K,
        "m": m,
        "n_pairs": n_pairs,
        "identity_max_dev": float(max_dev),
        "mean_S_off": float(s_off.real.mean()),
        "pred_mean_S_off": float(predicted_mean),
        "std_S_off": float(s_off.real.std()),
        "pred_std_S_off": float(predicted_std),
        "std_A": float(A_values.std()),
        "pred_std_A": float(m * m * predicted_std),
        "std_A_over_mN": float(A_values.std() / (m * N)),
    }


def main() -> None:
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    if os.path.exists(LOG):
        os.remove(LOG)
    t0 = time.time()
    designs = [(53, 10, 13), (199, 139, 11)]
    rows = [run_design(*design) for design in designs]
    out = {
        "script": "code/verification/h3_k2_exact_reduction.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "designs": rows,
        "verdict": "PASS"
        if all(r["identity_max_dev"] < 1e-8 for r in rows)
        else "FAIL",
        "walltime_s": time.time() - t0,
    }
    with open(OUT, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
    log(f"artifact -> {OUT}")
    log(f"verdict -> {out['verdict']}")


if __name__ == "__main__":
    main()
