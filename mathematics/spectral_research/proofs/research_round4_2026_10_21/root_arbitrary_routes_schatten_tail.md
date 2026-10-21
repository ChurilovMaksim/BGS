> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/root_arbitrary_routes_schatten_tail.md`. Embedded SHA256: `d05c0bc44decafe181e28b06a603b2309567ae8808bb8dd5dc7a81aa14457e3e`.
> [Thematic guide](../../topics/dephasing.md).

# A uniform Schatten bound for arbitrary Weyl routes after a fixed initial interval

21 October 2026. Supplement to the root all-entry theorem, frozen in
`root_all_entry_and_arbitrary_weyl_routes.md`, SHA-256
`c6bd70cda16691533eb8c13aafa9055009f41a97c932c56eb901b4b4ef176ecd`.
The original family and the original fixed kick are unchanged.

## 1. Claim, including the finite initial interval

Use the notation `C,D_j,R_j,rho,g,eta` from that theorem, with
`rho=1-g>=1/2`. Put

$$
 p=35,\qquad
 \delta_* =\min\left\{\frac{-\log(1-g/2)}{2\log(2(2-g)/g)},\frac1{70}\right\}>0.
$$

For `n>=35`, let `B_(n,N)^*` be the exact sum of words with at most
`floor(delta_* n)` complementary factors in
`(D_n+R_n)...(D_1+R_1)`. Define `B_(n,N)^*=0` for `1<=n<35`.
Thus this particular comparison explicitly leaves the first 34 times
unchanged. The arbitrary permutations may vary at every step and with `N`.

There is a fixed finite `K`, independent of `N` and of all these choices,
such that for all sufficiently large odd `N`,

$$
 \boxed{\sum_{n\ge1}|\operatorname{Tr}B_{n,N}^*|\le K.}
 \tag{1.1}
$$

Consequently the correction to every normalized, bounded-weight pair-trace
functional is at most `WK/N^2`. This is a bound for the sum of absolute
traces; no bound for the sum of trace norms of all early-time operators is
asserted. The earlier theorem still supplies estimates for those early-time
word sums if one chooses to remove them.

## 2. Proof of a uniform, unnormalized Schatten-35 bound

Each selected matrix `D_j` is a weighted permutation. Its singular values
are the moduli of its selected entries. The column bound in the root
theorem and the reindexing by `S` give

$$
 \|D_j\|_{S_{35}}^{35}
 \le2^{34}C_*^{35}
 \left[\sum_{v\in\Lambda_N}(1+|v|_N)^{-35/17}
                         +(N^2-1)N^{-35}\right].
$$

There are `8r` nonzero centered labels on the square shell of radius `r`.
Extending the sum to the infinite lattice and using integral comparison,

$$
 \sum_{v\ne0}(1+|v|)^{-35/17}
 \le8\sum_{r\ge1}r^{-18/17}
 \le8\left(1+\int_1^\infty x^{-18/17}dx\right)=144.
$$

The other term is at most one. Hence every selected factor satisfies

$$
 \boxed{\|D_j\|_{S_{35}}^{35}\le A:=145\,2^{34}C_*^{35}.}
 \tag{2.1}
$$

This estimate has no factor of the operator-space dimension.

## 3. Trace Holder and the exact word sum

The finite-dimensional inequality

$$
 |\operatorname{Tr}(X_1\cdots X_p)|\le\prod_{j=1}^p\|X_j\|_{S_p},
 \quad \|AXB\|_{S_p}\le\|A\|\|X\|_{S_p}\|B\|
 \tag{3.1}
$$

is proved in full in Section 2 of
`dual_sparse_cat_schatten_trace_sharpening.md`, SHA-256
`784f41271c57c3655215239153fafcd66dc9ecebdcab5eb462d6f25b451bc92d`.
The root has independently reconstructed that proof. In detail, exterior
powers give prefix-sum majorization for logarithms of singular values of a
product by the sums of the individual logarithms. Equality of full sums
comes from determinants. Integrating the inequalities for positive parts
against `exp(t)` proves the bound by the sum of aligned singular-value
products. Scalar Holder then gives (3.1); singular factors follow by
continuity. The ideal estimate follows directly from the positive-matrix
inequality `(XY)(XY)*<=||Y||^2 XX*` and the min-max principle. Thus (3.1)
introduces no extra assumption about the quantum evolution.

For `n>=35` and `r<=floor(delta_* n)`, there are at least 35 selected
factors: `n-r>=(1-1/70)n>=34.5`, and this number is integral. Select 35 of
them in the cyclic trace, apply (3.1) to the intervening 35 blocks, and use
(2.1). Charge every other factor in operator norm. The result is

$$
 |\operatorname{Tr}(\mathrm{word})|
       \le A\rho^{n-r-35}(2-g)^r.
 \tag{3.2}
$$

The words and the selected factors may be different at every time. No
commutation or independence was used. The binomial majorant from the root
theorem still holds for the smaller density `delta_*`:

$$
 \sum_{r\le\lfloor\delta_*n\rfloor}\binom nr
                \rho^{n-r}(2-g)^r\le\eta^n.
$$

Summing (3.2) therefore proves

$$
 |\operatorname{Tr}B_{n,N}^*|\le A\rho^{-35}\eta^n,
 \quad n\ge35.
$$

The geometric series gives (1.1) with, for example,
`K=A rho^(-35)/(1-eta)`. All constants depend only on the fixed original
family. For bounded complex weights,

$$
 \frac1{N^2}\sum_{n\ge1}|w_{n,N}|\,|\operatorname{Tr}B_{n,N}^*|
                                              \le WK/N^2.
$$

This is an estimate on the exact coherent trace correction over all retained
times, including arbitrarily long ones. It still gives no CUE value for
`Tr(C^n-B_(n,N)^*)`.

