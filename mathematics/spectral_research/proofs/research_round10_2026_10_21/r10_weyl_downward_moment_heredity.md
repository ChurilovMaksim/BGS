> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round10_2026_10_21/r10_weyl_downward_moment_heredity.md`. Embedded SHA256: `ba5e5fb7b2d812c8b9a9f28f2f555412399d0e749d941af2723137be206c65dd`.
> [Thematic guide](../../topics/closure.md).

# One complete correlation order determines every lower order

21 October 2026. Branch `/root/r10_weyl`.

Base master SHA-256:
`e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777`.

Companion input: `r10_weyl_orderwise_repulsion_stability.md`, SHA-256
`63ddeba5e72b200bf3dd16bed795423d4ed7e070a0b0e3f55fa30b93d3bc53d2`.
The precise inputs used from that note are its exact Gram identity,
its small-window majorant construction, and its proof of same-order
uniform integrability in Sections 1--4. No stability or spectral
matching hypothesis is used in the present theorem.

## 0. Statement, quantifiers, and limitation

Let `U_N` be any deterministic unitary sequence with the uniform-origin
point processes specified in the problem. Dimensions may run through
any sequence tending to infinity. Fix one integer `k>=2`. Suppose

$$
M^U_{k,N}(b)-M^{\mathrm{CUE}}_{k,N}(b)\longrightarrow0
\tag{0.1}
$$

for **every** admissible nonnegative bandlimited Schwartz `b`. Each
bandwidth is fixed before taking the dimension limit. Then

$$
\boxed{H_k\quad\Longrightarrow\quad H_j
\quad\text{for every }1\le j\le k.}
\tag{0.2}
$$

Order one is already an exact consequence of intensity one. For the
other lower orders, no higher moment hypothesis, ergodicity hypothesis,
or assumed weak limit is needed. The proof is directly on the prelimit
processes, with every auxiliary spatial scale fixed before `N` tends
to infinity.

In particular, the full criterion can equivalently be requested on
any unbounded set of integer orders, provided that at each of those
orders **all** the allowed tests are covered. This equivalence does
not show that a single finite order determines the higher orders.

Nothing here establishes (0.1) at even one order for the original
fixed-`tau` family. The result also does not start from a single test
at order `k`: the small-window majorants and polarization require
many individually fixed tests of that order.

## 1. Same-order local integrability forced by the hypothesis

Write `X_N(I)=Xi_(N,alpha)(I)` for the count in a bounded interval.
The companion proof establishes, from (0.1) alone, both

$$
\sup_N\mathbb E X_N(I)^k<\infty,
\qquad
\lim_{A\to\infty}\sup_N
\mathbb E[X_N(I)^k\mathbf1_{X_N(I)>A}]=0.
\tag{1.1}
$$

For clarity, its precise mechanism is recalled here. A fixed
nonnegative bandlimited Schwartz function `beta`, bounded above by
`1/2` and below by `1/8` on `[-1/2,1/2]`, is constructed explicitly
there. Its dilation `beta_delta(x)=beta(x/delta)` is admissible for
each fixed `delta>0`. The finite CUE Gram determinant obeys

$$
0\le\det[\mathcal K_N(x_a,x_b)]
\le C_k\prod_{a<b}|x_a-x_b|^2,
\quad
C_k=\frac{\pi^{k(k-1)}}{\prod_{r=0}^{k-1}(r!)^2}.
\tag{1.2}
$$

Consequently, with a fixed finite constant `D`,

$$
\limsup_N\mathbb E(X_N(J))_k\le D|J|^{k^2}
\tag{1.3}
$$

for each fixed interval `J`. The positive majorant, rather than an
`L^1` approximation for factorial moments, proves this bound. Once
`N>|J|`, different periodic copies of the same eigenvalue label
cannot occur together in `J`.

Partitioning a length-`L` interval `I` into `M` equal cells gives the
pointwise inequality

$$
X_N(I)^k\mathbf1_{X_N(I)>2kM}
\le2^k M^{k-1}\sum_{a=1}^M(X_N(I_a))_k.
$$

Thus

$$
\limsup_N\mathbb E[X_N(I)^k\mathbf1_{X_N(I)>2kM}]
\le2^kDL^{k^2}M^{-k(k-1)}.
\tag{1.4}
$$

First `M` is fixed, then `N` tends to infinity, and only then `M`
increases. The right side tends to zero. The finitely many initial
dimensions have deterministically bounded counts on `I`. This proves
(1.1) over the entire sequence. Stationarity implies that its constants
for a unit interval do not depend on the location of the interval.

No claim about uniform moments of orders above `k` is made.

## 2. From bandlimited diagonal tests to compact mixed tests

### 2.1 A norm that controls weighted counts

For a function `a` define

$$
\|a\|_{\mathcal W}
=\sum_{n\in\mathbb Z}\sup_{x\in[n,n+1]}|a(x)|.
\tag{2.1}
$$

All Schwartz functions and compactly supported bounded functions have
finite norm. Minkowski's inequality and (1.1), applied to unit
intervals and stationarity, give

$$
\sup_N\|\langle |a|,\Xi_N\rangle\|_{L^k}
\le C\|a\|_{\mathcal W}.
\tag{2.2}
$$

Here and below all expectation and `L^p` norms for the deterministic
sequence refer to the uniform origin.

Let

$$
F_{k,N}(a_1,\ldots,a_k)
=\mathbb E_\alpha
\sum_{j_1,\ldots,j_k\ {\rm distinct}}
\prod_{r=1}^k(a_r)_N(\theta_{j_r,N}-\alpha).
\tag{2.3}
$$

This is a symmetric multilinear functional on the indicated class.
For its diagonal, write `P_(k,N)(a)=F_(k,N)(a,...,a)`; thus
`P_(k,N)(a)=k! M^U_(k,N)(a)`. Formula (2.3) is a distinct-label
definition even for noncompact weights, so no periodic-copy convention
has been changed.

For nonnegative `a,b`, telescoping products and then using Hölder
with (2.2) yields

$$
\begin{split}
|P_{k,N}(a)-P_{k,N}(b)|
&\le k\mathbb E\!\left[
\langle|a-b|,\Xi_N\rangle
(\langle a+b,\Xi_N\rangle)^{k-1}\right]\\
&\le kC^k\|a-b\|_{\mathcal W}
(\|a\|_{\mathcal W}+\|b\|_{\mathcal W})^{k-1}.
\end{split}
\tag{2.4}
$$

Indeed the difference between the periodized arrays is bounded by
the periodization of `|a-b|`. Summation over all choices of the
remaining labels is bounded by the corresponding power of their
total nonnegative weights. The same reasoning controls mixed
functionals whenever one argument changes in weighted-count `L^k`.

### 2.2 Approximation of a smooth compact function

Take `h>=0` in `C_c^infty`, and first scale it so that `sup h<1`.
Choose a nonnegative Schwartz probability kernel `K` with smooth
compact Fourier support, as in the problem. Set

$$
K_B(x)=BK(Bx),\qquad h_B=h*K_B.
$$

Then every fixed `h_B` is admissible. In addition to its familiar
`L^1` approximation, one has the stronger estimate

$$
\|h_B-h\|_{\mathcal W}\longrightarrow0.
\tag{2.5}
$$

Here is a direct proof. For every real `t`, shifting unit cells shows

$$
\|h(\cdot-t)\|_{\mathcal W}\le2\|h\|_{\mathcal W}.
$$

For `|t|<=1`, all differences are supported in one fixed compact
set, and uniform continuity of `h` gives
`||h(.-t)-h||_W -> 0` as `t->0`. Finally,

$$
\|h_B-h\|_{\mathcal W}
\le\int K(u)\|h(\cdot-u/B)-h\|_{\mathcal W}\,du.
$$

The integrand tends pointwise to zero and is dominated by
`3 K(u)||h||_W`, so dominated convergence proves (2.5).

The exact finite CUE representation is

$$
P^{\mathrm{CUE}}_{k,N}(a)
=\int_{\mathbb R^k}\prod_{r=1}^k a(x_r)
\det[\mathcal K_N(x_a,x_b)]\,dx.
\tag{2.6}
$$

The centered frequency measure defining `K_N` is a probability
supported in `[-1/2,1/2]`. Its Gram vectors have norm one, so

$$
0\le\det[\mathcal K_N(x_a,x_b)]\le1.
\tag{2.7}
$$

This gives the uniform comparison continuity bound

$$
|P^{\mathrm{CUE}}_{k,N}(a)-P^{\mathrm{CUE}}_{k,N}(b)|
\le k\|a-b\|_1(\|a\|_1+\|b\|_1)^{k-1}.
\tag{2.8}
$$

The finite centered frequency Riemann sums converge on every compact
set to Lebesgue measure on `[-1/2,1/2]`. Their kernels therefore
converge to

$$
K(x-y)=\int_{-1/2}^{1/2}e^{2\pi i\xi(x-y)}\,d\xi
=\frac{\sin\pi(x-y)}{\pi(x-y)}.
$$

Using (2.7) as the domination in (2.6) proves the corresponding
diagonal comparison limit for every integrable nonnegative `a`.
Combining (0.1), (2.4), (2.5), and (2.8), with `B` fixed before
`N` tends to infinity, proves

$$
P_{k,N}(h)\longrightarrow
\int\prod_{r=1}^k h(x_r)\rho_k^{\mathrm{sine}}(x_1,\ldots,x_k)\,dx
\tag{2.9}
$$

for every nonnegative smooth compact `h`. Scaling recovers (2.9)
without the temporary restriction on its supremum.

### 2.3 Polarization and indicators

For nonnegative smooth compact `h_1,...,h_k`, finite polarization
gives

$$
k!F_{k,N}(h_1,\ldots,h_k)
=\sum_{S\subset\{1,\ldots,k\}}(-1)^{k-|S|}
P_{k,N}\!\left(\sum_{a\in S}h_a\right).
\tag{2.10}
$$

To verify it, expand the diagonal polynomial. Inclusion--exclusion
cancels every monomial omitting an index. A degree-`k` monomial
using all `k` indices uses each exactly once, and there are `k!`
permutations, with equal values by symmetry. Each sum on the right
can be rescaled to an allowed supremum. Thus (2.9) proves the
mixed convergence

$$
F_{k,N}(h_1,\ldots,h_k)\longrightarrow
\int\prod_{a=1}^k h_a(x_a)\rho_k^{\mathrm{sine}}(x)\,dx.
\tag{2.11}
$$

An indicator of a bounded interval is also allowed in any position
of (2.11). To prove this extension, approximate it by nonnegative
smooth functions bounded by one. Their difference is supported in
intervals near the two endpoints with total length tending to zero.
Let `D_N` be the weighted count of this difference. It is bounded
by `X_N(I^+)` for one fixed larger interval, and exact intensity
gives `E D_N` at most the boundary-strip length. For any `A>0`,

$$
\mathbb E D_N^k
\le\mathbb E[X_N(I^+)^k\mathbf1_{X_N(I^+)>A}]
+A^{k-1}\mathbb E D_N.
\tag{2.12}
$$

By (1.1), first choose `A` large and then make the strips small.
This proves `sup_N ||D_N||_(L^k)->0`. Product telescoping and
Hölder now pass (2.11) to the interval indicators. The limit side
follows either from the same argument or from (2.7) and ordinary
dominated convergence.

For every fixed finite collection of these compact supports, once
`N` exceeds their combined diameter, at most one periodic copy of
each eigenvalue label lies in the collection. Formula (2.3) is then
exactly the factorial tuple integral of the unfolded point measure.
Repeated eigenvalues cause no problem: their labels are different,
and the factorial measure retains those multiplicities. Counts at
fixed boundaries vanish almost surely because intensity is one.

In particular, for each fixed `R>0`,

$$
\mathbb E(X_N([0,R]))_k\longrightarrow
\int_{[0,R]^k}\rho_k^{\mathrm{sine}}(y)\,dy\le R^k.
\tag{2.13}
$$

## 3. The large-window density without an ergodic theorem

Put

$$
Y_{N,R}=X_N([0,R])/R,
\qquad R\ge1.
$$

Its expectation is exactly one for every `N,R`.

For every nonnegative integer `n`,

$$
n^k\le k^k(n)_k+k^{k-1}n.
\tag{3.1}
$$

Indeed, if `n>=k`, each factor in `(n)_k` is at least `n/k`;
if `n<k`, then `n^k<=k^(k-1)n`. Therefore (2.13) implies

$$
\limsup_N\mathbb E Y_{N,R}^k\le C_0,
\qquad C_0=k^k+k^{k-1},\quad R\ge1.
\tag{3.2}
$$

There is also the sharper elementary bound

$$
0\le n^k-(n)_k\le {k\choose2}n^{k-1}.
\tag{3.3}
$$

It counts maps from a `k`-element set into an `n`-element set.
The difference counts the noninjective maps. Such a map has at
least one pair with the same image; the union bound over the
`binom(k,2)` pairs gives (3.3).

Combining (2.13), (3.2), (3.3), and Hölder gives

$$
\limsup_N\mathbb E Y_{N,R}^k
\le1+\frac{C_1}{R},\qquad
C_1={k\choose2}C_0^{(k-1)/k}.
\tag{3.4}
$$

For `x>=0` and an integer `k>=2`,

$$
|x-1|^k\le x^k-1-k(x-1).
\tag{3.5}
$$

For `x>=1`, expand `(1+(x-1))^k`: the omitted terms of degrees
two through `k` are nonnegative and include `(x-1)^k`. For
`0<=x<=1`, put `t=1-x`. The difference between the right and
left sides of (3.5) is
`(1-t)^k-1+kt-t^k`; its value at zero is zero and its derivative
is `k[1-(1-t)^(k-1)-t^(k-1)]>=0` on `[0,1]`. This proves
(3.5) in both ranges.

Taking expectations, the linear term cancels by exact intensity.
Thus

$$
\boxed{
\limsup_N\mathbb E|Y_{N,R}-1|^k\le\frac{C_1}{R}.
}
\tag{3.6}
$$

This is the needed concentration of the large-window density. It
uses a fixed `R` dimension limit and then allows `R` to increase.
It assumes neither ergodicity nor an already constructed limiting
process. In particular, no exchange of a window growing with `N`
with the original moment hypothesis has occurred.

## 4. Recovering a lower local factorial moment

Fix `1<=j<k`, put `r=k-j`, and let `h>=0` be a smooth function
supported in a bounded interval `I`. Define the ordered local
moment

$$
A_{j,N}(h)=F_{j,N}(h,\ldots,h).
$$

For every fixed `R>=1`, consider the mixed higher moment

$$
Q_{j,N,R}(h)=R^{-r}
F_{k,N}(\underbrace{h,\ldots,h}_{j},
        \underbrace{\mathbf1_{[0,R]},\ldots,
                    \mathbf1_{[0,R]}}_{r}).
\tag{4.1}
$$

For large enough `N`, each tuple lies within a fixed region of
diameter less than `N`, so it has the exact factorial point-count
interpretation from Section 2. For a particular ordered distinct
local `j`-tuple, let `d` be the number of its selected points lying
in `[0,R]`. If `y=X_N([0,R])`, the number of allowed ordered
choices of the remaining `r` points is exactly

$$
(y-d)_r,\qquad 0\le d\le\min(j,y).
\tag{4.2}
$$

This explicitly removes collisions with the selected local points.
There is no independence assertion.

For these integers, elementary product telescoping gives a constant
depending only on `k` such that

$$
\left|\frac{(y-d)_r}{R^r}-1\right|
\le\left|\left(\frac yR\right)^r-1\right|
+\frac{C_k}{R}\left(1+\left(\frac yR\right)^{r-1}\right).
\tag{4.3}
$$

Indeed, replacing the factors `y-d-a` one at a time by `y`
bounds `|(y-d)_r-y^r|` by `rk(y+k)^(r-1)`. Divide by
`R^r` and use `R>=1` to obtain (4.3).

For `z>=0`,

$$
|z^r-1|\le r|z-1|(1+z^{r-1}).
$$

Hölder, with (3.2) and (3.6), therefore implies

$$
\limsup_N
\left\|
\max_{0\le d\le\min(j,X_N([0,R]))}
\left|\frac{(X_N([0,R])-d)_r}{R^r}-1\right|
\right\|_{L^{k/r}}
\le C_k' R^{-1/k}.
\tag{4.4}
$$

The term of degree `r-1` is controlled in `L^(k/(r-1))`
when `r>1`; for `r=1` it is the constant one. Explicitly,
the norm of `|z-1|z^(r-1)` in `L^(k/r)` is at most
`||z-1||_(L^k)||z||_(L^k)^(r-1)`, and the remaining
polynomial terms have norm bounded by (3.2). This verifies all
exponents in (4.4).

The weighted sum over the local tuples is at most
`||h||_infty^j X_N(I)^j`. Its `L^(k/j)` norm is bounded
uniformly in `N` by (1.1). Since `j/k+r/k=1`, Hölder
applied to (4.2)--(4.4) proves

$$
\boxed{
\limsup_N|Q_{j,N,R}(h)-A_{j,N}(h)|
\le C_{h,k}R^{-1/k}.
}
\tag{4.5}
$$

For each fixed `R`, (2.11) with its indicator extension also gives

$$
Q_{j,N,R}(h)\longrightarrow
R^{-r}\int_{\mathbb R^j}\prod_{a=1}^j h(x_a)
\int_{[0,R]^r}\rho_k^{\mathrm{sine}}(x,y)\,dy\,dx.
\tag{4.6}
$$

The next section evaluates the large-`R` limit of this deterministic
comparison integral.

## 5. Direct contraction of the sine determinant

Expand the `k` by `k` sine determinant in permutations. The
permutations fixing every one of the `r` new indices `y_1,...,y_r`
sum exactly to `rho_j^sine(x)`, since all their new diagonal
kernel factors equal one. Every remaining permutation has a
new index `a` with `sigma(a) != a`. Its product contains a
factor `K(y_a-z_sigma(a))` whose second argument is independent
of `y_a` when the other integration variables are held fixed.
All remaining factors have modulus at most one.

The elementary pointwise estimate

$$
|K(t)|\le\min(1,1/(\pi|t|))
$$

implies

$$
\int_{\mathbb R}|K(t)|^2dt
\le2+2/\pi^2<3.
$$

Cauchy--Schwarz therefore gives, uniformly in the other argument,

$$
\int_0^R|K(y-a)|\,dy\le\sqrt{3R}.
$$

Integrating the other `r-1` new variables costs at most `R^(r-1)`.
There are at most `k!` permutation terms. Hence, uniformly in
all real `x_1,...,x_j`,

$$
\left|
R^{-r}\int_{[0,R]^r}\rho_k^{\mathrm{sine}}(x,y)\,dy
-\rho_j^{\mathrm{sine}}(x)
\right|
\le\sqrt3\,k!R^{-1/2}.
\tag{5.1}
$$

This proof works even when some old coordinates coincide. It
does not assume factorization or discard an unestimated
off-diagonal determinant term; each such term has just been bounded
after integrating a variable on which its chosen factor depends.

Combining (4.5), (4.6), and (5.1) yields

$$
\limsup_N\left|
A_{j,N}(h)-\int\prod_{a=1}^j h(x_a)
\rho_j^{\mathrm{sine}}(x)\,dx
\right|
\le C_{h,k}R^{-1/k}
+\sqrt3\,k!\|h\|_1^jR^{-1/2}.
$$

Letting `R` tend to infinity proves convergence for every smooth
compact nonnegative `h` at order `j`.

## 6. Returning to the exact Schwartz tests of the criterion

Let now `b` be one of the original admissible nonnegative Schwartz
tests. Take smooth compact cutoffs `0<=chi_L<=1` equal to one
on `[-L,L]`, and put `h_L=b chi_L`. Schwartz decay gives

$$
\|b-h_L\|_{\mathcal W}\longrightarrow0.
$$

The moment telescoping bound (2.4) remains valid at order `j`
by using (2.2) and `L^j <= L^k` on the probability space.
It therefore implies

$$
\sup_N|M^U_{j,N}(b)-M^U_{j,N}(h_L)|\longrightarrow0.
\tag{6.1}
$$

This uses the original periodized, distinct-label definitions for
the noncompact test. It does not replace them by a factorial
measure allowing two widely separated periodic copies of one
eigenvalue label.

The same convergence holds uniformly for the CUE comparison,
either by its exact finite Gram formula and (2.8) at order `j`,
or by dominated convergence with determinant bounded by one.
For fixed `L`, Section 5 proves that the deterministic and CUE
moments for `h_L` have the same limit. First take the dimension
limit at fixed `L`, then send `L` to infinity in (6.1). This gives

$$
M^U_{j,N}(b)-M^{\mathrm{CUE}}_{j,N}(b)\longrightarrow0,
$$

which is `H_j`. The proof of (0.2) is complete.

## 7. Implications and the precise remaining gap

The arguments in the companion and present notes establish two
structural facts about the original criterion:

1. Under the matching proved for the normalization endpoints in
   Round 9, each full fixed-order statement `H_k` transfers by
   itself. A moment of order `k+1` is unnecessary.
2. For any sequence of the specified uniformly shifted unitary
   spectra, a full `H_k` already contains every smaller-order
   statement. An unbounded set of complete orders is sufficient
   for the all-order criterion.

These facts do not provide a new estimate for the original signed
Heisenberg-time trace sums. In particular, no bound has been proved
for the first open fixed test

$$
N^{-2}\sum_{1\le m<2N}|\widehat b_*(m/N)|^2
\left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right).
$$

The proofs do not infer the full same-order hypothesis from this
single test. They do not take a bandwidth depending on `N`,
average over dimensions, change `tau`, or replace the original
matrices by random ones. The missing input remains an actual
asymptotic cancellation estimate for those original matrices.

