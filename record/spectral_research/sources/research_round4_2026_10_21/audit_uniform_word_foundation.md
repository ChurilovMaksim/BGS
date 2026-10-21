> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round4_2026_10_21/audit_uniform_word_foundation.md`. Embedded SHA256: `3b9f422c7ba02c7b01da409eac17f2e1e06f4da30c4cceb0ba4f9867d21cb961`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the uniform commutator word and its finite torus descent

Date: 21 October 2026.

## 0. Verdict, claim card, and frozen inputs

**Primary verdict: proved as written, for the scoped operator estimates and the two escape theorems below.** No load-bearing gap was found. The argument was reconstructed from the three primary proof texts, without treating previous audit verdicts as premises.

The scoped claims are:

1. With the exact original Hamiltonian, fixed `tau=10^(-80)`, `h=(2pi N)^(-1)`, `t=tau/(2pi)`, and the threefold word `C_3` defined below,

   $$
   \|C_3(\delta)-e^{i\gamma Q_N(a_{qqqq})}\|
   \le 10^{12}\gamma\tau+10^{21}\gamma\delta,
   \quad \gamma=\tau N\delta^4,
   $$

   whenever `N` is odd, `0<=delta<=1`, and `N delta` is an integer.

2. For `N=d^2 m` odd, `m<=sqrt(N)`, `N>=10^140`, every input and output character of the exact subgroup `T_N(sN/d,uN/d)` satisfies

   $$
   \|P_\psi e^{i\tau N A_N}P_\chi\|
   \le \sqrt{4095/4096}.
   $$

3. For each fixed integer `r>=2`, there are constants `c_r>0,N_r` such that, for every odd `N=d^2m>=N_r` with `d>=N^(1/r)`, the same all-input/all-output estimate holds with `sqrt(1-c_r^2)`. The order `r` does not grow with `N`.

Audited primary sources:

| Source | SHA-256 |
|---|---|
| research_round3_2026_10_21/arithmetic_comb_fourth_difference_gap.md | 0b7bd5a0c21b79f1dd45d6b6377e58cd9f9afcdb8ed017199c874ace8e2fcc66 |
| research_round3_2026_10_21/arithmetic_comb_rescaled_gap.md | 898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f |
| research_round3_2026_10_21/arithmetic_comb_fixed_order_gap.md | e43296774f12851d7150e0d501afd1de76fd4feb11161e9f30692f1866cd1bf8 |

No source was modified. The trace-statistics conclusions beyond these operator inputs, the WKB/dispersive estimate, and the main `H_diag` conjecture are outside this audit. In particular this verdict does not certify a spectral limit.

## 1. Dependency graph and obligation matrix

The checked chain is

$$
\text{exact ordinary-half symbol}
\Longrightarrow \text{convergent Heisenberg series}
\Longrightarrow \text{bounded scaled brackets}
\Longrightarrow \text{finite prefix remainder}
\Longrightarrow \text{unitary Duhamel comparison}
\Longrightarrow \text{continuous finite Zak fibers}
\Longrightarrow \text{character compression and escape}.
$$

The fixed-order extension additionally uses the direct sine remainder, the ordinary Weyl product error, and a positive defect of a fixed smooth phase.

| Obligation | Status | Decisive check |
|---|---|---|
| Original modular half versus real half | passed | Direct multiplication of the scalar phases gives `(-1)^(kl)` |
| Exact Heisenberg equation with unbounded `P` | passed | Bounded `[P,A_h]`, graph-domain preservation, convergent operator series |
| Depth-four bracket budget | passed | Every nonzero bracket first reaches the periodic difference; four Fourier weights suffice |
| Prefix Taylor remainders when `s/h` is large | passed | New remainders contain original brackets only; outer operations are exact unitary conjugations |
| Quartic Lie coefficient and signs | passed | General formal induction gives degree four and positive `a_qqqq` |
| Finite torus descent | passed | Explicit unitary Zak map and continuous endpoint fibers |
| Numerical constant `1/64` | passed | Fixed permitted lattice rescaling and spectral inequality on `[-2,2]` |
| Arbitrary fixed derivative order | passed | Finite prefix count and finite smooth norms, with no uniformity in `r` asserted |
| `exp(iQ(G))` versus `Q(exp(iG))` | passed | Inhomogeneous Duhamel equation and exact product defect `O(h)` |
| Positive phase defect and aliases | passed | Nonzero Fourier coefficient at `(7,0)`; all nonconstant surviving compression frequencies are in the tail |
| All input and output characters | passed | Independent scalar normalizations cancel in the group commutator |
| `H_diag` or full Heisenberg-time trace cancellation | out of scope | Neither follows from this operator audit |

The computations used in the audit only evaluate source hashes and finite binomial coefficients. No numerical propagation, extrapolation in `N`, or agreement with an earlier reviewer is used as evidence for a uniform remainder.

## 2. Reconstruction of the exact symbol and Weyl product

On the line, use

$$
(W_h(k,l)u)(q)=e^{2\pi i k(q+l/(2N))}u(q+l/N),
\qquad h=(2\pi N)^{-1}.
$$

Its value on the zero finite torus fiber is

$$
W_N(k,l)=(-1)^{kl}T_N(l,k).
$$

Indeed the modular inverse of two in an odd modulus may be represented by `(N+1)/2`, whose excess over the real half contributes `exp(pi i kl)=(-1)^(kl)`. Thus the symbol of the original matrix is exactly

$$
\begin{aligned}
a(q,p)={}&\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}-\frac1{10}\\
&+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
\end{aligned}
$$

The shift in the mixed term multiplies its coefficients, where `l=+/-1`, by `(-1)^k`, as required. The support has `|k|+|l|<=9`; the Fourier one-norm is less than two.

Multiplying two line Weyl modes directly gives

$$
W_h(k,l)W_h(k',l')
=e^{2\pi^2 i h(lk'-kl')}W_h(k+k',l+l').
$$

Consequently, for `omega=lk'-kl'`, the symbol multiplier in
`(-i/h)[Q_h(a),Q_h(b)]` is

$$
\frac2h\sin(2\pi^2h\omega),
\qquad
\left|\frac2h\sin(2\pi^2h\omega)\right|
\le4\pi^2|\omega|.
$$

The sign agrees with the multiplier of `a_q b_p-a_p b_q`. The product identity remains exact on the finite fiber when integer frequencies alias. One must retain the integer-label definition `W_N(k,l)=(-1)^(kl)T_N(l,k)`; the audit never replaces it by a frequency-periodic real-half convention.

## 3. Domain control and the convergent Heisenberg series

Let `A_h=Q_h(a)` and `P=-ih partial_q`. The bounded operator `A_h` preserves `Dom P`, and

$$
[P,A_h]=-ihQ_h(a_q)
$$

is bounded. Preservation of `Dom P` by `E_h(s)=exp(isA_h/h)` can be seen without a propagation theorem: the commutator formula for `A_h^m` gives a convergent exponential series in the graph norm of `P` for each fixed `h,s`. The graph-norm constants need not be uniform in `h`; they only justify the identities on the common domain and are not used in any subsequent norm estimate.

Differentiating on that domain yields

$$
E_h(t)^*PE_h(t)-P
=\int_0^t E_h(s)^*Q_h(a_q)E_h(s)\,ds.
$$

The right side is bounded. Define `L_h` by the exact scaled commutator above. The support of `L_h^n a_q` is in radius `9(n+1)`. At the next step its Fourier one-norm costs at most

$$
40\cdot9\cdot9(n+1)\cdot2<7000(n+1).
$$

The initial derivative costs less than `120`. Therefore

$$
\|L_h^n a_q\|_0\le120\,7000^n n!.
$$

An additional Fourier weight of order `K` costs at most `10^K(n+1)^K`. Thus

$$
v_h=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}L_h^n a_q
$$

converges in every fixed weighted Fourier norm, uniformly in `h`. Its derivative series converges in operator norm for `|t|<1/7000` on compact subintervals. It solves the exact bounded-operator Heisenberg equation. Uniqueness for each fixed `h` identifies it with the actual conjugation in the integral identity. Hence

$$
E_h^*PE_h=P+Q_h(v_h)
$$

is an equality of self-adjoint operators on `Dom P`, with bounded difference. This use of uniqueness does not import an `exp(C/h)` loss into the symbol estimates.

Set

$$
H_0=-P,\qquad H_1=-P-Q_h(v_h).
$$

Both are self-adjoint on `Dom P`. Their exponentials preserve that domain. Every periodic symbol encountered below is smooth with all Fourier weights summable, so its commutators with `P` of every fixed required order are bounded. The single-conjugation Taylor formulas can therefore be proved on `Dom P` and extended as bounded differences; equivalently one may work on the common invariant Schwartz core.

## 4. The numerical bracket budget

For

$$
\|b\|_K=\sum_{k,l}|\widehat b(k,l)|(1+|k|+|l|)^K,
$$

the product weight inequality and the sine bound give

$$
\|h^{-1}[Q_h(b),Q_h(c)]\|_K
\le40\|b\|_{K+1}\|c\|_{K+1}.
$$

The left side denotes the norm of its exact commutator symbol. No factors `2pi` are concealed in this definition. A derivative costs at most `2pi` and one Fourier weight.

For `0<=K<=4` and `|t|<=10^(-12)`, the series above gives

$$
\|v_h\|_K\le240\,10^K|t|.
$$

The geometric parameter is at most `7*10^(-9)`, so the polynomial factor `(n+1)^(K-1)` leaves a sum less than two. A scaled commutator with either `H_0` or `H_1`, acting on a periodic symbol in norm of weight at most three, consequently costs at most `7` and one weight:

$$
2\pi+40\cdot240\cdot10^4\cdot10^{-12}<7.
$$

Every nonzero mixed bracket first brackets the two different generators and produces one derivative of `v_h`. Thus any original mixed scaled bracket of depth four has norm at most

$$
7^3\cdot2\pi\cdot240\cdot10^4|t|<10^{12}|t|.
$$

Brackets whose first pair consists of the same generator vanish, so the same bound covers them.

For the leading term, summing the series from its first nonlinear term gives

$$
\|\partial_q^3(v_h-ta_q)\|_0
\le120\,60^3|t|\sum_{n\ge1}(n+1)^2(7000|t|)^n
\le2\cdot10^{12}t^2.
$$

The constants therefore suffice exactly in the stated parameter range.

## 5. Independent finite prefix remainder calculation

Write `R(s)=exp(isH_0/h)`, `B(s)=exp(isH_1/h)`, and

$$
C_0=B,\qquad C_{j+1}=RC_jR^{-1}C_j^{-1}.
$$

For `C_3`, the word has 22 factors: fourteen of type `R` and eight of type `B`, counting inverses. Its logarithmic generator

$$
\mathcal A(s)=\frac h i C_3'(s)C_3(s)^*
$$

is a sum of 22 signed generators, each conjugated by the preceding prefix of length `p=0,...,21`.

For `F=H_j`, or any of the already formed original scaled brackets, the integral Taylor formula is

$$
\operatorname{Ad}_{e^{\epsilon isH/h}}F
=\sum_{a=0}^{L-1}\frac{(\epsilon s)^a}{a!}
\left(\frac i h\operatorname{ad}_H\right)^aF
+\mathcal R_L(s),
\qquad
\|\mathcal R_L(s)\|\le |s|^L M_L/L!.
$$

For an initially unbounded `F`, the zero-order term is kept on the common domain; the first commutator and every remainder are bounded. The signed zero-order sum cancels because the group word has separately zero exponent sums in `R` and `B`.

Expand each prefix from its innermost, rightmost conjugation towards the left. If a retained term has degree `j<=3`, expand the next single conjugation with remainder order `4-j`. Every new remainder then has exactly four original scaled brackets, multiplied by `s^4`. Previously formed remainders are not differentiated: the remaining prefix conjugates them exactly, preserving their operator norm.

The following direct count makes the finite budget explicit. After `m-1` inner conjugations, the number of retained multiindices of total degree at most three is

$$
\binom{m+2}{3}.
$$

The next conjugation creates at most one remainder for each of them. A prefix of length `p` therefore creates at most

$$
\sum_{m=1}^p\binom{m+2}{3}=\binom{p+3}{4}
$$

remainders. Summing over all 22 differentiated factors gives at most

$$
\sum_{p=1}^{21}\binom{p+3}{4}=\binom{25}{5}=53130
$$

remainder slots. Each retained Taylor coefficient has modulus at most one on `|s|<=1`. Thus the source's coarser bound `22*21*binomial(24,3)=935088<10^8` is safely sufficient, and its resulting bound

$$
\|\mathcal R_h(s)\|\le10^{20}|t||s|^4
$$

has ample margin. The count is not a truncation of a norm-convergent exponential series in `s/h`.

To identify the retained finite polynomial, work in the formal free associative algebra. If
`C(s)=I+s^j Z+O(s^(j+1))`, then

$$
e^{sX}C(s)e^{-sX}C(s)^{-1}
=I+s^{j+1}[X,Z]+O(s^{j+2}).
$$

Starting with `C_0=e^(sY)` proves the leading term
`s^4 ad_X^3 Y` for `C_3`. Therefore its already justified logarithmic-generator polynomial is

$$
\mathcal A(s)=4s^3K_h+\mathcal R_h(s),
\qquad
K_h=\left(\frac i h\right)^3
[H_0,[H_0,[H_0,H_1]]]
=Q_h(\partial_q^3v_h).
$$

The signs can be checked successively: the scaled first bracket is `Q(v_q)`, the next is `-Q(v_qq)`, and the third is `Q(v_qqq)`.

Both `C_3(s)` and `exp(is^4 K_h/h)` are unitary. Their inhomogeneous comparison consequently gives

$$
\|C_3(\delta)-e^{i\delta^4K_h/h}\|
\le\frac1h\int_0^\delta\|\mathcal R_h(s)\|\,ds
\le\frac{10^{20}|t|\delta^5}{5h}.
$$

This is valid even when `delta/h` is large. No factor `exp(C/h)` appears because the comparison propagators are unitary. The only displayed division by `h` is the one in the Duhamel integral.

## 6. Exact Zak descent, including signs and normalization

For a Schwartz function initially, define

$$
(Z\psi)(\alpha,\beta)_j
=N^{-1/2}\sum_{n\in\mathbb Z}e^{-2\pi in\alpha}
\psi((j+\beta)/N+n),\quad 0\le j<N.
$$

Parseval in `alpha` removes the cross terms in `n`. The factor `N^(-1)` is then cancelled by `d beta=N dq` on each interval. Summation over `j,n` partitions the entire real line. Thus

$$
\int_0^1\int_0^1\sum_j |Z\psi|^2\,d\alpha\,d\beta
=\|\psi\|_{L^2(\mathbb R)}^2.
$$

Inverse Fourier series in `alpha`, followed by the same interval partition, reconstruct every square-integrable fiber section. The map is therefore unitary onto the direct integral of `C^N` fibers.

Write `j+l=r+Nm`, with `0<=r<N`. Direct substitution yields

$$
(W_h(k,l)_{\alpha,\beta}u)_j
=e^{2\pi i k(j+\beta+l/2)/N}e^{2\pi im\alpha}u_r.
$$

The positive sign in `exp(2pi i m alpha)` follows by replacing the summation index `n` by `n+m`. These finite unitary matrices are continuous on the parameter rectangle. At `(alpha,beta)=(0,0)` they equal exactly `(-1)^(kl)T_N(l,k)`.

Every symbol used in the proof has an absolutely convergent Fourier series. Since every mode has norm one on every fiber, its matrix series converges uniformly in the fiber variables. Its bounded exponentials are also continuous. At the endpoint `N delta` integral, `R(delta)=W_h(0,-N delta)` is decomposable with continuous finite fibers; hence so is the entire endpoint word.

The norm of a decomposable operator is the essential supremum of its fiber norms. A line bound therefore holds almost everywhere in the fiber parameters, and continuity extends it to the zero fiber, including the boundary point `(0,0)`. No restriction to distributional comb vectors has been made.

The intermediate real parameter `s` need not preserve the zero fiber. All differentiation was performed on the line with `h,t` fixed; decomposability is required only for the endpoint inequality.

Combining the word bound with the leading-symbol estimate gives, with `gamma=t delta^4/h=tau N delta^4`,

$$
\begin{aligned}
\|C_3(\delta)-e^{i\gamma Q_N(a_{qqqq})}\|
&\le\frac{10^{20}}5\gamma\delta
+2\cdot10^{12}\gamma |t|\\
&\le10^{21}\gamma\delta+10^{12}\gamma\tau.
\end{aligned}
$$

The main exponential was retained intact, so no `gamma^2` error needs to be small in this statement.

## 7. Numerical gap and the all-character conclusion

The frequencies `(7,0)` and `(-7,0)` have coefficient `9/20` in the symbol `a`. Hence for `g=a_qqqq`,

$$
\sigma\ge\frac9{10\sqrt2}(14\pi)^4>2\cdot10^6.
$$

The explicit trigonometric expansion in the source bounds

$$
\|g\|_{\mathcal F}\le\frac{505319}{200}(2\pi)^4
<11\cdot10^6.
$$

Both are sufficiently coarse to be verified using elementary bounds on `pi`; no decimal numerical fit is needed.

The subgroup `H_d(s,u)` is an exact abelian representation since `(N/d)^2=Nm`. Its nonidentity elements have trace zero, which proves that every character projection has rank `m`. A Weyl mode changes the two characters by factors `e_d(k)` and `e_d(-l)`. Thus its compression vanishes unless both coordinates are divisible by `d`.

For `d>18`, the support differences in `Q_N(g)^*Q_N(g)` have only the zero frequency divisible by `d` in both coordinates. Its constant coefficient is `sigma^2`, giving exactly

$$
P_\chi Q_N(g)^*Q_N(g)P_\chi=\sigma^2P_\chi.
$$

For `b_0=2*10^18`, choose

$$
b=\lfloor b_0dN^{-1/4}\rfloor,\qquad\delta=b/d.
$$

The assumptions give `d>=N^(1/4)`, and hence

$$
0.99/6250000\le\gamma_N=\tau N\delta^4\le1/6250000,
\qquad N\delta=bdm\in\mathbb Z.
$$

For `N>=10^140`, `delta<=2*10^(-17)`, and the word error is at most

$$
1.6\cdot10^{-75}+2/625<1/250.
$$

Also `gamma_N ||Q_N(g)||<44/25<2`. The spectral inequality
`|exp(ix)-1|>=5|x|/6` on `[-2,2]` now gives, for every unit vector in any input character space,

$$
\|(e^{i\gamma_NQ_N(g)}-I)v\|>33/125,
\qquad
\|(C_3-I)v\|>13/50.
$$

Fix any output character `psi` and let `epsilon=||(I-P_psi)E_Nv||`. The translation `R` acts on the input and output spaces by scalars `r_chi,r_psi` of modulus one. Then

$$
(R/r_\chi)v=v,
\qquad
\|(E_N^*RE_N/r_\psi-I)v\|\le2\epsilon.
$$

The same bound holds for the inverse normalized `B`. Independent scalar multipliers of `R` and `B` cancel in the first group commutator, and therefore in every later one. Telescoping all factors gives `||(C_3-I)v||<=16 epsilon`. Thus

$$
\epsilon>13/800>1/64,
$$

which proves the numerical all-input/all-output estimate by unitarity. The scalar normalizations are different for input and output; the argument does not silently assume `chi=psi`.

## 8. Arbitrary fixed order: no hidden exponential loss

For fixed `r>=2`, every required Fourier seminorm of `v_h` is bounded by `V_r|t|`, uniformly in `h` and `|t|<=10^(-12)`. A nonzero original bracket of depth `r` is therefore bounded by a finite constant times `|t|`, for example by

$$
2\pi V_r(2\pi+40V_r10^{-12})^{r-1}|t|.
$$

The word has `L_r=3*2^(r-1)-2` factors. The preceding prefix argument, retaining degree at most `r-1`, creates only original depth-`r` brackets in its new remainders. The same multiindex count gives a finite upper bound

$$
\sum_{p=1}^{L_r-1}\binom{p+r-1}{r}
=\binom{L_r+r-1}{r+1}.
$$

This is bounded by the larger finite count used in the source. Formal induction identifies the leading generator:

$$
\frac h i C_{r-1}'(s)C_{r-1}(s)^*
=rs^{r-1}K_{r,h}+O_r(|t||s|^r),
$$

$$
K_{r,h}=\left(\frac i h\right)^{r-1}
\operatorname{ad}_{H_0}^{r-1}H_1
=(-1)^r Q_h(\partial_q^{r-1}v_h).
$$

Unitary comparison gives `O_r(|t|delta^(r+1)/h)`. With

$$
\delta=\lfloor dN^{-1/r}\rfloor/d,
\qquad \beta=N\delta^r\in[2^{-r},1],
$$

the factor `delta^r/h=2pi beta` is bounded. Thus this error is `O_{r,tau}(delta)`, rather than an exponential in `1/h`.

The sine remainder is exactly

$$
\left|\frac2h\sin(2\pi^2h\omega)-4\pi^2\omega\right|
\le\frac83\pi^6h^2|\omega|^3.
$$

In a telescoped difference of `L_h^n` and `L_0^n`, an exceptional bracket at position `j` has input support radius at most `9j`, so its additional cost relative to the original `7000j` majorant is at most `10^6 h^2 j^2`. Summing positions costs at most `10^6h^2 n^3`. Extra fixed Fourier weights only add a polynomial in `n`. Summing the convergent series therefore proves

$$
\|v_h-v_0\|_s=O_s(h^2t^2)
$$

for every fixed `s`. This independently checks the fixed smooth phase

$$
G_{r,\beta}=2\pi\beta(-1)^r\partial_q^{r-1}v_0.
$$

There is no first-order truncation in `tau` after taking these high derivatives. The first-order estimate is used only to certify a single nonzero Fourier coefficient of the undifferentiated `v_0`.

## 9. Audit of the bounded exponential versus the quantized phase

The ordinary Weyl multiplication law gives directly

$$
\|Q_h(b)Q_h(c)-Q_h(bc)\|
\le2\pi^2h\|b\|_1\|c\|_1.
$$

This holds on the line and on each finite fiber, including all aliases. Set
`Y(u)=exp(iuQ_h(G))` and `F(u)=Q_h(exp(iuG))`. Their difference satisfies an inhomogeneous equation with homogeneous generator `iQ_h(G)` and forcing

$$
i\bigl(Q_h(G)Q_h(e^{iuG})-Q_h(Ge^{iuG})\bigr).
$$

The homogeneous propagator is unitary. The matrix `F(u)` itself need not be unitary; no such assertion is needed. The forcing norm is `O(h)` uniformly for `u in [0,1]` and `beta in [2^(-r),1]`, because `G` is real and its required smooth norms are bounded on this compact parameter set. Summable weighted Fourier norms of `exp(iuG)` follow from a fixed number of integrations by parts.

Integration therefore gives

$$
e^{iQ_N(G_{r,\beta})}
=Q_N(e^{iG_{r,\beta}})+O_{r,\tau}(h).
$$

Combining this with the previous word and symbol estimates proves the source's

$$
C_{r-1}(\delta)=Q_N(e^{iG_{r,\beta}})+O_{r,\tau}(\delta+h).
$$

All constants can depend on fixed `r,tau`; none depends on `N,d,chi,psi,beta`. Large values of a fixed phase `G` cause large but finite smooth constants and do not produce a hidden `exp(C/h)`.

## 10. Positive defect, smooth compression, and final fixed-order gap

The convergent classical series gives

$$
\widehat v_0(7,0)=t\,63\pi i/10+O(2\cdot10^6t^2)\ne0.
$$

For each fixed `r` this coefficient remains nonzero after `r-1` derivatives. Hence every real `G_{r,beta}` is nonconstant. The equation `exp(iG)=1` everywhere on the connected torus would force `G` into one constant element of `2pi Z`. This is impossible. The continuous function

$$
\beta\longmapsto\int|e^{iG_{r,\beta}}-1|^2
$$

is strictly positive at every point of a compact interval; its minimum `mu_r` is therefore positive.

For every fixed smooth symbol `f`, the exact character selection rule gives

$$
\left\|P_\chi Q_N(f)P_\chi-\left(\int f\right)P_\chi\right\|
\le\sum_{|k|+|l|\ge d}|\widehat f(k,l)|
\le d^{-1}\|f\|_1.
$$

The tail includes all nonzero frequencies that can alias; none is discarded by assuming an injective infinite Fourier expansion. Apply this to `f=|exp(iG)-1|^2` and use the product defect to obtain

$$
\|Q_N(e^{iG}-1)v\|^2
\ge\mu_r-O_{r,\tau}(h+d^{-1}).
$$

The preceding word comparison then gives

$$
\|(C_{r-1}-I)v\|\ge\frac12\sqrt{\mu_r}
$$

above one threshold `N_r`, uniform over all permitted divisors and characters. There are exactly `2^(r-1)` normalized `B` factors, each with residual at most `2epsilon`. Telescoping yields

$$
\epsilon\ge2^{-(r+1)}\sqrt{\mu_r}=c_r>0.
$$

The exact covariance of `M_N` permutes the character spaces, so the same gap applies to `U_N` between all input/output character pairs. No primality assumption was introduced.

## 11. Scope, remaining gap, and provenance

The numerical and fixed-order escape bounds pass this focused audit. The large auxiliary step is legal, the original `tau` is unchanged, the scaled remainder remains uniform when `s/h` diverges, the zero Zak fiber is the correct modular quantization, and the fixed-order bounded-exponential replacement is justified by a direct equation.

There is no missing implication within the scoped chain. The next unproved implication relevant to the main research goal remains a signed, fully coherent trace-correlation estimate at times of order `N`. Neither a character-block norm gap nor this proof of that gap supplies such an estimate.

This is an independent reconstruction by the present audit agent from the frozen primary sources. Previous audit files were not used as mathematical premises. The binomial count was also evaluated exactly in Python (`53130`, against the source's safe bound `935088`), and the three SHA-256 values above were read from the actual files. The finite computation verifies only that integer arithmetic; the uniform asymptotic estimates are proved analytically above.
