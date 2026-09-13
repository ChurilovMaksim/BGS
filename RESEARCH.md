# Research brief: arithmetic return laws and the BGS frontier

## Question and choice of model

The long-term question is when classical chaos produces universal local
quantum spectral statistics. Hyperbolic toral automorphisms (cat maps) give an
exact setting in which classical hyperbolicity, Weyl quantization, arithmetic
returns, and perturbations can be studied together. Their simple definition
allows difficult mechanisms to be isolated with explicit constants and exact
finite checks.

Arithmetic is also a limitation: exceptional short quantum periods can
support exceptional eigenstates. This phenomenon is documented, for example,
by [Faure, Nonnenmacher and De Bièvre, *Scarred eigenstates for quantum cat maps
of minimal periods*](https://arxiv.org/abs/nlin/0207060).
A theorem about arithmetic cat maps therefore does not automatically extend
to generic nonlinear chaotic systems.

The purpose of this programme is to obtain precise return and regularity
mechanisms, identify the obstructions to universality, and determine which
estimates can survive a genuinely nonlinear perturbation. The model is a
controlled testing ground for that programme, not a substitute for its final
universality target.

## Current contributions and their boundaries

The detailed statements and proofs are in
[general_cat_return_laws.md](mathematics/general_cat_return_laws.md).
Here “proved” refers to the project derivation, subject to the internal-review
and external-validation limitations recorded in the claim ledger.

| Contribution | Scope | What it does not establish |
|---|---|---|
| Gevrey return suppression and absolute Gaussian approximation | Every fixed hyperbolic matrix in SL(2,Z), explicit odd-dimensional subsequences, each fixed finite Gevrey order, small scaled replica amplitude | Uniformity over all matrices or dimensions; arbitrary smooth symbols; fixed classical perturbation strength |
| Joint Gaussian law for period-averaged observables | Square-root logarithmic Fourier summability | Local spacing statistics of the kicked propagator |
| Sharp regularity obstruction after quantum centering | A fixed continuous symbol for each map; all smaller logarithmic exponents | Failure of universality for generic smooth nonlinear systems |
| Exact arithmetic and parity kernels | Explicit recurrence, class-count, phase, and finite-dimensional checks; selected Lean propositions | Formalization of the analytic estimates or of BGS |

The return period is logarithmic in dimension. With the manuscript convention
$\hbar_N=(2\pi N)^{-1}$, the classical action parameter corresponding to
quantum kick amplitude $\epsilon$ is $\kappa=\hbar_N\epsilon$.
The current small-amplitude return estimates therefore concern a vanishing
classical perturbation. This distinction matters when comparing with BGS.

The broader corpus contains complementary Cayley, Pell/Floquet, harmonic
transition, and fixed-strength locality results. Their hypotheses remain
separate; combining them in one manuscript does not supply a missing theorem.
See the [results index](mathematics/results.md).

The [short-return obstruction](mathematics/return_trace_obstruction.md) now
gives a necessary condition at the local-process level: an ergodic stationary
limit of intensity one requires sublinear-time returns to become Haar, and
empirical densities to self-average on every mesoscopic window. Applied to
the current shrinking-kick family, this requires K epsilon squared to diverge.
This condition is not sufficient; the clock counterexample and the effect of
density-dependent unfolding are included in the proof.
The strengthened theorem bounds the intensity of any ergodic local limit by
the essential infimum of the return density, even when first moments are lost.
The bound is sharp among abstract unitary spectra. At the free Brownian
harmonic endpoint with $0<t<4$, every ergodic local limit is empty; general
limits have a quantitative empty-component lower bound. These statements
retain the harmonic averaging and shrinking-kick assumptions.

An explicit inverse-density construction realizes the same smooth positive
return law with lattice, Poisson, or sine statistics after local unfolding.
Therefore knowing all fixed return moments cannot choose between those
statistics. The positive programme needs dynamical information about the
conditional local process, beyond its conditional first moment.

## Next decisive research tasks

1. **Independent validation and priority comparison.** Audit the general return
   proof, especially the capped-phase cluster estimate and the centered
   counterexample, against explicit source theorems. Success means a
   referee-checkable dependency chain and a precise comparison with prior work.
2. **Transfer beyond arithmetic linear dynamics.** Establish a quantitative
   statement for a specified nonlinear perturbation with fixed nonzero
   classical strength. Success requires uniform error estimates in the actual
   perturbation regime; merely substituting a growing quantum amplitude into
   a small-amplitude theorem does not qualify.
3. **Heisenberg-time spectral comparison.** Prove the needed desymmetrized
   joint-trace comparison on every compact Fourier support. The existing
   deterministic bridge explains how such input would imply microscopic
   correlation limits, but does not provide that input.

A useful outcome may be a new theorem or a rigorous obstruction that rules out
a proposed transfer mechanism. No advance is labeled a breakthrough solely
because it generalizes a finite experiment or increases computational size.

## Review package

The repository provides a canonical manuscript, proof sources, maintained
programs, a pinned formalization project, and reproducibility instructions.
The [publication review](record/publication_review_20260912.md) distinguishes
checks performed in this revision from historical evidence. External peer
review, a targeted journal article distilled from this large collection, and
a funding-call-specific application remain separate work. No funding budget,
affiliation, or external endorsement is asserted here.
