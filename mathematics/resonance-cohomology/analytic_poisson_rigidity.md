# Analytic rigidity of consecutive Poisson-commuting torus observables

Status: project proof. This note completes an argument prepared in the
uncommitted all-orders-conjugacy tree. It does not claim priority, a complete
Lean formalization, or positivity of every Green--Kubo variance.

Let S be any hyperbolic matrix in SL(2,Z), with either sign of trace. The torus
has normalized Lebesgue measure. For real C1 functions use

    {f,g}=partial_1 f partial_2 g-partial_2 f partial_1 g.

**Theorem.** If g is nonconstant and its critical set {x:dg(x)=0} has measure
zero, then {g,g composed with S} is not identically zero. In particular this
holds for every nonconstant real analytic g.

## Proof

Suppose the bracket is zero. Outside a null set both dg(x) and dg(Sx) are
nonzero. The two-dimensional determinant condition and the chain rule give
an equality of projective covector lines,

    [dg(x)]=[S^T dg(Sx)].                                   (1)

Let mu be the distribution of [dg(x)] for a uniformly chosen x. Since S
preserves Lebesgue measure, (1) makes mu invariant under the projective action
of the fixed hyperbolic matrix S^T.

In an eigenvector coordinate on the projective line, this action multiplies
a finite nonzero ratio by rho with |rho| not equal to one. Replacing the map
by its inverse if necessary, take |rho|>1. The pairwise disjoint measurable
annuli |rho|^k<=|r|<|rho|^(k+1), k in Z, have equal mu measure. A finite
measure forces that common value to be zero. These annuli cover the
projective line apart from its two fixed eigenlines. Thus mu is supported
on those two eigenlines.

The set where dg lies on either specified eigenline is S-invariant modulo
a null set by (1). S is ergodic. An elementary proof suitable here is to
expand an invariant L2 function in a Fourier series: its coefficients are
constant along each nonzero S^T orbit. Every such orbit is infinite because
S is hyperbolic. Square summability forces all its nonzero coefficients to
vanish. Apply this to the invariant indicator set. One eigenline therefore
contains dg almost everywhere.

Let w be a fixed nonzero vector annihilated by covectors on that eigenline.
Continuity of dg extends the equality w dot dg=0 from almost everywhere to
everywhere. The eigenline, and hence the direction w, has irrational slope.
Indeed a rational eigenvector of an integer unimodular hyperbolic matrix
would have a rational algebraic-integer eigenvalue with integer inverse;
it would have to be +1 or -1. The translation flow in direction w is dense
on the torus, while w dot dg=0 makes g constant along it. Continuity then
makes g constant on the whole torus, a contradiction.

Finally, a nonconstant real analytic function has at least one derivative
which is not identically zero. The zero set of a nonzero real analytic
function has measure zero. For completeness, this follows locally by
expanding in one coordinate. A slice which is not identically zero has a
discrete zero set; the exceptional slices are contained in the zero set
of a nonzero analytic coefficient in one less dimension. Induction, Fubini,
and a countable coordinate cover prove the statement. The critical set is
contained in the zero set of that derivative. End of proof.

## A normalized quantum consequence

For the explicitly invariant quantization in
[the general spectral note](../spectral-obstructions/general_hyperbolic_prime_spectra.md), let

    A=S^T,
    Q_N^*(a,b)=(-1)^(ab+a+b) W_N(a,b),
    Op_N^*(f)=sum_v fhat(v) Q_N^*(v),
    ||M||_(2,N)^2=Tr(M* M)/N.

For every fixed smooth g, writing h={g,g composed with S}, the sine Taylor
remainder yields in operator norm

    [Op_N^*(g),Op_N^*(g composed with S)]
       = -i Op_N^*(h)/(2*pi*N)+O_g(N^(-3)).                  (2)

Normalized Hilbert--Schmidt norms of Op_N^*(h) converge to ||h||_L2. For
finite Fourier sums this is exact once N exceeds every possible frequency
difference. For smooth h, approximate by a fixed Fourier sum and use its
absolutely summable Fourier tail to bound the operator norm uniformly in N.
Thus

    lim_(N odd -> infinity)
      N ||[Op_N^*(g),Op_N^*(g composed with S)]||_(2,N)
          = ||{g,g composed with S}||_L2/(2*pi).              (3)

By the theorem this limit is positive for every nonconstant real analytic g.
Consequently the superpolynomially small commutator used in the smooth
support-separated construction is impossible in that analytic class.
No fitted asymptotic exponent or empirical derivative estimate is needed.

## Boundaries which must not be dropped

A nonzero Poisson bracket is not the same as a positive Green--Kubo variance
of that bracket. A nonzero function can be a coboundary. This note therefore
does NOT prove

    sigma^2({g,g composed with S})>0

for all nonconstant analytic g. It does not solve the several-Fourier-orbit
zero-variance problem. It also does not rule out another conjugating mechanism,
or an isolated special value of the kick strength with spectral coincidence.

The measure-zero critical-set assumption is essential to the argument. The
explicit smooth bumps with separated supports have an open critical region
and give nonconstant counterexamples when that assumption is removed.
This distinguishes a rigorously proved analytic obstruction from an unjustified
extension to all smooth observables.
