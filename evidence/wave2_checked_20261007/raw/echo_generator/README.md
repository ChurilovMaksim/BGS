# Verified literal echo mechanism and balanced one-pinch deletion

## Result first

The full signed T16 endpoint and deterministic BGS remain open. This packet
proves a smaller useful long-link theorem for the unchanged literal operator:
for every complex smooth w supported in a fixed positive Heisenberg band,

    N^-2 sum_m w(m/N) integral E_N,m(theta)dtheta ->0,

where E_N,m(theta)=Tr[(V_theta D)(V_theta T)^(m-1)]. Consequently the
complete occupation-subtracted one-pinch functional equals its untwisted
functional up to o(1). For w>=0, its liminf is nonnegative, and proving
vanishing reduces to the genuinely positive untwisted long-echo estimate.
All powers remain m=Theta(N), all modulation labels b modulo N are retained,
and no finite auxiliary coupling replaces tau=10^-80.

The proof combines accepted whole-D operator-norm compactness with the
accepted phase-averaged pair Abel bound. It uses finite-rank approximation
before arbitrary occupation twists and takes the trace norm only after the
complete time sum. It also handles one consecutive block of j pinches,
including deterministic j_N<=aN. Arbitrary separated pinches and any
Hamming/switch coefficient masks remain outside its scope.

An independently audited changed-family counterexample shows that the
untwisted conclusion does NOT follow from flatness, reverse decay, strict
charge gap, collective compactness, or even D_N approaching the identity
rank-one projection. It reuses the existing exact period-six family and
has signed one-pinch liminf at least (1/6) integral w on every positive
band. It is not a counterexample to the literal fixed quantizer.

## Files

- `one_pinch_averaged_lemma.md`: main proof, exact hypotheses, extension,
  signed consequence, and remaining positive microscopic overlap estimate
- `exact_generator_and_echo.md`: independent sign/orientation/alias and
  charge-twirl derivation, physical symbol, flatness CN bound
- `generic_counterexample.md`: exact first-loop consequence of the
  inherited period-six changed family
- `positive_overlap_obligation.md`: PSD eigenbasis Gram representation,
  flatness norm bound, actual trace-o(N) statement, and its precise gap
- `independent_review.md`: isolated independent analytic review
- `computation_audit.md`: exact arithmetic/coverage, literal-time finite
  sign certificates, failed development controls, and evidence limits
- `check_exact_controls.py`, `exact_results.json`,
  `exact_results_optimized.json`: reproducible finite checks; final result
  payloads agree byte-for-byte between normal and optimized Python
- `packet_manifest.json`: final local payload and input-source hashes

## Base and boundaries

Exact checked 3930-file BGS snapshot manifest:
`d6d5ade7444d9a2de43be89fd9636554404a275aa6703fa93910e55c1a1826ba`,
read from `/workspace/shared/bgs_checked_checkpoint_validation/source_snapshot`.
The main long-link theorem uses accepted FM-028 and TRACE-023 in addition to
the exact FM-027 setup. Those extra dependencies are explicit, not silently
attributed to the FM-027 core. Input source files are pinned before and after
the finite runs. No canonical source edit, publication, or claim promotion.

Finite controls cover raw-Weyl arithmetic at N=3,5,7,9, 24 rational twirl
fixtures, actual N=3 symbolic jets through degree two for m=1,...,6, and the
changed N=25 return echo. A norm-controlled certificate at literal tau shows
the actual N=3 signed source is negative at m=3 and positive at m=4. These
are finite identities/certificates, not asymptotic estimates.
