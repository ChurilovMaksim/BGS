# Uniform microscopic source bounds from rank-one resampling

7 October 2026. Author derivation, independent review pending. This addendum does not alter the frozen compact_projector.md or uniform_abel_bound.md. It concerns the exact independent-phase ensemble V=DU for an arbitrary fixed N by N unitary U. It does not identify a limiting law.

## Main result

For s with Re s>0 define

X_N(s) = N^-1 Tr[ exp(-s/N) V (I-exp(-s/N)V)^-1 ].

For every sigma>0 and every integer p>=2,

sup_{N,U,Re s>=sigma} ||X_N(s)||_{L^p} <= L(sigma) p,
L(sigma)=100/(1-exp(-sigma)).                                  (1)

The numerical constant is deliberately loose. Therefore

sup_{N,U,Re s>=sigma} E exp[ |X_N(s)|/(2e L(sigma)) ] <= 2.      (2)

This controls the complex resolvent trace, including its imaginary part; dropping signs from the imaginary Cauchy kernel would only give a logarithmically growing estimate.

For any finite collection of retarded and advanced determinant ratios, write denominator sources a_j=exp(-s_j/N), b_l=exp(-t_l/N), and numerator sources c_j=exp(-(s_j+xi_j)/N), d_l=exp(-(t_l+eta_l)/N). Suppose every Re s_j,Re t_l>=sigma_*>0. Put

rho_* = 1/[2e L(sigma_*/2)].

If sum_j |xi_j|+sum_l |eta_l|<=rho_*, then

E | product_j det(I-c_j V)/det(I-a_j V)
      product_l det(I-d_l V*)/det(I-b_l V*) | <= 2,              (3)

uniformly in N and U. Since rho_*<sigma_*/2, all source paths remain strictly inside the unit disk. Thus the complete microscopic generating functions are locally uniformly bounded on a genuine complex source neighborhood, and every fixed source derivative is uniformly bounded there by Cauchy's formula in the microscopic variables xi,eta.

For the pair formula in compact_projector.md this is a bound on the full compact signed functional, not the absolute sum of its 4^N sectors. The proof also applies directly to any fixed number of original determinant ratios without invoking an unproved higher-flavor color-one CFT.

## 1. Generalized Minami resampling

Conditional spectral averaging and rank-one cyclic interlacing are proved in uniform_abel_bound.md. For a connected arc A, let Z=N_A and m=N|A|/(2pi). They imply, for every integer k>=0,

E (Z)_k <= m^k.                                                (4)

Here (Z)_k is the nonnegative count of ordered distinct k-tuples. For the induction, write

(Z)_k = sum_i <i,1_A(V)i> (Z-1)_(k-1).

When Z=0 the spectral weight is zero, so the potentially negative formal argument Z-1 is never used. When Z>=1, rank-one resampling gives Z-1<=Z' with both arguments nonnegative. The integer falling factorial n↦(n)_(k-1) is nondecreasing on n>=0, including its zero range. Integrating the spectral weight conditional on the resampled phase gives |A|/(2pi), and induction yields (4).

Consequently, for t>=0,

E exp[t(Z-m)] <= exp[m(exp(t)-1-t)],                            (5)

by the finite expansion exp(tZ)=(1+(exp t-1))^Z and (4). Also E Z=m and Var Z<=m, from k=1,2.

This is the standard generalized Minami resampling mechanism, adapted here to multiplicative unitary rank-one phases. A matching prior nested-interval statement and higher-order extensions are in Combes, Germinet and Klein, Generalized Eigenvalue-Counting Estimates for the Anderson Model, Theorem 2.1, equation (2.7), https://escholarship.org/uc/item/0kh9c48w . The present proof is self-contained for the precise finite-unitary hypotheses and makes no novelty claim for this mechanism.

For completeness, nested arcs A_1⊂...⊂A_k give the stronger ordered distinct-eigenvalue count bound

E sum_{j_1,...,j_k distinct} product_l 1_{A_l}(lambda_{j_l})
 <= N^k product_l |A_l|/(2pi).                                 (6)

The count is the combinatorial nonnegative version of product_l(N_{A_l}-l+1). Choose the first point in A_1, remove it, and resample the corresponding coordinate phase. Every remaining nested count drops by at most one. Monotonicity of the resulting count of injective assignments and conditional spectral averaging close the induction. Formal products with negative factors are not used as inequalities.

## 2. Centered count moments, including the lower tail

From (5), the usual elementary Poisson Chernoff bound gives, for x>=0,

P(Z-m >= sqrt(2mx)+2x) <= exp(-x).

For example, expand exp(t)-1-t<=t^2/[2(1-t/3)] on 0<t<3 and optimize; the displayed 2x is a conservative constant. Comparison with an exponential random variable and Minkowski then gives

||(Z-m)_+||_p <= sqrt(2mp)+2p.

The negative part needs a different argument; (5) was not asserted for negative t. Since 0<=(m-Z)_+<=m and Var Z<=m,

E[(m-Z)_+^p] <= m^(p-2) E[(Z-m)^2] <= m^(p-1),

for every integer p>=2. Hence

||Z-m||_p <= sqrt(2mp)+2p+m^(1-1/p).                            (7)

This weaker lower-tail estimate is enough because the Cauchy kernel integrates it with a summable power. It avoids falsely claiming two-sided Poisson concentration from the factorial upper bound.

## 3. Resolvent trace as an integral of centered arc counts

First take real s>0, r=exp(-s/N), delta=1-r, and f_r(theta)=r exp(i theta)/(1-r exp(i theta)). Its mean over the circle is zero. Let

C_+(u)=N_(0,u] - Nu/(2pi),
C_-(u)=N_[-u,0) - Nu/(2pi),     0<=u<=pi.

For almost every phase configuration there are no eigenvalues at the fixed endpoints. Stieltjes integration by parts gives

X_N(s) = -(1/N) integral_0^pi [f_r'(u) C_+(u)-f_r'(-u) C_-(u)] du.       (8)

The boundary contributions at pi cancel because f_r(pi)=f_r(-pi) and C_+(pi)+C_-(pi)=0. No deterministic bulk contribution remains, because f_r has mean zero.

For 0<=u<=pi,

|f_r'(u)| = r/[delta^2+4r sin^2(u/2)] <= pi^2/(delta+u)^2.      (9)

Indeed sin(u/2)>=u/pi and (delta+u)^2<=2delta^2+2u^2. Apply Minkowski, (7) with m=Nu/(2pi), and (9). The three resulting elementary integrals give

||X_N(s)||_p
 <= pi^(5/2) sqrt[p/(N delta)]
    +4pi^2 p/(N delta)
    +pi^3 p (N delta)^(-1/p).                                  (10)

The first integral uses integral_0^infinity u^(1/2)/(delta+u)^2 du=pi/(2sqrt(delta)). The third uses

integral_0^infinity u^(1-1/p)/(delta+u)^2 du
 = delta^(-1/p) Gamma(2-1/p)Gamma(1/p)
 <= delta^(-1/p) pi p/2.

Now N(1-exp(-s/N))>=1-exp(-sigma) for s>=sigma and N>=1. Since sigma_0=1-exp(-sigma)<1 and p>=2, the right side of (10) is at most

[(pi^(5/2)+pi^3) sigma_0^(-1/2)+4pi^2 sigma_0^(-1)]p
 <= 100 sigma_0^(-1) p.

This proves (1) for real s. For complex s, exp(-s/N)V differs from exp(-Re s/N)V by a common scalar phase. The ensemble is rotation invariant, so it has the same distribution and the same bound.

## 4. Exponential moments and complex source shifts

If ||X||_p<=Lp for all integer p>=2, then E|X|<=2L and p!>=(p/e)^p imply

E exp(|X|/(2eL))
 <=1+1/e+sum_{p>=2}(1/2)^p <2.

This proves (2).

Use the analytic logarithm log det(I-zV)=-sum_{m>=1}z^m Tr(V^m)/m on |z|<1. For a complex microscopic shift xi with the connecting segment in Re s>0,

log[det(I-exp(-(s+xi)/N)V)/det(I-exp(-s/N)V)]
 = xi integral_0^1 X_N(s+t xi)dt.                              (11)

Minkowski and (1) therefore bound its L^p norm by L(sigma)|xi|p whenever the segment stays in Re s>=sigma. The same estimate holds for V*, since it is another independent-phase ensemble after transposition, with fixed unitary conjugate(U).

For all the source shifts in (3), every segment stays in Re>=sigma_*/2. The L^p norm of the sum of absolute logarithm increments is at most L(sigma_*/2)rho_* p=p/(2e). The exponential estimate just proved gives (3).

For a concrete derivative statement, with K total numerator shifts, the polydisk |xi_j|,|eta_l|<rho_*/K is admissible. If H_N is the averaged generating function in those microscopic variables, then for every multiindex alpha,

|partial^alpha H_N(0)| <= 2 alpha! (K/rho_*)^|alpha|.           (12)

Smaller polydisks give the same control around any interior point. Differentiation under expectation is justified by the uniform L^1 bound on compact subpolydisks and the analytic sample functions. This is uniform fixed-order source control; it is not growing-order asymptotics or convergence to a specified limiting generating function.

## 5. Positive Poisson-trace Laplace functional

Equation (6) also gives a direct all-order positive statement. If f>=0 and all of its superlevel sets are connected arcs, then

E product_j [1+t f(lambda_j)] <= exp[t N integral f dtheta/(2pi)], t>=0.

Layer-cake and (6) prove the factorial coefficient bounds. Replacing t f by exp(t f)-1 yields

E exp[t sum_j f(lambda_j)]
 <= exp[N integral (exp(t f)-1) dtheta/(2pi)].                  (13)

For f=P_r/N, put M=(1+r)/[N(1-r)]. Since 0<=f<=M and N integral f=1, the chord bound for exp gives

E exp[(t/N)sum_j P_r(lambda_j)]
 <= exp[(exp(tM)-1)/M].                                       (14)

This is a genuine uniform exponential-moment estimate at r=exp(-s/N). It is useful in its own right, while the centered-count argument above is what also handles generic complex source directions.

## 6. Exact boundary of the result

The compact color-one identity now has a complete, dimension-uniform microscopic source neighborhood on which its total value and all fixed derivatives are bounded. No assertion says that individual compact sectors, or separately regulated original bulk/surface terms, have these bounds. The proof uses the original random-phase ensemble to control the completed sum.

This closes a uniform-integrability/source-regularity obligation. It does not close the separate identification obligation: neither the bound nor normal-family compactness determines the limiting function. Diagonal U supplies a Poisson limit and cyclic U supplies rigid alternatives while satisfying these universal estimates. The actual flatness and reverse-gap hypotheses have not yet been converted into the required signed cancellation. The unchanged deterministic off-charge defect remains separate.
