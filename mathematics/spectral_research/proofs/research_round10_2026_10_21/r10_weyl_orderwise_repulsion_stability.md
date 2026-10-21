> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round10_2026_10_21/r10_weyl_orderwise_repulsion_stability.md`. Embedded SHA256: `63ddeba5e72b200bf3dd16bed795423d4ed7e070a0b0e3f55fa30b93d3bc53d2`.
> [Thematic guide](../../topics/closure.md).

# Order-by-order stability from the repulsion of the CUE comparison

21 October 2026. Branch `/root/r10_weyl`.

Base master: SHA-256
`e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777`.

## 0. Statement and exact scope

For a deterministic unitary sequence, write `H_k` for the single-order
part of `H_diag`: for every admissible nonnegative bandlimited Schwartz
test `b`, its factorial moment of order `k` differs from the CUE
comparison by `o(1)`. The order `k>=2` is fixed; all test bandwidths
remain allowed, each fixed before the dimension limit.

**Theorem.** Suppose two deterministic unitary sequences of the same
dimensions admit a matching of real eigenangle lifts, after a common
scalar rotation, with

$$
\max_j N|\varepsilon_{j,N}|\le C,
\qquad \eta_N:=\sum_j|\varepsilon_{j,N}|\longrightarrow0.
\tag{0.1}
$$

Then, for every fixed `k>=2`,

$$
\boxed{H_k(U_N)\quad\Longleftrightarrow\quad H_k(V_N).}
\tag{0.2}
$$

No factorial-moment assumption of order `k+1` or higher is needed.
The proof obtains the uniform integrability of the required order
directly from the small-window repulsion forced by `H_k` itself.

For the original family and the exactly realized normalizations in
Round 9, (0.1) was proved by fixed-observable quantum ergodicity.
Thus their criterion can now be transferred **order by order**.
This strengthens the earlier proof that transferred the complete
all-order criterion at once.

It does not prove `H_2` for either endpoint. It does not transfer a
single isolated test merely from convergence for that one test:
the proof uses a sequence of increasingly narrow, individually fixed,
admissible tests at the same order. The original weighted pair sum
and all-order hierarchy remain unproved.

The theorem is an internal mathematical result; no historical
priority is asserted. Sections 1--6 give a complete proof without
using a black-box uniform-integrability or point-process theorem.

## 1. An exact CUE Gram representation

Let `b>=0` be an integrable Schwartz function. The exact comparison
from the problem is

$$
M^{\mathrm{CUE}}_{k,N}(b)=e_k(T_{N,b}),\qquad
(T_{N,b})_{ij}=\frac1N\int_{\mathbb R}
b(x)e^{-2\pi i(i-j)x/N}\,dx,
\quad 0\le i,j<N.
\tag{1.1}
$$

Put

$$
\xi_{r,N}=\frac{r-(N-1)/2}{N},\qquad
\nu_N=\frac1N\sum_{r=0}^{N-1}\delta_{\xi_{r,N}},
\tag{1.2}
$$

and define

$$
\mathcal K_N(x,y)=\int e^{2\pi i\xi(x-y)}\,d\nu_N(\xi).
$$

This differs from the uncentered finite CUE kernel only by a
factor `exp(i c_N x) exp(-i c_N y)`, which cancels in every
correlation determinant. The support of `nu_N` is contained in
`[-1/2,1/2]`, and its mass is one.

The finite Gram identity gives

$$
\boxed{
M^{\mathrm{CUE}}_{k,N}(b)
=\frac1{k!}\int_{\mathbb R^k}
\prod_{a=1}^k b(x_a)
\det[\mathcal K_N(x_a,x_b)]_{a,b=1}^k\,dx.}
\tag{1.3}
$$

Here is an algebraic verification. Expand `e_k(T)` as the sum
of all principal `k`-minors. In one such Gram determinant, expand
both determinants under its multiple integral; the `k!` possible
permutations of the integration variables have equal integrals.
Consequently that minor equals `1/k!` times the integral of the
squared modulus of the determinant of its `k` Fourier functions,
with weight `prod b`. Summing the squared minors over the finite
frequency subsets is exactly the finite Cauchy--Binet formula for
the determinant on the right of (1.3). Absolute integrability
follows from bounded Fourier functions and `b in L^1`. If `k>N`,
both sides vanish by rank. This proof uses the exact finite matrix
(1.1); no limiting sine-kernel result is needed.

## 2. A uniform finite-dimensional Vandermonde bound

For every probability measure `nu` supported in `[-1/2,1/2]`, let

$$
K_\nu(x,y)=\int e^{2\pi i\xi(x-y)}\,d\nu(\xi).
$$

**Lemma 1.** For all real `x_1,...,x_k`,

$$
0\le\det[K_\nu(x_a,x_b)]
\le C_k\prod_{a<b}|x_a-x_b|^2,
\qquad
C_k=\frac{\pi^{k(k-1)}}{\prod_{r=0}^{k-1}(r!)^2}.
\tag{2.1}
$$

**Proof.** Work in the Hilbert space `L^2(nu)` and set
`v(x)(xi)=exp(2 pi i xi x)`. The kernel is the Gram kernel of
these vectors (up to transposition, which preserves its determinant).
For every integer `r>=0`,

$$
\|v^{(r)}(x)\|_{L^2(\nu)}\le\pi^r
\quad\text{for every real }x.
\tag{2.2}
$$

Assume initially the nodes are distinct. Let
`d_j=v[x_1,...,x_j]` be the divided-difference vectors of orders
`j-1`. The integral formula for these differences is

$$
d_j=\int_{\substack{t_1,...,t_{j-1}\ge0\\
                    t_1+\cdots+t_{j-1}\le1}}
v^{(j-1)}\!\left((1-\textstyle\sum t_r)x_1+
                       \sum_{r=1}^{j-1}t_rx_{r+1}\right)dt.
\tag{2.3}
$$

Its simplex has volume `1/(j-1)!`, so (2.2) implies

$$
\|d_j\|\le\frac{\pi^{j-1}}{(j-1)!}.
\tag{2.4}
$$

For completeness, formula (2.3) for the exponential can be proved
without a vector-valued mean-value theorem. The elementary identity

$$
\sum_{n\ge0}[x_1,\ldots,x_j]X^n\,z^n
=\frac{z^{j-1}}{\prod_{a=1}^j(1-zx_a)}
\tag{2.5}
$$

uses the notation `[x_1,...,x_j]X^n` for the divided difference
of the monomial `X^n`. For `j=1` it is the geometric series;
subtracting the formulas for the first and last `j-1` nodes and
dividing by `x_j-x_1` proves the formula inductively. Hence that
divided difference is zero for `n<j-1` and is the complete
homogeneous polynomial `h_(n-j+1)(x_1,...,x_j)` otherwise.
On the simplex, repeated integration gives

$$
\int t_0^{a_0}\cdots t_{j-1}^{a_{j-1}}dt
=\frac{\prod_r a_r!}{(a_0+\cdots+a_{j-1}+j-1)!},
\quad t_0=1-\sum_{r=1}^{j-1}t_r.
\tag{2.6}
$$

The one-dimensional step is the beta integral for nonnegative
integers, obtained by repeated integration by parts; induction on
the simplex dimension then proves (2.6). Expand the exponential
in (2.3) and apply (2.6). Its coefficient of `(2 pi i xi)^n`
is exactly the monomial divided difference divided by `n!`,
as characterized by (2.5). This proves (2.3) pointwise in `xi`.
Uniform convergence for bounded `xi` also proves it in `L^2(nu)`.

Newton interpolation expresses `v(x_i)` as a lower triangular
linear combination of `d_1,...,d_i`, with diagonal coefficient
`prod_(a<i)(x_i-x_a)`. Its determinant is the Vandermonde.
The Gram determinant therefore equals

$$
\prod_{a<b}|x_a-x_b|^2\det[\langle d_a,d_b\rangle].
$$

Gram--Schmidt, or the product formula for squared successive
orthogonal distances, bounds the last determinant by
`prod_j ||d_j||^2`. Equations (2.4) prove the upper bound.
The lower bound is Gram positivity. Coincident nodes follow by
continuity; both determinants vanish when two nodes coincide.
This proves the lemma. `QED`.

## 3. Small-window tests force small factorial count moments

Fix once and for all a nonnegative admissible Schwartz function
`beta` with

$$
\beta(x)\ge c>0\quad\text{for }|x|\le1/2.
\tag{3.1}
$$

There is a completely explicit choice. Take the bump `phi` from
the original open test, put `I=int phi`, `g=F^(-1)phi`, and set

$$
\beta(x)=\frac{|g(x/8)|^2}{2I^2}.
\tag{3.2}
$$

It has supremum at most `1/2`, is Schwartz, and has smooth
Fourier support in `[-1/4,1/4]`. Since `phi>=0`, is supported in
`[-1,1]`, and `g(0)=I`,

$$
|g(t)-I|\le 2\pi |t|I.
$$

For `|x|<=1/2`, `|x/8|<=1/16` and `pi<4` imply
`|g(x/8)|>=I/2`. Thus (3.1) holds with `c=1/8`.

For each **fixed** `delta>0`, put `beta_delta(x)=beta(x/delta)`.
It remains an admissible test. Equations (1.3) and (2.1), followed
by `x_a=delta y_a`, give the finite bound

$$
M^{\mathrm{CUE}}_{k,N}(\beta_\delta)
\le A_{k,\beta}\,\delta^{k^2}
\quad\text{for every }N,
\tag{3.3}
$$

where

$$
A_{k,\beta}=\frac{C_k}{k!}
\int_{\mathbb R^k}\prod_a\beta(y_a)
          \prod_{a<b}|y_a-y_b|^2\,dy<\infty.
\tag{3.4}
$$

The exponent is `k` from volume plus `k(k-1)` from squared
Vandermonde. Finiteness follows from the Schwartz decay and the
fixed polynomial in (3.4).

Suppose now one deterministic endpoint satisfies `H_k` and write
`X_N(J)=Xi_(N,alpha)(J)`. For a length-`delta` interval `J`, and
all sufficiently large `N>delta`, each eigenvalue label has at most
one periodic copy in `J`. Every ordered `k`-tuple of points in `J`
therefore contributes at least `c^k` to the ordered distinct-label
sum defining the periodized test centered at `J`. All remaining
terms are nonnegative. Stationarity removes the choice of center.
Consequently,

$$
\mathbb E(X_N(J))_k
\le c^{-k}k! M^U_{k,N}(\beta_\delta),
\tag{3.5}
$$

where `(n)_k=n(n-1)...(n-k+1)`. For every fixed `delta`,
`H_k` and (3.3) imply

$$
\boxed{
\limsup_{N\to\infty}\mathbb E(X_N(J))_k
\le D_{k,\beta}\,\delta^{k^2},\qquad
D_{k,\beta}=c^{-k}k!A_{k,\beta}.}
\tag{3.6}
$$

The limit is through the prescribed dimension sequence, including
all odd dimensions in the original application. No test with a
dimension-dependent bandwidth has been used.

## 4. Repulsion implies uniform integrability of the same order

Fix a bounded interval `I` of length `L>0`. Partition it into `M`
half-open intervals of equal length `delta=L/M`. There is almost
surely no point at their finitely many boundaries: exact intensity
one assigns mass zero to a point. Put `n_i=X_N(I_i)` and
`n=sum_i n_i=X_N(I)`.

For nonnegative integers `n_i`,

$$
(n_i)_k\ge ((n_i-k+1)_+)^k.
$$

Also
`sum_i(n_i-k+1)_+ >= n-(k-1)M`. If `n>2kM`, this is at
least `n/2`. Convexity of `t^k` yields

$$
\sum_{i=1}^M(n_i)_k
\ge M^{1-k}(n/2)^k.
$$

It follows, pointwise, that

$$
n^k\mathbf1_{n>2kM}
\le 2^k M^{k-1}\sum_{i=1}^M(n_i)_k.
\tag{4.1}
$$

Taking expectations and applying (3.6) to the finite collection
of cells, with `M` fixed before `N` tends to infinity, proves

$$
\boxed{
\limsup_N\mathbb E\left[
X_N(I)^k\mathbf1_{X_N(I)>2kM}\right]
\le 2^kD_{k,\beta}L^{k^2}M^{-k(k-1)}.}
\tag{4.2}
$$

Because `k>=2`, the right side tends to zero as `M` increases.
Thus the family `X_N(I)^k` is asymptotically uniformly integrable.
It is uniformly integrable over the full sequence as well: for each
fixed finite set of dimensions the count on `I` is deterministically
bounded, and these finitely many terms can be removed by increasing
the truncation level. Uniform boundedness of `E X_N(I)^k` follows.

**Order of limits.** First fix `M`, use one fixed test of bandwidth
proportional to `M`, and take `N` to infinity; only then let `M`
grow. The theorem requires no uniform convergence rate across the
shrinking tests. In particular, (4.2) must not be integrated over
all truncation scales before the `N` limit to claim uniform higher
prelimit moments. Such a claim is not made here.

## 5. Transfer of uniform integrability and Schwartz weights

Assume the spectral matching (0.1), and absorb its common scalar
rotation into the uniform origin. Under the matching with a common
origin, each unfolded point moves by at most `C`. Therefore, for
every bounded interval `I`,

$$
\Xi^V_{N,\alpha}(I)
\le\Xi^U_{N,\alpha}(I+[-C,C]).
\tag{5.1}
$$

The uniform integrability of the source local counts to order `k`
thus passes to the target, by domination. Their uniform `L^k`
bounds also pass. Both processes are stationary under real
translations because the origin is uniform, so all bounds for a
unit interval are independent of its location.

Let `b` now be any nonnegative Schwartz test, and put

$$
Z_N^X=\langle b,\Xi^X_{N,\alpha}\rangle,\qquad X\in\{U,V\}.
$$

For `c_j=sup_[j,j+1) b`, the sequence `(c_j)` is summable.
Minkowski's inequality and the uniform unit-interval `L^k` bound
give, for tails outside finitely many cells,

$$
\sup_N\left\|
\sum_{|j|>R}c_j\Xi^X_{N,\alpha}([j,j+1))
\right\|_{L^k}
\le C_{k,X}\sum_{|j|>R}c_j\longrightarrow0.
\tag{5.2}
$$

For finitely many cells, the corresponding weighted count has
uniformly integrable `k`-th power. Indeed that power is bounded
by a constant times the finite sum of the local count `k`-th
powers, and finite sums of uniformly integrable nonnegative
variables are uniformly integrable. To check the latter fact,
if `Y=sum_(i=1)^d Y_i>A`, the terms with `Y_i<=A/(2d)`
sum to at most `A/2`, so `Y 1_(Y>A)` is at most twice the
sum of the large terms.

Uniform `L^k` approximation in (5.2) passes this conclusion to
the full weighted counts. Explicitly,

$$
\|Z^k-(Z^{(R)})^k\|_{L^1}
\le k(\|Z\|_{L^k}+\|Z^{(R)}\|_{L^k})^{k-1}
                   \|Z-Z^{(R)}\|_{L^k},
\tag{5.3}
$$

which tends to zero uniformly in `N`. Uniform `L^1` limits of
uniformly integrable families are uniformly integrable: bound the
tail by the approximant's tail and twice its `L^1` error, or use
uniform absolute continuity of their integrals. Thus

$$
\{(Z_N^U+Z_N^V)^k\}_N
\quad\text{is uniformly integrable}.
\tag{5.4}
$$

This step uses only order `k`, not a moment of order `k+1`.

## 6. Completion of the orderwise transfer

Write the two periodized weight arrays as `w_j^U,w_j^V` and set

$$
D_N=\sum_j|w_j^V-w_j^U|,\qquad
S_N=\sum_j(w_j^U+w_j^V)=Z_N^U+Z_N^V.
$$

Exact integration over the common uniform origin and the periodic
copies gives

$$
\mathbb ED_N
\le\frac1N\sum_j\|b(\cdot+N\varepsilon_{j,N})-b\|_1
\le\|b'\|_1\eta_N\longrightarrow0.
\tag{6.1}
$$

The first inequality is the triangle inequality inside each
periodization; equality holds before combining its copies. The
second follows by integrating the fundamental theorem of calculus.

Telescoping each product over distinct labels and summing proves

$$
|e_k(w^V)-e_k(w^U)|
\le\frac{D_NS_N^{k-1}}{(k-1)!}.
\tag{6.2}
$$

For example, at each specified differing label the remaining
`k-1` distinct positions are bounded by the corresponding power
of `S_N`; division by `k!` and summing over the `k` possible
specified positions gives exactly `1/(k-1)!`.

Since `D_N<=S_N`, equations (6.1), (6.2), and (5.4) give

$$
\begin{split}
|M^V_{k,N}(b)-M^U_{k,N}(b)|
&\le\frac1{(k-1)!}\left[
R^{k-1}\|b'\|_1\eta_N+
\mathbb E S_N^k\mathbf1_{S_N>R}\right]\\
&\longrightarrow0
\end{split}
\tag{6.3}
$$

by taking `N` to infinity first and `R` to infinity second.
Thus `H_k(U)` implies `H_k(V)`. The matching is symmetric,
so reversing the assumed source proves the reverse implication.
This proves the theorem.

## 7. Application and what remains unchanged

Round 9 proved (0.1) for the original family and each of its
constructed continuous-symbol normalization endpoints. All of its
operator and analytic arguments are retained; the present theorem
only improves the moment-transfer step. Consequently, for each
fixed `k>=2` separately,

$$
H_k(U_N)\iff H_k(\widetilde U_N)
\iff H_k(e^{iQ_N^+(v)/N}U_N).
\tag{7.1}
$$

The unconditional comparison of bounded Laplace functionals was
already proved and is not claimed anew. The present proof supplies
the missing same-order uniform integrability from CUE repulsion.

There is still no proof or original countersequence for

$$
N^{-2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
\bigl(|\operatorname{Tr}U_N^m|^2-\min(m,N)\bigr)\to0.
$$

In particular, (7.1) does not turn a solution for the one isolated
test `b_*` at a normalized endpoint into its solution at the
original endpoint. The small-window inputs used in Section 3
require the same fixed order but unboundedly many fixed bandwidths.

The theorem is a rigorously proved strengthening of the transfer
framework, not a solution of the signed hierarchy.
