# Algebraic-time transfer of simple-eigenvalue counts

Status: elementary candidate corollary of the registered Lindemann–Weierstrass identity principle, pending independent audit. Sector premises retain their own proof status. No quantitative gap or BGS claim is made.

## General rank principle

Let A be an algebraic Hermitian matrix and M an algebraic unitary matrix, and put U(t)=exp(itA)M. Every entry of any matrix polynomial with algebraic coefficients in U(t) is a finite exponential polynomial with algebraic coefficients and real algebraic frequencies. The characteristic coefficients of U(t) also have this property.

Therefore, if F(t) is any such algebraic matrix-polynomial expression, each minor satisfies the registered coefficient-separation principle:

    minor F(t*)=0 at nonzero algebraic real t*
      if and only if that minor is identically zero.

Consequently rank F(t*) equals its maximum rank over complex t. Any witnessed rank lower bound at even one real or complex time transfers to every nonzero real algebraic time. The maximum over complex t is also attained at real times arbitrarily near zero except at a discrete exceptional set, since a nonzero analytic minor cannot vanish on a real interval.

## Counting simple eigenvalues explicitly

Write chi_t(z)=det(zI-U(t)) and define

    B(t)=chi_t'(U(t)).

Its entries are polynomial expressions in U(t), with coefficients themselves polynomial in those entries. Thus the rank principle applies. For real t, diagonalize the unitary U(t). On the eigenspace for lambda, B acts by chi_t'(lambda). This scalar is nonzero exactly when lambda is a simple root. Hence

    rank B(t)=the number of simple eigenvalues of U(t).   (1)

No assertion about the full complex commutant is involved.

More generally stack chi_t^(j)(U(t)) for1<=j<=k vertically into F_k(t). The rank of F_k at real t is the total eigenspace dimension contributed by eigenvalues whose multiplicity is at most k: a root of multiplicity m has all derivatives below m zero and its mth derivative nonzero. Thus

    (rank F_k-rank F_(k-1))/k

is the number of distinct eigenvalues of multiplicity k. The whole spectral multiplicity partition is the same at every nonzero real algebraic time, and equals the generic real-time partition. This does not force that partition to be simple: persistent degeneracies are allowed.

## Uniform multiplicity bound from the actual cat at t=0

The stacked matrix F_7(0) has full column rank for N=7*5^e because the independently reviewed actual cat theorem bounds every M_N eigenvalue multiplicity by7. Indeed each eigenspace has some nonzero derivative chi_0^(j)(lambda) with j<=7. No invertibility of chi_0^(7)(M_N) alone is asserted.

One full-column-rank minor of this stack is nonzero at t=0, hence is a nonzero exponential polynomial. The registered separation principle transfers its nonvanishing to every nonzero real algebraic t. Thus F_7(t) has full column rank there, and every eigenvalue of the actual U_(7*5^e)(t) has multiplicity at most7, uniformly in e>=1. Equivalently gcd(chi_t,chi_t',...,chi_t^(7))=1; the stacked evaluated-derivative minor is an explicit substitute for a confluent resultant witness.

This bound is unconditional on the newest-sector candidate. It uses only the accepted cat multiplicity theorem and registered external LW input. It is neither simplicity nor a quantitative gap bound.

## Actual sector implications and their boundaries

Suppose a collection of complete, mutually distinct M_N eigenspaces, of total dimension D, has been proved to split into simple branches at some finite perturbation order near t=0. The initial cat eigenvalues separate these groups from all other groups. For sufficiently small nonzero real t, all D branches are simple eigenvalues of the full U_N(t), regardless of any degeneracies left in other groups. Equation(1) and the rank principle give at least D simple eigenvalues at every nonzero algebraic real t, including the literal t=10^(-80)N.

Applied to the accepted deepest-core theorems alone:

- N=7*5^(2r), r>=2: at least7 simple eigenvalues at every such time.
- N=7*5^(2r+1), r>=2: at least35 simple eigenvalues at every such time.

The newest-even-sector source even_new_sector_first_jet.md is presently a separate candidate awaiting its own audit. IF that uniform source is accepted, its D=24N/25 simple branches are disjoint from the accepted deepest even core. For even e>=4 this would give

    at least24N/25+7 simple eigenvalues of U_(7*5^e)(t)

at every nonzero algebraic real t. At mostN/25-7 dimensions could then belong to repeated eigenspaces. This remains a partial simplicity count, not full simplicity and not a quantitative spacing estimate.

The established finite dimensions with completely simple U remain separately attributed. No unaudited finite CRT experiment is used as a premise here. The external input is exactly the already registered Lindemann–Weierstrass linear independence theorem; all other steps are elementary polynomial/rank and unitary spectral calculations.
