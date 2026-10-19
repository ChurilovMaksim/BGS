# Rare star circuits obstruct unrestricted Heisenberg Gaussian comparison

17 October 2026. Working analytic proof and separate author self-review.
This is a continuation of the positive Wick measure in project TRACE-093/094,
outside the repository. It is not a counterexample to BGS or to the two-port
conjecture. The matrices in the non-Gaussian examples below have independent
entries and are not unitary. No priority or external certification is claimed.

## 1. Definitions and precise result

A rooted word is x=(x_1,...,x_m) in [N]^m, with x_(m+1)=x_1. Its directed
edge multiplicities are nu_ab=#{i:(x_i,x_(i+1))=(a,b)}. Let c(nu) count all
rooted words with table nu, including their distinct indexed rotations.
For unscaled independent standard complex Gaussians Y_ab put

    h_(N,m)=E|Tr Y^m|^2=sum_nu c(nu)^2 prod_e nu_e!,
    W_(N,m)(nu)=c(nu)^2 prod_e nu_e! / h_(N,m),
    D(nu)=#{e:nu_e>=2}.

The classical Gaussian normalization, recalled with its attribution below, is

    h_(N,m)=[prod_(j=0)^m(N+j)-prod_(j=0)^m(N-j)]/(m+1).       (1)

The falling product is zero for m>=N. If m/N->alpha>0, Stirling gives

    (log h_(N,m)-m log N)/N -> f(alpha),
    f(alpha)=(1+alpha)log(1+alpha)-alpha.                      (2)

Fix an integer s>=2, and let m=2sk, 2<=k<=N-1, k/N->beta in (0,1).
Thus alpha=2s beta. Define H(beta)=-beta log beta-(1-beta)log(1-beta),

    I_s(alpha)=(1+alpha)log(1+alpha)-alpha log(alpha/2)
                    -H(alpha/(2s)).                         (3)

**Theorem A.** There is an explicitly counted event Star_(N,k,s) for which

    W(Star)=4N binom(N-1,k) [(sk)!]^2 / h_(N,2sk),
    D=2k on Star,
    (1/N)log W(Star)->-I_s(alpha).                            (4)

Consequently, for every z>1,

    liminf (1/N)log E_W z^D >= (alpha/s)log z-I_s(alpha).      (5)

At s=2 and alpha=3 the right side is positive exactly when

    z>64/(3 sqrt(3)).                                       (6)

In particular E_W z^D then grows exponentially, even if restricted to tables
with no edge of multiplicity three. The prior convergence
D=>Poisson(2alpha^2), including all its fixed factorial moments, cannot be
upgraded to exponential-moment convergence for all z>1.

**Theorem B.** Let xi be circular, with mu_j=E|xi|^(2j), mu_0=mu_1=1,
and finite moments. Let Z_N have independent entries xi/sqrt(N), and let
X_N be the variance-1/N complex Ginibre matrix. For the same m=2sk,

    liminf (1/N)log [ E|Tr Z_N^m|^2 / E|Tr X_N^m|^2 ]
       >= (alpha/s)log(mu_s/s!)-I_s(alpha).                  (7)

This is a lower bound, not a claimed full rate or phase diagram. It yields
bounded-entry examples for which the ratio grows exponentially. It also yields
such examples matching ANY prescribed finite number of Gaussian radial
moments; see section 6.

## 2. Exact star count: the main combinatorial step

Choose a hub a and a set L of k distinct leaves, none equal to a. Set

    nu_(a,b)=nu_(b,a)=s for b in L; all other nu_e=0.          (8)

Every compatible word alternates between the hub and a leaf. There are two
choices of parity for the hub positions. In the sk leaf positions, every leaf
occurs s times. Hence

    c(nu)=2 (sk)!/(s!)^k,
    prod_e nu_e!=(s!)^(2k),
    c(nu)^2 prod_e nu_e!=4[(sk)!]^2.                         (9)

For k>=2 the hub is UNIQUE: its occupation is sk, whereas each leaf has
occupation s. Thus N binom(N-1,k) counts distinct tables exactly once.
This proves (4)'s finite identity. The k=1 case would count each two-cycle
table twice and is deliberately excluded. No simple-word or independent-word
approximation is involved.

Subtract m log N from the numerator in (4). Stirling and k/N->beta give

    (1/N)log[4N binom(N-1,k)((sk)!)^2/N^m]
        -> H(beta)+alpha[log(alpha/2)-1].                  (10)

Subtract (2) to get -I_s(alpha). On Star, D=2k; restricting a nonnegative
expectation to this event proves (5). At s=2 there are no triple edges on
Star. Thus even an O(1/N) estimate on the probability of any triple edge
does not address this exponential-weight obstruction.

## 3. An exact optimized threshold for this construction

For fixed s, the least z at which (5) is positive for SOME 0<alpha<2s is

    z_s=(4s)^s/(2s-1)^(s-1/2),
    attained at alpha=2s-1.                                (11)

This optimizes only the displayed star construction. It is not a sharp
integrability threshold for the entire Wick measure.

Proof: the critical logarithm is s I_s(alpha)/alpha. Direct differentiation
gives

    alpha I_s'(alpha)-I_s(alpha)
      =-log[(1+alpha)(1-alpha/(2s))].                       (12)

The product exceeds 1 on (0,2s-1) and is below 1 on (2s-1,2s). Thus (12)
has the required negative/positive signs. Substitution at alpha=2s-1 gives
I_s(alpha)/alpha=log(4s)-(1-1/(2s))log(2s-1), proving (11).
For s=2 this is (6). At alpha=3,

    I_2(3)=(9/4)log(16/3),
    (3/2)log(16)-I_2(3)=(9/4)log 3-3log 2>0.              (13)

The last sign follows exactly from 3^9>2^12.

## 4. Independent circular entries and a bounded example

Independence and circular symmetry eliminate cross terms with unequal edge
tables, giving the EXACT identity

    E|Tr Z_N^m|^2 / E|Tr X_N^m|^2
       = E_W prod_e [mu_(nu_e)/(nu_e!)].                   (14)

On Star this product is (mu_s/s!)^(2k). Combining (4) and (14) proves (7).
All terms are nonnegative, so no cancellation needs estimating.

Take R=|xi|^2 equal to 32 with probability 1/32 and 0 otherwise, and take
an independent uniform argument for xi. Then mu_1=1, mu_2=32, |xi|<=sqrt(32).
For s=2 and m=4 floor(3N/4), (7), (13) give

    liminf (1/N)log [ E|Tr Z_N^m|^2 / E|Tr X_N^m|^2 ]
        >= (9/4)log 3-3log 2 >0.                          (15)

Thus removing the all-orders bound mu_j<=j! from TRACE-094's radial corollary
cannot be justified just by bounded entries or by the Poisson collision law.
This does not contradict that corollary: mu_2=32 violates its hypothesis.

## 5. Same variance AND fourth moment as a Gaussian

There is also a bounded law with mu_1=1, mu_2=2, and an exponential separation.
Let

    Pr(R=256)=1/65026,
    Pr(R=254/255)=65025/65026.                            (16)

Direct rational arithmetic gives

    E R=1, E R^2=2, E R^3=66044/255.                      (17)

Choose s=3 and m=6 floor(5N/6). By (11), z_3=1728/(25 sqrt(5)). Since

    (mu_3/6)^2 *5^5 >12^6,                              (18)

equation (7) gives the strictly positive lower exponent

    Delta=(5/3)log[(66044/1530)/(1728/(25 sqrt(5)))].       (19)

The inequality (18) involves rational integers after clearing denominators.
Only (18), not a decimal approximation, establishes the positive sign.
The law is fixed independently of N, circular, and bounded by |xi|<=16.
The predicted fourth-moment-only ratio exp[(mu_2-2)alpha^2]=1 would be false.
The actual all-orders hypothesis of the earlier theorem is violated at j=3.

## 6. Matching any finite number of Gaussian moments is insufficient

**Theorem C.** For every integer J>=1 there exists a fixed bounded circular
xi with E|xi|^(2j)=j! for 0<=j<=J, and a sequence m_N/N->2J+1, along which
the ratio in (7) grows exponentially.

Here is a constructive existence proof, with all positivity issues explicit.
Put n=J+1. Apply Gram--Schmidt to 1,x,...,x^n with scalar product
integral_0^infinity p(x)q(x)e^(-x)dx. The monic orthogonal polynomial p_n
has n distinct roots x_i>0. To see this, multiply its factors at all of its
sign changes on (0,infinity); if fewer than n such changes existed, the
resulting polynomial q of degree <n would make p_n q have a constant
nonzero sign there, contradicting orthogonality. This also forces simplicity
and rules out other roots because p_n has degree n.

Let ell_i be the degree-J Lagrange polynomials of these roots. The associated
Gaussian-quadrature weights w_i=integral ell_i(x)e^(-x)dx are positive and
the quadrature is exact through degree 2n-1. For a proof, divide any such
polynomial by p_n; its quotient has degree <=n-1 and integrates against p_n
to zero. The remainder is its Lagrange interpolation at the roots. Apply
this exactness to ell_i^2: w_i=integral ell_i^2 e^(-x)dx>0. In particular
sum_i w_i x_i^j=j! for j<=J.

Choose L>max(1,x_1,...,x_n). For each i fix C_i>0 with
|ell_i(L)|<=C_i L^J for all such L. Fix a positive c small enough that
c C_i<=w_i/2 for every i. Set epsilon_L=c L^(-J) and define a radial law
with mass epsilon_L at L and mass

    w_i-epsilon_L ell_i(L) at x_i.                       (20)

All masses at x_i are >=w_i/2; they and epsilon_L sum to one because
sum_i ell_i(L)=1. For every j<=J, interpolation gives
sum_i ell_i(L)x_i^j=L^j, so (20) preserves j! exactly. But

    E R^(J+1)=c L+O(1) ->infinity.                       (21)

The correction at the bounded x_i stays bounded, so (21) is immediate.
Take s=J+1 and then choose one finite L large enough that mu_s/s!>z_s.
Fix this law, independently of N. Formula (7) at alpha=2s-1 proves the
claim. The support is bounded for that fixed law. Circularization by an
independent uniform argument preserves all the stated radial moments.

This is a standard finite moment perturbation using classical quadrature,
included with a proof; quadrature itself is not claimed as new.

## 7. Consequences and limits for the BGS program

The previous positive Wick collision theorem survives unchanged. Its bounded
probability-generating-function argument never promised (5) would stay finite.
The all-orders bound in its non-Gaussian corollary is substantial: even matching
any fixed finite list of Gaussian entry moments and imposing a fixed entry
bound does not replace it at times m proportional to N.

The new Bernstein construction for two-port transmission uses normalized,
bounded probability weights. It is not invalidated by these iid examples.
The missing two-port histogram flatness remains unproved, as does the signed
physical trace comparison. No admissible deterministic unitary counterexample
is constructed here. The exact rate for the FULL exponentially tilted Wick
measure, and the physically signed cancellation of the star sector, remain open.

## Dependencies and source boundary

Internal proofs: circular entry expansion (14), star counting, elementary
Stirling asymptotics, calculus (12), quadrature argument and moment perturbation.
Classical input (1): Kristjansen--Plefka--Semenoff--Staudacher (2002), Eq. (2.4),
with the all-m continuation derived from the Ginibre determinantal kernel in
the pinned project TRACE-093 and its source audit. Formula (1) and its
normalization are not new results. The prior Poisson theorem is used only to
explain compatibility; proofs (4)--(21) do not assume that theorem.

Finite evidence: exhaustive word/table counts, exact radial moments and exact
threshold signs in verify_star_sector.py and star_run/. These checks verify
the implemented finite cases, not the asymptotic theorems by themselves.
