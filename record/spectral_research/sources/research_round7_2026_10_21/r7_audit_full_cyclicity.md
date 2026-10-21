> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round7_2026_10_21/r7_audit_full_cyclicity.md`. Embedded SHA256: `53c7574eee6fd640c7d82492146ed0b0b520e824150f673ec234b7b5b27946ee`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/algebra.md).

# Independent audit: full coordinate cyclicity by a Laurent unit

Audit date: 21 October 2026. Auditor: r7_physical_audit.

## Verdict and precise scope

**PROVED as stated. No mathematical correction is required.** The argument establishes that, for every odd $N\ge3$ with $7\nmid N$, every physical coordinate is observable and cyclic for
$$
U_N(z)=e^{izNA_N}M_N
$$
at every nonzero algebraic complex $z$. In particular, every eigenvector has full physical support at the original real parameter $\tau=10^{-80}$.

This verdict comes from reconstructing the argument and its necessary arithmetic inputs, not from the authors' conclusions or earlier auditors' verdicts. The algebraic factor argument also received a separate skeptical crosscheck. No additional numerical tests were used: the asserted result is exact, and the proof checks below address its actual possible failure points.

The conclusion is qualitative. It gives no uniform positive lower bound for individual coordinates, no assertion for $7\mid N$, and no eigenvalue-ratio independence or local spectral statistics. Large positive and negative real time certify a nonzero exponential polynomial; they do not replace the prescribed phase by a limiting or averaged parameter.

## 1. Pinned sources

All four local sources below were inspected directly. Only the parts identified in the dependency column are used in this audit.

| ID | Source | SHA-256 | Necessary dependency |
|---|---|---|---|
| S1 | research_round7_2026_10_21/r7_original_full_cyclicity_laurent_unit.md | 214c77697b087b6457a76272b0665072b7b6d7f1f72e5eca857876f2f3f9cf17 | The theorem under audit, all sections |
| S2 | research_round7_2026_10_21/r7_original_two_endpoint_layers.md | 905b6a795eb90fa5462cf2a3542804696ee6804ce0ef3387df78e609b1fd97e5 | Sections 2–3 and 7: bordered minors; Section 5: real-time spectral scales and normalized eigenvectors |
| S3 | research_round2_2026_10_20/arithmetic_padic_jacobi_simplicity.md | f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df | Sections 2–6: exact Jacobi gauge, valuation bounds, all overlap minors |
| S4 | research_round6_2026_10_21/round6_main_report.md | 473b7b5b700a8ff17801eb9ca422c5949be15d0551c252e0b4035997db54b2bf | Section 1: original matrices and modular conventions |

S2's separate claims about top Jacobi eigenspaces and its older partial coordinate rank conclusions are not inputs to the new proof. S3's later commutant argument is not needed either.

The sole external transcendence input was checked in the author's primary PDF: S. A. Popescu, *A Simple and Self-contained Proof for the Lindemann–Weierstrass Theorem*, arXiv:2306.14352v2, Theorem 3.2, printed page 14, <https://arxiv.org/pdf/2306.14352v2>. It states the required linear independence over the algebraic numbers of exponentials with distinct algebraic exponents.

## 2. The arithmetic dependency really supplies the required bordered minors

Put $h=(N+1)/2$, $x_j=h+j\bmod N$, and $\omega=(-3+4i)/5$. Using the original modular inverse of 2 gives
$$
h+h\equiv1\pmod N,\qquad
L=200D^{-1}P^*A_NPD,\qquad D_{jj}=\omega^j.
$$
The matrix $L$ is a real symmetric Jacobi path with
$$
d_j=200V(x_j/N),\qquad b_j=r((j+1)/N)>0
\quad(0\le j<N-1).
$$
The closing edge vanishes. Here the hypothesis $7\nmid N$ is essential: on the odd grid the zeros of $r(y/N)$ satisfy $N\mid7y$, so there is exactly one zero edge under that hypothesis. Endpoint recurrence then proves simple spectrum; all eigenvalues and a normalized eigenbasis are algebraic. The original $A_N$ is Hermitian, and the modular cat kernel makes $M_N$ unitary.

At the two conjugate places above 5, normalized by $v_\pm(5)=1$,
$$
v_+(\omega)=1,\quad v_-(\omega)=-1,\qquad
v_\pm(d_j)\ge0,\quad 0\le v_\pm(b_j)\le\tfrac12.
$$
These bounds also hold when $5\mid N$. Indeed, for $\eta=e_N(y)$,
$$
r(y/N)=-\frac{(\eta^7-1)^2(\eta+1)^2}{4\eta^8};
$$
the odd-order root $\eta$ makes $\eta+1$ a unit, and a primitive $5^a$-root has $v(1-\eta)=1/(4\cdot5^{a-1})$.

For an eigenvector normalized at the initial endpoint, its $j$-th component is $p_j(\mu)/\prod_{r<j}b_r$, where $p_j$ is monic with valuation-integral coefficients. Alternant divisibility by the Vandermonde gives the minor estimate relative to the first $k$ rows:
$$
v\!\left(\frac{\det\Phi_{J,E}}{\det\Phi_{[0:k-1],E}}\right)
\ge-\tfrac12\left(\Sigma J-\tfrac{k(k-1)}2\right).
$$
The reference minor is nonzero. Reversing the path gives the corresponding estimate relative to the final $k$ rows. No eigenvalue difference is assumed to be a valuation unit: its Vandermonde factor cancels before the integral quotient is estimated.

In path coordinates $M_0=P^*M_NP$ is a Fourier kernel up to root-of-unity row and column factors, with cross coefficient $4^{-1}\bmod N$. Thus its nodes are distinct for every allowed odd $N$. Any Fourier alternant is its Vandermonde times an integral symmetric polynomial. Consecutive rows minimize the Vandermonde valuation: for $N=5^e n$, $(n,5)=1$, that valuation is a positive combination of collision counts modulo $n,5n,\ldots,5^{e-1}n$, and consecutive sets minimize each count by balanced occupancies. The scalar $N^{-k/2}$ cancels in ratios even in the ramified case.

These estimates justify S3's unique dominant term proof for every square minor of $B=Q^*M_NQ$. The extreme term uses final Jacobi rows on the left and initial rows on the right. A competing term at total index distance $g\ge1$ incurs gauge valuation $g$, loses at most $g/2$ through the Jacobi factors, and loses nothing through the Fourier factor. Its relative valuation is therefore at least $g/2>0$.

The bordered determinant needs the stronger estimate in S2, Section 7. Before normalization its exact expansion is
$$
\sum_{\substack{|I|=|J|=k-1\\ j\notin J}}
\epsilon(J,j)\det\Phi_{I,F}\det(M_0)_{I,J}
\det\Phi_{J\cup\{j\},E}\,
\omega^{j+\Sigma J-\Sigma I}.
$$
For $j<k$, the extreme pair is
$$
I_0=\{N-k+1,\ldots,N-1\},\qquad
J_0=\{0,\ldots,k-1\}\setminus\{j\}.
$$
Its Fourier determinant deletes one column from $k$ consecutive columns. Writing $\ell=k-1$, its excess over the consecutive-column Vandermonde has valuation
$$
\delta=v\!\left({\ell\brack j}_q\right)\le\tfrac14.
$$
This estimate was checked from the product formula, not assumed from the usual consecutive-minor bound. More explicitly,
$$
\delta=\sum_{s=0}^{e-1}\alpha_s
\left(
\left\lfloor\frac{\ell}{n5^s}\right\rfloor
-\left\lfloor\frac{j}{n5^s}\right\rfloor
-\left\lfloor\frac{\ell-j}{n5^s}\right\rfloor
\right),
$$
where $\alpha_0=1/(4\cdot5^{e-1})$, $\alpha_s=5^{s-e}$ for $s\ge1$, and $\sum_s\alpha_s=1/4$. Each bracket is 0 or 1. All product factors have exponent strictly below $N$, so none vanishes. When $5\nmid N$, $\delta=0$.

A competing bordered summand consequently has relative valuation at least
$$
g-\frac g2-\delta\ge\frac14>0.
$$
At $v_-$, reversing the two endpoint choices proves the same assertion for $j\ge N-k$; the sign of the gauge exponent reverses together with $v_-(\omega)$. Endpoint normalization factors are nonzero and cancel as row/column factors. The case $k=1$ at an endpoint is the elementary nonvanishing endpoint component.

The union of these two ranges is exactly $k\ge d(j)+1$, where $d(j)=\min(j,N-1-j)$. The calculation holds for every eigenvector set $E,F$, so reversing eigenvalue order is legitimate. This is precisely S1's needed input (1.2).

## 3. Both real-time limits, including eigenvector normalization

Order $a_1>\cdots>a_N$, and write $V(s)=e^{sA_N}M_N$. Let $b_k=\det B_{[1:k],[1:k]}\ne0$. At the scale $X=e^{sa_k}Y$, the characteristic-polynomial terms of adjacent degrees $k-1,k$ have the largest exponential rate. Successive rate differences are $a_\ell-a_k$, so no independence of subset sums is needed. The limiting polynomial has the simple nonzero root $Y=b_k/b_{k-1}$. Rouché's theorem on a small circle around this root yields
$$
\lambda_k(s)=e^{sa_k}(b_k/b_{k-1}+o(1)).
$$
The $N$ scales have distinct magnitudes for large positive $s$, giving simple spectrum there.

For the right eigenvector, the head block tends to the invertible $B_{[1:k-1],[1:k-1]}$; the tail block divided by $\lambda_k(s)$ is small. The resulting two inequalities bound the head by the central coordinate plus the tail, and the tail by a vanishing multiple of the head plus the central coordinate. They show that the central coordinate cannot be zero. After setting it equal to 1, the eigenvector converges to
$$
(-B_{I,I}^{-1}B_{I,k},1,0,\ldots,0),\qquad I=\{1,\ldots,k-1\}.
$$
Its physical $x_j$-coordinate is the bordered determinant divided by $b_{k-1}$. Thus every scale $k\ge d(j)+1$ is visible throughout a sufficiently distant positive tail.

For the negative tail, write $s=-t$ and apply the argument to $-A_N$. Since the bordered assertion holds for all eigenvector sets, the possible invisible scales in the original ordering are now only the final $d(j)$ values. All limiting constants used here are nonzero; no positivity of those complex constants is needed.

## 4. Laurent normality, invariant factors, and specialization

The group $\Gamma=\sum_i\mathbb Z a_i$ is finitely generated and torsion-free, hence free. Its rank can be smaller than $N$. The faithful exponential realization of
$$
\mathcal R=\overline{\mathbb Q}[\Gamma]
\simeq\overline{\mathbb Q}[t_1^{\pm1},\ldots,t_r^{\pm1}]
$$
follows by a distinct-frequency Vandermonde argument. Localization of a polynomial UFD gives a UFD, hence an integrally closed domain. The units are exactly $c e^{s\beta}$: in the real frequency ordering, the maximal and minimal product frequencies have unique noncancelling terms, so widths add and a product equal to 1 forces both factors to have one term.

If the observability determinant vanished identically, over $\mathcal K=\operatorname{Frac}\mathcal R$ its kernel $W$ would have dimension $q>0$. Cayley–Hamilton makes $W$ invariant, and invertibility of $V$ makes its restriction invertible. Completing a $\mathcal K$-basis gives monic factors $F,G\in\mathcal K[X]$ of the characteristic polynomial.

Every characteristic root is integral over $\mathcal R$. Coefficients of either monic factor are symmetric sums of a submultiset of those roots, hence integral; their membership in $\mathcal K$ and normality imply $F,G\in\mathcal R[X]$. Since
$$
F(s,0)G(s,0)=(-1)^N\det M_N\,e^{s\operatorname{Tr}A_N}
$$
is a unit, each constant term is a unit. Therefore $F(s,0)=c e^{s\beta}$ for one fixed real $\beta\in\Gamma$.

This argument does not assume that $W$ is a free or projective module over $\mathcal R$. Only its vector-space basis over $\mathcal K$ is used.

For a precise specialization check, write the completed basis as $P=H/D$, with $H$ a matrix over $\mathcal R$, $D\ne0$, and $\det H\ne0$. Each nonzero real-frequency exponential polynomial is nonzero in both sufficiently distant real tails by its extreme-term asymptotic. Thus $D(s)$ and $\det H(s)$ are eventually nonzero at both ends. The block-triangular conjugacy identities and the output-annihilation identities specialize there. In particular, $F(s,X)$ remains the characteristic polynomial of a $q$-dimensional invisible invariant subspace, with the same degree at both ends.

At simple spectrum an invariant subspace is a sum of eigenlines, as follows by applying polynomial spectral projections. Therefore $q\le d=d(j)$. Passing to a fixed-subset subsequence at each end is sufficient and gives
$$
\beta=\sum_{i\in I_+}a_i=\sum_{i\in I_-}a_i,
\quad
I_+\subset\{1,\ldots,d\},\quad
I_-\subset\{N-d+1,\ldots,N\},\quad |I_\pm|=q.
$$
Dividing $\log|F(s,0)|$ by negative $s$ at the negative end produces the same $\beta$; no sign changes the required equality. If $d=0$, $q>0$ is already impossible. Otherwise $2d\le N-1$ and
$$
\sum_{i\in I_+}a_i\ge q a_d
>q a_{N-d+1}\ge\sum_{i\in I_-}a_i.
$$
This is the contradiction. It uses strict ordering and equal cardinalities only, allowing arbitrary additive relations among the individual eigenvalues.

## 5. Exact algebraic phase and the cyclicity conclusion

The nonzero observability determinant is a finite exponential sum with algebraic coefficients. Collect equal frequencies first. For nonzero algebraic complex $z$, multiplication by $iNz$ takes its distinct algebraic frequencies to distinct algebraic exponents. The verified Lindemann–Weierstrass statement therefore applies and rules out a zero determinant at $s=iNz$.

Finally, the exact original identities $A_N^*=A_N$ and $M_N^*=M_N^{-1}$ give
$$
U_N(z)^*=U_N(\overline z)^{-1}.
$$
The adjoint observable matrix at $\overline z$ has columns $U_N(z)^{-k}e_{x_j}$. Multiplication by $U_N(z)^{N-1}$, followed by reversal of columns, gives the cyclic matrix at $z$, preserving full rank. A hypothetical eigenvector with zero $x_j$-coordinate would be annihilated by every observable row, a contradiction.

All hypotheses needed for both conclusions are present in the exact original family. No repair, extra genericity assumption, arithmetic subsequence, or limiting change of $\tau$ is required.
