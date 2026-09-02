r"""R108k -- THE COLLECTIVE-FIELD COLLAPSE OF THE CROSS TERMS (exact identity).

Exact algebra (no approximation):
  Cmat[p,p'] = (1/N) sum_w Y_p(w) conj(Y_p'(w)),  Y_p(w) := Ahat_p(w)^2
  (A_p real => Ahat(-w) = conj(Ahat(w))).
  => Cmat is the Gram matrix of {Y_p}: Hermitian PSD.
  => sum_{p != p'} Cmat[p,p'] = ||Y_sum||^2/N - sum_p E_p,
     Y_sum := sum_p Y_p  -- ONE collective field.
  => the k=4 off-system estimate collapses to bounding ||Y_sum||^2.

Verified (r108k, N=199 & 2161): identity rel err 5.07e-14 / 2.52e-12;
Gram energy rank-1 share 0.956 -> 0.995; cosines mean 0.859 -> 0.926;
constructive alignment (pos-frac 1.000, |sum|/l2 282 / 223);
corr(alpha, E_p) 0.963 -> 0.988; corr(alpha, |A0|) ~ -0.79.
Memory-lean variant (H3/A deleted asap).
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108k_collective.log")

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
    w = np.where(is_diag, 0.0, mult.astype(np.float64))

    flat = (c1 * m + c2) * N + d
    H3 = np.bincount(flat, weights=w, minlength=m * m * N)
    del flat, w
    H3 = H3.reshape(m, m, N)
    A = np.fft.fft2(H3, axes=(0, 1)).reshape(m * m, N)
    del H3
    Ah = np.fft.fft(A, axis=1)
    del A
    neg = (-np.arange(N)) % N
    sq = Ah ** 2
    sqn = Ah[:, neg] ** 2          # = conj(Ah)^2 (A real)
    Cmat = (sq @ sqn.T) / N
    mp = m * m

    # ---- EXACT CHECK of the Gram/collective identity ----
    Ysum = sq.sum(axis=0)
    lhs = float(np.real(Cmat.sum() - np.trace(Cmat)))
    rhs = float(np.real(np.vdot(Ysum, Ysum) / N - np.trace(Cmat)))
    log(f"=== N={N} K={K} m={m}")
    log(f"  COLLECTIVE IDENTITY: cross = {lhs:.6e} vs "
        f"||Y_sum||^2/N - sumE = {rhs:.6e}  (rel "
        f"{abs(lhs - rhs)/max(abs(lhs), 1e-300):.2e})")

    # ---- full giant list ----
    A0 = np.abs(Ah[:, 0])
    big = np.where(A0 > N / 4)[0]
    coords = [(int(i)//m, int(i) % m) for i in big]
    vals = sorted(set(np.round(A0[big]).astype(int).tolist()))
    log(f"  giant complete sums: {len(big)} pairs, |A0| values {vals}")
    log(f"  giant (j1,j2) full list: {coords}")
    j1s = np.array([c[0] for c in coords])
    j2s = np.array([c[1] for c in coords])
    c_oneside = int(((j1s == 0) | (j2s == 0)).sum())
    c_antisym = int(((j1s + j2s) % m == 0).sum())
    log(f"  criterion counts: one-side {c_oneside}/{len(big)}, "
        f"j1+j2==0 {c_antisym} (=> 3m-2 = {3*m-2})")

    # ---- collinearity / Perron profile of the nontriv block ----
    others = np.arange(1, mp)
    B = Cmat[np.ix_(others, others)]
    U, S, Vh = np.linalg.svd(B)
    sh = (S**2 / np.sum(S**2))[:4]
    log(f"  nontriv Gram SVD energy shares: {['%.3f' % x for x in sh]}")
    alpha = np.abs(U[:, 0])
    Epsi = (np.abs(Ah)**4).sum(axis=1) / N
    a0n = A0[others]
    epn = Epsi[others]

    def corr(x, y):
        x = x - x.mean()
        y = y - y.mean()
        return float((x*y).sum() / np.sqrt((x*x).sum()*(y*y).sum()))

    log(f"  corr(alpha, |A0|) = {corr(alpha, a0n):.3f};  "
        f"corr(alpha, E_p) = {corr(alpha, epn):.3f}")
    top = np.argsort(-alpha)[:8]
    log(f"  alpha top (j1,j2): "
        f"{[(int(others[i])//m, int(others[i]) % m) for i in top]}")
    nrm = np.sqrt(np.diag(B))
    G = B / np.outer(nrm, nrm)
    log(f"  Gram cosines: mean {float(np.mean(np.real(G))):.4f}  "
        f"min {float(np.real(G).min()):.4f}  "
        f"frac>0.9 {float((np.real(G) > 0.9).mean()):.3f}")
    Yabs = np.abs(Ysum)
    log(f"  |Y_sum(0)| = {Yabs[0]:.3e}; max {Yabs.max():.3e} "
        f"at w={int(np.argmax(Yabs))}; median(w!=0) {np.median(Yabs[1:]):.3e}")
    return dict(N=N, K=K, m=m, cross=lhs,
                identity_rel=float(abs(lhs-rhs)/max(abs(lhs), 1e-300)),
                giants=len(big), giant_values=vals,
                sv_shares=sh.tolist(), corr_alpha_A0=corr(alpha, a0n),
                corr_alpha_Ep=corr(alpha, epn),
                Ysum0=float(Yabs[0]), Ysum_max=float(Yabs.max()))


def main():
    log("R108k: collective-field collapse of the cross terms (exact)")
    res = {}
    for N, a in ((199, 139), (2161, 48)):
        res[f"N{N}"] = run(N, a)
    with open(os.path.join(OUT_DIR, "r108k_collective.json"), "w") as fh:
        json.dump(res, fh, indent=1, default=float)
    log("done")


if __name__ == "__main__":
    main()
