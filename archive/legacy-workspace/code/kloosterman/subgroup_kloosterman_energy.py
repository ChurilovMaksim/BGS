"""
Joint additive energy of the subgroup hyperbola  Gamma_H = {(h, h^{-1}) : h in H}
================================================================================

Object.  p prime, H <= F_p^*  the (unique) subgroup of order k (so k | p-1).
For a,b in F_p put the *subgroup Kloosterman sum*

        S_H(a,b) = sum_{h in H} e_p(a h + b h^{-1}).

Then, exactly,

        sum_{a,b in F_p} |S_H(a,b)|^{2s} = p^2 * E_s(H),                      (*)

        E_s(H) = # { (h_1,...,h_{2s}) in H^{2s} :
                        h_1+...+h_s = h_{s+1}+...+h_{2s}   in F_p,
                        h_1^{-1}+...+h_s^{-1} = h_{s+1}^{-1}+...+h_{2s}^{-1} }.

E_s(H) is the joint additive energy of Gamma_H.

Three counts are compared here.

  PAIR(s,k)  = # {(u,v) in H^s x H^s : u and v are equal as MULTISETS}
             = sum over multisets M of size s of (# orderings of M)^2
             ~ s! k^s   (the "complex Gaussian" value).

  CHAR0(s,k) = # {(a,b) in (Z/k)^{2s} : sum_i zeta^{a_i} = sum_j zeta^{b_j} }
               with zeta = primitive k-th root of unity in C.
             NOTE: over C the second (inverse) equation is the complex conjugate
             of the first, hence automatic.  So CHAR0 is a *single* vanishing-sum
             count.  CHAR0 >= PAIR always, with equality governed by the theory
             of vanishing sums of roots of unity (Mann / Conway-Jones).

  E_s(H)     = the F_p count above, computed by meet-in-the-middle.

Predictions to test (this is the content of the new theorem being checked):

  (P1)  E_s(H) >= CHAR0(s,k) >= PAIR(s,k)  for every admissible p.
  (P2)  CHAR0(s,k) = PAIR(s,k)  whenever every prime factor of k exceeds 2s.
  (P3)  E_s(H) = CHAR0(s,k) for all p outside a finite exceptional set
        B(k,s) (the "sporadic mod-p coincidences" of the project's T18(b)).
  (P4)  hence for lpf(k) > 2s and p outside B(k,s):
              sum_{a,b} |S_H(a,b)|^{2s} = p^2 * PAIR(s,k),
        i.e. the moments of S_H/sqrt(k) are EXACTLY the complex-Gaussian
        moments  PAIR(s,k)/k^s -> s!.

Run:  python subgroup_kloosterman_energy.py
"""

from __future__ import annotations

import itertools
import json
import math
import os
import sys
import time
from collections import Counter, defaultdict

# ----------------------------------------------------------------- utilities


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(r - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def prime_factors(n: int) -> list[int]:
    fs, d = [], 2
    while d * d <= n:
        if n % d == 0:
            fs.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs


def lpf(n: int) -> int:
    return prime_factors(n)[0] if n > 1 else 1


def subgroup_of_order(p: int, k: int) -> list[int]:
    """The unique subgroup of order k in F_p^*, as a sorted list, plus a generator."""
    assert (p - 1) % k == 0
    g = None
    for cand in range(2, p):
        ok = True
        for q in set(prime_factors(p - 1)):
            if pow(cand, (p - 1) // q, p) == 1:
                ok = False
                break
        if ok:
            g = cand
            break
    assert g is not None
    a = pow(g, (p - 1) // k, p)          # element of exact order k
    H = [pow(a, j, p) for j in range(k)]
    assert len(set(H)) == k
    return H, a


# ------------------------------------------------------- PAIR(s,k) exactly


def pair_count(s: int, k: int) -> int:
    """sum over multisets M of size s from a k-set of (multinomial(s;M))^2 ."""
    total = 0
    # iterate over partitions of s into at most k parts, count how many
    # multisets have that shape
    def parts(n, maxpart, maxlen):
        if n == 0:
            yield []
            return
        if maxlen == 0:
            return
        for first in range(min(n, maxpart), 0, -1):
            for rest in parts(n - first, first, maxlen - 1):
                yield [first] + rest

    for lam in parts(s, s, k):
        r = len(lam)
        # number of multisets of shape lam:  k! / ((k-r)! * prod_j (mult of j)!)
        shape_mult = Counter(lam)
        ways = math.perm(k, r)
        for v in shape_mult.values():
            ways //= math.factorial(v)
        multinom = math.factorial(s)
        for a in lam:
            multinom //= math.factorial(a)
        total += ways * multinom * multinom
    return total


# ------------------------------------------------- CHAR0(s,k) exactly (Z[x]/Phi_k)


def cyclotomic_poly(k: int) -> list[int]:
    """Phi_k(x) as a coefficient list (ascending), integer arithmetic only."""
    # x^k - 1 = prod_{d | k} Phi_d(x)  ->  divide out recursively
    num = [-1] + [0] * (k - 1) + [1]          # x^k - 1
    for d in range(1, k):
        if k % d == 0:
            num = poly_divide_exact(num, cyclotomic_poly(d))
    return num


_CYC_CACHE: dict[int, list[int]] = {1: [-1, 1]}


def cyc(k: int) -> list[int]:
    if k not in _CYC_CACHE:
        num = [-1] + [0] * (k - 1) + [1]
        for d in range(1, k):
            if k % d == 0:
                num = poly_divide_exact(num, cyc(d))
        _CYC_CACHE[k] = num
    return _CYC_CACHE[k]


def poly_divide_exact(a: list[int], b: list[int]) -> list[int]:
    a = a[:]
    q = [0] * (len(a) - len(b) + 1)
    for i in range(len(a) - 1, len(b) - 2, -1):
        c = a[i] // b[-1]
        q[i - len(b) + 1] = c
        if c:
            for j in range(len(b)):
                a[i - len(b) + 1 + j] -= c * b[j]
    assert all(x == 0 for x in a[: len(b) - 1]), "non-exact division"
    return q


def reduce_mod_cyc(coeffs: list[int], k: int) -> tuple[int, ...]:
    """Reduce a poly (ascending coeffs, degree < k) modulo Phi_k; canonical key."""
    phi = cyc(k)
    a = coeffs[:]
    dphi = len(phi) - 1
    for i in range(len(a) - 1, dphi - 1, -1):
        c = a[i]
        if c:
            for j in range(len(phi)):
                a[i - dphi + j] -= c * phi[j]
    return tuple(a[:dphi])


def char0_count(s: int, k: int) -> int:
    """# {(a,b) in (Z/k)^{2s} : sum zeta^{a_i} = sum zeta^{b_j} } in Z[zeta_k]."""
    sig = Counter()
    for tup in itertools.combinations_with_replacement(range(k), s):
        coeffs = [0] * k
        for a in tup:
            coeffs[a] += 1
        key = reduce_mod_cyc(coeffs, k)
        # number of orderings of this multiset
        mult = math.factorial(s)
        for v in Counter(tup).values():
            mult //= math.factorial(v)
        sig[key] += mult
    return sum(c * c for c in sig.values())


# --------------------------------------------------------- E_s(H) over F_p


def energy_Fp(p: int, k: int, s: int, cap: int = 40_000_000) -> int | None:
    """Meet-in-the-middle count of E_s(H).  Returns None if the s-tuple space
    exceeds `cap` (we enumerate multisets, so the cost is C(k+s-1, s))."""
    n_multisets = math.comb(k + s - 1, s)
    if n_multisets > cap:
        return None
    H, _ = subgroup_of_order(p, k)
    Hinv = [pow(h, p - 2, p) for h in H]
    sig = defaultdict(int)
    fact_s = math.factorial(s)
    for idx in itertools.combinations_with_replacement(range(k), s):
        u = 0
        v = 0
        for i in idx:
            u += H[i]
            v += Hinv[i]
        mult = fact_s
        for c in Counter(idx).values():
            mult //= math.factorial(c)
        sig[(u % p, v % p)] += mult
    return sum(c * c for c in sig.values())


# ----------------------------------------------------------------- driver


def main() -> int:
    out = {"generated": time.strftime("%Y-%m-%dT%H:%M:%S"), "rows": []}

    # (k, s) pairs and the primes p = 1 mod k to test
    plan = []
    for k in [3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 19, 20, 23, 25]:
        for s in [2, 3, 4]:
            if math.comb(k + s - 1, s) > 300_000:
                continue
            plan.append((k, s))

    # collect primes p == 1 mod k, several sizes
    prime_lists: dict[int, list[int]] = {}
    for k in {kk for kk, _ in plan}:
        ps = []
        n = 1
        while len(ps) < 8 and n < 4000:
            n += 1
            cand = k * n + 1
            if is_prime(cand):
                ps.append(cand)
        prime_lists[k] = ps

    print(f"{'k':>4} {'s':>2} {'lpf':>4} {'PAIR':>12} {'CHAR0':>12} "
          f"{'P2ok':>5}  primes -> E_s(H)")
    for k, s in plan:
        P = pair_count(s, k)
        C0 = char0_count(s, k)
        p2_expected = lpf(k) > 2 * s
        p2_ok = (C0 == P) == p2_expected
        row = {"k": k, "s": s, "lpf": lpf(k), "PAIR": P, "CHAR0": C0,
               "P2_predicted_equal": p2_expected, "P2_holds": p2_ok,
               "Fp": {}}
        cells = []
        for p in prime_lists[k]:
            E = energy_Fp(p, k, s)
            if E is None:
                continue
            row["Fp"][p] = E
            flag = "=" if E == C0 else ("+" if E > C0 else "!")
            cells.append(f"{p}:{E}{flag}")
        out["rows"].append(row)
        print(f"{k:>4} {s:>2} {lpf(k):>4} {P:>12} {C0:>12} "
              f"{('OK' if p2_ok else 'FAIL'):>5}  " + " ".join(cells))
        sys.stdout.flush()

    # ---- global verdicts
    v = {}
    v["P1_E_ge_CHAR0_ge_PAIR"] = all(
        r["CHAR0"] >= r["PAIR"] and all(E >= r["CHAR0"] for E in r["Fp"].values())
        for r in out["rows"])
    v["P2_mann_criterion"] = all(r["P2_holds"] for r in out["rows"])
    v["P3_eventual_equality_fraction"] = sum(
        1 for r in out["rows"] for E in r["Fp"].values() if E == r["CHAR0"]
    ) / max(1, sum(len(r["Fp"]) for r in out["rows"]))
    # largest prime where a sporadic coincidence still occurs
    spor = [(r["k"], r["s"], p, E, r["CHAR0"])
            for r in out["rows"] for p, E in r["Fp"].items() if E != r["CHAR0"]]
    v["sporadic_cases"] = spor
    out["verdict"] = v
    print("\nVERDICT")
    for kk, vv in v.items():
        if kk != "sporadic_cases":
            print(f"  {kk}: {vv}")
    print(f"  sporadic (E != CHAR0) cases: {len(spor)}")
    for c in spor[:40]:
        print(f"    k={c[0]} s={c[1]} p={c[2]}  E={c[3]}  CHAR0={c[4]}  "
              f"excess={c[3]-c[4]}")

    dest = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        "..", "artifacts", "r71", "subgroup_energy.json")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with open(dest, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=1)
    print(f"\nartifact -> {os.path.normpath(dest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
