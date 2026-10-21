> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_growing_routing_families.md`. Embedded SHA256: `4a78ed247faa8791b34f85b0ee69a6696ac8f9578b7e6d836bf9965f11e30555`.
> [Thematic guide](../../topics/arithmetic.md).

# Growing routing families and the remaining coherence obstruction

21 October 2026. A finite-dimensional extension of the one-step Hilbert--Schmidt argument.

This note proves a new estimate for a growing collection of routes, with one route assigned to each disjoint group of starting characters. It also gives exact Parseval and trace-closure identities showing the loss that remains for arbitrary routes, and two elementary examples proving limitations of norm-only arguments. It does not prove or refute the original spectral universality assertion.

## 0. Inputs and notation

The original matrices are unchanged:

$$
E_N=e^{i\tau N A_N},\qquad U_N=E_NM_N,\qquad \tau=10^{-80}.
$$

Let $N=d^2m$ be odd, let $G=(\mathbb Z/d\mathbb Z)^2$, and put $q=|G|=d^2$. The exact commuting Weyl representation $H_g$ has character projections $P_\chi$, $\chi\in\widehat G$, each of rank $m$. The exact metaplectic factor satisfies

$$
M_NP_\chi=P_{\mathsf S\chi}M_N,\qquad
\mathsf S\chi=\chi\circ L,\qquad
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}.
\tag{0.1}
$$

For a relative character $\nu$, define

$$
\mathcal Q_\nu(X)=\sum_\chi P_{\nu\chi}XP_\chi
=q^{-1}\sum_{g\in G}\overline{\nu(g)}H_gXH_g^*.
\tag{0.2}
$$

These are orthogonal projections on the Hilbert space of matrices with the Hilbert--Schmidt inner product. Positivity as a map on Hermitian matrices is not asserted for nontrivial $\nu$.

The required inputs are the following two bounds:

$$
\sup_{\chi,\psi}\|P_\psi E_NP_\chi\|\le \rho=1-g,\quad 0<g\le\tfrac12,
\qquad
\sup_\nu N^{-1/2}\|\mathcal Q_\nu(E_N)\|_{\rm HS}
\le\overline\sigma=d^{-1}+C N^{-1/32}.
\tag{0.3}
$$

The sources for these inputs are:

- counter_one_step_pinching_hs.md, SHA-256 a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629;
- its independent audit audit_one_step_pinching_hs.md, SHA-256 7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce;
- counter_relative_character_routes.md, SHA-256 1b27d09f2dc4a8e8d87ccdf31c7b3c7230065e0c5ee35492c7149880a75ecae3;
- the explicit exponent supplied by audit_explicit_symbol_finite_type16.md, SHA-256 1da0fbd15dec74a90a742804f69165f478673ce07aaf7eb38760de7f60cb7ffb.

All finite-dimensional estimates below use only (0.1)--(0.3). Their application to the original family uses exactly the analytic and arithmetic inputs in these frozen sources. This note is a new raw proof for separate audit.

## 1. A route may be assigned to each group of starting characters

Partition the character set into $J$ disjoint groups:

$$
\widehat G=A_1\sqcup\cdots\sqcup A_J,\qquad
P_j=\sum_{\chi\in A_j}P_\chi.
\tag{1.1}
$$

A disjoint partial collection is also permitted. For each $j$, choose an arbitrary deterministic time-dependent sequence of relative characters $\nu_{r,j}$. Put

$$
K_{r,j}=\mathcal Q_{\nu_{r,j}}(E_N)M_N,\qquad
R_{r,j}=U_N-K_{r,j}.
\tag{1.2}
$$

The chosen transition at time $r$ for group $j$ is
$\chi\mapsto\nu_{r,j}(\mathsf S\chi)$. It is a permutation, so its input and output blocks are pairwise orthogonal. Therefore

$$
\|K_{r,j}\|\le\rho,\qquad
N^{-1/2}\|K_{r,j}\|_{\rm HS}\le\overline\sigma,\qquad
\|R_{r,j}\|\le2-g.
\tag{1.3}
$$

Set

$$
z=\frac{g}{2(2-g)},\qquad
\delta=\frac{-\log(1-g/2)}{2\log(2(2-g)/g)},\qquad
\eta=\sqrt{1-g/2}.
\tag{1.4}
$$

Let $S_{n,j}$ be the sum of the terms in

$$
(K_{n,j}+R_{n,j})\cdots(K_{1,j}+R_{1,j})
\tag{1.5}
$$

with at most $\lfloor\delta n\rfloor$ factors $R_{r,j}$.
Since $0<\delta<1$, every retained term contains at least one factor $K_{r,j}$. Put one such factor in Hilbert--Schmidt norm, and use operator norms on the remaining factors. If there are $a$ factors $R$, the resulting bound is

$$
N^{-1/2}\|\text{word}\|_{\rm HS}
\le\overline\sigma\,\rho^{n-a-1}(2-g)^a.
\tag{1.6}
$$

For either norm, the relevant binomial sum is estimated exactly as follows:

$$
\begin{aligned}
\sum_{a\le\delta n}\binom na\rho^{n-a}(2-g)^a
&\le z^{-\delta n}\sum_{a=0}^n\binom na\rho^{n-a}((2-g)z)^a\\
&=z^{-\delta n}(\rho+(2-g)z)^n\\
&=(1-g/2)^{-n/2}(1-g/2)^n=\eta^n.
\end{aligned}
\tag{1.7}
$$

Here $0<z<1$, and $z^{-a}\le z^{-\delta n}$ for every retained integer $a$. Consequently

$$
\boxed{\quad
\|S_{n,j}\|\le\eta^n,\qquad
N^{-1/2}\|S_{n,j}\|_{\rm HS}
\le\frac{\overline\sigma}{\rho}\eta^n.
\quad}
\tag{1.8}
$$

No time-independence of a route is used.

Define the block-diagonal sum

$$
T_n=\sum_{j=1}^J P_jS_{n,j}P_j,\qquad s_n=\operatorname{Tr}T_n.
\tag{1.9}
$$

This trace is precisely the coherent sum of the selected closed character histories: each initial character in $A_j$ is assigned the route numbered $j$. To check this assertion, expand all factors by the character resolutions and use

$$
\operatorname{Tr}(P_jS_{n,j}P_j)
=\sum_{\chi\in A_j}\operatorname{Tr}(P_\chi S_{n,j}P_\chi).
\tag{1.10}
$$

An off-diagonal initial/final character block has zero trace. Histories belonging to different $A_j$ have disjoint starting characters, and so are not counted twice. A full partition in (1.1) can cover the entire starting space. Thus the construction is not restricted to a subspace of small rank.

## 2. Square-root dependence on the number of groups

The summands in (1.9) have orthogonal input and output spaces. Thus (1.8) gives

$$
\|T_n\|\le\eta^n,\qquad
\|T_n\|_{\rm HS}^2
=\sum_j\|P_jS_{n,j}P_j\|_{\rm HS}^2
\le JN\left(\frac{\overline\sigma}{\rho}\right)^2\eta^{2n}.
\tag{2.1}
$$

Using $|\operatorname{Tr}T|\le\sqrt N\|T\|_{\rm HS}$ and also the operator-norm estimate yields

$$
\boxed{\quad
\frac{|s_n|}{N}
\le\frac{\sqrt J\,\overline\sigma}{\rho}\eta^n,
\qquad
\frac{|s_n|}{N}\le\eta^n\le1.
\quad}
\tag{2.2}
$$

Let $p_n=\operatorname{Tr}U_N^n$, and let the deterministic complex weights satisfy $\sup_{n,N}|w_{n,N}|\le W$. Since $|p_n|/N\le1$, the exact square identity implies

$$
\frac{\big||p_n|^2-|p_n-s_n|^2\big|}{N^2}
\le 2\frac{|p_n|}{N}\frac{|s_n|}{N}
+\frac{|s_n|^2}{N^2}
\le3\frac{|s_n|}{N}.
\tag{2.3}
$$

Sum (2.2), and use $\rho\ge1/2$ and $1-\eta\ge g/4$. This proves

$$
\boxed{\quad
\frac1{N^2}\sum_{n\ge1}|w_{n,N}|
\big||p_n|^2-|p_n-s_n|^2\big|
\le24W\,\frac{\sqrt J\,\overline\sigma}{g}.
\quad}
\tag{2.4}
$$

The bound includes the entire cross-term with the retained trace. The difference series in (2.4) is absolutely convergent even if the bounded weights do not decay. Separate convergence of the two series of squared traces is not asserted.

The estimate is uniform over all partitions and prescribed routes. The partition and routes may even be chosen separately for each $n$, provided the number of groups is always at most $J$.

## 3. A growing family for the exact original matrices

The precise sufficient condition for (2.4) to tend to zero is

$$
\frac{\sqrt{J_N}}{g_N}
\left(d^{-1}+C N^{-1/32}\right)\longrightarrow0.
\tag{3.1}
$$

In particular, the sufficient growth condition

$$
J_N=o\!\left(g_N^2\min(d^2,N^{1/16})\right)
\tag{3.2}
$$

follows by applying the displayed inequality to each of the two summands.

For the original matrices, the frozen growing-order escape result gives, uniformly when

$$
\log d\ge C_2(\log N)^{2/3},
\tag{3.3}
$$

the valid compression gap

$$
g_N=\tfrac12\exp\!\left[-2C_3(\log N)^{1/3}\log\log N\right].
\tag{3.4}
$$

One completely explicit choice is

$$
J_N=\left\lfloor\min(d,N^{1/32})\right\rfloor.
\tag{3.5}
$$

Indeed,

$$
\frac{\sqrt{J_N}\,\overline\sigma}{g_N}
\le\frac1{g_N}\left(d^{-1/2}+C N^{-1/64}\right)\longrightarrow0.
\tag{3.6}
$$

For the first term, the negative exponent of size $(\log N)^{2/3}$ from (3.3) dominates the positive exponent of size $(\log N)^{1/3}\log\log N$ from (3.4). The second term tends to zero because $g_N^{-1}=N^{o(1)}$.

Thus the original squared traces may be corrected by the coherent family (1.9), with $J_N\to\infty$, at total error $o(1)$ for every bounded array of pair weights. Near the lower divisor scale (3.3), one may take $J_N=d$ and partition all $d^2$ initial characters into $d$ groups of $d$ characters. Every group may follow a different route, changing at each time. At $n$ comparable to $N$, each such route permits $N^{1-o(1)}$ deviations, while the permitted fraction tends to zero.

This controls a meaningful growing collection of prescribed routes. It does not sum the unrestricted set of all routes. Taking $J_N=d^2$ is not justified by (3.1), whose $d^{-1}$ contribution would then already be $1/g_N$.

## 4. Exact Parseval and closure: the remaining loss for arbitrary routes

For this section use all relative-character components

$$
K_\nu=\mathcal Q_\nu(E_N)M_N.
\tag{4.1}
$$

For $g\in G$, the matrix

$$
U_g=H_gE_NH_g^*M_N=\sum_{\nu\in\widehat G}\nu(g)K_\nu
\tag{4.2}
$$

is unitary. For a route $\boldsymbol\nu=(\nu_1,\ldots,\nu_n)$, put

$$
B_{\boldsymbol\nu}=K_{\nu_n}\cdots K_{\nu_1},\qquad
c_{\boldsymbol\nu}=\operatorname{Tr}B_{\boldsymbol\nu}.
\tag{4.3}
$$

Expanding the product of (4.2) and applying finite character orthogonality independently in each $g_j$ proves the exact identities

$$
\sum_{\boldsymbol\nu}\|B_{\boldsymbol\nu}\|_{\rm HS}^2
=\frac1{q^n}\sum_{g_1,\ldots,g_n}
\|U_{g_n}\cdots U_{g_1}\|_{\rm HS}^2=N,
\tag{4.4}
$$

$$
\sum_{\boldsymbol\nu}|c_{\boldsymbol\nu}|^2
=\frac1{q^n}\sum_{g_1,\ldots,g_n}
\left|\operatorname{Tr}(U_{g_n}\cdots U_{g_1})\right|^2.
\tag{4.5}
$$

These are auxiliary finite Fourier identities. They do not replace the original statistic by an averaged model.

Write the character group additively in the rest of this section. The route $\boldsymbol\nu$ maps a starting character $\chi$ to

$$
\mathsf S^n\chi+\xi_{\boldsymbol\nu},\qquad
\xi_{\boldsymbol\nu}=\sum_{j=1}^n\mathsf S^{n-j}\nu_j.
\tag{4.6}
$$

Let

$$
F_n=|\ker(\mathsf S^n-I:\widehat G\to\widehat G)|.
\tag{4.7}
$$

The affine map in (4.6) has either no fixed character or exactly $F_n$ fixed characters. All trace contributions of $B_{\boldsymbol\nu}$ lie in the sum $P$ of those fixed character spaces, of rank $mF_n$. Therefore

$$
|c_{\boldsymbol\nu}|^2
=|\operatorname{Tr}(PB_{\boldsymbol\nu}P)|^2
\le mF_n\|PB_{\boldsymbol\nu}P\|_{\rm HS}^2
\le mF_n\|B_{\boldsymbol\nu}\|_{\rm HS}^2.
\tag{4.8}
$$

Combining this with (4.4) gives

$$
\sum_{\boldsymbol\nu}|c_{\boldsymbol\nu}|^2
\le\frac{N^2F_n}{q}.
\tag{4.9}
$$

The map from routes to $\xi_{\boldsymbol\nu}$ is surjective, with every fiber of size $q^{n-1}$, because the coefficient of $\nu_n$ in (4.6) is the identity. Closure is possible precisely when
$\xi_{\boldsymbol\nu}\in\operatorname{im}(I-\mathsf S^n)$, a set of size $q/F_n$. Hence exactly

$$
\frac{q^n}{F_n}
\tag{4.10}
$$

routes can potentially have a nonzero trace. Internal cancellation may make some of those traces zero; (4.10) counts the routes allowed by the closure constraint.

For any collection $\mathcal R$ of $L_{\mathcal R}$ such routes, Cauchy--Schwarz and (4.9) give

$$
\frac1N\left|\sum_{\boldsymbol\nu\in\mathcal R}c_{\boldsymbol\nu}\right|
\le\sqrt{\frac{L_{\mathcal R}F_n}{q}}.
\tag{4.11}
$$

For the complete potentially closed set, the resulting factor is

$$
\sqrt{\frac{q^n}{F_n}\frac{F_n}{q}}
=q^{(n-1)/2}=d^{n-1}.
\tag{4.12}
$$

Thus this combination of exact Parseval and exact trace closure leaves an exponentially large loss in time. Unitarity independently bounds the full normalized trace by one, but these identities do not make that bound vanish.

Equivalently, the original trace is the finite Fourier polynomial in (4.2) evaluated with every $g_j=0$. Parseval controls its coefficient square sum, while evaluation at this single point can add the coefficients coherently. Formula (4.12) quantifies the remaining loss for this direct argument.

## 5. The square-root loss in the grouped estimate is norm-sharp

Here is an elementary example showing that the factor $\sqrt J$ in Section 2 cannot be removed from an assertion based only on the displayed individual norm bounds.

Let $J$ divide $N$, choose orthogonal projections $P_1,\ldots,P_J$ of equal rank $N/J$ with sum $I$, and let

$$
B_j=aP_j,\qquad 0<a\le1.
\tag{5.1}
$$

Then

$$
\|B_j\|=a,\qquad
N^{-1/2}\|B_j\|_{\rm HS}=\frac a{\sqrt J},
\qquad
\sum_jP_jB_jP_j=aI.
\tag{5.2}
$$

The normalized trace of the sum is exactly $a$, which is $\sqrt J$ times the individual normalized Hilbert--Schmidt bound. All block orthogonality statements used in Section 2 hold exactly.

These $B_j$ are not claimed to be history operators for the original matrices. The example proves optimality under those norm and block assumptions alone. Any improvement for the original matrices must establish an additional property.

## 6. Flat relative components do not preclude an exact trace revival

A second finite-dimensional example addresses the full route sum. It preserves exact character decompositions, a metaplectic-style permutation of the character spaces, and perfect one-step flatness, but has a trace revival.

Let $d\ge3$ be odd, let $G=(\mathbb Z/d\mathbb Z)^2$, and let the dimension be $N=q=d^2$. Use the character basis indexed by $x\in G$, with rank-one projections $P_x$. The discrete Fourier matrix is

$$
(\mathcal F_G\psi)(x)=\frac1d\sum_{y\in G}e_d(x\cdot y)\psi(y).
\tag{6.1}
$$

Finite character orthogonality gives

$$
\mathcal F_G^2\psi(x)=\psi(-x),\qquad \mathcal F_G^4=I.
\tag{6.2}
$$

Let $M$ be any unitary monomial matrix implementing the prescribed character permutation $\mathsf S$, with arbitrary phases. For example, after passing to its character basis, the exact $M_N$ for $N=d^2$ has this form. Define the auxiliary matrices

$$
\widetilde E=\mathcal F_GM^{-1},\qquad
\widetilde U=\widetilde E M=\mathcal F_G.
\tag{6.3}
$$

Right multiplication by $M^{-1}$ permutes columns and multiplies them by unit phases. Consequently every entry of $\widetilde E$ has modulus $1/d$. Every rank-one compression satisfies

$$
\|P_y\widetilde E P_x\|=\frac1d.
\tag{6.4}
$$

For each relative character $\nu$, the matrix
$\mathcal Q_\nu(\widetilde E)=\sum_xP_{\nu+x}\widetilde E P_x$
has exactly one nonzero entry in every row and column, all of modulus $1/d$. It is $1/d$ times a unitary monomial matrix. Hence

$$
\|\mathcal Q_\nu(\widetilde E)\|=\frac1d,\qquad
\frac1N\|\mathcal Q_\nu(\widetilde E)\|_{\rm HS}^2=\frac1{d^2}.
\tag{6.5}
$$

The different $\mathcal Q_\nu(\widetilde E)$ are exactly orthogonal in Hilbert--Schmidt norm, and all identities in Section 4 hold. Nevertheless,

$$
\operatorname{Tr}\widetilde U^4=N.
\tag{6.6}
$$

Therefore a universal implication from small compression norms, flat relative-character Hilbert--Schmidt masses, their orthogonality, and the trace-closure constraint to a vanishing full normalized trace is false. The example has these properties in their strongest flat form and still exhibits coherent revival.

The auxiliary kick $\widetilde E$ is not asserted to equal $e^{i\tau N A_N}$. Thus (6.6) is not a counterexample to the original $H_{\rm diag}$, and it is not a replacement of the original family in Sections 1--3. Its sole role is a verified obstruction to a closure lemma based only on the stated norms and exact orthogonality.

## 7. Scope of the advance

Sections 1--3 prove a complete signed error estimate for a growing coherent family of prescribed sparse routes, over the full starting character space, throughout the stated divisor range for the original matrices. The exact remaining criterion is (3.1), and (3.2)--(3.6) exhibit useful growth rates.

Sections 4--6 establish the remaining limitations of these inputs with finite exact calculations. They provide neither quantum decorrelation for the unrestricted histories nor any higher-order comparison required by $H_{\rm diag}$. Those estimates remain to be proved.
