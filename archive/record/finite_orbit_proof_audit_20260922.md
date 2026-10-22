# Proof audit: smooth finite-orbit rigidity

Date: 22 September 2026. Type: author-level adversarial self-review, not an
independent referee report. Scope: the new finite-orbit proof and its named
inputs, not the entire BGS repository.

## Claim contract

Every hyperbolic A in SL(2,Z); real nonconstant smooth g; nonzero Fourier
support in finitely many signed A-orbits; every nonzero finite real temporal
combination of h_r={g,C^r g}/(4 pi). Conclusion: strictly positive orbit
variance, hence no L2 coboundary. No uniform coercivity, arbitrary-orbit
analytic theorem, quantum spectral limit, or BGS conclusion is included.

## Load-bearing checks

| Obligation | Check and limitation |
|---|---|
| Rational eigenlines excluded | A rational eigenvalue of an integral unimodular matrix and its reciprocal are algebraic integers, hence it is +/-1; hyperbolicity excludes it. Both covectors are nonzero on every nonzero integer frequency. |
| All pair gaps, not a finite orbit window | Q comparison makes m-n bounded; the expanding covector then makes t bounded; the exact vector equation forces both fixed integer vectors to vanish. The proof covers arbitrary integer t and arbitrary nonnegative m. |
| Same Q is not same orbit | The vector equation is retained after invariant comparison. Distinct equal-Q representatives are allowed. Python uses actual exact orbit reduction, not Q equality as a sufficient test. |
| Negative trace | Absolute values remove the alternating sign in both growth comparisons; A to any integer power is integral. Eight tested matrices include four of each trace sign. |
| All Fourier phases | Positive-negative channels use conjugated correlations; positive-positive channels use unconjugated ones. The Gaussian-integer regression checks both on all ordered families in its test set. |
| Every relevant rearrangement | Smoothness gives every temporal exponential moment along each orbit. Fourier products, orbit sums, and the final all-pass convolution are absolutely summable. |
| Negative correlation tails | S_ij(-n)=S_ji(n), K_ij(-n)=conjugate(K_ji(n)); real a gives the required reflected B identities. Considering only i=j would not supply the common-factor argument. |
| Rational versus Laurent | The products are holomorphic on all of C*, not just an annulus. All possible finite nonzero poles of the rational quotient are removable. This is where smoothness matters. |
| Common factor has no hidden poles | Coprime Laurent polynomial vector plus Bezout makes F holomorphic. Only finitely many common zeros occur; remove them explicitly. |
| Reality of the temporal filter | Both product types are needed. Normalize at 1 after proving F_0 F_0(reverse) and F_0 F_0* are constants; their equality then forces coefficientwise reality. |
| Infinite all-pass factors are not discarded | R=exp(z-z^-1) is allowed; it is not Laurent polynomial. The proof transfers the classes to q, not g itself to a polynomial without a filter. |
| Final contradiction | The existing finite-Fourier all-lag theorem applies to the nonconstant real polynomial q. It is independently reconstructed/self-checked here but is NOT new. |

## Existing finite-Fourier input: checks of the support proof

The checked source is `manuscript/unified_sections/temporal_resonance.tex`
at the pinned base. Set lambda=(T+sqrt(T^2-4))/2, T=abs(tr A)>=3,
Lambda=lambda^r. The selected support functional has value at least
2 Lambda. The positive-iterate rectangle bound is
Lambda+Lambda/lambda+1+1/lambda; the negative-iterate bound is
1+Lambda+Lambda/lambda+Lambda/lambda^2. Both are strictly smaller than
2 Lambda, with the minimum gap lambda-lambda^-1-2>0 at r=1.
For an earlier lag j<r the bound 1+Lambda+lambda+lambda^(r-1)
is also smaller, since lambda^2-2lambda-1>0. Collinear summands give at
most Lambda+2+Lambda^-1<2 Lambda. The lexicographic support maximizers
make the coefficient unique. Thus no cancellation by lower lags or other
iterates occurs. These are exact inequalities for both trace signs, not
finite-window numerical assumptions.

The earlier large-gap separation mechanism also occurs in
`mathematics/phase_regularized_resonance.md`, Section 2. The new note gives
a different qualitative proof; it does not claim priority for separation.

## Negative controls

A constant g gives zero brackets and is explicitly excluded. A nonzero
Poisson bracket can still be a coboundary in other classes, so pointwise
noncommutation is not used as a variance proof. The local polynomial
counterexample in the repository is not a periodic torus counterexample.

Hermitian products alone are insufficient for the real-filter step:
R(z)=exp(i a(z+z^-1)), real a!=0, has RR*=1, but R(z)R(1/z) is nonpolynomial.
Conversely the real all-pass R(z)=exp(z-z^-1) has both products equal to 1
while R itself has infinite Laurent support. These controls explain the two
separate safeguards in the proof.

The late-collision identity v-A^n v=2v+(-v-A^n v) disproves any bound on the
separation threshold that is independent of the list of orbit families.
It does not furnish a zero-variance analytic observable.

## Actual verification status

Python: 2,976 exact channel comparisons and 28,520 enumerated cross-patterns
for the displayed eight matrices, with target gaps 1 through 24. For each
listed target the cross-gap search covers all m>=0 via an exact recurrence
stopping rule. The largest exceptional target gap observed is 4; this number
is NOT a universal threshold.

C++: 147,456 coefficient-identity candidates, 912 identity cases,
7,680 exact recurrence checks, and 40 arbitrarily-late-collision checks.
Arithmetic is Boost arbitrary-precision integers; compilation and execution
succeeded. This is a separately written implementation, not independent
mathematical peer review.

Wolfram: auxiliary exact scalar identities executed; full input and output
preserved. Lean: two conditional algebraic source lemmas only; not compiled,
not imported into the maintained Lean build, and not claimed as formal proof
of the analytic theorem. Full repository CI and full unified manuscript were
not run in the unavailable clone. The standalone new section was built.

## Remaining independent-review targets

A referee should first check Lemma 2 with equal-Q but distinct representatives,
then the two ordered-pair contributions in formula (FO.10), then the coprime
factorization and reality argument in Lemma 3. No unresolved step was found
in this self-review. That finding is not a guarantee against an overlooked error.
