> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/audit_final_monomial_interpolation_summary.md`. Embedded SHA256: `6eba5f5c9899f0a5519a99816e0c83c70871caf549e0de07af6b571668ba9879`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Final independent audit: arbitrary-phase monomial symmetries, interpolation, and Russian synthesis

Date: 21 October 2026.

## Verdict and exact scope

**PASS: no mathematical gap or counterexample was found in the frozen monomial theorem, the complex interpolation test, or their statements in the frozen Russian synthesis identified below.** This is a structural and method-boundary audit. It is not a proof of the original family's $H_{\rm diag}$, whose first specified pair test remains unresolved.

The monomial proof was reconstructed directly from the exact modular Weyl matrices and the quadratic kernel. The decisive arguments below do not use earlier PASS reports as mathematical premises. In particular, the unknown coordinate phases are allowed to be transcendental, the lifted local solution is not assumed unitary, and composite odd moduli are handled without inverting $3$.

Audited source snapshots:

| Source | SHA-256 |
|---|---|
| research_round3_2026_10_21/arithmetic_monomial_reversal_closure.md | 38462ab5c59f850c507b578b9b63092c452e427b48cdf3812a863434bb3a72f9 |
| research_round3_2026_10_21/phase_complex_interpolation_test.md | 724273439eb34d7536ac592e67de56d260a7dc46b20c40031eae77e088236216 |
| Spectral_research_2026-10-21.md | 241e694be03f59d2de3223c3e97d015c81d3d9e99fa63572763637724baa8cfb |
| research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md, exact definitions in Section 2 | 42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b |
| research_continuation_2026_10_20/finite_identities_and_closure.md | e1d85ef8ecff65a1fecffe200185d9e721dce14f9c356705cc04f5c97ffd6d35 |

The monomial source's published theorem input was checked against the author's primary text, S. A. Popescu, *A Simple and Self-contained Proof for the Lindemann-Weierstrass Theorem*, Theorem 3.2, https://arxiv.org/pdf/2306.14352. Its statement is precisely linear independence, over algebraic numbers, of exponentials of distinct complex algebraic numbers. No stronger transcendence conjecture is used.

## 1. Exact family and threshold

Use the source's frequency order $(k,l)$:
$$
W(k,l)=T_N(l,k),\qquad
(T_N(a,b)u)(x)=e_N(b(x+\overline2a))u(x+a),
$$
$$
M_{xy}=N^{-1/2}e_N[-\overline8(3x^2-2xy+3y^2)].
$$
All fractions in these formulas are modular. Direct character summation proves unitarity of $M$; the displayed kernel is symmetric. Hence $\overline M=M^{-1}$.

The original coefficient polynomial is
$$
f(q,p)-\frac1{10}
=\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}-\frac1{10}
+\frac{r(q)\cos(2\pi p-\alpha_0)}{100},
$$
where $r=(1-\cos14\pi q)(1+\cos2\pi q)$ and
$e^{i\alpha_0}=(-3+4i)/5$. Its coefficients define $A$ through the modular $W(k,l)$, without replacing the modular half by a real half. Consequently all entries of $A,M$ are algebraic, and $A=A^*$.

The relevant Fourier coefficients of $r$ are
$$
r_0=1,\quad r_{\pm1}=\frac12,\quad r_{\pm7}=-\frac12,
\quad r_{\pm6}=r_{\pm8}=-\frac14.
$$
The only shift rows of $A$ are $l=0,\pm1$. For every $N\ge11$,
$$
c_A(0,1)=\gamma=\frac{-3-4i}{1000},\qquad
c_A(0,-1)=\overline\gamma.
$$
There is no alias into $r_0$, because the largest nonzero frequency of $r$ is $8<N$. It is unnecessary to assume that all other Fourier coefficients remain unaliased.

This explains why the new threshold $N\ge11$ is safe. The remaining modular support arguments below only exclude $N\mid3$ and $N\mid8$, and the nonzero diagonal obstruction only needs the explicit positive value of $r(1/N)\sin(2\pi/N)$. No old threshold such as $N\ge75$ is required here.

## 2. Rank rigidity with arbitrary unknown phases

Fix real algebraic $c$, nonzero real algebraic $z_0$, and
$$
U_c(z)=e^{icNzA}M e^{i(1-c)NzA}.
$$
For distinct eigenvalues $\lambda$ of $A$, the spectral projection
$$
\Pi_\lambda=\prod_{\mu\ne\lambda}\frac{A-\mu I}{\lambda-\mu}
$$
has algebraic entries. All eigenvalues are algebraic as well. Thus every entry of $U_c(z)$, of its inverse, and of
$$
U_c^\flat(z)=e^{-icNz\overline A}\overline M
e^{-i(1-c)Nz\overline A}
=\overline{U_c(\overline z)}
$$
is a finite sum $\sum b_j e^{\lambda_j z}$ with algebraic $b_j,\lambda_j$. The last function is holomorphic; ordinary conjugation at a complex parameter would not have this property.

After equal exponents are grouped, Lindemann-Weierstrass gives
$$
F(z_0)=0\quad\Longleftrightarrow\quad F\equiv0
$$
for every such exponential polynomial. Products and matrix minors belong to the same class. In particular, every nonzero algebraic parameter has the maximal possible rank of any rectangular matrix of such entries. The argument requires no rational independence among the slopes.

### 2.1 Projective factor

Cyclicity gives
$$
p(z)=\operatorname{Tr}U_c(z)=\operatorname{Tr}(e^{iNzA}M).
$$
At zero,
$$
p(0)=N^{-1/2}\sum_xe_N(-\overline2x^2).
$$
For odd $N$, the substitution $u=x-y,\ v=x+y$ is a bijection. Therefore
$$
|p(0)|^2=\frac1N\sum_{u,v}e_N(-\overline2uv)=1.
$$
This is an exact proof for every odd composite modulus, not only a prime Gauss-sum formula.

Since $p(0)\ne0$, the exponential-polynomial evaluation property gives $p(z_0)\ne0$. The trace of an antiunitary conjugate is $\overline{p(z_0)}$; the trace of the inverse is also $\overline{p(z_0)}$, because $U_c(z_0)$ is unitary. Thus any scalar $\eta$ in the proposed projective reversal equals $1$. The same trace argument forces $\eta=1$ for a projective unitary commutant. No algebraicity of $\eta$ is needed.

### 2.2 Homogeneous system

For a fixed permutation $\pi$, write
$$
J_d=\operatorname{diag}(d_x)P_\pi,\qquad
(P_\pi u)(x)=u(\pi(x)).
$$
The reversal equation is the homogeneous linear system
$$
J_dU_c^\flat(z)-U_c(z)^{-1}J_d=0.
$$
It has $N$ unknowns and $N^2$ scalar equations. The unknown $d_x$ do not occur in the coefficients of its system matrix $B_\pi(z)$. Therefore their possible transcendence is irrelevant to the exponential-polynomial assertion for the maximal minors.

A nonzero solution at $z_0$ makes every $N$-column maximal minor vanish there. Each such minor vanishes identically. Hence
$$
\operatorname{rank}B_\pi(z)\le N-1
$$
for all complex $z$. The identical reasoning applies to the unitary commutant system $J_dU_c-U_cJ_d=0$.

## 3. Complete classification at zero and the analytic lift

At zero the reversal system says that $J_d$ commutes with $\overline M=M^{-1}$, equivalently with $M$. The commutant system directly says the same. For either symmetric matrix $F=M,\overline M$, reindexing its column yields
$$
d_xF_{\pi(x),\pi(y)}=d_yF_{x,y}.
$$

There is a small but essential issue here: the kernel vector obtained at zero is not initially known to have unit-modulus or even nonzero coordinates. The flat, nonzero kernel entries resolve it. If one $d_y\ne0$, every $d_x\ne0$.

The ratio $d_x/d_y$ is then an $N$-th root of unity. Swapping $x,y$ and using symmetry of $F$ makes the same ratio its own inverse. Since $N$ is odd, all these ratios equal $1$. Thus the kernel consists of constant diagonal vectors whenever it is nonzero.

Preservation of the quadratic phase gives, first on the diagonal and then after subtracting the squared terms,
$$
\pi(x)^2=x^2,\qquad \pi(x)\pi(y)=xy\pmod N.
$$
Let $a=\pi(1)$. Then $a^2=1$, so $a$ is a unit, and the second identity gives $\pi(x)=ax$. Conversely such a permutation preserves the kernel. This proves the entire classification, including every CRT involution and excluding affine translations with a nonzero offset. No cancellation by a possibly nonunit residue was used.

For each permissible $\pi=P_a$, the kernel at zero has dimension exactly one and is spanned by $(1,\ldots,1)$. Delete column zero: the other $N-1$ columns are independent, since no nonzero constant kernel vector has coordinate zero equal to zero. Select $N-1$ independent rows on those columns, set $d_0(z)=1$, and solve analytically for the other entries near zero. The selected rows remain independent; global rank at most $N-1$ then forces every other row to vanish too.

This produces an invertible analytic local solution
$$
J(z)=F(z)P_a,\qquad F(0)=I,
$$
with diagonal $F$. It is neither necessary nor asserted that this solution is unitary, or that it analytically continues the originally postulated vector at $z_0$. Its derivative
$$
Q=F'(0)/(iN)
$$
is an arbitrary complex diagonal matrix. The ensuing contradiction uses only its diagonality.

## 4. Independent differentiation and Fourier-support contradiction

Put $A_D=P_a\overline A P_a^{-1}$. Rewrite the local intertwining equation as
$$
F(z)e^{-icNzA_D}M^{-1}e^{-i(1-c)NzA_D}
=e^{-i(1-c)NzA}M^{-1}e^{-icNzA}F(z).
$$
Differentiating at zero, dividing by $iN$, and multiplying on the left by $M$ gives
$$
\operatorname{Ad}_M Q-Q
=c\operatorname{Ad}_M A_D+(1-c)A_D
-(1-c)\operatorname{Ad}_M A-cA.
\tag{A}
$$
This independently verifies all four coefficients and their positions in the source.

For the modular Weyl transport, direct substitution in the two kernels gives
$$
T(a,b)M=MT(3a-4b,-2a+3b).
$$
For example, the relative phases on the two sides are respectively
$$
(b-3a/4)x+(a/4)y+ba/2-3a^2/8,
$$
$$
-(a'/4)x+(3a'/4+b')y-3(a')^2/8-b'a'/2,
$$
which agree at $a'=3a-4b,\ b'=-2a+3b$. This includes their constant terms, so there is no omitted Weyl phase.

In frequency order $(k,l)$,
$$
\operatorname{Ad}_M W(v)=W(Sv),\qquad
S=\begin{pmatrix}3&2\\4&3\end{pmatrix}.
$$
The Weyl matrices form an orthogonal basis. The support lines of diagonal matrices and their $M$-conjugates are
$$
L=\{(k,0)\},\qquad SL=\{(3k,4k)\}.
$$
Their intersection is $\{0\}$, since $4$ is a unit. Therefore
$$
\mathcal D\cap\operatorname{Ad}_M\mathcal D=\mathbb C I.
$$

The exact antiunitary transformation is
$$
P_aK W(k,l)(P_aK)^{-1}=W(-ak,al),
$$
with conjugation of scalar coefficients. Thus $A_D$ has shift rows $l=0,\pm a$.

At $(0,1)$, the left side of (A) vanishes. The input for $\operatorname{Ad}_M A$ would be $S^{-1}(0,1)=(-2,3)$, outside the shift support of $A$. For $\operatorname{Ad}_M A_D$, the corresponding original input has shift coordinate $3a$. The possibility $3a=0$ would imply $N\mid3$, and $3a=\pm1$, together with $a^2=1$, would imply $N\mid8$. These are impossible at the stated threshold. Hence
$$
(1-c)c_{A_D}(0,1)-c\gamma=0.
\tag{B}
$$

The three cases are now exhaustive:

- If $a\ne\pm1$, the $A_D$ coefficient in (B) vanishes, forcing $c=0$. At $(0,a)$, equation (A) then has zero left side, nonzero $A_D$ coefficient $\overline\gamma$, and zero $\operatorname{Ad}_M A$ coefficient. The same $3a$ support argument applies. Contradiction.
- If $a=1$, (B) is $(1-c)\overline\gamma-c\gamma=0$. With $\gamma=u+iv$, its left side is $u(1-2c)-iv$; it cannot vanish for real $c$, because $v=-4/1000$.
- If $a=-1$, (B) forces $c=1/2$. The mixed coefficients are $\gamma r_k$ and $\overline\gamma r_k$ on rows $1,-1$. Conjugation and exchange of these rows leave all of them invariant. The difference is exactly diagonal:
  $$
  W=A_D-A,\qquad W_{xx}=-r(x/N)\sin(2\pi x/N)/50.
  $$
  It has trace zero by oddness and is nonzero at $x=1$. Indeed all three factors $1-\cos(14\pi/N)$, $1+\cos(2\pi/N)$, and $\sin(2\pi/N)$ are positive for $N\ge11$.
  Equation (A) becomes
  $$
  \operatorname{Ad}_M(Q-W/2)=Q+W/2.
  $$
  Both sides belong to the intersection of the two diagonal spaces, so both are scalar. This would make $W$ scalar, and its trace zero would make $W=0$, a contradiction.

This proves the arbitrary-phase monomial antiunitary exclusion exactly as stated.

## 5. Independent check of the unitary commutant corollary

For the commutant equation the same rank and kernel argument gives $J(z)=F(z)P_a$. Set
$$
A_a=P_aAP_a^{-1},\qquad X=A_a-A.
$$
Direct differentiation of $J(z)U_c(z)=U_c(z)J(z)$, followed by right multiplication by $M^{-1}$, gives
$$
\operatorname{Ad}_M Q-Q=cX+(1-c)\operatorname{Ad}_M X.
\tag{C}
$$

If $a\ne\pm1$, the $X$ coefficient at $(0,1)$ is $-\gamma$. If $a=-1$, it is $\overline\gamma-\gamma$. Both are nonzero. The left side and $\operatorname{Ad}_M X$ vanish at this frequency by the same exact support argument. Therefore $c=0$.

At $S(0,1)=(2,3)$, the left side of (C) is still zero: this point is not on $L$, and its preimage $(0,1)$ is not on $L$. The right side has the nonzero coefficient $c_X(0,1)$. Contradiction. The original permutation must be the identity.

The final scalarity argument must concern the original parameter $z_0$, not only the analytic germ at zero. The source correctly supplies it: some rank-$N-1$ minor at zero is nonzero, hence remains nonzero at $z_0$ by the exponential-polynomial lemma. The identity matrix is always a solution, so the diagonal kernel at $z_0$ is exactly one dimensional.

There is an additional direct check of this last step. Every entry $U_c(z)_{xy}$ is an algebraic exponential polynomial and has the nonzero value $M_{xy}$ at zero. Therefore every entry $U_c(z_0)_{xy}$ is nonzero. A diagonal commuting matrix must then have $d_x=d_y$ for every pair $x,y$. This reaches the same conclusion without reference to a local branch.

Finally,
$$
U_c(z_0)=E^{c-1}U_1(z_0)E^{1-c},\qquad E=e^{iNz_0A},
$$
so conjugation transports the excluded monomial classes exactly to the dressed classes $E^{1-c}DE^{c-1}$. This identity is valid for antiunitary $D$ as a composition of operators; it does not require commuting $D$ through $E$.

The restrictions in the manuscript are essential and correctly retained: $c,z_0$ are real algebraic, $z_0\ne0$, $N$ is odd and at least $11$, and the excluded symmetry class is specified. This does not exclude an abstract eigenbasis antiunitary, prove spectral simplicity, or prove $H_{\rm diag}$.

## 6. Independent interpolation audit

Write $\mathcal P(Y)=\sum_\chi P_\chi YP_\chi$,
$B=\mathcal P(E)$, $C=E-B$, $K=BM$, $R=CM$, where $E,M$ are unitary. The source's actual-family inputs are restricted to
$$
N=d^2m,\quad m\le\sqrt N,\quad N\ge10^{140},\quad N\ \text{odd},
$$
with equal sector rank $m$, sector count $Q=d^2$, and all blocks bounded by
$\rho=\sqrt{4095/4096}$. These hypotheses are not asserted for all odd dimensions.

### 6.1 Norm domain and exact sharpness

Since
$$
X(z)=[zE+(1-z)B]M,
$$
the triangle inequality gives
$$
\|X(z)\|\le r_\rho(z):=|z|+\rho|1-z|.
$$
The set $r_\rho<1$ contains $[0,1)$, has $1$ on its boundary, and its tangent interior sector there has half-angle $\arccos\rho=\arcsin(1/64)$. This is an exact guaranteed contraction domain, not a claim that the actual matrices attain its boundary at every point.

The proposed equality example satisfies the full all-block hypothesis. For fixed $z\ne0,1$, choose
$$
c=\rho e^{i(\arg z-\arg(1-z))},\qquad \lambda_0=1.
$$
When $Q(1-\rho)\ge2$, one has $|Qc-1|\le Q-1$. Since $Q-1$ is even, unit numbers in two equal groups symmetric about $\arg(Qc-1)$ can have exactly this sum; the zero case is obtained from equal numbers $i,-i$. Select them as $\lambda_1,\ldots,\lambda_{Q-1}$ and set
$$
E=F_Q^*\operatorname{diag}(\lambda_0,\ldots,\lambda_{Q-1})F_Q\otimes I_m.
$$
All diagonal blocks are $cI_m$. On the $\lambda_0$ eigenspace the interpolation before right multiplication by $M$ has eigenvalue
$$
z+(1-z)c,
$$
whose modulus is $r_\rho(z)$. Right multiplication by any unitary preserves this operator norm.

Every scalar diagonal entry has modulus $\rho$. Row unitarity bounds each off-diagonal entry by $\sqrt{1-\rho^2}=1/64<\rho$; tensoring gives the desired block norm bound. The cases $z=0,1$ also attain equality. Thus the universal norm and domain optimality claim is justified for this data class. The example may depend on $z$, which is sufficient for pointwise optimality.

The exact multiplier norm
$$
\|\mathcal P+z(I-\mathcal P)\|
=\frac{|1+(Q-1)z|+(Q-1)|1-z|}{Q}
$$
was also checked. The twirl gives its upper bound; a circulant unitary with one eigenvalue and a common value for the remaining eigenvalues aligns the two terms and attains it. Equality of this norm with $1$ occurs precisely on the real interval $[-1/(Q-1),1]$.

### 6.2 Hilbert-Schmidt and differentiated identities

Pinching is an orthogonal projection in the Hilbert-Schmidt inner product. Thus
$$
\operatorname{Tr}B^*C=0,\qquad
\|C\|_{\rm HS}^2=N-\|B\|_{\rm HS}^2,
$$
and exactly
$$
\|X(z)\|_{\rm HS}^2
=\|B\|_{\rm HS}^2+|z|^2(N-\|B\|_{\rm HS}^2).
$$
The bimodule identity also gives
$\mathcal P(C^*C)=I-B^*B$. For $|z|>1$, division by $N$ and $\|B\|_{\rm HS}^2/N\le\rho^2$ imply
$$
\|X(z)\|^2\ge1+(1-\rho^2)(|z|^2-1)>1.
$$
The sectorwise orthogonality of $Bv,Cv$ for $v$ in one sector is valid, but it does not extend to arbitrary superpositions. The source correctly avoids promoting it to a false full-space norm inequality.

At $t=1$, cyclicity of the differentiated finite polynomial gives
$$
\frac d{dt}\operatorname{Tr}X(t)^n
=n\operatorname{Tr}(RU^{n-1}).
$$
Hence the squared-trace derivative retains the mixed trace
$$
2n\left(|p_n|^2-\operatorname{Re}(\overline{p_n}q_n)\right),
\qquad q_n=\operatorname{Tr}(KU^{n-1}).
$$
In contrast, each of the $n$ terms in the Hilbert-Schmidt derivative reduces to
$\operatorname{Tr}(RU^*)=N-\|B\|_{\rm HS}^2$. Therefore
$$
\left.\frac d{dt}\|X(t)^n\|_{\rm HS}^2\right|_{1}
=2n(N-\|B\|_{\rm HS}^2)\ge2nN/4096.
$$
The two explicit three-dimensional examples have squared-trace derivatives $-25/6$ and $16/3$, as claimed. They exclude a universal sign deduction from these matrix identities.

### 6.3 Exact signed pair test

For the comparison involution with $2N/3$ eigenvalues $1$ and $N/3$ eigenvalues $-1$, coordinate pinching gives $B=cI$, $c=1/3$. Its all-block norms are bounded by $\sqrt{8/9}<\rho$. With $M=I$, the eigenvalues of $X(1-\delta)$ are
$$
x_+=1-(1-c)\delta,\qquad x_-=-[1-(1+c)\delta].
$$
The normalized multiplicities are $(1+c)/2$ and $(1-c)/2$. Taylor expansion, uniform for $n\le bN$ and $\delta N\to0$, gives
$$
N^{-1}\operatorname{Tr}X(1-\delta)^n
=\begin{cases}
1-(1-c^2)n\delta+O(n^2\delta^2),&n\ \text{even},\\
c+O(n^2\delta^2),&n\ \text{odd}.
\end{cases}
$$
The first derivative cancels exactly in the odd case. Squaring produces a difference $2(1-c^2)n\delta+O(n^2\delta^2)$ for even $n$, and $O(n^2\delta^2)$ for odd $n$.

For $w\in C_c^1([0,\infty))$, the even-lattice Riemann sum is
$$
\sum_{n\ge1,\ n\ {\rm even}}n\,w(n/N)
=\frac{N^2}{2}\int_0^\infty t\,w(t)\,dt+O_w(N).
$$
It follows independently that
$$
\frac1{N^2}\sum_{n\ge1}w(n/N)
\left(|\operatorname{Tr}E^n|^2-
|\operatorname{Tr}X(1-\delta)^n|^2\right)
=\frac89\delta N^2\int_0^\infty t\,w(t)\,dt
+O_w(\delta N+\delta^2N^3).
$$
At $\delta=\kappa/N^2$, this has the claimed nonzero limit whenever the first weighted moment is positive. The example uses arbitrarily large odd squares with $d$ an odd multiple of $3$; it is not an assertion about the original $M_N,A_N$.

The general telescoping estimate gives the corresponding upper order $O_w(\delta N^2)$, for compactly supported bounded weights and the full exponential weight. Damping the norm bound at times $n\asymp N$ requires $\delta N$ not to vanish; the continuity bound only yields a vanishing transfer when $\delta N^2\to0$. The example proves that this mismatch cannot be removed by using just these matrix hypotheses. It does not prove that the original signed trace error is large.

The scalar witness $[\rho+(1-\rho)z]^n$, realized in the comparison construction with $M=I$, and the involution's even closed traces both confirm that exponential decay on fixed interior compact subsets does not imply decay at $z=1$. No universality obstruction beyond this specified interpolation method is claimed.

## 7. Exact verification of the Russian synthesis update

The new frozen synthesis was checked in Sections 4.2 and 5.1--5.4 against the two frozen primary sources above. There is no distortion of their hypotheses or conclusion:

- The interpolation is attached to the existing $K_N,R_N$ and their admissible character decompositions. Its comparison examples are explicitly distinguished from the original family.
- The monomial theorem retains odd $N\ge11$, real algebraic split parameter, and nonzero real algebraic kick parameter. The coordinates $(l,k)$ in the synthesis are the reverse of the primary source's $(k,l)$; accordingly the unitary obstruction frequency $(3,2)$ in the synthesis is exactly $(2,3)$ in the source.
- The use of $JM=MJ$ at parameter zero is correct for the reversal problem as well: the initial equation is commutation with $M^{-1}$, which is equivalent.
- The analytic lift is expressly permitted to have a complex diagonal derivative. Its existence is not inferred by extending the unknown unitary phases themselves.
- The scalar commutant conclusion at the original parameter is supported by a nonzero minor at that parameter, not merely by the one-dimensional kernel of the limiting problem.
- The dressed symmetry statement follows from the exact unitary conjugation and is not a claim excluding all antiunitaries.

The unchanged part of the synthesis was verified by an exact byte reconstruction, not merely the author's statement that it was unchanged. Starting with current SHA
241e694be03f59d2de3223c3e97d015c81d3d9e99fa63572763637724baa8cfb, delete the interval from the new Section 4.2 through the end of the new Section 5, change the final heading number from 6 back to 5, and remove the one new introductory sentence about the monomial result. The resulting bytes have SHA
36db3d65e94eb27a98304ba1baf245fc8c058c39e07a45ec653c17a5558499a0,
the previously audited synthesis.

Thus the earlier independently checked arithmetic constants, all-input/all-output estimates, fixed-order quantifiers, inferred fixed-$r$ sparse extension, and first unproved $b_*$ pair test are exactly preserved. The applicable earlier records are:

| Audit record | SHA-256 |
|---|---|
| audit_russian_synthesis_and_closure.md | d3ca6b1005e29edf18526c5b9dd6bb35d042112b0cf0080c6fc7391fe43ded70 |
| audit_russian_synthesis_update.md | 6539d4f0709bd83081dbafda2e77be0f746a689d9802ca0f38f111dca5b56268 |

The finite identities and the conditional implication $H_{\rm diag}\Rightarrow\mathrm{Sine}_2$ were separately reconstructed in the first of those records. Their risk-bearing transitions are complete: exact alpha intensity controls periodization error in $L^1$; finite Bonferroni inequalities compare the two products using only fixed-order discrepancies and a CUE factorial tail $H^J/J!$; the approximation bandwidth and Bonferroni order are fixed before taking $N\to\infty$; compact-window CUE kernels converge after a gauge, with Gram determinants bounded by $1$; intensity gives tightness and the Laplace functionals identify the limit. No unproved deterministic exponential-moment tail is inserted.

Those conditional closure statements remain safe. What is not established is their antecedent for the original family. In particular, the explicit compact-band pair discrepancy in Section 4 of the synthesis is still labeled unproved, and no later monomial or interpolation result changes that status.

## 8. Final outcome

No source correction is required by this audit. The valid new result is the arbitrary-phase monomial symmetry exclusion, together with the scalar monomial unitary commutant assertion, for the exact algebraic family and stated parameters. The interpolation note proves exact norm and Hilbert-Schmidt statements and a sharp boundary-transfer limitation for the specified matrix data.

Neither result closes the all-odd-dimensional trace cancellation problem. No proof of $H_{\rm diag}$, no proof of the original local $\mathrm{Sine}_2$ limit, and no counterexample for the original family has been established in these new files.
