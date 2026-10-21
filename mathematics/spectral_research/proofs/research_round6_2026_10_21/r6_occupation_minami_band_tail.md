> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/r6_occupation_minami_band_tail.md`. Embedded SHA256: `99a6c1b0b6c63a132be7ff1a43c7dbed1cd8321c181ee416f9c61f6601da2032`.
> [Thematic guide](../../topics/histories.md).

# Same-occupation spectral bounds from exact rank-one resampling

21 October 2026. This note proves new quantitative bounds for the exact
same-occupation sector of the original trajectory expansion. The bounds
hold for every finite unitary matrix, so in particular for the prescribed
$U_N=e^{i10^{-80}NA_N}M_N$, with no change of parameter and along all odd
dimensions. A phase integral is used solely as an exact coefficient
extraction for this sector. No phase-averaged limit is substituted for
the original spectrum, and no estimate of the remaining unequal-occupation
sector is asserted.

The proof is self-contained. Its ingredients are finite Fourier
orthogonality, a proved circular rank-one interlacing lemma, and a
resampling induction. The argument is related to spectral averaging and
Minami estimates; no claim of historical priority is made.

## 1. Statements

Let $U$ be an $N\times N$ unitary matrix, $N\ge1$. For a rooted cyclic
word $x=(x_0,\ldots,x_{n-1})$, $x_n=x_0$, write
$$
a_U(x)=\prod_{j=0}^{n-1}U_{x_jx_{j+1}},\qquad
d_v(x)=\#\{j:x_j=v\}.
$$
Define the original finite coefficients and sector sum by
$$
A_{n,d}(U)=\sum_{x:\,d(x)=d}a_U(x),\qquad
\mathcal O_n(U)=\sum_{|d|=n}|A_{n,d}(U)|^2.
\tag{1.1}
$$
Equivalently,
$$
\mathcal O_n(U)
=\sum_{d(x)=d(y)}a_U(x)\overline{a_U(y)}.
\tag{1.2}
$$
The individual pair weights in (1.2) may be complex; the full expression
is real and nonnegative by (1.1).

Set $c_0=\pi^2/4$. Then, for every integer $M\ge1$,
$$
\boxed{\sum_{n=1}^{M}\mathcal O_n(U)\le c_0NM.}
\tag{1.3}
$$
Consequently, for every fixed $B,W>0$ and any weights with
$|w_{n,N}|\le W$,
$$
\boxed{
\frac1{N^2}\left|\sum_{1\le n\le BN}
w_{n,N}\mathcal O_n(U)\right|
\le c_0WB.}
\tag{1.4}
$$

For every $s>0$, $B\ge0$, and every $N\ge1$, one also has
$$
\boxed{
\frac1{N^2}\sum_{n>BN}e^{-2sn/N}\mathcal O_n(U)
\le c_0e^{-2sB}
\left(B+\frac1N+\frac1{2s}\right).}
\tag{1.5}
$$
In particular the infinite tail of this exact sector is uniformly
controlled before taking $B\to\infty$. A slightly sharper complete-sum
bound is
$$
\boxed{
\frac1{N^2}\sum_{n\ge1}e^{-2sn/N}\mathcal O_n(U)
\le \frac{c_0}{N(e^{2s/N}-1)}
\le\frac{c_0}{2s}.}
\tag{1.6}
$$

For comparison, the pointwise bound $\mathcal O_n\le N^2$ alone would
give an upper bound growing like $N$ after summation on $n\asymp N$.
Thus (1.3)--(1.6) improve the controlled scale by a full factor of $N$.
They do not identify the sector's limiting value.

## 2. The auxiliary phase polynomial, with no change of target

Let $\theta=(\theta_0,\ldots,\theta_{N-1})$ range over $[0,1)^N$,
with product Lebesgue measure, and put
$$
D_\theta=\operatorname{diag}(e^{2\pi i\theta_v}),\qquad
W_\theta=D_\theta U.
$$
Every departure from $v$ contributes one factor
$e^{2\pi i\theta_v}$, so
$$
\operatorname{Tr}(W_\theta^n)
=\sum_{|d|=n}A_{n,d}(U)e^{2\pi i d\cdot\theta}.
\tag{2.1}
$$
Parseval gives exactly
$$
\mathcal O_n(U)
=\mathbb E_\theta|\operatorname{Tr}(W_\theta^n)|^2.
\tag{2.2}
$$

Only the quantity on the left will receive conclusions about the original
trajectory expansion. The original squared trace is
$$
|\operatorname{Tr}U^n|^2=\mathcal O_n(U)+\Omega_n(U),\qquad
\Omega_n(U)=\sum_{d\ne e}A_{n,d}(U)\overline{A_{n,e}(U)}.
\tag{2.3}
$$
The value $\Omega_n(U)$ is not removed in this note.

## 3. Exact one-coordinate spectral averaging

Fix a coordinate $v$, fix all $\theta_w$ with $w\ne v$, and let
$$
\mu_{v,\theta}(E)=
\langle e_v,\mathbf1_E(W_\theta)e_v\rangle
$$
be the scalar spectral measure on the unit circle, expressed in normalized
angle coordinates. Then
$$
\boxed{\int_0^1\mu_{v,\theta}(E)\,d\theta_v=|E|}
\tag{3.1}
$$
for every Borel set $E\subset\mathbb R/\mathbb Z$, where $|E|$ is
normalized Lebesgue measure.

To prove this, take a positive integer $m$. The diagonal matrix element
$\langle e_v,W_\theta^me_v\rangle$ is a sum of closed length-$m$
words rooted at $v$. Every such word has at least one departure from
$v$. As a polynomial in $e^{2\pi i\theta_v}$, all its powers are
strictly positive. Hence
$$
\int_0^1\langle e_v,W_\theta^me_v\rangle\,d\theta_v=0.
\tag{3.2}
$$
Negative Fourier coefficients vanish by complex conjugation, and the
zeroth coefficient is one. Thus the averaged spectral measure has exactly
the Fourier coefficients of normalized Lebesgue measure.

For completeness, equality of these finite measures follows first on
trigonometric polynomials. Fejer approximations converge uniformly for
continuous periodic functions, giving equality on all continuous
functions. Approximating open arcs from below and closed arcs from above
then identifies the measures on Borel sets. This proves (3.1).

In particular, if $X_I(\theta)$ counts the eigenvalues of $W_\theta$
in an arc $I$, with algebraic multiplicities, then
$$
X_I(\theta)=\sum_v\mu_{v,\theta}(I),\qquad
\mathbb E_\theta X_I=N|I|.
\tag{3.3}
$$
Endpoint choices are irrelevant to these expectations. Indeed (3.3)
applied to a singleton gives zero, so any fixed endpoint is almost surely
not an eigenvalue of $W_\theta$.

## 4. Circular interlacing under one row-phase change

**Lemma.** If $V$ is unitary, $e$ is a unit vector, and
$$
V_\beta=(I+(e^{i\beta}-1)ee^*)V,
$$
then for every proper connected arc $I$ whose endpoints avoid both
spectra,
$$
\bigl|\operatorname{Tr}\mathbf1_I(V_\beta)
-\operatorname{Tr}\mathbf1_I(V)\bigr|\le1.
\tag{4.1}
$$
Multiplicities are included.

Here is a direct proof. Write the distinct eigenvalues of $V$ as
$\lambda_j=e^{i\varphi_j}$, with spectral projections $E_j$, and put
$w_j=\langle e,E_je\rangle\ge0$. Their sum is one. If $w_j=0$, its
whole eigenspace is unchanged. If $w_j>0$ and its multiplicity is
$m_j$, an $(m_j-1)$-dimensional subspace orthogonal to $E_je$ is
unchanged. It remains to compare one old eigenvalue at each active angle
$\varphi_j$ with the affected new eigenvalues.

The determinant lemma gives, away from the old spectrum,
$$
\frac{\det(zI-V_\beta)}{\det(zI-V)}
=1-(e^{i\beta}-1)
\sum_j\frac{w_j\lambda_j}{z-\lambda_j}.
\tag{4.2}
$$
Define
$$
H(z)=\sum_jw_j\frac{z+\lambda_j}{z-\lambda_j}.
$$
Since $\sum_jw_j=1$, equation (4.2) equals
$$
e^{i\beta/2}
\left(\cos\frac\beta2-i\sin\frac\beta2\,H(z)\right).
\tag{4.3}
$$
If $\beta=0\pmod{2\pi}$, there is nothing to prove. Otherwise, on the
unit circle away from the active poles, let $z=e^{i\varphi}$. Then
$$
H(e^{i\varphi})
=-i\sum_{j:w_j>0}w_j\cot\frac{\varphi-\varphi_j}{2}.
$$
The new active eigenvalues satisfy
$$
\sum_{j:w_j>0}w_j\cot\frac{\varphi-\varphi_j}{2}
=\cot\frac\beta2.
\tag{4.4}
$$
On each open cyclic gap between consecutive active old angles, the left
side decreases strictly from $+\infty$ to $-\infty$, since its
derivative is
$$
-\frac12\sum_{j:w_j>0}w_j
\csc^2\frac{\varphi-\varphi_j}{2}<0.
$$
There is therefore exactly one new active angle in each cyclic gap.
These account for all the affected eigenvalues by the degree of the
characteristic polynomial. The new active eigenvalues alternate with
the old active ones around the circle. Counts in any connected proper
arc differ by at most one. Adding back the common eigenspaces does not
change this difference, proving (4.1).

The proof includes a single active eigenvalue: its unique cyclic gap
is the rest of the circle. Degeneracies contribute precisely the common
subspaces already removed.

Changing one coordinate $\theta_v$ in $W_\theta$ is of the lemma's
form. The exceptional endpoint cases have product measure zero by
(3.3), also when an independent replacement phase is introduced.

## 5. All factorial count moments by resampling

For a nonnegative integer $m$, use
$$
(m)_k=m(m-1)\cdots(m-k+1),
$$
with $(m)_0=1$ and $(m)_k=0$ when $0\le m<k$.
For every connected arc $I$ and every integer $k\ge1$,
$$
\boxed{\mathbb E_\theta(X_I)_k\le (N|I|)^k.}
\tag{5.1}
$$
For the full circle the inequality is immediate, and for a proper arc
we give the induction.

The case $k=1$ is the equality (3.3). For each coordinate $v$, let
$\theta_v'$ be an independent uniform replacement, and denote the
count after replacement by $X_I^{(v)}$. By (4.1),
$$
X_I-1\le X_I^{(v)}
\tag{5.2}
$$
almost surely. On the event $X_I\ge1$, the function
$m\mapsto(m)_{k-1}$ is nondecreasing on nonnegative integers, so
$$
(X_I-1)_{k-1}\le(X_I^{(v)})_{k-1}.
$$
On the event $X_I=0$, every $\mu_{v,\theta}(I)$ is zero. Consequently
there is no need to evaluate a negative falling factorial, and
$$
(X_I)_k
\le\sum_v
\mu_{v,\theta}(I)(X_I^{(v)})_{k-1}.
\tag{5.3}
$$
This follows from equality with
$\sum_v\mu_{v,\theta}(I)(X_I-1)_{k-1}$ when $X_I\ge1$.

Fix the other phases and the replacement phase, and integrate the
original $\theta_v$. The second factor in the corresponding summand
of (5.3) is independent of $\theta_v$, while (3.1) integrates the
first factor to $|I|$. After the remaining integrations,
$$
\mathbb E(X_I)_k
\le\sum_v |I|\,\mathbb E(X_I^{(v)})_{k-1}
=N|I|\,\mathbb E(X_I)_{k-1}.
$$
The replaced phase vector has the same product distribution as the
original one. Induction proves (5.1), including $k>N$, when the
left side is zero.

The second moment consequence is
$$
\boxed{\operatorname{Var}_\theta X_I\le N|I|.}
\tag{5.4}
$$
Indeed $X_I^2=(X_I)_2+X_I$, the mean is $N|I|$, and
$\mathbb E(X_I)_2\le N^2|I|^2$.

No assertion about a mixed-interval factorial correlation density is
made. A row-phase ensemble can have deterministic eigenvalue gaps and
singular pair correlations. Bounds (5.1) concern all points lying in
one connected arc.

## 6. The variance identity and the time-band bound

The law of $W_\theta$ is invariant under multiplication by a common
scalar phase, because adding the same angle to every $\theta_v$
preserves product Lebesgue measure. Hence, for positive $n,m$,
$$
\mathbb E\,\operatorname{Tr}W_\theta^n=0,\qquad
\mathbb E\,\operatorname{Tr}W_\theta^n
\overline{\operatorname{Tr}W_\theta^m}
=\mathbf1_{\{n=m\}}\mathcal O_n(U).
\tag{6.1}
$$
Likewise two positive, unconjugated trace powers have zero average.

Let $I$ be an arc of normalized length $\ell$, $0<\ell<1$.
Its Fourier coefficients have moduli
$$
|\widehat{\mathbf1_I}(n)|
=\frac{|\sin(\pi n\ell)|}{\pi|n|},\qquad n\ne0.
$$
It follows that
$$
\boxed{
\operatorname{Var}X_I
=2\sum_{n\ge1}
\frac{\sin^2(\pi n\ell)}{\pi^2 n^2}\mathcal O_n(U).}
\tag{6.2}
$$

One can justify the nonsmooth indicator without invoking a distributional
identity. Replace it by its Fejer sums. These have finite Fourier
expansions and lie between zero and one. Their corresponding eigenvalue
counts converge almost surely to $X_I$, because endpoints have
probability zero, and are bounded by $N$. Thus they converge in
$L^2$. Equation (6.1) proves the finite variance identity. The squared
Fejer factors increase to one for each fixed Fourier index, so monotone
convergence gives the nonnegative series (6.2).

Now choose $\ell=1/(2M)$. For $1\le n\le M$, concavity of sine on
$[0,\pi/2]$ gives
$$
\sin\frac{\pi n}{2M}\ge\frac nM,
\qquad
\frac{\sin^2(\pi n\ell)}{\pi^2n^2}\ge\frac1{\pi^2M^2}.
$$
Using (5.4) and (6.2),
$$
\frac2{\pi^2M^2}\sum_{n=1}^M\mathcal O_n(U)
\le\operatorname{Var}X_I
\le\frac{N}{2M}.
$$
This proves (1.3). Positivity of $\mathcal O_n$, followed by
$M=\lfloor BN\rfloor$, proves (1.4). If $M=0$, its sum is empty.

## 7. Uniform all-time tails

Write $F(M)=\sum_{n=1}^M\mathcal O_n(U)$, $F(0)=0$. For
$0<q<1$ and $L\ge0$, summation by parts gives
$$
\sum_{n>L}q^n\mathcal O_n(U)
=(1-q)\sum_{m=L+1}^{\infty}q^mF(m)-q^{L+1}F(L).
\tag{7.1}
$$
The sums converge absolutely already from $\mathcal O_n\le N^2$.
Since $F(m)\le c_0Nm$,
$$
\sum_{n>L}q^n\mathcal O_n(U)
\le c_0Nq^{L+1}
\left(L+1+\frac q{1-q}\right).
\tag{7.2}
$$
For $q=e^{-2s/N}$, $L=\lfloor BN\rfloor$, we have
$$
q^{L+1}\le e^{-2sB},\quad
\frac{L+1}{N}\le B+\frac1N,\quad
\frac q{N(1-q)}
=\frac1{N(e^{2s/N}-1)}\le\frac1{2s}.
$$
This proves (1.5). Taking $L=0$ in (7.2) without separating its two
terms gives (1.6).

Thus the order of limits needed to discard the exponential tail is now
justified for $\mathcal O_n(U_N)$ itself. The statement is not about
the tail of $|\operatorname{Tr}U_N^n|^2$ or of $\Omega_n(U_N)$.

## 8. Local count uniform integrability in the auxiliary process

For any interval of scaled length $a$ and $N>a$, the auxiliary
periodically unfolded eigenvalue process of $W_\theta$ has count
$Y_{N,a}$ distributed as $X_I$ with $|I|=a/N$. Global phase
stationarity makes an additional uniform shift unnecessary. Equations
(3.3) and (5.1) give
$$
\mathbb E Y_{N,a}=a,\qquad
\mathbb E(Y_{N,a})_k\le a^k.
\tag{8.1}
$$
For every $t\ge0$, the binomial identity, followed by the factorial
bound, yields
$$
\boxed{
\mathbb E e^{tY_{N,a}}
=\sum_{k=0}^{N}
\frac{(e^t-1)^k}{k!}\mathbb E(Y_{N,a})_k
\le\exp\{a(e^t-1)\}.}
\tag{8.2}
$$
In particular every fixed positive count moment is uniformly integrable.
For example, for a fixed $p>0$ and any $t>0$,
$$
\mathbb E[Y_{N,a}^p\mathbf1_{\{Y_{N,a}>R\}}]
\le
\left(\sup_{x>R}x^pe^{-tx}\right)
\exp\{a(e^t-1)\}\longrightarrow0.
$$
The same domination applies to continuous compactly supported linear
statistics bounded by a constant times such an interval count.

The auxiliary laws are tight as locally finite point measures, by the
uniform mean bounds on a countable exhausting family of intervals.
Every subsequential limit retains intensity one: expectations of
continuous compactly supported test functions pass to the limit by
uniform integrability. Its interval count moments obey (8.1)--(8.2);
fixed interval endpoints have zero mass almost surely by stationarity
and the finite intensity.

These conclusions concern the auxiliary row-phase law, or quantities
identified with its integrals exactly as in (2.2). They do not imply
uniform integrability or a local limit for the original deterministic
spectrum with only its one global random shift.

## 9. Quantitative scope of the advance and the remaining estimate

For the original family, the exponential coherent edge class
$\mathcal F_n(U_N)$ was proved in round 5, and
$\mathcal R_n^{\rm occ}=-\mathcal F_n+\mathcal O_n$ exactly.
The present result improves control of its remaining sector after time
summation:
$$
\frac1{N^2}
\sum_{n\le BN}\mathcal O_n(U_N)=O(B),
$$
with a universal explicit constant, and gives a uniformly negligible
exponential tail.

It is still necessary to compute the limit of this bounded quantity
with the specified weights and to control the unequal-occupation
sector. For an admissible pair test $b$, the exact discrepancy remains
$$
\Delta_{2,N}(b)=\frac1{N^2}\sum_{n\ge1}
|\widehat b(n/N)|^2
\{\mathcal O_n(U_N)-\min(n,N)+\Omega_n(U_N)\}.
\tag{9.1}
$$
All sums in (9.1) are finite. The new bounds do not establish convergence
of (9.1) to zero, nor a bad subsequence for the original family.
The targets at higher $k$ remain separate requirements.
