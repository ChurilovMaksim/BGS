> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round3_2026_10_21/arithmetic_comb_rescaled_gap.md`. Embedded SHA256: `898528107bfc2691c0f17fe6d8a096592c46de537b045c6bbc41949d0f3bfd2f`.
> [Thematic guide](../../topics/arithmetic.md).

# A dimension-uniform numerical escape gap by rescaling the auxiliary word

Date: 21 October 2026. The original fixed `tau=10^(-80)` is unchanged.

## 0. Precise theorem

Let `N=d^2m` be odd, `m<=sqrt(N)`, and `N>=10^140`.
Let `P_chi` be any of the `d^2` character projections of

$$
H_d(s,u)=T_N(sN/d,uN/d),\qquad (s,u)\in(\mathbb Z/d\mathbb Z)^2.
$$

Each has rank `m`. For the actual original kick
`E_N=exp(i tau N A_N)`, every unit vector in its range satisfies

$$
\boxed{
\|(I-P_\chi)E_Nv\|\ge\frac1{64},\qquad
\|P_\chi E_NP_\chi\|\le\rho_*:=\sqrt{\frac{4095}{4096}}<1.
}
\tag{0.1}
$$

The assertion is uniform in the dimension, the square divisor, and the
character. In particular it includes `N=7^(4r)`, `d=7^r`, for all large
`r`. The explicit dimension threshold is deliberately loose.

This improves the previous gap proportional to `tau`. It changes only
an auxiliary lattice translation in a fixed commutator word; the original
Hamiltonian and the time `tau N` are not altered.

There is also a quantitative consequence for all time indices in the pair
functional. With the exact operator `K` and complementary traces defined
in Section 4,

$$
\frac1{N^2}\left|\sum_{n\ge1}w_n
 \left(|\operatorname{Tr}U_N^n|^2-|r_n|^2\right)\right|
\le C_*\|w\|_\infty d^{-\kappa_*},
\qquad
\kappa_*=-\frac{\log(4095/4096)}{\log(3+2\sqrt2)}>0.
\tag{0.2}
$$

This estimate includes both the compact Fourier weights of the requested
pair moment and its infinite Abel weights. It does not establish the
CUE limit for the remaining traces `r_n`, or any higher-order criterion.

## 1. Frozen exact-operator input and its hypotheses

The source proof is
`arithmetic_comb_fourth_difference_gap.md`, SHA-256
`0b7bd5a0c21b79f1dd45d6b6377e58cd9f9afcdb8ed017199c874ace8e2fcc66`.
Its Sections 3–4 prove an estimate for an arbitrary real auxiliary step
`0<=delta<=1`, before imposing the relation `N delta^4=1`.
The independent proof is
`audit_quartic_commutator_word.md`, SHA-256
`ac9afae71b2c9ad15bc00b4a2b98da25473131bcff15072432c605060b4118c6`.
The estimate is recalled here with every scale factor retained.

Use the exact physical symbol

$$
\begin{aligned}
a(q,p)={}&\cos14\pi q+\frac{r(q)}{10}
+\frac{r(q)\sin2\pi q}{100}-\frac1{10}\\
&+\frac{r(q+1/2)\cos(2\pi p-\alpha_0)}{100},
\end{aligned}
\tag{1.1}
$$

and `Q_N(exp(2pi i(kq+lp)))=(-1)^(kl)T_N(l,k)`, so `A_N=Q_N(a)`
exactly. Put

$$
g=\partial_q^4a,\qquad h=(2\pi N)^{-1},\qquad t=\tau/(2\pi).
$$

The exact Fourier Heisenberg series in the cited proofs produces a real
periodic symbol `v_h`, with

$$
K_h=Q_h(\partial_q^3v_h),\qquad
\|K_h-tQ_h(g)\|\le2\cdot10^{12}t^2.
\tag{1.2}
$$

For `H_0=-P`, `H_1=E_h^*(-P)E_h`, set

$$
R(s)=e^{isH_0/h},\qquad C_0(s)=e^{isH_1/h},\qquad
C_{j+1}(s)=R(s)C_j(s)R(s)^*C_j(s)^*,\quad j=0,1,2.
\tag{1.3}
$$

The right-to-left prefix Taylor proof, using depth-four scaled
commutators bounded by `10^12|t|`, gives

$$
\|C_3(\delta)-e^{i\delta^4K_h/h}\|
\le\frac{10^{20}|t|\delta^5}{5h}.
\tag{1.4}
$$

Here `h,t` remain fixed throughout the differentiation. If `N delta` is
an integer, the explicit continuous Zak fibers of these operators
descend (1.2)–(1.4) to the exact finite matrices. These are exactly the
hypotheses checked below, rather than an assumption about a generic
Fourier integral operator.

Write

$$
\gamma=\tau N\delta^4.
$$

Unitary Duhamel comparison applied to (1.2), and then (1.4), gives the
useful version valid also when `N delta^4` is a very large fixed number:

$$
\boxed{
\|C_3(\delta)-e^{i\gamma Q_N(g)}\|
\le10^{12}\gamma\tau+10^{21}\gamma\delta.
}
\tag{1.5}
$$

Indeed the first error is at most
`(delta^4/h)*2*10^12*t^2=(10^12/pi)gamma tau`, and the second equals
`(10^20/5)gamma delta`. The larger displayed constants are convenient
uniform bounds. In particular there is no `gamma^2` error: the leading
bounded exponential has not been linearized.

## 2. Two explicit bounds for the fourth derivative

Let

$$
\sigma^2=\sum_{k,l}|\widehat g(k,l)|^2.
$$

The `l=0,k=+/-7` coefficients of `a` are exactly `9/20`; hence

$$
\sigma\ge\frac{9}{10\sqrt2}(14\pi)^4>2\cdot10^6.
\tag{2.1}
$$

Only elementary numerical inequalities are needed for the last strict
bound. An inscribed regular twelve-gon gives
`pi>3(sqrt(6)-sqrt(2))>31/10`, while `sqrt(2)<10/7`. Therefore the
displayed lower bound exceeds
`(63/100)(217/5)^4=139694557023/62500>2*10^6`.

For an upper Fourier bound, the purely cosine part of `a` is

`(9/10)cos7+(1/10)cos1-(1/20)cos8-(1/20)cos6`,

where `cos j` denotes `cos(2pi j q)`. The exact sine expansion is

$$
r(q)\sin2\pi q
=\sin1+\tfrac12(\sin2+\sin6-\sin8)
+\tfrac14(\sin5-\sin9).
\tag{2.2}
$$

Also
`r(q+1/2)=1-cos1+cos7-(cos8+cos6)/2`.
Each sine or cosine has Fourier coefficient one-norm one. After four
`q` derivatives the three parts of (1.1), divided by `(2pi)^4`,
therefore have coefficient one-norm at most respectively

$$
\begin{aligned}
&\tfrac9{10}7^4+\tfrac1{10}
+\tfrac1{20}(8^4+6^4)=2430.6,\\
&\tfrac1{100}\left[1+\tfrac12(2^4+6^4+8^4)
+\tfrac14(5^4+9^4)\right]=45.015,\\
&\tfrac1{100}\left[1+7^4+\tfrac12(8^4+6^4)\right]=50.98.
\end{aligned}
$$

Thus

$$
\|g\|_{\mathcal F}\le\frac{505319}{200}(2\pi)^4
<11\cdot10^6.
\tag{2.3}
$$

The deliberately loose last bound follows just from `pi<4`, using the
circumscribed square: its left side is then less than
`258723328/25=10348933.12`. Tighter bounds for `pi` would give
`||g||_F<4*10^6`, but are unnecessary below. Quantization has norm at most
the Fourier coefficient one-norm, so (2.3) bounds `||Q_N(g)||` uniformly.

Finally the support of `g` lies in `|k|<=9, |l|<=1`. The exact character
compression identity, proved by Weyl character orthogonality in the
frozen source, gives for every `d>18`

$$
P_\chi Q_N(g)^*Q_N(g)P_\chi=\sigma^2P_\chi.
\tag{2.4}
$$

In particular `||Q_N(g)v||=sigma` for every unit vector in any of these
character spaces.

## 3. Choice of the permitted auxiliary step and proof of the gap

Fix the integer

$$
b_0=2\cdot10^{18},\qquad
\gamma_0=\tau b_0^4=\frac1{6250000}.
$$

For each allowed `N,d`, choose

$$
b=\lfloor b_0dN^{-1/4}\rfloor,\qquad
\delta=b/d,\qquad\gamma_N=\tau N\delta^4.
\tag{3.1}
$$

Since `d>=N^(1/4)`, the number inside the floor is at least `b_0`.
Consequently

$$
\delta\le b_0N^{-1/4},\qquad
\gamma_0(1-b_0^{-1})^4\le\gamma_N\le\gamma_0,
\qquad\gamma_N\ge\tfrac{99}{100}\gamma_0.
\tag{3.2}
$$

The last inequality follows from `(1-x)^4>=1-4x` on `[0,1]`.
Also `Ndelta=bN/d=bdm` is an integer, as required for exact torus
descent. For `N>=10^140`,

$$
\delta\le2\cdot10^{-17}<1,
\qquad
10^{12}\gamma_N\tau+10^{21}\gamma_N\delta
\le1.6\cdot10^{-75}+\frac2{625}<\frac1{250}.
\tag{3.3}
$$

The finite-dimensional self-adjoint operator `Q_N(g)` obeys
`gamma_N||Q_N(g)||<44/25<2` by (2.3). For real `|x|<=2`,

$$
|e^{ix}-1|=2|\sin(x/2)|\ge\frac56|x|.
\tag{3.4}
$$

For example, on `[0,1]` the inequality `sin y>=y-y^3/6>=5y/6`
follows by integrating `cos y>=1-y^2/2`; this proves (3.4).
Apply the ordinary finite spectral theorem and (2.4) to a unit
`v` in `P_chi`:

$$
\|(e^{i\gamma_NQ_N(g)}-I)v\|
\ge\frac56\gamma_N\|Q_N(g)v\|
>\frac56\frac{99}{100}\frac{2\cdot10^6}{6250000}
=\frac{33}{125}.
\tag{3.5}
$$

Combining (1.5), (3.3), and (3.5) yields

$$
\|(C_3(\delta)-I)v\|>\frac{33}{125}-\frac1{250}
=\frac{13}{50}>\frac14.
\tag{3.6}
$$

Now let `epsilon=||(I-P_chi)E_Nv||`.
The exact lattice translation `R=T_N(-bN/d,0)` acts on this character
space as a scalar `r_chi`. Set `B=E_N^*RE_N`. Then

$$
\|(B/r_\chi-I)v\|=\|(R-r_\chi)E_Nv\|\le2\epsilon.
\tag{3.7}
$$

The inverse has the same bound. Dividing `R,B` by their common scalar
does not change their nested commutator. Its fourteen normalized `R`
factors fix `v`, and its eight normalized `B` factors each have residual
at most `2epsilon`. Telescoping the twenty-two unitary factors gives
`||(C_3-I)v||<=16epsilon`. Equation (3.6) proves
`epsilon>13/800>1/64`, and unitarity proves (0.1).

This is a result about the original fixed-time exponential. Neither an
infinitesimal leakage assertion nor a generator estimate alone would
justify (0.1); the comparison (1.5) at the enlarged permitted lattice
step is the essential argument.

### 3.1 Every input and output character pair

In fact the same numerical estimate holds between any two character
spaces, not only a repeated character:

$$
\boxed{\sup_{\chi,\psi}\|P_\psi E_NP_\chi\|\le\rho_*.}
\tag{3.8}
$$

To prove it, take unit `v` in `P_chi` and put
`epsilon=||(I-P_psi)E_Nv||`. Let `r_chi,r_psi` be the scalars by which
`R` acts on the input and output spaces. Then
`||(B/r_psi-I)v||=||(R-r_psi)E_Nv||<=2epsilon`, while `R/r_chi`
fixes `v`. Independent scalar multipliers of `R` and `B` cancel in their
first group commutator, and then in every further commutator. Thus the
same twenty-two-factor telescoping proof gives
`||(C_3-I)v||<=16epsilon`. Its lower bound (3.6) depends only on the
input-space compression (2.4), which is unchanged. This proves (3.8).
Since `M_N` permutes the input characters, it also proves
`sup_(chi,psi)||P_psi U_NP_chi||<=rho_*`.

For any permutation `F` of the character set, the selected transition
operator `sum_chi P_(F(chi))E_NP_chi` is consequently a direct sum of
maps between mutually orthogonal input and output blocks and has norm
at most `rho_*`. No assertion about a noninjective choice of output
characters is needed here.

## 4. Full character itinerary and the complete signed pair error

Let `L(s,u)=(3s-4u,-2s+3u)` modulo `d`. Direct quadratic-kernel algebra
in the frozen proof gives exactly

$$
T_N(a,b)M_N=M_NT_N(3a-4b,-2a+3b),\qquad
M_NP_\chi M_N^*=P_{\chi\circ L}.
$$

Thus the operator following the unperturbed character itinerary is

$$
\mathcal K_{N,d}=\sum_\chi P_{\chi\circ L}U_NP_\chi
=\left(\sum_\chi P_\chi E_NP_\chi\right)M_N,
\qquad\|\mathcal K_{N,d}\|\le\rho_*.
\tag{4.1}
$$

Put `c_n=Tr(K^n)`, `r_n=Tr(U_N^n-K^n)` and `lambda=3+2sqrt(2)`.
Only characters fixed by `L^n` can contribute to `c_n`. For all composite
`d` their number is at most

$$
|\det(L^n-I)|=\lambda^n+\lambda^{-n}-2\le\lambda^n.
$$

For completeness, the kernel of an integer invertible rational matrix
`B` modulo `d` injects into `Z^2/BZ^2` by
`x -> Bx/d mod BZ^2`; its cardinality is at most `|det B|`.
Applying this to `B=(L^T)^n-I` proves the assertion without restricting
to primes. Every fixed-character block has rank `N/d^2`. Hence

$$
\frac{|c_n|}{N}\le\rho_*^n
\min\left(1,\frac{\lambda^n}{d^2}\right).
\tag{4.2}
$$

The identity `Tr(U_N^n)=r_n+c_n`, together with
`|Tr(U_N^n)|<=N` and `|r_n|<=N+|c_n|`, implies

$$
\frac1{N^2}\sum_{n\ge1}|w_n|
\left|\,|\operatorname{Tr}U_N^n|^2-|r_n|^2\right|
\le3\|w\|_\infty\sum_{n\ge1}\rho_*^n
\min\left(1,\frac{\lambda^n}{d^2}\right).
\tag{4.3}
$$

The grouped difference is absolutely summable even for nondecaying
bounded weights. Splitting the last sum at
`floor(2log d/log lambda)` proves (0.2), for example with the explicit
constant

$$
C_*=3\left(\frac{\lambda}{\lambda\rho_*-1}
+\frac1{1-\rho_*}\right).
\tag{4.4}
$$

This removes the entire character itinerary, including its cross term
with all complementary histories, at every time index. Words with at
least one transition to another character are all retained in `r_n`.
Their correlations have not been estimated.

## 5. Status and boundary

The actual new conclusion is a fixed numerical escape gap for the exact
original matrices, uniformly on every character sector of every square
divisor with rank at most `sqrt(N)`, and a quantitatively vanishing signed
pair error for removal of the corresponding complete itinerary.

The task's full `H_diag` remains unresolved. The first missing estimate
is still the CUE comparison for the retained exact traces on the time
scale of `N`, followed by all higher fixed-order weighted correlations.
The character decomposition spans the whole Hilbert space: the theorem
does not exclude eigenvectors that are superpositions across its sectors.
No claim of general absence of arithmetic spectral effects follows.
