# Retractions and permanent quarantines

These statements or proof routes are false, superseded, or too weak for the
conclusion historically attached to them. The current branch records the
failure mechanism without carrying a duplicate executable museum; exact old
bytes remain in Git history, with
`d0e414ec26ff7e43ad59e80f77c9d8c679e87c4b` as the last pre-cleanup curated
archive snapshot.

1. **Historical Möbius-fiber / M4D proof of M1.** Unsaturated elimination inserted a phantom `(1,1)` key and mishandled the multiplicity-`p-2` diagonal.
2. **Run 93.2 one-sided mixed count.** It included diagonal→off but omitted the distinct ordered off→diagonal class.
3. **Historical uniform Möbius-fiber square-root bound.** The `d=0` fiber is degenerate/constant; Lean keeps a finite regression guard.
4. **“Moment/Catalan data + an ESY citation implies BGS.”** False for this structured deterministic family.
5. **R86/R87 noncommutative trace shortcut.** Invalid as stated.
6. **Historical `N=95419` spacing verdict.** It compared different statistics.
7. **IID-KS interpretation of pooled unfolded spacing samples.** Withdrawn because the gaps are dependent.
8. **Historical “number variance” label and two-sigma pass criterion.** The algorithm uses forward edge-truncated windows, not stationary `Sigma^2(L)`.
9. **Old word-trace “certificate” and all-orders arcsine/Catalan promotion.** A higher-word rewrite case remained unresolved.
10. **Unrestricted historical twisted-Jacobi closed form.** The omitted domain condition `n1 != 0` matters.
11. **Hecke-centering Julia series.** Failed line; later red-team work exposed basis-selection and centering/noise artifacts.
12. **`cdense_transfer.jl` Perron bracket.** Falsified by a zero-cost self-loop of weight one.
13. **`sol6_closed_form.jl` closed-form claim.** Falsified by exact finite rows.
14. **Projective-order comment at `p=31`.** The historical comment said `5`; the exact full matrix order for the implemented condition is `15`.
15. **General `Sp(2g)` conclusion from diagonal/coset flatness.** Not established.
16. **A complete explicit cyclotomic exceptional-set theorem for arbitrary growing prime `K`.** Complete current resultant enumerations are only for `K=11,13`; `(461,23)` warns against extrapolation.
17. **Finite GOE resemblance as proof of a limiting BGS law.** Numerical evidence does not supply the microscopic bridge.
18. **Reconstruction-era entrywise-real spectral projection.** A temporary diagnostic formed the correct complex Hermitian matrix `H=M+M^*` and then diagonalized `H.real`. Hermitian matrices need not be entrywise real; the projection changed finite spectra. Current code diagonalizes the full complex Hermitian matrix, contains a regression guard, and the promoted numerical JSON files were regenerated. No exact pair-key, Cayley, Lean or theorem-level result depended on those floating-point records.
19. **Collapsing iterated frozen kicks to one exponential.** The expression
    `U_N^m=exp(i tau N sum_{ell<m} M_N^ell A_N M_N^{-ell}) M_N^m`
    is false for odd `7 not dividing N`, already at `m=2` and the maintained
    nonzero algebraic coupling. The exact identity is the ordered product of
    the conjugated exponentials. `BGS-FM-008` implies
    `[A_N,M_N A_N M_N^{-1}] != 0`; `EXT-POPESCU-2023` rules out accidental
    equality at `tau N` from a zero of the corresponding algebraic
    exponential polynomial. The scalar-generator case `N=7` is exceptional;
    this argument does not classify dimensions divisible by 7 and greater
    than 7. See
    [`frozen_spectral_flow_controls.md`](../mathematics/frozen_spectral_flow_controls.md).

## Editorial and implementation corrections

During the 2026-09-03 audit, an intermediate note had the inverse pair-key
formula with the wrong sign. The correct inverse is

```text
y=(1-v)/(u-v),   x=u(1-v)/(u-v),
```

while `d=(u-1)(v-1)/(v-u)` was already correct. Active code used the correct
formula, so finite certificates were not invalidated.

The historical Cayley verifier also had a one-way exception regression. The
maintained Python and C++ gates now test actual generic/exceptional behavior in
both directions.

The maintained `jacobi_matrix` contract accepts validated annihilator
sub-sectors (including parity sectors) while rejecting characters outside the
annihilator.

The historical certificate filename `second_moment_reduction.json` became
misleading after the pair-key reconstruction: the file actually contains the
fixed-`K` Cayley matching/resultant audit. It is now named
`cayley_fixed_k_audit.json`.

## Empirical CDF and draft triple filters (2026-09-05)

The former empirical-CDF supremum omitted left limits at jumps. It could
underestimate the descriptive discrepancy; this is corrected and the spacing
JSON is regenerated. No new spacing-law theorem follows.

Draft PR #13 asserted that each of 96 triple resultant filters equals p.
That is false: K=43,p=173 gives 865=5p. Complete observed sets and the K=29
pair-filter correction are in `referee_audit_20260905.md`. The necessary
p-divisibility argument is not retracted. This does not claim a complete
line-by-line review of that draft's mathematical corpus.


## Floquet continuation: numerical and finite-anchor corrections

The previous chat and the main-branch Pell rate note printed
`gamma=5.61214122496472564091...`. Recomputing the stated convergent series
independently gives `5.61422069215119807162796524101779463077...`.
The earlier delivered JSON already contained the latter value; prose and
computed evidence were inconsistent. The series, its tail estimate and the
fourth-moment formula are unchanged. The new consistency regression compares
the documentary decimal to the actual producer rather than another literal.

The advertised inverse transversality anchor K=7,p=29 has gcd degree zero
in all three real embeddings, not degree one. The matching shift-resultant
test therefore has degree zero, not two. All three affected inverse, shift and Sylvester scripts now retain that false
positive as a negative control and realize the positive cases using the
explicit second embedding of K=11,p=23, where tau=10. The inverse gcd degree
is one, and the row gcd degree is two. A direct reflected trace-set count
independently checks the inverse polynomial gcd. The general derivative
identities were not changed by this finite-anchor correction.

## Outside Heisenberg note: corrections before promotion (30 September 2026)

**ERR-023 — corrected before promotion.** The uploaded assertion that all
contained ideal base-7 lines have direction (1,1) is false: direction
(1,-6) persists in the limiting set. Different seven-strip labels also
do not imply circle distance at least 1/7. The repaired geometry and
finite-type hypotheses are in FM-014/FUP-001. The equal-base application
of the anisotropic Jin--Zhang--Zhang theorem is outside its hypotheses;
the ideal-model conclusion instead uses Cohen's isotropic criterion.
Uniform o(1) Egorov errors do not give the submitted logarithmic Fejer
rate; a quantitative summation budget is required. The raw Weyl expansion
must include (-1)^(nm) when using ordinary physical-symbol coefficients.
The [full audit](heisenberg_note_review_20260930.md) records all boundaries.
These outside statements were not previously accepted repository theorems.

## Outside prime-resonant summary: corrections before promotion (30 September 2026)

**ERR-024 — corrected before promotion.** For $U=e^{itA}M$, the
left-to-right ordered block uses $M^jAM^{-j}$, not $M^{-j}AM^j$.
The associated symplectic transversality sign changes with orientation.
Pointwise agreement of a single trace square with its Haar expectation
is not equivalent to the weighted pair target. The summary's claimed
reduction of full BGS to one square-root bound is rejected. Candidate
norm collisions at 29 and 97 do not create scalar exceptions: the
selected sums are 903/1000 and 9/10. See the
[reconstruction](prime_resonant_review_20260930.md) and TRACE-009.
These outside claims were never accepted repository theorems.

## Absolute sufficiency and the unaveraged all-order target (30 September 2026)

**ERR-025 — scope strengthened; sufficient implication retained.**
TRACE-003's triangle-inequality comparison is correct, including averages
taken before the modulus. It must not be interpreted as a feasible
simultaneous all-order absolute goal for one deterministic spectrum:
[TRACE-010](../mathematics/signed_heisenberg_comparison.md) proves that
its absolute pair CUE premise forces absolute cubic discrepancy to diverge
at least as sqrt(N) on a fixed positive box. The viable TRACE-005 target
is the signed weighted sum. This is a correction of the proposed norm's
scope, not a retraction of the exact trace bridge or of BGS. The formal
quadratic-phase control also fails moment positivity at N=3; no actual
quantum family is inferred from its trace amplitudes and phases.

## Polynomial coboundary-step scope (4 October 2026)

**ERR-026 — scope corrected; previous theorem retained.**
The current summary of FLOW-010 had incorrectly ruled out every polynomial
step regime. Its own bound gives convergence with
$t_N=L_N/N$, $L_N\to\infty$, $L_N=o(\log N)$ and
$\varepsilon_N=N^{-a}$, $a>20$, since
$N^{20}e^{CNt_N}\varepsilon_N=N^{20-a+o(1)}$.
The stronger [FLOW-011](../mathematics/coboundary_polynomial_limit.md)
now retains the $O_f(N^{-1/3})$ smooth-test rate at exactly $2N^{34}$
original random steps. Current status surfaces are corrected; the
30 September quantitative theorem and dated evidence are not retracted.
Neither result proves deterministic noise removal or BGS.



## 16 October: imported research-record corrections

1. Calling resonance-sector deletion (R) necessary for BGS is withdrawn.
   Root lifting preserves the complete origin-averaged local process while
   its positive collective trace energy can be concentrated on sparse times.
   See `mathematics/root_lifting_sector_boundary_20261015.md`.
2. The Hardy identity requires the characteristic polynomial of a unitary,
   not just a self-inversive polynomial. The latter can have off-circle roots.
3. A sampled Toeplitz matrix is a positive contraction by the discrete Fourier
   isometry only when the angular grid has at least N points. M<N is excluded.
4. The mesoscopic arc checker uses 0<phi<=ell at the initial right limit.
   Its strict-endpoint predecessor can give negative mean counts.
5. Under the complete every-order H_diag premise, local count UI is a
   consequence. This does not remove UI under weaker pair-only premises.
6. Strict finite Hardy positivity and vanishing fixed Taylor coefficients
   determine neither its full norm nor the required positive CUE excess.

Historical source bytes and original claimed execution scopes remain preserved
in `archive/history/2026/chat_20261015/`; current dispositions take precedence.

## ERR-031: stale failed-run input, 19 October 2026

The original failed transmission run from the imported 17 October packet no
longer has its original source revision at its recorded path. Preserve the
manifest and mark it stale; do not claim reproduction of that failed revision.
The separate successful v2 record validates against its preserved inputs.
[Exact disposition and downstream boundary](chat_integration_20261019.md).

## 20 October maintenance correction

ERR-032 repairs integration-gate drift and optimized-entry protection.
No mathematical statement is retracted or strengthened.


## 22 October 2026: metadata and dependency corrections (ERR-052–055)

The [full recheck](audits/repository_recheck_20261022/report.md) records missing
external inputs for CAYLEY-006/007, a false provenance-string inference in the
registry audit, missing source anchors, malformed errata paths and stale
current summaries. The density formula retains exact prime-count endpoints
to avoid an unnecessary quantitative PNT input. No claim state is changed;
no theorem is retracted by this correction. Earlier evidence is unchanged.

ERR-056: the first return-section synchronization check found proof details
present only in generated TeX: the 32-class estimate and the Green-kernel
derivation. They were restored to the authoritative Markdown before
regeneration; no mathematical text was discarded to obtain a passing check.

ERR-057: the full maintenance suite exposed a historical-input inventory
misclassification and an out-of-date integration epoch. The immutable spectral
source corpus is checked for byte preservation, not rewritten to satisfy a
maintained-entry guard. Newer registry rows and prior corrections are now
explicit epoch entries; mutation tests still reject undeclared changes.

ERR-058: the margin compiler now fails before imports under optimized Python.
Portable Wave2 uses three existing immutable governance copies with their
original seals; the v1 source and original input-binding hashes remain
unchanged. The current manuscript mapping was self-reviewed and refreshed
explicitly, retaining its previous digest and the missing-old-bytes limit.

ERR-059: two Markdown display defects were repaired at their canonical
sources: the visible brace in Möbius equation (8), and separate displays
for pair-heat equations (H22)/(H23). Their mathematical content is unchanged.
