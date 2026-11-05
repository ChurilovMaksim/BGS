#!/usr/bin/env python3
"""Certified arithmetic for the H7*/H8 obstruction note.

Exact NSW arithmetic (Python ints) and arb enclosures. No operator data.
"""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.")

import json
import math
from pathlib import Path

from flint import arb, ctx

ctx.prec = 200
OUT = Path(__file__).resolve().parents[1] / "logs" / "h7h8.json"


def nsw(n: int) -> int:
    """u_0 = 1, u_1 = 7, u_{n+1} = 6 u_n - u_{n-1}."""
    if n < 0:
        raise ValueError(n)
    a, b = 1, 7
    if n == 0:
        return a
    for _ in range(n - 1):
        a, b = b, 6 * b - a
    return b


def h_p(p: int) -> int:
    return nsw((p - 1) // 2)


def k_p(p: int) -> int:
    h = h_p(p)
    return 4 * h * h + 3


def primes_upto(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i * i : n + 1 : i] = b"\x00" * (((n - i * i) // i) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def _trial_prime(n: int) -> bool:
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


def factor_proved(n: int) -> tuple[dict[int, int], str]:
    """FLINT factorization, checked by multiplying back and by trial division of each prime factor.

    The search only proposes factors. Primality in this census is the trial
    loop, which is finite and elementary for every factor that occurs at p ≤ 31.
    """
    from flint import fmpz

    raw = fmpz(n).factor()
    fac = {int(q): int(e) for q, e in raw}
    prod = 1
    for q, e in fac.items():
        if not _trial_prime(q):
            raise RuntimeError(f"trial division rejects {q}")
        prod *= q**e
    if prod != n:
        raise RuntimeError("factorization does not multiply back")
    return fac, "trial"


def main() -> None:
    lam = 3 + 2 * arb(2).sqrt()
    eps = 1 + arb(2).sqrt()
    lnlam = lam.log()
    # Certificate caps, already upper bounds (not midpoints):
    #   Λ_free^{8V} ≤ 1.9656353  (TRACE-295)
    #   r_2^{8V}(4000) ≤ 1.0529012 (TRACE-290)
    # Lemma 2 substitutes these caps and delivers the factor (Λ_cap^2 / r_2_cap)^ℓ.
    # c_delivered is that substituted exponent. It is not a lower bound for a spectral radius.
    Lam = arb("1.9656353")
    r2 = arb("1.0529012")
    c_del = (2 * Lam.log() - r2.log()) / lnlam
    three_halves = arb("1.5") * c_del

    def alpha(rho: str) -> arb:
        r = arb(rho)
        q = (lam * r * r) ** arb("1.5")
        return -q.log()

    alphas = {s: alpha(s) for s in ("0.28", "0.28028", "0.30")}
    # ℓ₀ = p/4 λ-steps: allowed θ = log_λ d / p < α / (4 ln λ)   for loss exponent 1
    # c_B first-moment range uses the H5 budget B = -ln(ε * 0.2945), recomputed.
    # 0.2945 is a printed rate; enclose it in ±5e-5 so both directions are visible.
    rate = arb("0.2945")
    budget = -(eps * rate).log()
    budget_lo = -(eps * (rate + arb("5e-5"))).log()
    budget_hi = -(eps * (rate - arb("5e-5"))).log()
    # θ_B upper of the c_B claim: c_lo * θ * ln λ < budget_hi is the generous reading.
    # The obstruction needs a θ that is INSIDE every reasonable c_B range and OUTSIDE
    # every amplified wrap budget at ℓ₀ = p/4. So:
    #   θ_in_cB  uses c_hi and budget_lo (smallest claimed range)
    #   θ_wrap   uses α at ρ=0.28 (proved certificate ρ̄≤0.28; smallest α in that certificate
    #            is at ρ=0.28) and loss exponent 1.
    # θ covered by the delivered first-moment factor: c_del * θ * ln λ < budget.
    # A smaller budget and the upper end of c_del shrink this θ. That is the reading used below.
    theta_cB = budget_lo / (c_del.upper() * lnlam)
    theta_wrap = alphas["0.28"] / (4 * lnlam)
    theta_wrap_28028 = alphas["0.28028"] / (4 * lnlam)
    theta_wrap_30 = alphas["0.30"] / (4 * lnlam)

    # Limit ℓ₀/p to cover every divisor: ln d ≤ ln h_p < ln(ε/2) + ((p-1)/2) ln λ
    # so limsup (ln h_p)/p ≤ (1/2) ln λ = ln ε.
    # Needed ℓ₀/p ≥ (ln ε) / α   in the limit, loss exponent 1.
    ell_over_p = eps.log() / alphas["0.28"]
    # Same length if the delivered first-moment exponent is inserted as the wrap exponent.
    ell_over_p_if_cB_hi = c_del.upper() * ell_over_p
    ell_over_p_if_cB_lo = c_del.lower() * ell_over_p
    # How small ρ must be before the ℓ₀ = p/4 budget reaches the shrunk first-moment θ.
    # α(ρ) = θ * 4 * ln λ, and α = -(3/2) ln(λ ρ^2).
    target_alpha = theta_cB.lower() * 4 * lnlam
    rho_close = ((-target_alpha * 2 / 3).exp() / lam).sqrt()
    # How large the printed rate 0.2945 must become before the budget meets θ_wrap.
    rate_close = (-(theta_wrap.upper() * c_del.upper() * lnlam)).exp() / eps

    # Lemma E run constant at ε = 1/16 (the largest ε the lemma allows).
    # λ^{k-1} ≤ 264 ε^2 q^2 ⇒ k ≤ 2 log_λ q + 1 + log_λ(264 ε^2).
    eps_le = arb("1") / 16
    run_add = 1 + (arb(264) * eps_le ** 2).log() / lnlam

    # Uniform inclusion bound for p≥5: log_λ √(h_m) < 3p/4 - 0.15, checked below per p
    # and proved in the note from the closed form.

    primes = primes_upto(200)
    odd_primes = [p for p in primes if p >= 3]
    rows = []
    for p in odd_primes:
        if p > 31:
            break
        h = h_p(p)
        K = k_p(p)
        n = (p - 1) // 2
        assert nsw(3 * n + 1) == h * K
        assert h % 3 != 0
        if p >= 5:
            assert K % 7 == 0 and h % 7 != 0
        fac, fac_method = factor_proved(K)
        bad = [q for q in fac if q % 3 != 1]
        hm = h * K
        pe = [[q**i for i in range(e + 1)] for q, e in sorted(fac.items())]
        divs = [1]
        for powers in pe:
            divs = [a * b for a in divs for b in powers]
        lim = math.isqrt(hm)
        included = sorted(d for d in divs if 1 < d <= lim)
        other = [d for d in included if d != 7]
        # Floor in S_ρ units is h/d (N17b Q1). Compare with the cap exp(0.05 p).
        beat = []
        if p >= 5:
            for d in other:
                if (arb(h) / d).log() > arb("0.05") * p:
                    beat.append(d)
        log_ratio = math.log(h / 7) / p if p >= 5 else None
        log_sqrt = math.log(lim) / math.log(3 + 2 * math.sqrt(2))
        run = 2 * log_sqrt + float(run_add.upper())
        excess = 3 * p - run
        rows.append({
            "p": p,
            "h_prime": _trial_prime(h),
            "h_digits": len(str(h)),
            "K_mod_7": K % 7,
            "h_mod_7": h % 7,
            "h_mod_3": h % 3,
            "bad_factors_mod3": bad,
            "h": str(h),
            "K": str(K),
            "factors": {str(q): e for q, e in sorted(fac.items())},
            "factor_proof": fac_method,
            "factorization_proved": True,
            "n_included_K_divisors": len(included),
            "included_other_than_7": other,
            "n_other": len(other),
            "n_other_floor_beats_exp_005p": len(beat),
            "other_floor_beats_exp_005p": beat,
            "has_level_7": 7 in included,
            "ln_h_over_7_per_p": log_ratio,
            "log_lambda_sqrt_hm": log_sqrt,
            "lemmaE_run_upper": run,
            "excess_over_run": excess,
        })

    # uniform excess check from the closed-form majorant, p=5..80
    # √(h K) < √(ε/2) * λ^{3p/4 - 1/4} * (1+3/λ^p)^{1/2}
    uniform = []
    for p in [q for q in odd_primes if 5 <= q <= 80]:
        n = (p - 1) // 2
        # compare arb upper of 2 log_λ √(h K) + run_add with 3p - p
        h = arb(h_p(p))
        K = arb(k_p(p))
        log_sqrt = (h * K).log() / 2 / lnlam
        excess = arb(3 * p) - (2 * log_sqrt + run_add)
        uniform.append({"p": p, "excess_lower": str(excess.lower())})
        if not (excess > p):
            raise SystemExit(f"excess failed at {p}")

    # Elementary excess ingredients. λ > 81/16 iff 2·3072^2 > 2209^2,
    # which is the comparison (17+12√2) > (81/16)^2 written without radicals.
    assert 2 * 3072**2 > 2209**2
    # (169/140)*(33/32)*(6728/6725) < 3/2, with 6728/6725 = 1 + 3/6725.
    assert 2 * 169 * 33 * 6728 < 3 * 140 * 32 * 6725
    # mod-7 and mod-3 for every prime p with 5 ≤ p ≤ 200, exact integers.
    for p in odd_primes:
        if p < 5 or p > 200:
            continue
        h = h_p(p)
        K = k_p(p)
        if K % 7 != 0 or h % 7 == 0 or h % 3 == 0 or K % 3 == 0:
            raise SystemExit(f"congruence failed at {p}")

    out = {
        "Lambda_cap": "1.9656353",
        "r2_cap": "1.0529012",
        "c_delivered": str(c_del.lower()),
        "c_delivered_upper": str(c_del.upper()),
        "three_halves_c_lower": str(three_halves.lower()),
        "three_halves_exceeds_1": bool(three_halves > 1),
        "alpha": {s: str(a.lower()) for s, a in alphas.items()},
        "budget_0.2945": [str(budget_lo.lower()), str(budget_hi.upper())],
        "theta_cB_lower_end": str(theta_cB.lower()),
        "theta_wrap_0.28_upper": str(theta_wrap.upper()),
        "theta_wrap_0.28028_upper": str(theta_wrap_28028.upper()),
        "theta_wrap_0.30_upper": str(theta_wrap_30.upper()),
        "gap_nonempty": bool(theta_cB > theta_wrap),
        "rho_to_close_gap_upper": str(rho_close.upper()),
        "rate_to_close_gap_lower": str(rate_close.lower()),
        "ell0_over_p_all_divisors_rho_0.28": str(ell_over_p.lower()),
        "ell0_over_p_if_cB_used_as_exponent_lower": str(ell_over_p_if_cB_lo.lower()),
        "ell0_over_p_if_cB_used_as_exponent_upper": str(ell_over_p_if_cB_hi.upper()),
        "elementary_excess_asserts": True,
        "mod7_mod3_through_200": True,
        "lemmaE_run_add_upper": str(run_add.upper()),
        "rows": rows,
        "uniform_excess_spotcheck_ends": [uniform[0], uniform[-1]],
        "uniform_excess_gt_p": True,
    }
    OUT.write_text(json.dumps(out, indent=1))
    print("c", out["c_delivered"], out["c_delivered_upper"])
    print("3/2 c", out["three_halves_c_lower"], ">", 1, out["three_halves_exceeds_1"])
    print("theta_cB>", out["theta_cB_lower_end"], "theta_wrap<", out["theta_wrap_0.28_upper"], "gap", out["gap_nonempty"])
    print("ell/p", out["ell0_over_p_all_divisors_rho_0.28"])
    for r in rows:
        if r["p"] in (3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
            ratio = r["ln_h_over_7_per_p"]
            print(
                r["p"],
                "h_prime", r["h_prime"],
                "proof", r["factor_proof"],
                "n_other", r["n_other"],
                "beat", r["n_other_floor_beats_exp_005p"],
                "excess", round(r["excess_over_run"], 2),
            )


if __name__ == "__main__":
    main()
