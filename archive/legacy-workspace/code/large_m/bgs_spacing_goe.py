"""RUN 91.13 -- DIRECT BGS (GOE) SPACING TEST IN THE DESYMMETRISED SECTOR.

Measures the unfolded nearest-neighbour spacing distribution P(s) of the
parity-odd level-set coset matrix M_q (the U_A-eigenspace of dimension
m_+ = (N-1)/(2K)), against the Wigner-Dyson GOE surmise

    P_GOE(s) = (pi s / 2) exp(-pi s^2 / 4),   <s> = 1.

Object: M_q = C_q + C_q*, C_q[i,j] = e_N(-q/2) J(chi_i,chi_j;q)/(N-1),
restricted to the principal character coset chi_k(a) = 1 with parity-odd
characters.  This is the desymmetrised Hecke-sector observable; the full
character group is arcsine (classical, Theorems 91.2/91.5) and only the
parity-odd sector carries the quantum-chaotic GOE statistics.

Method: for each q in a sample, compute M_q, take eigenvalues, unfold via
a polynomial CDF fit (deg 11), collect the standardized gaps.  Tests:
KS against the GOE CDF 1 - exp(-pi s^2/4), and chi^2/dof.

Designs (split primes, ord(a)=K, parity-odd m_+):
  N=3571,  K=17, a=2469, m_+=105
  N=19489, K=29, a=4523, m_+=336

PASS condition (per R86.4): KS D below the 5% critical value 1.358/sqrt(n)
and chi^2/dof < 1.5 at both designs.

Output: artifacts/r91/bgs_spacing_goe.json + .log
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
LOG = os.path.join(OUT_DIR, "bgs_spacing_goe.log")

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


def unfold_via_polyfit(ev, deg=11):
    """Unfold to constant density via polynomial CDF fit."""
    ev = np.sort(ev)
    n = len(ev)
    x = ev
    y = np.arange(1, n + 1) / (n + 1)
    coeff = np.polyfit(x, y, deg)
    cdf = np.polyval(coeff, ev)
    return n * cdf


def gaps_stats(ev, deg=11):
    u = unfold_via_polyfit(ev, deg)
    u = np.sort(u)
    gaps = np.diff(u)
    return gaps / np.mean(gaps)


def goe_cdf(s):
    return 1 - np.exp(-np.pi * s ** 2 / 4)


def ks_test(gaps):
    gaps_sorted = np.sort(gaps)
    n = len(gaps_sorted)
    emp = np.arange(1, n + 1) / n
    D = np.max(np.abs(emp - goe_cdf(gaps_sorted)))
    crit = 1.358 / np.sqrt(n)
    return float(D), float(crit)


def chi2_test(gaps):
    bins = np.linspace(0, 4, 21)
    obs, _ = np.histogram(gaps, bins=bins)
    centers = (bins[:-1] + bins[1:]) / 2
    wigner = (np.pi * centers / 2) * np.exp(-np.pi * centers ** 2 / 4)
    exp = wigner * np.diff(bins) * len(gaps)
    mask = exp >= 5
    chi2 = float(np.sum((obs[mask] - exp[mask]) ** 2 / exp[mask]))
    dof = int(mask.sum()) - 1
    return chi2, dof


def run_design(N, K, a, q_step, q_max):
    g = primitive_root(N)
    dlog = dlog_table(N, g)
    ks = index_coset(N, K, a, dlog)
    ks_odd = ks[ks % 2 == 1]
    m = len(ks_odd)
    all_gaps = []
    for q in range(1, q_max, q_step):
        J = jacobi_matrix(N, K, a, dlog, ks_odd, q)
        inv2 = pow(2, N - 2, N)
        C = np.exp(-2j * np.pi * (inv2 * q % N) / N) * J / (N - 1)
        M = (C + C.conj().T).real
        ev = np.linalg.eigvalsh(M)
        g = gaps_stats(ev)
        all_gaps.extend(g)
    all_gaps = np.array(all_gaps)
    D, crit = ks_test(all_gaps)
    chi2, dof = chi2_test(all_gaps)
    row = {
        "N": N, "K": K, "a": a, "m_plus": int(m),
        "n_q": (q_max - 1) // q_step,
        "n_gaps": int(len(all_gaps)),
        "mean_gap": float(all_gaps.mean()),
        "ks_D": D, "ks_crit_5pct": crit,
        "ks_pass": D < crit,
        "chi2": chi2, "dof": dof, "chi2_over_dof": chi2 / dof,
    }
    log(f"N={N} K={K} m+={m}: {len(all_gaps)} gaps, KS D={D:.4f} "
        f"(crit {crit:.4f}) {'PASS' if D < crit else 'REJECT'}, "
        f"chi2/dof={chi2/dof:.2f}")
    return row


def main():
    t0 = time.time()
    log("RUN 91.13 -- BGS (GOE) spacing test in the desymmetrised sector")
    out = {
        "script": "src/large_m/bgs_spacing_goe.py",
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "designs": [],
        "goe_reference": "Wigner surmise P(s) = (pi s/2) exp(-pi s^2/4)",
    }
    out["designs"].append(run_design(3571, 17, 2469, 5, 200))
    out["designs"].append(run_design(19489, 29, 4523, 7, 300))
    out["overall_pass"] = all(d["ks_pass"] and d["chi2_over_dof"] < 1.5
                              for d in out["designs"])
    out["walltime_s"] = time.time() - t0
    out_path = os.path.join(OUT_DIR, "bgs_spacing_goe.json")
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    log(f"artifact written -> {out_path}")
    log(f"overall PASS = {out['overall_pass']}")


if __name__ == "__main__":
    main()
