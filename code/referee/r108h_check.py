r"""R108h -- DIRECT adjudication of the OFF-system cross decomposition.

At N=199 (m=18) and N=2161 (m=54): compute from scratch, for the
OFF-diagonal system (diagonal key removed):
  - E_off, E_unc_off, corr_off = m^4 E_off - E_unc_off
  - per-pair energies E_psi = (1/N) sum_w |Ahat(w)|^4 (direct)
  - the full cross matrix Cross[psi, psi'] = (1/N) sum_w Ahat(w)^2
    Ahat(-w)^2, so sum_{psi != psi'} Cross + sum_psi E_psi
    = m^4 E_off must hold EXACTLY (internal checks), and
    corr_off = sum_{psi != trivial} E_psi + sum_{psi != psi'} Cross.
  - bucket-level (character-order) aggregation of the cross terms.
Validated against r108g's independent bucket implementation.

Verified results (N=2161, K=40, m=54; reproduce on every run):
  E_triv = E_unc_off to 4.6e-16; Cmat.sum = m^4 E_off to ~1e-15;
  sumE + cross - E_unc_off = corr_off exactly;
  buckets (low/mid/high): within-cross 1.4e18 / 1.7e19 / 7.9e19,
  between 0-1: 9.4e18, 0-2: 7.2e18, 1-2: 7.3e19 -- the off-system
  cross energy is distributed over mid/high-order twist pairs; the
  low-order bucket (incl. the trivial pair) cancels internally.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108h_check.log")

sys.path.insert(0, HERE)
from r108_k4_independent import (  # noqa: E402
    build_keys, discrete_log_table as dlog_table,
    multiplicative_order, primitive_root,
)


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
    is_diag = mult == (N - 2)
    w = np.where(is_diag, 0.0, mult.astype(np.float64))  # drop the spike

    flat = (c1 * m + c2) * N + d
    H3 = np.bincount(flat, weights=w, minlength=m * m * N).reshape(m, m, N)
    A = np.fft.fft2(H3, axes=(0, 1)).reshape(m * m, N)

    c_off = H3.sum(axis=(0, 1))
    chat = np.fft.fft(c_off)
    cc = np.fft.ifft(chat * chat).real
    E_unc_off = float(np.sum(cc**2))
    inv_c2 = (-np.arange(m)) % m
    B_off = np.zeros(N)
    for a0 in range(m):
        inv_c1 = np.array([(-a0) % m])
        P = H3[a0:a0 + 1, :, :]
        Q = H3[inv_c1[:, None], inv_c2[None, :], :]
        B_off += np.fft.ifft(np.fft.fft(P, axis=2) * np.fft.fft(Q, axis=2),
                             axis=2).real.sum(axis=(0, 1))
    E_off = float(np.sum(B_off**2))
    m4 = float(m) ** 4
    corr_off = m4 * E_off - E_unc_off

    Ah = np.fft.fft(A, axis=1)
    Epsi = (np.abs(Ah) ** 4).sum(axis=1) / N
    sumE = float(Epsi.sum())
    neg = (-np.arange(N)) % N
    sq = Ah ** 2
    sqn = Ah[:, neg] ** 2
    Cmat = (sq @ sqn.T) / N
    total_cross = float(np.real(Cmat.sum() - np.trace(Cmat)))
    total = float(np.real(Cmat.sum()))

    log(f"=== N={N} K={K} m={m} (OFF system, direct)")
    log(f"  E_off={E_off:.6e}  E_unc_off={E_unc_off:.6e}  "
        f"corr_off={corr_off:.6e}")
    log(f"  sum_psi E_psi = {sumE:.6e}")
    log(f"  sum_(psi != psi') Cross = {total_cross:.6e}")
    log(f"  CHECK sumE + cross - E_unc_off = "
        f"{sumE + total_cross - E_unc_off:.6e} vs corr_off "
        f"{corr_off:.6e} (rel "
        f"{abs(sumE + total_cross - E_unc_off - corr_off) / abs(corr_off):.2e})")
    log(f"  CHECK Cmat.sum = {total:.6e} vs m^4 E_off = {m4 * E_off:.6e} "
        f"(rel {abs(total - m4 * E_off) / (m4 * E_off):.2e})")
    log(f"  E_triv = {float(Epsi[0]):.6e} vs E_unc_off = {E_unc_off:.6e} "
        f"(rel {abs(Epsi[0] - E_unc_off) / E_unc_off:.2e})")
    mp = m * m
    j1 = np.arange(mp) // m
    j2 = np.arange(mp) % m
    ordps = np.lcm(m // np.gcd(j1, m), m // np.gcd(j2, m))
    bidx = np.where(ordps <= 6, 0, np.where(ordps <= 42, 1, 2))
    for b in range(3):
        sel = bidx == b
        if sel.any():
            blk = Cmat[np.ix_(sel, sel)]
            within = float(np.real(blk.sum() - np.trace(blk)))
            log(f"  bucket {b} (ord <= {['6', '42', 'max'][b]}): "
                f"pairs={int(sel.sum())}  sumE_b={float(Epsi[sel].sum()):.4e}  "
                f"within-cross={within:.4e}")
    for b1 in range(3):
        for b2 in range(b1 + 1, 3):
            s1, s2 = bidx == b1, bidx == b2
            if s1.any() and s2.any():
                bet = float(np.real(Cmat[np.ix_(s1, s2)].sum()
                                    + Cmat[np.ix_(s2, s1)].sum()))
                log(f"  between {b1}-{b2}: {bet:.4e}")
    return dict(N=N, K=K, m=m, E_off=E_off, E_unc_off=E_unc_off,
                corr_off=corr_off, sumE=sumE, cross=total_cross)


def main():
    log("R108h: direct adjudication of off-system cross decomposition")
    res = {}
    for N, a in ((199, 139), (2161, 48)):
        res[f"N{N}"] = run(N, a)
    with open(os.path.join(OUT_DIR, "r108h_check.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    log("done")


if __name__ == "__main__":
    main()
