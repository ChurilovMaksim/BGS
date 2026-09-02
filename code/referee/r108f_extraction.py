r"""R108f -- THE (H,H)-STRATUM EXTRACTION TEST.

Hypothesis from r108e: the k=4 coupled-energy correction delta is
dominated by the non-flat structure of the H x H stratum (coset (0,0):
the diagonal key spike of mass N-2 at d=0 plus (K-1)(K-2) off-diagonal
H-keys), which carries only ~0.03% of the key mass but ~76-100% of the
deviation from the flat model.

Test: replace the (0,0)-stratum profile P_00 by its FLATTENED version
(same mass, spread uniformly over dbar), recompute
  E_c'  = sum_t B'(t)^2,  B' = B - (P_00 * P_00) + (P'_00 * P'_00),
  E_unc' from c' = c - P_00 + P'_00,
and report delta' = E_c'/(E_unc'/m^4) - 1.  Variants:
  V0: true delta (reference);
  V1: flatten the whole (0,0) stratum;
  V2: flatten only the diagonal key (remove the d=0 spike of mass N-2,
      spread it uniformly);
  V3: V1 + also flatten all (c,-c) strata (uv in H family).

If delta' is much smaller than delta, the honest decomposition
  E_c = E_flat + E_(H,H)-explicit + small remainder
is the corrected theorem route: the explicit part is closed-form
(O(K^2+N) data), and only the remainder needs a genuine estimate.
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108f_extraction.log")
JSON_PATH = os.path.join(OUT_DIR, "r108f_extraction.json")

sys.path.insert(0, HERE)
from r108_k4_independent import (  # noqa: E402
    build_keys, discrete_log_table as dlog_table,
    multiplicative_order, primitive_root,
)


def log(msg):
    print(str(msg), flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(str(msg) + "\n")


def conv_self(P):
    F = np.fft.fft(P)
    return np.fft.ifft(F * F).real


def run(N, a):
    K = multiplicative_order(a, N)
    m = (N - 1) // K
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    u, v, d, mult = build_keys(N)
    c1 = (dlog[u] % m).astype(np.int64)
    c2 = (dlog[v] % m).astype(np.int64)

    flat_idx = (c1 * m + c2) * N + d
    H3 = np.bincount(
        flat_idx, weights=mult.astype(np.float64), minlength=m * m * N
    ).reshape(m, m, N)
    del flat_idx
    inv_c2 = (-np.arange(m)) % m
    c1g = np.arange(m)[:, None] * np.ones((1, m), dtype=np.int64)
    c2g = np.arange(m)[None, :] * np.ones((m, 1), dtype=np.int64)
    cc_minus = (c1g + c2g) % m == 0  # (c,-c) family: uv in H

    def full_B(H3x):
        B = np.zeros(N, dtype=np.float64)
        CH = 8
        for a0 in range(0, m, CH):
            a1 = min(a0 + CH, m)
            inv_c1 = (-np.arange(a0, a1)) % m
            P = H3x[a0:a1, :, :]
            Q = H3x[inv_c1[:, None], inv_c2[None, :], :]
            D = np.fft.ifft(np.fft.fft(P, axis=2)
                            * np.fft.fft(Q, axis=2), axis=2).real
            B += D.sum(axis=(0, 1))
        return B

    def energy(H3x):
        c = H3x.sum(axis=(0, 1))
        chat = np.fft.fft(c)
        E_unc = float(np.sum(np.abs(chat) ** 4) / N)
        B = full_B(H3x)
        E_c = float(np.sum(B**2))
        return E_c, E_unc, B

    E_c, E_unc, B = energy(H3)
    delta0 = E_c / (E_unc / m**4) - 1
    log(f"=== N={N} K={K} m={m}: delta(V0 true) = {delta0*100:+.2f}%")

    results = dict(N=N, K=K, m=m, delta0_pct=delta0 * 100)

    P00 = H3[0, 0, :].copy()
    mass00 = float(P00.sum())
    # V1: flatten the whole (0,0) stratum
    H3v = H3.copy()
    H3v[0, 0, :] = mass00 / N
    E_c1, E_unc1, _ = energy(H3v)
    d1 = E_c1 / (E_unc1 / m**4) - 1
    log(f"  V1 flatten (0,0) stratum:      delta = {d1*100:+.2f}%")
    results["deltaV1_pct"] = d1 * 100

    # V2: flatten only the diagonal key spike at d=0
    diag_mass = float(P00[0]) - 0.0  # P00[0] includes diag + H-offdiag at 0
    # the diagonal key mass is N-2 by construction; H-offdiag keys never
    # sit at d=0, so P00[0] = N-2 exactly
    H3v = H3.copy()
    H3v[0, 0, 0] = 0.0
    H3v[0, 0, :] += diag_mass / N
    E_c2, E_unc2, _ = energy(H3v)
    d2 = E_c2 / (E_unc2 / m**4) - 1
    log(f"  V2 flatten diagonal spike only: delta = {d2*100:+.2f}%")
    results["deltaV2_pct"] = d2 * 100

    # V3: V1 + flatten all (c,-c) strata
    H3v = H3.copy()
    H3v[0, 0, :] = mass00 / N
    for i in range(m):
        j = (-i) % m
        if i == 0 and j == 0:
            continue
        massij = float(H3[i, j, :].sum())
        H3v[i, j, :] = massij / N
    E_c3, E_unc3, _ = energy(H3v)
    d3 = E_c3 / (E_unc3 / m**4) - 1
    log(f"  V3 V1 + flatten (c,-c) family:  delta = {d3*100:+.2f}%")
    results["deltaV3_pct"] = d3 * 100
    results["mass00"] = mass00
    return results


def main():
    log("R108f: (H,H)-stratum extraction test")
    res = {}
    for N, a in ((199, 139), (3571, 2469), (2161, 48), (6709, 3922),
                 (5081, 1032), (1229, 746)):
        try:
            res[f"N{N}"] = run(N, a)
        except Exception as exc:
            log(f"N={N} FAILED: {exc}")
    with open(JSON_PATH, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=float)
    log(f"WROTE {JSON_PATH}")


if __name__ == "__main__":
    main()
