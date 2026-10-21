> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round10_2026_10_21/r10_arithmetic_audit_downward_heredity.md`. Embedded SHA256: `40ce3feb3303f1cd1b42328d87fa4c936581746867e49c68edc0d6387f7ecf73`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Independent audit: one complete order implies all lower orders

21 October 2026. Auditor: `/root/r10_arithmetic`.

## 0. Object and verdict

Audited source: `research_round10_2026_10_21/r10_weyl_downward_moment_heredity.md`.

The initial complete mathematical text had SHA-256 `360f63ae8f42fea11086d8d56ffe984412787b04071603d22b722bf51eb9a520`. It was read in full. The version with one repaired TeX escape had SHA-256 `50079049ff2e24701bdff1fdf1e00412be3a8ee4fca60a944bc8e8198490f809` and was also read in full. The single escape change was independently verified by reconstructing the initial SHA from the revised raw bytes. A further bare carriage return inside the intended command `\rm distinct` was reported and corrected before final freezing. The final audited raw-byte SHA-256 is `ba5e5fb7b2d812c8b9a9f28f2f555412399d0e749d941af2723137be206c65dd`.

Its companion input is the independently audited orderwise-repulsion note, SHA-256 `63ddeba5e72b200bf3dd16bed795423d4ed7e070a0b0e3f55fa30b93d3bc53d2`. My independent audit of that input is `r10_arithmetic_audit_orderwise_repulsion.md`, SHA-256 `9865af8e544636611c09a8490f3b37380d36c085fb3380f9260d6bc226462fca`.

**Verdict: the complete mathematical chain passes.** A full criterion `H_k`, meaning every admissible test at one fixed order `k>=2`, implies `H_j` at every `j<=k`. No spectral matching, ergodicity hypothesis, point-process weak limit, or moment above order `k` is required.

This audit does not assert `H_k` for the original matrix family at any order. The exact first pair discrepancy remains unestimated. The theorem concerns the logical strength of a full fixed-order hypothesis; it does not start from the one isolated test `b_*`.

## 1. The same-order input is sufficient and explicit

The preceding audit checked directly that `H_k` implies uniform integrability of `X_N(I)^k` for each fixed bounded interval `I`. Its quantitative tail estimate is

$$
\limsup_N\mathbb E[X_N(I)^k\mathbf1_{X_N(I)>2kM}]
\le C_{k,\beta}|I|^{k^2}M^{-k(k-1)}.
\tag{1.1}
$$

It is obtained from the finite CUE Vandermonde estimate and a partition into `M` cells. Every `M` is fixed before the dimension limit. This supplies precisely the local `k`th moments used in the descent proof. It supplies no higher prelimit moment, and the descent does not request one.

In particular, stationarity and Minkowski give, for

$$
\|a\|_{\mathcal W}=\sum_{n\in\mathbb Z}\sup_{[n,n+1]}|a|,
$$

the bound

$$
\sup_N\|\langle|a|,\Xi_N\rangle\|_{L^k}
\le C\|a\|_{\mathcal W}.
\tag{1.2}
$$

Unit-cell endpoints have zero mass almost surely by exact intensity, so their harmless double coverage in this envelope does not affect the argument. All constants for unit intervals are independent of translation.

## 2. Admissible smoothing and polarization

For nonnegative smooth compact `h` with supremum less than one, let `h_B=h*K_B`, using a nonnegative Schwartz probability kernel with smooth compact Fourier support. Then `h_B` is an admissible test at every fixed `B`: positivity, the strict supremum bound, Schwartz decay, and smooth compact Fourier support all hold.

The source proves convergence in the stronger norm `mathcal W`, not merely in `L^1`. The proof is valid:

$$
\|h(\cdot-t)\|_{\mathcal W}\le2\|h\|_{\mathcal W},
\qquad
\|h(\cdot-t)-h\|_{\mathcal W}\longrightarrow0\quad(t\to0).
$$

Each translated unit cell overlaps at most two original cells, giving the first inequality. For small `t`, the difference is supported in one fixed compact interval and tends uniformly to zero, giving the second. Thus

$$
\|h_B-h\|_{\mathcal W}
\le\int K(u)\|h(\cdot-u/B)-h\|_{\mathcal W}du\longrightarrow0
\tag{2.1}
$$

by the integrable dominating bound `3K(u)||h||_W`.

Telescoping the ordered distinct-label products and applying Hölder to `k` weighted counts gives the required continuity of the deterministic diagonal polynomial. The exact finite CUE Gram determinant is bounded by one, giving the benchmark continuity in `L^1`. With `B` fixed before `N`, these facts extend `H_k` to all nonnegative smooth compact diagonal tests. Scaling removes any restriction on their supremum.

For the symmetric multilinear functional `F`, its diagonal `P(a)=F(a,...,a)` obeys

$$
\sum_{S\subset[k]}(-1)^{k-|S|}P\!\left(\sum_{i\in S}h_i\right)
=k!F(h_1,\ldots,h_k).
\tag{2.2}
$$

The factor `k!` is correct: every surviving monomial uses each of the `k` labels once, and the argument permutations all give the same value. All sums on the right are nonnegative; a scalar rescaling is enough to place them in the previously justified diagonal class. Negative admissible functions are not being assumed.

This obtains the full mixed `k`-point convergence for compact smooth tests. It uses finitely many fixed tests at a time.

## 3. Indicator tests and original-label copies

An interval indicator can be approximated by a smooth function between zero and one, agreeing with it away from small endpoint strips. Interpret the error count as

$$
D_N=\langle|\mathbf1_I-h|,\Xi_N\rangle\ge0.
$$

It obeys `D_N<=X_N(I^+)` for one fixed larger interval and `E D_N<=|strips|` by exact intensity. For every threshold `A`,

$$
\mathbb ED_N^k
\le\mathbb E[X_N(I^+)^k\mathbf1_{X_N(I^+)>A}]
+A^{k-1}\mathbb ED_N.
\tag{3.1}
$$

First the already proved `k`th-power uniform integrability makes the first term small, then the strip width makes the second small. This proves uniform convergence in weighted-count `L^k`. Hölder passes the mixed moments to the indicators. The argument is noncircular: the needed uniform integrability came from band-limited positive majorants, before the indicator approximation.

For all these compact mixed tests, require `N` larger than the diameter of the **union** of their supports. The union condition is needed: bounding each support's diameter separately would not prevent different supports from containing two copies of one original label. The source correctly uses the combined diameter. Under it, the distinct-label functional is precisely the factorial tuple count of the unfolded measure in that region. Multiplicities of different eigenvalue labels remain included.

Consequently, for each fixed `R`,

$$
\mathbb E(X_N([0,R]))_k\longrightarrow
\int_{[0,R]^k}\rho_k^{\rm sine}\le R^k.
\tag{3.2}
$$

This is the exact finite-window input to the next step, obtained before allowing `R` to grow.

## 4. Finite-dimensional density estimate

Set `Y=X_N([0,R])/R`, with `R>=1`. Exact intensity gives `EY=1` for every dimension, without taking a limit.

The source uses two elementary integer inequalities:

$$
n^k\le k^k(n)_k+k^{k-1}n,
\qquad
0\le n^k-(n)_k\le {k\choose2}n^{k-1}.
\tag{4.1}
$$

For the first, if `n>=k` every factor in `(n)_k` is at least `n/k`; if `n<k`, its second summand suffices. The second counts noninjective maps by choosing a colliding pair and then its image and all other images. It is valid even for `n<k`, when `(n)_k=0`, and for `n=0`.

The first bound, together with (3.2), gives

$$
\limsup_N\mathbb E Y^k\le C_0=k^k+k^{k-1},
$$

uniformly in the later choice of fixed `R>=1`. The second then gives

$$
\limsup_N\mathbb EY^k
\le1+\frac{{k\choose2}C_0^{(k-1)/k}}{R}.
\tag{4.2}
$$

Here Hölder controls the `(k-1)`st moment by the established `k`th moment. No convergence of a lower factorial moment has been assumed.

For `y>=0`, the exact inequality

$$
|y-1|^k\le y^k-1-k(y-1)
\tag{4.3}
$$

holds with constant one. The binomial expansion proves it for `y>=1`. For `y=1-t`, `0<=t<=1`, the difference has derivative `k[1-(1-t)^(k-1)-t^(k-1)]>=0` and starts at zero. Thus (4.2), (4.3), and `EY=1` yield

$$
\limsup_N\mathbb E|Y-1|^k\le C_1/R.
\tag{4.4}
$$

This is a two-stage limit statement: each `R` is fixed while `N` tends to infinity. The proof does not use a uniform rate of `H_k` for windows growing with `N`. It also does not invoke an ergodic theorem or a previously existing limiting point process.

## 5. The exact exclusion count and Hölder exponents

Fix `j<k`, write `r=k-j`, and select one ordered distinct local `j`-tuple. Let `y=X_N([0,R])` and let `d` be the number of these selected labels whose lifted points lie in `[0,R]`. Provided the combined-support diameter is less than `N`, the exact number of available ordered distinct choices for the remaining `r` labels is

$$
(y-d)_r,\qquad 0\le d\le\min(j,y).
\tag{5.1}
$$

The use of `d`, rather than automatically `j`, is necessary when the local test has support outside `[0,R]`. The source retains it explicitly. There is also no omitted collision via another periodic copy: the combined-diameter condition has already excluded that possibility.

Product telescoping gives

$$
|(y-d)_r-y^r|\le rk(y+k)^{r-1}.
\tag{5.2}
$$

This remains true when `y-d<r`; the falling product has a zero factor, and the absolute values of its individual factors are still bounded by `y+k`. After dividing by `R^r`, (5.2) is at most `C_k R^(-1)(1+Y^(r-1))`.

The other difference is bounded by

$$
|Y^r-1|\le r|Y-1|(1+Y^{r-1}).
$$

Its `L^(k/r)` norm is controlled using `||Y-1||_k` and `||Y||_k^(r-1)`. For `r=1` the additional factor is constant. Together with (4.4), these estimates give

$$
\limsup_N\left\|
\max_{0\le d\le\min(j,y)}\left|(y-d)_r/R^r-1\right|
\right\|_{k/r}\le C_k'R^{-1/k}.
\tag{5.3}
$$

The random local `j`-tuple weight sum is bounded by `||h||_infinity^j X_N(I)^j`, so it has a uniformly bounded `L^(k/j)` norm. Since `j/k+r/k=1`, Hölder gives exactly the source's normalized mixed-moment approximation at error `O_(h,k)(R^(-1/k))`. Independence between the local tuple and the large-window count is neither true in general nor needed.

The auxiliary finite checks enumerate actual ordered selections with repeated point positions and with some selected points inside and some outside the counting window. All ten tested mixed-count identities agree exactly with (5.1). A further 16,951 integer cases verify the polynomial bound (5.2). The general proofs above, not those enumerations, establish the result.

## 6. The sine determinant is contracted with an estimated remainder

In the permutation expansion of `rho_k^sine(x,y)`, the permutations fixing every one of the `r` new indices contribute exactly `rho_j^sine(x)`. Every remaining permutation moves some new index `a`, hence contains a factor

$$
K(y_a-z_{\sigma(a)}),\qquad\sigma(a)\ne a.
$$

Its second argument is independent of `y_a` when all other variables are fixed. Although other factors may also depend on `y_a`, replacing their absolute values by their upper bound one makes that dependence irrelevant for the upper bound. This is a valid inequality, not an independence or phase-cancellation assertion.

The elementary bounds

$$
|K(t)|\le\min(1,1/(\pi|t|)),\qquad
\int_{\mathbb R}|K(t)|^2dt\le2+2/\pi^2<3
$$

give uniformly in real `z`

$$
\int_0^R|K(y-z)|dy\le\sqrt{3R}.
$$

The other `r-1` integrations cost at most `R^(r-1)`. Summing at most `k!` terms proves the explicit uniform estimate

$$
\left|R^{-r}\int_{[0,R]^r}\rho_k^{\rm sine}(x,y)dy
-\rho_j^{\rm sine}(x)\right|
\le\sqrt3\,k!R^{-1/2}.
\tag{6.1}
$$

No off-diagonal determinant contribution is discarded without a bound. The estimate is valid even at coincident old coordinates. Combining (6.1) with (5.3), and only then allowing `R` to tend to infinity, proves the lower-order diagonal moment convergence for nonnegative smooth compact tests.

## 7. Return to the criterion's exact noncompact tests

If `b` is an admissible Schwartz test, choose smooth compact cutoffs and put `h_L=b chi_L`. Then `||b-h_L||_W->0`. The product telescoping bound at order `j` is justified by the same weighted-count estimate (1.2), since on the probability space `L^j` norms are bounded by `L^k` norms for `j<=k`.

This gives uniform convergence of the deterministic moments for `h_L` to those for `b` as `L` increases. The exact finite CUE Gram bound gives the same approximation uniformly in `N` using `L^1` instead of `mathcal W`. At fixed `L` the deterministic and CUE moments have the same limit, so taking `N` first and then `L` completes `H_j`.

The original distinct-label periodized definition is kept for these noncompact weights. The proof does not allow several widely separated copies of one label in a factorial tuple.

The assertion that an unbounded collection of complete orders suffices for all orders is now logical: for any desired fixed `j`, choose one available `k>=j` and apply the theorem. It imposes no simultaneous uniformity across orders. It also supplies no information about orders above one fixed known `k`.

## 8. Verification and status

The script and JSON manifest `r10_arithmetic_exact_checks` record exact input hashes and finite checks. The successful run includes 451 integer cases for (4.1), 9,460 rational cases for (4.3), 16,951 exclusion-polynomial cases, and ten complete selected-label identities. The previous orderwise checks are retained. No floating-point eigenphase calculation is involved.

The source's theorem is a valid structural strengthening of the criterion. Its hypothesis remains unproved for the specified original family; the audit does not conceal that missing hypothesis or promote a proof of one isolated pair test into the full `H_k` premise.

### Final raw-byte freeze

The final source has SHA-256 `ba5e5fb7b2d812c8b9a9f28f2f555412399d0e749d941af2723137be206c65dd` and contains no carriage returns. Replacing its one literal `\rm distinct` command by the original carriage-return-plus-`m distinct` bytes reconstructs SHA-256 `50079049ff2e24701bdff1fdf1e00412be3a8ee4fca60a944bc8e8198490f809`. Undoing the one corrected `\left` escape as well reconstructs SHA-256 `360f63ae8f42fea11086d8d56ffe984412787b04071603d22b722bf51eb9a520`. Thus the precise differences from the fully read initial proof were independently checked at the byte level and are formatting changes only.
