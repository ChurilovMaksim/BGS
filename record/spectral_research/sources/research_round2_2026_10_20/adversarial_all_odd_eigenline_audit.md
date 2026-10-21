> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_all_odd_eigenline_audit.md`. Embedded SHA256: `8b2143715121d41735b9d2c2baa586623effce0c524dcb8cdade7b4ece542fb5`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: exclusion of algebraic eigenlines for all odd N except 7

Research continuation, 20 October 2026.

## 1. Frozen inputs and verdict

| Input | SHA-256 |
|---|---|
| root_all_odd_no_algebraic_eigenvectors.md | 6634de7f0ccaf56270467f03401aadd66732ba704567e4b0b47ebdd6a74677e2 |
| root_jacobi_small_certificates.py | 4735755e1debe91ca6ab4ceaaf19d75d82ea75057d91fc3023f2ebfdaabc868b |
| root_jacobi_small_certificates.json | a61eec699954c72eee1e5ee3f786b7cb2e3f172ed07d5bf69bd0ef67d401215e |
| arithmetic_padic_jacobi_simplicity.md | f311596933d383976547ac5b2cd633b91107074da0fcab58db989eedcc4568df |

**Verdict: PASS.** The proof establishes, for every odd $N\geq3$
other than $7$,
$$
E_\lambda(A_N)\cap M_N^{-1}E_\lambda(A_N)=\{0\}
\tag{1.1}
$$
for every eigenvalue $\lambda$. Consequently the actual
$U_N(z)=e^{izNA_N}M_N$ has no eigenvector with an algebraic
projective representative whenever $z\ne0$ is algebraic. The
eigenvalue itself is not required to be algebraic.

The mixed-minor proof for $N=7n$, $n\geq9$, does not claim
simple spectrum of $A_N$ or $U_N$. It allows eigenspaces of
$A_N$ of dimension up to seven. The absence of algebraic
eigenlines does not prove simplicity or any lower bound on gaps.

## 2. The seven paths and their integral recurrence

The original modular half gives the same exact gauge as in the
independently audited one-path argument:
$$
x_j=(N+1)/2+j\bmod N,\qquad D_{jj}=\omega^j,\qquad
L=200D^*P^*A_NPD,
$$
where $\omega=(-3+4i)/5$.
The internal hopping is $r((j+1)/N)$, because the sum of the
two modular halves is $1$ modulo $N$.

For $N=7n$, the zero edges are precisely $j=sn-1$.
The seven support intervals are
$$
C_s=\{sn,\ldots,(s+1)n-1\},\quad s=0,\ldots,6.
$$
Each is an irreducible real Jacobi path and hence has simple
spectrum with nonzero endpoint coordinates. A global eigenspace
therefore has dimension at most seven, with at most one
eigenvector on each path.

At the prime over $1+2i$, normalized by $v(1+2i)=1$,
$$
v(\omega)=1,\quad v(d_j)\geq0,\quad
0\leq v(b_j)\leq1/2
$$
for all nonzero edges. These facts remain valid when $5\mid n$
or $7\mid n$: the identity for $r$ involves the root
$\eta^7$, and its only possible positive valuation at a
nonzero edge comes from a nontrivial $5$-power root.

For each path, its monic eigenvector polynomials are integral.
At local position $j$, normalizing the initial endpoint to
one gives valuation at least $-j/2$. The reversed recurrence
and the eigenvalue Vandermonde identity give, for $k$ distinct
eigenvectors on one path,
$$
v\left(\frac{\det X_I}{\det X_{I_*}}\right)
\geq-\frac12(\sum I_*-\sum I),
\tag{2.1}
$$
where $I_*$ consists of the last $k$ positions. Its
denominator is nonzero. This uses a polynomial Vandermonde
factorization; no eigenvalue difference is assumed to be a
valuation unit.

## 3. Why the new mixed minor avoids the earlier Fourier obstruction

Let $\mu$ be a global eigenvalue of $L$, of multiplicity
$k\leq7$, with basis columns $Y_1,\ldots,Y_k$ supported on
the distinct active paths $s_1,\ldots,s_k$. Choose a single
row path $C_r$. For $n\geq9$ it contains at least $n-1\geq8$
eigenvectors whose eigenvalues differ from $\mu$. Choose
any $k$ of them as columns of $X$. These are orthogonal
to the entire $\mu$-eigenspace.

The relevant square matrix is
$$
B=X^TD^{-1}M_0DY,\qquad M_0=P^*M_NP.
$$
Its Cauchy--Binet terms can be nonzero only for row sets
$I\subset C_r$ and column sets $J$ containing one coordinate
in each active path. The extremal sets are
$$
I_*=\{\text{last $k$ positions of }C_r\},\qquad
J_*=\{s_1n,\ldots,s_kn\}.
$$
The two endpoint eigenvector minors are nonzero.

The Fourier core of $M_0$ is
$\zeta_N^{cuv}$, $c=\overline4\bmod N$, with unit row and
column chirps and common scale $N^{-1/2}$. Write
the consecutive row coordinates as $u_0,u_0+1,\ldots,u_0+k-1$.
For column $s_jn$, its powers are powers of
$$
z_j=\zeta_N^{c s_jn}=\zeta_7^{c s_j}.
$$
After removing the nonzero factor $z_j^{u_0}$, the determinant
is $\operatorname{Vdm}(z_1,\ldots,z_k)$. The $z_j$ are
distinct, and every difference is a unit at the prime over $5$.
Thus
$$
v(\det(M_0)_{I_*,J_*})=-\frac{k}{2}v(N).
\tag{3.1}
$$
The roots here have exact order $7$; there is no extra factor
of $n$ in the row progression. This is why the rank-one
obstruction for endpoint sets in seven different row paths
does not apply.

Every other Fourier minor, after removing $N^{-k/2}$, is
a determinant of valuation-integral entries. Equation (3.1)
therefore gives a nonnegative valuation for its ratio to the
extremal Fourier minor.

Put $g_R=\sum I_*-\sum I$ and $g_C=\sum J-\sum J_*$.
The row eigenvector ratio loses at most $g_R/2$ by (2.1).
The column eigenvector minor is a signed product of one
coordinate per path and loses at most $g_C/2$.
The gauge contributes $g_R+g_C$. Thus any nonextremal term
has ratio valuation at least
$$
\frac12(g_R+g_C)>0.
$$
Equality in both endpoint sum inequalities occurs only at
$(I_*,J_*)$. The extremal term is consequently the unique
term of least valuation, proving $\det B\ne0$.

If a vector in $E_\mu(L)$ were mapped back into that
eigenspace by $D^{-1}M_0D$, every selected $X$-coordinate
of its image would vanish. Invertibility of $B$ forces the
vector to be zero. Undoing the gauge proves (1.1).

## 4. Independent verification of the three finite certificates

The only missing odd multiples of seven are $21,35,49$.
The certificate uses the following fields and images:

| $N$ | $p$ | $\zeta_N$ | $i$ |
|---:|---:|---:|---:|
| 21 | 337 | 13 | 148 |
| 35 | 281 | 98 | 228 |
| 49 | 197 | 16 | 183 |

The source was inspected in full. It checks primality,
the exact order of $\zeta_N$, the equation $i^2=-1$,
all seven path boundaries, the monic degree of the
characteristic polynomial, and the full Bezout identity.
The trigonometric coefficients are formed as
$$
\cos(j)=\frac{\zeta_N^j+\zeta_N^{-j}}2,\qquad
\sin(j)=\frac{\zeta_N^j-\zeta_N^{-j}}{2i}.
$$
Its diagonal and hopping expressions agree with the exact
gauged $200A_N$ in the preceding section.

Because $N$ is odd, the cyclotomic conductors $4$ and
$N$ are coprime. The displayed primitive roots define an
evaluation of $\mathbb Z[i,\zeta_N,1/200]$ into
$\mathbb F_p$; all denominators used are invertible.
Thus these are genuine reductions of the characteristic
polynomial, rather than unrelated finite-field models.

I reconstructed all three certificate cases by importing
the source without running its file-writing entry point
and calling its certificate function. The resulting full
dictionaries exactly matched the saved JSON data.
Separately, I expanded both recorded products
$UP$ and $VP'$ by direct nested integer loops,
without using the author's polynomial arithmetic or
Euclidean algorithm. In each field their sum was exactly
the constant polynomial $1$. The source and data hashes
above were rechecked.

Therefore the reduced monic characteristic polynomials
are squarefree. Their characteristic-zero discriminants
cannot vanish, proving simple spectrum of the actual
$A_N$ in these three dimensions.

With this simplicity, each eigenvector of the seven-path
direct sum is supported on a single interval of length
$n=N/7$. Its Fourier transform, after unit chirps and a
monomial factor, is a nonzero polynomial of degree at most
$n-1$ evaluated at $N$ distinct roots.
If its image were supported on the same path, it would
vanish at the $6n$ distinct outside coordinates.
This is impossible. Hence (1.1) holds in all three cases.

For $7\nmid N$, the already audited simple spectrum
and nonzero off-diagonal overlap entries give (1.1)
immediately.

## 5. The projective transcendence argument

Suppose an eigenline of $U_N(z_0)$ has a nonzero
algebraic representative $v$, where $z_0\ne0$ is
algebraic. Each expression
$$
v_i(U_N(z)v)_j-v_j(U_N(z)v)_i
$$
is an algebraic exponential polynomial and vanishes at
$z_0$. After collecting equal frequencies,
Lindemann--Weierstrass forces every coefficient to vanish.
The hypotheses are exactly algebraic coefficients and
distinct algebraic exponents after multiplication by the
nonzero algebraic parameter.

Thus $U_N(z)v$ lies in $\mathbb Cv$ for every complex
$z$. At $z=0$, $M_Nv$ is a nonzero multiple of
$v$. The derivative at zero is $iNA_NM_Nv$, which
also belongs to that line. Hence $A_Nv$ belongs to
the same line. This contradicts (1.1).

No algebraicity of the eigenvalue of $U_N(z_0)$ entered
the argument. Projective coordinate minors remove it
before applying the transcendence theorem.

At $N=7$, $r$ vanishes on the entire grid and
the diagonal is $9/10$; therefore $A_7=(9/10)I$.
The asserted finite exception is genuine.

## 6. Scope

The theorem is exact and covers every odd dimension
apart from the stated finite exception. It does not
convert algebraic nonresonance into a lower bound on
spectral distances. In particular the weighted trace
correlations on times proportional to $N$ required
for $H_{\rm diag}$ remain unproved.
