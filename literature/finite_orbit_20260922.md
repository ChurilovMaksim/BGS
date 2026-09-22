# Source and priority check, 22 September 2026

## Internal dependencies at the pinned revision

The base is `39d4e01ae6a6b3eb472ab30266b708ca71a70a16` in
`ChurilovMaksim/BGS`. The following are existing project results, not
contributions of this pass:

- `mathematics/extremal_resonance_nondegeneracy.md`: all real nonconstant
  finite Fourier polynomials have positive second-resonance variance.
- `manuscript/unified_sections/temporal_resonance.tex`: all finite-lag
  classes are independent for each real nonconstant Fourier polynomial.
- `mathematics/infinite_orbit_resonance.md`: all-member independence on
  one infinite signed orbit under the weighted Fourier M1 assumption.
- `mathematics/entire_temporal_gauge.md`: common real entire all-pass
  invariance and a one-harmonic finite-Gevrey obstruction.
- `mathematics/phase_regularized_resonance.md`, Section 2: a large-gap
  separation mechanism; the new proof gives an alternative qualitative route.

The new theorem combines pair-channel separation with a common-factor
normal form to cover every smooth observable supported on finitely many
signed orbits. The inspected prior statements do not give this conclusion.
This is a comparison with the inspected inputs, not a certified global
novelty claim about every file or the external literature.

## External mathematical background

Guy Cohen and Jean-Pierre Conze, *Central limit theorem for commutative
semigroups of toral endomorphisms*, arXiv:1304.4556.
Source checked: https://arxiv.org/abs/1304.4556 . The abstract explicitly
includes a criterion of non-degeneracy of variance for regular torus
observables. It is background, not an imported proof of our nonlinear
Poisson-bracket rigidity. The variance identity needed here is proved
directly by absolutely summable Fourier correlations.

Searches included the combinations `hyperbolic Poisson bracket coboundary
Fourier`, `toral automorphism finite orbits variance Gevrey`, and exact
Fourier-orbit / all-pass terminology. No matching external theorem was
identified in those results. That limited outcome does not establish priority;
a specialist literature review remains necessary. All-pass filtering and
rational/polynomial factorization are prior concepts.

## Current BGS bridge: exact source boundary

Paul Bourgade and Jiaoyang Huang, *Loop Equations Characterize Random Matrix
Statistics*, arXiv:2607.07617v2, 9 September 2026.
Source: https://arxiv.org/pdf/2607.07617v2 . Theorem 1.9, printed page 6,
was inspected in the PDF, including the displayed hypotheses. It assumes a
rational positive beta, particle-generated Nevanlinna functions, high-
probability events and moment integrability, and the normalized approximate
loop hierarchy for every order uniformly on compact subsets of both open
half-planes. It concludes vague convergence in distribution to Sine_beta.
For beta=2 the single-resolvent derivative term vanishes.

The repository's full normalized mixed-hierarchy reduction is consistent
with this theorem. It remains conditional: no such error bound was proved
here for the frozen deterministic matrices. Same-half-plane identities,
classical variance positivity, and a few diagonal mixed tests cannot be
substituted for the complete hypothesis. The new finite-orbit theorem does
not use Theorem 1.9 as an input and does not imply its hypotheses.
