"""
run44_class.py -- what actually controls the Dyson class of the multiplet
splitting?  A campaign over cat maps A and primes p of BOTH torsion signs
(A^k = +I vs A^k = -I mod p), with parity always broken.

Protocol (fixed before the run; see LEDGER "RUN 44 PREREGISTRATION"):
  * observable: Hermitian V = sum_n c_n T(n) over a label set closed under
    n -> R^T n and n -> -n, with |n| small; coefficients COMPLEX (so
    [Pi,V] != 0: the parity superposition artefact of runs 1-43 is removed).
  * two modes: 'sym'  = c_{R^T n} = conj(c_n)  (i.e. [Theta,V] = 0, TRS)
               'gen'  = unconstrained          (TRS broken)
  * statistic: unfolding-free consecutive spacing ratios rtilde = min(r,1/r),
    restricted to the BULK (central 70%) of each multiplet spectrum, pooled
    over all K multiplets.
  * controls: GOE and GUE of the same block size and sample count, same bulk
    restriction; reference means 0.5359 (GOE), 0.5996 (GUE), 0.3863 (Poisson).
  * decision: |<r> - GOE| vs |<r> - GUE| in units of the pooled s.e.m.
"""
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import bgs_core as bc                                            # noqa: E402
from run43_parity import build_coeffs, close_labels              # noqa: E402

ART = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "artifacts")
FREQS = [(1, 0), (0, 1), (1, 1), (1, -1), (2, 0), (0, 2)]
BULK = 0.70

CONFIGS = [
    # (name, A, p)   -- selected by ord_p(A) small, m = p//K >= 68
    ("t3", (2, 1, 1, 1), 2207), ("t3", (2, 1, 1, 1), 3571),
    ("t3", (2, 1, 1, 1), 5779),
    ("t4", (3, 1, 2, 1), 2017), ("t4", (3, 1, 2, 1), 2131),
    ("t4", (3, 1, 2, 1), 2521), ("t4", (3, 1, 2, 1), 2543),
    ("t4", (3, 1, 2, 1), 3361), ("t4", (3, 1, 2, 1), 3691),
    ("t6", (5, 2, 2, 1), 4663), ("t6", (5, 2, 2, 1), 5521),
    ("t6", (5, 2, 2, 1), 5741),
    ("t7", (3, 1, 5, 2), 2089), ("t7", (3, 1, 5, 2), 3191),
    ("t7", (3, 1, 5, 2), 5147),
]


def bulk_rtilde(levels, frac=BULK):
    x = np.sort(np.asarray(levels, dtype=float))
    n = len(x)
    lo = int(round((1 - frac) / 2 * n))
    x = x[lo:n - lo]
    s = np.diff(x)
    s = s[s > 0]
    if len(s) < 3:
        return np.array([])
    r = s[1:] / s[:-1]
    return np.minimum(r, 1.0 / r)


def control(m, K, kind, seed=17, reps=3):
    rng = np.random.default_rng(seed)
    acc = []
    for _ in range(reps * K):
        if kind == "goe":
            G = rng.standard_normal((m, m))
            H = (G + G.T) / math.sqrt(2)
        else:
            G = (rng.standard_normal((m, m)) +
                 1j * rng.standard_normal((m, m))) / math.sqrt(2)
            H = (G + G.conj().T) / math.sqrt(2)
        acc.append(bulk_rtilde(np.linalg.eigvalsh(H)))
    rr = np.concatenate([a for a in acc if len(a)])
    return dict(mean=float(rr.mean()), n=int(len(rr)),
                sem=float(rr.std(ddof=1) / math.sqrt(len(rr))),
                hist=np.histogram(rr, bins=20, range=(0, 1))[0].tolist())


def one_config(name, A, N, seed=3):
    k, sign, K = bc.mat_order(A, N)
    chi, tres = bc.torsion_certificate_fft(A, N, K, seed=seed)
    Rs = [Rx for Rx in bc.reversing_involution(A) if (-int(Rx[2])) % N != 0]
    R = Rs[0]
    RT = np.array([[R[0], R[2]], [R[1], R[3]]], dtype=np.int64)
    negI = -np.eye(2, dtype=np.int64)
    labels = close_labels(FREQS, [RT, negI], N)
    M = (R[0], R[1], -R[2], -R[3])            # M = S R, S = diag(1,-1)

    out = dict(name=name, A=list(A), N=N, k=k, sign=int(sign), K=K,
               torsion_res=tres, n_labels=len(labels), R=list(R))
    bases = []
    for s in range(K):
        lam, B, m, cert = bc.multiplet_basis_fft(A, N, K, chi, s, seed=seed)
        bases.append((B, m, cert))
    out["m"] = int(bases[0][1])
    out["max_cert"] = float(max(b[2] for b in bases))
    out["sum_m"] = int(sum(b[1] for b in bases))

    for mode in ("sym", "gen"):
        rng = np.random.default_rng(seed + 100)
        gens = [(negI, True)]
        if mode == "sym":
            gens.append((RT, True))
        coeffs = build_coeffs(labels, N, rng, gens)
        # symmetry certificates on a random probe block (FFT propagators only)
        probe = np.linalg.qr(np.random.default_rng(0).standard_normal((N, 6)) +
                             1j * np.random.default_rng(1).standard_normal((N, 6)))[0]
        VP = bc.weyl_sum_operator(coeffs, N, probe)
        out[f"{mode}_parity_dev"] = float(np.max(np.abs(
            bc.apply_parity(VP) - bc.weyl_sum_operator(
                coeffs, N, bc.apply_parity(probe)))))
        out[f"{mode}_theta_dev"] = float(np.max(np.abs(
            bc.theta_apply(M, N, coeffs, probe) - VP)))

        acc = []
        for (B, m, cert) in bases:
            VL = B.conj().T @ bc.weyl_sum_operator(coeffs, N, B)
            VL = 0.5 * (VL + VL.conj().T)
            acc.append(bulk_rtilde(np.linalg.eigvalsh(VL)))
        rr = np.concatenate([a for a in acc if len(a)])
        out[f"{mode}_r"] = dict(mean=float(rr.mean()), n=int(len(rr)),
                                sem=float(rr.std(ddof=1) / math.sqrt(len(rr))),
                                hist=np.histogram(rr, bins=20,
                                                  range=(0, 1))[0].tolist())
    out["ctrl_goe"] = control(out["m"], K, "goe")
    out["ctrl_gue"] = control(out["m"], K, "gue")
    return out


def main():
    rows = []
    for (name, A, N) in CONFIGS:
        try:
            out = one_config(name, A, N)
        except Exception as exc:                                  # noqa: BLE001
            print(f"!! {name} p={N}: {type(exc).__name__}: {exc}")
            continue
        rows.append(out)
        g, u = out["ctrl_goe"], out["ctrl_gue"]
        line = (f"{name:>4} p={N:<5} sign={out['sign']:+d} K={out['K']:<3} "
                f"m={out['m']:<4} cert={out['max_cert']:.1e} ")
        for mode in ("sym", "gen"):
            d = out[f"{mode}_r"]
            zg = (d["mean"] - g["mean"]) / math.hypot(d["sem"], g["sem"])
            zu = (d["mean"] - u["mean"]) / math.hypot(d["sem"], u["sem"])
            line += (f"| {mode} <r>={d['mean']:.4f}+-{d['sem']:.4f} "
                     f"zGOE={zg:+.1f} zGUE={zu:+.1f} ")
        line += f"| ctrl GOE {g['mean']:.4f} GUE {u['mean']:.4f}"
        print(line, flush=True)
        with open(os.path.join(ART, "run44_class.json"), "w") as f:
            json.dump(rows, f, indent=1, default=float)
    print("\nwrote artifacts/run44_class.json")

    # pooled by torsion sign
    for sg in (+1, -1):
        for mode in ("sym", "gen"):
            sel = [r for r in rows if r["sign"] == sg]
            if not sel:
                continue
            num = sum(r[f"{mode}_r"]["mean"] * r[f"{mode}_r"]["n"] for r in sel)
            den = sum(r[f"{mode}_r"]["n"] for r in sel)
            gc = sum(r["ctrl_goe"]["mean"] * r["ctrl_goe"]["n"] for r in sel) / \
                sum(r["ctrl_goe"]["n"] for r in sel)
            uc = sum(r["ctrl_gue"]["mean"] * r["ctrl_gue"]["n"] for r in sel) / \
                sum(r["ctrl_gue"]["n"] for r in sel)
            print(f"pooled sign={sg:+d} {mode}: <r>={num/den:.4f} (n={den}) "
                  f"ctrl GOE {gc:.4f} GUE {uc:.4f}")


if __name__ == "__main__":
    main()

