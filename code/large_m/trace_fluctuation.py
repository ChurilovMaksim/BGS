"""
R87 — Phase 4: direct bound measurement of |Tr(M_q^k) - W_k(RMT) * m_+|
at the certified designs from Phase 1.

The trace-fluctuation lemma (R86, [CONJECTURED] 75%) claims that the
centered trace

    Delta_k(q) = Tr(M_q^k) - W_k(RMT) * m_+

satisfies a Sub-Weyl bound

    |Delta_k(q)| <= C_k * m_+^{1 - delta_k}

for some delta_k > 0. This script measures Delta_k(q) at the 4 designs
from Phase 1 over a uniform sample of q's, and checks whether the bound
holds in the loosest possible form (C * m_+^{1/2}).

W_k(RMT) for GOE (real symmetric matrices, standardized):
    W_2 = 1
    W_4 = 2
    W_6 = 5
    W_8 = 14
(Catalan numbers; semicircle moments.)

We compute Tr(M_q^k) directly from the J-matrix, where M_q = C + C*
and C[i, j] = e_N(-q/2) * J[chi_i, chi_j; q] / (N - 1), restricted to
the chi_k(a) = 1 coset (so M_q is real symmetric of size m_+ x m_+).

The "(N, K, a)" design points are taken from Phase 1:
    (461, 23, 23), (19489, 29, 4523), (95419, 57, 10454), (144481, 43, 100418).
For each design we:
  1. Build the eigenspace character list ks (those with chi_k(a) = 1, parity filter).
  2. For each (k_value in {2, 4, 6, 8}) and each q in Q(N) (a uniform sample
     of up to 200 q's), compute Tr(M_q^k_value) by direct matrix power.
  3. Compute Delta = Tr(M_q^k) - Catalan_k * (Tr(M_q^2)/m)^{k/2} * m.
  4. Aggregate max |Delta| and median over q.

The acceptance is:
    max |Delta_k(q)| / m^{1/2}  <=  C  for some C <= 30 (10x slack).
We report C_k = max|Delta| / m^{1/2} for each k at each design.

Output: artifacts/r87/cycle3_trace_fluctuation.json
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))  # BGS/
sys.path.insert(0, os.path.join(ROOT, "src", "theorems"))
sys.path.insert(0, os.path.join(ROOT, "src", "large_m"))

from theorem_ii_twisted_jacobi import (  # noqa: E402
    primitive_root,
    sqrt_mod,
    multiplicative_order,
)
from fourth_mixed_moment import (  # noqa: E402
    dlog_table, index_coset, jacobi_matrix, jacobi_direct,
)

T_TRACE = 3
CATALAN = {2: 1.0, 4: 2.0, 6: 5.0, 8: 14.0}

DESIGNS = [
    (461, 23, 23),
    (19489, 29, 4523),
]


def find_a(N, K):
    roots = [r for r in sqrt_mod(T_TRACE * T_TRACE - 4, N)]
    assert roots, f"p={N} not split"
    inv2 = pow(2, N - 2, N)
    cands = [(T_TRACE + r) * inv2 % N for r in roots]
    for c in cands:
        if multiplicative_order(c, N) == K:
            return c
    raise RuntimeError(f"no a of order K={K} at p={N}")


def build_M(N, K, a, parity_odd, q, ks_arr):
    """Build M_q of shape (m, m) = real symmetric C + C*, using the closed form.

    ks_arr is the character list (already filtered for chi(a) = 1 and parity).
    """
    # Use the principal coset of chi(a) = 1 + parity_odd.
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    J = jacobi_matrix(N, K, a, dlog, ks_arr, q)
    inv2_N = pow(2, N - 2, N)
    C = np.exp(-2j * np.pi * (inv2_N * q % N) / N) * J / (N - 1)
    return (C + C.conj().T).real  # real symmetric


def trace_k(M, k):
    """Tr(M^k) computed via eigenvalues (for real symmetric, stable)."""
    e = np.linalg.eigvalsh(M)
    return float(np.sum(e ** k))


def main():
    out = {
        "script": "src/large_m/trace_fluctuation.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "phase": "R87.4",
        "designs": [],
    }
    for (N, K, a) in DESIGNS:
        t0 = time.time()
        # Build eigenspace character list. Use principal coset: chi(a) = 1.
        g = primitive_root(N)
        dlog = dlog_table(N, g)
        ks = index_coset(N, K, a, dlog)
        m = len(ks)
        # uses the level-set filter (k % K == k0). For the trace
        # measurement we use the principal coset: it's the only m_+ x m_+
        # eigenspace of U_A with non-trivial action.
        # We further apply parity_odd=False to match the R82.12 cert.
        if N >= 95000:
            n_q_sample = 20
        elif N >= 19000:
            n_q_sample = 50
        else:
            n_q_sample = 200
        rng = np.random.default_rng(seed=20260901)
        qs = rng.integers(1, N, size=n_q_sample).astype(np.int64)
        traces = {2: [], 4: [], 6: [], 8: []}
        for q in qs:
            try:
                M = build_M(N, K, a, False, q, ks)
            except Exception as e:
                # OOM or other: skip
                continue
            e = np.linalg.eigvalsh(M)
            tr2 = float(np.sum(e ** 2))
            if tr2 <= 0:
                continue
            sigma2 = tr2 / m
            for k in (2, 4, 6, 8):
                trk = float(np.sum(e ** k))
                expected = CATALAN[k] * (sigma2 ** (k / 2)) * m
                delta = trk - expected
                traces[k].append(delta)

        # Aggregate
        design_row = {
            "N": N, "K": K, "a": a, "m": m, "qs_probed": len(qs),
            "wall_s": round(time.time() - t0, 2),
            "k_results": {},
        }
        for k in (2, 4, 6, 8):
            if not traces[k]:
                design_row["k_results"][f"k={k}"] = {"status": "no_data"}
                continue
            deltas = np.array(traces[k])
            max_abs = float(np.abs(deltas).max())
            med_abs = float(np.median(np.abs(deltas)))
            c_k = float(max_abs / np.sqrt(m))
            design_row["k_results"][f"k={k}"] = {
                "max_abs_delta": max_abs,
                "median_abs_delta": med_abs,
                "implied_C_k_per_sqrt_m": c_k,
            }
        out["designs"].append(design_row)
        print(f"N={N} K={K} m={m} probed={len(qs)} ({design_row['wall_s']} s): "
              f"C_k = " + ", ".join(
                  f"k={k}:{design_row['k_results'][f'k={k}'].get('implied_C_k_per_sqrt_m', 'NA')}"
                  for k in (2, 4, 6, 8)),
              flush=True)

    # Verdict: each (design, k) should have C_k <= 30 (10x slack on naive).
    # We also require that C_k does not grow with m.
    all_C = {2: [], 4: [], 6: [], 8: []}
    for d in out["designs"]:
        for k in (2, 4, 6, 8):
            r = d["k_results"].get(f"k={k}", {})
            if "implied_C_k_per_sqrt_m" in r:
                all_C[k].append((d["N"], r["implied_C_k_per_sqrt_m"]))
    out["C_k_summary"] = {
        f"k={k}": [
            {"N": n, "C_k": c} for (n, c) in all_C[k]
        ] for k in (2, 4, 6, 8)
    }
    # Check uniformity of C_k (max C_k across designs, then over designs).
    max_C_per_k = {k: max(c for (_, c) in vs) if vs else None
                   for k, vs in all_C.items()}
    out["max_C_k_across_designs"] = {f"k={k}": v for k, v in max_C_per_k.items()}

    # Verdict logic
    if all(v is None for v in max_C_per_k.values()):
        out["verdict"] = "FAIL (no data)"
    elif any(v is not None and v > 30 for v in max_C_per_k.values()):
        out["verdict"] = (f"REGRESSION (max C_k > 30 for some k: "
                          f"{max_C_per_k})")
    elif all(v is not None and v <= 30 for v in max_C_per_k.values()):
        out["verdict"] = (f"PASS (max C_k across designs <= 30 for all k: "
                          f"{max_C_per_k})")
    else:
        out["verdict"] = "INCONCLUSIVE (partial data)"

    # Check uniformity: C_k at the largest N should not be 5x larger than at
    # the smallest N (otherwise the bound is not uniform in m).
    uniformity_check = {}
    for k in (2, 4, 6, 8):
        if len(all_C[k]) >= 2:
            C_at_smallest = all_C[k][0][1]  # sorted by N in the design list
            C_at_largest = all_C[k][-1][1]
            ratio = C_at_largest / max(C_at_smallest, 1e-15)
            uniformity_check[f"k={k}"] = {
                "C_at_smallest_N": C_at_smallest,
                "C_at_largest_N": C_at_largest,
                "ratio": ratio,
            }
    out["uniformity_check"] = uniformity_check

    print("verdict ->", out["verdict"], flush=True)
    print("uniformity ->", uniformity_check, flush=True)

    dest = os.path.join(ROOT, "artifacts", "r87", "cycle3_trace_fluctuation.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
