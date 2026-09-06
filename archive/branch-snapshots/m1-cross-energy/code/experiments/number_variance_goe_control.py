"""Matched-GOE number-variance experiment.

Numerical evidence only. Output: results/numerical/number_variance_goe_control.json.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
OUT_DIR = os.path.join(ROOT, "results", "numerical")
os.makedirs(OUT_DIR, exist_ok=True)
LOG = os.path.join(OUT_DIR, "number_variance_goe_control.log")
sys.path.insert(0, ROOT)

from code.math.jacobi import dlog_table, index_coset, jacobi_matrix  # noqa: E402
from code.math.twisted_jacobi import primitive_root  # noqa: E402


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
    u = np.sort(u)
    n = len(u)
    out = {}
    for L in L_values:
        counts = []
        for i in range(n):
            j = i
            while j < n and u[j] < u[i] + L:
                j += 1
            counts.append(j - i)
        out[L] = float(np.var(counts))
    return out


def main():
    t0 = time.time()
    N, K, a = 19489, 29, 4523
    L_values = [1, 2, 3, 5, 8, 12]
    rng = np.random.default_rng(20260901)
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ks = index_coset(N, K, a, dlog)
    ks_odd = ks[ks % 2 == 1]
    m = len(ks_odd)
    q_list = list(range(1, 300, 12))
    cat = {L: [] for L in L_values}
    for q in q_list:
        J = jacobi_matrix(N, K, a, dlog, ks_odd, q)
        inv2 = pow(2, N - 2, N)
        C = np.exp(-2j * np.pi * (inv2 * q % N) / N) * J / (N - 1)
        M = (C + C.conj().T).real
        stats = sig2_single(unfold_poly(np.linalg.eigvalsh(M)), L_values)
        for L in L_values:
            cat[L].append(stats[L])
    nsim = 60
    goe = {L: [] for L in L_values}
    for _ in range(nsim):
        A = rng.normal(size=(m, m))
        G = (A + A.T) / 2
        stats = sig2_single(unfold_poly(np.linalg.eigvalsh(G)), L_values)
        for L in L_values:
            goe[L].append(stats[L])
    rows = []
    all_pass = True
    for L in L_values:
        cm, gm = float(np.mean(cat[L])), float(np.mean(goe[L]))
        gs = float(np.std(goe[L]) / np.sqrt(nsim))
        cs = float(np.std(cat[L]) / np.sqrt(len(cat[L])))
        sigma = np.sqrt(gs ** 2 + cs ** 2)
        z = abs(cm - gm) / sigma
        ok = z < 2.0
        all_pass &= ok
        rows.append({"L": L, "catmap_mean": cm, "catmap_sem": cs,
                     "goe_mean": gm, "goe_sem": gs, "z": float(z), "pass": bool(ok)})
    out = {
        "script": "code/experiments/number_variance_goe_control.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "design": {"N": N, "K": K, "a": a, "m_plus": int(m),
                   "n_q": len(q_list), "nsim": nsim},
        "L_values": L_values, "rows": rows, "overall_pass": bool(all_pass),
        "walltime_s": time.time() - t0,
    }
    out_path = os.path.join(OUT_DIR, "number_variance_goe_control.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2)
    log(f"artifact -> {out_path}; numerical test pass={all_pass}")


if __name__ == "__main__":
    main()
