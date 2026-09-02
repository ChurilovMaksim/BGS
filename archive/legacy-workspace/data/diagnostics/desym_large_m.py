"""
Run 73, Priority 1: push the parity-desymmetrised ratio measurement to large m.
==============================================================================

Memory is the binding constraint (8 GB).  The eigenspace basis is built
INCREMENTALLY: blocks of `blk` random vectors are hit with the exact projector
P_lam = K^{-1} sum_j lam^{-j} U^j, orthogonalised against the basis accumulated
so far, and appended.  Peak memory is (N x m) + (N x blk) complex, instead of
(N x 1.7m) for the one-shot construction.

Because a small torsion exponent K forces N into a finite set (A^K = +-I mod N
means N divides a fixed nonzero integer), large m = N/K requires a moderately
large K as well.  The search below finds the admissible (N, K, m).

Statistic: the unfolding-free consecutive-spacing ratio
    r~_n = min(s_n, s_{n+1}) / max(s_n, s_{n+1}),
with class labels 0.38629 (Poisson), 0.53590 (GOE), 0.60266 (GUE).
"""

from __future__ import annotations

import gc
import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap                     # noqa: E402
from desym_ratio_statistic import RTILDE, r_tilde, ref_rtilde   # noqa: E402
from parity_desymmetrised import apply_parity, eps_of     # noqa: E402


def projector_basis_chunked(cm, K, lam, m_target, blk, rng, tol=1e-7,
                            max_rounds=40, verbose=True):
    """Orthonormal basis of ker(U - lam) built block by block."""
    N = cm.N
    cols = []
    total = 0
    for rnd in range(max_rounds):
        R = (rng.standard_normal((N, blk)) + 1j * rng.standard_normal((N, blk)))
        acc = np.zeros_like(R)
        cur = R
        for j in range(K):
            acc += (lam ** (-j)) * cur
            cur = cm.apply_U(cur)
        acc /= K
        del R, cur
        # orthogonalise against what we have
        for Q in cols:
            acc -= Q @ (Q.conj().T @ acc)
        for Q in cols:                      # second pass for stability
            acc -= Q @ (Q.conj().T @ acc)
        Q, s, _ = np.linalg.svd(acc, full_matrices=False)
        keep = int((s > tol * max(s[0], 1e-300)).sum())
        if keep:
            cols.append(np.ascontiguousarray(Q[:, :keep]))
            total += keep
        del acc, Q, s
        gc.collect()
        if verbose:
            print(f"      round {rnd + 1}: +{keep}, total {total}"
                  f"/{m_target}", flush=True)
        if total >= m_target or keep == 0:
            break
    B = np.concatenate(cols, axis=1) if cols else np.zeros((N, 0), dtype=complex)
    del cols
    gc.collect()
    return B


def find_designs(A, pmax, kmax, mmin, mmax, want_eps):
    A0 = np.array(A, dtype=np.int64)
    I = np.eye(2, dtype=np.int64)
    sieve = np.ones(pmax + 1, dtype=bool)
    sieve[:2] = False
    for i in range(2, int(pmax ** 0.5) + 1):
        if sieve[i]:
            sieve[i * i::i] = False
    out = []
    for p in np.flatnonzero(sieve):
        p = int(p)
        if p < 5000 or math.gcd(int(A0[1, 0]) % p, p) != 1:
            continue
        M = A0 % p
        k = eps = None
        for j in range(1, kmax + 1):
            if np.array_equal(M % p, I):
                k, eps = j, +1
                break
            if np.array_equal(M % p, (-I) % p):
                k, eps = j, -1
                break
            M = M @ A0 % p
        if k is None or eps != want_eps:
            continue
        K = k if eps == 1 else 2 * k
        m = p // K
        if mmin <= m <= mmax:
            out.append((p, k, K, m))
    return out


def main():
    rng = np.random.default_rng(73737373)
    A = [[2, 1], [1, 1]]
    cands = find_designs(A, 200000, 70, 800, 2600, +1)
    cands.sort(key=lambda t: t[3])
    print("candidate eps=+1 design points (p, k, K, m):", cands, flush=True)
    if not cands:
        print("none found")
        return 1
    # take the two largest that fit in memory
    picked = cands[-1:]

    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "rtilde_reference_values": RTILDE, "candidates": cands, "rows": []}
    NU = 6
    for p, k, K, mpred in picked:
        t0 = time.time()
        gb = p * mpred * 16 / 2 ** 30
        print("=" * 78)
        print(f"p={p} k={k} K={K} m~{mpred}   basis {gb:.2f} GB", flush=True)
        if gb > 3.0:
            print("   skipped: basis would exceed the memory budget")
            continue
        cm = CatMap(A, p)
        e0 = np.zeros((p, 1), dtype=complex)
        e0[0, 0] = 1.0
        v = e0
        for _ in range(K):
            v = cm.apply_U(v)
        chi = v[0, 0]
        lam = np.exp((np.log(chi + 0j)) / K)
        B = projector_basis_chunked(cm, K, lam, mpred, blk=64, rng=rng)
        m = B.shape[1]
        res = float(np.abs(cm.apply_U(B[:, :min(m, 64)])
                           - lam * B[:, :min(m, 64)]).max())
        RB = B.conj().T @ apply_parity(B)
        w, Vv = np.linalg.eigh(RB)
        mp, mm_ = int((w > 0).sum()), int((w <= 0).sum())
        print(f"   m={m}  |UB-lam B|={res:.2e}   parity split m+={mp} m-={mm_}",
              flush=True)
        Bp = B @ Vv[:, w > 0]
        Bm = B @ Vv[:, w <= 0]
        del RB, Vv
        gc.collect()

        nrep = 8
        refs_full = {kk: ref_rtilde(kk, m, nrep, rng)
                     for kk in ("GOE", "GUE", "Poisson", "SUP_GUE")}
        refs_blk = {kk: ref_rtilde(kk, mp, nrep, rng)
                    for kk in ("GOE", "GUE", "Poisson")}
        print("   refs full :", "  ".join(f"{a}={b[0]:.4f}+-{b[1]:.4f}"
                                         for a, b in refs_full.items()))
        print("   refs block:", "  ".join(f"{a}={b[0]:.4f}+-{b[1]:.4f}"
                                          for a, b in refs_blk.items()),
              flush=True)

        vals = {kk: [] for kk in ("full", "plus", "minus", "haar")}
        for t in range(NU):
            u = (int(rng.integers(1, p)), int(rng.integers(1, p)))
            H = B.conj().T @ cm.apply_T(u, B); H = H + H.conj().T
            vals["full"].append(r_tilde(np.linalg.eigvalsh(H))[0])
            del H
            Hp = Bp.conj().T @ cm.apply_T(u, Bp); Hp = Hp + Hp.conj().T
            vals["plus"].append(r_tilde(np.linalg.eigvalsh(Hp))[0])
            del Hp
            Hm = Bm.conj().T @ cm.apply_T(u, Bm); Hm = Hm + Hm.conj().T
            vals["minus"].append(r_tilde(np.linalg.eigvalsh(Hm))[0])
            del Hm
            Z = (rng.standard_normal((p, mp))
                 + 1j * rng.standard_normal((p, mp)))
            Q, _ = np.linalg.qr(Z)
            del Z
            Y = Q.conj().T @ cm.apply_T(u, Q); Y = Y + Y.conj().T
            vals["haar"].append(r_tilde(np.linalg.eigvalsh(Y))[0])
            del Q, Y
            gc.collect()
            print(f"      u#{t + 1}: full={vals['full'][-1]:.4f} "
                  f"plus={vals['plus'][-1]:.4f} minus={vals['minus'][-1]:.4f} "
                  f"haar={vals['haar'][-1]:.4f}", flush=True)

        row = {"p": p, "k": k, "K": K, "m": m, "m_plus": mp, "m_minus": mm_,
               "proj_res": res, "n_orbits": NU,
               "refs_full": {a: list(b) for a, b in refs_full.items()},
               "refs_block": {a: list(b) for a, b in refs_blk.items()},
               "measured": {}, "secs": round(time.time() - t0, 1)}
        for kk, v in vals.items():
            a = np.array([x for x in v if np.isfinite(x)])
            Rf = refs_full if kk == "full" else refs_blk
            row["measured"][kk] = {
                "rtilde_mean": float(a.mean()),
                "rtilde_sem": float(a.std(ddof=1) / math.sqrt(len(a))),
                "z": {nm: float((a.mean() - mu) / sd)
                      for nm, (mu, sd) in Rf.items()}}
            z = row["measured"][kk]["z"]
            print(f"   {kk:<6} <r~>={a.mean():.4f}+-"
                  f"{a.std(ddof=1)/math.sqrt(len(a)):.4f}   z: "
                  + "  ".join(f"{nm}={zz:+.2f}" for nm, zz in z.items()),
                  flush=True)
        out["rows"].append(row)
        del B, Bp, Bm
        gc.collect()

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r73", "desym_large_m.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", os.path.normpath(dest))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
