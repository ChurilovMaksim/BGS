> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_countermodel.md`. Embedded SHA256: `6ebea61daab7c46fafa67d1212ecaee110cc08c348b933d1eda7ff5a5acd761a`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Independent proof audit of the finite-field clock and its generic perturbation

Date: 21 October 2026. Auditor: the isolated task /root/r7_physical_audit.

## 0. Claim card and primary verdict

**Primary verdict: proved as written for the explicitly enumerated countermodel properties.** The finite-field construction, the growing range of flat powers and small reverse-edge operators, the deterministic algebraic eigenbasis choice, the nonvanishing statements for every nonzero power, the absence of a dark sector, the return-tail estimate, and the positive fixed-test pair-defect limit all follow from the supplied proofs.

One scope correction was identified during this audit and is now applied in the source: the initial phrase “no exact spectral resonances” was replaced by the stated distinctness of nontrivial ordered eigenvalue ratios. The binary perturbation retains exact higher multiplicative resonances. The corrected source explicitly acknowledges them, and §10 records the issue and an exact relation. None of the precise properties proved in §§3 and 9 had to be changed.

This is a countermodel to the sufficiency of the listed abstract inputs. Its dimensions are $N=p^2$, with $p>3$ prime. It is not the original one-dimensional Weyl family, and the audit makes no claim about the original family beyond distinguishing the scopes.

The base matrix is

$$
C_p=\mathcal F^*V_1\mathcal F,\qquad
(V_t\psi)(k,l)=e_p\!\left(\frac{tl^2}{2}
+\frac{t^2kl}{2}+\frac{t^3k^2}{6}\right)\psi(k,l+tk),
$$

where every finite-field fraction is modular. The Fourier transform has positive sign and normalization $p^{-1}$ on the $p^2$-dimensional space. The exact claims are

$$
C_p^p=I,\qquad |(C_p^n)_{xy}|^2=N^{-1},\qquad
\|Q(C_p^n)\|_{\rm op}=N^{-1/2}\quad(1\le n<p),
$$

with $Q(U)_{xy}=U_{xy}\overline{U_{yx}}$.

The perturbed sequence uses an algebraic unitary eigenbasis $H=GV$, a prescribed rational $\eta_N=N^{-12}$, and

$$
\varepsilon_N=2^{-N}\eta_N,\qquad
\widetilde U_N
=H\operatorname{diag}(\lambda_j e^{i\varepsilon_N2^j})H^*,
\qquad \lambda_j^p=1.
$$

Its precisely audited properties are:

- near-flat entries and probability operators, and reverse-edge norm tending to zero, uniformly for $1\le n<p=\sqrt N$;
- simple spectrum, pairwise distinct nontrivial ordered eigenvalue ratios, and transcendental nontrivial ratios for every nonzero integer power;
- every square minor of every nonzero integer power nonzero;
- no dark reducing subspace for the diagonal-pair return compression;
- exact return normalization $\sum_r\|F_r\|_{\rm HS}^2=N$ and first moment $\sum_r r\|F_r\|_{\rm HS}^2=N^2$;
- first-return probability concentrated at $r=p$, but normalized first moment satisfying
  $$
  1-\frac{13}{\sqrt N}
  \le\frac1{N^2}\sum_{r>N^{12}}r\|F_r\|_{\rm HS}^2\le1;
  $$
- an empty randomly rotated local limit, and, for every fixed nonzero admissible $b$,
  $$
  \frac{\Delta_{2,N}^{\widetilde U}(b)}{\sqrt N}
  \longrightarrow\int_0^\infty|\widehat b(u)|^2\,du>0.
  $$

The eigenvector intensity matrix is used only through its nonzero determinant. No quantitative lower bound for that determinant or its least singular value is asserted or needed.

## 1. Independence and dependency matrix

I read the two raw proofs and reconstructed the operators before inspecting any computation. No earlier checker or auditor verdict was used. The independent finite checker accompanying this report was written from the raw definitions and the derivations below.

The only external theorem used is the qualitative Lindemann–Weierstrass statement. Its exact form was checked directly in the author PDF of Cheng-Chao Huang, *Explicit Bounds for Linear Forms in the Exponentials of Algebraic Numbers*, arXiv:2112.05004v2, page 1, Theorem 1.1. Its hypotheses match the complex algebraic exponents and algebraic coefficients used here. The proof does not invoke the paper's quantitative estimates.

| Obligation | Status | Decisive check |
| --- | --- | --- |
| Finite-field group law and period | Passed | Expansion of the exact phase cocycle |
| Fourier signs, normalization, all nontrivial flat powers | Passed | Invertible two-dimensional Hessian and full Gauss norm |
| Reverse-edge operator norm | Passed | Nondegenerate alternating mixed coefficient |
| Trace values and cluster multiplicities | Passed | Fixed coordinates and weighted $p$-cycles |
| Deterministic algebraic $V,G,H$ | Passed | Algebraic projectors, Gram–Schmidt, analytic density, rational Cayley enumeration |
| All-power binary perturbation claims | Passed | Distinct ordered differences and subset sums, with verified transcendence input |
| Quantitative short-power and $Q$ perturbation estimates | Passed | Unitary telescoping and Hilbert–Schmidt product bounds |
| Absence of a dark sector | Passed | Projection injective on every eigenspace of $U\otimes\overline U$ |
| Return probability and exact mean | Passed | Block-unitarity telescoping with the correct dimensions |
| Mean beyond $N^{12}$ | Passed | Probability outside $\{1,p\}$ at most $4p\delta_N$ |
| Fixed-test pair normalization and positive leading coefficient | Passed | Fourier normalization, exact traces, uniform trace perturbation bound |
| Initial all-orders resonance wording | Corrected; stronger property explicitly excluded | Explicit equal-degree multiplicative relation in §10 |
| Quantitative intensity invertibility or return spectral gap | Not claimed | No such bound is used |
| Original family or all odd dimensions | Out of scope | The construction is an auxiliary sequence in prime-square dimensions |

## 2. Exact finite-field propagation and flat powers

Let

$$
a_t(k,l)=\frac{tl^2}{2}+\frac{t^2kl}{2}+\frac{t^3k^2}{6}.
$$

The multiplier in $V_tV_s$ is $a_t(k,l)+a_s(k,l+tk)$. Its $l^2$, $kl$, and $k^2$ coefficients are respectively

$$
\frac{t+s}{2},\qquad
\frac{t^2+s^2}{2}+st=\frac{(t+s)^2}{2},
$$

$$
\frac{t^3+s^3}{6}+\frac{st^2+s^2t}{2}
=\frac{(t+s)^3}{6}.
$$

Thus $V_tV_s=V_{t+s}$ exactly. The coordinate permutation is $l\mapsto l+tk$, and phases have modulus one, so each $V_t$ is unitary. Fourier orthogonality proves that $\mathcal F$ is unitary. Consequently $C_p^n=\mathcal F^*V_{n\bmod p}\mathcal F$, including $C_p^p=I$. This is an ordinary representation of the additive finite field, with no unresolved projective scalar.

Multiplying the three operators with the stated Fourier signs gives

$$
(C_{p,t})_{xy}
=p^{-2}\sum_{k,l}
e_p\bigl(a_t(k,l)+k(y_1-x_1+ty_2)+l(y_2-x_2)\bigr).
$$

With $z=(k,l)^T$, $v=Y_ty-x$,

$$
H_t=\begin{pmatrix}t^3/3&t^2/2\\t^2/2&t\end{pmatrix},
\qquad Y_t=\begin{pmatrix}1&t\\0&1\end{pmatrix},
$$

the exponent is $\tfrac12z^TH_tz+z^Tv$. Since $\det H_t=t^4/12$, it is nonsingular for every $t\ne0$ and every prime $p>3$.

For an invertible symmetric $H$, the complete Gauss sum $G(H)=\sum_z e_p(z^THz/2)$ satisfies

$$
|G(H)|^2
=\sum_{r,w}e_p(w^THr+r^THr/2)=p^2.
$$

Only $r=0$ survives the inner complete character sum. Completing the square is a bijective translation over the field and therefore gives

$$
(C_{p,t})_{xy}
=\frac{\gamma_{p,t}}p
e_p\!\left[-\frac12(Y_ty-x)^TH_t^{-1}(Y_ty-x)\right],
\qquad |\gamma_{p,t}|=1.
$$

This proves the exact flatness of all $p-1$ nonidentity powers. The exclusions $p=2,3$ are essential to the displayed definitions; no additional congruence restriction on $p$ is present.

## 3. The reverse-edge norm, traces, and multiplicities

Direct inversion gives

$$
G_t=H_t^{-1}
=\begin{pmatrix}12/t^3&-6/t^2\\-6/t^2&4/t\end{pmatrix},
\qquad
D_t=G_tY_t
=\begin{pmatrix}12/t^3&6/t^2\\-6/t^2&-2/t\end{pmatrix}.
$$

The completed-square phase is

$$
S_t(x,y)=-\tfrac12x^TG_tx+x^TD_ty
-\tfrac12y^TY_t^TG_tY_ty.
$$

Its reversal is

$$
S_t(x,y)-S_t(y,x)
=A_t(x)-A_t(y)+x^TL_ty,
\qquad
L_t=D_t-D_t^T
=\begin{pmatrix}0&12/t^2\\-12/t^2&0\end{pmatrix}.
$$

The determinant $144/t^4$ is nonzero. The scalar $\gamma_{p,t}$ cancels in $Q$, and endpoint phases are diagonal unitary multipliers. Thus its singular values equal those of $R_t(x,y)=p^{-2}e_p(x^TL_ty)$. Complete character orthogonality gives

$$
(R_tR_t^*)_{xx'}
=p^{-4}\sum_y e_p((x-x')^TL_ty)
=p^{-2}\delta_{xx'}.
$$

Every singular value is exactly $1/p$. This verifies the reverse-edge condition for every nontrivial power, with its stated normalization.

For $t\ne0$, the permutation defining $V_t$ fixes a coordinate precisely when $k=0$. Therefore

$$
\operatorname{Tr}C_{p,t}=\sum_l e_p(tl^2/2),
\qquad |\operatorname{Tr}C_{p,t}|^2=p.
$$

At $t=0$, the trace is $p^2$. Consequently

$$
|\operatorname{Tr}C_p^n|^2
=\begin{cases}p^4,&p\mid n,\\p,&p\nmid n.\end{cases}
$$

The multiplicities are also correct. Each $k\ne0$ gives one weighted $p$-cycle. Its product of phases is one because the sums of $1,l,l^2$ over $\mathbb F_p$ vanish in the required formula. Its characteristic polynomial is $z^p-1$. The $k=0$ subspace is diagonal with phases $e_p(l^2/2)$. Thus the multiplicity of $e_p(a)$ is

$$
\mu_a=p-1+\#\{l:l^2/2=a\},
$$

between $p-1$ and $p+1$, and all $p$ roots occur.

## 4. Deterministic algebraic choice of the eigenbasis

The entries of $C_p$ lie in a cyclotomic number field. Its spectral projectors can be written explicitly as

$$
P_a=\frac1p\sum_{t=0}^{p-1}e_p(-at)C_p^t.
$$

Their entries are algebraic. Choosing the first independent columns in the prescribed coordinate order and applying Gram–Schmidt stays in the algebraic numbers: conjugates are algebraic, squared norms are positive real algebraic, and their positive square roots are algebraic. Grouping the roots by $a=0,\ldots,p-1$ fixes a deterministic algebraic eigenbasis $V$.

For each square minor of $H=GV$, the squared modulus is a real-analytic function on $U(N)$. It is not identically zero, because some permutation matrix $H$ makes the chosen row-column minor a signed permutation determinant. The function $\det(|H_{vj}|^2)$ is not identically zero either; it equals one at $H=I$.

The continuation argument in the source is valid. Any two unitaries are connected by $G_0e^{itA}$, with $A$ Hermitian. A real-analytic function vanishing in a neighborhood of $G_0$ vanishes initially on this curve and hence on the whole curve by the one-variable identity theorem. It would vanish at every other unitary. Thus each nonzero condition has open dense complement of its zero set. There are finitely many conditions for each $N$, so their intersection is open dense and meets every ball around $I$.

The Cayley map

$$
A\mapsto(I+iA)(I-iA)^{-1}
$$

maps Hermitian matrices near zero analytically onto a neighborhood of $I$. Rational Hermitian matrices are dense. Their Cayley transforms lie in $\mathbb Q(i)$ and are exactly unitary. Consequently an algebraic $G$ satisfying $\|G-I\|_{\rm HS}<\eta_N$, all minor conditions, and intensity invertibility exists.

Once an enumeration of the rational Hermitian matrices is fixed, taking its first acceptable member is deterministic and terminates by the proved open density. The acceptance tests are exact algebraic tests; the squared Hilbert–Schmidt bound is an algebraic comparison. No random choice or unverified exceptional set remains. The enumeration need not be efficient. An explicit height/lexicographic enumeration would improve reproducibility but is not needed for the existence theorem.

Crucially, this proves only $\det\mathcal B_H\ne0$. The argument gives no quantitative lower bound as $N$ varies. The later argument needs only injectivity and therefore does not incur an unproved quantitative condition here.

## 5. Binary perturbations, transcendence, and every nonzero power

The external statement checked is the qualitative result that exponentials of distinct algebraic arguments have no nonzero linear relation with algebraic coefficients. See [Huang, Theorem 1.1, arXiv:2112.05004v2, p.1](https://arxiv.org/pdf/2112.05004v2), also [DOI 10.1145/3476446.3536170](https://doi.org/10.1145/3476446.3536170). In particular $e^\alpha$ is transcendental for nonzero algebraic $\alpha$, by using the arguments $0,\alpha$.

Set $z=e^{i\varepsilon_N}$. It is transcendental, and the perturbed eigenvalues are $\lambda_jz^{2^j}$. This gives a useful direct audit of the nonvanishing arguments.

For every nonzero integer $q$, the eigenvalue ratio of $\widetilde U_N^q$ is

$$
(\lambda_j/\lambda_k)^q
e^{iq\varepsilon_N(2^j-2^k)}.
$$

For $j\ne k$ its exponential has nonzero algebraic argument, hence is transcendental; multiplication by a nonzero algebraic number preserves transcendence. The ratio cannot be one or a root of unity.

If two such ordered ratios agree, then an exponential with argument

$$
iq\varepsilon_N(2^j-2^k-2^l+2^m)
$$

is algebraic. The argument must be zero. Nonzero ordered differences of powers of two are unique: the sign fixes orientation, the two-adic valuation fixes the smaller index, and the remaining odd factor fixes the larger index. Thus $(j,k)=(l,m)$. This proves simplicity and distinct nontrivial ordered ratios for every nonzero power of the same displayed matrix.

For equally sized nonempty $I,J$, Cauchy–Binet gives

$$
\det\widetilde U_N^q[I,J]
=\sum_{|S|=|I|}
\det H[I,S]\overline{\det H[J,S]}
\Bigl(\prod_{j\in S}\lambda_j^q\Bigr)
e^{iq\varepsilon_N\sum_{j\in S}2^j}.
$$

Every coefficient is nonzero algebraic. Distinct subsets have different binary sums, and multiplication by the nonzero integer $q$ preserves distinctness. The verified transcendence theorem applies directly. Equivalently, for $q>0$ this is a nonzero algebraic-coefficient polynomial in the transcendental $z$; for $q<0$, multiplication by a suitable power of $z$ gives such a polynomial. Hence every square minor is nonzero, simultaneously for all nonzero integer powers.

The arguments require distinct algebraic exponents, not their linear independence over $\mathbb Q$. The exponents here are commensurate, which is harmless for these linear-combination and subset-sum conclusions. It is precisely why the stronger absence of arbitrary higher multiplicative resonances must not be claimed.

## 6. Quantitative proximity and the growing physical range

The phase perturbation has operator norm at most

$$
\max_j|\lambda_j(e^{i\varepsilon_N2^j}-1)|
\le\varepsilon_N2^{N-1}=\eta_N/2.
$$

The eigenbasis conjugation contributes at most $2\|G-I\|_{\rm op}<2\eta_N$. Thus

$$
\delta_N=\|\widetilde U_N-C_p\|_{\rm op}
<\tfrac52\eta_N<3N^{-12}.
$$

Telescoping powers of unitaries gives $\|\widetilde U_N^n-C_p^n\|_{\rm op}\le n\delta_N$. For $1\le n<p$, the exact base flatness then implies

$$
\max_{x,y}|(\widetilde U_N^n)_{xy}|
\le N^{-1/2}+n\delta_N,
$$

$$
\bigl||(\widetilde U_N^n)_{xy}|^2-N^{-1}\bigr|
\le2N^{-1/2}n\delta_N+n^2\delta_N^2.
$$

Multiplying the maximum-entry bound by $N$ bounds the operator norm, so uniformly throughout this growing range,

$$
\bigl\||\widetilde U_N^n|^{\circ2}-J_N\bigr\|_{\rm op}
\le2N\delta_N+N^2\delta_N^2\longrightarrow0.
$$

For a flat base $A$ and $D=\widetilde A-A$,

$$
Q(\widetilde A)-Q(A)
=(D_{xy}\overline{A_{yx}})
+(A_{xy}\overline{D_{yx}})
+(D_{xy}\overline{D_{yx}}).
$$

The Hilbert–Schmidt norm is therefore at most

$$
(2N^{-1/2}+\|D\|_{\rm op})\|D\|_{\rm HS}
\le2\|D\|_{\rm op}+\sqrt N\|D\|_{\rm op}^2.
$$

At power $n$, use $\|D\|_{\rm op}\le n\delta_N$ and the exact base $Q$-norm $N^{-1/2}$. This gives the source's uniform bound

$$
\max_{1\le n<p}\|Q(\widetilde U_N^n)\|_{\rm op}
\le N^{-1/2}+2p\delta_N+\sqrt Np^2\delta_N^2\longrightarrow0.
$$

All dimension factors and range endpoints are correct. The power $p$ itself is excluded from this physical mixing range.

## 7. No dark sector and exact first-return identities

Let $W=\widetilde U_N\otimes\overline{\widetilde U_N}$, and let $\Pi$ project onto the diagonal coordinate pairs. On $\operatorname{ran}\Pi\oplus\operatorname{ran}O$, with $O=I-\Pi$,

$$
W=\begin{pmatrix}P&B\\C&S\end{pmatrix},
\qquad P=|\widetilde U_N|^{\circ2}.
$$

Here $S$ is the compression restricted to the $(N^2-N)$-dimensional space $\operatorname{ran}O$. In particular $S^0$ is the identity on that space when taking the Hilbert–Schmidt norm below.

If $Sv=\zeta v$, $|\zeta|=1$, norm preservation of $W$ forces $\Pi Wv=0$. Thus $Wv=\zeta v$ and $v\in O$. Conversely any $W$-eigenvector in $O$ gives such an eigenvector of $S$. In finite dimension, a nonzero unitary reducing part of $S$ has an eigenvector, so it suffices to exclude these.

The eigenvectors of $W$ are $h_j\otimes\overline{h_k}$. Every nonidentity eigenvalue has a one-dimensional eigenspace by the distinct-ratio result. Its $\Pi$-projection has components $H_{vj}\overline{H_{vk}}$, all nonzero. The eigenspace at one is exactly the span of the $N$ vectors with $j=k$; its projection is the linear map $c\mapsto\mathcal B_Hc$, which is injective. Hence no eigenspace contains a nonzero vector in $O$, and the dark sector is zero.

All eigenvalues of the finite-dimensional contraction $S$ consequently have modulus below one, and $S^m\to0$. This conclusion is qualitative at each fixed $N$; no uniform decay rate has been inserted.

The first-return operators are $F_1=P$ and $F_r=BS^{r-2}C$ for $r\ge2$. Unitarity gives

$$
P^*P+C^*C=I,\qquad B^*B+S^*S=I,\qquad CC^*+SS^*=I.
$$

These yield the exact telescoping identity

$$
\sum_{r=1}^{m+1}F_r^*F_r
=I-C^*S^{*m}S^mC.
$$

Taking the limit proves $\sum_r\|F_r\|_{\rm HS}^2=N$. For $m\ge1$,

$$
\sum_{r>m}\|F_r\|_{\rm HS}^2
=\|S^{m-1}C\|_{\rm HS}^2=a_{m-1}-a_m,
\qquad a_m=\|S^m\|_{\rm HS}^2.
$$

Since $a_m\to0$ and $a_0=N^2-N$, nonnegative tail summation gives

$$
\sum_{r\ge1}r\|F_r\|_{\rm HS}^2
=N+\sum_{m\ge1}(a_{m-1}-a_m)=N^2.
$$

Thus $\nu_N(r)=N^{-1}\|F_r\|_{\rm HS}^2$ is a probability law of exact mean $N$.

## 8. Why almost all normalized mean lies beyond $N^{12}$

For the base clock, unrestricted diagonal-pair returns are $J_N$ except at multiples of $p$, where they are $I_N$, including time zero. The exact formal renewal identity gives

$$
R(z)=\frac{J_N}{1-z}+\frac{I-J_N}{1-z^p},
\qquad
\sum_{r\ge1}z^rF_r=I-R(z)^{-1}.
$$

The two complementary projections allow the inverse to be taken separately. Hence

$$
F_1^{(0)}=J_N,\qquad F_p^{(0)}=I-J_N,\qquad
F_r^{(0)}=0\quad(r\ne1,p).
$$

This is an operator identity for the full first-return sequence, not an inference from transition probabilities without renewal.

The doubled unitaries differ by at most $2\delta_N$. A product defining $F_r$ has exactly $r$ unitary factors and contractive projections between them. Telescoping therefore gives

$$
\|F_r-F_r^{(0)}\|_{\rm op}\le2r\delta_N,\qquad
\|F_r-F_r^{(0)}\|_{\rm HS}\le2r\sqrt N\delta_N.
$$

At $r=p$, the reverse triangle inequality gives

$$
\nu_N(p)\ge
\left(\sqrt{1-\frac1N}-2p\delta_N\right)^2.
$$

The bracket is positive at the stated parameters. Since $P$ is doubly stochastic, $\|P\|_{\rm HS}^2\ge1$, so $\nu_N(1)\ge1/N$. Subtracting these two lower bounds from the exact total probability yields

$$
\nu_N(\mathbb N\setminus\{1,p\})
\le4p\delta_N\sqrt{1-\frac1N}-4p^2\delta_N^2
\le4p\delta_N\le12N^{-23/2}.
$$

This verifies the sign and exponent in the small remaining probability. In particular $\nu_N(p)\to1$.

For $X_N=r/N$, the contribution of $r=1,p$ to the truncated mean is at most $p/N$. The remainder at $r\le N^{12}$ is at most $N^{11}$ times its probability. Therefore

$$
\mathbb E[X_N\mathbf1_{r\le N^{12}}]
\le\frac pN+N^{11}(12N^{-23/2})
=\frac{13}{\sqrt N}.
$$

The exact mean is one, which proves the claimed lower bound for the tail after $N^{12}$. No quantitative spectral-radius or decay estimate for $S$ is used.

Also $X_N\to0$ in probability, since almost all return probability lies at $p/N=N^{-1/2}$, while $\mathbb EX_N=1$. The more general cutoff $\eta_N^{-1}$ is valid with any positive rational $\eta_N\le N^{-12}$: its contribution from the remaining mass is bounded by

$$
\frac{\eta_N^{-1}}N\,4p(3\eta_N)=\frac{12}{\sqrt N}.
$$

The claimed failure of uniform integrability and the extension to smaller rational perturbations therefore follow as stated.

## 9. Local empty limit and the positive fixed-test pair coefficient

The perturbed eigenphases lie within $\rho_N=\eta_N/(4\pi)$ of the $p$ base clock angles. A point in an unfolded interval $[-L,L]$ requires the uniform rotation to lie within circular distance $L/N+\rho_N$ of at least one base angle. Thus

$$
\mathbb P\{\widetilde\Xi_{N,\alpha}([-L,L])>0\}
\le2p(L/N+\rho_N)=2L/p+2p\rho_N\longrightarrow0.
$$

Any finite collection of compactly supported continuous test functions is supported in some such interval. This proves convergence in probability to the empty measure in the vague topology. Exact intensity one is compatible with it because the rare occupied windows contain order-$p$ clusters and their counts are not uniformly integrable.

For the pair statistic, the periodization has Fourier coefficients $N^{-1}\widehat b(n/N)$. Integrating two factors against the common rotation sets their Fourier indices to $n,-n$. Summing over distinct indices gives $|\operatorname{Tr}U^n|^2-N$. The zero-frequency comparison cancels, and the two nonzero signs cancel the factorial $1/2!$. Since $b$ is real,

$$
\Delta_{2,N}^{U}(b)
=N^{-2}\sum_{n\ge1}|\widehat b(n/N)|^2
\left(|\operatorname{Tr}U^n|^2-\min(n,N)\right).
$$

The reference trace moment follows directly from the finite CUE kernel: the two-point factorial density is $N^2-|K_N|^2$, and the coefficient of the appropriate nonzero Fourier difference in $|K_N|^2$ is $(N-|n|)_+$. Adding the $N$ diagonal terms gives $N-(N-|n|)_+=\min(|n|,N)$. The updated base note includes this exact calculation.

Put $w=|\widehat b|^2$. The base trace formula gives

$$
N^{-2}\sum_{n\ge1}w(n/N)|\operatorname{Tr}C_p^n|^2
=\sum_{r\ge1}w(r/p)
+p^{-3}\sum_{\substack{n\ge1\\p\nmid n}}w(n/p^2).
$$

The second term is $O_b(p^{-1})$. The first is

$$
p\int_0^\infty w(u)\,du+O_b(1)
$$

by an ordinary Riemann sum. The CUE part is $O_b(1)$, since $w$ has fixed compact support.

For the perturbation, $|\operatorname{Tr}\widetilde U_N^n-\operatorname{Tr}C_p^n|\le Nn\delta_N$, and each trace has modulus at most $N$. Therefore

$$
\left||\operatorname{Tr}\widetilde U_N^n|^2
-|\operatorname{Tr}C_p^n|^2\right|
\le2N^2n\delta_N.
$$

Summing over the fixed support $n\le BN$ gives

$$
|\Delta_{2,N}^{\widetilde U}(b)-\Delta_{2,N}^{C_p}(b)|
\le2\delta_N\sum_{n\le BN}n\,w(n/N)
=O_b(N^2\delta_N)=O_b(N^{-10}).
$$

Hence both sequences have the same exact positive leading coefficient:

$$
\frac{\Delta_{2,N}^{\widetilde U}(b)}{\sqrt N}
\longrightarrow\int_0^\infty|\widehat b(u)|^2\,du>0.
$$

Positivity follows from $\widehat b(0)=\int b>0$ and continuity. The test is fixed independently of $N$; no shrinking Fourier band or absolute-value replacement of the full signed spectral functional is used.

The separate physical-space lower bound is consistent with this coefficient. Same-cluster pairs have unfolded difference at most $N\rho_N\to0$; their averaged product is at least $\|b\|_2^2/(2N)$. Retaining the $1/2!$ factor and using $\sum_a m_a^2\ge N^2/p$ gives $M_2\ge\|b\|_2^2(p-1)/4$. The CUE bound $(\int b)^2/2$ is dimension-independent. This reproduces the stated lower bound without any sign error.

## 10. Exact wording issue and concrete correction

The initial companion title was “An obstruction with no dark sector, no exact spectral resonances, and almost flat short powers.” If “no exact spectral resonances” is read as excluding all multiplicative relations, it is false for this construction.

For every $j+2<N$,

$$
2\cdot2^j-3\cdot2^{j+1}+2^{j+2}=0.
$$

Since each base eigenvalue has $p$-th power one, the displayed perturbed eigenvalues satisfy exactly

$$
\widetilde\lambda_j^{\,2p}\widetilde\lambda_{j+2}^{\,p}
=\widetilde\lambda_{j+1}^{\,3p}.
$$

This relation has equal total degree on the two sides, so it persists under a common rotation of the spectrum. With the stated ordering of the base eigenvalues, indices $0,1,2$ all have base eigenvalue one; its multiplicity is $p$. Thus already

$$
\widetilde\lambda_0^2\widetilde\lambda_2=\widetilde\lambda_1^3.
$$

These relations do not identify two different nontrivial ordered ratios, do not create a scalar power, and do not cancel any binary subset polynomial in the minor proof. They distinguish the valid pairwise and subset nonvanishing conclusions from a stronger all-orders resonance claim.

**Concrete correction, now applied:** the title phrase was replaced by “distinct nontrivial eigenvalue ratios,” the introductory hypothesis was stated in those precise terms, and §3.1 now explicitly records the retained higher integer relation. I reread these changes and verified the amended source hash. The mathematical construction and the explicit theorem need no change. A different choice of dither would be needed to exclude these higher relations; that would be a new construction and is not required for the selected-input counterexample audited here.

The first base revision also had a display typo “sum” in its trace formula. The audited updated revision has the correct $\sum$ and includes the full CUE normalization. Neither change affects the substantive proof.

No other mathematical correction was identified. In particular, demanding a quantitative lower bound for the intensity matrix would add a hypothesis that these notes do not claim.

## 11. Exact checks, source revisions, and remaining scope

The independent script r7_audit_countermodel_checks.py passed **351,788 exact assertions**. It checks the raw group law, completed-square identity, Gauss norms, full reversal phase, reverse-edge orthogonality, traces, and base renewal coefficients at primes $5,7,11$. Character sums are handled as integer coefficient vectors modulo the prime cyclotomic polynomial, with no floating-point exponential.

It also checks ordered binary differences on indices $0,\ldots,63$, all subset exponents on fourteen indices at positive and negative nonzero powers, and the return-tail constants at primes through 31. Those finite checks supplement the universal algebraic arguments. They do not construct the extremely close generic matrix $H$, numerically test transcendence, or attempt to observe the late return tail.

Reproduction:

    python research_round7_2026_10_21/r7_audit_countermodel_checks.py

The complete check record is r7_audit_countermodel_checks.md. The checker SHA-256 is

f0cd9841244806cd11ac9b8f7e62371b36245a3a25220e41c3a3dea46ddc24af.

| Source | Inspection | SHA-256 |
| --- | --- | --- |
| Spectral_research_master.md | Original periodization and CUE reference normalization; base revision verified | 3534e4d7aa97c2f8621050248652363c639aeedf723f8b7fe7a971dc01ac2302 |
| root_unipotent_flat_clock.md | Complete initial proof, amended trace/CUE section, and verified presentation-only correction | 8f8e4cdbcd5c6576eb6bb9ce976d7a29ae4e77a310271576719ee8e39ad9d0bd |
| r7_return_generic_microperturbation.md | Complete raw perturbation proof, then corrected title, introduction, and §3.1 scope paragraph | 1127ad366de39f1c9293bb54fa4fe9ca88183e3baf44d355262f031d73b6cb34 |

The first base-file revision read had SHA-256 6f5720a26157b041e53576917f7bb59858f3769ea00fb0ef11b03cb3db4f83ca; the initial perturbation revision had SHA-256 ca51f83b6cf7d3e48cb1495d42f1cdc8f87e1dc845bb806326f2001e0fada781. The amendments were reread and the final hashes above were independently checked. The external transcendence source was read directly at arXiv:2112.05004v2, page 1, Theorem 1.1.

After the mathematical audit, the base file's SHA-256 changed from 5be806bed97adb3fa2448d0b389713e7cfd194848c41c3db897bf986e90d5366 to the final hash above solely because a form-feed control byte followed by “rac” at line 145 was restored to the literal TeX command \frac. Reversing that single byte-level correction reproduces the preceding hash exactly. This changes presentation only; no mathematical formula or audit verdict changes. The unchanged exact checker was rerun to record the final source hashes, without broadening its tests.

**Remaining gap for the explicit selected-input countermodel theorem: none identified.** The broad resonance wording has been restricted as described in §10. The safe conclusion is that the exact listed qualitative properties and growing short-power bounds do not force the signed pair functional to vanish. The conclusion does not cover quantitative eigenvector-intensity lower bounds, quantitative return contraction, all-orders spectral nonresonance, or the original Weyl family.
