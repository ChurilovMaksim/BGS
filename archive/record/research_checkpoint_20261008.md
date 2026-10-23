# Research checkpoint: phase memory and optimal matrix jets

**Date:** 8 October 2026. **Base main:**
`2104966cd72f5681a6c10b3a10a6d4ae00705ac1`.
**Scientific verdict:** deterministic microscopic BGS and TRACE-005 remain
open. Three subsidiary statements now have reconstructed project proofs;
the matrix jet result is strengthened to its optimal leading constant.

## Goal and exact remaining problem

The goal remains the complete correctly desymmetrized local spectral law
for the unchanged frozen map, then its appropriate generalizations and
applications. For the pair test, the required Abel form factor is

$$L_N(s)=N^{-2}\sum_{m\ge1}e^{-2sm/N}|\operatorname{Tr}U_N^m|^2
\longrightarrow\frac{1-e^{-2s}}{4s^2},\qquad s>0.$$

This necessary/reference pair target does not replace the every-fixed-order
factorial hierarchy. TRACE-005 retains every compact smooth Fourier weight,
the modulus outside the complete signed sum, the actual frozen propagator,
and the stated unfolding and symmetry obligations. No randomized, noisy,
shrinking-coupling or changing-model substitute closes it.

The phrase "all chaotic systems" also needs a precise genericity/symmetry
formulation: arithmetic exceptions are established in the literature. This
checkpoint neither claims a universal theorem without those qualifications
nor lowers the maintained fixed-model target.

## Audit coverage and the attached manuscript

The remote recursive tree and current authority files were inventoried.
All maintained mathematical Markdown sources, manuscript text sources and
formalization sources were materialized at the pinned revision. Review was
focused on the model, signed closure criterion, current phase/Ward and
unmasked insertion routes, channel extraction, and the attachment's latest
claims. This is not a line-by-line proof certification of the entire corpus.
The local materialization is a partial publication overlay, not a complete
Git checkout: the many historical evidence objects and unrelated binaries
were not silently downloaded or re-certified.

The attached 293-page PDF has SHA-256
`0f7af7c3867f6e3a179a4d2458bac18ff3dc441a6968b7e553dea40a68957090`.
Text was extracted throughout and the relevant final proof pages inspected.
Sections 1--68 were not wholesale re-certified; Sections 69--85 substantially
overlap indexed main research. Stronger arithmetic/simple-spectrum/cavity
assertions in Sections 87--88 were not imported just because the PDF labels
them verified. Its Section 89 disposition is explicit below.

| Claim | Current verdict | Exact support / missing obligation |
|---|---|---|
| BGS-TRACE-053 | Project proof, independent internal reconstruction | Full phase-path proof and positive Fejer majorant; both repeated-occupation corrections retained; degree-two identity and explicit rate |
| BGS-TRACE-054 | Strengthened project proof, independent internal reconstruction | Universal right-weighted matrix jet constant improved from 13/3 to optimal 4/3; finite factorization, singular-weight Cauchy, commutator/cubic trace expansions and Poisson identity proved explicitly |
| BGS-TRACE-055 | Verification-pending submission | Joint input/output delay barriers, killed second-clock moment <=12, ordinary-prefix stopped covariance, bad-clock control and physical-source analytic continuation need their raw proofs and hypothesis mapping |
| BGS-TRACE-056 | Direct project proof, independent internal reconstruction | Real unitary eigenphase flow, multiplicities included, and normally absorbed scalar L1 source transport; no anisotropic absorption or mixed-product conclusion |

The TRACE-055 summary has substantive formulas and a proof outline; the
reason for withholding promotion is not a claimed counterexample. It asserts
the barrier/moment estimates as reviewed inputs but does not supply their
complete derivation in the submitted text. Its claimed m=ceil(log(2N)^20)
endpoint cannot be inferred from boundary flatness alone. Even its acceptance
would compare to the original random scalar cavity, whose CUE identification
and deterministic phase removal remain separate problems.

## Evolution of the mathematical attempts

1. **Phase occupation route: closed at its genuine scope.** A naive
   permutation sum double-counts repeated labels. Reconstruction split the
   true repeated part from the repeated part of unrestricted pairings, bounded
   each by n! choose(n,2) delta, and proved endpoint peeling for arbitrary
   complex marks. The result needs maximum entry decay and a singular
   intensity gap for averaged pinching; it needs no reverse kernel.
2. **Pinching-rate route: strengthened.** Choosing
   L=floor(log(1/delta)/(8 log log(1/delta))) controls the factorial error
   uniformly and gives O(log log(1/delta)/log(1/delta)). No unspecified
   dimension-dependent moment constant is used.
3. **Scalar jet route, then noncommuting matrix route: closed.** Scalar
   Poisson energy suggests 4/3. Replacing noncommuting factors by scalar ones
   would be invalid. The successful step is the asymmetric split
   X=C+ipAP, Y=p'P-ipPA with PY=Y. Weighted matrix Cauchy cancels cross traces
   and exactly matches the cubic increment. Induction closes the general
   matrix inequality and the localized correction. A degree-two scalar
   family proves optimality even within each fixed matrix dimension.
4. **Real-flow scalar source route: closed without physical-cavity leaves.**
   Averaged pinching controls the sum of eigenphase velocity errors, including
   multiplicities. Common-phase L1 integration removes the microscopic
   resolvent Lipschitz dimension loss. This gives a direct absorbed scalar
   comparison and fixed derivatives, but does not authorize products of
   sources or an anisotropic complex flow.
5. **Universality extraction route: the proposed direct inference fails.**
   For symmetric Fourier S, the degree-two channel error is 1/m while its
   superoperator trace error is 1-1/m. Exact cubic occupations give
   6-9/m+4/m². Thus the available operator norm does not evaluate the required
   Heisenberg trace hierarchy. These examples are controls on an inference,
   not counterexamples to the actual nonlinear map.

This is a substantive stopping checkpoint, not an assertion that indefinite
iteration guarantees a solution. The successful branches have full proofs;
the unresolved branches retain their exact inputs and quantifiers.

## Verification and reproducibility

Evidence is in [the compact execution packet](../evidence/executions/20261008/phase-channel-jet/README.md).
Python checks exact phase-character quadratures in complex128, 1800
noncommuting cascade tuples, and 48 rational-inner products with 8192-point
circle quadrature and localization; 32 finite common-phase scalar-flow
controls use 16384 rotations. C++ independently enumerates 694526
words and verifies exact degree-two/three occupation numerators for m=3..40.
Wolfram evaluates the Poisson differential and count polynomial identities
to {0,0,0}. These computations are finite controls, not asymptotic proofs.

The complete pinned Lean 4.33.1 project builds: 20 active modules, 23 Lake
jobs. The new four coefficient kernels use ordinary omega proofs with
printed axioms propext and Quot.sound, no sorry or native_decide. Older
finite modules retain their explicitly reported native-evaluation trust.
The matrix analysis, stochastic limits, factorization and BGS are not
formalized. Runtime release digest and the unchanged compatibility shim
are recorded in the execution manifest.

The manuscript section contains the full matrix cascade proof and the
channel/real-flow proof mechanisms. Its build and visual checks are recorded
in the same packet. Registry/topic/dependency checks concern metadata only.
No claim is made to have re-run all historical verifiers or the complete
remote acceptance suite on this partial overlay.

## Repository organization and next mathematical work

The two reader introductions are rewritten around the problem, proved
families and exact gap. New proofs occupy three stable canonical files, with
one manuscript section and one compact evidence packet. Claim registry,
dependency graph, thematic index and status ledger are synchronized. Build
trees, executables, downloaded compiler and exploratory probes remain outside
the publication source surface. Unrelated indexed history is preserved;
deleting unread evidence would destroy reviewability, not strengthen science.

Next decisive estimates are: reconstruct TRACE-055's original-phase joint
barriers and prefix covariance; identify the resulting scalar cavity's
complete balanced local law under its actual retained law; control the signed
offcharge/marked-source remainder and undamped comparison; then prove every
fixed-order signed factorial target for the frozen map. Quantitative rates,
absorption removal and deterministic phase transfer need independent control.
The improved 4/3 jet theorem changes constants and localization accounting,
but by itself supplies none of these stochastic or spectral estimates.
