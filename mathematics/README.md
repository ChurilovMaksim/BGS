# Mathematical proofs

## Trace results and dependency closure, 22 October 2026

The [review](../record/spectral_research/trace_closure.md) closes the inserted-trace input in TRACE-109 by a
finite-grid corrected-amplitude proof. TRACE-110 now has proved global
$O(1/\log N)$ spectral matching and a matching Pell lower order.
[TRACE-112](fixed-map/displacement_density_trace_bound.md) supplies an
independent logarithmic-time upper-bound route;
[TRACE-113](fixed-map/fixed_kick_uniform_trace_bound.md) proves the
uniform power-trace input with one threshold for all iterates.
All statements have analytic project proofs with self-review, not external
refereeing. Microscopic signed cancellation and BGS remain open.

## Complete spectral research edition

[Fourteen-round thematic edition](spectral_research/README.md): individual
proofs, countertests, failed routes, reference code and exact source catalog.
The first maintained statements were TRACE-108--111. The 22 October
continuation closes the TRACE-109/110 inputs and adds TRACE-112/113. [Actual review scope](../record/spectral_research/spectral_final_integration.md).

## Physical-kick bounds, 21 October 2026

[Uniform trace decay and scalar-distance limits](fixed-map/physical_kick_trace_decay.md)
(TRACE-106) and [all-order polynomial approximation with Pell alias limits](fixed-map/physical_trace_polynomial_approximation.md)
(TRACE-107) are now recorded with full proofs. The imported exponent 1/25 is
strengthened to 1/9 for the single kick. The original microscopic trace hierarchy
remains open. [Review scope](../record/spectral_research/spectral_master_audit.md).


## Circular-phase research, 19 October

[Current theorem account](trace-bridge/phase_ensemble_continuation.md) adopts the
feedback, trace, neutral-scheme and Cauchy proofs with exact scope.
[Full second defect](trace-bridge/phase_second_defect.md) and
[joint quartic sum](trace-bridge/phase_quartic_cluster_sum.md) have different time
ranges. [The complete imported-source inventory](../archive/record/chat_integration_20261019_inventory.json)
preserves earlier derivations and unsuccessful runs. BGS remains open.

The canonical theorem sources live at stable paths in this directory.
[The theorem index](results.md) lists result families;
[the topic views](topics/README.md) provide reading sequences and dependencies.
[The claim ledger](../record/claim_ledger.md) controls current status, and
[open_questions.md](open_questions.md) states unresolved obligations.

## Principal reading paths

| Question | Start here | Scope |
|---|---|---|
| What is the exact BGS target? | [Frozen model](fixed-map/fixed_map_resolvent_frontier.md), [trace bridge](trace-bridge/trace_to_local_statistics_bridge.md) | Unchanged fixed coupling, correct symmetries/unfolding, every fixed factorial order |
| What does actual classical/intensity mixing establish? | [Position-chain mixing](fixed-map/position_chain_mixing.md), [reverse paths](fixed-map/reversed_path_decay.md) | Intensity singular gap and specified path families, not full quantum interference |
| Which arithmetic symmetry questions are closed? | [Combined pair commutant](fixed-map/actual_seven_primary_commutant.md), [literal multiplicities](fixed-map/literal_time_multiplicity_bounds.md) | Current combined classification includes every odd $N\ne7$; full propagator simplicity has a separate boundary |
| Where is the signed trace residual? | [WKB reduction](fixed-map/factorial_wkb_reduction.md), [ordered diagonal](fixed-map/factorial_ordered_diagonal.md), [low-switch removal](fixed-map/hamming_low_switch_residual.md), [switch transfer](global_switch_transfer.md) | Specified removed sectors and damped interior; signed high-switch/undamped endpoint remains |
| What is the balanced microscopic bottleneck? | [Phase Ward identity](phase_ward_identity.md), [Schur-energy reduction](balanced_pair_schur_reduction.md) | Exact absorbed pair reductions; their actual overlap/radial-energy limits are not evaluated |
| What survives noise or insertion averaging? | [Unmasked hierarchy](fixed-map/right_frame_unmasked_pinch_hierarchy.md), [signed stability](fixed-map/convex_pinch_weak_noise_and_deconvolution.md), [noise removal](fixed-map/microscopic_noise_removal.md) | Masks, source extraction and deterministic transfer retain explicit obligations |
| What are the reconstructed analytic inequalities? | [Max-entry phase channel](trace-bridge/max_entry_phase_channel.md), [sharp inner jets](trace-bridge/sharp_inner_jet.md), [real-flow transport](trace-bridge/phase_channel_real_flow.md) | TRACE-053/054/056; full proofs with internal reconstruction, no external-priority verdict |
| Which full-depth clock conclusions are unconditional? | [Exact Haar feedback and entropy-stable clocks](trace-bridge/haar_feedback_clock_law.md) | Independent initial laws with relative entropy O(log N) relative to Haar; deterministic and microscopic-law boundaries explicit |
| Which feedback flatness is unconditional? | [Max-entry feedback flatness](trace-bridge/unconditional_feedback_flatness.md) | TRACE-080 under its named phase-channel and matrix-concentration inputs; deterministic local spectral universality remains open |
| What is proved in the other regimes? | [Arithmetic/return/resonance topics](topics/README.md) | Each family retains its own hypotheses and scales |

## Essential distinctions

The deterministic target is signed Heisenberg-scale comparison. Moduli inside
individual summands change that target. Fixed coupling, shrinking coupling,
arithmetic averages, reused coordinate phases and noisy chains define
different mathematical families.

FM-020 closes the original two-copy common-noise rate left by FM-018/019;
higher-copy rates, nonlinear quenched control and deterministic transfer
remain separate. FLOW-014 and FLOW-017 use different step schedules.
The combined FM-024 pair-commutant theorem supersedes the older partial
arithmetic branches without turning pair irreducibility into simplicity of
$U_N$.

The [attached-article disposition](../literature/phase_channel_jet_sources_20261008.md)
identifies unpromoted cavity/simplicity candidates as well as accepted overlap.
TRACE-055 remains verification-pending. No theorem in this directory is
strengthened by a summary, a finite computation or a manuscript heading.

## Source and review boundaries

Maintain proofs at their canonical paths. Generated TeX is a publication
view; edit its Markdown authority and run the appropriate synchronizer.
[The source contracts](../record/generated_sources.json) identify generated
sections. Finite certificates, numerical diagnostics and formal kernels
certify their stated propositions only.

[The 8 October checkpoint](../archive/record/research_checkpoint_20261008.md) and
[the corpus review](../archive/record/corpus_revision_20261006.md) state actual review
coverage. Historical branch arguments remain traceable through the
[record index](../archive/history/2026/INDEX.md); an inventory is not a complete
proof certification.
