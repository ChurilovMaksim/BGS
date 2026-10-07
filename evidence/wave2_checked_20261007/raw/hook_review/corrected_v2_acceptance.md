# Corrected v2 acceptance

Date: 7 October 2026. Primary verdict: **proved as written**, for the exact finite identities and the conditional controlled-sector reduction stated in this corrected version. The asymptotic phase-current identification remains open.

Accepted artifact: `hook_tree_current_identity_v2.md`.

SHA-256: `1e1650468a3f4ec9ad3bfc1274cd0c79b54b22c5742a94708aedce2d6d098b59`.

The correction explicitly extends (K1) by zero exterior characters `e_j(A)=0` for `j>N` before the full degree-`m` cycle-index expansion. Thus (K2) is now applied to the correct expression for every `N,m`, including `m>N`. The explanation does not claim literal termwise cancellation in the unextended finite complex. The sparse-support sentence also fixes the interpretation of formal rectangular phases. No downstream identity or hypothesis is altered.

The v1 proof is preserved byte-for-byte as `hook_tree_current_identity_v1_preserved.md`, and the original proof/computation directory remains unchanged. The diff is confined to status/provenance, the explicit bridge, the top-sector interpretation, and sparse-support phase clarification.

## Regression evidence

`check_zero_extension_bridge.py` computes exterior characters from explicit permutation cycle indices, power sums from direct rooted words, and complete polynomials from an independent power-sum recursion. It shares the already-checked exact Gaussian arithmetic and fixture definitions with the copied authored checker, so it is not represented as a wholly independent arithmetic implementation.

Sixteen exact `m>N` cases pass:

- `N=1,U=i`: `m=2..6`
- `N=3,U=I`: `m=4..5`
- Rational `N=2` rotation: `m=3..6`
- Complex rational `N=3` unitary: `m=4..6`
- Both `N=4` Hadamards: `m=5`

All 36 appended exterior-character checks vanish exactly. Each case verifies that the truncated marked polynomial, zero-extended marked polynomial, direct trace polynomial, and signed hook polynomial agree, and that the completed covariance is unchanged.

The explicit `N=1,m=2` regression distinguishes the literal truncated cycle weights `(2,0)` from the full zero-extended weights `(0,2)`, for the identity permutation and transposition respectively. This tests the specific bridge missed by the original unrestricted-mask test.

The unchanged copied downstream checker was rerun normally and under `-O`. All 35 exact cases and all 873 permutation checks pass; every scientific output line agrees between these runs, and all computed rows agree with the original recorded rows. This rechecks hook signs, complete occupation polynomials, tree counts, periodicity, dihedral overlap, determinant factors, residual nonnegativity, covariance splitting, zero-current examples, and the finite same-`P,Q` discriminator in their declared ranges. The prior independent bounded boundary/pair checks remain separate supporting evidence.

Commands, run from the review directory:

`PYTHONDONTWRITEBYTECODE=1 python3 check_zero_extension_bridge.py`

`PYTHONDONTWRITEBYTECODE=1 python3 check_grouping_review_copy.py`

`PYTHONDONTWRITEBYTECODE=1 python3 -O check_grouping_review_copy.py`

No copied-run resource-cap claim is made. Original historical caps are described only by the original manifest. The new bridge took about 0.35 seconds; all arithmetic assertions are exact `Q(i)`/rational computations, without Monte Carlo.

## Acceptance boundary

The all-`N,m` conclusion rests on the corrected proof, not extrapolation from the finite regressions. Under the exact eventual fixed-constant assumptions (B3), the full removed Abel contribution is `1/(4s^2)`. The remaining target is still `-exp(-2s)/(4s^2)`. Accepted phase-ensemble endpoint and tail bounds support the all-time/near-zero passage, but do not identify this signed limit.

No estimate of the full oscillatory current sum has been supplied. The Hadamard example is finite non-identifiability only. No asymptotic universality, actual BGS operator evaluation, canonical repository edit, source-snapshot mutation, or publication is part of this acceptance.

`corrected_v2_acceptance_receipt.json` seals this proof revision, its frozen regression artifacts, the original proof/manifest, and all relevant pinned source hashes.
