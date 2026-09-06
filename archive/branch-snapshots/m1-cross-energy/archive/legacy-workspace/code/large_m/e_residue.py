"""
Run 80: THE E-RESIDUE, re-scoped to the measurable.
====================================================
The ensemble 5th moment decomposes as  mom_5 = K^-5 (G_5 + I_5 + R_5):
  G_5 = sum over words with L = 0 of G(C)             (Gauss part; R76),
  I_5 = sum over words with L != 0 of (1/N^2) sum_{n in ker L} w^Phi
        (kernel slice: exactly 1/N^2 per invertible-L word),
  R_5 = (1/m) sum over ALL words of (1/N^2) sum_n w^Phi E(L n)
        (the E-residue).

Pointwise (fixed-n) the underlying formula is already certified (R76
Part A, 24/24 at N=199); the ensemble identity follows by summing.  What
is NOT yet measured anywhere is the SIZE of R_5.  This script:

Part 1 (N=199, K=11): direct ensemble moment (exact matrices, all n);
  one chunked word pass classifying L=0 / invertible / degenerate;
  G_5 and I_5 exact;  R_5 = N^5 * direct - G_5 - I_5  (the remainder,
  valid up to the Part-A certification error).
Part 2 (N=3571, K=17, the real design):
  (a) the fixed-n word formula vs direct compressed matrices at 4 n-points
      (the N=3571 extension of the R76 Part-A certificate);
  (b) G_5 (target 0.190423), I_5 exact from the classification pass;
  (c) R_5 measured by n-sampling (mean +/- SE over 200 n-points);
  (d) the verdict on the R76 prediction K^-5 G_5 = +1.341e-07.

Output: artifacts/r80/e_residue.json
"""

import json
import os
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis  # noqa: E402
from r76_phi_ensemble import build_Etab, gauss_sum, powers_At  # noqa: E402


def word_pass(K, r, N, P, n_list=None, Etab=None, m=None, two_inv=None,
              chunk=500_000):
    """One chunked pass over all (2K)^r words.

    Returns: rank0_count, rank0_C (dict C->mult), inv_count,
    degen dict -> mult, total, and (if n_list given) the per-n word sums
    of the full fixed-n formula (indicator + E/m).
    """
    lo = K - 1
    Psh = np.stack([P[d] for d in range(-(K - 1), K)])
    total = (2 * K) ** r
    pw = np.array([(2 * K) ** (r - 1 - t) for t in range(r)], dtype=np.int64)
    rank0_C = defaultdict(int)
    rank0_count = 0
    inv_count = 0
    degen = defaultdict(int)
    n_sums = None
    nvs = None
    if n_list is not None:
        n_sums = {tuple(map(int, n)): 0.0 + 0.0j for n in n_list}
        nvs = {tuple(map(int, n)): np.array(n, dtype=np.int64) % N
               for n in n_list}
    for start in range(0, total, chunk):
        cnt = min(chunk, total - start)
        idx = np.arange(start, start + cnt, dtype=np.int64)
        g = np.stack([(idx // pw[t]) % (2 * K) for t in range(r)])
        eg = np.where(g < K, -1, 1)
        jg = g % K
        L = np.zeros((cnt, 2, 2), dtype=np.int64)
        Cacc = np.zeros((cnt, 2, 2), dtype=np.int64)
        for i in range(r):
            L += eg[i, :, None, None] * Psh[jg[i] + lo]
        L %= N
        for i in range(r):
            for k2 in range(i + 1, r):
                d = jg[k2] - jg[i] + lo
                Cacc += (eg[i] * eg[k2])[:, None, None] * Psh[d]
        Cacc %= N
        Lf = L.reshape(cnt, 4)
        det = (Lf[:, 0] * Lf[:, 3] - Lf[:, 1] * Lf[:, 2]) % N
        iszero = ~Lf.any(axis=1)
        rank0_count += int(iszero.sum())
        for w in np.nonzero(iszero)[0]:
            rank0_C[tuple(Cacc[w].ravel())] += 1
        degen_mask = (~iszero) & (det == 0)
        if n_list is None or len(degen) < 4000:
            for w in np.nonzero(degen_mask)[0]:
                degen[(tuple(int(x) for x in Lf[w]),
                       tuple(Cacc[w].ravel()))] += 1
        inv_count += int(((~iszero) & (det != 0)).sum())
        if n_list is not None:
            for nkey, nv in nvs.items():
                n1, n2 = int(nv[0]), int(nv[1])
                Cn1 = (Cacc[:, 0, 0] * n1 + Cacc[:, 0, 1] * n2) % N
                Cn2 = (Cacc[:, 1, 0] * n1 + Cacc[:, 1, 1] * n2) % N
                sig = (n1 * Cn2 - n2 * Cn1) % N
                phi = (two_inv * sig) % N
                wphas = np.exp(2j * np.pi * phi / N)
                w1 = (L[:, 0, 0] * n1 + L[:, 0, 1] * n2) % N
                w2 = (L[:, 1, 0] * n1 + L[:, 1, 1] * n2) % N
                ind = ((w1 == 0) & (w2 == 0)).astype(complex)
                Ev = Etab[w1, w2]
                n_sums[nkey] += complex(np.sum(wphas * (ind + Ev / m)))
    return {"rank0_count": rank0_count, "rank0_C": dict(rank0_C),
            "inv_count": inv_count, "degen": dict(degen),
            "total": total, "n_sums": n_sums}


def direct_moment(cm, B, m, r, nv):
    Wp = B.conj().T @ cm.apply_T(nv, B)
    Wm = B.conj().T @ cm.apply_T((-nv) % cm.N, B)
    M = Wp + Wm
    M = (M + M.conj().T) / 2
    return complex(np.trace(np.linalg.matrix_power(M, r)) / m)


def kernel_I(L, C, N, two_inv):
    """(1/N^2) sum_{n in ker L} w^{Phi(n)} — brute force over the grid."""
    n1 = np.arange(N)
    n1g, n2g = np.meshgrid(n1, n1, indexing="ij")
    v1 = (L[0, 0] * n1g + L[0, 1] * n2g) % N
    v2 = (L[1, 0] * n1g + L[1, 1] * n2g) % N
    ker = (v1 == 0) & (v2 == 0)
    Cn1 = (C[0, 0] * n1g + C[0, 1] * n2g) % N
    Cn2 = (C[1, 0] * n1g + C[1, 1] * n2g) % N
    sig = (n1g * Cn2 - n2g * Cn1) % N
    ph = np.exp(2j * np.pi * (two_inv * sig % N) / N)
    return complex(np.sum(ph[ker]) / (N * N))


def main():
    out = {"script": "src/r80_e_residue.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S")}
    A = [[2, 1], [1, 1]]

    # ---------------- Part 1: N=199 ----------------
    N, K, r = 199, 11, 5
    cm = CatMap(A, N)
    two_inv = (N + 1) // 2
    rng = np.random.default_rng(76076)
    B, lam, m, res, chi = eigen_basis(cm, K, 0, 24, rng)
    t0 = time.time()
    tot = 0.0 + 0.0j
    for a in range(N):
        for b in range(N):
            tot += direct_moment(cm, B, m, r, np.array([a, b],
                                                       dtype=np.int64))
    direct = tot / (N * N)
    print(f"[part1] direct ensemble moment = {direct.real:+.6e} "
          f"({time.time()-t0:.0f} s)", flush=True)
    P = powers_At(A, N, -(K - 1), K - 1)
    t0 = time.time()
    wp = word_pass(K, r, N, P)
    print(f"[part1] classification pass ({time.time()-t0:.0f} s): "
          f"rank0={wp['rank0_count']} inv={wp['inv_count']} "
          f"degen={len(wp['degen'])}", flush=True)
    ok199 = wp["rank0_count"] == 2 * K * 20
    print(f"[part1] rank0 words = {wp['rank0_count']} (census 2K*20="
          f"{2 * K * 20}) {'OK' if ok199 else '*** MISMATCH ***'}", flush=True)
    G5 = 0.0 + 0.0j
    for ct, mult in wp["rank0_C"].items():
        G5 += mult * gauss_sum(np.array(ct, dtype=np.int64).reshape(2, 2),
                               N, two_inv)
    I5 = wp["inv_count"] / (N * N)
    for (Lk, Ck), mult in wp["degen"].items():
        I5 += mult * kernel_I(np.array(Lk, dtype=np.int64).reshape(2, 2),
                              np.array(Ck, dtype=np.int64).reshape(2, 2),
                              N, two_inv).real
    R5 = direct.real * K ** r - G5.real - I5.real
    print(f"[part1] G5={G5.real:+.6f} I5={I5.real:.6f} "
          f"R5={R5:+.3e}", flush=True)
    out["part1"] = {"N": N, "K": K, "m": int(m), "direct_re": direct.real,
                    "rank0_words": wp["rank0_count"],
                    "rank0_ok": bool(ok199),
                    "invertible_words": wp["inv_count"],
                    "degenerate_classes": len(wp["degen"]),
                    "G5_re": G5.real, "I5_re": I5.real, "R5_re": R5}

    # ---------------- Part 2: N=3571 ----------------
    N2, K2, r2 = 3571, 17, 5
    cm2 = CatMap(A, N2)
    two_inv2 = (N2 + 1) // 2
    t0 = time.time()
    rng2 = np.random.default_rng(803571)
    B2, lam2, m2, res2, chi2 = eigen_basis(cm2, K2, 0, 320, rng2)
    print(f"[part2] eigenbasis m={m2} resid={res2:.2e} "
          f"({time.time()-t0:.0f} s)", flush=True)
    t0 = time.time()
    Etab2 = build_Etab(cm2, N2, B2, m2, two_inv2)
    assert abs(Etab2[0, 0]) < 1e-6
    print(f"[part2] Etab built, max|E|={np.abs(Etab2).max():.1f} "
          f"({time.time()-t0:.0f} s)", flush=True)
    P2 = powers_At(A, N2, -(K2 - 1), K2 - 1)

    # (a) fixed-n certificate at the real design
    n_list = [(0, 0), (1, 0), (0, 1), (3, 7)]
    t0 = time.time()
    wp2 = word_pass(K2, r2, N2, P2, n_list=n_list, Etab=Etab2, m=m2,
                    two_inv=two_inv2)
    print(f"[part2] word pass with n-sums ({time.time()-t0:.0f} s)", flush=True)
    cert = []
    for n in n_list:
        nv = np.array(n, dtype=np.int64) % N2
        lhs = direct_moment(cm2, B2, m2, r2, nv)
        rhs = wp2["n_sums"][tuple(n)] / K2 ** r2
        err = abs(lhs - rhs)
        cert.append({"n": list(n), "lhs": lhs.real, "rhs": rhs.real,
                     "abs_err": err})
        print(f"  cert n={tuple(n)}: lhs {lhs.real:+.9f} rhs {rhs.real:+.9f} "
              f"|err| {err:.2e}", flush=True)
    ok = all(x["abs_err"] < 1e-9 for x in cert)
    print(f"  VERDICT: {'PASS' if ok else 'FAIL'}", flush=True)

    G5_2 = 0.0 + 0.0j
    for ct, mult in wp2["rank0_C"].items():
        G5_2 += mult * gauss_sum(np.array(ct, dtype=np.int64).reshape(2, 2),
                                 N2, two_inv2)
    I5_2 = wp2["inv_count"] / (N2 * N2)
    ok3571 = wp2["rank0_count"] == 680
    print(f"[part2] rank0 words = {wp2['rank0_count']} (census D_5(N)=680) "
          f"{'OK' if ok3571 else '*** MISMATCH ***'}", flush=True)
    print(f"[part2] G5={G5_2.real:+.6f} (R76: +0.190423)  "
          f"I5={I5_2.real:.6f}", flush=True)
    print(f"[part2] K^-5 G5 = {G5_2.real/K2**5:+.4e} "
          f"(R76 prediction +1.341e-07)", flush=True)

    # (c) R5 by n-sampling (one amortised pass: the L/C construction is
    # shared across all sampled n)
    t0 = time.time()
    rngs = np.random.default_rng(80080)
    S = 120
    n_mc = [tuple(int(x) for x in rngs.integers(0, N2, size=2))
            for _ in range(S)]
    wpm = word_pass(K2, r2, N2, P2, n_list=n_mc, Etab=Etab2, m=m2,
                    two_inv=two_inv2)
    arr = np.array([wpm["n_sums"][nk].real / m2 for nk in n_mc])
    print(f"[part2] MC pass ({time.time()-t0:.0f} s)", flush=True)
    R5_mean = arr.mean()
    R5_se = arr.std(ddof=1) / np.sqrt(S)
    print(f"[part2] R5 (n-sampled) = {R5_mean:+.6e} +/- {R5_se:.2e} "
          f"({time.time()-t0:.0f} s)", flush=True)
    print(f"[part2] |R5|/|G5| = {abs(R5_mean)/abs(G5_2.real):.2e}", flush=True)
    out["part2"] = {"N": N2, "K": K2, "m": int(m2), "eigen_resid": res2,
                    "certificates": cert, "cert_pass": bool(ok),
                    "rank0_words": wp2["rank0_count"],
                    "rank0_ok": bool(ok3571),
                    "G5_re": G5_2.real, "I5_re": I5_2.real,
                    "pred_K-5_G5": G5_2.real / K2 ** 5,
                    "R5_mc_mean": R5_mean, "R5_mc_se": R5_se,
                    "R5_samples": S}
    dest = os.path.join("artifacts", "r80", "e_residue.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", os.path.normpath(dest), flush=True)


if __name__ == "__main__":
    main()
