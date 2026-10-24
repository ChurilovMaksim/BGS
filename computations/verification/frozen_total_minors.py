#!/usr/bin/env python3
"""Exact finite regressions accompanying BGS-FM-008.

All arithmetic is integer or Fraction arithmetic. No eigenvalue statistics,
random matrices, floating-point eigenvalues, or changes to the physical tau
are used. Adapted from verify_v2.py embedded in the user-supplied 24 September
article. Its positive-decomposition checks are auxiliary and are not promoted
as a separate theorem. Finite checks do not prove asymptotic assertions.

Run:
    python -S computations/verification/frozen_total_minors.py \
      --output build/frozen_total_minors.json
Requires Python >= 3.10; standard library only.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
import itertools
import json
import math
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

Poly = list[F]

def trim(p: Poly) -> Poly:
    p = p[:]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p or [F(0)]

def add(p: Poly, q: Poly) -> Poly:
    r = [F(0)] * max(len(p), len(q))
    for i, x in enumerate(p):
        r[i] += x
    for i, x in enumerate(q):
        r[i] += x
    return trim(r)

def scale(p: Poly, c: F) -> Poly:
    return trim([c*x for x in p])

def sub(p: Poly, q: Poly) -> Poly:
    return add(p, scale(q, F(-1)))

def mul(p: Poly, q: Poly) -> Poly:
    r = [F(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            r[i+j] += x*y
    return trim(r)

def value(p: Poly, x: F) -> F:
    ans = F(0)
    for c in reversed(p):
        ans = ans*x + c
    return ans

def divide_exact(p: Poly, q: Poly) -> Poly:
    r, q = trim(p), trim(q)
    if q == [F(0)]:
        raise ZeroDivisionError("zero polynomial")
    if len(r) < len(q):
        if r == [F(0)]:
            return [F(0)]
        raise AssertionError("nonzero polynomial remainder")
    out = [F(0)] * (len(r)-len(q)+1)
    while r != [F(0)] and len(r) >= len(q):
        shift, c = len(r)-len(q), r[-1]/q[-1]
        out[shift] += c
        r = sub(r, [F(0)]*shift + scale(q, c))
    if r != [F(0)]:
        raise AssertionError(f"nonzero polynomial remainder: {r}")
    return trim(out)

def chebyshev(max_degree: int) -> list[Poly]:
    ts = [[F(1)], [F(0), F(1)]]
    while len(ts) <= max_degree:
        ts.append(sub([F(0)] + scale(ts[-1], F(2)), ts[-2]))
    return ts[:max_degree+1]

def chebyshev_coefficients(p: Poly, ts: list[Poly]) -> list[F]:
    r = trim(p)
    coefficients = [F(0)]*len(r)
    for m in range(len(r)-1, -1, -1):
        if len(r) == m+1:
            c = r[-1]/ts[m][-1]
            coefficients[m] = c
            r = sub(r, scale(ts[m], c))
    if r != [F(0)]:
        raise AssertionError("Chebyshev decomposition failed")
    return coefficients

def check_positive_decomposition() -> dict[str, int]:
    identities, weights = 0, 0
    ts = chebyshev(20)
    for n in range(3, 21):
        qn = divide_exact(sub(ts[n], [F(1)]), [F(-1), F(1)])
        fourier_qn = [F(n)]
        for m in range(1, n):
            fourier_qn = add(fourier_qn, scale(ts[m], F(2*(n-m))))
        assert qn == fourier_qn
        for q in (F(1, 5), F(2, 5), F(3, 4)):
            a, sinh_eta = (1/q+q)/2, (1/q-q)/2
            qa = value(qn, a)
            assert qa > 0
            h = scale(
                divide_exact(sub([qa], qn), [a, F(-1)]),
                sinh_eta/qa,
            )
            assert len(h) <= n-1
            # Exact Hermite/linear-programming remainder identity.
            assert mul([a, F(-1)], h) == scale(
                sub([F(1)], scale(qn, 1/qa)), sinh_eta
            )
            hc = chebyshev_coefficients(h, ts)
            for m in range(1, n-1):
                length = n-m
                target = (
                    2*(q**(-length)-q**length-length*(1/q-q))
                    / (q**(-n)+q**n-2)
                )
                assert hc[m] == target and target > 0
                weights += 1
            f1 = (1+q)/(1-q)
            polygon_energy = n*n*hc[0]-n*value(h, F(1))+n*f1
            target_energy = n*n*(1+2*q**n/(1-q**n))
            assert polygon_energy == target_energy
            cue_form_factor = q*(1-q**n)/(n*n*(1-q)**2)
            polygon_form_factor = q**n/(1-q**n)
            low_frequency_part = sum((F(m)*hc[m] for m in range(1, n-1)), F(0))/(2*n*n)
            cue_remainder = cue_form_factor-polygon_form_factor-low_frequency_part
            assert cue_remainder > 0
            identities += 1
    return {"rational_parameter_cases": identities,
            "positive_coefficients_checked": weights}

def root_difference_valuation(n: int, d: int) -> F:
    """v_5(1-zeta_n**d) in any extension, for d not divisible by n."""
    d %= n
    if d == 0:
        raise ValueError("a zero root difference has infinite valuation")
    a, tame = 0, n
    while tame % 5 == 0:
        a += 1
        tame //= 5
    if d % tame:
        return F(0)
    j = 0
    while d % 5 == 0:
        j += 1
        d //= 5
    if not (0 <= j < a):
        raise AssertionError("unexpected order of root of unity")
    return F(1, 4*5**(a-j-1))

def check_fourier_valuations() -> dict[str, int]:
    row_sets, parameter_cases = 0, 0
    for n in (3, 5, 9, 15, 25, 35, 45):
        vd = {d: root_difference_valuation(n, d) for d in range(1, n)}
        for r in range(1, min(n, 4)+1):
            lower = sum((F(r-d)*vd[d] for d in range(1, r)), F(0))
            for rows in itertools.combinations(range(n), r):
                actual = sum(
                    (vd[j-i] for i, j in itertools.combinations(rows, 2)),
                    F(0),
                )
                assert actual >= lower
                row_sets += 1
            corner = tuple(range(n-r, n))
            actual = sum(
                (vd[j-i] for i, j in itertools.combinations(corner, 2)),
                F(0),
            )
            assert actual == lower
            parameter_cases += 1
    return {"dimension_rank_cases": parameter_cases,
            "row_subsets_checked": row_sets}

def check_joint_leading_term() -> dict[str, int]:
    cases = 0
    for n in range(3, 8):
        eigenvalues = tuple(n-1-j for j in range(n))
        for k in range(2, min(n, 4)+1):
            for original in itertools.product(range(-1, 2), repeat=k):
                if sum(original) != 0 or not any(original):
                    continue
                weights = tuple(sorted(original+(0,)*(n-k), reverse=True))
                beta = sum(w*a for w, a in zip(weights, eigenvalues))
                covariance = sum(
                    (weights[i]-weights[j])*(eigenvalues[i]-eigenvalues[j])
                    for i in range(n) for j in range(i+1, n)
                )
                assert beta > 0 and covariance == n*beta
                max_found, multiplicity = None, 0
                for indices in itertools.permutations(range(n), k):
                    exponent = sum(original[j]*eigenvalues[indices[j]]
                                   for j in range(k))
                    if max_found is None or exponent > max_found:
                        max_found, multiplicity = exponent, 1
                    elif exponent == max_found:
                        multiplicity += 1
                counts = Counter(weights)
                expected = math.prod(math.factorial(v) for v in counts.values())
                expected //= math.factorial(n-k)
                assert max_found == beta and multiplicity == expected
                cases += 1
    return {"balanced_weight_cases": cases}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {
        "status": "all exact regression checks passed",
        "scope": "Finite exact regressions; the all-N total-minor and algebraic-time proof is in mathematics/fixed-map/frozen_algebraic_spectral_simplicity.md; no CUE conclusion",
        "positive_decomposition": check_positive_decomposition(),
        "fourier_minor_valuations": check_fourier_valuations(),
        "joint_trace_leading_term": check_joint_leading_term(),
    }
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered+"\n", encoding="utf-8")
    print(rendered)

if __name__ == "__main__":
    main()
