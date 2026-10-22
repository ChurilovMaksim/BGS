#!/usr/bin/env python3
"""Bind the compiled finite Lean literals to pinned inputs; no abstract theorem."""
from pathlib import Path
import hashlib
import re
import json
import sympy as s
from actual_commutant_common import verify_data, require

ROOT = Path(__file__).resolve().parents[2]
EXPECTED_LEAN = '6f2be83b437cd9962a0c44b7c1316ad9b13ba402cc2a9b4737da22ee64341acc'

def check(source, data):
    verify_data(data)
    require(hashlib.sha256(source.read_bytes()).hexdigest() == EXPECTED_LEAN,
            'compiled Lean source identity changed')
    src = source.read_text()
    polys = json.loads((data / 'bounded_boundary_polynomials.json').read_text())
    norm = json.loads((data / 'bounded_boundary_norm.json').read_text())
    certs = json.loads((data / 'bounded_factor_certificates_fast.json').read_text())['certificates']
    entries = re.findall(r'def entry(\d+) : Entry := ⟨#\[([^]]*)\], (\d+), #\[(.*?)\]⟩', src, re.S)
    require([int(row[0]) for row in entries] == list(range(7)), 'entry index/coverage')
    q = s.symbols('q')
    parse = lambda text: list(map(int, text.split(','))) if text else []
    count = 0
    for i, ((index, poly, unit, factors), cert) in enumerate(zip(entries, certs)):
        coefficients = list(reversed(s.Poly(s.sympify(polys['y_numerators'][i + 1]), q, modulus=5).all_coeffs())) if i < 6 else list(reversed(norm['norm_coefficients']))
        require(parse(poly) == [int(x) % 5 for x in coefficients], 'polynomial literal')
        require(int(unit) == cert['factorization_unit'] % 5, 'unit literal')
        rows = re.findall(r'⟨#\[([^]]*)\],(\d+)⟩', factors)
        require(len(rows) == len(cert['factors']), 'factor coverage')
        for (coefficients, multiplicity), factor in zip(rows, cert['factors']):
            require(parse(coefficients) == [x % 5 for x in reversed(factor['coefficients'])], 'factor literal')
            require(int(multiplicity) == factor['multiplicity'], 'multiplicity literal')
            require(len(parse(coefficients)) - 1 == factor['degree'], 'degree binding')
            count += 1
    require(count == 46, 'factor occurrence total')
    return count

def main():
    count = check(ROOT / 'formalization/Bgs/SevenPrimary.lean', ROOT / 'computations/verification/actual_commutant_data')
    print(f'seven-primary certificate: 7 polynomial literals and {count} factor occurrences match pinned source; no abstract theorem certified')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
