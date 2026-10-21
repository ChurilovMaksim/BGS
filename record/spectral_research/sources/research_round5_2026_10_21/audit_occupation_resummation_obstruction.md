> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round5_2026_10_21/audit_occupation_resummation_obstruction.md`. Embedded SHA256: `680841fae8341687da7949090b2c2daf3db84ce89ec7885a1120c7af79e1eee6`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Independent audit: exact occupation resummation

21 October 2026. Auditor: /root/audit_uniform_word_r4.

## Reviewed source and verdict

Reviewed the complete frozen source:

- arithmetic_occupation_resummation_obstruction.md
- SHA256: 1aeefa2931e83e4368ecdc4b5b0aa3b31c81beef8eb6fbb69ea825e08e5b0556

**Verdict:** the finite identities, original-family entry nonvanishing statement, nonconstant row-phase coefficient, and stated limited consequences are proved. No substantive gap was found. In particular the source does not prove the original pair limit, any higher-order instance of $H_{\rm diag}$, or a countersequence.

The proof below was reconstructed directly. Another agent's assessment or numerical checks were not used as proof. The reviewed source remains unchanged.

The original-family exponential lower bound is an explicitly identified input, not reproved in this audit:

- root_exponential_coherent_edge_classes.md, SHA256 001fd27ca128f1a00417838e0f4b07d7ad19f291e8c2c5fbb593e614d2ec29e0;
- its earlier independent audit, audit_exponential_coherent_edge_classes.md, SHA256 effadaa4e2b66189a077f65cc6a50019781024d020c0ffd46d2197511b21dbbf.

Both hashes were rechecked. The present source makes no stronger assumptions about this input.

## 1. Formal coefficient and root multiplicity

All words are actual ordered lists $x_0,\ldots,x_{n-1}$, with the last edge returning to $x_0$. For $Z=\operatorname{diag}(z_v)$,
$$
 \operatorname{Tr}(ZU)^n
 =\sum_{x_0,\ldots,x_{n-1}}
    \left(\prod_{j=0}^{n-1}U_{x_jx_{j+1}}\right)
    \prod_{j=0}^{n-1}z_{x_j}
 =\sum_{|d|=n}A_{n,d}(U)z^d.
$$
This equality already includes all periods and repeated letters with their correct multiplicities. In particular, a constant word contributes once, not $n$ times.

The formal determinant has constant term one. Differentiating its formal logarithm, using the adjugate identity and then the formal geometric series, gives
$$
 -\partial_t\log\det(I-tZU)
 =\operatorname{Tr}\bigl((I-tZU)^{-1}ZU\bigr)
 =\sum_{m\ge1}t^{m-1}\operatorname{Tr}(ZU)^m.
$$
Formal integration in characteristic zero, with zero integration constant, yields
$$
 -\log\det(I-tZU)=\sum_{m\ge1}\frac{t^m}{m}
    \operatorname{Tr}(ZU)^m.
$$
Homogeneity identifies the coefficient of $t^nz^d$, for $|d|=n$, as $A_{n,d}/n$. Thus the factor $n$ in source (2.1) is correct. There is no orbit quotient, missing period divisor, convergence issue, or interchange of infinite numerical sums.

Choosing identity rows outside $S$ in the row-multilinear determinant expansion forces the same columns outside $S$. Deleting identical row and column index sets gives no additional cofactor sign. This proves
$$
 \det(I-ZU)=\sum_S(-1)^{|S|}\det(U_{S,S})\prod_{v\in S}z_v.
$$
The argument requires neither nonzero principal minors nor a unitary matrix.

## 2. Occupation projection and localization of compensation

The equal-occupation set is invariant under exchanging $x,y$; its complete sum is
$$
 \mathcal O_n(U)=\sum_{|d|=n}|A_{n,d}(U)|^2.
$$
For $D_\theta=\operatorname{diag}(e^{i\theta_v})$, departures from each vertex supply exactly its occupation character:
$$
 \operatorname{Tr}(D_\theta U)^n
 =\sum_{|d|=n}A_{n,d}(U)e^{id\cdot\theta}.
$$
Normalized torus integration annihilates every $d-e\ne0$. Therefore
$$
 \mathcal O_n(U)=\int_{\mathbb T^N}
       |\operatorname{Tr}(D_\theta U)^n|^2\,d\theta.
$$
For unitary $U$, each matrix inside the integrand is unitary and its trace power has modulus at most $N$. Consequently $0\le\mathcal O_n\le N^2$. This is a bound on an exactly specified subset of the original finite double sum. It does not replace the prescribed matrix or its form factor by a phase ensemble.

Equality of directed edge arrays implies equality of both their row sums and occupation vectors. Thus, writing $\mathcal R_n^{\rm occ}$ for the source's same-occupation, different-edge sum,
$$
 \mathcal O_n=\mathcal F_n+\mathcal R_n^{\rm occ},\qquad
 -\mathcal F_n\le\mathcal R_n^{\rm occ}\le N^2-\mathcal F_n.
$$
These are exact inequalities. The cited original-family lower bound for $\mathcal F_n$, uniformly for $c\le n/N\le B$, therefore forces an exponentially large negative sum within those same occupation sectors, with
$$
 \mathcal R_n^{\rm occ}=-\mathcal F_n+\mathcal O_n,\qquad
 0\le\mathcal O_n\le N^2.
$$
The location of the compensation is established, but its residual uncertainty is still $N^2$. It is not a computation at the desired form-factor scale $N$.

The distinct-occupation sum satisfies
$$
 \Omega_n=|\operatorname{Tr}U^n|^2-\mathcal O_n.
$$
It is real; for a unitary matrix the two terms on the right lie in $[0,N^2]$. None of this determines their difference, its sign, or the needed weighted asymptotic.

## 3. Row-phase invariants and the exact remaining data

Entrywise calculation gives
$$
 P(D_\theta U)=P(U),\qquad
 Q(D_\theta U)=D_\theta Q(U)D_\theta^*,
$$
because the latter entry acquires $e^{i(\theta_x-\theta_y)}$. Every individual equal-occupation pair also remains invariant. The full form factor has Fourier expansion
$$
 |\operatorname{Tr}(D_\theta U)^n|^2
 =\sum_{|d|=|e|=n} A_{n,d}\overline{A_{n,e}}\,
    e^{i(d-e)\cdot\theta}.
$$
Its constant coefficient is $\mathcal O_n$, whereas its value at $\theta=0$ includes the sum of all nonconstant coefficients. Therefore the displayed invariants do not recover the full row-phase polynomial. This is a precise obstruction to a universal exact deletion of all unequal-occupation modes. It does not exclude an argument using additional information about the prescribed original phase.

## 4. Independent check of Lindemann--Weierstrass hypotheses

The primary source was independently opened during this audit: Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials of Algebraic Numbers*, Proceedings of ISSAC 2022, Theorem 1.1, page 1.

- Published DOI: https://doi.org/10.1145/3476446.3536170
- Checked author version: https://arxiv.org/pdf/2112.05004v2
- Version date: 16 May 2022; checked on 21 October 2026.

The stated theorem excludes zero for a finite linear combination of exponentials whose exponents are distinct algebraic numbers and whose coefficients are nonzero algebraic numbers. A zero exponent is allowed. Only this qualitative statement is used; no unverified quantitative transcendence estimate is invoked.

For the prescribed family:

1. All entries of $A_N,M_N$ are algebraic. Modular inverses occur only in roots of unity, $N^{-1/2}$ is algebraic, and the trigonometric Fourier coefficients are algebraic because $e^{i\alpha_0}=(-3+4i)/5$.
2. The eigenvalues of the algebraic matrix $A_N$ are algebraic. Hermiticity makes it diagonalizable. For its set $\Lambda$ of distinct eigenvalues, the polynomial spectral projector formula has nonzero algebraic denominators and gives algebraic matrices $P_\lambda$. Multiplicities cause no difficulty.
3. In
   $$
   U_N(\tau)_{uv}=\sum_{\lambda\in\Lambda}
       (P_\lambda M_N)_{uv}\exp(iN\lambda\tau),
   $$
   the coefficients sum to $(M_N)_{uv}\ne0$. Hence at least one coefficient survives after zero coefficients are discarded.
4. The remaining coefficients are nonzero algebraic numbers, and the exponents $iN\lambda\tau$ are distinct algebraic numbers because $N\ne0$ and $\tau=10^{-80}$ is nonzero rational.

All hypotheses of Theorem 1.1 hold for each entry and every odd $N\ge3$, including $N=7$ and arbitrary odd composites. The conclusion $U_{N,uv}\ne0$ follows. No simplicity of the spectrum of $A_N$, eigenvector normalization over algebraic numbers, or nonzero individual projector entry is assumed.

## 5. A nonzero mode does not evaluate the original phase

For $u\ne v$, a difference of occupation vectors of total size $n$ can equal $n(e_u-e_v)$ only for $d=ne_u,e=ne_v$. The coordinate difference $n$, together with nonnegativity and the total-size constraint, forces this uniqueness. Each corresponding occupation sector contains precisely one constant rooted word. Thus
$$
 [e^{in(\theta_u-\theta_v)}]\,
 |\operatorname{Tr}(D_\theta U_N)^n|^2
 =U_{N,uu}^{\,n}\overline{U_{N,vv}^{\,n}}\ne0.
$$
There is no extra factor $n$, no sum of coefficients at this mode, and no possible cancellation within this particular coefficient.

This proves existence of nonzero nonconstant Fourier modes, not nonvanishing of every conceivable Fourier mode. It does not imply $\Omega_n(U_N)\ne0$ at $\theta=0$: different nonconstant modes may cancel at that point. It supplies no useful lower bound for the original spectral discrepancy. In the already established range $\max|U_{uv}|^2\le9/N$, the displayed coefficient has modulus at most $(9/N)^n$, consistent with a very small coefficient at $n\asymp N$.

## 6. Pair normalization and unresolved estimate

For real $b$, the factors at opposite Fourier indices are $|\widehat b(n/N)|^2$. The $n=0$ terms agree with CUE, and the factor two from $n$ and $-n$ cancels $1/2!$. The identity $D(n,-n)=|p_n|^2-N$ therefore gives source (6.1) with normalization $N^{-2}$.

The CUE circular projection kernel gives its second trace moment as $N-(N-n)_+=\min(n,N)$ for $n>0$: the diagonal contributes $N$, and the squared-kernel Fourier coefficient counts the $N-n$ pairs of projection indices when $n<N$. This also confirms the benchmark directly.

The exact first unproved estimate of this note remains
$$
 \frac1{N^2}\sum_{n\ge1}|\widehat b(n/N)|^2
 \bigl(\mathcal O_n(U_N)-\min(n,N)+\Omega_n(U_N)\bigr)
 \longrightarrow0
$$
for each admissible $b$, through all odd dimensions. Compact support of $\widehat b$ makes each sum finite. The proved occupation identities do not estimate this signed sum. Even its proof would leave all higher orders in $H_{\rm diag}$ to establish.

### Wording qualifications for incorporation

The source's sentence that individual terms in (3.1) can have either sign should be read as a statement about their real contributions: individual unsymmetrized terms can be complex. Their aggregate is real, and (3.1) proves nonnegativity. No argument relies on a termwise sign.

In a report that already uses $R_n$ for reversed paths, use a distinct notation such as $\mathcal R_n^{\rm occ}$ for the source's same-occupation, different-edge sum. These are different indexing sets.

The frozen source has not been edited. These qualifications do not alter any proved identity or bound.
