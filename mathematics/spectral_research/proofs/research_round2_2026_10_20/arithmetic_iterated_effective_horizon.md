> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_iterated_effective_horizon.md`. Embedded SHA256: `9739e62cc9a4282d39b379c50835f05fd3d46d664663cf6032b3337857751768`.
> [Thematic guide](../../topics/arithmetic.md).

# An explicit growing horizon for arithmetic-sector traces

## Status and frozen inputs

This note proves a quantitative consequence for the exact matrices in the
question, always with the fixed value `tau = 10^-80`. It does not prove
`H_diag`, and it does not claim a logarithmic or a power time horizon.
The horizon obtained below is an explicit constant times
`log log log N`. In particular, it is an effective growing horizon, not an
unspecified diagonal subsequence extracted from fixed-time convergence.

The following inputs were read and are not modified:

| File | SHA-256 |
|---|---|
| `arithmetic_iterated_sector_covariance.md` | `c8e02b81819350ab52e7bc3dd791ffbeb1ae1a2192a9a99f1168c4c56d7123e2` |
| `root_quantitative_trace_and_sectors.md` | `0a174f5de9d070c31311f4fdfd4ebc58b15df0b6bfd86baf5d6f169a99b2ef6a` |
| `arithmetic_oldspace_escape.md` | `596d44605310cc898fa75e23df4aa811189a1764fed21ce8b9f5d07ae734813a` |

The first input supplies the exact Egorov convention and, with a full proof,
the uniform Fourier lower bounds (2.1) below. The second supplies the
elementary finite-dimensional Weyl product and Hilbert--Schmidt estimates;
their needed statements and the dependence of every new constant on the
iterate are made explicit here.

All logarithms in this note are natural logarithms.

## 1. The quantitative assertion

Fix an odd integer `d >= 3`, write `N=d^2 m` with odd `m`, and use the exact
representation

$$
G_N(\alpha,\beta)=T_N(dm\alpha,dm\beta),
\qquad (\alpha,\beta)\in (\mathbb Z/d\mathbb Z)^2=G.
$$

For a character `chi` of `G`, set

$$
P_{\chi,N}=d^{-2}\sum_{g\in G}\overline{\chi(g)}G_N(g),
\qquad c=d^{-2},\qquad B_{\chi,N}=P_{\chi,N}-cI.
$$

The projectors are orthogonal and have rank `cN`. Define

$$
m_d=\frac{\tau}{1000d},\qquad
D_d=2\bigl(\lceil\log(4/m_d)\rceil+2\bigr),\qquad
\Lambda_N=\log\log N,
$$

and, when the expression is positive,

$$
T_N=\left\lfloor
\frac{\log(\Lambda_N/32000)}{\log256}\right\rfloor.       \tag{1.1}
$$

The estimates below hold whenever

$$
\Lambda_N\ge\max\{8192000,4\log D_d\},\qquad
\log N\ge192\log(\sqrt2/m_d).                            \tag{1.2}
$$

There is an absolute, effectively calculable constant `C_*` such that, with

$$
\mathcal R_N=
\sqrt{16\pi e^5}\exp\!\left(-\frac{\sqrt{\log N}}{768}\right)
+C_*(\log\log N)^{11}N^{-7/8},                          \tag{1.3}
$$

one has simultaneously for every pair of characters and every integer
`1 <= |r| <= T_N`

$$
\boxed{\left|
\frac1N\operatorname{Tr}
 (P_{\chi,N}U_N^{-r}P_{\eta,N}U_N^r)-c^2
\right|\le\mathcal R_N.}                                \tag{1.4}
$$

Let `E_U(B)=sum_lambda Pi_lambda B Pi_lambda` denote the orthogonal projection
onto the full matrix commutant of `U`, including the full blocks of repeated
eigenvalues. Then

$$
\boxed{\frac1N\|\mathcal E_{U_N}(P_{\chi,N})-cI\|_{\rm HS}^2
\le\frac{c-c^2}{T_N+1}+\mathcal R_N.}                    \tag{1.5}
$$

In particular the left side is `O_d(1/log log log N)`. There is no assumption
of simple eigenvalues or of a lower bound on eigenphase gaps.

The constant in (1.3) is independent of `d`, translations, `r`, and `N`.
It arises only from Fourier sums, differentiation up to order six, and one
fixed smooth scalar cutoff, specified in Section 5. No unspecified
analytic-continuation or Lojasiewicz constants are included in it.

## 2. A uniform lower bound for a torus defect

Use ordinary midpoint Weyl quantization
`W_N(k,l)=(-1)^(kl)T_N(l,k)`. The exact symbol of `A_N` is

$$
a(q,p)=V(q)+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0),
$$

where

$$
V(q)=\frac9{10}\cos(14\pi q)
+\frac{(1-\cos(14\pi q))\cos(2\pi q)}{10}
+\frac{r(q)\sin(2\pi q)}{100}.
$$

Its Fourier support is contained in `|k| <= 9, |l| <= 1`, and the sum of the
absolute Fourier coefficients is at most `59/50`. Let

$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
X=\frac1{2\pi}(a_p,-a_q),\qquad
\Psi=S\circ\Phi_\tau,
$$

where `Phi_s` is the time-`s` flow of `X`. These conventions give
`U_N Op_N(b) U_N^*=Op_N(b composed with Psi)+O_b(N^-2)`.

Put `lambda=3+2 sqrt2`, `ell=(1,sqrt2)/sqrt3`. On equivariant lifts define

$$
v_r(x)=\lambda^{-r}\ell\Psi^r(x)-\ell x.
$$

The discounted iteration argument in the frozen all-iterate note proves

$$
|\widehat v_r(e_i)|\ge\tau/800,
\qquad i=1,2,\quad r\ge1.                                \tag{2.1}
$$

Recall the substantive uniformity: if `delta=Phi_tau-Id`, then

$$
v_r=\sum_{j<r}\lambda^{-j}\ell\delta\circ\Psi^j,
\quad
\left\|v_r-\tau\sum_{j<r}\lambda^{-j}\ell X\circ S^j\right\|_\infty
\le3\cdot10^7\tau^2.
$$

The frequencies `S^(-Tj)e_i` lie outside `|l|<=1` for `j>=1`; therefore the
two fundamental coefficients of the linearized sum come only from `j=0`.
Their squared magnitudes before multiplication by `tau^2` are
`101/60000` and `1/120000`. The error bound holds for every `r`, not only
for a preassigned finite collection.

For translations `g,h` corresponding to elements of `G`, define

$$
\kappa=\Psi^r\circ t_h\circ\Psi^{-r}\circ t_g,
\qquad
f_i(x)=e^{2\pi i(\kappa_i(x)-x_i)}-1.                    \tag{2.2}
$$

Here the translation corresponding to `(alpha,beta)` is
`(alpha/d,-beta/d)`. Suppose `h` is nonzero on the torus. Then

$$
\boxed{\max_i\|f_i\|_\infty\ge m_d,\qquad r\ge1.}        \tag{2.3}
$$

This is a statement about torus defects, not just lift displacements. To
prove it, set `x=Psi^r(y)-g` and use equivariant lifts. Then

$$
\kappa(x)-x=G(y):=\Psi^r(y+h)-\Psi^r(y)+g.
$$

The function `G` is periodic. At least one coordinate `h_i` is nonzero
modulo one, and

$$
|e^{2\pi i h_i}-1|\ge4/d.
$$

Consequently its projected Fourier coefficient satisfies

$$
|\widehat{\ell G}(e_i)|
=\lambda^r|e^{2\pi i h_i}-1|\,|\widehat v_r(e_i)|
\ge\frac{\lambda^r\tau}{200d}.                          \tag{2.4}
$$

If both defects in (2.2) had supremum at most `epsilon < 1`, then
`dist(G_j(y),Z)<=epsilon/4`: use
`2 sin(pi t)>=4t` on `0<=t<=1/2`. The closest integer is unique and,
by continuity on the connected torus, is one constant integer `n_j`.
Thus `||ell(G-n)||_infinity <= sqrt2 epsilon/4 < epsilon/2`.
Comparison with (2.4) forces
`epsilon >= lambda^r tau/(100d)`. If a defect has supremum at least one,
(2.3) already holds. This proves (2.3), with ample room in the constant.

## 3. A complex strip and an Egorov bound uniform in the iterate

For a periodic function write `|b|_s=sum_v(1+|v|)^s |bhat(v)|`. All vector
and matrix norms used for complex-domain bounds in this section are the
maximum-coordinate norm and its induced row-sum matrix norm.

Let `sigma_0=1/100`. The support and coefficient bound for `a` give, on
`max |Im z_i| < sigma_0`,

$$
\|X\|_\infty\le22,\qquad \|DX\|_\infty\le2000.          \tag{3.1}
$$

Indeed the complex Fourier multiplier has modulus at most
`exp(2 pi (9+1)/100)<2`. The two bounds are respectively implied by
`2*9*(59/50)<22` and
`2*pi*2*9*10*(59/50)<2000`.

Since `X` is real on the real torus, integration along a vertical segment
shows `|Im X(z)|<=2000 |Im z|` as long as the segment stays in the strip.
Gronwall's inequality and the variational equation therefore give

$$
|\operatorname{Im}\Phi_s(z)|\le e^{2000|s|}|\operatorname{Im}z|,
\qquad \|D\Phi_s(z)\|_\infty\le e^{2000|s|}<2
\quad (|s|\le\tau),                                    \tag{3.2}
$$

when the initial imaginary part is at most `sigma_0/2`. The displayed
bound keeps the solution in the strip and therefore also justifies its
existence throughout the time interval. The vector field is bounded in the
strip, so no finite-time escape in a real direction is possible.

Both `S` and `S^(-1)` have row-sum norm seven. It follows that `Psi` and
`Psi^(-1)` are holomorphic on the strip of width `sigma_0/16`, and increase
the maximum imaginary part by at most a factor sixteen there. The same
bounds hold when a flow segment is replaced by a shorter segment
`|s|<=tau`.

For `r>=1` set

$$
\rho_r=\frac1{1000\,256^r}
=\frac{\sigma_0}{10\,16^{2r}}.                           \tag{3.3}
$$

Every partial word entering (2.2), including its intermediate shorter flow
segments, is holomorphic on this strip. There are at most `2r` factors
`Psi` or `Psi^(-1)`; before the last one the imaginary part is at most
`sigma_0/160`, and after the complete word it is at most `sigma_0/10`.
Real translations do not change these bounds.

In particular, `b_i composed with kappa`, for
`b_i(x)=exp(2 pi i x_i)`, is bounded by two on that entire strip. Both
`g_i=b_i-b_i composed with kappa` and the defects `f_i` in (2.2) are bounded
by four there. These are global periodic strip bounds, not bounds in a
neighborhood of one real point.

If `b` is periodic, holomorphic, and bounded by `M` on a strip of width
`rho<=1`, contour displacement of its Fourier coefficients gives

$$
|b|_s\le C_s M\rho^{-(s+2)},\qquad
C_s=2^{2s+4}(s+1)! .                                   \tag{3.4}
$$

One verification is to group frequencies by their one-norm `n`: there
are `4n` for `n>=1`, and bound the resulting sum by the integral of
`(x+1)^(s+1) exp(-2 pi rho x)`. The zero frequency is included by the
extra factor two in the stated constant.

For completeness, the exact Weyl product implies the quantitative
generator remainder

$$
\left\|iN[A_N,\operatorname{Op}_N(b)]-
\operatorname{Op}_N(X\cdot\nabla b)\right\|
\le\frac{\pi^3}{3N^2}|a|_3|b|_3.                       \tag{3.5}
$$

This follows term by term from `|sin t-t|<=|t|^3/6`. Here
`|a|_3<2000`. Duhamel's formula over a segment of length at most `tau`,
(3.4) with `s=3`, and the bound by two for all transported coordinate
characters give a remainder at most `10^10 rho_r^(-5) N^(-2)` per
flow segment. The cat part and translations have exact Egorov formulas.
Telescoping at most `2r` flow segments therefore proves, for

$$
F_{g,h,r,N}=G_N(g)U_N^{-r}G_N(h)U_N^r,
$$

the uniform coordinate-character estimate

$$
\|F_{g,h,r,N}\operatorname{Op}_N(b_i)F_{g,h,r,N}^*
       -\operatorname{Op}_N(b_i\circ\kappa)\|
\le10^{12}r\rho_r^{-5}N^{-2}.                           \tag{3.6}
$$

Only the two fixed coordinate characters are used here. No Egorov estimate
for the varying cutoffs in Section 5 is asserted or needed.

## 4. An explicit sublevel estimate

The one external analytic theorem used here is Theorem B, equation (1.8),
on printed page 62 of:

F. Nazarov, M. Sodin, A. Volberg, *Lower bounds for quasianalytic functions,
I. How to control smooth functions?*, **Math. Scand. 95** (2004), 59--79,
DOI [10.7146/math.scand.a-14449](https://doi.org/10.7146/math.scand.a-14449).
The [published PDF](https://journals.msp.org/mscand/article/download/770/769/801)
was checked directly, including its class definition and Bang-degree
normalization on pages 60--62.

In the instance needed here, if a real smooth `u` on `[0,1]` satisfies
`||u^(j)||<=j! A^j`, its Bang degree `n_u` is the largest integer `n` for which

$$
\frac1A\sum_{\log\|u\|_\infty^{-1}<j\le n}\frac1j<e.
$$

The theorem gives

$$
\|u\|_I\le
\left(\frac{4e^5|I|}{|E|}\right)^{2n_u}\|u\|_E,
\qquad E\subset I\subset[0,1].                          \tag{4.1}
$$

The hypotheses hold because `M_j=j! A^j` is log-convex, `M_0=1`,
the function generating it is `A(s)=As`, which is positive, nondecreasing,
and `C^1`, and `sup sA'(s)/A(s)=1`. The defining reciprocal series
diverges, so `n_u` is finite for the nonzero functions used below.

We now derive the required two-dimensional estimate, including all
geometric dependence. Let `f` be any periodic holomorphic function bounded
by four on a strip of width `rho<=1`, and suppose `||f||_infinity>=m>0`
on the real torus. Set

$$
D=2(\lceil\log(4/m)\rceil+2),\qquad K=D e^{8/\rho}.
$$

Then, for `0<epsilon<m`,

$$
\operatorname{area}\{|f|\le\epsilon\}
\le16\pi e^5(\epsilon/m)^{1/(2K)}.                      \tag{4.2}
$$

Choose a real point `x_0` attaining a value of modulus at least `m`, and
rotate `f` so its value there is positive real. Its real part has a
holomorphic extension
`(e^(-i phi)f(z)+e^(i phi)overline(f(overline z)))/2`
bounded by four. Restrict this extension to any ray from `x_0` inside a
convex fundamental square. The ray length is `L<=sqrt2<2`. After rescaling
the ray to `[0,1]` and dividing by four, Cauchy's formula along the entire
ray gives

$$
\|u^{(j)}\|_\infty\le j!(2/\rho)^j,
\qquad |u(0)|\ge m/4.
$$

Let `L_0=ceil(log(4/m))`. For
`n>=ceil((L_0+2)exp(8/rho))`, the harmonic sum from `L_0+1` to `n` is
at least `log((n+1)/(L_0+1))>=8/rho`. Its multiplication by `rho/2`
is at least four, exceeding `e`. Hence `n_u<=K`. Equation (4.1) shows
that the portion of any such ray on which `|f|<=epsilon` has length at most

$$
L\,4e^5(\epsilon/m)^{1/(2K)}.
$$

Finally integrate in polar coordinates about `x_0`. The radius is at most
`sqrt2`, the ray length is at most `sqrt2`, and the angle interval has
length at most `2 pi`. Their product gives the factor `4 pi`, proving
(4.2). This argument also works when `x_0` is on the boundary of the square.

Apply (4.2) to the defect guaranteed by (2.3), using (3.3). With

$$
K_r=D_d\exp(8000\,256^r),\qquad
v=|g_1|^2+|g_2|^2,
$$

one obtains

$$
\operatorname{area}\{v\le2\delta\}
\le16\pi e^5
 \left(\frac{\sqrt{2\delta}}{m_d}\right)^{1/(2K_r)},
\qquad \sqrt{2\delta}<m_d.                              \tag{4.3}
$$

On real points `|g_i|=|f_i|`; thus (4.3) is exactly a bound for the
neighborhood of the fixed set required in the trace argument.

## 5. Quantitative trace cutoff, with all iterate dependence exposed

The elementary Weyl estimates in the frozen trace note are

$$
\begin{split}
\|\operatorname{Op}(a)\operatorname{Op}(b)-\operatorname{Op}(ab)\|
 &\le C N^{-1}|a|_1|b|_1,\\
\|[\operatorname{Op}(a),\operatorname{Op}(b)]\|
 &\le C N^{-1}|a|_1|b|_1,\\
\bigl(N^{-1}\operatorname{Tr}\operatorname{Op}(a)^*
                  \operatorname{Op}(a)\bigr)^{1/2}
 &\le\|a\|_2+C N^{-1}|a|_2,\\
|a|_1&\le C\|a\|_{C^5},\qquad
|a|_2\le C\|a\|_{C^6}.                                  \tag{5.1}
\end{split}
$$

All constants here are absolute. The third estimate follows by separating
the diagonal Fourier terms from aliases `v-w in N Z^2`; for every
off-diagonal alias one frequency has modulus at least `N/2`. The first two
follow directly from the exact Weyl product; the last two are convergent
Fourier sums after five or six integrations by parts.

Write `mu(a)=N^(-1)Tr(Op_N(a)F)`. Cyclicity, (3.6), and the first two
estimates in (5.1) imply, for any smooth `a`, including an `N`-dependent one,

$$
|\mu(a g_i)|\le
C N^{-1}\rho_r^{-3}|a|_1
+10^{12}r\rho_r^{-5}N^{-2}|a|_0.                         \tag{5.2}
$$

The factor `rho_r^(-3)` comes from (3.4) for `|b_i composed with kappa|_1`.
For clarity, subtract `Tr Op(a)F Op(b_i)` from
`Tr Op(a)Op(b_i)F`; cyclicity leaves a commutator with `Op(a)`.
Replace `F Op(b_i)` using the fixed-character Egorov remainder, and replace
the two symbol products using (5.1). This gives (5.2) without propagating
the varying `a` through the dynamics.

Fix once and for all a smooth scalar cutoff `chi` equal to one on
`(-infinity,1]` and zero on `[2,infinity)`, between zero and one. For example,
on `1<s<2` take

$$
\chi(s)=\frac{\eta(2-s)}{\eta(2-s)+\eta(s-1)},\qquad
\eta(t)=\begin{cases}e^{-1/t},&t>0,\\0,&t\le0.\end{cases}
$$

For `0<delta<1` put

$$
\chi_\delta=\chi(v/\delta),\qquad
a_{i,\delta}=(1-\chi_\delta)\overline{g_i}/v,
$$

extending the last expression by zero near `v=0`. The real analytic function
`v` has a holomorphic extension bounded by 32 on the strip of width
`rho_r`, using `overline(g_i(overline z))` for its conjugate factor.
Cauchy's derivative estimates and the ordinary product and chain rules
therefore give

$$
|a_{i,\delta}|_1\le C\delta^{-6}\rho_r^{-5},
\qquad |\chi_\delta|_2\le C\delta^{-6}\rho_r^{-6}.        \tag{5.3}
$$

Here `C` depends only on the displayed scalar cutoff. In a derivative of
total order `j`, the powers of `rho_r^(-1)` sum to exactly `j`; they do not
multiply to `rho_r^(-j^2)`. For `a_i`, at most `j+1` inverse factors of
`delta` occur, and `j<=5`; for the cutoff, at most six occur.

Since `sum a_i g_i=1-chi_delta`, (5.2), (5.3), and the Hilbert--Schmidt
bound in (5.1) prove the following uniform master estimate:

$$
\boxed{\frac{|\operatorname{Tr}F_{g,h,r,N}|}{N}
\le\sqrt{16\pi e^5}
\left(\frac{\sqrt{2\delta}}{m_d}\right)^{1/(4K_r)}
+C(r+1)\rho_r^{-10}N^{-1}\delta^{-6}.}                  \tag{5.4}
$$

It holds for `h!=0` and `sqrt(2 delta)<m_d`. Indeed, before the harmless
weakening in (5.4), the three algebraic errors are bounded by a constant
times

$$
\delta^{-6}
\bigl(N^{-1}\rho_r^{-8}
+rN^{-2}\rho_r^{-10}
+N^{-1}\rho_r^{-6}\bigr).
$$

If `h=0,g!=0` the trace is exactly zero. If `g=0,h!=0`, the same is true
by cyclicity. The identity pair contributes exactly `N`.

## 6. Choosing a genuinely growing horizon

Let `T_N` and `Lambda_N` be as in (1.1). Conditions (1.2) ensure `T_N>=1`
and, uniformly for `1<=r<=T_N`,

$$
8000\,256^r\le\Lambda_N/4,
\qquad \log D_d\le\Lambda_N/4,
\qquad K_r\le e^{\Lambda_N/2}=\sqrt{\log N}.             \tag{6.1}
$$

Choose `delta=N^(-1/48)`. The second condition in (1.2) gives

$$
\log\left(\frac{\sqrt{2\delta}}{m_d}\right)
=\log(\sqrt2/m_d)-\frac{\log N}{96}
\le-\frac{\log N}{192}.
$$

The first term of (5.4) is therefore at most

$$
\sqrt{16\pi e^5}\exp(-\sqrt{\log N}/768).
$$

For the second term,

$$
(r+1)\rho_r^{-10}N^{-1}\delta^{-6}
\le10^{30}(T_N+1)256^{10T_N}N^{-7/8}
\le C\Lambda_N^{11}N^{-7/8},                            \tag{6.2}
$$

because `256^T_N<=Lambda_N/32000` and `T_N+1<=Lambda_N` under (1.2).
This proves the normalized trace bound `mathcal R_N` for every nonidentity
pair simultaneously up to `T_N`.

Expanding the projectors proves (1.4): the identity pair has coefficient
`d^(-4)`, and the sum of the absolute values of all the other coefficients
is `1-d^(-4)<=1`. Negative `r` follow by cyclicity and interchange of the
two projectors. No estimate is averaged over `N`, over a kick, or over
independent phases.

## 7. Effective commutant variance and moving spectral windows

For `B=P_chi-cI`, let

$$
\mathcal A_L(B)=\frac1L\sum_{j=0}^{L-1}U_N^{-j}BU_N^j,
\qquad L=T_N+1.
$$

The zero-lag correlation is exactly
`N^(-1)Tr B^2=c-c^2`; every nonzero lag with absolute value below `L`
has modulus at most `mathcal R_N` by (1.4). Expanding the square yields

$$
\frac1N\|\mathcal A_L(B)\|_{\rm HS}^2
\le\frac{c-c^2}{L}+\mathcal R_N.                        \tag{7.1}
$$

Since the full commutant projection is an orthogonal contraction in
Hilbert--Schmidt norm and `E_U A_L(B)=E_U B`, (7.1) proves (1.5), including
all possible multiplicity blocks.

There is also a quantitative statement for nearby eigenphase pairs, with
their actual matrix-element weights. Define a positive measure on `R/Z` by

$$
\nu_{\chi,N}=
\frac1N\sum_{\lambda,\mu}
 \|\Pi_\lambda B_{\chi,N}\Pi_\mu\|_{\rm HS}^2
 \delta_{(\arg\lambda-\arg\mu)/(2\pi)}.                 \tag{7.2}
$$

This definition is basis independent. Its Fourier coefficients are the
centered sector correlations just used. The elementary Fejer expression

$$
F_L(t)=\left|\frac1L\sum_{j=0}^{L-1}e^{2\pi ijt}\right|^2
$$

satisfies `F_L(t)>=4/pi^2` whenever `dist(t,Z)<=1/(2L)`, by the sine
formula. The same correlation calculation as (7.1), with the added phases
for any center `omega`, gives

$$
\boxed{\sup_{\omega\in\mathbb R/\mathbb Z}
\nu_{\chi,N}\{t:\operatorname{dist}(t,\omega)\le1/(2(T_N+1))\}
\le\frac{\pi^2}{4}
\left(\frac{c-c^2}{T_N+1}+\mathcal R_N\right).}          \tag{7.3}
$$

Thus there is an explicit shrinking window, of order
`1/log log log N`, in which the total normalized centered-sector
matrix-element weight is `O_d(1/log log log N)`, uniformly in the window
center. This estimate applies in particular to any narrower window,
including windows of width `1/N`, but it is still a weighted estimate.

## 8. The exact remaining obstruction

The rate obtained here is deliberately stated at the scale proved. The
global complex strip in Section 3 narrows exponentially with the iterate,
and the verified Remez estimate in Section 4 gives an exponent of size
`exp(-C 256^r)`. These proved estimates require a triple-logarithmic
horizon. They do not establish a logarithmic horizon, much less a time
comparable with `N`.

A first possible route to improve this particular method would be a
quantitative sublevel theorem for the specific maps (2.2) substantially
stronger than (4.3), with full dependence on `r`. Such a theorem is not
proved here. One cannot replace the proved value of `K_r` by a polynomial
in `rho_r^(-1)` merely from the fact that the function is analytic.

Even an improved sector estimate would not identify unweighted eigenphase
statistics: (7.2) assigns matrix-element weights, and no lower bound for
those weights on all close eigenphase pairs is available. Accordingly
(1.4)--(1.5) and (7.3) neither establish `H_diag` nor provide a
counterexample to it. The full weighted products of quantum traces at
indices of order `N` remain unevaluated.
