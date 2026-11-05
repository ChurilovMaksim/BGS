#!/usr/bin/env python3
"""Cross-line and partial-isotropic masses inside H5(b) and H5(c).

Exact integers decide the coefficient comparisons. mpmath at 80 decimal
places encloses the idealised slack and the hypothetical divisor sums.
No registry file is written.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80
OUT = Path(__file__).resolve().parents[1] / "logs" / "h5_lines.json"

R = mp.mpf("6.234e-4")
DELTAS = ("3.4962e-4", "7.4115e-6")
THRESHOLDS = ((1409, "7.4115e-6"), (3307, "3.4962e-4"))


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
    if m <= a:
        return False
    return (m - a) ** 2 > 2 * b * b


def w_max_eps(p: int) -> int:
    a, b = lambda_pow(p)
    w = 0
    fact = 1
    prod = 1
    base = p - 1
    while True:
        w1 = w + 1
        fact *= w1
        prod *= base
        if exceeds_lambda(prod * fact * prod * fact, a, b):
            return w
        w = w1


def primes_up_to(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            step = i
            start = i * i
            sieve[start : n + 1 : step] = b"\x00" * (((n - start) // step) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def smallest_allowed_primes(p: int, h: int) -> list[int]:
    """Smallest primes ≡ ±1 (mod 2p) whose product is still ≤ h.

    The search stops at the first allowed prime that would push the product
    over h. Any later prime is larger, so no further prime can be added, and
    no set of greater cardinality has product ≤ h.
    """
    allowed: list[int] = []
    prod = 1
    limit = 1000
    while True:
        hit_barrier = False
        for q in primes_up_to(limit):
            if q <= (allowed[-1] if allowed else 1):
                continue
            if q % (2 * p) in (1, 2 * p - 1):
                if prod * q > h:
                    hit_barrier = True
                    break
                prod *= q
                allowed.append(q)
        if hit_barrier:
            break
        if limit > 50 * p * p:
            raise RuntimeError(f"sieve limit exceeded for p={p}")
        limit *= 4
    if not allowed:
        raise RuntimeError(f"no allowed prime for p={p}")
    return allowed


def gas_slot(p: int, delta_str: str, h: int) -> dict:
    delta = mp.mpf(delta_str)
    lnb = mp.log1p(R) - delta
    M = 2 * mp.e ** (p * lnb) - 1
    K = 4 * h * h + 3
    L = mp.log(K)
    robin = mp.e ** mp.euler * mp.log(L) + mp.mpf("0.6483") / mp.log(L) - 1
    need = mp.sqrt(1 + robin)
    tail = mp.e ** (-mp.mpf("0.28") * p)
    slack = M - need - tail
    return {
        "M": M,
        "robin": robin,
        "need": need,
        "tail": tail,
        "slack": slack,
    }


def divisor_sum_bound(primes: list[int], gamma: mp.mpf) -> mp.mpf:
    """2 (∏(1 + q^{-γ}) - 1), an upper bound for Σ min(d, h/d)^{-γ}."""
    acc = mp.mpf(0)
    for q in primes:
        acc += mp.log1p(mp.power(q, -gamma))
    return 2 * (mp.e**acc - 1)


def lemma_w_floors(p: int, w: int) -> list[int]:
    """q_j ≥ max(2p−1, (p−1) j). These integers need not be prime."""
    return [max(2 * p - 1, (p - 1) * j) for j in range(1, w + 1)]


def progression_floors(p: int, w: int) -> list[int]:
    """The first w integers ≥ 2p−1 that are ≡ ±1 (mod 2p).

    The j-th prime in those two classes is at least this integer.
    """
    out = []
    for j in range(1, w + 1):
        m = (j + 1) // 2
        out.append(2 * m * p - 1 if j % 2 else 2 * m * p + 1)
    return out


def sum_min_inverse(values: list[int]) -> Fraction:
    """2 (∏(1 + 1/v) − 1), exact, for the γ = 1 divisor sum."""
    acc = Fraction(1)
    for v in values:
        acc *= Fraction(v + 1, v)
    return 2 * (acc - 1)


def fit_gamma(primes: list[int], budget: mp.mpf) -> str | None:
    """Smallest γ in [0, 2] with the divisor-sum bound ≤ budget, or None."""
    if budget <= 0:
        return None
    if divisor_sum_bound(primes, mp.mpf(2)) > budget:
        return None
    lo, hi = mp.mpf(0), mp.mpf(2)
    for _ in range(80):
        mid = (lo + hi) / 2
        if divisor_sum_bound(primes, mid) <= budget:
            hi = mid
        else:
            lo = mid
    return str(hi)


def cosine_sum_lower_ok(q: int) -> dict:
    """Σ_{k=1}^{q-1} 2|cos(π k/q)| against 4(q-7)/7."""
    s = mp.mpf(0)
    for k in range(1, q):
        s += 2 * mp.fabs(mp.cos(mp.pi * k / q))
    bound = mp.mpf(4 * (q - 7)) / 7
    return {
        "q": q,
        "sum_abs_kappa": str(s),
        "rational_lower_4_over_7": str(bound),
        "sum_exceeds_lower": bool(s > bound),
    }


def main() -> None:
    assert h_nsw(3) == 7
    assert h_nsw(5) == 41
    assert h_nsw(11) == 23 * 353
    assert h_nsw(1409) > 10**539
    assert h_nsw(3307) > 10**1265
    assert w_max_eps(1409) == 112
    assert w_max_eps(3307) == 231
    assert 12 * 12 < 3 * 7 * 7  # (12/7)^2 < 3, so 12/7 < √3
    assert 64 * 3 > 161  # 64/161 > 1/3
    assert 64 * 5 < 2 * 161  # 64/161 < 2/5
    assert 112 * 25 < 2817  # w_max(1409)/(2*1409-1) < 1/25, checked after w_max
    # λ^4 = 577 + 408√2 > 1000, used for the 4.12 constant.
    assert (577 - 1000) ** 2 < 2 * 408 * 408

    rows = []
    for p, delta in list(THRESHOLDS) + [(1409, "3.4962e-4"), (3307, "7.4115e-6")]:
        h = h_nsw(p)
        w = w_max_eps(p)
        allowed = smallest_allowed_primes(p, h)
        slot = gas_slot(p, delta, h)
        gammas = {}
        for g_str in ("1", "1/2", "1/4", "1/10"):
            g = mp.mpf(g_str)
            upper = divisor_sum_bound(allowed, g)
            gammas[g_str] = {
                "sum_upper": str(upper),
                "M_times_sum": str(slot["M"] * upper),
                "sum_under_slack": bool(upper < slot["slack"]) if slot["slack"] > 0 else False,
                "M_times_sum_under_slack": bool(slot["M"] * upper < slot["slack"])
                if slot["slack"] > 0
                else False,
            }
        # Largest γ in [0, 2] is not the question; smallest γ whose sum fits.
        lo, hi = mp.mpf(0), mp.mpf(2)
        if slot["slack"] > 0:
            for _ in range(60):
                mid = (lo + hi) / 2
                if divisor_sum_bound(allowed, mid) <= slot["slack"]:
                    hi = mid
                else:
                    lo = mid
        point_factor = 1 - mp.mpf(w) / (2 * p - 1)
        log10_h = mp.log10(h)
        log10_need = mp.log10(slot["slack"]) - mp.log10(point_factor * h) if slot["slack"] > 0 else None
        floors = lemma_w_floors(p, w)
        prog = progression_floors(p, w)
        crude = divisor_sum_bound(floors, mp.mpf(1))
        prog_sum = divisor_sum_bound(prog, mp.mpf(1))
        exact_sharp = sum_min_inverse(allowed)
        exact_crude = sum_min_inverse(floors)
        exact_prog = sum_min_inverse(prog)
        prod = 1
        for q in allowed:
            prod *= q
        rows.append(
            {
                "p": p,
                "delta": delta,
                "h_p": str(h),
                "log10_h": str(log10_h),
                "w_max": w,
                "n_allowed_primes_product_le_h": len(allowed),
                "least_allowed": allowed[0],
                "allowed_head": allowed[:8],
                "allowed_tail": allowed[-3:],
                "product_of_allowed_le_h": prod <= h,
                "log10_product_allowed": str(mp.log10(prod)),
                "point_count_over_h_lower": str(point_factor),
                "M": str(slot["M"]),
                "slack_after_tail": str(slot["slack"]),
                "gammas": gammas,
                "gamma_abs_fit": str(hi) if slot["slack"] > 0 else None,
                "gamma_times_M_fit": fit_gamma(allowed, slot["slack"] / slot["M"])
                if slot["slack"] > 0
                else None,
                "crude_floor_sum_gamma_1": str(crude),
                "progression_sum_gamma_1": str(prog_sum),
                "exact_sharp_lt_slack": bool(mp.mpf(exact_sharp) < slot["slack"]) if slot["slack"] > 0 else False,
                "exact_crude_lt_slack": bool(mp.mpf(exact_crude) < slot["slack"]) if slot["slack"] > 0 else False,
                "exact_prog_lt_slack": bool(mp.mpf(exact_prog) < slot["slack"]) if slot["slack"] > 0 else False,
                "exact_sharp_decimal": str(mp.mpf(exact_sharp)),
                "exact_prog_decimal": str(mp.mpf(exact_prog)),
                "crude_under_slack": bool(crude < slot["slack"]) if slot["slack"] > 0 else False,
                "prog_under_slack": bool(prog_sum < slot["slack"]) if slot["slack"] > 0 else False,
                "crude_M_under_slack": bool(slot["M"] * crude < slot["slack"]) if slot["slack"] > 0 else False,
                "prog_M_under_slack": bool(slot["M"] * prog_sum < slot["slack"]) if slot["slack"] > 0 else False,
                "log10_max_r_for_triangle": str(log10_need) if log10_need is not None else None,
                "l1_over_slack_lower": str((mp.mpf(64) / 161) * h / slot["slack"])
                if slot["slack"] > 0
                else None,
            }
        )

# w < p/ln(p-1) is Theorem 1 of proofs/h5_factor.md. Each progression
    # integer is a lower bound for the corresponding prime, so the sum
    # majorises every admissible γ=1 sum at that omega cap.
    def progression_sum(p: int, w: int) -> mp.mpf:
        acc = mp.mpf(0)
        for j in range(1, w + 1):
            m = (j + 1) // 2
            v = 2 * m * p - 1 if j % 2 else 2 * m * p + 1
            acc += mp.log1p(1 / mp.mpf(v))
        return 2 * (mp.e**acc - 1)

    uniform = []
    for p in (1409, 3307, 4000, 4600, 6000, 10000, 20000):
        w_hi = int(mp.floor(p / mp.log(p - 1)))
        crude_w = progression_sum(p, w_hi)
        harmonic_exp = 2 * (mp.e ** ((1 + mp.log(p / mp.log(p - 1))) / p) - 1)
        uniform.append(
            {
                "p": p,
                "w_hi": w_hi,
                "progression_sum": str(crude_w),
                "harmonic_exp_majorant": str(harmonic_exp),
                "under_0_02011297": bool(crude_w < mp.mpf("0.02011297")),
                "under_0_00334719": bool(crude_w < mp.mpf("0.00334719")),
                "harmonic_exp_under_0_02011297": bool(harmonic_exp < mp.mpf("0.02011297")),
                "harmonic_exp_under_0_00334719": bool(harmonic_exp < mp.mpf("0.00334719")),
            }
        )
    # Every integer from 3307 through 4599, at 20 decimals. The sum is not
    # monotone in p. The recorded maximum and the last exceedance of the
    # fragile cap are what the uniform statement uses.
    scan_max = mp.mpf(0)
    scan_at = 3307
    scan_max_after = mp.mpf(0)
    scan_at_after = 3566
    increases = 0
    last_over = None
    previous = None
    cap_fragile = mp.mpf("0.00334719")
    with mp.workdps(20):
        for p in range(3307, 4600):
            w_hi = int(mp.floor(p / mp.log(p - 1)))
            s = progression_sum(p, w_hi)
            if previous is not None and s > previous:
                increases += 1
            previous = s
            if s > scan_max:
                scan_max = s
                scan_at = p
            if p >= 3566 and s > scan_max_after:
                scan_max_after = s
                scan_at_after = p
            if s >= cap_fragile:
                last_over = p
        scan_max_s = str(scan_max)
        scan_at_p = scan_at
        scan_after_s = str(scan_max_after)
        scan_after_p = scan_at_after
        scan_increases = increases
        scan_last_over = last_over
        scan_ok = last_over is None or last_over < 3566
    boundary = []
    with mp.workdps(50):
        for p in (3565, 3566, 3567, 3568):
            w_hi = int(mp.floor(p / mp.log(p - 1)))
            s = progression_sum(p, w_hi)
            boundary.append(
                {
                    "p": p,
                    "w_hi": w_hi,
                    "sum": str(s),
                    "gap_to_0_00334719": str(cap_fragile - s),
                }
            )

    # p = 11 exact shape: one mixed class, semiprime 23 * 353.
    q, Q = 23, 353
    h11 = q * Q
    cos = cosine_sum_lower_ok(q)
    # True ℓ1 for iso at Q, unit at q: N_iso(Q) * (q-1)/(q-2) * Σ|κ|.
    sum_kappa = mp.mpf(cos["sum_abs_kappa"])
    l1 = (2 * (Q - 1)) * (mp.mpf(q - 1) / (q - 2)) * sum_kappa
    rational = mp.mpf(64) / 161 * h11
    checks = {
        "sqrt3_lower_12_over_7": True,
        "lambda4_gt_1000": True,
        "h11": h11,
        "cosine_q23": cos,
        "l1_mixed_iso_at_353": str(l1),
        "rational_lower_64_161_h": str(rational),
        "l1_exceeds_rational_lower": bool(l1 > rational),
        "cross_line_point_count_p11": (q - 1) * (Q - 1),
        "w_max_1409": w_max_eps(1409),
        "w_max_3307": w_max_eps(3307),
        "h_1409_gt_10_539": h_nsw(1409) > 10**539,
        "h_3307_gt_10_1265": h_nsw(3307) > 10**1265,
        "112_over_2817_lt_1_25": 112 * 25 < 2817,
        "231_over_6613_lt_1_28": 231 * 28 < 6613,
        "64_161_lt_2_5": True,
    }
    payload = {
        "rows": rows,
        "checks": checks,
        "uniform_crude": uniform,
        "scan_3307_4599": {
            "max_progression_sum": scan_max_s,
            "at_p": scan_at_p,
            "increases": scan_increases,
            "last_p_at_or_above_0_00334719": scan_last_over,
            "every_p_from_3566_under_cap": scan_ok,
            "max_from_3566": scan_after_s,
            "max_from_3566_at_p": scan_after_p,
            "boundary_dps50": boundary,
        },
    }
    OUT.write_text(json.dumps(payload, indent=1) + "\n")
    print(json.dumps({"out": str(OUT), "w1409": checks["w_max_1409"], "w3307": checks["w_max_3307"]}, indent=1))


if __name__ == "__main__":
    main()
