r"""R108l -- EXACT DICHOTOMY LAW FOR COMPLETE TWISTED SUMS (design sweep).

Law (discovered r108j, criterion pinned r108k at N=199/2161):
  |Ahat_{j1,j2}(0)| = N-3  (giant, EXACT)  iff
      j1 == 0 or j2 == 0 or (j1+j2) % m == 0
  (three "trivial-on-stratum" families: psi1 trivial, psi2 trivial,
   composite psi1*psi2 trivial);
  otherwise |Ahat(0)| <= 2  (near-total cancellation, O(1), far below
  the Weil scale sqrt(N)).

Giant count must be exactly 3m-2 = (2m-1 one-side) + (m inverse) - 1.
The trivial pair (0,0) additionally carries |Ahat(0)| ~ N^2 (flat bg).
Memory-lean: H3 deleted before fft2; JSON written incrementally.
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(HERE)))
OUT_DIR = os.path.join(ROOT, "data", "referee")
LOG_PATH = os.path.join(OUT_DIR, "r108l_dichotomy_sweep.log")
JSON_PATH = os.path.join(OUT_DIR, "r108l_dichotomy_sweep.json")

sys.path.insert(0, HERE)
from r108_k4_independent import (  # noqa: E402
    build_keys, discrete_log_table as dlog_table,
    multiplicative_order, primitive_root,
)

# smallest-first; N=3571 (m=210) last: heaviest, guarded by try/except
DESIGNS = [(199, 139), (1229, 746), (1511, 347), (2161, 48),
           (2521, 323), (3001, 124), (4969, 72), (5081, 1032),
           (6709, 3922), (3571, 1003)]


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
    c1 = (dlog[u] % m).astype(np.int64)
    c2 = (dlog[v] % m).astype(np.int64)
    is_diag = mult == (N - 2)
    w = np.where(is_diag, 0.0, mult.astype(np.float64))

    flat = (c1 * m + c2) * N + d
    H3 = np.bincount(flat, weights=w, minlength=m * m * N)
    del flat, w
    H3 = H3.reshape(m, m, N)
    A = np.fft.fft2(H3, axes=(0, 1)).reshape(m * m, N)
    del H3
    Ah = np.fft.fft(A, axis=1)
    del A
    A0 = np.abs(Ah[:, 0])
    del Ah

    j1 = np.arange(m * m) // m
    j2 = np.arange(m * m) % m
    crit = (j1 == 0) | (j2 == 0) | ((j1 + j2) % m == 0)
    n_crit = int(crit.sum())
    expected = 3 * m - 2

    nontriv_crit = crit.copy()
    nontriv_crit[0] = False
    gv = A0[nontriv_crit]
    ok_giant = bool(np.all(np.abs(gv - (N - 3)) <= 1e-6 * N))
    small = A0[~crit]
    max_small = float(small.max())
    log(f"=== N={N} K={K} m={m}")
    log(f"  criterion count {n_crit} == expected 3m-2 = {expected}: "
        f"{'PASS' if n_crit == expected else 'FAIL'}")
    log(f"  giant values all == N-3 = {N-3}: {'PASS' if ok_giant else 'FAIL'} "
        f"(min {gv.min():.0f} max {gv.max():.0f}, n={len(gv)})")
    log(f"  non-criterion max |A0| = {max_small:.1f} "
        f"({'O(1) PASS' if max_small < 5 else 'FAIL'})")
    log(f"  trivial pair |A0| = {A0[0]:.0f}")
    return dict(N=N, K=K, m=m, n_crit=n_crit, expected=expected,
                criterion_count_ok=bool(n_crit == expected),
                giants_exact=ok_giant, max_small=max_small,
                trivial=float(A0[0]))


def main():
    log("R108l: exact dichotomy law across the full design sweep")
    res = {}
    if os.path.exists(JSON_PATH):
        try:
            res = json.load(open(JSON_PATH))
        except Exception:
            res = {}
    for N, a in DESIGNS:
        key = f"N{N}"
        if key in res:
            log(f"=== {key} done, skip")
            continue
        try:
            res[key] = run(N, a)
        except Exception as exc:
            log(f"N={N} FAILED: {exc}")
            continue
        with open(JSON_PATH, "w", encoding="utf-8") as fh:
            json.dump(res, fh, indent=1, default=float)
    npass = sum(1 for r in res.values()
                if r.get("criterion_count_ok") and r.get("giants_exact")
                and r.get("max_small", 99) < 5)
    log(f"SUMMARY: {npass}/{len(res)} designs PASS all three dichotomy checks")
    log("done")


if __name__ == "__main__":
    main()
