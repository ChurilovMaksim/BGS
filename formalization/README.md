# Lean 4 formalization

**Claim ID:** BGS-FORMAL-001. This is the finite-certificate, algebraic-kernel
and falsifier layer. A Lean theorem certifies the proposition in its source;
the informal analytic corpus is substantially larger.

## Build and current receipt

From the repository root:

```sh
(cd formalization && lake build)
```

The pinned release is **Lean 4.33.1**. The
[8 October log](../evidence/executions/20261008/phase-channel-jet/lean.log)
and [source-bound manifest](../evidence/executions/20261008/phase-channel-jet/run_manifest.json)
record a successful aggregate build of **20 active modules**, 23 Lake jobs.
This is the current build scope; earlier 16-, 17- and 19-module receipts are
historical. It is not a new execution reported by this documentation revision.

`Bgs.lean` imports every module directly under `Bgs/`. Historical `drafts/`
remain outside the active graph; speculative `sorry` files do not count as
formal progress.

## Active modules

| Module | Maintained scope |
|---|---|
| `PhaseChannelJetKernels.lean` | TRACE-053/054 integer coefficient and Fourier trace-defect implications only; no matrix/analytic identities or limits |
| `AnalyticOrbitKernels.lean` | symbolic discrete-increment growth and exact signed-action counterexample; no analytic estimates |
| `CayleyCurveEnergy.lean` | finite ratio-curve/energy certificate for explicit `(p,K,a)=(53,13,10)`; not the general external curve theorem |
| `CayleyEnergy.lean` | generic/exceptional finite mixed Cayley energies, including the `K=23` non-uniformity witness |
| `CueLoopKernels.lean` | integer positive-part cubic identity and cleared-denominator elimination; analytic hypotheses and limits are not formalized |
| `SevenPrimary.lean` | FORMAL-003: 22 executable GF(5) array predicates, 7 products and 46 factor occurrences; native-evaluation trust, generic Rabin/array interpretation and actual commutant theorem unformalized |
| `FourCutKernel.lean` | bounded rank-two four-cut predicates: 3858/560 pair cases, 650/0 oriented triples; m=4 exclusions; native-evaluation trust for full ranges, no abstract or analytic reduction formalized |
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

The former isolated `CayleyExceptionalK23.lean` was folded into
`CayleyEnergy.lean`; generic and exceptional controls share one implementation.

## Trust boundary

Large finite propositions in several modules use `native_decide`. Their
acceptance includes trust in native compilation/evaluation; printed axiom
lists expose those dependencies. They are not independent small-kernel
recomputations of the finite search. Ordinary symbolic proofs retain their
separately printed dependencies.

The four new `PhaseChannelJetKernels` implications use `omega`, no `sorry`
and no `native_decide`; printed axioms are `propext` and `Quot.sound`.
They certify coefficient arithmetic, not rational-inner matrix analysis.
[The seven-primary certificate note](seven_primary_certificate.md) states
its exact finite semantics and unformalized bridges. No active module proves
the general analytic limits, eigenvector-overlap estimate or BGS.

## Runtime and historical evidence

Ordinary environments use `lake build` directly. The optional Linux shim
`computations/maintenance/lean_proc_self_compat.c` redirects only a missing
exact self-executable lookup in the hosted runtime; it does not change the
Lean executable or proof checker. The
[execution packet](../evidence/executions/20261008/phase-channel-jet/README.md)
records the actual command and verified release-archive digest.

Earlier receipts, including the [seven-primary aggregate build](../evidence/formalization/seven_primary_20261006/aggregate-build.json)
and [September review](../record/referee_audit_20260908.md), retain their
original scope and provenance. A later aggregate build does not strengthen
the mathematical proposition certified by an older module.
