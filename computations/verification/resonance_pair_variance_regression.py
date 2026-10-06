#!/usr/bin/env python3
"""Independent finite checks of the resonance-to-pair-correlation bridge.

Variance is computed twice with exact rational arithmetic: circular interval
intersections and a sweep over jump intervals. Fourier sums provide a third,
floating-point lower-bound check. Gaussian factorial statistics are computed
both directly from eigenphase differences and via traces/Poisson summation.

These checks do not prove the Pell Floquet normal form or a growing-parameter
limit, and the existence of this source is not evidence that it was executed.
Only the report emitted by a successful invocation is execution evidence.
"""
from __future__ import annotations

# Fail before imports or output when Python removes verification assertions.
if not __debug__:
    raise RuntimeError('Verification requires assertions; run Python without -O/-OO or PYTHONOPTIMIZE.')

import argparse
import cmath
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
from typing import Sequence

Phase = Fraction


def normalized_phases(values: Sequence[Fraction]) -> list[Phase]:
    if not values:
        raise ValueError("the spectrum must be nonempty")
    return [Fraction(x) % 1 for x in values]


def overlap_variance(phases: Sequence[Phase], length: Fraction) -> Fraction:
    """Exact integral variance using pairwise overlaps of circular arcs."""
    phases = normalized_phases(phases)
    dimension = len(phases)
    if not 0 < length < dimension:
        raise ValueError("require 0 < L < dimension")
    width = length / dimension
    second = Fraction(0)
    for x in phases:
        for y in phases:
            delta = (x-y) % 1
            second += max(width-delta, 0) + max(width-(1-delta), 0)
    return second-length*length


def sweep_variance(phases: Sequence[Phase], length: Fraction) -> Fraction:
    """Exact independent integration between all entry and exit events."""
    phases = normalized_phases(phases)
    dimension = len(phases)
    if not 0 < length < dimension:
        raise ValueError("require 0 < L < dimension")
    width = length / dimension
    endpoints = sorted({Fraction(0), Fraction(1)}
                       | {x for x in phases}
                       | {(x-width) % 1 for x in phases})
    variance = Fraction(0)
    mean = Fraction(0)
    for left, right in zip(endpoints, endpoints[1:]):
        center = (left+right)/2
        count = sum((x-center) % 1 < width for x in phases)
        mean += (right-left)*count
        variance += (right-left)*(count-length)**2
    assert mean == length
    return variance


def trace(phases: Sequence[Phase], power: int) -> complex:
    # Reduce in rational arithmetic before converting to an angle. This also
    # avoids unnecessary loss of precision for large integer powers.
    return sum(cmath.exp(2j*math.pi*float((power*x) % 1)) for x in phases)


def fourier_variance_lower(phases: Sequence[Phase], length: Fraction,
                           cutoff: int) -> float:
    if cutoff < 1:
        raise ValueError("positive Fourier cutoff required")
    dimension = len(phases)
    width = float(length)/dimension
    return 2*math.fsum(
        (math.sin(math.pi*k*width)/(math.pi*k))**2
        * abs(trace(phases, k))**2 for k in range(1, cutoff+1))


def gaussian_test(s: float, scale: float) -> float:
    return math.exp(-(s/scale)**2)/(math.sqrt(math.pi)*scale)


def pair_statistic_direct(phases: Sequence[Phase], scale: float) -> float:
    """Gaussian periodization; truncation reaches twelve Gaussian widths.

    This is a floating-point regression, not an interval certificate.
    """
    if scale <= 0:
        raise ValueError("scale must be positive")
    dimension = len(phases)
    winding = math.ceil(12*scale/dimension)+2
    terms = []
    for i, x in enumerate(phases):
        for j, y in enumerate(phases):
            if i == j:
                continue
            delta = float(x-y)
            terms.extend(gaussian_test(dimension*(delta+ell), scale)
                         for ell in range(-winding, winding+1))
    return math.fsum(terms)/dimension


def gaussian_diagonal(dimension: int, scale: float) -> float:
    winding = math.ceil(12*scale/dimension)+2
    return math.fsum(gaussian_test(dimension*ell, scale)
                     for ell in range(-winding, winding+1))


def pair_statistic_fourier(phases: Sequence[Phase], scale: float) -> float:
    dimension = len(phases)
    cutoff = math.ceil(12*dimension/(math.pi*scale))+2
    positive = math.fsum(
        math.exp(-(math.pi*scale*k/dimension)**2)
        * abs(trace(phases, k)/dimension)**2
        for k in range(1, cutoff+1))
    return 1+2*positive-gaussian_diagonal(dimension, scale)


def single_resonance_pair_lower(phases: Sequence[Phase], scale: float,
                                power: int) -> float:
    dimension = len(phases)
    return (1 + 2*math.exp(-(math.pi*scale*power/dimension)**2)
            * abs(trace(phases, power)/dimension)**2
            - gaussian_diagonal(dimension, scale))


def run_checks() -> dict:
    cases = [
        ("clock", [Fraction(j, 9) for j in range(9)], Fraction(7, 3)),
        ("triple_clock", [Fraction(j, 4) for j in range(4)
                          for _ in range(3)], Fraction(5, 2)),
        ("nonuniform_with_multiplicity",
         [Fraction(0), Fraction(0), Fraction(1, 7), Fraction(2, 5),
          Fraction(3, 8), Fraction(6, 7)], Fraction(11, 5)),
        ("wide_wrapping_window",
         [Fraction(0), Fraction(1, 11), Fraction(4, 7), Fraction(5, 6)],
         Fraction(13, 4)),
    ]
    rows = []
    for name, raw, length in cases:
        phases = normalized_phases(raw)
        direct = overlap_variance(phases, length)
        sweep = sweep_variance(phases, length)
        assert direct == sweep
        lower = fourier_variance_lower(phases, length, 4000)
        assert -1e-9 <= float(direct)-lower < 0.02
        if name == "clock":
            assert direct == Fraction(2, 9)
        if name == "triple_clock":
            assert direct == Fraction(5, 4)
        pair_rows = []
        for scale in (0.7, 2.0, 7.0):
            real_space = pair_statistic_direct(phases, scale)
            frequency_space = pair_statistic_fourier(phases, scale)
            assert abs(real_space-frequency_space) < 2e-10
            for power in (1, 2, 4):
                bound = single_resonance_pair_lower(phases, scale, power)
                assert bound <= real_space+2e-10
            pair_rows.append({"scale": scale, "direct": real_space,
                              "fourier": frequency_space})
        rows.append({"case": name, "dimension": len(phases),
                     "L": str(length), "exact_variance": str(direct),
                     "fourier_partial_variance": lower,
                     "pair_statistics": pair_rows})

    # A rigid periodic replication tests that the relevant frequency is the
    # recurrence order, not the full dimension, and retains the distinction
    # between diagonal subtraction and genuine repeated eigenvalues.
    inner = [Fraction(1, 13), Fraction(2, 7), Fraction(3, 5), Fraction(9, 10)]
    copies = 5
    phases = [(r+y)/copies for r in range(copies) for y in inner]
    for power in range(1, 26):
        expected = (copies*trace(inner, power//copies)
                    if power % copies == 0 else 0j)
        assert abs(trace(phases, power)-expected) < 2e-10

    # Negative control: a finite set of positive Fourier modes is not the
    # entire variance. An accidental equality assertion would be incorrect.
    clock = [Fraction(j, 9) for j in range(9)]
    partial = fourier_variance_lower(clock, Fraction(7, 3), 9)
    assert partial < float(Fraction(2, 9))-0.01

    return {"status": "passed", "checks": rows,
            "replicated_spectrum_trace_checks": 25,
            "scope": ("Exact rational finite variance identities and numerical "
                      "Poisson/positivity checks only. No proof of the Pell "
                      "normal form, Gaussian limit, or BGS is inferred."),
            "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_checks()
    text = json.dumps(result, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
