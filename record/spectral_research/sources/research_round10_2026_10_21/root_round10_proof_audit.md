> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round10_2026_10_21/root_round10_proof_audit.md`. Embedded SHA256: `b4344242965f7687125b46705971ef6e41a95402db055cb5488a6666b6be5c0b`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Coordinator audit of the new Round 10 results

21 October 2026. Actual proof texts were read, not only their titles
or branch summaries. No original-family asymptotic is certified by
this audit.

## 1. Same-order repulsion and matching

Read in full: r10_weyl_orderwise_repulsion_stability.md, SHA-256
63ddeba5e72b200bf3dd16bed795423d4ed7e070a0b0e3f55fa30b93d3bc53d2.

The Gram integral is for the original distinct-label statistic;
it is not globally identified with the factorial measure of all
periodic copies. Counts use intervals of diameter less than $N$.
The bounded-frequency vectors have derivative norms at most
$\pi^r$, so divided differences have norms at most $\pi^r/r!$.
Newton interpolation gives exactly the stated Vandermonde-squared
bound. Scaling the positive majorant yields $\delta^{k^2}$.

The partition inequality

$$
n^k{\bf1}_{n>2kM}\le2^kM^{k-1}\sum_{a=1}^M(n_a)_k
$$

is valid before expectation. Its limiting tail estimate is
$O(M^{-k(k-1)})$, with the dimension limit preceding the
cell-number limit. Finitely many initial dimensions have bounded
counts. This proves same-order uniform integrability without a
moment of order $k+1$.

Bounded unfolded displacement transfers the count bound by interval
enlargement. Summable Schwartz cell envelopes transfer it to weighted
counts. The total periodized weight discrepancy has expectation at
most $\|b'\|_1\sum_j|\varepsilon_{j,N}|$; the final product
telescoping and truncation are valid.

**Verdict:** the matching theorem $H_k(U)\iff H_k(V)$ is proved,
for every fixed complete order. It does not transfer an isolated
test on the basis of that test alone.

## 2. Recovery of lower orders

The full substantive proof in r10_weyl_downward_moment_heredity.md
was read at SHA-256
360f63ae8f42fea11086d8d56ffe984412787b04071603d22b722bf51eb9a520.
The next version only repaired a TeX escape. The final independent
arithmetic audit records the further single control-character
repair and final hash
ba5e5fb7b2d812c8b9a9f28f2f555412399d0e749d941af2723137be206c65dd.

The summable unit-cell supremum norm controls weighted counts in
$L^k$. Convolution approximates compact smooth functions in that
norm. Positive polarization and boundary-strip approximation,
using the already proved same-order uniform integrability, give
mixed compact moments and interval indicators without circularity.

The combinatorial bounds on $n^k-(n)_k$ give
$\limsup_N\mathbb E[(X_N([0,R])/R)^k]\le1+C_k/R$.
The inequality
$$
|y-1|^k\le y^k-1-k(y-1),\qquad y\ge0,
$$
and exact intensity remove the linear term. Thus the density error
is controlled in $L^k$, with $R$ fixed before the dimension
limit; neither ergodicity nor a growing window was assumed.

For a local $j$-tuple, exactly $d$ selected points lie in the
large count interval. The remaining count is
$(X_N([0,R])-d)_{k-j}$. Its collision correction was retained.
The Hölder exponents $k/j$ and $k/(k-j)$ are conjugate,
yielding the stated $O(R^{-1/k})$ error.

Every sine-determinant permutation moving a new variable contains
an off-diagonal factor depending on that variable. Its absolute
integral over a length-$R$ interval is at most $\sqrt{3R}$;
all other factors have modulus at most one. This gives the uniform
$\sqrt3\,k!R^{-1/2}$ contraction bound. Schwartz truncation
at the end remains in the original distinct-label definition.

**Verdict:** $H_k\Rightarrow H_j$ for all $j<k$ is proved.
It neither proves $H_k$ in the first place nor determines higher
orders from one finite order.

## 3. Exact conjugacy average and the critical scale

Read in full: r10_mixed_isospectral_twirl_obstruction.md, final SHA-256
673a8fbbe93cb26db469b7c7dd13b5960352e3ec2cdbf9e248aa4d7f2be1d9b9.

The elementary commutant argument gives
$$
\mathbb E_G\operatorname{Ad}(GUG^*)=
P+\frac{|\operatorname{Tr}U|^2-1}{N^2-1}(I-P).
$$
Keeping the same conjugation in a power replaces the numerator
by $|\operatorname{Tr}U^m|^2-1$. Taking a power of the averaged
operator instead raises the first coefficient to that power.
Center rotation leaves the adjoint exactly unchanged.

The finite CUE form factor is obtained from its two-point kernel by
counting $N-m$ matching frequency pairs when $m<N$. The
lost term under independent resampling has operator norm at most
$1/(N+1)$, while its normalized weighted supertrace tends to
$\int w(u)\min(u,1)\,du$. The powers of $N$ and the
positive-frequency pair normalization were checked.

**Verdict:** the exact scale obstruction is proved; it does not
estimate the unknown original trace coefficient.

## 4. Shrinking isospectral Weyl noise

Read in full: r10_mixed_shrinking_isospectral_noise.md, final SHA-256
5c9265843ce9ad7037ca35b0b601bfed4cca9bd87a44d15405a30f68d22683fb.

The direct modular kernel calculation gives
$$
M_NT(k)M_N^*=T(Sk),\quad
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\quad
\det(S-I)=-4.
$$
Thus $S-I$ is invertible at every odd dimension. The Poisson
difference distribution has exactly the Fourier transform used in
the weighted permutation, and its squared torus displacement has
expectation at most $2N^{-\alpha}$.

For a nonzero closed label, if every centered orbit vector had
coordinate maximum at most $N/16$, the row bound $7/16<1/2$
would prevent every modular wrap, including the last transition.
It would be a nonzero integer periodic vector of a hyperbolic real
matrix, which is impossible. This proves the stated all-time
trace estimate with $c=1-\cos(\pi/8)>0$.

The stronger logarithmic-block proof also checks out: at the middle
of an unwrapped block the unstable component is bounded by its
final endpoint and the stable component by its initial endpoint.
For the stated block length both are small enough to force the
middle integer vector to be zero. The resulting spectral-radius
bound is valid. The note correctly states only an $O(\log N)$
inverse-norm estimate, not a uniform singular-value gap.

For the explicit odd dimensions
$$
N_r=\frac{(3+2\sqrt2)^r-(3-2\sqrt2)^r}{4\sqrt2},
\qquad r\ge3\ {\rm odd},
$$
the recurrence proves integrality and oddness, and
$S^{2r}=I\bmod N_r$. Weyl covariance and its elementary
commutant give a scalar $M_{N_r}^{2r}$. Positive terms at
multiples of $2r$ prove the divergent fixed-test pair statistic.
The bound of $2r$ on the number of distinct eigenangles proves
the empty local limit by a union bound over origin intervals.

The same-sample noise penalty is
$\ell_N((S^m-I)k)$; the resampled penalty is
$\sum_{j<m}\ell_N((S-I)S^jk)$. The former vanishes on closed
labels and the latter does not. This identifies the lost
coherence before taking any trace.

**Verdict:** these statements are proved for auxiliary conjugacy
ensembles of the bare $M_N$. They are not an original-$U_N$
counterexample. There is no transfer across the fixed nonzero kick.

## 5. Rational inactive-kick calculation

Read in full: r10_arithmetic_stationary_rational_test.md.
The corrected ordinary symbol shifts $r$ by $1/2$ in its
$p$-dependent term. Its derivative bound forces every fixed
point of the prescribed tiny-time autonomous flow to be stationary:
a nonconstant closed velocity would require $CT\ge2$.

At rational $p$, the sine phase cannot vanish because
$(-3+4i)/5$ is not a root of unity. The candidates from
$r(q+1/2)=0$ are checked directly. At the six nontrivial
candidates, the magnitude $10|\sin(2\pi q)|>2$ exceeds the
possible quadratic cosine term. Only $q=0,1/2$ remain.

The untouched rational set is indexed by
$\mathbb Z/2\times\mathbb Z/8$, with map
$(a,b)\mapsto(a-b,3b)$. Its four fixed points, six two-cycles,
and absence of nonzero odd torsion follow directly. The proof
correctly makes no inference to a growing quantum eigencluster.

## 6. Original-family status

The first fixed pair sum in the checkpoint is still unestimated
at its required asymptotic scale. The new theorems strengthen the
criterion and expose specific failed approximation steps. They
neither prove nor refute the original $H_{\rm diag}$.

Finite consistency checks, source titles, and the statistics of
an auxiliary ensemble do not replace that missing estimate. No
formal verification or historical priority is claimed.
