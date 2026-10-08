# Independent follow-up audit: sharp scalar jet and real-flow scalar source

## Verdict

Both proposed partial statements are valid, with the conventions specified below. The scalar constant `4/3` is sharp as a leading universal constant. The source conclusion is an absorbed **L1 comparison of unweighted scalar traces along a real unitary flow**. It does not, by itself, compare anisotropic absorption `exp(-sH/m)`, give mixed moments, or identify a limiting scalar spectral law.

## 1. Sharp scalar circle-integrated second jet

Let

\[
F(z)=c\,z\prod_{j=1}^{d-1} b_{a_j}(z),\qquad |c|=1,\quad |a_j|<1,
\]

and let `dmu=dtheta/(2pi)`. Its boundary delay is

\[
T(\theta)=\overline{F(e^{i\theta})}\,e^{i\theta}F'(e^{i\theta})
=1+\sum_{j=1}^{d-1}p_{a_j}(\theta)\ge1,
\qquad \int T\,d\mu=d.
\]

Include the constant Poisson factor `p_0=1`. The scalar differentiation identity is

\[
\overline F z^2F''=T^2-T-iT',
\]

so

\[
\frac{|F''|^2}{T}=T^3-2T^2+T+\frac{T'^2}{T}.
\]

Weighted pointwise Cauchy gives

\[
\frac{T'^2}{T}
=\frac{(\sum_{j=0}^{d-1}p_j')^2}{\sum_{j=0}^{d-1}p_j}
\le\sum_{j=0}^{d-1}\frac{p_j'^2}{p_j}.
\]

For `r=|a|`, direct Poisson-circle integration gives

\[
M_2=\int p_a^2\,d\mu=\frac{1+r^2}{1-r^2},\qquad
M_3=\int p_a^3\,d\mu=\frac{1+4r^2+r^4}{(1-r^2)^2},
\]

\[
\int\frac{p_a'^2}{p_a}\,d\mu
=\frac{2r^2}{(1-r^2)^2}
=\frac{M_3-1}{3}.
\]

For example, the last integral can be checked without differentiating an integral parameter: with `q=1-2r cos(theta)+r^2` and `p=(1-r^2)/q`,

\[
(\log p)''=\frac{1+r^2}{1-r^2}p-p^2.
\]

Integration by parts gives `int p'^2/p = M_3-M_2^2`, which equals the displayed value.

Since all factors are nonnegative, `sum_j p_j^3 <= T^3`. Integrating the Cauchy bound therefore gives

\[
\int\frac{T'^2}{T}\,d\mu\le\frac13\left(\int T^3\,d\mu-d\right).
\]

Consequently the proposed refinement is rigorous:

\[
\boxed{\int\frac{|F''|^2}{T}\,d\mu
\le\frac43\int T^3\,d\mu-2\int T^2\,d\mu+\frac23\int T\,d\mu.}
\]

Because `T>=1`, the correction `-2 int T^2 +(2/3)int T` is strictly negative, so the result is strictly below `(4/3) int T^3`. At `F(z)=cz`, the refined right side and left side are both zero.

### Sharpness

Take `F_r(z)=z b_r(z)`, `r` real and increasing to one. Then `T=1+p_r`,

\[
\int T^3=M_3+3M_2+4,\qquad
\int (T^3-2T^2+T)=M_3+M_2.
\]

Let `J=int p_r'^2/(1+p_r)`. The loss from the exact Poisson integral is

\[
0\le\int\frac{p_r'^2}{p_r}-J
=\int\frac{p_r'^2}{p_r(1+p_r)}
\le\int\left(\frac{p_r'}{p_r}\right)^2
=\frac{2r^2}{1-r^2}.
\]

The final identity follows from the Fourier series of `log p_r`; its derivative has sine coefficients `-2r^n`. Since `M_3` has order `(1-r^2)^(-2)` whereas `M_2` and the loss have order `(1-r^2)^(-1)`,

\[
\frac{\int |F_r''|^2/T}{\int T^3}\longrightarrow\frac43.
\]

No smaller universal leading coefficient is possible. This establishes sharpness for the scalar class; it makes no corresponding claim for the matrix-valued constant in Theorem 89.2.

## 2. Direct real-flow scalar source consequence

Assume `H=H*` is deterministic and independent of `D`, with

\[
\operatorname{Tr}H=m,\qquad \operatorname{Tr}H^2\le C_Hm.
\]

Write `K=H-I`, so `Tr K=0` and `||K||_F^2 <= m(C_H-1)`. Define

\[
W_x=DS\exp(i xH/m),\qquad V_x=e^{ix/m}DS,
\]

and assume, uniformly for `|x|<=R`,

\[
\|\mathbb E_D E_{W_x}\|_{\rm traceless\to traceless}\le\beta.
\]

Here `E_W` is full eigenspace pinching; eigenvalue degeneracies are allowed.

Choose continuous unwrapped eigenphase branches `theta_j(x)` of the analytic unitary flow `W_x`, matching their initial phases at zero. The scalar flow has phases `theta_j(0)+x/m`. At regular points,

\[
\sum_{j=1}^m(\theta_j'(x)-1/m)^2
=\frac1{m^2}\|E_{W_x}K\|_F^2.
\]

This also holds almost everywhere with repeated eigenvalues: their derivatives are the eigenvalues of the compressed generator on the full degenerate eigenspace, and the sum of their squares is its Frobenius-square trace. Rellich branches, or standard absolutely continuous spectral-flow branches, supply the needed matching.

Since eigenspace pinching is an orthogonal projection,

\[
\mathbb E_D\|E_{W_x}K\|_F^2
=\langle K,(\mathbb E_DE_{W_x})K\rangle
\le\beta\|K\|_F^2.
\]

Integrating velocities and using Cauchy--Schwarz in the branch index and probability gives

\[
\boxed{\mathbb E_D\sum_{j=1}^m
|\theta_j(x)-\theta_j(0)-x/m|
\le |x|\sqrt{(C_H-1)\beta}.}
\]

This is the expected mean matching distance when microscopic angular distance is measured in units `m times radians`: `(1/m)sum_j m|Delta theta_j|`. The optimal circle matching distance is at most this explicit branch matching distance. If unfolded coordinates instead use `m theta/(2pi)`, divide the distance bound by `2pi`.

### Absorbed resolvent estimate

For `Re s=a>0`, put `r=exp(-a/m)` and

\[
k_r(t)=\frac1{1-r e^{it}}.
\]

The imaginary part of `s` only translates the angular argument. With normalized circle measure,

\[
\|k_r'\|_{L^1(d\mu)}
=\int\frac{r}{|1-r e^{it}|^2}\,d\mu(t)
=\frac{r}{1-r^2}
=\frac1{2\sinh(a/m)}\le\frac{m}{2a}.
\]

For every phase displacement `h`, the fundamental theorem of calculus and translation invariance give

\[
\int|k_r(t+h)-k_r(t)|\,d\mu(t)\le |h|\|k_r'\|_1.
\]

The joint law of `(W_x,V_x)` has a uniform common phase: write `D=e^{it}\widetilde D`, where `t` is independent uniform and the remaining relative phases form `widetilde D`. The pinching, branch velocities, and phase displacements are invariant under this common rotation. Averaging first over this phase, applying the branch matching inequality, and then averaging over relative phases yields

\[
\boxed{\mathbb E_D\left|
\frac1m\operatorname{Tr}\left[(I-e^{-s/m}W_x)^{-1}
-(I-e^{-s/m}V_x)^{-1}\right]\right|
\le\frac{|x|}{2\operatorname{Re}s}\sqrt{(C_H-1)\beta}.}
\]

This conclusion needs no positivity of `H`, because `x` is real and both flows are unitary. Its constant and normalization are correct. If Theorem 89.1 supplies `beta=O_rho(log log(1/delta)/log(1/delta))` uniformly along this real flow, the displayed L1 difference is of order the square root of that rate for fixed `x,s,C_H`.

No complex-flow continuation, anisotropically absorbed source theorem, higher mixed moments, or spectral-law identification has been used in this direct argument.
