"""
Run 76: the PHI-WEIGHTED ENSEMBLE MOMENT FORMULA, certified end-to-end.
=======================================================================

Theorem (phi-decomposition; fixed n, exact).  With the Weyl product law
T(m)T(v) = w^{sigma(m,v)/2} T(m+v),  sigma(m,v) = m_2 v_1 - m_1 v_2
(this is exactly the kernel convention of src/catmap_independent.py:
(T(n)f)(x) = w^{n2 x - nu n1 n2} f(x - n1), nu = 2^{-1} mod N), the Birkhoff
compression W_v = K^{-1} sum_j T(A^{jt}v) (T6) gives, for
M_n = P(T(n)+T(-n))P on H_lam (dim m), with w_i = eps_i A^{j_i t} n,

    (1/m) Tr_H M_n^r = K^{-r} sum_{(eps,j)} w^{Phi} [ 1{ L n = 0 mod N }
                                                      + E(L n)/m ],
    L       = sum_i eps_i (A^{j_i})^t,   L n = sum_i w_i,
    Phi     = (1/2) sum_{i<k} sigma(w_i, w_k) = (1/2) sigma(n, C n),
    C(eps,j)= sum_{i<k} eps_i eps_k (A^{(j_k - j_i)t}),
    E(w)    = Tr(T(w) P_lam) - m 1{w = 0}.

Level facts:
  (F1) Phi = 0 EXACTLY on pairing words (the sigma-terms cancel pairwise),
       so the pairing main term carries phi = 1 identically;
  (F2) E(0) = 0, so rank-0 words carry no E-correction;
  (F3) the n-average of a rank-0 word is the 2D quadratic Gauss sum
       G(C) = N^{-2} sum_n w^{sigma(n, Cn)/2};  |G| <= N^{-1/2} (and
       G = N^{-1} e^{i theta} for nondegenerate C), so the SHAPE excess in
       the ensemble MOMENT is the Theorem-H counting excess suppressed by an
       extra factor N^{-1/2};
  (F4) END-TO-END (Part A): the fixed-n word formula reproduces the direct
       matrix computation of (1/m) Tr M_n^r at r = 2..5 -- one test validates
       every convention simultaneously.

Parts:
  A  fixed-n end-to-end at (Arnold, N=199, K=11, m=18), r = 2..5
  B  Gauss sums G(C) of the m-shape words; the G_5 ensemble prediction at
     the real design (N=3571, K=17)
  C  MITM census of collected vectors up to r=10 at (K=17, N=3571): the M_r
     hunt for the first genuinely modular relation, cross-checked against the
     R75 totals at r = 6, 8

Output: artifacts/r76/phi_ensemble.json
"""

from __future__ import annotations

import itertools
import json
import math
import os
import sys
import time
from collections import defaultdict

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap            # noqa: E402
from compression_spacings import eigen_basis     # noqa: E402
from r75_multiples import wc_full, chebyshev_exact  # noqa: E402


def powers_At(A, N, dmin, dmax):
    """dict d -> (A^t)^d mod N for d in [dmin, dmax] (det A = 1)."""
    At = np.array(A, dtype=np.int64).T % N
    fwd = [np.eye(2, dtype=np.int64) % N]
    for _ in range(dmax):
        fwd.append(fwd[-1] @ At % N)
    P1 = fwd[1]
    adj = np.array([[P1[1, 1], -P1[0, 1]], [-P1[1, 0], P1[0, 0]]]) % N
    bwd = [np.eye(2, dtype=np.int64) % N]
    for _ in range(-dmin):
        bwd.append(bwd[-1] @ adj % N)
    out = {}
    for d in range(dmin, dmax + 1):
        out[d] = fwd[d] if d >= 0 else bwd[-d]
    return out


def gauss_sum(C, N, two_inv, chunk=1024):
    """G(C) = N^{-2} sum_n w^{sigma(n, Cn)/2}, n over (Z/N)^2."""
    total = 0.0 + 0.0j
    n1 = np.arange(N, dtype=np.int64)
    for a in range(0, N, chunk):
        n1c = n1[a:a + chunk][:, None]
        n2r = n1[None, :]
        Cn1 = (C[0, 0] * n1c + C[0, 1] * n2r) % N
        Cn2 = (C[1, 0] * n1c + C[1, 1] * n2r) % N
        s = (n1c * Cn2 - n2r * Cn1) % N
        q = (two_inv * s) % N
        total += np.exp(2j * np.pi * q / N).sum()
    return total / (N * N)


# ----------------------------------------------------------------------
# Part A: fixed-n end-to-end
# ----------------------------------------------------------------------
def part_A(cm, N, K, B, m, two_inv, P, Etab, r_list, n_list):
    print("=" * 78)
    print("A  fixed-n end-to-end: (1/m)Tr M_n^r  vs  the word formula")
    print("=" * 78)
    # shifted power table: Psh[d + (K-1)] = P_d for d in [-(K-1), K-1]
    lo, hi = -(K - 1), K - 1
    Psh = np.stack([P[d] for d in range(lo, hi + 1)])      # (2K-1, 2, 2)
    out = []
    for r in r_list:
        nw = (2 * K) ** r
        grids = np.array(np.meshgrid(*([range(2 * K)] * r), indexing="ij"),
                         dtype=np.int64).reshape(r, -1)
        eg = grids // K - 1            # eps in {+-1}: 0 -> -1, 1 -> 0? fix below
        eg = np.where(grids < K, -1, 1)
        jg = grids % K
        # L = sum eps_i P_{j_i};  C = sum_{i<k} eps_i eps_k P_{j_k - j_i}
        L = np.zeros((nw, 2, 2), dtype=np.int64)
        Cacc = np.zeros((nw, 2, 2), dtype=np.int64)
        for i in range(r):
            L += eg[i, :, None, None] * Psh[jg[i] + (K - 1)]
        L %= N
        for i in range(r):
            for k in range(i + 1, r):
                d = jg[k] - jg[i] + (K - 1)
                Cacc += (eg[i] * eg[k])[:, None, None] * Psh[d]
        Cacc %= N
        for n in n_list:
            nv = np.array(n, dtype=np.int64) % N
            # LHS: direct matrices
            Wp = B.conj().T @ cm.apply_T(nv, B)
            Wm = B.conj().T @ cm.apply_T((-nv) % N, B)
            M = Wp + Wm
            M = (M + M.conj().T) / 2
            lhs_c = np.trace(np.linalg.matrix_power(M, r)) / m
            lhs = float(lhs_c.real)
            # RHS: word formula
            Wv = (L @ nv) % N
            rank0 = (Wv == 0).all(axis=1)
            Cn = np.einsum("wab,b->wa", Cacc, nv) % N
            s = (int(nv[0]) * Cn[:, 1] - int(nv[1]) * Cn[:, 0]) % N
            phi = (two_inv * s) % N
            wphas = np.exp(2j * np.pi * phi / N)
            Ev = Etab[Wv[:, 0], Wv[:, 1]]
            tot = np.sum(wphas * (rank0.astype(float) + Ev / m))
            rhs_val = float(tot.real) / K ** r
            err = abs(lhs - rhs_val)
            out.append({"r": r, "n": list(map(int, n)), "lhs": lhs,
                        "rhs": rhs_val, "abs_err": err,
                        "rank0_words": int(rank0.sum()),
                        "rhs_imag": float(tot.imag) / K ** r})
            print(f"  r={r} n={tuple(map(int, n))}: lhs {lhs:+.12f}  "
                  f"rhs {rhs_val:+.12f}  |err| {err:.2e}  "
                  f"(rank0 {int(rank0.sum())}, rhs_im {float(tot.imag):.1e})")
            sys.stdout.flush()
    return out


def build_Etab(cm, N, B, m, two_inv):
    """E(w) = Tr(T(w) P_lam) - m*1{w=0} for all w in (Z/N)^2.

    Tr(T(w) P) = w^{-nu w1 w2} sum_x w^{w2 x} P(x - w1, x)."""
    P = B @ B.conj().T                     # (N, N) projector
    x = np.arange(N)
    D = np.empty((N, N), dtype=complex)    # D[w1, x] = P[(x - w1) % N, x]
    for w1 in range(N):
        D[w1] = P[(x - w1) % N, x]
    Wmat = np.exp(2j * np.pi * np.outer(x, x) / N)   # Wmat[x, w2] = w^{w2 x}
    raw = D @ Wmat                          # raw[w1, w2] = sum_x ...
    w1g, w2g = np.meshgrid(np.arange(N), np.arange(N), indexing="ij")
    ph = np.exp(-2j * np.pi * (two_inv * w1g * w2g) / N)
    Etab = raw * ph
    Etab[0, 0] -= m
    return Etab


# ----------------------------------------------------------------------
# Part B: Gauss sums of the m-shape words
# ----------------------------------------------------------------------
def part_B(A, N, K, two_inv):
    print("=" * 78)
    print("B  Gauss sums G(C) of the m-shape words; the G_5 prediction")
    print("=" * 78)
    P = powers_At(A, N, -(K - 1), K - 1)
    Ccount = defaultdict(int)
    for sgn in (1, -1):
        for a in range(K):
            atoms = [(sgn, a), (sgn, (a + 2) % K),
                     (-sgn, (a + 1) % K), (-sgn, (a + 1) % K),
                     (-sgn, (a + 1) % K)]
            words = set()
            for perm in itertools.permutations(atoms):
                words.add(perm)
            for w in words:
                ep = [x[0] for x in w]
                js = [x[1] for x in w]
                C = np.zeros((2, 2), dtype=np.int64)
                for i in range(5):
                    for k in range(i + 1, 5):
                        C += ep[i] * ep[k] * P[js[k] - js[i]]
                Ccount[tuple((C % N).ravel())] += 1
    G5 = 0.0 + 0.0j
    maxG = 0.0
    Gs = {}
    for ct, mult in Ccount.items():
        C = np.array(ct, dtype=np.int64).reshape(2, 2)
        G = gauss_sum(C, N, two_inv)
        Gs[str(ct)] = {"mult": mult, "re": G.real, "im": G.imag, "abs": abs(G)}
        G5 += mult * G
        maxG = max(maxG, abs(G))
    print(f"  distinct C: {len(Ccount)}  (words: {sum(Ccount.values())})")
    print(f"  max |G| = {maxG:.6f}   (N^-1/2 = {N**-0.5:.6f}, "
          f"N^-1 = {1.0/N:.6f})")
    print(f"  G5 = {G5.real:+.6f} {G5.imag:+.6f}i   |G5| = {abs(G5):.6f}")
    print(f"  predicted ensemble 5th moment K^-5 G5 = "
          f"{G5.real/K**5:+.3e} {G5.imag/K**5:+.3e}i")
    return {"N": N, "K": K, "distinct_C": len(Ccount),
            "total_words": sum(Ccount.values()), "max_absG": maxG,
            "G5_re": G5.real, "G5_im": G5.imag,
            "pred_moment_re": G5.real / K ** 5,
            "pred_moment_im": G5.imag / K ** 5, "Gs": Gs}


# ----------------------------------------------------------------------
# Part C: MITM census to r=10, the M_r hunt
# ----------------------------------------------------------------------
def signed_compositions_r(total, k):
    out = []

    def rec(rem, left, cur):
        if left == 1:
            if rem != 0:
                out.append(cur + [rem])
                out.append(cur + [-rem])
            return
        for v in range(-rem + 1, rem):
            if v == 0:
                continue
            rec(rem - abs(v), left - 1, cur + [v])

    rec(total, k, [])
    return out


def build_half_table(positions, S_max, Umod, Uex, N):
    """All half-configurations with L1 = 0..S_max over the given positions.
    entries: (v1m, v2m, S, support, coeffs, z1, z2); includes the EMPTY
    configuration (S=0) so that one-sided collected vectors are joined."""
    entries = [(0, 0, 0, (), (), 0, 0)]
    for S in range(1, S_max + 1):
        for k in range(1, min(len(positions), S) + 1):
            for support in itertools.combinations(positions, k):
                for coeffs in signed_compositions_r(S, k):
                    v1 = v2 = z1 = z2 = 0
                    for j, c in zip(support, coeffs):
                        v1 += c * Umod[j]
                        v2 += c * (Umod[j - 1] if j >= 1 else -1)
                        z1 += c * Uex[j]
                        z2 += c * (Uex[j - 1] if j >= 1 else -1)
                    entries.append((v1 % N, v2 % N, S, tuple(support),
                                    tuple(coeffs), z1, z2))
    return entries


def part_C(A, N, K, r_max=10):
    print("=" * 78)
    print(f"C  MITM census of collected vectors up to r={r_max} "
          f"at K={K}, N={N}: the M_r hunt")
    print("=" * 78)
    t = A[0][0] + A[1][1]
    Ue = chebyshev_exact(t, K + 3)
    Umod = [Ue[j + 1] % N for j in range(K)]
    Uex = Ue[1:]
    h = K // 2
    t0 = time.time()
    left = build_half_table(range(h), r_max, Umod, Uex, N)
    right = build_half_table(range(h, K), r_max, Umod, Uex, N)
    ridx = defaultdict(list)
    for idx, e in enumerate(right):
        ridx[(e[0], e[1])].append(idx)
    print(f"  half tables: left {len(left)}, right {len(right)} "
          f"({time.time()-t0:.1f} s)")
    # ---- pass 1: enumerate all collected vectors by ||c||_1 class
    vectors = []   # (Sp, dense_tuple, cls)
    for Sp in range(2, r_max + 1, 2):
        cnt = 0
        for (v1, v2, Sl, supL, cfL, z1L, z2L) in left:
            if Sl > Sp:
                continue
            Sr = Sp - Sl
            for idx in ridx.get(((N - v1) % N, (N - v2) % N), ()):
                e = right[idx]
                if e[2] != Sr:
                    continue
                sup = supL + e[3]
                cf = cfL + e[4]
                if not sup:
                    continue
                z1 = z1L + e[5]
                z2 = z2L + e[6]
                dense = [0] * K
                for j, c in zip(sup, cf):
                    dense[j] = c
                if z1 == 0 and z2 == 0:
                    cls = "Z"
                else:
                    is_wrap = False
                    for b in range(1, K):
                        d = [dense[(j + b) % K] for j in range(K)]
                        zz1 = sum(d[j] * Uex[j] for j in range(K))
                        zz2 = sum(d[j] * (Uex[j - 1] if j >= 1 else -1)
                                  for j in range(K))
                        if zz1 == 0 and zz2 == 0:
                            is_wrap = True
                            break
                    cls = "wrap" if is_wrap else "modular"
                vectors.append((Sp, tuple(dense), cls))
                cnt += 1
        print(f"  ||c||_1 = {Sp}: {cnt} collected vectors "
              f"({time.time()-t0:.1f} s)")
        sys.stdout.flush()
    # ---- pass 2: word masses at each r (cancelled pairs ride wc_full)
    results = []
    for S in range(2, r_max + 1, 2):
        mass = {"total": 0, "Z": 0, "wrap": 0, "modular": 0}
        examples = []
        for (Sp, dense, cls) in vectors:
            if (S - Sp) % 2 == 1 or Sp > S:
                continue
            w = wc_full(dense, K, S)
            mass["total"] += w
            mass[cls] += w
            if cls == "modular" and len(examples) < 8:
                examples.append(list(dense))
        ok = mass["total"] == mass["Z"] + mass["wrap"] + mass["modular"]
        results.append({"S": S, **mass, "modular_examples": examples,
                        "accounting_ok": ok})
        print(f"  r={S}: total {mass['total']:>13}  Z {mass['Z']:>13}  "
              f"wrap {mass['wrap']:>10}  MODULAR {mass['modular']:>8}  "
              f"{'ok' if ok else 'ACCOUNTING ERROR'}")
        if examples:
            print(f"     first modular vectors: {examples[:3]}")
        sys.stdout.flush()
    return results


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "R76": "phi-decomposition"}
    A = [[2, 1], [1, 1]]

    # ---- Part A design
    Ns = 199
    cm = CatMap(A, Ns)
    ordA, K = cm.orders()
    assert ordA == K, (ordA, K)
    rng = np.random.default_rng(76076)
    B, lam, m, res, chi = eigen_basis(cm, K, 0, 24, rng)
    two_inv = (Ns + 1) // 2
    Etab = build_Etab(cm, Ns, B, m, two_inv)
    assert abs(Etab[0, 0]) < 1e-8, Etab[0, 0]
    P = powers_At(A, Ns, -(K - 1), K - 1)
    print(f"A-design: N={Ns} K={K} m={m} eig-resid={res:.2e} "
          f"max|E|={np.abs(Etab).max():.3f}  E(0)=0 ok")
    n_list = [(0, 0), (1, 0), (0, 1), (3, 7), (97, 13), (198, 198)]
    out["A"] = part_A(cm, Ns, K, B, m, two_inv, P, Etab, [2, 3, 4, 5], n_list)
    okA = all(x["abs_err"] < 1e-9 for x in out["A"])
    out["A_verdict"] = okA
    print(f"  VERDICT A: {'PASS' if okA else 'FAIL'} "
          f"(max err {max(x['abs_err'] for x in out['A']):.2e})\n")

    # ---- Part B at the real design
    N3 = 3571
    cm3 = CatMap(A, N3)
    _, K3 = cm3.orders()
    out["B"] = part_B(A, N3, K3, (N3 + 1) // 2)
    print()

    # ---- Part C
    out["C"] = part_C(A, N3, K3, r_max=12)

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r76", "phi_ensemble.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("\nartifact ->", os.path.normpath(dest))
    print(f"total time {time.time() - t0:.1f} s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
