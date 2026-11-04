"""Phase-keeping carry iteration, single window, float complex128.

Rebuilds the sector-4 Galerkin blocks from the Line F/N6 formulae (midpoint
float, not arb) and runs the N14/N15 map

    (TY)_{(e, a)} = sum_e T_v(Y_{(a,b)}),  v = e - 6a + b,  |v|<=60,

on the box |e|<=E. T_v(Y) = sum_n N_n Y N_{n-v}^*, N_n = w_4(n) M_n / s.
This is [N]: binary64 blocks and a binary64 power iteration. It is the same
scheme as g_carry.py. A match to the published E=1 and E=4 rates is the
check that the rebuild is faithful.

Mass is the Frobenius norm, as in g_carry.py (the nuclear-norm branch there
is dead). After each step the whole collection is scaled to mass 1, so
||Y_{(0,0)}||_F is the (0,0) share.
"""
from __future__ import annotations

import json
import math
import os
import time

import numpy as np
from scipy.special import jv

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(ROOT, "logs")
os.makedirs(LOGS, exist_ok=True)

K = 55
K0 = 4
NMAX = 60
RHO = 1.2
ETA = 2.0
XJ = 0.9 * ETA
A_SEC = 4
LAM = 3.0 + 2.0 * math.sqrt(2.0)
CC = 1.0 / (LAM - 1.0 / LAM)


def rnd_half(t: float) -> int:
    return math.floor(t + 0.5)


def build_model():
    t0 = time.time()
    cores = [c2 for c2 in range(-2 * K0 - 2, 2 * K0 + 3) if c2 % 2 == 0 and abs(c2) / 2 <= K0]
    idx = {c2: i for i, c2 in enumerate(cores)}
    D = len(cores) * K
    fact = [1.0]
    for i in range(1, K):
        fact.append(fact[-1] * i)
    lamp = [1.0]
    for i in range(1, K):
        lamp.append(lamp[-1] / LAM)

    def j_signed(n: int) -> float:
        j = float(jv(abs(n), XJ))
        if n < 0 and (n % 2):
            j = -j
        return j

    def wa(n: int) -> complex:
        phase = np.exp(2j * np.pi * (CC * n * n / 2 + A_SEC * n / 8.0))
        return (1j) ** (n % 4) * j_signed(n) * phase

    blocks = {}  # n -> list of (ib, jb, B)
    ns = set()
    for c2 in cores:
        c = c2 // 2
        ib = idx[c2]
        for n in range(-NMAX, NMAX + 1):
            val = (c + n) / LAM
            j = rnd_half(val)
            j2 = 2 * j
            if j2 not in idx:
                continue
            dl = val - j
            z = 2j * np.pi * CC * n * RHO
            Bcoef = dl / RHO
            M = np.zeros((K, K), np.complex128)
            zl = 1.0 + 0.0j
            for d in range(K):
                # M[l, l-d] = z^d / d! for l-d >= 0
                pass
            for l in range(K):
                zl = 1.0 + 0.0j
                for d in range(l + 1):
                    M[l, l - d] = zl / fact[d]
                    zl *= z
            Cm = np.zeros((K, K), np.complex128)
            bp = 1.0 + 0.0j
            bpow = []
            for i in range(K):
                bpow.append(bp)
                bp *= Bcoef
            for kk in range(K):
                for jj in range(kk + 1):
                    Cm[jj, kk] = fact[kk] / (fact[jj] * fact[kk - jj]) * lamp[jj] * bpow[kk - jj]
            ph = np.exp(2j * np.pi * CC * n * (c2 / 2.0))
            B = (M @ Cm) * ph
            blocks.setdefault(n, []).append((ib, idx[j2], B))
            ns.add(n)
    NS = sorted(ns)
    # dense N_n / later divide by s. First form A(0) = sum wa(n) M_n
    A0 = np.zeros((D, D), np.complex128)
    raw = {}
    for n in NS:
        coef = wa(n)
        raw[n] = []
        for ib, jb, B in blocks[n]:
            BB = coef * B
            raw[n].append((ib, jb, BB))
            A0[ib * K : (ib + 1) * K, jb * K : (jb + 1) * K] += BB
    ev, R = np.linalg.eig(A0)
    i = int(np.argmax(np.abs(ev)))
    s = ev[i]
    Phi = R[:, i]
    evl, Lv = np.linalg.eig(A0.T)
    psi = Lv[:, int(np.argmin(np.abs(evl - s)))]
    Msh = A0 - (s + 1e-7) * np.eye(D)
    for _ in range(3):
        Phi = np.linalg.solve(Msh, Phi)
        Phi /= np.linalg.norm(Phi)
        psi = np.linalg.solve(Msh.T, psi)
        psi /= np.linalg.norm(psi)
    s = (psi @ A0 @ Phi) / (psi @ Phi)
    Phi = Phi / np.linalg.norm(Phi)
    psi = psi / (psi @ Phi)
    # store N_n = wa M_n / s
    Nn = {}
    for n in NS:
        Nn[n] = [(ib, jb, B / s) for ib, jb, B in raw[n]]
    # pairs for each v
    pair = {}
    for v in range(-60, 61):
        lst = []
        for n in NS:
            m = n - v
            if m in Nn:
                lst.append((n, m))
        pair[v] = lst
    print(
        "model",
        "D",
        D,
        "cores",
        len(cores),
        "modes",
        len(NS),
        "pairs_v0",
        len(pair[0]),
        "|s|",
        abs(s),
        "sec",
        round(time.time() - t0, 2),
        flush=True,
    )
    return D, NS, Nn, pair, complex(s), Phi.astype(np.complex128), psi.astype(np.complex128)


def prepare_batch(Nn):
    """Stack every core block so N@Y is one GEMM."""
    meta = []  # (n, ib, jb)
    Bs = []
    for n, bl in Nn.items():
        for ib, jb, B in bl:
            meta.append((n, ib, jb))
            Bs.append(np.ascontiguousarray(B))
    Bstack = np.stack(Bs)
    BH = np.conjugate(np.transpose(Bstack, (0, 2, 1)))
    # index blocks by n
    by_n = {}
    for i, (n, ib, jb) in enumerate(meta):
        by_n.setdefault(n, []).append(i)
    return Bstack, BH, meta, by_n


def apply_N_all(Bstack, meta, Y, D, NS):
    nb = len(meta)
    Ys = np.empty((nb, K, D), np.complex128)
    for i, (_n, _ib, jb) in enumerate(meta):
        Ys[i] = Y[jb * K : (jb + 1) * K]
    Out = Bstack @ Ys
    Ws = {n: np.zeros((D, D), np.complex128) for n in NS}
    for i, (n, ib, _jb) in enumerate(meta):
        Ws[n][ib * K : (ib + 1) * K] += Out[i]
    return Ws


def accumulate_Tv(Z, Ws, n, m, Nn, D):
    W = Ws[n]
    for ib, jb, B in Nn[m]:
        Z[:, ib * K : (ib + 1) * K] += W[:, jb * K : (jb + 1) * K] @ B.conj().T


def run(E: int, iters: int, model):
    D, NS, Nn, pair, s, Phi, psi = model
    es = range(-E, E + 1)
    nE = 2 * E + 1
    nst = nE * nE

    def sid(a, b):
        return (a + E) * nE + (b + E)

    Y = np.zeros((nst, D, D), np.complex128)
    Y[sid(0, 0)] = np.outer(Phi, Phi.conj())
    rates = []
    shares = []
    t0 = time.time()
    m0 = float(np.linalg.norm(Y[sid(0, 0)]))
    Bstack, _BH, meta, _by_n = prepare_batch(Nn)
    for it in range(iters):
        new = np.zeros_like(Y)
        for a in es:
            for b in es:
                i = sid(a, b)
                if not np.any(Y[i]):
                    continue
                Ws = apply_N_all(Bstack, meta, Y[i], D, NS)
                for e in es:
                    v = e - 6 * a + b
                    if abs(v) > 60 or not pair[v]:
                        continue
                    Z = new[sid(e, a)]
                    for n, m in pair[v]:
                        accumulate_Tv(Z, Ws, n, m, Nn, D)
        # g_carry mass is the sum of Frobenius norms, not the global Frobenius norm
        m1 = float(sum(np.linalg.norm(new[i]) for i in range(nst)))
        rate = m1 / m0
        new /= m1
        Y = new
        m0 = 1.0
        share = float(np.linalg.norm(Y[sid(0, 0)]))
        rates.append(rate)
        shares.append(share)
        print(
            "E",
            E,
            "it",
            it,
            "rate",
            "%.8f" % rate,
            "share",
            "%.6f" % share,
            "inv",
            "%.4f" % (1.0 / share if share else float("inf")),
            "sec",
            round(time.time() - t0, 1),
            flush=True,
        )
    out = dict(
        E=E,
        iters=iters,
        rates=rates,
        shares=shares,
        inv_share=[(1.0 / s_ if s_ else None) for s_ in shares],
        final_rate=rates[-1],
        final_share=shares[-1],
        seconds=time.time() - t0,
        D=D,
        n_modes=len(NS),
        abs_s=abs(s),
        tag="N",
        note="binary64 Galerkin rebuild and Frobenius power iteration; not an interval certificate",
    )
    path = os.path.join(LOGS, f"phase_carry_E{E}.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print("wrote", path, flush=True)
    return out


if __name__ == "__main__":
    import sys

    model = build_model()
    E = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    iters = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    run(E, iters, model)
