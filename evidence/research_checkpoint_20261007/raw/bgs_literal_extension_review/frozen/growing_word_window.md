# An explicit triple-logarithmic window for the literal mixed-word traces

Author proof candidate, 7 October 2026. This extends the independently
reviewed qualitative theorem in `fixed_word_freeness.md`. The quantitative
continuation is not yet independently reviewed. Canonical BGS remains
untouched. The original microscopic signed target remains open.

## Q1. Exact quantitative target

Use the unchanged Q_N=exp(i tau N A_N), M_N, tau=10^(-80), odd N. Word
length |w| means freely reduced letter length in q,q^(-1),m,m^(-1), with
integer powers expanded into letters. Let W_N(w)=w(Q_N,M_N).

For N sufficiently large that all logarithms below are positive, put

    L_N=floor[log log log N/(4 log 8)].                       (Q1)

**Candidate theorem.** Uniformly over nonidentity words of length at most
L_N,

    sup_(1<=|w|<=L_N) |N^(-1)Tr W_N(w)| ->0                  (Q2)

through all odd N. There is no averaging or changed quantum model. The
window is extremely small. It neither competes with the already known
logarithmic bound for pure U_N powers nor reaches growing Pell periods,
Heisenberg powers, or the complete signed factorial target.

The proof gives the following explicit dependence on a prescribed length
bound L>=1. Define

    d0=125*10^80,
    h_L=(14 d0)^L,
    B_L=(24 L h_L^2)^(216 L),
    D_L=L(B_L+1+log d0),
    R_L=1/(1000*8^L),
    J_L=ceil(4/R_L),
    K_L=ceil[100*2^(J_L)*(D_L+log(100/R_L)+1)].               (Q3)

There is a finite absolute constant C_0, depending only on the fixed
explicit smooth cutoff and the specified torus Sobolev-norm conventions,
independent of N,L,w, such that

    |tr_N W_N(w)|
      <= min(1, C_0 exp(K_L^3)
                     [N^(-1/(16K_L))+N^(-1/2)]),             (Q4)

for every nonidentity w with |w|<=L. Using exp(K_L^4) instead of
C_0 exp(K_L^3) is valid once the fixed numerical cutoff constant is below
that enormous envelope. No practical numerical startup is claimed. Q4
tracks every length-dependent loss; C_0 conceals no word, N, or tau growth.

## Q2. Effective separation of the derivative word from the identity

At the common equilibrium P, the exact derivatives of the generators are

    S=[[3,4],[2,3]],       T(x)=I+xE21,
    x=(9803/d0)pi.

The reviewed derivative-faithfulness proof shows that the derivative of
any nontrivial word differs from I. In the inverse-Egorov convention the
generators are S^(-1),T(-x), which makes no difference to the estimates.

For a 2-by-2 polynomial matrix use the maximum row sum of coefficient l1
norms. The norms of S and S^(-1) are at most7, and those of I+uE21 and
I-uE21 are at most2. Thus every entry of a length-L derivative word has
coefficient l1 norm at most7^L. At least one entry of the word minus I is
a nonzero integer polynomial P(u), of degree at mostL and coefficient
l1 norm at most7^L+1<=14^L.

Set

    R(z)=d0^L P(9803 z/d0).

This is a nonzero integer polynomial of degree d<=L and coefficient
height at most h_L, because 9803<d0. We claim

    |P(x)| >= exp(-D_L).                                    (Q5)

If R is constant or all its roots have distance at least1 from pi, then
|R(pi)|>=1, which is more than sufficient. Otherwise choose a closest
root alpha, with |alpha-pi|<1. It is nonzero. All conjugates of alpha are
roots of R, hence have modulus at most1+h_L<=2h_L by the Cauchy root bound.
If a_d is the nonzero leading coefficient, |a_d|alpha is an algebraic
integer, by the elementary scaled-root monic polynomial. Therefore
beta=i alpha is a nonzero algebraic number satisfying

    [Q(beta):Q]<=2L,
    all conjugates of beta have modulus <=2h_L,
    q beta is integral for q=|a_d|<=h_L.

Apply the registered Roy effective Lindemann-Weierstrass theorem,
arXiv:1607.00579v1, Theorem1.1 on printed page2, with one exponent beta,
polynomial Z+1, degree bound1, coefficient bound1. Its parameter
S_Roy=6[Q(beta):Q] is at most12L. Monotonic enlargement of the theorem's
positive quantities yields

    |exp(i alpha)+1| >= exp[-(24L h_L^2)^(216L)]=exp(-B_L).

The straight segment from pi to alpha has imaginary part of modulus<1,
so |exp(i alpha)+1|<=e|alpha-pi|. Hence the closest-root distance is at
least exp(-B_L-1). Factoring R, every one of its at mostL roots has at
least that distance from pi, while |a_d|>=1. Thus

    |R(pi)| >= exp[-L(B_L+1)].

Divide by d0^L to obtain Q5. No p-adic valuation is interpreted as real
smallness, and no lower bound follows from transcendence alone; the
explicit Roy inequality supplies exactly this extra quantitative arrow.

This use of Roy is distinct from FM-011's huge eigenvalue-discriminant
application. Only the exponent i alpha and polynomial Z+1 occur here.
The primary theorem was re-read for this application; see the separate
source record. Complex alpha is allowed by its stated hypotheses.

## Q3. Uniform holomorphic strip for a word of length at mostL

The exact finite physical g has support |k|+|l|<=10 and Fourier second
moment less than52. On the strip |Im q|,|Im p|<=1/100 its vector field and
first derivative have bounds1000 and5000, as in the accepted FM-023
complex-flow estimate. At time |kappa|=tau/(2pi)<10^(-80), both the positive
and negative kick flow take a sufficiently thin strip into a strip at
most twice as wide. One direct justification is that the real flow stays
on the real torus and the complex variational bound is exp(5000|kappa|)<2;
the displacement bound keeps every intermediate point inside the1/100
domain. S and S^(-1) expand maximum-coordinate imaginary width by at most7.

Starting with strip width R_L=1/(1000*8^L), every prefix of a word of
length at mostL therefore remains in width at most1/1000. Every word map
F_w is holomorphic on that initial strip. The four embedding-coordinate
differences

    b_j=a_j composed with F_w-a_j

are real on the real torus and bounded in modulus by4 throughout it.
Periodicity handles lifts of real parts; no bound on real winding is
needed. By Q5 and the sine coordinates at the common fixed point, at least
one of these b_j has a first coordinate derivative at P of modulus at
least delta_L=exp(-D_L). Fix that scalar b for this word.

## Q4. An elementary quantitative analytic propagation lemma

We record the deliberately crude uniform finite-type bound rather than
using a qualitative analytic zero-set theorem with unspecified constants.
Let b be holomorphic and |b|<=4 on the torus strip of width R=R_L. Assume
one first derivative at P has modulus at least delta=exp(-D_L). Let J,K
be as inQ3, and put eta=exp(-K/4). Then, at every real point y,

    max_(|alpha|<=K)
       |partial^alpha b(y)| R^|alpha|/alpha! > eta.          (Q6)

To prove it, assume the contrary at some y. Cauchy bounds all normalized
Taylor coefficients by4. On the polydisc of radius R/2 centered at y,
the terms of total degree<=K sum to at most4eta. The higher terms sum to
at most16*2^(-K/2), since there are n+1 two-variable coefficients at degree
n and sum_(n>K)(n+1)2^(-n)<4*2^(-K/2). Hence the supremum eta_0 there is
at most20exp(-K/4)<=exp(-K/5), since K>=1000.

Join y to P along a real torus path with maximum-coordinate displacement
at most1, using at most J=ceil(4/R) steps of length at most R/4. Suppose
the radius-R/2 polydisc at a current center has bound a. The radius-R/4
polydisc at the next center lies inside it. The next radius-R polydisc
has the global bound4. Hadamard three-circle on every complex line through
the next center gives a bound sqrt(4a) on its radius-R/2 polydisc. For a
polydisc, this follows by applying the one-variable theorem to b(z+t v)
for each fixed vector v of maximum norm R/2, at |t|=1/2,1,2. The needed
one-variable inequality follows directly from the maximum principle for
log|h(t)| minus the harmonic radial function interpolating the two boundary
logarithmic bounds on that annulus; zeros are handled by a small positive
regularization or by their removable upper-bound singularities.

After at mostJ steps the bound at P is at most

    4 exp[-K/(5*2^J)].

Cauchy on that polydisc bounds each first derivative at P by
8 R^(-1)exp[-K/(5*2^J)]. From the definition ofK this is strictly below
delta, a contradiction. This provesQ6, including order0 when b itself
is already large. No compactness-only step is hidden in this argument.

## Q5. Explicit finite-type sublevel control

For K>=1000, Q6 implies the coarse but uniform estimate

    area{|b|<=s} <= exp(K^2) s^(1/K),        0<s<=1.          (Q7)

Here are the constants needed for that deduction. Some ordinary partial
derivative of order k<=K has modulus at least eta, since R<=1. For k>=1,
the polarization formula for its symmetric k-linear derivative expresses
it as an average of directional k-th derivatives at vectors of norm<=k.
Thus one unit direction has derivative modulus at least

    beta=eta/K^K >= exp(-2K logK).

Cauchy bounds all partial derivatives through orderK+1 by

    A=4(K+1)!R^(-(K+1)) <= exp(3K logK),

where the last inequality uses K>=100/R. The gradient of each selected
directional derivative is bounded by 2^(K+2)A<=exp(4K logK). Therefore on
a ball of radius r=exp(-8K logK) its modulus stays at least beta/2. A
finite grid covers the torus by at most C r^(-2) such convex patches. The
chosen direction and order may depend on the patch. If k=0, |b| stays
at least beta/2 there and that patch contributes nothing when s<beta/4.

For positive k, slice the patch along the chosen direction. The elementary
one-variable divided-difference sublevel lemma gives length at most

    8k (s/beta)^(1/k) <= 8K (s/beta)^(1/K),  s<=beta/4.

Indeed select k+1 measure-quantile points separated by at least a fixed
multiple of the sublevel length divided byk, use the explicit divided
difference denominator, and use the repeated mean-value theorem. The
factor8 safely includes the half-beta derivative bound and endpoint slack.
Integrating transverse slices of width at most1 and summing patches gives
at most exp(20K logK)s^(1/K), which is bounded by the right side ofQ7.
For beta/4<=s<=1 that right side is already>=1. This provesQ7 globally.

The loss exp(K^2) is intentionally generous; no optimized order or
sublevel exponent is claimed.

## Q6. Quantitative word Egorov and trace cutoff, with aliases retained

The actual Fourier sine calculus, exact cat Egorov and fixed kick time
give for every smooth a

    ||Q_N*Op_N(a)Q_N-Op_N(a composed with Phi^(-1))||
          <= C N^(-2)||a||_(H5),                            (Q8)

with the same estimate for Q_N^(-1), and an exact identity for M_N^±1.
Every prefix-composed embedding coordinate is holomorphic in widthR_L and
bounded by2 there. Cauchy therefore bounds its H5 norm by C R_L^(-5).
Telescoping at mostL conjugations proves, uniformly over words |w|<=L,

    ||W_N(w)*Op_N(a_j)W_N(w)-Op_N(a_j composed with F_w)||
          <= C L R_L^(-5) N^(-2).                          (Q9)

This is an explicit induction from the one-step estimate. It does not
assume an unproved long-word version of qualitative Egorov.

The following uniform smooth-symbol estimates follow directly from the
exact Weyl product and Fourier tail and are also derived in FM-023:

    ||Op_N(c)Op_N(v)-Op_N(cv)||
        <= C N^(-1)||c||_(H3)||v||_(H3),
    ||Op_N(c)|| <= C||c||_(H2),
    ||Op_N(c)||_N <= ||c||_(L2)+C N^(-2)||c||_(H3).           (Q10)

The last inequality truncates to a centered N-by-N Fourier cell, using
its exact Weyl orthogonality and the l1 norm of the remaining smooth tail.
It is valid for N-dependent smooth symbols. No alias-free assertion about
the whole symbol is made.

Put t_N(c)=tr_N(W_N(w)Op_N(c)). Q9, cyclicity and Q10 give for the scalar
embedding difference b chosen inQ3

    |t_N(cb)| <= C[R_L^(-3)N^(-1)||c||_(H3)
                   +L R_L^(-5)N^(-2)||c||_(H2)].             (Q11)

Choose a fixed smooth chi with 0<=chi<=1, chi=1 on[0,1], zero on[4,infinity),
and define, with the quotient smoothly zero near b=0,

    chi_epsilon=chi(b^2/epsilon^2),
    c_epsilon=(1-chi_epsilon)/b.

The chain rule and Cauchy derivative bounds yield

    ||c_epsilon||_(H3)<=C R_L^(-9)epsilon^(-4),
    ||c_epsilon||_(H2)<=C R_L^(-6)epsilon^(-3),
    ||chi_epsilon||_(H3)<=C R_L^(-9)epsilon^(-3).              (Q12)

Using Q7 for its support, Q10 for its normalized HS norm, and Q11 for
the complementary term gives

    |tr_N W_N(w)|
       <= exp(K_L^2)epsilon^(1/(2K_L))
          +C R_L^(-12)N^(-1)epsilon^(-4)
          +C(L+1)R_L^(-11)N^(-2)epsilon^(-3).               (Q13)

Enlarging the fixed C, and using K_L>=100/R_L, all prefactors are bounded
by C_0 exp(K_L^3). Set epsilon=N^(-1/8). The three powers are respectively
N^(-1/(16K_L)), N^(-1/2), and N^(-13/8), provingQ4.

## Q7. Check the explicit growth window rather than hiding it in constants

The displayed formulas give

    log K_L = O_tau(8^L+L^2+L log(L+1)).                     (Q14)

More explicitly, logB_L=216L[log(24L)+2L log(14d0)], while
J_L<=4000*8^L+1. No other dependence on word length occurs inK_L.

At L=L_N fromQ1,

    8^L <= (log logN)^(1/4),
    L^2=O((log log logN)^2),
    logK_(L_N)=o(log logN),
    K_(L_N)=(logN)^(o(1)).                                  (Q15)

In particular K_(L_N)^4 logK_(L_N)=o(logN), and

    K_(L_N)^3-logN/(16K_(L_N)) -> -infinity,
    K_(L_N)^3-(logN)/2 -> -infinity.

The common upper boundQ4 tends to zero, so taking a supremum over every
nonidentity word in that length window costs nothing further. This proves
the candidateQ2. The literal value of tau enters the enormous height
d0 and thus the startup; it is not sent to zero withN.

## Q8. Boundary and audit questions

This is a quantitative fixed-model mixed-word statement. It excludes an
approximate scalar word return with complexity at most the displayed
triple-logarithmic window, since scalar-return closeness would force a
normalized trace modulus approaching1. It gives no Heisenberg form factor,
no signed factorial comparison, and no microscopic CUE law. Pure U_N
logarithmic trace information in the existing corpus is stronger in its
different one-word-family direction.

The critical new audit obligations are: Roy's nearby-root height/degree
mapping; the global complex-strip width for arbitrary signed words; the
two-variable three-circle propagation; the finite-type patch constants;
and uniform alias-aware trace estimates for N-dependent cutoff symbols.
The formulas have been selected with large margins, not for useful sizes.
An explicit window has been written; a numerically evaluated startup and
an optimal growing-word rate have not been produced.
