> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/arithmetic_comb_fixed_order_gap.md`. Embedded SHA256: `e43296774f12851d7150e0d501afd1de76fd4feb11161e9f30692f1866cd1bf8`.
> [Thematic guide](../../topics/arithmetic.md).

# Fixed-order quantum differences exclude all polynomially growing character combs

Date: 21 October 2026. Original fixed `tau=10^(-80)` throughout.

## 0. Theorem and quantifiers

For every fixed integer `r>=2` there are constants `c_r>0` and `N_r`
with the following property. If `N=d^2m` is odd, `N>=N_r`, and
`d>=N^(1/r)`, then for every pair of characters `chi,psi` of the exact
Weyl subgroup

$$
H_d(s,u)=T_N(sN/d,uN/d),\qquad (s,u)\in(\mathbb Z/d\mathbb Z)^2,
$$

its rank-`m` character projections satisfy

$$
\boxed{
\|P_\psi E_NP_\chi\|\le\sqrt{1-c_r^2}<1,
\qquad E_N=e^{i\tau N A_N}.
}
\tag{0.1}
$$

Equivalently, every unit vector initially in any one character space
has norm at least `c_r` outside every chosen output character space
after the actual kick. The same estimate holds with `U_N` in place
of `E_N`, because `M_N` exactly permutes the input characters.

Thus, for every fixed `eta>0`, all square divisors with `d>=N^eta`
are covered by choosing one fixed integer `r` with `1/r<=eta`.
The corresponding ranks satisfy `m<=N^(1-2eta)`.
The integer `r` is not allowed to grow with `N`. No assertion is made
here for arbitrary subpolynomial `d=N^(o(1))`.

The constants are constructed from a fixed, explicit smooth function:

$$
c_r=2^{-(r+1)}\sqrt{\mu_r},\qquad
\mu_r=\min_{\beta\in[2^{-r},1]}
\int_{\mathbb T^2}|e^{iG_{r,\beta}(q,p)}-1|^2\,dq\,dp>0.
\tag{0.2}
$$

Both the definition of `G` and the strict positivity of `mu_r` are
proved below. They are not hypotheses. A separate rescaling of the
quartic case gives the stronger explicit constant `c_4=1/64` in the
range `d>=N^(1/4)`, `N>=10^140`; the present theorem supplies the
extension to every fixed polynomial growth exponent.

## 1. Exact symbol and convergent quantum and classical series

Use

$$
h=(2\pi N)^{-1},\quad t=\tau/(2\pi),\quad
Q_N(e^{2\pi i(kq+lp)})=(-1)^{kl}T_N(l,k).
$$

The actual Hamiltonian is `A_N=Q_N(a)` for

$$
\begin{aligned}
a(q,p)={}&\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}-\frac1{10}\\
&+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100}.
\end{aligned}
\tag{1.1}
$$

Its Fourier support has `|k|+|l|<=9`, coefficient one-norm less than
two, and coefficients `a_(7,0)=a_(-7,0)=9/20`.
On the line let `P=-ih partial_q`, `A_h=Q_h(a)`, and
`E_h=exp(it A_h/h)`.

For the weighted Fourier norm

$$
\|b\|_s=\sum_{k,l}|\widehat b(k,l)|(1+|k|+|l|)^s,
$$

define `L_h` by
`Q_h(L_h b)=(-i/h)[A_h,Q_h(b)]`.
Its pairwise Fourier multiplier is

$$
\frac2h\sin(2\pi^2h\omega),\qquad
\omega=lk'-kl',
\qquad
\left|\frac2h\sin(2\pi^2h\omega)\right|\le4\pi^2|\omega|.
\tag{1.2}
$$

Let `L_0 b={a,b}=a_q b_p-a_p b_q`, whose Fourier multiplier is
`4pi^2 omega`. For either `L_h` or `L_0`, elementary induction yields

$$
\|L_h^n a_q\|_0\le120\,7000^n n!,\qquad
\operatorname{supp}\widehat{L_h^n a_q}
\subset\{|k|+|l|\le9(n+1)\}.
\tag{1.3}
$$

The next bracket at step `j` costs less than `7000j`; the initial
derivative has one-norm less than `120`. Consequently

$$
v_h(t)=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}L_h^n a_q,
\qquad
v_0(t)=\sum_{n\ge0}\frac{t^{n+1}}{(n+1)!}L_0^n a_q
\tag{1.4}
$$

converge in every fixed weighted Fourier norm, uniformly in `h`.
Indeed an extra weight of order `s` costs at most
`10^s(n+1)^s`, and the remaining series has geometric parameter
`7000|t|<10^(-76)`. The same argument with a small fixed exponential
Fourier weight proves analyticity. Each series is real-valued.

The first series is the actual quantum Heisenberg series, rather
than an expansion in `h`: for each fixed `h`, its quantization solves
the unique bounded-operator Heisenberg equation. Integration of the
bounded commutator with `P` gives exactly

$$
E_h^*PE_h=P+Q_h(v_h).
\tag{1.5}
$$

We also need its classical limit with arbitrary fixed differentiability.
The sine remainder gives

$$
\left|\frac2h\sin(2\pi^2h\omega)-4\pi^2\omega\right|
\le\frac83\pi^6h^2|\omega|^3.
\tag{1.6}
$$

Telescope the difference `L_h^n-L_0^n`. At the exceptional bracket
number `j`, the right side of (1.6) is at most `10^6 h^2 j^2`
times the `7000j` majorant used in (1.3). Summing those positions
adds at most `10^6 h^2 n^3` to that majorant. Extra Fourier weights
cost only another fixed power of `n+1`. Thus (1.4) gives, for every
fixed `s`,

$$
\boxed{\|v_h-v_0\|_s\le C_s h^2t^2.}
\tag{1.7}
$$

The constants are finite and independent of `h,N,d`. This follows
from a convergent geometric series times a polynomial, and does not
need a semiclassical propagation theorem at a growing time.

One Fourier coefficient will exclude a constant limiting phase.
Equation (1.3), summed from `n=1`, gives

$$
\|v_0-t a_q\|_0\le2\cdot10^6t^2,
\qquad
\widehat{a_q}(7,0)=\frac{63\pi i}{10}.
\tag{1.8}
$$

For the given positive `t`, (1.8) proves
`|vhat_0(7,0)|>t>0`. This is a fixed explicit nonzero coefficient.

## 2. The general finite-word remainder

Put

$$
H_0=-P,\qquad H_1=-E_h^*PE_h=-P-Q_h(v_h),
\quad R(s)=e^{isH_0/h},\quad B(s)=e^{isH_1/h}.
$$

Define `C_0(s)=B(s)` and

$$
C_{j+1}(s)=R(s)C_j(s)R(s)^*C_j(s)^*,\qquad 0\le j<r-1.
\tag{2.1}
$$

The word `C_(r-1)` has `L_r=3*2^(r-1)-2` factors, of which exactly
`2^(r-1)` are `B` or its inverse.

All mixed scaled commutators of depth `r` of `H_0,H_1` are bounded
uniformly in `h` by `M_r<=C_r|t|`. Here is an explicit finite-norm
justification at arbitrary fixed `r`. From (1.3)–(1.4),
`||v_h||_r<=V_r|t|` for a finite constant `V_r`, uniformly for
`|t|<=10^(-12)`. A scaled commutator with `-P` differentiates a
symbol, costing at most `2pi` and one Fourier weight. A scaled
commutator with `Q_h(v_h)` costs at most
`40||v_h||_(s+1)||b||_(s+1)` in norm of weight `s`, by (1.2).
The first nonzero mixed bracket is one derivative of `v_h`.
It follows, for example, that

`M_r <= 2pi V_r (2pi+40 V_r 10^(-12))^(r-1) |t|`.

This may be large when `r` is large, but is finite for every fixed
`r`, which is the quantifier in the theorem.

Consider the left logarithmic generator

$$
\mathcal A_r(s)=\frac h i C_{r-1}'(s)C_{r-1}(s)^*.
$$

Differentiate the finite word. Every term is a signed `H_0` or `H_1`
conjugated by a prefix. Expand prefix conjugations from right to left,
retaining total degree at most `r-1` in `s`. A remainder arising
after degree `j` uses `r-j` additional brackets and therefore has
total original bracket depth exactly `r`. Any subsequent prefix
factors transport it unitarily without increasing its norm.
There are only finitely many such terms; for instance
`L_r^2 binomial(L_r+r,r)` is a sufficient bound for their number.
Thus the total remainder is bounded by `C_r M_r |s|^r` on `|s|<=1`.

The coefficients of this justified finite Taylor polynomial are
universal Lie coefficients. Inducting on the commutators gives

`C_(r-1)(s)=I+s^r ad_X^(r-1)Y+O(s^(r+1))`

as a formal identity, where `X=iH_0/h,Y=iH_1/h`. This identifies
the already bounded-generator polynomial; it does not assume an
operator-norm exponential series for unbounded generators. Therefore

$$
\mathcal A_r(s)=r s^{r-1}K_{r,h}+O_r(|t|\,|s|^r),
\qquad
K_{r,h}=\left(\frac{i}{h}\right)^{r-1}
\operatorname{ad}_{H_0}^{r-1}H_1
=(-1)^rQ_h(\partial_q^{r-1}v_h).
\tag{2.2}
$$

Unitary Duhamel comparison with `exp(i s^r K_(r,h)/h)` now gives

$$
\boxed{
\|C_{r-1}(\delta)-e^{i\delta^rK_{r,h}/h}\|
\le C_r |t|\delta^{r+1}/h,
\qquad0\le\delta\le1.
}
\tag{2.3}
$$

All domain statements are first on the common invariant Schwartz core.
After the first bracket the operators in the Taylor differences are
bounded, so the displayed remainders extend to the whole line space.
The common unbounded linear parts cancel in the logarithmic generator.
The method requires neither high-frequency Egorov nor an unspecified
Fourier integral amplitude.

## 3. Exact torus descent and the fixed smooth limiting phase

Choose

$$
b=\lfloor dN^{-1/r}\rfloor\ge1,\qquad
\delta=b/d,\qquad\beta=N\delta^r.
\tag{3.1}
$$

Then `delta<=N^(-1/r)` and `beta in [2^(-r),1]`, because
`floor x>=x/2` for `x>=1`. Furthermore `Ndelta=bdm` is an integer.
At this endpoint `R(delta)=T_N(-bN/d,0)` on the exact odd torus fiber.

The finite-fiber implication can be verified by the same explicit Zak
decomposition as for the quartic word:

$$
(Z\varphi)(\alpha,\zeta)_j
=N^{-1/2}\sum_{n\in\mathbb Z}e^{-2\pi in\alpha}
\varphi((j+\zeta)/N+n),\qquad0\le j<N.
\tag{3.2}
$$

Parseval and partition of the line show that this is unitary onto
the direct integral of `C^N` fibers. If `j+l=u+Nv`, the integer
Weyl mode has the continuous fiber matrix

`(W_h(k,l)_(alpha,zeta) z)_j`
`=exp(2pi i k(j+zeta+l/2)/N) exp(2pi i v alpha) z_u`.

At `(alpha,zeta)=(0,0)` this is exactly
`(-1)^(kl)T_N(l,k)`. All Fourier symbols here have absolutely
convergent series, so their fibers and bounded exponentials are
continuous. Since `Ndelta` is an integer, the complete endpoint
word also has continuous fibers. The norm of a decomposable operator
is the essential supremum of its fiber norms; continuity extends a
line bound to every fiber. Thus (2.3) holds for the exact finite
matrices. The intermediate real parameter never needs to preserve
the chosen fiber.

Define

$$
G_{r,\beta}(q,p)=2\pi\beta(-1)^r
\partial_q^{r-1}v_0(t;q,p).
\tag{3.3}
$$

Equations (1.7), (2.3), and `delta^r/h=2pi beta` imply

$$
C_{r-1}(\delta)=e^{iQ_N(G_{r,\beta})}+O_r(\tau\delta+h^2t^2).
\tag{3.4}
$$

To replace its bounded exponential by a quantized ordinary function,
the exact Weyl product gives, for weighted Fourier norms,

$$
\|Q_h(b)Q_h(c)-Q_h(bc)\|
\le2\pi^2h\|b\|_1\|c\|_1.
\tag{3.5}
$$

This follows directly from
`|exp(2pi^2 i h omega)-1|<=2pi^2h|omega|`.
Compare `Q_h(exp(iuG))` with `exp(iuQ_h(G))` for `0<=u<=1`.
Their differential equations differ by the product error (3.5);
unitary Duhamel bounds its integral by `O_r(h)`.
The Fourier norms involved are uniformly bounded for
`beta in [2^(-r),1]`: `G` is fixed and smooth, and the interval is
compact. Repeated integration by parts in Fourier coefficients
supplies every required summable weight. Consequently

$$
\boxed{
C_{r-1}(\delta)=Q_N(e^{iG_{r,\beta}})+O_{r,\tau}(\delta+h),
}
\tag{3.6}
$$

uniformly over all dimensions and divisors in the stated range.
There is no Taylor expansion in `tau` at derivative order `r`.
That distinction is essential for large fixed `r`, because high
derivative constants need not make a first-order `tau` truncation
useful.

## 4. Positivity of the phase defect and its exact character compression

By (1.8), the `(7,0)` coefficient of
`partial_q^(r-1)v_0` is nonzero. Thus every `G_(r,beta)` with
`beta>0` is a nonconstant real continuous function. If
`exp(iG_(r,beta))` were identically one, its values would force
`G_(r,beta)` into `2pi Z`; connectedness of the torus would then
make it constant, a contradiction. Hence

$$
\int_{\mathbb T^2}|e^{iG_{r,\beta}}-1|^2>0
\qquad\text{for every }\beta\in[2^{-r},1].
$$

The integral depends continuously on `beta`. Compactness of this
closed interval proves the strict lower bound `mu_r>0` in (0.2).

Set `z_beta=e^{iG_(r,beta)}-1`. The exact Weyl character relation
gives

$$
P_\chi Q_N(e^{2\pi i(kq+lp)})P_\chi=0
\quad\text{unless }d\mid k\text{ and }d\mid l.
\tag{4.1}
$$

Indeed conjugation by the two group generators multiplies that mode
by `e_d(k)` and `e_d(-l)`. A nontrivial multiplier changes the
character and makes its compression vanish. The surviving nonconstant
frequencies have size at least `d`. Therefore for any fixed smooth
symbol `f`, uniformly in `chi`,

$$
\left\|P_\chi Q_N(f)P_\chi
-\left(\int_{\mathbb T^2}f\right)P_\chi\right\|
\le\sum_{|k|+|l|\ge d}|\widehat f(k,l)|
\le d^{-1}\|f\|_1.
\tag{4.2}
$$

This argument includes frequencies that alias modulo `N`; they still
belong to the displayed tail. Apply (3.5) and (4.2) with
`f=|z_beta|^2`. Smoothness and compactness in `beta` make the bounds
uniform, yielding for every unit `v` in `P_chi`

$$
\|Q_N(z_\beta)v\|^2
=\int_{\mathbb T^2}|z_\beta|^2+O_{r,\tau}(h+d^{-1})
\ge\mu_r-O_{r,\tau}(h+d^{-1}).
\tag{4.3}
$$

Combine (3.6) and (4.3). Since
`delta<=N^(-1/r)`, `d^(-1)<=N^(-1/r)`, and `h=O(N^(-1))`,
there exists one threshold `N_r`, independent of the divisor and
both characters, for which

$$
\boxed{\|(C_{r-1}(\delta)-I)v\|\ge\frac12\sqrt{\mu_r}.}
\tag{4.4}
$$

For example, take the squared-norm error in (4.3) at most `mu_r/4`
and the operator error in (3.6) at most `sqrt(mu_r)/4`; their
combination is stronger than (4.4). These errors tend to zero with
explicit powers of `N`, and `mu_r` has already been proved positive.

## 5. All input and output characters

Fix any input `chi` and output `psi`, and let `v` be unit in `P_chi`.
Put `epsilon=||(I-P_psi)E_Nv||`. On these spaces the lattice
translation `R=T_N(-bN/d,0)` acts by scalars `r_chi,r_psi`.
With `B=E_N^*RE_N`,

$$
\|(B/r_\psi-I)v\|=\|(R-r_\psi)E_Nv\|\le2\epsilon.
\tag{5.1}
$$

The inverse has the same bound, and `R/r_chi` fixes `v` exactly.
Multiplying `R` and `B` independently by scalar phases leaves their
group commutator unchanged, and consequently leaves every further
commutator unchanged. The word has exactly `2^(r-1)` factors of
type `B` or `B^(-1)`. Telescoping its unitary factors therefore gives

$$
\|(C_{r-1}(\delta)-I)v\|\le2^r\epsilon.
\tag{5.2}
$$

Equations (4.4)–(5.2) prove
`epsilon>=2^(-(r+1))sqrt(mu_r)=c_r`. Unitarity proves (0.1).

The subgroup is an exact abelian representation because
`(N/d)^2=Nm` is divisible by `N`, so the Weyl multiplication phases
inside it equal one. Orthogonality of its characters proves that
the `P_chi` sum to the identity; the trace of every nonidentity
group element is zero, so every projection has rank `N/d^2`.
Thus no representation-theoretic assumptions on composite moduli
were used in the proof.

Finally the exact kernel identity

$$
T_N(a,b)M_N=M_NT_N(3a-4b,-2a+3b)
$$

shows that `M_N` permutes the characters by
`chi -> chi composed with L`, `L(s,u)=(3s-4u,-2s+3u)`.
It gives the asserted version of (0.1) for `U_N=E_NM_N` as well.

## 6. Consequence for the all-time pair functional and boundary

Let `rho_r=sqrt(1-c_r^2)`, and define

$$
\mathcal K_{N,d}=
\left(\sum_\chi P_\chi E_NP_\chi\right)M_N,
\qquad q_n=\operatorname{Tr}(U_N^n-\mathcal K_{N,d}^{\,n}).
$$

Then `||K||<=rho_r`. With `lambda=3+2sqrt(2)`, its block
permutation and the fixed-character count prove

$$
\frac{|\operatorname{Tr}\mathcal K_{N,d}^{\,n}|}{N}
\le\rho_r^n\min\left(1,\frac{\lambda^n}{d^2}\right).
\tag{6.1}
$$

To check the count at every composite `d`, the kernel of an integer
rationally invertible matrix `B` modulo `d` injects into
`Z^2/BZ^2` by `x -> Bx/d mod BZ^2`. Therefore the number of
characters fixed by `L^n` is at most
`|det(L^n-I)|=lambda^n+lambda^(-n)-2<=lambda^n`.

For any bounded weights `w_n`, grouping each difference before
summing gives the absolutely convergent estimate

$$
\begin{aligned}
\frac1{N^2}\left|\sum_{n\ge1}w_n
\left(|\operatorname{Tr}U_N^n|^2-|q_n|^2\right)\right|
&\le3\|w\|_\infty\sum_{n\ge1}\rho_r^n
\min\left(1,\frac{\lambda^n}{d^2}\right)\\
&=O_r\left(\|w\|_\infty d^{-\kappa_r}\right),
\qquad\kappa_r=-\frac{2\log\rho_r}{\log\lambda}>0.
\end{aligned}
\tag{6.2}
$$

Here `rho_r lambda>1`, since `mu_r<=4` and hence
`c_r<=2^(-r)<=1/4`. Split the sum at
`floor(2log d/log lambda)` to obtain the stated power bound.
For `d>=N^eta`, the error is `O_r(N^(-eta kappa_r))`.

This proves that the complete character itinerary contributes a
vanishing signed error to the compactly weighted pair sum and to
the infinite Abel pair sum, including its cross term with all
retained histories. The remaining exact traces `q_n` include words
with inter-character transitions; their CUE discrepancy is still
unproved. Higher fixed-order correlations required by `H_diag`
are likewise unproved. The theorem is an original-family exclusion
of a specified growing arithmetic sector mechanism, not a solution
of the full spectral-statistics problem.

## 7. Provenance

The quartic exact-operator foundation is
`arithmetic_comb_fourth_difference_gap.md`, SHA-256
`0b7bd5a0c21b79f1dd45d6b6377e58cd9f9afcdb8ed017199c874ace8e2fcc66`,
independently reconstructed in
`audit_quartic_commutator_word.md`, SHA-256
`ac9afae71b2c9ad15bc00b4a2b98da25473131bcff15072432c605060b4118c6`.
The present proof repeats the needed series, extends the prefix
remainder to arbitrary fixed order, proves the classical phase
limit and its strict nonconstant defect, and checks uniform
compression and independent input/output scalar phases.

The explicit numerical quartic strengthening is separately recorded
in `arithmetic_comb_rescaled_gap.md`, SHA-256
`898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f`.
No historical source was changed, and no unspecified universality
theorem is used.
