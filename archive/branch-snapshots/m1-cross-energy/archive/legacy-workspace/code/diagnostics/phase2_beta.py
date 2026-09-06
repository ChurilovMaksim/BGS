"""PHASE 2: beta-discrimination at large n.
Primes with small projective order in (3000,6600]; unitary flow;
per-prime KS + pooled GOE-vs-GUE resolution."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from sympy import primerange
from scipy.optimize import linear_sum_assignment
from scipy.stats import kstest
from scipy.interpolate import interp1d

sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat

ART = _BGS_ROOT + r"\artifacts"
A = [2, 1, 1, 1]


def proj_order(p):
    """Least n with A^n == +-I (mod p) -- the projective order itself
    (audit fix 2026-08-26: an earlier version returned n//2, halving
    the true order; that produced the wrong K labels in exp:beta)."""
    Am = np.array(A).reshape(2, 2) % p
    I = np.eye(2, dtype=int)
    negI = (-I) % p
    X = Am.copy()
    n = 1
    while n <= 4 * p:
        if np.array_equal(X % p, I):
            return n
        if np.array_equal(X % p, negI):
            return n
        X = (X @ Am) % p
        n += 1
    return None


def find_primes(lo=3000, hi=6600, kmax=17):
    out = []
    for p in primerange(lo, hi):
        K = proj_order(p)
        if K and K <= kmax:
            out.append((int(p), int(K)))
    return out


def unitary_spacings(p, eps=1e-4, seed=None, min_cluster=12, top=99):
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
    big = sorted((sorted(v) for v in splits.values()
                  if len(v) >= min_cluster), key=len, reverse=True)[:top]
    sp, sizes = [], [len(b) for b in big]
    for arr in big:
        a_ = np.array(arr)
        d = np.diff(a_)
        sp.extend((d / d.mean()).tolist())
    return sp, sizes


def gue_cdf(x_max):
    grid = np.linspace(0.0, x_max, 40000)
    pdf = (32.0 / np.pi ** 2) * grid ** 2 * np.exp(-4.0 * grid ** 2 / np.pi)
    dx = grid[1] - grid[0]
    c = np.cumsum(pdf) * dx
    c /= c[-1]
    return interp1d(grid, c, bounds_error=False, fill_value=(0.0, 1.0))


def main():
    print("searching primes...", flush=True)
    cands = find_primes()
    print("candidates:", cands, flush=True)
    chosen = sorted([t for t in cands if t[1] <= 17],
                    key=lambda t: t[0])[-5:]
    print("chosen:", chosen, flush=True)

    all_sp, per_prime = [], []
    for p, K in chosen:
        sp, sizes = unitary_spacings(p)
        s = np.sort(np.array(sp))
        kw, _ = kstest(s, lambda x: 1 - np.exp(-np.pi * x * x / 4))
        kp_, _ = kstest(s, lambda x: 1 - np.exp(-x))
        per_prime.append(dict(p=p, K=K, n=int(len(s)),
                              ks_wd=float(kw), ks_poisson=float(kp_),
                              clusters_head=sizes[:8]))
        all_sp.extend(sp)
        print(f"p={p} K={K}: mults={len(sizes)} n={len(s)} "
              f"KS_WD={kw:.4f}", flush=True)

    s = np.sort(np.array(all_sp))
    n = len(s)
    Fg = gue_cdf(max(float(s.max()), 5.0))
    kw, _ = kstest(s, lambda x: 1 - np.exp(-np.pi * x * x / 4))
    kg, _ = kstest(s, Fg)
    kp_, _ = kstest(s, lambda x: 1 - np.exp(-x))
    crit = 1.36 / np.sqrt(n)
    sep = abs(kw - kg)
    closer = "GOE" if kw < kg else "GUE"
    print(f"\nPOOLED n={n}: KS_GOE={kw:.4f} KS_GUE={kg:.4f} "
          f"KS_Pois={kp_:.4f} crit5%={crit:.4f}")
    print(f"closer={closer}; separation {sep:.4f} "
          f"{'RESOLVED' if sep > crit else 'NOT resolved'}")

    # ---- MC reference comparison (removes surmise systematics) ----
    sizes_all = [mm // 1 for pp in per_prime for mm in []]  # placeholder
    # rebuild multiplet sizes by re-collecting during loop would be heavy;
    # instead sample matrix dims from observed cluster-size distribution
    # recorded per prime head; use representative dims set:
    dims = sorted({d for pp in per_prime for d in
                   range(max(6, min(pp["clusters_head"]) if pp["clusters_head"] else 12),
                         75)})
    rng = np.random.default_rng(20260826)
    def mc_pool(ens, trials=3500):
        pool = []
        for _ in range(trials):
            m = int(rng.choice(dims))
            X = rng.normal(size=(m, m))
            M = (X + X.T) / 2 if ens == "GOE" else \
                ((X + 1j * rng.normal(size=(m, m)))
                 + (X + 1j * rng.normal(size=(m, m))).conj().T) / 2
            ev = np.linalg.eigvalsh(M)
            d_ = np.diff(ev); d_ /= d_.mean()
            pool.extend(d_.tolist())
        return np.sort(np.array(pool))
    ref_goe = mc_pool("GOE")
    ref_gue = mc_pool("GUE")
    Fg_e = lambda arr: interp1d(np.linspace(0, max(arr.max(), 5), 20000),
                                None) if False else None
    def ecdf_test(sample_sorted, ref_sorted):
        nr, ns = len(ref_sorted), len(sample_sorted)
        grid = np.concatenate([ref_sorted, sample_sorted])
        cdf_r = np.searchsorted(ref_sorted, grid, side="right") / nr
        cdf_s = np.searchsorted(sample_sorted, grid, side="right") / ns
        return float(np.max(np.abs(cdf_r - cdf_s)))
    ks_mc_goe = ecdf_test(s, ref_goe)
    ks_mc_gue = ecdf_test(s, ref_gue)
    sep2 = abs(ks_mc_goe - ks_mc_gue)
    crit_ref = 1.36 * np.sqrt(1.0 / n + 1.0 / len(ref_goe))
    closer2 = "GOE" if ks_mc_goe < ks_mc_gue else "GUE"
    print(f"MC-reference (|ref|={len(ref_goe)}): "
          f"KS_vs_GOE={ks_mc_goe:.4f} KS_vs_GUE={ks_mc_gue:.4f}; "
          f"gap={sep2:.4f} crit~{crit_ref:.4f} -> "
          f"{closer2} "
          f"{'RESOLVED' if sep2 > crit_ref else 'not resolved'}")

    out = dict(per_prime=per_prime,
               pooled=dict(n=int(n), ks_goe=float(kw), ks_gue=float(kg),
                           ks_poisson=float(kp_), crit5=float(crit),
                           closer=closer, gap=float(sep),
                           separated=bool(sep > crit)),
               mc_reference=dict(ref_size=int(len(ref_goe)),
                                 ks_vs_goe=float(ks_mc_goe),
                                 ks_vs_gue=float(ks_mc_gue),
                                 gap=float(sep2),
                                 crit=float(crit_ref),
                                 closer=closer2,
                                 resolved=bool(sep2 > crit_ref)))
    json.dump(out, open(os.path.join(ART, "phase2_beta.json"), "w"),
              indent=1)
    print("saved artifacts/phase2_beta.json")


if __name__ == "__main__":
    main()
