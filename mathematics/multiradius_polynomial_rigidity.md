# Sharp multiradius rigidity for vector polynomials

Status: self-contained project proof. Priority has not been established by an exhaustive literature review. This general algebraic theorem is independent of the BGS conjecture and of any numerical experiment.

## 1. A bound independent of polynomial degree

Let

    P(z)=sum_(j=0)^n v_j z^j, v_j in C^d,
    r=dim_C span{v_0,...,v_n}>=1.

A positive radius rho is called flat when ||P(rho exp(i theta))||^2 is independent of theta.

**Theorem 1.** Exactly one of the following alternatives holds:

(a) the nonzero coefficient vectors are pairwise Hermitian-orthogonal. Then every positive radius is flat, and there are at most r nonzero coefficients;

(b) the number of distinct positive flat radii is at most r-1.

In particular, flatness at r distinct positive radii forces pairwise orthogonality, regardless of the degree n. The same statement holds for a vector Laurent polynomial after multiplication by a monomial.

## 2. Sparse positive zeros

A nonzero real polynomial with k nonzero monomials has at most k-1 distinct positive zeros. An elementary induction proves this: divide by the lowest monomial, differentiate, and use Rolle's theorem between consecutive positive zeros. The derivative has at most k-1 nonzero monomials. The statement also holds for complex coefficients: take a real part after a scalar phase rotation which leaves at least one coefficient nonzero. Every positive zero of the complex polynomial remains a zero of that real polynomial.

No unproved extension of Rolle's theorem to complex-valued functions is used here.

## 3. Proof of Theorem 1

Suppose the coefficients are not pairwise orthogonal. Let L>=1 be the largest separation for which some inner product <v_j,v_(j+L)> is nonzero. The angular Fourier coefficient at frequency L of ||P(rho exp(i theta))||^2 is rho^L B(rho^2), where

    B(x)=sum_(j=0)^(n-L) <v_j,v_(j+L)> x^j.

Let j_1<...<j_k be the indices of its nonzero coefficients. Consider the k by k matrix

    M_(a,b)=<v_(j_a),v_(j_b+L)>.

If b>a, then j_b+L-j_a>L, so maximality of L makes this entry zero. Every diagonal entry is nonzero. Thus M is triangular and invertible, of rank k. On the other hand it factors through the coefficient span of dimension r, hence k<=r.

Every positive flat radius gives a distinct positive zero of the nonzero k-term polynomial B. Section 2 bounds their number by k-1<=r-1. If there is no such positive separation L, all distinct coefficient vectors are orthogonal and the norm is radial for every radius. This proves the dichotomy.

The argument uses the furthest nonzero off-diagonal of the coefficient Gram matrix. Its nonzero positions form an invertible triangular cross-Gram matrix. The rank estimate is why the final bound depends on the target rank rather than the polynomial degree.

## 4. Sharpness at any prescribed radii

Let d>=2 and choose any distinct positive rho_1,...,rho_(d-1). Write

    B(x)=product_(s=1)^(d-1)(x-rho_s^2)=sum_(j=0)^(d-1) a_j x^j.

All a_j are nonzero. Define a C^d-valued polynomial by its components:

    P_j(z)=sqrt(|a_j|) z^j [1+sign(a_j)z], 0<=j<d.         (1)

Its coefficient span has rank d: its first d coefficient columns contain a triangular d by d matrix with nonzero diagonal. Directly,

    ||P(rho exp(i theta))||^2
      =(1+rho^2)sum_j |a_j|rho^(2j)
         +2rho cos(theta)B(rho^2).                         (2)

It follows that the positive flat radii are exactly the prescribed d-1 radii. The coefficient vectors are not pairwise orthogonal. Therefore the rank-minus-one bound cannot be improved.

For d=3 and radii 1,2 an explicit example is

    P(z)=(2(1+z), sqrt(5)z(1-z), z^2(1+z)).

Its squared norm is radial on those two circles and on no other positive circle.

## 5. The two-quadrature consequence

For a scalar complex polynomial p=A+iB with coefficientwise real A,B, apply Theorem 1 to the two-component vector polynomial (A,B). If

    |A(rho exp(i theta))|^2+|B(rho exp(i theta))|^2

is constant at two distinct positive radii, p has at most two nonzero coefficients, and the real scalar product of any two is zero:

    Re(c_j conjugate(c_k))=0.

This proves the single-orbit flat-tail classification in two_radius_quadrature_rigidity.md by a shorter rank argument. In the dynamical application the two radii are lambda and lambda^(-1), not two chosen quantum energies. The exact diagonal covariance formula in that note is an additional consequence of the hyperbolic orbit geometry, not a consequence of radial flatness alone.

## 6. Interpretation and limits

For a d-output finite polynomial filter, testing radial gain-flatness at d distinct positive gains certifies complete orthogonality of its time-coefficient vectors. At d-1 gains this is false, even when those gains are prescribed in advance; (1) is an explicit obstruction.

This is a rigidity and construction theorem. It does not imply Gaussianity, statistical independence, random-matrix eigenvalue laws, or a new proof of BGS. Possible overlap with prior work on polynomial sphere maps and paraunitary filters must be assessed before asserting novelty or priority.
