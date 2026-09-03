"""CRITICAL CHECK: was the R29 'heavy-tail' finding an artifact of an
INERT prime (p=2207)? Compare singular-value spread of compressed
Hermitian operators at SPLIT small-K primes vs inert 2207."""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np

sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix
from master_formula_strong import find_orbit_H

ART = _BGS_ROOT + r"\artifacts"


def compressed_stats(p):
    A = [2, 1, 1, 1]
    H = find_orbit_H(p, A)
    status = "split" if H else "inert"
    k = len(H) if H else None
    U = U_cat(A, p)
    w, v = np.linalg.eig(U)
    from collections import Counter
    keys = Counter([(round(float(x.real), 5),
                     round(float(x.imag), 5)) for x in w])
    key, _ = keys.most_common(1)[0]
    idx = [i for i, x in enumerate(w)
           if abs(x - complex(*key)) < 1e-4]
    m = len(idx)
    B = v[:, idx]                       # p x m eigenbasis
    T10 = weyl_matrix(1, 0, p); T01 = weyl_matrix(0, 1, p)
    V = T10 + T10.conj().T + 0.7 * (T01 + T01.conj().T)
    W = B.conj().T @ (V @ B)            # m x m Hermitian
    mu = np.trace(W) / m
    Wc = W - mu * np.eye(m, dtype=complex)
    sv = np.linalg.svd(Wc, compute_uv=False)
    spread = float(sv.max() / max(sv.min(), 1e-300))
    # second-largest / median ratios for robustness
    med = float(np.median(sv))
    return dict(p=p, status=status, k=k, m=m,
                sv_max=float(sv.max()), sv_min=float(sv.min()),
                sv_median=med,
                spread=spread,
                spread_robust=float(sv.max() / med))


def main():
    rows = []
    for p in [2207, 1597,          # inert controls
              3571, 4481, 5779]:   # split small-K targets
        try:
            r = compressed_stats(p)
        except MemoryError:
            print(f"p={p}: OOM"); continue
        rows.append(r)
        print(f"p={p} [{r['status']:5s}] m={r['m']:4d}: "
              f"sv_max/min={r['spread']:.3e}  "
              f"sv_max/med={r['spread_robust']:.2f}")
    json.dump(rows, open(os.path.join(
        ART, "check_split_vs_inert.json"), "w"), indent=1)
    print("saved artifacts/check_split_vs_inert.json")


if __name__ == "__main__":
    main()
