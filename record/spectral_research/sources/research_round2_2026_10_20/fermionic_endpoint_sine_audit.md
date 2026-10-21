> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/fermionic_endpoint_sine_audit.md`. Embedded SHA256: `0214633ec222c7d3a15fc32171b3517e1f24c0c17db77e780a1f1295ca18aa76`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/dephasing.md).

# Independent audit: actual endpoint laws and sine compression

Research continuation, 20 October 2026.

## Input and outcome

The complete input read for this audit is
arithmetic_endpoint_laws_and_sine_compression.md, SHA-256

    8307e8bed074727caee3788adca79a44cab2fdf2627bbbfdcb2058a50863dfe1

The outcome is **PASS**. No mathematical correction was found.
In particular the proof establishes the actual endpoint measures,
their area normalization, and the exact sine-compression scaling.
It does not assert the full spectral limit.

For the local-product regularity check, the complete relevant
construction in Section 2 of root_uniform_translation_contact.md
was also reread. Its SHA-256 is

    257afa4511da2fae8bd9260cc33a654bf045115f80aa0861bb8eae6a4f92347e

The signed-profile input was checked against its frozen SHA-256

    edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5

The geometric equilibrium theorem is used through the explicitly
stated published inputs already checked in the frozen
fermionic_pressure_transfer.md. This audit checks the use of
those inputs and the new entropy and volume arguments. It does
not claim a new independent download of the primary article.

## 1. The exact transfer measure, not only periodic weights

The normalized reverse kernel is
$$
 p(ex)=w(ex)\frac{\mathfrak h(ex)}{\mathfrak h(x)},\qquad
 \sum_e p(ex)=1.
$$
The positive measure $\mu^+=\mathfrak h\nu$ has mass one.
Its kernel invariance follows from $\nu\mathcal T=\nu$, while
$R(f\circ\sigma_+)=f$ proves shift invariance. The identity
$$
 \int f(\sigma_+y)g(y)\,d\mu^+(y)
       =\int f(x)Rg(x)\,d\mu^+(x)
$$
does identify the conditional law of the preceding edge given
the whole future. No independent conditional-measure assertion
is required.

The two-sided stationary extension therefore has cylinder
probabilities
$$
 \widehat\mu([w])=\nu(J_w\mathfrak h).
$$
This formula has the same reversed prefix-operator ordering as
the signed-profile theorem.

The reverse entropy chain rule gives
$-\int\log p=-\int\log w$; both the eigenfunction quotient and
the Perron-vector quotient have zero invariant logarithmic
integral. The latter is the integral of the actual unstable
logarithm, by the already constructed metric and one-sided
coboundaries.

The finite-fiber entropy argument is valid. Conditional on the
factor point, an $n$-name has at most four possibilities.
For each fixed $n$, a finite factor partition can approximate
that conditional entropy by $\log4+\eta$. For $k$ blocks,
the factor join at all $kn$ times refines the conditioning
needed at each block start, so the chain rule gives the
displayed inequality with $k(\log4+\eta)$. Division by $kn$
and then $n\to\infty$ removes that error, even though the
approximating factor partition depends on $n$. The opposite
entropy inequality follows from pulled-back partitions.

Consequently the pushed-forward transfer measure has zero
geometric free energy. The checked uniqueness theorem applies
to the actual area-preserving Anosov map through its constant
roof suspension. It identifies this measure with area. The
angle coboundary correctly identifies map and inverse unstable
integrals; no forward/inverse sign is lost.

## 2. Geometry of the endpoint intervals

An individual edge of the Berg coding is a connected crossing
strip. Fixing the zero past and selecting edge $a$ therefore
cuts one nondegenerate interval on the corresponding fixed-point
plaque. Further future words partition this interval into
subintervals. The analogous backward statement gives the other
endpoint intervals. Equivariant conjugacy preserves these
local-product intersections, but its differentiability is never
asserted.

The local scalar maps on the actual fixed-point curves satisfy
$$
 f(t)=\Lambda^{-1}t+O(t^2),\qquad
 |f^j(t)|\le C\Lambda^{-j}|t|.
$$
The derivative products of the linearizing limit have factors
$1+O(\Lambda^{-j}|t|)$. On a sufficiently small fixed interval
their logarithms converge uniformly and the products are bounded
away from zero. Thus the limit coordinate is strictly monotone
and $C^1$. The fixed finite entry map extends that assertion
to each compact edge arc. This proves that the scattering ranges
are actual nondegenerate intervals and that their finite-cylinder
subinterval meshes tend to zero.

The exact endpoint indexing also matches the signed-profile
file: the stable coordinate uses $R$ zeros before the right
$a$, and the unstable coordinate uses $R$ zeros after the
left $a$. There is no shift by one edge.

## 3. Local product regularity and area

The graph construction in root_uniform_translation_contact.md
does prove $C^1$ dependence in the base point, with values in
one fixed holomorphic graph space. Its graph contraction is
less than $1/25$; differentiation in the base costs at most
$\|DF\|<6$. Hence the differentiated iteration contracts with
constant below $6/25$, and its forcing differences are summable.

For the inverse map, exchanging eigendirections leaves the same
hyperbolic factors $\lambda,\lambda^{-1}$. The expression
$\Xi_\tau^{-1}=\Phi_{-\tau}S^{-1}$ and the previously bounded
short-time flow give the same tiny analytic perturbation on a
fixed slightly smaller strip, with derivative norm below six.
The very large reserved margin in the perturbation estimates
preserves the graph bounds. Thus applying that graph argument
to both foliations is legitimate here.

Their local intersection map $B(t,u)$ is $C^1$, with
$$
 B_t(0,0)=(1,s_{\rm s}),\qquad
 B_u(0,0)=(1,s_{\rm u}).
$$
The absolute determinant is therefore
$\chi=s_{\rm s}-s_{\rm u}>0$. This is the Jacobian in the
original $dq\,dp$ area; no $2\pi$ or quantum normalization
belongs in it.

## 4. The same shrinking cylinder in two exact calculations

The centered word is exactly
$$
 v\,a\,0^{2R}\,a\,w.
$$
Its transfer mass is
$$
 \nu(J_w A J^{2R}A J_v\mathfrak h).
$$
After multiplication by $\Lambda^{2R}$, the zero-branch limit
gives
$$
 \nu(J_wAg)(AJ_v\mathfrak h)(o)
       =cP_K(w)Q_K(v).
$$

In the actual product chart the stable and unstable projections
are the intervals with horizontal displacements
$\Lambda^{-R}I_{S,R}(w)$ and
$\Lambda^{-R}I_{U,R}(v)$. Their endpoints converge to the
scattering intervals. The $C^1$ area formula therefore gives
for the very same rescaled cylinder mass
$$
 \chi |I_S(w)|\,|I_U(v)|.
$$
Coding boundary arcs are area null, so they do not create a
multiplicity factor. Empty refinements first give
$c=\chi|I_S||I_U|$, and one-sided refinements then give the
normalized interval lengths. The mesh approximation proves
exactly uniform pushforward measures $\sigma,\upsilon$.
This avoids conditioning a probability measure on an infinite
tail event of zero probability.

## 5. Sine-compression normalization

For uniform endpoint intervals of lengths $A,B$, removing the
interval-center phase gives the kernel
$$
 \frac{\sin(\pi\chi xB(s-s'))}{\pi\chi xB(s-s')}
$$
relative to $ds'/A$. With $y=\chi xB(s-\bar s)$, the new
interval length is
$$
 L=\chi xAB=cx.
$$
The unitary map is $f\mapsto L^{-1/2}f(\bar s+y/(\chi xB))$.
It sends the probability measure to ordinary length measure
with exactly the factor $L^{-1}$ in the integral operator.
Thus $K_{2\pi\chi x}$ is unitarily equivalent to
$L^{-1}\mathsf S_L$.

Finally $c_*=c^3$ and $L=cN\varepsilon$. Hence the cubic
normalization cancels exactly:
$$
 c^3m^4\varepsilon^3\operatorname{Tr}(K^3)
     =\frac{m^4}{N^3}\operatorname{Tr}(\mathsf S_L^3).
$$
The coefficient $1/144$, the escape factor, and the uniform
$o(N)$ remainder from the signed-profile theorem are therefore
unchanged. This checks the advertised actual sine-kernel profile.

## Scope

The proof applies to the explicitly specified endpoint measures
and to the entire signed three-cell family already evaluated.
It supplies no estimate of the other orbit pairs. In particular
the occurrence of the sine compression in this exact profile
does not establish $H_{\rm diag}$ or weak convergence of the
full spectrum.
