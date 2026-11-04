# Lean 4 formalization

The active source graph consists of **33 modules listed below**
(29 pre-existing modules and 4 fixed-diagonal-kick modules added in PR #56),
**39 adapted Aristotle/Mathlib modules** and **32 further finite-certificate
modules imported directly by `Bgs.lean`** (listed below; 20 on main plus `LineE.lean` and
`LineEResonance.lean` added in PR #57, `LineF.lean` and `LineG.lean` added for Lines F and G, `LineH.lean` added for Line H, `LineI.lean` and `LineIArith.lean` added for Line I, `LineJArith.lean` added for Line J, `LineKFinite.lean` added for Line K, `LineLConst.lean` added for Line L, and `LineMArith.lean` and `LineNArith.lean` added for Lines M and N; the five Line D orbit-pair modules `LineDDefs`, `LineDOrbitPair`, `LineDBridge`, `LineDParity`, `LineDOrbitPairFull` added on main in b96ef6bd the twelve Line B / Line D modules added on main in 0a6a798b and 121df8b4, and `LineBTraceM1` added on main in 64559f4b are imported by `Bgs.lean` but not yet counted here), with **102 leaf modules**
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

All 29 earlier leaf modules were compiled on 26 October (3,075 Lake jobs), including `CoherenceBudget`, `TraceStatement`, `RetTowerGeometry`, `Fm009TraceObstruction`, `Fm001Statement` and `Fm021Statement`; see the [toolchain follow-up](../archive/evidence/executions/20261020/toolchain-followup/README.md) and its exact scope.

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
| `LineI.lean` | `Bgs.LineI` (BGS-TRACE-212): the finite algebra of the dilation-coset L² law: `cross_term`, `sum_N_sq` (Σ_u N(u)² = d³ + d² − d), `coset_decomp`, and the norm counts `norm_count_7` (Z/7) and `norm_count_23_zero` (Z/23). The Fourier step, the congruence P ≡ y′Nm(α_n) and Prop I2′ are paper proofs. |
| `LineIArith.lean` | `Bgs.LineIArith` (BGS-TRACE-212, 219; BGS-TRACE-216 cites `seven_dvd_nsw_iff` only as an auxiliary fact): the Pell identity h_m² − 2U_m² = (−1)^m, `two_isSq_mod` (ε = +1 for odd m), `seven_dvd_nsw_iff` (7 ∣ h_m ↔ m ≡ 3 mod 6), `lucasU_two_mul` (U_2m = 2h_mU_m), `primitive_dvd_nsw` and `finite_set_fails`. The primitive-divisor theorem (Bilu–Hanrot–Voutier) is an explicit **hypothesis** and is not formalised. No certificate numbers enter Lean. |
| `LineJArith.lean` | `Bgs.LineJArith` (BGS-TRACE-221, 224, 228, 230; arithmetic cores only): `rank_core` (for a unit ε of a commutative ring and odd m, ε^m + (−ε⁻¹)^m = 0 ↔ (ε²)^m = 1), `pell49_period` and `pell49_periodic` (the coordinates of (1+√2)^m mod 49 have exact period 42), `pell49_lambda_order` (λ has order 21 mod 49), `count_excl_one` and `count_units` (q − 2 and q − 1 residues in ZMod q), `window_step` (real-line stepping core of the window lemma) and `window_N` (⌈2π/1.130677114⌉ = 6, (2π − 1.131054118)/θ ≤ 5). The sector law, the certificates, Theorem J, L16, inheritance, J3 and the passage to ℤ[√2]/q are **not** formalised. |
| `LineKFinite.lean` | `Bgs.LineK` (BGS-TRACE-234, 235; finite inputs only; Lean core, no Mathlib import, kernel `decide`): `sieve_enumeration` and `sieve_survivors` (the subsets of {3, 5, 11, 13, 17, 19}: exactly 9 possible failures, each with 56(F+1)/A_low ≤ 2645), `big_prime_excluded` (the ℓ = 23 inequality), `bprime_ge` (3 ∣ b, b ≥ 1339 ⇒ b/3 ≥ 447), `sixth_lt_A` (1/6 < 18001/100000), `noFrac_sound` and `no_small_denominator` (no fraction a/b with 1 ≤ b < 1339 in the widened enclosure [0.88797590, 0.88797628] of arg ξ/2π, as in Line J), `exceptions_excluded` (none for b ∈ {1512, 560, 1680, 616, 1848, 2520}) and `gaps_447` (gap ≤ b′/6 for 447 ≤ b′ ≤ 466). `#print axioms`: none, or `propext`/`Quot.sound` only. The full gap range 447 ≤ b′ ≤ 2645 is checked by the author's 62 `decide +kernel` chunk files in `computations/verification/lineK/lean/` that are **not** part of `lake build Bgs` (memory: a 100-modulus chunk needs 12 GB or more); 61 were recompiled sequentially at integration, and chunk 1547..1646, which exceeded the 15 GB box, was re-checked as five 20-modulus chunks with identical definitions (`evidence/executions/20261031/lineK/lean_gaps/`). The inclusion–exclusion inequality, the monotonicity step for ℓ > 23, the arb bound 0.18001 ≤ A and Theorem K3 itself are **not** formalised. |
| `LineLConst.lean` | `Bgs.LineL` (BGS-TRACE-251, 258, 260, 261, 264, 265; scalar constants only; Lean core, no Mathlib import, `decide` on natural numbers): `propS_const` ((1.28359/1.9154712)^30 ≤ 6.1·10⁻⁶, Prop S), `rate_*_lt_target` and `delta8V` (the arb upper ends of the four certified OP rates are below the targets; δ_OP(8V) ≥ 0.0162), `barrier8`, `barrier16` ((G/T)² ≥ 3.4074 and ≥ 2.5832 from G ≥ 2.3693985), `sqrt2_lower`/`sqrt2_upper`, `hpair`, `h9`, `h21`, `h_norm`, `barrier_above_h`, `barrier_above_h21` (h_9 = 1393, h_21 = 54608393, 2.5832 > 1 + √2, h_21 < 2.5832^21; L2-F1), `lambda_gt_five` (λ > 5, Cauchy bound), `B1_const` ((L/(L−1))² ≤ 1.4572 at L = 5.828427 ≤ λ), `B2_const` (1.4923³ ≤ 3.3234); Line L3 (BGS-TRACE-264, 265): `L3_S3_identity` (h_{3p} = h_p(4h_p² + 3) for p = 5…23), `L3_F2_seven` and `L3_F2_49` (gcd(h_p, K_p) = 1 and 7 ∣ K_p for p = 5…23, 49 ∣ K_7), `L3_F1_rate` ((1 + √2)/1.28359 ≥ 1.8808). `#print axioms`: none. The arb certificates (OP, the bound on G = Σ\|J_n(1.8)\|), the monotonicity of x/(x−1) and every analytic lemma are **not** formalised. |
| `LineMArith.lean` | `Bgs.LineM` (BGS-TRACE-269, 272, 277; referee file `computations/verification/lineM/referee/lean/LineMArith.lean`, namespace renamed; imports `Bgs.LineIArith`): `three_not_dvd_nsw` (3 ∤ h_m for odd m), `pp_eq`, `strong_div_small` (gcd(h_m, h_n) = h_gcd(m,n) for odd m, n < 60), `three_small`, `triple_small`, `nsw_three_mul` (h_{3m} = h_m(4h_m² + 3)), `coprime_core` ((h/d)(h/d′) ∣ h for coprime cofactors), `lam_pow_eq` (λ^p = 1 + 2h_pε^p for odd p, a ring identity in ℤ[√2]). `#print axioms`: at most `propext`, `Classical.choice`, `Quot.sound`. The LTE valuation step, the inclusion rule and the Line F bound are **not** formalised. |
| `LineNArith.lean` | `Bgs.LineN` (BGS-TRACE-279, 280, 283, 285; referee file `computations/verification/lineN/referee/lean/LineNArith.lean` plus `theta8V`; `import Mathlib`, `decide +kernel`/`norm_num`, no `native_decide`): `fix3`, `fix5`, `fix7` (\|det(S^p − 1)\| = 4h_p² for p = 3, 5, 7), `idx` (32/8 = 4, N-F8), `c17` (4·3^{4/3} < 17.31 in the form 3⁴ < (17.31/4)³), `j2a` (2τ² − τ at three tested levels), `theta8V` (θ_F(8V) < 5.4·10⁻⁶ from 1.278387 ≥ (1 − δ_F/2)·1.28359 and μ* ≥ 1.915471). `#print axioms`: at most `propext`, `Classical.choice`, `Quot.sound`. The general index statement, the OSV/Voloch/Cochrane–Pinner/Bourgain theorems and Theorem N3 are **not** formalised. |
| `Fm001Exact.lean` | `Bgs.Fm001Exact` (BGS-FM-001, partial; Lean batch 1, 1 Nov 2026): **proves** three `Prop`s of `Fm001Statement`: `fm001_dictionary_holds` (§1, ordinary Weyl quantization of g equals A_N for odd N, termwise sign cancellation), `fm001_fourier_weight_holds` (§3, Σ(\|Re c\|+\|Im c\|)\|v\|² = 51451/1000) and `fm001_mode_count_holds` (§3, exactly 32 nonzero modes), via exact Gaussian-integer coefficients 4000·c_v and kernel `decide`. The §2 dynamical conclusions and the bounds (5) are **not** formalised. |
| `Fm009CubeArith.lean` | `Bgs.Fm009CubeArith` (BGS-FM-009, partial; batch 1): `S_cube`, `S_cube_sub_one` (S³ − I = 14·[[7,10],[5,7]]), `det_B` (−1), `det_S_cube_sub_one` (−196), `det_unit_of_coprime` (I − S³ invertible mod N for gcd(N,14) = 1). With `Fm009TraceObstruction` this is the linked FM-009 kernel; the nonvanishing Tr[A_N,M_N]³ ≠ 0 is **not** formalised. |
| `PellModuliArith.lean` | `Bgs.PellModuliArith` (BGS-FM-036, partial; batch 1): §4 arithmetic of N + F√2 = (1+√2)^K, K odd: `pell_norm` (N² − 2F² = −1), `s_mul_F`, `s_sq`, `one_add_s_pow`, `h_facts` (s = 2F = F⁻¹, s² = 2, (1+s)^K = 1, h = 3+2s, h^K = 1, h − 1 = 2(1+s) mod every m ∣ N), and for K prime, p ∣ N prime: `orderOf_h` (= K), `h_pow_ne_one`, `h_pow_ne_neg_one`. Theorem C's spectral conclusions are **not** formalised. |
| `LineLCollision.lean` | `Bgs.LineLCollision` (BGS-TRACE-248, partial; batch 1): `lam_minpoly`, `alpha_eq_zero_iff` (v(λ) = 0 ⇔ (X² − 6X + 1) ∣ v in ℤ[X]), `carry_coeff` (v_j = e_j − 6e_{j−1} + e_{j−2}), `no_small_collision_k6` (referee check, \|v_j\| ≤ 3, j = 0..5). The Green-function carry bound is **not** formalised. |
| `LineM3Const.lean` | `Bgs.LineM3Const` (BGS-TRACE-271 part (c) constants; batch 1; imports `Bgs.LineN16Arith`): `rate_ge_113287` (μ_lo²/λ^{2/3} ≥ 1.13287) and `excess_ge_111238` (μ_lo²/(λ^{2/3}·1.0184224) ≥ 1.11238; the rounded quotient 1.13287/1.0184224 = 1.11237… would not suffice). Parts (a), (b), (d), (e) are **not** formalised. |
| `LineN3Order.lean` | `Bgs.LineN3Order` (BGS-TRACE-291, order part; batch 1; imports `Bgs.LineMArith`): `norm_lam_sub_one` (N(λ − 1) = −4), `l_pow_p`, `l_ne_one`, `orderOf_l` (λ mod 𝔮′ has order exactly p for odd primes p, q, q ∣ h_p, q split via s² = 2). The twist-sequence description is **not** formalised. |
| `LineN4Gauge.lean` | `Bgs.LineN4Gauge` (BGS-TRACE-297, partial; batch 1): `gauge_T` (L_τT_σ = T_{λσ}L_{τ−κλσ}), `gauge_G` (L_τG_ν = G_{ν/λ}L_{τ+ν/λ}), `T_G_comm` (T_σG_ν = e(νσ)G_νT_σ, referee N4-F1), for arbitrary weights and all functions ℂ → ℂ (tsum form). The geometric-twist corollary is in `LineN4GaugeTwist.lean` (batch 2). |
| `LineN4GaugeTwist.lean` | `Bgs.LineN4GaugeTwist` (BGS-TRACE-297 corollary; Lean batch 2, 1 Nov 2026; imports `Bgs.LineN4Gauge`): `twist_step`, `twist_product` (Π_{i<n} L_{τ_i} = T_{−λσ_{n−1}} G_{−bλ^{1−n}} L_{t₀}^n G_{λb} T_{σ_0} for τ_i = t₀ + aλ^i + bλ^{−i}, σ_i = −aλ^{i−1}/κ, ν_i = bλ^{1−i}, by induction; scalar exactly 1 in this ordering), `endpoints`, `twist_product_up_to_scalar`. The disc-space (small-gauge) reading is **not** formalised. |
| `LineIPhaseSplit.lean` | `Bgs.LineIPhaseSplit` (BGS-TRACE-211, partial; batch 2): `phase_split` (Z(ν₀ + δ) = Z(ν₀)σ̂(δ) for every integer δ), `sigma_mass` (Σ_p σ(p) = 1), `e_shift`, `e_intCast`, for a finitely supported kick and any modulus M = 2h. The absolutely summable (infinitely supported) kick is **not** formalised. |
| `LineIAliasing.lean` | `Bgs.LineIAliasing` (BGS-TRACE-218, first identity; batch 2): `geom_root_sum` (Σ_{ν<q} e(−νk/q) = q·1[q ∣ k]), `Z_mul_conj`, `aliasing_mean` ((1/q)Σ_ν \|Z(ν/q)\|² = Σ_{n,n′} Φ̂(n)conj Φ̂(n′)1[q ∣ P(n) − P(n′)] = Σ_j C_Z(jq)), finitely supported kick. The Möbius formula for F_m is **not** formalised. |
| `LineJ3PrimeLevel.lean` | `Bgs.LineJ3PrimeLevel` (BGS-TRACE-229, character-sum step; batch 2): `sum_inv_units` (Σ_{t∈F_q^*} e(Nt̄/q) = −1, N ≠ 0), `W_nonisotropic`, `W_nonisotropic_norm` (\|W\| ≤ 2/q²), `W_isotropic` ((q − 2)/q²), `Wfull_nonisotropic`, `Wfull_isotropic` (no missing label). The completing-the-square identity, the label covering and the isotropic count are **not** formalised. |
| `ResonanceMarginConst.lean` | `Bgs.ResonanceMarginConst` (BGS-RES-023, final arithmetic step; batch 2): `B` (the deposited margin integer, verbatim), `B_bit_length` (2^711 ≤ B < 2^712), `B_le_two_pow_714`, `nd10_of_margin` (Γ ≥ (π²/41472)2^{−2B}X ⇒ Γ ≥ (π²/41472)2^{−2^715}X). The certificate replay and the compilation of B are **not** formalised. |
| `LineLLineOrth.lean` | `Bgs.LineLLineOrth` (BGS-TRACE-259, 267, partial; Lean batch 3): model `O/q = 𝔽_q × 𝔽_q`, `𝔮 = ker(a + b√2 ↦ a + sb)`, `ℓ(𝔮)` its annihilator: `mem_ell_iff`, `sum_ell` (ℓ(𝔮) is a line of q points), `line_orth` ((1/q)Σ_{β∈ℓ(𝔮)} e(Tr γβ/q) = 1[γ ∈ 𝔮]), `lemmaQ` (Lemma Q for absolutely summable c), `norm_dvd_of_mem` (q ∣ Nm γ on 𝔮), `lemmaA1_parseval` (Σ_{β∈ℓ(𝔮)}\|Ẑ_β\|² = qΣ_u\|A(u+𝔮)\|²), `lemmaA1_CS` (\|D_𝔮\|² ≤ (1 − 1/q)C_𝔮). The collision form of C_𝔮 is in `LineLCollisionForm` and the c₀ closure of Lemma Q in `LineL3Quadrature` (batch 4); the block-energy use is **not** formalised. |
| `LineIMoebius.lean` | `Bgs.LineIMoebius` (BGS-TRACE-218, Möbius part; batch 3): `sum_moebius_divisors`, `sum_units_moebius` (Möbius sieve over units mod M), `Fm_moebius` (F_m = φ(2h)⁻¹Σ_{e∣2h}μ(e)(2h/e)Σ_{pairs}1[(2h/e) ∣ ΔP]), finite support. |
| `LineISummable.lean` | `Bgs.LineISummable` (BGS-TRACE-211, 218; batch 3): `phase_split`, `sigma_mass` and `aliasing_mean` for kicks with Σ\|Φ̂\| < ∞ (tsum form). |
| `LineJ3GaussSquare.lean` | `Bgs.LineJ3GaussSquare` (BGS-TRACE-229; batch 3): `completing_square` (G_t(β) = e(t̄ Nm β/q)G_t(0)), `g_normSq`, `gauss_normSq` (\|G_t(0)\|² = q²), `conj_G_mul_G`, `W_eq` (Gauss-sum weight = the batch-2 W), `two_isSq`, `card_isotropic` (#{β ≠ 0 : Nm β = 0} = 2(q − 1)). The label covering is **not** formalised. |
| `LineIMonomial.lean` | `Bgs.LineIMonomial` (BGS-TRACE-216, partial; batch 3): automaton tables of the eight (m mod 24, a = ±2) cases exported from `sym_v3/monomial_intertw.py` (generator in `evidence/executions/20261101/lean_batch3/scripts/`), `case_*`/`reflection` (intertwining relations, `decide`), `monomial_intertwines`, `X_mul_star`, `matrix_*`, `unitary_*` (X A = A′X, X Xᴴ = 1). The table derivation and the infinite-dimensional consequences are **not** formalised. |
| `LineCDFTStar.lean` | `Bgs.LineCDFTStar` (BGS-TRACE-143, partial; batch 3): `M_eq` (M_N = ΔF_{1/4}Δ), `P_F_eq` (PF_{1/4}P⁻¹ = F), `conj_DFT` ((PΔ)(D_θM_N) = (D_θ′F)(PΔ)), `PDelta_unitary`, odd N. The measure statement, Remark 1′ and the numerics are **not** formalised. |
| `Fm026Counts.lean` | `Bgs.Fm026Counts` (BGS-FM-026, bookkeeping only; batch 3): `count_integral`, `special_4375` (4200 + 18·7 + 7 = 4333), `special_109375` (105000 + 324·7 + 175 = 107443), `core_875`. The multiplicity and splitting certificates are **not** formalised. |
| `LineBTorsionSplit.lean` | `Bgs.LineBTorsionSplit` (BGS-TRACE-178; batch 3): `torsion_split` (F = F_gen + F_tor for the Prop C double sum with any pair weight). Prop C and the numerical values are **not** formalised. |
| `LineGDilution.lean` | `Bgs.LineGDilution` (BGS-TRACE-204, partial; batch 4): `square_identity` (t Nm γ + Tr βγ = t Nm(γ + t̄ conj β) − t̄ Nm β on O/d, any modulus d), `completing_square` (G_t(β) = e(t̄ Nm β/d) G_d(t)), `dilution` (d⁻²Σ_β Ẑ(β)G_t(β) = (G_d(t)/d²)Σ_β e(t̄ Nm β/d)Ẑ(β)), `sum_neg_invariant`. Prop I2′ is an input; \|G_d(t)\| = d only at primes (`LineJ3GaussSquare`). |
| `LineN3SignConj.lean` | `Bgs.LineN3SignConj` (BGS-TRACE-293, partial; batch 4): `nu0_neg`, `label_neg` (t_b(−ρ) = −t_b(ρ)), `W_neg_label` (W(N, −t_b) = conj W(N, t_b)), `W_sign_conj`, `isotropic_equal`, at prime levels. Composite levels via inheritance are **not** formalised. |
| `LineL3Quadrature.lean` | `Bgs.LineL3Quadrature` (BGS-TRACE-267, partial; batch 4): `nm_eq_zero_iff` (a² − 2b² = 0 ⇔ a = b = 0), `q_le_abs_nm` (\|Nm γ\| ≥ q on 𝔮∖0), `lemmaQ_c0` (the line average is exactly c₀ without frequencies of norm ≥ q). The block-energy band is **not** formalised. |
| `LineLCollisionForm.lean` | `Bgs.LineLCollisionForm` (BGS-TRACE-254, 259, partial; batch 4): `collision_form` (Σ_u\|A(u)\|² = Σ_{v∈s−s, f v = 0} R(v)), `collision_split`, `theoremU_consequence`, `orth`/`parseval_level` (Σ_β\|Ẑ_β\|² = h²Σ_x\|A(x)\|² on (ℤ/h)², h odd), `theoremU_level` (Σ\|A\|² = 1, Σ\|Ẑ\|² = h²), `Acoset_Aw`, `Cq_collision`, `Cq_collision_exact` (C_𝔮 = 1 + Σ_{α_v∈𝔮∖0}R(v) − \|Z\|²/q). Theorem U (vanishing of R, Σ J_n(1.8)² = 1) enters as hypotheses. |
| `LineL2Decomp.lean` | `Bgs.LineL2Decomp` (BGS-TRACE-255, partial; batch 4): `A_ideal_line`, `A_qO`, `Dq_eq` (D_𝔮 = q⁻¹Σ_{ℓ(𝔮)∖0}Ẑ), `A_qO_sub`, `inter_eq` (𝔮 ∩ 𝔮̄ = qO), `Diso_eq` (D_iso = D_𝔮 + D_𝔮̄ − (A(qO) − A_tot/q²)), `Diso_fourier`. The Theorem K1 use is **not** formalised. |
| `LineIRegroup.lean` | `Bgs.LineIRegroup` (BGS-TRACE-218, regrouping; batch 4): `regroup_pairs`, `pairs_eq_tsum_CZ`, `aliasing_CZ` ((1/q)Σ_ν\|Z_m(ν/q)\|² = Σ_j C_Z(jq)), `Fm_CZ` (F_m = φ(2h)⁻¹Σ_{e∣2h}μ(e)(2h/e)Σ_j C_Z(j·2h/e)), finite support. The summable Möbius case is **not** formalised. |
| `LineMInclusion.lean` | `Bgs.LineMInclusion` (BGS-TRACE-273, inclusion step only; batch 4): `included_of_bound`, `included_all` (\|Z_ρ\|² ≥ 4mh ⇒ every d ∣ h with 1 < d ≤ √h is included). The certified Line F bound and the interval check are **not** formalised. |
| `LineJSectorConj.lean` | `Bgs.LineJSectorConj` (BGS-TRACE-222, partial; batch 5): `e_half_int`, `K_weight` ((C, a, τ) ↦ (−C, 4 − a, −τ)), `R_weight` ((C, a, τ) ↦ (C, −a, −τ)), `RK_weight` ((C, a, τ) ↦ (−C, a − 4, τ), every real τ), `trace_conj`, `prod_conj`, `trace_prod_conj` (Tr∏U conj(V_i)U⁻¹ = conj Tr∏V_i, matrices). The lattice operators and the ℓ² trace-class setting are **not** formalised. |
| `LineIHorocycle.lean` | `Bgs.LineIHorocycle` (BGS-TRACE-214, partial; batch 5): `pair_char`, `char_sum` (Σ_ν\|Z_ν\|²e(kν/M) = M·C(k)), `interchange`, `horocycle_all` ((a)), `horocycle_units` ((b), Ramanujan sums), finite support, Σ\|c_k\| < ∞. |
| `LineIReduction.lean` | `Bgs.LineIReduction` (BGS-TRACE-213, 317, partial; batch 5): `reduction` (W′_m = φ⁻¹Σ_{non-res}(\|Z_ν\|² − RMT) + φ⁻¹ΣDev_d(ρ), disjointness assumed), `rmt_le`, `NR_ge`, `Dev_ge`. The disjointness proof and (E″), (T″), (D) ⇒ R′ are **not** formalised. |
| `LineIMoebiusSummable.lean` | `Bgs.LineIMoebiusSummable` (BGS-TRACE-218, summable Möbius; batch 5): `FmS_moebius` (Möbius formula for Σ\|Φ̂\| < ∞, pair series). |
| `LineN3SignConjComposite.lean` | `Bgs.LineN3SignConjComposite` (BGS-TRACE-293, composite levels; batch 5): `inherit_conj`, `prime_inherit_conj`, with the BGS-TRACE-228 inheritance as hypothesis. |
| `LineIRegroupSummable.lean` | `Bgs.LineIRegroupSummable` (BGS-TRACE-218, summable regrouping; batch 6b): `regroup_tsum`, `pairs_eq_tsum_CZS`, `aliasing_CZS` ((1/q)Σ_ν\|Z(ν/q)\|² = Σ_j C_Z(jq)), `FmS_CZS` (Möbius formula in C_Z form), for Σ\|Φ̂\| < ∞. |
| `LineIHorocycleSummable.lean` | `Bgs.LineIHorocycleSummable` (BGS-TRACE-214, summable kicks; batch 6b): `interchangeG`, `pair_charS`, `char_sumS`, `horocycle_allS` ((a)), `horocycle_unitsS` ((b), Ramanujan sums), for Σ\|Φ̂\| < ∞ and Σ\|c_k\| < ∞. |

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
[execution packet](../archive/evidence/executions/20261008/phase-channel-jet/README.md)
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
Std modules. See the [CI observation receipt](../archive/evidence/executions/20261014/first-return/ci_observation.json).
TRACE-083 adds no Lean operator formalization.
