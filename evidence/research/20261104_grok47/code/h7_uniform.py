"""Uniform bound on the finite-section trace, over every twist.

The section is the multi-disc vertex operator of h7_multidisc_cert.py:
centres |c| <= 3, 40 modes, letters |n| <= 16, dimension 280, disc radius
6/5. A positive diagonal weight, recorded as exact float64 dyadics, induces
a vector norm in which every twisted step has operator norm at most R.
The monodromy of any twist sequence of length P then has trace at most
dim * R^P. Sectors are shifts of the twist and are included.

Commands
    python3 h7_uniform.py self-test
    python3 h7_uniform.py freeze
    python3 h7_uniform.py cert
    python3 h7_uniform.py kappa
    python3 h7_uniform.py all

self-test checks the cosine sum, a 2x2 norm certificate, and the d=287
mass formula. freeze writes the diagonal. cert encloses the operator norm.
kappa encloses the residue weight and the comparison at d=3437426497.
"""

from __future__ import annotations

import json
import math
import os
import struct
import sys
import time

import numpy as np
from flint import acb, acb_mat, arb, ctx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h7_multidisc_cert as cert  # noqa: E402
from h7_lin_cert import f_hi, f_lo, kappa_acb, tb_prime  # noqa: E402
from h7_rates import hi_f, lo_f, newton_enclose  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "..", "logs")
WEIGHTS = os.path.join(LOG_DIR, "h7_uniform_weights.json")
OUT = os.path.join(LOG_DIR, "h7_uniform.json")

DIM = 280
K_MODES = 40
CENTRES = list(range(-3, 4))
U_ROUND = arb(2) ** (-52)


def arb_from_float(x: float) -> arb:
    """Exact arb for a binary64 value. Powers of two are exact in flint."""
    if x == 0.0:
        return arb(0)
    if not math.isfinite(x):
        raise ValueError(x)
    bits = struct.unpack(">Q", struct.pack(">d", x))[0]
    sign = -1 if (bits >> 63) else 1
    exp = (bits >> 52) & 0x7FF
    mant = bits & ((1 << 52) - 1)
    if exp == 0:
        return arb(sign * mant) * (arb(2) ** (1 - 1023 - 52))
    if exp == 0x7FF:
        raise ValueError(x)
    mant |= 1 << 52
    return arb(sign * mant) * (arb(2) ** (exp - 1023 - 52))


def ulp(x: float) -> float:
    """Unit in the last place of a binary64 number. Zero maps to the minimum."""
    if x == 0.0 or not math.isfinite(x):
        return 2.0**-1074
    return 2.0 ** (math.floor(math.log2(abs(x))) - 52)


def acb_from_complex(z: complex) -> acb:
    return acb(arb_from_float(float(z.real)), arb_from_float(float(z.imag)))


def frob_np(M: np.ndarray) -> arb:
    """Upper bound on the Frobenius norm of a complex matrix of binary64 entries."""
    s = arb(0)
    # Each |z|^2 = re^2 + im^2 is exact as a mathematical function of the
    # dyadics; the arb sum encloses it.
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            z = M[i, j]
            re = arb_from_float(float(z.real))
            im = arb_from_float(float(z.imag))
            s += re * re + im * im
    return s.sqrt()


def eval_factor(k: int) -> arb:
    """Factor in ||float combination - exact combination||_F <= factor * sum |c| ||M||_F.

    Binary64, round to nearest, componentwise on complex values. A fused
    multiply-add would only make the product error smaller. k terms.
    """
    u = U_ROUND
    if not (k * u < arb(1) / 2):
        raise RuntimeError("summation length too long for the gamma bound")
    gamma = (k * u) / (1 - k * u)
    # |complex error| <= sqrt(2) * (6u + gamma*(1+6u)) * sum |terms|
    return arb(2).sqrt() * (6 * u + gamma * (1 + 6 * u))


def certify_op(M: np.ndarray, R: arb) -> dict:
    """Prove ||M||_2 <= R for the exact matrix whose entries are these binary64 values.

    A float Cholesky factor of R^2 I - M* M is a witness. Ball arithmetic
    encloses the residual, and a float inverse encloses the smallest
    singular value of the factor from below.
    """
    n = M.shape[0]
    Rf = float(R)
    Gram = M.conj().T @ M
    H = (Rf * Rf) * np.eye(n) - Gram
    H = (H + H.conj().T) / 2
    try:
        G = np.linalg.cholesky(H)
    except np.linalg.LinAlgError:
        return {"ok": False, "reason": "cholesky"}
    B = np.linalg.inv(G)
    data_M = [acb_from_complex(M[i, j]) for i in range(n) for j in range(n)]
    data_G = [acb_from_complex(G[i, j]) for i in range(n) for j in range(n)]
    data_B = [acb_from_complex(B[i, j]) for i in range(n) for j in range(n)]
    AM = acb_mat(n, n, data_M)
    AG = acb_mat(n, n, data_G)
    AB = acb_mat(n, n, data_B)
    Gram_ex = AM.conjugate().transpose() * AM
    # numpy.linalg.cholesky returns G with G G^H = H.
    GG = AG * AG.conjugate().transpose()
    eye = [acb(1 if i == j else 0) for i in range(n) for j in range(n)]
    # F = I - G B, so G^{-1} = B (I-F)^{-1} when ||F||_2 < 1.
    FB = acb_mat(n, n, eye) - AG * AB
    R2 = R * R
    sE = arb(0)
    sF = arb(0)
    sB = arb(0)
    for i in range(n):
        for j in range(n):
            e = ((R2 if i == j else arb(0)) - Gram_ex[i, j]) - GG[i, j]
            sE += e.abs_upper() ** 2
            sF += FB[i, j].abs_upper() ** 2
            sB += AB[i, j].abs_upper() ** 2
    e_frob = sE.sqrt()
    f_frob = sF.sqrt()
    b_frob = sB.sqrt()
    if not (f_frob < 1):
        return {
            "ok": False,
            "reason": "inverse residual",
            "f_frob": str(f_frob),
            "e_frob": str(e_frob),
        }
    sig = (1 - f_frob) / b_frob
    slack = sig * sig - e_frob
    ok = bool(slack > 0)
    return {
        "ok": ok,
        "reason": None if ok else "slack",
        "e_frob_hi": hi_f(e_frob),
        "f_frob_hi": hi_f(f_frob),
        "sig_lo": lo_f(sig),
        "slack_lo": lo_f(slack) if ok else f_lo(slack),
    }


# ---------- weights ----------


def _layout_logw(gamma: float, delta: float) -> np.ndarray:
    logw = np.empty(DIM)
    for ci, c in enumerate(CENTRES):
        for k in range(K_MODES):
            logw[ci * K_MODES + k] = k * math.log(gamma) + abs(c) * math.log(delta)
    return logw


def freeze_weights() -> dict:
    """Diagonal that minimises the max twist 2-norm, from a geometric start.

    The search is floating point. The certificate uses the dyadics it writes,
    not the fact that they are optimal.
    """
    sys.path.insert(0, HERE)
    import h7_multidisc as md

    ns, mats, _meta = md.build_letters(3, 1.2, 40, 16)
    grid = np.linspace(0.0, 1.0, 25, endpoint=False)
    Ls = [md.L_of(ns, mats, float(th)) for th in grid]
    logw = _layout_logw(0.5, 0.45)
    eta = 0.2

    def apply(logw, L):
        s = np.exp(logw - logw.mean())
        return (s[:, None] * L) / s[None, :]

    for it in range(36):
        grads = []
        worst = -1.0
        for L in Ls:
            Lw = apply(logw, L)
            u, sig, vh = np.linalg.svd(Lw, full_matrices=False)
            op = float(sig[0])
            if op > worst:
                worst = op
            grads.append((op, np.abs(u[:, 0]) ** 2 - np.abs(vh[0]) ** 2))
        g = np.zeros(DIM)
        nused = 0
        for op, gi in grads:
            if op > worst * 0.998:
                g += gi
                nused += 1
        g /= max(nused, 1)
        g -= g.mean()
        logw = logw - eta * g
        if it % 6 == 5:
            eta = max(eta * 0.8, 0.04)
            print(f"  freeze iter {it} worst {worst:.6f} nused {nused}", flush=True)
    s = np.exp(logw - logw.max())
    fine = np.linspace(0.0, 1.0, 361, endpoint=False)
    mx = 0.0
    arg = 0.0
    for th in fine:
        Lw = (s[:, None] * md.L_of(ns, mats, float(th))) / s[None, :]
        op = float(np.linalg.norm(Lw, 2))
        if op > mx:
            mx = op
            arg = float(th)
    L0 = md.L_of(ns, mats, 0.0)
    rho0 = float(max(abs(z) for z in np.linalg.eigvals(L0)))
    op0 = float(np.linalg.norm(L0, 2))
    # geometric comparison, not certified
    sg = np.exp(_layout_logw(0.5, 0.45))
    sg /= sg.max()
    gmx = 0.0
    for th in fine[::3]:
        Lw = (sg[:, None] * md.L_of(ns, mats, float(th))) / sg[None, :]
        gmx = max(gmx, float(np.linalg.norm(Lw, 2)))
    doc = {
        "dim": DIM,
        "centres": CENTRES,
        "K": K_MODES,
        "normalisation": "max entry 1",
        "float_max_op": mx,
        "float_max_at": arg,
        "float_grid": 361,
        "float_rho_unweighted_theta0": rho0,
        "float_op_unweighted_theta0": op0,
        "float_geometric_max_op": gmx,
        "geometric": {"mode": "1/2", "centre": "0.45^|c|"},
        "weights_hex": [float(v).hex() for v in s],
    }
    os.makedirs(LOG_DIR, exist_ok=True)
    json.dump(doc, open(WEIGHTS, "w"), indent=1)
    print(f"froze max op {mx:.6f} at {arg} rho0 {rho0:.6f} geometric {gmx:.6f}", flush=True)
    return doc


def load_weights() -> np.ndarray:
    doc = json.load(open(WEIGHTS))
    s = np.array([float.fromhex(h) for h in doc["weights_hex"]], dtype=np.float64)
    if s.shape != (DIM,) or np.any(s <= 0):
        raise RuntimeError("bad weights")
    return s


# ---------- letters ----------


def build_weighted_letters(s: np.ndarray):
    """Arb letters, then binary64 midpoints and a Frobenius radius for each."""
    centers, index, blocks, n_out = cert.build_blocks()
    if n_out != 0:
        raise RuntimeError(f"section is not forward-invariant: {n_out}")
    s_arb = [arb_from_float(float(v)) for v in s]
    mids = []
    radii = []
    frobs = []
    unweighted_sum = [acb(0)] * (DIM * DIM)
    for n in range(-cert.N_MAX, cert.N_MAX + 1):
        data = [acb(0)] * (DIM * DIM)
        for c in centers:
            key = (n, c)
            if key not in blocks:
                continue
            j, block = blocks[key]
            r0 = index[c] * K_MODES
            q0 = index[j] * K_MODES
            for r in range(K_MODES):
                for q in range(K_MODES):
                    data[(r0 + r) * DIM + (q0 + q)] += block[r, q]
        M = np.zeros((DIM, DIM), dtype=np.complex128)
        rad2 = arb(0)
        for i in range(DIM):
            for j in range(DIM):
                raw = data[i * DIM + j]
                if i == 0 and j == 0 and n == 0:
                    pass
                weighted = raw * (s_arb[i] / s_arb[j])
                mid = weighted.mid()
                re = float(mid.real)
                im = float(mid.imag)
                M[i, j] = re + 1j * im
                extra = arb_from_float(ulp(re)) + arb_from_float(ulp(im))
                rad = weighted.rad() + extra
                rad2 += rad * rad
                if n == 0 or True:
                    unweighted_sum[i * DIM + j] += raw
        mids.append(M)
        radii.append(rad2.sqrt())
        frobs.append(frob_np(M))
        print(f"  letter {n} frob {hi_f(frobs[-1]):.6f} rad {hi_f(radii[-1]):.3e}", flush=True)
    L0 = acb_mat(DIM, DIM, unweighted_sum)
    ns = list(range(-cert.N_MAX, cert.N_MAX + 1))
    return ns, mids, radii, frobs, L0


def coeff(n: int, theta: arb, delta: arb, sign: int) -> acb:
    """exp(2 π i n θ) * (1 + sign * δ * 2 π i n)."""
    phase = acb(2 * n * theta).exp_pi_i()
    two_pi_i_n = acb(0, 2) * arb.pi() * n
    return phase * (1 + acb(sign) * delta * two_pi_i_n)


def combine(ns, mids, cs: list[acb]) -> tuple[np.ndarray, list[float], list[float]]:
    """Sequential binary64 combination. Returns the matrix, |c| used, and coefficient-error bounds."""
    acc = np.zeros((DIM, DIM), dtype=np.complex128)
    used = []
    cerr = []
    for c, M in zip(cs, mids):
        mid = c.mid()
        re = float(mid.real)
        im = float(mid.imag)
        acc += complex(re, im) * M
        used.append(abs(complex(re, im)))
        cerr.append(hi_f(c.rad()) + ulp(re) + ulp(im))
    return acc, used, cerr


def lambda2(ns, radii, frobs) -> arb:
    """||L''(θ)||_2 <= sum (2 π n)^2 (||mid||_F + radius), for every θ."""
    total = arb(0)
    two_pi = 2 * arb.pi()
    for n, rad, fr in zip(ns, radii, frobs):
        total += (two_pi * abs(n)) ** 2 * (fr + rad)
    return total


def budget(ns, cs, used, cerr, radii, frobs, factor: arb) -> arb:
    """||true linear combination - float combination||_2."""
    eps = arb(0)
    sum_abs = arb(0)
    for c, u, ce, rad, fr in zip(cs, used, cerr, radii, frobs):
        # |c_true| <= abs_upper of the ball
        eps += c.abs_upper() * rad
        eps += arb_from_float(ce) * fr
        sum_abs += arb_from_float(u) * fr
    eps += factor * sum_abs
    return eps


# ---------- cosine mass ----------


def cos_sum_closed(q: int) -> arb:
    """sum_{k=1}^{q-1} |cos(π k/q)| = csc(π/(2q)) - 1, q odd."""
    if q % 2 == 0:
        raise ValueError(q)
    s = (arb.pi() / (2 * q)).sin()
    return 1 / s - 1


def local_mass(q: int) -> arb:
    """sum_{x,y mod q} |κ_q(N(x,y))|, with |κ(0)|=q-2 and |κ(v)|=2|cos| off zero.

    r(0)=2q-1 and r(v)=q-1 for v≠0, because (2/q)=1 makes x^2-2y^2 equivalent to uv.
    That Legendre symbol is +1 precisely when q is 1 or 7 mod 8.
    """
    if q % 8 not in (1, 7):
        raise ValueError((q, "2 is not a square"))
    cos_mass = cos_sum_closed(q)
    # sum_{v≠0} |κ(v)| = sum_{k=1}^{q-1} 2|cos(π k/q)| = 2 (csc(π/(2q))-1)
    nonzero = 2 * cos_mass
    return arb(2 * q - 1) * (q - 2) + arb(q - 1) * nonzero


def mass_check_small() -> dict:
    """Closed form against a direct sum, at a few odd primes, and at d=7*41."""
    rows = []
    # q=5 is not 1 or 7 mod 8; the cosine identity does not need that congruence.
    # Check it by a direct sum, bypassing local_mass.
    for q in (5, 17, 41):
        direct = arb(0)
        for k in range(1, (q - 1) // 2 + 1):
            # k/q <= 1/2, so π k/q is in (0, π/2] and the cosine is nonnegative.
            direct += (arb.pi() * k / q).cos()
        direct *= 2
        s = (arb.pi() / (2 * q)).sin()
        closed = 1 / s - 1
        gap = (direct - closed).abs_upper()
        rows.append({"q": q, "closed": str(closed), "direct": str(direct), "gap_hi": hi_f(gap)})
        if not (gap < arb(10) ** (-10)):
            raise RuntimeError(("cosine", q, str(gap)))
    # d=287 brute force of |κ(Nβ)| against the product of local masses
    m = 15
    facs = [7, 41]
    d = 287
    tbs = []
    invs = []
    for q in facs:
        cof = d // q
        tb = (tb_prime(m, q) * cof) % q
        tbs.append(tb)
        invs.append(pow(cof, -1, q))

    def kabs(u: int) -> float:
        acc = 1.0
        uu = u % d
        for q, tb, inv in zip(facs, tbs, invs):
            v = (uu * inv) % q
            if v == 0:
                acc *= float(q - 2)
            else:
                ang = (pow(tb, -1, q) * v) % q
                # |-1 - exp(2 π i ang/q)| = 2 |cos(π ang/q)|
                acc *= 2.0 * abs(math.cos(math.pi * ang / q))
        return acc

    total = 0.0
    for x in range(d):
        x2 = (x * x) % d
        for y in range(d):
            u = (x2 - 2 * ((y * y) % d)) % d
            total += kabs(u)
    product = local_mass(7) * local_mass(41)
    # float total versus the ball
    tf = arb_from_float(total)
    # brute-force rounding: each of d^2 terms has a few ulps. Allow 1e-8 relative.
    rel = (tf - product).abs_upper() / product.abs_lower()
    if not (rel < arb("1e-8")):
        raise RuntimeError(("mass", total, str(product), str(rel)))
    zero = kabs(0)
    return {
        "cosine": rows,
        "d": d,
        "brute_float": total,
        "product": str(product),
        "rel_hi": hi_f(rel),
        "kappa0_float": zero,
        "kappa0_exact": (7 - 2) * (41 - 2),
    }


def kappa_report(R_num: int | None, R_den: int | None) -> dict:
    """Residue weight at d=457*7521721 and the comparison with the η=1 threshold."""
    ctx.prec = 160
    q1, q2 = 457, 7521721
    for q in (q1, q2):
        if q % 8 != 1:
            raise RuntimeError((q, "not 1 mod 8"))
    S1 = local_mass(q1)
    S2 = local_mass(q2)
    total = S1 * S2
    zero = arb((q1 - 2) * (q2 - 2))
    nonzero = total - zero
    d = q1 * q2
    # threshold, same formula as h7_lin_cert.py
    lam = arb(3) + 2 * arb(2).sqrt()
    mu = arb("1.9154712")
    m = 57
    h = 9369319
    # recompute h_19
    u0, u1 = 1, 7
    for _ in range(1, (19 - 1) // 2):
        u0, u1 = u1, 6 * u1 - u0
    if u1 != h:
        raise RuntimeError((u1, h))
    zlo = (arb(1) / 2) * (1 - lam ** (-m)) * (mu ** m - arb("3012.4"))
    T = zlo * (arb(d) ** 2) / (2 * h)
    # untwisted section trace, sector 0, from the existing enclosure
    traces = json.load(open(os.path.join(LOG_DIR, "h7_lin_traces.json")))
    tr = next(
        row
        for row in traces["traces"]
        if row["d"] == d and row["beta"] == [0, 0] and row["sector"] == 0 and row["period"] == 57
    )
    re = arb(tr["trace"]["re"])
    im = arb(tr["trace"]["im"])
    tr_abs = (re * re + im * im).sqrt()
    C = arb(DIM)
    doc = {
        "d": d,
        "q": [q1, q2],
        "q_mod_8": [q1 % 8, q2 % 8],
        "S_q": [str(S1), str(S2)],
        "sum_all_beta": str(total),
        "sum_all_hi": hi_f(total),
        "sum_all_lo": lo_f(total),
        "kappa0": str(zero),
        "sum_nonzero": str(nonzero),
        "sum_nonzero_hi": hi_f(nonzero),
        "sum_nonzero_lo": lo_f(nonzero),
        "d2": str(d * d),
        "zlo": str(zlo),
        "zlo_lo": lo_f(zlo),
        "T": str(T),
        "T_lo": lo_f(T),
        "T_hi": hi_f(T),
        "untwisted_abs": str(tr_abs),
        "untwisted_lo": lo_f(tr_abs),
        "untwisted_hi": hi_f(tr_abs),
        "C": DIM,
        "P": 57,
    }
    # Any uniform cap is at least the untwisted trace. Triangle then exceeds T.
    obstacle = nonzero * tr_abs / T
    doc["triangle_from_untwisted_trace"] = str(obstacle)
    doc["triangle_from_untwisted_lo"] = lo_f(obstacle)
    if R_num is not None:
        R = arb(R_num) / R_den
        majorant = C * nonzero * (R ** 57)
        excess = majorant / T
        # R_* from C * U_hi * R_*^57 = T_lo would understate the ball.
        # Solve C * nonzero * R_*^57 = T inside the balls.
        ratio = T / (C * nonzero)
        # principal real 57th root
        Rstar = ratio ** (arb(1) / 57)
        doc.update(
            {
                "R": f"{R_num}/{R_den}",
                "majorant": str(majorant),
                "majorant_hi": hi_f(majorant),
                "majorant_lo": lo_f(majorant),
                "excess": str(excess),
                "excess_lo": lo_f(excess),
                "excess_hi": hi_f(excess),
                "Rstar": str(Rstar),
                "Rstar_lo": lo_f(Rstar),
                "Rstar_hi": hi_f(Rstar),
                "shrink": str(R / Rstar),
                "shrink_lo": lo_f(R / Rstar),
                "shrink_hi": hi_f(R / Rstar),
            }
        )
        # spectral-radius floor from the trace: rho >= (|Tr|/dim)^{1/57}
        floor = (tr_abs / C) ** (arb(1) / 57)
        doc["rho_floor_from_trace"] = str(floor)
        doc["rho_floor_lo"] = lo_f(floor)
        doc["rho_floor_over_Rstar_lo"] = lo_f(floor / Rstar)
    return doc


# ---------- certificate ----------


def certify() -> dict:
    t0 = time.time()
    ctx.prec = 160
    cert.RHO = arb(6) / arb(5)
    s = load_weights()
    ns, mids, radii, frobs, L0 = build_weighted_letters(s)
    factor = eval_factor(len(ns))
    L2 = lambda2(ns, radii, frobs)
    print(f"Lambda2 {hi_f(L2):.6f} factor {hi_f(factor):.3e}", flush=True)
    # Remainder target 0.004, with a cap so a loose majorant cannot explode the grid.
    rem_target = arb("0.006")
    # δ^2 = 2 rem / Λ2, N = ceil(1/(2δ))
    delta_max = (2 * rem_target / L2).sqrt()
    N = int(math.ceil(1.0 / (2.0 * float(delta_max))))
    N = max(N, 8)
    if N > 400:
        N = 400
    delta = arb(1) / (2 * N)
    rem = L2 * delta * delta / 2
    print(f"N {N} remainder {hi_f(rem):.6e}", flush=True)
    # Float pre-pass of the Taylor endpoints, to choose R.
    mx = 0.0
    for k in range(N):
        theta = arb(2 * k + 1) / (2 * N)
        for sign in (1, -1):
            cs = [coeff(n, theta, delta, sign) for n in ns]
            acc, _used, _cerr = combine(ns, mids, cs)
            mx = max(mx, float(np.linalg.norm(acc, 2)))
        if k % 40 == 0:
            print(f"  prepass {k}/{N} max {mx:.6f}", flush=True)
    target = mx + hi_f(rem) + 0.008
    # R = k/100 just above the target
    kR = int(math.ceil(target * 100.0 - 1e-12))
    print(f"prepass max {mx:.6f} R candidate {kR}/100", flush=True)
    passes = []
    worst = None
    bumps = 0
    while True:
        R = arb(kR) / 100
        failed = []
        worst_slack = None
        for k in range(N):
            theta = arb(2 * k + 1) / (2 * N)
            for sign in (1, -1):
                cs = [coeff(n, theta, delta, sign) for n in ns]
                acc, used, cerr = combine(ns, mids, cs)
                eps = budget(ns, cs, used, cerr, radii, frobs, factor)
                gap = R - rem - eps
                if not (gap > 0):
                    failed.append((k, sign, "budget"))
                    continue
                # A binary64 number at most the lower end of R - remainder - evaluation error.
                r_float = f_lo(gap)
                if r_float <= 0:
                    failed.append((k, sign, "budget"))
                    continue
                got = certify_op(acc, arb_from_float(r_float))
                if not got["ok"]:
                    failed.append((k, sign, got.get("reason")))
                else:
                    sl = got["slack_lo"]
                    if worst_slack is None or sl < worst_slack:
                        worst_slack = sl
            if k % 20 == 0:
                print(
                    f"  cert {k}/{N} fail {len(failed)} slack {worst_slack} t {time.time()-t0:.1f}",
                    flush=True,
                )
        if not failed:
            passes.append({"kR": kR, "n_fail": 0, "worst_slack_lo": worst_slack})
            break
        bumps += 1
        print(f"  {len(failed)} failures at {kR}/100, bumping", flush=True)
        passes.append({"kR": kR, "n_fail": len(failed), "sample": failed[:5]})
        if bumps > 6:
            raise RuntimeError("norm certificate did not close")
        kR += 1
    print("newton on the untwisted step", flush=True)
    newt = newton_enclose(L0, 1)
    doc = {
        "prec": ctx.prec,
        "dim": DIM,
        "K": K_MODES,
        "nmax": cert.N_MAX,
        "k0": cert.K0,
        "rho": "6/5",
        "n_letters": len(ns),
        "N_intervals": N,
        "delta": f"1/{2*N}",
        "Lambda2": str(L2),
        "Lambda2_hi": hi_f(L2),
        "remainder": str(rem),
        "remainder_hi": hi_f(rem),
        "eval_factor": str(factor),
        "prepass_max": mx,
        "R": f"{kR}/100",
        "R_num": kR,
        "R_den": 100,
        "attempts": passes,
        "newton_untwisted_step": newt,
        "seconds": round(time.time() - t0, 2),
        "weight_file": "logs/h7_uniform_weights.json",
    }
    return doc


def self_test() -> None:
    ctx.prec = 128
    # 2x2 diagonal
    M = np.diag([3.0 + 0j, 1.0 + 0j])
    ok = certify_op(M, arb(31) / 10)
    bad = certify_op(M, arb(29) / 10)
    print("diag", ok.get("ok"), bad.get("ok"), ok.get("slack_lo"), bad.get("reason"))
    if not ok["ok"] or bad["ok"]:
        raise SystemExit("2x2 certificate failed")
    # a non-normal 3x3 well under a loose cap
    A = np.array(
        [[1.0, 2.0, 0.0], [0.0, 0.5, 0.0], [0.0, 0.0, 0.25]],
        dtype=np.complex128,
    )
    cap = float(np.linalg.norm(A, 2)) + 0.05
    k = int(math.ceil(cap * 100))
    got = certify_op(A, arb(k) / 100)
    print("3x3", got.get("ok"), "numpy", float(np.linalg.norm(A, 2)), "R", k / 100)
    if not got["ok"]:
        raise SystemExit("3x3 certificate failed")
    mass = mass_check_small()
    print("mass rel", mass["rel_hi"], "kappa0", mass["kappa0_float"], mass["kappa0_exact"])
    for row in mass["cosine"]:
        print(" cosine", row["q"], "gap", row["gap_hi"])
    # one arb kappa against the float modulus, at a nonzero value
    z = kappa_acb(15, [7, 41], 3)
    if not (z.rad() < arb("1e-10")):
        raise SystemExit("kappa radius")
    print("self-test ok")


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    os.makedirs(LOG_DIR, exist_ok=True)
    if cmd == "self-test":
        self_test()
        return
    if cmd == "freeze":
        freeze_weights()
        return
    ctx.prec = 160
    cert.RHO = arb(6) / arb(5)
    if cmd == "kappa":
        # R is read from an existing cert log if present
        Rnum = Rden = None
        if os.path.exists(OUT):
            prev = json.load(open(OUT))
            if "norm" in prev and prev["norm"].get("R_num"):
                Rnum = prev["norm"]["R_num"]
                Rden = prev["norm"]["R_den"]
        doc = {"kappa": kappa_report(Rnum, Rden), "prec": ctx.prec}
        if os.path.exists(OUT):
            prev = json.load(open(OUT))
            prev["kappa"] = doc["kappa"]
            json.dump(prev, open(OUT, "w"), indent=1)
        else:
            json.dump(doc, open(OUT, "w"), indent=1)
        print(json.dumps({k: doc["kappa"].get(k) for k in (
            "sum_nonzero_lo", "sum_nonzero_hi", "T_lo", "T_hi",
            "excess_lo", "Rstar_lo", "Rstar_hi", "shrink_lo", "shrink_hi",
            "triangle_from_untwisted_lo", "rho_floor_lo",
        )}, indent=1)[:4000], flush=True)
        return
    if cmd == "cert":
        if not os.path.exists(WEIGHTS):
            freeze_weights()
        norm = certify()
        prev = json.load(open(OUT)) if os.path.exists(OUT) else {}
        prev["norm"] = norm
        json.dump(prev, open(OUT, "w"), indent=1)
        print("certified R", norm["R"], "seconds", norm["seconds"], flush=True)
        return
    if cmd == "all":
        self_test()
        if not os.path.exists(WEIGHTS):
            freeze_weights()
        norm = certify()
        kap = kappa_report(norm["R_num"], norm["R_den"])
        doc = {"prec": ctx.prec, "norm": norm, "kappa": kap, "mass_check": mass_check_small()}
        json.dump(doc, open(OUT, "w"), indent=1)
        print("certified R", norm["R"], "excess", kap.get("excess_lo"), flush=True)
        return
    raise SystemExit(cmd)


if __name__ == "__main__":
    main()
