"""Ball enclosure of the TRACE-223 multi-disc finite section, plus tail majorants.

The one-step matrix is the compression of the vertex transfer operator onto the
discs |c| <= k0 and the monomials u^k, k < K, with letters |n| <= nmax.
Composition, multiplication by exp(z u), and the weight ghat(n) e(C n^2/2)
are the same formulae as certG_build_sector.py. The 3-cycle is not tensored
into the state: the per-step rate is the spectral radius of the period product.

Commands
    python3 h7_multidisc_cert.py check
    python3 h7_multidisc_cert.py enclose
    python3 h7_multidisc_cert.py tail
"""

from __future__ import annotations

if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")

import json
import math
import os
import sys
import time

import numpy as np
from flint import acb, acb_mat, arb, ctx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h7_rates import hi_f, lo_f, newton_enclose  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "..", "logs")
# Truncation. |c| <= 3 and |n| <= 16 is forward-invariant: 19/lambda < 3.5.
K0 = 3
K_MODES = 40
N_MAX = 16
# Set in main(), after ctx.prec. An arb built at import time keeps the
# default precision and poisons every later product.
RHO = None


def lam_c():
    lam = arb(3) + 2 * arb(2).sqrt()
    C = -(1 / (lam - 1 / lam))
    return lam, C


def j_bound(n: int) -> arb:
    """|J_n(1.8)| <= (0.9)^n / n!."""
    if n < 0:
        n = -n
    t = arb("9") / arb(10)
    term = t ** n
    for i in range(1, n + 1):
        term /= i
    return term


def letter_tail(N: int) -> arb:
    """sum_{|n| > N} |J_n(1.8)| exp(alpha |n|) / (1-theta), alpha = pi rho /(2 sqrt2)."""
    lam, _C = lam_c()
    theta = 1 / (2 * RHO) + 1 / lam
    alpha = arb.pi() * RHO / (2 * arb(2).sqrt())
    t = (arb(9) / arb(10)) * alpha.exp()
    term = t ** (N + 1)
    for i in range(1, N + 2):
        term /= i
    q = t / (N + 2)
    if not (q < 1):
        raise RuntimeError("Bessel tail ratio")
    return 2 * term / (1 - q) / (1 - theta)


def _fact_tail(z: arb, m: int) -> arb:
    if m <= 0:
        return z.exp()
    term = z ** m
    for i in range(1, m + 1):
        term /= i
    s = term
    for k in range(m, m + 40):
        term *= z / (k + 1)
        s += term
    return s


def mode_pieces(K: int, N: int) -> tuple[arb, arb]:
    """One source disc, letters |n| <= N.

    exit: low modes to high modes. A low input mode k < K produces output modes
    >= K only through the tail of exp(z u), at most theta^k * sum_{m >= K-k} |z|^m/m!.
    back: high modes into the whole space. Mode k >= K has H^2 mass <= theta^k,
    and ||exp(z u)|| <= exp(|z|), so the block is at most exp(|z|) theta^K/(1-theta).
    """
    lam, _C = lam_c()
    theta = 1 / (2 * RHO) + 1 / lam
    alpha = arb.pi() * RHO / (2 * arb(2).sqrt())
    exit_b = arb(0)
    back = arb(0)
    for n in range(0, N + 1):
        z = alpha * n
        w = arb(1) if n == 0 else j_bound(n)
        mult = 1 if n == 0 else 2
        s_exit = arb(0)
        for k in range(K):
            s_exit += theta ** k * _fact_tail(z, K - k)
        exit_b += s_exit * w * mult
        back += z.exp() * theta ** K / (1 - theta) * w * mult
    return exit_b, back


def tail_report() -> dict:
    lam, C = lam_c()
    theta = 1 / (2 * RHO) + 1 / lam
    # Core invariance for every kept letter.
    exits = []
    for c in range(-K0, K0 + 1):
        for n in range(-N_MAX, N_MAX + 1):
            val = arb(c + n) / lam
            j = int(round(float(val)))
            gap = arb("1") / 2 - abs(val - j)
            if not (gap > arb("1e-6")) or abs(j) > K0:
                exits.append((c, n, float(val)))
    # Column overlap: at most n_src sources, so ||L|| <= sqrt(n_src) * max block.
    n_src = 2 * K0 + 1
    stack = arb(n_src).sqrt()
    exit_b, back = mode_pieces(K_MODES, N_MAX)
    far = letter_tail(N_MAX)
    # At most one block per source column, and at most n_src sources share a target,
    # so the operator norm is at most sqrt(n_src) times the one-disc bound.
    eps_exit = exit_b * stack
    eps_back = back * stack
    eps_letter = far * stack
    return {
        "k0": K0,
        "K": K_MODES,
        "nmax": N_MAX,
        "rho": "1.2",
        "theta": str(theta),
        "theta_hi": hi_f(theta),
        "C": str(C),
        "exits": exits,
        "n_src": n_src,
        "exit_hi": hi_f(eps_exit),
        "back_hi": hi_f(eps_back),
        "letter_hi": hi_f(eps_letter),
        "eps_hi": hi_f(eps_exit + eps_back + eps_letter),
        "exit_str": str(eps_exit),
        "back_str": str(eps_back),
        "letter_str": str(eps_letter),
    }


def inclusion_report() -> dict:
    """d | K_p, d^2 <= h_p K_p, and the TRACE-199 test |Z|^2 >= 4 m h_m."""
    def nsw_h(p: int) -> int:
        # h_p = u_{(p-1)/2}, u_0=1, u_1=7, u_{n+1}=6 u_n - u_{n-1}
        n = (p - 1) // 2
        u0, u1 = 1, 7
        if n == 0:
            return u0
        for _ in range(1, n):
            u0, u1 = u1, 6 * u1 - u0
        return u1

    rows = []
    specs = [
        (19, 3437426497, -208, 0),
        (19, 24061985479, 227, 227),
        (29, 2735635252619983, -89, 0),
    ]
    lam, _C = lam_c()
    mu = arb("1.9154712")
    sub = arb("3012.4")
    for p, d, bx, by in specs:
        h = nsw_h(p)
        K = 4 * h * h + 3
        h_m = h * K
        m = 3 * p
        # |Z| >= 1/2 (1-lambda^{-m}) (mu^m - 3012.4), TRACE-273's constant.
        zlo = (arb(1) / 2) * (1 - lam ** (-m)) * (mu ** m - sub)
        four = arb(4) * m * h_m
        rows.append(
            {
                "p": p,
                "m": m,
                "d": d,
                "beta": [bx, by],
                "h_p": str(h),
                "K_p": str(K),
                "h_m": str(h_m),
                "K_mod_d": K % d,
                "h_mod_d": h % d,
                "d_sq_le_hm": d * d <= h_m,
                "hm_over_d_sq": str(h_m // (d * d)),
                "gcd_beta": int(math.gcd(math.gcd(bx, by), d)),
                "zlo_sq": str(zlo ** 2),
                "four_m_hm": str(four),
                "z_test": bool(zlo ** 2 > four),
            }
        )
    return {"rows": rows}


def build_blocks():
    """Exact blocks. Returns dict (n, c) -> (j, acb_mat) for branches that land in the core."""
    lam, C = lam_c()
    centers = list(range(-K0, K0 + 1))
    index = {c: i for i, c in enumerate(centers)}
    facts = [arb.fac_ui(k) for k in range(K_MODES)]
    blocks = {}
    n_out = 0
    for n in range(-N_MAX, N_MAX + 1):
        z = acb(0, 1) * (2 * acb.pi() * C * n * RHO)
        # multiplication by exp(z u): lower triangular, 1's on the diagonal
        mult = [acb(0)] * (K_MODES * K_MODES)
        for j in range(K_MODES):
            mult[j * K_MODES + j] = acb(1)
        zp = acb(1)
        for m in range(1, K_MODES):
            zp *= z / m
            for jj in range(K_MODES - m):
                mult[(jj + m) * K_MODES + jj] = zp
        Mmult = acb_mat(K_MODES, K_MODES, mult)
        g = (acb(0, 1) ** n) * (acb(9) / acb(5)).bessel_j(acb(n))
        quad = acb(C * n * n).exp_pi_i()
        weight = g * quad
        for c in centers:
            val = arb(c + n) / lam
            j = int(round(float(val)))
            gap = arb(1) / 2 - abs(val - j)
            if not (gap > arb("1e-8")):
                raise RuntimeError(f"uncertified rounding c={c} n={n}")
            if j not in index:
                n_out += 1
                continue
            dl = val - j
            B = dl / RHO
            comp = [acb(0)] * (K_MODES * K_MODES)
            # c+n = 0 gives image 0 and B = 0 exactly; composition is diagonal.
            if c + n == 0:
                for k in range(K_MODES):
                    comp[k * K_MODES + k] = acb(lam ** (-k))
            else:
                # comp[jj, k] = C(k,jj) lam^{-jj} B^{k-jj}
                for k in range(K_MODES):
                    term = acb(B ** k) if k else acb(1)
                    # B**0 = 1 even if B is a ball around 0; use arb power carefully
                    if k == 0:
                        term = acb(1)
                    else:
                        term = acb(B ** k)
                    comp[0 * K_MODES + k] = term
                    for jj in range(1, k + 1):
                        term *= arb(k - jj + 1) / jj / lam / B
                        comp[jj * K_MODES + k] = term
            block = (Mmult * acb_mat(K_MODES, K_MODES, comp)) * (weight * acb(2 * C * n * c).exp_pi_i())
            blocks[(n, c)] = (j, block)
    return centers, index, blocks, n_out


def assemble(centers, index, blocks, d: int, tw: int, a: int) -> acb_mat:
    dim = len(centers) * K_MODES
    data = [acb(0)] * (dim * dim)
    for (n, c), (j, block) in blocks.items():
        phase = (acb(2 * n * tw) / d).exp_pi_i() * (acb(n * a) / 4).exp_pi_i()
        r0 = index[c] * K_MODES
        q0 = index[j] * K_MODES
        for r in range(K_MODES):
            for q in range(K_MODES):
                data[(r0 + r) * dim + (q0 + q)] += block[r, q] * phase
    return acb_mat(dim, dim, data)


def lambda_orbit(d: int):
    x, y = 1, 0
    out = []
    for _ in range(d + 2):
        out.append((x % d, y % d))
        x, y = (3 * x + 4 * y) % d, (2 * x + 3 * y) % d
        if (x % d, y % d) == (1, 0):
            return out
    raise RuntimeError("no return")


def twists(d, bx, by, pw):
    return [(2 * (bx * x + 2 * by * y)) % d for (x, y) in pw]


def scale_down(Q: acb_mat):
    """Divide by an exact power of two so sampled midpoints stay below 4.

    Eigenvalues and Frobenius norms are restored by the caller. Shrinking the
    entries keeps ball radii from overflowing a long product.
    """
    n = Q.nrows()
    mx = 0.0
    for i in range(n):
        for j in range(n):
            z = Q[i, j]
            mx = max(mx, abs(complex(float(z.real), float(z.imag))))
    if not math.isfinite(mx) or mx < 4.0:
        return Q, 0
    e = int(math.floor(math.log2(mx))) - 1
    if e <= 0:
        return Q, 0
    s = arb(2) ** (-e)
    data = [Q[i, j] * s for i in range(n) for j in range(n)]
    return acb_mat(n, n, data), e


def eye(dim: int) -> acb_mat:
    data = [acb(0)] * (dim * dim)
    for i in range(dim):
        data[i * dim + i] = acb(1)
    return acb_mat(dim, dim, data)


def enclose_one(centers, index, blocks, name, d, bx, by, a, _tail) -> dict:
    pw = lambda_orbit(d)
    tws = twists(d, bx, by, pw)
    period = len(pw)
    dim = len(centers) * K_MODES
    print(f"enclose {name} dim={dim} period={period}", flush=True)
    t0 = time.time()
    Q = eye(dim)
    exp_r = 0
    # No Gram matrix in this loop. Forming Q* Q squares the radii and, at a
    # long period, makes the Frobenius ball indeterminate while Q itself is fine.
    for step, tw in enumerate(tws, start=1):
        Q = assemble(centers, index, blocks, d, tw, a) * Q
        Q, e = scale_down(Q)
        exp_r += e
        if step % 10 == 0 or step == period:
            rad = float(Q[0, 0].rad().abs_upper())
            print(
                f"  step {step}/{period} exp {exp_r} rad00 {rad:.3e} bits {Q[0, 0].rel_accuracy_bits()} t {time.time()-t0:.1f}",
                flush=True,
            )
    newt = newton_enclose(Q, period)
    if newt and newt.get("ok") and exp_r:
        # Q was divided by 2^{exp_r}. The per-step root gains 2^{exp_r/period}.
        gain = arb(2) ** (arb(exp_r) / period)
        newt = dict(newt)
        newt["scale_exp_product"] = exp_r
        newt["lo"] = lo_f(arb(newt["lo"]) * gain)
        newt["hi"] = hi_f(arb(newt["hi"]) * gain)
        if newt.get("product_lo"):
            newt["product_lo"] = lo_f(arb(newt["product_lo"]) * arb(2) ** exp_r)
            newt["product_hi"] = hi_f(arb(newt["product_hi"]) * arb(2) ** exp_r)
    print("  newton", {k: newt.get(k) for k in ("ok", "lo", "hi", "h", "delta", "gap")}, flush=True)
    return {
        "name": name,
        "d": d,
        "beta": [bx, by],
        "sector": a,
        "period": period,
        "dim": dim,
        "k0": K0,
        "K": K_MODES,
        "nmax": N_MAX,
        "seconds": round(time.time() - t0, 2),
        "newton": newt,
        "scale_exp": exp_r,
    }


def check_block() -> None:
    """One block against the numpy builder, and the level-7 one-step radius."""
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "md", os.path.join(HERE, "h7_multidisc.py")
    )
    md = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(md)
    ns, mats, meta = md.build_letters(K0, 1.2, K_MODES, N_MAX)
    centers, index, blocks, n_out = build_blocks()
    # n=1, c=0
    j, block = blocks[(1, 0)]
    r0 = index[0] * K_MODES
    q0 = index[j] * K_MODES
    M = mats[list(ns).index(1)]
    err = 0.0
    for r in range(K_MODES):
        for q in range(K_MODES):
            z = block[r, q]
            mid = complex(float(z.real), float(z.imag))
            err = max(err, abs(mid - M[r0 + r, q0 + q]))
    print({"block_err": err, "n_out": n_out, "j": j, "dim": meta["dim"]}, flush=True)
    if err > 1e-9:
        raise SystemExit("block mismatch")


ORBITS = [
    ("level7_2_1", 7, 2, 1, 4),
    ("level7_1_3", 7, 1, 3, 6),
    ("d3437426497", 3437426497, -208, 0, 0),
    ("d24061985479", 24061985479, 227, 227, 0),
    ("d2735635252619983", 2735635252619983, -89, 0, 0),
]


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "enclose"
    os.makedirs(LOG_DIR, exist_ok=True)
    # Period 87 wants about 8*87 bits of product growth plus the working residual.
    global RHO
    ctx.prec = 320
    RHO = arb(6) / arb(5)
    if cmd == "tail":
        rep = {"tail": tail_report(), "inclusion": inclusion_report()}
        print(json.dumps(rep, indent=1)[:4000], flush=True)
        json.dump(rep, open(os.path.join(LOG_DIR, "h7_multidisc_tail.json"), "w"), indent=1)
        return
    if cmd == "check":
        check_block()
        return
    if cmd != "enclose":
        raise SystemExit(cmd)
    tail = tail_report()
    incl = inclusion_report()
    print("tail eps", tail["eps_hi"], "exits", tail["exits"], flush=True)
    print("inclusion", [(r["p"], r["d"], r["K_mod_d"], r["d_sq_le_hm"], r["z_test"]) for r in incl["rows"]], flush=True)
    check_block()
    centers, index, blocks, n_out = build_blocks()
    rows = []
    only = sys.argv[2] if len(sys.argv) > 2 else None
    for spec in ORBITS:
        if only and spec[0] != only:
            continue
        rows.append(enclose_one(centers, index, blocks, *spec, tail))
        json.dump(
            {"tail": tail, "inclusion": incl, "n_out": n_out, "orbits": rows, "prec": ctx.prec},
            open(os.path.join(LOG_DIR, "h7_multidisc_enclose.json"), "w"),
            indent=1,
            default=str,
        )
    print("wrote enclose json", flush=True)


if __name__ == "__main__":
    main()
