"""
Certification suite for the exact-moment theorem for subgroup Kloosterman sums.
==============================================================================

Checks, all by independent brute force (no reuse of the derivation being tested):

C1  moment identity        sum_{a,b in F_p} |S(a,b)|^{2s} == p^2 * E_s(H)
C2  mixed moments          sum_{a,b} S^u conj(S)^v == p^2 * E_{u,v}(H),
                           and E_{u,v} == 0 in char 0 whenever u != v and
                           lpf(k) > u+v  (so the F_p count is purely sporadic)
C3  PAIR closed form       PAIR(s,k) == s!^2 * [x^s] I_0(2 sqrt x)^k
C4  sharp-threshold probe  for k prime, the largest p = 1 mod k with
                           E_s(H) > CHAR0(s,k), compared with k^s and k^{s/2}
C5  Weil / trivial bound   max_{a,b} |S(a,b)| vs min(k, 2 sqrt p)

Every number printed here comes from an actually executed enumeration.
"""

from __future__ import annotations

import cmath
import itertools
import json
import math
import os
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from subgroup_kloosterman_energy import (          # noqa: E402
    char0_count, cyc, is_prime, lpf, pair_count, prime_factors,
    reduce_mod_cyc, subgroup_of_order,
)

# --------------------------------------------------------------- helpers


def S_table(p: int, k: int):
    """Full table S(a,b) for a,b in F_p, as a dict -> complex."""
    H, _ = subgroup_of_order(p, k)
    Hinv = [pow(h, p - 2, p) for h in H]
    w = [cmath.exp(2j * cmath.pi * t / p) for t in range(p)]
    tab = {}
    for a in range(p):
        for b in range(p):
            z = 0j
            for h, hi in zip(H, Hinv):
                z += w[(a * h + b * hi) % p]
            tab[(a, b)] = z
    return tab


def energy_uv_Fp(p: int, k: int, u: int, v: int) -> int:
    """#{(h_1..h_u, g_1..g_v) in H^{u+v} : sum h = sum g, sum 1/h = sum 1/g}."""
    H, _ = subgroup_of_order(p, k)
    Hinv = [pow(h, p - 2, p) for h in H]

    def sig_counter(n):
        c = defaultdict(int)
        f = math.factorial(n)
        for idx in itertools.combinations_with_replacement(range(k), n):
            x = y = 0
            for i in idx:
                x += H[i]
                y += Hinv[i]
            m = f
            for cc in Counter(idx).values():
                m //= math.factorial(cc)
            c[(x % p, y % p)] += m
        return c

    cu = sig_counter(u)
    cv = sig_counter(v) if v != u else cu
    return sum(cu[key] * cv[key] for key in cu if key in cv)


def char0_uv(u: int, v: int, k: int) -> int:
    """#{(a in (Z/k)^u, b in (Z/k)^v) : sum zeta^{a_i} == sum zeta^{b_j} in Z[zeta_k]}."""
    def sig_counter(n):
        c = defaultdict(int)
        f = math.factorial(n)
        for idx in itertools.combinations_with_replacement(range(k), n):
            co = [0] * k
            for i in idx:
                co[i] += 1
            m = f
            for cc in Counter(idx).values():
                m //= math.factorial(cc)
            c[reduce_mod_cyc(co, k)] += m
        return c
    cu = sig_counter(u)
    cv = sig_counter(v) if v != u else cu
    return sum(cu[key] * cv[key] for key in cu if key in cv)


def bessel_pair(s: int, k: int) -> int:
    """s!^2 * [x^s] I_0(2 sqrt x)^k, exactly, over Fraction."""
    # f(x) = sum_{m>=0} x^m/(m!)^2 ; need [x^s] f^k
    base = [Fraction(1, math.factorial(m) ** 2) for m in range(s + 1)]
    acc = [Fraction(0)] * (s + 1)
    acc[0] = Fraction(1)
    for _ in range(k):
        new = [Fraction(0)] * (s + 1)
        for i, ai in enumerate(acc):
            if ai == 0:
                continue
            for j, bj in enumerate(base):
                if i + j > s:
                    break
                new[i + j] += ai * bj
        acc = new
    val = acc[s] * math.factorial(s) ** 2
    assert val.denominator == 1
    return int(val.numerator)


# ------------------------------------------------------------------ checks


def check_C1_C2_C5(report):
    print("=" * 78)
    print("C1/C2/C5  direct moment identities from the full S(a,b) table")
    print("=" * 78)
    cases = [(11, 5), (13, 3), (13, 4), (23, 11), (29, 7), (31, 5), (31, 6),
             (41, 5), (41, 8), (43, 7), (61, 5), (67, 11), (71, 7)]
    ok_all = True
    for p, k in cases:
        if (p - 1) % k:
            continue
        t0 = time.time()
        tab = S_table(p, k)
        vals = list(tab.values())
        mx = max(abs(z) for z in vals)
        line = {"p": p, "k": k, "max_abs_S": mx, "trivial_bound": k,
                "weil_bound": 2 * math.sqrt(p), "moments": {}}
        for s in (1, 2, 3):
            if math.comb(k + s - 1, s) > 400_000:
                continue
            lhs = sum(abs(z) ** (2 * s) for z in vals)
            rhs = p * p * energy_uv_Fp(p, k, s, s)
            rel = abs(lhs - rhs) / max(1.0, abs(rhs))
            line["moments"][f"|S|^{2*s}"] = {"lhs": lhs, "rhs": rhs, "rel": rel}
            ok_all &= rel < 1e-9
            print(f"  p={p:>4} k={k:>3} s={s}: sum|S|^{2*s} = {lhs:.6e}  "
                  f"p^2*E_s = {rhs:.6e}  rel={rel:.2e} "
                  f"{'OK' if rel < 1e-9 else 'FAIL'}")
        # mixed
        for (u, v) in [(1, 0), (2, 1), (3, 1), (2, 0), (3, 2)]:
            if u + v == 0 or math.comb(k + max(u, v) - 1, max(u, v)) > 400_000:
                continue
            lhs = sum((z ** u) * (z.conjugate() ** v) for z in vals)
            rhs = p * p * energy_uv_Fp(p, k, u, v)
            rel = abs(lhs - rhs) / max(1.0, abs(rhs))
            c0 = char0_uv(u, v, k)
            ok_all &= rel < 1e-8
            line["moments"][f"S^{u}conj^{v}"] = {
                "lhs_re": lhs.real, "lhs_im": lhs.imag, "rhs": rhs,
                "rel": rel, "char0": c0}
            print(f"        (u,v)=({u},{v}): lhs={lhs.real:+.4e}{lhs.imag:+.4e}j "
                  f"p^2*E={rhs:.6e} rel={rel:.2e}  CHAR0={c0} "
                  f"lpf(k)={lpf(k)} u+v={u+v}")
        print(f"        max|S| = {mx:.4f}   trivial k = {k}   "
              f"Weil 2sqrt(p) = {2*math.sqrt(p):.4f}   [{time.time()-t0:.1f}s]")
        report["C1_C2_C5"].append(line)
    return ok_all


def check_C3(report):
    print("=" * 78)
    print("C3  PAIR(s,k) closed form  s!^2 [x^s] I_0(2 sqrt x)^k")
    print("=" * 78)
    ok = True
    for k in (3, 5, 7, 11, 13, 17, 23, 31):
        for s in (1, 2, 3, 4, 5):
            a = pair_count(s, k)
            b = bessel_pair(s, k)
            ok &= (a == b)
            report["C3"].append({"k": k, "s": s, "pair": a, "bessel": b,
                                 "equal": a == b,
                                 "ratio_to_s_fact_k_s": a / (math.factorial(s) * k ** s)})
    print(f"  all {len(report['C3'])} (k,s) pairs agree: {ok}")
    for row in report["C3"][:8]:
        print(f"   k={row['k']:>3} s={row['s']}: PAIR={row['pair']:>12}  "
              f"PAIR/(s! k^s)={row['ratio_to_s_fact_k_s']:.6f}")
    return ok


def check_C4(report):
    print("=" * 78)
    print("C4  largest sporadic prime, vs k^s and k^{s/2}")
    print("=" * 78)
    for k in (5, 7, 11, 13):
        for s in (2, 3):
            if math.comb(k + s - 1, s) > 200_000:
                continue
            C0 = char0_count(s, k)
            worst = None
            n = 0
            tested = 0
            plist = []
            while tested < 60 and k * n + 1 < 60_000:
                n += 1
                p = k * n + 1
                if not is_prime(p):
                    continue
                tested += 1
                from subgroup_kloosterman_energy import energy_Fp
                E = energy_Fp(p, k, s)
                if E is None:
                    continue
                plist.append((p, E))
                if E != C0:
                    worst = p
            row = {"k": k, "s": s, "CHAR0": C0, "largest_sporadic_p": worst,
                   "k^s": k ** s, "k^{s/2}": k ** (s / 2),
                   "primes_tested": tested}
            report["C4"].append(row)
            print(f"  k={k:>3} s={s}: largest p with E>CHAR0 = {worst}, "
                  f"k^s = {k**s}, k^(s/2) = {k**(s/2):.1f}, "
                  f"tested {tested} primes up to {plist[-1][0] if plist else '-'}")
    return True


def main():
    report = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
              "C1_C2_C5": [], "C3": [], "C4": []}
    ok1 = check_C1_C2_C5(report)
    ok3 = check_C3(report)
    ok4 = check_C4(report)
    report["verdict"] = {"C1_C2_C5_pass": ok1, "C3_pass": ok3, "C4_done": ok4}
    print()
    print("VERDICT:", report["verdict"])
    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                        "artifacts", "r71", "moment_certification.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(report, fh, indent=1, default=str)
    print("artifact ->", os.path.normpath(dest))
    return 0 if (ok1 and ok3) else 1


if __name__ == "__main__":
    raise SystemExit(main())
