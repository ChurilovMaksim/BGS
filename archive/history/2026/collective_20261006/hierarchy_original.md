# Exact collective occupation hierarchy through Heisenberg degree

6 October 2026. Author candidate, independent review required. The coordinate
operator sectors below are NOT Haar polynomial projections of spectral tests,
NOT the full balanced replica space, and NOT an alteration or phase average of
U_N. Haar integration appears only in the exact invariant Gram projector.
Prior ownership includes FLOW-019/020's different growing-degree spectral
projections, TRACE-014's full-copy Haar invariant projector and its norm
obstruction, and the existing Newton/hook/occupation bookkeeping.

## 1. Ambient space, grading, and exact corrected trace

Let W_m=(C^N)^tensor m and identify W_m tensor conjugate(W_m) with End(W_m),
using ordinary unnormalized HS. The SAME slot cycle on ket and bra acts as
R_m(X)=C_m X C_m*. This is the convention with
Tr_End(W_m)(R_m Ad(U^tensor m))=|Tr U^m|².

Let D_0 be the traceless diagonal matrices, of HS dimension d=N-1. For
1<=q<=m and B in Sym^q(D_0), insert B in all q-element subsets of the ordered
m slots, with identities elsewhere, to obtain J_(m,q)(B). Sym^q here refers
only to the local coefficient tensor, not to a Sym^m restriction of W_m.
Let P_H be the full U(N)-invariant projector on End(W_m), and set

 Y_(m,q)(B)=(I-P_H)J_(m,q)(B),  H_(m,q)=range Y_(m,q).

Each local tensor has zero partial traces. Haar conjugation preserves that
property. Hence distinct slot subsets, and distinct q, are HS orthogonal,
both before and after Haar projection. The normalization factor at order q is
L_(m,q)=binom(m,q)N^(m-q); it cancels in the corrected operator trace.
Every H_(m,q) is fixed by R_m because its operators are invariant under
CONJUGATION by slot permutations. No one-sided cycle is being substituted.

For any unitary U, let P_U=(|U_ab|²), T_U=P_U-J acting on D_0. Define

 H_(q,N)=E_(V Haar in U(N)) Sym^q(T_V),
 G_(q,N)=I-H_(q,N).                                                 (C1)

H_(q,N) is the compression of an orthogonal Haar projector, hence is positive
and self-adjoint. H_(1,N)=0. The exact inner products are

 <Y_(m,q)(B),Y_(m,q)(C)>=L_(m,q)<B,G_(q,N)C>,
 <Y_(m,q)(B),Ad(U^tensor m)Y_(m,q)(C)>
   =L_(m,q)<B,[Sym^q(T_U)-H_(q,N)]C>.                              (C2)

Once G is inverted as justified below, the entire centered collective
occupation hierarchy H_(m,coll)=orthogonal sum_(q=1)^m H_(m,q) has EXACT trace

 S_(m,N)(U)=sum_(q=1)^m
   Tr[G_(q,N)^-1(Sym^q(T_U)-H_(q,N))].                             (C3)

Its dimension is binom(N+m-1,m)-1. Thus C3 retains every collective occupation
degree through m, including m>N. It is still only one specified subspace of
the much larger balanced replica space. Its orthogonal projector need not
commute with the compressed memory kernel K.

## 2. Uniform Gram conditioning, with no stable-degree restriction

For Haar V the exact fourth entry moments give

 E(T_V*T_V)=E(T_V T_V*)=I_(D0)/(N+1),  ||T_V||<=1.                 (C4)

For completeness E|V_ia|^4=2/[N(N+1)] and
E|V_ia|²|V_ib|²=1/[N(N+1)] for a!=b; these follow from a normalized vector
of independent complex Gaussians. Summing rows and subtracting J yields C4.

For q>=2 and any v in D_0^tensor q, factor two distinct tensor legs:

 |<v,T_V^tensor q v>|
 =|<(T_V* on leg1)v,(T_V on legs2...q)v>|
 <=||(T_V* on leg1)v|| ||(T_V on leg2)v||.

The other legs are contractions. Cauchy–Schwarz in Haar V and C4 give

 0<=H_(q,N)<=I/(N+1),
 ||G_(q,N)^-1||<= (N+1)/N,                                        (C5)

for EVERY q>=2. There is no conditioning singularity at q=N. This is an
actual invariant-Gram identity, not a universality statement about a moment
channel; TRACE-014's extraction-norm warning remains relevant.

The image of H_(q,N) is obtained by restricting invariant symmetric tensors
on traceless Hermitian matrices to their diagonal Cartan space. Spectral
diagonalization identifies those polynomials with symmetric polynomials of
traceless eigenvalues, generated in degrees 2,...,N. Restriction is injective
and its adjoint projection is onto, so

 rank H_(q,N)=r_N(q)=[z^q] product_(j=2)^N (1-z^j)^-1 <=p(q).        (C6)

The elementary Euler-product estimate gives p(q)<=exp(3sqrt(q)) for q>=1:
log product_j(1-e^-tj)^-1<=pi²/(6t), and optimize t.

## 3. Exact degree generating formula and its scope

For |z|<1, termwise Haar integration is absolutely justified by the finite
dimension d and the contraction ||T_V||<=1. Thus

 sum_(q>=0) z^q Tr H_(q,N)
     =E_Haar det_(D0)(I-z T_V)^-1,  H_(0,N)=1.                     (C7)

Every coefficient is nonnegative. No finite value at z=1 is assumed.
Indeed N=2 supplies a failure control: T_V is the scalar 2X-1 with X uniform
on [0,1], so H_(2k,2)=1/(2k+1), H_(2k+1,2)=0. Therefore

 sum_(q=2)^m Tr[H_(q,2)(I-H_(q,2))^-1]
                       =(1/2)sum_(k=1)^floor(m/2)1/k,              (C8)

which diverges with m. The finite Heisenberg-degree result below is uniform
as N grows with m<=bN; it asserts no infinite-degree negative moment for any N.

## 4. An elementary Haar tail sufficient for finite degrees q<=bN

For all N>=20, with rho=sqrt(159/160)<1,

 Pr_Haar(||T_V||>rho)<=4N² exp(-N/160).                             (C9)

Here is a direct proof. A Haar row u is z/||z|| with independent complex
Gaussian coordinates, so X_j=|z_j|² are independent mean-one exponentials.
Except with probability at most exp(-N/40)+exp(-N/4), at least N/10 indices
have 1<=X_j<=2 and sum_j X_j<=2N. The count estimate uses
Pr(1<=X<=2)=e^-1-e^-2>1/5 and the elementary Bernoulli Chernoff lower tail;
the norm estimate uses the exponential Chernoff upper tail. On this event,
there is a coordinate set I with |I|>=N/10 and |u_j|²>=1/(2N) on I.

Conditional on u, a second Haar row v is uniform on the unit sphere of u^perp.
The subspace C^I intersect u^perp has dimension at least |I|-1>=N/20. A
Gaussian representation on u^perp shows, except with probability at most
exp(-N/160)+exp(-N/8), that at least N/40 Gaussian squared norm lies in that
subspace while the total is at most2N. Thus sum_(j in I)|v_j|²>=1/80 and

 sum_j |u_j|²|v_j|²>=1/(160N).

These estimates are uniform in the conditioned row. Union bound over row
pairs gives C9: all entries of P_V P_V* are at least1/(160N), diagonals
included by Cauchy–Schwarz. Consequently
P_V P_V*=J/160+(159/160)R with R symmetric doubly stochastic and nonnegative.
On mean-zero vectors its largest eigenvalue is at most159/160.
No independence between different rows is assumed.

Let

 A_(m,N)=sum_(q=2)^m Tr[H_(q,N)(I-H_(q,N))^-1].                     (C10)

For every fixed b<infinity and epsilon>0,

 sup_(2<=m<=bN) A_(m,N)<=C_(b,epsilon) N^(-1+epsilon).               (C11)

For m>=2 the lower bound A_(m,N)>=1/N follows from the exact q=2 term.
To prove the upper bound, C5, C6 and C9 give

 Tr H_(q,N)<=r_N(q) min{1/(N+1), rho^q+4N²e^(-N/160)}.

Split at L=floor((epsilon log N/6)^2). The q<=L sum is at most
L exp(3sqrt L)/(N+1)=O_epsilon(N^(-1+epsilon)). For q>L, the good-event
sum sum_q exp(3sqrt q)rho^q is superpolynomially small in N; for the bad event,
summing only q<=bN costs at most4bN³ exp(3sqrt(bN)-N/160), exponentially small.
Multiplication by (N+1)/N bounds C10 using C5. Finitely many startup values
are absorbed into C_(b,epsilon). The restriction q<=bN is ESSENTIAL to this
argument; no uncontrolled z-up-to-one determinant expectation is used.

## 5. Resumming the actual collective trace

For the actual unchanged U_N, FM-021 gives ||T_N||<=1/2 eventually and
P_N(a,b)<=C/N. Hence ||T_N||_HS²<=C and |Tr T_N|<=C+1. At |z|=3/2,

 log det(I-zT_N)^-1=sum_(k>=1) z^k Tr(T_N^k)/k,
 |Tr T_N^k|<=C 2^(-(k-2)) for k>=2.

The generating function is bounded uniformly in N on that circle. Cauchy
therefore gives absolute summability of its symmetric-power coefficients,
with an exponential remainder after degree m:

 sum_(q=1)^m Tr Sym^q T_N
           =det_(D0)(I-T_N)^-1-1+O_C((2/3)^m).                     (C12)

The extra Gram-weighted actual term is bounded uniformly in m by

 sum_(q=2)^m |Tr[H_q(I-H_q)^-1 Sym^q T_N]|
 <=N^-1 sum_(q>=2)r_N(q)2^-q=O(N^-1).                              (C13)

The infinite partition generating product at z=1/2 is finite. Combining
C3 and C10–C13, for every fixed b and epsilon>0,

 S_(m,N)(U_N)=det_(D0)(I-T_N)^-1-1
        +O_(b,epsilon)(N^(-1+epsilon)+(2/3)^m),  2<=m<=bN.          (C14)

In particular S_(m,N)(U_N)=O_b(1) on compact positive Heisenberg bands, and
its original N^-2 compact-time aggregate is O_w(N^-1). This is a signed
trace of an exponential-dimensional, all-multiplicity coordinate sector.
It is not the entire charge-zero trace Tr(R Pi C_U), nor the full trace
Tr(R C_U); most balanced coherence and nontrivial permutation sectors remain.
It does not supply the O(N) plateau correction or prove BGS.

## 6. Exact finite Kostka matrix for independent checks

At cap degree m, let n run over contents |n|=m, lambda over partitions of m
with length<=N, M_n=m!/product_i n_i!, f_lambda the Specht dimension,
d_lambda=s_lambda(1^N), and K_(lambda,n) the Kostka multiplicity. Define

 R_(n,lambda)=sqrt(f_lambda/d_lambda) K_(lambda,n)/sqrt(M_n).          (C15)

This follows by restricting the central Schur projector to a weight space:
its diagonal is constant on each ordered-word content class, and the total
weight-space trace is f_lambda K_(lambda,n). The nonzero spectrum of R*R
is exactly {1} together with all nonzero spectra of H_(q,N), 2<=q<=m.
The constant eigenvector is sqrt(f_lambda d_lambda/N^m).
Thus C10 can be computed from this finite matrix after removing that one
constant direction. Algebraic matrix entries can be handled by a diagonal
similarity to avoid square roots. No numerical pattern is used to prove C11.
