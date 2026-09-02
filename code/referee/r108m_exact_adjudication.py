r"""R108m -- EXACT ADJUDICATION of the dichotomy theorem + DC formula.

Theorem (proved by orthogonality on S = (F_N^*\{1})^2 \ {u=v}):
  Ahat_{j1,j2}(0) = sum_{(u,v) in S} chi^{j1}(u) chi^{j2}(v)
    = (N-2)(N-3)                if (j1,j2) = (0,0)
    = -(N-3)                    if j1==0 or j2==0 or (j1+j2)%m==0
    = +2                        otherwise.
  Y_sum(0) = (N-2)^2 (N-3)^2 + (3m-3)(N-3)^2 + 4(m^2-3m+2)  (exact).

Verification: direct one-stage 2D DFT of the (m,m) key-exponent count
matrix (NOT the 3-stage FFT pipeline) -- independent code path, fp err
~1e-12.  Plus the Y_sum(0) closed formula vs pipeline value.
"""
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108m_exact_adjudication.log")

sys.path.insert(0, HERE)
from r108_k4_independent import (  # noqa: E402
    build_keys, discrete_log_table as dlog_table,
    multiplicative_order, primitive_root,
)


def log(msg):
    print(str(msg), flush=True)
    with open(LOG_PATH, "a", encoding="utf-8") as fh:
        fh.write(str(msg) + "\n")


def run(N, a):
    K = multiplicative_order(a, N)
    m = (N - 1) // K
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    u, v, d, mult = build_keys(N)
    is_diag = mult == (N - 2)
    uo = u[~is_diag].astype(np.int64)
    vo = v[~is_diag].astype(np.int64)
    c1o = (dlog[uo] % m).astype(np.int64)
    c2o = (dlog[vo] % m).astype(np.int64)
    nkeys = len(uo)
    assert nkeys == (N - 2) * (N - 3), nkeys

    # (m, m) count matrix of key exponents; one-stage 2D DFT
    Cnts = np.bincount(c1o * m + c2o, minlength=m * m).reshape(m, m)
    E = np.exp((-2j * np.pi / m) * np.outer(np.arange(m), np.arange(m)))
    Ahat0 = E @ Cnts @ E          # Ahat0[j1, j2] = complete twisted sum

    j1g, j2g = np.meshgrid(np.arange(m), np.arange(m), indexing="ij")
    crit = (j1g == 0) | (j2g == 0) | (((j1g + j2g) % m) == 0)
    target = np.where((j1g == 0) & (j2g == 0), (N - 2) * (N - 3),
                      np.where(crit, -(N - 3), 2.0))
    err = np.abs(Ahat0 - target) / np.maximum(np.abs(target), 1)
    worst = float(err.max())
    ok = bool(np.all(err < 1e-9))
    log(f"=== N={N} K={K} m={m}: one-stage 2D DFT, {m*m} pairs, "
        f"worst rel err {worst:.2e}  {'ALL PASS' if ok else 'FAIL'}")

    # Y_sum(0) exact formula vs direct sum of Ahat^2
    ysum0_formula = ((N - 2)**2 * (N - 3)**2
                     + (3 * m - 3) * (N - 3)**2
                     + 4 * (m * m - 3 * m + 2))
    ysum0_direct = float(np.real(np.sum(Ahat0**2)))
    rel = abs(ysum0_direct - ysum0_formula) / ysum0_formula
    log(f"  Y_sum(0): formula {ysum0_formula:.6e} vs direct {ysum0_direct:.6e} "
        f"(rel {rel:.2e}) {'PASS' if rel < 1e-9 else 'FAIL'}")
    try:
        import json as _json
        kk = _json.load(open(os.path.join(OUT_DIR, "r108k_collective.json")))
        yk = kk.get(f"N{N}", {}).get("Ysum0")
        if yk:
            log(f"  FFT-pipeline Y_sum(0) = {yk:.6e} vs formula "
                f"{ysum0_formula:.6e} (rel {abs(yk - ysum0_formula)/ysum0_formula:.2e})")
    except Exception:
        pass
    return dict(N=N, m=m, worst_rel=worst, all_pass=ok,
                Ysum0=float(ysum0_formula), Ysum0_direct=ysum0_direct)


def main():
    log("R108m: exact adjudication of the dichotomy theorem + DC formula")
    for N, a in ((199, 139), (1229, 746), (1511, 347), (2161, 48),
                 (2521, 323), (3001, 124), (4969, 72), (5081, 1032)):
        run(N, a)
    log("done")


if __name__ == "__main__":
    main()
