# Analytic rigidity of Poisson-flat generators for a hyperbolic torus map

Status: a self-contained analytic project lemma. No priority claim is made.
This proves a boundary of the support-separated construction; it does not
classify the larger set where the second resonance variance vanishes.

## Theorem

Let S be a hyperbolic matrix in SL(2,Z), acting on the two-torus with Haar
probability measure. Let g be a real C1 periodic function for which its
critical set {x:dg(x)=0} has measure zero. Then

    {g,g composed with S}=0 everywhere

is impossible. Consequently, if g is real analytic and

    {g,g composed with S}=0,

then g is constant.

The Poisson bracket is g_q h_p-g_p h_q. No semiclassical or random-matrix
hypothesis is used.

## Proof

Away from the null critical set, define the measurable line
L(x)=ker dg(x) in the real projective line RP1. Remove also every forward
and backward iterate of that critical set. The resulting invariant subset
still has full measure. On it both dg(x) and dg(Sx) are nonzero.

The vanishing Poisson bracket means the two nonzero covectors

    dg(x) and S^T dg(Sx)

are linearly dependent. Therefore S L(x)=L(Sx). The pushforward nu of Haar
measure under L is an invariant probability measure for the projective
action of S.

This projective action has exactly two invariant probability atoms available:
its stable and unstable eigenlines. More precisely, choose eigenbasis
coordinates and identify the complement of these two lines with the nonzero
slope t. Under S the slope is multiplied by a fixed positive number rho
not equal to one; replace S by its inverse if needed so rho>1. The projective
sets with 1<=|t|<rho and their iterates rho^j<=|t|<rho^(j+1) are pairwise
disjoint for j in Z. Invariance of a finite measure forces the measure of
each to be zero. Their countable union is the complement of the two
eigenlines. Hence nu is supported on those two lines.

The preimage of either eigenline under L is S-invariant modulo null sets.
The toral map S is ergodic: if an L2 function is invariant, its Fourier
coefficients are equal along every orbit of S^T on integer frequencies;
each nonzero orbit is infinite by hyperbolicity, and square summability
forces all its coefficients to be zero. Only the constant coefficient
remains. Applying this to the invariant indicator shows that L equals one
fixed eigenline almost everywhere.

Choose a nonzero vector v on that eigenline. The directional derivative
D_v g is therefore zero almost everywhere. It is continuous, so it is
zero everywhere. The eigenline has irrational slope. Indeed, a rational
eigenline would give a rational algebraic-integer eigenvalue, hence an
integer; its reciprocal is also an algebraic integer, forcing that integer
to be 1 or -1, contrary to hyperbolicity. Translation along v consequently
has dense orbits on the torus, so the continuous function g is constant.
That contradicts the assumed null critical set, proving the C1 assertion.

Finally, a nonconstant real analytic periodic g has at least one analytic
partial derivative which is not identically zero. Its zero set has measure
zero. One elementary justification is the local analytic zero-set lemma,
proved by induction on dimension: in a power-series box expand in one
coordinate; unless every coefficient vanishes, the exceptional base points
where every coefficient vanishes lie in the zero set of one nonzero analytic
coefficient, and almost every remaining one-dimensional slice has isolated
zeros. Fubini's theorem and a countable cover give measure zero. The critical
set of g is contained in the zero set of the chosen partial derivative.
The C1 conclusion now applies and proves the analytic assertion.

## Consequences and non-consequences

A nonconstant smooth generator with {g,g composed with S}=0 must have a
critical set of positive Haar measure. Compactly supported even bumps with
support disjoint from its S-pullback satisfy this requirement: their gradients
vanish on a nonempty open set. Their existence is not in conflict with the
analytic theorem.

For the cat map, the support-separated generator makes every local mixed
Weyl commutator coefficient vanish and gives an all-orders operator-norm
quantum conjugacy. The present lemma shows that this particular Poisson-flat
mechanism cannot be extended to a nonconstant real analytic generator.
It does not rule out other isospectral analytic quantizations or other
cancellation mechanisms.

In particular, the condition

    Gamma(g)=sigma^2({g,g composed with S}/(4 pi))=0

is weaker than the condition in this theorem. It allows the Poisson bracket
to be a nonzero coboundary. Nothing above proves that Gamma is strictly
positive for every nonconstant analytic g. Such a claim would require a
separate argument controlling that cohomological possibility.

This is an invariant-line and Fourier-ergodicity argument, not a positive BGS
universality theorem. Its role is to prevent the fixed-strength smooth
conjugacy construction from being incorrectly advertised as analytic or
arithmetically generic.
