> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_continuation_2026_10_20/audit_quantitative.md`. Embedded SHA256: `91f854140a2fd1e28db50fead59afd9e1cbf70d6bef631895bdedbd85bed0455`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the effective transcendence bound

Date: 20 October 2026.

Audited packet: quantitative_transcendence_limits.md, SHA-256
35a8399e59a1ff390031cab2be39c654d08acf095326dcbc160dadca23f9eae4.

This audit also checks the separate rank-one counterexample supplied by
the amplitude agent, from its exact formulas.

## 1. Verdict

The quantitative argument passes. It proves an explicit positive lower
bound for the distance between distinct eigenvalues of the original
matrix at $\tau=10^{-80}$, with repeated eigenvalues allowed. Its bound
is uniform in the unknown number of distinct eigenvalues. The degree,
coefficient-height, and exponent-height estimates are valid and assume
no lower bound for a spectral-projector denominator.

The published formula has been checked against the rendered second page
of Huang's versioned PDF. The substitution of upper bounds and the
extraction of the minimum-gap estimate are correct. No decimal expansion
of the enormous bound is required.

The packet also correctly distinguishes a very small certified lower
bound from a claim that the actual gaps are small. Its configurations
show that both resulting numerical constraints, on the minimum gap and
on the complete gap product, allow quadratically many pairs at scale
$1/N$. This excludes a conclusion from these particular constraints
alone; it does not exclude stronger estimates or additional information
about the original family.

One clarification was suggested during the audit: the displayed bound is
monotone already on $t\ge1,d\ge1,h\ge0$. The author incorporated this,
covering actual degree one and actual height below one directly.

## 2. Authentication of the published estimate

The external result is Cheng-Chao Huang, *Explicit Bounds for Linear
Forms in the Exponentials of Algebraic Numbers*, ISSAC 2022, DOI
<https://doi.org/10.1145/3476446.3536170>, Theorem 1.2. The exact version
checked independently is arXiv:2112.05004v2, 16 May 2022:
<https://arxiv.org/pdf/2112.05004v2>.

The source permits complex algebraic exponents. They must be distinct,
and the algebraic coefficients must be nonzero. Its height is the
absolute logarithmic Weil height, as defined in Section 2.2. The degree
parameter bounds the individual degrees of both exponents and
coefficients. Rational linear independence of the exponents is not
required.

Replacing the source's number-of-terms variable by $t$, write
$$
S=\sum_{\nu=1}^t\beta_\nu e^{\alpha_\nu}.
$$
Its bound is $\log|S|\ge-\Phi(t,d,h)$, where
$$
\delta=d^{2t},\qquad
\mu=t d^{6t}(2h/d+3),
$$
$$
r=82(9/2)^\delta\delta^{3\delta+2},\qquad
r''=16(1+6\delta^2)(9/2)^\delta\delta^{3\delta},
$$
$$
\begin{aligned}
r'={}&12(9/2)^\delta\delta^{3\delta+2}\\
&+16(1+6\delta^2)(9/2)^\delta\delta^{3\delta}
       \log(9\delta^3)\\
&+80(9/2)^\delta\delta^{3\delta+4}(1+6\delta)\mu,
\end{aligned}
$$
$$
R=r't^\delta e^{6\delta^2\mu}
 +r''t^\delta e^{6\delta^2\mu}(\log t+6\delta\mu)
 +72e^{2\delta\mu},
$$
$$
\boxed{\displaystyle
\Phi(t,d,h)=e^{8\delta\mu}
 +rt^\delta e^{6\delta^2\mu}
       \left(th+\frac{39}{164}\mu+e^R\right).}
\tag{2.1}
$$

The factors $t^\delta$, $e^{6\delta^2\mu}$, $39/164$, and
$72e^{2\delta\mu}$, and all three contributions to $r'$, agree with
the rendered PDF. This is a direct transcription check rather than
reliance on text extraction alone.

All components are nondecreasing in their inputs on
$t\ge1,d\ge1,h\ge0$. For the factor containing $h/d$, write
$$
\mu=t\bigl(2h\,d^{6t-1}+3d^{6t}\bigr).
$$
The powers have positive exponents, while $t^\delta$, $\log t$, and
$\log(9\delta^3)$ have the required monotonicity and signs. Thus upper
bounds can replace actual term count, degrees, and heights.

This audit applies the published theorem. It does not claim a new proof
of that theorem or an exhaustive comparison with every effective
transcendence result.

## 3. The algebraic field and simultaneous eigenvalue height

Let
$$
K_0=\mathbb Q(\zeta_N,i,\sqrt N),\qquad
K=K_0(\rho_1,\ldots,\rho_s),
$$
where $\rho_j$ are the distinct eigenvalues of $A_N$, not those of
$U_N(\tau)$. The bounds
$$
[K_0:\mathbb Q]\le4\varphi(N),\qquad
[K:K_0]\le N!
$$
are valid. The latter follows because the splitting field acts faithfully
by permutations of at most $N$ distinct roots. Repetitions in the
characteristic polynomial do not affect separability after its repeated
factors are removed. Thus
$$
[K:\mathbb Q]\le4\varphi(N)N!\le d_N:=4NN!.
\tag{3.1}
$$
Normality of $K$ over $\mathbb Q$ is not needed.

The exact Weyl coefficients satisfy $4000c_{kl}\in\mathbb Z[i]$.
Their Fourier mass is bounded by
$$
\sum_{k,l}|c_{kl}|
\le1+\frac3{10}+\frac4{100}+\frac4{100}
=\frac{69}{50}=:\Lambda.
\tag{3.2}
$$
The constant term of $r/10$ has already been canceled by $-1/10$
in this calculation. Aliasing cannot increase the sum.

Under any complex embedding of $K_0$, Weyl matrices remain unitary,
and the Gaussian rational coefficients are unchanged or conjugated.
Therefore
$$
\|\sigma(A_N)\|\le\Lambda.
$$
Every conjugate of every $\rho_j$ is a root of a conjugate
characteristic polynomial and has absolute value at most $\Lambda$.

All entries of $4000A_N$ are algebraic integers. Its eigenvalues
$4000\rho_j$ are algebraic integers as well. Hence, at each finite
place, simultaneously for all entries and all $j$,
$$
|(A_N)_{xy}|_v,\ |\rho_j|_v\le|4000|_v^{-1}.
$$
The archimedean maximum is at most $\Lambda$. The product formula and
the tuple-height definition now give
$$
h(A_N)\le h_0,\qquad
h(\rho_1,\ldots,\rho_s)\le h_0,\qquad
h_0=\log(4000\Lambda)=\log5520.
\tag{3.3}
$$

The second bound is simultaneous, not a sum of $s$ scalar heights.
Its finite-place contribution is at most $\log4000$, and its
infinite-place contribution is at most $\log\Lambda$. No second
$\log4000$ should be added.

Every entry of $M_N^{\pm1}$ is a root of unity times $N^{-1/2}$.
All these entries have the same local absolute value, so
$$
h(M_N)=h(M_N^{-1})=\tfrac12\log N.
\tag{3.4}
$$
All eventual algebraic coefficients and exponents lie in $K$. No
eigenvalue of $U_N(\tau)$ is assumed algebraic or assigned a height.

## 4. Projector heights and the possible denominator gap

For the distinct eigenvalues of $A_N$,
$$
P_j=\prod_{k\ne j}\frac{A_N-\rho_kI}{\rho_j-\rho_k}.
\tag{4.1}
$$
This holds for eigenspaces of any dimension. Distinctness makes the
denominators nonzero; their numerical sizes are not assumed.

For entry-tuple height, local multiplication and triangle inequalities
give
$$
\begin{aligned}
h(XY)&\le h(X)+h(Y)+\log N,\\
h(X-aI)&\le h(X)+h(a)+\log2,\\
h(ab)&\le h(a)+h(b),\\
h(a-b)&\le h(a)+h(b)+\log2,\\
h(a^{-1})&=h(a)\quad(a\ne0).
\end{aligned}
\tag{4.2}
$$
The last identity follows from the product formula. It controls the
height of an inverse difference without a separate lower bound at a
chosen archimedean embedding.

The $s-1$ numerator factors in (4.1) have total height at most
$$
(s-1)(2h_0+\log2)+(s-2)_+\log N.
$$
The scalar denominator has height at most
$(s-1)(2h_0+\log2)$. Dividing gives
$$
h(P_j)\le
2(s-1)(2h_0+\log2)+(s-2)_+\log N
\le P_N,
$$
$$
P_N=N(4h_0+2\log2+\log N).
\tag{4.3}
$$
The empty-product case $s=1$ gives $P_1=I$.

Put $B_j=P_jM_N$, $C_j=M_N^{-1}P_j$. Equations (3.4) and (4.2)
give
$$
h(B_j),h(C_j)\le P_N+\tfrac32\log N.
$$
Concatenating their entry tuples costs at most the sum of the tuple
heights. Since there are $2s\le2N$ such matrices,
$$
h((B_j,C_j)_{j\le s})
\le B_N:=2N\left(P_N+\tfrac32\log N\right).
\tag{4.4}
$$
Using only the maximum of individual heights would not be justified,
because different entries can have different bad finite places. The
packet correctly uses the sum before introducing common local bounds.

As an independent denominator check, let $\kappa_j=4000\rho_j$ and
$$
\mathscr D=\prod_{i<j}(\kappa_i-\kappa_j)^2.
$$
This is a nonzero algebraic integer. Formula (4.1), written in terms of
$4000A_N$ and the $\kappa_j$, shows that
$\mathscr D P_j$ has integral entries for every $j$: its denominator
is a product of differences dividing the displayed product.
Every conjugate difference has absolute value at most $11040$, so
$$
h(\mathscr D)\le s(s-1)\log11040.
$$
A common denominator thus has a proved height bound even if some of its
complex values are very small. This additional check is not needed to
change the constants (4.3)–(4.4).

## 5. Why the Gram determinant avoids a simplicity hypothesis

For every integer $k$, including negative integers, define
$$
p_k(z)=\operatorname{Tr}U_N(z)^k,\qquad p_0(z)=N.
$$
These functions are entire, since
$$
U_N(z)^{-1}=M_N^{-1}e^{-izNA_N}.
$$
For formal Laurent variables set
$$
\mathcal U(X)=\sum_jB_jX_j,\qquad
\mathcal V(X)=\sum_jC_jX_j^{-1}.
$$
The projector identities give both
$\mathcal U\mathcal V=I$ and $\mathcal V\mathcal U=I$.
Specialization $X_j=e^{izN\rho_j}$ represents the matrix and its inverse.

Let $q$ be the actual number of distinct eigenvalues of $U_N(\tau)$.
Write those values as $\lambda_1,\ldots,\lambda_q$, with multiplicities
$m_a\ge1$, $\sum_a m_a=N$. Define
$$
D_q(z)=\det[p_{j-k}(z)]_{0\le j,k<q}.
$$
At the real parameter $\tau$, unitarity gives
$$
[p_{j-k}(\tau)]_{j,k}
=V\operatorname{diag}(m_a)V^*,\qquad V_{ja}=\lambda_a^j.
$$
The square Vandermonde matrix is invertible. Therefore
$$
\boxed{\displaystyle
D_q(\tau)=
\left(\prod_a m_a\right)
\prod_{a<b}|\lambda_a-\lambda_b|^2>0.}
\tag{5.1}
$$

This uses only the literal distinctness of the $q$ listed values.
It assumes neither a numerical gap nor simplicity of the original
$N$-dimensional matrix. In particular, one does not replace $q$ by
$N$ in this positivity assertion.

All effective estimates are uniform for $1\le q\le N$. Thus the proof
can choose the actual $q$ without knowing or computing it. The final
constant depends only on $N$, and positivity ensures that at least one
nonzero coefficient survives in its exponential-polynomial expression.
No lower bound on $q$ is used. If $q=1$, the gap assertion is vacuous.

The packet's additional maximal-rank observation is correct. Let $q_*$
be the maximum number of distinct eigenvalues attained over real
parameters. At a real parameter attaining this integer maximum,
$D_{q_*}>0$, so it is a nonzero algebraic exponential polynomial.
Qualitative Lindemann–Weierstrass makes it nonzero at every nonzero real
algebraic parameter. Its Gram rank there is at least $q_*$, hence equal
to $q_*$ by maximality. This does not show that $q_*=N$.

## 6. Support, degree, and heights after all frequency collisions

Set
$$
L_N=N(N-1),\qquad t_N=(2L_N+1)^N.
$$
A determinant term is a product of the traces $p_{j-\sigma(j)}$.
Its Laurent exponent vector has $\ell^1$-norm at most
$$
\sum_{j=0}^{q-1}|j-\sigma(j)|
\le q(q-1)\le L_N.
$$
The loose bound is sufficient; a sharp combinatorial maximum is
unnecessary.

After combining equal frequencies and deleting zero coefficients,
$$
D_q(\tau)=\sum_{\nu=1}^t\beta_\nu e^{\alpha_\nu},
\qquad
\alpha_\nu=i\tau N\sum_{j=1}^s n_{\nu j}\rho_j,
$$
$$
\sum_j|n_{\nu j}|\le L_N,\qquad
1\le t\le(2L_N+1)^s\le t_N.
\tag{6.1}
$$
The final exponents are distinct and coefficients nonzero. Distinct
integer exponent vectors may give the same frequency; the coefficient
bounds below explicitly allow this.

At a finite place, an integer linear combination of the $\rho_j$
is bounded by their common local maximum. At an infinite place, the
additional factor is at most $L_N$. Using the simultaneous bound (3.3),
$$
h(\alpha_\nu)\le
A_N^{\rm ht}:=h_0+\log(NL_N)+80\log10.
\tag{6.2}
$$
Here $80\log10$ is the height of the exact rational parameter
$10^{-80}$, not its small real absolute value.

At each place define
$$
b_v=\max\left(1,\max_{j,x,y}|(B_j)_{xy}|_v,
                  \max_{j,x,y}|(C_j)_{xy}|_v\right).
$$
Its global log average is at most $B_N$. At an infinite place, the
Laurent coefficient mass of $p_k$ is bounded by
$$
N^{2|k|+1}b_v^{|k|}.
\tag{6.3}
$$
For $|k|\ge1$, there are at most $s^{|k|}\le N^{|k|}$ choices of
projector labels and $N^{|k|}$ matrix-index cycles, each bounded by
$b_v^{|k|}$. The extra factor $N$ makes (6.3) also valid for $p_0=N$.

At a finite place, the nonarchimedean Gauss norm of this Laurent
polynomial is at most $b_v^{|k|}$. Sums, integer multiplicities, and
signs require no counting factor in that norm.

Both norms are submultiplicative. The determinant expansion therefore
has infinite-place coefficient mass at most
$$
N!N^{2L_N+N}b_v^{L_N},
$$
and finite-place Gauss norm at most $b_v^{L_N}$. Grouping coefficients
whose frequencies coincide cannot increase the former mass or the
latter norm. Hence the entire final coefficient tuple satisfies
$$
h(\beta_1,\ldots,\beta_t)\le
C_N^{\rm ht}
:=L_NB_N+\log(N!)+(2L_N+N)\log N.
\tag{6.4}
$$
There is no missing collision factor and no unjustified replacement of
a sum of heights by a maximum.

All exponents and coefficients lie in $K$, so their individual degrees
are at most $d_N$. A valid common height bound is
$$
h_N=1+A_N^{\rm ht}+C_N^{\rm ht}.
\tag{6.5}
$$
These are exactly the inputs required by the published theorem, even
when $q$, $s$, or the surviving $t$ is small.

## 7. The gap bound and the direct gap-product limitation

Set $F_N=\Phi(t_N,d_N,h_N)$. The published estimate, monotonicity, and
(5.1) give
$$
D_q(\tau)\ge e^{-F_N}.
\tag{7.1}
$$
For $q\ge2$, let $g_N$ be the minimum chordal distance between
distinct eigenvalues. One pair contributes $g_N^2$, all other squared
distances are at most $4$, and $\prod_a m_a\le N^N$. Thus
$$
D_q(\tau)\le N^Ng_N^2\,2^{N(N-1)-2}.
$$
Consequently
$$
\boxed{\displaystyle
g_N\ge\varepsilon_N
:=2^{\,1-N(N-1)/2}N^{-N/2}e^{-F_N/2}.}
\tag{7.2}
$$
The multiplicity factor and exponent of $2$ are correct. Angular
distance in radians is at least chordal distance. For phases modulo
one the corresponding lower bound is $\varepsilon_N/(2\pi)$.

The chosen input bounds have growth
$$
\log d_N=\Theta(N\log N),\qquad
\log t_N=2N\log N+O(N),\qquad
h_N=2N^4\log N+O(N^4).
$$
The first term of (2.1) already gives
$$
F_N\ge e^{8\delta\mu}
\ge\exp\!\left(24t_Nd_N^{8t_N}\right),
$$
because $\mu\ge3t_Nd_N^{6t_N}$ and $\delta=d_N^{2t_N}$. Hence the
explicit number (7.2) satisfies
$$
\varepsilon_N
\le\exp\!\left[-\tfrac12
       \exp\!\left(24t_Nd_N^{8t_N}\right)\right].
\tag{7.3}
$$
In particular $\varepsilon_N=o(N^{-K})$ for every fixed $K>0$.
This is an upper bound on the guaranteed lower bound; it is not an
upper bound on an actual spectral gap.

The strengthened full-product argument also passes. In the favorable
case of simple spectrum, let $R_a$ count unordered pairs at angular
distance at most $a/N$. Their chordal distances are also at most
$a/N$; all other chordal distances are at most $2$. Thus
$$
D_N(\tau)\le(a/N)^{2R_a}2^{N(N-1)-2R_a}.
$$
For $2N>a$, (7.1) gives
$$
R_a\le
\frac{F_N+N(N-1)\log2}{2\log(2N/a)}.
\tag{7.4}
$$
This bound exceeds the trivial pair count for large $N$.
Keeping the entire product therefore does not help at the scale of
this $F_N$.

The compatibility example establishes more than the failure of one
rearrangement. For fixed $a>0$, use phases in radians
$$
\varphi_j=\frac{ja}{2N^2},\qquad0\le j<N.
$$
For sufficiently large $N$, their minimum chordal distance is at
least $a/(4N^2)$, and their total angular span is less than $a/N$.
All $N(N-1)$ ordered distinct pairs are therefore close. Nevertheless
$$
D_N\ge\left(\frac{a}{4N^2}\right)^{N(N-1)}
\ge e^{-F_N},
$$
and the minimum gap is larger than $\varepsilon_N$.
Both numerical guarantees hold. This example tests the information
content of (7.1)–(7.2); it is not asserted to be the original spectrum.

The separate finite-range trace comparison is also correct:
$$
\|U_N-M_N\|\le\Lambda\tau N,\qquad
|p_m(\tau)-p_m(0)|\le\Lambda m\tau N^2.
$$
Using the exact bare-cat identity
$|p_m(0)|^2=\#\ker(S^m-I)\ge1$ gives
$$
|p_m(\tau)|\ge\tfrac12
\quad\text{if}\quad
mN^2\le(2\Lambda\tau)^{-1}.
$$
For $m$ proportional to $N$, this is a finite range at fixed $\tau$,
not an $N\to\infty$ statement.

## 8. Independent check of the rank-one counterexample

This is a separate family testing structural implications. It is not
a counterexample asserted for the original matrix.

Let $n=2d+1$, $d\ge3$, and
$$
A=\operatorname{diag}(-d,\ldots,-1,\tfrac12,1,\ldots,d).
$$
Let $J$ exchange the $-j$ and $j$ coordinates, fixing the central
one. Put
$$
v=n^{-1/2}(1,\ldots,1)^T,\quad
R=I-2vv^*,\quad
M=JR=J-2vv^*,\quad U(z)=e^{izA}M.
$$
Since $Jv=v$, $J$ and $R$ commute. Both are real symmetric
orthogonal involutions, so $M$ is too. Its rational entries are
$-2/n$ or $1-2/n$, and none is zero.

Set $B(z)=e^{izA}J$. On each paired coordinate block it is
$$
\begin{pmatrix}0&e^{-ijz}\\e^{ijz}&0\end{pmatrix},
$$
with eigenvalues exactly $1,-1$ for every complex $z$.
Each corresponding eigenspace of $B(z)$ therefore has dimension at
least $d$. The difference
$$
U(z)-B(z)=-2e^{izA}vv^*
$$
vanishes on $\ker v^*$. Intersecting either eigenspace with this
hyperplane leaves dimension at least $d-1$. Consequently
$$
\dim\ker(U(z)-I)\ge d-1,\qquad
\dim\ker(U(z)+I)\ge d-1
\tag{8.1}
$$
for every complex $z$. Repeated eigenvalues persist for all parameters.

The matrix $A$ has simple spectrum. Any matrix commuting with $A$
is diagonal; commuting also with the everywhere nonzero $M$ forces all
its diagonal entries to be equal. Thus the joint commutant of $A,M$
is scalar.

Also $M^2=I$ and
$$
\operatorname{Tr}M=\operatorname{Tr}J-2=-1.
$$
Every positive power trace at zero is nonzero: it is $n$ for even
powers and $-1$ for odd powers. Each power trace is an algebraic
exponential polynomial, so qualitative Lindemann–Weierstrass gives
$$
\operatorname{Tr}U(z)^m\ne0
\quad(m\ge1)
$$
at every nonzero algebraic $z$.

Odd scalar powers are impossible because both $1$ and $-1$ are
eigenvalues. An even scalar power would have to equal $I$. But
$\operatorname{Tr}A=1/2$, and for even $m$
$$
\det U(z)^m=e^{izm/2},
$$
since $(\det M)^m=1$. This cannot equal one at nonzero algebraic
$z$: $izm/2$ is nonzero algebraic, and its exponential is
transcendental.

The eigenspaces in (8.1) account for at least $n-3$ dimensions. At most
three additional distinct eigenvalues remain, so this family satisfies
$$
q\le5
$$
throughout. Thus simple $A$, scalar joint commutant, nonvanishing of
every power trace, and absence of scalar powers do not even force the
number of distinct eigenvalues to grow with dimension. This confirms
why a lower bound on $q$ may not be inserted into the Gram argument.
The argument audited above uses none.

## 9. Disposition

The published estimate and the elementary field, local-norm, and
linear-algebra calculations establish explicit finite-dimensional
separation of distinct eigenvalues at the exact original parameter.
Their resulting minimum-gap and full gap-product constraints do not
imply an $O(N)$ microscopic pair count.

Multiplicity control for the original family, microscopic signed orbit
cancellation, and Hdiag are not resolved by this calculation.

