"""Float orbit sum of kappa(N beta) Tr Q_beta at a prime.

This is a binary64 scan, not an enclosure. The err_frob column is a
Frobenius majorant from an unweighted Lipschitz grid; at q=457 it is far
too large to certify the traces. h7_average.py orbit only folds the table.

Command
    python3 h7_avg_orbit.py 457 57 0
"""

from __future__ import annotations

import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h7_lin_cert import tb_prime
from h7_multidisc import build_letters

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "..", "logs")


def lambda_table(q: int):
    x, y = 1, 0
    pw = []
    while True:
        pw.append((x % q, y % q))
        x, y = (3 * x + 4 * y) % q, (2 * x + 3 * y) % q
        if (x % q, y % q) == (1, 0):
            return pw


def apply_lambda(x, y, q):
    return (3 * x + 4 * y) % q, (2 * x + 3 * y) % q


def main():
    q = int(sys.argv[1])
    m = int(sys.argv[2]) if len(sys.argv) > 2 else 57
    sector = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    t0 = time.time()
    ns, mats, meta = build_letters(3, 1.2, 40, 16)
    if meta["n_out"] != 0 or meta["dim"] != 280:
        raise RuntimeError(meta)
    pw = lambda_table(q)
    P = len(pw)
    tb = tb_prime(m, q)
    print({"q": q, "P": P, "tb": tb, "m": m, "sector": sector, "build": round(time.time() - t0, 2)}, flush=True)
    # Precompute powers of lambda as integer arrays for the twist dot product.
    xs = np.array([p[0] for p in pw], dtype=np.int64)
    ys = np.array([p[1] for p in pw], dtype=np.int64)
    dim = 280
    # Operator-norm envelope of one unweighted step. The grid is a float scan.
    # The Lipschitz majorant is sum |2 pi n| ||A_n||_F, a float upper bound
    # on the derivative of the step in Frobenius norm, hence in operator norm.
    grid_n = 4096
    grid_t = np.linspace(0.0, 1.0, grid_n, endpoint=False)
    # Sample ||L||_2. Letters are combined once per node.
    op_grid = np.empty(grid_n)
    frob_letters = []
    for n, M in zip(ns, mats):
        frob_letters.append(float(np.linalg.norm(M, ord="fro")))
    lip = 0.0
    for n, fr in zip(ns, frob_letters):
        lip += abs(2 * np.pi * float(n)) * fr
    print({"lip_frob": lip, "letter_frob_sum": float(sum(frob_letters))}, flush=True)
    t_grid = time.time()
    for i, t in enumerate(grid_t):
        w = np.exp(2j * np.pi * ns * (t + sector / 8.0))
        L = np.tensordot(w, mats, axes=(0, 0))
        op_grid[i] = np.linalg.norm(L, 2)
    half = 0.5 / grid_n
    pad = lip * half
    print(
        {
            "grid": grid_n,
            "op_min": float(op_grid.min()),
            "op_max": float(op_grid.max()),
            "pad": pad,
            "grid_seconds": round(time.time() - t_grid, 2),
        },
        flush=True,
    )

    def step_cap(t_frac: float) -> float:
        """Float upper bound ||L(t)||_2 <= grid neighbour + Lip * distance."""
        u = (t_frac % 1.0) * grid_n
        j = int(np.round(u)) % grid_n
        dist = abs(u - np.round(u))
        if dist > grid_n / 2:
            dist = grid_n - dist
        return float(op_grid[j] + lip * (dist / grid_n))

    seen = np.zeros(q * q, dtype=np.uint8)

    def key(x, y):
        return x * q + y

    orbits = []
    S = 0j
    abs_tri = 0.0
    n_iso = 0
    t1 = time.time()
    for x0 in range(q):
        for y0 in range(q):
            if seen[key(x0, y0)]:
                continue
            # walk the orbit
            orb = []
            x, y = x0, y0
            for _ in range(P + 2):
                k = key(x, y)
                if seen[k] and orb:
                    break
                seen[k] = 1
                orb.append((x, y))
                x, y = apply_lambda(x, y, q)
                if (x, y) == (x0, y0):
                    break
            length = len(orb)
            bx, by = orb[0]
            N = (bx * bx - 2 * by * by) % q
            if N == 0:
                kap = q - 2 + 0j
                n_iso += 1
            else:
                ang = (pow(tb, -1, q) * N) % q
                kap = -1 - np.exp(2j * np.pi * ang / q)
            # phases along this representative
            tau = (2 * (bx * xs + 2 * by * ys)) % q
            Q = np.eye(dim, dtype=np.complex128)
            frob_max = 1.0
            # Scalar majorant of ||Q_true - Q_float||_F. R_step is a float
            # upper bound on ||L||_2; the pad makes it a Lipschitz ceiling.
            # gamma is a binary64 dot-product factor for length dim, used as
            # ||fl(LQ) - LQ||_F <= gamma ||L||_F ||Q||_F. This pass records
            # the majorant; the note states which constants were proved.
            gamma = (dim * np.finfo(np.float64).eps) / (1.0 - dim * np.finfo(np.float64).eps)
            err = 0.0
            cap_prod = 1.0
            for t in tau:
                phase = t / q + sector / 8.0
                w = np.exp(2j * np.pi * (ns * phase))
                L = np.tensordot(w, mats, axes=(0, 0))
                cap = step_cap(phase)
                fn = float(np.linalg.norm(Q, ord="fro"))
                lf = float(np.linalg.norm(L, ord="fro"))
                # Incoming error is amplified by ||L||_2, and this step adds
                # the matmul rounding. Letter-approximation error is added
                # later as a uniform ε, once that ε is enclosed.
                err = cap * err + gamma * lf * fn
                Q = L @ Q
                fn2 = float(np.linalg.norm(Q, ord="fro"))
                if fn2 > frob_max:
                    frob_max = fn2
                cap_prod *= cap
            tr = np.trace(Q)
            contrib = kap * length * tr
            S += contrib
            abs_tri += abs(kap) * length * abs(tr)
            orbits.append(
                {
                    "beta": [int(bx), int(by)],
                    "len": int(length),
                    "N": int(N),
                    "kap_re": float(kap.real),
                    "kap_im": float(kap.imag),
                    "tr_re": float(tr.real),
                    "tr_im": float(tr.imag),
                    "tr_abs": float(abs(tr)),
                    "frob_max": frob_max,
                    "err_frob": err,
                    "cap_prod": cap_prod,
                }
            )
            if len(orbits) % 200 == 0:
                print(
                    f"orbits {len(orbits)} S {S.real:.6e}{S.imag:+.6e}j |tri| {abs_tri:.6e} t {time.time()-t1:.0f}",
                    flush=True,
                )
    if int(seen.sum()) != q * q:
        raise RuntimeError(("coverage", int(seen.sum()), q * q))
    # Sort a short head by |contribution|
    orbits.sort(key=lambda r: abs(r["kap_re"] + 1j * r["kap_im"]) * r["len"] * r["tr_abs"], reverse=True)
    head = orbits[:30]
    doc = {
        "q": q,
        "m": m,
        "sector": sector,
        "P_lambda": P,
        "tb": int(tb),
        "n_orbits": len(orbits),
        "n_iso_orbits": n_iso,
        "dim": dim,
        "S_re": float(S.real),
        "S_im": float(S.imag),
        "S_abs": float(abs(S)),
        "triangle_abs": abs_tri,
        "seconds": round(time.time() - t0, 2),
        "head": head,
        "note": "Float64 scan of every lambda-orbit. Not an enclosure by itself.",
    }
    os.makedirs(LOG_DIR, exist_ok=True)
    out = os.path.join(LOG_DIR, f"h7_avg_orbit_q{q}_a{sector}.json")
    # drop the full list from the json head-only file; write full traces separately as npy-free compact arrays
    json.dump(doc, open(out, "w"), indent=1)
    # compact full table
    full = {
        "beta0": [r["beta"][0] for r in orbits],
        "beta1": [r["beta"][1] for r in orbits],
        "len": [r["len"] for r in orbits],
        "N": [r["N"] for r in orbits],
        "tr_re": [r["tr_re"] for r in orbits],
        "tr_im": [r["tr_im"] for r in orbits],
        "tr_abs": [r["tr_abs"] for r in orbits],
        "frob_max": [r["frob_max"] for r in orbits],
        "err_frob": [r["err_frob"] for r in orbits],
        "cap_prod": [r["cap_prod"] for r in orbits],
    }
    json.dump(full, open(os.path.join(LOG_DIR, f"h7_avg_orbit_q{q}_a{sector}_full.json"), "w"))
    print("DONE", doc["S_re"], doc["S_im"], "abs", doc["S_abs"], "tri", doc["triangle_abs"], "orbits", doc["n_orbits"], "sec", doc["seconds"], flush=True)


if __name__ == "__main__":
    main()
