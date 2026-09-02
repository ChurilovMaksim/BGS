"""
UNITARY perturbation flow verification: U_eps = expm(i eps E) @ U_A.
Mirrors paper Lemma lem:perturb / Exp multi; also epsilon-sensitivity
at one prime. Replaces the earlier additive-model numbers.
"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment
from scipy.stats import kstest

sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat

ART = _BGS_ROOT + r"\artifacts"


def gue(n, rng):
    X = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    return (X + X.conj().T) / 2


def run_prime(p, eps=1e-4, seed=None, min_cluster=15, top=3):
    A = [2, 1, 1, 1]
    rng = np.random.default_rng(seed if seed is not None else p)
    U = U_cat(A, p)
    w0 = np.linalg.eigvals(U)
    E = gue(p, rng)
    # unitary flow via eigendecomposition of Hermitian E
    mu_e, V_e = np.linalg.eigh(E)
    Ue = (V_e * np.exp(1j * eps * mu_e)) @ V_e.conj().T @ U
    wp = np.linalg.eigvals(Ue)
    C = np.abs(wp[:, None] - w0[None, :])
    ri, ci = linear_sum_assignment(C)
    splits = {}
    maxd = 0.0
    for i, j in zip(ri, ci):
        maxd = max(maxd, C[i, j])
        key = (round(float(w0[j].real), 5), round(float(w0[j].imag), 5))
        splits.setdefault(key, []).append(float(np.angle(wp[i])))
    big = sorted((sorted(v) for v in splits.values() if len(v) >= min_cluster),
                 key=len, reverse=True)[:top]
    sp_all = []
    sizes = []
    for arr in big:
        arr = np.array(arr)
        d = np.diff(arr)
        d = d / d.mean()
        sp_all.extend(d.tolist())
        sizes.append(len(arr))
    sp = np.sort(np.array(sp_all))
    ks_wd, _ = kstest(sp, lambda x: 1 - np.exp(-np.pi * x * x / 4))   # GOE surmise
    ks_po, _ = kstest(sp, lambda x: 1 - np.exp(-x))                    # Poisson
    return dict(p=p, n=int(len(sp)), clusters=sizes,
                ks_wd=float(ks_wd), ks_poisson=float(ks_po),
                max_match_dist=float(maxd))


def main():
    print("=== Unitary-flow perturbation verification ===")
    rows = []
    for p in [1597, 2161, 2207, 3001]:
        r = run_prime(p)
        rows.append(r)
        print(f"p={p}: n={r['n']} clusters={r['clusters']} "
              f"KS_WD={r['ks_wd']:.4f} KS_Pois={r['ks_poisson']:.4f}")
    print("--- epsilon sensitivity at p=2207 ---")
    sens = []
    for eps in (1e-3, 1e-4, 1e-5):
        r = run_prime(2207, eps=eps, seed=99)
        sens.append(dict(eps=eps, n=r["n"], ks_wd=r["ks_wd"],
                         ks_poisson=r["ks_poisson"]))
        print(f"eps={eps:g}: n={r['n']} KS_WD={r['ks_wd']:.4f} "
              f"KS_Pois={r['ks_poisson']:.4f}")
    out = dict(unitary_rows=rows, epsilon_sensitivity=sens,
               model="U_eps = expm(i eps E) @ U_A, E ~ GUE(N)")
    json.dump(out, open(os.path.join(ART,
              "unitary_perturbation.json"), "w"), indent=1)
    print("saved artifacts/unitary_perturbation.json")


if __name__ == "__main__":
    main()
