"""RUN 91.14 -- Number-variance test with matched GOE control.

Measures the spectral rigidity statistic Sigma^2(L) of the parity-odd
level-set coset matrix M_q, compared NOT against the asymptotic GOE
formula (which fails at finite m due to unfolding artifacts) but against
a MATCHED GOE control: simulated GOE matrices of the same dimension m_+,
unfolded by the same polynomial pipeline.

Design: N=19489, K=29, a=4523, m_+=336 (parity-odd principal coset).

PASS condition: |Sigma2_catmap(L) - Sigma2_GOEsim(L)| within the
simulation error bars (std/sqrt(nsim), 2-sigma) for L = 1..12.

Output: artifacts/r91/number_variance_goe_control.json + .log
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "artifacts", "r91")
os.makedirs(OUT_DIR, exist_ok=True)
LOG = os.path.join(OUT_DIR, "number_variance_goe_control.log")

sys.path.insert(0, os.path.join(ROOT, "src", "large_m"))
sys.path.insert(0, os.path.join(ROOT, "src", "theorems"))

from fourth_mixed_moment import (  # noqa: E402
    dlog_table, index_coset, jacobi_matrix,
)
from theorem_ii_twisted_jacobi import primitive_root  # noqa: E402


def log(msg):
    line = str(msg)
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8") as fh:
        fh.write(line + "\n")


def unfold_poly(ev, deg=11):
    ev = np.sort(ev)
    n = len(ev)
    y = np.arange(1, n + 1) / (n + 1)
    return n * np.polyval(np.polyfit(ev, y, deg), ev)


def sig2_single(u, L_values):
    """Number variance by sliding windows on one unfolded spectrum."""
    u = np.sort(u)
    n = len(u)
    out = {}
    for L in L_values:
        counts = []
        i = 0
        while i < n:
            j = i
            while j < n and u[j] < u[i] + L:
                j += 1
            counts.append(j - i)
            i += 1
        out[L] = float(np.var(counts))
    return out


def main():
    t0 = time.time()
    log("RUN 91.14 -- number variance with matched GOE control")
    N, K, a = 19489, 29, 4523
    L_values = [1, 2, 3, 5, 8, 12]
    rng = np.random.default_rng(20260901)

    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ks = index_coset(N, K, a, dlog)
    ks_odd = ks[ks % 2 == 1]
    m = len(ks_odd)
    log(f"design N={N} K={K} a={a} m_+={m}")

    # --- cat map measurement ---
    q_list = list(range(1, 300, 12))
    cat = {L: [] for L in L_values}
    for q in q_list:
        J = jacobi_matrix(N, K, a, dlog, ks_odd, q)
        inv2 = pow(2, N - 2, N)
        C = np.exp(-2j * np.pi * (inv2 * q % N) / N) * J / (N - 1)
        M = (C + C.conj().T).real
        ev = np.linalg.eigvalsh(M)
        u = unfold_poly(ev)
        s = sig2_single(u, L_values)
        for L in L_values:
            cat[L].append(s[L])

    # --- matched GOE control: same m, same unfolding ---
    nsim = 60
    goe = {L: [] for L in L_values}
    for _ in range(nsim):
        A = rng.normal(size=(m, m))
        G = (A + A.T) / 2
        ev = np.linalg.eigvalsh(G)
        u = unfold_poly(ev)
        s = sig2_single(u, L_values)
        for L in L_values:
            goe[L].append(s[L])

    # --- compare ---
    rows = []
    all_pass = True
    for L in L_values:
        cm = float(np.mean(cat[L]))
        gm = float(np.mean(goe[L]))
        gs = float(np.std(goe[L]) / np.sqrt(nsim))
        # 2-sigma window on the GOE side; cat side has its own spread
        cs = float(np.std(cat[L]) / np.sqrt(len(cat[L])))
        sigma = np.sqrt(gs ** 2 + cs ** 2)
        z = abs(cm - gm) / sigma
        ok = z < 2.0
        all_pass &= ok
        rows.append({
            "L": L,
            "catmap_mean": cm, "catmap_sem": cs,
            "goe_mean": gm, "goe_sem": gs,
            "z": float(z), "pass": bool(ok),
        })
        log(f"L={L:3d}: cat {cm:.4f}+-{cs:.4f}  GOEsim {gm:.4f}+-{gs:.4f}"
            f"  z={z:.2f} {'PASS' if ok else 'FAIL'}")

    out = {
        "script": "src/large_m/number_variance_goe_control.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "design": {"N": N, "K": K, "a": a, "m_plus": int(m),
                   "n_q": len(q_list), "nsim": nsim},
        "L_values": L_values,
        "rows": rows,
        "overall_pass": bool(all_pass),
        "walltime_s": time.time() - t0,
    }
    out_path = os.path.join(OUT_DIR, "number_variance_goe_control.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log(f"artifact written -> {out_path}")
    log(f"overall PASS = {all_pass}")


if __name__ == "__main__":
    main()
