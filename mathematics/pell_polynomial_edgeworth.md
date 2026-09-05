# Minimal Pell relations and the first polynomial Gaussian correction

Status: analytic derivation in the continuation; no execution, priority,
external-referee, or complete Lean-verification claim. This note concerns
the averaged observable, not a new claim of microscopic universality.
The microscopic obstruction is a separate consequence of the Floquet route.

## 1. Definitions and required lifting input

Let alpha=1+sqrt(2), lambda=alpha^2=3+2sqrt(2), and let K be an odd prime.
Write N+F sqrt(2)=alpha^K, put D=(N-1)/2, and use the fixed cat matrix
T=((3,2),(4,3)). Let

    B_j = U_0^j B U_0^(-j),
    X_K = (2K)^(-1/2) sum_(j=0)^(K-1) B_j,
    mu_m(K) = D^(-1) Tr_-(X_K^m).

The diagonal-coordinate signed words have reciprocal labels h^j,h^(-j),
with h=3+2/F mod N. The standard largest-gap/quadratic-norm lifting step
says the following: for each fixed m and sufficiently large K, a central
signed m-word, after cancellation and a cyclic rotation, gives an integer
polynomial P with P(lambda)=0 and coefficient l1 norm at most m.

For clarity its numerical condition is

    m^2 lambda^(K-ceil(K/m)) < N^2.

The proof divides P by z^2-6z+1. Its remainder az+b vanishes at h and
h^(-1); their difference is a unit, so N divides both a and b. A nonzero
quadratic norm of P(lambda) would be a nonzero multiple of N^2 but have
absolute value bounded by the left side above. This proves the lifting
claim without assuming N is prime.

## 2. The minimum nonzero relation has weight eight

**Lemma 1.** If a nonzero integer polynomial P vanishes at lambda, then
its coefficient l1 norm is at least eight. Equality holds precisely for

    P(z) = +/- z^j (z^2-6z+1),  j>=0.                       (1)

**Proof of the lower bound.** Since the monic minimal polynomial divides
P in Z[z], P(1) is divisible by -4. The l1 norm has the same parity as
P(1), so it is even. If that norm were at most six, a leading coefficient
of magnitude a>=1 would have to satisfy

    a lambda <= 6-a,

by bounding every lower monomial by lambda^(degree(P)-1). But lambda>5,
so this is impossible. Hence the norm is at least eight.

**Equality classification.** The leading coefficient has magnitude one;
a leading magnitude at least two would instead require 2lambda<=6.
Change the overall sign to make it one and write, for degree L>=2,

    P(z)=z^L+c z^(L-1)+R(z),
    degree R<=L-2, ||R||_1=7-|c|.

Evaluation at lambda gives

    |(6+c)lambda-1| <= 7-|c|.

For -5<=c<=7 this is impossible, using lambda>5. The case c=-7 is
also impossible. Thus c=-6, ||R||_1=1, and
R(lambda)=lambda^(L-2). The one remaining signed monomial must therefore
be +z^(L-2). This proves (1). End of proof.

In particular, nonbalanced central words of lengths four and six are
absent once lifting applies. The first nonbalanced words have length eight.

### Sharper fixed-order counting

The bounded-cluster argument can now use eight instead of three as the
minimum number of signed occurrences in a nonzero component. A gap larger
than 2 log_lambda(m) splits a lifted relation into two vanishing pieces:
a nonzero high part has absolute value at least 1/m by its quadratic norm,
whereas the low part has absolute value at most m lambda^a. Thus every
component has width bounded in terms of m.

Restore cancelled opposite pairs as two-occurrence components. A
nonbalanced 2r-word has at least one component with at least eight
occurrences; it therefore has at most r-3 components in total. Counting
bounded relative offsets, signs, and cyclic translations gives

    # nonbalanced central 2r-words = O_r(K^(r-3)), r>=4.     (2)

For r<4 the count is zero. After normalization by (2K)^r, the nonbalanced
contribution is O_r(K^(-3)), not merely O_r(K^(-1)). No additional factor K
is introduced by a choice of a cut: the actual count parameterizes the
cyclic translations of the components themselves.

## 3. A phase graph lemma

Let

    z_d = exp_N(-2 P_(2 delta)),

where delta is the signed representative of d mod K and P_j is the Pell
sequence. Let S_K=K^(-1) sum_d z_d. The symmetry z_(-d)=conjugate(z_d)
makes S_K real. The already derived summable estimate is

    sum_d |z_d-1| < 9.                                      (3)

For independent uniform labels t_v in Z/KZ on the vertices of a fixed
simple graph G, orient every edge and choose arbitrary signs sigma_e=+/-1.
Define

    Z_G = product_(e=(u,v)) z_(t_v-t_u)^(sigma_e).

**Lemma 2.** If c is the number of edges, then

    E Z_G = 1+c(S_K-1)+O_G(K^(-2)).                          (4)

In fact the sharper relation holds:

    E Z_G = S_K^c + O_G(K^(-3)+N^(-1)).                      (5)

**First-order proof.** Put w_e=z_e^(sigma_e)-1. The product-minus-linear
remainder is bounded in absolute value by
sum_(e<f)|w_e||w_f|, by telescoping products of unit-modulus factors. Any
two distinct edges of a simple graph form a forest. Their differences of
independent uniform vertex labels are independent uniform elements of
Z/KZ. Each term in this bound therefore has expectation at most 81/K^2.
Also E w_e=S_K-1. This proves (4).

**Second-order proof.** Forests with three edges similarly have three
independent uniform edge differences, so the expected absolute product
of their defects is at most 9^3/K^3. The only three-edge exception is a
triangle. It is frustrated by the half-period concentration, as follows.

Put H=(K-1)/2, r=lambda^(-1), and A=4pi/(sqrt(2)alpha). For a nonzero signed
representative delta let ell=H-|delta|. The Pell ratio gives

    |z_d-1| <= A lambda^(-ell)/(1-lambda^(-K)).

Three triangle differences sum to zero mod K. If none is zero, their signs
have odd sum. Consequently their three ell values have sum at least
(K-3)/2: the distance of either H or 3H to a multiple of K is at least
(K-3)/2. Their defect product is thus O(lambda^(-K/2))=O(1/N), uniformly
in the labels. If one difference is zero the product is zero.

Expand the finite product through second order. Every subset of at least
three edges either is a three-edge triangle, or contains a three-edge
forest; bound all other defect factors by two. First- and second-order
expectations are exactly c(S_K-1) and binom(c,2)(S_K-1)^2. The preceding
bounds control the remainder. Since S_K-1=O(1/K), comparison with the
binomial expansion of S_K^c proves (5). End of proof.

This lemma is for a fixed graph; its constants are not uniform for a graph
whose number of vertices or edges grows with K.

## 4. The first correction for every fixed polynomial observable

Define

    a = 4pi/(sqrt(2)alpha),
    gamma = 3/2 + 2 sum_(ell>=0) [1-cos(a lambda^(-ell))].

Reindexing the exact Pell phases at the half-period and summing their
geometric tails gives

    S_K = 1-(gamma-3/2)/K + O(1/(K N)).                      (6)

One can check the error without decimal approximation. The summed
difference of the finite phase arguments from a lambda^(-ell) is O(1/N),
and the omitted cosine tail is O(lambda^(-K)); divide by K.

**Theorem 3.** For every fixed r>=2, as K tends through odd primes,

    mu_(2r)(K)
      = (2r-1)!!
        - [gamma/K] binom(2r,4)(2r-5)!!
        + O_r(K^(-2)) + O_r(K^r/N).                         (7)

The second moment is 1+O(K/N). Fixed odd moments are exponentially small
in K, with the existing bound (2K)^(m/2)/(N-1) once lifting applies.

**Proof.** Start with the overcounted balanced-word sum indexed by perfect
matchings of 2r positions. Each matching has K^r choices of pair labels and
2^r opposite-sign orientations. Its Weyl phase is a product over the
crossing graph of that matching. Lemma 2 gives its normalized contribution
1+c(pi)(S_K-1)+O_r(K^(-2)). The total number of crossings, summed over all
matchings, is

    A_r = binom(2r,4)(2r-5)!!
        = (2r-1)!! r(r-1)/6.                                (8)

Choose the four interlaced endpoints of one distinguished crossing and
match the remaining positions to prove (8).

The leading overcount consists of four positions at the same time label
with two positive and two negative occurrences; all other labels are
paired and distinct. A word of this type has two opposite-sign matchings
instead of one. Its excess count, after normalization, is

    (3/2K) binom(2r,4)(2r-5)!! + O_r(K^(-2)).                (9)

Indeed the four signs have six choices, the other pair orientations have
2^(r-2) choices, and the r-1 distinct labels have K^(r-1)+O_r(K^(r-2))
choices. Dividing by 2^r K^r gives the coefficient 6/4=3/2. The averaged
phase of these words is 1+O_r(1/K): after merging the repeated label, use
a finite telescoping sum of edge defects and (3). This changes (9) only
at order K^(-2). Words with two or more independent label identifications
also contribute only O_r(K^(-2)).

The true nonbalanced contribution is O_r(K^(-3)) by (2). Finally, for any
Weyl word exp_N(phi)W(v), its normalized odd trace is

    exp_N(phi) [N 1_(v=0)-1]/(N-1).

The total subtracted part is at most (2K)^r/(N-1). Combining (6), (8),
and (9) proves (7): the phase contribution gamma-3/2 and the repeated-label
contribution 3/2 add to gamma. End of proof.

Equivalently, for every fixed real polynomial f and a standard normal Z,

    tau_-(f(X_K))
      = E f(Z) - gamma/(24K) E f''''(Z)
        + O_f(K^(-2)) + O_f(K^(degree(f)/2)/N).               (10)

This is a polynomial Edgeworth-type expansion, not an Edgeworth theorem
for distribution functions, all smooth tests, or characteristic functions
with growing argument. Those stronger conclusions would need uniform
control of the constants as the polynomial degree grows.

For example the 1/K coefficients in the fourth, sixth, and eighth moments
are respectively -gamma, -15 gamma, and -210 gamma. These are analytic
coefficients, not claimed fitted or executed numerical results.

## 5. The first genuinely nonbalanced central contribution

For m=8, a sufficient lifting condition is

    lambda^(K/8)(1-lambda^(-K))^2 > 256.

It holds for all K>=29. For a purely elementary check use lambda>5,
5^(29/8)>320, and 1-5^(-29)>9/10, so the left side is greater than 259.2.
The fractional-power inequality can equivalently be checked by the integer
comparison 5^21>2^48.

By Lemma 1, every nonbalanced central eight-word then has one label j
occurring six times with one sign, and the neighbours j-1,j+1 occurring
once each with the opposite sign. There are exactly 112K such ordered
signed words.

Their phases are computable in the original integer T coordinates, not
only in a modular diagonalization. The three vectors are

    v_(-1)=(3,-4),  v_0=(1,0),  v_1=(3,4),
    v_(-1)+v_1-6v_0=0.

Use the letters v_(-1), v_1, and six copies of -v_0. If the two exceptional
letters occupy positions at distance d, 1<=d<=7, the two possible orders
have Weyl phases +/-4(4-d). Each of the seven phases

    -12, -8, -4, 0, 4, 8, 12

occurs eight times among the 56 position choices. Reversing all signs
leaves the symplectic phase unchanged. Translating all time labels
preserves it as well. Thus their exact central contribution to mu_8 is

    Delta_arith(K)
      = [N/(N-1)] K^(-3)
         [1+2 cos(8pi/N)+2 cos(16pi/N)+2 cos(24pi/N)]
      = 7/K^3 + O(1/(K^3 N)).                               (11)

If B_8(K) denotes the exact balanced central-word sum with normalization
N/(N-1)(2K)^(-4), then

    mu_8(K) = B_8(K) + Delta_arith(K) + R_8(K),
    |R_8(K)| <= 16 K^4/(N-1).                               (12)

It would be incorrect to drop B_8(K)'s own 1/K, 1/K^2 and 1/K^3
corrections and announce mu_8=105+7/K^3. Equation (11) isolates a specific
arithmetic contribution only.

## Verification scope

All displayed coefficients in this note have symbolic derivations above.
No computer execution is asserted. Useful independent regressions are the
crossing-count identity (8), a direct enumeration of the 56 eight-letter
phases in the original integer coordinates, and graph-phase averages with
both forest and triangle controls. General moment limits, priority, and
local spectral statistics cannot be certified by those finite checks.
