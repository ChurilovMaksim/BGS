> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_stationary_dephasing.md`. Embedded SHA256: `e250e40e254ac47fecb0fa8252e4f87123781dfa2bd75ad961d8918035fa51f5`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: uniform stationary dephasing for the original family

21 October 2026. Auditor: r7_physical_audit.

## 1. Verdict and scope

**Verdict: Theorems 1 and 2 are proved for the exact original family along all odd dimensions. No mathematical gap was found.** The signed return identities in §7 are also correctly derived from their explicitly stated additional finite-dimensional input.

The audited raw source is r7_return_uniform_stationary_dephasing.md, SHA-256
c2bf50a33a642b984afa7bfa83fdc0d28b8019c79d4f47121ab52adee5e53075.
I reconstructed the argument independently. I did not use the author's verdict, the parent's verdict, another auditor's verdict, or an author checker as evidence.

Let $\mathcal E_N$ be the orthogonal projection onto the entire commutant of $U_N$, let $\Pi_N$ project onto coordinate diagonal matrices in unnormalized Hilbert--Schmidt space, and identify that range with ordinary $\mathbb C^N$. With $J_N$ the normalized constant projection, the main result is
$$
 0\le Q_N=\Pi_N\mathcal E_N\Pi_N-J_N,
 \qquad q_N=\|Q_N\|_{\rm op}\longrightarrow0.
$$
It includes arbitrary $N$-dependent diagonal observables and arbitrary choices of eigenbasis within degenerate eigenspaces:
$$
 0\le B_NB_N^*-J_N\le Q_N.
$$
The source also proves that a subspace of dimension $d_N-1\ge N-1$, where $d_N=\dim\ker(\operatorname{Ad}U_N-I)$, consists of off-diagonal approximate stationary vectors with residual bound
$$
 \|(I-S_N)Y\|_{\rm HS}
 \le\sqrt{\frac{q_N}{1-q_N}}\,\|Y\|_{\rm HS}.
$$
These two conclusions have no restriction $7\nmid N$.

The additional signed identities
$$
 \sum_{r\ge1}F_{r,N}=I_N,\qquad
 \sum_{r\ge1}rF_{r,N}=(B_NB_N^*)^{-1}
$$
use the separately stated simple-spectrum and nonsingular-intensity theorem for odd $N$ with $7\nmid N$. This audit verifies that implication, its convergence justification, and the resulting divergence on the nonconstant subspace. It does not repeat the separate p-adic coefficient-Jacobian proof supplying that additional input. The restriction is correctly retained everywhere it is needed.

The core internal analytic input is the all-fixed-power kernel theorem, which I independently audited in r7_audit_all_fixed_powers.md. That audit includes its full nonlinear phase separation and finite-grid proof. Here the particular classical density interpretation of each kernel, not just smoothness or bistochasticity, is also checked.

| Obligation | Finding |
| --- | --- |
| Actual classical map and its volume | Correct symbol and momentum convention; analytic area-preserving torus diffeomorphism |
| Uniform hyperbolicity | Explicit invariant-cone and line-bundle construction is valid |
| External ergodicity theorem | Xia, author version v2, Theorem 4.2; every hypothesis is satisfied |
| Discrete-to-continuous embedding | Centered Fourier isometry is exact on polynomial kernels and converges in norm for continuous kernels |
| Classical operator identification | Kernels equal compressions of powers of the same unitary Koopman operator |
| Fejér domination | Exact, positive, correctly normalized, and valid with spectral multiplicities |
| Low and high frequencies | Compatible nested fixed cutoffs; no missing off-diagonal block |
| Arbitrary eigenbasis bound | Full commutant dominates the eigenbasis-projector subspace |
| Approximate stationary subspace | Correct dimension, injectivity, and singular-value conclusion |
| Signed derivative | Correct finite-dimensional algebra and absolute convergence under the stated extra input |

## 2. The classical hypotheses are genuinely verified

Use the notation of the raw source:
$$
 F_+=\kappa_\tau\mathsf S,\qquad
 \kappa_v=C\Phi_{-v}C,\qquad C(q,p)=(q,-p),
 \qquad \mathsf S=\begin{pmatrix}3&4\\2&3\end{pmatrix}.
$$
The vector field of $\Phi_v$ is $X=(a_p,-a_q)/(2\pi)$, with the corrected ordinary Weyl symbol of the exact modular matrix. The $p$-dependent factor is $r(q+1/2)$, as required by the modular half. No uncorrected symbol or different map is substituted.

The finite Fourier support and coefficient bound give $\|DX\|_\infty<2000$. Hence
$$
 \|D\kappa_\tau-I\|_\infty\le e^{2000\tau}-1\le4000\tau.
$$
The vector field is periodic, bounded, and analytic. Its real flow exists globally. Its divergence is zero, so the flow has determinant one by the variational equation. Conjugation by the fixed reflection $C$ preserves area preservation, and $\det\mathsf S=1$. Thus $F_+$ is an analytic area-preserving diffeomorphism of the compact connected torus.

The hyperbolicity argument is explicit and does not rely on an unstated structural-stability neighborhood. Let
$$
 \lambda=3+2\sqrt2,\qquad
 Z=\begin{pmatrix}\sqrt2&\sqrt2\\1&-1\end{pmatrix}.
$$
Then
$$
 Z^{-1}\mathsf SZ=\operatorname{diag}(\lambda,\lambda^{-1}),
 \quad \|Z\|_\infty<3,\quad \|Z^{-1}\|_\infty<1,
$$
and
$$
 Z^{-1}DF_+(z)Z=
 \operatorname{diag}(\lambda,\lambda^{-1})+E(z),
 \qquad \|E(z)\|_\infty<84000\tau<10^{-3}.
$$
For a determinant-one two-by-two matrix, inversion swaps the diagonal entries and negates the off-diagonal entries. The inverse therefore has row-sum error less than $2\cdot10^{-3}$ from $\operatorname{diag}(\lambda^{-1},\lambda)$.

For the unstable cone $|v|\le|u|$, the outgoing first coordinate has modulus at least $(\lambda-10^{-3})|u|$, and the second at most $(\lambda^{-1}+10^{-3})|u|$. The image lies in $|v|<|u|/4$, and the maximum norm expands by more than five. The inverse has the same properties on the stable cone, with the coordinates exchanged and the stated doubled error.

The invariant bundles are also supplied. The slope map of a determinant-one matrix is
$$
 \eta\longmapsto\frac{c+d\eta}{a+b\eta},
 \qquad
 \frac{d}{d\eta}\frac{c+d\eta}{a+b\eta}
 =\frac1{(a+b\eta)^2}.
$$
On the cone this derivative is bounded by $1/25$. Applying the maps along successive backward orbit points gives nested intervals whose diameters shrink uniformly. Their unique limiting slope is continuous, since finite compositions are continuous and convergence is uniform. Shifting the compositions gives invariance. The analogous inverse construction gives the stable line. The two limiting lines lie in disjoint narrower cones and span the tangent plane. Expansion by five in the appropriate direction yields the global Anosov inequalities after a fixed change of norm.

I independently reopened the primary source: Zhihong Xia, [Hyperbolic invariant sets with positive measures, author version arXiv:math/0503437v2](https://arxiv.org/html/math/0503437v2). Theorem 4.2 gives ergodicity for a volume-preserving Anosov diffeomorphism with regularity $C^r$, $r>1$. Compact connected manifolds and smooth volume are standing assumptions in the introduction. I also checked the [journal record](https://www.aimsciences.org/article/doi/10.3934/dcds.2006.15.811), DCDS 15 (2006), 811–818. Every hypothesis holds here; normalized area is the relevant volume. The argument uses ergodicity only, without a mixing rate.

## 3. The centered Fourier embedding has no hidden alias error

All Hilbert-space normalizations are consistent. For odd $N$, let $m_N=(N-1)/2$ and
$$
 \mathcal H_N=\operatorname{span}\{e_k(q)=e^{2\pi ikq}:|k|\le m_N\}.
$$
The map in the source sends $v\in\mathbb C^N$ to the trigonometric polynomial with coefficients
$$
 \widehat v_N(k)=N^{-1/2}\sum_xv_xe^{-2\pi ikx/N}.
$$
Finite character orthogonality proves that this is an isometry $\mathcal I_N$ onto $\mathcal H_N$. It sends the vector $N^{-1/2}(1,\ldots,1)$ to the function one. In particular
$$
 \mathcal I_NJ_N\mathcal I_N^*=J
$$
exactly. The finite identity becomes the projection $P_{\mathcal H_N}$, which converges strongly but not in operator norm to the infinite identity. The source retains this distinction.

For a polynomial kernel
$$
 k(q,s)=\sum_{|u|,|v|\le M}c_{uv}e_u(q)e_v(s),
$$
take $N>2M$. An input Fourier mode $e_j$, $|j|\le m_N$, gives a discrete inner character sum with frequency $v+j$. Since
$$
 |v+j|\le M+m_N\le N-1,
$$
divisibility by $N$ is equivalent to $v+j=0$. Thus the sampled matrix acts exactly as the integral kernel on every retained input mode. Output modes are also retained, and the integral operator kills all input modes outside the retained space. This proves exact equality of the embedded sampled operator and the continuous polynomial-kernel operator on all of $L^2(\mathbb T)$.

Every continuous torus kernel is uniformly approximable by trigonometric polynomial kernels. If the error is at most $\eta$, its integral-operator norm is at most $\eta$, by the Hilbert--Schmidt bound. Its sampled matrix has absolute row and column sums at most $\eta$, and hence operator norm at most $\eta$. The isometry preserves that norm. The triangle inequality proves
$$
 \left\|\mathcal I_N
 [N^{-1}k(x/N,y/N)]\mathcal I_N^*-\mathcal K\right\|_{\rm op}
 \longrightarrow0.
$$
The same polynomial approximation proves compactness of $\mathcal K$.

Applied to the fixed-power theorem, this yields
$$
 \widehat R_{n,N}:=\mathcal I_N|U_N^n|^{\circ2}\mathcal I_N^*
 \longrightarrow\mathcal R_n
$$
in operator norm for every fixed $n\ge1$. Adjoints converge as well. The zero-time term is not included in this compact convergence.

The density interpretation of the all-fixed-power kernel gives the correct common classical operator. Let $\iota g(q,r)=g(q)$ and
$$
 \mathcal C h=h\circ F_+^{-1}.
$$
Area preservation makes $\mathcal C$ unitary. For continuous $g,h$, changing variables by $F_+^n$ gives
$$
 \langle h,\mathcal R_ng\rangle
 =\int_{\mathbb T^2}
 \overline{h(q(F_+^n(s,r)))}g(s)\,ds\,dr
 =\langle\iota h,\mathcal C^n\iota g\rangle.
$$
Both operators are contractions, so density extends the identity to $L^2$:
$$
 \mathcal R_n=\iota^*\mathcal C^n\iota.
$$
Only knowing that the kernels were compact and bistochastic would not give this identity. The stronger identification is part of the audited input and is correctly used.

## 4. Exact Fejér domination and low frequencies

For any unitary $\mathcal W$, write
$$
 A_T(\mathcal W)=\frac1T\sum_{j=0}^{T-1}\mathcal W^j.
$$
At eigenvalue one, $A_T^*A_T$ equals one. At every other eigenvalue it is nonnegative. Therefore the stationary orthogonal projection obeys
$$
 \mathcal E\le A_T^*A_T.
$$
Counting ordered pairs of indices in the product gives the exact coefficients
$$
 A_T^*A_T=\frac1T I+
 \frac1T\sum_{n=1}^{T-1}(1-n/T)(\mathcal W^n+\mathcal W^{-n}).
$$
The diagonal compression of $(\operatorname{Ad}U_N)^n$ is $|U_N^n|^{\circ2}$. The normalized constant diagonal vector is stationary, and the coefficients above sum to one. Subtracting its rank-one projection consequently yields
$$
 0\le Q_N\le\frac1T(I_N-J_N)
 +\frac2T\sum_{n=1}^{T-1}(1-n/T)
 \operatorname{Re}(R_{n,N}-J_N).
$$
The right side is positive despite its individual nonzero-time terms not having to be positive.

For each fixed $T$, let
$$
 K_T=\frac2T\sum_{n=1}^{T-1}(1-n/T)
 \operatorname{Re}(\mathcal R_n-J).
$$
This is compact and self-adjoint. Its embedded discrete counterpart converges in operator norm. Thus the embedded upper bound is
$$
 \frac1T(P_{\mathcal H_N}-J)+\widehat K_{T,N},
 \qquad \|\widehat K_{T,N}-K_T\|\to0.
$$
The exact classical identity is
$$
 \frac1T(I-J)+K_T
 =\iota^*A_T(\mathcal C)^*A_T(\mathcal C)\iota-J.
$$

The mean-ergodic argument is proved in the source rather than assumed with a quantitative rate. Orthogonal complements give
$$
 \overline{\operatorname{ran}(I-\mathcal C)}
 =\ker(I-\mathcal C)^\perp.
$$
On $(I-\mathcal C)h$, the time average is $(h-\mathcal C^Th)/T$, whose norm tends to zero. The averages are contractions, so the conclusion extends to the closure. They are the identity on fixed vectors. Ergodicity makes those fixed vectors exactly the constants. Hence, for every fixed mean-zero $g$,
$$
 \|A_T(\mathcal C)\iota g\|_2\longrightarrow0.
$$

For a fixed trigonometric polynomial $g$, take the quantum quadratic form and let $N\to\infty$ with $T$ fixed. The kernel convergence and exact Fourier representation give
$$
 0\le\limsup_N\langle g,\widehat Q_Ng\rangle
 \le\|A_T(\mathcal C)\iota g\|_2^2.
$$
Letting $T\to\infty$ proves that each such form tends to zero. The constant mode is zero identically. On any fixed Fourier space $E_ML^2$, the trace of the positive compression is the sum of finitely many such diagonal forms, so
$$
 \|E_M\widehat Q_NE_M\|\longrightarrow0.
$$
This argument proves a statement for every fixed $M$; it does not give a bound at $M=M(N)$, and none is needed.

## 5. High frequencies and the order of limits

On $E_M^\perp$, the embedded Fejér inequality gives
$$
 \|(I-E_M)\widehat Q_N(I-E_M)\|
 \le\frac1T+\|(I-E_M)K_T(I-E_M)\|+o_T(1).
$$
The coefficient of the finite identity is $1/T$, and $P_{\mathcal H_N}\le I$. The error is independent of $M$, being bounded by the operator-norm error of the entire finite sum.

For fixed $T$, compactness implies
$$
 \|(I-E_M)K_T(I-E_M)\|\longrightarrow0.
$$
One can approximate $K_T$ by a finite-rank operator and use strong convergence of $E_M$ uniformly on the finite-dimensional ranges of that operator and its adjoint. No collective compactness in $T$ is asserted.

The off-diagonal blocks are not discarded. For a positive operator $Q$ and a projection $E$, semidefinite Cauchy--Schwarz gives
$$
 |\langle x,Qy\rangle|
 \le\langle x,Qx\rangle^{1/2}\langle y,Qy\rangle^{1/2}.
$$
For $x=Ev$, $y=(I-E)v$, this implies
$$
 \|Q\|\le\|EQE\|+\|(I-E)Q(I-E)\|.
$$
Combining the two frequency bounds therefore proves
$$
 \limsup_N\|\widehat Q_N\|
 \le\frac1T+\|(I-E_M)K_T(I-E_M)\|.
$$
First send $M$ to infinity for this fixed $T$, and then send $T$ to infinity.

An explicit choice order makes clear why no growing-time theorem is hidden. Given an error tolerance, choose a fixed Fejér length $T_{\rm high}$ to make $1/T_{\rm high}$ small. Choose a fixed Fourier cutoff $M$ using compactness of $K_{T_{\rm high}}$. The finitely many low Fourier modes can then use a separate fixed $T_{\rm low}$, chosen by classical ergodicity. Finally choose $N$ large enough for the finitely many kernels through both chosen lengths. All cutoffs are fixed before this final $N$-limit.

This is a valid upgrade from convergence on fixed test functions to operator-norm convergence. Strong ergodic convergence alone would not make that upgrade; compactness of the fixed nonzero-time kernels supplies the required control of the remaining frequencies.

## 6. Eigenbasis independence and approximate stationary vectors

For any orthonormal eigenbasis, the rank-one projectors $\psi_j\psi_j^*$ form an orthonormal family in Hilbert--Schmidt space. The orthogonal projection onto their span is dominated by the full commutant projection, including in the presence of repeated eigenvalues. Its coordinate-diagonal compression is exactly $B_NB_N^*$.

The intensity matrix is bistochastic, so $B_NB_N^*$ fixes the normalized constant vector. Its orthogonal complement is invariant, and its restriction there is positive. Subtracting the common constant projection from the compressed inequality gives
$$
 0\le B_NB_N^*-J_N\le Q_N.
$$
This upper bound is independent of the choice of eigenbasis. The asserted uniformity is therefore valid without any choice-of-basis compactness argument.

Let $u_N=\mathbf I_N/\sqrt N$, and put $P_0=|u_N\rangle\langle u_N|$. For
$$
 T_N=\Pi_N\mathcal E_N-P_0,
$$
one has $T_NT_N^*=\Pi_N\mathcal E_N\Pi_N-P_0$, whose nonzero part is $Q_N$. Thus $\|T_N\|=\sqrt{q_N}$. On a stationary traceless matrix $X$, one has $T_NX=\Pi_NX$, giving
$$
 \|\Pi_NX\|_{\rm HS}\le\sqrt{q_N}\|X\|_{\rm HS}.
$$
For large $N$, $q_N<1$, so $X\mapsto O_NX$ is injective on the $d_N-1$ dimensional stationary traceless space:
$$
 \|O_NX\|_{\rm HS}^2\ge(1-q_N)\|X\|_{\rm HS}^2.
$$
If $Y=O_NX$ and $D=\Pi_NX$, the lower stationary equation is
$$
 (I-S_N)Y=C_N^{\rm in}D.
$$
The coupling block is a contraction. Dividing the two bounds proves Theorem 2 on the image subspace. The singular-value min--max principle follows by diagonalizing $(I-S_N)^*(I-S_N)$. A subspace of the stated dimension with Rayleigh quotient at most $q_N/(1-q_N)$ forces at least that many singular values below the displayed bound.

For a unitary, $d_N=\sum_\lambda m_\lambda^2\ge\sum_\lambda m_\lambda=N$. Thus at least $N-1$ small singular values are obtained. This reasoning permits exact stationary dark vectors in dimensions where they have not been excluded. It does not claim eigenvalues of the nonnormal compression $S_N$ near one.

The identity
$$
 \Pi_N\mathcal E_N\Pi_N
 =\lim_{T\to\infty}\frac1T\sum_{n=0}^{T-1}|U_N^n|^{\circ2}
$$
is also correct for each fixed finite $N$, by the finite spectral theorem. Its interpretation takes the infinite time average first for each $N$; it does not replace the limit order used in the proof above.

## 7. The signed first-return conclusion is correctly conditional

This section uses the declared extra input only where necessary: for odd $N$ with $7\nmid N$, $U_N$ has simple spectrum and the intensity matrix is invertible.

Write $\mathcal W=\left(\begin{smallmatrix}P&B\\C&S\end{smallmatrix}\right)$, with $B$ now the outgoing coupling block. If $Sy=y$, norm preservation of the full unitary forces $By=0$, so $(0,y)$ is stationary. Under the input assumption, every stationary matrix is a linear combination of the eigenprojectors and its diagonal is the invertible intensity map applied to those coefficients. Hence $y=0$, and $R=(I-S)^{-1}$ exists.

Every diagonal vector has a unique stationary extension. Its lower component is $RC$ applied to that vector, so
$$
 X=\begin{pmatrix}I\\RC\end{pmatrix},\quad
 \mathcal WX=X,\quad
 P+BRC=I.
$$
Unitarity also gives $\mathcal W^*X=X$, whose lower component yields
$$
 B=C^*R^*(I-S).
$$
The return function is
$$
 \mathfrak F(z)=zP+z^2B(I-zS)^{-1}C.
$$
Differentiation at one and $R+RSR=R^2$ give
$$
 \mathfrak F'(1)
 =P+2BRC+BRSRC
 =I+BR^2C
 =I+C^*R^*RC
 =X^*X.
$$
Let $\mathcal J$ have the normalized eigenprojectors as columns. It is an isometry onto the commutant, and $\Pi\mathcal J=B_N$. Thus $X=\mathcal JB_N^{-1}$, proving
$$
 X^*X=(B_NB_N^*)^{-1}.
$$
All multiplication orders in this calculation are correct.

The absolute convergence claim is justified even if nonstationary dark modes survive. Every unit-circle eigenvector $Sy=\zeta y$ of a contraction satisfies $S^*y=\overline\zeta y$, by equality in the contraction norm. The span of these eigenspaces is reducing and unitary. Unitarity of the full block matrix gives $By=0$ and $C^*y=0$. On its orthogonal complement the finite-dimensional compression has spectral radius strictly below one. Jordan form therefore bounds its powers by a polynomial times a decaying geometric sequence. Only that complement contributes to $BS^{r-2}C$, so
$$
 \sum_{r\ge1}r\|F_r\|_{\rm op}<\infty.
$$
Evaluation of the series and its derivative at one is consequently legitimate. No uniform spectral radius bound in $N$ is claimed.

On the nonconstant diagonal subspace, $B_NB_N^*$ is positive definite and its largest eigenvalue is
$$
 \beta_N=\|B_NB_N^*-J_N\|\le q_N\to0.
$$
Therefore the least eigenvalue of its inverse on that subspace is $\beta_N^{-1}\to\infty$. This is the stated divergence of the signed derivative. It is not an assertion about the scalar probability mean $\sum r\|F_r\|_{\rm HS}^2$.

## 8. Evidence, limitations, and provenance

No gap was found in the discrete normalization, the compact limit, the two frequency cutoffs, the classical theorem hypotheses, the basis-independent compression, or the finite signed derivative calculation. No proof step treats $\tau$ as tending to zero, assumes simple spectrum along all odd dimensions, or imports a time estimate uniform for $R(N)$.

The full signed trace functional at times proportional to $N$, and all higher orders required for the original spectral claim, remain outside the proved conclusion. Neither the small singular values of $I-S_N$ nor the stationary projection bound evaluates that functional.

The fresh checker r7_audit_stationary_dephasing_checks.py passed **78,425 exact assertions**. Its SHA-256 is
1fa3708987334148dd8070a968b514d9aa6fdd4940d6b7fc275e4d4a71888098.
It checks the Fourier no-alias conditions, Fejér coefficients, cone constants, and finite compression identities using integer and Gaussian-rational arithmetic. The abstract matrix examples include complex eigenbases and degenerate spectra. The signed derivative identity is checked directly from the blocks of $\operatorname{Ad}U$ in dimensions three and four. These examples verify algebra, not the asymptotics of the original tiny-kick family; the analytic proof above supplies those.

| Source inspected | Scope | SHA-256 |
| --- | --- | --- |
| research_round7_2026_10_21/r7_return_uniform_stationary_dephasing.md | Complete raw proof, including all additional conclusions | c2bf50a33a642b984afa7bfa83fdc0d28b8019c79d4f47121ab52adee5e53075 |
| research_round7_2026_10_21/r7_return_all_fixed_powers_phase_separation.md | Full input independently reconstructed in this audit assignment; density identification used here | 46982efaa581d322d4e82d5f5782ccf69f979a5a59adfb863dd40ef292205527 |
| research_round7_2026_10_21/root_original_intensity_at_prescribed_phase.md | Exact statement, $7\nmid N$ restriction, and stationary-intensity consequence; separate p-adic proof not re-audited in this pass | deea7755070222fdfca37d5c8f2721dc82b62afa34d56b18df614756308b5c63 |
| research_round6_2026_10_21/round6_main_report.md | Original family and normalizations | 473b7b5b700a8ff17801eb9ca422c5949be15d0551c252e0b4035997db54b2bf |
| Spectral_research_master.md | Frozen base identification only | 3534e4d7aa97c2f8621050248652363c639aeedf723f8b7fe7a971dc01ac2302 |

External input independently checked: Xia, arXiv:math/0503437v2, introduction and Theorem 4.2, with the publication record DOI 10.3934/dcds.2006.15.811. The retrieved PDF identifies itself as version 2, 26 August 2005. No unverified external theorem is needed in the main proof.

**Required corrections to this source: none.**
