# BGS research brief

**Current scientific status, 11 October 2026:** the unchanged fixed-strength
microscopic BGS claim and the every-fixed-order TRACE-005 hierarchy are open.
This page summarizes established conclusions and exact missing implications.
The [claim ledger](record/claim_ledger.md) is the status authority; a dated
review or an attached manuscript cannot override it.

## Maximal paths and source continuation, 11 October 2026

[TRACE-071](mathematics/laplace_path_transport_20261011.md) transports the entire centered
phase-ensemble local point-process path and every fixed normal-source product.
[TRACE-072](mathematics/deterministic_path_transport_20261011.md) gives the deterministic
maximal time-average bound and the actual-map growing interval. The initial
local law remains unidentified. [The complete disposition](record/chat_integration_20261011.md)
also indexes reconstructed physical-source covariance, conditional joint delays,
clock obstructions, signed finite-field collisions and frozen circular laws.

## Model and complete target

The maintained odd-dimensional family is
$U_N=e^{i\tau N A_N}M_N$, $\tau=10^{-80}$, with ordinary Weyl convention and
cat matrix $\bigl(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\bigr)$.
[The model proof](mathematics/fixed_map_resolvent_frontier.md) fixes the symbol,
normalizations, symmetry qualifications and exceptional dimensions.

TRACE-005 asks for signed weighted factorial joint-trace comparison at
Heisenberg powers, for every fixed order and every smooth compact Fourier
weight. The modulus is taken outside the complete normalized sum. The
[exact bridge](mathematics/trace_to_local_statistics_bridge.md) states the
additional positivity and extension hypotheses needed for local correlations.
The necessary pair reference is

$$\frac1{N^2}\sum_{n\ge1}e^{-2sn/N}|\operatorname{Tr}U_N^n|^2
\longrightarrow\frac{1-e^{-2s}}{4s^2},\qquad s>0.$$

Shrinking-coupling returns, arithmetic averages, coordinate-phase ensembles
and noisy dynamics have their own conclusions. Their comparison with this
particular frozen propagator must itself be proved.

## Established conclusions by mathematical role

| Role | Maintained theorem sources | Exact scope |
|---|---|---|
| Actual quantum structure | [FM-024 common commutant](mathematics/actual_seven_primary_commutant.md); [FM-025 pure-five family](mathematics/uniform_five_cluster_simplicity.md); [FM-026 multiplicities](mathematics/literal_time_multiplicity_bounds.md) | Pair commutant classified for every odd $N\ge3$ except $N=7$; separate kick-simplicity and literal-time multiplicity bounds. Full $U_N$ simplicity is not inferred from pair irreducibility |
| Intensity and paths | [FM-021](mathematics/position_chain_mixing.md); [FM-022](mathematics/reversed_path_decay.md); [three-block](mathematics/three_block_unmarking.md) and [four-block](mathematics/four_block_unmarking.md) controls | Eventual constant intensity singular gap, cyclic ramp, reverse-cycle suppression and specified distinct-port reconnections; not all noncyclic interference |
| Fixed-order Fourier sectors | [TRACE-017 WKB reduction](mathematics/factorial_wkb_reduction.md); [TRACE-019](mathematics/selected_weighted_coefficient.md); [TRACE-020](mathematics/factorial_ordered_diagonal.md); [TRACE-021](mathematics/hamming_low_switch_residual.md) | Complete reduction to named finite-order tables, selected full-weight WKB and ordered-diagonal removal, checksum-free specified low-switch removal; the signed complementary sectors remain |
| Source and insertion calculus | [TRACE-027](mathematics/weighted_phase_coherence_covariance.md); [TRACE-028](mathematics/right_frame_unmasked_pinch_hierarchy.md); [TRACE-029](mathematics/convex_pinch_weak_noise_and_deconvolution.md) | Qualified growing-window Ward control; complete unmasked separated/convex hierarchy; bounded-parameter signed stability and an actual unsigned logarithmic obstruction |
| Original common-noise rate | [FM-020](mathematics/original_channel_gap.md) | Two-copy singular gap dominates $N^{-1}$ at $u=N^{-\alpha}$, $0<\alpha<1$. This closes the original-rate question left by FM-018/019, but not nonlinear quenched control, higher-copy rates or deterministic transfer |
| Noisy local statistics | [FLOW-014](mathematics/circular_dyson_actual_start.md); [FLOW-017](mathematics/coboundary_all_order_limit.md) | Actual-start weak local law on a polynomial schedule; all fixed factorial orders and one-chain origin averages on a different superpolynomial schedule |
| Reused phase channel | [TRACE-053](mathematics/max_entry_phase_channel.md) | Full complex endpoint marks, both collision corrections, exact second-degree norm and an explicit max-entry averaged-pinching rate |
| Rational matrix inner functions | [TRACE-054](mathematics/sharp_inner_jet.md) | Self-contained noncommuting right-weighted second-jet inequality with optimal leading coefficient $4/3$ and the exact smooth-localization penalty |
| Real unitary source flow | [TRACE-056](mathematics/phase_channel_real_flow.md) | Normally absorbed unweighted scalar $L^1$ source transport, including fixed derivatives and repeated eigenvalues; anisotropic sources and mixed products are outside the conclusion |

Other maintained arithmetic, Pell/Floquet, return-law, resonance, locality and
information-theory results are indexed by [topic](mathematics/topics/README.md).
They retain their own regimes and are not automatic BGS inputs.

## Submitted article: accepted overlap and pending assertions

The [source-disposition review](literature/phase_channel_jet_sources_20261008.md)
identifies the attached 293-page PDF by hash, maps its final sections to the
maintained corpus and separates proved overlap from unreconstructed inputs.
The [8 October checkpoint](record/research_checkpoint_20261008.md) supplies
full proofs for TRACE-053/054/056 and an explicit disposition of TRACE-055.
TRACE-053 also covers the article's fixed-flatness TRACE-047 as a corollary.

The full five-primary simplicity and deep all-order cavity hierarchy are not
promoted from a summary. TRACE-057/059 now reconstruct source covariance and
physical L2 continuation. The [reviewed cavity continuation](record/cavity_continuation_20261011.md)
strengthens TRACE-060 to all fixed killed upper moments and
[uniform equality laws at every fixed order](record/clock_universality_continuation_20261011.md)
at the log^(1+kappa) cutoff. The full-depth reference measure includes
an atom explained by an exact pathwise rank bound. TRACE-073 supplies conditional
position-chain and [reversal-gap propagation](record/reversal_channel_continuation_20261011.md) at log^(3+kappa). Both require all-time entry
flatness. The all-fixed-order clock induction is now accepted after
two substantive word repairs; its uncorrected input remains preserved.
TRACE-055 remains verification-pending. The flatness probability, actual cavity
hypotheses and scalar microscopic law are further missing implications.

## Exact unresolved spectral estimates

The complete balanced coordinate-phase microscopic law remains open.
[The phase Ward identity](mathematics/phase_ward_identity.md) isolates a signed
absorbed overlap defect; [the Schur-energy reduction](mathematics/balanced_pair_schur_reduction.md)
is an independent exact description of the same pair frontier. Neither
ordinary intensity mixing nor averaged eigenbasis pinching evaluates it.

[The global switch transfer](mathematics/global_switch_transfer.md) controls
its stated damped interior. The signed marked/high-switch and undamped
endpoint, including the plateau contribution, remain unproved. Masks/source
extraction are not consequences of the unmasked insertion theorem.
[FLOW-015](mathematics/microscopic_noise_removal.md) records the deterministic
noise-removal defect without proving its vanishing. Higher factorial orders
remain part of the full target.

Known controls explain why weaker criteria do not close the problem:
[absolute all-order comparison](mathematics/signed_heisenberg_comparison.md),
[same-ensemble clock norms](mathematics/isospectral_clock_moment_control.md),
and [microscopic rounding](mathematics/microscopic_rounding_control.md).
The rounding example changes the operator and does not preserve exact
quantization; it is not a counterexample to the maintained literal family.
Exact open statements are in [open_questions.md](mathematics/open_questions.md).

## Proof, computation, and review scope

Analytic project proof, an external theorem with an exact locator, finite
arithmetic, floating diagnostics and formal kernels are distinct evidence.
The core registry is narrower than the full theorem corpus. A file inventory
is not a complete proof review; inherited analytic chains retain their
recorded review boundaries. Priority for the reconstructed inequalities is
not established.

The [11 October execution packet](evidence/executions/20261011/chat-research/fresh/README.md)
records the complete 217-check workspace snapshot, 236 maintenance tests,
23 active Lean modules / 26 Lake jobs and its 284-page manuscript build.
The [subsequent cavity packet](evidence/executions/20261011/cavity-continuation/README.md)
records the new controls and manuscript continuation at their own scope.
The [reversal extension](evidence/executions/20261011/reversal-gap/README.md)
records the current analytic review and manuscript build, and the completed
219-check/25-target CI of its preceding commit. New source acceptance is
checked on its own final commit; historical receipts retain their original scope.
The [7 October integration](record/checked_research_checkpoint_20261007.md),
[Wave2 review](record/wave2_checked_integration_20261007.md), and
[Wave3 review](record/wave3_checked_integration_20261007.md) retain their own
actual execution and applicability scopes. The dated receipts distinguish
those executions from later source changes and external journal refereeing.

[Reproduction](REPRODUCE_unified.md) · [Review policy](REVIEWING.md) ·
[Publication scopes](papers/README.md) · [Historical index](record/history/2026/INDEX.md)

<!-- Stable fragment targets retained for earlier linked research views. -->
<a id="research-brief-arithmetic-return-laws-and-the-bgs-frontier"></a>
<a id="original-ordered-two-pair-microscopic-mass-6-october-2026"></a>
<a id="question-and-choice-of-model"></a>
<a id="current-contributions-and-their-boundaries"></a>
<a id="next-decisive-research-tasks"></a>
<a id="review-package"></a>
