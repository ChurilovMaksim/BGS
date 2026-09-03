"""
run48b_support.py -- statistics vs number d of E-orbits in the support.

Implements the corrected version of the aborted run-48 sweep:
  * supports are UNIONS OF WHOLE E-ORBITS (roots inside a small box);
  * Hermitian completion by c_{-n} = conj(c_n);
  * statistic: bulk-restricted consecutive spacing ratios rtilde, pooled
    over MULTIPLETS s = 0..7 (a fixed subset -- enough for the trend),
    6 seeds per d;
  * controls at same m.
Prints progressively (python -u).
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bgs_core as bc                                            # noqa: E402
from run44_class import bulk_rtilde, control                     # noqa: E402

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
N_MULT = 8          # multiplets used in the sweep
SEEDS = 6


def orb_of(root, E, N):
    cur = np.array(root, dtype=np.int64) % N
    out = []
    for _ in range(4 * N):
        key = (int(cur[0]) % N, int(cur[1]) % N)
        out.append(key)
        cur = (E @ cur) % N
        if (int(cur[0]) % N, int(cur[1]) % N) == (root[0] % N, root[1] % N):
            break
    return out


def main():
    A = (2, 1, 1, 1)
    N = 2207
    k, sgn, K = bc.mat_order(A, N)
    chi, tres = bc.torsion_certificate_fft(A, N, K)
    E = np.array([[A[0], A[2]], [A[1], A[3]]], dtype=np.int64)
    bases = [bc.multiplet_basis_fft(A, N, K, chi, s) for s in range(N_MULT)]
    m = bases[0][2]
    g_c = control(m, N_MULT, "goe")["mean"]
    u_c = control(m, N_MULT, "gue")["mean"]
    print(f"A={A} p={N} K={K} m={m}; controls GOE {g_c:.4f} GUE {u_c:.4f}",
          flush=True)

    # distinct E-orbits whose root (centred) lies in the box
    roots, seen = [], set()
    box = 25
    for x in range(-box, box + 1):
        for y in range(-box, box + 1):
            if (x, y) == (0, 0):
                continue
            lab = (x % N, y % N)
            neg = ((N - x) % N, (N - y) % N)
            if lab in seen or neg in seen:
                continue
            o = orb_of(lab, E, N)
            seen |= set(o)
            seen |= {((N - a) % N, (N - b) % N) for a, b in o}
            roots.append(lab)
    print(f"distinct orbits with root in box {box}: {len(roots)}", flush=True)

    orbs = [orb_of(r, E, N) for r in roots]
    rows = []
    dgrid = sorted({1, 2, 4, 8, 16, 32, min(64, len(orbs)), len(orbs)})
    for d in dgrid:
        acc = []
        for sd in range(SEEDS):
            rng = np.random.default_rng(300 + sd)
            co = {}
            for orb in orbs[:d]:
                c = complex(rng.standard_normal(), rng.standard_normal())
                for l in orb:
                    co[l] = c / math.sqrt(2)      # one coefficient per ORBIT
            full = dict(co)
            for (n1, n2), c in co.items():
                full[((-n1) % N, (-n2) % N)] = np.conj(c)
            vals = []
            for (lam, B, mm, cert) in bases:
                VL = B.conj().T @ bc.weyl_sum_operator(full, N, B)
                VL = 0.5 * (VL + VL.conj().T)
                vals.append(bulk_rtilde(np.linalg.eigvalsh(VL)))
            rr = np.concatenate(vals)
            acc.append(round(float(rr.mean()), 4))
        row = dict(d=d, means=acc,
                   spread=round(float(np.std(acc)), 5))
        rows.append(row)
        print(f"d={d:>3}: <r> per seed {acc}  spread {row['spread']:.4f}",
              flush=True)
    rows.append(dict(d="ctrl", goe=g_c, gue=u_c))
    with open(os.path.join(ART, "run48_orbit_support.json"), "w") as f:
        json.dump(rows, f, indent=1, default=float)
    print("wrote artifacts/run48_orbit_support.json", flush=True)


if __name__ == "__main__":
    main()
