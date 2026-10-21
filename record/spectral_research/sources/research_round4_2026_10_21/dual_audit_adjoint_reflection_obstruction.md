> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/dual_audit_adjoint_reflection_obstruction.md`. Embedded SHA256: `dbabea71891ba19df2ff263f65ff8c80b2cb41285e6735ac5d5bb7bc44d33d0e`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/symmetry.md).

# Independent audit of the adjoint-flat reflection obstruction

21 October 2026. Separate audit by the dual-Weyl branch.

## 1. Frozen target and verdict

Target: `counter_adjoint_reflection_obstruction.md`, SHA-256
`7b800ee5f2b088a4e4449816ff4680e0079a6b48c5c7f3a2458ddda2741f266e`.
The entire target, Sections 1--7, was checked without modifying it.

**Verdict: proved as written.** The construction is a deterministic auxiliary
family of actual unitary conjugations with asymptotically small entries and
selected-route Schatten norms, but with exact coherent revivals, divergent
pair moments, and the empty vague limit. It is not the prescribed family and
does not refute H_diag for that family. The target states this restriction
explicitly and correctly.

The checks below include the only external probabilistic theorem and all its
application hypotheses. The mean, metric normalization, tail constants,
compact deterministic selection, pair normalization, and bounded-observable
conclusion were reconstructed independently.

## 2. Primary-source check of the concentration theorem

The primary [author PDF](https://arxiv.org/pdf/1210.2681) was opened and
Corollary 17 was read on printed page 13, PDF index 12; that page was also
retrieved as a screenshot. It is version 3 of 20 September 2013. The
[arXiv record](https://arxiv.org/abs/1210.2681) and
[publisher record](https://projecteuclid.org/journals/electronic-communications-in-probability/volume-18/issue-none/Spectral-measures-of-powers-of-random-matrices/10.1214/ECP.v18-2551.full)
confirm Meckes--Meckes, Electronic Communications in Probability 18 (2013),
article 78, pages 1--13, DOI 10.1214/ECP.v18-2551.

For one Haar U(N) factor the corollary gives, for real L-Lipschitz F in the
ordinary Hilbert--Schmidt distance,

$$
\Pr\{F\ge\mathbb EF+s\}\le\exp[-Ns^2/(12L^2)].
$$

The paper's Theorem 15 gives its supporting log-Sobolev constant 6/N.
The actual application uses exactly U(N), one factor, Haar law, real parts
or imaginary parts and their negatives, and ordinary HS metric. Independence
is vacuous for one factor. No geodesic or normalized-metric conversion is
inserted. The formula and hypotheses in the target match the source.

## 3. Exact Haar twirl and its mean zero

For odd N, the diagonal reflection R0 has (N+1)/2 positive and (N-1)/2
negative entries. Thus every R(V)=VR0V^* is Hermitian unitary with square I
and trace exactly one.

The averaged conjugation map T commutes with conjugation by every fixed
unitary, by Haar invariance. Under diagonal unitary conjugation each
off-diagonal matrix unit E_ij has a distinct character z_i conjugate(z_j).
The corresponding common character space is one-dimensional. Hence
T(E_ij)=alpha_ij E_ij. Permutation conjugations make all alpha_ij equal.

For a pair of coordinates the real unitary Hadamard matrix sends
E_ii-E_jj to E_ij+E_ji. Covariance then forces the same scalar action on
E_ii-E_jj. There is no unidentified diagonal component: conjugating the
already known image of E_ij+E_ji back by that Hadamard matrix determines the
whole image of the difference. These differences and off-diagonal units span
the entire traceless space. Meanwhile T(I)=I exactly.

The diagonal superoperator coefficient of conjugation by R at E_ij is
R_ii conjugate(R_jj); summing over i,j gives |Tr R|^2. In this construction
it is one. Therefore the trace of the average map is

$$
1+\alpha(N^2-1)=1,
$$

which proves alpha=0. The map is the scalar projection onto I and vanishes
on the traceless space. Every nonzero modular Weyl matrix is traceless:
a nonzero shift has zero diagonal, while a zero shift with nonzero character
has zero character sum, regardless of whether the nonzero residue is a unit.
Thus every relevant complex coefficient has exact Haar mean zero for every
odd N, including composite N.

## 4. Lipschitz normalization and all constants

Expanding R(V)-R(V') into its two changed unitary factors gives

$$
\|R(V)-R(V')\|_{\rm HS}\le2\|V-V'\|_{\rm HS}.
$$

In the coefficient f_(w,v), expand the two changed R factors separately.
After cyclic permutation, each term pairs R(V)-R(V') with a product of
unitaries of HS norm sqrt(N). The prefactor 1/N therefore makes each term
at most ||R(V)-R(V')||_HS/sqrt(N). Adding them proves the exact bound

$$
|f_{w,v}(V)-f_{w,v}(V')|
\le\frac4{\sqrt N}\|V-V'\|_{\rm HS}.
$$

Each of the four real functions Re f, -Re f, Im f, -Im f has this same
Lipschitz constant and mean zero. The event |f|>=u is contained in the
union of the four one-sided events at u/sqrt(2). The concentration exponent
therefore becomes

$$
\frac{N(u/\sqrt2)^2}{12(4/\sqrt N)^2}
=\frac{N^2u^2}{384}.
$$

There are (N^2-1)^2<N^4 relevant pairs. Substituting
a_N=100 sqrt(log N)/N into the union bound gives

$$
4N^4\exp[-10000\log N/384]
=4N^{4-625/24}=4N^{-529/24}<1
$$

for N>=3. In fact the exponent 529/24 is greater than two, so the last
quantity is bounded by 4/9. This verifies the stated strict existence
probability without relying on a numerical experiment. If a_N exceeds one
at a small dimension, the event is already impossible or the estimate is
simply nonsharp; this causes no logical problem.

## 5. Deterministic selection and exact conjugation structure

The maximum of finitely many continuous coefficient moduli is continuous on
compact U(N), hence has a nonempty compact set of global minimizers. At each
lexicographic coordinate step, minimizing that continuous real coordinate
over the previous compact set leaves a nonempty compact set. After the
finite list of real and imaginary entry coordinates, all coordinates are
fixed and at most one matrix remains. Nonemptiness then gives exactly one.
Thus the stated selection defines V_N deterministically; it does not leave
a random choice or a probabilistic subsequence.

The positive-probability existence bound places the minimum strictly below
a_N, which implies the advertised weak inequality. This proves the entry
bound in each odd dimension. Conjugating R0 by V_N preserves its two
eigenvalue multiplicities. Consequently

$$
\operatorname{Tr}\widetilde U_N^n=
\begin{cases}1,&n\text{ odd},\\N,&n\text{ even},\end{cases}
$$

and the exact adjoint trace identity, after subtracting its scalar identity
mode, gives zero at odd times and N^2-1 at every positive even time.
The restriction is an actual M by M unitary involution, not an arbitrary
unitary matrix inserted in place of quantum conjugation.

A selected permutation branch has singular values equal to its selected
entry moduli. Therefore its operator, normalized-HS, and Schatten-p bounds
are exactly the ones asserted. In particular

$$
\|K_\pi\|_{S^{35}}
\le100(N^2-1)^{1/35}N^{-1}\sqrt{\log N}
\le100N^{-33/35}\sqrt{\log N}\longrightarrow0,
$$

uniformly over all permutations. The maximum-entry estimate also implies
the weaker label-dependent 1/17 decay from the earlier norm theorem after
increasing a fixed constant: every centered label has size O(N), while
N^(-1) sqrt(log N) is bounded by a constant times N^(-1/17). No classical
phase representation, finite-shift symbol, or Egorov property is inferred
for this auxiliary family.

## 6. Pair-moment divergence, with multiplicities and normalization

Let r=(N+1)/2 and s=(N-1)/2. The ordered within-cluster pairs number
r(r-1)+s(s-1), and the factorial prefactor is one half. Direct arithmetic
gives

$$
\frac{r(r-1)+s(s-1)}2=\frac{(N-1)^2}{4}.
$$

All cross-cluster contributions are nonnegative because the admissible b
is nonnegative. Periodic translation invariance makes the integrals for the
two clusters identical. Thus the target's lower bound (6.1) has the correct
ordered/unordered normalization.

The squared nonnegative periodization dominates the sum of individual
squares. Tonelli and the change of variable x=N(t+ell) yield

$$
\int_0^1 b_N(t)^2\,dt\ge\frac1N\int_{\mathbb R}b(x)^2\,dx.
$$

The CUE bound is finite and independent of N: its positive semidefinite
matrix T has trace H=int b, so e_2(T)<=H^2/2. For every fixed nonzero
admissible b, continuity and nonnegativity imply int b^2>0. Therefore

$$
\Delta_{2,N}(b)
\ge\frac{(N-1)^2}{4N}\int b^2-\frac12\left(\int b\right)^2
\longrightarrow+\infty.
$$

The construction of an admissible nonzero b as a small positive multiple of
|g|^2, where g is the inverse transform of a smooth compactly supported
function, is valid: it is Schwartz, nonnegative, has bounded positive
supremum, and its Fourier transform is a smooth compactly supported
convolution. No additional existence hypothesis is hidden here.

## 7. Empty vague limit is a separate bounded-observable conclusion

For a fixed compact interval [-L,L], a point can occur only if the uniformly
chosen origin lies within L/N on the circle of either 0 or 1/2. The union
of these two arcs has measure at most 4L/N. Multiplicities change the number
of points on this rare event but do not increase its probability.

For any fixed nonnegative compactly supported test f inside this interval,

$$
0\le1-\mathbb E\exp(-\langle f,\Xi_N\rangle)
\le\Pr\{\Xi_N([-L,L])>0\}\le4L/N.
$$

This proves convergence of its Laplace functional to one. Directly in the
vague topology, a basic neighborhood of the zero measure imposes finitely
many compactly supported test constraints. Taking an interval containing
their supports, absence of every point in that interval puts the process
in the neighborhood. Its probability tends to one. Thus the laws converge
to the point mass at the empty measure. Equivalently any bounded continuous
functional converges in expectation to its value at zero, by continuity
at zero and the preceding neighborhood estimate.

There is no contradiction with unit intensity at each N: on the rare event
the count is of order N, so the first moments are not uniformly integrable.
This supplies a genuine bounded-observable obstruction to the sine-process
limit for the auxiliary family; it is stronger than just inferring weak
failure from divergent moments.

## 8. Scope of the obstruction

The auxiliary family satisfies the exact adjoint identity and much stronger
one-step entry and selected-branch norms than those already proved for the
prescribed kick family. Nevertheless its coherent powers revive at every
even time and its local law tends to the empty process. Thus these norm
properties alone cannot imply the required full signed trace comparison.

The example does not preserve or claim the original explicit action,
finite-shift generator, nonlinear classical dynamics, or WKB/Egorov data.
It therefore rules out only a closure argument that discards that additional
structure. The target does not present it as a counterexample to the original
U_N or as permission to average that family. This logical distinction is
necessary and is maintained throughout.
