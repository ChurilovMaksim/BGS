#!/usr/bin/env python3
"""Closed fourth moment, independently checked against Weyl convolution.

Exact formula and counting proof: mathematics/pell_coboundary_fourth_moment.md.
Real trigonometric expressions are evaluated at high precision, not with
interval-certified rounding. The limiting-series tail is bounded separately.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

import mpmath as mp

from pell_coboundary_regression import central_fourth_audit, species_vectors


def pell(index: int) -> tuple[int, int]:
    if index < 0:
        raise ValueError('Pell index must be nonnegative')
    q, p = 1, 0
    for _ in range(index):
        q, p = q+2*p, q+p
    return q, p


def constant(terms: int = 60) -> dict:
    if terms < 1:
        raise ValueError('at least one series term is required')
    with mp.workdps(90):
        alpha = 1+mp.sqrt(2)
        r = alpha**-2
        a = 8*mp.pi/(mp.sqrt(2)*alpha)
        b = 8*mp.pi/alpha
        value = -mp.mpf(9)/4 + sum(mp.sin(a*r**j)**2 + mp.sin(2*a*r**j)**2
                                  + 2*mp.sin(b*r**j)**2 for j in range(terms))
        tail = (5*a*a+2*b*b)*r**(2*terms)/(1-r*r)
        return {'gamma_decimal': mp.nstr(value, 70), 'terms': terms,
                'analytic_series_tail_bound': mp.nstr(tail, 12),
                'rounding_scope': '90-decimal arithmetic, not interval rounding certification'}


def closed_fourth(k: int) -> dict:
    if k < 11:
        raise ValueError('the proved four-atom classification requires prime K>=11')
    n, _ = species_vectors(k)  # also validates the admissible design
    with mp.workdps(max(90, len(str(n))+30)):
        nn = mp.mpf(n)
        gsum = mp.mpf(0)
        for j in range(1, (k+1)//2):
            q, p = pell(2*j)
            gsum += (mp.cos(8*mp.pi*p/nn)**2 + mp.cos(16*mp.pi*p/nn)**2
                     + 2*mp.cos(8*mp.pi*q/nn)**2)
        c = lambda a: mp.cos(a*mp.pi/nn)
        structural = c(32)*c(16)+c(24)**2+2*c(8)**2
        moment = 1+mp.mpf(1)/(4*k)+(gsum+structural)/k
        # Exact Lipschitz-plus-tail bound for the limiting correction.
        alpha = 1+mp.sqrt(2)
        r = alpha**-2
        a, b = 8*mp.pi/(mp.sqrt(2)*alpha), 8*mp.pi/alpha
        d_error = ((3*a+2*b)*(r**k+r**((k+1)//2)) / ((1-r**k)*(1-r))
                   + (5*a*a+2*b*b)*r**(k-1)/(1-r*r))
        coefficient_error = mp.mpf(1344)*mp.pi**2/nn**2
        correction_error = d_error+coefficient_error
        gamma_data = constant()
        gamma = mp.mpf(gamma_data['gamma_decimal'])
        series_tail = mp.mpf(gamma_data['analytic_series_tail_bound'])
        gap = abs(k*(3-moment)-gamma)
        assert gap <= correction_error + series_tail + mp.mpf('1e-65')
        return {'K': k, 'N': str(n), 'full_fourth_decimal': mp.nstr(moment, 70),
                'K_times_three_minus_moment': mp.nstr(k*(3-moment), 70),
                'correction_error_bound': mp.nstr(correction_error, 16),
                'structural_contribution': mp.nstr(structural/k, 40),
                'odd_trace_noncentral_bound': mp.nstr(mp.mpf(16)*k*k/(n-1), 16)}


def report() -> dict:
    checks = []
    for k in (11, 13, 17, 23, 47, 101):
        row = closed_fourth(k)
        convolution = central_fourth_audit(k)['full_fourth_moment']
        difference = abs(float(row['full_fourth_decimal'])-convolution)
        assert difference < 2e-11
        row.update(convolution_fourth=convolution, absolute_implementation_difference=difference)
        checks.append(row)
    large = [closed_fourth(k) for k in (251, 503)]
    return {'producer': str(Path(__file__).name),
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'status': 'PASS',
            'scope': 'Exact analytic formula checked numerically by independent O(K^2) Weyl convolution; not an asymptotic proof by computation.',
            'constant': constant(), 'independent_checks': checks, 'large_K_formula_checks': large}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(report(), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
