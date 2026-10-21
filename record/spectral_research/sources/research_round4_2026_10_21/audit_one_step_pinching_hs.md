> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_one_step_pinching_hs.md`. Embedded SHA256: `7c59bc69854347e4615db94691d7d15bd86e0e776ce4bc639c07878bc611acce`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit: one-step HS pinching and all-time history removal

Date: 21 October 2026.

## 0. Verdict, frozen inputs, and scope

**Primary verdict: Theorems 1 and 2 are proved as written by §§1–9.** The exact finite quantization, the center-action construction, the normalized Hilbert–Schmidt remainder, the uniform translation integral, and the mixed-norm history estimate all pass independent adversarial reconstruction. No first missing estimate was found within this theorem chain.

The primary frozen source is:

- `research_round4_2026_10_21/counter_one_step_pinching_hs.md`;
- SHA-256 `a8babde8cfa7cdf0ef794775ac73672431bd9f9d36491f50e3bf19515543c629`.

The independent oscillation input was read in its raw form:

- `research_round4_2026_10_21/root_uniform_analytic_oscillation.md`;
- SHA-256 `5eaae7946e30df2507a870535ec46c2dbc2bce07cc96c8b85366772cab590d31`.

Both hashes were checked on disk. The verdict does not use another audit's PASS as a substitute for the raw analytic lemma. Its compactification, finite-type argument, localization, one-dimensional proof, and grid sum were checked directly below. The growing-order escape theorem used in Theorem 2 was already independently reconstructed in this auditor's `audit_growing_order_comb_quantitative.md`, SHA-256 `30a2039b988d49f12960ffb1d27fc72dedc6eefcb38d005d75ebee06c5de17cb`.

All prior files remain unchanged. The source's §10 phrase about the complete infinite Abel tail is valid for the **difference/correction** bounded in (8.1). It does not prove uniform control of the original Abel tail by itself. This distinction is retained throughout this audit.

## 1. Exact Weyl product and the two alias identities

Use `h=(2pi N)^-1`, `t=tau/(2pi)`, and the real-half modes `W_N(k,l)=(-1)^(kl)T_N(l,k)`. The ordinary symbol is exactly the polynomial with the `q+1/2` shift in its mixed rows. Its support radius is at most nine, its coefficient one-norm is below two, and its two stated coefficients are `1/20-i/200` and `(-3-4i)/1000`.

The exact multiplication phase is `exp(pi i omega(v,w)/N)`, with `omega(v,w)=v_2w_1-v_1w_2`. Since `Jv=(v_2,-v_1)`, translating a mode of `F` by `pi hJv` produces precisely this phase. Thus

$$
Q_N(a)Q_N(F)=Q_N(a\star_hF),\qquad
a\star_hF=\sum_v a_ve^{2\pi iv\cdot x}F(x+\pi hJv)
\tag{1.1}
$$

is an exact finite-shift identity, not a truncated symbolic expansion.

### 1.1. The sup-norm to normalized-HS bound

Oddness of `N` gives, for `v=(k,l)` and `m=(r,s)`,

$$
W_N(v+Nm)=(-1)^{ks+lr+rs}W_N(v),\qquad
W_N(v+2Nm)=W_N(v).
\tag{1.2}
$$

Collapse the absolutely convergent Fourier series modulo `2N`. The collapsed coefficients are exactly the discrete Fourier coefficients of `F` on the `(2N)^2` grid. Each residue modulo `N` contains four such coefficients, with signs given by (1.2). Orthogonality of the `N^2` Weyl modes modulo `N` and Cauchy–Schwarz on each four-term sum imply

$$
N^{-1}\|Q_N(F)\|_{\rm HS}^2
\le4\sum_{v\bmod2N}|\widetilde F(v)|^2
=\frac4{(2N)^2}\sum_{x\in(2N)^{-1}\mathbb Z^2/\mathbb Z^2}|F(x)|^2.
$$

Consequently

$$
N^{-1/2}\|Q_N(F)\|_{\rm HS}\le2\|F\|_\infty.
\tag{1.3}
$$

This remains valid for the rapidly oscillating symbol later used. There is no derivative loss and no assumption that its Fourier series fits below the alias threshold.

### 1.2. The exact trace pairing

In the pairing of `Q(F)` and `Q(G)`, only labels of the form `w=v+Nm` survive. Their inner-product sign is exactly (1.2). Expanding the integral therefore proves

$$
\frac1N\operatorname{Tr}(Q_N(F)^*Q_N(G))
=\sum_{m=(r,s)}(-1)^{rs}
\int\overline{F(x+(s/2,r/2))}G(x)e^{-2\pi iNm\cdot x}\,dx.
\tag{1.4}
$$

For example, the translated conjugate Fourier mode contributes `exp[-pi i(ks+lr)]`, equal to `(-1)^(ks+lr)`; this checks the sign and the order of the two half-period shifts. Absolute Fourier convergence at each fixed `N` justifies regrouping. Later estimates control the resulting infinite alias sum uniformly; no such uniformity is assumed at this step.

## 2. The certified center phase

The numerical Fourier bounds on the complex tube of width `2rho`, `rho=10^-3`, are valid:

$$
\|\nabla a\|_\infty<200,
\qquad\|DY\|_{\infty\to\infty}<10^4,
\qquad Y=-J\nabla a.
\tag{2.1}
$$

Indeed the derivative row sum is bounded by `2(2pi)^2 9^2 exp(2pi(2rho)9)`, which is below `10^4`; it already includes both columns. The gradient bound follows from the analogous first derivative expression. The interval `0<=s<=t_0=10^-10` is well inside the margin of the tube.

The analytic flow `Phi_s` has displacement at most `200s` for initial points in the tube of width `rho`, and derivative difference at most `2*10^4 s`. Its center map is `x_s(y)=(y+Phi_s(y))/2=y+q_s(y)`, with `||q_s||<=100s` and `||Dq_s||<=10^4s<=10^-6`. For every endpoint in the tube of width `rho/2`, the fixed-point equation `y=x-q_s(y)` maps its radius-`200s` polydisk into itself and is a contraction. The polydisk stays strictly inside the width-`rho` tube. This gives the required global analytic inverse, real on real endpoints and equivariant under integer shifts.

Define `xi_s=J(Phi_s-y)` and `H(x,xi)=-a(x-Jxi/2)`. The identities

$$
x_s-J\xi_s/2=\Phi_s(y),\qquad
x_s'=-J\nabla a(\Phi_s)/2=H_\xi,
\qquad\xi_s'=\nabla a(\Phi_s)=-H_x
$$

verify the Hamilton equations and their signs. The action integral in source (2.4) has endpoint variation `xi_s dot dx_s`: integrating the variation of `xi dot x'-H` by parts cancels the interior terms, and the initial momentum is zero. At a fixed final endpoint, time differentiation leaves `-H`. Thus

$$
\nabla S_s(x_s(y))=\xi_s(y),\qquad
\partial_sS_s(x)=a(x-J\nabla S_s(x)/2),\qquad S_0=0.
\tag{2.2}
$$

The action is single valued and periodic because the initial zero section and all flow quantities are equivariant under integer translations, while the action integrand is invariant. There is no assumed global generating function beyond this explicit short-time construction.

The displacement gives `||grad S_s||_infty<=200s`. The right-hand side of (2.2) differs from `a(x)` by at most `400*100s`, by the complex or real mean-value integral along the short segment. Integrating gives `||S_s-sa||_infty<=2*10^4s^2`. In particular the actual fixed phase has both Fourier coefficients in source (2.8) at least `t/250`: the smaller coefficient of `a` has modulus `1/200`, whereas `2*10^4t<=2*10^-6` throughout the certified interval. These are coefficients of the exact action, not a replacement by `ta` in an oscillatory exponential.

## 3. Transport and the order-`h` cancellation

Set `y_s=x-J grad S_s/2` and `V_s=J grad a(y_s)/2`. On the width-`rho/4` tube, Cauchy's estimate on `grad S_s`, initially bounded on width `rho/2`, gives each Hessian entry at most `8*10^5s`. Its row-sum norm is at most `1.6*10^6s<=1.6*10^-4`. Therefore `||Dy_s||<=2`, `||V_s||<=100`, and `||DV_s||<=10^4` there. Characteristics starting or ending on the width-`rho/8` tube stay inside the larger tube during the entire interval. The displacement is at most `10^-8`, much less than the available margin.

The transport equation

$$
\partial_s b_s=V_s\cdot\nabla b_s+\tfrac12(\operatorname{div}V_s)b_s,
\qquad b_0=1,
\tag{3.1}
$$

is solved along `x'=-V_s`. Its scalar multiplier is the exponential of the integral of `div V_s/2`. The complex bound `|div V_s/2|<=10^4` yields `|b_s|<2` on the common smaller strip. Cauchy then gives all required fixed derivative bounds. The solution is real and positive on the real torus and periodic. Its exact conservation law is `partial_s(b_s^2)=div(V_s b_s^2)`, hence `int b_s^2=1`.

For `F_(s,h)=b_s exp(iS_s/h)`, expand only the finitely many real shifts in (1.1). The leading phase is

$$
2\pi v\cdot x+\pi(Jv)\cdot\nabla S_s
=2\pi v\cdot y_s.
$$

The amplitude correction is `pi h(Jv) dot grad b_s`. The quadratic phase correction is `i pi^2 h S_s''[Jv,Jv]/2`. The Fourier first and second derivative identities give respectively

$$
-ihV_s\cdot\nabla b_s,
\qquad
-\frac{ih}{8}\operatorname{Tr}(S_s''J a''(y_s)J^T)b_s.
\tag{3.2}
$$

These verify both the sign and the factor `1/8` in source (3.4). Direct differentiation also gives

$$
\tfrac12\operatorname{div}V_s
=\tfrac18\operatorname{Tr}(S_s''J a''(y_s)J^T),
\tag{3.3}
$$

because `Tr(Ja'')=0` and `J^T=-J`. Equations (2.2), (3.1), and (3.3) cancel the terms of orders zero and one in the evolution equation.

All needed derivatives of `S_s,b_s` are uniformly bounded for `0<=s<=t_0`. Taylor's integral remainder is taken along real torus segments, so it remains valid even when a shift crosses a fundamental-domain boundary. The exponential remainders are bounded using a real phase, not an exponential of a large complex norm. The finite support makes the summed remainder uniformly `O(h^2)`. Thus

$$
\|\partial_sF_{s,h}-(i/h)(a\star_hF_{s,h})\|_\infty\le Ch.
\tag{3.4}
$$

This is a uniform residual for the exact finite-shift product, not a formal semiclassical ansatz without a norm estimate.

## 4. Exact matrix comparison in normalized HS norm

Apply `Q_N` to (3.4). The exact product (1.1) and the alias bound (1.3) give the normalized Hilbert–Schmidt residual at most `2Ch`. The initial value is exactly `Q_N(1)=I`. Left multiplication by `exp(isA_N/h)` is unitary on the Hilbert–Schmidt space, so the inhomogeneous Duhamel formula proves

$$
N^{-1/2}\|E_N-Q_N(b_te^{iS_t/h})\|_{\rm HS}\le C'h.
\tag{4.1}
$$

No operator-norm derivative of the oscillatory symbol is used. The comparison does not assume the approximate matrix is unitary. Every constant is fixed before `N`, the divisor, or a Weyl translation is chosen.

## 5. Uniform translation echo and removal of all nonzero aliases

Exact Weyl conjugation translates the ordinary symbol by `z=(a_0/N,-b_0/N)`. Let `Q=Q_N(F)` and `eta=N^-1/2||E_N-Q||_HS`. Then `N^-1/2||Q||_HS<=1+eta`. Hilbert–Schmidt Cauchy–Schwarz bounds the difference between the exact and approximate translation pairings by `eta(2+eta)`, uniformly in the unitary translation. Equation (4.1) therefore produces `O(N^-1)` in this normalized trace.

In the alias identity (1.4), the zero label gives

$$
\int b(x)b(x+z)e^{i(S(x+z)-S(x))/h}\,dx.
\tag{5.1}
$$

For a nonzero `m=(r,s)`, the phase divided by `2pi N` is

$$
S(x+z)-S(x+(s/2,r/2))-m\cdot x.
\tag{5.2}
$$

Choose a coordinate with `|m_j|=|m|_infty`. The two phase gradients have combined size less than `1/4`; hence the chosen derivative in (5.2) has magnitude at least `3|m|_infty/4`. Dividing by `|m|_infty` gives uniformly bounded fixed derivatives and a derivative uniformly separated from zero. The translated amplitudes have uniform fixed derivative bounds as well.

Repeated integration by parts yields `C_K(N|m|_infty)^-K`. The boundary terms vanish: the phase exponential has integer modulation `exp(-2pi iNm dot x)`, and its other factors and the integration-operator coefficients are periodic. The two half-period coordinates have only four residue choices, and no nonzero alias was discarded. For `K>2`, the sum over `m` converges uniformly and is `O(N^-K)`.

Thus the exact translation echo has the representation

$$
\frac1N\operatorname{Tr}(E_N^*TE_NT^*)
=\int b(x)b(x+z)e^{i(2\pi N)(S(x+z)-S(x))}\,dx+O(N^{-1}),
\tag{5.3}
$$

uniformly over all Weyl translations. This is precisely the representation that the separate oscillation lemma left as a condition; the present proof supplies it independently. There is no circular use of that lemma to construct `S` or the HS approximation.

## 6. Independent check of the raw analytic oscillation lemma

The lemma normalizes a translation by its centered distance `r` and direction `omega`. Its family

$$
F_{r,\omega}(x)=\int_0^1\omega\cdot\nabla S(x+ur\omega)\,du
$$

is continuous in every fixed smooth norm on the compact parameter set that includes `r=0`. At zero it is the directional derivative, not an undefined quotient. The two nonzero coordinate Fourier coefficients give a uniform nonconstant-mode lower bound: for centered coordinates, `|exp(2pi iz_j)-1|>=4|z_j|`, and at least one direction coordinate has modulus at least `1/sqrt(2)`.

No member is constant. If every positive-order derivative at a point vanished, analyticity would make that member locally constant and then constant on the connected torus. A finite subcover of parameter space times the torus therefore supplies one finite derivative order and one positive derivative lower bound everywhere. This is a valid compactness proof of uniform finite type; nonconstancy alone in a merely smooth class would not suffice.

The reduction of mixed derivatives to finitely many unit directions is an invertible Vandermonde calculation at directions proportional to `(1,j)`. Product neighborhoods with closures inside the derivative-bound sets support parameter cutoffs and smooth spatial cutoffs. Dividing by their positive total constructs a partition with uniform spatial derivative bounds; parameter smoothness or continuity of the chosen amplitudes is not required. Each resulting spatial ball can be sliced along its selected direction.

The one-dimensional estimate in the raw lemma was checked directly. If `|phi^(m)|>=c`, `m>=2`, then for `g=phi'`, `r=m-1`, separated measure-quantile points in the set `|g|<=eta` and the divided-difference mean-value theorem give its measure at most `C_r(eta/c)^(1/r)`. The calculation has the correct inequality direction: the derivative lower bound bounds the divided difference from below, and interpolation bounds it above by `2^r eta/(r!delta^r)`.

Rolle's theorem bounds the number of zeros of `g'` by `r-1`, so the complement can be split into at most `2r` monotone sign intervals. On each, integration by parts bounds the large-derivative part by `C/(nu eta)` times the amplitude's supremum and derivative integral. Taking `eta=c^(1/m)nu^(-(m-1)/m)` gives `C(c nu)^(-1/m)`. For `m=1`, a single integration by parts uses the fixed second-derivative upper bound and requires no monotonicity. The finite localization then proves the stated uniform `nu^-1/M` bound; bounded `nu` is handled by the absolute integral estimate.

Finally, the centered grid shell of maximum coordinate `k` has `O(k)` points and distance at least `k/d`. For `epsilon=1/M<=1<2`,

$$
d^{-2}\sum_{z\ne0}\operatorname{dist}(z,0)^{-\epsilon}
\le C d^{\epsilon-2}\sum_{k\le d/2+1}k^{1-\epsilon}\le C_\epsilon.
\tag{6.1}
$$

The constant is independent of the divisor; the `d=1` sum is empty. All hypotheses of this lemma hold for the exact `S_t` and the amplitudes `b(x)b(x+z)` in (5.3).

## 7. HS pinching for every square divisor

The pinching map is an orthogonal projection in Hilbert–Schmidt inner product. Its group-average identity therefore gives

$$
\sigma_{N,d}^2
=d^{-2}\sum_{z\in(d^{-1}\mathbb Z/\mathbb Z)^2}
\frac1N\operatorname{Tr}(E_N^*T_zE_NT_z^*).
\tag{7.1}
$$

The sign change in the second translation coordinate merely permutes this grid. Its identity term equals exactly `d^-2`, independently of the approximation. The remaining oscillatory terms are bounded using (5.3) and (6.1). The averaged `O(N^-1)` error stays `O(N^-1)` because the averaging weights sum to at most one; it does not acquire a factor `d^2`. Thus

$$
|\sigma_{N,d}^2-d^{-2}|\le CN^{-\epsilon},
\qquad
\sigma_{N,d}\le d^{-1}+CN^{-\epsilon/2}.
\tag{7.2}
$$

This proves Theorem 1 uniformly over every positive square divisor, including arbitrarily varying divisors and `d=1`. All constants and the exponent are fixed by the symbol and the original exact kick.

## 8. The mixed HS/operator estimate and the constant 24

Let `K=mathcal P_d(E_N)M_N`, `R=U_N-K`, with `||K||<=rho=1-g`, `0<g<=1/2`. Then `||K||_HS=sqrt(N)sigma` and `||R||<=2-g`.

For a word with `j<n` letters `R`, place one of its `K` factors in HS norm and all other factors in operator norm. The ideal property and `|Tr X|<=sqrt(N)||X||_HS` give

$$
|\operatorname{Tr}(\text{word})|/N
\le\sigma\rho^{n-j-1}(2-g)^j.
\tag{8.1}
$$

This holds at every placement; commutation or probabilistic independence is not used. The selected density satisfies `delta(g)<1`, so every retained word contains at least one `K`. The exact binomial estimate with `z_g=g/[2(2-g)]` gives

$$
|s_n|/N\le(\sigma/\rho)\eta^n,
\qquad\|S_n\|\le\eta^n,
\qquad\eta=\sqrt{1-g/2}.
\tag{8.2}
$$

The second inequality ensures `|s_n|/N<=1`. Since `|p_n|<=N`, the full square difference is bounded by `3|s_n|/N` after normalization. Summing and using `rho^-1<=2` and `(1-eta)^-1<=4/g` proves

$$
\frac1{N^2}\sum_{n\ge1}|w_{n,N}|
\big||p_n|^2-|p_n-s_n|^2\big|
\le24W\sigma/g.
\tag{8.3}
$$

The coefficient `24` is therefore correct. This includes the entire cross-term and gives absolute convergence of the difference series, even for bounded weights that do not decay. For pure powers `K^n`, (8.1) gives the stronger sum `3W sigma/g` because the geometric series starts with `rho^(n-1)`.

This step removes the need for an early-time cutoff. The new small quantity is `sigma/g`, rather than a condition involving `g log N` from the earlier purely geometric majorants.

## 9. The broad subpolynomial range

The growing-order theorem supplies escape `ell_N=exp[-C_3L^(1/3)log L]`, `L=log N`, under `log d>=C_2L^(2/3)`. The inequality `1-sqrt(1-x)>=x/2` permits

$$
g_N=\tfrac12\exp[-2C_3L^{1/3}\log L].
$$

It is positive and at most `1/2`, and the compression norm is at most `1-g_N`. Combining with (7.2) gives

$$
\frac{\sigma_{N,d}}{g_N}
\le C e^{-C_2L^{2/3}+2C_3L^{1/3}\log L}
 +C e^{-(\epsilon/2)L+2C_3L^{1/3}\log L}\longrightarrow0.
\tag{9.1}
$$

The limit is uniform over the allowed divisors. It remains valid though this inserted gap has `g_N log N` tending to zero. This proves the claimed extension beyond the previous failed geometric majorant.

The density asymptotic `delta(g)~g/[4log(4/g)]` follows by first-order expansion of `-log(1-g/2)` and the denominator. Hence `delta_N` tends to zero, while `log(1/delta_N)=O(L^(1/3)log L)=o(L)`. At times proportional to `N`, the permitted number of deviations is `N^(1-o(1))`. No fixed positive density is claimed.

## 10. Exact scope of the conclusion

For the compact-Fourier pair weight, (8.3) is the correction in the original pair factorial expression: positive and negative frequencies cancel its factor `1/2`, while the zero term and subtraction of `N` remain unchanged. For the Abel weight, the same theorem controls the complete infinite **difference series**, and hence every tail of that correction. It does not provide a uniform tail estimate for the original square-trace series alone.

The retained histories have not been compared with CUE. Their modified traces need not be traces of a unitary matrix. No higher-order factorial comparison, spectral countersequence, or sine-process limit is established by this theorem. The positive verdict covers the exact HS pinching and the stated removal of arithmetic histories, with these limits made explicit.
