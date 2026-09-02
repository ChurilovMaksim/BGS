"""TASK A: entry-level Gaussianity of compressed Hermitian operators
at split small-K primes. Kurtosis + KS-vs-normal per entry class;
GOE reference for calibration. Answers: does KR-style entry
Gaussianity hold inside RAW multiplets, or only after Hecke
desymmetrisation?"""
import os as _os
_BGS_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sys, os, json
import numpy as np
from scipy import stats

sys.path.insert(0, _BGS_ROOT + r"\src")
from catmap_core import U_cat
from master_formula_r4 import weyl_matrix

ART = _BGS_ROOT + r"\artifacts"
A = [2, 1, 1, 1]


def compressed(p):
    U = U_cat(A, p)
    w, v = np.linalg.eig(U)
    from collections import Counter
    keys = Counter([(round(float(x.real), 5),
                     round(float(x.imag), 5)) for x in w])
    key, _ = keys.most_common(1)[0]
    idx = [i for i, x in enumerate(w) if abs(x - complex(*key)) < 1e-4]
    B = v[:, idx]; m = len(idx)
    T10 = weyl_matrix(1, 0, p); T01 = weyl_matrix(0, 1, p)
    V = T10 + T10.conj().T + 0.7 * (T01 + T01.conj().T)
    W = B.conj().T @ (V @ B)
    mu = np.trace(W) / m
    return W - mu * np.eye(m, dtype=complex), m


def entry_stats(Z, label):
    """Z: complex Hermitian; stats over off-diag entries + diagonal."""
    off_i, off_j = np.triu_indices(len(Z), 1)
    off = Z[off_i, off_j]
    re, im = off.real, off.imag
    diag = np.diag(Z).real
    out = {"class": label}
    for nm, arr in (("off_re", re), ("off_im", im), ("diag", diag)):
        kur = float(stats.kurtosis(arr, fisher=True, bias=False))
        ks, pv = stats.kstest(
            (arr - arr.mean()) / (arr.std() + 1e-300), "norm")
        out[nm] = dict(kurtosis=round(kur, 3), ks_norm=round(float(ks), 4),
                       p=float(f"{pv:.3g}"))
    return out


def main():
    rows = []
    # calibration: true GOE(m) entries
    rng = np.random.default_rng(7)
    X = rng.standard_normal((71, 71)); G = (X + X.T) / 2
    rows.append(entry_stats(G, "GOE(71) reference"))
    for p in (4481, 3571):
        W, m = compressed(p)
        rows.append(entry_stats(W, f"compressed p={p} (m={m})"))
        ev = np.linalg.eigvalsh(W)
        sd = ev.std()
        rows[-1]["ev_max/std"] = round(float(np.abs(ev).max() / sd), 2)
        rows[-1]["ev_kurtosis"] = round(float(
            stats.kurtosis(ev, fisher=True, bias=False)), 3)
        print(json.dumps(rows[-1], indent=1))
    json.dump(rows, open(os.path.join(
        ART, "taskA_entry_gaussianity.json"), "w"), indent=1)
    print("saved artifacts/taskA_entry_gaussianity.json")


if __name__ == "__main__":
    main()
