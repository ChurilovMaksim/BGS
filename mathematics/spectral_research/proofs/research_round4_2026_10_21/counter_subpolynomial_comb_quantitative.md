> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_subpolynomial_comb_quantitative.md`. Embedded SHA256: `3b59bd021e393489cd709073e683a2dec137333e0e657849b0636a9f85f90def`.
> [Thematic guide](../../topics/approximation.md).

# Quantitative growing-order exclusion of subpolynomial character combs

Date: 21 October 2026. Research branch: attempted arithmetic countersequence for the exact fixed family.

## 0. Status, target, and exact advance

The original target is still the all-odd-dimensional `H_diag` statement, or a fixed-test infinite countersequence for the same matrices. This note does not establish either conclusion. It investigates a remaining counterexample mechanism: microscopic quasimodes concentrated in character spaces whose square divisors grow subpolynomially.

The fixed-order statement from the preceding continuation does not by itself permit `r=r_N` to grow. Here all constants relevant to that growth are estimated. The resulting statement covers an explicit subpolynomial range and excludes character-comb quasimodes at the spectral spacing scale in that range.

Base checkpoint:

- Spectral_research_2026-10-21.md, SHA-256 `388b7c16c198a67d8a7f06358f1c1b8b0ae6e44724e91d91ef679848909bc394`.
- research_round3_2026_10_21/arithmetic_comb_fixed_order_gap.md, SHA-256 `e43296774f12851d7150e0d501afd1de76fd4feb11161e9f30692f1866cd1bf8`.

The earlier files are not edited. Their finite-word and Zak arguments are reconstructed below with a bound uniform in the order. This manuscript is a new candidate theorem pending independent audit; it must not be marked proved solely because it extends an earlier audited fixed-order result.

## 1. Quantified theorem

Let `tau=10^(-80)` be the exact constant from the question, and let

$$
E_N=e^{i\tau N A_N},\qquad U_N=E_NM_N.
$$

For odd `N=d^2m`, let `P_chi` denote the character projections of the commuting Weyl subgroup

$$
H_d(s,u)=T_N(sN/d,uN/d),\qquad (s,u)\in(\mathbb Z/d\mathbb Z)^2.
$$

**Theorem.** There are finite positive constants `C_0,C_1`, depending only on the explicit symbol and the fixed `tau`, such that for every integer `r>=2`, every odd `N=d^2m` satisfying

$$
\log N\ge C_0r^3,\qquad d\ge N^{1/r},
\tag{1.1}
$$

and every pair of characters `chi,psi`,

$$
\boxed{
\|(I-P_\psi)E_Nv\|
\ge \exp[-C_1r\log(r+1)]
\quad (v\in\operatorname{Ran}P_\chi,\ \|v\|=1).
}
\tag{1.2}
$$

Equivalently,

$$
\|P_\psi E_NP_\chi\|
\le\sqrt{1-\exp[-2C_1r\log(r+1)]}.
\tag{1.3}
$$

The same statement holds with `U_N` in place of `E_N`, since `M_N` permutes the character spaces exactly. The constants are uniform in `r,N,d,m,chi,psi`; in particular, (1.1) permits the stated growing orders. No assertion is made for all subpolynomial divisors.

**Corollary.** There are constants `C_2,C_3,N_0` such that, whenever `N=d^2m>=N_0` is odd and

$$
\log d\ge C_2(\log N)^{2/3},
\tag{1.4}
$$

the escape norm in (1.2), for both `E_N` and `U_N`, is at least

$$
\epsilon_N:=\exp[-C_3(\log N)^{1/3}\log\log N]=N^{-o(1)}.
\tag{1.5}
$$

This is larger than `N^(-a)` for every fixed `a>0` for all sufficiently large `N`.

## 2. The exact symbol and an analytic norm uniform in h

Set

$$
h=(2\pi N)^{-1},\qquad t=\tau/(2\pi),
\qquad Q_N(e^{2\pi i(kq+lp)})=(-1)^{kl}T_N(l,k).
$$

The exact ordinary Weyl symbol of `A_N` is

$$
\begin{aligned}
a(q,p)={}&\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}-\frac1{10}\\
&+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
\end{aligned}
\tag{2.1}
$$

The shift by `1/2` is necessary for the original modular convention. The Fourier support is contained in `|k|+|l|<=9`, the coefficient one-norm is less than two, and `a_(7,0)=9/20`.

For `sigma>=0`, use the analytic Fourier norm

$$
\|b\|_\sigma=\sum_{v=(k,l)\in\mathbb Z^2}
e^{\sigma|v|_1}|\widehat b(v)|.
$$

On the line let `P=-ih partial_q`, `A_h=Q_h(a)`, and `E_h=exp(it A_h/h)`. Define `L_h` by

$$
Q_h(L_hb)=(-i/h)[Q_h(a),Q_h(b)].
$$

The exact pairwise multiplier is `2h^(-1) sin(2pi^2 h omega)` with `omega=lk'-kl'`, and its absolute value is at most `4pi^2 |omega|`. Elementary support induction gives

$$
\|L_h^n a_q\|_0\le120\,7000^n n!,\qquad
\operatorname{supp}\widehat{L_h^n a_q}
\subset\{|v|_1\le9(n+1)\}.
\tag{2.2}
$$

The same bounds hold for `L_0 b={a,b}`, whose multiplier is `4pi^2 omega`.

Consequently the series

$$
v_h=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}L_h^na_q,
\qquad
v_0=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}L_0^na_q
\tag{2.3}
$$

converge in `||.||_1`, uniformly in `h`. Indeed their geometric parameter is `7000t e^9<1/2`. In particular there is an absolute finite `V`, independent of `h` and of every later order `r`, with

$$
\|v_h\|_1+\|v_0\|_1\le Vt.
\tag{2.4}
$$

For example, (2.2) bounds each of the two norms by
`120 e^9 t/(1-7000t e^9)`, so `V=4*10^6` is sufficient.

The first series solves the bounded-operator Heisenberg equation. Integrating its commutator with `P` gives exactly

$$
E_h^*PE_h=P+Q_h(v_h).
\tag{2.5}
$$

The sine remainder is bounded by `(8/3)pi^6 h^2|omega|^3`. Telescoping `L_h^n-L_0^n` and using the support in (2.2) gives an additional factor bounded by `10^6h^2n^3` relative to its majorant. Multiplication by the analytic weight adds only `e^{9(n+1)}`. A convergent geometric series times `n^3` therefore proves

$$
\|v_h-v_0\|_1\le V' h^2t^2
\tag{2.6}
$$

for an absolute finite `V'`. Both functions are real valued.

We retain the explicit coefficient bound

$$
\widehat v_0(7,0)=t\,63\pi i/10+e,
\qquad |e|\le2\cdot10^6t^2,
\qquad |\widehat v_0(7,0)|>t.
\tag{2.7}
$$

This follows by summing (2.2) from `n=1`. All constants in this section precede the choice of the growing order.

## 3. Uniform bounds on long commutator words

Put

$$
H_0=-P,\qquad H_1=-P-Q_h(v_h),\qquad
R(s)=e^{isH_0/h},\quad B(s)=e^{isH_1/h}.
$$

Define `C_0=B` and `C_(j+1)=RC_jR^*C_j^*`. For order `r`, the word `C_(r-1)` has

$$
L_r=3\cdot2^{r-1}-2\le2^{r+1}
\tag{3.1}
$$

factors, including exactly `2^(r-1)` factors of type `B` or `B^*`.

### 3.1. Scaled bracket norms

Let `0<sigma'<sigma`. From the Fourier multiplier and
`sup_(x>=0) x e^{-(sigma-sigma')x}<=1/(sigma-sigma')`,

$$
\|(-i/h)[Q_h(b),Q_h(c)]\|_{\sigma'}
\le4\pi^2(\sigma-\sigma')^{-2}
\|b\|_\sigma\|c\|_\sigma.
\tag{3.2}
$$

Here the notation on the left means the analytic norm of its explicit Fourier symbol. A scaled bracket with `P` is a derivative, costing at most `2pi/(sigma-sigma')`.

Allocate a total loss of analytic weight at most `1/2` over `r+1` steps, each losing `1/(2r+2)`. After the first bracket of `H_0,H_1`, all symbols are bounded and contain at least one factor `v_h`. Applying (3.2) and (2.4) to each subsequent bracket yields

$$
M_r\le C t\,[C(r+1)^2]^r
\le t\exp[C r\log(r+1)],
\tag{3.3}
$$

where `M_r` bounds every iterated scaled bracket of depth `r` needed below in operator norm. Constants `C` may increase by an absolute amount from display to display, but never depend on `r,h,N,d`. Treating the fixed `t` as at most one is sufficient for the upper bound.

### 3.2. Counting the Taylor remainders

Differentiate the finite word and write its left logarithmic generator

$$
\mathcal A_r(s)=(h/i) C_{r-1}'(s)C_{r-1}(s)^*.
$$

Each term is a signed `H_0` or `H_1` conjugated by a prefix of length at most `L_r-1`. Expand the prefix conjugations from right to left, retaining total degree at most `r-1`. The integral Taylor formula for a conjugation uses one additional scaled bracket per degree. Every new remainder has total original bracket depth exactly `r`; outer unexpanded conjugations are unitary and do not increase its norm. Once a remainder has been created, leave it unexpanded.

For a prefix of length at most `L_r`, the number of retained multiindices and possible positions of a first remainder is bounded by `L_r binomial(L_r+r,r)`. There are at most `L_r` differentiated terms. Coefficients from Taylor factorials are at most one in absolute value. Thus

$$
\|\text{total remainder}\|
\le L_r^2\binom{L_r+r}{r}M_r |s|^r.
\tag{3.4}
$$

Since `L_r<=2^(r+1)`, elementary factorial or product bounds give

$$
L_r^2\binom{L_r+r}{r}\le\exp(Cr^2).
\tag{3.5}
$$

The finite Lie polynomial has first nonzero degree `r-1` in the generator. This follows by induction from the group commutator identity: if `C_(j-1)=I+s^j ad_X^(j-1)Y+O(s^(j+1))` formally, then `[exp(sX),C_(j-1)]` has leading term `s^(j+1)ad_X^jY`, with `X=iH_0/h`, `Y=iH_1/h`. The base `j=1` is immediate. This identifies the coefficients of the already justified Taylor polynomial, and does not assert operator-norm analyticity of an unbounded exponential.

Consequently, with

$$
K_{r,h}=(i/h)^{r-1}\operatorname{ad}_{H_0}^{r-1}H_1
=(-1)^rQ_h(\partial_q^{r-1}v_h),
$$

we have the quantitative bound

$$
\mathcal A_r(s)=rs^{r-1}K_{r,h}+\mathcal R_r(s),
\qquad
\|\mathcal R_r(s)\|\le t e^{Cr^2}|s|^r,
\quad |s|\le1.
\tag{3.6}
$$

The common unbounded linear terms cancel. Domain manipulations are first on the invariant Schwartz core; all differences after the first bracket are bounded, so the remainder estimates extend to the full line space.

Unitary Duhamel comparison with `exp(i s^r K_(r,h)/h)` proves

$$
\boxed{
\|C_{r-1}(\delta)-e^{i\delta^rK_{r,h}/h}\|
\le t e^{Cr^2}\delta^{r+1}/h,
\qquad 0\le\delta\le1.
}
\tag{3.7}
$$

This is the point at which the earlier fixed-order proof acquires a uniform order budget. The bound is exponential in `r^2`, not an unnamed order-dependent constant.

## 4. Quantitative phase bounds and a lower bound for every mu_r

For `beta in [2^(-r),1]`, define the real, mean-zero function

$$
G_{r,\beta}=2\pi\beta(-1)^r\partial_q^{r-1}v_0.
\tag{4.1}
$$

For each fixed nonnegative integer `s`, the analytic norm bound and
`x^j<=j!e^x` imply

$$
\|G_{r,\beta}\|_{C^s}
\le C_s t (2\pi)^{r+s}(r+s)!V
\le\exp[C_s r\log(r+1)].
\tag{4.2}
$$

These bounds are uniform in `beta` and valid for all `r>=2`. The fixed, very small `t` causes no difficulty in upper bounds.

For the lower bound, (2.7) implies

$$
|\widehat G_{r,\beta}(7,0)|
\ge 2\pi 2^{-r}(14\pi)^{r-1}t
=\frac t7(7\pi)^r>t.
\tag{4.3}
$$

In particular `max|G|>t`. Since `G` has mean zero and the torus is connected, its range includes zero and either `t` or `-t`. Choose a point `z_0` at one of these latter levels. Let

$$
\Lambda_r=1+\sup_{\beta}\|\nabla G_{r,\beta}\|_\infty,
\qquad a_r=t/(4\Lambda_r).
$$

Here the gradient norm is the Euclidean norm; increasing the constant in (4.2) absorbs the two components. The torus ball of radius `a_r<1/8` about `z_0` has area `pi a_r^2`. Throughout it,

$$
3t/4\le |G|\le5t/4<1.
$$

For `|x|<=1`, `|e^{ix}-1|>=|x|/2`. Therefore

$$
\int_{\mathbb T^2}|e^{iG_{r,\beta}}-1|^2
\ge\frac{9\pi}{1024}\frac{t^4}{\Lambda_r^2}.
\tag{4.4}
$$

The same lower bound holds for every `beta`. Combining (4.2) and (4.4), and absorbing the fixed positive factor `t^4`, gives

$$
\boxed{
\mu_r:=\min_{\beta\in[2^{-r},1]}
\int|e^{iG_{r,\beta}}-1|^2
\ge\exp[-C r\log(r+1)].
}
\tag{4.5}
$$

This estimate does not use uniform stationary phase as `r` grows. It remains valid even when the phase is large and highly oscillatory, because a small specified phase level is selected before taking the Lipschitz ball.

For later use, the chain and product rules applied to the real phase give, for every fixed `s`,

$$
\sup_{0\le u\le1}\|e^{iuG_{r,\beta}}\|_{C^s}
+\||e^{iG_{r,\beta}}-1|^2\|_{C^s}
\le\exp[C_s r\log(r+1)].
\tag{4.6}
$$

Only finitely many derivatives, for example at most eight, are needed below. No analytic norm of the exponential is used; such a norm could have a much worse dependence on the large phase.

## 5. Finite torus descent and uniform symbol errors

Choose

$$
b=\lfloor dN^{-1/r}\rfloor\ge1,\qquad
\delta=b/d,
\qquad\beta_N=N\delta^r\in[2^{-r},1].
\tag{5.1}
$$

Then `delta<=N^(-1/r)` and `Ndelta=bdm` is an integer.

The exact Weyl operators on the line and every endpoint word in (3.7) decompose into finite torus fibers under

$$
(Zf)(\alpha,\zeta)_j
=N^{-1/2}\sum_{n\in\mathbb Z}e^{-2\pi in\alpha}
f((j+\zeta)/N+n),\qquad0\le j<N.
\tag{5.2}
$$

Parseval and the partition of the real line prove unitarity of this direct-integral decomposition. The zero fiber of a mode is exactly `(-1)^(kl)T_N(l,k)`. Since `Ndelta` is integral, `R(delta)` also preserves fibers. The fiber matrices are continuous in their parameters, so an operator-norm estimate on the line holds in every fiber, not only almost everywhere. Applying this to the finite endpoint word transfers (3.7) to the original matrices.

From (2.6) and the analytic derivative bound,

$$
\|2\pi\beta_N\partial_q^{r-1}(v_h-v_0)\|_0
\le h^2\exp[C r\log(r+1)].
\tag{5.3}
$$

Both quantized generators are Hermitian. Their exponentials differ in norm by at most the generator difference, by a unitary Duhamel integral.

The exact integer-frequency Weyl multiplication formula implies

$$
\|Q_N(F)Q_N(G)-Q_N(FG)\|
\le\frac C N
\Big(\sum_v(1+|v|_1)|\widehat F(v)|\Big)
\Big(\sum_v(1+|v|_1)|\widehat G(v)|\Big).
\tag{5.4}
$$

Indeed its phase differs from one by at most `pi|omega|/N`; triangle inequality then suffices. The formula is valid for all integer frequencies before reduction modulo `N`, so aliasing does not invalidate the bound. In dimension two, each weighted coefficient sum in (5.4) is bounded by a constant times the `C^4` norm, using two applications of `1-Delta` and the convergent sum `sum_v(1+|v|)(1+|v|^2)^(-2)`.

Differentiate `Q_N(e^{iuG})` and compare with `exp(iu Q_N(G))` by Duhamel. Equations (4.2), (4.6), and (5.4) give

$$
\|e^{iQ_N(G_{r,\beta})}-Q_N(e^{iG_{r,\beta}})\|
\le N^{-1}\exp[C r\log(r+1)].
\tag{5.5}
$$

Since `Ndelta^r<=1`, (3.7), (5.3), and (5.5) together prove

$$
\boxed{
\|C_{r-1}(\delta)-Q_N(e^{iG_{r,\beta_N}})\|
\le e^{Cr^2}N^{-1/r}.
}
\tag{5.6}
$$

Finally character orthogonality gives, for any smooth periodic `F`,

$$
\|P_\chi Q_N(F)P_\chi-(\int F)P_\chi\|
\le\sum_{|v|_1\ge d}|\widehat F(v)|
\le C d^{-1}\|F\|_{C^4}.
\tag{5.7}
$$

To see the first bound, every frequency with either coordinate not divisible by `d` is killed by compression; all surviving nonzero frequencies have `|v|_1>=d`. The estimate includes frequencies that alias to zero modulo `N`. For the second bound, use the same Fourier decay as in (5.4).

Set `F=e^{iG}-1`. The product estimate (5.4), (4.6), and (5.7) show that every unit vector in a character space satisfies

$$
\left|\|Q_N(F)v\|^2-\int|F|^2\right|
\le e^{C r\log(r+1)}(d^{-1}+N^{-1}).
\tag{5.8}
$$

## 6. Completion with a growing order

All constants in (4.5), (5.6), (5.8) are independent of the order. Since `d>=N^(1/r)`, their error terms are bounded by `e^(C r^2)N^(-1/r)`. If

$$
\log N\ge C_0 r^3
$$

with a sufficiently large fixed `C_0`, this is at most a fixed small fraction of both the lower bound (4.5) and its square root. This follows by taking logarithms:

$$
Cr^2-(\log N)/r\le-(C_0-C)r^2,
$$

whereas `r log(r+1)<=r^2` for `r>=2`. Enlarging `C_0` also handles the finitely many smallest orders and all fixed constants.

It follows from (4.5), (5.6), and (5.8) that

$$
\|(C_{r-1}(\delta)-I)v\|
\ge\frac12\exp[-C r\log(r+1)]
\tag{6.1}
$$

for every input character and every unit vector in it.

Let `epsilon=||(I-P_psi)E_Nv||`. At the chosen endpoint, `R=T_N(-bN/d,0)` acts on the input character as a scalar `r_chi` and on the desired output character as a scalar `r_psi`. Hence

$$
(R/r_\chi)v=v,\qquad
\|(E_N^*RE_N/r_\psi-I)v\|\le2\epsilon.
$$

Scalar normalization does not change the group commutator word. Telescoping its `2^(r-1)` occurrences of `B` or its inverse gives

$$
\|(C_{r-1}-I)v\|\le2^r\epsilon.
\tag{6.2}
$$

Combining (6.1) and (6.2), and absorbing `2^(r+1)` into `exp(C_1 r log(r+1))`, proves (1.2). No phase equality between `chi` and `psi` is assumed.

For the subpolynomial corollary let

$$
r=\left\lfloor ((\log N)/C_0)^{1/3}\right\rfloor.
$$

For sufficiently large `N`, `r>=2` and
`r>=((log N)/C_0)^(1/3)/2`. Thus (1.4), for a sufficiently large fixed `C_2`, implies `d>=N^(1/r)`. Substitution in (1.2) gives (1.5).

The exact covariance

$$
T_N(a,b)M_N=M_NT_N(3a-4b,-2a+3b)
$$

permutes the characters. Applying the same result to the input `M_Nv` proves the claim for `U_N`.

## 7. What is ruled out, and what remains open

For every unit `v` in one of the covered character spaces and every `|lambda|=1`,

$$
\|(U_N-\lambda)v\|
\ge\|(I-P_\chi)U_Nv\|
\ge\epsilon_N.
\tag{7.1}
$$

Since `epsilon_N=N^(-o(1))`, there can be no such character-comb quasimodes with residual `o(1/N)` in the subpolynomial range (1.4). This also excludes a spectral microcluster construction whose entire proposed quasimode space is contained in one such character space.

The exclusion has a robust version. For an arbitrary unit vector `v`, let `a=||P_chi v||`, `b=||(I-P_chi)v||`. Apply the leakage theorem to the normalized vector `P_chi v/a` when `a>0`. The outside projection of `(U_N-lambda)v` equals `(I-P_chi)U_NP_chi v+(I-P_chi)(U_N-lambda)(I-P_chi)v`; the last term is bounded by `2b`. Therefore

$$
\boxed{\|(U_N-\lambda)v\|\ge\epsilon_N a-2b.}
\tag{7.2}
$$

Thus microscopic quasimodes cannot have distance `o(epsilon_N)` from one of these character spaces. The factor two explicitly retains the `-lambda(I-P_chi)v` term.

This does not exclude spectral clusters with delocalized eigenvectors, superpositions over many characters, or character spaces with `log d` below the range (1.4). The earlier all-time signed trace removal does not automatically extend with its former constants: the present escape constant shrinks with `N`, and the sum of its geometric majorant may grow. No conclusion about that trace sum is inserted.

The first original-family pair discrepancy remains

$$
\frac1{N^2}\sum_{1\le n<2N}|\widehat b_*(n/N)|^2
\bigl(|\operatorname{Tr}U_N^n|^2-\min(n,N)\bigr),
$$

whose limit is not evaluated here. No fixed-test infinite discrepancy sequence is produced.

The demonstrated change at the previous bottleneck is quantitative control of the growing order and of `mu_r`; this must be independently audited before promotion to the program's proved results.
