> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/dual_singular_gap_graph_comparison.md`. Embedded SHA256: `6b867aaaace2d9f52edea61d3cc24fa07a7dbc0bb096ed992d2b4dab8df787c2`.
> [Thematic guide](../../topics/closure.md).

# A stronger effective singular gap from the exact Weyl transition graph

Research continuation, 21 October 2026.

This note uses the exact prescribed family and the fixed $\tau=10^{-80}$,
for all odd $N\ge3$, $N\ne7$. It supplements, without changing, these
frozen notes:

- `dual_weyl_primitivity_and_quantitative_limits.md`, SHA-256
  `90cb06de5c56441dfdb17f6fa32a35484b00c7919bbddd899fb8954f950043c1`;
- `dual_coherent_participation_and_fejers.md`, SHA-256
  `8a0779ea28cd664bf207e50fa2c71f908479b2dd1f5bacde414a87e3352825d1`.

The improvement replaces a long-path minorization by a reversible graph
comparison for $P^tP$. It proves a stronger effective rate for the exact
Markov matrix, but its present arithmetic constant still gives no control at
times of order N.

## 1. Statement

As before, put
$$
\Lambda=(\mathbb Z/N\mathbb Z)^2\setminus\{0\},\quad M=N^2-1,
\quad C=C_N(\tau)|_\Lambda,\quad P=|C|^{\circ2},
\quad\Pi=M^{-1}\mathbf1\mathbf1^t.
$$
Let $s_2(P)$ be the operator norm of P on the orthogonal complement of
the uniform vector. For a doubly stochastic P this equals its second singular
value, counted with multiplicity. The first frozen note proves that every
nonzero entry of P is at least
$$
\varepsilon_N=e^{-2F_N},
\tag{1.1}
$$
where $F_N$ is its explicit, finite exponential-form bound.
Define
$$
\delta_N=\frac25 e^{-4F_N}\sin^2\frac\pi N.
\tag{1.2}
$$

**Theorem E.** For this exact family,
$$
\boxed{\delta_N\le1-s_2(P)^2
 \le\frac{64\pi^2}{4375}\tau^2.}
\tag{1.3}
$$
In particular,
$$
\|P^n-\Pi\|_{2\to2}
 \le(1-\delta_N)^{n/2}
 \le e^{-\delta_N n/2},\qquad n\ge0.
\tag{1.4}
$$
The lower bound obeys
$$
\delta_N\ge\frac8{5N^2}e^{-4F_N},
\tag{1.5}
$$
by $\sin(\pi/N)\ge2/N$. This substantially improves the earlier
$\exp(-12N^2F_N)$-scale lower bound obtained from a complete positive
matrix power. It is a singular-value bound, so it also bounds all nontrivial
eigenvalues in modulus. The upper bound in (1.3) concerns the one-step singular
gap, not a necessary lower bound of order $\tau^{-2}$ on every mixing time
of this nonnormal matrix.

## 2. Squaring P exposes the elementary graph directly

Set $R=P^tP$. This is real symmetric, positive semidefinite and doubly
stochastic. Recall the exact support statements from the first frozen note:
$$
P_{w,S^{-1}w}>0,
\qquad
P_{w+\kappa,S^{-1}w}>0
\tag{2.1}
$$
for every nonzero w and every allowed elementary step
$$
w=(k,l)\longleftrightarrow w+(\pm1,0)\quad(l\ne0),
$$
$$
w=(k,l)\longleftrightarrow w+(0,\pm1)\quad(k\ne0),
\tag{2.2}
$$
with $S=\begin{pmatrix}3&2\\4&3\end{pmatrix}$. All listed endpoints
remain nonzero. The support proof uses the exact alias coefficients and
Lindemann--Weierstrass at the given algebraic kick, and was proved for composite
N as well. Combining the two entries in the common row $w+\kappa$ gives
$$
R_{S^{-1}(w+\kappa),S^{-1}w}
\ge P_{w+\kappa,S^{-1}(w+\kappa)}
     P_{w+\kappa,S^{-1}w}
\ge\varepsilon_N^2.
\tag{2.3}
$$
Thus, after relabeling by S, R contains the undirected elementary graph (2.2)
with every edge weight at least $\varepsilon_N^2$. No simulation by
$\operatorname{ord}_N S$ consecutive steps is needed here.

## 3. Poincare inequality for the elementary graph, uniformly over composite N

Represent residues by $0,1,\ldots,N-1$. For a function x on $\Lambda$,
let its graph energy be
$$
\mathcal E_G(x)=
 \sum_{l\ne0}\sum_k|x(k+1,l)-x(k,l)|^2
 +\sum_{k\ne0}\sum_l|x(k,l+1)-x(k,l)|^2,
\tag{3.1}
$$
where additions are modulo N. Each undirected cycle edge is counted once
since $N\ge3$. We prove
$$
\boxed{\mathcal E_G(x)\ge\frac25\sin^2\frac\pi N
 \sum_{v\in\Lambda}|x(v)-\bar x_\Lambda|^2.}
\tag{3.2}
$$

Extend x to the full torus by setting $\widetilde x(0,0)=x(1,1)$.
Its full nearest-neighbor torus energy consists of (3.1) and the missing
horizontal edges in row zero and vertical edges in column zero. Every missing
horizontal edge can be expressed by one of the following paths in G, with
$(0,0)$ interpreted as the anchor $(1,1)$:

- For $1\le k\le N-2$, the row-zero edge from $(k,0)$ to
  $(k+1,0)$ uses
  $(k,0),(k,1),(k+1,1),(k+1,0)$.
- The row-zero edge from $(0,0)$ to $(1,0)$ uses
  $(1,1),(1,0)$.
- The row-zero edge from $(N-1,0)$ to $(0,0)$ uses
  $(N-1,0),(N-1,1),(0,1),(1,1)$.

The missing vertical edges use the transposed paths:

- For $1\le l\le N-2$, use
  $(0,l),(1,l),(1,l+1),(0,l+1)$.
- From $(0,0)$ to $(0,1)$, use $(1,1),(0,1)$.
- From $(0,N-1)$ to $(0,0)$, use
  $(0,N-1),(1,N-1),(1,0),(1,1)$.

All paths have at most three edges. The horizontal-edge paths use each vertical
edge between row zero and row one at most twice, and each horizontal edge in
row one at most once. The vertical-edge paths use each horizontal edge between
column zero and column one at most twice, and each vertical edge in column one
at most once. The only overlaps between these two descriptions have total use
at most three. Therefore every edge of G is used by the entire list at most
three times. This count remains valid at N=3; no unit-residue property is used.

By $|a_1+\cdots+a_j|^2\le j\sum_i|a_i|^2$ along each path, the missing
energy is at most $9\mathcal E_G(x)$. Consequently
$$
\mathcal E_{\rm torus}(\widetilde x)\le10\mathcal E_G(x).
\tag{3.3}
$$
The Fourier characters on the full discrete torus diagonalize its Laplacian,
with eigenvalues
$$
4\sin^2\frac{\pi a}N+4\sin^2\frac{\pi b}N,
\qquad(a,b)\in(\mathbb Z/N\mathbb Z)^2.
$$
This follows by substituting a character into the four nearest-neighbor
differences. Orthogonality of the characters then gives
$$
\mathcal E_{\rm torus}(\widetilde x)
\ge4\sin^2\frac\pi N
 \sum_{v\in(\mathbb Z/N\mathbb Z)^2}
  |\widetilde x(v)-\bar{\widetilde x}|^2.
\tag{3.4}
$$
The last variance is at least $\sum_{v\in\Lambda}|x(v)-\bar x_\Lambda|^2$:
discard the nonnegative anchor term and minimize the remaining sum over the
choice of its mean. Equations (3.3), (3.4) prove (3.2).

## 4. From the graph inequality to contraction of the exact P

For a symmetric doubly stochastic matrix R,
$$
\langle x,(I-R)x\rangle
=\frac12\sum_{u,v}R_{uv}|x(u)-x(v)|^2.
\tag{4.1}
$$
This follows by expanding the square and using the row and column sums. Use
(2.3), and relabel x by the bijection S. For $x\perp\mathbf1$, (3.2)
therefore gives
$$
\langle x,(I-P^tP)x\rangle
\ge\varepsilon_N^2\mathcal E_G(x\circ S^{-1})
\ge\delta_N\|x\|_2^2.
\tag{4.2}
$$
Both P and its transpose preserve $\mathbf1^\perp$. Thus (4.2) is exactly
$s_2(P)^2\le1-\delta_N$. Taking powers of its operator-norm bound proves
(1.4). For $0\le t\le\pi/2$, concavity of sine gives
$\sin t\ge2t/\pi$; insert $t=\pi/N$ to obtain (1.5).

For example, every initial probability vector $p_0$ satisfies
$$
\|P^n p_0-M^{-1}\mathbf1\|_{\rm TV}
\le\frac{\sqrt M}{2}e^{-\delta_Nn/2}.
\tag{4.3}
$$
Indeed, total variation is one half the one-norm, the one-norm is at most
$\sqrt M$ times the two-norm, and
$\|p_0-M^{-1}\mathbf1\|_2\le1$.

## 5. An actual upper bound on the one-step singular gap

The low-frequency column gives a useful quantitative check on what (1.4)
can and cannot mean. Put $w=(1,0)$ and $v=S^{-1}w$ modulo N. The exact
dual factorization gives $Ce_v=e^{\tau G_N}e_w$.
For this w, the generator formula of the first note has
$\omega(\kappa,w)=\kappa_l$. The pure-q terms commute with $W_N(w)$,
while the mixed Fourier terms have $\kappa_l=\pm1$. Their total absolute
coefficient sum is
$$
2|\gamma|\sum_k|r_k|=2\cdot\frac1{200}\cdot4=\frac1{25}.
$$
The exact sine coefficient obeys
$2N|\sin(\pi/N)|\le2\pi$, including all small-modulus aliases after
the triangle inequality. Hence
$$
\|G_Ne_w\|_2\le\|G_Ne_w\|_1\le\frac{2\pi}{25}.
\tag{5.1}
$$
The generator is skew Hermitian, so its exponential is unitary. The elementary
integral identity
$$
(e^{\tau G_N}-I)e_w=\int_0^\tau e^{tG_N}G_Ne_w\,dt
$$
gives $\|(e^{\tau G_N}-I)e_w\|_2\le2\pi\tau/25$, with no restriction
on $\tau N$. It follows that
$$
P_{w,v}\ge1-\epsilon,\qquad
\epsilon=\frac{4\pi^2}{625}\tau^2.
\tag{5.2}
$$
To check the implication, if a is the w coordinate of the unit vector
$e^{\tau G_N}e_w$, then
$1-|a|^2\le2(1-\Re a)=\|(e^{\tau G_N}-I)e_w\|_2^2$.

Use the mean-zero vector $x=e_v-M^{-1}\mathbf1$. Its squared norm is
$1-1/M$, while
$$
\|Px\|_2^2=\sum_uP_{u,v}^2-\frac1M
\ge(1-\epsilon)^2-\frac1M
\ge1-2\epsilon-\frac1M.
$$
Taking its Rayleigh quotient yields
$$
1-s_2(P)^2\le\frac{2\epsilon}{1-1/M}
\le\frac{16}{7}\epsilon
=\frac{64\pi^2}{4375}\tau^2,
$$
since $M\ge8$. This proves the second half of (1.3). It is a bound for an
actual low-frequency column, not an invalid uniform first-derivative lower
bound at labels of size N.

## 6. Improved explicit time in the coherent-probability obstruction

Retain the normalized Fejer averages $\mathscr Z_T,\mathscr P_T$ and
$\gamma_N=(N-2)/(N+1)$ from the second frozen note. By (1.4), putting
$s=\sqrt{1-\delta_N}$,
$$
\|\mathscr P_T-\Pi\|_{2\to2}
\le\frac1T\left(1+2\sum_{n\ge1}s^n\right)
=\frac{1+s}{T(1-s)}
=\frac{(1+s)^2}{T\delta_N}
\le\frac4{T\delta_N}.
\tag{6.1}
$$
Consequently the conclusions of Theorem D, including the fixed-label witness,
hold already for every
$$
T\ge T_N^*:=\left\lceil\frac{8M}{\gamma_N\delta_N}\right\rceil:
\tag{6.2}
$$
$$
\operatorname{Tr}(\mathscr Z_T-\mathscr P_T)\ge\frac{\gamma_N}{2},
\qquad
(\mathscr Z_T-\mathscr P_T)_{v_Nv_N}
\ge\frac{\gamma_N}{2M}.
\tag{6.3}
$$
There is also a time $N\le n<T_N^*$ with
$\operatorname{Tr}Z_n-\operatorname{Tr}P^n\ge\gamma_N/4$.
The earlier proof that removes times $n<N$ applies because
$\delta_N\le(2/5)(\pi/N)^2<4/N^2\le1/(N-1)$, so
$T_N^*\ge8M(N-1)/\gamma_N$.

The new finite scale is of size at most a polynomial factor in N times
$e^{4F_N}$, instead of $e^{12N^2F_N}$. These are explicit upper bounds
on a sufficient comparison time, not estimates of the true optimal mixing
time. The available $F_N$ is still far too large to place the discrepancy
at $n=O(N)$, and none of these positive-probability bounds establishes
the signed pair sum or higher-order $H_{\rm diag}$.
