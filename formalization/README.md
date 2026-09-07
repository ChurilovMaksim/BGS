# Lean 4 formalization

`formalization/` is the active finite-certificate, algebraic-kernel and falsifier layer. It is intentionally smaller than the informal mathematics: a Lean theorem certifies only the proposition and scope stated in its source. The repository does not treat speculative `sorry` files as progress.

Build every active module with

```bash
cd formalization
lake build
```

`Bgs.lean` imports every `.lean` file directly under `formalization/Bgs/`. The current active import graph contains exactly the following 15 modules; `formalization/drafts/` is deliberately outside it.

| Module | Maintained scope |
|---|---|
| `CayleyCurveEnergy.lean` | finite ratio-curve/energy certificate for explicit `(p,K,a)=(53,13,10)`; not the general external curve theorem |
| `CayleyEnergy.lean` | generic/exceptional finite mixed Cayley energies, including the `K=23` non-uniformity witness |
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

Many large finite propositions use `native_decide`. They are exact kernel-checked finite statements when a real `lake build` succeeds; they do not become symbolic theorems for all primes. The September 7 unrestricted finite-Fourier theorem, Corvaja--Zannier Cayley theorem, Gaussian information-limit theorems and microscopic BGS questions are not claimed to be fully formalized by this tree.

Source presence is not compilation evidence. During the September 7 repeat audit the available local environment had no `lean`/`lake`, and the contemporary GitHub-hosted jobs ended before executing any step. Therefore that audit records static import-graph completeness, not a fresh Lean compiler pass.

Historical formal drafts remain recoverable from Git history. `formalization/drafts/TemporalCancellation.lean` is explicitly not imported by `Bgs.lean` until its compiler/proof status is promoted.