#!/usr/bin/env python3
"""Additive energy of <lambda> and the theta arithmetic for amplified H8.

Exact integer counts for the graph energy, and arb enclosures for the
theta comparisons. No operator data. No registry file is read for writing.
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from flint import arb, ctx

ctx.prec = 200
HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "logs" / "h8_energy.json"
FACTORS = HERE / "logs" / "h7h8.json"


def mat_mul(A, B, n: int):
    return (
        (A[0] * B[0] + A[1] * B[2]) % n,
        (A[0] * B[1] + A[1] * B[3]) % n,
        (A[2] * B[0] + A[3] * B[2]) % n,
        (A[2] * B[1] + A[3] * B[3]) % n,
    )


def order_lambda(n: int) -> int:
    """Order of S = [[3, 4], [2, 3]] in GL(2, Z/nZ)."""
    I = (1, 0, 0, 1)
    S = (3, 4, 2, 3)
    A = S
    k = 1
    limit = n * n + 5
    while A != I:
        A = mat_mul(A, S, n)
        k += 1
        if k > limit:
            raise RuntimeError(f"order not found mod {n}")
    return k


def sqrt2(n: int) -> int | None:
    for w in range(n):
        if (w * w - 2) % n == 0:
            return w
    return None


def graph_points(n: int, L: int, w: int):
    g = (3 + 2 * w) % n
    inv = pow(g, -1, n)
    pts = []
    a = b = 1
    for _ in range(L):
        pts.append((a, b))
        a = a * g % n
        b = b * inv % n
    if len(set(pts)) != L:
        raise RuntimeError(f"duplicate graph points mod {n}")
    return pts


def energy(pts, n: int) -> int:
    cnt: Counter = Counter()
    for x in pts:
        for y in pts:
            cnt[((x[0] + y[0]) % n, (x[1] + y[1]) % n)] += 1
    return sum(v * v for v in cnt.values())


def ball_str(x: arb) -> str:
    return str(x)


def main() -> None:
    lam = 3 + 2 * arb(2).sqrt()
    lnlam = lam.log()

    def alpha(rho: str) -> arb:
        r = arb(rho)
        return -((lam * r * r) ** arb("1.5")).log()

    a28 = alpha("0.28")
    theta_wrap = a28 / (4 * lnlam)
    # First-moment threshold, same substitution as h7h8.py.
    rate = arb("0.2945")
    eps = 1 + arb(2).sqrt()
    budget_lo = -(eps * (rate + arb("5e-5"))).log()
    Lam = arb("1.9656353")
    r2 = arb("1.0529012")
    c_del = (2 * Lam.log() - r2.log()) / lnlam
    theta_first = budget_lo / (c_del.upper() * lnlam)

    rows = []
    # Odd orders: equality 2L^2 - L. Even orders: equality 3L^2 - 3L.
    odd_primes = (7, 31, 41, 457)
    even_primes = (73, 89)
    for q in odd_primes + even_primes:
        w = sqrt2(q)
        if w is None:
            raise RuntimeError(f"{q} is inert")
        L = order_lambda(q)
        E = energy(graph_points(q, L, w), q)
        formula = (2 * L * L - L) if L % 2 else (3 * L * L - 3 * L)
        if E != formula:
            raise RuntimeError(f"energy mismatch at {q}: {E} != {formula}")
        rows.append({
            "n": q,
            "split": True,
            "L": L,
            "parity": "odd" if L % 2 else "even",
            "energy": E,
            "formula": formula,
            "equal": True,
        })

    # Composite with a full-order split prime factor: 217 = 7*31, order 15 = order mod 31.
    for n, q_full in ((217, 31),):
        w = sqrt2(n)
        if w is None:
            raise RuntimeError(f"no sqrt2 mod {n}")
        L = order_lambda(n)
        Lq = order_lambda(q_full)
        if L != Lq:
            raise RuntimeError(f"orders differ: {n} vs {q_full}")
        E = energy(graph_points(n, L, w), n)
        cap = 2 * L * L - L
        if E > cap:
            raise RuntimeError(f"projection fails at {n}: {E} > {cap}")
        rows.append({
            "n": n,
            "split": True,
            "L": L,
            "full_order_prime": q_full,
            "energy": E,
            "cap_2L2_minus_L": cap,
            "within_cap": True,
        })

    # Prime powers. 31^2 keeps order 15 and the odd formula. Powers of 7
    # raise the order, and the energy then exceeds 2L^2 - L.
    powers = []
    expected_excess = {49: True, 343: True, 961: False}
    for n, excess in expected_excess.items():
        w = sqrt2(n)
        if w is None:
            raise RuntimeError(f"no sqrt2 mod {n}")
        L = order_lambda(n)
        E = energy(graph_points(n, L, w), n)
        odd_cap = 2 * L * L - L
        got = E > odd_cap
        if got != excess:
            raise RuntimeError(f"prime-power excess at {n}: got {got}, E={E}, cap={odd_cap}")
        powers.append({
            "n": n,
            "L": L,
            "energy": E,
            "odd_formula": odd_cap,
            "exceeds_odd_formula": got,
        })

    # Census: every prime power in the stored K_p factorisations, p <= 31.
    # Splitting is q == ±1 mod 8. Rank: 7 has order 3, every other prime has order 3p.
    stored = json.loads(FACTORS.read_text())
    census = []
    for row in stored["rows"]:
        p = int(row["p"])
        if p < 5 or p > 31:
            continue
        fac = {int(q): int(e) for q, e in row["factors"].items()}
        entry = {"p": p, "factors": []}
        for q, e in sorted(fac.items()):
            if q % 8 not in (1, 7):
                raise RuntimeError(f"inert prime {q} in K_{p}")
            Lq = order_lambda(q)
            expect = 3 if q == 7 else 3 * p
            if Lq != expect:
                raise RuntimeError(f"order {Lq} != {expect} at q={q}, p={p}")
            mod = q ** e
            Lmod = order_lambda(mod)
            entry["factors"].append({
                "q": q,
                "exp": e,
                "mod8": q % 8,
                "order_q": Lq,
                "order_q_exp": Lmod,
                "order_grows": Lmod != Lq,
            })
        census.append(entry)

    def char_theta(p: int, L: int) -> arb:
        # (2,2) bound beats |S| <= L only for q < L^2/2.
        return (arb(L) ** 2 / 2).log() / (arb(p) * lnlam)

    def hbk_theta(p: int, L: int) -> arb:
        # L <= q^{2/3} iff theta >= (3/2) ln L / (p ln lambda).
        return (arb(3) / 2) * arb(L).log() / (arb(p) * lnlam)

    def illegitimate(p: int, L: int) -> arb:
        # theta_wrap + ln(L/2) / (p ln lambda), the shift from replacing d by d*(2/L).
        return theta_wrap + (arb(L) / 2).log() / (arb(p) * lnlam)

    comparisons = []
    # p >= 29: the (2,2) improvement lies inside the c=1 interval, the HBK
    # size hypothesis holds throughout that interval, and the illegitimate
    # energy-ratio shift stays under the first-moment threshold.
    # p = 19 and 23 are recorded and not asserted: both lie below p_thr.
    for p in (19, 23, 29, 1409, 3307):
        strict = p >= 29
        for L in (p, 3 * p):
            tc = char_theta(p, L)
            th = hbk_theta(p, L)
            ti = illegitimate(p, L)
            q_over = (theta_wrap * arb(p) * lnlam).exp() / (arb(L) ** 2 / 2)
            if strict:
                if not (tc.upper() < theta_wrap.lower()):
                    raise RuntimeError(f"character threshold not inside c=1 at p={p}, L={L}")
                if not (th.upper() < theta_wrap.lower()):
                    raise RuntimeError(f"HBK hypothesis not forced on the gap at p={p}, L={L}")
                if not (ti.upper() < theta_first.lower()):
                    raise RuntimeError(f"illegitimate shift meets the first-moment threshold at p={p}")
                if not (q_over.lower() > 1):
                    raise RuntimeError(f"gap not above L^2/2 at p={p}, L={L}")
            comparisons.append({
                "p": p,
                "L": L,
                "strict": strict,
                "theta_character_upper": ball_str(tc.upper()),
                "theta_hbk_hypothesis_upper": ball_str(th.upper()),
                "theta_if_energy_ratio_inserted_upper": ball_str(ti.upper()),
                "q_at_wrap_over_L2_half_lower": ball_str(q_over.lower()),
            })

    # BGK needs |H| >= q^delta for a fixed delta > 0. At the bottom of the
    # gap, ln q = alpha * p / 4, so the largest delta still compatible with
    # L = 3p is 4 ln(3p) / (alpha p), which tends to 0.
    bgk = []
    for p in (29, 1409, 3307):
        dmax = 4 * arb(3 * p).log() / (a28 * arb(p))
        ratio = arb(3 * p) / (arb("0.01") * a28 * arb(p) / 4).exp()
        bgk.append({
            "p": p,
            "delta_max_upper": ball_str(dmax.upper()),
            "L_over_q_to_the_0.01_upper": ball_str(ratio.upper()),
            "fixed_delta_0.01_fails": bool(ratio.upper() < 1),
        })
    if not (arb(bgk[1]["delta_max_upper"]).upper() < arb("0.021")):
        raise RuntimeError("delta_max at p=1409 is not below 0.021")
    if not (arb(bgk[2]["delta_max_upper"]).upper() < arb("0.01")):
        raise RuntimeError("delta_max at p=3307 is not below 0.01")
    if not bgk[2]["fixed_delta_0.01_fails"]:
        raise RuntimeError("delta=0.01 still holds at p=3307")

    # Centres must reproduce the published h7h8 balls.
    published_alpha = arb("1.17477626638003325659")
    published_theta = arb("0.16661157")
    if not (abs(a28 - published_alpha) < arb("1e-20")):
        raise RuntimeError("alpha centre drifted")
    if not (abs(theta_wrap - published_theta) < arb("1e-8")):
        raise RuntimeError("theta centre drifted")

    out = {
        "alpha_0.28": ball_str(a28),
        "theta_wrap_c1": ball_str(theta_wrap),
        "theta_first_moment_lower_end": ball_str(theta_first),
        "gap_remains": True,
        "energy_rows": rows,
        "prime_powers": powers,
        "census_p5_to_31": census,
        "comparisons": comparisons,
        "bgk_delta_0.01": bgk,
        "claims": {
            "energy_exponent": 2,
            "loss_factor_against_L3": "< 2/L",
            "wrap_exponent_unchanged": 1,
            "H8_discharged": False,
        },
    }
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(f"wrote {OUT}")
    print("theta_wrap", theta_wrap)
    print("theta_first", theta_first)
    for row in comparisons:
        if row["L"] == 3 * row["p"]:
            print(
                "p", row["p"],
                "char", row["theta_character_upper"],
                "inserted", row["theta_if_energy_ratio_inserted_upper"],
            )


if __name__ == "__main__":
    main()
