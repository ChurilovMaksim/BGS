> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round6_2026_10_21/root_all_orders_weighted_occupation_bound.md`. Embedded SHA256: `843da22fde6f586adbbdec0fe51b17875456477ed0f78dcb4f5b0115e87f919d`.
> [Thematic guide](../../topics/histories.md).

# All-order weighted bounds for the exact phase-constant sector

Date: 21 October 2026. This result follows from the proved arc resampling
inequality, not from any mixed-interval density bound. Its phase
integrals identify specific finite sums of the original matrix.
They are not a replacement for the deterministic target.

Base input: r6_occupation_minami_band_tail.md, SHA256
99a6c1b0b6c63a132be7ff1a43c7dbed1cd8321c181ee416f9c61f6601da2032,
Sections 2--5 and 8; separately audited in root_audit_occupation_minami.md.

## 1. Exact statement

Let $U$ be any $N\times N$ unitary matrix, $N\ge2$, and let
$D_\theta=\operatorname{diag}(e^{2\pi i\theta_v})$ have independent
uniform coordinate phases. Let $b\ge0$ be any Schwartz function on
$\mathbb R$. Put
$$
\beta_j=\sup_{x\in[j,j+1]}b(x),\qquad
B_b=\sum_{j\in\mathbb Z}\beta_j<\infty.
\tag{1.1}
$$
Let $\mathscr X_N^\theta$ be the periodic unfolding, at scale $N$,
of the eigenangles of $D_\theta U$, and define
$$
X_b=\langle b,\mathscr X_N^\theta\rangle.
$$
Then, for every real $t\ge0$,
$$
\boxed{\mathbb E_\theta e^{tX_b}
\le \exp\!\left(e^{tB_b}-1\right).}
\tag{1.2}
$$
Write $\mathfrak B_k=\sum_{j=0}^k S(k,j)$ for the $k$-th Bell
number, with $S(k,j)$ the Stirling number of the second kind and
$\mathfrak B_0=1$. If
$$
\overline M_{k,N}(U;b)
=\mathbb E_\theta M^{D_\theta U}_{k,N}(b)
$$
uses exactly the distinct-eigenvalue-label and global-shift definition
in the question, then
$$
\boxed{0\le\overline M_{k,N}(U;b)
\le \frac{\mathfrak B_k B_b^k}{k!}.}
\tag{1.3}
$$
This is uniform in $N,U$, for all $k\ge0$ at once. Moreover,
$$
\sum_{k\ge0}\frac{\mathfrak B_k B_b^k}{k!}
=\exp(e^{B_b}-1)<\infty.
\tag{1.4}
$$
For fixed $b$, the tails on the right of (1.4) tend to zero and
dominate the coefficient tails on the left of (1.3).

## 2. Proof without mixed-interval assumptions

Let $Y_j=\mathscr X_N^\theta([j,j+1))$. Since $N\ge2$, this
interval projects injectively, apart from endpoints, to an arc of
normalized length $1/N$. Endpoints have zero probability of being
eigenangles. The arc resampling theorem gives
$$
\mathbb E(Y_j)_k\le1
\quad (k\ge0),\qquad
\mathbb E e^{sY_j}\le\exp(e^s-1)
\quad(s\ge0).
\tag{2.1}
$$
No independence between different $Y_j$'s is asserted or needed.

Pointwise,
$$
0\le X_b\le\sum_j\beta_jY_j.
\tag{2.2}
$$
The sum is finite almost surely: its expectation is $B_b$ by
Tonelli and $\mathbb EY_j=1$. If $B_b=0$, all claims are immediate.
Otherwise set $a_j=\beta_j/B_b$, so $\sum_j a_j=1$.
Jensen's inequality for the probability weights $a_j$ gives
$$
\exp\!\left(tB_b\sum_j a_jY_j\right)
\le\sum_j a_j\exp(tB_bY_j).
\tag{2.3}
$$
One may first use finitely many indices, place the remaining mass at
the number zero, and then use monotone convergence. Taking expectation
and using (2.1) proves (1.2).

The elementary polynomial identity
$$
m^k=\sum_{r=0}^k S(k,r)(m)_r,\qquad m\in\mathbb Z_{\ge0},
$$
counts functions from a $k$-element set by the size of their image;
it proves $\mathbb EY_j^k\le\mathfrak B_k$. Jensen with the
convex function $x\mapsto x^k$, followed by (2.2), gives
$$
\mathbb E X_b^k\le B_b^k\mathfrak B_k.
\tag{2.4}
$$

Let the eigenangles of $D_\theta U$ be $\vartheta_1,\ldots,\vartheta_N$.
Periodization shows
$$
X_b=\sum_{a=1}^N b_N(\vartheta_a).
$$
Every summand in the elementary symmetric polynomial of order $k$
is included in $X_b^k/k!$, with nonnegative weights. Therefore
$$
e_k(b_N(\vartheta_1),\ldots,b_N(\vartheta_N))
\le X_b^k/k!.
\tag{2.5}
$$
Multiplying the matrix $D_\theta U$ by the common scalar
$e^{-2\pi i\alpha}$ is the same as shifting all coordinate phases
by $-\alpha$, and preserves their product uniform law. Consequently
the global $\alpha$-integral in the definition of $M_{k,N}$ is
redundant after expectation over $\theta$. Equations (2.4)--(2.5)
prove (1.3), also for $k>N$, when $e_k=0$.

To verify (1.4) directly, expand
$$
e^{e^z-1}
=e^{-1}\sum_{m=0}^\infty\frac{e^{mz}}{m!}.
$$
Nonnegative sums may be interchanged for real $z\ge0$. The
coefficient of $z^k/k!$ is
$e^{-1}\sum_{m\ge0}m^k/m!=\sum_{r=0}^kS(k,r)=\mathfrak B_k$.
Here the falling-factorial expansion was used and
$e^{-1}\sum_{m\ge0}(m)_r/m!=1$. This proves (1.4).

## 3. What the expectation extracts from the original finite formula

Suppose in addition that $\widehat b$ is smooth and compactly
supported, as required in the question. The exact Fourier formula
for $M_{k,N}$, followed by its partition expansion into traces,
is a finite expression. For each nonzero integer trace power $m$,
expand $\operatorname{Tr}(D_\theta U)^m$ as a sum of original
closed words when $m>0$, and use the conjugate expansion when
$m<0$. The factor $p_0=N$ carries no phases.

Integration over $\theta$ keeps exactly those tuples of original
words for which
$$
\sum_{\text{positive trace powers}}d(x)
=
\sum_{\text{negative trace powers}}d(y)
\quad\hbox{coordinate by coordinate}.
\tag{3.1}
$$
All Fourier weights and all partition inclusion--exclusion factors
remain exactly as in the question. No large-$N$ approximation is
involved in this extraction. Thus (1.3) bounds the *full* finite
phase-constant contribution to the $k$-th hierarchy functional,
including its internal cancellations and arbitrary numbers of
reconnections.

The complementary, nonconstant Fourier contributions at the original
phase vector zero are still present in $M^U_{k,N}$. Formula (1.3)
does not bound those contributions, compare the two laws, or
establish their limiting value. In particular it does not prove
$H_{\mathrm{diag}}$. At $k=2$ the sharper time-band bound from
the base input remains available for $\mathcal O_n$.

## 4. Consequences and limits

The same argument supplies uniform integrability for any fixed
weighted local count moment in the auxiliary row-phase process.
Its moment generating function is uniformly finite for every
positive real argument. These facts remove a possible moment-tail
obstruction when analyzing that precisely identified sector.

The estimate uses the envelope constant $B_b$, not $\int b$.
Replacing it by $\int b$ would require an additional argument
and is not claimed. Neither a mixed-interval determinantal formula
nor Poisson independence was used.

For the prescribed $U_N$, all statements hold with the exact
fixed value $\tau=10^{-80}$ and every odd $N\ge3$.
The target comparison remains a separate, unproved assertion.
