#!/usr/bin/env python3
"""Factorisation room left by Lemma W (BGS-TRACE-342) inside H5.

Exact integer arithmetic decides w_max and the comparison of 2^{w_max}
with the gas main term. mpmath at 80 decimal places, the same inputs as
crossover_sharp.py, encloses the additive slack in B_p. No registry file
is written.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80
OUT = Path(__file__).resolve().parents[1] / "logs" / "h5_factor.json"

R = mp.mpf("6.234e-4")
R_FRAC = Fraction(6234, 10**7)
DELTAS = ("3.4962e-4", "7.4115e-6")
PRIMES = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 1409, 3307]


def lambda_pow(n: int) -> tuple[int, int]:
    """(3+2√2)^n = a + b√2."""
    a, b = 1, 0
    for _ in range(n):
        a, b = 3 * a + 4 * b, 2 * a + 3 * b
    return a, b


def h_nsw(p: int) -> int:
    a, b = 1, 7
    for _ in range((p - 1) // 2 - 1):
        a, b = b, 6 * b - a
    return b


def exceeds_lambda(m: int, a: int, b: int) -> bool:
    """True when the positive integer m is strictly larger than a + b√2."""
    if m <= a:
        return False
    return (m - a) ** 2 > 2 * b * b


def w_max_eps(p: int) -> int:
    """max{w : (p-1)^w w! ≤ ε^p}, ε = 1+√2. Registry definition."""
    a, b = lambda_pow(p)
    w = 0
    fact = 1
    base = p - 1
    prod = 1
    while True:
        w1 = w + 1
        fact *= w1
        prod *= base
        m = prod * fact
        if exceeds_lambda(m * m, a, b):
            return w
        w = w1
        if w > p:
            raise RuntimeError("w_max exceeded p")


def w_sharp(p: int) -> int:
    """max{w : (p-1)^w w! ≤ h_p}. The product in the proof of Lemma W."""
    h = h_nsw(p)
    w = 0
    fact = 1
    prod = 1
    base = p - 1
    while True:
        w1 = w + 1
        fact *= w1
        prod *= base
        if prod * fact > h:
            return w
        w = w1


def crude_cap(p: int) -> int:
    """max{w : (p-1)^w ≤ ε^p}. Drops the w! and still bounds ω."""
    a, b = lambda_pow(p)
    w = 0
    prod = 1
    base = p - 1
    while True:
        nxt = prod * base
        if exceeds_lambda(nxt * nxt, a, b):
            return w
        prod = nxt
        w += 1


def exp_upper(z: Fraction, nterms: int) -> Fraction:
    """Strict upper bound of exp(z) by the Taylor series with a geometric tail."""
    if z <= 0:
        raise ValueError("z must be positive")
    term = Fraction(1)
    total = Fraction(1)
    for k in range(1, nterms + 1):
        term *= z / k
        total += term
    # tail < term * z/(nterms+1) / (1 - z/(nterms+1))
    ratio = z / (nterms + 1)
    if ratio >= 1:
        raise ValueError("tail ratio")
    total += term * ratio / (1 - ratio)
    return total


def rational_main_term(p: int) -> dict:
    """2^{w} against 2(1+R)^p, with R = 6.234e-4 and exp bounded by rationals."""
    w = w_max_eps(p)
    z = R_FRAC * p
    upper = exp_upper(z, 40)
    # (1+R)^p < exp(p R) < upper, and the gas factor b^p < (1+R)^p.
    two_b = 2 * upper
    return {
        "p": p,
        "w_max": w,
        "two_exp_upper_lt_int": 5 if p == 1409 else 16,
        "two_exp_upper_float": float(two_b),
        "two_to_w_exceeds_2_exp_pR": (1 << w) > two_b,
        "two_exp_upper_below_display_int": two_b < (5 if p == 1409 else 16),
    }


def factor_small(limit: int = 47) -> list[dict]:
    """Complete factorisation of h_p by trial division, for small p."""
    rows = []
    for p in PRIMES:
        if p > limit:
            continue
        n0 = h_nsw(p)
        n = n0
        fac: list[list[int]] = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                e = 0
                while n % d == 0:
                    n //= d
                    e += 1
                fac.append([d, e])
            d += 1 if d == 2 else 2
        if n > 1:
            fac.append([n, 1])
        omega = len(fac)
        squarefree = all(e == 1 for _, e in fac)
        primes = [q for q, _ in fac]
        # largest proper divisor
        if omega == 1 and fac[0][1] == 1:
            proper = 1
            prime_h = True
        else:
            prime_h = False
            # h / smallest prime factor
            proper = n0 // primes[0]
        lam = mp.mpf(3) + 2 * mp.sqrt(2)
        theta_proper = mp.log(proper) / mp.log(lam) / p if proper > 1 else mp.mpf(0)
        theta_h = mp.log(n0) / mp.log(lam) / p
        rows.append(
            {
                "p": p,
                "h_p": str(n0),
                "factors": fac,
                "omega": omega,
                "squarefree": squarefree,
                "prime": prime_h,
                "q_min": primes[0],
                "q_min_mod_2p": primes[0] % (2 * p),
                "largest_proper_divisor": str(proper),
                "theta_proper": str(theta_proper),
                "theta_h": str(theta_h),
                "proper_below_0.262": bool(theta_proper < mp.mpf("0.262")),
            }
        )
    return rows


def gas_row(p: int, delta_str: str) -> dict:
    delta = mp.mpf(delta_str)
    lnb = mp.log1p(R) - delta
    x = mp.e ** (p * lnb)
    M = 2 * x - 1
    K = 4 * h_nsw(p) ** 2 + 3
    L = mp.log(K)
    robin = mp.e ** mp.euler * mp.log(L) + mp.mpf("0.6483") / mp.log(L) - 1
    G = M**2 - 1
    # Room for |X_cross|+|Y|+|X_tail|+e^{-0.28 p} before (inside)^2 - 1 = robin,
    # at n/h_p = 1. Other epsilons are left at 0, as in the idealised crossover.
    need = mp.sqrt(1 + robin)
    slack = M - need
    tail = mp.e ** (-mp.mpf("0.28") * p)
    slack_after_tail = slack - tail
    w = w_max_eps(p)
    ws = w_sharp(p)
    cap = crude_cap(p)
    return {
        "p": p,
        "delta": delta_str,
        "rate": str(lnb),
        "M": str(M),
        "robin": str(robin),
        "G_minus_robin": str(G - robin),
        "slack_before_tail": str(slack),
        "e_minus_0.28p": str(tail),
        "slack_after_tail": str(slack_after_tail),
        "w_max": w,
        "w_sharp": ws,
        "crude_cap": cap,
        "log2_slack_after_tail": str(mp.log(slack_after_tail) / mp.log(2))
        if slack_after_tail > 0
        else None,
        "w_max_ln2": str(w * mp.log(2)),
        "ln_M": str(mp.log(M)),
        "count_exceeds_M": bool(w * mp.log(2) > mp.log(M)),
    }


def balanced_gap(p: int) -> dict:
    """h_p / (2p-1) against (397/250)^p = 1.588^p, by exact integers."""
    h = h_nsw(p)
    base_num, base_den = 397, 250
    # Compare h * 250^p  ?  (2p-1) * 397^p
    left = h * pow(base_den, p)
    right = (2 * p - 1) * pow(base_num, p)
    lam = mp.mpf(3) + 2 * mp.sqrt(2)
    # theta of the cofactor h_p/(2p-1)
    theta = mp.log(mp.mpf(h) / (2 * p - 1)) / mp.log(lam) / p
    return {
        "p": p,
        "h_over_2p_minus_1_exceeds_1.588_to_p": left > right,
        "log10_ratio": str(mp.log10(mp.mpf(left) / right)),
        "theta_of_cofactor_at_qmin_2p_minus_1": str(theta),
        "lemmaW_qmin_lower": 2 * p - 1,
    }


def uniform_constants() -> dict:
    """Rational checks for w_max(n) > (1+R)^n on 2000 ≤ n ≤ exp(170)."""
    ln2_lower = Fraction(693, 1000)
    e_bound = exp_upper(Fraction(693, 1000), 30)
    # At ln n = 170 the coefficient ln2/(6*170) is the smallest on the interval.
    # f(n) = ln2/(6 ln n) - 2 ln2/n is decreasing for n ≥ 2000, since
    # n > 12 (ln n)^2 there, and its minimum on n ≤ exp(170) is essentially
    # ln2/1020. The comparison below uses 693/1000 < ln 2.
    left = ln2_lower / (6 * 170) - R_FRAC
    # ln 2 < 7/10 because the partial sum of exp(7/10) already exceeds 2.
    z = Fraction(7, 10)
    term = Fraction(1)
    lower_e = Fraction(1)
    for k in range(1, 20):
        term *= z / k
        lower_e += term
    e_lower_11 = (Fraction(8, 3)) ** 11
    tiny = 2 * Fraction(7, 10) / e_lower_11
    return {
        "exp_693_1000_upper_lt_2": bool(e_bound < 2),
        "exp_7_10_partial_gt_2": bool(lower_e > 2),
        "forty_squared_lt_2_29_squared": 40**2 < 2 * 29**2,
        "e_series_gt_8_over_3": Fraction(163, 60) > Fraction(8, 3),
        "eight_thirds_pow_11": str(e_lower_11.numerator),
        "endpoint_margin_positive": bool(left > tiny),
        "endpoint_margin": f"{(left - tiny).numerator}/{(left - tiny).denominator}",
    }


def main() -> None:
    factor_rows = factor_small(47)
    # The trial loop is the elementary one. Confirm h_31.
    gas = [gas_row(p, d) for d in DELTAS for p in (1409, 3307)]
    rational = [rational_main_term(p) for p in (1409, 3307)]
    # Drop the unused None field's bulk by replacing the fraction string only.
    for row in rational:
        row.pop("exp_pR_upper", None)
    caps = []
    for p in PRIMES:
        caps.append(
            {
                "p": p,
                "w_max": w_max_eps(p),
                "w_sharp": w_sharp(p),
                "crude_cap": crude_cap(p),
                "h_digits": len(str(h_nsw(p))),
            }
        )
    balanced = [balanced_gap(p) for p in (31, 1409, 3307)]
    constants = uniform_constants()
    if not (
        constants["exp_693_1000_upper_lt_2"]
        and constants["endpoint_margin_positive"]
        and int(constants["eight_thirds_pow_11"]) > 40000
        and constants["forty_squared_lt_2_29_squared"]
        and constants["e_series_gt_8_over_3"]
        and constants["exp_7_10_partial_gt_2"]
    ):
        raise SystemExit("uniform rational checks failed")
    # Spot-check the lower bound at the two conditional primes and at 2000.
    spots = []
    for n in (1409, 2000, 3307):
        # s with e^{s-1} < n ≤ e^s, using mpmath only to name s; the
        # inequality w_max ≥ floor(n/(3s)) is then an exact integer fact.
        s = int(mp.ceil(mp.log(n)))
        w = n // (3 * s)
        spots.append(
            {
                "n": n,
                "s_ceil_ln": s,
                "floor_n_over_3s": w,
                "w_max": w_max_eps(n),
                "w_max_ge_floor": w_max_eps(n) >= w,
            }
        )
    out = {
        "dps": 80,
        "R": "6.234e-4",
        "caps": caps,
        "factors_p_le_47": factor_rows,
        "gas": gas,
        "rational_main_term": rational,
        "balanced": balanced,
        "uniform_constants": constants,
        "lower_bound_spots": spots,
        "claims": {
            "H5_replaced": False,
            "omega_bound_is_lemma_W": True,
            "count_fits_in_Bp": False,
            "positive_density_proved": False,
        },
    }
    OUT.write_text(json.dumps(out, indent=2) + "\n")
    print("wrote", OUT)
    for row in caps:
        print("cap", row)
    for row in factor_rows:
        print(
            "fac",
            row["p"],
            row["factors"],
            "prime" if row["prime"] else "composite",
            "theta_proper",
            row["theta_proper"],
        )
    for row in gas:
        print(
            "gas",
            row["p"],
            row["delta"],
            "slack",
            row["slack_after_tail"],
            "w_max",
            row["w_max"],
            "exceeds",
            row["count_exceeds_M"],
        )
    for row in rational:
        print("rat", row["p"], row["w_max"], row["two_exp_upper_float"], row["two_to_w_exceeds_2_exp_pR"])
    for row in balanced:
        print("bal", row["p"], row["h_over_2p_minus_1_exceeds_1.588_to_p"], row["log10_ratio"])
    print(
        "constants",
        constants["exp_693_1000_upper_lt_2"],
        constants["endpoint_margin_positive"],
        int(constants["eight_thirds_pow_11"]) > 40000,
    )
    print("spots", spots)


if __name__ == "__main__":
    main()
