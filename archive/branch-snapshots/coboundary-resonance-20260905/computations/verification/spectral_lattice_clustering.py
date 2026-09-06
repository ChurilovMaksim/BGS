#!/usr/bin/env python3
"""Exact finite tests of the circle concentration lemma, not a BGS proof.

Coordinates, thresholds and inequalities use fractions. The optional C++
verifier uses independently cleared integer inequalities on a different grid.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from itertools import combinations_with_replacement
import hashlib
import json
from pathlib import Path
import subprocess
from typing import Sequence


def circle_distance(x: Q, y: Q) -> Q:
    delta = abs(x-y) % 1
    return min(delta, 1-delta)


def check(points: Sequence[Q], k: int, width: Q, threshold: Q) -> None:
    if not points or k < 1 or not 0 < width < Q(1, 2*k) or threshold <= 0:
        raise ValueError('invalid finite concentration instance')
    theta = sorted(x % 1 for x in points)
    d = len(theta)
    lattice = [Q(j, k) for j in range(k)]
    a2 = sum(min(circle_distance(x, y) for y in lattice)**2 for x in theta)/d
    cyclic = theta[1:]+[theta[0]+1]
    large = sum(d*(y-x) > threshold for x, y in zip(theta, cyclic))
    upper = 2*a2/width**2 + Q(k, d) + 2*k*width/threshold
    if Q(large, d) > upper:
        raise AssertionError(('spacing bound', theta, k, width, threshold))
    pairs = sum(i != j and d*circle_distance(x, y) <= threshold
                for i, x in enumerate(theta) for j, y in enumerate(theta))
    good = max(Q(0), 1-a2/width**2)
    lower = good**2/(Q(k, d)+2*k*width/threshold)-1
    if Q(pairs, d) < lower:
        raise AssertionError(('pair bound', theta, k, width, threshold))
    # This identity is deliberately retained: weak collapse need not preserve
    # the first moment, which is exactly one for every finite cyclic spectrum.
    assert sum(d*(y-x) for x, y in zip(theta, cyclic)) == d


def report(cpp: Path | None = None) -> dict:
    count = 0
    grid = [Q(j, 8) for j in range(8)]
    for d in range(1, 6):
        for theta in combinations_with_replacement(grid, d):
            for k in (1, 2, 4):
                for width in (Q(1, 4*k), Q(1, 3*k)):
                    for threshold in (Q(1, 2), Q(1), Q(2)):
                        check(theta, k, width, threshold)
                        count += 1
    # Points straddling the coordinate seam, and repeated lattice levels.
    for theta in ([Q(1, 1000), Q(999, 1000), Q(0)],
                  [Q(0)]*17,
                  [Q(j, 3) for j in range(3) for _ in range(11)]):
        for k in (1, 3, 7):
            for threshold in (Q(1, 10), Q(1), Q(7)):
                check(theta, k, Q(1, 5*k), threshold)
                count += 1
    # Exact control: n repeats of each root have K nonzero spacings of size n.
    for k, n in ((3, 11), (5, 7)):
        theta = [Q(j, k) for j in range(k) for _ in range(n)]
        d = k*n
        gaps = [d*(theta[(i+1) % d]+(i+1 == d)-theta[i]) for i in range(d)]
        assert gaps.count(0) == d-k and gaps.count(n) == k
        pairs = sum(i != j and d*circle_distance(x, y) <= Q(1, 2)
                    for i, x in enumerate(theta) for j, y in enumerate(theta))
        assert Q(pairs, d) == n-1
    out = {
        'producer': 'computations/verification/spectral_lattice_clustering.py',
        'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope': 'Exact finite rational tests of the concentration lemma; not formalization or evidence of positive BGS universality.',
        'rational_instances': count,
        'inequalities_per_instance': 2,
        'controls': ['repeated points', 'circle seam', 'uniform rational grids',
                     'mean spacing equals one despite weak collapse'],
        'passed': True,
    }
    if cpp is not None:
        result = subprocess.run([str(cpp.resolve())], check=True,
                                capture_output=True, text=True, timeout=120)
        out['independent_integer_verifier'] = json.loads(result.stdout)
        assert out['independent_integer_verifier']['passed'] is True
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cpp', type=Path)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    text = json.dumps(report(args.cpp), indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
    else:
        print(text, end='')


if __name__ == '__main__':
    main()
