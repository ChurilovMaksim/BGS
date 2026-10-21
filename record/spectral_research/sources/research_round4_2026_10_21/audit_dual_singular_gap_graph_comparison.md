> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_dual_singular_gap_graph_comparison.md`. Embedded SHA256: `139cfda2b82de6cb401ef50950f5a1465b04a081c2de253375151986b6823db9`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: singular gap from the exact elementary Weyl graph

Date: 21 October 2026. Auditor: `/root/audit_uniform_word_r4`.

## 1. Frozen scope and verdict

The audited source is `dual_singular_gap_graph_comparison.md`, SHA-256
`6b867aaaace2d9f52edea61d3cc24fa07a7dbc0bb096ed992d2b4dab8df787c2`.
The source was read in full and its hash checked before this audit. It was not
modified. The verdict is **proved as written**, for Theorem E and the stated
Fejer consequences, for all odd $N\ge3$, $N\ne7$.

This verdict concerns the exact stochastic matrix of squared Weyl coefficients.
It does not establish cancellation of coherent quantum traces or
$H_{\rm diag}$.

The prerequisites used below are the explicit support and exponential-entry
bounds from the frozen source
`dual_weyl_primitivity_and_quantitative_limits.md`, SHA-256
`90cb06de5c56441dfdb17f6fa32a35484b00c7919bbddd899fb8954f950043c1`.
Their algebraic, small-modulus, and composite-modulus arguments were independently
reconstructed in `audit_dual_weyl_primitivity_quantitative.md`, SHA-256
`fee116da2d8d0611ac624b3815212803c223774edcf4a5ec1997efc058e95dac`.
The exact Fejer participation inequality was independently reconstructed in
`audit_dual_coherent_fejers.md`, SHA-256
`2c7f66b1a47f0674d81f95016623c10bd51abbc6b519a4e47d331d09b556be42`.
Those recorded proofs, rather than another agent's agreement, are the
dependencies of this audit.

## 2. The common-row argument for $P^tP$

Use the notation
$$
\Lambda=(\mathbb Z/N\mathbb Z)^2\setminus\{0\},\quad M=N^2-1,
\quad C=C_N(\tau)|_\Lambda,\quad P_{uv}=|C_{uv}|^2,
\quad \Pi=M^{-1}\mathbf1\mathbf1^t.
$$
The restricted $C$ is unitary: the full adjoint action fixes the identity
Weyl vector, so its orthogonal complement is invariant. Consequently $P$
has nonnegative entries and both row and column sums equal to one.

Put $\varepsilon=e^{-2F_N}$. The support theorem gives, for every elementary
edge $w\leftrightarrow w+\kappa$,
$$
P_{w+\kappa,S^{-1}w}\ge\varepsilon,
\qquad P_{w+\kappa,S^{-1}(w+\kappa)}\ge\varepsilon.
$$
Both factors have the same row. Thus direct multiplication, with no powers of
$S$ or repeated transition argument, gives
$$
(P^tP)_{S^{-1}(w+\kappa),S^{-1}w}
 =\sum_uP_{u,S^{-1}(w+\kappa)}P_{u,S^{-1}w}
 \ge\varepsilon^2.
$$
Here $S=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$
has determinant one, so relabeling by $S$ is a bijection for every modulus.
No residue appearing in the graph argument must be a unit.

## 3. Exact path congestion, including $N=3$

Let $G$ contain horizontal cyclic edges in every nonzero row and vertical
cyclic edges in every nonzero column. Its energy $\mathcal E_G$ counts
each undirected edge once. This convention remains valid for a cycle of
length three.

Extend a function $x$ on $\Lambda$ to the missing origin with value
$x(1,1)$. The source's paths for horizontal edges missing from row zero
have the following exact multiplicities:

* Every vertical edge from $(k,0)$ to $(k,1)$, $k\ne0$, occurs
  twice. At $k=1$, one occurrence is the short anchor path and the other
  is the first length-three path. At $k=N-1$, the last ordinary path
  and the wrap path give the two occurrences. Interior columns have their
  two adjacent ordinary paths.
* Every horizontal edge in row one occurs once. The ordinary paths supply
  the edges with starting columns $1,\ldots,N-2$; the wrap path supplies
  the remaining two edges.

The transposed path family supplies every horizontal edge between columns
zero and one in a nonzero row twice, and every vertical edge in column one
once. A vertical edge can belong to both descriptions only at column one
between rows zero and one; its total multiplicity is three. Likewise the
only horizontal overlap occurs in row one between columns zero and one,
again with multiplicity three. All other multiplicities are at most two.
All paths have length at most three. This proves the claimed congestion
bound directly for every $N\ge3$; it does not depend on a large-modulus
picture or on numerical enumeration.

For completeness an auxiliary exact combinatorial enumeration was run at
$N=3,5,9,15,21,101$; it gave maximum congestion three and confirmed that
all listed path edges belong to $G$. The preceding argument is the proof;
the finite enumeration is only a check.

The squared telescoping estimate on a path of length $j\le3$ is
$$
|x(v_j)-x(v_0)|^2\le j\sum_{a=1}^j|x(v_a)-x(v_{a-1})|^2.
$$
Summing over missing edges therefore costs at most $9\mathcal E_G(x)$.
The full torus energy of the extension satisfies
$$
\mathcal E_{\rm torus}(\widetilde x)\le10\mathcal E_G(x).
$$

Discrete Fourier orthogonality gives eigenvalues
$4\sin^2(\pi a/N)+4\sin^2(\pi b/N)$ for the full torus Laplacian.
Its smallest nonzero eigenvalue is $4\sin^2(\pi/N)$. Also
$$
\sum_{v\in(\mathbb Z/N\mathbb Z)^2}
 |\widetilde x(v)-\overline{\widetilde x}|^2
\ge\min_{c\in\mathbb C}\sum_{v\in\Lambda}|x(v)-c|^2
=\sum_{v\in\Lambda}|x(v)-\bar x_\Lambda|^2.
$$
The first inequality discards the anchor term and then minimizes the
remaining expression. Consequently
$$
\mathcal E_G(x)\ge\frac25\sin^2\frac\pi N
 \sum_{v\in\Lambda}|x(v)-\bar x_\Lambda|^2.
$$

## 4. Singular contraction and normalization

The matrix $R=P^tP$ is symmetric, positive semidefinite, and doubly
stochastic. Expanding the squares, for complex $x$, yields
$$
\langle x,(I-R)x\rangle
 =\frac12\sum_{u,v}R_{uv}|x(u)-x(v)|^2.
$$
Because the sum counts both orientations of each graph edge, its factor
$1/2$ leaves precisely one copy. Section 2 and the graph inequality imply,
for $x\perp\mathbf1$,
$$
\langle x,(I-P^tP)x\rangle
\ge\frac25 e^{-4F_N}\sin^2\frac\pi N\,\|x\|_2^2
=\delta_N\|x\|_2^2.
$$
Both $P$ and $P^t$ preserve the mean-zero subspace. Hence this inequality
is exactly $s_2(P)^2\le1-\delta_N$, not merely an estimate of a real
part of an eigenvalue. Submultiplicativity on the invariant subspace proves
$$
\|P^n-\Pi\|_{2\to2}\le(1-\delta_N)^{n/2}
 \le e^{-n\delta_N/2}.
$$
Concavity of sine on $[0,\pi/2]$, evaluated at $\pi/N$, gives
$\delta_N\ge8e^{-4F_N}/(5N^2)$. The total variation bound in the source
then follows from $\|y\|_1\le\sqrt M\|y\|_2$ and
$\|p_0-M^{-1}\mathbf1\|_2^2\le1-1/M\le1$.

## 5. The actual low-column upper bound

Let $w=(1,0)$, $v=S^{-1}w$. The exact dual factorization is
$Ce_v=e^{\tau G_N}e_w$, with $G_N$ skew Hermitian. The pure-q Fourier
terms commute with the Weyl vector at $w$. For mixed terms the symplectic
integer is $\pm1$, so the absolute commutator coefficient is at most
$2N|\sin(\pi/N)|\le2\pi$ times the absolute symbol coefficient.

The Fourier coefficients of
$r=(1-\cos(14\pi q))(1+\cos(2\pi q))$ have absolute sum
$1+1+1+1/2+1/2=4$; each mixed sign has factor $1/200$.
The total absolute mixed coefficient sum is therefore $1/25$.
Even when distinct Fourier labels alias at a small modulus, the triangle
inequality gives
$$
\|G_Ne_w\|_2\le\|G_Ne_w\|_1\le2\pi/25.
$$
No first-order approximation in $\tau N$ is made. The exact integral
identity and unitarity give
$$
\|(e^{\tau G_N}-I)e_w\|_2\le2\pi\tau/25.
$$
For $a=(e^{\tau G_N})_{ww}$,
$1-|a|^2\le2(1-\Re a)$; the right side is the preceding squared norm.
Thus $P_{wv}\ge1-\epsilon$, where
$\epsilon=4\pi^2\tau^2/625$.

The mean-zero test vector $e_v-M^{-1}\mathbf1$ has squared norm
$1-1/M$, and its image under $P$ has squared norm
$\sum_uP_{uv}^2-1/M\ge1-2\epsilon-1/M$. Consequently
$$
1-s_2(P)^2\le\frac{2\epsilon}{1-1/M}
\le\frac{16}{7}\epsilon
=\frac{64\pi^2}{4375}\tau^2,
$$
where $M\ge8$. This argument remains valid at every small modulus in
the theorem, and its uniformity does not rely on controlling all columns
by their first derivative.

## 6. Fejer comparison time and scope

Write $s=\sqrt{1-\delta_N}$. Positive and negative Markov times in the
Fejer convention are powers of $P$ and $P^t$, respectively, with the
same contraction bound. Dropping the Fejer weights above gives
$$
\|\mathscr P_T-\Pi\|_{2\to2}
\le\frac1T\left(1+2\sum_{n\ge1}s^n\right)
=\frac{(1+s)^2}{T\delta_N}\le\frac4{T\delta_N}.
$$
The previous participation proof supplies a fixed label $v_N$ and
$\gamma_N=(N-2)/(N+1)$ with trace excess at least $\gamma_N$
over $\Pi$, and fixed-label diagonal excess at least $\gamma_N/M$.
The operator bound loses at most $M$ in trace and nothing on a diagonal
entry. Therefore every
$T\ge\lceil8M/(\gamma_N\delta_N)\rceil$ gives the stated trace and
diagonal discrepancies $\gamma_N/2$ and $\gamma_N/(2M)$.

To check the exclusion of early times, note
$$
\delta_N\le(2/5)(\pi/N)^2<4/N^2\le1/(N-1),
$$
where the last inequality is equivalent to $(N-2)^2\ge0$.
Thus the new $T_N^*$ is at least $8M(N-1)/\gamma_N$. Each individual
trace difference is bounded in absolute value by $M$, and its Fejer
coefficient is at most $2/T_N^*$. The whole contribution of
$1\le n<N$ is at most $\gamma_N/4$. A remaining time
$N\le n<T_N^*$ must have discrepancy at least $\gamma_N/4$, since
the total remaining nonnegative Fejer weights are at most one. This is the
same early-time deletion argument as in the independently checked source.

Finally, the bound on $\delta_N$ gives the explicit sufficient-time
estimate
$$
T_N^*\le5MN^2\gamma_N^{-1}e^{4F_N}+1.
$$
This improves the previous sufficient Markov comparison scale. It is not
a bound locating a coherent discrepancy at time $O(N)$. Likewise a
small one-step singular gap alone is not a lower bound on the mixing time
of a nonnormal matrix. The source states these scope restrictions correctly.

## 7. First unproved step beyond this theorem

No gap was found in the stated theorem. The step not supplied by this
theorem, and still needed for the original problem, is control of the
signed weighted sums of coherent powers (and their higher-order products)
on the original scale. A graph or singular-gap estimate for $|C|^{\circ2}$
does not identify $|C^n|^{\circ2}$ with $(|C|^{\circ2})^n$, and the
preceding Fejer argument explicitly exhibits this distinction.
