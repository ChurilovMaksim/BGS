"""
Run 81c: THE DECISIVE CONTROL for the rigidity excess.
======================================================
R81b established: the arithmetic ensemble {V_n} has semicircle-matching
density (KS = GOE's own) and matching mean counts, but 2.7x (m=105) to
5.7-7.9x (m=246) EXCESS variance of the bulk level counts across n.

Control: the SAME statistic for
  (a) the arithmetic parity block (the eigenspace),
  (b) HAAR-random subspaces of the same dimension compressing the SAME
      operators T(n)+T(-n),
  (c) plain GOE samples.
If (b) matches GOE (ratio ~ 1) and (a) does not, the excess is ARITHMETIC
(eigenspace structure).  If (b) also shows excess, the deviation belongs to
the operator family, not to the arithmetic subspace.

Also reports the window-resolved variance profile (is the excess spread or
concentrated at the edges?).

Output: artifacts/r81/rigidity_control.json
"""

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catmap_independent import CatMap  # noqa: E402
from compression_spacings import eigen_basis, orbit_reps  # noqa: E402
from parity_desymmetrised import apply_parity  # noqa: E402
from r81_local_law_pilot import goe_samples, semicircle_quantiles, count_var  # noqa: E402

A = [[2, 1], [1, 1]]


def main():
    out = {"script": "src/r81c_rigidity_control.py",
           "generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "designs": []}
    rng = np.random.default_rng(810811)
    nrep = 24
    nwin = 12

    for N, batch in ((3571, 512), (9349, 1024)):
        t0 = time.time()
        cm = CatMap(A, N)
        _, K = cm.orders()
        B, lam, m, res, chi = eigen_basis(cm, K, 0, batch, rng)
        RB = B.conj().T @ apply_parity(B)
        w, Vv = np.linalg.eigh(RB)
        mp = int((w > 0).sum())
        Bp = B @ Vv[:, w > 0]
        reps = orbit_reps(cm, K, nrep, rng)

        # (a) arithmetic block
        evs_a = []
        for u in reps:
            H = Bp.conj().T @ cm.apply_T(u, Bp)
            H = H + H.conj().T
            ev = np.linalg.eigvalsh(H)
            ev = ev - ev.mean()
            evs_a.append(ev / np.sqrt((ev ** 2).mean()))
        evs_a = np.array(evs_a)
        gref = goe_samples(mp, nrep, rng)
        quant = semicircle_quantiles(mp, nwin)
        cnt_a = np.array([count_var(e, quant) for e in evs_a])
        cnt_g = np.array([count_var(e, quant) for e in gref])
        var_a = cnt_a.var(axis=0, ddof=1).mean()
        var_g = cnt_g.var(axis=0, ddof=1).mean()

        # (b) Haar control: random N x mp subspaces, SAME operators
        evs_h = []
        for u in reps:
            Z = (rng.standard_normal((N, mp)) +
                 1j * rng.standard_normal((N, mp)))
            Q, _ = np.linalg.qr(Z)
            Y = Q.conj().T @ (cm.apply_T(u, Q) + cm.apply_T((-u[0], -u[1]), Q))
            Y = (Y + Y.conj().T) / 2
            ev = np.linalg.eigvalsh(Y)
            ev = ev - ev.mean()
            evs_h.append(ev / np.sqrt((ev ** 2).mean()))
        evs_h = np.array(evs_h)
        cnt_h = np.array([count_var(e, quant) for e in evs_h])
        var_h = cnt_h.var(axis=0, ddof=1).mean()

        row = {"N": N, "K": int(K), "m_plus": mp, "nrep": nrep,
               "var_arith": var_a, "var_haar": var_h, "var_goe": var_g,
               "ratio_arith_over_goe": var_a / var_g,
               "ratio_haar_over_goe": var_h / var_g,
               "var_profile_arith": cnt_a.var(axis=0, ddof=1).tolist(),
               "var_profile_goe": cnt_g.var(axis=0, ddof=1).tolist()}
        out["designs"].append(row)
        print(f"=== N={N} m+={mp} ({time.time()-t0:.0f} s)", flush=True)
        print(f"  count-var ratio: arithmetic/GOE = {var_a/var_g:.2f}   "
              f"Haar/GOE = {var_h/var_g:.2f}", flush=True)
        print(f"  variance profile (arith): "
              f"{[round(x,2) for x in row['var_profile_arith']]}", flush=True)
        print(f"  variance profile (GOE):   "
              f"{[round(x,2) for x in row['var_profile_goe']]}", flush=True)

    dest = os.path.join("artifacts", "r81", "rigidity_control.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1, default=str)
    print("artifact ->", os.path.normpath(dest), flush=True)


if __name__ == "__main__":
    main()
