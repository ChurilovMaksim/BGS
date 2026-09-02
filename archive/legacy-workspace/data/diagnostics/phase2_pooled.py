"""PHASE 2a: pooled spacings at large p (unitary flow) -> save to disk."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from sympy import primerange
from scipy.optimize import linear_sum_assignment
from scipy.stats import kstest

sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat

ART = _BGS_ROOT + r"\artifacts"
A = [2, 1, 1, 1]
# audit fix 2026-08-26: K labels corrected to true projective orders
# (least n with A^n == +-I); the earlier labels 8/16/13 were halves.
CHOSEN = [(3571, 17), (4481, 32), (5779, 27)]


def unitary_spacings(p, eps=1e-4, seed=None):
    rng = np.random.default_rng(seed if seed is not None else p)
    U = U_cat(A, p)
    w0 = np.linalg.eigvals(U)
    X = rng.normal(size=(p, p)) + 1j * rng.normal(size=(p, p))
    E = (X + X.conj().T) / 2.0
    mu, V = np.linalg.eigh(E)
    Ue = (V * np.exp(1j * eps * mu)) @ V.conj().T @ U
    del X
    wp = np.linalg.eigvals(Ue)
    del Ue, V, mu, E, U
    Cm = np.abs(wp[:, None] - w0[None, :])
    ri, ci = linear_sum_assignment(Cm)
    splits = {}
    for i, j in zip(ri, ci):
        key = (round(float(w0[j].real), 5),
               round(float(w0[j].imag), 5))
        splits.setdefault(key, []).append(float(np.angle(wp[i])))
    big = sorted((sorted(v) for v in splits.values() if len(v) >= 12),
                 key=len, reverse=True)
    sp, sizes = [], [len(b) for b in big]
    for arr in big:
        a_ = np.array(arr)
        d = np.diff(a_)
        sp.extend((d / d.mean()).tolist())
    return sp, sizes


def main():
    all_sp, per_prime = [], []
    for p, K in CHOSEN:
        sp, sizes = unitary_spacings(p)
        s = np.sort(np.array(sp))
        kw, _ = kstest(s, lambda x: 1 - np.exp(-np.pi * x * x / 4))
        kp_, _ = kstest(s, lambda x: 1 - np.exp(-x))
        per_prime.append(dict(p=p, K=K, n=int(len(s)),
                              ks_wd=float(kw), ks_poisson=float(kp_),
                              n_multiplets=len(sizes),
                              size_min=int(min(sizes)),
                              size_max=int(max(sizes))))
        all_sp.extend(sp)
        print(f"p={p} K={K}: mults={len(sizes)} "
              f"sizes[{min(sizes)}..{max(sizes)}] n={len(s)} "
              f"KS_WD={kw:.4f}", flush=True)

    s = np.sort(np.array(all_sp)).astype(np.float64)
    np.save(os.path.join(ART, "phase2_spacings.npy"), s)
    crit = 1.36 / np.sqrt(len(s))
    kw, _ = kstest(s, lambda x: 1 - np.exp(-np.pi * x * x / 4))
    kp_, _ = kstest(s, lambda x: 1 - np.exp(-x))
    out = dict(per_prime=per_prime,
               pooled=dict(n=int(len(s)), ks_goe_surrogate=float(kw),
                           ks_poisson=float(kp_), crit5=float(crit)))
    json.dump(out, open(os.path.join(ART, "phase2_summary.json"), "w"),
              indent=1)
    print(f"POOLED n={len(s)} KS_WD(surro)={kw:.4f} "
          f"crit={crit:.4f}; spacings saved.", flush=True)


if __name__ == "__main__":
    main()
