# BGS research brief

## Kick-blind arithmetic spikes, 28 October 2026

[TRACE-117](mathematics/fixed-map/kick_blind_arithmetic_spike.md) proves two statements for the maintained family. The pure cat map at \(N=u_n\), for every odd \(n\ge5\), has Abel value \(L_N(M_N;1)>3/4\). The fixed kick \(\tau=10^{-80}\) preserves \(L_N(U_N;1)>3/4\) for every odd \(n\) with \(5\le n\le201\). The distance to the CUE value \((1-e^{-2})/4\) is therefore greater than \(1/2\) on those dimensions, and no effective startup \(N_0\le u_{201}\) works for every larger odd dimension. The one-term lower bound drops to at most \(3/4\) at \(n=203\).

[TRACE-118](mathematics/fixed-map/orbit_orthogonal_kick_spike.md) replaces that one-term estimate at the single dimension \(N=u_{203}\). The cat-map orbit of the \(32\) Fourier modes is trace-orthogonal except for the overlap \(\gamma(1)=-7/2000000\), and the second-order trace expansion with a third-order operator-norm remainder still gives \(L_N(U_N;1)>3/4\). The same remainder is already at least \(1\) at \(n=205\), and the Hilbert--Schmidt triangle is silent there. At \(n=207\) the pure second-order center satisfies \((1-\varepsilon_2)^2<3/4\), so the disk cannot prove the gap. Any effective startup for every larger odd dimension now needs \(N_0>u_{203}\) (78 decimal digits). This is not the \(N\to\infty\) limit. BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

[TRACE-119](mathematics/fixed-map/positive_time_spike.md) clears the next odd index by a different estimate. At the single dimension \(N=u_{205}\), a positive-time diagram expansion whose resonant diagrams remain trace-orthogonal gives \(L_N(U_N;1)>3/4\). The third-order operator-norm remainder and the Hilbert--Schmidt triangle stay silent at that index; they are not the argument. The integer \(u_{205}\) has 79 decimal digits, so the effective startup for every larger odd dimension now needs \(N_0>u_{205}\). At \(n=207\) the pure second-order center still satisfies \((1-\varepsilon_2)^2<3/4\), and no disk \(N(1-\varepsilon_2-E)\) with \(E\ge0\) proves the gap. BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Aristotle formalization integration, 28 October 2026

Adapted all 39 substantive modules from the older Aristotle snapshot into the existing Lean 4.33.1 graph. The [coverage map](formalization/MATHLIB_LAYER_RU.md) and [receipt](evidence/formalization/aristotle_20261027/receipt.json) record exact theorem scope, 589 axiom-audited declarations and the successful aggregate build. ERR-060 corrects the pure-loss scalar identity in the proof and manuscript. Current claim states, TRACE-114–116 and pinned dependencies are retained; no BGS closure is asserted.

## Trace results and dependency closure, 22 October 2026

The [review](record/spectral_research/trace_closure.md) closes the inserted-trace input in TRACE-109 by a
finite-grid corrected-amplitude proof. TRACE-110 now has proved global
$O(1/\log N)$ spectral matching and a matching Pell lower order.
[TRACE-112](mathematics/fixed-map/displacement_density_trace_bound.md) supplies an
independent logarithmic-time upper-bound route;
[TRACE-113](mathematics/fixed-map/fixed_kick_uniform_trace_bound.md) proves the
uniform power-trace input with one threshold for all iterates.
All statements have analytic project proofs with author check, not external
refereeing. Microscopic signed cancellation and BGS remain open.

## Final spectral corpus, 21 October 2026

The [thematic research edition](mathematics/spectral_research/README.md)
preserves all 535 source units of the final supplied master. TRACE-108 gives
the quartic one-step coordinate return; TRACE-111 gives the full weighted
initial gradient/Hessian and forced early inflection. The qualifications for TRACE-109/110 were closed on 22 October,
as documented above. [Complete review](record/spectral_research/spectral_final_integration.md)
and [independent remaining task](record/remaining_breakthrough_task_20261021.md).
BGS-TRACE-005 and BGS-BGS-001 remain OPEN.

## Physical-kick bounds, 21 October 2026

[Uniform trace decay and scalar-distance limits](mathematics/fixed-map/physical_kick_trace_decay.md)
(TRACE-106) and [all-order polynomial approximation with Pell alias limits](mathematics/fixed-map/physical_trace_polynomial_approximation.md)
(TRACE-107) are now recorded with full proofs. The imported exponent 1/25 is
strengthened to 1/9 for the single kick. The original microscopic trace hierarchy
remains open. [Review scope](record/spectral_research/spectral_master_audit.md).


## Integrated continuation, 19 October 2026

[TRACE-095 through TRACE-105](mathematics/trace-bridge/phase_ensemble_continuation.md)
cover the checked auxiliary phase research. The full four-port zero and total
defect-two sum are complete at the stated scope. The joint local-defect-at-most-two
sum has a quartic limit for tau<1/9 and uniform finite-size control; it retains
a nonzero -3 tau^3 term. The exact positive Cauchy projection laws do not identify
a matrix law, as shown by an explicit signed-source counterexample.
[Integration, evidence audit and next obligations](archive/record/chat_integration_20261019.md).
BGS-TRACE-005 and BGS-BGS-001 remain OPEN. Conditional G/TC/R premises remain explicit.

## Checked continuation, 16 October 2026

- **BGS-TRACE-092:** [Positive Abel decomposition and optimal square-root clock rigidity](mathematics/trace-bridge/abel_clock_rigidity.md), including stationary processes and multiple eigenvalues.
- **BGS-TRACE-093:** [Flat-sector Gaussian comparison for every m=o(N), exact Heisenberg exponential rate and collision mean](mathematics/trace-bridge/gaussian_equal_edge.md).

The Gaussian benchmark and its sinh crossover are prior results. The subsequent
[TRACE-094 proof](mathematics/trace-bridge/wick_collision_poisson.md) closes the flat
Heisenberg collision law and exact ratio B/G->exp(-alpha^2). It also gives
geometric vertex occupations and a bounded radial-entry comparison. The
physical non-flat extension and original signed BGS hierarchy remain open.
[Current proof outcome and next obligations](archive/record/wick_poisson_continuation_20261016.md).
The [earlier checkpoint](archive/record/research_continuation_20261016.md) retains its original scope.

## Research-record integration, 16 October 2026

[Exact review and 90-entry inventory](archive/record/chat_integration_20261016.md).
The all-order process implication no longer requires an independent UI premise.
The actual signed hierarchy, physical parameter moment and positive Hardy
excess limits remain unproved. Resonance deletion is sufficient only.

- **BGS-FM-032** — [Prime cyclic cohomology and parity-resolved susceptibility](mathematics/fixed-map/quantum_cyclic_cohomology.md); proved within its stated scope.
- **BGS-TRACE-084** — [Mesoscopic block number-variance criterion and collective trace-energy boundary](mathematics/trace-bridge/resonant_mesoscopic_criterion.md); proved within its stated scope.
- **BGS-TRACE-085** — [Exact root lifting and failure of necessity for resonance-sector deletion](mathematics/trace-bridge/root_lifting_sector_boundary.md); proved within its stated scope.
- **BGS-TRACE-086** — [All-order signed diagonal hierarchy implies local Sine2 and local moment UI](mathematics/trace-bridge/all_order_process_closure.md); proved within its stated scope.
- **BGS-FM-033** — [All-label-scale one-step Weyl overlap and prime-orbit corollaries](mathematics/fixed-map/scaled_weyl_overlap.md); conditional within its stated scope.
- **BGS-CUE-002** — [All-positive-frequency CUE trace-square covariance and exact coupling derivative](mathematics/trace-bridge/full_pair_cue_covariance.md); proved within its stated scope.
- **BGS-TRACE-087** — [Exact parameter bandwidth and quantitative de-averaging to a fixed coupling](mathematics/trace-bridge/parameter_deaveraging.md); proved within its stated scope.
- **BGS-TRACE-088** — [Rooted BEST count, extensive equal-edge mass and unitary compensation](mathematics/trace-bridge/equal_edge_occupation.md); proved within its stated scope.
- **BGS-TRACE-089** — [Factorially weighted square-root-time equal-edge collision crossover](mathematics/trace-bridge/collision_crossover.md); proved within its stated scope.
- **BGS-TRACE-090** — [Contractive full-spectrum radial ratios and mixed-moment weak-process criterion](mathematics/trace-bridge/bounded_radial_ratios.md); proved within its stated scope.
- **BGS-TRACE-091** — [Sharp clock minimum and exact radial and Abel Hardy remainders](mathematics/trace-bridge/hardy_spectral_remainder.md); proved within its stated scope.


**Current scientific status, 22 October 2026:** the unchanged fixed-strength
microscopic BGS claim and the every-fixed-order TRACE-005 hierarchy are open.
This page summarizes established conclusions and exact missing implications.
The [claim registry](record/claims.json) controls registered status; the
[dated ledger](record/claim_ledger.md) explains changes. A review or attached
manuscript cannot strengthen the registered claim.

## Spectral information beyond intensity mixing

[TRACE-083](mathematics/spectral-obstructions/coherent_first_return_pulse.md) evaluates
a single observed memory coefficient for the TRACE-081 family.
At time 2p it is almost an isometry on nearly all centered diagonal
directions, although its remaining monitored energy tail is at most
16 N^-6. Unconjugated first and second pulse traces can vanish while
the cubic trace stays large. Repeated completed excursions and a
later first-return coefficient are different operators. These are
abstract-family conclusions; the original physical signed source
and the BGS limit remain open.

[TRACE-081](mathematics/spectral-obstructions/flat_spectrum_obstruction.md) proves that
perfect intensity mixing, a vanishing coordinate reversal norm, simple
spectrum and a uniform macroscopic phase law can coexist with an empty
origin-averaged microscopic limit and clustered spacings. The construction
is an abstract unitary family; it is not the fixed smooth chaotic model.
[TRACE-082](mathematics/spectral-obstructions/coherence_memory_plateau.md) identifies
exact coherent return memory and proves a universal obstruction:

$$
\mathcal E=\mathcal Q\operatorname{Ad}_U\mathcal Q,
\qquad \|\mathcal E^r\|_{\mathrm{HS}\to\mathrm{HS}}=1
\quad(0\le r<N).
$$

Here Q removes the diagonal part and the norm acts on Hilbert--Schmidt
matrix space. A general early norm contraction cannot replace the missing
source-specific signed cancellation. [Exact outcome](archive/record/spectral_coherence_continuation_20261014.md).

## Full-depth clocks and microscopic paths

[TRACE-080](mathematics/trace-bridge/unconditional_feedback_flatness.md) now
proves unconditional entry flatness from any deterministic unitary startup
with intensity bound C0/N and centered singular norm at most 1/100.
Uniform ports and fresh uniform phases preserve flatness, a small intensity
gap, bounded row/column fourth-power energies and a uniform two-step bound
at every depth down to ceil(log(2N)^(4+kappa)), with failure
O(log(2N)^(-1-kappa)). Fixed-order clocks and the empirical weak law are
unconditional on that same cutoff; reversal convergence uses its separate
initial-channel assumption. The actual odd-N fixed-coupling family has
these named eventual startup inputs. The deterministic microscopic law
and BGS remain open.

[TRACE-079](mathematics/trace-bridge/two_step_stopped_concentration.md) supplies
the all-pair stopped concentration input, including the diagonal and full
first crossings. [Exact outcome](archive/record/feedback_flatness_continuation_20261013.md).

[TRACE-078](mathematics/trace-bridge/two_step_increment_variance.md) adds
an exact raw second-moment bound for the complete two-step feedback
increment: `2600 delta²[(P²)ij+(P³)ij]/u` for a uniform port and any
phases, with frozen endpoints. Its one-step bound alone does not give concentration. TRACE-079 and
TRACE-080 supply the separate stopped and global dynamic proofs.

[TRACE-077](mathematics/trace-bridge/green_compression_gap.md) linearizes
classical elimination in centered Green coordinates. Its decaying initial
compression and adapted martingale give a shrinking intensity singular
norm on the entry-stopped prefix, with quantitative failure probability.
This proves the deep-range three-step forcing estimate on reached states.
The stopped theorem alone supplies no entry-survival probability;
TRACE-080 closes it under its smaller startup-gap hypothesis.
[Exact outcome](archive/record/green_compression_continuation_20261013.md).

[TRACE-076](mathematics/trace-bridge/haar_feedback_clock_law.md) gives an exact
finite Haar scattering/delay factorization and inverse-Jacobi spectrum.
Its Haar trajectory bound closes the all-time probability premise for
that initial ensemble. Every fixed full-depth clock law and the empirical
weak law extend unconditionally to independent initial distributions
with relative entropy O(log N) relative to Haar. The
[outcome](archive/record/haar_feedback_continuation_20261012.md) distinguishes
this extension from the unresolved deterministic initial family and from
prescribed-origin microscopic universality.

[TRACE-074](mathematics/trace-bridge/unitary_two_step_obstruction.md) closes the
static unitary shortcut: flat entries and vanishing intensity singular
norm do not bound the two-step kernel by O(1/n). Its three-step positive
bound does not replace the exact entry bracket.
[The outcome](archive/record/unitary_two_step_continuation_20261012.md) separates
this obstruction from the dynamic question subsequently treated by TRACE-080 under its stated startup hypotheses.
[TRACE-075](mathematics/trace-bridge/two_step_restoring_drift.md) controls the
complete coherent term by a three-step path-swap pairing and proves a
restoring one-step mean for the constructed peaks. TRACE-078/079/080 now
supply its fluctuation, stopped concentration and global trajectory companions.


[TRACE-071](mathematics/trace-bridge/laplace_path_transport.md) transports the entire centered
phase-ensemble local point-process path and every fixed normal-source product.
[TRACE-072](mathematics/trace-bridge/deterministic_path_transport.md) gives the deterministic
maximal time-average bound and the actual-map growing interval. The initial
local law remains unidentified. [The complete disposition](archive/record/chat_integration_20261011.md)
also indexes reconstructed physical-source covariance, conditional joint delays,
clock obstructions, signed finite-field collisions and frozen circular laws.

## Model and complete target

The maintained odd-dimensional family is
$U_N=e^{i\tau N A_N}M_N$, $\tau=10^{-80}$, with ordinary Weyl convention and
cat matrix $\bigl(\begin{smallmatrix}3&4\\2&3\end{smallmatrix}\bigr)$.
[The model proof](mathematics/fixed-map/fixed_map_resolvent_frontier.md) fixes the symbol,
normalizations, symmetry qualifications and exceptional dimensions.

TRACE-005 asks for signed weighted factorial joint-trace comparison at
Heisenberg powers, for every fixed order and every smooth compact Fourier
weight. The modulus is taken outside the complete normalized sum. The
[exact bridge](mathematics/trace-bridge/trace_to_local_statistics_bridge.md) states the
additional positivity and extension hypotheses needed for local correlations.
The pair-moment reference in the prescribed hierarchy is

$$\frac1{N^2}\sum_{n\ge1}e^{-2sn/N}|\operatorname{Tr}U_N^n|^2
\longrightarrow\frac{1-e^{-2s}}{4s^2},\qquad s>0.$$

Shrinking-coupling returns, arithmetic averages, coordinate-phase ensembles
and noisy dynamics have their own conclusions. Their comparison with this
particular frozen propagator must itself be proved.

## Established conclusions by mathematical role

| Role | Maintained theorem sources | Exact scope |
|---|---|---|
| Actual quantum structure | [FM-024 common commutant](mathematics/fixed-map/actual_seven_primary_commutant.md); [FM-025 pure-five family](mathematics/fixed-map/uniform_five_cluster_simplicity.md); [FM-026 multiplicities](mathematics/fixed-map/literal_time_multiplicity_bounds.md) | Pair commutant classified for every odd $N\ge3$ except $N=7$; separate kick-simplicity and literal-time multiplicity bounds. Full $U_N$ simplicity is not inferred from pair irreducibility |
| Intensity and paths | [FM-021](mathematics/fixed-map/position_chain_mixing.md); [FM-022](mathematics/fixed-map/reversed_path_decay.md); [three-block](mathematics/fixed-map/three_block_unmarking.md) and [four-block](mathematics/fixed-map/four_block_unmarking.md) controls | Eventual constant intensity singular gap, cyclic ramp, reverse-cycle suppression and specified distinct-port reconnections; not all noncyclic interference |
| Fixed-order Fourier sectors | [TRACE-017 WKB reduction](mathematics/fixed-map/factorial_wkb_reduction.md); [TRACE-019](mathematics/fixed-map/selected_weighted_coefficient.md); [TRACE-020](mathematics/fixed-map/factorial_ordered_diagonal.md); [TRACE-021](mathematics/fixed-map/hamming_low_switch_residual.md) | Complete reduction to named finite-order tables, selected full-weight WKB and ordered-diagonal removal, checksum-free specified low-switch removal; the signed complementary sectors remain |
| Source and insertion calculus | [TRACE-027](mathematics/fixed-map/weighted_phase_coherence_covariance.md); [TRACE-028](mathematics/fixed-map/right_frame_unmasked_pinch_hierarchy.md); [TRACE-029](mathematics/fixed-map/convex_pinch_weak_noise_and_deconvolution.md) | Qualified growing-window Ward control; complete unmasked separated/convex hierarchy; bounded-parameter signed stability and an actual unsigned logarithmic obstruction |
| Original common-noise rate | [FM-020](mathematics/fixed-map/original_channel_gap.md) | Two-copy singular gap dominates $N^{-1}$ at $u=N^{-\alpha}$, $0<\alpha<1$. This closes the original-rate question left by FM-018/019, but not nonlinear quenched control, higher-copy rates or deterministic transfer |
| Noisy local statistics | [FLOW-014](mathematics/fixed-map/circular_dyson_actual_start.md); [FLOW-017](mathematics/fixed-map/coboundary_all_order_limit.md) | Actual-start weak local law on a polynomial schedule; all fixed factorial orders and one-chain origin averages on a different superpolynomial schedule |
| Reused phase channel | [TRACE-053](mathematics/trace-bridge/max_entry_phase_channel.md) | Full complex endpoint marks, both collision corrections, exact second-degree norm and an explicit max-entry averaged-pinching rate |
| Rational matrix inner functions | [TRACE-054](mathematics/trace-bridge/sharp_inner_jet.md) | Self-contained noncommuting right-weighted second-jet inequality with optimal leading coefficient $4/3$ and the exact smooth-localization penalty |
| Real unitary source flow | [TRACE-056](mathematics/trace-bridge/phase_channel_real_flow.md) | Normally absorbed unweighted scalar $L^1$ source transport, including fixed derivatives and repeated eigenvalues; anisotropic sources and mixed products are outside the conclusion |

Other maintained arithmetic, Pell/Floquet, return-law, resonance, locality and
information-theory results are indexed by [topic](mathematics/topics/README.md).
They retain their own regimes and are not automatic BGS inputs.

## Submitted article: accepted overlap and pending assertions

The [source-disposition review](literature/phase_channel_jet_sources_20261008.md)
identifies the attached 293-page PDF by hash, maps its final sections to the
maintained corpus and separates proved overlap from unreconstructed inputs.
The [8 October checkpoint](archive/record/research_checkpoint_20261008.md) supplies
full proofs for TRACE-053/054/056 and an explicit disposition of TRACE-055.
TRACE-053 also covers the article's fixed-flatness TRACE-047 as a corollary.

The full five-primary simplicity and deep all-order cavity hierarchy are not
promoted from a summary. TRACE-057/059 now reconstruct source covariance and
physical L2 continuation. The [reviewed cavity continuation](archive/record/cavity_continuation_20261011.md)
strengthens TRACE-060 to all fixed killed upper moments and
[uniform equality laws at every fixed order](archive/record/clock_universality_continuation_20261011.md)
at the log^(1+kappa) cutoff. The full-depth reference measure includes
an atom explained by an exact pathwise rank bound. TRACE-073 supplies conditional
position-chain and [reversal-gap propagation](archive/record/reversal_channel_continuation_20261011.md) at log^(3+kappa). Both require all-time entry
flatness. The all-fixed-order clock induction is now accepted after
two substantive word repairs; its uncorrected input remains preserved.
TRACE-055 remains verification-pending for the full physical hierarchy.
TRACE-080 now supplies the maintained deterministic startup's feedback
probability and cutoff-matched clock/reversal applications. The physical
microscopic cavity reference and signed spectral comparison remain missing.

## Exact unresolved spectral estimates

The complete balanced coordinate-phase microscopic law remains open.
[The phase Ward identity](mathematics/trace-bridge/phase_ward_identity.md) isolates a signed
absorbed overlap defect; [the Schur-energy reduction](mathematics/trace-bridge/balanced_pair_schur_reduction.md)
is an independent exact description of the same pair frontier. Neither
ordinary intensity mixing nor averaged eigenbasis pinching evaluates it.

[The global switch transfer](mathematics/trace-bridge/global_switch_transfer.md) controls
its stated damped interior. The signed marked/high-switch and undamped
endpoint, including the plateau contribution, remain unproved. Masks/source
extraction are not consequences of the unmasked insertion theorem.
[FLOW-015](mathematics/fixed-map/microscopic_noise_removal.md) records the deterministic
noise-removal defect without proving its vanishing. Higher factorial orders
remain part of the full target.

Known controls explain why weaker criteria do not close the problem:
[absolute all-order comparison](mathematics/trace-bridge/signed_heisenberg_comparison.md),
[same-ensemble clock norms](mathematics/spectral-obstructions/isospectral_clock_moment_control.md),
and [microscopic rounding](mathematics/spectral-obstructions/microscopic_rounding_control.md).
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

The [11 October execution packet](archive/evidence/executions/20261011/chat-research/fresh/README.md)
records the complete 217-check workspace snapshot, 236 maintenance tests,
23 active Lean modules / 26 Lake jobs and its 284-page manuscript build.
The [subsequent cavity packet](archive/evidence/executions/20261011/cavity-continuation/README.md)
records the new controls and manuscript continuation at their own scope.
The [reversal extension](archive/evidence/executions/20261011/reversal-gap/README.md)
records the current analytic review and manuscript build, and the completed
219-check/25-target CI of its preceding commit. New source acceptance is
checked on its own final commit; historical receipts retain their original scope.
The [12 October packet](archive/evidence/executions/20261012/two-step-drift/README.md)
records the new exact controls and 291-page manuscript. Its preceding
clock commit passed all seven scientific CI jobs, 220 workspace checks,
236 maintenance tests, 25 C++ builds and the 26-job Lake build, plus the
independent manuscript workflow. These preceding receipts are explicitly
not final-source acceptance for TRACE-074/075.

The [Haar packet](archive/evidence/executions/20261012/haar-feedback/README.md)
adds independent proof reconstruction, exact noncommuting and Jacobian
controls, twelve one-port moment integrals and an actual Wolfram result.
It preserves the failed preceding source CI: 236 maintenance tests and
six scientific jobs passed, but the workspace suite rejected omitted
TRACE-074/075 epoch rows. The explicit epoch repair includes 076 while
leaving historical wrapper bytes unchanged. Final-head acceptance is a
separate execution receipt.

The [7 October integration](record/checked_research_checkpoint_20261007.md),
[Wave2 review](record/wave2_checked_integration_20261007.md), and
[Wave3 review](archive/record/wave3_checked_integration_20261007.md) retain their own
actual execution and applicability scopes. The dated receipts distinguish
those executions from later source changes and external journal refereeing.

[Reproduction](REPRODUCE_unified.md) · [Review policy](REVIEWING.md) ·
[Publication scopes](papers/README.md) · [Historical index](archive/history/2026/INDEX.md)

<!-- Stable fragment targets retained for earlier linked research views. -->
<a id="research-brief-arithmetic-return-laws-and-the-bgs-frontier"></a>
<a id="original-ordered-two-pair-microscopic-mass-6-october-2026"></a>
<a id="question-and-choice-of-model"></a>
<a id="current-contributions-and-their-boundaries"></a>
<a id="next-decisive-research-tasks"></a>
<a id="review-package"></a>


## Operator resolution and short-trace information

The [unitary stability and original-family pair-transfer theorem](mathematics/trace-bridge/microscopic_unitary_stability_20261027.md) gives a concrete continuation of TRACE-113: an $O(N^{-2})$ matrix approximant has the same compact pair trace test, with vanishing error. For weak point-process limits, $o(N^{-1})$ unitary error suffices; the stronger pair statement uses positive energy rather than an implicit uniform-integrability assumption. No suitable approximant with a proved CUE law is currently known.

The complementary [balanced-rounding theorem](mathematics/fixed-map/balanced_rounding_research_20261027.md) shows that polynomial short-trace data and coarser operator/eigenvector control do not determine a local law for a general quantizer. It changes the exact kicked matrices. [The disposition review](record/trace005_continuation_review.md) connects the complete prior continuation to current sources and unresolved proof obligations; its historical source is kept once in the archive.
