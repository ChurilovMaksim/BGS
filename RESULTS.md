# BGS programme: what was achieved

*Generated from [`record/claims.json`](record/claims.json) (registry updated 2026-11-04) and [`record/results_spec.json`](record/results_spec.json) by `computations/maintenance/render_results.py`. Do not edit by hand. This page is a summary for navigation. The registry decides every status; see [SOURCE_OF_TRUTH.md](SOURCE_OF_TRUTH.md).*

## In one paragraph

This repository studies the Bohigas–Giannoni–Schmit (BGS) conjecture for one explicitly specified quantized, kicked cat map on the torus. **The BGS limit for this map is not proved.** Fixed-strength microscopic universality (BGS-BGS-001) and the model-specific signed trace estimate that would close the gap (BGS-TRACE-005) are both **open**. Around that target, the programme registers 421 precisely scoped claims. 339 are proved at their stated scope (project proofs, many computer-assisted, many with an internal independent referee, none externally refereed). The work ran in seven phases from September to November 2026: Cayley arithmetic, Pell return laws, resonance cohomology and locality (Phase I); the structure of the fixed map, the exact trace-to-statistics bridge and noisy Dyson comparisons (Phase II); phase channels, clock laws, collision laws and obstructions (Phase III); uniform power-trace bounds for the original kick family (Phase IV); arithmetic Abel spikes and exact random-phase form factors (Phase V); the fixed diagonal kick and a computer-assisted refutation of Conjecture R at η = 2 (BGS-TRACE-179, Phase VI, Lines B–H); and the corrected mean law R′ (BGS-TRACE-206, Phase VII, Lines I–N), which remains **open and is not refuted**. The end point of Phase VII, **Theorem R♯-mod v5 (BGS-TRACE-325), is conditional**: it reduces the failure of frozen R′ along m = 3p to explicitly listed open inputs H0, H1 and H5–H8.

## Status at a glance

| Registered state | Claims | Meaning |
|---|---:|---|
| proved | 339 | Project proof at the stated scope, including computer-assisted proofs; not external refereeing |
| verification-pending | 17 | Argument or computation exists; an independent check is outstanding |
| conditional | 22 | Proved implication from stated hypotheses that are themselves open |
| open | 42 | Conjecture, hypothesis or programme obligation without a proof |
| refuted | 1 | Shown false as stated |
| **total** | **421** | |

172 non-open claims link Lean 4 files, out of 189 modules in `formalization/Bgs`. Lean certifies the finite or arithmetic statements named in each claim boundary, not the full analytic arguments.

## Headline results

This is a selection. The complete per-claim list is [`record/claim_registry.md`](record/claim_registry.md), and the theorem families with their limits are in [`mathematics/results.md`](mathematics/results.md).

### The target: still open

These are the questions the programme set out to answer. None of them is settled.

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-BGS-001` | **open** | Fixed-strength microscopic BGS universality for the maintained frozen map | — | [fixed_map_resolvent_frontier.md](mathematics/fixed-map/fixed_map_resolvent_frontier.md) |
| `BGS-TRACE-005` | **open** | Signed Heisenberg-scale desymmetrized joint-trace estimate (the model-specific gap to BGS) | statement only | [open_questions.md](mathematics/open_questions.md) |
| `BGS-TRACE-148` | **open** | Scaling limit of the Haar diagonal-phase cat-map form factor | — | [random_phase_encounter_pairs.md](mathematics/fixed-map/random_phase_encounter_pairs.md) |

### Phase I (September 2026): Cayley arithmetic, Pell returns, resonance, locality

The earliest corpus: arithmetic and dynamical side programmes that fix the vocabulary used later.

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-CAYLEY-002` | **proved** | Cayley additive-energy reduction | yes | [cayley_additive_energy.md](mathematics/cayley-arithmetic/cayley_additive_energy.md) |
| `BGS-CAYLEY-006` | **proved** | Gaussian limits of the full Cayley–Jacobi trace | — | [cayley_trace_gaussian_limit.md](mathematics/cayley-arithmetic/cayley_trace_gaussian_limit.md) |
| `BGS-CAYLEY-005` | **open** | Sharp centered pointwise Cayley energy target | — | [open_questions.md](mathematics/open_questions.md) |
| `BGS-RET-001` | **proved** | Harmonic return law for the kicked Pell propagator | — | [pell_harmonic_returns.md](mathematics/pell/pell_harmonic_returns.md) |
| `BGS-FLOW-022` | **proved** | Critical resonance law for the kicked Pell propagator | yes | [pell_floquet_normal_form.md](mathematics/pell/pell_floquet_normal_form.md) |
| `BGS-RET-003` | **conditional** | All-orders quantum conjugacy for noncommuting return words | — | [noncommuting_return_words.md](mathematics/returns/noncommuting_return_words.md) |
| `BGS-RES-005` | **proved** | Full-lag classical Riesz gap for the frozen symbol | — | [frozen_full_lag_resonance.md](mathematics/resonance-cohomology/frozen_full_lag_resonance.md) |
| `BGS-RES-003` | **open** | All-members analytic resonance nondegeneracy | — | [open_questions.md](mathematics/open_questions.md) |
| `BGS-FM-034` | **proved** | Fixed-strength all-orders comparison for a coboundary kick | yes | [fixed_strength_locality.md](mathematics/locality/fixed_strength_locality.md) |
| `BGS-INFO-001` | **open** | Full vanishing-noise tomography transition | — | [open_questions.md](mathematics/open_questions.md) |

### Phase II (20 September – 7 October 2026): the fixed map, the trace bridge and noisy comparisons

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-TRACE-003` | **proved** | Weighted Heisenberg-scale joint-trace comparison suffices for band-limited RMT correlations | — | [trace_to_local_statistics_bridge.md](mathematics/trace-bridge/trace_to_local_statistics_bridge.md) |
| `BGS-TRACE-004` | **proved** | Every-compact-bandwidth comparison extends to Schwartz tests | — | [bandlimited_correlation_extension.md](mathematics/trace-bridge/bandlimited_correlation_extension.md) |
| `BGS-LOOP-001` | **conditional** | Full mixed loop hierarchy implies the target compact correlations | yes | [fixed_map_resolvent_frontier.md](mathematics/fixed-map/fixed_map_resolvent_frontier.md) |
| `BGS-FM-001` | **proved** | Classical symmetry exclusions for the frozen model | yes | [fixed_model_symmetry_theorem.md](mathematics/fixed-map/fixed_model_symmetry_theorem.md) |
| `BGS-FM-010` | **proved** | Every power trace is nonzero; scalar returns classified | — | [frozen_arithmetic_trace_rigidity.md](mathematics/fixed-map/frozen_arithmetic_trace_rigidity.md) |
| `BGS-FM-021` | **proved** | Position-chain mixing and cyclic ramp for the actual map | — | [position_chain_mixing.md](mathematics/fixed-map/position_chain_mixing.md) |
| `BGS-TRACE-017` | **proved** | Fixed-order WKB reduction of the factorial trace hierarchy | — | [factorial_wkb_reduction.md](mathematics/fixed-map/factorial_wkb_reduction.md) |
| `BGS-TRACE-010` | **proved** | Absolute all-order comparison against CUE is impossible (obstruction) | — | [signed_heisenberg_comparison.md](mathematics/trace-bridge/signed_heisenberg_comparison.md) |
| `BGS-FLOW-014` | **proved** | Circular Dyson relaxation and original-chain Sine2 from the actual start | — | [circular_dyson_actual_start.md](mathematics/fixed-map/circular_dyson_actual_start.md) |

### Phase III (8–19 October 2026): phase channels, clocks, collisions, obstructions

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-TRACE-068` | **proved** | Frozen circular phase laws in the three symmetry classes | — | [phase_contraction.md](mathematics/trace-bridge/phase_contraction.md) |
| `BGS-TRACE-080` | **proved** | Unconditional feedback flatness and fixed-order clock laws | — | [unconditional_feedback_flatness.md](mathematics/trace-bridge/unconditional_feedback_flatness.md) |
| `BGS-TRACE-086` | **proved** | All-order signed diagonal hierarchy implies local Sine2 and moment UI (implication) | — | [all_order_process_closure.md](mathematics/trace-bridge/all_order_process_closure.md) |
| `BGS-TRACE-094` | **proved** | Heisenberg Wick collision Poisson law | — | [wick_collision_poisson.md](mathematics/trace-bridge/wick_collision_poisson.md) |
| `BGS-TRACE-081` | **proved** | Perfect intensity mixing does not identify microscopic statistics (obstruction) | yes | [flat_spectrum_obstruction.md](mathematics/spectral-obstructions/flat_spectrum_obstruction.md) |
| `BGS-TRACE-055` | **verification-pending** | Submitted polylogarithmic deep-source hierarchy | — | [research_checkpoint_20261008.md](archive/record/research_checkpoint_20261008.md) |

### Phases IV–V (21–29 October 2026): uniform traces and arithmetic spikes

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-TRACE-113` | **proved** | Uniform power-trace bound for the original fixed-kick family (strict pressure gap) | — | [fixed_kick_uniform_trace_bound.md](mathematics/fixed-map/fixed_kick_uniform_trace_bound.md) |
| `BGS-TRACE-116` | **proved** | Compact pair test transfers through an O(N^-2) matrix error | — | [microscopic_unitary_stability_20261027.md](mathematics/trace-bridge/microscopic_unitary_stability_20261027.md) |
| `BGS-TRACE-114` | **proved** | Short traces do not determine a local law for a general quantizer (barrier) | — | [balanced_rounding_research_20261027.md](mathematics/fixed-map/balanced_rounding_research_20261027.md) |
| `BGS-TRACE-117` | **proved** | Kick-blind arithmetic spikes: Abel pair statistic stays more than 1/2 from CUE at odd Pell returns | yes | [kick_blind_arithmetic_spike.md](mathematics/fixed-map/kick_blind_arithmetic_spike.md) |
| `BGS-TRACE-124` | **proved** | Every odd modulus lies above 3/4 or below 5/7 (pure cat map) | yes | [odd_modulus_abel.md](mathematics/fixed-map/odd_modulus_abel.md) |
| `BGS-TRACE-125` | **proved** | Quadratic trace coefficient at every odd Pell return | yes | [uniform_orbit_overlap.md](mathematics/fixed-map/uniform_orbit_overlap.md) |

### Random-phase and random-kick ensembles (Phase V and Lines C, D)

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-TRACE-127` | **proved** | Diagonal random-phase form factor at times one, two and three | yes | [diagonal_phase_form_factor.md](mathematics/fixed-map/diagonal_phase_form_factor.md) |
| `BGS-TRACE-143` | **proved** | Haar diagonal-phase cat map = random-phase DFT star graph; exact encounter-pair identity | yes | [random_phase_encounter_pairs.md](mathematics/fixed-map/random_phase_encounter_pairs.md) |
| `BGS-TRACE-147` | **verification-pending** | Exact expansions to m = 12 and the fixed-m deviation from the COE tau^3 value | — | [random_phase_encounter_pairs.md](mathematics/fixed-map/random_phase_encounter_pairs.md) |
| `BGS-TRACE-149` | **proved** | Band-limited random kick: exact trace bridge E\|Tr U^m\|^2 = Psi_m(t_N) | yes | [band_limited_kick_bridge.md](mathematics/fixed-map/band_limited_kick_bridge.md) |
| `BGS-TRACE-154` | **proved** | B_m^sym < 2m for every odd m | yes | [band_limited_kick_bridge.md](mathematics/fixed-map/band_limited_kick_bridge.md) |

### Fixed diagonal kick and Conjecture R (Phase VI: Lines B, E–H)

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-TRACE-163` | **proved** | Exact Pell-norm trace formula, orbit form and kernel structure | yes | [derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-173` | **proved** | Certified exponential decay of chi_m for eta in [1, 81.574] (computer-assisted) | yes | [derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-175` | **proved** | N-average reproduces the nu-average (Theorem U) | yes | [derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-199` | **proved** | k1-kick analogue of Conjecture R fails at eta = 2 for every odd m >= 15 (computer-assisted) | — | [lifted_transfer_lineF.md](mathematics/fixed-map/lifted_transfer_lineF.md) |
| `BGS-TRACE-209` | **proved** | Conjecture R fails for the Line B kick at eta = 2: W~rest_m/m >= 1.4e4 for odd m >= 47, 3 not dividing m | yes | [lineH_49state_certificate.md](mathematics/fixed-map/lineH_49state_certificate.md) |
| `BGS-TRACE-179` | **refuted** | Conjecture R as stated (o(m) uniformly on compact eta-ranges) | — | [derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |
| `BGS-TRACE-210` | **open** | Conjecture R_NSW (along m with h_m prime) | — | [derandomized_fixed_kick.md](mathematics/fixed-map/derandomized_fixed_kick.md) |

### Frozen R′ along m = 3p (Phase VII: Lines G, I–N4)

R′ (BGS-TRACE-206) is a corrected mean law for the k1 kick at η = 2. Everything below either bounds a part of it or derives its failure from a stated hypothesis. R′ is neither proved nor refuted.

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-TRACE-206` | **open** | Conjecture R′ (corrected mean law, k1 kick, eta = 2) | — | [resonance_classification_lineG.md](mathematics/fixed-map/resonance_classification_lineG.md) |
| `BGS-TRACE-213` | **proved** | Exact reduction of R′ to (E″), (T″) and (D), none of them proved (Line I) | yes | [lineI_rprime_reduction.md](mathematics/fixed-map/lineI_rprime_reduction.md) |
| `BGS-TRACE-225` | **proved** | Theorem J: the d = 7 contribution oscillates with growth >= 1.0184224^m (computer-assisted) | — | [lineJ_d7_twisted_coefficient.md](mathematics/fixed-map/lineJ_d7_twisted_coefficient.md) |
| `BGS-TRACE-235` | **proved** | Theorem K3: S+ contains infinitely many m = 3p in every unit class mod 56 | yes | [lineK_harg_removal.md](mathematics/fixed-map/lineK_harg_removal.md) |
| `BGS-TRACE-244` | **proved** | Operator input OP for the four families (arb certificate) | yes | [lineK_harg_removal.md](mathematics/fixed-map/lineK_harg_removal.md) |
| `BGS-TRACE-257` | **proved** | H_mean implies frozen R′ is false along m = 3p (implication only) | — | [lineL_op_open_range.md](mathematics/fixed-map/lineL_op_open_range.md) |
| `BGS-TRACE-256` | **open** | Hypothesis H_mean | — | [lineL_op_open_range.md](mathematics/fixed-map/lineL_op_open_range.md) |
| `BGS-TRACE-280` | **proved** | Theorem W+: explicit range beyond Weil (only for p >= 10^264.5) | yes | [lineMN_conductor_structure.md](mathematics/fixed-map/lineMN_conductor_structure.md) |
| `BGS-TRACE-283` | **proved** | Theorem N3: scarred conductors carry the slow orbit beta = 1 | yes | [lineMN_conductor_structure.md](mathematics/fixed-map/lineMN_conductor_structure.md) |
| `BGS-TRACE-296` | **proved** | Theorem C′: unit-beta part at h_p, for p with h_p squarefree (not proved for any p) | yes | [lineN2N4_inherited_level.md](mathematics/fixed-map/lineN2N4_inherited_level.md) |

### End point of Phase VII: Theorem R♯-mod v5 (Lines N5–N21, polymer-gas route)

This theorem is conditional. It says that if the open inputs H0, H1 and H5–H8 hold and B_p ≥ κ > 0 for infinitely many primes p ≥ p_thr, then W′_{3p}/m → ∞, so frozen R′ fails along m = 3p. H2 and H4 are met and H3 follows from H1. The inputs are open, so this is a reduction, not a refutation of R′. v5 (referee lineN22) supersedes v4 (BGS-TRACE-299): B_p now also charges the bad-cluster rate A_bad^KP, so the threshold depends on H1’s constant.

| Claim | State | Result (short label) | Lean | Source |
|---|---|---|---|---|
| `BGS-TRACE-325` | **conditional** | Theorem R♯-mod v5: conditional reduction of 'frozen R′ fails along m = 3p' to H0, H1, H5–H8 | yes | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-336` | **open** | H1 (re-scoped by N20): bad-cluster joint (A,B) second moment + near-collision constants | — | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-303` | **open** | H5: composite h_p | — | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-304` | **open** | H6: inputs of Theorem C′ (explicit p0, squarefree h_p) | — | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-305` | **open** | H7*: levels other than h_p | — | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-306` | **open** | H8: wrap-around points at composite h_p | — | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-307` | **proved** | Interaction bound delta_int^core <= 5.14476e-7 (H2 met; computer-assisted) | yes | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-302` | **proved** | H4 met: core-to-true conversion of the interaction constant | yes | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-326` | **proved** | delta_true <= 5.0313e-6 for all G (computer-assisted, [CA-fp]) | yes | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-332` | **conditional** | Prop. K: H1 implies H3 (Kotecký–Preiss weight a = a(C)) | yes | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-333` | **conditional** | Gas vs Robin crossover with all rate budgets: first prime 3307 (C <= 0.082) / 1409 (C <= 8.8e-4) | yes | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-329` | **proved** | Prop. F: no unrestricted carry/torus bound gives H1 (lower bound proved; ratio numerical) | — | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-299` | **conditional** | Theorem R♯-mod v4 (superseded by v5) | yes | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |
| `BGS-TRACE-324` | **verification-pending** | Prop X′ | yes | [lineN5N18_gas_conditional.md](mathematics/fixed-map/lineN5N18_gas_conditional.md) |

## How to read this repository

* **Start here**, then go to [RESEARCH.md](RESEARCH.md) for the dated research brief, [docs/reader_guide.en.md](docs/reader_guide.en.md) (or [Russian](docs/reader_guide.ru.md)) for the mathematical introduction, and [docs/corpus_atlas.md](docs/corpus_atlas.md) for a map of every proof note.
* **Status labels.** Use only the registry state. Inside a note, [P] marks a paper proof, [CA] and [CA-fp] computer-assisted steps (interval arithmetic or floating point), [N] numerics, which are evidence and not proof, and [H] a hypothesis. A conditional theorem is exactly as strong as its weakest open input.
* **Where things live.** `mathematics/` holds proofs and their boundaries. `computations/verification/` holds reproducible checks; the `line*/` folders are frozen author and referee packets. `evidence/` holds dated receipts. `formalization/` holds the Lean 4 kernels. `record/` holds the registry, ledger and audits. `manuscript/` holds the unified PDF source.
* **Reproduce.** `python computations/verification/scientific_registry_audit.py` checks the registry. `python -m unittest discover -s computations/maintenance/tests` runs the maintenance tests. `cd formalization && lake exe cache get && lake build` builds Lean. `python computations/maintenance/build_unified_manuscript.py --output-dir out` builds the manuscript (pdflatex or tectonic). See [REPRODUCE_unified.md](REPRODUCE_unified.md).

## Known issues

* **Continuous integration was not running as of 1 November 2026.** GitHub Actions refused to start jobs on this repository (account billing). All check results quoted in recent PRs are local runs.
* **Legacy `native_decide`.** 37 uses in 8 older Lean modules (`CayleyEnergy` (2), `FibonacciRatioSmall` (2), `FourCutKernel` (2), `MagneticTraceSmall` (1), `PairKeyFourthMoment` (2), `PellCoboundary` (3), `SevenPrimary` (22), `TorusLevelSets` (3)) rely on native evaluation and therefore trust the compiler, beyond the kernel axioms. The claim boundaries disclose this. The LineB–N modules use none.
* **Hash-pinned broken links.** 24 relative links in 11 files point to paths that later moved: `literature/arithmetic_dependency_closure_20261022.md`, `mathematics/fixed-map/fractional_hamming_cancellation.md`, `mathematics/fixed-map/onestep_charge_gap.md`, `mathematics/spectral-obstructions/flat_spectrum_obstruction.md`, `mathematics/trace-bridge/balanced_pair_schur_reduction.md`, `record/audits/20261006/README.md`, `record/charge_strengthening_promotion.md`, `record/circular_kernel_route_20261004.md`, `record/frozen_algebraic_review_20260924.md` and `supplement/fixed_map/resolvent-flow/loop_test_reductions.md` are byte-pinned by seals, manifests or receipts, and `literature/bibliography.md` is generated. They are left unedited on purpose: editing them would break the pins.
* **Frozen evidence packets.** 368 verbatim, sha256-pinned packet files under `computations/verification/line*/` are outside the assertion-entry policy and the SyntaxWarning compile step ([registry](computations/maintenance/frozen_evidence_packets.json), [rationale](computations/maintenance/ASSERTION_POLICY.md)). They are evidence of what was run, not maintained entry points.
* **Thin evidence on a few registered claims.** BGS-TRACE-095 and BGS-TRACE-097 (conditional) list no verifier; their only evidence is an integrity audit recording `all_valid: false`. BGS-RES-015 (proved) cites its own source note as evidence and depends on the conditional BGS-RES-014 for a symbol identity that it recomputes directly (see its `dependency_scope`).
* **Manuscript is a summary for Lines I–N.** The unified manuscript has full sections through BGS-TRACE-210 (Line H). Lines I–N (BGS-TRACE-211..336), including Theorem R♯-mod v5, are covered by one concise chapter (`manuscript/unified_sections/lines_I_N_gas_theorem.tex`) that states the main results and their registry states; the proofs stay in the `mathematics/fixed-map/line*.md` notes and the frozen packets. The earlier claim skeleton `manuscript/unified_sections/lines_I_N_skeleton.tex` is kept unwired as history.
