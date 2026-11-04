#!/usr/bin/env python3
"""Prop. K tail with the proved span law, in arb.

Inputs taken from the registered record (not re-derived):
  rho_bar = 0.28, Re Lambda_lo' = 6.234e-4, delta_true <= 5.0313e-6,
  unweighted finite activity W0 = 2.03157e-6  (N15 / TRACE-321, j<=12, g0=4, core functional).

Span law (proved here): for a shell-j class, span < kappa*j + 3,
  kappa = ln2/ln(eps). Cluster length ell = span + g0 < kappa*j + 3 + g0.
The v5 tail used ell <= 2*j + g0.

Both tails are evaluated with the same finite-part majorant
  S0_fin(a) <= W0 * exp(a*ell_max), ell_max = kappa*12 + 3 + g0,
  S1_fin <= ell_max * S0_fin,
so the comparison is internal. Absolute a may sit slightly above the published
fixed point because ell_max majorises the true finite spans.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

from flint import arb, ctx

ctx.prec = 300
OUT = Path(__file__).resolve().parents[1] / "logs" / "propk_sharp.json"

rho = arb("0.28")
lam = 3 + 2 * arb(2).sqrt()
eps = 1 + arb(2).sqrt()
kappa = arb(2).log() / eps.log()
beta = 2 * (-rho.log()) / lam.log()
q = (arb(2).log() * arb("1.5") * (1 - beta)).exp()
Rlam = arb("6.234e-4")
DT = arb("5.0313e-6")
W0 = arb("2.03157e-6")  # cited upper bound, core functional, j<=12, g0=4
G0 = 4
J0 = 12
ELL_FIN = kappa * J0 + 3 + G0  # strict span bound; using <= is valid


def geo_sum(r, J):
    """sum_{j>=J} r^j and sum_{j>=J} j r^j, r<1."""
    rj = r ** J
    one = 1 - r
    s = rj / one
    sj = rj * (J - (J - 1) * r) / (one ** 2)
    return s, sj


def tails(C, a, mode):
    """Return (T0, T1) upper enclosures."""
    C = arb(C)
    a = arb(a)
    pref_C = 2 * C ** arb("1.5")
    if mode == "v5_2j":
        # ell <= 2j + g0
        r = q * (2 * a).exp()
        pref = pref_C * (a * G0).exp()
        s, sj = geo_sum(r, J0 + 1)
        T0 = pref * s
        T1 = pref * (2 * sj + G0 * s)
        return T0, T1, r
    if mode == "sharp":
        # ell < kappa*j + 3 + g0
        r = q * (kappa * a).exp()
        pref = pref_C * (a * (3 + G0)).exp()
        s, sj = geo_sum(r, J0 + 1)
        T0 = pref * s
        T1 = pref * (kappa * sj + (3 + G0) * s)
        return T0, T1, r
    raise ValueError(mode)


def finite(a):
    a = arb(a)
    s0 = W0 * (a * ELL_FIN).exp()
    s1 = ELL_FIN * s0
    return s0, s1


def kp_lhs(C, a, mode):
    s0f, s1f = finite(a)
    t0, t1, r = tails(C, a, mode)
    S0 = s0f + t0
    S1 = s1f + t1
    lhs = S0 + S1 / (1 + G0)
    return lhs, S0, S1, t0, t1, r


def solve(C, mode):
    # fixed-point iteration on upper endpoints, inflated 1+1e-9 each step
    a = arb("1e-8")
    for _ in range(80):
        lhs, *_ = kp_lhs(C, a, mode)
        a = arb(lhs.upper()) * (1 + arb("1e-9"))
        if a > arb("0.1"):
            break
    lhs, S0, S1, t0, t1, r = kp_lhs(C, a, mode)
    budget = Rlam - S0 - DT
    return {
        "mode": mode,
        "C": C,
        "a_upper": str(a.upper()),
        "lhs_upper": str(lhs.upper()),
        "kp_ok": bool(lhs < a),
        "S0_upper": str(S0.upper()),
        "T0_upper": str(t0.upper()),
        "T1_upper": str(t1.upper()),
        "r_upper": str(r.upper()),
        "budget_lower": str(budget.lower()),
        "budget_positive": bool(budget > 0),
    }


def main():
    cases = []
    for C in ("0.082", "0.04", "0.00088", "0.00044"):
        for mode in ("v5_2j", "sharp"):
            row = solve(C, mode)
            cases.append(row)
            print(mode, C, "a", row["a_upper"], "S0", row["S0_upper"], "budget", row["budget_lower"], "ok", row["kp_ok"])
    # relative tail drop at the published a values (fixed a, not the fixed point)
    published_a = {"0.082": "2.6925e-3", "0.04": "8.6596e-4", "0.00088": "8.2498e-6", "0.00044": "6.4867e-6"}
    at_published = []
    for C, a in published_a.items():
        _, _, _, t_old, _, _ = kp_lhs(C, a, "v5_2j")
        _, S0n, _, t_new, _, _ = kp_lhs(C, a, "sharp")
        # S0 using cited finite + new tail, at the published a
        s0f, _ = finite(a)
        S0 = s0f + t_new
        at_published.append({
            "C": C,
            "a": a,
            "T0_v5_upper": str(t_old.upper()),
            "T0_sharp_upper": str(t_new.upper()),
            "T0_ratio_upper": str((t_new / t_old).upper()),
            "S0_sharp_upper": str(S0.upper()),
            "delta_eff_upper": str((S0 + DT).upper()),
        })
        print("published", C, "ratio", at_published[-1]["T0_ratio_upper"], "deff", at_published[-1]["delta_eff_upper"])
    meta = {
        "kappa": [str(kappa.lower()), str(kappa.upper())],
        "beta": [str(beta.lower()), str(beta.upper())],
        "q": [str(q.lower()), str(q.upper())],
        "ell_fin_upper": str(ELL_FIN.upper()),
        "note": "S0_fin uses W0*exp(a*ell_fin), a valid majorant of the registered unweighted finite activity, not a recomputation of a_cert3.",
    }
    OUT.write_text(json.dumps({"meta": meta, "fixed_points": cases, "at_published_a": at_published}, indent=1))


if __name__ == "__main__":
    main()
