#!/usr/bin/env python3
"""Exact finite regression for the two-circle instability construction.

All Laurent-polynomial identities, uniform angular error bounds and interior
separation inequalities use fractions. No angular grid or floating-point fit
is used to verify a bound. The analytic all-degree proof is in the manuscript.
No files are written unless --output is supplied.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')
import argparse
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

Laurent = dict[int, F]
BASE = F(1, 4)


def add(a: Laurent, b: Laurent, sign: int = 1) -> Laurent:
    out = a.copy()
    for n, c in b.items():
        out[n] = out.get(n, F(0)) + sign*c
        if not out[n]:
            out.pop(n)
    return out


def scale_argument(a: Laurent, q: F) -> Laurent:
    return {n: c*q**n for n, c in a.items()}


def monomial(a: Laurent, power: int, scale: F = F(1)) -> Laurent:
    return {n+power: scale*c for n, c in a.items()}


def reciprocal(a: Laurent) -> Laurent:
    return {-n: c for n, c in a.items()}


def evaluate(a: Laurent, x: F) -> F:
    return sum((c*x**n for n, c in a.items()), F(0))


def intensity_coefficients(a: Laurent, radius: F) -> Laurent:
    """Exact angular Fourier coefficients of |a(radius*exp(i theta))|^2."""
    out: Laurent = {}
    for n, c in a.items():
        for m, d in a.items():
            k = n-m
            out[k] = out.get(k, F(0))+c*d*radius**(n+m)
    return {k: c for k, c in out.items() if c}


def interval_tail_bound() -> F:
    """Rational upper bound for the infinite positive Laurent sum at 3/4."""
    x = F(3, 4)
    term = lambda n: BASE**(2*n*n+n)*x**(4*n+1)
    head = sum((term(n) for n in (-2, -1, 0, 1)), F(0))
    # Positive n>=2: consecutive ratio <= q^11*x^4.
    # Negative n=-k, k>=3: consecutive ratio <= q^13/x^4.
    tail = term(2)/(1-BASE**11*x**4)+term(-3)/(1-BASE**13/x**4)
    bound = head+tail
    assert bound < F(27, 20)
    assert term(1)+term(0)+term(-1) > 0
    return bound


def verify(m: int) -> dict:
    if m < 1:
        raise ValueError('M must be positive')
    a = {4*n+1: BASE**(2*n*n+n) for n in range(-m, m+1)}
    b = reciprocal(a)
    defect = add(scale_argument(a, BASE), monomial(a, -4, BASE**-2), -1)
    predicted = {4*m+1: BASE**(2*m*m+5*m+1),
                 -4*m-3: -BASE**(2*m*m-m-2)}
    assert defect == predicted
    # This bound controls the full circle |z|=2, not sampled arguments.
    defect_bound = sum((abs(c)*F(2)**n for n, c in defect.items()), F(0))
    assert defect_bound <= F(2)**(-4*m*m-2*m+2)
    length = 4*m+1
    normalizer = F(1, 4*2**length)
    p, q = monomial(a, length, normalizer), monomial(b, length, normalizer)
    assert min(p) >= 0 and min(q) >= 0
    assert max(max(p), max(q)) == 8*m+2
    assert evaluate(p, F(2)) < 1 and evaluate(q, F(2)) < 1
    # Positive coefficients bound the norms on D_2 by their values at 2.
    outer = add(intensity_coefficients(p, F(1)), intensity_coefficients(q, F(1)), -1)
    assert outer == {}
    inner = add(intensity_coefficients(p, F(1, 2)), intensity_coefficients(q, F(1, 2)), -1)
    angular_l1 = sum(map(abs, inner.values()), F(0))
    error_bound = F(2)**(-4*m*m-18*m-3)
    assert F(0) < angular_l1 <= error_bound
    assert evaluate(a, F(3, 4)) < F(27, 20)
    assert evaluate(b, F(3, 4)) > F(3, 2)
    gap = evaluate(q, F(3, 4))**2-evaluate(p, F(3, 4))**2
    gap_bound = F(1, 40)*F(3, 8)**(8*m+2)
    assert gap >= gap_bound > 0
    # A wrong sign in the recurrence must be rejected.
    assert defect != {n: -c for n, c in predicted.items()}
    return {'M': m, 'degree': 8*m+2,
            'measurement_upper_bound': str(error_bound),
            'interior_lower_bound': str(gap_bound),
            'exact_angular_l1_le_upper_bound': True,
            'exact_target_gap_ge_lower_bound': True}


def main() -> None:
    if not __debug__:
        raise RuntimeError('Do not run verification with python -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-M', type=int, default=24)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if not 1 <= args.max_M <= 200:
        parser.error('--max-M must lie between 1 and 200')
    tail = interval_tail_bound()
    rows = [verify(m) for m in range(1, args.max_M+1)]
    data = {'status': 'PASS', 'scope': 'finite exact regression; not an all-degree proof',
            'construction_count': len(rows), 'largest_degree': rows[-1]['degree'],
            'whole_circle_checks': 2*len(rows), 'tampered_sign_controls': len(rows),
            'infinite_tail_bound_at_three_quarters': str(tail),
            'independent_bounds': ['Laurent recurrence', 'angular Fourier l1',
                                   'disk supremum via positive coefficients', 'rational target value'],
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'anchors': [rows[0], rows[len(rows)//2], rows[-1]]}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
