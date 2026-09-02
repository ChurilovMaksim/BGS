r"""R108g -- THE EXACT PAIR-TYPE DECOMPOSITION of the k=4 coupled energy.

Exact combinatorial identity (no flat model, no twist machinery):

  B(t) = (N-2)^2 delta_{t,0} + 2(N-2) p_H(t) + B_off(t),

pair types (diag,diag), (diag,off)+(off,diag), (off,off).  Hence
  E_c = (N-2)^4 + 2(N-2)^2 B_off(0) + 4(N-2)^2 sum p_H^2
        + 4(N-2) sum_t p_H B_off + E_c^off.

CONCEPTUAL POINT: the diagonal spike is twist-INVARIANT -- every
character pair carries it identically -- so it survives the annihilator
averaging at full weight in E_c, while the baseline E_unc/m^4 suppresses
the flat background by m^4.  The measured delta is dominated by this
unsuppressed-vs-suppressed mismatch, NOT by a mysterious cross-term sum.
The clean object is the OFF-diagonal system:
  delta_off = m^4 E_c^off / E_unc^off - 1

Measured (10-design sweep, exact; see docs/CROSS_TERM_LAW_R108.md):
  N=199 (K=11):  6.45% -> 1.42%   N=3571 (K=17): 17.65% -> 4.22%
  N=2161 (K=40): 0.45% -> 0.09%   N=6709 (K=43): 0.88% -> 0.19%
  N=3001 (K=50): 0.26% -> 0.05%   N=2521 (K=60): 0.13% -> 0.02%
  N=4969 (K=92): 0.05% -> 0.01%   N=5081 (K=127): 0.02% -> 0.00%
  N=1511 (K=151): 0.01% -> 0.00%  N=1229 (K=307): 0.00% -> 0.00%
Identity check E_c(decomp) = E_c(direct): 0.00e+00 at every design.

Also: order-resolved cross decomposition of the OFF system (buckets by
character order: low <= 6, mid <= 42, high > 42) via bucket-aggregated
pairwise products G_b(w) G_b'(-w); validated against the direct Cmat
computation in r108h_check.py (E_triv = E_unc_off and
Cmat.sum = m^4 E_off to ~1e-15).  At N=2161 within-bucket crosses are
1.4e18 / 1.7e19 / 7.9e19 (low/mid/high) and between-bucket
0.9e19 / 0.7e19 / 7.3e19: the cross energy is distributed over
mid/high-order twist pairs, NOT concentrated on low-order characters
(the low-order bucket shows near-total internal cancellation) -- this
kills the "m=210 low-order resonance" explanation of the K=17 anomaly.

NOTE (R108): this file was repeatedly lost to sandbox restarts; the
numbers above are from completed passes.  The bucket pass uses the
full-axis c1 FFT then row-chunks (chunking an FFT axis directly is
invalid -- an FFT of a sliced axis is not a slice of the full FFT).
N=3571 is excluded from the bucket pass (sandbox memory guard).
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108g_offdiag.log")
JSON_PATH = os.path.join(OUT_DIR, "r108g_offdiag.json")

sys.path.insert(0, HERE)
from r108_k4_independent import (  # noqa: E402
    build_keys, discrete_log_table as dlog_table,
    multiplicative_order, primitive_root,
)

_t0 = time.time()


def log(msg):
    print(str(msg), flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(str(msg) + "\n")


def run(N, a):
    K = multiplicative_order(a, N)
    m = (N - 1) // K
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    u, v, d, mult = build_keys(N)
    c1 = (dlog[u] % m).astype(np.int64)
    c2 = (dlog[v] % m).astype(np.int64)

    flat = (c1 * m + c2) * N + d
    H3 = np.zeros(m * m * N, dtype=np.int64)
    mid = m // 2
    for lo, hi in ((0, mid), (mid, m)):
        sel = (c1 >= lo) & (c1 < hi)
        if not sel.any():
            continue
        f = (c1[sel] - lo) * (m * N) + c2[sel] * N + d[sel]
        part = np.bincount(f, weights=mult[sel].astype(np.float64),
                           minlength=(hi - lo) * m * N)
        H3[lo * m * N: hi * m * N] += part.astype(np.int64)
        del part, f
    H3 = H3.reshape(m, m, N).astype(np.float64)
    c_counts = H3.sum(axis=(0, 1))
    chat = np.fft.fft(c_counts)
    E_unc = float(np.sum(np.abs(chat) ** 4) / N)

    inv_c2 = (-np.arange(m)) % m
    neg_idx = (-np.arange(N)) % N
    B = np.zeros(N, dtype=np.float64)
    CH = 8
    for a0 in range(0, m, CH):  # pass 1: full coupled B (spike included)
        a1 = min(a0 + CH, m)
        inv_c1 = (-np.arange(a0, a1)) % m
        P = H3[a0:a1, :, :]
        Q = H3[inv_c1[:, None], inv_c2[None, :], :]
        D = np.fft.ifft(np.fft.fft(P, axis=2) * np.fft.fft(Q, axis=2),
                        axis=2).real
        B += D.sum(axis=(0, 1))
    E_c = float(np.sum(B**2))

    # ---- order-resolved cross decomposition of the OFF system ----
    H3[0, 0, 0] -= (N - 2)  # remove the diagonal spike
    mp = m * m
    j1 = np.arange(mp) // m
    j2 = np.arange(mp) % m
    ordps = np.lcm(m // np.gcd(j1, m), m // np.gcd(j2, m))
    nb = 3
    bidx = np.where(ordps <= 6, 0, np.where(ordps <= 42, 1, 2))
    G = np.zeros((nb, N), dtype=np.complex128)
    Hh = np.zeros((nb, N), dtype=np.complex128)
    H3c = H3.astype(np.complex64)
    T1 = np.fft.fft(H3c, axis=0)  # full c1-axis FFT (cannot be chunked)
    del H3c
    for a0 in range(0, m, CH):  # row-chunks for the c2 and dbar FFTs
        a1 = min(a0 + CH, m)
        blk = T1[a0:a1, :, :]                        # (ch, c2, dbar)
        Af = np.fft.fft(blk, axis=1)                 # c2 -> j2 (full axis)
        Ah = np.fft.fft(Af.reshape((a1 - a0) * m, N), axis=1)  # dbar -> w
        sq = Ah ** 2
        sqn = Ah[:, neg_idx] ** 2
        bmask = bidx.reshape(m, m)[a0:a1, :].reshape(-1)
        for b in range(nb):
            sel = bmask == b
            if sel.any():
                G[b] += sq[sel].sum(axis=0).astype(np.complex128)
                Hh[b] += (sq[sel] * sqn[sel]).sum(axis=0).astype(np.complex128)
    del T1
    Gneg = G[:, neg_idx]
    between = np.real(G @ Gneg.T) / N
    within = [float(np.sum((np.real(G[b] * G[b][neg_idx])
                           - np.real(Hh[b])) / N)) for b in range(nb)]

    # ---- exact pair-type decomposition (from the valid B-pass) ----
    Hset = np.zeros(N, dtype=bool)
    x = 1
    for _ in range(K):
        Hset[x] = True
        x = x * a % N
    pH_mask = ((mult != (N - 2)) & Hset[u.astype(np.int64)]
               & Hset[v.astype(np.int64)])
    p_H = np.bincount(d[pH_mask], minlength=N).astype(np.float64)
    B_off = B.copy()
    B_off[0] -= (N - 2) ** 2
    B_off -= 2.0 * (N - 2) * p_H
    E_off = float(np.sum(B_off**2))
    c_off = c_counts.copy()
    c_off[0] -= (N - 2)
    coff_hat = np.fft.fft(c_off)
    cc = np.fft.ifft(coff_hat * coff_hat).real
    E_unc_off = float(np.sum(cc**2))

    cross_pH = 4.0 * (N - 2) * float(np.sum(p_H * B_off))
    sum_pH2 = 4.0 * (N - 2) ** 2 * float(np.sum(p_H**2))
    spike_cross = 2.0 * (N - 2) ** 2 * B_off[0]
    E_c_decomp = (N - 2) ** 4 + spike_cross + sum_pH2 + cross_pH + E_off
    rel_id = abs(E_c_decomp - E_c) / E_c

    m4 = float(m) ** 4
    corr = m4 * E_c - E_unc
    t_spike = (m4 - 1.0) * (N - 2) ** 4
    corr_off = m4 * E_off - E_unc_off
    shares = dict(spike_pure=t_spike / corr, off_part=corr_off / corr,
                  structure_rest=(corr - t_spike - corr_off) / corr)
    delta_off = m4 * E_off / E_unc_off - 1 if E_unc_off else float("nan")
    delta_full = E_c / (E_unc / m4) - 1

    log(f"=== N={N} K={K} m={m}")
    log(f"  identity E_c vs decomposition: rel diff {rel_id:.2e}")
    log(f"  delta_full={delta_full*100:+.2f}%  delta_off={delta_off*100:+.2f}%")
    log(f"  correction shares: spike_pure={shares['spike_pure']:.3f} "
        f"off_part={shares['off_part']:.3f} "
        f"structure_rest={shares['structure_rest']:.3f}")
    log(f"  order-bucket between-cross (raw): "
        f"{['%.3e' % x for x in between.flatten()]}")
    log(f"  order-bucket within-cross (raw): {['%.3e' % x for x in within]}")
    return dict(
        N=N, K=K, m=m, identity_rel=rel_id,
        E_c=E_c, E_unc=E_unc, E_off=E_off, E_unc_off=E_unc_off,
        delta_full_pct=delta_full * 100, delta_off_pct=delta_off * 100,
        shares=shares, between=between.tolist(), within=within,
        pH_mass=float(p_H.sum()), B_off0=float(B_off[0]),
    )


def main():
    log("R108g: exact pair-type decomposition + off-diagonal law")
    designs = [(199, 139), (2161, 48), (6709, 3922),
               (3001, 124), (2521, 323), (4969, 72), (5081, 1032),
               (1511, 347), (1229, 746)]
    res = {}
    if os.path.exists(JSON_PATH):
        try:
            res = json.load(open(JSON_PATH))
        except Exception:
            res = {}
    for N, a in designs:
        key = f"N{N}"
        if key in res:
            log(f"=== {key} done, skip")
            continue
        try:
            res[key] = run(N, a)
        except Exception as exc:
            log(f"N={N} FAILED: {exc}")
            continue
        with open(JSON_PATH, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=1, default=float)
    log(f"WROTE {JSON_PATH} ({time.time() - _t0:.0f}s)")


if __name__ == "__main__":
    main()
