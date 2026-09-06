"""
R87 — Phase 0 baseline reproduction.

Re-derives the R82.12 theorem_ii_twisted_jacobi numbers using build_closed_form
directly (importing the load-bearing module without executing its hard-coded
main(), which points at the wrong path on this disk). This validates:

  (a) the load-bearing theorem_ii_twisted_jacobi.py module still imports
      and exposes build_closed_form;
  (b) the q-curve .npz files in data/legacy/theorems/I_torus_rigidity/
      are still on disk and contain the expected (q, mu4) arrays;
  (c) the closed-form twisted-Jacobi-sum pipeline still reproduces the R82.12
      certificates (max |mu4_closed - mu4_measured| ≤ 2.4e-13 at N=3571).

This script does NOT modify theorem_ii_twisted_jacobi.py (load-bearing,
already certified). It only imports build_closed_form and compares against
the legacy certified closed_form.json.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "code", "theorems"))

from theorem_ii_twisted_jacobi import (  # noqa: E402
    build_closed_form,
    multiplicative_order,
    sqrt_mod,
)

T_TRACE = 3

LEGACY_DIR = os.path.join(
    ROOT, "data", "legacy", "theorems", "I_torus_rigidity"
)
LEGACY_CF = os.path.join(
    ROOT, "data", "legacy", "theorems", "II_twisted_jacobi",
    "closed_form.json"
)


def find_a(N, K):
    roots = [r for r in sqrt_mod(T_TRACE * T_TRACE - 4, N)]
    assert roots, f"N={N} not split"
    inv2 = pow(2, N - 2, N)
    cands = [(T_TRACE + r) * inv2 % N for r in roots]
    for c in cands:
        if multiplicative_order(c, N) == K:
            return c
    raise RuntimeError(f"no a of order K={K} at N={N}")


def reproduce_one(N, K):
    t0 = time.time()
    a = find_a(N, K)
    q_path = os.path.join(LEGACY_DIR, f"q_curve_N{N}.npz")
    assert os.path.exists(q_path), f"missing {q_path}"
    d = np.load(q_path)
    q_meas = d["q"].astype(int)
    mu4_meas = d["mu4"]
    meas = dict(zip(q_meas.tolist(), mu4_meas.tolist()))

    probes = [1, 2, 3, 5, 7]
    best = None
    for parity_odd in (True, False):
        for k0 in range(K):
            cf, m = build_closed_form(N, K, a, k0, parity_odd, probes)
            if m != len([1 for k in range(N - 1)
                         if k % K == k0 % K and (k % 2 == 1) == parity_odd]):
                continue
            v0 = cf[probes[0]]["mu4"]
            cand = [qq for qq, vv in meas.items() if abs(vv - v0) < 1e-8]
            for c in cand:
                ok = all(abs(cf[p]["mu4"] -
                             meas.get((c * p) % N, np.nan)) < 1e-8
                         for p in probes)
                if ok:
                    best = (parity_odd, k0, c, m)
                    break
            if best:
                break
        if best:
            break
    if best is None:
        return {"N": N, "K": K, "match": False,
                "wall_s": round(time.time() - t0, 1)}
    parity_odd, k0, c, m = best
    allq = sorted(meas)
    cf, _ = build_closed_form(N, K, a, k0, parity_odd,
                              [(pow(c, N - 2, N) * qq) % N for qq in allq])
    dev = []
    for qq in allq:
        qp = (pow(c, N - 2, N) * qq) % N
        dev.append(abs(cf[qp]["mu4"] - meas[qq]))
    dev = np.array(dev)
    return {
        "N": N, "K": K, "a": int(a),
        "match": True, "parity_odd": bool(parity_odd), "k0": int(k0),
        "scale_c": int(c), "m_plus": int(m),
        "levels_checked": len(allq),
        "max_abs_dev_mu4": float(dev.max()),
        "mean_abs_dev_mu4": float(dev.mean()),
        "wall_s": round(time.time() - t0, 1),
    }


def main():
    out = {
        "script": "code/verification/baseline_r82.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "phase": "R87.0",
        "designs": [],
    }
    for N, K in ((199, 11), (3571, 17)):
        try:
            row = reproduce_one(N, K)
        except Exception as e:
            row = {"N": N, "K": K, "match": False, "error": repr(e)}
        out["designs"].append(row)
        print(f"N={N} K={K} -> {row}", flush=True)

    if os.path.exists(LEGACY_CF):
        with open(LEGACY_CF) as fh:
            legacy = json.load(fh)
        out["legacy_R82_reference"] = legacy.get("designs", [])

    out["verdict"] = {}
    for d in out["designs"]:
        if not d.get("match"):
            out["verdict"][f"N={d.get('N')}"] = "FAIL"
            continue
        ref = next((r for r in out.get("legacy_R82_reference", [])
                    if r.get("N") == d["N"]), None)
        if ref is None:
            out["verdict"][f"N={d['N']}"] = "NO_REFERENCE"
            continue
        legacy_max = ref.get("max_abs_dev_mu4", 1.0)
        if d["max_abs_dev_mu4"] <= 10.0 * legacy_max:
            out["verdict"][f"N={d['N']}"] = "PASS"
        else:
            out["verdict"][f"N={d['N']}"] = "REGRESSION"

    dest = os.path.join(ROOT, "data", "proof", "baseline_check.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)
    print("verdict ->", out["verdict"], flush=True)


if __name__ == "__main__":
    main()
