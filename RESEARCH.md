# BGS research brief

The fixed-strength microscopic BGS claim for the maintained frozen quantum map is **open**. This repository establishes subsidiary structural, arithmetic and noisy comparison results; it does not yet establish the deterministic local spectral law. Current status is controlled by [the claim ledger](record/claim_ledger.md), with exact statements in [mathematics](mathematics/README.md).

## Model and target

The target is the prescribed odd-dimensional quantization with fixed coupling tau=10^(-80), with its stated symmetry reduction and unfolding. Shrinking-coupling Pell return theorems, averaged arithmetic designs and auxiliary noisy dynamics have different hypotheses and must not be silently substituted for this operator.

The remaining TRACE-005 target is signed weighted factorial joint-trace comparison at Heisenberg powers: for every fixed order and every smooth compact Fourier weight, the normalized complete Fourier sum must converge to the matching ensemble value. Any modulus belongs outside the entire sum. [The exact bridge](mathematics/trace_to_local_statistics_bridge.md) converts this to local correlations and supplies the every-bandwidth extension under its positivity assumptions. [TRACE-010](mathematics/signed_heisenberg_comparison.md) excludes simultaneous all-order **absolute**, unaveraged deterministic CUE comparison; it does not exclude the signed target.

## Current spectral and selected-family frontier

The actual pair commutant is classified for odd N>=3 with the exact N=7
exception ([FM-024](mathematics/actual_seven_primary_commutant.md)); its7∤N leaf
now has fresh independent review. [FM-025](mathematics/uniform_five_cluster_simplicity.md)
gives the pure-five kick family, while [FM-026](mathematics/literal_time_multiplicity_bounds.md)
gives literal-time multiplicity<=7 and precise simple-eigenvalue counts on
N=7*5^e. Finite U-simplicity cases remain explicitly bounded. The
[FM-010 companion](mathematics/uniform_trace_square_transcendence.md) concerns
one-step squared traces for odd N>=3,N!=7.

[TRACE-019](mathematics/selected_weighted_coefficient.md) controls a selected
full-weight WKB family. Separately, [TRACE-020](mathematics/collective_occupation_hierarchy.md)
controls collective and, separately, full ordered-diagonal sectors in actual-U
operator space. Their cancellation bounds differ; neither is identified with WKB path masks.
The exact signed complement, plateau/torsion mechanism and higher factorial
hierarchy remain open; no BGS conclusion follows.

## Strongest current subsidiary conclusions

- **Frozen-map structure.** Symmetry exclusions, algebraic nondegeneracy, logarithmic trace information and exact transfer identities constrain the actual model. Their constants, exceptional dimensions and external inputs belong to their proof statements; they do not estimate the Heisenberg-scale signed hierarchy.
- **Actual-start noisy local law.** [FLOW-014](mathematics/circular_dyson_actual_start.md) gives the Dyson reference from the centered actual start at t=8g_N, g_N=4 log(J_N)/J_N, J_N=floor(c log N), and a weak local law for the original uncentered random chain on a polynomial step schedule. [FLOW-017](mathematics/coboundary_all_order_limit.md) gives all fixed factorial orders and one-chain origin averages in L2 on a different, superpolynomial schedule. These are noisy conclusions, with recorded internal-review boundaries.
- **Auxiliary channel gaps.** [FM-020](mathematics/original_channel_gap.md) gives a two-copy singular-gap lower bound for the original ordered common-noise law that dominates N^(-1) at u=N^(-alpha), 0<alpha<1. It supersedes the original-rate gap left by FM-018/019. It does not control the nonlinear quenched functional, higher-copy rates or the deterministic spectrum.
- **Actual coordinate-path controls.** [FM-021](mathematics/position_chain_mixing.md) gives an eventual constant singular gap for P=|U|², the cyclic path ramp and a specified marked three-link cancellation. [FM-022](mathematics/reversed_path_decay.md) suppresses reverse-cyclic paths. [TRACE-015](mathematics/three_block_unmarking.md) and [TRACE-016](mathematics/four_block_unmarking.md) now control once-counted distinct-port three- and four-block families, with errors O_w((log N)^5/N) and O_w((log N)^10/N). Their bounded classification certificate does not formalize the analytic chain. Repeated ports, inter-family overlaps, general noncyclic interference, the plateau correction and higher trace orders remain open.
- **Fixed-order WKB reduction.** [TRACE-017](mathematics/factorial_wkb_reduction.md) reduces each complete fixed-k signed partition target to either named finite-J trace table, J>=k, with error O(N^(k-J-1/2)). Exact reciprocity, formal connected coefficients and a conditioned rotated-box theorem are supporting results. The finite-band contour/tail step is now controlled by the global rotated-box theorem; signed comparison and unrestricted bands remain open.
- **Arithmetic translation exclusion.** [FM-023](mathematics/arithmetic_translation_exclusion.md) excludes the indicated odd d-grid algebras for d|N and d<=N^delta, each fixed delta<1/262, with a fixed-tau constant. Projector normalization requires a nonzero centered part in that algebra; arbitrary projectors and the full commutant remain outside its scope.
- **Arithmetic, resonance and return laws.** The Cayley, Pell, locality and cohomology programmes give exact identities, scoped asymptotic laws and sharp obstructions under their own assumptions. Their proof families and limitations are indexed in [the topic views](mathematics/topics/README.md); fixed return moments alone cannot identify microscopic statistics.

## What remains unresolved

The decisive missing estimate is the actual deterministic signed comparison. [FLOW-015](mathematics/microscopic_noise_removal.md) and FLOW-017 express corresponding noise-removal defects but do not prove their vanishing. The [pair-heat formula](mathematics/heisenberg_pair_heat_formula.md) controls a smoothed pair band; the unperturbed band and higher signed hierarchy remain unknown.

Known boundaries rule out replacing this task with fixed/sublinear trace information, absolute all-order comparison, initial heat derivatives alone, or microscopic continuity inferred from a fixed-smooth-observable norm. [The same-ensemble clock control](mathematics/isospectral_clock_moment_control.md) additionally rules out unqualified all-copy induced-HS channel proximity as a spectral-universality criterion. The [microscopic-rounding refinement](mathematics/microscopic_rounding_control.md) preserves a specified sub-cubic-root unnormalized low-trace window and coarse path/Egorov controls while violating a fixed pair target; it changes the operator and does not preserve exact quantization. Faster actual-start relaxation at the clock time N^(-2/3), one polynomial schedule for all factorial orders, effective startup thresholds and growing-order control are separate open questions. See [the current obligation board](mathematics/open_questions.md).

## Evidence and current revision gate

The repository separates project proof, exact-source input, finite arithmetic, floating diagnostics and formal kernels. Passing software checks does not certify analytic limits. The core registry is intentionally narrower than the complete theorem corpus. An exhaustive file inventory is not a line-by-line proof review; inherited heavy analytic chains need their own exact review coverage.

The scoped repository/corpus revision and cross-surface reconciliation passed remote acceptance at `0ffb20cc152d0ddd2620887e46d21d1120b95fd8`. Research has resumed with the recorded proof and source boundaries retained. [Reproduction instructions](REPRODUCE_unified.md), [review policy](REVIEWING.md), [publication scopes](papers/README.md) and [historical records](record/history/2026/INDEX.md) provide the corresponding entry points. Publication candidates are scopes, not acceptance or priority claims.

## Revision record

The earlier cumulative brief is preserved byte-for-byte in [the pre-revision archive](record/history/2026/corpus_revision_20261006/RESEARCH.md.txt). The current corpus audit is documented in [the revision report](record/corpus_revision_20261006.md); unresolved review obligations are distinct from open research problems.

<!-- Stable fragment targets retained from the pre-revision reader entry. -->
<a id="research-brief-arithmetic-return-laws-and-the-bgs-frontier"></a>
<a id="original-ordered-two-pair-microscopic-mass-6-october-2026"></a>
<a id="question-and-choice-of-model"></a>
<a id="current-contributions-and-their-boundaries"></a>
<a id="next-decisive-research-tasks"></a>
<a id="review-package"></a>
