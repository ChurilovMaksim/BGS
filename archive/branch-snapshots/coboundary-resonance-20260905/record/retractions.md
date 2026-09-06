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
