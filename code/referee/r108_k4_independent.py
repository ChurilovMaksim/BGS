r"""R108 -- INDEPENDENT REFEREE VERIFICATION OF THE k=4 COUPLED-ENERGY CHAIN.

Written from the paper definitions only (cat_map_bgs_main.tex sec:r92/r95/r101,
mobius_fiber_theorem.tex), without importing any workspace module, so that it
constitutes an independent check of:

  (G)  ground truth at N=53: B(t) by brute-force enumeration of admissible
       key pairs with the H-coupling constraints; E_c, Z_0 = B(0), the
       mean/variance of Sigma_4(q) over q in F_N^*.
  (T)  the twist identity: B = (1/m^2) sum_{psi in S^2} A_psi * A_psi via the
       coset 2D-DFT pipeline, compared digit-for-digit against (G) at N=53,
       then used at N=199 and N=3571.
  (F)  flatness: c(d) = (N-2) + eps(d), |eps| <= 2 (elementary count check).
  (W)  per-fiber Weil test: max |A_psi(d)| over all nontrivial pairs and all
       fibers, against 4*sqrt(N)   (the paper only tested N=53,199).
  (P)  per-pair Parseval test: max_psi E_psi / N^5 against the claimed
       constant 16 (the paper's Theorem "delta envelope" derives
       E_twist <= 16 N^5 per nontrivial pair).
  (X)  cross-term test: m^4 * E_c  vs  E_unc + sum_{psi != 11} E_psi
       (equality iff the claimed exact twist decomposition has no cross
       terms).
  (D)  delta = (E_c - E_unc/m^4) / (E_unc/m^4) against the paper table
       (+1.1%, +6.4%, -6.9%) and the claimed envelope 16/K^2.

Designs (from the workspace scripts): (N, a) = (53, 10), (199, 139),
(3571, 2469).  H = <a>, K = ord(a), m = (N-1)/K, S = annihilator of H.

Key table (derived from Thm 92.2's parametrisation, re-derived here):
  pairs (x,y) in (F_N^* \ {1})^2  <->  keys (u,v) = (x/y, (x-1)/(y-1))
  with u,v in F_N^*, u != v, plus the diagonal key (1,1) carrying the
  N-2 pairs (x,x).  Difference d(u,v) = (u-1)(1-v)/(u-v); diagonal key
  contributes d = 0.
"""
import json
import math
import os
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
os.makedirs(OUT_DIR, exist_ok=True)
LOG_PATH = os.path.join(OUT_DIR, "r108_k4_independent.log")
JSON_PATH = os.path.join(OUT_DIR, "r108_k4_independent.json")

_t0 = time.time()


def log(msg):
    line = str(msg)
    print(line, flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def discrete_log_table(N, g):
    tab = np.zeros(N, dtype=np.int64)
    x = 1
    for s in range(N - 1):
        tab[x] = s
        x = x * g % N
    return tab


def primitive_root(N):
    for g in range(2, N):
        if pow(g, N - 1, N) != 1:
            continue
        ok = True
        # trial: g is primitive iff no proper divisor f of N-1 has g^f = 1
        for f in range(2, N - 1):
            if (N - 1) % f == 0 and pow(g, f, N) == 1:
                ok = False
                break
        if ok:
            return g
    raise RuntimeError("no primitive root")


def multiplicative_order(a, N):
    x, k = a % N, 1
    while x != 1:
        x = x * a % N
        k += 1
    return k


def build_keys(N):
    """All pairs (x,y) in (F_N^* \\ {1})^2 as key arrays.

    Returns u, v, d, mult arrays over the *pair* list; the diagonal pairs
    (x,x) collapse to the single key (1,1) with multiplicity N-2, so the
    returned arrays have (N-2)(N-3) + 1 rows.
    """
    inv = np.zeros(N, dtype=np.int64)
    for x in range(1, N):
        inv[x] = pow(x, N - 2, N)
    vals = np.array([x for x in range(1, N) if x != 1], dtype=np.int64)
    X, Y = np.meshgrid(vals, vals, indexing="ij")
    Xf, Yf = X.ravel(), Y.ravel()
    diag = Xf == Yf
    U = (Xf * inv[Yf]) % N
    V = ((Xf - 1) * inv[(Yf - 1) % N]) % N
    D = (Xf - Yf) % N
    # collapse diagonal pairs (all map to key (1,1), d = 0)
    U = np.where(diag, 1, U)
    V = np.where(diag, 1, V)
    D = np.where(diag, 0, D)
    # deduplicate: keep one row for key (1,1) with multiplicity N-2
    keep = ~diag | (Xf == 2)  # first diagonal pair represents all
    mult = np.where(diag, N - 2, 1)
    return U[keep], V[keep], D[keep], mult[keep].astype(np.int64)


def coset_index(dlog, x, m):
    return (dlog[x] % m).astype(np.int64)


def ground_truth_B(N, a, u, v, d, mult):
    """Brute-force B(t) over admissible key pairs (only for small N).

    B(t) = sum over key pairs (p1,p2) with u1*u2 in H, v1*v2 in H,
    d1+d2 = t (mod N) of mult1*mult2.
    """
    K = multiplicative_order(a, N)
    Hset = np.zeros(N, dtype=bool)
    x = 1
    for _ in range(K):
        Hset[x] = True
        x = x * a % N
    # membership test via discrete log: u1*u2 in H <=> dlog(u1)+dlog(u2) in
    # dlog(H); use direct set membership on products instead (small N).
    inH = Hset  # boolean over residues
    nk = len(u)
    B = np.zeros(N, dtype=np.int64)
    for i in range(nk):
        prod_u = (u[i] * u) % N
        prod_v = (v[i] * v) % N
        sel = inH[prod_u] & inH[prod_v]
        if not sel.any():
            continue
        dd = (d[i] + d[sel]) % N
        w = mult[i] * mult[sel]
        B += np.bincount(dd, weights=w.astype(np.float64), minlength=N).astype(
            np.int64
        )
    return B


def twist_pipeline(N, a, u, v, d, mult, chunk_d=256, chunk_pairs=2048):
    """Full twist decomposition via coset 2D-DFT, exact up to float FFT error.

    Returns dict with B, E_c, E_unc, per-pair E_psi stats, max |A|, etc.
    """
    K = multiplicative_order(a, N)
    m = (N - 1) // K
    g = primitive_root(N)
    dlog = discrete_log_table(N, g)
    ell = int(dlog[a])
    assert ell % m == 0, "design consistency: dlog(a) must be 0 mod m"

    c1 = coset_index(dlog, u, m)
    c2 = coset_index(dlog, v, m)

    # 3D histogram over (c1, c2, dbar) with multiplicities
    flat = (c1 * m + c2) * N + d
    total_bins = m * m * N
    # bincount in halves over c1 to cap peak memory at N=3571
    H3 = np.zeros(total_bins, dtype=np.int64)
    mid = m // 2
    for lo, hi in ((0, mid), (mid, m)):
        sel = (c1 >= lo) & (c1 < hi)
        if not sel.any():
            continue
        f = (c1[sel] - lo) * (m * N) + c2[sel] * N + d[sel]
        w = mult[sel].astype(np.float64)
        part = np.bincount(f, weights=w, minlength=(hi - lo) * m * N)
        H3[lo * m * N : hi * m * N] += part.astype(np.int64)
    H3 = H3.reshape(m, m, N)

    # trivial-pair fiber counts c(dbar) (sanity vs flatness lemma)
    c_counts = H3.sum(axis=(0, 1))

    # A[j1, j2, dbar] = sum_{c1,c2} H3[c1,c2,dbar] * omega^{j1 c1 + j2 c2}
    # (fft sign convention relabels j -> -j; harmless for all quantities
    #  computed here, which are invariant under conjugation)
    use_memmap = m * m * N > 40_000_000
    if use_memmap:
        A_path = os.path.join(OUT_DIR, "r108_A_3571.dat")
        A_mm = np.lib.format.open_memmap(
            A_path, mode="w+", dtype=np.complex128, shape=(m * m, N)
        )
    else:
        A_mm = np.empty((m * m, N), dtype=np.complex128)
    for d0 in range(0, N, chunk_d):
        d1 = min(d0 + chunk_d, N)
        blk = H3[:, :, d0:d1]
        Af = np.fft.fft2(blk, axes=(0, 1))  # (m, m, chunk)
        A_mm[:, d0:d1] = Af.reshape(m * m, d1 - d0)
    if use_memmap:
        A_mm.flush()

    # per-pair pass: E_psi = (1/N) sum_omega |Ahat(omega)|^4,
    # Ahat = full complex FFT over dbar (cyclic group Z/N); accumulate
    # Ahat2_sum[omega] = sum_psi Ahat^2 for B.
    Ahat2_sum = np.zeros(N, dtype=np.complex128)
    E_pair = np.empty(m * m, dtype=np.float64)
    max_abs_A = 0.0
    sum_abs2_A = 0.0
    for p0 in range(0, m * m, chunk_pairs):
        p1 = min(p0 + chunk_pairs, m * m)
        blk = np.asarray(A_mm[p0:p1, :])  # (nchunk, N)
        max_abs_A = max(max_abs_A, float(np.max(np.abs(blk))))
        sum_abs2_A += float(np.sum(np.abs(blk) ** 2))
        Ah = np.fft.fft(blk, axis=1)
        Ahat2_sum += (Ah**2).sum(axis=0)
        E_pair[p0:p1] = (np.abs(Ah) ** 4).sum(axis=1) / N
    Bhat_full = Ahat2_sum / (m * m)
    Bc = np.fft.ifft(Bhat_full)
    B = Bc.real
    imag_err = float(np.max(np.abs(Bc.imag)))
    E_c = float(np.sum(B**2))

    # uncoupled energy from c
    chat = np.fft.fft(c_counts.astype(np.float64))
    E_unc = float(np.sum(np.abs(chat) ** 4) / N)

    # twist-pair bookkeeping: index (j1,j2) = j1*m + j2 ; trivial = 0
    E_triv = E_pair[0]
    E_nontriv_sum = float(E_pair[1:].sum())
    max_E_nontriv = float(E_pair[1:].max())

    out = dict(
        K=K,
        m=m,
        dlog_a=int(ell),
        B=B,
        imag_err=imag_err,
        E_c=E_c,
        E_unc=E_unc,
        E_triv=float(E_triv),
        E_nontriv_sum=E_nontriv_sum,
        max_E_nontriv=max_E_nontriv,
        max_abs_A=max_abs_A,
        sum_abs2_A=sum_abs2_A,
        c_counts=c_counts,
        E_pair=E_pair,
    )
    return out


def main():
    designs = [(53, 10), (199, 139), (3571, 2469)]
    results = {}
    log("R108 independent k=4 referee verification")
    log(f"start {time.time() - _t0:.1f}s")

    for N, a in designs:
        log(f"=== design N={N}, a={a} ===")
        K = multiplicative_order(a, N)
        m = (N - 1) // K
        # design checks
        root_check = (a * a - 3 * a + 1) % N == 0
        disc_qr = pow(5, (N - 1) // 2, N) == 1
        log(f"K=ord(a)={K}, m=(N-1)/K={m}")
        log(f"a root of x^2-3x+1 mod N: {root_check}; 5 QR mod N: {disc_qr}")
        results[f"N{N}_design"] = dict(
            N=N, a=a, K=K, m=m, a_is_root=bool(root_check), five_is_qr=bool(disc_qr)
        )

        u, v, d, mult = build_keys(N)
        log(f"keys: {len(u)} rows (expect (N-2)(N-3)+1 = {(N - 2) * (N - 3) + 1})")

        if N <= 60:
            # ground truth brute force
            Bg = ground_truth_B(N, a, u, v, d, mult)
            Z0 = int(Bg[0])
            E_c_g = int(np.sum(Bg.astype(np.float64) ** 2))
            # Sigma_4(q) and its q-statistics
            qv = np.arange(1, N)
            ph = np.exp(2j * np.pi * np.outer(qv, np.arange(N)) / N)
            S4 = (ph @ Bg.astype(np.float64)).real
            mean_S4 = float(S4.mean())
            std_S4 = float(S4.std())
            log(f"GROUND TRUTH: E_c={E_c_g:.6e}, Z_0={Z0}, "
                f"mean(S4)={mean_S4:.4f}, std(S4)={std_S4:.4f}")
            results[f"N{N}_ground"] = dict(
                E_c=E_c_g, Z0=Z0, mean_S4=mean_S4, std_S4=std_S4
            )

        tw = twist_pipeline(N, a, u, v, d, mult)
        B = tw["B"]
        log(f"twist pipeline: E_c={tw['E_c']:.6e} (imag err {tw['imag_err']:.2e})")
        log(f"  E_unc={tw['E_unc']:.6e}, E_triv={tw['E_triv']:.6e}")
        log(f"  sum nontriv E_psi={tw['E_nontriv_sum']:.6e}, "
            f"max E_psi={tw['max_E_nontriv']:.6e}")
        if N <= 60:
            log(f"  vs ground truth E_c: rel diff "
                f"{abs(tw['E_c'] - E_c_g) / E_c_g:.3e}")
            results[f"N{N}_ground"]["E_c_twist_rel_diff"] = float(
                abs(tw["E_c"] - E_c_g) / E_c_g
            )
        delta = (tw["E_c"] - tw["E_unc"] / m**4) / (tw["E_unc"] / m**4)
        log(f"  delta = {delta * 100:+.2f}%   (paper table: see note)")
        log(f"  envelope 16/K^2 = {16 / K**2 * 100:.2f}%, "
            f"256/K^2 = {256 / K**2 * 100:.2f}%")
        # cross-term test
        cross = m**4 * tw["E_c"] - (tw["E_unc"] + tw["E_nontriv_sum"])
        cross_rel = cross / (m**4 * tw["E_c"])
        log(f"  cross-term residual: {cross:.6e} (rel {cross_rel:+.3e})")
        # Weil test
        wbound = 4 * math.sqrt(N)
        log(f"  max |A_psi(d)| = {tw['max_abs_A']:.3f} vs 4*sqrt(N)={wbound:.3f}"
            f"  -> {'OK' if tw['max_abs_A'] <= wbound else 'VIOLATION'}")
        # per-pair N^5 test
        max_ratio = tw["max_E_nontriv"] / N**5
        log(f"  max E_psi/N^5 = {max_ratio:.3f} vs claimed 16"
            f"  -> {'OK' if max_ratio <= 16 else 'VIOLATION of Parseval constant'}")
        # flatness
        cc = tw["c_counts"]
        eps = cc - (N - 2)
        log(f"  flatness: c in [{int(cc.min())},{int(cc.max())}], "
            f"eps in [{int(eps.min())},{int(eps.max())}] (claim |eps|<=2)")
        results[f"N{N}_twist"] = dict(
            E_c=tw["E_c"],
            E_unc=tw["E_unc"],
            E_triv=tw["E_triv"],
            E_nontriv_sum=tw["E_nontriv_sum"],
            max_E_nontriv=tw["max_E_nontriv"],
            max_E_over_N5=max_ratio,
            max_abs_A=tw["max_abs_A"],
            weil_bound_4sqrtN=wbound,
            delta_pct=delta * 100,
            envelope_16_over_K2_pct=16 / K**2 * 100,
            envelope_256_over_K2_pct=256 / K**2 * 100,
            cross_rel=float(cross_rel),
            c_min=int(cc.min()),
            c_max=int(cc.max()),
            eps_min=int(eps.min()),
            eps_max=int(eps.max()),
            imag_err=tw["imag_err"],
            Z0_twist=float(B[0]),
            sum_abs2_A=tw["sum_abs2_A"],
        )
        if N == 53:
            np.save(os.path.join(OUT_DIR, "r108_B_N53.npy"), B)
        # cleanup memmap
        for f in os.listdir(OUT_DIR):
            if f.startswith("r108_A_") and f.endswith(".dat"):
                os.remove(os.path.join(OUT_DIR, f))
        log(f"design done at {time.time() - _t0:.1f}s")

    with open(JSON_PATH, "w", encoding="utf-8") as fh:
        json.dump(results, fh, indent=1, default=float)
    log(f"WROTE {JSON_PATH}")


if __name__ == "__main__":
    main()
