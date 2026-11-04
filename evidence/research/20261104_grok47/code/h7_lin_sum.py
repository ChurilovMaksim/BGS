"""Aggregate Lin sum for the multi-disc finite section.

Lin_d = (2/d^2) Re(conj(Z) * S), S = sum_{beta != 0} kappa_d(N beta) Zhat(beta).
For a prime q || h_m, q != 7, with (2/q) = 1, the Gauss sum in h7_lin.md gives

    S = q^2 A_{N=0} - (2q - 2) Zhat(0) - q E_full,

where E_full = sum_x A(x) e(-t_b N(x)/q) and A is the word mass. On the
finite section this is the trace of the letter product, weighted by that
kernel. The beta = 0 term has been removed.

Commands
    python3 h7_lin_sum.py validate
    python3 h7_lin_sum.py iso
    python3 h7_lin_sum.py hutch
    python3 h7_lin_sum.py bounds
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h7_multidisc import build_letters  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "..", "logs")
LAM = 3 + 2 * math.sqrt(2)


def lam_pows(m: int, q: int):
    x, y = 1, 0
    out = []
    for _ in range(m):
        out.append((x % q, y % q))
        x, y = (3 * x + 4 * y) % q, (2 * x + 3 * y) % q
    return out


def sqrt2_mod(q: int) -> int:
    for i in range(q):
        if (i * i - 2) % q == 0:
            return i
    raise RuntimeError(q)


def missing_label(m: int, q: int, a: int = 2) -> int:
    """t_b = j_b y' mod q, the one dilation label excluded from the members."""
    # h_m from the Pell data, via the same recurrence the cert uses for h_p * K_p.
    # m = 3p is not required: build h from y' of the Pell solution of length m.
    sys.path.insert(0, "/workspace/computations/verification/lineI/code")
    from law import mdata

    D = mdata(m)
    h, yp = D["h"], D["yp"]
    assert h % q == 0 and (h // q) % q != 0
    nu0 = next(x for x in [((a // 2) * pow(4, -1, h)) % h + s * h for s in (0, 1)] if x % 2 == 1)
    bad = []
    step = 2 * (h // q)
    for j in range(q):
        if math.gcd((nu0 + step * j) % (2 * h), 2 * h) != 1:
            bad.append(j)
    if bad != [0] and 0 in bad:
        bad = [j for j in bad if j != 0]
    # j = 0 is nu0, which is a unit. The single bad j in 1..q-1 is the missing member.
    bad = [j for j in range(1, q) if math.gcd((nu0 + step * j) % (2 * h), 2 * h) != 1]
    if len(bad) != 1:
        raise RuntimeError(bad)
    return (bad[0] * yp) % q


def G_of(q: int, tb: int) -> np.ndarray:
    xs = np.arange(q)
    x, y = np.meshgrid(xs, xs, indexing="ij")
    nn = (x * x - 2 * y * y) % q
    phase = np.exp(-2j * np.pi * ((tb * nn) % q) / q)
    inner = np.where(nn == 0, q, 0).astype(np.complex128) - 1 - phase
    return q * inner


def sector_letters(ns, mats, a: int):
    """Fold the sector phase e(a n/8) into the letter. Beta phases stay outside."""
    out = []
    for n, M in zip(ns, mats):
        out.append(M * np.exp(2j * np.pi * n * a / 8.0))
    return out


def split_blocks(ns, letters, k0: int, K: int):
    """Each letter reads one input centre and writes one output centre.

    The builder stores L[output centre c, input centre j], with
    j = round((c+n)/lambda). A core centre with no preimage in the core
    is omitted; that is the exit tail.
    """
    centers = list(range(-k0, k0 + 1))
    index = {c: i for i, c in enumerate(centers)}
    blocks = []
    for n, M in zip(ns, letters):
        pieces = []
        for c in centers:
            r0 = index[c] * K
            hits = []
            for j in centers:
                q0 = index[j] * K
                block = M[r0 : r0 + K, q0 : q0 + K]
                if np.max(np.abs(block)) > 0.0:
                    hits.append((index[j], block.copy()))
            if len(hits) > 1:
                raise RuntimeError((int(n), c, len(hits)))
            if len(hits) == 1:
                pieces.append((hits[0][0], index[c], hits[0][1]))
        blocks.append(pieces)
    return blocks


def run_propagate(q, m, ns, letters, k0, K, probes):
    blocks = split_blocks(ns, letters, k0, K)
    P = probes.shape[1]
    ncent = len(range(-k0, k0 + 1))
    psi = [np.zeros((q, q, K, P), dtype=np.complex128) for _ in range(ncent)]
    for c in range(ncent):
        psi[c][0, 0] = probes[c * K : (c + 1) * K, :]
    pw = lam_pows(m, q)
    xs = np.arange(q)
    X, Y = np.meshgrid(xs, xs, indexing="ij")
    t0 = time.time()
    for step, (px, py) in enumerate(pw):
        new = [np.zeros_like(psi[0]) for _ in range(ncent)]
        for n, pieces in zip(ns, blocks):
            sx = (int(n) * px) % q
            sy = (int(n) * py) % q
            srcx = (X - sx) % q
            srcy = (Y - sy) % q
            for c_i, j_i, block in pieces:
                gathered = psi[c_i][srcx, srcy]  # (q,q,K,P)
                flat = gathered.reshape(q * q * P, K)
                img = flat @ block.T
                new[j_i] += img.reshape(q, q, K, P)
        psi = new
        if (step + 1) % 10 == 0 or step + 1 == m:
            mass = sum(float(np.linalg.norm(p)) for p in psi)
            print(f"  step {step+1}/{m} mass {mass:.6e} t {time.time()-t0:.1f}", flush=True)
    return psi


def contract(psi, weight):
    """weight (q,q), psi list of (q,q,K,P). Returns (P,) of sum conj? No: v was the
    initial probe stored only as the propagated image. The caller dots."""
    acc = None
    for p in psi:
        # p: (q,q,K,P)
        term = np.einsum("ij,ijkp->kp", weight, p, optimize=True)
        acc = term if acc is None else acc + term
    return acc  # (K*ncent? no) (K, P) summed over centres -> need sum over K too, caller stacks


def dot_probes(psi, probes, weight):
    acc = contract_stacked(psi, weight)  # (dim, P)
    # v* W v = sum_i conj(v_i) * (W v)_i
    return np.sum(np.conj(probes) * acc, axis=0)


def contract_stacked(psi, weight):
    chunks = []
    for p in psi:
        chunks.append(np.einsum("ij,ijkp->kp", weight, p, optimize=True))
    return np.concatenate(chunks, axis=0)


def beta_trace(ns, letters, q, m, bx, by, pw):
    dim = letters[0].shape[0]
    Q = np.eye(dim, dtype=np.complex128)
    for step, (px, py) in enumerate(pw):
        tw = (2 * (bx * px + 2 * by * py)) % q
        L = 0
        for n, M in zip(ns, letters):
            L = L + M * np.exp(2j * np.pi * n * tw / q)
        Q = L @ Q
    return np.trace(Q)


def validate():
    """q=41, m=15, full sum over beta versus the Gauss kernel, one sector."""
    q, m, a = 41, 15, 0
    k0, K, nmax = 3, 20, 10
    ns, mats, meta = build_letters(k0, 1.2, K, nmax)
    letters = sector_letters(ns, mats, a)
    tb = missing_label(m, q)
    G = G_of(q, tb)
    pw = lam_pows(m, q)
    t0 = time.time()
    S = 0j
    Z0 = None
    for bx in range(q):
        for by in range(q):
            tr = beta_trace(ns, letters, q, m, bx, by, pw)
            if bx == 0 and by == 0:
                Z0 = tr
            # kappa from the same formula as G's Fourier dual: compute directly
            nn = (bx * bx - 2 * by * by) % q
            if nn == 0:
                kap = q - 2
            else:
                kap = -1 - np.exp(2j * np.pi * ((pow(tb, -1, q) * nn) % q) / q)
            if not (bx == 0 and by == 0):
                S += kap * tr
    # grid, all columns
    dim = meta["dim"]
    eye = np.eye(dim, dtype=np.complex128)
    psi = run_propagate(q, m, ns, letters, k0, K, eye)
    ones = np.ones((q, q), dtype=np.complex128)
    full = np.trace(contract_stacked(psi, G))  # includes beta=0
    # beta=0 contribution inside full is (q-2)*Z0, so nonzero S_grid = full - (q-2)*Z0
    # contract_stacked returns (dim, P=dim); trace is sum of diagonal of W.
    W_G = contract_stacked(psi, G)
    W_1 = contract_stacked(psi, ones)
    S_grid = np.trace(W_G) - (q - 2) * np.trace(W_1)
    rec = {
        "q": q,
        "m": m,
        "K": K,
        "dim": dim,
        "tb": tb,
        "S_beta": [S.real, S.imag],
        "S_grid": [S_grid.real, S_grid.imag],
        "abs_err": abs(S - S_grid),
        "Z0_beta": [Z0.real, Z0.imag],
        "Z0_grid": [np.trace(W_1).real, np.trace(W_1).imag],
        "seconds": time.time() - t0,
    }
    print(json.dumps(rec), flush=True)
    if rec["abs_err"] > 1e-6 * max(1.0, abs(S)):
        raise SystemExit("validate failed")
    os.makedirs(LOG_DIR, exist_ok=True)
    json.dump(rec, open(os.path.join(LOG_DIR, "h7_lin_validate.json"), "w"), indent=1)
    return rec


def iso_lines(q: int):
    w = sqrt2_mod(q)
    lines = []
    for sign in (1, -1):
        v = ((sign * w) % q, 1)
        # ell: lambda * v = ell * v
        lx = (3 * v[0] + 4 * v[1]) % q
        ly = (2 * v[0] + 3 * v[1]) % q
        # ly should be ell, lx = ell * v[0]
        ell = ly % q
        assert (ell * v[0] - lx) % q == 0
        seen = [False] * q
        reps = []
        for s in range(1, q):
            if seen[s]:
                continue
            t = s
            while not seen[t]:
                seen[t] = True
                t = (t * ell) % q
            reps.append(s)
        betas = [((s * v[0]) % q, (s * v[1]) % q) for s in reps]
        lines.append({"sign": sign, "ell": ell, "reps": betas, "orbit": q - 1})
    return lines


def iso():
    q, m, a = 457, 57, 0
    k0, K, nmax = 3, 40, 16
    ns, mats, meta = build_letters(k0, 1.2, K, nmax)
    letters = sector_letters(ns, mats, a)
    pw = lam_pows(m, q)
    rows = []
    for line in iso_lines(q):
        for bx, by in line["reps"]:
            t0 = time.time()
            tr = beta_trace(ns, letters, q, m, bx, by, pw)
            rows.append({"sign": line["sign"], "beta": [bx, by], "tr": [tr.real, tr.imag], "seconds": time.time() - t0})
            print(rows[-1], flush=True)
    # each rep stands for an orbit of length 57; kappa on the isotropic line is q-2
    orbit = 57
    kap = q - 2
    S = 0j
    for row in rows:
        S += orbit * kap * complex(row["tr"][0], row["tr"][1])
    # two lines. reps cover each line once.
    rec = {"q": q, "m": m, "sector": a, "kappa0": kap, "orbit": orbit, "S_iso": [S.real, S.imag], "rows": rows}
    os.makedirs(LOG_DIR, exist_ok=True)
    json.dump(rec, open(os.path.join(LOG_DIR, "h7_lin_iso.json"), "w"), indent=1)
    print("S_iso", rec["S_iso"], flush=True)


def hutch():
    q, m, a = 457, 57, 0
    probes_n = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    k0, K, nmax = 3, 40, 16
    ns, mats, meta = build_letters(k0, 1.2, K, nmax)
    letters = sector_letters(ns, mats, a)
    dim = meta["dim"]
    rng = np.random.default_rng(457)
    # complex gaussian, E[|v_i|^2] = 1 so E[v* M v] = Tr M
    v = rng.normal(size=(dim, probes_n)) + 1j * rng.normal(size=(dim, probes_n))
    tb = missing_label(m, q)
    G = G_of(q, tb)
    print({"dim": dim, "tb": tb, "probes": probes_n, "G0": complex(G[0, 0])}, flush=True)
    psi = run_propagate(q, m, ns, letters, k0, K, v)
    WG = contract_stacked(psi, G)
    W1 = contract_stacked(psi, np.ones((q, q), dtype=np.complex128))
    est_full = np.sum(np.conj(v) * WG, axis=0)
    est_Z = np.sum(np.conj(v) * W1, axis=0)
    est_S = est_full - (q - 2) * est_Z
    # exact section trace at beta=0, same letters, for scale
    Z_exact = beta_trace(ns, letters, q, m, 0, 0, lam_pows(m, q))
    rec = {
        "q": q,
        "m": m,
        "sector": a,
        "K": K,
        "dim": dim,
        "tb": int(tb),
        "probes": probes_n,
        "S": [[z.real, z.imag] for z in est_S],
        "S_mean": [complex(est_S.mean()).real, complex(est_S.mean()).imag],
        "Z_probes": [[z.real, z.imag] for z in est_Z],
        "Z_exact_trace": [Z_exact.real, Z_exact.imag],
        "note": "Hutchinson estimator of the finite-section trace sum. Not an enclosure.",
    }
    os.makedirs(LOG_DIR, exist_ok=True)
    json.dump(rec, open(os.path.join(LOG_DIR, "h7_lin_hutch.json"), "w"), indent=1)
    print(json.dumps({k: rec[k] for k in ("S_mean", "Z_exact_trace", "S")}), flush=True)


def nsw_h(p: int) -> int:
    n = (p - 1) // 2
    u0, u1 = 1, 7
    for _ in range(1, n):
        u0, u1 = u1, 6 * u1 - u0
    return u1


def bounds():
    """Exact |kappa| pattern and the one-orbit epsilon majorant. No floats of Zhat."""
    z_mu = 1.9154712
    rows = []
    specs = [
        (19, 3437426497, [457, 7521721], (-208, 0), 1.458772466390154),
        (19, 24061985479, [7, 457, 7521721], (227, 227), 1.5119805975188876),
        (29, 2735635252619983, [7, 13921, 28073057689], (-89, 0), 1.4686852948918232),
    ]
    for p, d, facs, beta, r_hi in specs:
        m = 3 * p
        hp = nsw_h(p)
        Kp = 4 * hp * hp + 3
        hm = hp * Kp
        zlo = 0.5 * (1 - LAM ** (-m)) * (z_mu ** m - 3012.4)
        bx, by = beta
        nn = bx * bx - 2 * by * by
        local = []
        kap_abs_hi = 1
        for q in facs:
            nmod = nn % q
            # |kappa_q| <= q-2 if q|N, else <= 2. q=7 is not of the (2/q)=1 shape;
            # the member weight is still an integer linear combination of q-th roots,
            # and the prime-level bound |W|<=2/q^2 is |kappa|<=2 off the isotropic set
            # only for q||h with the missing-label formula. For q=7 the same
            # |sum_{t != tb} e| <= 6 = q-1, a worse trivial bound. Use q-1.
            if nmod == 0:
                kap_abs_hi *= q - 1
                local.append({"q": q, "N": 0, "kap_hi": q - 1})
            else:
                hi = 2 if q != 7 else 6
                kap_abs_hi *= hi
                local.append({"q": q, "N": int(nmod), "kap_hi": hi})
        # |Tr| <= dim * r^m, dim = 7*40 = 280, and the lambda orbit has m points
        # on which the trace repeats.
        dim = 280
        tr_hi = dim * (r_hi ** m)
        S_hi = m * kap_abs_hi * tr_hi
        eps_hi = 2 * S_hi * hp / (d * d * zlo)
        rows.append(
            {
                "p": p,
                "d": d,
                "m": m,
                "beta": [bx, by],
                "squarefree": all(pow(q, 2) > d or d % (q * q) != 0 for q in facs),
                "local": local,
                "kappa_abs_hi": kap_abs_hi,
                "zlo": zlo,
                "tr_hi": tr_hi,
                "eps_hi_one_orbit": eps_hi,
                "rate_hi": r_hi,
            }
        )
        print(p, d, "eps_one", eps_hi, "kap", kap_abs_hi, flush=True)
    os.makedirs(LOG_DIR, exist_ok=True)
    json.dump({"rows": rows}, open(os.path.join(LOG_DIR, "h7_lin_bounds.json"), "w"), indent=1)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "validate"
    {"validate": validate, "iso": iso, "hutch": hutch, "bounds": bounds}[cmd]()
