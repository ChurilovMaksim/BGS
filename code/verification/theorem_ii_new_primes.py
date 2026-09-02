"""Independent scalar-sum regression check for twisted-Jacobi matrix elements.

This is a computational certification of the current finite-N kernel, not an
asymptotic theorem. The active gate intentionally uses only the two designs
rerun during the 2026-09-02 canonical rebuild:

    N=461,   K=23
    N=19489, K=29

For each design the vectorised matrix implementation is compared with direct
scalar character sums. At N=461 all 100 matrix entries are checked for each q;
at N=19489 a deterministic 32-entry sample is checked for each q. Historical
larger designs remain in ``archive/legacy-workspace``.

Output: results/verified/theorem_ii_new_primes.json
"""
from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, ROOT)

from code.math.twisted_jacobi import (  # noqa: E402
    multiplicative_order,
    primitive_root,
    sqrt_mod,
)

T_TRACE = 3
DESIGNS = ((461, 23), (19489, 29))
PROBES = (1, 2, 3, 5, 7)
REL_TOL = 5e-10
OUT = os.path.join(ROOT, "results", "verified", "theorem_ii_new_primes.json")


def find_a(N: int, K: int) -> int:
    inv2 = pow(2, N - 2, N)
    for root in sqrt_mod(T_TRACE * T_TRACE - 4, N):
        candidate = (T_TRACE + root) * inv2 % N
        if multiplicative_order(candidate, N) == K:
            return candidate
    raise ValueError(f"no order-{K} split eigenvalue at N={N}")


def character_data(N: int, K: int):
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    ks = np.array(
        [k for k in range(N - 1) if k % K == 1 and k % 2 == 0],
        dtype=np.int64,
    )
    xs = np.arange(2, N, dtype=np.int64)
    return dlog, ks, xs


def sample_pairs(m: int) -> list[tuple[int, int]]:
    if m <= 16:
        return [(i, j) for i in range(m) for j in range(m)]
    pairs = {
        (0, 0), (0, m - 1), (m - 1, 0), (m - 1, m - 1),
        (m // 2, m // 2), (1, 2), (2, 1),
    }
    rng = np.random.default_rng(20260902)
    while len(pairs) < 32:
        pairs.add((int(rng.integers(0, m)), int(rng.integers(0, m))))
    return sorted(pairs)


def certify_one(N: int, K: int) -> dict:
    t0 = time.time()
    a = find_a(N, K)
    dlog, ks, xs = character_data(N, K)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]

    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    V = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))

    pairs = sample_pairs(len(ks))
    max_abs = 0.0
    max_rel = 0.0
    worst = None
    for q in PROBES:
        additive = np.exp(2j * np.pi * (q * xs % N) / N)
        closed = (W * additive) @ V.T
        for i, j in pairs:
            left = np.exp(-2j * np.pi * int(ks[i]) * dl_x / (N - 1))
            right = np.exp(2j * np.pi * int(ks[j]) * dl_xm1 / (N - 1))
            direct = np.sum(left * right * additive)
            dev = abs(complex(closed[i, j]) - complex(direct))
            rel = dev / max(abs(complex(direct)), 1e-15)
            if dev > max_abs:
                max_abs = float(dev)
                worst = [int(q), int(i), int(j)]
            max_rel = max(max_rel, float(rel))

    return {
        "N": N,
        "K": K,
        "a": int(a),
        "k0": 1,
        "parity_odd": False,
        "m_plus": int(len(ks)),
        "qs_probed": len(PROBES),
        "entries_checked_per_q": len(pairs),
        "max_abs_dev_J": max_abs,
        "max_rel_dev_J": max_rel,
        "relative_tolerance": REL_TOL,
        "worst_q_i_j": worst,
        "wall_s": round(time.time() - t0, 2),
    }


def main() -> None:
    rows = []
    verdict = {}
    for N, K in DESIGNS:
        try:
            row = certify_one(N, K)
            verdict[f"N={N}"] = (
                "PASS" if row["max_rel_dev_J"] <= REL_TOL else "REGRESSION"
            )
        except Exception as exc:
            row = {"N": N, "K": K, "error": repr(exc)}
            verdict[f"N={N}"] = "FAIL"
        rows.append(row)
        print(f"N={N} K={K} -> {row}", flush=True)

    out = {
        "script": "code/verification/theorem_ii_new_primes.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "phase": "canonical-rebuild/R87.1-independent-scalar",
        "scope": "audited-fast",
        "designs": rows,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as handle:
        json.dump(out, handle, indent=2)
    print("verdict ->", verdict, flush=True)
    print("artifact ->", OUT, flush=True)


if __name__ == "__main__":
    main()
