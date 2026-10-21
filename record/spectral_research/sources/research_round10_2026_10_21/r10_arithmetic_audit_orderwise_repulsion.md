> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round10_2026_10_21/r10_arithmetic_audit_orderwise_repulsion.md`. Embedded SHA256: `9865af8e544636611c09a8490f3b37380d36c085fb3380f9260d6bc226462fca`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/closure.md).

# Independent audit: same-order repulsion and spectral matching

21 October 2026. Auditor: `/root/r10_arithmetic`.

## 0. Frozen object and verdict

Audited source: `research_round10_2026_10_21/r10_weyl_orderwise_repulsion_stability.md`.

Final audited SHA-256:

`63ddeba5e72b200bf3dd16bed795423d4ed7e070a0b0e3f55fa30b93d3bc53d2`.

The full initial version with SHA-256 `a3b229e79c3be353da491c06433351f1d42ad9aef8222c37a279afb2c1fc11b7` was read, and the full revised version was reread. The reported revision sharpens the stated Fourier-support enclosure of the explicit test from `[-16,16]` to `[-1/4,1/4]` and repairs two TeX escapes. The initial larger enclosure was still true, but loose. No mathematical hypothesis or inference changed in that revision.

**Verdict: passed for the theorem in Sections 0–6.** If two deterministic spectral sequences admit one matching with uniformly bounded unfolded displacement and total angular displacement tending to zero, then their complete single-order criteria `H_k` are equivalent, for each fixed `k>=2`. The proof needs all the admissible tests at that order, including arbitrarily large fixed Fourier bands. It needs no moment of order greater than `k`.

This verdict does not establish `H_2` for the original matrices or produce an original countersequence. The application to Round 9 uses its previously proved matching, whose exact source passage is checked below. The quantum-ergodicity proof underlying that matching is not reconstructed anew in this audit.

## 1. Exact finite CUE comparison and periodic copies

For each frequency index `r`, define

$$
f_r(x)=N^{-1/2}e^{2\pi i r x/N}.
$$

Then the finite comparison matrix is the Gram matrix

$$
T_{rs}=\int b(x)\overline{f_r(x)}f_s(x)\,dx.
$$

For a frequency set `E` of cardinality `k`, expanding both determinants gives

$$
\det T_{E,E}
=\frac1{k!}\int_{\mathbb R^k}\prod_{a=1}^k b(x_a)
\left|\det[f_r(x_a)]_{r\in E,\,1\le a\le k}\right|^2 dx.
\tag{1.1}
$$

Every one of the `k!` relabelings of the integration variables gives the same integral. There is no unproved limiting argument: this is a finite determinant expansion, with absolute convergence from `b in L^1`. Summing (1.1) over `E` and applying finite Cauchy–Binet gives the source's formula (1.3). Centering the frequency set multiplies row and column `a` by inverse unit phases, so the determinant is unchanged.

**Copy issue.** The integral over all of `R^k` in (1.1) is a formula for the distinct-original-label statistic from the question. It is not asserted to be the full factorial correlation measure of the infinitely periodized point process, which also has singular contributions when copies of one original label are selected at distances that are integer multiples of `N`. The finite Gram identity is valid for the requested statistic independently of that distinction. In particular, at inputs differing by a period, the corresponding Gram vectors are proportional and their determinant vanishes.

When the proof later bounds a count in one interval `J` of fixed length `delta`, it first restricts to dimensions `N>delta`. One original label then has at most one lifted copy in `J`. Therefore the ordered falling factorial `(Xi_N(J))_k` really is a sum over distinct original labels. This is the exact point at which the copy issue is resolved; no global identification of the two factorial measures is used.

The finite check accompanying this audit uses exact Gaussian rational arithmetic, dimensions `3,5,7`, and test measures with points separated by one full period. It verifies eleven Gram identities and six duplicate-period zero determinants. These checks confirm the normalizations but do not replace (1.1).

## 2. Global Vandermonde estimate

Let `nu` be any probability measure on `[-1/2,1/2]`, and work in `L^2(nu)` with

$$
v(x)(\xi)=e^{2\pi i\xi x}.
$$

The derivative bound is exactly

$$
\|v^{(r)}(x)\|^2
=\int |2\pi\xi|^{2r}d\nu(\xi)\le\pi^{2r}.
\tag{2.1}
$$

For distinct real nodes, the divided difference of order `j-1` is the integral of `v^(j-1)` over the simplex of barycentric coefficients. The simplex has volume `1/(j-1)!`, so its norm is at most `pi^(j-1)/(j-1)!`. This vector-valued identity follows either by iterated integration of the fundamental theorem of calculus or by the exponential power-series calculation provided in the source; that calculation was checked, including its beta-integral normalization.

The Newton interpolation coefficient matrix has determinant `prod_(a<b)(x_b-x_a)`. Transforming the Gram matrix by it and applying the Gram determinant inequality gives

$$
0\le\det[K_\nu(x_a,x_b)]
\le
\frac{\pi^{k(k-1)}}{\prod_{r=0}^{k-1}(r!)^2}
\prod_{a<b}|x_a-x_b|^2.
\tag{2.2}
$$

This bound is global in the real nodes and uniform over `nu`, hence over `N`. It does not require the nodes to lie in a small common interval. At repeated nodes it follows by continuity, with both sides zero. No extra `k!` is missing: the factorial factors in (2.2) are already the volumes of the divided-difference simplices.

For a Schwartz test, its integral against the polynomial on the right is finite, so the subsequent integration on the whole real space is legitimate.

## 3. The positive admissible test and exact order of quantifiers

With the source's nonnegative bump `phi` supported in `[-1,1]`, let `I=int phi>0`, `g=F^(-1)phi`, and

$$
\beta(x)=\frac{|g(x/8)|^2}{2I^2}.
$$

Then `beta` is nonnegative Schwartz and has supremum at most `1/2`. Since `widehat{|g|^2}` is supported in `[-2,2]`, scaling by `x/8` puts the Fourier support in `[-1/4,1/4]`; it remains smooth. Moreover

$$
|g(t)-I|\le\int\varphi(\xi)|e^{2\pi i\xi t}-1|d\xi
\le2\pi |t|I.
$$

For `|x|<=1/2`, this gives `beta(x)>=1/8`. Thus `beta_delta(x)=beta(x/delta)` is a legal nonnegative test for every fixed `delta>0`, with Fourier support in `[-1/(4delta),1/(4delta)]`.

The finite CUE bound is

$$
M^{\rm CUE}_{k,N}(\beta_\delta)
\le A_{k,\beta}\delta^{k^2}.
\tag{3.1}
$$

The exponent has `k` factors from the change of volume and `k(k-1)` from the squared Vandermonde. For one fixed interval `J` of length `delta` and all large `N>delta`, positivity and the copy argument give

$$
\mathbb E(\Xi_N(J))_k
\le 8^k k! M^U_{k,N}(\beta_\delta).
\tag{3.2}
$$

Stationarity allows the center of `J` to be absorbed into the uniform origin. The limit in (3.2) uses precisely `H_k` for `beta_delta`. It does not use `H_(k+1)` or a test depending on `N`.

## 4. Same-order uniform integrability, independently checked

Partition an interval of length `L` into `M` cells, and write their integer counts as `n_i`, with `n=sum n_i`. For `n>2kM`,

$$
\sum_i(n_i)_k
\ge\sum_i((n_i-k+1)_+)^k
\ge M^{1-k}(n-(k-1)M)^k
\ge M^{1-k}(n/2)^k.
\tag{4.1}
$$

This proves the pointwise tail inequality used in the source. Applying (3.2) at `delta=L/M` to the fixed collection of cells gives

$$
\limsup_N\mathbb E\big[n^k\mathbf1_{n>2kM}\big]
\le C_{k,\beta} L^{k^2}M^{-k(k-1)}.
\tag{4.2}
$$

The factor in `M` is correct: `M^(k-1)` from (4.1), `M` cells, and `M^(-k^2)` from (3.1). It tends to zero for every `k>=2`.

The quantifier order in this step is essential and valid. For each fixed `M`, the single test is fixed before the dimension limit. Taking `M` to infinity after the `limsup_N` proves asymptotic uniform integrability. To obtain ordinary uniform integrability over the full sequence, fix a desired error, choose such an `M`, then discard the finitely many dimensions before the eventual tail bound holds. Each of their counts on the fixed interval is deterministically bounded; increasing the truncation threshold handles those finite exceptions. No rate uniform in `M` is needed.

This argument establishes the `k`th-power tail itself. There is no inference of a higher prelimit moment from integrating (4.2) in `M`. The source explicitly avoids that invalid exchange of quantifiers.

The accompanying exact integer check verifies (4.1)'s resulting inequality for 154,700 choices with `2<=k<=6`, `1<=M<=4`, and cell counts between zero and twelve. It is a normalization check, not an argument for (4.2).

## 5. Coupling and noncompact Schwartz weights

After the one scalar phase centering allowed in the matching, couple both spectra with the same uniform origin. Every lifted point moves by at most `C`. Therefore

$$
\Xi_N^V(J)\le\Xi_N^U(J+[-C,C]).
\tag{5.1}
$$

It follows by domination that the target has the same local-count uniform integrability of order `k`. Stationarity makes the associated `L^k` bound for a unit interval independent of its position.

For a nonnegative Schwartz weight `b`, take `c_j=sup_[j,j+1)b`. The series of `c_j` converges. Minkowski's inequality bounds the `L^k` norm of the weighted count outside finitely many cells by a fixed constant times the tail of that series. This tail goes to zero uniformly in the dimension. On finitely many cells the `k`th power is bounded by a finite sum of uniformly integrable local-count powers. Hölder's inequality gives

$$
\|Z^k-Z_R^k\|_1
\le k(\|Z\|_k+\|Z_R\|_k)^{k-1}\|Z-Z_R\|_k,
\tag{5.2}
$$

so the finite-cell conclusion extends to the full Schwartz weight by uniform `L^1` approximation. In particular, `(Z_N^U+Z_N^V)^k` is uniformly integrable. A moment at order `k+1` has not entered this argument.

No new band-limited majorant for this `b` is needed: the source first proves local-count control and then uses the summable unit-cell envelope. This avoids an implicit invocation of a majorant theorem with unstated constants.

## 6. Transfer of the actual factorial statistic

For the matched periodized arrays, let `D_N` be the sum of absolute differences and `S_N` the sum of both nonnegative arrays. Exact integration over the uniform origin gives

$$
\mathbb ED_N\le\frac1N\sum_j
\|b(\cdot+N\varepsilon_{j,N})-b\|_1
\le\|b'\|_1\sum_j|\varepsilon_{j,N}|\longrightarrow0.
\tag{6.1}
$$

The first relation is an inequality because the absolute value of a periodized sum is at most the sum of the absolute values of its copies. Summing telescoping products over ordered distinct labels gives

$$
|e_k(w^V)-e_k(w^U)|
\le\frac{D_NS_N^{k-1}}{(k-1)!}.
\tag{6.2}
$$

Only nonnegativity is required in (6.2); the periodized entries need not be bounded by one at this stage. Since `D_N<=S_N`, splitting according to `S_N<=R` proves

$$
|M^V_{k,N}(b)-M^U_{k,N}(b)|
\le\frac{R^{k-1}\mathbb ED_N+
\mathbb E[S_N^k\mathbf1_{S_N>R}]}{(k-1)!}\longrightarrow0,
\tag{6.3}
$$

by taking `N` first and then `R`. The source `H_k` gives the required uniform integrability through Sections 3–5, rather than assuming it. Matching is symmetric, so the implication reverses when the other endpoint is assumed to satisfy `H_k`.

## 7. The Round 9 matching passage and remaining scope

I read lines 335–410 of `research_round9_2026_10_21/r9_sector_continuous_symbol_stability.md`. Its explicit slope formula is

$$
\theta_j'(s)=\frac1{2\pi N}\langle\psi_j(s),B_N\psi_j(s)\rangle.
$$

Its preceding input bounds the mean-square deviation of these matrix elements from a fixed scalar by `q_N->0`, uniformly along the path. Integration and Cauchy–Schwarz therefore give

$$
\sum_j|\theta_j(1)-\theta_j(0)-\bar v/(2\pi N)|
\le\frac1{2\pi}\sqrt{q_N}\longrightarrow0.
\tag{7.1}
$$

The uniform generator norm gives bounded individual unfolded displacement, before and after scalar centering. Thus this matching has exactly the hypotheses of the audited theorem. No spectral-statistics hypothesis was inserted in the matching passage. The separate analytic and ergodic derivation of `q_N` remains the frozen Round 9 input, rather than a new claim established by this audit.

The first original weighted pair sum remains unproved. The theorem transfers a whole order across the original matching; it does not produce that order's asymptotic on either endpoint, and does not transfer a single test on the basis of that test alone.

## 8. Provenance and finite checks

The script `r10_arithmetic_exact_checks.py` and its JSON output record all exact finite identities and input hashes. The script initially encountered an unavailable optional symbolic package; it was replaced by a self-contained Gaussian-rational determinant calculation using only Python's standard library. The final successful run makes no floating-point spectral computation and does not replace `tau` by a machine zero.

The frozen Round 10 base is `e338400f1f360b680ea74c739283b296c9c67eb4e598c2067b136f9f29773777`. The audit file does not amend the candidate or the master proof. No unverified original-family theorem is promoted by the verdict above.
