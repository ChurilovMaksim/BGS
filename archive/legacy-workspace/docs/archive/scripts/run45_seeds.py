"""
run45_seeds.py -- is the observed Dyson class a property of (A,p) or of the
observable V?

Run 44 found: for A^k = +I mod p (K odd) the classical dichotomy holds
(TRS-invariant V -> GOE, generic V -> GUE), but for A^k = -I mod p (K even)
6 of 8 configurations gave GOE even for a TRS-BROKEN V, while 2 (A = (3,1,5,2))
gave GUE.  Two hypotheses:

  H-A  the class is fixed by the arithmetic of (A,p) [then all seeds agree];
  H-B  the class is fixed by the observable [then seeds disagree].

Discriminator: 6 independent coefficient seeds per configuration, plus a
variant with a larger frequency set (|n| <= 3, more E-orbits in play).
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bgs_core as bc                                            # noqa: E402
from run43_parity import build_coeffs, close_labels              # noqa: E402
from run44_class import bulk_rtilde, control                     # noqa: E402

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
SMALL = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 0), (0, 2)]
BIG = [(a, b) for a in range(-3, 4) for b in range(-3, 4)
       if (a, b) != (0, 0)]

CONFIGS = [
    ("t3", (2, 1, 1, 1), 2207),      # sign -1, gave GOE for generic V
    ("t4", (3, 1, 2, 1), 2131),      # sign -1, gave GOE
    ("t7", (3, 1, 5, 2), 2089),      # sign -1, gave GUE
    ("t3", (2, 1, 1, 1), 3571),      # sign +1, gave GUE (reference)
    ("t4", (3, 1, 2, 1), 2017),      # sign +1, gave GUE (reference)
]


def orbit_labels(labels, E, N):
    """Group labels into E-orbits; return (orbit_id per label, orbits)."""
    seen = {}
    orbits = []
    for lab in labels:
        if lab in seen:
            continue
        cur = np.array(lab, dtype=np.int64)
        orb = []
        for _ in range(4 * N):
            key = (int(cur[0]) % N, int(cur[1]) % N)
            orb.append(key)
            cur = (E @ cur) % N
            if (int(cur[0]) % N, int(cur[1]) % N) == lab:
                break
        oid = len(orbits)
        orbits.append(orb)
        for key in orb:
            seen[key] = oid
    return seen, orbits


def one(name, A, N, freqs, seeds=(1, 2, 3, 4, 5, 6), mode="gen"):
    k, sign, K = bc.mat_order(A, N)
    chi, tres = bc.torsion_certificate_fft(A, N, K)
    E = np.array([[A[0], A[2]], [A[1], A[3]]], dtype=np.int64)
    Rs = [Rx for Rx in bc.reversing_involution(A) if (-int(Rx[2])) % N != 0]
    R = Rs[0]
    RT = np.array([[R[0], R[2]], [R[1], R[3]]], dtype=np.int64)
    negI = -np.eye(2, dtype=np.int64)
    labels = close_labels(freqs, [RT, negI], N)
    seen, orbits = orbit_labels(labels, E, N)
    n_orb = len(orbits)
    bases = [bc.multiplet_basis_fft(A, N, K, chi, s) for s in range(K)]
    m = bases[0][2]
    res = dict(name=name, A=list(A), N=N, sign=int(sign), K=K, m=int(m),
               n_labels=len(labels), n_orbits=n_orb, mode=mode,
               max_cert=float(max(b[3] for b in bases)), rows=[])
    for sd in seeds:
        rng = np.random.default_rng(1000 + sd)
        gens = [(negI, True)]
        if mode == "sym":
            gens.append((RT, True))
        coeffs = build_coeffs(labels, N, rng, gens)
        acc = []
        for (lam, B, mm, cert) in bases:
            VL = B.conj().T @ bc.weyl_sum_operator(coeffs, N, B)
            VL = 0.5 * (VL + VL.conj().T)
            acc.append(bulk_rtilde(np.linalg.eigvalsh(VL)))
        rr = np.concatenate([a for a in acc if len(a)])
        res["rows"].append(dict(seed=sd, mean=float(rr.mean()), n=int(len(rr)),
                                sem=float(rr.std(ddof=1) / math.sqrt(len(rr)))))
    res["ctrl_goe"] = control(m, K, "goe")
    res["ctrl_gue"] = control(m, K, "gue")
    return res


def main():
    rows = []
    for tag, freqs in (("small", SMALL), ("big", BIG)):
        for (name, A, N) in CONFIGS:
            out = one(name, A, N, freqs)
            out["freqset"] = tag
            rows.append(out)
            g, u = out["ctrl_goe"]["mean"], out["ctrl_gue"]["mean"]
            means = " ".join(f"{r['mean']:.4f}" for r in out["rows"])
            pooled = sum(r["mean"] * r["n"] for r in out["rows"]) / \
                sum(r["n"] for r in out["rows"])
            ntot = sum(r["n"] for r in out["rows"])
            sem = out["rows"][0]["sem"] / math.sqrt(len(out["rows"]))
            verdict = "GOE" if abs(pooled - g) < abs(pooled - u) else "GUE"
            print(f"{tag:>5} {name:>3} p={N:<5} sign={out['sign']:+d} K={out['K']:<3} "
                  f"m={out['m']:<4} orbits={out['n_orbits']:<3} seeds[{means}] "
                  f"pooled={pooled:.4f}+-{sem:.4f} (n={ntot}) "
                  f"ctrl {g:.4f}/{u:.4f} -> {verdict}", flush=True)
            with open(os.path.join(ART, "run45_seeds.json"), "w") as f:
                json.dump(rows, f, indent=1, default=float)
    print("wrote artifacts/run45_seeds.json")


if __name__ == "__main__":
    main()

