# Lean 4 formalization

The active source graph consists of **33 modules listed below**
(29 pre-existing modules and 4 fixed-diagonal-kick modules added in PR #56),
**39 adapted Aristotle/Mathlib modules** and **25 further finite-certificate
modules imported directly by `Bgs.lean`** (listed below; 20 on main plus `LineE.lean` and
`LineEResonance.lean` added in PR #57, `LineF.lean` and `LineG.lean` added for Lines F and G, and `LineH.lean` added for Line H), with **97 leaf modules**
and two aggregators (`Bgs.lean` and `Bgs.Mathlib`). They share the original Lean 4.33.1/Lake project: `Bgs.lean` imports `Bgs.Mathlib`, which reaches every new module. No second project root or duplicate proof tree is maintained.

The [Mathlib coverage map](MATHLIB_LAYER_RU.md) links individual declarations to existing theorem families and their exact proof scope. The [integration receipt](../evidence/formalization/aristotle_20261027/receipt.json) separates the earlier 8,776-job Lean build and 589 public-declaration axiom checks from the later GitHub merge. This is not an independent verification of the full analytic corpus, and it does not close BGS.

**Claim ID:** BGS-FORMAL-001. This is the finite-certificate, algebraic-kernel
and falsifier layer, extended by scoped Mathlib theorems including selected scalar/reference limits. A Lean theorem certifies the proposition in its source;
the informal analytic corpus is substantially larger.

## Build and execution provenance

From the repository root:

```sh
(cd formalization && lake exe cache get && lake build Bgs)
```

Run `lake exe cache get` once per environment (or after a Mathlib pin change) to install prebuilt Mathlib oleans; reuse the same `formalization/.lake` tree across branch checkouts. The [2026-10-29 aggregate receipt](../evidence/formalization/bgs_aggregate_20261029/README.md) records a full `Bgs` build after the rational-module namespace fix on the TRACE-127 stack.

The pinned release is **Lean 4.33.1**. The previous integration environment recorded a completed build of the adapted source graph (8,776 Lake jobs, 589 declaration axiom inventories); its raw execution logs were not recoverable after the environment change. The source and historical execution digests are preserved in the integration receipt. Hosted CI did not independently validate the merged source because the repository owner reported exhausted GitHub Actions minutes. No post-merge Lean build is claimed.

All 29 earlier leaf modules were compiled on 26 October (3,075 Lake jobs), including `CoherenceBudget`, `TraceStatement`, `RetTowerGeometry`, `Fm009TraceObstruction`, `Fm001Statement` and `Fm021Statement`; see the [toolchain follow-up](../evidence/executions/20261020/toolchain-followup/README.md) and its exact scope.

The [11 October execution](../archive/evidence/executions/20261011/chat-research/fresh/lean_execution.json)
and its preserved Lake logs record **23 active modules / 26 Lake jobs**.
The hosted formalization job on main 4c2afe5 also completed the same aggregate
build without the local application-path adapter. Earlier 16-, 17-, 19- and
20-module receipts remain historical. The new cavity analysis is not formalized.

`Bgs.lean` reaches every active module recursively, including `Bgs.Mathlib`. Historical `drafts/`
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
| `LineBDerand.lean` | `Bgs.LineB.Derand`: finite `decide` certificates for the fixed diagonal kick (Lemma Q, Pell identity, \(D_m\), \(g'_m\)); no `sorry`, no `native_decide`; no analytic limit |
| `LineBPhase2.lean` | `Bgs.LineB.Phase2`: finite `decide` certificates for Theorem D at odd \(m\le 9\), symbol symmetries through \(n\le 60\), and Theorem N hypotheses at \(m=7,19\); no `sorry`, no `native_decide` |
| `LineBPhase3.lean` | `Bgs.LineB.Phase3`: norm-class invariance by `ring`, odd-symbol square, parity-lattice sums, and the \(m=7\) order check; imports `Mathlib.Tactic.Ring`; no `sorry`, no `native_decide` |
| `LineBPhase4.lean` | `Bgs.LineB.Phase4`: rational bounds by `norm_num` and the lattice relation `m3_relation` by `decide`; imports `Mathlib`; no `sorry`, no `native_decide`; not a formalization of Theorem D_cert |
| `CrtCompositeRational.lean` | Rational witness for BGS-TRACE-122: integer comparisons placing every product of two odd primes on a definite side of the Abel thresholds, plus positivity integers for the seven-family majorant; does not formalize the Chinese-remainder count, the order trichotomy, or the kick telescoping |
| `DiagonalPhaseFormFactorRational.lean` | Rational witness for BGS-TRACE-127: integer matrix factorizations for `S^2-I` and `S^3-I` and the comparisons `(2N-1)/N > 1`, `(6N^2-9N+4)/N^2 > 1` and `< 6`; does not formalize the path count, the trace closure, or the sixteen-phase sample |
| `DiagonalPhaseShortTimeRational.lean` | Rational witness for BGS-TRACE-128: integer comparisons for the symmetric error constant, the time-three gap, integer main terms at dimensions 3, 5 and 7, and the Kloosterman quadruple census at primes 5 and 7; does not sum the complex form factor |
| `HyperbolicDiagonalFormFactor.lean` | Finite certificate for BGS-TRACE-131: Cassini at ten pairs, `u 6 3 = 198`, identities `S^n = v_n S - v_{n-1} I` and `det(S^n - I) = 2 - u_n` for the listed matrices/exponents, and kernels of the reduced matrices; does not formalize `D_2` or the phase average |
| `HyperbolicShortTime.lean` | Arithmetic of integers written in BGS-TRACE-132 (`3! * 7 = 42`, `4! * 13 = 312`, `13 + 9 = 22`, `22 * 18 = 11 * 36`, `121 * 11 > 6 * 18`); does not formalize the occupation estimate, the form factor, or `D_2` |
| `KickBlindRational.lean` | Rational witness for BGS-TRACE-117: fully expanded rational inequalities, with `B = 184981/160000` as the rational majorant of `Σ |c_kl|` and `u_201` from the recurrence `(1+√2)^n = u_n + v_n √2`; does not formalize Weyl operators, the matrix exponential, or the trace comparison |
| `LineCEncounter.lean` | Line C finite algebraic core of the first off-diagonal (Sieber–Richter-type) term: kernel-`decide` certificates for `mathematics/fixed-map/random_phase_encounter_pairs.md` (BGS-TRACE-144, BGS-TRACE-145 and BGS-TRACE-146: finite instances only) |
| `MomentumPhaseCue.lean` | Rational witness for BGS-TRACE-140, BGS-TRACE-141 and BGS-TRACE-142: odd-symbol energy `9/125000`, time-three error constant `(3!)²(1+2·3·2) = 468`, time-two constant `20`, and residues `27 mod 5, 7, 11, 13` (residues at `t = 3` only); conditions `t = 1` and `t = 2` are not formalized, `p = 13` is not excluded, the form factor is not formalized |
| `OddModulusRational.lean` | Rational witness for BGS-TRACE-124: closed integer comparisons placing every odd modulus above 3/4 or below 5/7 and clearing the fixed-kick margin inside the stated windows; does not formalize the kernel expansion, the quadrant comparison, or the kick telescoping |
| `OrbitOrthogonalRational.lean` | Rational witness for BGS-TRACE-118: integer comparisons used in the quadrature spike at `N = u_203`; does not formalize Weyl operators, the matrix exponential, or the trace |
| `OrderLadderRational.lean` | Rational witness for BGS-TRACE-120: integer comparisons used to place the cat-map order on either side of the Abel threshold; does not formalize Weyl operators, the trace-square identity, or the kick telescoping |
| `OrderTrichotomyRational.lean` | Rational witness for BGS-TRACE-121: integer comparisons placing every odd prime and every odd prime power on a definite side of the Abel thresholds; does not formalize the splitting law, the kernel count, or the kick telescoping |
| `PhaseFormFactorRational.lean` | Rational witness for BGS-TRACE-126: integer table for `fCoeff` from `TraceStatement.lean` scaled by 4000 — 32 nonzero modes, Hermitian symmetry, Hilbert–Schmidt energy `66033/160000`, parity energy `663/4000000`, strict majorant `184981/160000`, unreduced reversal sum `66031/80000`, scaled zero-mode energies at primes 3, 5, 7, 11, three small prime-revival identities, and the folded symbol identity `A_7 = (9/10) I` |
| `PositiveTimeRational.lean` | Rational witness for BGS-TRACE-119: integer comparisons used in the positive-time expansion at `N = u_205`; does not formalize Weyl operators, diagram partitions, or the trace |
| `RevivalClosureRational.lean` | Rational witness for BGS-TRACE-133, BGS-TRACE-134 and BGS-TRACE-135: finite integer facts behind `mathematics/fixed-map/revival_closure_law.md`; every theorem closed by kernel `decide`, no `sorry`, no `native_decide` (per the file header) |
| `ScalarReturnBesselRational.lean` | Rational witness for BGS-TRACE-129: integer matrix orders, momentum-row energy `9/160000`, and additive quadruple counts of the position orbit; the Bessel average is not summed here |
| `SixteenPhaseSymmetryRational.lean` | Rational witness for BGS-TRACE-130: momentum-row energy `9/160000`, `det(S-I) = -4`, and the rational identity `1/4 + 1/4 = 1/2` for the momentum-sine symbol; the antiunitary is not formalized |
| `SquarefreeProductRational.lean` | Rational witness for BGS-TRACE-123: integer comparisons placing every square-free odd modulus with at least three distinct prime factors above 3/4 and clearing the fixed-kick margin inside the stated windows; does not formalize the divisibility of the orders, the least-common-multiple bound, or the kick telescoping |
| `UniformOrbitOverlapRational.lean` | Rational witness for BGS-TRACE-125: integer seeds, the 32-mode mass, the lag-1 coefficient, the exponent-1 box count, and the exhaustive support scan at `N = 41`; does not formalize the Pell induction, the archimedean embedding, or the quadratic-form descent |
| `LineDCerts.lean` | Line D finite arithmetic certificates (kernel `decide`, Lean core only, no Mathlib import) for `mathematics/fixed-map/band_limited_kick_bridge.md`: `hx_ok` (`H_m X_m = D_m I` for `3 ≤ m ≤ 8`), `fix_count` (period-`m` sequence count equals `D_m` for `m = 3, d₂ = 28` and `m = 4, d₂ = 96`), `rad_count` (`D_m / D_eff` values for `m = 3..6`), `coll4_ok`/`coll6_ok` (listed collision sequences only); does not formalize the Gauss-sum completion (Theorem D1), Fourier inversion (Prop. D3), strong-kick limit (Theorem D4), analytic bounds, or numerics; does not certify support, Γ-inequivalence, or completeness of the collision set |
| `LineE.lean` | `Bgs.LineE`: Line E resonant residue N ≡ −4 (mod h_m) (BGS-TRACE-183): Pell identity and x_d mod 4, y_d mod 2 for all d; exact coefficient congruences `cert5`…`cert21` by `decide`, control `cert11_control`; no `sorry`, no `native_decide`; the analytic IFS law and the ball-arithmetic certificates are not formalized |
| `LineEResonance.lean` | `Bgs.LineE` (step 2, audited by the second referee; BGS-TRACE-193, 194): `nsw_mod7` (7 ∣ h_m ↔ 3 ∣ m, all m) and the a = 7 resonance coefficient identities `cert49_*` at m = 5,…,19, s = ±1, by `decide`, control `cert49_11_control`; no `sorry`, no `native_decide` |
| `LineF.lean` | `Bgs.LineF` (BGS-TRACE-197): the combinatorial core of the lifted trace identity — monotone integer step maps, closed vertex chains minus closed edge chains equal one (`count_identity`, `vertex_minus_edge`), with the rounding-map hypotheses stated in each theorem. The analytic trace-class part is not formalised. |
| `LineG.lean` | `Bgs.LineG` (BGS-TRACE-203, 205): the G1 phase split over ℚ, the Pell recursion/quadratic-form identity, `nsw_dvd` (d ∣ m, m odd ⇒ h_d ∣ h_m, all m, via ℤ√2), and `decide` instances `nsw_3`…`nsw_17` with the h₁₇ factorisation. |
| `LineH.lean` | `Bgs.LineH` (BGS-TRACE-207, 209): the parity steps of the κ lemma (`h_odd`, `yp_odd`, `k_odd`, `kappa_odd`, `inv49_mod8`), the Gauss-sum residues mod 8 (`sq_residues_mod8`, `shift4`), and the generic chain lemmas `geom_tail` (monotone propagation in m) and `dom_lower` (triangle step). No certificate numbers enter Lean; the Gauss-sum evaluation, the operator theory and the arb certificates are not formalised. |

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
