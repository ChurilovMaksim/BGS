#!/usr/bin/env python3
"""Idempotently register the general-hyperbolic continuation.

Default mode reports pending text edits without applying them. --apply writes
only the explicitly named files and preserves all existing text. This script
neither runs scientific checks nor changes any theorem's verification status.
"""
from __future__ import annotations

import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MARKER = '## General hyperbolic covariance and fixed-strength conjugacy'


def append_once(text: str, marker: str, addition: str) -> str:
    if marker in text:
        return text
    return text.rstrip()+'\n\n'+addition.strip()+'\n'


def planned_edits() -> dict[Path, str]:
    required = [
        'mathematics/general_hyperbolic_prime_spectra.md',
        'mathematics/hyperbolic_signed_trace_extension.md',
        'mathematics/analytic_poisson_rigidity.md',
        'mathematics/quantitative_resonance_transversality.md',
        'computations/verification/general_hyperbolic_prime_spectra.py',
        'computations/cpp/general_hyperbolic_periods.cpp',
        'formalization/Bgs/GeneralHyperbolicParity.lean',
        'manuscript/general_hyperbolic_section.tex',
    ]
    missing = [p for p in required if not (ROOT/p).is_file()]
    if missing:
        raise RuntimeError('Missing maintained source files: '+', '.join(missing))
    result: dict[Path, str] = {}
    summaries = {
        'README.md': '''
## General hyperbolic covariance and fixed-strength conjugacy

A self-contained finite Weyl-character argument determines the complete
parity spectrum without a split-torus assumption. The signed recurrence
extends the construction to every matrix in SL(2,Z) with absolute trace
larger than two, including mixed split/nonsplit and prime-square moduli.
The uniform sector is odd or even according to an explicit Legendre symbol.

[Finite spectral theorem and fixed-strength construction](mathematics/general_hyperbolic_prime_spectra.md)
are supplemented by the [signed-trace extension](mathematics/hyperbolic_signed_trace_extension.md),
[analytic rigidity](mathematics/analytic_poisson_rigidity.md), and
[quantitative one-mode transversality](mathematics/quantitative_resonance_transversality.md).

The nonlinear classical maps are deliberately smoothly symplectically
conjugate to arithmetic maps. Operator-norm comparison holds to every inverse
power and on all polynomial time windows for this family. The notes derive
all fixed factorial local statistics and distinguish their divergent count
moments from the weak empty-process limit. None is a positive generic BGS
theorem or a claim of established priority. Finite Python/C++ and Lean sources
have separate scopes; their presence is not an execution or compilation record.
''',
        'mathematics/results.md': '''
## General hyperbolic covariance and fixed-strength conjugacy

[General covariance theorem](general_hyperbolic_prime_spectra.md): an odd
fixed-point-free cyclic symplectic action determines exact full and parity
multiplicities by Weyl-basis traces and integer character orthogonality.
[Signed traces](hyperbolic_signed_trace_extension.md) give exponentially
growing odd moduli for both signs of every hyperbolic trace, with the uniform
sector selected by a Legendre symbol. No residue-ring eigenbasis is assumed.

The same note supplies the fixed-classical-strength smooth conjugacy and
its all-polynomial-time operator-norm error, cluster ranks, every fixed
factorial correlation, and random-origin count law. The retained arithmetic
conjugacy is essential and excludes an interpretation as generic BGS.
[Analytic rigidity](analytic_poisson_rigidity.md) excludes this commuting
mechanism for nonconstant analytic generators, but does not imply positive
Green--Kubo variance. [One-mode transversality](quantitative_resonance_transversality.md)
quantifies near-degeneracy uniformly over arbitrary smooth backgrounds.
The several-orbit exact-zero problem remains distinct and unresolved here.
''',
        'record/claim_ledger.md': '''
## General hyperbolic covariance and fixed-strength conjugacy

PROJECT PROOFS: general_hyperbolic_prime_spectra.md,
hyperbolic_signed_trace_extension.md, analytic_poisson_rigidity.md,
quantitative_resonance_transversality.md. The finite character theorem and
signed recurrence are independent of the previous Gaussian-average corpus.
The fixed-strength examples use smooth support separation and remain
arithmetically conjugate. The analytic theorem rules out a zero Poisson
bracket under its critical-set hypothesis, not every zero variance of a
nonzero bracket. The transversality estimate allows exceptional coefficients.

VERIFICATION SCOPE: Python exact arithmetic and floating-point finite spectra;
independent C++ integer matrix trace sums; finite Lean characteristic and
modulus identities. Compilation, execution and publication must be reported
from actual outputs tied to source hashes. This integration entry asserts no
new successful run, no full analytic formalization, and no repository-wide
CI status. No worldwide priority or positive generic BGS claim is made.
''',
    }
    for name, addition in summaries.items():
        path = ROOT/name
        text = path.read_text(encoding='utf-8')
        updated = append_once(text, MARKER, addition)
        if updated != text:
            result[path] = updated
    path = ROOT/'formalization/Bgs.lean'
    text = path.read_text(encoding='utf-8')
    command = 'import Bgs.GeneralHyperbolicParity'
    updated = append_once(text, command, command)
    if updated != text:
        result[path] = updated
    path = ROOT/'manuscript/arithmetic_cat_map_moments.tex'
    text = path.read_text(encoding='utf-8')
    command = r'\input{general_hyperbolic_section.tex}'
    if command not in text:
        anchor = r'\begin{thebibliography}'
        if text.count(anchor) != 1:
            raise RuntimeError('Expected one bibliography anchor in the main article')
        result[path] = text.replace(anchor, command+'\n\n'+anchor, 1)
    path = ROOT/'CMakeLists.txt'
    text = path.read_text(encoding='utf-8')
    updated = text
    for target in ('pell_floquet_pair_verifier', 'spectral_lattice_clustering',
                   'pell_minimal_relation_verifier', 'general_hyperbolic_periods'):
        source = ROOT/f'computations/cpp/{target}.cpp'
        if not source.is_file():
            raise RuntimeError(f'Missing registered source: {source.relative_to(ROOT)}')
        if f'add_executable({target} ' not in updated:
            block = f'''add_executable({target} computations/cpp/{target}.cpp)
target_include_directories({target} PRIVATE ${{Boost_INCLUDE_DIRS}})
if(MSVC)
  target_compile_options({target} PRIVATE /W4)
else()
  target_compile_options({target} PRIVATE -Wall -Wextra -Wpedantic)
endif()'''
            updated = updated.rstrip()+'\n\n'+block+'\n'
    if updated != text:
        result[path] = updated
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--apply', action='store_true')
    args = parser.parse_args()
    edits = planned_edits()
    for path, contents in edits.items():
        print(('WRITE ' if args.apply else 'PENDING ')+str(path.relative_to(ROOT)))
        if args.apply:
            path.write_text(contents, encoding='utf-8')
    if args.apply and planned_edits():
        raise RuntimeError('Integration was not idempotent')
    print(f'{len(edits)} integration edits; no scientific execution status inferred.')


if __name__ == '__main__':
    main()
