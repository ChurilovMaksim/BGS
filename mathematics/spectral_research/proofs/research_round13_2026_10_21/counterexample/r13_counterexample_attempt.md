> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round13_2026_10_21/counterexample/r13_counterexample_attempt.md`. Embedded SHA256: `b1d23504a8571c58e2c21387cd5f02ad2757850adf977ebdc5b1cf1a5bd158bf`.
> [Thematic guide](../../../topics/closure.md).

# Round 13: original-family counterexample attempt

Date: 21 October 2026. Branch: `/root/r13_original_counterexample`.

## 1. Outcome and ancestry

No counterexample to the original `H_diag` has been constructed in this
branch. No new asymptotic value or lower bound for an original pair
functional is claimed. The original value `tau = 10^(-80)` has not changed.

The exact base checkpoint is `Spectral_research_master.md`, SHA-256
`10b90c7d12668cd7327bcc08bda292f4c7d6cf82218ee95d5d4f7603fac86cef`.
The byte hash was checked at the start of this branch. The disjoint write
scope is `research_round13_2026_10_21/counterexample/`. All input hashes
are recorded in `input_hashes.json`.

The required negative result is a fixed admissible `k,b`, an `epsilon>0`,
and infinitely many original odd dimensions such that
`|Delta_(k,N)(b)| >= epsilon`. Exact finite-dimensional nonresonance,
the exclusion of one proposed construction, or an auxiliary matrix with
different statistics does not satisfy this requirement.

## 2. Zero hopping edges and constant hopping phases

The first attempted mechanism was to use the zero hopping edges of `A_N`
to remove its constant phase by Jacobi gauges and then infer a surviving
time-reversal or a decomposition of the spectrum of `U_N`.

This is already addressed by the existing exact project work, and it was
not rerun as a new result. The relevant statement is
`research_round3_2026_10_21/arithmetic_monomial_reversal_closure.md`,
Theorem 1 and Sections 5--7. Its class includes arbitrary diagonal phases,
coordinate permutations, independent phase choices on the seven Jacobi
paths when `7|N`, and algebraic symmetric splittings. In particular, making
one Hermitian factor real does not make the complete kicked product
reversible in that class.

Similarly, the seven-chain cutting theorem in
`research_round3_2026_10_21/arithmetic_seven_chain_cut_stability.md`
retains the dense metaplectic factor. It does not give seven independent
spectra. The current branch found no additional invariant projection of
the complete product. These files were screened at their exact statements
and relevant sections; this branch does not claim a fresh audit of every
line of their proofs.

## 3. Algebraic parameter and exact spectral resonances

A second attempted mechanism used algebraicity of `tau` together with
Lindemann--Weierstrass. The relevant old work was then located and read:

* `research_round4_2026_10_21/counter_no_exact_scalar_powers.md` was read
  in full. It already proves that for every odd `N != 7`, every nonzero
  algebraic parameter, and every positive integer power, the original
  kicked matrix is not scalar.
* `research_round2_2026_10_20/arithmetic_transcendental_eigenvalue_ratios.md`
  was read in full. For `7` not dividing `N`, it already excludes every
  algebraic ratio between distinct eigenvalues, using the resultant and
  the nonzero ordered principal minors at complex time. Consequently every
  nonzero power is simple in those dimensions.
* The complete seven-component checkpoint and the all-odd one-component
  physical-minor theorem were read. They do not settle the mixed-component
  discriminant at `7|N` and do not provide quantitative separation.

Thus neither exact scalar-return exclusion nor the resultant argument is
a new Round 13 result. The quantitative-transcendence record was screened
for its exact stated bound and asymptotic limitation; it was not claimed
to provide the `1/N` information missing here.

The remaining implication in a recurrence-based counterexample is
quantitative. One would have to exhibit near-returns of the complete
original `U_N` at times of order `N`, or sufficiently large microscopic
spectral clusters. Nonvanishing at each individual algebraic parameter
does not provide such an implication, in either direction.

## 4. Pell returns beyond fixed-degree comparisons

The possible use of the Pell subsequence was reconsidered at physical
degree `tau N`, rather than fixed degree. With the notation of Round 12,
`c/N` approaches `2 sqrt(2)` with error of order `N^(-2)`: indeed
`c^2-8N^2=(x^2-2y^2)^2=1`, so the difference is exactly
`1/[N^2(sqrt(8+N^(-2))+sqrt(8))]`. Merely
multiplying this error by a quadratic label scale of order `(tau N)^2`
leaves an error of order `tau^2`, which is fixed, not `o(1)`.

Even a fixed tiny error could conceivably be enough to transfer a
counterexample with a fixed margin. But the exact additional label
collisions begin at order `sqrt(N)`, as proved in Round 12. They cannot be
removed by the preceding phase estimate. No control of their complete
coefficient-weighted contribution was found. In particular, a count of
the additional collisions is not a bound, upper or lower, for their
signed contribution to the original trace.

This is an open continuation, not an impossibility theorem. A valid
resumption requires a bound for the weighted alias contribution of the
complete return product, or a different exact expression that genuinely
controls it. Changing only the vocabulary of the fixed-word comparison
does not change this unresolved obligation.

## 5. Primary literature check of exceptional-dimension symmetries

The primary published paper checked was M. Degli Esposti and B. Winn,
*The quantum perturbed cat map and symmetry*, J. Phys. A 38 (2005),
5895--5912, DOI `10.1088/0305-4470/38/26/005`:
<https://www.dm.unibo.it/fismat/pub/a5_26_005.pdf>.

The paper's translated-inversion construction requires dimensions
divisible by four. Its translation construction requires a denominator
dividing both the dimension and `gcd(A_12,A_22-1)`. For our linear map
`[[3,4],[2,3]]`, the latter gcd is two; with odd dimensions the common
denominator is one. Thus these specific published constructions do not
produce an original-family countersequence. This check does not claim
that all possible quantum symmetries have been excluded by that paper.

Primary retrieval references are `turn483view0` and `turn483view1`.
The theorem constructions and their proof discussion were inspected,
especially the translation interpretation on pages 7--8 and the proof
on pages 8--9. The primary PDF identifies the publication as 2005; search
engine freshness labels were not interpreted as publication dates.
No statistical universality theorem from that paper is imported.

## 6. Unchanged first original spectral estimate

Let

$$
\phi(\xi)=e^{-1/(1-\xi^2)}\mathbf 1_{|\xi|<1},\qquad
I=\int\phi,\qquad
b_*=\frac{|\mathcal F^{-1}\phi|^2}{2I^2},\qquad
w=|\widehat b_*|^2.
$$

The original exact pair expression is

$$
\Delta_{2,N}(b_*)=
\frac1{N^2}\sum_{1\le m<2N}w(m/N)
\left(
\left|\operatorname{Tr}[(e^{i10^{-80}NA_N}M_N)^m]\right|^2
-\min(m,N)
\right).
$$

This branch proves neither that the expression tends to zero nor that
its absolute value exceeds a fixed positive constant along infinitely
many original odd dimensions. No new lower bound for it is hidden in
the exact nonresonance results or in the arithmetic phase comparison.

The branch remains available for independent audit of any proposed
estimate for this expression. None of the excluded constructions closes
the overall mathematical problem.
