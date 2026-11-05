"""H7* rates on the included K_p-divisors, in the single-disc sector model.

The model is the Line G / Line J one-parameter family used by
computations/verification/lineJ/J3/code/lyap.py:

    L_t = sum_{|n|<=10} ghat(n) e(n t) e(C n^2/2) MC_n
    on the monomial basis of H^2(D_rho), rho=2.6, K=40,
    ghat(n) = i^n J_n(1.8), C = -1/(lambda - lambda^{-1}).

A twisted orbit at conductor d and sector a in {0,2,4,6} is the product of
L_{a/8 + tau_i} along tau_i = Tr(beta lambda^i)/d. The per-step rate is the
spectral radius of that product, to the power 1/ord. Surviving sectors of the
pm rho sum are a in {0,4} (TRACE-221). Sectors 2 and 6 cancel in that sum.

Commands
    python3 h7_rates.py self-test
    python3 h7_rates.py survey
    python3 h7_rates.py certify --d 31 --sectors 0,4 --squares 4
    python3 h7_rates.py certify --d 217 --bx0 0 --bx1 55 --sectors 0,4 --squares 4
    python3 h7_rates.py enclose --d 457 --bx 1 --by 0 --sectors 0,4

Ball arithmetic is flint acb at the working precision. A Frobenius power is an
upper bound on the spectral radius. An isolated acb eigenvalue enclosure is a
two-sided bound. Numpy is used only to locate candidates and for the survey.
"""

from __future__ import annotations

if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")

import argparse
import json
import math
import os
import sys
import time

import numpy as np
from flint import acb, acb_mat, arb, ctx
from scipy.linalg import matrix_balance

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
sys.path.insert(0, os.path.join(ROOT, "computations", "verification", "lineI", "code"))
from law import C0, MC, kick_ghat  # noqa: E402

K_MODES = 40
RHO = 2.6
L_CUT = 10
T_PRIME = arb("1.42785")
T_PRIME_F = 1.42785
PREC = 128


def working_precision(period: int) -> int:
    """Bits lost are about 7 per multiplication. Leave a margin for the Newton step."""
    if period <= 16:
        return 128
    if period <= 24:
        return 160
    return 8 * period + 64

# Included K_p-divisors other than 7, from the trial factorisation in h7h8.json:
# p = 5: 31, 217. p = 7: 49, 4663. p = 19 and p = 29: the ten extras each.
# TARGETS is the list the recorded runs used. It omits d = 4663 at p = 7
# (referee audit, 2026-11-05: 4663 | K_7 = 228487, 4663^2 <= h_21, order 21);
# that conductor is listed in UNSEARCHED_INCLUDED and was not searched.
TARGETS = [
    (31, 5),
    (217, 5),
    (49, 7),
    (457, 19),
    (3199, 19),
    (14593, 19),
    (102151, 19),
    (6669001, 19),
    (7521721, 19),
    (46683007, 19),
    (52652047, 19),
    (3437426497, 19),
    (24061985479, 19),
    (13921, 29),
    (97447, 29),
    (5806729, 29),
    (40647103, 29),
    (28073057689, 29),
    (80835474409, 29),
    (196511403823, 29),
    (565848320863, 29),
    (390805036088569, 29),
    (2735635252619983, 29),
]

# Included K_p-divisors that no recorded run searched (eighteen open conductors =
# these plus the seventeen non-exhausted TARGETS at p = 19, 29).
UNSEARCHED_INCLUDED = [(4663, 7)]

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "..", "logs")


def nsw_u(n: int) -> int:
    a, b = 1, 7
    if n == 0:
        return 1
    for _ in range(1, n):
        a, b = b, 6 * b - a
    return b


def h_and_K(p: int) -> tuple[int, int]:
    h = nsw_u((p - 1) // 2)
    return h, 4 * h * h + 3


def lambda_powers(d: int, limit: int = 100000) -> list[tuple[int, int]]:
    """Powers lambda^0, lambda^1, ... up to but not including the first return to 1.
    Multiplication by lambda = 3+2*sqrt(2) on x+y*sqrt(2)."""
    x, y = 1, 0
    out = []
    for _ in range(limit):
        out.append((x, y))
        x, y = (3 * x + 4 * y) % d, (2 * x + 3 * y) % d
        if (x, y) == (1, 0):
            return out
    raise RuntimeError(f"order of lambda mod {d} exceeds {limit}")


def phase_index(a: int, tw: int, d: int) -> int:
    """(a/8 + tw/d) = (a*d + 8*tw)/(8*d)."""
    return (a * d + 8 * tw) % (8 * d)


def twists(d: int, bx: int, by: int, pw) -> list[int]:
    return [(2 * (bx * x + 2 * by * y)) % d for (x, y) in pw]


# ---------- numpy model (survey, candidate location) ----------

def numpy_letters():
    gh = kick_ghat("k1", 2.0, L_CUT)
    C = float(-C0)
    ns = np.array(sorted(n for n, g in gh.items() if abs(g) > 0))
    Ms = np.stack(
        [
            complex(gh[int(n)])
            * np.exp(2j * np.pi * C * int(n) * int(n) / 2)
            * MC(int(n), C, RHO, K_MODES)
            for n in ns
        ]
    )
    return ns, Ms


def numpy_family(ns, Ms, denom_phases: int):
    """L at every multiple of 1/denom_phases. Used only for small conductors."""
    out = []
    for p in range(denom_phases):
        w = np.exp(2j * np.pi * ns * (p / denom_phases))
        out.append(np.tensordot(w, Ms, axes=(0, 0)))
    return out


def numpy_L(ns, Ms, t: float):
    w = np.exp(2j * np.pi * ns * t)
    return np.tensordot(w, Ms, axes=(0, 0))


def scaled_product_rate(factors) -> float:
    """Per-step spectral radius of a product, rescaled so long orbits do not overflow."""
    K = factors[0].shape[0]
    Q = np.eye(K, dtype=complex)
    log_scale = 0.0
    for L in factors:
        Q = L @ Q
        nrm = np.linalg.norm(Q, ord="fro")
        if not np.isfinite(nrm) or nrm == 0.0:
            return float("inf")
        if nrm > 1e8 or nrm < 1e-8:
            Q /= nrm
            log_scale += math.log(nrm)
    ev = np.linalg.eigvals(Q)
    m = max(abs(z) for z in ev)
    if m == 0.0:
        return 0.0
    return math.exp((math.log(m) + log_scale) / len(factors))


def numpy_orbit_rate(ns, Ms, d, bx, by, a, pw, cache=None) -> float:
    factors = []
    for tw in twists(d, bx, by, pw):
        key = phase_index(a, tw, d)
        if cache is not None:
            factors.append(cache[key])
        else:
            t = ((a / 8.0) + tw / d) % 1.0
            factors.append(numpy_L(ns, Ms, t))
    return scaled_product_rate(factors)


def phase_energy(d, bx, by, pw) -> float:
    s = 0.0
    for tw in twists(d, bx, by, pw):
        dist = min(tw, d - tw) / d
        s += dist * dist
    return s


# ---------- arb model ----------

def hi_f(x: arb) -> float:
    """Python float guaranteed at least the upper end of a real ball.

    float() of the exact upper bound rounds to nearest, so step one ulp up.
    """
    return math.nextafter(float(x.abs_upper()), math.inf)


def lo_f(x: arb) -> float:
    """Python float guaranteed at most the lower end of a nonnegative ball.

    float() of the exact lower bound rounds to nearest, so step one ulp down
    (never below 0).
    """
    v = float(x.abs_lower())
    return max(0.0, math.nextafter(v, -math.inf)) if v > 0.0 else 0.0


def ub(x) -> arb:
    """Exact arb upper bound of |x| for an arb or acb ball."""
    return arb(x.abs_upper()) if isinstance(x, arb) else arb(abs(x).abs_upper())


def amax(xs) -> arb:
    """Rigorous upper bound of the maximum of a list of balls (union hull)."""
    out = None
    for x in xs:
        u = ub(x)
        out = u if out is None else out.union(u)
    return arb(out.abs_upper())


def ball_ends(x: arb) -> dict:
    return {"lo": lo_f(x), "hi": hi_f(x), "str": str(x)}


def eye_acb(K: int) -> acb_mat:
    data = [acb(0)] * (K * K)
    for i in range(K):
        data[i * K + i] = acb(1)
    return acb_mat(K, K, data)


def build_letters_arb():
    sqrt2 = arb(2).sqrt()
    lam = arb(3) + 2 * sqrt2
    C = -(1 / (lam - 1 / lam))
    rho = arb(str(RHO))
    facts = [arb.fac_ui(k) for k in range(K_MODES)]
    flog = [facts[k].log() for k in range(K_MODES)]
    lam_log = lam.log()
    rho_log = rho.log()
    ns = list(range(-L_CUT, L_CUT + 1))
    Gs = []
    for n in ns:
        G = mc_arb(n, C, rho, lam, K_MODES, flog, lam_log, rho_log)
        g = (acb(0, 1) ** n) * (acb(9) / acb(5)).bessel_j(acb(n))
        phase = acb(C * n * n).exp_pi_i()
        Gs.append(G * (g * phase))
    return ns, Gs, C, lam


def mc_arb(n, C, rho, lam, K, flog, lam_log, rho_log) -> acb_mat:
    if n == 0:
        data = [acb(0)] * (K * K)
        for k in range(K):
            data[k * K + k] = acb(lam ** (-k))
        return acb_mat(K, K, data)
    z = acb(0, 1) * (2 * acb.pi() * C * n * rho)
    zlog = z.log()
    sgn = 1 if n > 0 else -1
    absn_log = arb(abs(n)).log() - rho_log
    Mm = [acb(0)] * (K * K)
    Cm = [acb(0)] * (K * K)
    for j in range(K):
        fj = flog[j]
        for k in range(K):
            dlt = j - k
            if dlt >= 0:
                Mm[j * K + k] = (dlt * zlog - flog[dlt]).exp()
            e = k - j
            if e >= 0:
                logb = flog[k] - fj - flog[e]
                Cm[j * K + k] = (logb - k * lam_log + e * absn_log).exp() * (sgn ** e)
    return acb_mat(K, K, Mm) * acb_mat(K, K, Cm)


def family_arb(ns, Gs, d: int):
    """L at p/(8d) for p = 0 .. 8d-1."""
    denom = 8 * d
    out = []
    zero = None
    for p in range(denom):
        acc = None
        for n, G in zip(ns, Gs):
            # e(n * p / (8d)) = exp(2 pi i * n * p / (8d)) = exp_pi_i(n*p/(4d))
            w = (acb(n * p) / (4 * d)).exp_pi_i()
            term = G * w
            acc = term if acc is None else acc + term
        out.append(acc)
    return out


def product_arb(Ls, d, bx, by, a, pw) -> acb_mat:
    Q = eye_acb(K_MODES)
    for tw in twists(d, bx, by, pw):
        Q = Ls[phase_index(a, tw, d)] * Q
    return Q


_POW2 = {}


def pow2(exp: int) -> arb:
    """Exact power of two at the current precision. Multiplication by it is exact."""
    hit = _POW2.get((ctx.prec, exp))
    if hit is None:
        hit = arb(2) ** exp
        _POW2[(ctx.prec, exp)] = hit
    return hit


def frob_rate(Q: acb_mat, steps: int) -> arb:
    """Ball for ||Q||_F ** (1/steps). ||Q||_F^2 = Tr(Q* Q) for every matrix in the ball."""
    gram = Q.conjugate().transpose() * Q
    tr = gram.trace().real
    return tr.sqrt() ** (arb(1) / steps)


def midpoint_matrix(Q: acb_mat) -> np.ndarray:
    K = Q.nrows()
    M = np.zeros((K, K), dtype=complex)
    for i in range(K):
        for j in range(K):
            z = Q[i, j]
            M[i, j] = complex(float(z.real), float(z.imag))
    return M


def balance_pow2(Q: acb_mat) -> acb_mat:
    """Diagonal similarity by powers of two. Eigenvalues are unchanged.

    Scipy's balancing (permute=False) returns scales that are powers of two, and
    the balanced midpoint is M_ij * scale[j] / scale[i]. The same multipliers
    applied to the ball give a ball for D^{-1} A D.
    """
    M = midpoint_matrix(Q)
    balanced, (scale, _perm) = matrix_balance(M, permute=False, separate=True)
    ex = np.rint(np.log2(np.abs(scale))).astype(int)
    K = Q.nrows()
    # Convention check on one entry, against the scipy midpoint.
    i0, j0 = 0, min(1, K - 1)
    pred = M[i0, j0] * (scale[j0] / scale[i0])
    if abs(pred - balanced[i0, j0]) > 1e-6 * (1 + abs(balanced[i0, j0])):
        raise RuntimeError("power-of-two balancing convention does not match scipy")
    data = [
        Q[i, j] * pow2(int(ex[j] - ex[i]))
        for i in range(K)
        for j in range(K)
    ]
    return acb_mat(K, K, data)


def balanced_cap(Q: acb_mat, period: int, squares: int) -> dict:
    """Spectral-radius upper bound from Frobenius norms of the balanced matrix.

    rho <= ||B^{2^s}||_F ^{1/(2^s period)}. Balancing makes the norm close to rho.
    """
    B = balance_pow2(Q)
    m = 1
    rate = frob_rate(B, m * period)
    for _ in range(squares):
        B = B * B
        m *= 2
        rate = frob_rate(B, m * period)
    return {
        "cap_hi": hi_f(rate),
        "cap_lo": lo_f(rate),
        "power": m,
        "rate_str": str(rate),
    }


def newton_enclose(Q: acb_mat, period: int) -> dict | None:
    """Two-sided enclosure of one eigenvalue's per-step modulus.

    The matrix is balanced by an exact power-of-two similarity. A float eigenpair
    of the midpoint is the Newton centre. Newton-Kantorovich in the infinity norm,
    with Lipschitz constant 2 for the eigen-equation F(v, lambda) = (B - lambda)v
    normalised by v_p = 1, gives ||(v, lambda) - centre||_inf <= 2 eta whenever
    h = 2 * ||J^{-1}||_inf * eta <= 1/2.

    The Jacobian inverse is computed on the midpoint. Its norm beta0 is inflated
    by the Neumann factor 1/(1 - beta0*delta), where delta is the infinity-norm
    bound on the ball radius of B. The residual is computed on the ball, so eta
    covers the true matrix inside the product enclosure. Existence of an
    eigenvalue in that disc lower-bounds the spectral radius. It is an upper
    bound on the spectral radius only together with a norm cap.
    """
    B = balance_pow2(Q)
    M = midpoint_matrix(B)
    ev, vecs = np.linalg.eig(M)
    idx = int(np.argmax(np.abs(ev)))
    mu = complex(ev[idx])
    v = vecs[:, idx].copy()
    pivot = int(np.argmax(np.abs(v)))
    if v[pivot] == 0:
        return None
    v /= v[pivot]
    K = M.shape[0]
    # Float64 cannot resolve an eigenvalue of size 2^{50} to the absolute
    # accuracy Kantorovich needs. Divide by an exact power of two so the
    # unknown has magnitude in [1, 2). The per-step root multiplies back.
    mag = abs(mu)
    if mag == 0.0 or not math.isfinite(mag):
        return None
    exp2 = int(math.floor(math.log2(mag)))
    if exp2 != 0:
        scale = pow2(-exp2)
        B = acb_mat(K, K, [B[i, j] * scale for i in range(K) for j in range(K)])
        mu = mu / (2.0 ** exp2)
    free = [k for k in range(K) if k != pivot]
    vv = [acb(complex(v[k])) for k in range(K)]
    vv[pivot] = acb(1)
    mu_a = acb(mu)
    # Residual of the ball matrix. Its absolute upper bound covers the true
    # matrix inside the product ball, not only the midpoint.
    # Every error quantity below (row sums, delta, beta, eta, h, disc) is an arb
    # ball and is accumulated in ball arithmetic (referee audit 2026-11-05: the
    # earlier float64 round-to-nearest sums were not directed).
    residual = []
    row_rads = []
    for r in range(K):
        acc = acb(0)
        row_rad = arb(0)
        for c in range(K):
            entry = B[r, c]
            row_rad += ub(entry.rad())
            coeff = entry - (mu_a if r == c else 0)
            acc += coeff * vv[c]
        residual.append(acc)
        row_rads.append(row_rad)
    delta = amax(row_rads)
    # Point Jacobian at the midpoint. acb_mat.solve on a ball matrix encloses
    # rounding of one system; it does not enclose the solution set of the ball.
    # The inverse of the true Jacobian is recovered by a Neumann bound.
    jac = [acb(0)] * (K * K)
    for col, k in enumerate(free):
        for r in range(K):
            mid = B[r, k].mid()
            jac[r * K + col] = mid - (mu_a if r == k else 0)
    for r in range(K):
        jac[r * K + (K - 1)] = -vv[r]
    J = acb_mat(K, K, jac)
    try:
        eye = [acb(1 if r == c else 0) for r in range(K) for c in range(K)]
        inv = J.solve(acb_mat(K, K, eye))
    except (ValueError, ZeroDivisionError):
        return None
    rows = []
    for r in range(K):
        row = arb(0)
        for c in range(K):
            row += ub(inv[r, c])
        rows.append(row)
    beta0 = amax(rows)
    gap = ub(beta0 * delta)
    if not gap.is_finite() or not (gap < 1):
        return {"ok": False, "h": None, "beta": hi_f(beta0), "delta": hi_f(delta), "gap": hi_f(gap)}
    beta = ub(beta0 / (1 - gap))
    # ||F_true(y0)||_inf <= R, and ||J_true^{-1}||_inf <= beta, so eta = beta*R.
    Rres = amax(residual)
    eta = ub(beta * Rres)
    # h = K_lip * beta * eta with K_lip = 2.
    h_kan = ub(2 * beta * eta)
    if not h_kan.is_finite() or not (h_kan <= arb(1) / 2):
        return {
            "ok": False,
            "h": hi_f(h_kan),
            "beta": hi_f(beta),
            "eta": hi_f(eta),
            "mu_abs": abs(mu),
        }
    # rho_Newton <= 2 eta, so the eigenvalue lies within distance 2*eta of mu.
    disc = ub(2 * eta)
    mod = (mu_a.real ** 2 + mu_a.imag ** 2).sqrt()
    lo_mod = (mod - disc) * pow2(exp2)
    hi_mod = (mod + disc) * pow2(exp2)
    exponent = arb(1) / period
    lo_step = lo_mod ** exponent
    hi_step = hi_mod ** exponent
    return {
        "ok": True,
        "h": hi_f(h_kan),
        "beta": hi_f(beta),
        "beta0": hi_f(beta0),
        "delta": hi_f(delta),
        "scale_exp": exp2,
        "eta": hi_f(eta),
        "disc": hi_f(disc),
        "error_sums": "arb",
        "lo_str": str(lo_step),
        "hi_str": str(hi_step),
        "product_lo": lo_f(lo_mod),
        "product_hi": hi_f(hi_mod),
        "lo": lo_f(lo_step),
        "hi": hi_f(hi_step),
        "pivot": pivot,
    }


# ---------- commands ----------

def cmd_self_test() -> None:
    ctx.prec = PREC
    t0 = time.time()
    ns_a, Gs, C, lam = build_letters_arb()
    print(f"letters built in {time.time()-t0:.2f}s  C={C}", flush=True)
    ns_n, Ms = numpy_letters()
    assert list(ns_n) == ns_a
    # Compare one twisted matrix at t = 1/8 against numpy.
    L_arb = family_one(ns_a, Gs, 1, 8)  # p/(8d) with d=1, p=1 -> t=1/8
    L_np = numpy_L(ns_n, Ms, 0.125)
    diff = matrix_diff(L_arb, L_np)
    print(f"L(1/8) max entry diff {diff:.3e}", flush=True)
    # Entries reach size 10^4. The difference is float64 rounding in the numpy matrix.
    if diff > 1e-8:
        raise SystemExit("arb family does not match numpy")
    # Untwisted spectral radius, and the three level-7 classes.
    pw = lambda_powers(7)
    assert len(pw) == 3
    Ls = family_arb(ns_a, Gs, 7)
    classes = {
        (1, 3): {6: None, 2: None},
        (2, 1): {4: None, 0: None},
        (0, 1): {0: None},
    }
    for (bx, by), sectors in classes.items():
        for a in sectors:
            Q = product_arb(Ls, 7, bx, by, a, pw)
            step = newton_enclose(Q, 3)
            if step is None or not step.get("ok"):
                raise SystemExit(f"Newton failed on d=7 class {(bx, by)} sector {a}: {step}")
            sectors[a] = step
            print(
                f"d=7 beta={(bx, by)} a={a} rate in [{step['lo']:.12f}, {step['hi']:.12f}] "
                f"h={step['h']:.2e}",
                flush=True,
            )
    # TRACE-223 discs. The model value of class 1:3 sits just under the cap 1.2837144,
    # and the model value of class 2:1 sits inside the certified disc.
    r13 = classes[(1, 3)][6]
    if not (r13["lo"] > 1.2837142 and r13["hi"] < 1.2837144):
        raise SystemExit(f"level-7 class 1:3 enclosure {r13} missed the model value")
    r21 = classes[(2, 1)][4]
    if not (1.2835950326 < r21["lo"] and r21["hi"] < 1.2835952326):
        raise SystemExit(f"level-7 class 2:1 enclosure {r21} is outside the TRACE-223 disc")
    r01 = classes[(0, 1)][0]
    if not (r01["hi"] < 1.2624308 and r01["lo"] > 1.2624305):
        raise SystemExit(f"level-7 class 0:1 enclosure {r01} missed the model value")
    Q = product_arb(Ls, 7, 2, 1, 4, pw)
    cap = balanced_cap(Q, 3, squares=2)
    print(f"d=7 survivor balanced cap {cap}", flush=True)
    if cap["cap_hi"] >= T_PRIME_F:
        raise SystemExit("level-7 balanced cap did not fall under T'")
    if cap["cap_hi"] < r21["lo"]:
        raise SystemExit("balanced cap undercut the Newton lower bound")
    # Orders
    assert len(lambda_powers(31)) == 15
    assert len(lambda_powers(49)) == 21
    assert len(lambda_powers(217)) == 15
    # d = 4663 at p = 7 (referee audit 2026-11-05): included, order 21, not searched.
    h7, k7 = h_and_K(7)
    assert k7 == 228487 and k7 % 4663 == 0 and 4663 ** 2 <= h7 * k7 and nsw_u(10) == h7 * k7
    assert len(lambda_powers(4663)) == 21
    # Phase inheritance: tau(e beta') at conductor c*e equals tau(beta') at conductor c.
    def _phases(d, bx, by):
        return [(2 * (bx * x + 2 * by * y)) % d for (x, y) in lambda_powers(d)]

    def _same(seq_d, d, seq_c, c):
        return all(seq_d[i] * c == seq_c[i % len(seq_c)] * d for i in range(len(seq_d)))

    p7 = _phases(7, 1, 3)
    if not _same(_phases(49, 7, 21), 49, p7, 7):
        raise SystemExit("phase identity failed for 49 = 7*7")
    if not _same(_phases(217, 31, 93), 217, p7, 7):
        raise SystemExit("phase identity failed for 217 inherited from 7")
    if not _same(_phases(217, 7, 63), 217, _phases(31, 1, 9), 31):
        raise SystemExit("phase identity failed for 217 inherited from 31")
    print(f"self-test passed in {time.time()-t0:.1f}s", flush=True)


def family_one(ns, Gs, p, denom_8d):
    """Single phase p/denom, denom = 8d."""
    d = denom_8d // 8
    acc = None
    for n, G in zip(ns, Gs):
        w = (acb(n * p) / (4 * d)).exp_pi_i()
        term = G * w
        acc = term if acc is None else acc + term
    return acc


def matrix_diff(M: acb_mat, N: np.ndarray) -> float:
    K = N.shape[0]
    mx = 0.0
    for i in range(K):
        for j in range(K):
            z = M[i, j]
            c = complex(float(z.real), float(z.imag))
            mx = max(mx, abs(c - N[i, j]))
    return mx


def cmd_survey() -> None:
    os.makedirs(LOG_DIR, exist_ok=True)
    ns, Ms = numpy_letters()
    # mu* of the model
    L0 = numpy_L(ns, Ms, 0.0)
    mu_star = max(abs(z) for z in np.linalg.eigvals(L0))
    print(f"model mu* {mu_star}", flush=True)
    rows = []
    # Full scans for conductors that fit.
    for d, p in ((7, None), (31, 5), (49, 7), (217, 5)):
        rows.append(full_scan(ns, Ms, d, p))
    # Probes for the twenty large conductors.
    for d, p in TARGETS:
        if d in (31, 217, 49):
            continue
        rows.append(probe(ns, Ms, d, p))
    # Exact divisibility checks.
    checks = []
    for p in (5, 7, 19, 29):
        h, Kp = h_and_K(p)
        for d, pp in TARGETS:
            if pp != p:
                continue
            checks.append(
                {
                    "d": d,
                    "p": p,
                    "divides_K": (Kp % d) == 0,
                    "under_sqrt": d * d <= h * Kp,
                    "order": len(lambda_powers(d)),
                    "three_p": 3 * p,
                }
            )
            if Kp % d != 0 or d * d > h * Kp:
                raise SystemExit(f"inclusion check failed for d={d}")
    out = {"mu_star_model": mu_star, "Tprime": T_PRIME_F, "levels": rows, "checks": checks}
    path = os.path.join(LOG_DIR, "h7_rates_survey.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {path}", flush=True)


def full_scan(ns, Ms, d: int, p) -> dict:
    t0 = time.time()
    pw = lambda_powers(d)
    per = len(pw)
    Ls = numpy_family(ns, Ms, 8 * d)
    best = {a: {"rho": -1.0, "beta": None} for a in (0, 2, 4, 6)}
    # Frobenius power caps, surviving sectors only (the discharge bound).
    frob_best = {8: -1.0, 16: -1.0}
    frob_at = {8: None, 16: None}
    for bx in range(d):
        for by in range(d):
            if bx == 0 and by == 0:
                continue
            tws = twists(d, bx, by, pw)
            for a in (0, 2, 4, 6):
                Q = np.eye(K_MODES, dtype=complex)
                for tw in tws:
                    Q = Ls[phase_index(a, tw, d)] @ Q
                rho = float(max(abs(z) for z in np.linalg.eigvals(Q)) ** (1.0 / per))
                if rho > best[a]["rho"]:
                    best[a] = {"rho": rho, "beta": [bx, by]}
                if a in (0, 4):
                    Q2 = Q @ Q
                    Q4 = Q2 @ Q2
                    Q8 = Q4 @ Q4
                    Q16 = Q8 @ Q8
                    for m, Mm in ((8, Q8), (16, Q16)):
                        fr = float(np.linalg.norm(Mm, ord="fro") ** (1.0 / (m * per)))
                        if fr > frob_best[m]:
                            frob_best[m] = fr
                            frob_at[m] = [bx, by, a]
    surv = max(best[0]["rho"], best[4]["rho"])
    print(
        f"scan d={d} period={per} surv={surv:.6f} "
        f"all={max(best[a]['rho'] for a in best):.6f} "
        f"frob8={frob_best[8]:.6f} frob16={frob_best[16]:.6f} "
        f"sec={time.time()-t0:.1f}",
        flush=True,
    )
    return {
        "d": d,
        "p": p,
        "kind": "full_scan_float",
        "order": per,
        "by_sector": best,
        "surviving_max": surv,
        "frob_power_rate": frob_best,
        "frob_at": frob_at,
        "seconds": time.time() - t0,
    }


def probe(ns, Ms, d: int, p: int) -> dict:
    t0 = time.time()
    pw = lambda_powers(d)
    per = len(pw)
    betas = []
    for bx in range(-4, 5):
        for by in range(-4, 5):
            if bx == 0 and by == 0:
                continue
            betas.append((bx % d, by % d))
    rng = np.random.default_rng(20261104 + d % 100000)
    # Low phase-energy samples: the slow orbits.
    scored = []
    for _ in range(4000):
        bx = int(rng.integers(0, d))
        by = int(rng.integers(0, d))
        if bx == 0 and by == 0:
            continue
        scored.append((phase_energy(d, bx, by, pw), bx, by))
    scored.sort()
    for _, bx, by in scored[:25]:
        betas.append((bx, by))
    for _ in range(80):
        betas.append((int(rng.integers(0, d)), int(rng.integers(0, d))))
    # unique
    seen = set()
    uniq = []
    for b in betas:
        if b == (0, 0) or b in seen:
            continue
        seen.add(b)
        uniq.append(b)
    best = {"rho": -1.0, "beta": None, "a": None}
    best_slow = {"rho": -1.0, "beta": [1, 0], "a": None}
    for bx, by in uniq:
        for a in (0, 4):
            rho = numpy_orbit_rate(ns, Ms, d, bx, by, a, pw)
            if rho > best["rho"]:
                best = {"rho": rho, "beta": [bx, by], "a": a}
            if [bx, by] == [1 % d, 0]:
                if rho > best_slow["rho"]:
                    best_slow = {"rho": rho, "beta": [1, 0], "a": a}
    # K-stability of the winner, K=32 and K=48 would require rebuilding letters.
    # Record the K=40 value; a separate enclose call recomputes in arb.
    print(
        f"probe d={d} p={p} period={per} n={len(uniq)} "
        f"max={best['rho']:.6f} at {best['beta']} a={best['a']} "
        f"slow10={best_slow['rho']:.6f} sec={time.time()-t0:.1f}",
        flush=True,
    )
    return {
        "d": d,
        "p": p,
        "kind": "probe_float",
        "order": per,
        "n_beta": len(uniq),
        "sample_max": best,
        "beta_1_0": best_slow,
        "above_Tprime": best["rho"] > T_PRIME_F,
        "seconds": time.time() - t0,
    }


def cmd_certify(args) -> None:
    d = args.d
    sectors = [int(s) for s in args.sectors.split(",")]
    bx0 = 0 if args.bx0 is None else args.bx0
    bx1 = d if args.bx1 is None else args.bx1
    os.makedirs(LOG_DIR, exist_ok=True)
    t0 = time.time()
    pw = lambda_powers(d)
    per = len(pw)
    ctx.prec = working_precision(per)
    print(
        f"certify d={d} bx=[{bx0},{bx1}) sectors={sectors} prec={ctx.prec} period={per}",
        flush=True,
    )
    ns, Gs, C, lam = build_letters_arb()
    t1 = time.time()
    Ls = family_arb(ns, Gs, d)
    print(f"family {8*d} matrices in {time.time()-t1:.1f}s", flush=True)
    # Float family from the same phases, for locating the maximizer inside this slice.
    ns_n, Ms = numpy_letters()
    Lf = numpy_family(ns_n, Ms, 8 * d)
    cap_max = -1.0
    cap_at = None
    float_max = -1.0
    float_at = None
    n_beta = 0
    worst_power = 1
    for bx in range(bx0, bx1):
        for by in range(d):
            if bx == 0 and by == 0:
                continue
            n_beta += 1
            tws = twists(d, bx, by, pw)
            for a in sectors:
                # float rate
                Qf = np.eye(K_MODES, dtype=complex)
                for tw in tws:
                    Qf = Lf[phase_index(a, tw, d)] @ Qf
                rho = float(max(abs(z) for z in np.linalg.eigvals(Qf)) ** (1.0 / per))
                if rho > float_max:
                    float_max = rho
                    float_at = [bx, by, a, rho]
                Q = eye_acb(K_MODES)
                for tw in tws:
                    Q = Ls[phase_index(a, tw, d)] * Q
                cap = balanced_cap(Q, per, args.squares)
                if cap["cap_hi"] > cap_max:
                    cap_max = cap["cap_hi"]
                    cap_at = {"beta": [bx, by], "a": a, **cap}
                worst_power = max(worst_power, cap["power"])
            if n_beta % 200 == 0:
                print(
                    f"  d={d} bx={bx} n={n_beta} cap={cap_max:.6f} float={float_max:.6f} "
                    f"sec={time.time()-t0:.0f}",
                    flush=True,
                )
    # Two-sided enclosure of the float maximizer, if it lies in this slice.
    enclosure = None
    if float_at is not None:
        bx, by, a, _ = float_at
        Q = product_arb(Ls, d, bx, by, a, pw)
        step = newton_enclose(Q, per)
        tight = balanced_cap(Q, per, max(args.squares, 4))
        enclosure = {"beta": [bx, by], "a": a, "newton": step, "tight_cap": tight}
        print(f"enclose newton={step} cap={tight['cap_hi']}", flush=True)
    out = {
        "d": d,
        "bx0": bx0,
        "bx1": bx1,
        "sectors": sectors,
        "order": per,
        "n_beta": n_beta,
        "prec": ctx.prec,
        "target": args.target,
        "max_squares": args.squares,
        "cap_hi": cap_max,
        "cap_at": cap_at,
        "float_max": float_max,
        "float_at": float_at,
        "enclosure": enclosure,
        "below_Tprime": cap_max < T_PRIME_F,
        "seconds": time.time() - t0,
    }
    if args.out:
        path = args.out
    else:
        path = os.path.join(LOG_DIR, f"h7_rates_d{d}_{bx0}_{bx1}.json")
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {path} cap={cap_max:.6f} below={out['below_Tprime']} sec={out['seconds']:.1f}", flush=True)


def cmd_enclose(args) -> None:
    d = args.d
    sectors = [int(s) for s in args.sectors.split(",")]
    pw = lambda_powers(d)
    per = len(pw)
    ctx.prec = args.prec if args.prec else working_precision(per)
    ns, Gs, C, lam = build_letters_arb()
    # Build only the phases this orbit uses.
    rows = []
    for a in sectors:
        acc_factors = []
        Q = eye_acb(K_MODES)
        for tw in twists(d, args.bx, args.by, pw):
            p = phase_index(a, tw, d)
            acc = None
            for n, G in zip(ns, Gs):
                w = (acb(n * p) / (4 * d)).exp_pi_i()
                term = G * w
                acc = term if acc is None else acc + term
            Q = acc * Q
        step = newton_enclose(Q, per)
        cap = balanced_cap(Q, per, args.squares)
        row = {
            "d": d,
            "beta": [args.bx, args.by],
            "a": a,
            "order": per,
            "newton": step,
            "cap": cap,
            "above_Tprime": bool(step and step.get("ok") and step["lo"] > T_PRIME_F),
            "cap_below_Tprime": cap["cap_hi"] < T_PRIME_F,
        }
        rows.append(row)
        print(json.dumps(row), flush=True)
    path = args.out or os.path.join(
        LOG_DIR, f"h7_rates_orbit_d{d}_{args.bx}_{args.by}.json"
    )
    with open(path, "w") as f:
        json.dump({"rows": rows, "prec": ctx.prec}, f, indent=1)
    print(f"wrote {path}", flush=True)


def cmd_certify_probes() -> None:
    """Float search of short vectors at the twenty large conductors, then a ball enclosure of the winner."""
    os.makedirs(LOG_DIR, exist_ok=True)
    ns_n, Ms = numpy_letters()
    # One precision covers the longer period. Letters do not depend on the conductor.
    ctx.prec = working_precision(87)
    ns_a, Gs, _C, _lam = build_letters_arb()
    # Untwisted one-step spectral radius of the model.
    L0 = None
    acc = None
    for n, G in zip(ns_a, Gs):
        acc = G if acc is None else acc + G
    L0 = acc
    mu = newton_enclose(L0, 1)
    mu_cap = balanced_cap(L0, 1, 4)
    print(f"mu* newton={mu} cap={mu_cap['cap_hi']}", flush=True)
    rows = []
    for d, p in TARGETS:
        if d in (31, 49, 217):
            continue
        pw = lambda_powers(d)
        per = len(pw)
        seen = set()
        betas = []
        for bx in range(-8, 9):
            for by in range(-8, 9):
                b = (bx % d, by % d)
                if b == (0, 0) or b in seen:
                    continue
                seen.add(b)
                betas.append(b)
        best = {"rho": -1.0, "beta": None, "a": None}
        for bx, by in betas:
            for a in (0, 4):
                rho = numpy_orbit_rate(ns_n, Ms, d, bx, by, a, pw)
                if rho > best["rho"]:
                    best = {"rho": rho, "beta": [bx, by], "a": a}
        bx, by = best["beta"]
        a = best["a"]
        # Rebuild only the phases this orbit uses.
        Q = eye_acb(K_MODES)
        for tw in twists(d, bx, by, pw):
            key = phase_index(a, tw, d)
            acc = None
            for n, G in zip(ns_a, Gs):
                w = (acb(n * key) / (4 * d)).exp_pi_i()
                term = G * w
                acc = term if acc is None else acc + term
            Q = acc * Q
        step = newton_enclose(Q, per)
        cap = balanced_cap(Q, per, 4)
        row = {
            "d": d,
            "p": p,
            "order": per,
            "box": 8,
            "n_beta_float": len(betas),
            "float_max": best,
            "newton": step,
            "cap": cap,
            "cap_below_Tprime": cap["cap_hi"] < T_PRIME_F,
            "newton_above_Tprime": bool(step and step.get("ok") and step["lo"] > T_PRIME_F),
        }
        rows.append(row)
        print(
            f"d={d} float={best['rho']:.6f} at {best['beta']} a={best['a']} "
            f"newton_hi={None if not step or not step.get('ok') else step['hi']:.6f} "
            f"cap={cap['cap_hi']:.6f}",
            flush=True,
        )
    out = {"prec": ctx.prec, "mu_star": {"newton": mu, "cap": mu_cap}, "rows": rows}
    path = os.path.join(LOG_DIR, "h7_rates_probes.json")
    with open(path, "w") as f:
        json.dump(out, f, indent=1)
    print(f"wrote {path}", flush=True)


def cmd_wide() -> None:
    """Float search wider than the certificate box: |b|<=32, short rays, low phase energy.

    This does not certify a level. It locates the largest rate the search can find,
    so a later ball enclosure has the right orbit.
    """
    os.makedirs(LOG_DIR, exist_ok=True)
    ns, Ms = numpy_letters()
    rows = []
    for d, p in TARGETS:
        if d in (31, 49, 217):
            continue
        t0 = time.time()
        pw = lambda_powers(d)
        per = len(pw)
        best = {"rho": -1.0, "beta": None, "a": None, "where": None}
        seen = set()

        def consider(bx: int, by: int, where: str) -> None:
            b = (bx % d, by % d)
            if b == (0, 0) or b in seen:
                return
            seen.add(b)
            for a in (0, 4):
                rho = numpy_orbit_rate(ns, Ms, d, b[0], b[1], a, pw)
                if rho > best["rho"]:
                    best["rho"] = rho
                    best["beta"] = [b[0], b[1]]
                    best["a"] = a
                    best["where"] = where

        for bx in range(-32, 33):
            for by in range(-32, 33):
                consider(bx, by, "box32")
        for k in range(1, 97):
            for bx, by in (
                (k, 0),
                (0, k),
                (k, k),
                (k, -k),
                (k, 2 * k),
                (2 * k, k),
                (-k, k),
                (k, 3),
                (3, k),
                (4, k),
                (k, 4),
            ):
                consider(bx, by, "ray")
        rng = np.random.default_rng(20261104 + (d % 100000))
        scored = []
        for _ in range(20000):
            bx = int(rng.integers(0, d))
            by = int(rng.integers(0, d))
            if bx == 0 and by == 0:
                continue
            scored.append((phase_energy(d, bx, by, pw), bx, by))
        scored.sort()
        for _, bx, by in scored[:40]:
            consider(bx, by, "low_energy")
        row = {
            "d": d,
            "p": p,
            "order": per,
            "n_beta": len(seen),
            "float_max": best,
            "above_Tprime": best["rho"] > T_PRIME_F,
            "seconds": time.time() - t0,
        }
        rows.append(row)
        print(
            f"wide d={d} n={len(seen)} max={best['rho']:.6f} "
            f"at {best['beta']} a={best['a']} via {best['where']} "
            f"sec={row['seconds']:.1f}",
            flush=True,
        )
    path = os.path.join(LOG_DIR, "h7_rates_wide.json")
    with open(path, "w") as f:
        json.dump({"rows": rows, "Tprime": T_PRIME_F}, f, indent=1)
    print(f"wrote {path}", flush=True)


def cmd_rays() -> None:
    """One-dimensional search in short directions. Float only; ball-enclose the winners separately."""
    os.makedirs(LOG_DIR, exist_ok=True)
    ns, Ms = numpy_letters()
    # Conductors whose box search already sits near T', plus the certified witness.
    focus = [
        52652047,
        3437426497,
        24061985479,
        196511403823,
        390805036088569,
        2735635252619983,
    ]
    rows = []
    for d, p in TARGETS:
        if d not in focus:
            continue
        t0 = time.time()
        pw = lambda_powers(d)
        per = len(pw)
        best = {"rho": -1.0, "beta": None, "a": None, "shape": None}
        for k in range(-160, 161):
            if k == 0:
                continue
            shapes = {
                "k,0": (k, 0),
                "0,k": (0, k),
                "k,k": (k, k),
                "k,-k": (k, -k),
                "k,1": (k, 1),
                "k,-1": (k, -1),
                "k,3": (k, 3),
                "k,4": (k, 4),
                "1,k": (1, k),
                "3,k": (3, k),
            }
            for name, (bx, by) in shapes.items():
                b = (bx % d, by % d)
                if b == (0, 0):
                    continue
                for a in (0, 4):
                    rho = numpy_orbit_rate(ns, Ms, d, b[0], b[1], a, pw)
                    if rho > best["rho"]:
                        best = {
                            "rho": rho,
                            "beta": [b[0], b[1]],
                            "rep": [bx, by],
                            "a": a,
                            "shape": name,
                        }
        row = {
            "d": d,
            "p": p,
            "order": per,
            "float_max": best,
            "above_Tprime": best["rho"] > T_PRIME_F,
            "seconds": time.time() - t0,
        }
        rows.append(row)
        print(
            f"rays d={d} max={best['rho']:.8f} at {best['rep']} a={best['a']} "
            f"shape={best['shape']} above={row['above_Tprime']} sec={row['seconds']:.1f}",
            flush=True,
        )
    path = os.path.join(LOG_DIR, "h7_rates_rays.json")
    with open(path, "w") as f:
        json.dump({"rows": rows, "Tprime": T_PRIME_F}, f, indent=1)
    print(f"wrote {path}", flush=True)


def cmd_rays_ext() -> None:
    """Longer rays on every large conductor, in the shapes that won the short search."""
    os.makedirs(LOG_DIR, exist_ok=True)
    ns, Ms = numpy_letters()
    rows = []
    for d, p in TARGETS:
        if d in (31, 49, 217):
            continue
        t0 = time.time()
        pw = lambda_powers(d)
        best = {"rho": -1.0, "beta": None, "a": None, "shape": None, "rep": None}
        for k in range(-240, 241):
            if k == 0:
                continue
            shapes = (
                ("k,0", k, 0),
                ("0,k", 0, k),
                ("k,k", k, k),
                ("k,-k", k, -k),
                ("2k,k", 2 * k, k),
                ("k,2k", k, 2 * k),
            )
            for name, bx, by in shapes:
                b = (bx % d, by % d)
                if b == (0, 0):
                    continue
                for a in (0, 4):
                    rho = numpy_orbit_rate(ns, Ms, d, b[0], b[1], a, pw)
                    if rho > best["rho"]:
                        best = {
                            "rho": rho,
                            "beta": [b[0], b[1]],
                            "rep": [bx, by],
                            "a": a,
                            "shape": name,
                        }
        row = {
            "d": d,
            "p": p,
            "order": len(pw),
            "float_max": best,
            "above_Tprime": best["rho"] > T_PRIME_F,
            "seconds": time.time() - t0,
        }
        rows.append(row)
        print(
            f"ext d={d} max={best['rho']:.8f} rep={best['rep']} a={best['a']} "
            f"shape={best['shape']} above={row['above_Tprime']} sec={row['seconds']:.1f}",
            flush=True,
        )
    path = os.path.join(LOG_DIR, "h7_rates_rays_ext.json")
    with open(path, "w") as f:
        json.dump({"kmax": 240, "rows": rows, "Tprime": T_PRIME_F}, f, indent=1)
    print(f"wrote {path}", flush=True)


def cmd_rays_deep() -> None:
    """Longer rays on the conductors whose |k|<=240 search stayed under T' but above 1.2."""
    os.makedirs(LOG_DIR, exist_ok=True)
    ns, Ms = numpy_letters()
    focus = {
        6669001,
        7521721,
        46683007,
        52652047,
        28073057689,
        80835474409,
        196511403823,
        565848320863,
        390805036088569,
    }
    rows = []
    for d, p in TARGETS:
        if d not in focus:
            continue
        t0 = time.time()
        pw = lambda_powers(d)
        best = {"rho": -1.0, "beta": None, "a": None, "shape": None, "rep": None}
        for k in range(-500, 501):
            if k == 0:
                continue
            shapes = (
                ("k,0", k, 0),
                ("0,k", 0, k),
                ("k,k", k, k),
                ("k,-k", k, -k),
                ("2k,k", 2 * k, k),
                ("k,2k", k, 2 * k),
                ("3k,k", 3 * k, k),
            )
            for name, bx, by in shapes:
                b = (bx % d, by % d)
                if b == (0, 0):
                    continue
                for a in (0, 4):
                    rho = numpy_orbit_rate(ns, Ms, d, b[0], b[1], a, pw)
                    if rho > best["rho"]:
                        best = {
                            "rho": rho,
                            "beta": [int(b[0]), int(b[1])],
                            "rep": [int(bx), int(by)],
                            "a": int(a),
                            "shape": name,
                        }
        row = {
            "d": d,
            "p": p,
            "order": len(pw),
            "float_max": best,
            "above_Tprime": bool(best["rho"] > T_PRIME_F),
            "seconds": time.time() - t0,
        }
        rows.append(row)
        print(
            f"deep d={d} max={best['rho']:.8f} rep={best['rep']} a={best['a']} "
            f"shape={best['shape']} above={row['above_Tprime']} sec={row['seconds']:.1f}",
            flush=True,
        )
    path = os.path.join(LOG_DIR, "h7_rates_rays_deep.json")
    with open(path, "w") as f:
        json.dump({"kmax": 500, "rows": rows, "Tprime": T_PRIME_F}, f, indent=1)
    print(f"wrote {path}", flush=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("self-test")
    sub.add_parser("survey")
    sub.add_parser("certify-probes")
    sub.add_parser("wide")
    sub.add_parser("rays")
    sub.add_parser("rays-ext")
    sub.add_parser("rays-deep")
    c = sub.add_parser("certify")
    c.add_argument("--d", type=int, required=True)
    c.add_argument("--bx0", type=int, default=None)
    c.add_argument("--bx1", type=int, default=None)
    c.add_argument("--sectors", default="0,4")
    c.add_argument("--squares", type=int, default=2)
    c.add_argument("--target", type=float, default=1.40)
    c.add_argument("--out", default=None)
    e = sub.add_parser("enclose")
    e.add_argument("--d", type=int, required=True)
    e.add_argument("--bx", type=int, required=True)
    e.add_argument("--by", type=int, required=True)
    e.add_argument("--sectors", default="0,4")
    e.add_argument("--squares", type=int, default=4)
    e.add_argument("--target", type=float, default=1.40)
    e.add_argument("--prec", type=int, default=None)
    e.add_argument("--out", default=None)
    args = ap.parse_args()
    if args.cmd == "self-test":
        cmd_self_test()
    elif args.cmd == "survey":
        cmd_survey()
    elif args.cmd == "certify-probes":
        cmd_certify_probes()
    elif args.cmd == "wide":
        cmd_wide()
    elif args.cmd == "rays":
        cmd_rays()
    elif args.cmd == "rays-ext":
        cmd_rays_ext()
    elif args.cmd == "rays-deep":
        cmd_rays_deep()
    elif args.cmd == "certify":
        cmd_certify(args)
    elif args.cmd == "enclose":
        cmd_enclose(args)


if __name__ == "__main__":
    main()
