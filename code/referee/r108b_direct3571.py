r"""R108b -- DIRECT (FFT-free) B(t) at N=3571 + half-coset hypothesis test.

Part 1: B(t) by direct enumeration of H-coupled key pairs, using a
precomputed difference table Dtab[u,v].  Arbitrates the N=3571 E_c
discrepancy: r108 twist pipeline gave 4.459482e15; the paper's table
claims 3.545e15.

Part 2: twist pipeline restricted to the half coset S_+ (characters
trivial on H.<-1>, index 2 in S, m_+ = 105) -- tests whether the
paper's E_c(3571) was computed on the desymmetrised half coset but
compared against the full-coset baseline E_unc/m^4.

Part 3: honest per-fiber Weil test (nontrivial pairs, d != 0) and
per-pair Parseval constant, plus the delta decomposition
(trivial / nontriv pairs / cross terms).
"""
import json
import math
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108b_direct3571.log")
JSON_PATH = os.path.join(OUT_DIR, "r108b_direct3571.json")

_t0 = time.time()


def log(msg):
    print(str(msg), flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(str(msg) + "\n")


def dlog_table(N, g):
    tab = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        tab[x] = s
        x = x * g % N
    return tab


def prim_root(N):
    for g in range(2, N):
        if pow(g, N - 1, N) != 1:
            continue
        if all(pow(g, f, N) != 1 for f in range(2, N - 1) if (N - 1) % f == 0):
            return g
    raise RuntimeError


def build_keys(N):
    inv = np.zeros(N, dtype=np.int64)
    for x in range(1, N):
        inv[x] = pow(x, N - 2, N)
    vals = np.array([x for x in range(1, N) if x != 1], dtype=np.int64)
    X, Y = np.meshgrid(vals, vals, indexing="ij")
    Xf, Yf = X.ravel(), Y.ravel()
    diag = Xf == Yf
    U = np.where(diag, 1, (Xf * inv[Yf]) % N)
    V = np.where(diag, 1, ((Xf - 1) * inv[(Yf - 1) % N]) % N)
    D = np.where(diag, 0, (Xf - Yf) % N)
    keep = ~diag | (Xf == 2)
    mult = np.where(diag, N - 2, 1)
    return U[keep], V[keep], D[keep], mult[keep].astype(np.int64), inv


def diff_table(N, inv):
    """Dtab_flat[u*N+v] = d(u,v) if (u,v) is an admissible key, else -1."""
    D = np.full((N, N), -1, dtype=np.int32)
    vv = np.arange(N, dtype=np.int64)
    for u in range(N):
        if u in (0, 1):
            continue
        diff = (u - vv) % N
        ok = (vv != 0) & (vv != 1) & (vv != u) & (diff != 0)
        # d = (u-1)(1-v)/(u-v)
        dval = ((u - 1) * ((1 - vv) % N) % N) * inv[diff] % N
        row = np.where(ok, dval, -1)
        D[u, :] = row.astype(np.int32)
    return D.ravel()


def direct_B(N, a, u, v, d, mult, inv):
    """B(t) by direct enumeration: for each (h_i, h_j) in H^2, all key pairs
    (p1,p2) with u1 = h_i/u2, v1 = h_j/v2 are exactly the H-coupled pairs."""
    K = 1
    x = a % N
    while x != 1:
        x = x * a % N
        K += 1
    H = np.array([pow(a, i, N) for i in range(K)], dtype=np.int64)
    Dtab = diff_table(N, inv)
    inv_u = inv[u]
    inv_v = inv[v]
    d2 = d.astype(np.int64)  # build_keys d is correct incl. diagonal row (0)
    B = np.zeros(N, dtype=np.float64)
    m2 = mult.astype(np.float64)
    for i in range(K):
        u1 = (H[i] * inv_u) % N
        base_u = u1 * N
        # p1 = diagonal key (1,1) arises exactly when u2 = h_i and v2 = h_j:
        # always admissible, multiplicity N-2, difference 0.
        diag_u = u == H[i]
        for j in range(K):
            v1 = (H[j] * inv_v) % N
            flat = base_u + v1
            d1 = Dtab[flat].astype(np.int64)
            ok = d1 >= 0
            if ok.any():
                t = (d1 + d2) % N
                B += np.bincount(t[ok], weights=m2[ok], minlength=N)
            dj = diag_u & (v == H[j])
            if dj.any():
                B += np.bincount(d2[dj], weights=(N - 2) * m2[dj], minlength=N)
    return B, K


def twist_full(N, a, u, v, d, mult, inv):
    """Twist pipeline (as r108) but returns A matrix in memory for N=3571
    via float32 memmap-less chunking; computes full- and half-coset B/E_c,
    per-pair energies (nontrivial), per-fiber max |A| (d != 0), cross terms."""
    K = 1
    x = a % N
    while x != 1:
        x = x * a % N
        K += 1
    m = (N - 1) // K
    g = prim_root(N)
    dlog = dlog_table(N, g)
    ell = int(dlog[a])
    assert ell % m == 0
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
        part = np.bincount(
            f, weights=mult[sel].astype(np.float64), minlength=(hi - lo) * m * N
        )
        H3[lo * m * N : hi * m * N] += part.astype(np.int64)
    H3 = H3.reshape(m, m, N)
    c_counts = H3.sum(axis=(0, 1))
    chat = np.fft.fft(c_counts.astype(np.float64))
    E_unc = float(np.sum(np.abs(chat) ** 4) / N)

    # A in float32 chunks to keep memory bounded; error ~1e-7 relative,
    # ample for 4-digit comparisons
    mp = m * m
    A32 = np.empty((mp, N), dtype=np.complex64)
    CH = 512
    for d0 in range(0, N, CH):
        d1 = min(d0 + CH, N)
        Af = np.fft.fft2(H3[:, :, d0:d1], axes=(0, 1))
        A32[:, d0:d1] = Af.reshape(mp, d1 - d0).astype(np.complex64)

    # pair masks
    j1 = np.arange(mp) // m
    j2 = np.arange(mp) % m
    # S_+ = characters trivial on H.<-1>: chi_{Kj}(-1) = (-1)^j -> j even
    half_mask = (j1 % 2 == 0) & (j2 % 2 == 0)
    nontriv_mask = np.ones(mp, dtype=bool)
    nontriv_mask[0] = False  # trivial pair (0,0)

    # per-pair pass
    E_pair = np.empty(mp, dtype=np.float64)
    Ah2_full = np.zeros(N, dtype=np.complex128)
    Ah2_half = np.zeros(N, dtype=np.complex128)
    maxA_nontriv_dne0 = 0.0
    PCH = 2048
    for p0 in range(0, mp, PCH):
        p1 = min(p0 + PCH, mp)
        blk = A32[p0:p1, :].astype(np.complex128)
        Ah = np.fft.fft(blk, axis=1)
        E_pair[p0:p1] = (np.abs(Ah) ** 4).sum(axis=1) / N
        sq = Ah**2
        Ah2_full += sq.sum(axis=0)
        hsel = half_mask[p0:p1]
        if hsel.any():
            Ah2_half += sq[hsel].sum(axis=0)
        nsel = nontriv_mask[p0:p1]
        if nsel.any():
            blk_nt = blk[nsel]
            blk_nt = blk_nt[:, 1:]  # exclude d = 0 fiber
            mx = float(np.max(np.abs(blk_nt)))
            maxA_nontriv_dne0 = max(maxA_nontriv_dne0, mx)

    Bf = np.fft.ifft(Ah2_full / (m * m))
    B_full = Bf.real
    E_c_full = float(np.sum(B_full**2))
    Bh = np.fft.ifft(Ah2_half / (m_half := int(half_mask.sum())))
    B_half = Bh.real
    E_c_half = float(np.sum(B_half**2))

    E_triv = E_pair[0]
    E_nontriv_sum = float(E_pair[1:].sum())
    cross_full = m**4 * E_c_full - (E_unc + E_nontriv_sum)

    out = dict(
        K=K, m=m, m_half=m_half, E_unc=E_unc,
        E_c_full=E_c_full, E_c_half=E_c_half,
        E_triv=float(E_triv), E_nontriv_sum=E_nontriv_sum,
        cross_full=float(cross_full),
        max_E_nontriv=float(E_pair[1:].max()),
        maxA_nontriv_dne0=maxA_nontriv_dne0,
        B_full0=float(B_full[0]), B_half0=float(B_half[0]),
        imag_full=float(np.max(np.abs(Bf.imag))),
    )
    return out


def main():
    N, a = 3571, 2469
    log(f"R108b: N={N}, a={a}")
    u, v, d, mult, inv = build_keys(N)
    log(f"keys: {len(u)} rows, built at {time.time() - _t0:.1f}s")

    # ---- Part 1: direct B
    B, K = direct_B(N, a, u, v, d, mult, inv)
    E_c_direct = float(np.sum(B**2))
    Z0_direct = float(B[0])
    log(f"DIRECT: K={K}, E_c={E_c_direct:.6e}, Z_0={Z0_direct:.0f}, "
        f"B nonneg: {bool((B >= -1e-6).all())}, "
        f"max|B|={B.max():.0f} at t={int(np.argmax(B))}")
    log(f"  (r108 twist pipeline gave 4.459482e15; paper claims 3.545e15)")

    # ---- Part 2+3: twist pipeline, full + half coset
    tw = twist_full(N, a, u, v, d, mult, inv)
    m = tw["m"]
    log(f"TWIST full coset:  E_c={tw['E_c_full']:.6e} "
        f"(vs direct rel {abs(tw['E_c_full'] - E_c_direct) / E_c_direct:.2e})")
    log(f"TWIST half coset (m_+={tw['m_half']}): E_c={tw['E_c_half']:.6e}")
    base_full = tw["E_unc"] / m**4
    m_plus = int(round(math.sqrt(tw["m_half"])))  # half-coset size
    base_half = tw["E_unc"] / m_plus**4
    log(f"  baseline full  E_unc/m^4   = {base_full:.6e}")
    log(f"  baseline half  E_unc/m_+^4 = {base_half:.6e}")
    delta_full_ok = (tw["E_c_full"] - base_full) / base_full
    delta_half_ok = (tw["E_c_half"] - base_half) / base_half
    delta_mixed = (tw["E_c_half"] - base_full) / base_full
    log(f"  delta(full/full)   = {delta_full_ok * 100:+.2f}%")
    log(f"  delta(half/half)   = {delta_half_ok * 100:+.2f}%")
    log(f"  delta(half/full) MIXED = {delta_mixed * 100:+.2f}%   "
        f"<-- paper's -6.9%?")
    log(f"  E_triv={tw['E_triv']:.6e}  sum_nontriv={tw['E_nontriv_sum']:.4e}  "
        f"cross={tw['cross_full']:.4e}")
    log(f"  max E_psi (nontriv)/N^5 = {tw['max_E_nontriv'] / N**5:.4f}")
    log(f"  max |A_psi(d)|, nontriv, d!=0: {tw['maxA_nontriv_dne0']:.2f} "
        f"vs 4sqrt(N)={4 * math.sqrt(N):.2f} "
        f"({'OK' if tw['maxA_nontriv_dne0'] <= 4 * math.sqrt(N) else 'VIOLATION'})")

    results = dict(
        N=N, a=a, K=K, m=m,
        E_c_direct=E_c_direct, Z0_direct=Z0_direct,
        E_unc=tw["E_unc"], E_c_full=tw["E_c_full"], E_c_half=tw["E_c_half"],
        E_triv=tw["E_triv"], E_nontriv_sum=tw["E_nontriv_sum"],
        cross_full=tw["cross_full"], max_E_nontriv=tw["max_E_nontriv"],
        maxA_nontriv_dne0=tw["maxA_nontriv_dne0"],
        B_full0=tw["B_full0"], B_half0=tw["B_half0"],
        imag_full=tw["imag_full"], m_half_pairs=tw["m_half"],
        base_full=base_full, base_half=base_half,
        delta_full_pct=delta_full_ok * 100,
        delta_half_pct=delta_half_ok * 100,
        delta_mixed_pct=delta_mixed * 100,
    )
    with open(JSON_PATH, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=1, default=float)
    log(f"WROTE {JSON_PATH}  ({time.time() - _t0:.1f}s)")


if __name__ == "__main__":
    main()
