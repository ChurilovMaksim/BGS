"""Averaged section operator: identities, readout norm, and the threshold comparison.

The aggregate sum_beta kappa_d(N beta) Tr Q_beta is the trace of one operator
on the section tensored with O/dO. Its norm equals the uniform step norm of
h7_uniform.py, so the norm majorant is a product of local readout norms.
This script encloses that majorant and checks the Gauss-transform identity
on a small prime. It does not enumerate the composite level.

Commands
    python3 h7_average.py check
    python3 h7_average.py majorant
    python3 h7_average.py orbit
    python3 h7_average.py all
"""

from __future__ import annotations

import json
import os
import sys

import numpy as np
from flint import arb, ctx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from h7_rates import hi_f, lo_f

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "..", "logs")
OUT = os.path.join(LOG_DIR, "h7_average.json")

Q1 = 457
Q2 = 7521721
DIM = 280
P = 57
R_NUM, R_DEN = 246, 100
# Untwisted sector-0 trace, period 57, from logs/h7_lin_traces.json.
# The majorant script re-reads the enclosure rather than this decimal.
def kappa_prime(q: int, tb: int, v: int) -> complex:
    v %= q
    if v == 0:
        return complex(q - 2)
    m = (pow(tb, -1, q) * v) % q
    return -1 - np.exp(2j * np.pi * m / q)


def gamma_closed(q: int, tb: int, N: int) -> complex:
    """Dual weight proved in proofs/h7_average.md. N is an integer residue."""
    N %= q
    if N == 0:
        return complex(q * (q - 2))
    ang = (-tb * N) % q
    return complex(q) * (-1 - np.exp(2j * np.pi * ang / q))


def gamma_direct(q: int, tb: int, xx: int, yy: int) -> complex:
    s = 0j
    for bx in range(q):
        for by in range(q):
            Nv = (bx * bx - 2 * by * by) % q
            tr = (2 * (bx * xx + 2 * by * yy)) % q
            s += kappa_prime(q, tb, Nv) * np.exp(2j * np.pi * tr / q)
    return s


def check_gamma(q: int = 17, tb: int = 3) -> dict:
    """Every norm class at q, direct sum versus the closed form."""
    worst = 0.0
    seen = set()
    for xx in range(q):
        for yy in range(q):
            N = (xx * xx - 2 * yy * yy) % q
            if N in seen:
                continue
            seen.add(N)
            got = gamma_direct(q, tb, xx, yy)
            pred = gamma_closed(q, tb, N)
            worst = max(worst, abs(got - pred))
    if worst > 1e-9:
        raise RuntimeError(("gamma", q, worst))
    return {"q": q, "tb": tb, "n_norms": len(seen), "max_abs_gap": worst}


def lambda_pows(mod: int):
    x, y = 1, 0
    out = []
    while True:
        out.append((x % mod, y % mod))
        x, y = (3 * x + 4 * y) % mod, (2 * x + 3 * y) % mod
        if (x, y) == (1, 0):
            return out


def scalar_sum(mod: int, facs: list[int], tbs: list[int], coeffs: dict[int, complex]):
    ns = sorted(coeffs)
    c = np.array([coeffs[n] for n in ns], dtype=np.complex128)
    pw = lambda_pows(mod)
    S = 0j
    for bx in range(mod):
        for by in range(mod):
            kap = 1 + 0j
            Nfull = (bx * bx - 2 * by * by) % mod
            for qq, tb in zip(facs, tbs):
                cof = mod // qq
                v = (Nfull * pow(cof, -1, qq)) % qq
                tc = (tb * cof) % qq
                kap *= kappa_prime(qq, tc, v)
            prod = 1 + 0j
            for x, y in pw:
                tau = (2 * (bx * x + 2 * by * y)) % mod
                ph = np.exp(2j * np.pi * np.array(ns) * tau / mod)
                prod *= ph @ c
            S += kap * prod
    return S, len(pw)


def check_words(q: int = 17, tb: int = 3) -> dict:
    """Character-sum pairing against the closed form, full period, three letters.

    The word position is xi = sum_j n_j lambda^j, and the product is taken
    with the first letter on the right. Equality here is the scalar case of
    the identity in proofs/h7_average.md section 4. It is not an enclosure.
    """
    coeffs = {-1: 0.3 + 0.1j, 0: 1.0 + 0.0j, 1: -0.2 + 0.05j}
    ns = sorted(coeffs)
    pw = lambda_pows(q)
    P = len(pw)
    # Direct sum over beta.
    direct = 0j
    for bx in range(q):
        for by in range(q):
            kap = kappa_prime(q, tb, (bx * bx - 2 * by * by) % q)
            prod = 1 + 0j
            for x, y in pw:
                tau = (2 * (bx * x + 2 * by * y)) % q
                ph = np.exp(2j * np.pi * np.array(ns) * tau / q)
                prod *= ph @ np.array([coeffs[n] for n in ns])
            direct += kap * prod
    # Word sum. 3^P is 6561 at P=8.
    acc = 0j

    def rec(j, mx, my, prod):
        nonlocal acc
        if j == P:
            N = (mx * mx - 2 * my * my) % q
            acc += gamma_closed(q, tb, N) * prod
            return
        x, y = pw[j]
        for n in ns:
            nx = (mx + n * x) % q
            ny = (my + n * y) % q
            rec(j + 1, nx, ny, prod * coeffs[n])

    rec(0, 0, 0, 1 + 0j)
    gap = abs(acc - direct)
    if gap > 1e-8:
        raise RuntimeError(("word pairing", gap, acc, direct))
    return {
        "q": q,
        "tb": tb,
        "P": P,
        "direct": [float(direct.real), float(direct.imag)],
        "word": [float(acc.real), float(acc.imag)],
        "abs_gap": float(gap),
    }


def check_factor() -> dict:
    """S(q1 q2) is not the product of the local sums. Scalar letters, exact enough to see it."""
    coeffs = {-1: 0.3 + 0.1j, 0: 1.0 + 0.0j, 1: -0.2 + 0.05j}
    s17, p17 = scalar_sum(17, [17], [3], coeffs)
    s41, p41 = scalar_sum(41, [41], [5], coeffs)
    s, p = scalar_sum(17 * 41, [17, 41], [3, 5], coeffs)
    ratio = s / (s17 * s41)
    # A genuine product formula would make this ratio 1.
    if abs(ratio - 1) < 1e-6:
        raise RuntimeError("unexpected factorisation")
    return {
        "q": [17, 41],
        "P": [p17, p41, p],
        "S17": [float(s17.real), float(s17.imag)],
        "S41": [float(s41.real), float(s41.imag)],
        "S": [float(s.real), float(s.imag)],
        "ratio_over_product": [float(ratio.real), float(ratio.imag)],
        "abs_ratio": float(abs(ratio)),
    }


def readout_l2(q: int) -> arb:
    """||Gamma_q||_2 = (q^3 (q-2) (2q-3))^{1/2}."""
    return (arb(q) ** 3 * (q - 2) * (2 * q - 3)).sqrt()


def pack(z: arb) -> dict:
    return {"str": str(z), "lo": lo_f(z), "hi": hi_f(z)}


def majorant() -> dict:
    ctx.prec = 200
    traces = json.load(open(os.path.join(LOG_DIR, "h7_lin_traces.json")))
    row = next(
        r
        for r in traces["traces"]
        if r["d"] == Q1 * Q2 and r["beta"] == [0, 0] and r["sector"] == 0 and r["period"] == 57
    )
    re = arb(row["trace"]["re"])
    im = arb(row["trace"]["im"])
    tr_abs = (re * re + im * im).sqrt()
    # Threshold, same arithmetic as h7_uniform.kappa_report.
    lam = arb(3) + 2 * arb(2).sqrt()
    mu = arb("1.9154712")
    h = 9369319
    u0, u1 = 1, 7
    for _ in range(1, (19 - 1) // 2):
        u0, u1 = u1, 6 * u1 - u0
    if u1 != h:
        raise RuntimeError((u1, h))
    m = 57
    zlo = (arb(1) / 2) * (1 - lam ** (-m)) * (mu ** m - arb("3012.4"))
    d = arb(Q1 * Q2)
    T = zlo * (d ** 2) / (2 * h)
    R = arb(R_NUM) / R_DEN
    RP = R ** P
    r1 = readout_l2(Q1)
    r2 = readout_l2(Q2)
    # |S| <= dim * ||Gamma||_2 * ||R||^P, and ||Gamma_d||_2 = ||Gamma_q1||_2 ||Gamma_q2||_2.
    cap = arb(DIM) * r1 * r2 * RP
    # Koopman form: |Tr(M T^P)| <= max|kappa| * dim * d^2 * R^P.
    max_kappa = arb((Q1 - 2) * (Q2 - 2))
    koop = max_kappa * DIM * (d ** 2) * RP
    # Constant arithmetic piece: d * Tr Q_0. Under the threshold.
    term1 = d * tr_abs
    # beta = 0 carries kappa(0) = (q-2)(q'-2), not the dual constant d.
    kappa0 = arb(Q1 - 2) * arb(Q2 - 2)
    zero_mode = kappa0 * tr_abs
    # Spectral radius of the Koopman operator: at least the untwisted step.
    # The Newton endpoint is re-read from the uniform log.
    uniform = json.load(open(os.path.join(LOG_DIR, "h7_uniform.json")))
    rho_lo = arb(str(uniform["norm"]["newton_untwisted_step"]["product_lo"]))
    return {
        "d": Q1 * Q2,
        "dim": DIM,
        "P": P,
        "R": f"{R_NUM}/{R_DEN}",
        "readout_457": pack(r1),
        "readout_7521721": pack(r2),
        "R_power": pack(RP),
        "cs_majorant": pack(cap),
        "cs_over_T": pack(cap / T),
        "koopman_majorant": pack(koop),
        "koopman_over_T": pack(koop / T),
        "term1_abs": pack(term1),
        "T_over_term1": pack(T / term1),
        "kappa0": str(kappa0),
        "zero_mode_abs": pack(zero_mode),
        "T_over_zero_mode": pack(T / zero_mode),
        "T": pack(T),
        "tr_abs": pack(tr_abs),
        "rho_T_lo": pack(rho_lo),
        "rho_T_hi_from_norm": f"{R_NUM}/{R_DEN}",
    }


def orbit457() -> dict:
    """Float remainder at q=457, sector 0, from the finished orbit scan.

    Not an enclosure. The scan's Frobenius majorant is recorded so that a
    reader can see it does not certify the traces.
    """
    full_path = os.path.join(LOG_DIR, "h7_avg_orbit_q457_a0_full.json")
    iso_path = os.path.join(LOG_DIR, "h7_lin_iso_sum.json")
    uniform_path = os.path.join(LOG_DIR, "h7_uniform.json")
    full = json.load(open(full_path))
    q, tb = 457, 247
    b0 = np.array(full["beta0"])
    b1 = np.array(full["beta1"])
    Nv = np.array(full["N"]) % q
    length = np.array(full["len"])
    tr = np.array(full["tr_re"]) + 1j * np.array(full["tr_im"])
    frob = np.array(full["frob_max"])
    err = np.array(full["err_frob"])
    tinv = pow(tb, -1, q)
    kap = np.empty(len(Nv), dtype=np.complex128)
    zero = Nv == 0
    kap[zero] = q - 2
    ang = (tinv * Nv[~zero]) % q
    kap[~zero] = -1 - np.exp(2j * np.pi * ang / q)
    contrib = kap * length * tr
    ident = (b0 == 0) & (b1 == 0)
    if int(ident.sum()) != 1:
        raise RuntimeError("identity class")
    rest = ~ident
    iso = zero & rest
    ani = ~zero
    Srest = contrib[rest].sum()
    Siso = contrib[iso].sum()
    Sani = contrib[ani].sum()
    iso_log = json.load(open(iso_path))
    certified = None
    for row in iso_log["rows"]:
        if row.get("sector") == 0:
            certified = row["S_iso"]["abs_lo"]
    if certified is None:
        raise RuntimeError(list(iso_log.keys()))
    uniform = json.load(open(uniform_path))
    ctx.prec = 200
    mass = arb(uniform["kappa"]["sum_nonzero"])
    T = arb(uniform["kappa"]["T"])
    room = T / mass
    zero_tr = abs(tr[ident][0])
    certified_tr = float(arb(uniform["kappa"]["untwisted_abs"]))
    return {
        "q": q,
        "sector": 0,
        "n_orbits": int(len(Nv)),
        "n_rest": int(rest.sum()),
        "n_iso_nonzero": int(iso.sum()),
        "n_anisotropic": int(ani.sum()),
        "zero_abs": float(abs(contrib[ident][0])),
        "zero_tr_abs": float(zero_tr),
        "zero_tr_certified": certified_tr,
        "zero_tr_rel_gap": float(abs(zero_tr - certified_tr) / certified_tr),
        "rest_re": float(Srest.real),
        "rest_im": float(Srest.imag),
        "rest_abs": float(abs(Srest)),
        "rest_triangle": float(np.abs(contrib[rest]).sum()),
        "iso_abs": float(abs(Siso)),
        "iso_certified_abs": certified,
        "iso_abs_gap": float(abs(abs(Siso) - certified)),
        "ani_abs": float(abs(Sani)),
        "ani_triangle": float(np.abs(contrib[ani]).sum()),
        "max_tr_rest": float(np.abs(tr[rest]).max()),
        "max_contrib_rest": float(np.abs(contrib[rest]).max()),
        "max_frob_rest": float(frob[rest].max()),
        "max_err_frob": float(err.max()),
        "trace_room": pack(room),
        "note": "Float64. The err_frob column is not an enclosure.",
    }


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    os.makedirs(LOG_DIR, exist_ok=True)
    doc = {}
    if os.path.exists(OUT):
        doc = json.load(open(OUT))
    if cmd in ("check", "all"):
        g = check_gamma()
        print("gamma", g, flush=True)
        doc["gamma_check"] = g
        w = check_words()
        print("words", w, flush=True)
        doc["word_check"] = w
        if cmd == "all":
            # The factor check is a few times 10^5 residue classes. Run it
            # only in `all`, not in a second accidental `check`.
            fac = check_factor()
            print("factor", fac, flush=True)
            doc["factor_check"] = fac
        json.dump(doc, open(OUT, "w"), indent=1)
    if cmd == "orbit":
        doc["orbit457"] = orbit457()
        json.dump(doc, open(OUT, "w"), indent=1)
        print("rest_abs", doc["orbit457"]["rest_abs"], "iso_gap", doc["orbit457"]["iso_abs_gap"], flush=True)
    if cmd in ("majorant", "all"):
        doc["majorant"] = majorant()
        json.dump(doc, open(OUT, "w"), indent=1)
        print("cs_over_T", doc["majorant"]["cs_over_T"]["lo"], flush=True)
        print("T_over_term1", doc["majorant"]["T_over_term1"]["lo"], flush=True)
    if cmd not in ("check", "majorant", "orbit", "all"):
        raise SystemExit(f"unknown {cmd}")


if __name__ == "__main__":
    main()
