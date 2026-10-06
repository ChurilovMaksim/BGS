#!/usr/bin/env python3
"""Exact finite checks of the clock-pair spectral resolution obstruction.

Cyclotomic reductions and all gap measures use exact arithmetic. This is a
negative control for insufficient abstract spectral assumptions, not a
chaotic-map universality test. No files are written without --output.
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
import sympy as sp


def cyclic_gaps(points: list[F]) -> list[F]:
    points = sorted(points)
    n = len(points)
    return [n*(points[(j+1) % n]-points[j]+(1 if j+1 == n else 0)) for j in range(n)]


def check(m: int) -> dict:
    n = 2*m
    u = [F(j, n) for j in range(n)]
    v = sorted((F(3*j, 3*m)+F(sign, 6*m)) % 1 for j in range(m) for sign in (-1, 1))
    assert len(set(v)) == n
    assert set(cyclic_gaps(u)) == {F(1)}
    gaps = cyclic_gaps(v)
    assert gaps.count(F(2, 3)) == m and gaps.count(F(4, 3)) == m
    assert sum((abs(g-1) for g in gaps), F(0))/n == F(1, 3)
    z = sp.Symbol('z')
    phi = sp.Poly(sp.cyclotomic_poly(6*m, z), z)
    trace_checks = 0
    # Root-of-unity exponents modulo 6M. Independent of the geometric-sum formula.
    for k in range(1, m+1):
        tu = sum(z**((3*j*k) % (6*m)) for j in range(n))
        tv = sum(z**(((6*j+sign)*k) % (6*m)) for j in range(m) for sign in (-1, 1))
        ru, rv = sp.Poly(tu, z).rem(phi), sp.Poly(tv, z).rem(phi)
        assert ru.is_zero
        if k < m:
            assert rv.is_zero
        else:
            assert rv.as_expr() == m
        trace_checks += 1
    # Newton's identity via logarithmic derivative checks the determinant traces.
    du, dv = 1-z**n, 1-z**m+z**n
    gu = sp.series(-z*sp.diff(du, z)/du, z, 0, n+1).removeO()
    gv = sp.series(-z*sp.diff(dv, z)/dv, z, 0, n+1).removeO()
    assert sp.expand(gu).coeff(z, m) == 0
    assert sp.expand(gv).coeff(z, m) == m
    assert sp.expand(gv).coeff(z, n) == -m
    # Rounded multisets have at most M occupied roots; split clusters exactly.
    for ell in (2, 3, 5):
        dim = max(ell, n)
        grid = dim//ell
        phases = [F((17*j*j+11*j+3) % (101*dim), 101*dim) for j in range(dim)]
        clusters: dict[int, list[int]] = {}
        for j, phase in enumerate(phases):
            label = int(phase*grid+F(1, 2)) % grid
            clusters.setdefault(label, []).append(j)
        rounded = [F(label, grid) for label, members in clusters.items() for _ in members]
        assert cyclic_gaps(rounded).count(F(0)) >= dim-grid
        eps = F(1, 10*dim)
        split = []
        for label, members in clusters.items():
            for j in range(len(members)):
                split.append((F(label, grid)+eps*F(2*j-len(members)+1, dim*len(members))) % 1)
        assert len(set(split)) == dim
        assert sum(g <= 2*eps for g in cyclic_gaps(split)) >= dim-grid
    return {'N': n, 'cyclotomic_trace_checks': trace_checks, 'wasserstein_gap': '1/3'}


def main() -> None:
    if not __debug__:
        raise RuntimeError('Do not disable assertions')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-M', type=int, default=12)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if not 1 <= args.max_M <= 60:
        parser.error('--max-M must lie in [1,60]')
    rows = [check(m) for m in range(1, args.max_M+1)]
    data = {'status': 'PASS', 'scope': 'finite exact negative controls; no BGS theorem',
            'clock_pairs': len(rows), 'cyclotomic_trace_checks': sum(r['cyclotomic_trace_checks'] for r in rows),
            'rounding_and_simple_splitting_cases': 3*len(rows),
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'anchors': rows}
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, indent=2)+'\n')
    print(json.dumps(data, indent=2))


if __name__ == '__main__':
    main()
