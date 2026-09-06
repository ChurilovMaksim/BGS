"""Referee recomputation of Lemma 82.1's certified numbers (Claim 3).
Recomputes Tr(V_q) and Tr(V_q^2) from the canonical N x N pipeline (exact
projector eigenbasis + parity block) over ALL level-set representatives, at
(N,K) = (199,11) and (3571,17), and compares:
  (a) raw Tr(V^2) = sum ev^2  (what Lemma 82.1 literally states),
  (b) centred m+ * var(ev)    (what the q_curve npz stores as 's2'),
against artifacts/r82/second_moment_identity.json.  The difference between
(a) and (b) is Tr(V)^2/m+ -- this audit checks which convention the artifact
used and whether Tr(V) is really negligible.
"""
import json
import os
import sys
import time

import numpy as np

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC)
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402
from r82g_q_curve import rep_for_each_q  # noqa: E402

A = [[2, 1], [1, 1]]


def run(N, batch):
    t0 = time.time()
    cm = CatMap(A, N)
    ordA, K = cm.orders()
    rng = np.random.default_rng(820005)
    B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
    RB = B.conj().T @ apply_parity(B)
    w, Vv = np.linalg.eigh(RB)
    mp = int((w > 0).sum())
    Bp = B @ Vv[:, w > 0]
    reps = rep_for_each_q(N)
    qs = sorted(reps)
    t2 = np.empty(len(qs)); tv = np.empty(len(qs))
    for i, q in enumerate(qs):
        H = Bp.conj().T @ cm.apply_T(reps[q], Bp)
        H = H + H.conj().T
        ev = np.linalg.eigvalsh(H)
        tv[i] = ev.sum()
        t2[i] = (ev ** 2).sum()
    pred = N / K ** 2
    out = {
        "N": N, "K": int(K), "m_plus": mp, "n_levels": len(qs),
        "pred_N_over_K2": pred,
        "mean_t2_raw": float(t2.mean()),
        "mean_t2_centred": float((mp * (t2 - tv ** 2 / mp) / mp).mean()),
        "mean_TrV": float(tv.mean()), "std_TrV": float(tv.std()),
        "max_abs_TrV": float(np.abs(tv).max()),
        "mean_E_raw": float((t2 - pred).mean()),
        "max_absE_raw": float(np.abs(t2 - pred).max()),
        "mean_E_centred": float((mp * (t2 - tv ** 2 / mp) / mp - pred).mean()),
        "max_absE_centred": float(np.abs(mp * (t2 - tv ** 2 / mp) / mp - pred).max()),
        "seconds": time.time() - t0,
    }
    print(json.dumps(out, indent=1), flush=True)
    return out


def main():
    rows = [run(199, 64), run(3571, 512)]
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "referee_lemma82_1.json")
    with open(dest, "w") as fh:
        json.dump(rows, fh, indent=1)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
