# Corrected phase-integral checkpoint v1

Sealed 7 October 2026, approximately 03:20 UTC, after the user's direction to complete current audit work before the next work wave. Canonical BGS base observed at d37c92e563d10d25bb1d6ab85bedffc1f160f773. Existing canonical overlays were not changed. This is an isolated research checkpoint, not a canonical integration, commit, publication, or BGS solution.

## Original goal and disposition

The goal is the complete annealed balanced pair law for the unchanged odd-dimensional literal-tau BGS operator, ultimately leaving its separate deterministic off-charge comparison. That goal remains OPEN.

Three analytic source obligations now have independent internal review:

1. A complete finite-N color-one pair source identity: a product of compact four-state coefficient functionals reproduces the exact phase-average determinant ratio. It handles the known bulk/surface anomaly without separately divergent summands.
2. A universal dimension-uniform Abel bound for the complete pair observable, F_N(s)<=(1/(2N))coth(s/N), with normal-family and weighted-tail control.
3. Uniform complex microscopic source regularity: the normalized complex resolvent trace has L^p norm at most 100p/(1-exp(-sigma)); its small exponential moment controls a genuine complex numerator-source neighborhood for every fixed finite number of ratios, including all fixed microscopic source derivatives. The review additionally proves an L^(3/2) bound below 4 for the complete ratio product on the closed admissible shift ball, establishing uniform integrability.

The third result concerns the original phase ensemble for any fixed flavor count; it does NOT assert a higher-flavor color-one CFT. For the pair, it controls the full compact signed functional, not the absolute sum of its sectors.

## Reviewed sources and exact acceptance pins

All three author source files are unchanged from the submitted review snapshots:

- proofs/compact_projector.md: SHA-256 4b821bd3c4d67e0f07b32982be8ec06a5e7592d8574aa34c99f67b382b2060f3
- proofs/uniform_abel_bound.md: SHA-256 ecd82a74edfabb89f6cbf46054d76c52dd41e5eb2d5a9790771b16a7c033da3f
- proofs/microscopic_source_bounds.md: SHA-256 9fcf9168a6ff39c8df8e4c1f106e969ce3e1cb3cfac963b7d81d2e9990b52b76

Independent reviews:

- reviews/review_first_pair.md: fd2f0d76ff4326fb4a80e6c84bff69b264ee7b0665448105c59c8cd2128d27b1
- reviews/review_microscopic_source_bounds.md: 0631f08703f39be984ada6e8cdc83d484877830ae54a7f9921bcdaee7e7e2d1a

The copied original reviewer manifests retain their historical paths. This packet's manifest.json and validate_checkpoint.py separately verify the portable copies and this checkpoint's file set. Agent agreement is not a proof certificate; the reviews reconstruct the mathematics and list their exact finite controls.

## Exact next target

frontier/exact_identification_target.md gives the signed growing-degree hook covariance estimate still needed. It includes:

- The exact quantity N^-2 sum_m exp(-2sm/N) sum_(k,l)(-1)^(k+l)[M_(m;k,l)(U_N)-delta_kl].
- The concrete mixed block M_(m;0,1)=E[h_m(DU) conjugate(h_(m-1)(DU)Tr(DU)-h_m(DU))], retaining all weight multiplicities.
- A finite exact flat-matrix discriminator Re M_(4;0,1)=3sqrt(5)/625 for a 5-dimensional cubic-permuted Fourier matrix. This is an auxiliary diagnostic, not an asymptotic or actual-model counterexample.
- The mandatory top-fermion compact term N^2 q^N E|det(I-sqrt(q)DU)|^-2. Its Haar comparison alone is order N^3 microscopically, although the completed answer is order N^2. This rules out estimating every compact sector separately as an error and identifies the signed cancellation that remains necessary.

This frontier note has author-level algebra and direct finite checks; it is not included in the independent acceptance of the three source proofs. The universal source bounds do not identify a limit, and actual P/Q/charge gap estimates have not been converted into the displayed signed estimate.

frontier/centering_candidate.md records an ordinary circle/disk-stratum centering calculation, including its N=1,2 boundary degeneracies. It is explicitly UNREVIEWED/DEFERRED. It is not a dependency of any accepted result and does not block this checkpoint.

## Reproduction and actual finite coverage

From this directory, using Python with SymPy (and NumPy only for the separately labeled floating Q-norm diagnostic):

python checks/check_compact_n2.py 6
python checks/independent_checks.py 3 3
python checks/independent_checks.py 4 3
python checks/check_source_bound_lemmas.py
python checks/check_hook_covariance.py 5 6
python checks/check_frontier_direct.py
python validate_checkpoint.py

The author N=2 exterior-polynomial check uses exact rational arithmetic through t^12. The independent reviewer uses Gaussian-rational arithmetic, a different inverse-Berezinian construction, and ordinary principal-minor phase projection: N=1,2 through t^8, and genuinely complex N=3,4 through t^6, including independent trace-source derivatives. The source-moment controls enumerate 3,002 nested chains, 7,294 monotonicity cases, 240 exact count laws, 3,240 factorial and 2,640 lower-deviation inequalities. These finite checks do not establish the analytic dimension-uniform theorems; their proofs are in the reviewed files.

The hook discriminator is independently recomputed from all rooted words and repeated-index permanents at m=2,3,4. Its printed Q norm is a floating diagnostic only. A separate exploratory Monte Carlo source-bound conjecture test was NOT copied into this accepted checkpoint and supplies no theorem claim.

## Prior source and scope

The color-one coherent sections are Zirnbauer 2021, arXiv:2109.10272v1, Table 1 and (4.36)-(4.40). The actual dual pairing corrects the source's verified index typo. The paired bulk-plus-surface anomaly was independently audited before this work; inputs/color_one_boundary_review.md preserves that scope.

The resampling mechanism is credited to the generalized Minami literature, specifically Combes-Germinet-Klein, J. Stat. Phys. 135 (2009), 201-216, Theorem 2.1 (2.7) and Theorem 2.3 (2.12)-(2.13). The unitary adaptation is proved here directly; no self-adjoint theorem is imported without translation. The reviewer checked the primary institutional PDF at https://escholarship.org/content/qt0kh9c48w/qt0kh9c48w.pdf and arXiv:0804.3202v3. No global novelty claim is made.

All research branches stop at this checkpoint in accordance with the latest user instruction. Remaining identification, the centering review, higher-flavor explicit CFT geometry, and deterministic off-charge comparison are deferred, not declared impossible or complete.
