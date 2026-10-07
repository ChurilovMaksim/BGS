# An actual common-fixed-point outlier rules out strong freeness

Author continuation candidate, 7 October 2026. This note keeps the literal
actual Q_N=exp(i tau N A_N), M_N, and tau=10^(-80). It is a counterexample
to strengthening their fixed-word moment law to operator-norm convergence.
It is not a counterexample to the microscopic statistics of U_N=Q_N M_N.
All inputs and source conventions are those of `fixed_word_freeness.md`.

## S1. A fixed phase-free polynomial and its two incompatible norm scales

Define the actual commutator and its cat translate

    C_N=Q_N M_N Q_N* M_N*,
    D_N=M_N C_N M_N*,
    H_N=(C_N+C_N*+D_N+D_N*)/4.                                (S1)

H_N is self-adjoint, ||H_N||<=1, and every coefficient in this polynomial
is fixed independently of N. Global scalar phases in Q_N or M_N cancel.

**Claim.** The empirical spectral measure of H_N has the moment limit of
the normalized adjacency operator on the four-regular tree, whose spectral
radius is sqrt(3)/2. Nevertheless

    liminf_(N odd ->infinity) lambda_max(H_N) >= 1-10^(-148).  (S2)

Thus (Q_N,M_N) are asymptotically free Haar in normalized *-moments but
not strongly asymptotically free. The common equilibrium supplies a spectral
outlier for this derived fixed polynomial. The statement does not identify
an eigenphase cluster of U_N and changes none of its target hypotheses.

## S2. A local coherent-state estimate from the exact raw matrices

Let phi_N be the normalized periodization on the N-point torus grid of

    phi_N(j) proportional to sum_(l in Z) exp(-pi(j+lN)^2/N).

Normalization is in ordinary Euclidean l2; choosing normalized coordinate
l2 instead does not affect unit-vector expectations after renormalization.
The state is centered at P=(0,0). Let a be a fixed finite Fourier symbol
with da(P)=0 and a(P)=a_0. Then

    limsup_N N||(Op_N(a)-a_0)phi_N||
       <= 6 sum_v |a_hat(v)| |v|^2.                          (S3)

Here Fourier labels v=(a,b) use e_v(q,p)=exp(2pi i(bq+ap)). The raw-to-
midpoint dictionary is essential. On centered integer representatives,

    (W_N(a,b)psi)(j)=exp(2pi i b(j+a/2)/N) psi(j+a).

Put y=j/sqrt(N), epsilon=N^(-1/2), and f(y)=2^(1/4)exp(-pi y^2), of L2
norm one. Away from exponentially small periodization tails this is exactly
the sampled continuous Weyl action

    exp(epsilon L_v)f,     L_v=a d/dy+2pi i b y.

Taylor expansion on the Schwartz vector f gives

    exp(epsilon L_v)f=f+epsilon L_v f+(epsilon^2/2)L_v^2 f
                       +O_(v)(epsilon^3) in L2.             (S4)

The same expansion holds for sampled norms, by Riemann sums for Schwartz
functions; the tails from noncentral periodization images are exponentially
small, also after multiplication by N. There are only finitely many fixed
Fourier labels. The a_0 term cancels and da(P)=0 cancels sum a_hat(v)L_v.
Hence the scaled residual converges in norm to one half of the sum of the
L_v^2 f terms. Directly, with z=-a+ib,

    L_v^2 f=2pi a z f+4pi^2 z^2 y^2 f,
    ||y^2 f||=sqrt(3)/(4pi).

Thus

    ||L_v^2 f|| <= pi(2+sqrt(3))|v|^2 <12|v|^2,

which proves S3. This is a local quadratic estimate for fixed symbols; it
does not assume global pseudodifferential positivity or growing-frequency
uniformity. It can equivalently be proved by Taylor-expanding the displayed
Gaussian shifts and modulation factors before taking Gaussian Riemann sums.

## S3. Apply the estimate at the exact common equilibrium

For the actual centered physical symbol, g(P)=9/10, dg(P)=0, and the exact
coefficient bound inherited from FM-001 is

    sum_v |g_hat(v)| |v|^2 <= 51451/1000 <52.

The point P is fixed by S. Exact cat Egorov gives, for j=0,1,2,

    N||(A_N-9/10)M_N^(-j)phi_N||
       =N||(Op_N(g composed with S^j)-9/10)phi_N||.

The transformed symbols still have zero differential at P and are fixed
finite Fourier symbols. Since ||S||<7, S3 yields

    limsup_N N||(A_N-9/10)M_N^(-j)phi_N|| <= B_j,
    B_j=312*7^(2j),       j=0,1,2.                           (S5)

Write Q'_N=exp(-i tau N*9/10)Q_N. For every vector psi, spectral calculus
or Duhamel gives the exact estimate

    ||(Q'_N-I)psi|| <= tau N||(A_N-9/10)psi||.                (S6)

The same norm bound holds for Q'_N* because |exp(iu)-1| is even. Although
tau N is unbounded, S5 cancels this factor on the specified local states.
No expansion in tau N is made.

Scalar phases cancel from C_N. The identity

    C_N-I=Q'_N M_N(Q'_N*-I)M_N*+(Q'_N-I)

therefore implies

    limsup_N ||(C_N-I)phi_N|| <= tau(B_0+B_1),
    limsup_N ||(D_N-I)phi_N|| <= tau(B_1+B_2).                 (S7)

The second inequality applies the first telescoping identity to M_N*phi_N
and uses D_N-I=M_N(C_N-I)M_N*. Only unitary norm preservation is used.

For any unitary V and unit vector phi,
Re<phi,V phi>=1-||(V-I)phi||^2/2. Consequently

    <phi_N,H_N phi_N>
      =1-(||(C_N-I)phi_N||^2+||(D_N-I)phi_N||^2)/4.

Now B_0=312, B_1=15288, B_2=749112, so

    [(B_0+B_1)^2+(B_1+B_2)^2]/4=146137680000.

Multiplication by tau^2=10^(-160) is less than 10^(-148). The variational
principle proves S2.

## S4. Why the moment-limit polynomial has radius sqrt(3)/2

In the free group F_2=<q,m>, set q_j=m^j q m^(-j). The three elements
q_0,q_1,q_2 freely generate: after combining adjacent powers of an equal
q_j, any nonempty reduced word expands to nonzero q-powers separated by
nonzero m-powers, hence cannot freely reduce to the identity.

The words represented by C_N,D_N are

    c=q_0 q_1^(-1),     d=q_1 q_2^(-1).

The triple (c,d,q_2) is another free basis of the same rank-three group:
q_1=d q_2 and q_0=c d q_2 provide the inverse substitution. Thus c and d
freely generate a rank-two subgroup. The normalized trace of any nontrivial
word in C_N,D_N tends to zero by Theorem F. Their *-moment limit is therefore
two free Haar unitaries too, so H_N's limiting moments are those of

    H_free=(lambda(c)+lambda(c)^*+lambda(d)+lambda(d)^*)/4

on the regular representation of that subgroup. This is normalized adjacency
on the four-regular tree.

For completeness its norm is sqrt(3)/2 by an elementary tree calculation.
For unnormalized adjacency A, the positive radial weight f(v)=3^(-r/2),
where r is distance from the root, has Af/f=2sqrt(3) off the root and
4/sqrt(3)<2sqrt(3) at the root. Weighted Cauchy-Schwarz/Schur bounds
||A||<=2sqrt(3). Truncate f at radius R. Its norm squared is 1+4R/3 and
its adjacency quadratic form is 8R/sqrt(3), so its Rayleigh quotient tends
to 2sqrt(3). Hence ||H_free||=sqrt(3)/2.

Since all H_N are bounded in [-1,1], convergence of all moments also gives
weak convergence of the empirical measures. S2 forces actual high outliers
outside the limiting support; their proportion tends to zero. No count or
rate for those outliers is asserted.

## S5. Interpretation and boundary

This is an actual-model failure of strong freeness, proved using the same
fixed common equilibrium that establishes the derivative representation.
Macroscopic moment cancellation sees almost every phase-space point, while
operator norm can see localized states at the common equilibrium. There is
no contradiction between Theorem F and S2.

It rules out upgrading the new fixed-word free moment law to a strong
free-probability norm comparison. It does not refute TRACE-005, microscopic
CUE, fixed-model spectral simplicity, or the scalar pair-commutant theorem.
H_N is a derived polynomial in the actual factors, not the BGS propagator.
No new spectral model or altered coupling is used to obtain the obstruction.
