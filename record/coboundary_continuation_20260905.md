# Coboundary continuation: research and verification record

Date: 2026-09-05. The resumed pass began from source checkpoint
`b2d86ddac308929770066d9851767e8ab8cbaf66`. The research branch was created
from the then-current `aa8cf7f83734834eae947d39a0e498bbb0ac00c4` because
main continued to advance independently. No force update of main was used.

## Research tree and decisions

The first continuation checked whether the recurrence trace implied a compact
pair-statistics or moving-window-variance obstruction. That implication was
already present in the incoming Floquet notes. It was reused with attribution
to the earlier project result, not counted as a new discovery.

The new branch changes the fixed Fourier observable explicitly to a
coboundary, `H=A-Ad(U0)A`. Its first-order period average is exactly zero.
A formal BCH calculation was only a heuristic starting point: the critical
quantum exponent grows, so a proof requiring small `epsilon*||A||` would fail.
The maintained three-factor Duhamel estimate instead controls nested
commutators and remains valid for every real epsilon.

The generated observable contains two Fourier species. An attempted transfer
of the earlier collision-free pair argument is false. The structural identity
`T(z-u)=z+u`, with `u=(2,4)` and `z=(4,4)`, produces collisions over the
integers before any modular specialization. The replacement is the proved
multiplicity-two classification, including all double classes. K=3 is kept
as a negative control because it has triple keys.

The resulting second-order spectral law has critical quantum scale
`sqrt(N)*K^(-1/4)`. The corresponding classical action amplitude is still
proportional to `epsilon/N` and tends to zero. This distinction is part of
the theorem, not a qualification to be removed in summaries. The necessary
escape criterion for globally unfolded pair statistics is not a sufficient
condition for random-matrix universality.

## Direct prior art

The full primary preprint of Prosen and Znidaric, *Quantum Freeze of Fidelity
Decay for Chaotic Dynamics*, was read, including its discrete coboundary,
second-order commutator and renormalized-strength formulas. Pages 2--3 were
also visually inspected. That residual-perturbation mechanism is prior art.
The specific finite norm bound, Pell collision classification and deterministic
spectral combination require their own priority review. No world-priority or
prize-level assertion is made.

A broad recent-literature search also returned work on quantum graphs,
eigenfunction delocalization and distinctions between eigenbasis chaos and
spectral universality. None of these abstracts was used as a theorem proving
the present result. Positive BGS for a fixed nonzero classical perturbation
and Heisenberg-scale joint trace control remain separate targets.

## Executed local checks

The exact Python classifier iterates original integral T-vectors. The C++20
classifier independently iterates multiplication by `3+2sqrt(2)` after dividing
out a quadratic-ring unit. They agree at K=3,5,7,11,13,17,23,31,47,101.
All double classes, not only their total number, are checked in Python.
The generic Hermitian loop falsifiers include both signs of epsilon.
Dense actual-propagator controls use K=3,5,7 and two recurrence modes.

The extended sparse implementation uses the actual residual kick, not the
averaged effective model. It retains both recurrence modes at K=11,13 and
critical parameters 0.5 and 1. At K=13,t=1 the first real trace is about
0.6086 versus its limiting value 0.6065; the second is about 0.1004 versus
0.1353. The latter finite-size deviation is deliberately retained, not
hidden or interpreted as a simulation proof. Promoted JSON is authoritative
for the complete values and seeds.

The initial K=13 exponential-action experiment with 16 probes exceeded a
240-second local limit. It produced no successful result. The maintained
implementation uses a Chebyshev expansion with an analytic Bessel-series
tail bound, plus norm-drift checks. An independent exponential-action check
at K=11 agreed with this implementation at about 1e-13. Truncation bounds,
floating-point rounding and stochastic probe error remain separate.

An attempted broad local parallel run of historical Python verifiers was
interrupted by a time limit; the partial logs are not a repository-wide green
certificate. Targeted checks are reported as targeted checks. Source-hashed
workflow evidence specifies exactly what ran.

## First remote verification and corrected integration defect

Run `33975204783` at source `0865b7800733bb2fa19f0c60ba82fc6af9277626`
passed the new exact Python/C++ cross-check, all extended numerical checks,
and the complete imported Lean build. The log records
`Built Bgs.PellCoboundary` and `Build completed successfully (13 jobs)`.
Both the nine-page companion and the main paper compiled without horizontal
overflow. The job nevertheless correctly failed before publication: the
repository audit found two inherited C++ sources not registered in CMake,
`pell_floquet_pair_verifier.cpp` and `spectral_lattice_clustering.cpp`.
They were explicitly registered, rather than exempted from the audit.

The Lean module proves a universal integer structural identity and finite
K=11 cardinalities. Finite counts use `native_decide`; their computational
trust basis is not represented as a general analytic formalization. The
workflow checks actual command status and compiler logs with failure
propagation. Duhamel estimates, asymptotic word counting, Wasserstein limits
and microscopic consequences are not formalized in Lean by this module.

## Reproducibility and publication

The targeted workflow is `.github/workflows/coboundary-validation.yml`.
It uses an idempotent integration script, reconstructs evidence, builds every
registered C++ source and imported Lean module, rebuilds both papers, and
checks repository structure. Derived-file publication is restricted to the
research branch and guarded by its exact remote head. A separate PR/main
integration must preserve concurrent work. Successful validation manifests
record input commit, runtime versions, source hashes and the exact scope.

Local companion pages were rendered and visually reviewed, including the
weighted phase estimates and both diagnostic plots. No glyph clipping or
horizontal overflow was observed. Final remote artifacts must still be
matched to their recorded source and checksums before delivery.

A useful further direction is a joint normal form for a coboundary plus a
small non-coboundary component, and then finite Fourier observables with a
cohomological variance. This is a research target, not a theorem established
by the current files. It would not by itself replace the still-missing
Heisenberg-scale spectral comparison.
