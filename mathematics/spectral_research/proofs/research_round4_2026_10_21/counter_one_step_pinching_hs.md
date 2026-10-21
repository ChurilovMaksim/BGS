> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round4_2026_10_21/counter_one_step_pinching_hs.md`. Embedded SHA256: `a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`.
> [Thematic guide](../../topics/closure.md).

# One-step Hilbert--Schmidt pinching and all-time arithmetic-history removal

Date: 21 October 2026. New proof for the original fixed kick and original deterministic matrices.

## 0. Statement and audit status

Put `E_N=exp(i tau N A_N)` with exactly `tau=10^(-80)`. For odd `N=d^2m`, let `P_chi` be the character projections of

$$
H_d(s,u)=T_N(sN/d,uN/d),\qquad (s,u)\in(\mathbb Z/d\mathbb Z)^2,
$$

and write

$$
\mathcal P_d(X)=\sum_\chi P_\chi X P_\chi,
\qquad \sigma_{N,d}=N^{-1/2}\|\mathcal P_d(E_N)\|_{\rm HS}.
$$

**Theorem 1.** There are fixed finite `C,N_0` and a fixed `epsilon>0`, depending only on the explicit symbol and the fixed `tau`, such that for every odd `N>=N_0` and every `d` with `d^2|N`,

$$
\boxed{
\left|\sigma_{N,d}^2-\frac1{d^2}\right|\le C N^{-\epsilon},
\qquad
\sigma_{N,d}\le\frac1d+C N^{-\epsilon/2}.
}
\tag{0.1}
$$

The exponent is a fixed positive number, not a number permitted to tend to zero with the divisor. Its numerical size is not optimized.

**Theorem 2.** Combine Theorem 1 with the independently audited growing-order escape theorem. There are fixed `C_2,C_3,N_1` such that, for every odd `N=d^2m>=N_1` with

$$
\log d\ge C_2(\log N)^{2/3},
\tag{0.2}
$$

the complete pair-trace functional, with any uniformly bounded array of weights, is changed by `o(1)` when one removes all character histories containing at most `floor(delta_N n)` deviations from the exact metaplectic character permutation at time `n`. The density is explicit in (9.2), tends to zero, and satisfies `delta_N=N^{-o(1)}`. The conclusion includes the full cross-term with all retained histories and all positive times, including an infinite Abel tail. It does not use a short-time cutoff.

This is a new theorem candidate pending an independent audit of this manuscript. It does not establish or refute `H_diag`. The earlier escape theorem used in Theorem 2 is frozen in `counter_subpolynomial_comb_quantitative.md`, SHA-256 `3b59bd021e393489cd709073e683a2dec137333e0e657849b0636a9f85f90def`, and independently audited in `audit_growing_order_comb_quantitative.md`, SHA-256 `30a2039b988d49f12960ffb1d27fc72dedc6eefcb38d005d75ebee06c5de17cb`.

The only additional oscillatory lemma used below is proved in full in `root_uniform_analytic_oscillation.md`, SHA-256 `5eaae7946e30df2507a870535ec46c2dbc2bce07cc96c8b85366772cab590d31`, Sections 1--5. I read and checked its compactification, derivative bound, localization, one-dimensional estimate, and grid summation before applying it. Its Section 6 is explicitly conditional on an exact kick representation; Sections 1--6 of the present manuscript supply that representation and its uniform error. Thus those two manuscripts do not rely circularly on one another.

## 1. Exact quantization identities, including modular aliases

Use

$$
h=(2\pi N)^{-1},\qquad t=\tau/(2\pi),\qquad
W_N(k,l)=(-1)^{kl}T_N(l,k),\qquad Q_N(F)=\sum_v\widehat F(v)W_N(v).
\tag{1.1}
$$

For smooth functions the sum is absolutely convergent at each fixed `N`. The exact ordinary-half symbol of `A_N` is

$$
\begin{aligned}
a(q,p)={}&\cos(14\pi q)+\frac{r(q)}{10}
 +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}\\
&+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0).
\end{aligned}
\tag{1.2}
$$

Indeed multiplying each original Fourier coefficient by `(-1)^(kl)` gives this half-period shift in the rows `l=+/-1`. Hence `A_N=Q_N(a)` and `exp(it A_N/h)=E_N`. Its Fourier support satisfies `|k|+|l|<=9`, its coefficient one-norm is less than two, and

$$
\widehat a(1,0)=\frac1{20}-\frac{i}{200},\qquad
\widehat a(0,1)=\frac{-3-4i}{1000}.
\tag{1.3}
$$

Let

$$
J=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
\omega(v,w)=v_2w_1-v_1w_2.
$$

Direct multiplication of the Weyl operators, including the signs in (1.1), gives

$$
W_N(v)W_N(w)=e^{\pi i\omega(v,w)/N}W_N(v+w).
\tag{1.4}
$$

The modular-half contribution `(-1)^omega` cancels the signs from `(-1)^(kl)`; thus the phase in (1.4) uses an ordinary real half. Since `a` has finite support, (1.4) gives the exact finite-shift left product

$$
Q_N(a)Q_N(F)=Q_N(a\star_h F),\qquad
(a\star_h F)(x)=\sum_v a_v e^{2\pi i v\cdot x}
F(x+\pi hJv).
\tag{1.5}
$$

Two further exact identities control rapidly oscillating symbols without an operator-norm expansion. First,

$$
\boxed{N^{-1/2}\|Q_N(F)\|_{\rm HS}\le2\|F\|_\infty.}
\tag{1.6}
$$

To prove it, note that `W_N(v+2Nk)=W_N(v)`. Collapse the Fourier coefficients modulo `2N`. They are the discrete Fourier coefficients of the values of `F` on the `(2N)^2` grid. Each class modulo `N` consists of four such coefficients whose Weyl matrices differ only by signs. Orthogonality of the `N^2` Weyl matrices modulo `N` and Cauchy--Schwarz on each four-term sum show

$$
N^{-1}\|Q_N(F)\|_{\rm HS}^2
\le4\sum_{v\bmod2N}|\widetilde F(v)|^2
=\frac4{(2N)^2}\sum_{x\in(2N)^{-1}\mathbb Z^2/\mathbb Z^2}|F(x)|^2.
$$

This proves (1.6), including every alias.

Second, for smooth `F,G`,

$$
\boxed{
\frac1N\operatorname{Tr}(Q_N(F)^*Q_N(G))
=\sum_{m=(r,s)\in\mathbb Z^2}(-1)^{rs}
\int_{\mathbb T^2}\overline{F(x+(s/2,r/2))}\,G(x)
e^{-2\pi iN m\cdot x}\,dx.
}
\tag{1.7}
$$

For this identity, if `v=(k,l)`, then oddness of `N` gives

$$
W_N(v+Nm)=(-1)^{ks+lr+rs}W_N(v).
$$

The trace pairing vanishes unless the two Fourier labels differ by `Nm`. Substitution and Fourier orthogonality prove (1.7). Absolute convergence of the original two Fourier series justifies regrouping. The half-period shifts in (1.7) will be retained below; they are not discarded by replacing the modular quantization with a continuous convention.

## 2. A global analytic center phase on a certified short interval

This section constructs the phase rather than assuming an FIO formula. Fix

$$
\rho=10^{-3},\qquad t_0=10^{-10},\qquad Y=-J\nabla a.
$$

On the complex tube `|Im x_j|<=2 rho`, the support and coefficient sum in Section 1 imply

$$
\|\nabla a\|_\infty<200,\qquad \|DY\|_{\infty\to\infty}<10^4.
\tag{2.1}
$$

For the first bound use `2(2 pi)9 exp(2 pi(2rho)9)<200`. For the second use
`2(2 pi)^2 9^2 exp(2 pi(2rho)9)<10^4`; the factor `|v_j|(|v_1|+|v_2|)` already bounds the complete matrix row sum. Every higher derivative is bounded as well, since the support is finite.

Let `Phi_s(y)` solve `Phi'=Y(Phi)`, `Phi_0(y)=y`. Picard iteration and (2.1) give the analytic flow for initial points with imaginary parts at most `rho` and all `0<=s<=t_0`. Its displacement is at most `200s`, so it stays inside the larger tube, and

$$
\|D\Phi_s-I\|_{\infty\to\infty}
\le e^{10^4s}-1\le2\cdot10^4s.
\tag{2.2}
$$

Consider the center map

$$
x_s(y)=\frac{y+\Phi_s(y)}2.
\tag{2.3}
$$

It is `y+q_s(y)`, with `||q_s||_infty<=100s` and `||Dq_s||<=10^4s<=10^(-6)`. For every `x` in the strip of width `rho/2`, the equation `y=x-q_s(y)` is a contraction in a ball of radius `200s`. The ball lies in the strip of width `rho`. Hence (2.3) has a unique analytic inverse there. It is real on the real torus and respects all integer translations.

Define along these characteristics

$$
\xi_s(y)=J(\Phi_s(y)-y),\qquad
H(x,\xi)=-a(x-J\xi/2).
$$

A direct calculation gives `x_s'=partial_xi H` and `xi_s'=-partial_x H`. Indeed `x_s-J xi_s/2=Phi_s(y)`, `x_s'=-J grad a(Phi_s(y))/2`, and `xi_s'=grad a(Phi_s(y))`.

Define the action by

$$
S_s(x_s(y))=\int_0^s
\big(\xi_u(y)\cdot x_u'(y)-H(x_u(y),\xi_u(y))\big)\,du.
\tag{2.4}
$$

It is analytic on the smaller complex strip, real valued on the real torus, and periodic: shifting the starting point by an integer shifts `Phi,x` by that integer and leaves the integrand unchanged. Differentiating (2.4) in the initial point, integrating by parts, and using the two Hamilton equations cancels the interior terms and leaves `xi_s dot dx_s`; the initial momentum is zero. Thus

$$
\nabla S_s(x_s(y))=\xi_s(y),\qquad
\partial_sS_s(x)=a(x-J\nabla S_s(x)/2),\qquad S_0=0.
\tag{2.5}
$$

The second identity follows by differentiating the action at fixed endpoint, which leaves `-H`. This calculation proves the Hamilton--Jacobi equation with the sign forced by (1.5).

The displacement bound gives

$$
\|\nabla S_s\|_\infty\le200s.
\tag{2.6}
$$

On the real torus, the argument of `a` in (2.5) differs from `x` by at most `100s` in each coordinate. Since the sum of the absolute partial derivatives of `a` is at most `400`, integration in `s` yields the numerical estimate

$$
\|S_s-sa\|_\infty\le2\cdot10^4s^2.
\tag{2.7}
$$

For every fixed derivative order, analytic continuation on a fixed smaller strip gives finite uniform derivative bounds on `S_s` for `0<=s<=t_0`. The value needed for the original family, `t=tau/(2 pi)`, lies inside this certified interval.

In particular, (1.3) and (2.7) prove at this fixed positive `t`

$$
\boxed{|widehat S_t(1,0)|\ge t/250,
\qquad |widehat S_t(0,1)|\ge t/250.}
\tag{2.8}
$$

Indeed the smaller original coefficient has modulus `1/200`, whereas `2*10^4 t<=2*10^(-6)` on the entire interval. These are actual nonzero coefficients of the exact center phase, not coefficients substituted from its first-order approximation.

## 3. Transport and the exact finite-shift residual

For `0<=s<=t_0`, set

$$
y_s(x)=x-J\nabla S_s(x)/2,\qquad
V_s(x)=\tfrac12J\nabla a(y_s(x)).
$$

Let `b_s` solve

$$
\partial_s b_s=V_s\cdot\nabla b_s
 +\tfrac12(\operatorname{div}V_s)b_s,
\qquad b_0=1.
\tag{3.1}
$$

This equation is solved along the real characteristics `x'=-V_s(x)` by exponentiating the integral of `div V_s/2`. The analytic construction has a numerical common interval as well. On the strip of width `rho/4`, Cauchy's estimate applied to (2.6) gives each entry of `D^2S_s` magnitude at most `8*10^5 s`, hence its matrix row-sum norm is at most `1.6*10^6 s<=1.6*10^(-4)`. Thus `||D y_s||<=2`, `||V_s||_infty<=100`, and `||DV_s||<=10^4`. Starting in the strip of width `rho/8`, its time-dependent characteristics stay in the strip of width `rho/4` throughout `t_0`; their displacement is at most `100t_0=10^(-8)`. Analytic ODE iteration gives the transport solution on that common smaller strip. Since `|div V_s/2|<=10^4`, the exponential formula bounds `|b_s|<=exp(10^4t_0)<2` there. Cauchy's estimates on a further fixed smaller strip bound each derivative independently of `h,N`. The function is real and positive on the real torus. The exact conservation identity

$$
\partial_s(b_s^2)=\operatorname{div}(V_s b_s^2),\qquad
\int_{\mathbb T^2}b_s^2=1
\tag{3.2}
$$

also follows directly from (3.1).

Define

$$
F_{s,h}(x)=b_s(x)e^{iS_s(x)/h}.
\tag{3.3}
$$

Taylor expansion of the exact finite shifts in (1.5), with only finitely many vectors `v`, gives

$$
\begin{aligned}
a\star_h F_{s,h}
=e^{iS_s/h}\bigg[
&a(y_s)b_s
-ih\,V_s\cdot\nabla b_s\\
&-\frac{ih}{8}\operatorname{Tr}
\big(D^2S_s\,J D^2a(y_s)J^T\big)b_s
 +O(h^2)\bigg].
\end{aligned}
\tag{3.4}
$$

The remainder is uniformly bounded pointwise by `C h^2` for all `0<=s<=t_0` and all `N>=3`. To check it explicitly, expand

$$
\frac{S_s(x+\pi hJv)-S_s(x)}h
=\pi Jv\cdot\nabla S_s
 +\frac{\pi^2h}{2}D^2S_s[Jv,Jv]+O(h^2),
$$

and `b_s(x+pi hJv)=b_s+pi hJv dot grad b_s+O(h^2)`. The derivatives required for these remainders are bounded uniformly by the preceding construction; the phase is real on the integration torus. The leading sum equals `a(y_s)`. Using
`sum_v v a_v e^(2 pi i v y)=grad a(y)/(2 pi i)` and its second derivative identifies the two order-`h` terms in (3.4).

A direct derivative of `V_s` yields

$$
\frac12\operatorname{div}V_s
=\frac18\operatorname{Tr}
\big(D^2S_s\,J D^2a(y_s)J^T\big).
\tag{3.5}
$$

For this, the term `Tr(J D^2a)` vanishes and `J^T=-J`. Thus (2.5) and (3.1) cancel both displayed orders when differentiating (3.3):

$$
\left\|\partial_sF_{s,h}-\frac ih(a\star_hF_{s,h})\right\|_\infty
\le C h.
\tag{3.6}
$$

This is a bound for the actual finite-shift equation, not a formal substitution of a classical phase into the original matrix exponential.

## 4. Approximation to the exact matrix exponential in normalized HS norm

Put `W_s=Q_N(F_(s,h))`. From (1.5), (1.6), and (3.6),

$$
N^{-1/2}\left\|\partial_s W_s-\frac ihA_NW_s\right\|_{\rm HS}
\le2Ch,
\qquad W_0=I.
$$

The exact propagator `exp(is A_N/h)` is unitary. Duhamel's identity in this finite-dimensional space therefore gives

$$
\boxed{
N^{-1/2}\|E_N-Q_N(F_{t,h})\|_{\rm HS}\le C'h.
}
\tag{4.1}
$$

All constants are fixed before `N,d` or a translation is selected. No derivative of `e^(iS/h)` is estimated in operator norm; the uniform pointwise residual is passed to normalized HS norm by the exact alias inequality (1.6).

## 5. Exact translation echo and the nonzero alias terms

Let `T_N(a_0,b_0)` be any Weyl translation, and put `z=(a_0/N,-b_0/N)` on the torus. Exact conjugation gives

$$
T_N(a_0,b_0)Q_N(F)T_N(a_0,b_0)^*=Q_N(F(\cdot+z)).
\tag{5.1}
$$

Set `S=S_t`, `b=b_t`, `F=b exp(iS/h)`. By (4.1), HS Cauchy--Schwarz, and unitary invariance,

$$
\frac1N\operatorname{Tr}(E_N^*T E_NT^*)
=\frac1N\operatorname{Tr}(Q_N(F)^*Q_N(F(\cdot+z)))+O(N^{-1}),
\tag{5.2}
$$

uniformly in the translation. For example, the difference of the two pairings is at most `eta(2+eta)`, where `eta=N^(-1/2)||E_N-Q_N(F)||_HS=O(N^(-1))`.

Apply the exact alias formula (1.7). Its `m=0` term is

$$
\int_{\mathbb T^2}b(x)b(x+z)
e^{i(S(x+z)-S(x))/h}\,dx.
\tag{5.3}
$$

For `m=(r,s)!=0`, its phase is

$$
2\pi N\big[S(x+z)-S(x+(s/2,r/2))-m\cdot x\big].
\tag{5.4}
$$

Choose a coordinate with `|m_j|=|m|_infty`. By (2.6), `||grad S||_infty<=200t<1/8`; hence the absolute derivative of the bracket in (5.4) in that coordinate is at least `|m|_infty-1/4>=3|m|_infty/4`. After division of that bracket by `|m|_infty`, all its derivatives of every fixed order are uniformly bounded. The amplitudes `b(x+(s/2,r/2))b(x+z)` also have uniform derivative bounds; there are only four possible half-period shifts modulo the torus.

Repeated integration by parts in the selected coordinate therefore bounds that term, for every fixed integer `K`, by

$$
C_K(N|m|_\infty)^{-K}.
$$

The coefficients in the integration operator and their derivatives are uniformly bounded because the normalized phase derivative is bounded away from zero. Boundary terms vanish by periodicity, including the integer Fourier modulation in (5.4). For `K>2`, summing over all `m!=0` proves an `O_K(N^(-K))` alias error, uniformly in `z`.

Combining this with (5.2) gives the desired exact-kick representation

$$
\boxed{
\frac1N\operatorname{Tr}(E_N^*T E_NT^*)
=\int b(x)b(x+z)
e^{i(2\pi N)(S(x+z)-S(x))}\,dx+O(N^{-1}),
}
\tag{5.5}
$$

uniformly over all Weyl translations. The phase and amplitude are fixed functions determined by the exact value of `tau`; the error is uniform and proved for the original modular quantization.

## 6. Uniform oscillation and proof of Theorem 1

The fixed function `S` is real analytic, periodic, and satisfies both nonzero Fourier conditions (2.8). The amplitudes `b(x)b(x+z)` have a uniform `C^1` bound. Therefore all hypotheses of the fully proved oscillatory lemma in `root_uniform_analytic_oscillation.md`, Sections 1--5, hold with `lambda=2 pi N`. In its notation there is one fixed `epsilon=1/M` with `0<epsilon<=1` such that the integral in (5.5) is bounded by

$$
C(1+N\operatorname{dist}(z,\mathbb Z^2))^{-\epsilon}.
\tag{6.1}
$$

For clarity, the essential nondegeneracy is uniform even when `z->0`. Write `z=r omega` using a centered representative. The normalized phases are

$$
\frac{S(x+z)-S(x)}r
=\int_0^1\omega\cdot\nabla S(x+u r\omega)\,du.
$$

They form a compact analytic family including `r=0`. The two coefficients in (2.8) ensure no member is constant, including every limiting directional derivative. Analyticity and compactness then provide one finite derivative order on every point of every member. The cited lemma proves its local oscillatory estimate from that finite-order bound, rather than assuming a stationary-phase formula valid only at nondegenerate critical points.

The character pinching is the orthogonal projection for the HS inner product and equals the exact finite group average

$$
\mathcal P_d(E_N)=d^{-2}\sum_{g_0\in G_d}H_d(g_0)E_NH_d(g_0)^*.
$$

Consequently,

$$
\sigma_{N,d}^2
=\frac1{d^2}\sum_{z\in(d^{-1}\mathbb Z/\mathbb Z)^2}
\frac1N\operatorname{Tr}(E_N^*T_zE_NT_z^*).
\tag{6.2}
$$

Here `T_z` denotes the corresponding Weyl operator; the sign reversal in its second coordinate permutes the grid. The identity translation contributes exactly `d^(-2)`.

For the remaining terms, average (6.1) on the grid. In two dimensions the singularity `dist(z)^(-epsilon)` is integrable, and its discrete average is bounded uniformly in `d`:

$$
\frac1{d^2}\sum_{z\ne0}\operatorname{dist}(z,\mathbb Z^2)^{-\epsilon}\le C_\epsilon.
\tag{6.3}
$$

Indeed the shell `max(|j_1|,|j_2|)=k` in the centered integer representatives has `O(k)` points, and its distance after division by `d` is at least `k/d`; thus the sum is at most `C d^(epsilon-2) sum_(k<=d/2+1) k^(1-epsilon)<=C_epsilon`.

Equations (5.5), (6.1), and (6.3), applied to (6.2) after isolating the identity term, yield

$$
\left|\sigma_{N,d}^2-d^{-2}\right|
\le C N^{-\epsilon}+C N^{-1}\le C' N^{-\epsilon}.
$$

Taking square roots and using `sqrt(x+y)<=sqrt(x)+sqrt(y)` proves (0.1). This proves Theorem 1 uniformly for every allowed square divisor, including ones depending arbitrarily on `N`.

## 7. Mixing one HS estimate with the operator compression gap

This section is a finite-dimensional inequality. Let

$$
K=\mathcal P_d(E_N)M_N,\qquad R=U_N-K,
\qquad \|K\|\le\rho=1-g,\qquad 0<g\le1/2.
$$

Then

$$
\|K\|_{\rm HS}=\sqrt N\,\sigma_{N,d},\qquad
\|R\|\le2-g.
\tag{7.1}
$$

For any word of length `n` containing `j<n` letters `R`, put one of its `K` factors in HS norm and every other factor in operator norm. The ideal inequality for HS norm and `|Tr X|<=sqrt N ||X||_HS` give

$$
\frac{|\operatorname{Tr}(\mathrm{word})|}{N}
\le\sigma_{N,d}\rho^{n-j-1}(2-g)^j.
\tag{7.2}
$$

No independence assumption is used. This estimate holds for every placement of the letters, irrespective of their commutators.

Define

$$
z_g=\frac{g}{2(2-g)},\quad
\delta(g)=\frac{-\log(1-g/2)}{2\log(2(2-g)/g)},\quad
\eta=\sqrt{1-g/2}.
\tag{7.3}
$$

Let `S_n` be the sum of all words in `K,R` with at most `floor(delta(g)n)` occurrences of `R`, and `s_n=Tr S_n`. Since `delta(g)<1`, every retained word has at least one factor `K`, so (7.2) applies to all of them. The binomial estimate

$$
\sum_{j\le\lfloor\delta(g)n\rfloor}
\binom nj\rho^{n-j}(2-g)^j
\le z_g^{-\delta(g)n}\big(\rho+z_g(2-g)\big)^n
=\eta^n
\tag{7.4}
$$

therefore proves

$$
\boxed{
\frac{|s_n|}{N}\le\frac{\sigma_{N,d}}\rho\eta^n,
\qquad \|S_n\|\le\eta^n.
}
\tag{7.5}
$$

The second inequality follows from the same binomial calculation in operator norm. It ensures that `|s_n|/N<=1`, including any dimensions where the first upper bound might exceed one.

## 8. Complete signed pair removal without an early-time gap

Put `p_n=Tr U_N^n` and `q_n=p_n-s_n`. For any complex array of weights `w_(n,N)` with `sup|w_(n,N)|<=W`, the square identity and (7.5) give

$$
\begin{aligned}
\frac1{N^2}\sum_{n\ge1}|w_{n,N}|
\left||p_n|^2-|p_n-s_n|^2\right|
&\le3W\frac{\sigma_{N,d}}\rho
\sum_{n\ge1}\eta^n\\
&\le\boxed{24W\,\frac{\sigma_{N,d}}g}.
\end{aligned}
\tag{8.1}
$$

Here `|p_n|<=N`, `rho>=1/2`, and `1-eta=(g/2)/(1+eta)>=g/4`. Thus the bound includes the cross-term between the removed histories and the entire retained trace. The difference series is absolutely convergent at every dimension. For nondecaying bounded weights, this makes no assertion about separate convergence of the two individual square-trace series.

The analogous pure-history bound, with `s_n=Tr K^n`, is

$$
\frac1{N^2}\sum_{n\ge1}|w_{n,N}|
\left||p_n|^2-|p_n-\operatorname{Tr}K^n|^2\right|
\le3W\,\frac{\sigma_{N,d}}g.
\tag{8.2}
$$

Indeed (7.2) gives `|Tr K^n|/N<=sigma_(N,d) rho^(n-1)` and its operator norm also bounds the normalized trace by one.

The sufficient condition from (8.1) is `sigma_(N,d)/g_N -> 0`. It replaces the earlier requirement that the gap times `log N` be large: one small HS factor already controls the whole early-time interval. This is why the estimate is useful even when `g_N log N -> 0`.

## 9. Application to the full previously reached subpolynomial range

The independently audited growing-order escape theorem states that under (0.2), for sufficiently large `N`, every character compression satisfies

$$
\|P_\psi E_NP_\chi\|
\le\sqrt{1-\ell_N^2},\qquad
\ell_N=\exp[-C_3(\log N)^{1/3}\log\log N].
\tag{9.1}
$$

Enlarging constants or the fixed threshold if needed does not change the asserted range. The diagonal case and `1-sqrt(1-x)>=x/2` allow the explicit choice

$$
\boxed{
g_N=\tfrac12\exp[-2C_3(\log N)^{1/3}\log\log N],
\qquad \delta_N=\delta(g_N).
}
\tag{9.2}
$$

Then `||K||<=1-g_N`, and Theorem 1 gives, with `L=log N`,

$$
\begin{aligned}
\frac{\sigma_{N,d}}{g_N}
&\le C\exp[-C_2L^{2/3}+2C_3L^{1/3}\log L]\\
&\quad+C\exp[-(\epsilon/2)L+2C_3L^{1/3}\log L]
\longrightarrow0.
\end{aligned}
\tag{9.3}
$$

Both limits are uniform over the divisors in (0.2), because `L^(1/3)log L=o(L^(2/3))` and `o(L)`. Equations (8.1) and (9.3) prove Theorem 2, including every positive time in the weighted sum. This closes the intermediate-time failure of the earlier purely geometric majorants throughout the larger range (0.2).

The retained-density parameter is accurately described by

$$
\delta(g)\sim\frac{g}{4\log(4/g)}\quad(g\downarrow0).
\tag{9.4}
$$

Thus `delta_N -> 0` and `log(1/delta_N)=O(L^(1/3)log L)=o(L)`. At times `n` comparable to `N`, the removed class allows `N^(1-o(1))` character changes, although the fraction of allowed changes tends to zero. It does not allow a fixed positive density in this range.

## 10. Relation to the exact factorial statistic and the remaining problem

For `w_(n,N)=|bhat(n/N)|^2`, (8.1) bounds exactly the change in the pair factorial Fourier expression when replacing `p_n` by `q_n` at positive indices and by its conjugate at negative indices. The factor `1/2` in the original formula cancels the two signs, while the zero-index term and the subtraction of `N` remain unchanged. The same estimate applies to `w_(n,N)=exp(-2s n/N)` and proves control of its complete infinite tail.

The operators `K,R,S_n` arise from an exact partition of the original deterministic trace histories. The group average in (6.2) is an identity used to estimate an operator already present in that partition. Neither the kick, the spectral measure, the sequence of dimensions, nor `tau` is averaged or replaced.

The `q_n` are not claimed to be traces of a new unitary matrix. They still contain all histories with more than `floor(delta_N n)` character deviations. No weighted CUE comparison for that remaining coherent sum is proved here, and the higher fixed factorial orders in `H_diag` are not controlled. The new theorem removes a specified arithmetic contribution over a broader divisor range; it is not a proof of sine statistics or a spectral countersequence.

