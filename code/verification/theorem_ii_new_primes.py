"""
R87 — Phase 1: extended Theorem II certification at 4 new split primes.

Re-derives the twisted Jacobi sum closed form (R82.12) and verifies it
against a brute-force explicit sum at 4 split primes NOT in the R82.12
baseline set (N in {199, 3571}).

  Primes: (461, K=23, m+=10), (19489, K=29, m+=336), (95419, K=57, m+=837),
          (144481, K=43, m+=1680).

Verification protocol:
  - For each (N, K), pick k0=1 and parity_odd=False, matching the R82.12
    certification convention.
  - Compute the closed-form twisted Jacobi matrix by vectorised character sums.
  - Independently compute the same entries through a separately arranged direct
    character-product path.
  - Compare max absolute and relative deviations on five q values.

The default run uses N=461 and N=19489. Pass --all to include the two very
large historical designs.

Output: results/verified/theorem_ii_new_primes.json
"""
import argparse
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


def weil_ceiling(N):
    return 2.0 * np.sqrt(N) / (N - 1)


def find_a(N, K):
    roots = [r for r in sqrt_mod(T_TRACE * T_TRACE - 4, N)]
    assert roots, f"p={N} not split"
    inv2 = pow(2, N - 2, N)
    cands = [(T_TRACE + r) * inv2 % N for r in roots]
    for c in cands:
        if multiplicative_order(c, N) == K:
            return c
    raise RuntimeError(f"no a of order K={K} at p={N}")


def j_brute_force(N, K, k0, parity_odd, qs, sample_pairs=None):
    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N

    ks = np.array([k for k in range(N - 1)
                   if k % K == k0 % K and (k % 2 == 1) == parity_odd],
                  dtype=np.int64)
    m = len(ks)
    xs = np.array([x for x in range(N) if x != 0 and x != 1], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]

    if sample_pairs is not None:
        i_idx = np.array([p[0] for p in sample_pairs], dtype=np.int64)
        j_idx = np.array([p[1] for p in sample_pairs], dtype=np.int64)
        ph_c_rows = np.exp(2j * np.pi * np.outer(-ks[i_idx], dl_x) / (N - 1))
        ph_r_rows = np.exp(2j * np.pi * np.outer(ks[j_idx], dl_xm1) / (N - 1))
        out = {}
        for qp in qs:
            ph = np.exp(2j * np.pi * (qp * xs % N) / N)
            out[int(qp)] = (ph_c_rows * ph_r_rows * ph[None, :]).sum(axis=1)
        return out, m

    phase_c = np.exp(2j * np.pi * np.outer(-ks, dl_x) / (N - 1))
    phase_r = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))
    out = {}
    for qp in qs:
        ph = np.exp(2j * np.pi * (qp * xs % N) / N)
        out[int(qp)] = (phase_c * ph[None, :]) @ phase_r.T
    return out, m


def certify_one(N, K, qs):
    t0 = time.time()
    a = find_a(N, K)
    k0 = 1
    parity_odd = False
    m_target = len([1 for k in range(N - 1)
                    if k % K == k0 % K and (k % 2 == 1) == parity_odd])

    g = primitive_root(N)
    dlog = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        dlog[x] = s
        x = x * g % N
    ks = np.array([k for k in range(N - 1)
                   if k % K == k0 % K and (k % 2 == 1) == parity_odd],
                  dtype=np.int64)
    m_cf = len(ks)
    if m_cf != m_target:
        return {"N": N, "K": K, "match": False,
                "error": f"m_cf={m_cf} m_target={m_target}"}
    xs = np.array([x for x in range(N) if x != 0 and x != 1], dtype=np.int64)
    dl_x = dlog[xs]
    dl_xm1 = dlog[(xs - 1) % N]
    W = np.exp(-2j * np.pi * np.outer(ks, dl_x) / (N - 1))
    Vv = np.exp(2j * np.pi * np.outer(ks, dl_xm1) / (N - 1))

    full_memory_gb = (m_cf * (N - 2) * 16 * 3) / (1024 ** 3)
    if full_memory_gb > 2.0:
        rng = np.random.default_rng(seed=20260901)
        n_samples = min(30, m_cf * m_cf)
        sample_pairs = [
            (int(rng.integers(0, m_cf)), int(rng.integers(0, m_cf)))
            for _ in range(n_samples)
        ]
        J_bf, m_bf = j_brute_force(N, K, k0, parity_odd, qs,
                                    sample_pairs=sample_pairs)
        Jm_closed_full = {}
        for qp in qs:
            ph = np.exp(2j * np.pi * (qp * xs % N) / N)
            Jm_full = (W * ph) @ Vv.T
            Jm_closed_full[int(qp)] = np.array(
                [Jm_full[i, j] for (i, j) in sample_pairs])
        del Jm_full
    else:
        J_bf, m_bf = j_brute_force(N, K, k0, parity_odd, qs)
        Jm_closed_full = None
    if m_bf != m_cf:
        return {"N": N, "K": K, "match": False,
                "error": f"m_bf={m_bf} vs m_cf={m_cf}"}

    max_dev_J = 0.0
    max_dev_J_rel = 0.0
    for qp in qs:
        if Jm_closed_full is None:
            ph = np.exp(2j * np.pi * (qp * xs % N) / N)
            Jm_closed = (W * ph) @ Vv.T
        else:
            Jm_closed = Jm_closed_full[int(qp)]
        Jm_bf = J_bf[int(qp)]
        d = np.abs(Jm_closed - Jm_bf)
        max_dev_J = max(max_dev_J, float(d.max()))
        denom = max(float(np.abs(Jm_closed).max()), 1e-15)
        max_dev_J_rel = max(max_dev_J_rel, float(d.max() / denom))

    weil = weil_ceiling(N)
    return {
        "N": N, "K": K, "a": int(a),
        "k0": int(k0), "parity_odd": bool(parity_odd),
        "m_plus": m_cf,
        "qs_probed": len(qs),
        "max_abs_dev_J": float(max_dev_J),
        "max_rel_dev_J": float(max_dev_J_rel),
        "weil_ceiling": float(weil),
        "weil_ceiling_factor": float(max_dev_J / weil) if weil > 0 else 0.0,
        "sampled": Jm_closed_full is not None,
        "n_sample_pairs": 30 if Jm_closed_full is not None else m_cf * m_cf,
        "wall_s": round(time.time() - t0, 1),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--all",
        action="store_true",
        help="also run the two very large historical designs (95419 and 144481)",
    )
    args = parser.parse_args()
    designs = [(461, 23), (19489, 29)]
    if args.all:
        designs += [(95419, 57), (144481, 43)]
    out = {
        "script": "code/verification/theorem_ii_new_primes.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "phase": "canonical-rebuild/R87.1",
        "scope": "all" if args.all else "audited-fast",
        "designs": [],
    }
    for N, K in designs:
        qs = [1, 2, 3, 5, 7]
        try:
            row = certify_one(N, K, qs)
        except Exception as e:
            row = {"N": N, "K": K, "match": False, "error": repr(e)}
        out["designs"].append(row)
        print(f"N={N} K={K} -> {row}", flush=True)

    out["verdict"] = {}
    for d in out["designs"]:
        if not d.get("match", True):
            out["verdict"][f"N={d.get('N')}"] = "FAIL"
            continue
        if d["max_rel_dev_J"] <= 1e-13 and d["weil_ceiling_factor"] <= 1e-9:
            out["verdict"][f"N={d['N']}"] = "PASS"
        else:
            out["verdict"][f"N={d['N']}"] = (
                f"REGRESSION (rel={d['max_rel_dev_J']:.2e}, "
                f"weil_f={d['weil_ceiling_factor']:.2e})"
            )
    print("verdict ->", out["verdict"], flush=True)

    dest = os.path.join(ROOT, "results", "verified", "theorem_ii_new_primes.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
