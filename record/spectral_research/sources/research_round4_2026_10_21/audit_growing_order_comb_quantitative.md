> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_growing_order_comb_quantitative.md`. Embedded SHA256: `30a2039b988d49f12960ffb1d27fc72dedc6eefcb38d005d75ebee06c5de17cb`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/arithmetic.md).

# Independent audit: growing-order exclusion of character combs

Date: 21 October 2026.

## 0. Verdict, scope, and frozen input

**Primary verdict: proved as written, for the theorem in §§1–6 and the robust quasimode consequence in §7 of the frozen manuscript below.** The audit finds no unresolved estimate in that stated result. This verdict does not prove `H_diag`, does not produce a fixed-test countersequence, and does not extend the earlier all-time trace estimate to an order depending on `N`.

The audited primary source is:

- `research_round4_2026_10_21/counter_subpolynomial_comb_quantitative.md`;
- SHA-256: `3b59bd021e393489cd709073e683a2dec137333e0e657849b0636a9f85f90def`.

That source was read in full and its hash was checked on disk. Its pending-audit label is part of the frozen source and has not been edited.

The fixed-order analytic and finite-dimensional conventions were independently reconstructed in the separate audit:

- `research_round4_2026_10_21/audit_uniform_word_foundation.md`;
- SHA-256: `3b9f422c7ba02c7b01da409eac17f2e1e06f4da30c4cceb0ba4f9867d21cb961`.

The present verdict is not inferred from that earlier verdict. In particular, a constant allowed to depend arbitrarily on a fixed order would be insufficient here. The proof below checks the new dependence on the order, including every source of derivative, word-length, phase, and finite-torus error. The old audit is unchanged.

No numerical spectral experiment, formal proof assistant, external universality theorem, or unpublished operator theorem is used as a premise. The estimates are obtained from explicit Fourier multiplication, integral Taylor formulas, and unitary Duhamel formulas.

## 1. Exact statement being audited

Write `E_N=exp(i tau N A_N)`, with the exact fixed `tau=10^(-80)`. For odd `N=d^2m`, let `P_chi` be the character projections of

$$
H_d(s,u)=T_N(sN/d,uN/d),\qquad (s,u)\in(\mathbb Z/d\mathbb Z)^2.
$$

The statement is that constants `C_0,C_1>0`, independent of `r,N,d,m,chi,psi`, exist such that

$$
r\ge2,\quad \log N\ge C_0r^3,\quad d\ge N^{1/r}
\quad\Longrightarrow\quad
\|(I-P_\psi)E_Nv\|\ge e^{-C_1r\log(r+1)}
\tag{1.1}
$$

for every pair of characters and every unit `v` in the input character space. The same statement holds for `U_N=E_NM_N`.

The claimed corollary covers

$$
\log d\ge C_2(\log N)^{2/3}
$$

and gives escape at least

$$
\epsilon_N=\exp[-C_3(\log N)^{1/3}\log\log N]=N^{-o(1)}.
\tag{1.2}
$$

All logarithms may be taken natural; changing the base only changes fixed constants. Because `d<=sqrt(N)`, some small dimensions or large constants yield an empty range. The large-`N` range is nonempty, for example along sufficiently large odd squares.

## 2. Exact Weyl convention and the analytic input

Set

$$
h=(2\pi N)^{-1},\qquad t=\tau/(2\pi).
$$

For integer modes on the line,

$$
(W_h(k,l)u)(q)=e^{2\pi ik(q+l/(2N))}u(q+l/N).
$$

At the zero finite-torus fiber,

$$
W_N(k,l)=(-1)^{kl}T_N(l,k).
\tag{2.1}
$$

Indeed the modular inverse of `2` is represented by `(N+1)/2`, whereas the line mode uses the real half; their ratio is `exp(pi i kl)=(-1)^(kl)`. This sign is necessary also for integer labels that later alias modulo `N`.

The ordinary real-half symbol of `A_N` therefore is

$$
\begin{aligned}
a(q,p)={}&\cos14\pi q+\frac{r(q)}{10}
 +\frac{r(q)\sin2\pi q}{100}-\frac1{10}\\
&+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
\end{aligned}
\tag{2.2}
$$

Multiplication of the original coefficients with `l=±1` by `(-1)^k` explains the `q+1/2` shift. Direct expansion gives support in `|k|+|l|<=9`, coefficient one-norm less than `2`, and `a_hat(7,0)=9/20`.

For `omega=lk'-kl'`, the exact product multiplier is

$$
W_h(k,l)W_h(k',l')
=e^{2\pi^2ih\omega}W_h(k+k',l+l').
$$

Consequently the scaled commutator `(-i/h)[Q_h(a),Q_h(b)]` has pairwise multiplier

$$
\frac2h\sin(2\pi^2h\omega),
$$

whose absolute value is at most `4pi^2|omega|`. The positive classical multiplier is `4pi^2 omega` with this convention.

Let `L_h` denote this explicit Fourier operation, and let `L_0` denote its classical limit. A bracket against `a`, acting on a symbol of support radius at most `9j`, increases that radius to at most `9(j+1)` and costs at most

$$
2\cdot4\pi^2\cdot9\cdot9j<7000j
$$

in coefficient one-norm. Also `||a_q||_0<120`. Thus, independently of `h`,

$$
\|L_h^na_q\|_0\le120\,7000^n n!,\qquad
\operatorname{supp}\widehat{L_h^na_q}
\subset\{|ν|_1\le9(n+1)\}.
\tag{2.3}
$$

The same proof applies to `L_0`.

For the analytic coefficient norm

$$
\|b\|_\sigma=\sum_ν e^{\sigma|ν|_1}|\widehat b(ν)|,
$$

the two exact series

$$
v_h=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}L_h^na_q,
\qquad
v_0=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}L_0^na_q
$$

satisfy

$$
\|v_h\|_1+\|v_0\|_1\le Vt,
\qquad V=4\cdot10^6.
\tag{2.4}
$$

Each series is bounded by `120e^9t/(1-7000te^9)`. The fixed parameter obeys `7000te^9<1/2`, and `480e^9<4*10^6`. There is no dependence on the future order in this analytic norm.

The series for `v_h` also has the asserted operator meaning. For each fixed `h`, it solves the bounded-operator Heisenberg equation and hence agrees, by uniqueness, with the conjugated bounded derivative observable. The identity

$$
E_h^*PE_h=P+Q_h(v_h),\qquad
P=-ih\partial_q,\quad E_h=e^{itQ_h(a)/h},
\tag{2.5}
$$

then follows by integrating the commutator with `P`. There is no norm Taylor expansion of the unbounded `P`. The common domain is justified because `[P,Q_h(a)]` is bounded, so the bounded exponential `E_h` preserves `Dom(P)`. One can obtain this directly by its graph-norm series. Constants used solely to establish domain preservation need not be uniform in `h`; they do not enter any remainder bound below. Finite Weyl translations and smooth multipliers preserve the Schwartz core, and the same exponential series does so in every Schwartz seminorm for each fixed `h`.

### 2.1. The `h^2` symbol error is uniform before choosing the order

The elementary sine remainder gives

$$
\left|\frac2h\sin(2\pi^2h\omega)-4\pi^2\omega\right|
\le\frac83\pi^6h^2|\omega|^3.
\tag{2.6}
$$

At the `j`th bracket, the input support radius is at most `9j`, so `|omega|<=81j`. Including the coefficient one-norm of `a`, the exceptional multiplier is bounded by the usual `7000j` majorant times `10^6h^2j^2`. In

$$
L_h^n-L_0^n
=\sum_{j=0}^{n-1}L_h^{n-1-j}(L_h-L_0)L_0^j
$$

all other factors obey the same support induction. Summing the exceptional positions costs at most `10^6h^2n^3`. The factor `e^{9(n+1)}` supplies the weight at `sigma=1`. A geometric series with polynomial `n^3` factor converges and starts at `n=1`, yielding

$$
\|v_h-v_0\|_1\le V'h^2t^2
\tag{2.7}
$$

for a finite absolute constant `V'`. This constant is independent of `r`.

Likewise, retaining the `n=0` coefficient at `(7,0)` and summing the unweighted tail gives

$$
\widehat v_0(7,0)=t\frac{63\pi i}{10}+e,
\qquad |e|\le2\cdot10^6t^2,
\qquad |\widehat v_0(7,0)|>t.
\tag{2.8}
$$

Reality follows from preservation of the conjugate symmetry of Fourier coefficients by each commutator operation.

## 3. New order-uniform commutator budget

Put `H_0=-P`, `H_1=-P-Q_h(v_h)`. After the first nonzero bracket between two original generators, the result is a bounded symbol with at least one factor `v_h` or a derivative of it. This observation is essential: bounding the original generators in norm is not permitted.

If `0<=sigma'<sigma`, Fourier multiplication and `sup(xe^(-ax))<=1/a` imply

$$
\|\mathcal L_h(b,c)\|_{\sigma'}
\le4\pi^2(\sigma-\sigma')^{-2}
\|b\|_\sigma\|c\|_\sigma,
\tag{3.1}
$$

where `Q_h(mathcal L_h(b,c))=(-i/h)[Q_h(b),Q_h(c)]`. A scaled bracket with `P` is a derivative and costs at most `2pi/(sigma-sigma')`.

For the depth-`r` expressions use losses

$$
\Delta=\frac1{2r+2}
$$

at each step. At most `r+1` losses are required, so the final analytic radius remains at least `1/2`. Every occurrence of `v_h` is bounded by the same `Vt` from (2.4). After the first bracket, each further bracket with `H_0` or `H_1` costs at most `C(r+1)^2`; the split of `H_1` into `P` and `Q(v_h)` is included in this constant. Thus every needed original iterated scaled bracket has operator norm bounded by

$$
M_r\le Ct\,[C(r+1)^2]^r
\le t e^{C r\log(r+1)}.
\tag{3.2}
$$

The constants here are independent of `r` and `h`. This is a genuine improvement over an unspecified fixed-order estimate. In particular, raising a derivative-dependent constant `V_r` to the `r`th power would not supply the stated budget; the fixed initial analytic radius and the explicit allocation of its loss avoid that problem.

## 4. Finite-word counting and its exact bounded remainder

Let

$$
R(s)=e^{isH_0/h},\quad B(s)=e^{isH_1/h},\quad
C_0=B,\quad C_{j+1}=RC_jR^*C_j^*.
$$

The order-`r` word `C_(r-1)` has

$$
L_r=3\cdot2^{r-1}-2\le2^{r+1}
$$

factors and exactly `2^(r-1)` factors of `B` or `B^*`.

Differentiate the finite word. Its left logarithmic generator is a sum of signed `H_0,H_1`, each conjugated by its preceding prefix. Apply the integral Taylor formula to prefix conjugations from right to left, retaining total polynomial degree at most `r-1`. If a term already has total bracket depth `j`, its next expansion is stopped after degree `r-1-j`; its new integral remainder contains exactly `r` original scaled brackets. Subsequent outer conjugations are left unexpanded on that remainder. Their unitarity preserves its norm.

This procedure never asks for a bracket of a previously integrated remainder, and never replaces an original bracket by a bracket with a large conjugated generator. It therefore uses exactly the bound in (3.2), even when `s/h` is large.

A retained multiindex has nonnegative entries and total at most `r-1`; counting these entries and the position where its first remainder is formed gives the source's safe upper bound

$$
L_r^2\binom{L_r+r}{r}
\tag{4.1}
$$

for all remainder slots in the differentiated word. The Taylor denominators and integral denominators are at most one, so omitting them only enlarges the estimate. For `r>=2`,

$$
L_r+r\le2^{r+2},\qquad
L_r^2\binom{L_r+r}{r}
\le2^{2r+2}(L_r+r)^r
\le2^{r^2+4r+2}
\le e^{Cr^2}.
\tag{4.2}
$$

For comparison, an exact count from the same right-to-left construction can be bounded by `binomial(L_r+r-1,r+1)`; this sharper count is unnecessary. The larger count in the source already has the required order of growth.

Formal free-algebra multiplication is used only to identify the finite polynomial whose bounded remainders have just been controlled. If `X=iH_0/h`, `Y=iH_1/h`, induction in the group commutator gives first nonzero word term `s^r ad_X^(r-1)Y`. Hence the first nonzero term of the left logarithmic generator is

$$
rs^{r-1}K_{r,h},\qquad
K_{r,h}=(i/h)^{r-1}\operatorname{ad}_{H_0}^{r-1}H_1
=(-1)^rQ_h(\partial_q^{r-1}v_h).
\tag{4.3}
$$

For example, its signs at `r=2,3,4` are respectively `+v_q,-v_qq,+v_qqq`, agreeing with the original generator convention. All unbounded degree-zero terms cancel; every higher term is a bounded original bracket. Multiplying (3.2) and (4.2), and using `r log(r+1)<=r^2`, proves

$$
(h/i)C_{r-1}'(s)C_{r-1}(s)^*
=rs^{r-1}K_{r,h}+\mathcal R_r(s),
\qquad
\|\mathcal R_r(s)\|\le t e^{Cr^2}|s|^r.
\tag{4.4}
$$

These identities initially hold on the common invariant core. After cancellation, boundedness extends them to the whole Hilbert space. Duhamel comparison with `exp(is^rK_(r,h)/h)` is between unitary propagators, so

$$
\|C_{r-1}(\delta)-e^{i\delta^rK_{r,h}/h}\|
\le \frac{t e^{Cr^2}}h\int_0^\delta s^r\,ds
\le t e^{Cr^2}\frac{\delta^{r+1}}h.
\tag{4.5}
$$

There is no factor `exp(C/h)`, and no assumption `delta=O(h)`.

## 5. A quantitative lower bound for every phase integral

For `beta in [2^(-r),1]`, define

$$
G_{r,\beta}=2\pi\beta(-1)^r\partial_q^{r-1}v_0.
$$

For every fixed integer `s>=0`, the analytic norm and `x^j<=j!e^x` yield

$$
\|G_{r,\beta}\|_{C^s}
\le C_s Vt(2\pi)^{r+s}(r+s)!
\le e^{C_s r\log(r+1)}.
\tag{5.1}
$$

The constants can depend on the fixed derivative index `s`, but not on `r` or `beta`. Only a fixed finite number of such indices is used later.

The phase has mean zero because it is a positive-order `q` derivative. Its `(7,0)` Fourier coefficient obeys, by (2.8),

$$
|\widehat G_{r,\beta}(7,0)|
\ge2\pi\,2^{-r}(14\pi)^{r-1}t
=\frac t7(7\pi)^r>t.
\tag{5.2}
$$

Thus `max|G|>t`. Reality, mean zero, and connectedness of the torus imply that its image contains zero and at least one of the levels `t,-t`. No estimate on the measure of a global nonoscillatory region is being assumed.

Choose `z_0` at a level `±t`, and put

$$
\Lambda_r=1+\sup_\beta\|\nabla G_{r,\beta}\|_\infty,
\qquad a_r=t/(4\Lambda_r).
$$

The Euclidean gradient norm controls the flat-torus geodesic Lipschitz constant. The radius `a_r<1/8` ball has exact area `pi a_r^2`. On it,

$$
3t/4\le|G|\le5t/4<1.
$$

The elementary inequality `|exp(ix)-1|>=|x|/2` for `|x|<=1` gives

$$
\int_{\mathbb T^2}|e^{iG_{r,\beta}}-1|^2
\ge\frac{9t^2}{64}\cdot\frac{\pi t^2}{16\Lambda_r^2}
=\frac{9\pi}{1024}\frac{t^4}{\Lambda_r^2}.
\tag{5.3}
$$

The same lower bound holds for every allowed `beta`. Equation (5.1), with `s=1`, gives `Lambda_r<=exp(C r log(r+1))`. The fixed strictly positive factor `t^4` is absorbed into a fixed larger constant in the exponent, uniformly for `r>=2`. Therefore

$$
\mu_r:=\min_{\beta\in[2^{-r},1]}
\int|e^{iG_{r,\beta}}-1|^2
\ge e^{-C_\mu r\log(r+1)}.
\tag{5.4}
$$

Continuity in `beta` ensures the displayed minimum exists, although the same proof would suffice with an infimum. This lower bound remains valid for very large global phase amplitudes and for growing `r`. It is not an unproved uniform stationary-phase assertion.

## 6. The large real phase does not introduce a double exponential

For every fixed `s`, derivatives of `exp(iuG)`, `0<=u<=1`, are finite sums of products of at most `s` derivatives of `G`, multiplied by a factor of modulus one. Thus (5.1) implies

$$
\sup_{0\le u\le1}\|e^{iuG}\|_{C^s}
+\||e^{iG}-1|^2\|_{C^s}
\le e^{C_s r\log(r+1)}.
\tag{6.1}
$$

This bound uses real smooth norms. Substituting an analytic norm of `exp(iG)` would be unjustified at this budget and could produce a much larger exponential. The source does not make that substitution.

For a smooth function on the two-dimensional torus, two applications of `1-Delta` give

$$
|\widehat F(ν)|\le
C\|F\|_{C^4}(1+|ν|^2)^{-2}.
$$

The weighted sum

$$
\sum_{ν\in\mathbb Z^2}(1+|ν|_1)(1+|ν|^2)^{-2}
$$

converges: a shell of radius `R` has `O(R)` points and contributes `O(R^-2)`. Thus a `C^4` bound is sufficient for precisely the Fourier weight one used below. No stronger borderline Fourier weight is being silently inserted.

The exact unreduced integer-frequency Weyl product gives

$$
\|Q_N(F)Q_N(J)-Q_N(FJ)\|
\le\frac{C}{N}
\left(\sum_ν(1+|ν|_1)|\widehat F(ν)|\right)
\left(\sum_ν(1+|ν|_1)|\widehat J(ν)|\right).
\tag{6.2}
$$

This uses `|exp(pi i omega/N)-1|<=pi|omega|/N`. The mode labels have not been reduced before estimating, so the identity and bound cover all aliases.

Let `Y(u)=Q_N(exp(iuG))`. Its derivative is `iQ_N(G exp(iuG))`. Subtract the differential equation for `exp(iuQ_N(G))` and apply the inhomogeneous Duhamel formula. The homogeneous propagator is unitary because `G` is real. It is neither necessary nor correct to assume that `Y(u)` itself is unitary. Equations (5.1), (6.1), and (6.2) yield

$$
\|e^{iQ_N(G)}-Q_N(e^{iG})\|
\le N^{-1}e^{C r\log(r+1)}.
\tag{6.3}
$$

Similarly, (2.7) and the analytic derivative estimate show

$$
\|2\pi\beta\partial_q^{r-1}(v_h-v_0)\|_0
\le h^2e^{C r\log(r+1)}.
\tag{6.4}
$$

Both resulting quantized phases are Hermitian. Their exponentials differ by at most their generator difference, again by unitary Duhamel. A factor exponential in the norm of either large generator is not present.

## 7. Exact endpoint descent and character compression

Let

$$
b=\lfloor dN^{-1/r}\rfloor,
\qquad\delta=b/d,
\qquad\beta_N=N\delta^r.
$$

The hypothesis `d>=N^(1/r)` gives `b>=1`. For every real `x>=1`, `floor(x)>=x/2`; hence

$$
\delta\le N^{-1/r},\qquad
2^{-r}\le\beta_N\le1,\qquad
N\delta=bdm\in\mathbb Z.
\tag{7.1}
$$

The lower `beta` endpoint is important because it contributes exactly the `2^-r` factor already included in (5.2).

For completeness, the line-to-finite normalization is

$$
(Zf)(\alpha,\zeta)_j
=N^{-1/2}\sum_{n\in\mathbb Z}e^{-2\pi in\alpha}
f((j+\zeta)/N+n),\qquad0\le j<N.
\tag{7.2}
$$

Parseval in `alpha`, followed by `dq=d zeta/N`, proves exact norm preservation. If `j+l=j'+Nm` with `0<=j'<N`, the mode fiber acts by

$$
e^{2\pi ik(j+\zeta+l/2)/N}e^{2\pi im\alpha}u_{j'}.
\tag{7.3}
$$

This derives both the positive wrap phase and the zero-fiber convention (2.1). At the endpoint `delta`, the translation also preserves fibers because `N delta` is integral. The norm bound on the line therefore holds almost everywhere in the fiber parameters. All finite endpoint matrices are continuous in these parameters, including their one-sided values at the zero corner, so the same bound holds at the required zero fiber. No norm loss or order-dependent constant is introduced by this descent.

Intermediate values `s` in the line Duhamel integral need not preserve these fibers. The proof uses line estimates for every `s` and descends only the endpoint operator. It does not incorrectly assume finite-dimensional fiber preservation along the entire path.

Since `delta^r/h=2pi beta_N<=2pi`, equations (4.5), (6.3), and (6.4) imply

$$
\|C_{r-1}(\delta)-Q_N(e^{iG_{r,\beta_N}})\|
\le e^{C_Er^2}N^{-1/r}.
\tag{7.4}
$$

Here the `N^-1` and `N^-2` errors have been enlarged to `N^(-1/r)`, and `r log(r+1)` has been enlarged to `r^2`; both changes are valid for `r>=2`.

For the character compression, Weyl conjugation shows that a mode is killed unless both its coordinates are divisible by `d`. Every surviving nonzero integer label has `|nu|_1>=d`, including a nonzero label that aliases to zero modulo `N`. Therefore

$$
\|P_\chi Q_N(F)P_\chi-(\int F)P_\chi\|
\le\sum_{|ν|_1\ge d}|\widehat F(ν)|
\le Cd^{-1}\|F\|_{C^4}.
\tag{7.5}
$$

The final bound follows, for example, by taking `d^-1` out of the convergent weighted coefficient sum. It does not discard arithmetic aliases.

For `F=e^(iG)-1`, use the exact adjoint identity `Q(F)^*=Q(conjugate F)`, the product defect (6.2), and (7.5) applied to `|F|^2`. For every unit input character vector,

$$
\left|\|Q_N(F)v\|^2-\int|F|^2\right|
\le e^{C r\log(r+1)}(d^{-1}+N^{-1}).
\tag{7.6}
$$

This is uniform over every vector in every character space; no averaging over characters or vectors is involved.

## 8. A single threshold controls every order

Let the lower bound in (5.4) have constant `C_mu`, and enlarge `C_E` in (7.4) to cover also (7.6). Since `d>=N^(1/r)`, all errors are bounded by

$$
\exp[C_Er^2-(\log N)/r].
\tag{8.1}
$$

If `log N>=C_0r^3`, then this is at most `exp[-(C_0-C_E)r^2]`. Because `r log(r+1)<=r^2` for all `r>=2`, one fixed sufficiently large `C_0` makes the squared-norm error smaller than one quarter of the lower bound (5.4), and the operator error smaller than one quarter of its square root, for every order. Fixed numerical factors and the fixed `t^4` lower-bound factor can be absorbed at the same time. No additional order-dependent threshold remains.

Consequently

$$
\|(C_{r-1}(\delta)-I)v\|
\ge\tfrac12e^{-C r\log(r+1)}.
\tag{8.2}
$$

To convert this to an all-pairs escape estimate, let

$$
\varepsilon=\|(I-P_\psi)E_Nv\|.
$$

At the chosen endpoint, `R=T_N(-bN/d,0)` is a member of the commuting subgroup. It acts on the input and target character spaces by possibly different unit scalars `r_chi,r_psi`. Hence

$$
(R/r_\chi)v=v,\qquad
\|(E_N^*RE_N/r_\psi-I)v\|\le2\varepsilon.
\tag{8.3}
$$

For the second estimate, decompose `E_Nv` into its `P_psi` and outside parts; the first is annihilated by `R/r_psi-I`, and the latter is acted on with norm at most two. The inverse normalized `B` has the same error on `v` because `B` is unitary. Scalar normalizations cancel inside every commutator word for `r>=2`.

The elementary telescoping identity for a product of unitary factors, evaluated on this one fixed vector, bounds the defect by the sum of the individual factor defects on that vector. Thus the `2^(r-1)` occurrences of `B` or `B^*` give

$$
\|(C_{r-1}-I)v\|\le2^r\varepsilon.
\tag{8.4}
$$

Equations (8.2) and (8.4) prove (1.1), after absorbing `2^(r+1)` into `exp(C_1r log(r+1))`. Distinct input and target character phases cause no obstruction.

Finally, the exact covariance

$$
T_N(a,b)M_N=M_NT_N(3a-4b,-2a+3b)
$$

maps the subgroup to itself and permutes its character spaces, since the indicated matrix has determinant one. Applying (1.1) to `M_Nv` proves the asserted statement for `U_N`.

## 9. Subpolynomial range and robust quasimodes

Put `L=log N` and

$$
r=\left\lfloor(L/C_0)^{1/3}\right\rfloor.
$$

For sufficiently large `N`, `r>=2`, `C_0r^3<=L`, and `r>=(L/C_0)^(1/3)/2`. Therefore

$$
L/r\le2C_0^{1/3}L^{2/3}.
$$

One may take `C_2` at least `2C_0^(1/3)` and enlarge `N_0` to handle the floor. The divisor hypothesis then implies `d>=N^(1/r)`. Substitution in (1.1) yields (1.2), for a fixed suitable `C_3`.

Since

$$
\frac{L^{1/3}\log L}{L}=L^{-2/3}\log L\longrightarrow0,
$$

this escape norm is `N^(-o(1))` and eventually exceeds every fixed negative power `N^-a`.

For arbitrary unit `v`, write `P=P_chi`, `a=||Pv||`, `b=||(I-P)v||`. The outside component of the residual decomposes exactly as

$$
(I-P)(U_N-\lambda)v
=(I-P)U_NPv+(I-P)(U_N-\lambda)(I-P)v.
$$

If `a>0`, the first term has norm at least `epsilon_N a`, by applying the escape theorem to `Pv/a`; if `a=0`, the eventual bound is trivial. Since `|lambda|=1`, the second term has norm at most `2b`. Therefore

$$
\|(U_N-\lambda)v\|\ge\epsilon_N a-2b.
\tag{9.1}
$$

If `b=o(epsilon_N)`, then `a` tends to one and the lower bound is `(1-o(1))epsilon_N`, much larger than `1/N`. This proves the claimed robust exclusion of microscopic quasimodes near one covered character space. The factor two correctly includes the outside component of `-lambda v`.

## 10. Limits of the audited conclusion

The new theorem controls the explicit divisor range `log d>=C_2(log N)^(2/3)`. It does not cover every subpolynomial square divisor. It does not exclude clusters formed by vectors spread over many character spaces, or by another mechanism entirely.

The earlier all-time trace-removal conclusion cannot simply be carried over from a fixed positive escape constant. Here the escape norm shrinks with `N`; geometric-series constants involving its reciprocal may grow. The source expressly retains this limitation. The present audit verifies no such trace extension.

The original first unresolved spectral step remains the signed original-family pair discrepancy, for example the fixed admissible test described in the source,

$$
\frac1{N^2}\sum_{1\le n<2N}|\widehat b_*(n/N)|^2
\bigl(|\operatorname{Tr}U_N^n|^2-\min(n,N)\bigr).
$$

Its limit is not evaluated by the audited theorem. No assertion of `H_diag`, no counterexample to it, and no historical-priority claim follows from this audit.

The complete local dependency chain checked here is: exact real-half symbol and Heisenberg series; fixed analytic radius; radius allocation for depth `r`; finite-word remainder count; quantitative phase integral lower bound; real smooth exponential norms; exact endpoint Zak descent and Fourier compression; one threshold `log N>=C_0r^3`; character telescoping; and the robust projection estimate. Within that chain and the stated theorem, no first missing estimate was found.
