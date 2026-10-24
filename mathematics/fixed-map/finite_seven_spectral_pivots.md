# BGS finite spectral-pivot certificates

Date: 2026-10-06. Status: finite computer-assisted project result with independent exact outward-interval audit.

## Exact finite claim

For each **N in {21, 35, 49, 63}**, the unchanged frozen generator A_N has N distinct real eigenvalues. Order them decreasingly. In an eigenbasis in that order, every leading principal minor of the unchanged raw cat matrix M_N is nonzero.

Subject to the accepted implementation and the already-maintained large-imaginary-time/Lindemann–Weierstrass argument in `mathematics/fixed-map/frozen_algebraic_spectral_simplicity.md`, Section 4, this proves simple spectrum of U_N(t)=exp(it A_N) M_N for **every nonzero real algebraic t** in these four dimensions, including t=10^-80 N. This is a finite-dimensional addition only. It is not an all-seven-divisible theorem, a quantitative eigenphase-gap estimate, a common-commutant inference, or BGS.

For **N=7**, A_7=(9/10)I and the actual U_7(t) is never simple. The separate exact cyclotomic computation proves that its cat factor has at most three distinct eigenvalues.

## Authority and model conventions

Base repository: `BGS checkout`, HEAD `41a2788ef21e787e983e88a8b58470d104013740`, clean at the recorded pre-run check. Authoritative mathematical inputs:

- `mathematics/fixed-map/frozen_kick_rank_boundary.md`, Section 1: A diagonal, off-diagonal, exact zero bonds, chain decomposition.
- `mathematics/fixed-map/fixed_model_symmetry_theorem.md`, Section 1: raw modular cat kernel.
- `mathematics/fixed-map/frozen_algebraic_spectral_simplicity.md`, Section 4: sufficient leading-minor criterion and fixed-algebraic-time implication. Its theorem for 7 not dividing N is prior work; no claim of a new asymptotic argument is made here.

With h=2^{-1} mod N, r_x=(1-cos(14 pi x/N))(1+cos(2 pi x/N)), the upper A bond is eta-bar r_{x+h}/200, eta=(-3+4i)/5. Cut bonds satisfy 7(x+h)=0 mod N exactly. Each path starts at the vertex immediately after a cut and advances by +1 modulo N. Its length is N/7. On this path D_j=eta^j obeys D* A D=J, where J is real tridiagonal with positive off-diagonals r_{x+h}/200. The diagonal is cos(14 pi x/N)+r_x/10+r_x sin(2 pi x/N)/100-1/10.

The computation uses G=sqrt(N) M, whose entries are exp(2 pi i [-8^{-1}(3x^2-2xy+3y^2)]/N). The omitted nonzero scalar does not affect any minor's nonvanishing.

## What the program proves, assuming ordinary Python integer semantics

1. Every interval is [l/2^P,h/2^P], where l,h are integers and P=512. Addition is exact; multiplication uses the minimum/maximum endpoint products followed by floor/ceiling division. Division uses all endpoint quotients and rejects intervals containing zero. Squaring is tightened when the input straddles zero. All scientific branch decisions use integer inequalities.
2. Pi is enclosed by Machin's identity pi=16 atan(1/5)-4 atan(1/239). Each arctangent uses an exact rational alternating sum and the first-omitted-term bound, then rounds outward to the dyadic grid.
3. Angles are reduced to (-pi,pi]. Cosine and sine are enclosed by Taylor polynomials of degrees 2K and 2K+1. K is selected exactly so 4^(2K+1)/(2K+1)! <= 2^-P. Since |angle|<4, the Lagrange remainder of each polynomial is at most 2^-P. Interval evaluation includes all rounding and pi uncertainty. Each final trigonometric interval is expanded by one dyadic unit at both ends. No library trigonometric function is used.
4. The real Jacobi characteristic determinants at a dyadic q obey p_0=1, p_1=d_0-q, p_{j+1}=(d_j-q)p_j-b_{j-1}^2 p_{j-1}. If every interval determinant excludes zero, the number of sign variations equals the number of eigenvalues below q. No uncertain sign is accepted. The proven bound ||A||<=79/50<2 initializes root-independent bisection at [-2,2]. Every accepted final interval has width <=2^-384 and endpoint Sturm counts k,k+1. All N intervals across the seven paths are then strictly separated by integer endpoint comparison. This certifies A's simple spectrum and the ordering.
5. For each enclosed eigenvalue lambda, a real eigenvector is determined by v_0=1, v_1=(lambda-d_0)/b_0, v_{j+1}=((lambda-d_j)v_j-b_{j-1}v_{j-1})/b_j. The positive b_j intervals permit division. Multiplication by D returns an eigenvector of the original complex A. Every actual component is enclosed.
6. Let V be these eigenvectors in certified decreasing order. Direct interval summation encloses H=V* G V. The eigenvectors need not be normalized: because A is Hermitian and simple, V=Q R for an orthonormal eigenbasis Q and an invertible diagonal normalization R. For every leading index set I, det H_I=|det R_I|^2 det(Q*GQ)_I. Thus the tested nonvanishing is the required eigenbasis nonvanishing.
7. Complex interval Gaussian elimination proceeds **without row or column permutations**. Every pivot rectangle excludes zero, and the denominator used in complex division has a strictly positive interval lower bound. The exact leading determinant of order k is the product of the first k exact pivots, so all leading principal minors are nonzero. Interval dependence may enlarge uncertainty but cannot create a false successful exclusion.
8. The original author implementation rejected disabled assertions; the maintained independent replay instead uses explicit checks that remain active under optimization. No floating-point eigensolver, floating trigonometry, or numerical tolerance enters certification. `screen.py` and part of `controls.py` use ordinary floating arithmetic solely as separately labeled diagnostics.

## Why this finite condition suffices

For ordered eigenvalues a_1>...>a_N and nonzero leading minors b_r, the rth characteristic coefficient of exp(sA)M has leading term b_r exp(s(a_1+...+a_r)). The top r-element subset is the unique largest exponent. The resulting separated scales give N distinct eigenvalues for sufficiently large real s (the maintained Section 4 uses Rouché). Consequently the time-dependent discriminant is a nonzero exponential polynomial with algebraic coefficients and real algebraic frequencies. At a nonzero algebraic t, grouping equal frequencies and applying the checked Lindemann–Weierstrass input prevents its vanishing. This implication does not require a uniform lower bound on a gap or minor.

This package does not re-audit the external transcendence theorem. Any promotion must retain the canonical theorem's stated external-dependency and review boundaries. In particular no general irreducibility-to-simple-spectrum implication is used.

## Already published exception

The exact N7 multiplicities and dimension are owned by
[FM-024](actual_seven_primary_commutant.md), not a new claim here.

## Portable replay and provenance

Run `python computations/verification/spectral_extensions.py --mode pivots`.
The independent replay uses exact outward decimal intervals, a separate pi
identity, Horner trigonometry, LDL inertia and reversed eigenvector recurrence.
All 168 root intervals and all 168 leading pivots are checked independently.
Its mathematical interval outputs must agree with the original independent
review; elapsed time and Python version are execution metadata only.
The original author instructions, control results and dyadic certificate inputs
remain source-bound historical provenance. The independent replay uses explicit
failures under normal and optimized Python; original assertions are preserved
only in historical source files. No floating screen is a proof input.

The large-imaginary-time and registered Lindemann–Weierstrass implication is
prior FM-008 Section 4. Its review and external-source boundaries are inherited,
not re-proved by this finite checker. The new scope is exactly four dimensions.
