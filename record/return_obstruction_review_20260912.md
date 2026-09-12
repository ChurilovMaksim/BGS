# Return obstruction: scoped research review, 12 September 2026

Base checkpoint: `96b0abd6386704b7fdf4be57a2d7a5223f8161af`.
Proof: [return_trace_obstruction.md](../mathematics/return_trace_obstruction.md).

## Verdict and dependencies

The deterministic necessary-condition argument is proved as written in the
project derivation and has undergone adversarial self-review, not independent
external review or Lean formalization. Its cat-map corollaries are conditional
on the existing project return-law theorems; those long analytic proofs were
not freshly audited end to end in this revision. No priority claim is made.

The main implication uses a compact mark that changes negligibly under local
translations. Ergodicity makes its limiting coupling independent of the local
process. Intensity preservation gives uniform integrability of first local
counts, permitting the exact marked Fourier identity to pass to the limit.
A second derivation uses positive Gaussian Fourier weights and the exact
factorial trace formula. It assumes pair convergence and does not infer it
from weak process convergence.

The strengthening replaces a Fourier character by any bounded slowly varying
test. It implies spatial L1 convergence of the empirical density on every
window containing a diverging number of mean spacings. The measurable
maximizer is chosen from a countable dense Lipschitz class. The explicit
convolution error is bounded by M/D times the first moment of the test window.

## Adversarial checks

| Obligation | Outcome |
|---|---|
| Random spectra and cancellation of a global phase | Passed: a spectrum-dependent phase alignment yields expected absolute trace, not its possibly vanishing expectation |
| Maximum over growing frequency sets | Passed: select a measurable maximizing frequency; the uniform translation error is M/D |
| Unbounded local counts | Passed using first-moment uniform integrability; no second-moment inference |
| Necessity of ergodicity | Half-filled cells give a stationary intensity-one nonergodic counterexample |
| Necessity of preserved intensity | Coincident spectra converge locally to the empty process |
| Necessity of sublinear frequency | A clock has unit trace at frequency D and an ergodic local limit |
| Sufficiency of Haar return laws | Refuted by the same clock spectrum |
| Diagonal subtraction and winding terms | Retained exactly; omitting the diagonal fails in dimension one |
| Infinite harmonic sum | Limit is taken first at each finite harmonic cutoff, then by positivity |
| Unfolding invariance | Not claimed; an explicit bounded-distortion density unfolding removes the critical return obstruction |

## Research routes executed

1. Direct transfer to fixed classical strength fails at the known small-quantum-
   amplitude hypothesis: epsilon=2 pi N kappa is outside its fixed radius.
2. Existing all-orders conjugacies give fixed-strength exceptional systems;
   their arithmetic structure prevents them from being a positive universality
   route. No unjustified extension beyond those conjugacies was made.
3. The return-to-local route yields the new necessary-condition proof,
   critical-kick exclusions, the uniform low-frequency budgets, and the
   mesoscopic density implication. The positive Heisenberg-time comparison
   remains an independent missing input.

## Source comparison

Primary statements and relevant proof passages were inspected for:

- Aistleitner--Lachmann--Pausinger, arXiv:1612.05495, Theorems 1--2:
  Poissonian pair correlations, equidistribution and density-square bounds.
- Steinerberger, arXiv:1812.10458v3, Theorem 2 and its Fourier-kernel proof:
  low-frequency exponential-sum budgets. The positivity principle is prior work.
- Soshnikov, arXiv:math/0002099v4, Theorem 7 and the mixing proof, printed
  pages 39--41: the translation-invariant sine determinantal process is ergodic.

This is a targeted comparison, not an exhaustive priority review. The analytic
cat-map inputs remain identified by their repository statements.

## Executed finite checks

`python computations/verification/return_trace_obstruction.py` passes 3,000
exact rational pair identities/inequalities and 3,000 integer marked-convolution
identities over all four-site multiplicity vectors of total size 1 through 10.
Separate double-precision checks cover 80 Gaussian cases, four sine-kernel
quadratures, three half-filled-cell cases, and the clock converse control.
The largest pair/trace residual is 1.43e-14 or smaller in the recorded run.
These are finite checks, not certificates of asymptotic or ergodic assertions.

An initial numerical implementation reused a Fourier cutoff for the diagonal
winding sum. The dimension-one, broad-window case detected the inadequate
cutoff. Separate reciprocal cutoffs corrected the implementation; the exact
mathematical identity was unchanged.

## File recovery and publication

After the user's PDF report, the available local checkout was at `83b4810`,
while GitHub main still pointed to the verified publication commit `96b0abd`.
All 25 changed files were retrieved with blob-hash verification; the reconstructed
Git tree was exactly `5e40aa76044b4558349aef53b5ad0be6993084c8`.
The available older PDF had invalid cross-references and no readable trailer.
A fresh build from the restored sources passed, produced 214 pages, and was
checked by full text extraction and last-page rendering before a replacement
file was delivered. The cause of the stale checkout and damaged bytes was not
established. Later article integration is recorded by its own build manifest.

## Final execution and article integration

The restored verifier was rerun through the bounded computation runner and
the manifest validator accepted the completed execution record. The workspace
runner also passed a focused `--only return_trace_obstruction` invocation.
The complete historical Python/C++ suite was not rerun, and no new Lean build
or analytic formalization is asserted.

The canonical manuscript now includes the new proof as Section 31 and builds
to 219 pages with no rejected reference or layout warnings. Full text extraction
passed; pages 95, 96 and 99 were visually inspected. This is a layout sample,
not a complete visual or scientific audit of the collection.

Verifier SHA-256: `e68b39e1e9da8f15acaaa711aa85a63bef09a56fc93746125155fa9c9ac335a7`.

PDF SHA-256: `46aa30b0031db7bf6f649e1ab1066767d18b37b7b37e714d67ce8419526a9578`.

Generated execution results remain in `build/return-obstruction-final-audit/`;
the article build manifest is in `build/return-obstruction-paper/`.
The figure `assets/figures/return_obstruction.svg` is generated by the maintained
analysis script and displays analytic bounds, not measured spectral data.

The delivered replacement was retrieved and checked again: 219 pages parse,
the complete extracted text matches the local build byte for byte, and the
last page renders. The delivered PDF bytes differ from the local build; no
byte-identical delivery claim is made. Delivered PDF SHA-256:
`b4eb5dae8abdb8a0d5c49803f9de48e7dab0cff8c9507e3affd49266950ad000`.
