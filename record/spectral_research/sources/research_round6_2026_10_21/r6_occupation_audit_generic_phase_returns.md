> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/r6_occupation_audit_generic_phase_returns.md`. Embedded SHA256: `618bda8ed21be5e1fc2db73a401db5133d4659eab4b6c33b4313fb57e8ccfdca`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: principal minors and generic auxiliary return energy

21 October 2026. Auditor: occupation/cross-phase branch.

## 1. Frozen source, verdict, and exact scope

The source read and reconstructed in full is:

- research_round6_2026_10_21/r6_dense_principal_minors_generic_phase_returns.md
- SHA256: 2f5d4896e461fe33cf6f8ed25c71d994a4d2842206f48f5fba7bf75189f9d0f8

The hash was verified against the author's frozen source.

**Verdict:** the source's arithmetic, algebraic, generic spectral, and first-return conclusions are justified. I found no mathematical defect requiring amendment. The potentially delicate Laurent-localization/Gauss step is made fully explicit in Section 5 below.

There are two different scopes, which must remain separate:

1. Every specified initial principal minor and every matrix entry is nonzero for the actual original $U_N$, for each odd $N$.
2. Simplicity, full eigenvector support, invertibility of the eigenangle Jacobian, distinct nontrivial eigenvalue ratios, and absence of a dark subspace are proved for almost every auxiliary phase vector $z$, for each fixed odd $N$.

The specified vector $z=(1,\ldots,1)$ may belong to the exceptional null set. Neither the source nor this audit excludes that possibility.

I also read the corresponding new §8.1 of round6_main_report.md, including (8.8)--(8.9), and checked its formulas and scope against the frozen source. The report correctly distinguishes the original-minor theorem from the auxiliary almost-everywhere theorem.

## 2. Published arithmetic input and its hypotheses

I independently opened the author version of:

Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022, Theorem 1.1, DOI https://doi.org/10.1145/3476446.3536170; author PDF https://arxiv.org/pdf/2112.05004, page 1.

The theorem there states the needed Lindemann--Weierstrass conclusion for distinct algebraic exponents and nonzero algebraic coefficients. The publication metadata and theorem number agree with the source note. Only this qualitative conclusion is used.

Every entry of $A_N$ and $M_N$ is algebraic: their ingredients are algebraic Fourier coefficients, roots of unity, and the algebraic factor $N^{-1/2}$. The prescribed phase $e^{i\alpha_0}=(-3+4i)/5$ is algebraic; the angle $\alpha_0$ itself need not be algebraic. A Hermitian algebraic matrix has algebraic eigenvalues, and its projectors onto distinct spectral values are algebraic by the polynomial projector formula displayed in the source.

Thus for algebraic vectors $v,w$ and Hermitian algebraic $H$,
$$
 \langle v,e^{iN\tau H}w\rangle
 =\sum_\mu c_\mu e^{iN\tau\mu}
$$
has algebraic coefficients $c_\mu$. If its value at zero parameter is nonzero, their sum is nonzero, so they are not all zero. After discarding zero coefficients, the exponents are distinct algebraic numbers because $\tau=10^{-80}$ is nonzero and algebraic. The published theorem applies exactly.

The rescaled time $\tau/(2\pi)$ is not used as an algebraic exponent parameter. The source correctly retains $\tau$ in this argument.

## 3. The original principal minors and exterior powers

The given modular-half kernel has the exact factorization
$$
 M_N(x,y)=N^{-1/2}\eta_x
       \bigl(e_N(4^{-1}y)\bigr)^x\eta_y,
 \qquad \eta_x=e_N(-3\,8^{-1}x^2).
$$
For the initial index set $S_k=\{0,\ldots,k-1\}$, the remaining middle matrix is an ordinary Vandermonde matrix. Its bases are distinct because $4^{-1}$ is a unit modulo every odd $N$. Therefore
$$
 \det M_N[S_k,S_k]
 =N^{-k/2}\prod_{x<k}\eta_x^2
     \prod_{0\le a<b<k}
       \left(e_N(4^{-1}b)-e_N(4^{-1}a)\right)\ne0.
$$
This includes composite dimensions and $k=N$.

The additive exterior generator $A_N^{[k]}$ is Hermitian and algebraic on the standard wedge space. Tensor differentiation, restricted to the alternating subspace, proves
$$
 \bigwedge^k e^{iN\tau A_N}
 =e^{iN\tau A_N^{[k]}}.
$$
The relevant wedge matrix entry of
$$
 e^{iN\tau A_N^{[k]}}\bigwedge^k M_N
$$
is exactly $\det U_N[S_k,S_k]$.

If sums of eigenvalues coincide, they are grouped into a single spectral value of $A_N^{[k]}$. The polynomial projector construction remains valid for these grouped distinct values. The value at zero parameter is the nonzero Vandermonde minor above, so the arithmetic argument in Section 2 proves the desired original minor is nonzero.

The same calculation with $k=1$, but arbitrary input and output coordinates, has nonzero zero-parameter value $M_N(x,y)$. It proves every original entry $U_N(x,y)$ is nonzero.

The theorem concerns a complete chain of initial principal minors. It does not claim that every possible principal minor of $M_N$ or $U_N$ is nonzero.

## 4. Leading coefficient of the logarithmic Jacobian

Write
$$
 p(\lambda,z)=\det(\lambda I-ZU)
 =\lambda^N+\sum_{k=1}^N c_k(z)\lambda^{N-k}.
$$
The principal-minor expansion gives
$$
 c_k(z)=(-1)^k\sum_{|S|=k}\det U[S,S]\,z_S.
$$
Under lexicographic order $z_0>\cdots>z_{N-1}$, the leading term is
$$
 L_k=(-1)^k\Delta_k(U)z_0\cdots z_{k-1}.
$$

In the matrix with entries $z_a\partial_{z_a}c_k$, the monomial of $L_k$ occurs precisely when $a<k$, with its unchanged coefficient. All other terms are strictly smaller. For any selection of a smaller term in at least one row, multiplicativity of the monomial order makes the product strictly smaller than the product of all $L_k$; it cannot contribute to the target coefficient.

The coefficient matrix of the leading row terms is lower triangular, with diagonal entries one after factoring the coefficients of the $L_k$. Hence
$$
 [z_0^Nz_1^{N-1}\cdots z_{N-1}]\,
 \det[z_a\partial_{z_a}c_k]
 =(-1)^{N(N+1)/2}\prod_{k=1}^N\Delta_k(U)\ne0.
$$
This checks the sign, exponents, and absence of cancellation.

In the main report, the coefficient functions are instead the unsigned elementary symmetric functions $\sigma_k=(-1)^kc_k$. Its corresponding leading coefficient therefore has no overall sign. This difference between the source and report is intentional and correct.

The nonzero logarithmic Jacobian is a genuine polynomial nonvanishing statement. It does not assert that this Jacobian is nonzero at every point of the unit torus.

## 5. Irreducibility, Laurent localization, and resultants

For an invertible $U$ with $U_{ab}U_{ba}\ne0$ whenever $a\ne b$, consider
$$
 D(w)=\det(\operatorname{diag}(w)-U).
$$

### 5.1. The mixed-minor obstruction to factorization

The degree of $D$ in each variable is one. In a factorization $D=FG$, degrees in each variable add, so each variable can occur in only one factor. Its leading full monomial is $\prod_a w_a$, so every variable occurs and any nontrivial factorization induces a nonempty partition of the variables between $F$ and $G$.

Normalize both full-monomial coefficients to one. For an index $a$ in the first part and $b$ in the second, the coefficients missing $a$ and $b$ from the full monomial are $-U_{aa}$ and $-U_{bb}$. Since the factors use disjoint variables, their product forces the coefficient missing both to be $U_{aa}U_{bb}$.

The determinant expansion gives instead
$$
 U_{aa}U_{bb}-U_{ab}U_{ba}.
$$
These differ by a nonzero quantity. Thus no nontrivial partition factorization exists, and $D$ is irreducible over $\mathbb C$.

This argument does not require its diagonal entries to be nonzero. The actual original matrix satisfies the stronger all-entry nonvanishing already proved.

### 5.2. The localization step in explicit rings

Let
$$
 R=\mathbb C[z_0^{\pm1},\ldots,z_{N-1}^{\pm1}],
 \qquad K=\mathbb C(z_0,\ldots,z_{N-1}).
$$
The nonzero constant coefficient $(-1)^N\det U$ shows that $D$ is not a coordinate factor. As an irreducible polynomial in a unique factorization domain it is prime; localizing in its variables preserves this prime because none of the inverted coordinate monomials is divisible by $D$.

Adjoining and inverting an independent variable $\lambda$ likewise preserves the prime. The map
$$
 w_a=\lambda/z_a,\qquad \lambda=\lambda
$$
is an automorphism of the Laurent ring in $N+1$ variables; its inverse is $z_a=\lambda/w_a$. Therefore
$$
 p(\lambda,z)=\left(\prod_a z_a\right)D(\lambda/z)
$$
is irreducible in $R[\lambda,\lambda^{-1}]$, since the displayed prefactor is a unit there.

Now view $p$ as an element of $R[\lambda]$. Any factor that becomes a unit after inverting $\lambda$ must be an $R$-unit times a power of $\lambda$. A positive such power cannot divide $p$, because its $\lambda$-constant coefficient
$$
 (-1)^N\det U\prod_a z_a
$$
is a unit of $R$. A zero power gives an already invertible factor of $R[\lambda]$. Hence $p$ is irreducible in $R[\lambda]$.

Finally $p$ is monic in $\lambda$, so it is primitive over the unique factorization domain $R$. Gauss's lemma proves irreducibility in $K[\lambda]$. No factor can disappear in the passage to the coefficient field. This supplies the ring details implicit in the frozen source's brief localization argument.

### 5.3. Simplicity and full coordinate support

In characteristic zero, the irreducible degree-$N$ polynomial $p$ is relatively prime to $\partial_\lambda p$, which is nonzero and has smaller degree. It is also relatively prime to each deleted-principal characteristic polynomial $p_a$, which is monic of degree $N-1$.

Thus all corresponding Sylvester resultants are nonzero elements of $R$, in fact they arise from polynomial coefficients. A nonzero Laurent polynomial has a null zero set on the unit torus: after clearing monomial factors, induct on the variables, fix all but the last variable outside the null common-zero set of its coefficient polynomials, and use the finite number of zeros of a nonzero one-variable polynomial. Fubini completes the argument. One nonzero coefficient polynomial suffices to bound the exceptional coefficient set at the induction step.

It follows that outside a null set of phases the spectrum of $ZU$ is simple and is disjoint from that of every deleted principal matrix.

For unit phases, $ZU$ is normal. At a simple eigenvalue $\lambda_j$, spectral resolution of the resolvent gives
$$
 \operatorname{adj}(\lambda_j I-ZU)
 =p'(\lambda_j,z)\,v_jv_j^*.
$$
Its $aa$ entry is the deleted principal polynomial $p_a(\lambda_j,z)$, with positive cofactor sign. Therefore
$$
 p_a(\lambda_j,z)=p'(\lambda_j,z)|v_j(a)|^2.
$$
Both factors on the left and $p'$ are nonzero on the selected full-measure set, so every eigenvector coordinate is nonzero.

## 6. Angle Jacobian and generic distinct ratios

At a point with simple spectrum, choose smooth local eigenvalue and normalized eigenvector branches. With input and output angles in radians,
$$
 z_a=e^{i\phi_a},\qquad \lambda_j=e^{i\theta_j},
$$
differentiation of the normal eigenvalue equation gives
$$
 \partial_{\phi_a}\lambda_j
 =v_j^*(iE_{aa}ZU)v_j
 =i\lambda_j|v_j(a)|^2,
 \qquad
 \partial_{\phi_a}\theta_j=|v_j(a)|^2.
$$
The factors of $i$ cancel, and there is no $2\pi$ factor under this radian convention.

The map from distinct roots to characteristic coefficients has invertible Jacobian. To see this directly, differentiate the characteristic polynomial with respect to each root. The resulting polynomials
$$
 -\prod_{\ell\ne j}(\lambda-\lambda_\ell)
$$
are linearly independent: evaluation at $\lambda_j$ isolates the corresponding coefficient.

The chain rule then factors the coefficient Jacobian with respect to the input angles into this invertible root-coefficient matrix, the invertible diagonal matrix of $i\lambda_j$, and the real matrix
$$
 B_{ja}=|v_j(a)|^2.
$$
On the other hand the coefficient-input Jacobian equals $i$ times each column of the logarithmic coefficient Jacobian. Since the latter polynomial is nonzero outside a torus null set, $\det B\ne0$ almost everywhere.

The real inverse function theorem gives local diffeomorphisms of angle coordinates on this full-measure open set. A countable cover by inverse charts is available. Such diffeomorphisms preserve null sets locally; equivalently, apply the ordinary change-of-variables theorem on smaller patches. Thus the resulting eigenangle law is absolutely continuous in local coordinates. No quantitative density or inverse-Jacobian bound is implied.

For two distinct ordered pairs with unequal indices within each pair, equality of eigenvalue ratios is
$$
 \theta_j-\theta_k-\theta_\ell+\theta_m\in2\pi\mathbb Z.
$$
The linear form is nonzero unless the ordered pairs coincide. This includes reversed pairs: their coincidence would impose a nontrivial doubled-gap condition, which is also a hyperplane condition.

The countable collection of these hyperplanes has zero measure in angle space. Pulling back through the countable inverse-chart cover and taking the finite union over index pairs proves that nontrivial ordered eigenvalue ratios are distinct almost everywhere. Simplicity already excludes any nontrivial ratio from equalling one.

## 7. The eigenvalue-one sector of the doubled transfer

Let $V=ZU_N$ at one of the good phase vectors, and $W=V\otimes\overline V$. Under the matrix-unit identification, its eigenvectors are
$$
 |v_j\rangle\langle v_k|,
 \qquad\text{with eigenvalue }\lambda_j\overline{\lambda_k}.
$$

For $j\ne k$, each such eigenvalue is simple by the distinct-ratio result. Its diagonal projection has entries
$$
 v_j(a)\overline{v_k(a)},
$$
which are all nonzero by full support. Thus its one-dimensional eigenspace has no nonzero vector in the off-diagonal-pair space $O$.

The eigenvalue one is different: its eigenspace has dimension $N$, not one. Simplicity of $V$ makes it exactly
$$
 \operatorname{span}\{|v_j\rangle\langle v_j|:1\le j\le N\}.
$$
On this space, diagonal projection maps coefficients $t_j$ to
$$
 \left(\sum_jt_j|v_j(a)|^2\right)_a.
$$
Its matrix is the transpose of the invertible angle Jacobian $B$. The projection is therefore injective, including for complex coefficients $t_j$, so this eigenspace also has trivial intersection with $O$.

Finally the dark reducing subspace for $S=OWO$ is reducing for $W$. Indeed
$$
 B_{\rm block}^*B_{\rm block}+S^*S=I_O,\qquad
 C_{\rm block}C_{\rm block}^*+SS^*=I_O.
$$
On any unitary reducing subspace of $S$, both off-diagonal couplings vanish. Hence $W$ and $W^*$ preserve that subspace. Any nonzero reducing subspace of a finite unitary contains an eigenvector. The preceding checks exclude every possible eigenvalue, including the full eigenvalue-one eigenspace. Consequently the dark subspace is zero almost everywhere.

## 8. Return energy, averaging, and compatibility with long transients

The independently checked finite-dimensional first-return identities are
$$
 \sum_{r\ge1}\|F_r\|_{\rm HS}^2=N,
 \qquad
 \sum_{r\ge1}r\|F_r\|_{\rm HS}^2
 =N^2-\dim\mathcal H_{\rm dark}.
$$
For clarity, their weighted scalar identity can be recovered directly from
$$
 g_m=\|S^mC_{\rm block}\|_{\rm HS}^2
 =\|S^m\|_{\rm HS}^2-\|S^{m+1}\|_{\rm HS}^2.
$$
The first-return energy at $r=m+2$ is $g_m-g_{m+1}$, and the energy tail from that return onwards is $g_m$. Summing the tails gives
$$
 \sum_r r\|F_r\|_{\rm HS}^2
 =N+\sum_{m\ge0}g_m
 =N+\dim O-\dim\mathcal H_{\rm dark}.
$$
A finite contraction splits into its unitary reducing part and a part with spectral radius strictly below one, which justifies the final limit. Since $\dim O=N^2-N$, this is the claimed formula.

At the generic phases just proved to have no dark part, the weighted energy is exactly $N^2$. For every phase it is between zero and $N^2$. Tonelli therefore gives
$$
 \sum_{r\ge1}r\,\mathbb E_z\|F_r(z)\|_{\rm HS}^2=N^2.
$$
Likewise the unweighted energy is always $N$, so
$$
 \nu_N(r)=N^{-1}\mathbb E_z\|F_r(z)\|_{\rm HS}^2
$$
is a probability measure with mean $N$. Its stated tail bound $1/B$ at $r\ge BN$ is the ordinary Markov inequality.

There is no conflict with $\|S^m\|=1$ for $m<N$: the latter is an exact finite-time isometric-subspace property, while almost-everywhere absence of a dark part implies eventual decay only for each fixed finite $N$. No uniform decay rate in $N$ is established.

## 9. Check against the main report

The new main-report subsection correctly states:

- original all-odd nonvanishing of the initial principal minors;
- the grouping of coincident exterior eigenvalue sums before applying Lindemann--Weierstrass;
- the unsigned coefficient-Jacobian convention, hence no missing sign there;
- the use of radians in the angle Jacobian;
- separate treatment of eigenvector support and nontrivial phase differences;
- injectivity of the diagonal projection on the entire eigenvalue-one eigenspace;
- the almost-everywhere restriction on the no-dark and $N^2$-energy conclusions.

Its brief implication from a nonzero coefficient Jacobian to generic simple spectrum is also valid independently: a nonzero complex Jacobian makes the coefficient map locally open at some complex point, so the nonzero discriminant polynomial cannot vanish identically after composition. Alternatively the immediately following irreducibility/resultant argument supplies generic simplicity exactly as in the frozen source.

No change to the main report's mathematical claims is required. The original point $z=1$, the large-$N$ signed trace estimate, and $H_{\rm diag}$ remain unresolved by this addition.

