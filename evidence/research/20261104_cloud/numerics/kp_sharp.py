"""Prop. K tail with the proved span bound, plus the uniform-norm obstruction.

Reproduces the N20 tail at ell <= 2j+g0 (regression), then replaces it by
ell <= j*theta + 3 + g0, theta = log_eps(2), and by the rational majorant
ell <= (4/5)*j + 3 + g0. Finite-part weights are the certified a_cert3
upper bounds; spans are the a_enum lengths, which span_exact.py matched
to the exact support on every class.

Crossover (gas versus Robin) is the V5 formula with additive budgets
idealised. It is conditional on H1 through A_bad^KP.
"""
from __future__ import annotations

import json
import math
import os

from flint import arb, ctx

ctx.prec = 200

ROOT = os.path.dirname(os.path.abspath(__file__))
LOGS = os.path.join(ROOT, "logs")
os.makedirs(LOGS, exist_ok=True)

ENUM = "/workspace/computations/verification/lineN14/logs/a_enum.jsonl"
CERT = "/workspace/computations/verification/lineN15/logs/a_cert3.jsonl"

DT = arb("5.0313e-6")
RE_LAM = arb("6.234e-4")
RHO = arb("0.28")
N_MAX = arb("2.91656")
G0 = 4
MODEL = {(1, 0), (0, 1), (2, 0), (0, 2)}


def load():
    span = {}
    zr = {}
    shell = {}
    for line in open(ENUM):
        r = json.loads(line)
        key = (int(r["a"]), int(r["b"]))
        span[key] = int(r["span"])
        zr[key] = int(r["zr"])
        shell[key] = int(r["j"])
    rows = []
    for line in open(CERT):
        r = json.loads(line)
        key = (int(r["a"]), int(r["b"]))
        rows.append((float(r["absw_up"]), span[key], shell[key], zr[key], key))
    return rows


def constants():
    lam = 3 + 2 * arb(2).sqrt()
    beta = 2 * (1 / RHO).log() / lam.log()
    # q = 2^{(3/2)(1-beta)}
    q = (arb(2).log() * arb("1.5") * (1 - beta)).exp()
    theta = arb(2).log() / (1 + arb(2).sqrt()).log()
    return lam, beta, q, theta


def fin(rows, J0, g0, a):
    s0 = arb(0)
    s1 = arb(0)
    n = 0
    aa = arb(a)
    for w, sp, j, z, ab in rows:
        if j > J0 or ab in MODEL or z >= g0:
            continue
        ell = sp + g0
        term = arb(w) * (aa * ell).exp()
        s0 += 2 * term
        s1 += 2 * term * ell
        n += 1
    # same inflation model as N20 tail_kp.py: <= 2e4 positive terms
    infl = 1 + arb("1e-9")
    return s0 * infl, s1 * infl, n


def tail(C, J0, g0, a, q, slope, add):
    """T0, T1 for ell <= slope*j + add + g0.

    slope=2, add=0 recovers N20. slope=theta, add=3 is the proved bound.
    """
    aa = arb(a)
    r = q * (aa * slope).exp()
    if not bool(r < 1):
        raise RuntimeError(f"tail ratio not < 1: {r}")
    J = J0 + 1
    # sum_{j>=J} r^j = r^J/(1-r)
    # sum_{j>=J} j r^j = r^J * (J - (J-1)*r) / (1-r)^2
    one = arb(1)
    g = (r ** J) / (one - r)
    gj = (r ** J) * (J - (J - 1) * r) / (one - r) ** 2
    pref = 2 * arb(C) ** arb("1.5") * (aa * (g0 + add)).exp()
    T0 = pref * g
    T1 = pref * (slope * gj + (add + g0) * g)
    return T0, T1, r


def solve(rows, C, J0, g0, q, slope, add):
    a = 1e-8
    for _ in range(80):
        s0, s1, n = fin(rows, J0, g0, a)
        T0, T1, r = tail(C, J0, g0, a, q, slope, add)
        need = s0 + T0 + (s1 + T1) / (1 + g0)
        a = float(need.upper()) * 1.001
    s0, s1, n = fin(rows, J0, g0, a)
    T0, T1, r = tail(C, J0, g0, a, q, slope, add)
    S0 = s0 + T0
    S1 = s1 + T1
    lhs = S0 + S1 / (1 + g0)
    budget = RE_LAM - S0 - DT
    return dict(
        C=C,
        J0=J0,
        slope=str(slope),
        add=add,
        n_finite=n,
        a_upper=a,
        S0fin_upper=float(s0.upper()),
        T0_upper=float(T0.upper()),
        T1_upper=float(T1.upper()),
        S0_upper=float(S0.upper()),
        KP_lhs_upper=float(lhs.upper()),
        KP_ok=bool(lhs < arb(a)),
        ratio_upper=float(r.upper()),
        budget_left_lower=float(budget.lower()),
        delta_eff_upper=float((DT + S0).upper()),
    )


def primes_upto(n):
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p * p :: p] = b"\x00" * len(sieve[p * p :: p])
    return [i for i in range(n + 1) if sieve[i]]


def h_nsw(p):
    """h_p along odd indices, copied from crossover_v5.py."""
    a, b = 1, 7
    for _ in range((p - 1) // 2 - 1):
        a, b = b, 6 * b - a
    return b


def crossover(delta_eff):
    """First prime where the idealised gas beats Robin. Float, as in V5, plus an arb check at that prime."""
    R = 6.234e-4
    dl = float(delta_eff)
    gam = 0.5772156649015329
    lne = math.log(1 + math.sqrt(2))
    lnb = math.log1p(R) - dl

    def G(p):
        x = math.exp(p * lnb)
        return (2 * x - 1) ** 2 - 1

    def robin(L):
        return math.exp(gam) * math.log(L) + 0.6483 / math.log(L) - 1

    def lnK(p):
        return math.log(4 * h_nsw(p) ** 2 + 3)

    def env(p):
        return robin((2 * p + 1) * lne)

    primes = [p for p in primes_upto(6000) if p >= 1000]
    first_int = next(p for p in range(1000, 6000) if G(p) > env(p))
    first_prime = next(p for p in primes if G(p) > robin(lnK(p)))
    viol = [p for p in primes if p >= first_prime and p <= 5000 and not (G(p) > robin(lnK(p)))]
    # arb confirmation of G(first_prime) > robin(ln K) is not attempted at full Robin;
    # record the float margin only.
    return dict(
        delta_eff=dl,
        first_int_envelope=first_int,
        first_prime_exact=first_prime,
        violations_to_5000=viol,
        G_at_prime=G(first_prime),
        robin_at_prime=robin(lnK(first_prime)),
        margin=G(first_prime) - robin(lnK(first_prime)),
    )


def obstruction(beta, theta):
    """Uniform step-norm majorant versus the H1 shell budget.

    One class of span <= floor(theta*j)+3, majorised by N_max^{2*span},
    compared with the whole shell budget C*2^{j(1-beta)} at C=0.082.
    """
    rows = []
    C = arb("0.082")
    first = None
    for j in range(1, 41):
        span_up = int(math.floor(float((theta * j).upper()))) + 3
        # span_up must dominate floor(theta*j)+3. If the ball is tight this is exact.
        majorant = N_MAX ** (2 * span_up)
        budget = C * (arb(2) ** (j * (1 - beta)))
        ratio = majorant / budget
        rec = dict(
            j=j,
            span_cap_used=span_up,
            log10_ratio_lower=float((ratio.log() / arb(10).log()).lower()),
        )
        rows.append(rec)
        if first is None and bool(ratio > 1):
            first = j
    return dict(N_max="2.91656", first_j_majorant_exceeds_shell_budget=first, rows=rows[::5])


def main():
    rows = load()
    lam, beta, q, theta = constants()
    print("beta", beta.str(20))
    print("q", q.str(20))
    print("theta", theta.str(20))
    cases = []
    # regression: N20 slope 2, add 0
    for C in (0.082, 0.04, 8.8e-4, 4.4e-4):
        cases.append(solve(rows, C, 12, G0, q, arb(2), 0))
        print("old", cases[-1], flush=True)
    # proved theta
    sharp = []
    for C in (0.082, 0.04, 8.8e-4, 4.4e-4):
        sharp.append(solve(rows, C, 12, G0, q, theta, 3))
        print("sharp", sharp[-1], flush=True)
    # rational 4/5
    rational = []
    for C in (0.082, 8.8e-4):
        rational.append(solve(rows, C, 12, G0, q, arb(4) / 5, 3))
        print("rat", rational[-1], flush=True)

    cross = {
        "old_C082": crossover(cases[0]["delta_eff_upper"]),
        "sharp_C082": crossover(sharp[0]["delta_eff_upper"]),
        "rat_C082": crossover(rational[0]["delta_eff_upper"]),
        "sharp_C88e4": crossover(sharp[2]["delta_eff_upper"]),
        "published_3.4962e-4": crossover(3.4962e-4),
        "published_7.4115e-6": crossover(7.4115e-6),
    }
    print(json.dumps(cross, indent=1))
    obs = obstruction(beta, theta)
    print("obstruction first j", obs["first_j_majorant_exceeds_shell_budget"])
    out = dict(
        beta=[float(beta.lower()), float(beta.upper())],
        q=[float(q.lower()), float(q.upper())],
        theta=[float(theta.lower()), float(theta.upper())],
        old_slope2=cases,
        sharp_theta=sharp,
        rational_4_5=rational,
        crossover=cross,
        obstruction=obs,
    )
    with open(os.path.join(LOGS, "kp_sharp.json"), "w") as f:
        json.dump(out, f, indent=1)


if __name__ == "__main__":
    main()
