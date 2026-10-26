# Lean 4 formalization

There are 29 active source modules. All 29 compiled with Lean 4.33.1 on 26 October (3075 Lake jobs, no warnings or errors), including CoherenceBudget, TraceStatement, RetTowerGeometry, Fm009TraceObstruction, Fm001Statement and Fm021Statement. See the [toolchain follow-up](../evidence/executions/20261020/toolchain-followup/README.md) for the previous receipt's source hashes, logs, adapter and exact scope. The older receipts below retain their historical scope.

**Claim ID:** BGS-FORMAL-001. This is the finite-certificate, algebraic-kernel
and falsifier layer. A Lean theorem certifies the proposition in its source;
the informal analytic corpus is substantially larger.

## Build and current receipt

From the repository root:

```sh
(cd formalization && lake build)
```

The pinned release is **Lean 4.33.1**. The
[11 October execution](../archive/evidence/executions/20261011/chat-research/fresh/lean_execution.json)
and its preserved Lake logs record **23 active modules / 26 Lake jobs**.
The hosted formalization job on main 4c2afe5 also completed the same aggregate
build without the local application-path adapter. Earlier 16-, 17-, 19- and
20-module receipts remain historical. The new cavity analysis is not formalized.

`Bgs.lean` imports every module directly under `Bgs/`. Historical `drafts/`
remain outside the active graph; speculative `sorry` files do not count as
formal progress.

The standalone `FiniteOrbitAlgebra20260922.lean` (22 September 2026) is
retained as a draft at `drafts/FiniteOrbitAlgebra20260922.lean`, outside
the active graph. It is source only and has not been typechecked; it
imports Mathlib, which this project does not vendor as in-repo sources (`lake-manifest.json` declares Mathlib v4.33.1 as a Lake dependency).

## Active modules

| Module | Maintained scope |
|---|---|
| `PhaseFrameWitness.lean` | integer determinant-one witness only |
| `TorusDimensionBound.lean` | natural-number dimension inequality only |
| `ActiveRankDefect.lean` | two natural-number rank/dimension inequalities only |
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
| `TraceStatement.lean` | TRACE-005: statement formalization only — definitions of the frozen propagator family and the criterion/first test as `Prop`s (`trace005_statement`, `trace005_k2_test`, `trace005_k2_plateau_form`); no theorems and no proofs; the claim remains open |
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
| `CoherenceBudget.lean` | natural-number budget positivity only; compiled 20 October 2026; axioms [propext, Quot.sound]; no matrix/codimension or BGS formalization |
| `RetTowerGeometry.lean` | RET-004 §3 finite certificate only: S³, 30 (RW14) separations, candidate completeness, j=1,2 emptiness, gap 37/528, area 1/288; axioms [propext, Classical.choice, Quot.sound]; no analytic RW3/RW7 or bracket formalization |
| `Fm009TraceObstruction.lean` | FM-009 implication kernel only: common reversor ⇒ trace([A,M]³) = 0; axioms [propext, Classical.choice, Quot.sound]; the nonzero computation (1) remains project proof |
| `Fm001Statement.lean` | FM-001: statement formalization only — exact Weyl dictionary (§1), Fourier weight 51451/1000 and 32-mode count (§3) as `Prop`s; no theorems and no proofs; the §2 classical conclusions (Anosov, trivial C¹ centralizer, no C¹ reversor, no affine conjugacy) are NOT stated — no C¹-diffeomorphism/Anosov API in Mathlib 4.33.1; statement definitions depend on axioms [propext, Classical.choice, Quot.sound] |
| `Fm021Statement.lean` | FM-021: statement formalization only — mixing, powers, trace/cyclic ramps and marked three-link bounds as `Prop`s, plus the §4 pair CUE target stated as open; no theorems and no proofs; statement definitions depend on axioms [propext, Classical.choice, Quot.sound] |

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
and [September review](../archive/record/referee_audit_20260908.md), retain their
original scope and provenance. A later aggregate build does not strengthen
the mathematical proposition certified by an older module.

## Checked 11 October research

The [integration disposition](../archive/record/chat_integration_20261011.md) indexes maximal microscopic paths, source transport, finite-field collision calculus and frozen circular phase laws. The global deterministic BGS and TRACE-005 claims remain open. Original receipts and fresh executions have separate scope.

The three new Std kernels PhaseFrameWitness, TorusDimensionBound and ActiveRankDefect were successfully compiled with Lean 4.33.1. They cover an integer determinant and two natural-number inequality fragments only. JackArithmeticCore remains an uncompiled Mathlib draft. The local compiler required an application-path portability adapter; its source and exact scope are in the 11 October execution packet. No kernel function is replaced.

## Coherence budget kernel, 14 October

Bgs/CoherenceBudget.lean proves only that (N-1)(N-r)>0 for natural
N>=2 and r<N. It is the arithmetic leaf of TRACE-082, not a formalization
of complex linear algebra, codimension or the Hilbert--Schmidt norm theorem.
The active entry point imports it; actual compiler execution and printed
axioms are reported in the dated spectrum/coherence evidence packet and CI.
It uses ordinary Std/omega proof terms, not native_decide or an admitted
operator statement.

The new main 57150ac formalization job was skipped after the prerequisite
jobs failed without available code-step receipts; its rerun also skipped
formalization. At that checkpoint CoherenceBudget remained without a confirmed
compiler execution; the 20 October follow-up above now supplies one. This does not change the earlier actually compiled
Std modules. See the [CI observation receipt](../evidence/executions/20261014/first-return/ci_observation.json).
TRACE-083 adds no Lean operator formalization.
