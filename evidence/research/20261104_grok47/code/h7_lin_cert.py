"""Ball traces of finite-section monodromy pieces that enter Lin_d.

The sum over every beta at d = 3437426497 is not computed: that state has
d^2 fibres. This script encloses

  * kappa_d(N beta) for the three crossing betas, by the product formula
  * the sector-0 and sector-4 vertex-section traces of those three orbits,
    of the untwisted section, and of the 16 isotropic orbit representatives
    at the prime 457

Commands
    python3 h7_lin_cert.py kappa
    python3 h7_lin_cert.py cross
    python3 h7_lin_cert.py iso
    python3 h7_lin_cert.py all
"""

from __future__ import annotations

import json
import math
import os
import sys
import time

from flint import acb, arb, ctx

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import h7_multidisc_cert as cert  # noqa: E402
from h7_rates import hi_f, lo_f  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
LOG_DIR = os.path.join(HERE, "..", "logs")
OUT = os.path.join(LOG_DIR, "h7_lin_traces.json")

# Squarefree included conductors, each prime || h_m, all != the h_p prime.
SPECS = [
    {
        "name": "d3437426497",
        "p": 19,
        "d": 3437426497,
        "facs": [457, 7521721],
        "beta": [-208, 0],
        "N": (-208) ** 2 - 2 * 0 ** 2,
    },
    {
        "name": "d24061985479",
        "p": 19,
        "d": 24061985479,
        "facs": [7, 457, 7521721],
        "beta": [227, 227],
        "N": 227 ** 2 - 2 * 227 ** 2,
    },
    {
        "name": "d2735635252619983",
        "p": 29,
        "d": 2735635252619983,
        "facs": [7, 13921, 28073057689],
        "beta": [-89, 0],
        "N": (-89) ** 2 - 2 * 0 ** 2,
    },
]


def nsw_h(p: int) -> int:
    n = (p - 1) // 2
    u0, u1 = 1, 7
    for _ in range(1, n):
        u0, u1 = u1, 6 * u1 - u0
    return u1


def trial_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            return False
        f += 2
    return True


def nu0_of(m: int, a: int = 2) -> tuple[int, int, int]:
    sys.path.insert(0, "/workspace/computations/verification/lineI/code")
    from law import mdata

    D = mdata(m)
    h, yp = D["h"], D["yp"]
    nu0 = next(
        x
        for x in [((a // 2) * pow(4, -1, h)) % h + s * h for s in (0, 1)]
        if x % 2 == 1
    )
    return h, yp, nu0


def tb_prime(m: int, q: int, a: int = 2) -> int:
    """Missing label at the prime level q || h_m. One linear condition."""
    h, yp, nu0 = nu0_of(m, a)
    if h % q != 0 or (h // q) % q == 0:
        raise RuntimeError((m, q, "not exactly ||"))
    step = 2 * (h // q)
    j = (-nu0 * pow(step, -1, q)) % q
    if j == 0:
        raise RuntimeError("bad j is 0")
    nu = (nu0 + step * j) % (2 * h)
    if math.gcd(nu, 2 * h) == 1 or nu % q != 0:
        raise RuntimeError("closed form is not the missing member")
    return (j * yp) % q


def k_std(q: int, tb: int, v: int) -> acb:
    v %= q
    if v == 0:
        return acb(q - 2)
    ang = acb(2 * ((pow(tb, -1, q) * v) % q)) / q
    return -acb(1) - ang.exp_pi_i()


def kappa_acb(m: int, facs: list[int], u: int) -> acb:
    """Product formula. t_c(q) = t_b(q) * (d/q) mod q, argument scaled by (d/q)^{-1}."""
    d = 1
    for q in facs:
        d *= q
    u %= d
    prod = acb(1)
    for q in facs:
        cof = d // q
        tb = (tb_prime(m, q) * cof) % q
        v = (u * pow(cof, -1, q)) % q
        prod *= k_std(q, tb, v)
    return prod


def f_lo(x: arb) -> float:
    """Float at most the lower endpoint. The flint string is the enclosure."""
    s = x.lower()
    v = float(s.mid())
    rad = float(s.rad().abs_upper())
    return v - rad - abs(v) * 1e-15 - 1e-30


def f_hi(x: arb) -> float:
    s = x.upper()
    v = float(s.mid())
    rad = float(s.rad().abs_upper())
    return v + rad + abs(v) * 1e-15 + 1e-30


def pack(z: acb) -> dict:
    return {
        "re": str(z.real),
        "im": str(z.imag),
        "re_lo": f_lo(z.real),
        "re_hi": f_hi(z.real),
        "im_lo": f_lo(z.imag),
        "im_hi": f_hi(z.imag),
        "abs_lo": lo_f(z.abs_lower()),
        "abs_hi": hi_f(z.abs_upper()),
        "rad_hi": hi_f(z.rad()),
        "bits": int(z.rel_accuracy_bits()),
    }


def load() -> dict:
    if os.path.exists(OUT):
        return json.load(open(OUT))
    return {"prec": ctx.prec, "kappa": [], "traces": [], "iso": []}


def save(doc: dict) -> None:
    os.makedirs(LOG_DIR, exist_ok=True)
    json.dump(doc, open(OUT, "w"), indent=1)


def prepare():
    ctx.prec = 320
    cert.RHO = arb(6) / arb(5)
    # Importing the cert module must not have built letters yet.
    if cert.RHO is None:
        raise RuntimeError("RHO")
    t0 = time.time()
    centers, index, blocks, n_out = cert.build_blocks()
    print({"built": round(time.time() - t0, 2), "n_out": n_out, "letters": len(blocks)}, flush=True)
    if n_out != 0:
        raise RuntimeError("core is not forward-invariant")
    return centers, index, blocks


def frobenius_majorant(blocks) -> dict:
    """||L(tw)||_F <= sum_n ||block_n||_F, phases unimodular. Not a spectral bound."""
    # Group entries by n, summing the centre blocks into one Frobenius square.
    acc = {}
    for (n, _c), (_j, block) in blocks.items():
        s = acc.get(n, arb(0))
        K = block.nrows()
        for r in range(K):
            for q in range(K):
                s += block[r, q].abs_upper() ** 2
        acc[n] = s
    total = arb(0)
    for s in acc.values():
        total += s.sqrt()
    return {
        "n_letters_with_core_image": len(acc),
        "sum_frob_hi": hi_f(total),
        "note": "Upper bound on the Frobenius norm of one twisted step. (sum)^P is a majorant of ||Q||_F and is not expected to sit under the epsilon budget.",
    }


def period_trace(centers, index, blocks, d: int, bx: int, by: int, a: int):
    pw = cert.lambda_orbit(d)
    tws = cert.twists(d, bx, by, pw)
    dim = len(centers) * cert.K_MODES
    Q = cert.eye(dim)
    exp_r = 0
    t0 = time.time()
    period = len(pw)
    print(f"trace d={d} beta=({bx},{by}) sector={a} P={period}", flush=True)
    for step, tw in enumerate(tws, start=1):
        Q = cert.assemble(centers, index, blocks, d, tw, a) * Q
        Q, e = cert.scale_down(Q)
        exp_r += e
        if step % 20 == 0 or step == period:
            print(
                f"  step {step}/{period} exp {exp_r} bits {Q[0, 0].rel_accuracy_bits()} t {time.time()-t0:.1f}",
                flush=True,
            )
    tr = acb(0)
    for i in range(dim):
        tr += Q[i, i]
    tr *= arb(2) ** exp_r
    rec = {
        "d": d,
        "beta": [bx, by],
        "sector": a,
        "period": period,
        "scale_exp": exp_r,
        "seconds": round(time.time() - t0, 2),
        "trace": pack(tr),
    }
    print("  abs", rec["trace"]["abs_lo"], rec["trace"]["abs_hi"], "bits", rec["trace"]["bits"], flush=True)
    return tr, rec


def have(doc, d, bx, by, a) -> bool:
    for row in doc["traces"]:
        if row["d"] == d and row["beta"] == [bx, by] and row["sector"] == a:
            return True
    return False


def add_trace(doc, centers, index, blocks, d, bx, by, a):
    if have(doc, d, bx, by, a):
        print("skip", d, bx, by, a, flush=True)
        return
    _tr, rec = period_trace(centers, index, blocks, d, bx, by, a)
    doc["traces"].append(rec)
    save(doc)


def cmd_kappa(doc) -> None:
    rows = []
    for spec in SPECS:
        m = 3 * spec["p"]
        for q in spec["facs"]:
            if not trial_prime(q):
                raise RuntimeError(q)
            if q % 8 not in (1, 7):
                raise RuntimeError((q, "2 is not a square"))
        d = 1
        for q in spec["facs"]:
            d *= q
        if d != spec["d"]:
            raise RuntimeError((d, spec["d"]))
        if spec["N"] != spec["beta"][0] ** 2 - 2 * spec["beta"][1] ** 2:
            raise RuntimeError("N")
        # Unit at every prime factor: the product formula's local argument is nonzero.
        for q in spec["facs"]:
            if spec["N"] % q == 0:
                raise RuntimeError((q, "isotropic"))
        k = kappa_acb(m, spec["facs"], spec["N"] % spec["d"])
        h = nsw_h(spec["p"])
        Kp = 4 * h * h + 3
        hm = h * Kp
        lam = arb(3) + 2 * arb(2).sqrt()
        mu = arb("1.9154712")
        zlo = (arb(1) / 2) * (1 - lam ** (-m)) * (mu ** m - arb("3012.4"))
        # |S| threshold at which eta = |Lin| h_p / |Z|^2 reaches 1, using |Z|>=zlo
        # and |Lin| <= (2/d^2) |Z| |S|: need |S| >= zlo * d^2 / (2 h_p) to be able to reach eta=1.
        budget = zlo * spec["d"] ** 2 / (2 * h)
        rows.append(
            {
                "name": spec["name"],
                "p": spec["p"],
                "m": m,
                "d": spec["d"],
                "facs": spec["facs"],
                "beta": spec["beta"],
                "N": spec["N"],
                "kappa": pack(k),
                "h_p": str(h),
                "K_mod_d": Kp % spec["d"],
                "d_sq_le_hm": spec["d"] ** 2 <= hm,
                "zlo_lo": lo_f(zlo),
                "S_for_eta_1_lo": lo_f(budget),
            }
        )
        print(spec["name"], "kappa_abs", rows[-1]["kappa"]["abs_lo"], rows[-1]["kappa"]["abs_hi"], flush=True)
    doc["kappa"] = rows
    doc["prec"] = ctx.prec
    save(doc)


def cmd_cross(doc, centers, index, blocks) -> None:
    # Untwisted section, one product per period. d is only the modulus of lambda's order.
    add_trace(doc, centers, index, blocks, 3437426497, 0, 0, 0)
    add_trace(doc, centers, index, blocks, 3437426497, 0, 0, 4)
    add_trace(doc, centers, index, blocks, 2735635252619983, 0, 0, 0)
    add_trace(doc, centers, index, blocks, 2735635252619983, 0, 0, 4)
    for spec in SPECS:
        bx, by = spec["beta"]
        for a in (0, 4):
            add_trace(doc, centers, index, blocks, spec["d"], bx, by, a)


def sqrt2_mod(q: int) -> int:
    # q == 1 or 7 mod 8, so 2 is a square. Tonelli for p == 5 or 1 mod 8 is
    # unnecessary: q % 8 == 1, and a search of residues is fine at q = 457.
    for i in range(q):
        if (i * i - 2) % q == 0:
            return i
    raise RuntimeError(q)


def iso_reps(q: int = 457):
    w = sqrt2_mod(q)
    out = []
    for sign in (1, -1):
        v = ((sign * w) % q, 1)
        lx = (3 * v[0] + 4 * v[1]) % q
        ly = (2 * v[0] + 3 * v[1]) % q
        ell = ly % q
        if (ell * v[0] - lx) % q != 0:
            raise RuntimeError("not an eigenvector")
        seen = [False] * q
        reps = []
        for s in range(1, q):
            if seen[s]:
                continue
            t = s
            length = 0
            while not seen[t]:
                seen[t] = True
                t = (t * ell) % q
                length += 1
            reps.append((s, length))
        betas = []
        for s, length in reps:
            bx, by = (s * v[0]) % q, (s * v[1]) % q
            nn = (bx * bx - 2 * by * by) % q
            if nn != 0:
                raise RuntimeError("not isotropic")
            betas.append({"beta": [bx, by], "orbit_len": length})
        if sum(b["orbit_len"] for b in betas) != q - 1:
            raise RuntimeError("line not covered")
        out.append({"sign": sign, "ell": ell, "w": w, "reps": betas})
    return out


def cmd_iso(doc, centers, index, blocks, sectors=(0, 4), out_path=None) -> None:
    q = 457
    lines = iso_reps(q)
    doc["iso_reps"] = [
        {"sign": ln["sign"], "ell": ln["ell"], "n_reps": len(ln["reps"]), "reps": ln["reps"]}
        for ln in lines
    ]
    save(doc)
    for ln in lines:
        for rep in ln["reps"]:
            bx, by = rep["beta"]
            for a in sectors:
                add_trace(doc, centers, index, blocks, q, bx, by, a)


def cmd_check() -> None:
    """Float check of the product formula against the member enumeration at m=15, d=287."""
    import numpy as np

    m, d, facs = 15, 7 * 41, [7, 41]
    _h, _yp, _nu0 = nu0_of(m, 2)
    # Re-enumerate with the same rule as lineJ/J3/code/inherit7q.py, exact level.
    sys.path.insert(0, "/workspace/computations/verification/lineI/code")
    from law import mdata

    D = mdata(m)
    h, yp = D["h"], D["yp"]
    nu0 = next(x for x in [((2 // 2) * pow(4, -1, h)) % h + s * h for s in (0, 1)] if x % 2 == 1)
    ts = []
    for j in range(1, d):
        if math.gcd(j, d) != 1:
            continue
        nu = (nu0 + (2 * h // d) * j) % (2 * h)
        if math.gcd(nu, 2 * h) != 1:
            continue
        ts.append((j * yp) % d)
    rng = np.random.default_rng(0)
    us = [int(u) for u in rng.integers(0, d, size=40)] + [0, 1]
    mx = 0.0
    for u in us:
        brute = 0j
        for t in ts:
            brute += np.exp(2j * np.pi * ((pow(int(t), -1, d) * u) % d) / d)
        ka = kappa_acb(m, facs, u)
        mid = complex(float(ka.real.mid()), float(ka.imag.mid()))
        mx = max(mx, abs(brute - mid))
    rec = {"m": m, "d": d, "n_members": len(ts), "n_u": len(us), "max_abs_err": float(mx), "prec": int(ctx.prec)}
    json.dump(rec, open(os.path.join(LOG_DIR, "h7_lin_kappa_check.json"), "w"), indent=1)
    print(rec, flush=True)
    if mx > 1e-8:
        raise SystemExit("kappa check failed")


def cmd_sum_iso() -> None:
    """Sum the stored isotropic traces. Reads the per-sector logs, writes one summary."""
    rows = []
    for sector in (0, 4):
        path = os.path.join(LOG_DIR, f"h7_lin_iso_s{sector}.json")
        doc = json.load(open(path))
        acc = acb(0)
        n = 0
        for row in doc["traces"]:
            if row["d"] != 457 or row["sector"] != sector or row["period"] != 57:
                raise RuntimeError(row["beta"])
            acc += acb(arb(row["trace"]["re"]), arb(row["trace"]["im"]))
            n += 1
        if n != 16:
            raise RuntimeError(n)
        # kappa = q-2 on the isotropic line, and every orbit has length 57.
        S = acc * acb((457 - 2) * 57)
        rows.append({"sector": sector, "n": n, "sum_reps": pack(acc), "S_iso": pack(S)})
        print(sector, "S_abs", rows[-1]["S_iso"]["abs_lo"], rows[-1]["S_iso"]["abs_hi"], flush=True)
    json.dump({"q": 457, "kappa": 455, "orbit": 57, "rows": rows}, open(os.path.join(LOG_DIR, "h7_lin_iso_sum.json"), "w"), indent=1)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    os.makedirs(LOG_DIR, exist_ok=True)
    ctx.prec = 320
    cert.RHO = arb(6) / arb(5)
    doc = load()
    doc["prec"] = 320
    if cmd == "check":
        cmd_check()
        return
    if cmd == "sum-iso":
        cmd_sum_iso()
        return
    if cmd == "kappa":
        cmd_kappa(doc)
        return
    centers, index, blocks = prepare()
    doc["frobenius_step"] = frobenius_majorant(blocks)
    doc["section"] = {"k0": cert.K0, "K": cert.K_MODES, "nmax": cert.N_MAX, "dim": 7 * cert.K_MODES, "rho": "1.2"}
    save(doc)
    print("frob step", doc["frobenius_step"]["sum_frob_hi"], flush=True)
    if cmd in ("kappa", "all", "cross", "iso"):
        if not doc.get("kappa"):
            cmd_kappa(doc)
    if cmd in ("all", "cross"):
        cmd_cross(doc, centers, index, blocks)
    if cmd in ("all", "iso"):
        global OUT
        sectors = (0, 4)
        if len(sys.argv) > 2:
            sectors = tuple(int(x) for x in sys.argv[2].split(","))
            OUT = os.path.join(LOG_DIR, "h7_lin_iso_s" + "_".join(str(a) for a in sectors) + ".json")
            # Own file, so two sector jobs can run together. Kappa is copied for the record.
            doc = {
                "prec": 320,
                "kappa": doc.get("kappa", []),
                "traces": [],
                "iso": [],
                "frobenius_step": doc.get("frobenius_step"),
                "section": doc.get("section"),
            }
            save(doc)
        cmd_iso(doc, centers, index, blocks, sectors=sectors)
    print("done", len(doc["traces"]), flush=True)


if __name__ == "__main__":
    main()
