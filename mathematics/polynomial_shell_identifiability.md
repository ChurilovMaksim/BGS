# Degree-independent identification from concentric intensity shells

Status: self-contained project proof. Priority relative to polynomial sphere maps, phase retrieval and low-rank Hermitian polynomial forms has not been established. This theorem is independent of BGS and is not a noisy-data stability theorem.

## 1. A rank bound for vanishing circles

Let M be a nonzero Hermitian (n+1) by (n+1) matrix of rank r. Set

    b(z)=(1,z,...,z^n)^T,
    H_M(z)=b(z)^* M b(z).

A positive zero radius is a number rho>0 such that H_M(rho exp(i theta))=0 for every theta.

**Theorem 1.** The number of distinct positive zero radii is at most r-1, independently of n. This bound is sharp at any prescribed r-1 positive radii.

Proof. Suppose M has a nonzero off-diagonal entry and choose the largest upper-diagonal lag L>=1 with one. The angular Fourier coefficient at that lag is

    rho^L B(rho^2), B(x)=sum_j M_(j,j+L)x^j.

If B has k nonzero monomials, at positions j_1<...<j_k, the submatrix

    (M_(j_a,j_b+L))_(a,b=1)^k

is lower triangular with nonzero diagonal: every entry above its diagonal has lag greater than L. Hence k<=rank(M)=r. A nonzero k-term complex polynomial has at most k-1 distinct positive zeros. To verify this last fact, rotate its coefficients by a scalar phase and take a real part which is not identically zero; divide by the lowest power and use Rolle's theorem inductively on its derivative. Thus r zero radii would contradict B!=0.

If M has no off-diagonal entry, exactly r diagonal entries are nonzero. H_M is then a nonzero r-term polynomial in |z|^2 and again has at most r-1 positive zero radii. This proves the bound.

For sharpness let B(x)=product_(s=1)^(r-1)(x-rho_s^2)=sum_(j=0)^(r-1)a_j x^j and take M=diag(a_0,...,a_(r-1)). Every coefficient is nonzero because the roots are positive, so M has rank r. Its zero radii are exactly those prescribed.

Unlike a coefficient Gram matrix, M may be indefinite. The argument uses matrix rank and Hermitian symmetry, not positivity.

## 2. Higher-dimensional concentric spheres

Let M be a nonzero Hermitian matrix indexed by the monomials z^alpha of degree at most n in C^m. Let b(z) be the column of those monomials and again H_M(z)=b(z)^*M b(z).

**Theorem 2.** H_M can vanish identically on at most rank(M)-1 distinct positive concentric spheres centered at zero.

Proof. Suppose it vanishes on r=rank(M) such spheres. Fix a unit vector u and restrict z=w u. The resulting one-variable Hermitian polynomial has coefficient matrix M_u=T_u^*M T_u, where T_u maps powers of w to their monomial coefficient columns. Thus rank(M_u)<=r. Theorem 1 makes M_u zero, because its polynomial vanishes on r distinct positive circles. This holds for every u, so H_M vanishes everywhere in C^m. The monomials z^alpha conjugate(z)^beta are linearly independent as polynomials in real and imaginary coordinates. Therefore M=0, a contradiction.

Sharpness of the universal rank bound is already attained for m=1. No claim of optimality for each separately fixed higher domain dimension is needed.

## 3. Sharp norm-identification theorem for vector polynomial maps

Let P:C^m -> C^d and Q:C^m -> C^e be holomorphic polynomial maps, of arbitrary finite degrees. Pad their coefficient arrays with zero columns so they use the same monomial vector, P=V b and Q=W b. Put

    M=V^*V-W^*W, rank(M)<=d+e.

**Corollary.** If ||P(z)||=||Q(z)|| on d+e distinct positive concentric spheres, then V^*V=W^*W. Consequently there is a linear isometry from the coefficient span of P onto that of Q taking P(z) to Q(z) for every z. When d=e this isometry extends to a fixed unitary U on C^d and Q(z)=U P(z).

Proof. The norm equality makes H_M zero on all the specified spheres, so Theorem 2 forces M=0. Equality of the coefficient Gram matrices makes the map sum_alpha a_alpha v_alpha -> sum_alpha a_alpha w_alpha well-defined and norm preserving. Extending orthonormal bases proves the unitary assertion in equal target dimensions.

The sharper number rank(V^*V-W^*W) is sufficient when that rank is known and nonzero. The d+e formulation is useful because it requires no advance knowledge of the coefficient arrays or their degree.

## 4. Optimality for equal target dimensions

For P,Q:C -> C^d, the bound 2d is sharp. Prescribe any 2d-1 distinct positive radii rho_s and expand

    B(x)=product_(s=1)^(2d-1)(x-rho_s^2)=sum_(j=0)^(2d-1)a_j x^j.

The coefficients alternate signs, with exactly d positive and d negative coefficients. Give P one component sqrt(a_j)z^j for each a_j>0, and Q one component sqrt(-a_j)z^j for each a_j<0. Then

    ||P(z)||^2-||Q(z)||^2=B(|z|^2).

They have equal intensity on every prescribed circle and nowhere else radially, yet no fixed unitary relates them because their global norm functions differ.

For d=2 write s_1,s_2,s_3 for the elementary symmetric sums of rho_1^2,rho_2^2,rho_3^2. One explicit pair is

    P(z)=(sqrt(s_2)z,z^3), Q(z)=(sqrt(s_3),sqrt(s_1)z^2).

Three prescribed circles cannot distinguish their intensity profiles; equality on four distinct circles would force unitary equivalence for any pair of two-output polynomial maps.

## 5. Interpretation and boundary

The conclusion uses intensity values on entire circles or spheres, not finitely many angular samples. The required number of radial shells is controlled by target dimension rather than polynomial degree. The theorem is exact: it gives no dimension-independent condition number for recovery from approximately equal intensities, and does not cover rational maps with poles or general infinite power series. Those restrictions are essential to the proof and are not removed by calling the maps analytic.
