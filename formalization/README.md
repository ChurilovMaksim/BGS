# Lean 4 formalization

**Claim ID:** `BGS-FORMAL-001`


`formalization/` is the active finite-certificate, algebraic-kernel and falsifier layer. It is intentionally smaller than the informal mathematics: a Lean theorem certifies only the proposition and scope stated in its source. The repository does not treat speculative `sorry` files as progress.

Build every active module with

```bash
cd formalization
lake build
```

`Bgs.lean` imports every `.lean` file directly under `formalization/Bgs/`. The current active import graph contains the following 17 modules; `formalization/drafts/` is deliberately outside it.

| Module | Maintained scope |
|---|---|
| `AnalyticOrbitKernels.lean` | symbolic discrete-increment growth and exact signed-action counterexample; no analytic estimates |
| `CayleyCurveEnergy.lean` | finite ratio-curve/energy certificate for explicit `(p,K,a)=(53,13,10)`; not the general external curve theorem |
| `CayleyEnergy.lean` | generic/exceptional finite mixed Cayley energies, including the `K=23` non-uniformity witness |
| `CueLoopKernels.lean` | integer positive-part cubic identity and cleared-denominator elimination; analytic hypotheses and limits are not formalized |
| `FibonacciRatioSmall.lean` | exact residual Lucas/Fibonacci ratio range `1..12`; not a formalization of Carmichael's theorem |
| `GeneralHyperbolicParity.lean` | finite Boolean/parity and explicit hyperbolic-period kernels; not the full character-theoretic spectral theorem |
| `HistoricalMobiusDegenerateFiber.lean` | concrete finite falsifier for the retracted Möbius route |
| `LocalityKernels.lean` | cleared-denominator support-strip and elementary locality/exponent-budget kernels; no semiclassical limit |
| `MagneticTraceSmall.lean` | exact affine-word histograms at `p=7,K=3` through fourth order; not the global semicircle theorem |
| `PairKeyFourthMoment.lean` | finite diagonal/off-diagonal pair-key and coupled fourth-moment count certificate |
| `PairKeySecondMoment.lean` | finite pair-key parametrization/constraint-count certificate |
| `PellCoboundary.lean` | universal integer structural identity plus finite Pell coboundary/pair-key certificates; no Duhamel or limiting law |
| `PellCohomology.lean` | cleared-denominator cohomological identities plus finite original-coordinate pair-key certificate |
| `PellEchoWeights.lean` | finite/exact algebraic kernels for Pell echo weights and their rational identities |
| `PellFourierKernel.lean` | finite/exact Fourier-kernel identities used by the Pell/Floquet branch |
| `TorusLevelSets.lean` | finite torus level-set cardinalities, orbit counts and freeness |
| `TorusScaleLaw.lean` | finite branch-scale identities |

The former isolated `CayleyExceptionalK23.lean` was folded into `CayleyEnergy.lean` so generic and exceptional controls share one implementation.

## Trust boundary

Many large finite propositions use `native_decide`. A successful build accepts
these certificates with additional trust in native compilation/evaluation;
`#print axioms` exposes generated `native_decide` axioms. They are not
independent small-kernel recomputations of the finite search. Ordinary
symbolic proofs have their separately printed dependencies. None of these
finite propositions becomes a uniform analytic or BGS theorem.

On 8 September 2026 the pinned Lean 4.33.1 archive was downloaded and its
release SHA-256 verified. The full project, including all 16 active modules,
built successfully (19 Lake jobs). `AnalyticOrbitKernels` uses no
`native_decide`: its growth lemma depends on `propext` and `Quot.sound`, and
its three concrete signed-action checks have no axioms.

This runtime exposes `/proc/self/exe` but not the per-process executable link
used by Lean. The optional Linux shim
`computations/maintenance/lean_proc_self_compat.c` redirects only that exact
self lookup. The official Lean executable and proof-checking code are unchanged.
Ordinary environments do not need this shim. See `record/referee_audit_20260908.md`
for the reproduction commands and evidence boundary.

Historical drafts remain outside the active import graph. No general analytic
asymptotic theorem is claimed to have been formalized by this build.

## Current verified build, 6 October 2026

The pinned Lean 4.33.1 build now passes for all **17 active modules**, including `CueLoopKernels` (20 Lake jobs). The [complete log](../evidence/executions/20261006/original-channel-gap/lean.log) retains printed axiom lists and the [integration receipt](../evidence/executions/20261006/original-channel-gap/integration.json) records the execution scope. Remote formalization CI also passed at `131e8aac5684f72cc993a54a46237a812a577ae9`.

This supersedes the earlier source-only/pending-build status. It certifies the maintained finite/algebraic propositions with the trust boundaries above; it does not formalize the analytic limits, the channel-gap proof, or BGS. The historical September records remain unchanged.

## Publication revision, 12 September 2026

The full pinned Lean 4.33.1 project was rebuilt successfully: 16 active
modules, 19 Lake jobs. `GeneralHyperbolicParity` now also proves
`refinement_polarization` and `nontrivial_central_parity`. Both use ordinary
`decide`; their printed axiom lists are empty. The existing invariant
refinement proof remains the finite modulo-two invariance check. These
statements certify the parity algebra used in the general return-law
construction, not its operator realization, cluster estimates, or limits.
See `record/publication_review_20260912.md` for this revision's checks.
