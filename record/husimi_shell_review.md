# Finite-rank Husimi-shell tomography: proof and execution review

Date: 6 September 2026.
Base: `e702a660ea542d0d0f36a97a87761c8fd89f1210`.

The canonical article now includes `unified_sections/husimi_shell_tomography.tex`.
The section derives infinite-dimensional rank-bounded bosonic tomography from
the preceding analytic finite-rank contact theorem. No photon-number cutoff
or mean-energy assumption is needed for exact injectivity. The energy bound
is imposed only in the separate uniform-continuity statement.

## Mathematical scope checked

1. The Bargmann functions of square-summable vectors are entire by the explicit
   Cauchy--Schwarz bound. Polarization recovers all occupation-basis matrix
   elements. Two states of ranks a,b are distinguished by a+b total complete
   shell/normal-jet conditions. Radii are distinct, positive, and finite.
2. The even/odd binomial mixtures have trace one and orthogonal supports.
   Their Husimi difference is a Gaussian times a Laguerre polynomial.
   Degree 2r-1 gives two rank-r counterexamples on 2r-1 circles, proving the
   sharp universal guarantee over choices of radii, not failure for every
   prescribed design. Degree 2r supplies ranks r and r+1, so rank-r complete
   measurements cannot automatically be called rank-r strictly complete.
3. Finite sets of coherent probes leave an infinite-dimensional orthogonal
   complement. The complete angular data in the theorem are not a claim of
   finite scalar sampling or finite-copy statistical efficiency.
4. Orthogonal high-occupation number states defeat any uniform inverse trace-
   distance modulus without an energy bound. The vacuum/high-number cat pairs
   have fixed mean energy E, rank one, and an eventual positive intensity floor
   on each fixed disk, yet defeat every uniform Holder trace-distance bound.
5. With mean energy at most E and rank at most r the state class is trace-norm
   compact. The inverse from at least 2r complete circles is uniformly
   continuous, but its modulus is at least a constant times
   sqrt(log(log(1/delta))/log(1/delta)). No matching upper rate is proved.

The general coherent-state representation, the scalar two-circle uniqueness
case, and the distinction between complete and strictly complete tomography
are prior mathematics and are cited in the article. Priority of this precise
combination of shell geometry, no-cutoff rank bound, normalized ambiguities,
and conditioned trace-distance obstruction is not established. It does not
prove BGS or determine the eigenphase law of a fixed chaotic propagator.

## Fresh exact computations

```sh
mkdir -p build/recheck
python computations/verification/husimi_shell_tomography.py \
  --max-rank 12 --output build/recheck/husimi-1.json
python computations/verification/husimi_shell_tomography.py \
  --max-rank 16 --output build/recheck/husimi-2.json
```

Both runs returned PASS. They cover 32 distinct Laguerre degrees, with degrees
1 through 24 checked twice. Normalization, positivity, ranks, trace distance,
and the Husimi/Laguerre identity are checked with exact rational coefficients.
An exact Sturm count and polynomial gcd verify all positive simple roots.
Each run also checks 12 algebraic two-by-two cat-state pairs, 36 exact disk
error bounds, and a finite-probe orthogonality construction with a tampered-
root negative control. The programs do not infer the infinite-dimensional
statements from these finite examples.

## Publication verification

The four new sections from this and the preceding commit were compiled together
in a ten-page research excerpt, with the five relevant bibliography entries.
The final version completed three pdfTeX passes, with no overfull boxes or
unresolved references/citations. All pages were rendered and inspected. A
source control-character scan caught two malformed text-mode labels in the
binomial sums; they were replaced by explicit math roman labels, the distinct-
radius hypothesis was made explicit, and the excerpt was rebuilt and the
changed page inspected again. The scientific formulas were unchanged.

The excerpt is not a second maintained publication root. The full canonical
source is still `manuscript/WoW_unified.tex`; its input graph was updated.
No fresh build or full proof audit of every older chapter is claimed. Lean
compilation, successful cloud CI, and independent referee acceptance are not
asserted. The earlier seven-page excerpt and its execution certificate remain
historical evidence for their own source versions.

Source, result and log hashes are in
`evidence/certificates/husimi_shell_review.json`. Build logs, rendered images,
and PDFs are distributed as artifacts rather than checked into main.
