# Temporal integration and spectral-module continuation

Baseline: ff546c6e66d3ece903f025a14ec4082ca3ecc18a. That commit added only an
unused placeholder after the earlier one-lag note; the temporal packet had
not been integrated. This pass removes the placeholder and installs the
previous packet together with the new spectral-module continuation.

## Scientific review

The temporal support proof was rechecked for both signs of the trace, all
integer orbit shifts, ordered-decomposition uniqueness, the collinear case,
and arbitrary complex Fourier phases compatible with reality. The filter
classification, exact Gram identities and finite-section estimates were
checked separately from computational regressions. The new section extends
the analysis to free temporal modules, arbitrary finite-symbol orbit-filter
gcds, a uniform one-harmonic repair crossover, all-time finite quantum cycles,
and the even-period phase/rank transition. Complete derivations and scope
restrictions are in the canonical manuscript. This is not a fresh line-by-
line referee audit of every inherited arithmetic and Pell theorem.

## Integration and corrections

The canonical master includes temporal_resonance.tex, spectral_modules.tex
and cayley_scaling.tex. The C++ replay is a CMake target. The existing
verify_workspace.py remains the orchestration entry point and now runs the
extended producer and the independent C++ replay in the required order.
The claim ledger is extended without altering the earlier arithmetic/Pell
claim scopes. Missing proof-index references and reproduction instructions
are supplied. No competing paper entry point or generated PDF is committed.

Two pre-existing TeX defects were identified from exact Git blobs:
transversality.tex (0f4d70dd54b529c6ed4449de757038a7180ee93b) lacked its final
proof-environment closure; cobfourth.tex
(f0ed97d85e230b07f2e33c79ec8cecffcfec0d13) contained E_K outside math mode,
which reproduced a fatal Missing $ error. These are repaired without changing
their mathematical inequalities; the obsolete finite-band scope sentence is
updated to point to the new theorem.

## Evidence boundaries

Fresh source/log hashes and counts are recorded in
../evidence/certificates/temporal_integration_20260906.json. The original packet
logs are not relabelled as fresh executions. Supporting exact tests do not
prove an asymptotic theorem; the proofs are separate. Dense matrix errors are
explicitly numerical. The new Lean file is a draft, not a compiled analytic
formalization. Wolfram returned HTTP 404 on retry. No remote-CI success or
complete canonical-PDF build is asserted by this record; those require their
own execution evidence.

The positive microscopic BGS theorem remains open. In particular, an all-time
identity for unperturbed commutator observables is not a joint-trace estimate
for the eigenphases of a nonlinear kicked propagator. External priority for
the specialized new theorems has not been established.
