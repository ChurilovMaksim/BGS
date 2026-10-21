> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/root_audit_dual_singular_gap.md`. Embedded SHA256: `7d08a0b146b5e802c282ef86a98de6b180878a24952f4de3cd0d8dd66b80c49a`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent root audit: singular gap of the exact dephased adjoint

21 October 2026.

Audited source: `dual_singular_gap_graph_comparison.md`, SHA-256
`6b867aaaace2d9f52edea61d3cc24fa07a7dbc0bb096ed992d2b4dab8df787c2`.
The source was read in full. Its two frozen dependencies were also read directly;
their audit verdicts were not used in place of the relevant arguments. The
primary Huang PDF, Theorems 1.1--1.2 and its definition of logarithmic height,
was opened directly by root during this turn.

## Verdict and scope

Theorem E and its stated finite-time consequences are proved as written for
the exact prescribed family, every odd N>=3 other than 7. The conclusion is
about P=|Ad(U_N)|^2 in the nonzero Weyl coordinates. It does not establish a
spectral gap for Ad(U_N), a useful Heisenberg-time mixing rate, or H_diag.

## 1. Nonzero edges and the algebraic quantitative input

The matrix is C=e^(tau G) P_S with S=[[3,2],[4,3]]. The exact modular Weyl
phase yields the coefficient -2N c_kappa (-1)^omega sin(pi omega/N).
The e_1 and e_2 alias coefficients are nonzero for every specified modulus;
the explicit exceptions N=3,5,9,11 were recomputed directly from the 32 modes.
At N=7, the complete symbol aliases to 9I/10, which explains the exclusion.

The permutation entry in row w and column S^-1 w has constant term 1.
The adjusted entry in row w+kappa and column S^-1 w has nonzero first
derivative for every allowed elementary edge. Every entry is a finite
exponential polynomial with algebraic coefficients and algebraic slopes.
Lindemann--Weierstrass therefore preserves each indicated edge at the exact
nonzero algebraic tau. This is nonvanishing, not an assumed lower bound.

For the actual lower bound, the spectral projectors of A lie in a splitting
field of degree at most 2N N!, the eigenvalues have logarithmic height <9,
and the projector product formula gives the stated polynomial height bound.
The grouping of equal exponents retains at most N^2 nonzero terms. The source's
F_N is an application of the explicitly verified published exponential-form
bound, not an unidentified minimum over entries. Consequently every selected
entry of P is at least epsilon_N=e^(-2F_N).

For R=P^t P, the common row w+kappa gives exactly

$$
R_{S^{-1}(w+\kappa),S^{-1}w}
\ge P_{w+\kappa,S^{-1}(w+\kappa)}
P_{w+\kappa,S^{-1}w}\ge\epsilon_N^2.
$$

This checks that the elementary edges appear directly in R, with the required
squared probability lower bound. No assumption of reversibility of P is made.

## 2. The comparison graph, including N=3

The graph on the torus minus the origin retains horizontal edges in rows l!=0
and vertical edges in columns k!=0. With x(0,0) set equal to x(1,1), the
source's six explicit path patterns replace every missing full-torus edge.
Each path has length at most three and stays in the retained graph.

The congestion count was checked separately at the intersecting row and
column. A vertical edge from row zero to row one appears in at most two
horizontal bypasses, and at most one transposed bypass. A horizontal edge
from column zero to column one obeys the transposed count. The other retained
edges appear no more often. The wrap-around paths obey the same rule at N=3:
the two edges adjacent to the anchor have total use three, not four.
Therefore the missing energy is at most 9 times the retained energy, and
E_torus<=10 E_G follows with no prime-modulus hypothesis.

Substitution of Fourier characters gives the full-torus Laplacian eigenvalues
4 sin^2(pi a/N)+4 sin^2(pi b/N). Its least positive eigenvalue is
4 sin^2(pi/N). The full-torus variance of the extended vector is at least the
variance on the punctured torus: discard the extra nonnegative term and
minimize over a common mean. Hence

$$
\mathcal E_G(x)\ge\frac25\sin^2(\pi/N)
\|x-\bar x\|_2^2.
$$

No normalization by the number of vertices is missing: both energy and
variance use counting measure, and each undirected edge is counted once.

## 3. Lower and upper singular-gap bounds

For symmetric doubly stochastic R, expanding the square gives
<x,(I-R)x>=1/2 sum R_uv |x_u-x_v|^2. Thus the preceding graph inclusion and
Poincare inequality give

$$
1-s_2(P)^2\ge\delta_N
=\frac25 e^{-4F_N}\sin^2(\pi/N).
$$

The mean-zero space is invariant under both P and P^t. This proves the power
bound by submultiplicativity of the Euclidean operator norm, without a
diagonalizability or normality assumption on P.

For the upper bound, at w=(1,0) only the mixed Fourier rows occur in G e_w.
Their total coefficient norm is 1/25; the sine coefficient is at most 2pi.
Aliasing can only reduce the triangle majorant. Thus ||G e_w||<=2pi/25.
The exact unitary Duhamel formula gives
||(e^(tau G)-I)e_w||<=2pi tau/25. If a is its w coordinate, then
1-|a|^2<=2(1-Re a), so the indicated stochastic entry is at least
1-epsilon with epsilon=4pi^2 tau^2/625. Testing P on
e_(S^-1 w)-1/M yields

$$
1-s_2(P)^2\le\frac{2\epsilon}{1-1/M}
\le\frac{64\pi^2}{4375}\tau^2,
\qquad M=N^2-1\ge8.
$$

This upper bound is for a singular gap. It does not assert a corresponding
lower bound on the optimal mixing time of a nonnormal stochastic matrix.

## 4. Finite Fejer comparison

The dependency's exact Schur-product expansion has nonnegative Fejer weights;
each summand Q_lambda circ conjugate(Q_mu) is positive semidefinite by the
tensor Gram construction. The eigenvalue-one projector of C has rank at least
N-1, so the coherent return average has trace at least
1+gamma_N, gamma_N=(N-2)/(N+1), at every positive averaging time.

For the Markov average, summing the geometric singular bound gives
||Pbar_T-Pi||<=4/(T delta_N). Its trace error is at most
4M/(T delta_N), and its selected diagonal error is at most
4/(T delta_N). This proves the claimed inequalities for
T>=ceil(8M/(gamma_N delta_N)). The removal of n<N in the individual-time
consequence retains the adequate margin since delta_N<4/N^2<=1/(N-1).

These are large, explicitly bounded finite times. The source correctly makes
no assertion that such a discrepancy occurs at n=O(N). The coherent return
observable sums squared moduli of diagonal entries of C^n; the original pair
statistic instead sums the diagonal entries themselves. These observables
are not identified in this audit or in the source's stated conclusion.
