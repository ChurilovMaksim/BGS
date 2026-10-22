# Integration proposal

## Placement and ownership

Prepared against repository commit
`d4132ccee82849b644520d88c953cb9b33382a59`.
This is an unintegrated overlay: it does not modify the checkout.

Use the existing ledger owner “Holomorphic shell rigidity and spectral
resolution,” immediately after the preexisting spectral-rounding row.
Inspection of the stable-ID registry at this base finds no registered
spectral-resolution/rounding owner. The registry is intentionally narrower
than the full ledger. Do not invent a new top-level ID merely for this
extension, and do not repurpose TRACE-006, TRACE-008 or TRACE-014, which own
different witnesses. None of FM-007/013/021/022 changes its theorem or status.

## Proposed maintained changes

1. Add `mathematics/microscopic_rounding_control.md` as the single canonical
   proof of the refinement; retain the old spectral-resolution proposition
   as its credited predecessor, without duplicating this new proof in TeX.
2. Add the curated review at `record/microscopic_rounding_review.md` and
   the source manifest at `evidence/microscopic_rounding_provenance.json`.
3. Extend the existing ledger owner with this row:

   Claim: Unbiased spectral rounding preserves simultaneous unnormalized
   low traces for each specified K_N=o(N^(1/3)), with simple spectrum,
   O(N^-1) norm distance and coarse P/Q/Egorov control, while a fixed
   stable-band pair test has liminf greater than 1/2.

   Status: EXACT; independently internally reviewed.

   Boundary: Extension of prior project spectral rounding. Changed operator;
   no preservation of exact quantization, subprincipal data or all-order
   microlocal structure; no counterexample to actual BGS. Proof:
   `mathematics/microscopic_rounding_control.md`.
4. Add one capsule and source membership link to
   `mathematics/topics/spectral-obstructions/README.md` and one short
   pointer in the spectral-obstruction part of `mathematics/results.md`.
   If topic membership is maintained in `record/mathematics_topics.json`,
   add only this proof to the existing spectral-obstructions topic,
   retaining its schema and all other memberships.
5. Add the following short exposition after the old rounding proposition
   in `manuscript/unified_sections/spectral_resolution.tex`:

   The microscopic-rounding refinement selects the lattice rounding by an
   unbiased second-moment argument. For any specified
   K_N=o(N^(1/3)), its simple-spectrum perturbation preserves the whole
   vector of unnormalized traces through K_N with l2 error o(1).
   Operator-norm continuity also preserves the coarse position-chain gap,
   entry flatness, reversed-entry decay and fixed-observable first-order
   Egorov bounds. Nevertheless a fixed stable-band pair statistic has
   liminf greater than one half. The canonical proof and exact scope are
   in mathematics/microscopic_rounding_control.md. The construction changes
   the quantum operator and retains no claim of exact quantization or
   subprincipal-symbol preservation; the actual deterministic BGS target
   remains open.

   Format this paragraph using the manuscript's existing TeX conventions;
   do not reproduce a second maintained proof.
6. Keep BGS-BGS-001 and TRACE-005 OPEN, with unchanged closure conditions.
   No new registry node or dependency edge is needed: this negative
   control is not a prerequisite for their positive conclusions.

## Required integration gate

Review the full diff against the then-current base, preserving concurrent
work. Validate repository links, topic membership and schema; run the
repository's existing structural checks and compile the affected manuscript
if the toolchain is available. Record commands and actual coverage, not
planned success. Recheck the frozen-input provenance if the base changes.
No external dependency entry is needed for the elementary extension.
No claim of full repository build, CI, Lean compilation, integration,
commit, push or external referee acceptance is made by this overlay.
