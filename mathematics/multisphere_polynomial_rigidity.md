# Rank-controlled rigidity on concentric complex spheres

Status: self-contained project proof, derived from the multiradius rank lemma. Priority relative to the literature on polynomial sphere maps has not been established. No BGS conclusion is asserted.

## The theorem

Let P:C^m -> C^d be a nonzero holomorphic polynomial map, written

    P(z)=sum_alpha v_alpha z^alpha,
    r=dim_C span{v_alpha}.

Suppose there are r distinct positive radii rho_s such that ||P(z)|| is constant on each sphere ||z||=rho_s. The constants may differ from sphere to sphere.

**Theorem.** Then ||P(z)|| is radial on every sphere. More precisely, there are nonnegative constants c_k such that

    ||P(z)||^2=sum_k c_k ||z||^(2k),                        (1)

and its coefficient vectors satisfy

    <v_alpha,v_beta>=0 for alpha!=beta,
    ||v_alpha||^2=c_(|alpha|) * (|alpha|! / product_j alpha_j!). (2)

After a unitary change of target coordinates, P is an orthogonal direct sum of scaled homogeneous Veronese maps, possibly including a constant component. In particular,

    r=sum_(k:c_k>0) binomial(m+k-1,k).                      (3)

Thus a nonradial squared norm can be constant on at most r-1 distinct positive concentric spheres. The bound is independent of the polynomial degree and is sharp in general, already for domain dimension one.

## Proof

Write P=sum_k P_k in homogeneous degrees. Fix a unit vector u in C^m and restrict to the complex line z=w u. The resulting vector polynomial sum_k P_k(u) w^k has coefficient span of dimension at most r. On each of the r specified circles its norm is independent of the argument of w. The one-variable rank theorem in multiradius_polynomial_rigidity.md therefore gives

    <P_k(u),P_l(u)>=0 for k!=l.                            (4)

Positive real scaling extends (4) to every z in C^m. Expansion in the independent monomials z^alpha conjugate(z)^beta shows that the coefficient ranges of different homogeneous pieces are orthogonal.

Let S be the set of degrees for which P_k is not identically zero. There is a unit vector u at which every P_k with k in S is nonzero: a finite union of proper polynomial zero sets cannot cover the sphere. At this u, (4) gives |S|<=r.

On the unit sphere put a_k(u)=||P_k(u)||^2. For each prescribed radius,

    sum_(k in S) rho_s^(2k) a_k(u)=C_s,

where C_s is independent of u. The matrix with entries rho_s^(2k) has full column rank. Indeed a nonzero linear dependence would be a polynomial with at most |S| nonzero monomials vanishing at the r distinct positive numbers rho_s^2, contradicting the sparse-positive-zero lemma. Therefore every a_k(u) is a constant c_k.

Homogeneity yields

    ||P_k(z)||^2=c_k (sum_j |z_j|^2)^k.

Compare coefficients after the multinomial expansion. Every off-diagonal coefficient inner product inside a fixed degree vanishes, and each diagonal coefficient has exactly the norm in (2). Together with the cross-degree orthogonality this proves (1)--(2). When c_k>0 every degree-k monomial has a nonzero orthogonal coefficient vector, giving (3). A target-unitary change of basis gives the stated Veronese description.

## Why rank rather than degree appears

In one variable, choose the largest lag L with a nonzero coefficient inner product. If its angular coefficient has k nonzero monomials, those k inner products lie on the diagonal of an invertible triangular cross-Gram matrix. Hence k<=r. A k-term polynomial has at most k-1 distinct positive zeros. That argument is independent of the maximal exponent, and is the only rigidity input used above.

## Boundary of the statement

The spheres are concentric in the domain, and the target norm is taken about one fixed origin. The theorem is not asserted for arbitrary moving target centers, rational maps with poles, infinite power series, or indefinite target forms. Sharpness in domain dimension one does not establish optimal target-dimension bounds for each fixed higher domain dimension.

The homogeneous Veronese classification is a mathematical rigidity statement. It does not turn covariance flatness into probability independence or into quantum spectral universality.
