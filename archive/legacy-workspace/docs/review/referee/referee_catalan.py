"""Referee recomputation of the Catalan/Sato-Tate claims (Claim 5).
Direct summation of <|J|^{2k}> over the character block (k0=1, even parity,
the same block the canonical scripts use), at four designs, using the
canonical J_matrix from src/r82n_fourth_moment.py.

Computes BOTH normalisations:
  raw:   m_{2k}/N^k = mean(|J|^{2k}) / N^k
  emp:   m_{2k}/<|J|^2>^k = mean(|J|^{2k}) / mean(|J|^2)^k
because the audit found evidence that LEDGER R82.16's N=199 row
(<|J|^4>/N^2 = 2.0143 etc.) is the SECOND one, mislabelled as the first.
"""
import json
import os
import sys
import time

import numpy as np

SRC = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC)
from r82n_fourth_moment import J_matrix  # noqa: E402
from r82k_bgs_large_m import design_params  # noqa: E402

CATALAN = [1, 1, 2, 5, 14, 42, 132]


def run(N, K, qs):
    t0 = time.time()
    a = design_params(N, K)
    rows = []
    for q in qs:
        J, m, dlog, k1 = J_matrix(N, K, a, q)
        a2 = np.abs(J) ** 2
        m2 = a2.mean()
        row = {"N": N, "K": K, "q": int(q), "m": m,
               "m1_over_N1": float(m2 / N), "m1_over_emp1": 1.0}
        for k in range(2, 6):
            mk = float((a2 ** k).mean())
            row[f"m{k}_over_N{k}"] = mk / N ** k
            row[f"m{k}_over_emp{k}"] = mk / m2 ** k
        rows.append(row)
        print(f"  N={N} q={q}: " + "  ".join(
            f"e{k}={row[f'm{k}_over_N{k}']:.4f}" for k in range(1, 6)) +
            f"   ({time.time()-t0:.0f} s)", flush=True)
    mean = {"N": N, "K": K, "n_q": len(qs)}
    for k in range(1, 6):
        mean[f"e{k}_raw_mean"] = float(np.mean([r[f"m{k}_over_N{k}"] for r in rows]))
        mean[f"e{k}_emp_mean"] = float(np.mean([r[f"m{k}_over_emp{k}"] for r in rows]))
        mean[f"dev_from_C{k}_raw"] = mean[f"e{k}_raw_mean"] - CATALAN[k]
        mean[f"dev_from_C{k}_emp"] = mean[f"e{k}_emp_mean"] - CATALAN[k]
    print(f"  N={N} MEANS: " + "  ".join(
        f"e{k}: raw {mean[f'e{k}_raw_mean']:.4f} (dev {mean[f'dev_from_C{k}_raw']:+.4f})"
        f" / emp {mean[f'e{k}_emp_mean']:.4f} (dev {mean[f'dev_from_C{k}_emp']:+.4f})"
        for k in range(1, 6)), flush=True)
    return {"design": mean, "rows": rows}


def main():
    out = []
    out.append(run(199, 11, [1, 2, 3, 5, 7]))
    out.append(run(3571, 17, [1, 2, 3]))
    out.append(run(19489, 29, [1, 2]))
    out.append(run(95419, 57, [1, 2]))
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "referee_catalan.json")
    with open(dest, "w") as fh:
        json.dump(out, fh, indent=1)
    print("artifact ->", dest, flush=True)


if __name__ == "__main__":
    main()
