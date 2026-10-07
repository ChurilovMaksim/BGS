# Canonical dependency impact: one-color CFT boundary correction

7 October 2026. Observed base d37c92e563d10d25bb1d6ab85bedffc1f160f773, with pre-existing active integration overlays. Read-only scan, no edits. Search covered mathematics/, supplement/, literature/, record/, manuscript/ Markdown, JSON and TeX, using color/colour-flavor, Zirnbauer, graph authors, superintegral, supersymmetry, Berezin, SDet, sigma-model and noncompact terms. Search hits are retained in canonical_matches.txt; finite search is not a proof of exhaustive semantic coverage.

## No established internal theorem identified as relying on the false bulk-only identity

- BGS-FM-018, mathematics/frozen_operator_transfer_coercivity.md §§8–10, especially lines 414–419 and O21–O25: O21/O22 are direct finite-dimensional Gaussian/adjoint identities; O23 is a singular-value estimate; O25 compares explicitly defined ordinary determinant functions. They survive unchanged. The surrounding interpretation identifies a quadratic block in Zirnbauer's 1998 formalism, and expressly leaves the full integral and zero-mode approximation open. The source-based interpretation should be qualified to require a valid boundary-completed superintegral. This is an exposition/dependency-boundary correction, not a retraction of O1–O29.
- literature/frozen_operator_transfer_sources_20261006.md, paragraph beginning “Martin R. Zirnbauer”: describes the 1998 determinant functional as exact. The pinned 1998 source itself explicitly says its measure is only locally flat and writes “+ ...” for global anomalies (printed p.5); it also switches to one color and physical-N flavors (p.4). Therefore this is not evidence for a bulk-only formula. Add the missing small-color/boundary qualification and the 2021 source; retain the elementary Hessian extraction as algebra.
- record/frozen_operator_transfer_review_20261006.md and record/frozen_operator_transfer_program_20261006.md: their acceptance of O1–O29 and O21–O23 only concerns elementary matrix/channel calculations. No new failed premise occurs in those proofs. Clarify the attribution if the source-exactness wording is updated.
- manuscript/unified_sections/fixed_map_frontier.tex, FM-018 portion around lines 1390–1445: states the quadratic mass and rank-one determinant discriminator, while leaving the nonlinear functional open. The math stays valid; it should follow any clarification of the source interpretation.
- record/claims.json: FM-018's only registered external dependency is EXT-PP-1990. CFT is not a load-bearing theorem leaf. FM-019/FM-020 use the elementary finite-dimensional channel results, not CFT. Their proved states need no downgrade for this finding. TRACE-005 and BGS are already open.

## Background claims needing qualification

- literature/frontier_2026.md, §“Rigorous BGS in special model classes”, lines 35–41: calls Pluhař–Weidenmüller graph universality rigorous. The present exact-source audit does not verify that categorization: its flat one-color transformation needs the omitted completion, and its all-order asymptotics need independent scrutiny. Replace with a scoped description of the claimed supersymmetric result and its unresolved source bridge, rather than using it as a rigorous template.
- literature/bibliography.md entries 10–11, lines 104–105: says the graph paper “proves” all correlation functions and gives an all-correlation generating-function result. Add the same validity caveat. Do not assert the graph universality conclusion false.
- record/frontier_pass_20260904.md line 69: historical claim of a “complete rigorous BGS-type theorem” for those graphs. Preserve history and append a correction link through ordinary repository process; do not rewrite historical evidence as if the caveat was known then.

## Already safely scoped source discussions

- literature/all_order_sources_20261005.md §“Quantum-graph route: no imported arrow” and record/all_order_program_20261005.md: explicitly exclude importing the graph claim and inspect only averaging setup. No theorem-status change needed.
- literature/bgs_scope_and_polynomial_flow_20261004.md: transparently records abstract/bibliography-only inspection and nontransferability. Needs no retraction; a new exact-source audit can supersede its limited evidentiary scope.
- mathematics/pell_resonance_lattice.md lines 416–421 and supplement/fixed_map/block-memory/block_memory_theorem.md near line 389 only contrast independent phase averaging with a deterministic model. That distinction remains correct.
- Ordinary coercivity of S_U(Z), including scalar and block variants, is a statement about a defined determinant function and does not require a supersymmetric identity. No effect on their mathematical validity is inferred.

## Important distinction in the 1998 source

The 1998 chaotic-map construction averages one common U(1) phase and consequently has one color with physical-N flavors, not physical-N colors. It retains unspecified global-anomaly terms in the measure. This differs from independent coordinate phases, which have M separate color-one integrations and fixed flavor count per site. Neither model satisfies the standard stable-range hypothesis merely because its physical dimension grows. The existence and adequate control of the required boundary completion must be supplied for the intended model; a formal measure name or Hessian cannot supply it.
