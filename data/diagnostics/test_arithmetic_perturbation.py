"""ARITHMETIC perturbation test: U_eps = expm(i eps * Vt) U_A with
Vt = Hermitian Weyl combination (arithmetic, NOT random).
Q: do intra-multiplet splittings still follow GUE?
Refs built at matching dims m in {69,70,71}."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linear_sum_assignment

sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix

ART = _BGS_ROOT + r"\artifacts"
A = [2, 1, 1, 1]


def arithmetic_V(p):
    T10 = weyl_matrix(1, 0, p); T01 = weyl_matrix(0, 1, p)
    return T10 + T10.conj().T + 0.7 * (T01 + T01.conj().T)


def run_prime(p, eps=1e-4):
    U = U_cat(A, p)
    w0 = np.linalg.eigvals(U)
    Vt = arithmetic_V(p)
    Ue = expm(1j * eps * Vt) @ U
    del Vt
    wp = np.linalg.eigvals(Ue); del Ue
    Cm = np.abs(wp[:, None] - w0[None, :])
    ri, ci = linear_sum_assignment(Cm)
    splits = {}
    for i, j in zip(ri, ci):
        key = (round(float(w0[j].real), 5),
               round(float(w0[j].imag), 5))
        splits.setdefault(key, []).append(float(np.angle(wp[i])))
    big = sorted((sorted(v) for v in splits.values()
                  if len(v) >= 12), key=len, reverse=True)
    sp = []
    sizes = [len(b) for b in big]
    for arr in big:
        a_ = np.array(arr); d = np.diff(a_)
        sp.extend((d / d.mean()).tolist())
    return np.sort(np.array(sp)), sizes


def mc_ref(m, ens, trials, rng):
    out = []
    for _ in range(trials):
        X = rng.standard_normal((m, m))
        M = (X + X.T) / 2.0 if ens == "GOE" else \
            (X + X.T) / 2.0 + 1j * ((rng.standard_normal((m, m))
                                     - rng.standard_normal((m, m)).T) / 2.0)
        ev = np.linalg.eigvalsh(M)
        d = np.diff(ev); d /= d.mean(); out.extend(d.tolist())
    return out


def ks2(s_sorted, r_sorted):
    grid = np.unique(np.concatenate([r_sorted[::7], s_sorted]))
    cr = np.searchsorted(r_sorted, grid, side="right") / len(r_sorted)
    cs = np.searchsorted(s_sorted, grid, side="right") / len(s_sorted)
    return float(np.max(np.abs(cr - cs)))


def main():
    rng = np.random.default_rng(555)
    refs = {}
    for ens in ("GOE", "GUE"):
        parts = [mc_ref(m, ens, 1500, rng) for m in (69, 70, 71)]
        refs[ens] = np.sort(np.concatenate(parts))
    print("refs built:", {k: len(v) for k, v in refs.items()}, flush=True)

    results = {}
    for p in (2207, 4481):
        s, sizes = run_prime(p)
        k_goe = ks2(s, refs["GOE"])
        k_gue = ks2(s, refs["GUE"])
        results[p] = dict(n=int(len(s)),
                          mults=len(sizes),
                          size_min=int(min(sizes)) if sizes else None,
                          size_max=int(max(sizes)) if sizes else None,
                          ks_vs_goe=k_goe, ks_vs_gue=k_gue,
                          closer=("GOE" if k_goe < k_gue else "GUE"),
                          gap=abs(k_goe - k_gue))
        print(f"p={p}: n={len(s)} mults={len(sizes)} "
              f"KS_GOE={k_goe:.4f} KS_GUE={k_gue:.4f} "
              f"-> {results[p]['closer']}", flush=True)

    json.dump(results, open(os.path.join(
        ART, "arithmetic_perturbation.json"), "w"), indent=1)
    print("saved artifacts/arithmetic_perturbation.json")


if __name__ == "__main__":
    main()
