> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_adjoint_reflection_obstruction.md`. Embedded SHA256: `e1fed89859b6e2b79b1ad66c5bd596147c100d2d15b16eadc57125e032a95d03`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Independent audit: flat adjoint involutions as a norm-only obstruction

21 October 2026. Auditor: /root/audit_uniform_word_r4.

## Source identity and verdict

Target: counter_adjoint_reflection_obstruction.md.

SHA-256: 7b800ee5f2b088a4e4449816ff4680e0079a6b48c5c7f3a2458ddda2741f266e.

The hash was recomputed. The frozen source was not changed.

**Verdict:** the auxiliary construction and all stated inequalities are
proved. The use of concentration is supported by a directly checked
published theorem with the right metric and constants. The construction
preserves exact unitary-conjugation structure and shows that the stated
entry and selected-route norm properties alone do not imply the desired
full trace statistics. It is not a counterexample for the family in the
original problem.

## 1. The published concentration theorem

The primary publication was opened directly:

Elizabeth S. Meckes and Mark W. Meckes, *Spectral measures of powers of
random matrices*, Electronic Communications in Probability 18 (2013),
paper 78, pages 1--13, DOI 10.1214/ECP.v18-2551.

Published PDF:

https://emis.muni.cz/journals/EJP-ECP/article/download/2551/2551-14838-1-PB.pdf

Author manuscript:

https://arxiv.org/pdf/1210.2681

**Corollary 17** is on printed page 12 of the publication, PDF index 11;
it is on printed page 13, PDF index 12, in the author manuscript
arXiv:1210.2681v3 dated 20 September 2013. Both statements were checked,
including page images. The page location given in the target is correct
for the explicitly identified author manuscript.

For a real $L$-Lipschitz function on one copy of $U(N)$, with the
ordinary, unnormalized Hilbert--Schmidt distance and normalized Haar
measure, the corollary gives

$$
 \mathbb P(F\ge\mathbb EF+s)
 \le \exp\left(-\frac{Ns^2}{12L^2}\right),\qquad s>0.
 \tag{1.1}
$$

The product-group independence assumption is vacuous for one factor.
The theorem is stated for $U(N)$, not only $SU(N)$, and does not
require that $F$ be invariant under the central circle. In the present
application the functions are real or imaginary parts of smooth matrix
coefficients, or their negatives; they satisfy the stated global
Lipschitz condition as verified below.

## 2. Exact centering on the traceless space

Let $R_0$ have $(N+1)/2$ eigenvalues $+1$ and $(N-1)/2$
eigenvalues $-1$. For odd $N$, $R(V)=VR_0V^*$ is a Hermitian
unitary with trace one. Consider

$$
 {\cal T}(X)=\mathbb E_V R(V)XR(V)^*.
$$

Haar invariance makes ${\cal T}$ commute with conjugation by every
unitary. Under diagonal conjugations, the character
$z_i\overline z_j$, $i\ne j$, has the one-dimensional matrix-unit
eigenspace spanned by $E_{ij}$. Therefore each $E_{ij}$ is an
eigenvector of ${\cal T}$. Permutation matrices make all these
eigenvalues equal to one scalar $\alpha$.

The unitary Hadamard change of basis on coordinates $i,j$ conjugates
$E_{ii}-E_{jj}$ to $E_{ij}+E_{ji}$. Applying covariance and conjugating
back proves that every diagonal difference also has eigenvalue $\alpha$.
These vectors span the traceless matrix space. Since ${\cal T}(I)=I$,
its full superoperator trace is $1+\alpha(N^2-1)$.

For each fixed $R$, the diagonal coefficient of the conjugation map
at $E_{ij}$ is $R_{ii}\overline{R_{jj}}$. Hence the full trace is
$|\operatorname{Tr}R|^2=1$. Linearity of trace and expectation therefore
gives $\alpha=0$, exactly.

For every nonzero Weyl label, $\operatorname{Tr}W_v=0$: a nonzero shift
has zero diagonal, while a zero shift with nonzero modulation has zero
character sum. Thus

$$
 f_{w,v}(V)=N^{-1}\operatorname{Tr}
             (W_w^*R(V)W_vR(V)^*)
$$

has mean zero whenever $v\ne0$, including all coefficients used in the
target. This centering is exact in every odd dimension, not an asymptotic
approximation.

## 3. Lipschitz normalization and the simultaneous bound

Telescoping the two factors of $VR_0V^*$, using their operator norms
one, gives

$$
 \|R(V)-R(V')\|_{\rm HS}\le2\|V-V'\|_{\rm HS}.
$$

Telescoping the two occurrences of $R$ in the coefficient and applying
Hilbert--Schmidt Cauchy--Schwarz gives

$$
 |f_{w,v}(V)-f_{w,v}(V')|
 \le \frac2{\sqrt N}\|R(V)-R(V')\|_{\rm HS}
 \le\frac4{\sqrt N}\|V-V'\|_{\rm HS}.
 \tag{3.1}
$$

The factor $N^{-1/2}$ arises from $N^{-1}\|W_w\|_{\rm HS}$, since
$\|W_w\|_{\rm HS}=\sqrt N$. There is no normalization of the group metric
in (3.1). Each signed real or imaginary part is therefore
$L=4/\sqrt N$-Lipschitz.

If $|f|\ge u$, one of those four real functions is at least
$u/\sqrt2$. Applying (1.1) to each, with its zero expectation, gives

$$
 \mathbb P(|f_{w,v}|\ge u)
 \le4\exp\left(-\frac{N^2u^2}{384}\right).
 \tag{3.2}
$$

There are $(N^2-1)^2<N^4$ label pairs. Substituting
$u=100\sqrt{\log N}/N$, the union bound is

$$
 4N^{\,4-10000/384}=4N^{-529/24}<1,\qquad N\ge3.
 \tag{3.3}
$$

For example $529/24>2$, so the last strict inequality follows already
from $4/3^2<1$. The arithmetic of both 384 and $529/24$ is correct.
No independence between different matrix coefficients is needed.

## 4. Deterministic choice and selected branches

The maximum of the finitely many coefficient moduli is a continuous
function of $V$ on compact $U(N)$. Its minimizers form a nonempty
compact set. Successively minimizing the real and imaginary parts of all
entries in a fixed order leaves nested nonempty compact sets. After the
finitely many coordinates, at most one matrix can remain, since its full
matrix entries are prescribed; compactness gives existence. This defines
a deterministic minimizer in every odd dimension.

Equation (3.3) supplies a matrix whose coefficient maximum is strictly
below the asserted threshold, so the minimizer obeys the required weak
inequality. Haar measure was used to prove existence of an auxiliary
matrix, not as randomness in its final definition.

For every permutation branch $K_\pi$, its singular values are the
selected coefficient moduli. Therefore, with $D=N^2-1$,

$$
 \|K_\pi\|\le a_N,\qquad
 D^{-1/2}\|K_\pi\|_{\rm HS}\le a_N,\qquad
 \|K_\pi\|_{S^p}\le D^{1/p}a_N.
$$

For $p=35$, the last expression is bounded by
$100N^{-33/35}\sqrt{\log N}$, which tends to zero. These conclusions
are uniform over all permutations.

The uniform entry bound also implies spatially weighted all-entry bounds
of the form used for the original family, after increasing a fixed
constant: centered labels satisfy $|v|_N\le N/\sqrt2$, whereas
$N^{-1}\sqrt{\log N}=O(N^{-1/17})$. This comparison concerns inequalities,
not the phase, locality, or dynamical construction behind the original
family.

## 5. Exact revival and failure of the auxiliary pair statistic

The selected unitary remains a conjugate of $R_0$, so its square is
the identity and its trace is one. Its trace is consequently $N$ at
every positive even time and one at every positive odd time. On the
traceless coefficient space, the exact supertrace identity gives

$$
 \operatorname{Tr}\widetilde C_N^n
 =|\operatorname{Tr}\widetilde U_N^n|^2-1
 =\begin{cases}0,&n\ \text{odd},\\N^2-1,&n\ \text{even}.
   \end{cases}
$$

Thus small one-step coefficients coexist with full coherent revival at
time two, within the exact adjoint representation of an original
$N$-dimensional unitary.

For a fixed nonzero admissible $b$, keep only pairs in the same
eigenphase cluster. Their unordered count is

$$
 \frac{r(r-1)+s(s-1)}2=\frac{(N-1)^2}{4},
 \qquad r=(N+1)/2,\quad s=(N-1)/2.
$$

All discarded terms are nonnegative. Nonnegativity also gives
$\int_0^1b_N^2\ge N^{-1}\int_{\mathbb R}b^2$ by retaining only equal
copies in the square. The exact CUE upper bound then yields

$$
 \Delta^{\rm auxiliary}_{2,N}(b)
 \ge\frac{(N-1)^2}{4N}\int b^2-\frac12\left(\int b\right)^2
 \longrightarrow+\infty.
$$

The strict positivity of $\int b^2$ follows from continuity and the
assumption $b\ne0$. The two eigenphase clusters have multiplicities,
so this is genuinely a factorial pair statistic, not a mistakenly
included self-pair contribution.

There is also a bounded-observable failure for this auxiliary family.
For a fixed interval $[-L,L]$, a microscopic point can be present only
if the random origin lies within $L/N$ of one of the two phases.
The probability is at most $4L/N$. Therefore every nonnegative smooth
test supported there has Laplace functional tending to one, the value
for the empty process. A nonzero nonnegative test has a strictly smaller
Laplace functional under Sine intensity one. Thus this conclusion does
not rely on inferring weak failure from divergent moments.

## 6. Logical boundary

The construction proves the stated obstruction to closure using only
entrywise bounds, a fixed entry gap, selected-permutation Hilbert--Schmidt
or Schatten estimates, and exact unitary-conjugation structure. It does
not preserve the prescribed kick, its finite Fourier symbol, its exact
center generating phase, or the cat dynamics.

Accordingly it cannot refute $H_{\rm diag}$ for
$U_N=e^{i\tau N A_N}M_N$. Its valid conclusion is that additional
information specific to that family is necessary for any argument
evaluating the full signed trace sum. No gap in the target's stated
auxiliary theorem was found.
