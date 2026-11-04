"""Entrywise disk-ball iteration of the single-window carry map.

Blocks are built in flint balls, then stored as complex128 midpoints and
float64 radii. Each product (A±α)(B±β) is enclosed by

    mid  = fl(A B)
    rad  = (1+θ) (|A| β + α |B| + α β + γ |A| |B|)

with γ a Higham factor for the complex dot products and θ = 10^{-8} a
margin for rounding in the radius products themselves. Sums of balls add
radii and add a unit roundoff times the new magnitude.

The scalar s is the Rayleigh quotient of the computed unit vectors, enclosed
by the same block balls. It is not a separate enclosure of the exact
eigenvalue of A(0). The initial matrix is the float outer product φφ*,
widened by a unit-roundoff disk.

Mass is the sum of Frobenius norms. For one matrix the Frobenius norm of
every entrywise selection inside the disks lies between

    sqrt(sum max(0, |m|-r)^2)  and  sqrt(sum (|m|+r)^2).

Tag [CA] when those disks are propagated. Pass --float for the binary64
midpoint iteration with no radii, which is [N].
"""
from __future__ import annotations

import json
import math
import os
import time

import numpy as np
from flint import acb, arb, ctx

import phase_carry as pc

ctx.prec = 80

K = pc.K
K0 = pc.K0
NMAX = pc.NMAX
RHO = pc.RHO
XJ = pc.XJ
A_SEC = pc.A_SEC
U = 2.0**-53
# Complex accumulation over K terms: four real multiplies, a generous factor 16.
GAMMA = (16 * K * U) / (1.0 - 16 * K * U)
THETA = 1e-8
LOGS = pc.LOGS


def cores_and_index():
    cores = [c2 for c2 in range(-2 * K0 - 2, 2 * K0 + 3) if c2 % 2 == 0 and abs(c2) / 2 <= K0]
    idx = {c2: i for i, c2 in enumerate(cores)}
    return cores, idx


def entry_disk(z: acb):
    re = float(z.real.mid())
    im = float(z.imag.mid())
    rr = float(z.real.rad())
    ri = float(z.imag.rad())
    rad = math.hypot(rr, ri) + (2.0**-52) * (abs(re) + abs(im))
    return re, im, rad


def build_block_disks():
    """Enclose wa(n) M_n before division by s."""
    t0 = time.time()
    sqrt2 = arb(2).sqrt()
    lam = arb(3) + 2 * sqrt2
    cc = 1 / (lam - 1 / lam)
    pi = arb.pi()
    two_pi_i = acb(0, 2 * pi)
    cores, idx = cores_and_index()
    D = len(cores) * K
    fact = [arb(1)]
    for i in range(1, K):
        fact.append(fact[-1] * i)
    lamp = [arb(1)]
    inv_lam = 1 / lam
    for i in range(1, K):
        lamp.append(lamp[-1] * inv_lam)
    xj = arb(str(XJ))

    def j_signed(n: int) -> arb:
        j = xj.bessel_j(arb(abs(n)))
        if n < 0 and (n % 2):
            j = -j
        return j

    def wa(n: int) -> acb:
        theta = cc * (arb(n) * n) / 2 + arb(A_SEC) * n / 8
        phase = (two_pi_i * theta).exp()
        turn = [acb(1), acb(0, 1), acb(-1), acb(0, -1)][n % 4]
        return turn * j_signed(n) * phase

    raw = {}  # n -> list (ib, jb, mid, rad) of wa*B, not yet /s
    ns = set()
    for c2 in cores:
        c = c2 // 2
        ib = idx[c2]
        for n in range(-NMAX, NMAX + 1):
            val = (arb(c) + n) / lam
            # floor(val + 1/2). lam is irrational, so this is never a half-integer.
            # The ball radius at precision 80 is far below 10^{-10}; refuse if the
            # midpoint sits within 10^{-8} of an integer, where the floor could flip.
            probe = val + arb(1) / 2
            midf = float(probe.mid())
            if float(probe.rad()) > 1e-10 or abs(midf - round(midf)) < 1e-8:
                raise RuntimeError(f"rounding ball is ambiguous at n={n} c={c}")
            j = math.floor(midf)
            j2 = 2 * j
            if j2 not in idx:
                continue
            dl = val - j
            z = two_pi_i * cc * n * arb(str(RHO))
            bcoef = dl / arb(str(RHO))
            M = acb.mat(K, K) if False else None
            M = __import__("flint").acb_mat(K, K)
            zl = acb(1)
            for l in range(K):
                zl = acb(1)
                for d in range(l + 1):
                    M[l, l - d] = zl / fact[d]
                    zl *= z
            Cm = __import__("flint").acb_mat(K, K)
            bp = acb(1)
            bpow = []
            for i in range(K):
                bpow.append(bp)
                bp *= bcoef
            for kk in range(K):
                for jj in range(kk + 1):
                    Cm[jj, kk] = (
                        fact[kk] / (fact[jj] * fact[kk - jj]) * lamp[jj] * bpow[kk - jj]
                    )
            ph = (two_pi_i * cc * n * arb(c2) / 2).exp()
            B = (M * Cm) * ph
            coef = wa(n)
            mid = np.empty((K, K), np.complex128)
            rad = np.empty((K, K), np.float64)
            for r in range(K):
                for col in range(K):
                    re, im, rd = entry_disk(coef * B[r, col])
                    mid[r, col] = re + 1j * im
                    rad[r, col] = rd
            raw.setdefault(n, []).append((ib, idx[j2], mid, rad))
            ns.add(n)
    NS = sorted(ns)
    print("blocks", sum(len(v) for v in raw.values()), "modes", len(NS), "sec", round(time.time() - t0, 2), flush=True)
    return D, NS, raw


def rayleigh(D, raw, phi, psi):
    """Enclose ψ* A φ / ψ* φ for the undivided blocks, φ and ψ exact float vectors."""
    aphi_mid = np.zeros(D, np.complex128)
    aphi_rad = np.zeros(D, np.float64)
    for bl in raw.values():
        for ib, jb, mid, rad in bl:
            seg = phi[jb * K : (jb + 1) * K]
            abseg = np.abs(seg)
            aphi_mid[ib * K : (ib + 1) * K] += mid @ seg
            aphi_rad[ib * K : (ib + 1) * K] += rad @ abseg + GAMMA * (np.abs(mid) @ abseg)
    aphi_rad *= 1.0 + THETA
    num_mid = psi @ aphi_mid
    num_rad = float(np.abs(psi) @ aphi_rad) + GAMMA * float(np.abs(psi) @ np.abs(aphi_mid))
    num_rad *= 1.0 + THETA
    den_mid = psi @ phi
    den_rad = GAMMA * float(np.abs(psi) @ np.abs(phi))
    den_rad *= 1.0 + THETA
    # (n ± ν) / (d ± δ)
    den_abs = abs(den_mid)
    if den_rad >= den_abs:
        raise RuntimeError("denominator ball contains 0")
    inv_abs = 1.0 / (den_abs - den_rad)
    s_mid = num_mid / den_mid
    s_rad = (num_rad * den_abs + abs(num_mid) * den_rad) * inv_abs * inv_abs
    s_rad += (2.0**-52) * abs(s_mid)
    s_rad *= 1.0 + THETA
    return s_mid, s_rad, num_mid, num_rad, den_mid, den_rad


def divide_by_s(raw, s_mid, s_rad):
    s_abs = abs(s_mid)
    if s_rad >= s_abs:
        raise RuntimeError("s ball contains 0")
    inv_abs = 1.0 / (s_abs - s_rad)
    Nn = {}
    for n, bl in raw.items():
        out = []
        for ib, jb, mid, rad in bl:
            mid_s = mid / s_mid
            rad_s = (rad * s_abs + np.abs(mid) * s_rad) * inv_abs * inv_abs
            rad_s += (2.0**-52) * np.abs(mid_s)
            rad_s *= 1.0 + THETA
            out.append(
                (
                    ib,
                    jb,
                    np.ascontiguousarray(mid_s),
                    np.ascontiguousarray(rad_s),
                    np.ascontiguousarray(mid_s.conj().T),
                    np.ascontiguousarray(rad_s.T),
                )
            )
        Nn[n] = out
    return Nn


def fro_bounds(mid, rad):
    mag = np.abs(mid)
    hi = float(np.sqrt(np.sum((mag + rad) ** 2)))
    lo = float(np.sqrt(np.sum(np.maximum(0.0, mag - rad) ** 2)))
    return lo, hi


def left_apply(Nn, NS, Ymid, Yrad, D):
    Wmid = {n: np.zeros((D, D), np.complex128) for n in NS}
    Wrad = {n: np.zeros((D, D), np.float64) for n in NS}
    for n, bl in Nn.items():
        for ib, jb, mid, rad, _ct, _rt in bl:
            ys = Ymid[jb * K : (jb + 1) * K, :]
            yr = Yrad[jb * K : (jb + 1) * K, :]
            ab_ys = np.abs(ys)
            ab_b = np.abs(mid)
            out_m = mid @ ys
            out_r = ab_b @ yr + rad @ ab_ys + rad @ yr + GAMMA * (ab_b @ ab_ys)
            out_r *= 1.0 + THETA
            sl = slice(ib * K, (ib + 1) * K)
            Wrad[n][sl, :] += out_r + U * (np.abs(Wmid[n][sl, :]) + np.abs(out_m))
            Wmid[n][sl, :] += out_m
    return Wmid, Wrad


def scatter_chunk(Zmid, Zrad, out_m, out_r, ibs):
    for i, ib in enumerate(ibs):
        sl = slice(ib * K, (ib + 1) * K)
        Zrad[:, sl] += out_r[i] + U * (np.abs(Zmid[:, sl]) + np.abs(out_m[i]))
        Zmid[:, sl] += out_m[i]


def right_edges(Wmid, Wrad, Nn, pair, a, E, D, new):
    """Apply every legal carry step out of (a, ·) and add into new[(e, a)]."""
    tasks_e = []
    tasks_ib = []
    tasks_n = []
    tasks_jb = []
    tasks_ct = []
    tasks_rt = []
    for e in range(-E, E + 1):
        v = e - 6 * a + 0  # placeholder, b is closed over below
        # filled by caller via closure — replaced in run()
        raise RuntimeError("use right_edges_b")
    return tasks_e


def apply_state(Wmid, Wrad, Nn, pair, a, b, E, D, new, use_rad):
    es_tasks = []
    for e in range(-E, E + 1):
        v = e - 6 * a + b
        if abs(v) > 60:
            continue
        for n, m in pair[v]:
            for ib, jb, _mid, _rad, ct, rt in Nn[m]:
                es_tasks.append((e, n, ib, jb, ct, rt))
    if not es_tasks:
        return
    chunk = 160
    for start in range(0, len(es_tasks), chunk):
        part = es_tasks[start : start + chunk]
        L = np.empty((len(part), D, K), np.complex128)
        R = np.empty((len(part), K, K), np.complex128)
        for i, (e, n, ib, jb, ct, rt) in enumerate(part):
            L[i] = Wmid[n][:, jb * K : (jb + 1) * K]
            R[i] = ct
        out_m = L @ R
        if use_rad:
            La = np.empty((len(part), D, K), np.float64)
            Ra = np.empty((len(part), K, K), np.float64)
            Lr = np.empty((len(part), D, K), np.float64)
            Rr = np.empty((len(part), K, K), np.float64)
            for i, (e, n, ib, jb, ct, rt) in enumerate(part):
                sl = Wmid[n][:, jb * K : (jb + 1) * K]
                La[i] = np.abs(sl)
                Lr[i] = Wrad[n][:, jb * K : (jb + 1) * K]
                Ra[i] = np.abs(ct)
                Rr[i] = rt
            out_r = La @ Rr + Lr @ Ra + Lr @ Rr + GAMMA * (La @ Ra)
            out_r *= 1.0 + THETA
        for i, (e, n, ib, jb, ct, rt) in enumerate(part):
            key = (e, a)
            if key not in new:
                new[key] = (
                    np.zeros((D, D), np.complex128),
                    np.zeros((D, D), np.float64) if use_rad else None,
                )
            Zm, Zr = new[key]
            sl = slice(ib * K, (ib + 1) * K)
            if use_rad:
                Zr[:, sl] += out_r[i] + U * (np.abs(Zm[:, sl]) + np.abs(out_m[i]))
            Zm[:, sl] += out_m[i]


def mass_bounds(states, use_rad):
    lo = 0.0
    hi = 0.0
    for mid, rad in states.values():
        if use_rad:
            a, b = fro_bounds(mid, rad)
        else:
            a = b = float(np.linalg.norm(mid))
        lo += a
        hi += b
    return lo, hi


def run(E, iters, use_rad, model_float, disks):
    D, NS, raw = disks
    _D, _NS, _Nn, pair, s_float, Phi, psi = model_float
    s_mid, s_rad, num_mid, num_rad, den_mid, den_rad = rayleigh(D, raw, Phi, psi)
    Nn = divide_by_s(raw, s_mid, s_rad)
    # compare one block to the float model
    n0 = NS[len(NS) // 2]
    ib, jb, mid, rad, _ct, _rt = Nn[n0][0]
    float_blocks = {(ib_, jb_): B for ib_, jb_, B in _Nn[n0]}
    if (ib, jb) in float_blocks:
        diff = float(np.max(np.abs(mid - float_blocks[(ib, jb)])))
    else:
        diff = None
    Ymid = np.outer(Phi, Phi.conj())
    Yrad = (4 * U) * (np.abs(Ymid) + 1e-30)
    states = {(0, 0): (Ymid, Yrad if use_rad else None)}
    rates = []
    shares = []
    t0 = time.time()
    print(
        "s_rad",
        s_rad,
        "|s_mid|",
        abs(s_mid),
        "|s_float|",
        abs(s_float),
        "block_diff",
        diff,
        "gamma",
        GAMMA,
        flush=True,
    )
    for it in range(iters):
        m_lo, m_hi = mass_bounds(states, use_rad)
        new = {}
        # Pop inputs as they are consumed so the live set is one generation.
        for a, b in list(states.keys()):
            mid, rad = states.pop((a, b))
            if use_rad:
                if m_hi == 0:
                    continue
            elif not np.any(mid):
                continue
            if use_rad:
                Wm, Wr = left_apply(Nn, NS, mid, rad, D)
            else:
                Wm, Wr = left_apply(Nn, NS, mid, np.zeros((D, D)), D)
            apply_state(Wm, Wr, Nn, pair, a, b, E, D, new, use_rad)
            del Wm, Wr, mid, rad
        n_lo, n_hi = mass_bounds(new, use_rad)
        if m_lo <= 0 or n_lo <= 0:
            rate_lo, rate_hi = 0.0, float("inf")
        else:
            rate_lo = n_lo / m_hi
            rate_hi = n_hi / m_lo
        rate_mid = n_hi / m_hi if m_hi else float("nan")  # replaced below
        # scale by a float inside [n_lo, n_hi] when the interval is finite
        scale = 0.5 * (n_lo + n_hi) if n_hi < float("inf") and n_lo > 0 else (n_hi or 1.0)
        rel = ((n_hi - n_lo) / n_lo) if n_lo > 0 else float("inf")
        scaled = {}
        for key, (mid, rad) in new.items():
            mid = mid / scale
            if use_rad:
                rad = rad / scale
                # μ/M lies in scale/[n_hi] .. scale/[n_lo]; widen by that factor
                rad = rad * (scale / n_lo) + np.abs(mid) * rel
                rad *= 1.0 + THETA
            scaled[key] = (mid, rad)
        states = scaled
        share_lo, share_hi = fro_bounds(*states[(0, 0)]) if (0, 0) in states else (0.0, 0.0)
        # rate of this step, from the pre-scale masses
        if not use_rad:
            rate_lo = rate_hi = n_hi / m_hi
        rates.append({"lo": rate_lo, "hi": rate_hi})
        shares.append({"lo": share_lo, "hi": share_hi, "rel_width": rel})
        print(
            "E",
            E,
            "ball" if use_rad else "float",
            "it",
            it,
            "rate",
            "%.10f" % rate_lo,
            "%.10f" % rate_hi,
            "share",
            "%.6f" % share_lo,
            "%.6f" % share_hi,
            "rel",
            "%.3e" % rel,
            "states",
            len(states),
            "sec",
            round(time.time() - t0, 1),
            flush=True,
        )
        if use_rad and not math.isfinite(rate_hi):
            break
    # prefactor at 0.28 from upper rates
    prod = 1.0
    pmax = 1.0
    p_at = []
    finite = True
    for i, r in enumerate(rates):
        if not math.isfinite(r["hi"]):
            finite = False
            break
        prod *= r["hi"] / 0.28
        pmax = max(pmax, prod)
        p_at.append(prod)
    out = {
        "E": E,
        "ball": use_rad,
        "tag": "CA" if use_rad else "N",
        "iters": len(rates),
        "rates": rates,
        "shares": shares,
        "rate_hi_last": rates[-1]["hi"] if rates else None,
        "rate_lo_last": rates[-1]["lo"] if rates else None,
        "rate_hi_below_0.28": bool(rates) and all(math.isfinite(r["hi"]) and r["hi"] < 0.28 for r in rates[3:]),
        "prefactor_0.28_hi": pmax if finite else None,
        "prefactor_path": p_at,
        "s_mid_re": s_mid.real,
        "s_mid_im": s_mid.imag,
        "s_rad": s_rad,
        "s_float_abs": abs(s_float),
        "s_mid_abs": abs(s_mid),
        "block_mid_minus_float_max": diff,
        "gamma": GAMMA,
        "theta": THETA,
        "seconds": time.time() - t0,
        "n_states_final": len(states),
        "note": (
            "Entrywise complex disks around the Rayleigh-normalised Galerkin carry map. "
            "s is the Rayleigh quotient of the computed vectors, not a certified eigenpair. "
            "rate_hi < 0.28 on the tail of the orbit encloses that orbit only."
            if use_rad
            else "binary64 midpoints of the same blocks; not an enclosure."
        ),
    }
    tag = "ball" if use_rad else "stream"
    path = os.path.join(LOGS, f"phase_carry_{tag}_E{E}.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print("wrote", path, flush=True)
    return out


def main():
    import sys

    argv = sys.argv[1:]
    use_rad = "--float" not in argv
    argv = [a for a in argv if a != "--float"]
    print("building float model", flush=True)
    model = pc.build_model()
    print("building arb blocks", flush=True)
    disks = build_block_disks()
    if argv and argv[0] == "range":
        lo = int(argv[1])
        hi = int(argv[2])
        for E in range(lo, hi + 1):
            iters = 8 if E <= 4 else 6
            print("==== E", E, "iters", iters, "====", flush=True)
            try:
                run(E, iters, use_rad, model, disks)
            except Exception as exc:
                print("FAIL E", E, type(exc).__name__, exc, flush=True)
                continue
        return
    E = int(argv[0]) if argv else 0
    iters = int(argv[1]) if len(argv) > 1 else 8
    run(E, iters, use_rad, model, disks)


if __name__ == "__main__":
    main()
