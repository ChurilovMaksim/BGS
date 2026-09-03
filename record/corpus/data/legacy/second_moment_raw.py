"""
Run 82t: raw-pipeline second moment, over ALL level sets (referee D2 fix).
=======================================================================
The original artifact second_moment_identity.json certified the CENTRED
second moment m_+ Var(ev) instead of Tr(V^2).  This script recomputes the raw
quantity from the pipeline over every level set and re-certifies Lemma 82.1:

    Tr(V_q^2) = N/K^2 + E(q),   |E(q)| <= (4K^2-2)/K^2 < 4   (K odd),

with raw Tr(V^2) = trace of the full matrix (trace NOT removed).

Output: artifacts/r82/second_moment_raw.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402

A = [[2, 1], [1, 1]]


def rep_for_each_q(N):
    got = {}
    for n1 in range(N):
        for n2 in (1, 2, 3):
            q = (n1 * n1 - n1 * n2 - n2 * n2) % N
            if q and q not in got:
                got[q] = (n1, n2)
        if len(got) == N - 1:
            break
    if len(got) < N - 1:
        for n1 in range(N):
            for n2 in range(N):
                q = (n1 * n1 - n1 * n2 - n2 * n2) % N
                if q and q not in got:
                    got[q] = (n1, n2)
            if len(got) == N - 1:
                break
    return got


def main():
    out = {"script": "src/r82t_second_moment_raw.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
           "observable": "Tr(V^2), raw (trace NOT removed)", "designs": []}
    for N, batch in ((199, 64), (3571, 512)):
        t0 = time.time()
        cm = CatMap(A, N)
        ordA, K = cm.orders()
        assert ordA == K
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch,
                                          np.random.default_rng(820018))
        assert res < 1e-9 and m in ((N - 1) // K, (N + 1) // K)
        RB = B.conj().T @ apply_parity(B)
        w, Vv = np.linalg.eigh(RB)
        mp = int((w > 0).sum())
        Bp = B @ Vv[:, w > 0]
        reps = rep_for_each_q(N)
        qs = np.array(sorted(reps), dtype=np.int64)
        tr2 = np.empty(len(qs))
        tr1 = np.empty(len(qs))
        for i, q in enumerate(qs):
            u = reps[int(q)]
            H = Bp.conj().T @ cm.apply_T(u, Bp)
            H = H + H.conj().T
            ev = np.linalg.eigvalsh(H)
            tr1[i] = ev.sum()
            tr2[i] = (ev ** 2).sum()
        pred = N / K ** 2
        E = tr2 - pred
        row = {"N": N, "K": int(K), "m_plus": mp, "n_levels": int(len(qs)),
               "N_over_K2": float(pred), "mean_TrV2": float(tr2.mean()),
               "mean_E": float(E.mean()), "std_E": float(E.std()),
               "max_abs_E": float(np.abs(E).max()),
               "bound": float((4 * K * K - 2) / K ** 2),
               "mean_TrV": float(tr1.mean()), "std_TrV": float(tr1.std()),
               "max_TrV": float(tr1.max())}
        out["designs"].append(row)
        print(f"N={N} K={K}: over ALL {len(qs)} level sets -- "
              f"mean Tr(V^2) = {tr2.mean():.6f} (N/K^2 = {pred:.6f});  "
              f"mean E = {E.mean():+.5f};  max|E| = {np.abs(E).max():.4f}  "
              f"vs bound {(4*K*K-2)/K**2:.3f};  "
              f"[Tr V: mean {tr1.mean():.4f}, std {tr1.std():.4f}, "
              f"max {tr1.max():.4f}]  ({time.time()-t0:.0f} s)", flush=True)
    dest = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                        "artifacts", "r82", "second_moment_raw.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
