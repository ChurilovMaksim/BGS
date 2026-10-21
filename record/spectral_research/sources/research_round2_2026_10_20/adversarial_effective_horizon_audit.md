> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round2_2026_10_20/adversarial_effective_horizon_audit.md`. Embedded SHA256: `996abb617d3ea49f9e566b00b662c74ee4cf0ffc8fbc334a1c27ff12a39eec0a`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of the explicit sector horizon

Date: 20 October 2026. This audit concerns the exact fixed parameter
`tau=10^-80` and the matrices in the question. It does not assume any
spectral universality conclusion.

## 1. Frozen input and verdict

The audited file is `arithmetic_iterated_effective_horizon.md`, SHA-256
`9739e62cc9a4282d39b379c50835f05fd3d46d664663cf6032b3337857751768`.
Its all-iterate geometric input, independently checked earlier, is
`arithmetic_iterated_sector_covariance.md`, SHA-256
`c8e02b81819350ab52e7bc3dd791ffbeb1ae1a2192a9a99f1168c4c56d7123e2`.

**Verdict:** the displayed growing-horizon estimates pass the independent
audit. In particular, the proof does not propagate an `N`-dependent cutoff
by an unjustified fixed-symbol Egorov theorem. Only the two coordinate
characters are propagated. The remaining cutoff dependence is bounded by
an exact Weyl product estimate and explicit derivatives.

For fixed odd `d`, `N=d^2 m`, and

$$
T_N=\left\lfloor
\frac{\log((\log\log N)/32000)}{\log256}\right\rfloor,
$$

the input proves, under its explicit two thresholds, a uniform error

$$
\mathcal R_N=
\sqrt{16\pi e^5}\exp[-\sqrt{\log N}/768]
+C_*(\log\log N)^{11}N^{-7/8}
$$

for every nonzero sector-correlation lag of absolute value at most `T_N`.
The constant `C_*` is independent of `d`, the translations, the lag, and
`N`. It is effectively obtainable from finitely many derivatives of one
explicit scalar cutoff. Its numerical value is not claimed to have been
computed.

## 2. Torus defect, including the lift issue

Write `Psi=S Phi_tau`, `lambda=3+2sqrt2`,
`ell=(1,sqrt2)/sqrt3`, and

$$
v_r(x)=\lambda^{-r}\ell\Psi^r(x)-\ell x.
$$

The all-iterate input proves
`|vhat_r(e_i)|>=tau/800` for `i=1,2` and every `r>=1`, with one uniform
error bound. It does not use a Taylor expansion with a constant depending
implicitly on `r`.

For
`kappa=Psi^r t_h Psi^(-r) t_g`, put
`f_i=exp(2pi i(kappa_i-x_i))-1`. When `h` is a nonzero translation with
denominator `d`, set `x=Psi^r(y)-g`. The lift difference becomes the
periodic vector

$$
G(y)=\Psi^r(y+h)-\Psi^r(y)+g.
$$

For a nonintegral coordinate `h_i`, its nonconstant projected Fourier
coefficient is

$$
\widehat{\ell G}(e_i)
=\lambda^r(e^{2\pi i h_i}-1)\widehat v_r(e_i),
\quad
|\widehat{\ell G}(e_i)|\ge\lambda^r\tau/(200d).
$$

Here `|exp(2pi i h_i)-1|>=4/d` follows from
`2 sin(pi t)>=4t` for `0<=t<=1/2`. If both torus defects have norm at most
`epsilon<1`, then every component of `G` lies within `epsilon/4` of an
integer. The nearest integer is unique and is constant on the connected
torus. Thus, for one `n` in `Z^2`,

$$
\|\ell(G-n)\|_\infty<\epsilon/2.
$$

Comparison with the preceding nonconstant coefficient forces
`epsilon>=lambda^r tau/(100d)`. If a defect has norm at least one there is
nothing to prove. Consequently the lower bound
`max_i ||f_i||>=tau/(1000d)` is valid uniformly in `r`. It is a bound for
the torus defect itself, not only for an unbounded lift displacement.

## 3. Global complex strip and the propagated observables

The exact ordinary-Weyl symbol has support `|k|<=9, |l|<=1` and Fourier
coefficient norm at most `59/50`. On the complex strip of width `1/100`,
these give `||X||<=22`, `||DX||<=2000`, using the maximum coordinate norm
and its induced row norm. Indeed the complex Fourier multiplier is less
than two.

Reality on the real torus gives
`|Im X(z)|<=2000 |Im z|`. Gronwall and the variational equation then give
imaginary growth and derivative growth at most `exp(2000 tau)<2` during
each complete or partial flow segment. Starting at half the strip width
keeps the entire segment inside the strip. Boundedness of the vector field
there also excludes finite-time escape in a real direction.

Both `S` and `S^-1` have row norm seven. Each factor `Psi` or `Psi^-1`
therefore increases imaginary parts by at most sixteen. The chosen strip

$$
\rho_r=(1000\,256^r)^{-1}
=\frac{1/100}{10\,16^{2r}}
$$

works for the entire word and all its suffixes, including intermediate
partial flow segments. Before the last of at most `2r` factors the
imaginary part is at most `(1/100)/160`, and after it at most
`(1/100)/10`. Real translations change none of these bounds.

Therefore every transported coordinate character is bounded by two on
the full periodic strip above the real torus. The coordinate differences
and the torus defects are bounded by four there. This is the global strip
bound needed for the subsequent ray argument; it is not merely a local
holomorphic extension near a point of large modulus.

For a strip-holomorphic function bounded by `M`, grouping the Fourier
frequencies by their one-norm gives

$$
|b|_s\le 2^{2s+4}(s+1)!M\rho_r^{-(s+2)}.
$$

The exact sine commutator gives

$$
\|iN[A_N,\operatorname{Op}_N b]-\operatorname{Op}_N(Xb)\|
\le \frac{\pi^3}{3N^2}|a|_3|b|_3,
\qquad |a|_3<2000.
$$

Duhamel on each segment and telescoping with unitary conjugations prove
the stated coordinate-character remainder
`10^12 r rho_r^-5 N^-2`. The constants `10^10` per segment and `10^12` for
the word are generous: the preceding Fourier constant for `s=3` is
`24576`, and the actual segment length is at most `tau<1`.

## 4. Published one-dimensional theorem and the two-dimensional estimate

The source checked directly is F. Nazarov, M. Sodin and A. Volberg,
*Lower bounds for quasianalytic functions, I. How to control smooth
functions?*, Math. Scand. 95 (2004), 59–79, Theorem B, equation (1.8),
printed page 62. The class and Bang-degree definitions are on pages
60–62. Published PDF:
<https://journals.msp.org/mscand/article/download/770/769/801>.
DOI: <https://doi.org/10.7146/math.scand.a-14449>.

For the derivative sequence `M_j=j!A^j`, the generating function is
`A(s)=As`; hence `sup s A'(s)/A(s)=1` and the theorem's constant is
`4e^5`. The reciprocal series diverges. The theorem gives

$$
\|u\|_I\le
\left(\frac{4e^5|I|}{|E|}\right)^{2n_u}\|u\|_E,
$$

with exactly the Bang normalization used in the input. In particular the
summand is `1/(Aj)`, and the cutoff in the sum is
`log ||u||_infinity^-1`; no normalization factor is missing.

For a periodic holomorphic `f` bounded by four on a strip of width `rho`,
choose a real maximum point with modulus at least `m`, rotate its value,
and take its real part. This real part has a holomorphic extension bounded
by four. Every ray in a convex fundamental square starting at that point
has length at most `sqrt2`. After rescaling to `[0,1]` and dividing by
four, the derivative bounds are `j!(2/rho)^j` and the starting value is
at least `m/4`. The global strip established in Section 3 justifies these
Cauchy estimates along every point of every ray.

If `L_0=ceil(log(4/m))`, the harmonic-sum estimate in the input proves

$$
n_u\le K,
\qquad K=2(L_0+2)e^{8/\rho}.
$$

Indeed, at the indicated upper integer the harmonic sum is at least
`8/rho`; multiplication by `rho/2` gives four, exceeding the Bang
threshold `e`. Applying the published one-dimensional inequality along
each full ray bounds its bad portion by
`4e^5 (epsilon/m)^(1/(2K))` times its length. Polar integration contributes
at most `sqrt2*sqrt2*2pi=4pi`. Thus

$$
\operatorname{area}\{|f|\le\epsilon\}
\le16\pi e^5(\epsilon/m)^{1/(2K)}.
$$

This also covers a maximizing point on the boundary of the chosen square.
No multivariate Remez theorem is used without proof. With
`m=m_d=tau/(1000d)` and `rho=rho_r`, it gives
`K_r=D_d exp(8000*256^r)` exactly as stated in the input.

## 5. The varying cutoff: why the Egorov objection does not apply

Let `F=G_N(g)U_N^-r G_N(h)U_N^r`,
`mu(b)=Tr(Op_N(b)F)/N`, `b_i=exp(2pi i x_i)`, and
`g_i=b_i-b_i composed with kappa`. Cyclicity and the coordinate-character
Egorov estimate imply, for **every** smooth `b`,

$$
|\mu(bg_i)|\le
C N^{-1}\rho_r^{-3}|b|_1
+10^{12}r\rho_r^{-5}N^{-2}|b|_0.
$$

To verify this directly, replace the two pointwise symbol products by
operator products, move the fixed character past `F`, and use cyclicity
to leave its commutator with `Op(b)`. Both products and that commutator
are bounded by the exact Fourier Weyl-product inequality. The variable
`b` is never transported through `Psi`.

Put `v=|g_1|^2+|g_2|^2`,
`chi_delta=chi(v/delta)`,
`b_i,delta=(1-chi_delta) conjugate(g_i)/v`, extended by zero near `v=0`.
The input's explicitly specified scalar cutoff is smooth. The complex
extension of `v` is bounded by 32. Total derivative orders in products
add, so a derivative of order `j` costs `rho_r^-j`; it does not cost
`rho_r^(-j^2)`. At most `j+1` inverse powers of `delta` are needed for
`b_i,delta`. Hence the stated bounds

$$
|b_{i,\delta}|_1\le C\delta^{-6}\rho_r^{-5},
\qquad |\chi_\delta|_2\le C\delta^{-6}\rho_r^{-6}
$$

follow from five and six ordinary derivatives respectively. The
Hilbert–Schmidt alias estimate for `Op(chi_delta)` uses only these
Fourier norms. Before weakening, the three algebraic errors are

$$
C\delta^{-6}
\bigl(N^{-1}\rho_r^{-8}
+rN^{-2}\rho_r^{-10}+N^{-1}\rho_r^{-6}\bigr).
$$

Together with the sublevel-area square root, these prove the master
estimate in the input. Every constant needed here is a finite expression
in the earlier absolute constants and finitely many cutoff derivatives.

## 6. Horizon, uniformity, and spectral-window consequence

The thresholds in the input imply, simultaneously for `1<=r<=T_N`,

$$
8000\,256^r\le\tfrac14\log\log N,
\quad \log D_d\le\tfrac14\log\log N,
\quad K_r\le\sqrt{\log N}.
$$

With `delta=N^-1/48`, the logarithm of the sublevel ratio is at most
`-(log N)/192`. The power `1/(4K_r)` after taking its square root gives
`exp[-sqrt(log N)/768]`. The algebraic error has
`N^-1 delta^-6=N^-7/8`; also
`(r+1)rho_r^-10<=C(log log N)^11`. These are precisely the two terms of
`mathcal R_N`.

The character coefficients of the two projectors have total absolute
sum one. The identity pair contributes `d^-4`, while the sum of all other
absolute coefficients is at most one. Negative lags follow by cyclicity.
Thus no extra factor depending on `d` is lost when passing from word
traces to the sector correlation.

For `B=P_chi-d^-2 I`, the zero-lag normalized correlation is
`d^-2-d^-4`. Averaging the conjugates of `B` over `T_N+1` times gives the
commutant bound by an orthogonal Hilbert–Schmidt contraction. This includes
the full eigenspace blocks of every repeated eigenvalue. The same
calculation with moving phases, and the elementary lower bound `4/pi^2`
for the squared normalized Dirichlet sum on a window of half-width
`1/(2(T_N+1))`, gives the asserted uniform moving-window estimate.

The theorem controls actual centered-sector matrix-element weights. It
does not count unweighted close eigenphase pairs. The exact missing
weight-to-count estimate is recorded in `adversarial_pair_sector_windows.md`.

## 7. A limited but rigorous obstruction to improving only the analytic step

This final lemma concerns the **information used in the analytic step**,
not the actual iterated defect. It explains why preserving its exact
dynamical functional equation matters.

Let

$$
w_r=\tau\sum_{j<r}\lambda^{-j}f(S^j x),
\qquad f=\ell X,
\qquad \rho_r=(1000\,256^r)^{-1}.
$$

The Fourier bounds already used above give, on this strip,

$$
\|w_r\|\le30\tau,
\quad \|\nabla w_r\|\le10^4\tau r,
\quad \int w_r=0,
\quad |\widehat w_r(e_i)|\ge\tau/400.
$$

For example `||f||_Fourier<=12`, each transformed frequency has one-norm
at most `20 lambda^j`, and its complex multiplier on the strip is less
than two. These give the displayed function and gradient bounds by
summing the geometric weights. The mean is zero because `X` is a
Hamiltonian vector field and `S` preserves area.

For every sufficiently large integer `r` there is a real periodic
holomorphic function `F_r` on this same strip such that

$$
\int F_r=0,\quad
\|F_r\|_{\rm strip}<31\tau,\quad
\|F_r-w_r\|_{\infty,\mathbb T^2}<\tau^2/2,
\quad |\widehat F_r(e_i)|\ge\tau/800,
$$

yet any upper sublevel bound
`area{|F_r|<=epsilon}<=C_r epsilon^beta_r`, valid for all small positive
`epsilon` with a finite constant `C_r`, must have

$$
\beta_r\le 1/M_r,
\qquad
M_r\ge\frac1{32}
\exp\!\left(\frac{\tau}{16\cdot10^{10}r\rho_r}\right).
\tag{7.1}
$$

Here is an explicit construction and proof. Set

$$
a=\tau^2/10^6,
\quad \kappa=(16\cdot10^4\tau r\rho_r)^{-1},
\quad K=\kappa a,
\quad M_r=\lfloor e^K/16\rfloor.
$$

For example `r>=40` makes `K>=4`, and hence `M_r>=e^K/32`.
The gradient bound and reality imply `|Im(kappa w_r)|<=1/16` on the
whole strip. Thus

$$
B_r=\tanh(\kappa w_r)^{2M_r}
$$

is periodic and holomorphic there, with `|B_r|<=1`; this last inequality
follows from the elementary formula for the modulus of `tanh z` when
`|Im z|<pi/4`. On real points, for `x=|w_r|>=a`,

$$
0\le1-B_r\le4M_r e^{-2\kappa x}.
$$

Since `x exp(-2kappa x)` decreases for `x>=a`, this proves
`||w_r B_r-w_r||<=a`; for `x<=a` the same bound is immediate.

The elementary coefficient inequality gives `int |w_r|>=tau/400`.
Therefore the set `|w_r|>=tau/800` has area at least `1/24000`, using
`||w_r||<=30tau`. On that set the preceding exponential bound gives
`B_r>=1/2`; hence `int B_r>=1/48000`. Define

$$
c_r=\frac{\int w_r B_r}{\int B_r},
\qquad F_r=(w_r-c_r)B_r.
$$

Because `int w_r=0`, one has `|c_r|<=48000a`. Consequently
`||F_r-w_r||<=48001a<tau^2/2`, the mean is zero, the strip norm is
less than `31tau`, and the two Fourier lower bounds are preserved.

The nonzero real mean-zero function `w_r` has a real zero `x_0`. At that
point `F_r` vanishes to total order at least `2M_r`. Its convergent Taylor
series gives, in a sufficiently small real ball,
`|F_r(x)|<=C'_r |x-x_0|^(2M_r)`. Thus for sufficiently small `epsilon`,

$$
\operatorname{area}\{|F_r|\le\epsilon\}
\ge c'_r\epsilon^{1/M_r},\qquad c'_r>0.
$$

This proves (7.1). In particular `M_r` eventually exceeds every fixed
power of `rho_r^-1`, so those analytic, low-frequency, and uniform
`C^0`-approximation facts alone cannot supply a sublevel exponent bounded
below by a positive power of `rho_r`.

The constructed `F_r` is **not** the actual function `v_r`. It is not
claimed to satisfy the exact iterate equation

$$
v_{r+s}=v_r+\lambda^{-r}v_s\circ\Psi^r.
$$

That equation, or additional leafwise information from the actual map,
is precisely information absent from this limited obstruction. The lemma
does not exclude improving the actual theorem by using that information.
