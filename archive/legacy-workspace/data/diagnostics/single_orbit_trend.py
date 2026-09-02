"""
PRIORITY 1 (op:local_deterministic).  Does a FIXED low-complexity observable
give Wigner-Dyson statistics for the cat-map compression, and does the deviation
shrink as the multiplet grows?

For each design point (A, p) with small torsion K (hence large multiplet
m ~ N/K) we compress a SINGLE Weyl operator onto the eigenspace, measure the L1
distance of the unfolded nearest-neighbour spacings to the beta=1 curve, and
convert it to a z-score against size-matched true GOE controls run through the
identical pipeline.  The question is the sign and trend of

        z(m) = ( L1_GOE(single orbit) - mean L1_GOE(GOE control) ) / sd(control)

If z(m) -> 0 the deterministic BGS statement is plausible; if z(m) grows the
single-orbit family is NOT in the GOE class.
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import (                       # noqa: E402
    CatMap, L1_to, reference_L1, unfolded_spacings,
)
from compression_spacings import EDGES, eigen_basis, orbit_reps  # noqa: E402


def small_torsion_designs(A, pmax, kmax, mmin):
    """primes p <= pmax with projective order of A at most kmax and m >= mmin."""
    out = []
    A = np.array(A, dtype=np.int64)
    I = np.eye(2, dtype=np.int64)
    sieve = np.ones(pmax + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(pmax ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    for p in np.flatnonzero(sieve):
        p = int(p)
        if p < 41 or p % 2 == 0:
            continue
        if math.gcd(int(A[1, 0]) % p, p) != 1:
            continue
        M = A % p
        K = None
        for j in range(1, kmax + 1):
            if np.array_equal(M % p, I):
                K = j
                break
            if np.array_equal(M % p, (-I) % p):
                K = 2 * j
                break
            M = M @ A % p
        if K is None:
            continue
        m = p // K
        if m >= mmin:
            out.append((p, K, m))
    return out


def main():
    rng = np.random.default_rng(987654321)
    A = [[2, 1], [1, 1]]
    designs = small_torsion_designs(A, 30000, 60, 90)
    designs.sort(key=lambda t: t[2])
    # keep a spread in m, and cap the largest for memory
    keep = []
    seen = set()
    for p, K, m in designs:
        b = int(math.log2(max(m, 2)) * 2)
        if b in seen or m > 700:
            continue
        seen.add(b)
        keep.append((p, K, m))
    print("design points (p, K, m_pred):", keep)
    sys.stdout.flush()

    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "A": A, "rows": []}
    for p, Kp, mp in keep:
        t0 = time.time()
        cm = CatMap(A, p)
        ordA, K = cm.orders()
        batch = min(int(mp * 1.6) + 40, 1000)
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        if m < 40:
            print(f"  p={p}: m={m} too small, skip")
            continue
        nrep = 24 if m <= 300 else 10
        refs = {k: reference_L1(k, m, nrep, EDGES, rng)
                for k in ("GOE", "GUE", "Poisson")}
        mu, sd = refs["GOE"]
        reps = orbit_reps(cm, K, 8, rng)
        zs, l1s = [], []
        for u in reps:
            Mo = cm.apply_T(u, B)
            H = B.conj().T @ Mo
            H = H + H.conj().T
            ev = np.linalg.eigvalsh(H)
            s = unfolded_spacings(ev)
            l1 = L1_to(s, 1, EDGES)
            l1s.append(l1)
            zs.append((l1 - mu[0]) / sd[0])
        zs = np.array(zs)
        row = {"p": p, "K": K, "m": m, "proj_res": res,
               "n_orbits": len(reps), "control_reps": nrep,
               "control_GOE_mean": float(mu[0]), "control_GOE_sd": float(sd[0]),
               "L1_single_orbit": [float(x) for x in l1s],
               "z_mean": float(zs.mean()),
               "z_sem": float(zs.std(ddof=1) / math.sqrt(len(zs))),
               "z_min": float(zs.min()), "z_max": float(zs.max()),
               "secs": round(time.time() - t0, 1)}
        out["rows"].append(row)
        print(f"  p={p:>6} K={K:>3} m={m:>4}: control GOE {mu[0]:.4f}+-{sd[0]:.4f}"
              f"   single-orbit L1 mean {np.mean(l1s):.4f}"
              f"   z = {zs.mean():+.2f} +- {row['z_sem']:.2f}"
              f"  [range {zs.min():+.2f},{zs.max():+.2f}]  {row['secs']}s")
        sys.stdout.flush()

    # trend
    if len(out["rows"]) >= 3:
        ms = np.array([r["m"] for r in out["rows"]], dtype=float)
        zz = np.array([r["z_mean"] for r in out["rows"]])
        w = np.array([1.0 / max(r["z_sem"], 1e-3) ** 2 for r in out["rows"]])
        sl, ic = np.polyfit(np.log(ms), zz, 1, w=np.sqrt(w))
        out["trend"] = {"z_vs_log_m_slope": float(sl), "intercept": float(ic)}
        print(f"\nweighted fit  z = {sl:+.3f} * log m + {ic:+.3f}")
        print("  slope > 0  => deviation GROWS with multiplet size "
              "(single orbit not in the GOE class)")
        print("  slope < 0  => deviation shrinks (deterministic BGS plausible)")

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r71", "single_orbit_trend.json")
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
