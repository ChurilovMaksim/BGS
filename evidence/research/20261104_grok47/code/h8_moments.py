#!/usr/bin/env python3
"""Window energies of powers of lambda, by lifting to Z[sqrt(2)].

Exact integer checks of the mass-7 relation and of the ordered energy on
short windows, and arb enclosures for the theta arithmetic. The amplified
weight is not replaced by the energy. No registry file is written.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from math import factorial
from pathlib import Path

from flint import arb, ctx

ctx.prec = 200
HERE = Path(__file__).resolve().parents[1]
OUT = HERE / "logs" / "h8_moments.json"
sys.path.insert(0, str(HERE / "code"))

from span_audit import digits_of, support_bounds  # noqa: E402


def lam_pow(n: int) -> tuple[int, int]:
    """lambda^n = a + b sqrt(2), lambda = 3+2 sqrt(2)."""
    if n < 0:
        a, b = lam_pow(-n)
        # lambda^{-1} = 3-2 sqrt(2), and N(lambda^n) = 1, so inverse is a - b sqrt(2).
        return a, -b
    a, b = 1, 0
    for _ in range(n):
        a, b = 3 * a + 4 * b, 2 * a + 3 * b
    return a, b


def lin_combo(mult: dict[int, int]) -> tuple[int, int]:
    a = b = 0
    for e, m in mult.items():
        pa, pb = lam_pow(e)
        a += m * pa
        b += m * pb
    return a, b


def window_energy(length: int, k: int) -> tuple[int, int]:
    """Ordered energy and the permutation energy on exponents {0,...,length-1}."""
    pw = [lam_pow(n) for n in range(length)]
    buckets: dict[tuple[int, int], int] = defaultdict(int)
    perm = 0

    def rec(pos: int, left: int, mult: list[int]) -> None:
        nonlocal perm
        if pos == length:
            if left != 0:
                return
            weight = factorial(k)
            for m in mult:
                weight //= factorial(m)
            a = b = 0
            for i, m in enumerate(mult):
                if m:
                    a += m * pw[i][0]
                    b += m * pw[i][1]
            buckets[(a, b)] += weight
            perm += weight * weight
            return
        for m in range(left + 1):
            mult.append(m)
            rec(pos + 1, left - m, mult)
            mult.pop()

    rec(0, k, [])
    energy = sum(v * v for v in buckets.values())
    return energy, perm


def ball_str(x: arb) -> str:
    return str(x)


def main() -> None:
    # lambda^4 + 6 lambda = 6 lambda^3 + 1.
    left = lin_combo({4: 1, 1: 6})
    right = lin_combo({3: 6, 0: 1})
    if left != right:
        raise RuntimeError(f"mass-7 identity failed: {left} != {right}")
    # The generator (x-1)(x^2-6x+1) has mass 8: lambda^3 + 7 lambda = 7 lambda^2 + 1.
    if lin_combo({3: 1, 1: 7}) != lin_combo({2: 7, 0: 1}):
        raise RuntimeError("mass-8 generator failed")

    # Integer comparisons used in the mass bound. lambda^{-1} = 3-2 sqrt(2).
    # 5 < lambda iff 49 < 50. 5 lambda^{-1} + lambda^{-2} < 1 iff 961 < 968.
    # 5 lambda^{-1} + 2 lambda^{-2} < 1 iff 576 < 578.
    if not (49 < 50 and 961 < 968 and 576 < 578 and 25 < 32):
        raise RuntimeError("integer comparisons failed")
    # 6 lambda^{-1} - 1 = lambda^{-2}, and 6 lambda^{-3} = lambda^{-2} + lambda^{-4}.
    # lambda^{-2} = 17-12 sqrt(2). lambda^{-3} = 99-70 sqrt(2). lambda^{-4} = 577-408 sqrt(2).
    # 6*(3-2 sqrt2) - 1 = 17-12 sqrt2.
    if 6 * 3 - 1 != 17 or 6 * (-2) != -12:
        raise RuntimeError("6/lambda - 1")
    # 6*lambda^{-3} = 6*(99-70 sqrt2) = 594-420 sqrt2
    # lambda^{-2}+lambda^{-4} = (17+577) + (-12-408) sqrt2 = 594-420 sqrt2.
    if 6 * 99 != 594 or 6 * 70 != 420:
        raise RuntimeError("six lambda^{-3}")
    if 17 + 577 != 594 or 12 + 408 != 420:
        raise RuntimeError("lambda^{-2}+lambda^{-4}")
    # 4*113^2 = 51076 < lambda^7 and 4*261^2 = 272484 < lambda^8, so those
    # diagonal values of k still lie inside the lifting range at span p/4.
    def exceeds(n: int, bound: int) -> bool:
        a, b = lam_pow(n)
        if a > bound:
            return True
        gap = bound - a
        return 2 * b * b > gap * gap

    if not exceeds(7, 4 * 113 * 113) or not exceeds(8, 4 * 261 * 261):
        raise RuntimeError("large-k height still inside the lifting range")

    windows = []
    for length in range(4, 11):
        for k in range(1, 8):
            energy, perm = window_energy(length, k)
            extra = energy - perm
            expect = 0 if k < 7 else 98 * max(length - 4, 0)
            if extra != expect:
                raise RuntimeError(
                    f"window L={length} k={k}: extra {extra} != {expect}"
                )
            windows.append({
                "length": length,
                "k": k,
                "energy": energy,
                "permutation_energy": perm,
                "extra": extra,
            })

    digits = []
    for n in range(-12, 13):
        a, b = lam_pow(n)
        k_left, k_right, nabs = support_bounds(a, b)
        if nabs != 1:
            raise RuntimeError(f"norm of lambda^{n} is {nabs}")
        word = digits_of(a, b, k_left - 2, k_right + 4)
        nonzero = {k: v for k, v in word.items() if v}
        expect = {1 - 2 * n: 1}
        if nonzero != expect:
            raise RuntimeError(f"digit of lambda^{n}: {nonzero} != {expect}")
        digits.append({"n": n, "site": 1 - 2 * n, "K_left": k_left, "K_right": k_right})

    lam = 3 + 2 * arb(2).sqrt()
    lnlam = lam.log()

    def alpha(rho: str) -> arb:
        r = arb(rho)
        return -((lam * r * r) ** arb("1.5")).log()

    a28 = alpha("0.28")
    theta_wrap = a28 / (4 * lnlam)
    rate = arb("0.2945")
    eps = 1 + arb(2).sqrt()
    budget_lo = -(eps * (rate + arb("5e-5"))).log()
    Lam = arb("1.9656353")
    r2 = arb("1.0529012")
    c_del = (2 * Lam.log() - r2.log()) / lnlam
    theta_first = budget_lo / (c_del.upper() * lnlam)
    theta_star = arb("0.26223963")
    c_needed = theta_wrap / theta_star

    published_alpha = arb("1.17477626638003325659")
    published_theta = arb("0.16661157")
    if not (abs(a28 - published_alpha) < arb("1e-20")):
        raise RuntimeError("alpha centre drifted")
    if not (abs(theta_wrap - published_theta) < arb("1e-8")):
        raise RuntimeError("theta centre drifted")
    if not (theta_wrap.upper() < arb("0.16661156569722353507")):
        raise RuntimeError("wrap threshold")
    if not (theta_first.lower() > arb("0.26223963")):
        raise RuntimeError("first-moment end")
    if not (c_needed.upper() < arb("0.63534092")):
        raise RuntimeError("c needed to reach 0.26223963")
    if not (c_needed.lower() > arb("0.63534091")):
        raise RuntimeError("c needed lower")

    rows = []
    for p in (1409, 3307):
        width = p // 4 + 1  # integers in an interval of span p/4
        for k in range(2, 8):
            # E equals the permutation count for k <= 6, and is at least that
            # count for k = 7. The permutation count is at least the injections
            # and at most k! |W|^k. The larger saving is the injection one.
            log_bang = arb(factorial(k)).log()
            saving_diag = arb(k) * arb(width).log() - log_bang
            inflate = sum(
                (arb(width) / (arb(width) - j)).log() for j in range(1, k)
            )
            saving_upper = saving_diag + inflate
            fibre = arb(1) if k < 7 else arb(2)
            # Character-sum estimate uses an upper bound on E.
            saving_for_char = saving_diag - fibre.log()
            theta_char = saving_for_char / (2 * arb(p) * lnlam)
            theta_formal = theta_wrap + saving_upper / (arb(p) * lnlam)
            # Smallest formal exponent: largest saving, smallest theta in ln d.
            gamma_wrap = -saving_upper / (theta_wrap * arb(p) * lnlam)
            gamma_star = -saving_upper / (theta_star * arb(p) * lnlam)
            lift = arb("0.125") + arb(4 * k * k).log() / (2 * arb(p) * lnlam)
            crude = arb("0.25") + arb(2 * k).log() / (arb(p) * lnlam)
            slack = (
                2 * theta_wrap * arb(p) * lnlam
                - (arb(p) / 4) * lnlam
                - arb(4 * k * k).log()
            )
            if k == 6 and p == 1409 and not (slack.lower() > 200):
                raise RuntimeError("slack at p=1409")
            if k == 6 and p == 3307 and not (slack.lower() > 400):
                raise RuntimeError("slack at p=3307")
            rows.append({
                "p": p,
                "k": k,
                "window": width,
                "fibre_factor": 1 if k < 7 else 2,
                "theta_character_upper": ball_str(theta_char.upper()),
                "theta_formal_upper": ball_str(theta_formal.upper()),
                "gamma_at_wrap": ball_str(gamma_wrap),
                "combined_at_wrap": ball_str(1 + gamma_wrap),
                "combined_at_star": ball_str(1 + gamma_star),
                "lift_threshold_upper": ball_str(lift.upper()),
                "crude_threshold_upper": ball_str(crude.upper()),
                "lift_slack_at_wrap_lower": ball_str(slack.lower()),
            })

    ceilings = {
        (1409, 6): ("0.00576146", "0.17815167", "0.12600049", "0.93073649", "0.95599406"),
        (3307, 6): ("0.00289289", "0.17240046", "0.12542628", "0.96525520", "0.97792520"),
        (1409, 7): ("0.00641117", "0.17973708", "0.12606255", "0.92122088", "0.94994840"),
        (3307, 7): ("0.00324273", "0.17322030", "0.12545272", "0.96033453", "0.97479890"),
    }
    by_key = {(row["p"], row["k"]): row for row in rows}
    for key, (char_c, formal_c, lift_c, comb_c, star_c) in ceilings.items():
        row = by_key[key]
        if not (arb(row["theta_character_upper"]) < arb(char_c)):
            raise RuntimeError(f"character ceiling {key}")
        if not (arb(row["theta_formal_upper"]) < arb(formal_c)):
            raise RuntimeError(f"formal ceiling {key}")
        if not (arb(row["lift_threshold_upper"]) < arb(lift_c)):
            raise RuntimeError(f"lift ceiling {key}")
        if not (arb(row["combined_at_wrap"]).lower() > arb(comb_c)):
            raise RuntimeError(f"combined exponent {key}")
        if not (arb(row["combined_at_star"]).lower() > arb(star_c)):
            raise RuntimeError(f"combined at star {key}")
        if not (arb(row["lift_slack_at_wrap_lower"]) > 0):
            raise RuntimeError(f"window p/4 does not lift at {key}")

    # The crude both-embeddings threshold sits above 1/4, hence above the
    # bottom of the gap. The stated length ln d/(2 ln lambda) needs theta >= 1/2.
    if not (arb(by_key[(1409, 6)]["crude_threshold_upper"]) > arb("0.25")):
        raise RuntimeError("crude threshold")
    if not (theta_first.upper() < arb("0.5")):
        raise RuntimeError("gap reaches 1/2")

    # Diagonal substitution, not a theorem: smallest k whose saving
    # k ln|W| - ln(k!) reaches theta_star. Both values are past mass 7.
    diagonal_k = []
    for p, width in ((1409, 353), (3307, 827)):
        need = (theta_star - theta_wrap) * arb(p) * lnlam
        found = None
        for k in range(7, 400):
            saving = arb(k) * arb(width).log() - arb(k + 1).lgamma()
            if saving.lower() > need.upper():
                found = k
                break
        if found is None:
            raise RuntimeError(f"no diagonal k at p={p}")
        diagonal_k.append({"p": p, "window": width, "k": found, "theorem": False})
    if diagonal_k[0]["k"] != 113 or diagonal_k[1]["k"] != 261:
        raise RuntimeError(f"diagonal k moved: {diagonal_k}")

    out = {
        "alpha_0.28": ball_str(a28),
        "theta_wrap_c1": ball_str(theta_wrap),
        "theta_first_moment_lower_end": ball_str(theta_first),
        "c_required_for_0.26223963": ball_str(c_needed),
        "mass7_identity": {"left": left, "right": right},
        "windows_checked": windows,
        "single_digits": digits,
        "rows": rows,
        "diagonal_k_not_a_theorem": diagonal_k,
        "claims": {
            "rigidity_holds_for_k": "<= 6",
            "first_extra_mass": 7,
            "wrap_exponent_unchanged": 1,
            "best_proved_formal_theta_p1409": "< 0.17973708",
            "best_proved_formal_theta_p3307": "< 0.17322030",
            "H8_discharged": False,
        },
    }
    OUT.write_text(json.dumps(out, indent=1) + "\n")
    print(f"wrote {OUT}")
    print("c_needed", c_needed)
    for key in ((1409, 6), (3307, 6), (1409, 7), (3307, 7)):
        row = by_key[key]
        print(
            "p", row["p"], "k", row["k"],
            "char", row["theta_character_upper"],
            "formal", row["theta_formal_upper"],
            "lift", row["lift_threshold_upper"],
        )


if __name__ == "__main__":
    main()
