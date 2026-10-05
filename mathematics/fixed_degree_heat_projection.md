# Every fixed neutral trace degree contributes a vanishing heat defect

**Claim ID: BGS-FLOW-019. Status: project proof with independent internal review of the new implications.**
5 October 2026. This is an actual-map partial estimate, not deterministic
noise removal. The Haar stable-range trace moments, finite-dimensional
projection and semigroup mechanisms are prior or standard. The five
character examples in the preceding programme are extended to an entire
fixed neutral trace filtration, without a rational-character assumption.

## 1. Exact theorem

For full normalized Brownian motion on $U(N)$ use $P_t$ and $G_N$ of
FLOW-015. Fix an integer $Q\ge0$. Let $\mathcal H_{Q,N}$ be the complex
span of the constant and trace monomials

$$
W_{\boldsymbol m}(U)=\prod_jp_{m_j}(U),\quad m_j\ne0,\qquad
\sum_{m_j>0}m_j=\sum_{m_j<0}|m_j|\le Q.
\tag{P1}
$$

Repetitions are factor multiplicities; sorted tuples index the monomials.
Let $\mathsf P_{Q,N}$ be Haar-$L^2$ orthogonal projection onto this span.
If $N\ge\max(3,2Q)$, $|p_m(A_N)|\le K$ for $1\le m\le Q$, and
$F_N$ is any smooth conjugation- and rotation-invariant function with
$\|F_N\|_{L^2({\rm Haar})}\le1$, then for $0\le t\le1$,

$$
|(P_t-I)\mathsf P_{Q,N}F_N(A_N)|\le C_{Q,K}t.
\tag{P2}
$$

The constant is independent of $N$ and $F_N$. The case $Q=0$ gives
zero exactly. No uniform bound as $Q$ grows is asserted.
The projection commutes with $P_t$, so the remaining defect is exactly

$$
(P_t-I)F_N(A_N)
=(P_t-I)\mathsf P_{Q,N}F_N(A_N)
+(P_t-I)(I-\mathsf P_{Q,N})F_N(A_N).
\tag{P3}
$$

In particular, FM-013 and $0\le\Phi_{N,f}\le1$ imply P2 for the
unchanged actual map, every fixed $Q$ and every positive compact local
Laplace test, at the existing $t_N\to0$. The second term of P3 remains
open. This is an estimate for a Haar projection of an observable,
not a bound on every Fourier summand at a Heisenberg index.

## 2. Stable Gram matrix and bounded evaluation

The prior Diaconis--Evans Theorem 2.1(a) states that Haar joint trace
moments equal those of independent centered complex Gaussian variables
$Z_m$ with $\mathbb E|Z_m|^2=m$, provided both weighted degrees are at
most $N$. For two words in P1, their Haar Gram entry is the expectation
of $W_{\boldsymbol m}\overline{W_{\boldsymbol n}}$.
Its positive and negative weighted degrees are each at most $2Q$.
Therefore, throughout $N\ge2Q$, the Gram matrix is one fixed matrix
$H_Q$, obtained by the Gaussian rule

$$
\mathbb E\prod_m Z_m^{a_m}\overline{Z_m}^{b_m}
=\mathbf1_{a=b}\prod_m m^{a_m}a_m!.
\tag{P4}
$$

It is positive definite: the distinct sorted words are distinct
polynomials in $Z_1,\bar Z_1,\ldots,Z_Q,\bar Z_Q$, hence in their real
and imaginary parts. A nonzero polynomial cannot vanish almost
everywhere for their strictly positive Gaussian density. Thus the
words really are independent in this stable range; no independence
of trace symbols at growing degree or small dimension is presumed.

There are $d_Q=\sum_{q=0}^Q p(q)^2$ words, with $p(0)=1$.
Writing $\mathsf P_{Q,N}F_N=\sum c_jW_j$, projection gives
$c^*H_Qc\le1$ and consequently
$\|c\|_2\le\lambda_{\min}(H_Q)^{-1/2}$.
At $A_N$, each word has at most $2Q$ factors; the assumed trace bound
gives $|W_j(A_N)|\le\max(1,K)^{2Q}$. Evaluation on this finite span
is therefore uniformly bounded in the coefficient norm.

The exact external input is EXT-DE-2001, checked in the existing
[source record](../literature/signed_heisenberg_sources.md), Theorem
2.1(a), printed pp.3--4. Its Gaussian formula is used only in the
stable range $2Q\le N$, not for degrees of order $N$.

## 3. Generator invariance and commuting projection

FLOW-015 D5 preserves the positive weighted degree under splitting and
same-sign merging; opposite-sign merging reduces it. When an index
becomes zero it is removed with its factor $p_0=N$.
Its prefactor $1/N$ then cancels that factor. Consequently
$G_N\mathcal H_{Q,N}\subset\mathcal H_{Q,N}$, and its matrix in the
sorted-word basis has coefficients of the form $a+b/N$, with fixed
real numbers $a,b$ depending only on $Q$. The number of transitions
is finite. Its coefficient operator norm is bounded by a constant
$C_Q$ throughout $N\ge\max(3,2Q)$.

These smooth polynomial functions lie in the generator domain, and
their finite-dimensional generator evolution is $P_t|_{\mathcal H}
=e^{tG_N|_{\mathcal H}}$. One can verify this by uniqueness of the
semigroup equation on the compact group. Since $P_t$ is self-adjoint
for Haar measure, this invariant finite span is reducing: for
$v\perp\mathcal H$ and $w\in\mathcal H$,
$\langle P_tv,w\rangle=\langle v,P_tw\rangle=0$.
Thus $\mathsf P_{Q,N}P_t=P_t\mathsf P_{Q,N}$.

The coefficient difference between $e^{tG_N}\mathsf PF_N$ and
$\mathsf PF_N$ is bounded by
$tC_Qe^{C_Qt}\lambda_{\min}(H_Q)^{-1/2}$.
Combining this with the evaluation bound proves P2 and the exact
decomposition P3. Full and traceless Brownian motion agree on these
charge-zero observables; no determinant mode is silently included.

## 4. Local CUE self-averaging and the actual projected statistic

There is a stronger local corollary. Let $F_N$ be either the uniform-origin
positive compact Laplace statistic, or a fixed compact continuous factorial
test statistic of order $k$, as in C11 of FLOW-017. If $V_N$ is Haar CUE,
then, with $b_N=\mathbb EF_N(V_N)$,

$$
\mathbb E|F_N(V_N)-b_N|^2\le C_F/N.
\tag{P5}
$$

**Proof of P5.** First take $N>8R$ for the support radius below;
the finitely many smaller dimensions are absorbed into $C_F$.
The unfolded CUE kernel has diagonal one and, in magnitude,

$$
|K_N(x,y)|\le1,\qquad
|K_N(x,y)|\le[2\operatorname{dist}_N(x,y)]^{-1}.
$$

The second bound uses $N|\sin(\pi(x-y)/N)|\ge2\operatorname{dist}_N(x,y)$;
the numerator is at most one. Let the local observable be $\varphi$, with
support window $[-R,R]$, and let $d=\operatorname{dist}_N(0,s)$.
For $d>4R$, the two windows are disjoint. For a factorial statistic the
covariance is the integral of its two weights against
$\det K_{2k}-\det K_k\det K_k$. Every non-block-diagonal permutation
has at least two cross-window entries, each at most $C_R/d$; all other
entries have magnitude at most one. It follows that
$|\operatorname{Cov}(\varphi,\overline{\varphi\circ T_s})|\le C_F/d^2$.
For $d\le4R$, the count moment of order $2k$ bounds the covariance.
CUE factorial densities are at most one by Hadamard and positivity,
so these fixed-window count moments are bounded independently of $N$.

For a Laplace statistic, expand the two disjoint-window Fredholm series
with $h=1-e^{-f}$ and $H=\int h$. At total size $n=k+l$, replace the
cross blocks of the correlation matrix by $z$ times those blocks.
Its determinant has first derivative zero at $z=0$. Taylor's formula
and two differentiated cross entries bound its block-factorization
error by
$C d^{-2}n^4\max(1,(n-2)^{(n-2)/2})$. The remaining minors have entries
of magnitude at most one for $0\le z\le1$. After integrating weights,
the majorant sums because

$$
\sum_{n\ge2}\frac{(2H)^n}{n!}
n^4\max(1,n^{n/2})<\infty.
$$

This gives the same covariance bound; nearby-window covariance is bounded
since $0\le\varphi\le1$. CUE rotation invariance makes the field stationary.
For its exact period-$N$ origin average,

$$
\operatorname{Var}F_N=\frac1N\int_0^N
\operatorname{Cov}(\varphi,\overline{\varphi\circ T_s})ds\le C_F/N,
$$

proving P5. This proof is a finite determinantal calculation; it requires
neither an ergodic-rate theorem nor independence of distant windows.

Let $A_N$ satisfy the starting trace bound of Section 1. The coefficient
and evaluation bound from Section 2, and Haar-$L^2$ contractivity, give
uniformly for **every** $t\ge0$,

$$
|\mathsf P_{Q,N}F_N(A_N)-b_N|\le C_{Q,K,F}N^{-1/2},\qquad
|P_t\mathsf P_{Q,N}F_N(A_N)-b_N|\le C_{Q,K,F}N^{-1/2}.
\tag{P6}
$$

Apply the same evaluation bound to the projection of $F_N-b_N$, whose
Haar norm is at most $C_F^{1/2}N^{-1/2}$; the constant is in the span,
and $P_t$ commutes with the projection. P2 can similarly be sharpened
to $C_{Q,K,F}tN^{-1/2}$ for the projected defect when $0\le t\le1$.
For fixed Schwartz factorial tests, truncate in space and use the CUE
uniform count moments and tiled $L^2$ tails from FLOW-017. This proves
P5 with $o(1)$ in place of $C_F/N$ and P6 with $o(1)$ in place of
$C_{Q,K,F}N^{-1/2}$; no Schwartz rate is asserted here.

For the actual $U_N$, FM-013 supplies every fixed starting trace bound.
Thus every fixed-degree projected local statistic already tends to the
correct CUE/Sine expectation, at time zero as well as after heat evolution.
The projection is an algebraic approximation of the observable; this is
not convergence of the actual unprojected local statistic. In particular,

$$
F_N(U_N)-b_N=(I-\mathsf P_{Q,N})F_N(U_N)+o_Q(1).
\tag{P7}
$$

The complementary point evaluation is the remaining deterministic
obligation. P7 alone places no small bound on it.

## 5. What this rules out and what remains

The remaining evaluation cannot be inferred from its small Haar norm,
even for the actual positive local Laplace observable. Fix nonzero
$0\le f\in C_c^\infty$ with support width below one, and fix $Q$.
Write $R_{Q,N}=(I-\mathsf P_{Q,N})\Phi_{N,f}$. Then

$$
\|R_{Q,N}\|_{L^2({\rm Haar})}\le C_fN^{-1/2},\qquad
R_{Q,N}(C_N)\longrightarrow-\delta_f<0,
\quad \delta_f=\Phi_{\rm Sine}(f)-(1-a_f),\quad
a_f=\int(1-e^{-f}).
\tag{P8}
$$

The norm bound follows since the projection contains constants and P5
bounds $\|\Phi-b_N\|_2$. The initial clock value is exactly $1-a_f$;
P6 gives $\mathsf P_Q\Phi(C_N)-b_N=O_Q(N^{-1/2})$ because the fixed
clock traces vanish. The strict inequality $\delta_f>0$ and its explicit
lower bound are proved in FLOW-015 D15--D16. This proves P8 and a
point-evaluation amplification at least $c_{Q,f}\sqrt N$ on these
complements. It is a statement for a particular local Laplace test,
not just a global character. It is not a heat-inverse norm estimate.
At $t_N\to0$, $Nt_N\to\infty$, the same complement has heat defect
tending to $\delta_f$, using FLOW-007 and P2. Small Haar-$L^2$ norm
does not close the actual deterministic complementary estimate.

All fixed neutral trace degrees are harmless at a vanishing noise time
for the actual map. The growing-degree complement is the remaining
part of this particular decomposition. No dimension-uniform small
norm of that complement at $A_N$ follows from the Haar-$L^2$ bound.
Nor does P2 license exchanging $Q\to\infty$ with $N\to\infty$.

The flat-clock falsifier of FLOW-015 is compatible with this theorem:
its fixed starting traces are bounded and every fixed projected defect
vanishes, but its complete local heat defect has a positive limit.
FLOW-018 additionally exhibits explicit low-band local pair tests whose
unprojected defect is nonzero at $Nt\asymp1$ or larger. A successful
actual-map continuation must control the complementary term in P3,
or obtain a different signed Heisenberg estimate. TRACE-005 and full
BGS remain open.

The companion finite check verifies stable Gram positivity, generator
closure and self-adjointness for explicitly listed degrees and dimensions.
These controls do not prove the all-$Q$ statement or certify BGS. The
proof above and its prior stable-range input supply those implications.
