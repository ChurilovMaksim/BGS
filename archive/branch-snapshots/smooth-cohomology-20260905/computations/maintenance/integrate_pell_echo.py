#!/usr/bin/env python3
"""Idempotent source integration for the weighted echo extension.

This script does not label tests or analytic Lean formalization as complete.
It is intended to run after publish_pell_research.py and before verification.
"""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]


def append_once(name: str, marker: str, addition: str) -> None:
    path=ROOT/name
    text=path.read_text(encoding='utf-8')
    if marker not in text:
        path.write_text(text.rstrip()+'\n\n'+addition.strip()+'\n',encoding='utf-8')


def main() -> None:
    root=ROOT/'formalization/Bgs.lean'
    text=root.read_text(encoding='utf-8')
    line='import Bgs.PellEchoWeights'
    if line not in text.splitlines():
        root.write_text(line+'\n'+text,encoding='utf-8')
    paper=ROOT/'manuscript/arithmetic_cat_map_moments.tex'
    text=paper.read_text(encoding='utf-8')
    anchor=r'\begin{thebibliography}'
    if text.count(anchor)!=1:
        raise RuntimeError('unexpected bibliography structure; no manuscript rewrite performed')
    include=(r'\IfFileExists{manuscript/pell_weighted_echo_section.tex}'
             r'{\input{manuscript/pell_weighted_echo_section.tex}}'
             r'{\input{pell_weighted_echo_section.tex}}')
    if include not in text:
        paper.write_text(text.replace(anchor,include+'\n\n'+anchor),encoding='utf-8')
    append_once('README.md','## Weighted Gaussian arrays and the quantum echo',r'''
## Weighted Gaussian arrays and the quantum echo

The [weighted tracial limit and echo theorem](mathematics/pell_weighted_gaussian_echo.md) allows arbitrary uniformly bounded real coefficient arrays, with ordered mixed moments governed by their empirical Gram matrices. The proof uses reciprocal-relation counting and summable Weyl phases, not an independence assumption.

For `epsilon=tau/sqrt(2K)` and `t/K -> alpha=m+a`, `0<=a<1`, the actual echo operator `U_epsilon^t U_0^(-t)` has a wrapped-normal spectral limit of angular variance `tau^2[m^2+(2m+1)a]`. Its finite-dimensional tracial limit is `exp(i tau Y(alpha))`, where `Y(m+a)=m B(1)+B(a)` for one Brownian path repeated across periods. This describes persistent arithmetic memory, not independent fresh noise each period.

The proof does not assert a sample-path convergence theorem, a joint eigenvalue law for noncommuting finite matrices, or positive microscopic BGS. The time scale remains O(log N) and the classical kick tends to zero.

The [coefficient Lean module](formalization/Bgs/PellEchoWeights.lean) contains only cleared algebraic weight identities. Its successful build must be checked separately and does not formalize the analytic theorems. Run `python computations/verification/pell_weighted_echo_regression.py` for exact coefficient and covariance checks plus finite intermediate-time and negative-time operator comparisons.
''')
    append_once('record/claim_ledger.md','## Weighted echo extension, 2026-09-05',r'''
## Weighted echo extension, 2026-09-05

PROJECT PROOFS: bounded-array weighted tracial Wick limits; normalized Hilbert--Schmidt asymptotic commutativity; an explicit finite interaction-picture normal form; and the finite-dimensional periodic Brownian echo limit, with variance `m^2+(2m+1)a` at time fraction `m+a`.

SCOPE: these are same-observable/operator tracial statements at bounded recurrence times, not independent-eigenvalue laws, path-space convergence, fixed classical-strength BGS, or a priority certificate. The six Lean coefficient identities are a strictly narrower formalization target. A successful build is required before calling those identities machine-checked; the analytic limit is not declared Lean-proved.

Finite verification sources include intermediate times, negative times, the circle seam in coefficient indices, and the three-half-period variance 5/2. Numerical finite traces are retained even when they differ appreciably from their limiting values. Actual pass/fail status belongs to the generated execution manifest.
''')
    append_once('mathematics/results.md','## Weighted tracial arrays and periodic-memory echo',r'''
## Weighted tracial arrays and periodic-memory echo

[Complete proof](pell_weighted_gaussian_echo.md): mixed Wick moments for arbitrary bounded coefficient arrays; quantitative asymptotic commutativity; finite echo comparison; and a periodic Brownian finite-dimensional tracial limit. The first-cycle variance is linear, while integer-return variance is quadratic in the cycle count. These results retain the shrinking-kick and bounded-recurrence-time assumptions.
''')
    print('Weighted echo source integration complete; verification status is not inferred.')


if __name__=='__main__':
    main()
