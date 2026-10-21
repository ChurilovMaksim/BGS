> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_endpoint_sine_audit.md`. Embedded SHA256: `b5862f0991191234860f1d728517d2c6b326ac9b1f5701659f50f6366dc5b97d`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: actual endpoint laws and sine compression

20 October 2026. The parameter remains exactly $\tau=10^{-80}$.

## 1. Input and verdict

The complete input read and checked is
arithmetic_endpoint_laws_and_sine_compression.md, SHA-256
$$
\text{8307e8bed074727caee3788adca79a44cab2fdf2627bbbfdcb2058a50863dfe1}.
$$
Its uses of the frozen signed-profile proof, positive transfer
construction, and the $C^1$ holomorphic graph construction were
also checked against those texts. **PASS.** No correction is needed.

The proved normalization is
$$
 \sigma=\frac{\mathbf1_{I_S}}{|I_S|}\,ds,\qquad
 \upsilon=\frac{\mathbf1_{I_U}}{|I_U|}\,du,\qquad
 c=\nu(Ag)(A\mathfrak h)(o)=\chi |I_S||I_U|.
$$
In particular this is an identification of the actual endpoint
measures in their actual scattering coordinates.

## 2. The transfer measure and its entropy

For a one-sided preimage $y=e x$, define
$$
 p(y)=w(y)\frac{\mathfrak h(y)}{\mathfrak h(x)},\qquad
 w(y)=\frac{l_{s(e)}}{\lambda l_{t(e)}}e^{v(y)}.
$$
The equation $T\mathfrak h=\mathfrak h$ gives
$\sum_{\sigma y=x}p(y)=1$. The measure
$\mu^+=\mathfrak h\nu$ is invariant under this normalized
backward kernel because
$$
 \int Rf\,d\mu^+=\nu(T(\mathfrak hf))=\nu(\mathfrak hf).
$$
The identity
$$
 \int f(\sigma y)g(y)\,d\mu^+(y)
 =\int f(x)Rg(x)\,d\mu^+(x)
$$
identifies $p$ as the conditional probability of the preceding
edge given the complete future.

In the stationary two-sided extension, the reverse chain rule
for a finite-alphabet word makes its entropy per edge the Cesàro
limit of conditional entropies given progressively longer futures.
Conditional probabilities converge to the full-future conditional
law; bounded finite-alphabet entropy permits passage to the limit.
Hence
$$
 h_{\widehat\mu}(\sigma)=-\int\log p\,d\widehat\mu
                       =-\int\log w\,d\widehat\mu.
$$
The logarithms of $\mathfrak h$ and of the state vector $l$
contribute only bounded shift coboundaries. The specified actual
potential therefore gives
$$
 h_{\widehat\mu}(\sigma)
 =\int\log J^u_{\Xi_\tau}\,d(H\pi)_*\widehat\mu.
$$
The sign is appropriate to the forward coded map
$\Xi_\tau=\Psi^{-1}$.

For completeness, the finite-fiber entropy argument in the input
is valid on the actual compact metric spaces. Given a finite
partition $\mathcal A$ of the coding space and a factor with at
most $D$ points in each fiber,
$$
 H(\mathcal A^{(n)}\mid\Gamma^{-1}\mathcal B_Y)\le\log D.
$$
For fixed $n$, approximate this conditional entropy by a finite
factor partition $\mathcal B$, with error less than $\eta$.
Then
$$
 \begin{aligned}
 H(\mathcal A^{(kn)})
 &\le H(\mathcal B^{(kn)})
       +H(\mathcal A^{(kn)}\mid\Gamma^{-1}\mathcal B^{(kn)})\\
 &\le H(\mathcal B^{(kn)})
       +\sum_{j<k}H(T^{-jn}\mathcal A^{(n)}
                    \mid\Gamma^{-1}S^{-jn}\mathcal B)\\
 &=H(\mathcal B^{(kn)})
       +kH(\mathcal A^{(n)}\mid\Gamma^{-1}\mathcal B).
 \end{aligned}
$$
Thus
$$
 h(T,\mathcal A)\le h(S)+(\log D+\eta)/n.
$$
Here $\mathcal B$ may depend on $n$; the upper bound by
$h(S)$ is independent of that choice. Taking $n\to\infty$
and then the supremum over $\mathcal A$ proves entropy
equality; the reverse inequality follows by pullback partitions.
The coding has $D=4$, so no entropy is lost.

## 3. The exact published equilibrium input

The primary article was reopened directly during this audit:

R. Bowen and D. Ruelle, *The Ergodic Theory of Axiom A Flows*,
Invent. Math. 29 (1975), 181--202,
DOI 10.1007/BF01389848,
<https://www.ihes.fr/~ruelle/PUBLICATIONS/%5B42%5D.pdf>.

Theorem 3.3 supplies uniqueness for Hölder potentials on a basic
hyperbolic set. Proposition 4.4(b) supplies zero geometric pressure
for an attractor. Theorem 5.1 and Remark 5.2 identify invariant
smooth probability volume in the Anosov case with that equilibrium
state. Their actual text agrees with the input's use.

The mapping torus here is a smooth compact constant-roof suspension
of the proved area-preserving Anosov map. Its vertical vector field
has no zeros; its stable and unstable bundles are the suspended
ones. Topological transitivity and density of periodic orbits
follow from the already constructed cat-map conjugacy. The whole
space is the relevant locally maximal basic set and attractor.
The smooth form $dq\wedge dp\wedge ds$ glues across the section
because the base map preserves area. Mixing of the suspension is
not a hypothesis of the cited uniqueness statement.

The frozen map-to-flow proof gives equality of invariant entropies
and identifies the integrated geometric potential with the base
negative unstable logarithm modulo a bounded metric coboundary.
Consequently the zero free-energy equality in Section 2 identifies
$(H\pi)_*\widehat\mu$ with normalized area.

Switching from $\Xi_\tau$ to $\Psi$ causes no change in the
invariant geometric integral. In dimension two, the determinant
identity
$$
 J^u_F(x)J^s_F(x)\sin\alpha(Fx)=\sin\alpha(x)
$$
and $J^u_{F^{-1}}(Fx)=1/J^s_F(x)$ prove this by integration.
Entropy is also unchanged on inversion.

Coding multiplicities do not change cylinder masses: their images
lie on a countable union of iterates of finite actual stable and
unstable arcs, an area-null set. Since the pushforward is area,
its full inverse image has zero $\widehat\mu$-mass.

## 4. The intervals are actual connected edge subarcs

The twelve-edge coding records individual connected crossing
strips. Fixing all negative edges to zero selects the fixed
unstable plaque of the coded forward map. Requiring the next edge
to be $a$ cuts one nondegenerate compact interval. Requiring
additional future edges partitions that interval into compact
subintervals with disjoint interiors. The analogous past
construction gives the other interval.

The topological conjugacy preserves the two foliations and their
local product, so these become the actual physical stable and
unstable edge subarcs. No differentiability of that conjugacy
is used. The actual cone bounds make their lifted horizontal
coordinates one-to-one.

On either local fixed curve the contraction toward the fixed
point is
$$
 f(t)=\Lambda^{-1}t+O(t^2),\qquad
 f'(t)=\Lambda^{-1}+O(t).
$$
The products
$$
 \Lambda^R(f^R)'(t)
 =\prod_{j<R}\Lambda f'(f^j(t))
$$
converge uniformly to a strictly positive continuous function,
because their logarithmic deviations are bounded by a summable
multiple of $\Lambda^{-j}|t|$. The linearizing limit is thus
$C^1$, strictly monotone, and has derivative $1$ at zero.
A fixed finite entry iterate extends it over each compact
edge subarc. Its images are exactly the intervals $I_S,I_U$
in the signed-profile coordinate convention.

## 5. The midpoint cylinder fixes the full normalization

Use the chronological block
$$
 v\,a\,0^{2R}\,a\,w
$$
at the midpoint of its zero run. Assign the zero edges indices
$-R,\ldots,R-1$; the adjacent $a$'s are $-R-1$ and $R$.
This places precisely $R$ zero edges between each scattering
base and the cut. The midpoint is $R+1$ shifts from the first
$a$, but there is no additional multiplier in either tail.

The exact cylinder formula, with the reversed chronological
operator convention, is
$$
 \widehat\mu(C_R(w,v))
 =\nu(J_w A J^{2R}A J_v\mathfrak h).
$$
The normalized $J$-limit gives
$$
 \Lambda^{2R}\widehat\mu(C_R(w,v))
 \longrightarrow\nu(J_wAg)(AJ_v\mathfrak h)(o)
 =cP_K(w)Q_K(v).
$$

Independently, both actual graph families are $C^1$ in their
real base points in a fixed holomorphic norm, by the previously
proved inverse graph construction. Its contraction is below
$1/25$, and the differentiated contraction is below $6/25$.
The same argument applies to the inverse map with eigendirections
exchanged: its derivative norm remains below $6$, and the
finite additional factors in the short-flow derivatives fit
within the reserved smallness margins.

Let $z_s(t),z_u(u)$ be the fixed-point curves parametrized by
horizontal displacement and let
$$
 \mathcal B(t,u)
 =W^u_{\rm loc}(z_s(t))\cap W^s_{\rm loc}(z_u(u)).
$$
The implicit-function theorem for the two $C^1$ graph
families gives a $C^1$ local product. Its two derivative
columns at zero are $(1,s_s)$ and $(1,s_u)$, so
$$
 |\det D\mathcal B(0,0)|=s_s-s_u=\chi.
$$

The midpoint cylinder is exactly a product in this chart.
Replacing its past by all zeros projects to the fixed stable
curve along unstable plaques, preserving its future
$0^R a w\cdots$. This is precisely the stable contraction
of the actual $a$-subarc with refinement $w$, for $R$
steps. Replacing its future by zeros similarly projects its
past $\cdots v a0^R$ onto the fixed unstable curve.
These are exactly the tail conventions defining $S,U$.

The rescaled projection intervals converge to $I_S(w)$ and
$I_U(v)$. The $C^1$ product Jacobian tends uniformly to
$\chi$. Changing variables and using the already identified
area pushforward therefore gives
$$
 \Lambda^{2R}\widehat\mu(C_R(w,v))
 \longrightarrow \chi |I_S(w)||I_U(v)|.
$$
This argument measures finite, positive-area rectangles. It
does not condition on an infinite zero tail of measure zero.

Compare the two limits with both refinements empty:
$$
 c=\chi |I_S||I_U|.
$$
Then refine only one side:
$$
 P_K(w)=|I_S(w)|/|I_S|,\qquad
 Q_K(v)=|I_U(v)|/|I_U|.
$$
The cylinder meshes tend to zero by the proved coding modulus.
Approximation of continuous functions on the intervals now
identifies the two pushforward measures with their normalized
Lebesgue measures.

## 6. Exact compression and the prefactor

The actual kernel relative to $ds/|I_S|$ is
$$
 \frac1{|I_U|}\int_{I_U}e^{2\pi i\chi x(s-s')u}\,du
 =e^{2\pi i\chi x\bar u(s-s')}
 \frac{\sin\{\pi\chi x|I_U|(s-s')\}}
      {\pi\chi x|I_U|(s-s')}.
$$
A unitary multiplication removes the midpoint phase. Set
$$
 d=\chi x|I_U|,\qquad
 y=d(s-\bar s),\qquad
 L=d|I_S|=cx.
$$
The map
$$
 f\longmapsto L^{-1/2}f(\bar s+y/d)
$$
is unitary from $L^2(I_S,ds/|I_S|)$ to
$L^2([-L/2,L/2],dy)$, since $d/L=1/|I_S|$.
The transformed operator is exactly $L^{-1}\mathsf S_L$,
where $\mathsf S_L$ is the usual sinc-kernel compression.
There is no extra $2\pi$ in $L$.

Because $c_*=c^3$, the signed-profile factor simplifies exactly:
$$
 c^3m^4\varepsilon^3\operatorname{Tr}K^3
 =\frac{m^4}{N^3}
       \operatorname{Tr}\mathsf S_{cN\varepsilon}^{\,3}.
$$
The coefficient $1/144$, uniform $o(N)$, and bounded rounding
parameter remain those of the independently audited profile.

## 7. Scope

The result is a genuine sine-compression identity for the actual
complete three-cell encounter family. Neither this identification
nor the geometric equilibrium theorem controls the complementary
families in the complete weighted quantum power-trace sum.
It is not a proof of $H_{\rm diag}$ or of the full point-process
limit.
