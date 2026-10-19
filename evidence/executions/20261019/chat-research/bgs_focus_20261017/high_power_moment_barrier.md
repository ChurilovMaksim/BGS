# Heisenberg trace powers: exponential collision tilts and a finite-moment barrier

17 October 2026. Work outside BGS; proof with author self-review only.
These results concern positive auxiliary iid matrix models. They do not
settle unitary BGS, and they do not provide a counterexample to local
universality of iid eigenvalues. No novelty or independent certification
is claimed.

## 1. Definitions and normalization

For a rooted closed vertex word a_1,...,a_m on N labels, a_(m+1)=a_1,
let nu_ab count its directed edges a->b. Let c(nu) be the number of such
ordered words with this table, including their specified root position.
Put d(nu)=product_ab nu_ab! and

    h_(N,m)=sum_nu c(nu)^2 d(nu),
    W_(N,m)(nu)=c(nu)^2 d(nu)/h_(N,m),
    C(nu)=sum_ab binom(nu_ab,2), M=binom(m,2).            (1)

If Y has independent standard circular complex Gaussian entries, then
h_(N,m)=E|Tr Y^m|^2 by Wick integration. Thus for variance 1/N Ginibre

    G_(N,m)=h_(N,m)/N^m
      =[product_(j=0)^m(N+j)-product_(j=0)^m(N-j)]
          /[(m+1)N^m],                                (2)

where the second product is zero when m>=N. This is a PRIOR Gaussian
formula. A derivation for every m>=1 is obtained from the finite Ginibre
kernel K_N(z,w)=sum_(k=0)^(N-1)(z conjugate(w))^k/(pi k!)
with Gaussian area weight. The variance of the analytic linear statistic
z^m is

    sum_(k=0)^(N-1)(k+m)!/k!
      -sum_(k=0)^(N-m-1)(k+m)!/k!,

with empty sums zero. Summing binomial coefficients gives (2).
In particular, for m/N->alpha in (0,infinity),

    log G_(N,m)/N -> I(alpha),
    I(alpha)=(1+alpha)log(1+alpha)-alpha.                 (3)

For 0<alpha<1 the ratio of falling to rising products is exponentially
small. The logarithm of the rising product, after canceling N^m, is a
Riemann sum for integral_0^alpha log(1+x)dx, with an O(log N) remainder.
At alpha>=1 the falling product vanishes or is still negligible. These
observations prove (3), including sequences approaching alpha=1.

## 2. Exact positive-tilt condensation

**Theorem 1.** Fix lambda>0. Whenever N>=2, m->infinity and
m/log(Nm)->infinity,

    E_W exp(lambda C)
      =[N m!/h_(N,m)] exp(lambda M) (1+o(1)).            (4)

Under the tilted probability proportional to exp(lambda C)W, the table
is a single repeated self-loop, nu_aa=m for some a, with probability
tending to one. Its label a is uniform.

Here is a finite explicit remainder bound. If
x=(Nm)^2 exp(-lambda m/2)<1, the relative error in (4), before taking any
limit, lies between zero and

    x(1+x)/(1-x)^3 + N^(2m-1) exp(-lambda m^2/4).        (5)

Proof. Directed word tables are balanced at every vertex. A non-loop
edge nu_ab, a!=b, is at most m/2: row a has at least nu_ab edges, and
row b has total degree equal to its incoming degree, also at least
nu_ab. These are distinct rows.

If an edge exceeds m/2, it is consequently a unique loop aa. Write
nu_aa=m-r, 1<=r<m/2. In a word with this property, let q be the number
of positions not equal to a. The number of departures a->other labels
is at least one and

    r=q+(number of such departures).

Hence q<=r-1. The total number A_r of words for this fixed a is at most

    sum_(q=0)^(r-1) binom(m,q)(N-1)^q <= r(Nm)^r.

The remaining edge counts total r, so
d(nu)<=(m-r)! r!, and sum c(nu)^2<=A_r^2 on this class. Its untilted
weight divided by m! is thus at most A_r^2/binom(m,r)<=r^2(Nm)^(2r).
The collision deficit is at least

    M-C(nu)>=r(m-r)>=rm/2.

Sum over a and r, dividing by the exact weight N m! exp(lambda M)
of all constant words. Their relative near-loop contribution is bounded
by sum_(r>=1)r^2 x^r=x(1+x)/(1-x)^3.

For every remaining table max_e nu_e<=m/2. Therefore
sum_e nu_e^2<=m^2/2, and M-C>=m^2/4. The crude but adequate bound
h_(N,m)<=m! (sum_nu c(nu))^2=m!N^(2m) gives the second term in (5).
Both terms tend to zero in the stated range. This proves the theorem.

At m/N->alpha>0, Stirling's formula and (3) sharpen (4) to

    log E_W exp(lambda C)
      =lambda binom(m,2)-N H(alpha)+o(N),
    H(alpha)=(1+alpha)log(1+alpha)-alpha log alpha.        (6)

In particular N^(-2)log E_W exp(lambda C)->lambda alpha^2/2.
The unweighted probability of the union of constant-word tables is
exp[-N H(alpha)+o(N)], not exp[-alpha N log N+O(N)].

Thus a Poisson weak limit of C, if supplied by the project's separate
fixed-order factorial analysis, CANNOT justify any positive exponential
moment limit. No such external collision theorem is needed to prove (4).
This obstruction alone does not imply failure of all radial entry
comparisons: their factorial weights need not equal exp(lambda C).

## 3. A bounded fourth-moment-matched counterexample at m=N

Let xi be circular, X=|xi|^2 and r_j=E X^j, with r_1=1. For an iid
matrix Z_N with entries xi/sqrt(N), circular integration gives the exact
positive expansion

    M_(N,m)=E|Tr Z_N^m|^2
      =N^(-m) sum_nu c(nu)^2 product_e r_(nu_e).         (7)

Choose q vertices, retain all q^2 directed edges including loops, and
let each multiplicity equal a fixed L>=2. Here m=Lq^2. The rooted
Euler-word count is

    c(nu)=[(Lq)!]^q/(L!)^(q^2).                         (8)

For completeness, the directed matrix-tree cofactor is
L^(q-1)q^(q-2); the rooted BEST count is
m times this cofactor times product_a(Lq-1)!, divided by
product_ab L!. This simplifies to (8). The q=1 case is 1 directly.
The root count includes periodic words; no unproved assumption of
aperiodicity is used.

Take m=Lq^2 and integer N with m/N->alpha>0. This single positive term
of (7), together with Stirling's formula, proves

    liminf (1/N)log M_(N,m) >= J_(alpha,L),
    J_(alpha,L)=alpha log(alpha L)-2alpha
          +(alpha/L)[log r_L-2log(L!)].                 (9)

No assumption that this is the full leading rate is made. Consequently

    liminf (1/N)log(M_(N,m)/G_(N,m))
       >=J_(alpha,L)-I(alpha).                         (10)

Now put R=4096 and choose the bounded radial variable

    P(X=0)=1/R,
    P(X=1)=(R-2)/(R-1),
    P(X=R)=1/[R(R-1)].                                 (11)

These probabilities sum to one and r_1=1, r_2=2, r_3=R+2=4098.
With an independent uniform angle, xi=sqrt(X)exp(i theta) matches
every mixed moment of the standard circular complex Gaussian of total
degree at most four (indeed five), and |xi|<=64 deterministically.

Set L=3, N=m=3q^2. Then (10) has the strictly positive bound

    delta=(1/3)log[3*4098/(256 e^3)]>0.                 (12)

Positivity needs no decimal estimate: e<3 and 3*4098>256*27.
Odd q give odd N if that convention is desired. Thus even exact Gaussian
fourth-moment matching and bounded entries permit an exponentially larger
Heisenberg trace second moment than Ginibre.

## 4. Arbitrarily many fixed matching moments do not repair the implication

**Theorem 2.** For every fixed K>=1 and alpha>0, there is ONE fixed
bounded circular entry law matching all standard complex Gaussian mixed
moments of total degree <=2K, for which along m/N->alpha

    liminf (1/N)log(M_(N,m)/G_(N,m))>0.                 (13)

Proof. Put L=K+1. A nonnegative bounded variable X can match
E X^j=j!, 0<=j<=K, while E X^(K+1) is arbitrarily large. Here is a
positive construction, avoiding a hidden truncated-moment assumption.

Choose K+1 disjoint short intervals I_i around distinct positive points
so that the matrix A_(j,i)=integral_(I_i) x^j exp(-x)dx, 0<=j<=K,
is invertible. This follows by shrinking the intervals and using the
Vandermonde determinant. Choose M beyond these intervals. The density
exp(-x)1_[0,M] has deficits
b_j=integral_M^infinity x^j exp(-x)dx. For sufficiently large M,
the coefficients a=A^(-1)b satisfy ||a||_infinity<=1/4. Correct its
density on I_i by adding a_i exp(-x). This yields a positive compactly
supported probability matching all the desired moments.

Next add an atom at R>M of mass p_R=c R^(-K), and subtract from those
interval coefficients the vector

    A^(-1) p_R(1,R,...,R^K)^T.

Choose a positive c, independent of R>=max(M,1), with
c||A^(-1)||_infinity<=1/4 (induced matrix norm). The corrected density
is still at least exp(-x)/2 on the intervals and nonnegative elsewhere.
The first K moments and total mass remain exact; the new (K+1)st
moment is at least cR, tending to infinity. Fix R large enough that

    r_L>(L!)^2 exp[(L/alpha)I(alpha)-L log(alpha L)+2L].

This is one bounded law independent of q,N. Apply (9)--(10) with
m=Lq^2 and N the nearest suitable integer to Lq^2/alpha. The latter is
larger than q eventually; rounding, including odd-N rounding, is harmless.
Circular symmetry removes all mixed moments with unequal holomorphic and
antiholomorphic degrees; equal degrees up to K match by construction.
The strict inequality proves (13).

## 5. What this changes for the BGS program

The auxiliary finite-block Gaussian theorem supplies every fixed moment,
but supplies no uniform comparison for trace powers proportional to the
retained dimension. Theorems 1--2 show why such an implication requires
additional information: neither Poisson collision convergence nor any
prescribed finite number of matching radial moments suffices in the
positive iid proxy.

These examples do not preserve unitarity, the exact feedback law, or the
phase-stationary eigenvector constraint. They therefore do not disprove
the desired two-channel uniform law, phase-ensemble BGS, or the original
frozen deterministic conjecture. Their useful conclusion is to exclude
a false shortcut at the precise growing-power step. The bounded
eigenvector-ratio route in transmission_spectral_averaging.md avoids this
unbounded observable but still requires its own intensity input.

## 6. Provenance and verification boundary

Equation (2) is classical, not a new formula: see Kristjansen--Plefka--
Semenoff--Staudacher, hep-th/0205033v2, equation (2.4), and the finite
Ginibre kernel in Byun--Forrester, arXiv:2211.16223v3, propositions 2.1--2.2.
The kernel proof above covers m>=N without extending a source formula
beyond its stated N>m range. Rooted BEST and the directed matrix-tree
theorem are standard; the project's equal_edge_occupation_20261015.md
fixes the identical root and loop conventions. Source attribution does
not claim prior publication of the exact two theorems in this note.

Finite integer/rational enumeration checks (when attached) test (1),
(2), (5), (7), (8), and (11). They are supporting finite evidence, not
certificates of the asymptotic theorems or independent proof review.
