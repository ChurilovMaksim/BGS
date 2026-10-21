> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_shrinking_gap_signed_removal.md`. Embedded SHA256: `cb90be5f0058eb2c2188c36b9ed53602060e1af2068f3745c64da86199b8b7d2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: all-time signed removal with a shrinking gap

Date: 21 October 2026.

## 0. Verdict and exact scope

**Primary verdict: proved as written for the general estimates in §§2–5, the original-family application in §6, and the late-time and failed-majorant statements in §7.** No missing estimate was found in the stated chain. The original `H_diag` problem remains open; the theorem removes only its explicitly defined subset of character histories.

The frozen primary source is:

- `research_round4_2026_10_21/counter_shrinking_gap_signed_removal.md`;
- SHA-256 `afde78e7a2e14403792eca9e0d5b92ec4831544fd1e8a79fe4b3fb7a5bdfb9c5`.

The source was read in full and its hash was checked on disk. Its dependence on the growing-order escape theorem is covered by the separately written independent audit `audit_growing_order_comb_quantitative.md`, SHA-256 `30a2039b988d49f12960ffb1d27fc72dedc6eefcb38d005d75ebee06c5de17cb`.

For the translated-product constants, the raw proof in `research_round3_2026_10_21/phase_logtime_dispersion_and_missing_modes.md`, §§2–7, was read and reconstructed. The related raw translation argument in `phase_sparse_character_histories.md`, §§2–4, was also read. The verdict below does not infer the required uniformity from a prior PASS label or from a fixed-time asymptotic statement.

Only this new audit file is written. All prior source manuscripts and audits remain unchanged.

## 1. Exact character decomposition and the meaning of the gap

For odd `N=d^2m`, the Weyl subgroup with labels `(sN/d,uN/d)` has trivial product cocycle, since their pairwise symplectic products are multiples of `N`. Its character projectors are orthogonal and have rank `m`. The trace computation giving this rank is exact: the identity term contributes `N/d^2=m`, and each other Weyl element has trace zero.

The exact quadratic covariance implies that `M_N` permutes these characters by `S chi=chi composed with L`, where

$$
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix}.
$$

Thus

$$
K=\left(\sum_\chi P_\chi E_NP_\chi\right)M_N
$$

has exactly the blocks following this permutation, and `R=U_N-K` has exactly the complementary blocks. If the diagonal compression norm is bounded by `rho=1-g`, then `||K||<=rho` and `||R||<=2-g`. The general estimates are correctly conditional on this single explicitly stated norm bound. Section 6 supplies it for the actual family and the stated divisors; it is not left as a new assumption in that application.

## 2. Pure histories: arithmetic count and the full sum

Let `c_n=Tr K^n`. Only characters fixed by `S^n` contribute to this trace. Each contributing block has dimension `m` and norm at most `rho^n`.

The kernel bound used to count such characters is valid over composite moduli. For an integer matrix `B` invertible over `Q`, and an integer lift `x` satisfying `Bx=d y`, map its kernel residue to `y mod B Z^2`. This is well defined because changing `x` by `dz` changes `y` by `Bz`. If two images agree, then `B(x-x'-dz)=0`; rational invertibility gives equality modulo `d`. The injection into the finite cokernel proves the upper bound `|det B|`.

The eigenvalues of `L` are `lambda=3+2sqrt(2)` and `lambda^-1`. Therefore `B=(L^T)^n-I` is rationally invertible and

$$
|\det B|=\lambda^n+\lambda^{-n}-2\le\lambda^n.
$$

Combining this with the trivial count `d^2` gives

$$
|c_n|/N\le\rho^n\min\{1,\lambda^n/d^2\}.
\tag{2.1}
$$

To check the constants in its sum, set `x=2log d/log lambda` and `j=floor x`. Since `rho>=1/2` and `lambda/2>1`,

$$
\sum_{n\ge1}\rho^n\min\{1,\lambda^n/d^2\}
\le d^{-2}\frac{(\lambda\rho)^{j+1}}{\lambda\rho-1}
 +\frac{\rho^{j+1}}g.
$$

For the first term, `d^-2(lambda rho)^(j+1)=(lambda rho)^(j+1-x)rho^x<=lambda rho rho^x`. For the second, `rho^(j+1)<=rho^x`. The fraction `lambda rho/(lambda rho-1)` is at most `lambda/(lambda-2)<2`, while `1/g>=2`. Hence

$$
\sum_{n\ge1}\rho^n\min\{1,\lambda^n/d^2\}
\le\frac2g\exp[-c_\lambda g\log d],
\qquad c_\lambda=\frac2{\log\lambda}.
\tag{2.2}
$$

The floor and the direction of the inequalities are correct even when `x` is integral.

For `|p_n|<=N` and any `|c_n|<=Na_n` with `a_n<=1`,

$$
N^{-2}\big||p_n|^2-|p_n-c_n|^2\big|
\le2a_n+a_n^2\le3a_n.
\tag{2.3}
$$

Multiplying by arbitrary weights bounded by `W` and summing (2.2) proves exactly the source's factor `6W/g`. It controls the complete square difference, including the cross-term. The difference series is absolutely convergent at each dimension; the separate unweighted infinite series need not converge.

Taking logarithms of the bound gives the correct sufficient condition

$$
c_\lambda g_N\log d_N-\log(1/g_N)\longrightarrow+\infty.
\tag{2.4}
$$

No unmentioned relation between `g_N` and `d_N` is used.

## 3. Sum of all words with the allowed number of changes

The parameters are

$$
z=\frac g{2(2-g)},\qquad r_*=1-g/2,
\qquad
\delta(g)=\frac{-\log r_*}{2\log(1/z)},
\qquad\eta=\sqrt{r_*}.
$$

For `0<g<=1/2`, these obey `0<z<1`, `0<delta<1`, and `eta<1`. A word with `j` letters `R` has norm at most `rho^(n-j)(2-g)^j`. For the retained values `j<=floor(delta n)`, `z^j>=z^(delta n)`. Thus, summing all placements,

$$
\|S_n\|
\le z^{-\delta n}\sum_{j=0}^n\binom nj
\rho^{n-j}[z(2-g)]^j
=\left(z^{-\delta}r_*\right)^n
=\eta^n.
\tag{3.1}
$$

In the last step, `z^-delta=r_*^-1/2`. The estimate has already included every permitted number of changes and every placement, not a selected word. Inserting character projectors shows that the decomposition into `K` and `R` really partitions the histories by whether each transition follows the fixed permutation. Returning to a previously visited character does not alter that count.

## 4. Why the short-time constants are uniform in the shrinking gap

Finite character orthogonality gives the exact pinching identity

$$
\sum_\chi P_\chi E_NP_\chi
=d^{-2}\sum_{a\in(\mathbb Z/d\mathbb Z)^2}H_d(a)E_NH_d(a)^*.
\tag{4.1}
$$

Each average has total absolute coefficient one. Expanding `R=U_0-K` in a word with `j` letters `R` costs total absolute coefficient at most `2^j`. Summing all retained words costs at most `sum_j binomial(n,j)2^j<=3^n`. These bounds are independent of the group cardinality and of the density parameter. The group average is an exact operator identity inside the proof, not an average of the requested spectral statistic.

For `H=T_N(a_0,b_0)`, exact conjugation multiplies mode `(k,l)` by `e_N(a_0k-b_0l)`. In the real-half symbol convention this is precisely the real translation

$$
a(q,p)\longmapsto a(q+a_0/N,p-b_0/N).
\tag{4.2}
$$

It preserves the finite Fourier support and every coefficient modulus. It also preserves every complex-strip derivative bound because the shifts are real.

The raw dispersion proof was checked at its actual uniformity points:

1. Its graph class is `p=rq+b+w(q)`, with slope `-1<=r<=-1/2`, a fixed strip of width `10^-3`, and uniformly tiny holomorphic `w`. The linear graph transform has denominator `3-4r>=5`, doubles the available strip, contracts the perturbation by at least five, and keeps the new slope in a fixed interior interval.
2. Every translated kick has the same complex field bounds as the original one, because of (4.2). Its time is fixed. The small characteristic displacement and the inverse-function contraction preserve the original strip and graph class. No derivative loss accumulates with the number of steps.
3. For a localized sampled WKB vector, direct expansion of the finitely many shifts gives the Hamilton–Jacobi equation, the transport equation, and a pointwise residual of order `h^(5/2)` after normalization, hence a vector residual of order `h^2`. Unitary Duhamel divides by `h` and yields a one-step error `O(h)` times the input amplitude norm. This is a finite-shift expansion in the sampling scale, not in the large product `tau N`.
4. The exact eight-character decomposition of the modular quadratic kernel precedes ordinary Poisson summation. The input momentum intercept may be reduced by an integer at the sampled level. The fixed chart supports and fixed derivative bounds leave a bounded set of stationary Poisson indices, independent of the translation sequence and the iteration count. The other indices are controlled by four integrations by parts.
5. The retained phases are uniformly strictly concave in their integration variable. The elementary quadratic change of variable in the raw source gives a stationary-phase vector error `O(h)` with a fixed `C^4` amplitude bound. The leading amplitudes are produced by a fixed finite collection of maps; their total `C^4` norm grows by at most one fixed factor per step.
6. Previous error vectors are acted on by exact unitary translated factors, so their norms do not grow during later propagation.

These facts justify, for every sequence of real translations, the same recurrences

$$
\mathcal A_{n+1}\le A_0\mathcal A_n,
\qquad
\|\text{new error}\|_2\le C_0h\mathcal A_n.
\tag{4.3}
$$

The raw source uses `h=N^-1`, whereas the new manuscript sometimes writes `h=(2pi N)^-1` in this bookkeeping. This changes the unspecified fixed error constant by the factor `2pi` only. It does not change the finite matrix being estimated, the original time, the uniformity assertions, or any numerical exponent in the final summation.

Choosing a fixed `A_*>max(2,A_0)` and summing the geometric error recurrence proves

$$
\max_{x,y}|(U_{a_n,N}\cdots U_{a_1,N})_{xy}|
\le C_*A_*^nN^{-1/2}.
\tag{4.4}
$$

The constants depend on the original fixed polynomial, its fixed kick, graph strips, and cutoffs. They do not depend on the gap, the divisor, the escape order, or the selected translation sequence. Bounds exceeding one at large `n` remain valid. Finitely many excluded small dimensions, if needed, can be absorbed into a fixed larger `C_*`; the application is asymptotic in any event.

Taking a trace and applying the exact coefficient cost `3^n` proves

$$
|s_n|/N\le C_*N^{-1/2}B^n,\qquad B=3A_*>1.
\tag{4.5}
$$

This is the only short-time analytic input used in the new summation, and its required parameter independence has been checked directly.

## 5. All-time summation with the reciprocal gap retained

Combine (3.1) and (4.5):

$$
|s_n|/N\le a_n:=\min\{C_*N^{-1/2}B^n,\eta^n\}\le1.
$$

The square difference obeys (2.3) with `c_n` replaced by `s_n`. Put

$$
n_0=\left\lfloor\frac{\log N}{4\log B}\right\rfloor.
$$

The initial geometric sum is bounded by

$$
C_*N^{-1/2}\sum_{n=1}^{n_0}B^n
\le\frac{C_*B}{B-1}N^{-1/4}.
$$

For the tail, use

$$
\log\eta\le-g/4,
\qquad 1-\eta=\frac{g/2}{1+\eta}\ge g/4,
\qquad n_0+1>\frac{\log N}{4\log B}.
$$

This gives

$$
\sum_{n>n_0}\eta^n
\le\frac4g\exp\!\left[-\frac{g\log N}{16\log B}\right].
$$

Hence the full signed correction is at most

$$
3W\left[C_BN^{-1/4}+\frac4g e^{-c_Bg\log N}\right],
\qquad
C_B=\frac{C_*B}{B-1},\quad c_B=\frac1{16\log B}.
\tag{5.1}
$$

Both constants are independent of the arithmetic parameters. No dominated-convergence argument with a shrinking majorant has been used. The exact sufficient condition from this bound is

$$
c_Bg_N\log N-\log(1/g_N)\longrightarrow+\infty.
\tag{5.2}
$$

The positive numerical factor `c_B` cannot generally be removed from this criterion.

For the pair factorial functional, its `1/2` factor is canceled by the two nonzero Fourier signs. Thus the positive-frequency weight `|b_hat(n/N)|^2` gives exactly the claimed square-difference correction, with the zero-frequency term and subtraction of `N` unchanged. The same absolutely convergent difference estimate applies to the entire Abel weight. The modified traces are defined sums of retained histories; no unitary spectrum with those traces is asserted.

## 6. The actual shrinking gap and divisor range

The already independently proved escape theorem supplies constants `C_0,C_1`, with `C_1>=1` after enlargement, and squared escape at least `exp[-2C_1r log(r+1)]` when `log N>=C_0r^3` and `d>=N^(1/r)`.

Write

$$
L=\log N,\quad\ell=\log L,\quad\ell_2=\log\ell,
\quad c=(16C_1)^{-1},\quad
r_N=\left\lfloor c\ell/\ell_2\right\rfloor.
$$

For sufficiently large `N`, the floor gives `r_N>=c ell/(2ell_2)`, and `log(r_N+1)<=2ell_2`. Therefore

$$
r_N\log(r_N+1)\le2c\ell,
\qquad C_0r_N^3\le L.
$$

The second assertion follows from polynomial growth in `ell` compared to `L=e^ell`. With `D=2/c=32C_1`, the exact source condition

$$
\log d\ge D\frac{L\ell_2}{\ell}
\tag{6.1}
$$

implies `log d>=L/r_N`. Its squared escape is consequently at least `L^-1/4`. Since `1-sqrt(1-x)>=x/2`, the compression norm is bounded above by

$$
1-\tfrac12L^{-1/4}\le1-L^{-1/2}
$$

once `L>=16`. Thus the explicit weaker gap

$$
g_N=L^{-1/2}
\tag{6.2}
$$

is genuinely proved for the original kick, independently of the divisor satisfying (6.1).

Substituting (6.1)–(6.2) into the pure-history and mixed-history bounds gives respectively

$$
6W L^{1/2}e^{-c_\lambda D L^{1/2}\ell_2/\ell}
\quad\text{and}\quad
3WC_BN^{-1/4}+12W L^{1/2}e^{-c_B L^{1/2}}.
\tag{6.3}
$$

Both tend to zero; their negative exponents dominate `(1/2)ell`. No constant depends on the chosen divisor within the covered range.

The allowed density satisfies

$$
\delta_N\sim\frac{g_N}{4\log(4/g_N)}
\sim\frac1{2\sqrt{\log N}\log\log N}.
$$

At time proportional to `N`, its permitted number of changes tends to infinity, while its fraction tends to zero. The source correctly does not claim a fixed positive fraction in this range.

The divisor range is nonempty and genuinely subpolynomial. For `N_k=7^(2k)` and `d_k=7^ceil(A k loglog k/log k)`, the divisibility holds for all sufficiently large `k`. If `A>2D`, the logarithms give (6.1), because `loglog N_k~log k` and `logloglog N_k~loglog k`. Moreover `log d_k/log N_k` tends to zero. The isolated scalar dimension `N=7` is irrelevant to this large-dimensional sequence.

## 7. The late tail and the obstruction to a wider all-time claim

For any proved gap `g_N=N^(-o(1))`, summing only the bound `|s_n|/N<=eta_N^n` beyond `floor(N^a)` gives

$$
\frac{12W}{g_N}\exp[-g_NN^a/4].
\tag{7.1}
$$

The floor is handled in the favorable direction by `floor(N^a)+1>N^a`. This bound tends to zero because `g_NN^a=N^(a-o(1))`, whereas `log(1/g_N)=o(log N)`. The pure-history tail has the asserted bound `3W g_N^-1 exp(-g_NN^a)` by the same calculation.

The two lower bounds for the complete majorants are also correct. If `g_N->0` and `g_N log d_N->0`, the pure majorant contains the entire tail

$$
\frac{\rho_N^{\lfloor2\log d_N/\log\lambda\rfloor+1}}{g_N}
\sim\frac1{g_N}.
\tag{7.2}
$$

Indeed the exponent times `log rho_N=-g_N+O(g_N^2)` tends to zero. For the mixed minimum, set

$$
J_N=\left\lceil\frac{\log(\sqrt N/C_*)}{\log(B/\eta_N)}\right\rceil.
$$

For large `N`, `J_N>=1` and `J_N=O(log N)`. For every `n>=J_N`, the minimum equals `eta_N^n`. If `g_N log N->0`, then `eta_N^(J_N)->1` and `1-eta_N~g_N/4`, proving the lower tail asymptotic `4/g_N` in source (7.4).

Thus these majorants cannot prove an all-time vanishing correction in the larger range where the inserted gap satisfies `g_N log N->0`. This is an obstruction to those bounds, not a lower bound for the actual signed discrepancy. The source makes exactly that distinction.

There is also no missing factor `1/N` available to remove the early interval: after `|p_n|<=N`, the leading normalized cross-term is controlled by `|s_n|/N`.

## 8. Boundary of the positive result

The new summation proves a genuine all-time signed removal for the stated subpolynomial divisor range and an explicit growing number of deviations. Its analytic constants are uniform in the shrinking gap. Its broader-range statement is only a late-time removal, accompanied by explicit lower bounds demonstrating the failure of the complete geometric majorants there.

The retained coherent histories have not been compared with CUE. The first fixed-test pair discrepancy and every higher fixed factorial order needed for `H_diag` remain unproved. No estimate in this audit fills that original missing step.
