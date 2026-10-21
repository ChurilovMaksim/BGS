> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round6_2026_10_21/root_audit_rational_inner_and_dense_involution.md`. Embedded SHA256: `424e57074b1fe33005be0b9efc9820a6cf4ef103e151c60900e9ba71250e1ca4`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/histories.md).

# Second-reader audit: rational-inner occupations and the dense involution

Date: 21 October 2026. Reviewer: root. This is a direct reconstruction
and proof audit of the two named sources. It is not a Lean certificate,
an independent publication, or a claim of historical priority.

## 1. Sources and verdicts

The following sources were read in full, including their limitations:

1. `r6_occupation_rational_inner_kac.md`, SHA256
   `4bf2d0ef9ea39227cb0af38569df5432722799b32f322811a969a2ac85323e6a`.
2. `r6_dense_higher_block_involution.md`, SHA256
   `4a59d67a8196ae73555f6bea28b70c5566c76f0c4d24a160eb87e809a28b79ab`.

**Verdict for both: the stated theorems and stated obstruction examples
are proved.** Neither source proves the spectral limit for the original
family. Their explicit distinction between a signed total, a positive
subclass, and the original target must be retained.

## 2. Rational-inner normalization: reconstructed proof

For a finite unitary matrix, let
$$
A_{n,d}=n[z^d]\{-\log\det(I-ZU)\},\qquad |d|=n.
$$
Schur elimination at vertex $v$ gives
$$
\det(I-ZU)=Q(z_R)(1-z_v\phi_v(z_R)),\quad
\phi_v=a+bZ_R(I-DZ_R)^{-1}c.
$$
The norm identity
$$
1-|\phi_v|^2=\sum_{w\in R}(1-|z_w|^2)|y_w|^2,
\quad y=(I-DZ_R)^{-1}c,
$$
was recomputed from unitarity. It proves contractivity in the polydisc.
The exceptional boundary set where the polynomial $Q$ vanishes has
Haar measure zero by induction on the number of variables. At the other
boundary points the same identity proves unit modulus.

For $d_v=k$, the coefficient relation is
$$
A_{|d|,d}/|d|=k^{-1}[z_R^{d_R}]\phi_v^k.
$$
Radius Parseval, bounded dominated convergence, and monotone convergence
therefore give
$$
\sum_{d:d_v=k}|A_{|d|,d}|^2/|d|^2=1/k^2.
$$
There is no unproved interchange at a singular boundary point.

For the weighted identity, the determinant is multiaffine, so the
$z_w$ slice of $\phi_v$ is fractional linear. Its determinant
polynomial at the remaining variables equal to zero is exactly
$U_{vw}U_{wv}$. Under the source's stated nonvanishing assumption,
this is not the zero polynomial. The boundary slice is therefore
nonconstant almost everywhere. Stability of the denominator in the
open disc extends to $|q_1|\le|q_0|$ on the closed remaining polydisc;
a boundary common zero would contradict the nonzero determinant.
These facts justify a degree-one Blaschke function on almost every slice.

For its $k$-th power, the one-variable coefficient identity is
$\sum_j j|g_j|^2=k$, because the boundary logarithmic derivative is
$k$ times the Poisson kernel. The coefficients $g_j$ themselves are
bounded holomorphic functions in the remaining variables. Applying
Parseval to each such coefficient and then Tonelli to the nonnegative
sum proves
$$
\sum_{d:d_v=k}d_w |A_{|d|,d}|^2/|d|^2=1/k.
$$
In particular, the proof does **not** interchange an unbounded derivative
with the integral in the other variables. The normalization, first
moments, and support-weighted identity follow exactly as stated.

## 3. Arithmetic input and the divergent second moment

The original $A_N$ and $M_N$ have algebraic entries; the finite
spectral projectors of the Hermitian $A_N$ are algebraic polynomial
expressions in it. For each matrix entry,
$$
(U_N)_{vw}=\sum_\lambda(P_\lambda M_N)_{vw}e^{iN\tau\lambda}.
$$
The coefficients do not all vanish, since their sum is $(M_N)_{vw}\ne0$.
After zero coefficients are discarded, all exponents are distinct
algebraic numbers. The precise Lindemann--Weierstrass statement used in
the source was personally checked in Huang, ISSAC 2022, Theorem 1.1,
author PDF <https://arxiv.org/pdf/2112.05004>, page 1.
Thus every original matrix entry is nonzero, and all stated first-moment
identities apply at every odd dimension. This use of transcendence is
qualitative and supplies no small-denominator or phase-cancellation bound.

The Fourier-matrix example was recomputed:
$$
S_{01}(z)=\frac{1-iz}{\sqrt3(1-\omega z/\sqrt3)}.
$$
At $z=-i$, the denominator's squared modulus is $1/3$, and the
numerator has a simple zero. Hence $\delta(-ie^{it})=t^2(1+O(t))$.
The squared Blaschke coefficients give conditional second moment
$(2-\delta)/\delta$, whose integral diverges. The example disproves
the proposed general finite-second-moment inference even for an exactly
flat matrix. It is not an infinite-dimensional countersequence for the
prescribed family, nor does it satisfy every extra original-family
condition by assertion.

## 4. Higher-block involution: checks of multiplicity and connectivity

The higher-block transfer is an exact presentation of the original
closed-word traces. Its rectangular factorization is an $RS/SR$
identity, so the nonzero spectrum and determinant are unchanged.

A pseudoorbit is specified by a selected subset of block states and a
permutation of that subset. The involution chooses the first two selected
states with the same suffix by a rule depending only on the selected
set. Their outgoing rows agree. Swapping their successors therefore
preserves every directed physical-edge multiplicity, the full amplitude,
and the selected set. The same pair is selected after the operation;
there are no fixed points. The number of cycles changes by exactly one.
Thus this is an actual involution on unmarked objects, not a cancellation
of overcounted descriptions.

The survivor bijection with the lower-block presentation was checked in
both directions. Every lower-block state has exactly one selected
predecessor in its permutation; this supplies its unique first letter
when lifted. The determinant cancellation at cycle fugacity one is
therefore exact.

The fugacity refinement is essential:
$$
\mathscr Z_K(z,t)-\mathscr Z_{K-1}(z,t)
=t(1-t)\mathscr R_K(z,t).
$$
The factor $1-t$ kills the full determinant value at $t=1$, while
the coefficient of a single cycle at $t=0$ is generally nonzero.
The explicitly displayed rational orthogonal matrix gives
$[z^3]\mathscr R_2(z,0)=-128/243$. It was checked against the direct
expression $\sum_iU_{ii}(1-U_{ii}^2)$. Consequently the determinant
involution alone does not cancel the connected trace contribution.

## 5. Positive mass at long times

The original-family entry bound and singular mixing estimate are used
only after they have been proved in the preceding round. They imply
$P^6_{ab}\ge1/(2N)$ at large odd dimensions by the displayed
row/column sandwich argument in the source. Sampling a closed path every
six steps then bounds the vertex-simple mass by
$$
9\exp[-m(m-1)/(4N)],\qquad m=\lfloor n/6\rfloor.
$$
The closing transition was kept rather than silently treating the path
as an independent sample.

An equality of two length-$K$ blocks with $K<n/2$ imposes $K$
independent vertex identifications. The associated identification graph
is a forest, including overlapping blocks. Summing a spanning tree with
the stochastic transition weights leaves one redundant transition,
bounded by $C/N$, and each additional identification costs $C/N$.
This gives the stated $C\binom n2(C/N)^K$ bound. The exact finite
rank checks corroborate the combinatorics but are not used to infer it.

At $K=\lceil4\log_2N\rceil$ and $cN\le n\le BN$, these two
bounds prove that the nonvertex-simple but long-block-regular class has
positive $P$-mass $1+O_A(N^{-A})$. The canonical first-failure
involution pairs these one-cycle objects with two-cycle objects. This is
a theorem about positive path mass and an exact change of connectivity.
It gives no signed lower bound on the unresolved spectral remainder.

## 6. Boundaries retained in the cumulative report

The following inferences remain invalid and are not recorded as results:

- replacing the unknown original unequal-occupation sum by its phase
  average;
- inferring a CUE ramp from the occupation first moments;
- inferring finite occupation second moments from flat entries;
- using cancellation at determinant fugacity one as cancellation of its
  connected one-cycle coefficient;
- converting the positive path-mass statement into a lower bound for a
  signed total.

The sources' conclusions respect each of these boundaries.
