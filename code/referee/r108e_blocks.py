r"""R108e -- WHERE DOES THE CROSS TERM LIVE?  Block decomposition of the
coupled energy by coset-stratum type.

B(t) = sum_{e in (G/H)^2} (P_e * P_{e-bar})(t),  e-bar = (-c1, -c2),
where P_e(dbar) = weighted key mass in stratum e at difference dbar
(H3[c1, c2, dbar]).

Blocks: strata are grouped by the inversion-stable flags
  f1: c1 == 0   (u in H)
  f2: c2 == 0   (v in H)
  f3: c1 == c2  (u and v in the same H-coset)
giving 8 blocks beta, each closed under inversion, so
  B = sum_beta (Pb_beta * Pb_beta),  Pb_beta = sum_{e in beta} P_e,
and
  E_c = sum_beta E_beta + sum_{beta != beta'} Cross_beta beta',
  E_beta = sum_t (Pb_b * Pb_b)^2,  Cross_bb' = sum_t C_b C_b'.

Output: the 8x8 block matrix, each block's share of
(m^4 E_c - E_unc), per-stratum flat-deviation top list, and the
sweep-context numbers.  Designs: N=3571 (the delta=+17.65% outlier)
and N=199 (delta=+6.45%) for contrast.
"""
import json
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108e_blocks.log")
JSON_PATH = os.path.join(OUT_DIR, "r108e_blocks.json")

sys.path.insert(0, HERE)
from r108_k4_independent import (  # noqa: E402
    build_keys, discrete_log_table as dlog_table,
    multiplicative_order, primitive_root,
)


def log(msg):
    print(str(msg), flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(str(msg) + "\n")


def block_index(c1, c2, m):
    f1 = (c1 == 0).astype(np.int64)
    f2 = (c2 == 0).astype(np.int64)
    f3 = (c1 == c2).astype(np.int64)
    return f1 * 4 + f2 * 2 + f3  # 0..7


def run(N, a):
    K = multiplicative_order(a, N)
    m = (N - 1) // K
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    u, v, d, mult = build_keys(N)
    c1 = (dlog[u] % m).astype(np.int32)
    c2 = (dlog[v] % m).astype(np.int32)
    blk = block_index(c1, c2, m)

    # stratum histogram H3[c1, c2, dbar] (weighted), int64->float path
    flat_idx = (c1.astype(np.int64) * m + c2) * N + d
    H3 = np.bincount(
        flat_idx, weights=mult.astype(np.float64), minlength=m * m * N
    ).reshape(m, m, N)
    del flat_idx
    c_counts = H3.sum(axis=(0, 1))
    chat = np.fft.fft(c_counts)
    E_unc = float(np.sum(np.abs(chat) ** 4) / N)

    # B = sum_e (P_e * P_ebar), ebar = (-c1, -c2) mod m.  Aggregate by
    # block: B_b(t) = sum_{e in block b} (P_e * P_ebar)(t).  (Direct
    # block-profile convolutions would spuriously pair e with the
    # inverse of a different stratum in the same block -- R108e bug fix.)
    Bblk = np.zeros((8, N), dtype=np.float64)
    inv_c2 = (-np.arange(m)) % m
    c1g = np.arange(m)[:, None] * np.ones((1, m), dtype=np.int64)
    c2g = np.arange(m)[None, :] * np.ones((m, 1), dtype=np.int64)
    bb_all = block_index(c1g, c2g, m)
    CH = 8  # c1-chunk
    for a0 in range(0, m, CH):
        a1 = min(a0 + CH, m)
        inv_c1 = (-np.arange(a0, a1)) % m
        P = H3[a0:a1, :, :]                        # (ch, m, N)
        Q = H3[inv_c1[:, None], inv_c2[None, :], :]  # P_ebar, aligned
        D = np.fft.ifft(np.fft.fft(P, axis=2)
                        * np.fft.fft(Q, axis=2), axis=2).real
        Db = D.reshape((a1 - a0) * m, N)
        bmask = bb_all[a0:a1, :].reshape(-1)
        for b in range(8):
            sel = bmask == b
            if sel.any():
                Bblk[b] += Db[sel].sum(axis=0)
    B = Bblk.sum(axis=0)
    E_c = float(np.sum(B**2))
    delta = E_c / (E_unc / (m**4)) - 1

    E2 = Bblk @ Bblk.T  # E2[b,b'] = sum_t B_b(t) B_b'(t)
    total_corr = m**4 * E_c - E_unc
    log(f"=== N={N} K={K} m={m}: E_c={E_c:.6e}, delta={delta*100:+.2f}% "
        f"(m^4 E_c - E_unc = {total_corr:.4e})")
    names = []
    for b in range(8):
        f1, r = divmod(b, 4)
        f2, f3 = divmod(r, 2)
        names.append(f"uH={f1}vH={f2}same={f3}")
    mass = np.array([H3[bb_all == b].sum() for b in range(8)])
    log("block masses (key mass per block):")
    for b in range(8):
        log(f"  {names[b]:20s} mass={mass[b]:12.0f} "
            f"E2diag={E2[b, b]:.4e}")
    diag_sum = float(np.trace(E2))
    off_sum = float(E2.sum() - np.trace(E2))
    log(f"block-diag total {diag_sum:.6e} (=E_c), block-cross total "
        f"{off_sum:.4e}, E_unc {E_unc:.4e}")
    log("cross-block matrix (sum_t B_b B_b', absolute):")
    for b in range(8):
        row = " ".join(f"{E2[b, bp]:12.4e}" for bp in range(8))
        log(f"  {names[b]:20s} {row}")
    # top non-flat strata by L2 deviation from the flat per-cell mass
    flat_cell = ((N - 2) ** 2) / (m * m * N)
    flat_prof = np.full(N, flat_cell)
    per_stratum = None
    if m * m <= 40000:
        stratum_l2 = np.sqrt(((H3 - flat_prof) ** 2).sum(axis=2))
        top = np.dstack(np.unravel_index(
            np.argsort(stratum_l2.ravel())[::-1][:6], stratum_l2.shape))[0]
        per_stratum = [
            (int(x), int(y), float(stratum_l2[x, y])) for x, y in top
        ]
        log("top non-flat strata (c1, c2, L2 dev from flat):")
        for x, y, dev in per_stratum:
            log(f"  ({x:4d},{y:4d})  {dev:.3e}")
    del H3
    out = dict(
        N=N, K=K, m=m, E_c=E_c, E_unc=E_unc, delta_pct=delta * 100,
        block_names=names, block_mass=mass.tolist(),
        E2=E2.tolist(), diag_sum=diag_sum, off_sum=off_sum,
        per_stratum=per_stratum,
    )
    return out


def main():
    log("R108e: block decomposition of the coupled-energy correction")
    res = {}
    for N, a in ((199, 139), (3571, 2469)):
        try:
            res[f"N{N}"] = run(N, a)
        except Exception as exc:
            log(f"N={N} FAILED: {exc}")
    with open(JSON_PATH, "w", encoding="utf-8") as fh:
        json.dump(res, fh, indent=1, default=float)
    log(f"WROTE {JSON_PATH}")


if __name__ == "__main__":
    main()
