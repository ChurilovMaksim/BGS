# Scientific integrity audit — first pass (2026-10-28)

Base commit: `d58eeaae0c48bf37330c6858be1735cb9360dadb`. This audit changes no theorem statement or claim state.

## Implemented repository corrections

- Reconciled the evidence inventory from 199 to all 202 current claim IDs; added TRACE-114, TRACE-115, TRACE-116. Updated exact structured metadata, including 20 added Mathlib links and the revised FORMAL-001 entry.
- Preserved historical risk assessments instead of pretending the fresh Mathlib links prove entire analytic statements. All 20 links requiring mathematical scope review are explicitly flagged, and new records remain provisional.
- Added fail-closed inventory/registry consistency checks to the scientific registry audit.
- Corrected source-generation metadata: the six return-law chapters, the fixed-map frontier chapter and the finite-orbit chapter are TeX-canonical after manual amsthm editions. Their sync scripts intentionally SKIP; their execution must not be presented as verification of source-text equivalence.

## Independently checked mathematical content

FM-001 finite scalar assertions were independently recalculated using SymPy and 80-decimal-digit mpmath from the displayed ordinary Weyl symbol (rather than copying the existing verifier): the four fixed-point values of `g_qq/pi²` are exactly `-19606/125, -19594/125, 24306/125, 24894/125`; `g_pp=0` at those points. The period-three orbit is cyclic under `S=[[3,4],[2,3]]`, `C²=S` for `C=[[1,2],[1,1]]`, and `R0 S R0=S^{-1}` for `R0=diag(1,-1)`. Independent period-three values of `(A_I-A_B)/pi²` are `-520.0488777028559264...` (minus identity), `568.9423619313295605...` (R0), and `-1088.9912396341854870...` (minus R0). These fall strictly within the printed enclosures (7b). Numerical agreement is **not** a formal interval certificate; the existing exact rational interval script is `computations/verification/fixed_model_period_three.py`. No redundant verifier was committed.

## Remaining proof obligations — not certified by this pass

- **FM-001:** full centralizer/reversor classification and global conjugacy, including uniform analytic error estimates. The finite calculations above do not prove the theorem.
- **FM-021:** full four-branch WKB residual justification, the alias-safe discrete oscillatory estimate and the two-stage zero-set excision are still subject to independent analytic reconstruction. Marked contributions are not the unmarked signed pair sum.
- **TRACE-113:** exact all-time quantum trace identity, uniform trace-class convergence and rank-one cocycle splitting are the key steps needing an independent proof audit. The Bowen–Ruelle input is documented separately; this pass does not independently verify the entire analytic chain.
- **TeX comparison:** all eight hand-edited TeX sections need a manual theorem/hypothesis concordance before declaring Markdown/TeX synchronized.
- **Reproduction:** no post-merge Lake build, full workspace test, or PDF build was executed in this pass; old receipts retain their historical scope.

The deterministic fixed-coupling BGS conjecture and the signed Heisenberg-scale comparison remain **open**.
