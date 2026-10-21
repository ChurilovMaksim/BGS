> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_pressure_analytic_potential.md`. Embedded SHA256: `44da5eefab7cce7d7eb222fa54f027eec8a1a545b8ca0c4fd3fcf1fc7520637f`.
> [Thematic guide](../../topics/classical_trace.md).

# An explicit analytic parameter disk for the pulled-back unstable potential

## Scope and input

This note supplies a functional-analytic input for a pressure expansion
of the exact classical family. It does not prove the pressure expansion
or any spectral-statistics assertion.

The ordinary Weyl symbol `a` and the map convention are those of the
frozen `arithmetic_iterated_logarithmic_horizon.md`, SHA-256
`37cae903cc22d77e04ba9848f00fdfd4f19920e9c3a22381de92e965588ce8c6`.
In particular, the corrected symbol has Fourier support
`|k|<=9, |l|<=1`, coefficient l1 norm at most `59/50`, and

$$
X=(a_p,-a_q)/(2\pi),\qquad
\Xi_s=S\Phi_s,\qquad
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},
$$

where `Phi_s` is the flow of `X`. The actual parameter is still
`tau=10^-80`; the complex parameter disk below is a device for proving
derivative bounds at this exact parameter, not a modification of it.

## 1. Statement

Fix any exponent `0<alpha<=1/2`; thus `alpha=1/100` is allowed. There
is a holomorphic family, with values in a fixed complex Holder space,

$$
\psi_s\in C^\alpha(\mathbb T^2;\mathbb C),\qquad
|s|<R:=10^{-16},                                       \tag{1.1}
$$

satisfying

$$
\boxed{\psi_0=\log\lambda,\qquad
\|\psi_s-\log\lambda\|_{C^\alpha}\le10^{11}|s|,
\qquad\lambda=3+2\sqrt2.}                              \tag{1.2}
$$

For real `s`, there is a homeomorphism `H_s`, with
`Xi_s H_s=H_s S`, such that the geometric unstable potential obeys

$$
\log J_s^u\circ H_s
=\psi_s+u_s\circ S-u_s                                \tag{1.3}
$$

for a real continuous (indeed Holder) function `u_s`. Thus `psi_s` is
the coordinate-expansion representative of this pulled-back potential.
Its first variation in the original `(q,p)` coordinates is exactly

$$
\boxed{\left.\partial_s\psi_s\right|_{s=0}
=\xi:=\frac{a_{pp}-2a_{qq}}{4\pi\sqrt2}.}              \tag{1.4}
$$

There is no assumption that a base-dependent invariant section is
analytic in the spatial variable. Spatial regularity throughout is
`C^alpha`; holomorphy refers to the scalar parameter `s` and to the
finite-dimensional spatial arguments of the original vector field.

The norm in (1.2) uses the fixed eigen-coordinate metric defined below.
Switching to the standard torus metric changes the norm by a fixed
factor below two; the generous constant `10^11` includes this change.

## 2. Fixed Holder spaces and the Green operator

Let

$$
Q=\frac1{\sqrt3}\begin{pmatrix}1&\sqrt2\\1&-\sqrt2\end{pmatrix},
\qquad D=QSQ^{-1}=\operatorname{diag}(\lambda,\mu),
\qquad\mu=\lambda^{-1}.
$$

Use `z=Qx=(u,v)`, lattice `Lambda=Q Z^2`, and the quotient distance
of the maximum norm. Its diameter is below one: representatives of
differences in the original coordinates can be chosen in
`[-1/2,1/2]^2`, whose `Q` images have maximum norm below one.
For a complex vector or matrix field, put

$$
\|f\|_\alpha=\sup|f|+
\sup_{z\ne w}\frac{|f(z)-f(w)|}{\operatorname{dist}(z,w)^\alpha}.
$$

Matrix norms are induced row-sum norms. Scalar multiplication and
matrix-vector multiplication obey the Banach algebra inequalities
`||fg||_alpha<=||f||_alpha||g||_alpha`. Also

$$
\|f\circ D^n\|_\alpha\le\lambda^{\alpha|n|}\|f\|_\alpha.
                                                               \tag{2.1}
$$

For a periodic forcing `f`, the equation `w(Dz)-Dw(z)=f(z)` has
Green solution

$$
(\mathcal G f)^u=-\sum_{j\ge0}\lambda^{-j-1}f^u\circ D^j,
\qquad
(\mathcal G f)^v=\sum_{j\ge1}\mu^{j-1}f^v\circ D^{-j}.
                                                               \tag{2.2}
$$

Its supremum norm bound is `(1-mu)^(-1)<5/4`. Its Holder seminorm
bound is the larger of

$$
\frac1{\lambda-\lambda^\alpha},\qquad
\frac{\lambda^\alpha}{1-\lambda^{\alpha-1}}.
$$

For `alpha<=1/2`, both are less than five. The second is at most
`lambda/(sqrt(lambda)-1)=lambda/sqrt2<5`. Hence

$$
\boxed{\|\mathcal G\|_{C^\alpha\to C^\alpha}\le5.}       \tag{2.3}
$$

Convergence in this fixed Holder norm, rather than in an analytic
space of base variables, is the point of this construction.

## 3. A common complex spatial tube and parameter disk

The finite Fourier polynomial gives, on `max|Im x_i|<1/100`,

$$
\|X\|\le22,\qquad\|DX\|\le2000,\qquad\|D^2X\|\le10^5.
                                                               \tag{3.1}
$$

For example the last bound is
`2*(59/50)*9*(2*pi*10)^2<10^5`. The first two calculations are in
the input note. For complex `|s|<=10^-8` and `max|Im z_i|<10^-4`,
the integral equation
`Phi_s(x)=x+s integral_0^1 X(Phi_(ts)(x))dt` stays inside this
spatial strip: its displacement is at most `22|s|`, and
`|Im Q^-1 z|<2*10^-4`. Picard iteration there is a contraction;
it proves joint holomorphy in the complex time and spatial variables.
Its first two variational equations give

$$
\|\Phi_s-\mathrm{Id}\|\le22|s|,\quad
\|D\Phi_s-I\|\le4000|s|,\quad
\|D^2\Phi_s\|\le2\cdot10^5|s|.                         \tag{3.2}
$$

Indeed `exp(2000|s|)<2`, and the second-variation integral is bounded
by `10^5|s| exp(6000|s|)<2*10^5|s|`. The same bounds justify the
domain throughout the iteration and variational equations.

Write the eigen-coordinate lift as

$$
F_s:=Q\Xi_sQ^{-1}=D+V_s.
$$

Using `||Q||,||Q^-1||<2` and `||S||=7`, (3.2) proves on that fixed
tube, for `|s|<=10^-8`,

$$
\boxed{\|V_s\|,\|DV_s\|,\|D^2V_s\|\le M|s|,
\qquad M=10^9.}                                       \tag{3.3}
$$

The individual elementary bounds are already much smaller: the
second-derivative one is below `2*7*4*2*10^5|s|`.
All `V_s` are periodic under `Lambda`. The determinant of `DF_s` is
one even at complex arguments: the derivative of the flow determinant
is `div(X)` times that determinant, and `div(X)=0` identically.

## 4. Analytic structural conjugacy in C^alpha

Let `mathcal B` be the complex Holder ball `||w||_alpha<=10^-5`.
For `|s|<R=10^-16`, consider

$$
\mathcal C_s(w)=\mathcal G\bigl(V_s\circ(\mathrm{Id}+w)\bigr).
                                                               \tag{4.1}
$$

The spatial arguments stay within the tube of (3.3). For a pair of
torus points, choose their shortest lift difference. The mean value
formula in the complex tube bounds the Holder seminorm of the
composition using
`|z-w|^(1-alpha)<=1` and the seminorm of `w`. Consequently

$$
\|V_s\circ(\mathrm{Id}+w)\|_\alpha
\le3M|s|,\qquad
\|DV_s\circ(\mathrm{Id}+w)\|_\alpha\le3M|s|.            \tag{4.2}
$$

For the second inequality use the second derivative in (3.3).
The integral mean value formula and the Banach algebra bound therefore
give

$$
\|\mathcal C_s(w_1)-\mathcal C_s(w_2)\|_\alpha
\le15M|s|\,\|w_1-w_2\|_\alpha.
$$

Thus its contraction constant is at most `1.5*10^-6`, and its image
has norm at most `15MR=1.5*10^-6<10^-5`. It has a unique fixed point
`w_s`, with

$$
\|w_s\|_\alpha\le15M|s|\le2\cdot10^{10}|s|.             \tag{4.3}
$$

The composition in (4.1) is holomorphic as a map of the complex
Banach variables. To justify this without an implicit smoothness
assumption, expand the original holomorphic `V_s(z+w+h)` in `h`
inside the reserved spatial margin. Cauchy's inequalities bound each
coefficient and its Holder seminorm by a geometric constant times
the corresponding inverse margin power. The Banach algebra inequality
then makes that Taylor series converge in `C^alpha` for sufficiently
small `||h||_alpha`. The bounds are uniform on the present ball.
The same argument applies jointly in `s`.

Iterate (4.1) from zero. Each iterate is Banach-valued holomorphic
in `s`, and the uniform contraction makes the iterates converge in
Holder norm locally uniformly in the parameter disk. The limit is
holomorphic: the Cauchy integral formula passes to the uniform limit
in the Banach norm and gives its derivative. No differentiation in
the spatial base is needed.

The Green equation shows that `H_s=Id+w_s` satisfies

$$
F_s H_s=H_s D.                                         \tag{4.4}
$$

For real `s`, this is a real homeomorphism. One direct verification
is the bounded Green argument in Section 3 of the logarithmic input:
construct the reverse semiconjugacy along `F_s` with forcing `-V_s`.
Both compositions have bounded displacement; one is forced to be
identity by expansion and contraction of `D`, and the other by the
two-sided Green inequality. Its needed smallness is
`(1-mu)^(-1)||DV_s||<1`, which here is below `2*10^-7`.
This proves invertibility without differentiating the Holder map.

## 5. An analytic unstable section over the fixed base

The pulled-back derivative cocycle is

$$
A_s(z)=DF_s(H_s z)=D+B_s(z).
$$

The composition argument in (4.2) and (4.3) gives

$$
\|B_s\|_\alpha\le3M|s|\le10^{10}|s|=:a_s.              \tag{5.1}
$$

It is a holomorphic parameter family in the same fixed Holder space,
and `a_s<=10^-6`. Consider an unstable vector `(1,eta_s(z))`.
Its projective invariance is the fixed-point equation

$$
(\mathcal T_s\eta)(z)=
\left[\frac{B_s^{21}+(\mu+B_s^{22})\eta}
{\lambda+B_s^{11}+B_s^{12}\eta}\right](D^{-1}z).        \tag{5.2}
$$

On the Holder ball `||eta||_alpha<=10^-4`, the denominator is
invertible in the Banach algebra and its inverse norm is below `1/5`,
by a Neumann series. The derivative of the fraction with respect
to `eta` is exactly the reciprocal of its denominator squared,
because `det A_s=1`. It has Holder norm at most `1/25`.
Composition with `D^-1` costs at most `lambda^alpha<3`. Hence

$$
\|\mathcal T_s\eta_1-\mathcal T_s\eta_2\|_\alpha
\le(3/25)\|\eta_1-\eta_2\|_\alpha.                     \tag{5.3}
$$

Moreover `||T_s0||_alpha<=3a_s/5`, so this ball is invariant and
the fixed point satisfies

$$
\|\eta_s\|_\alpha\le\frac{3/5}{1-3/25}a_s<a_s.         \tag{5.4}
$$

The same holomorphic-contraction argument as in Section 4 proves
holomorphy in `s`. The base of (5.2) is the fixed map `D`; no
parameter-dependent composition of arbitrary Holder sections occurs.

Define the coordinate multiplier

$$
b_s(z)=\lambda+B_s^{11}(z)+B_s^{12}(z)\eta_s(z).         \tag{5.5}
$$

Then
`A_s(z)(1,eta_s(z))=b_s(z)(1,eta_s(Dz))`. Its deviation from lambda
has Holder norm at most `2a_s`. Therefore the convergent Banach-algebra
logarithm series gives a holomorphic potential

$$
\psi_s=\log\lambda+
\log\left(1+(b_s-\lambda)/\lambda\right),
\qquad\|\psi_s-\log\lambda\|_\alpha<a_s.               \tag{5.6}
$$

The weaker bound (1.2) includes coordinate-norm changes with room to
spare. This construction proves the promised parameter analyticity
using only Holder spatial regularity.

## 6. Geometric meaning and the exact first variation

For real `s`, the multiplier `b_s` is positive and exceeds five. Its
invariant direction is unstable: inverse iteration of that direction
contracts by the product of its reciprocal multipliers, with uniformly
bounded endpoint vector norms.

Let `v_s(z)=Q^-1(1,eta_s(z))` in the physical Euclidean metric and
put `u_s(z)=log||v_s(z)||`. The cocycle identity gives exactly

$$
\log J_s^u(H_s z)=\log b_s(z)+u_s(Dz)-u_s(z).            \tag{6.1}
$$

Returning to the original torus coordinates proves (1.3). The
cohomology is exact, not an error estimate. No theorem on pressure
is being invoked at this point.

At `s=0`, `H_0=Id`, `eta_0=0`, and `B_0=0`. Since `DF_0=D` is
spatially constant, differentiating the pulled-back derivative
cocycle introduces no term from `partial_s H_s`. Equivalently,
the extra composition contribution is quadratic because both
`DV_s` and `w_s` vanish at zero. Thus

$$
\partial_s A_s|_0=D\,Q(DX)Q^{-1},\qquad
\partial_s\log b_s|_0=\ell_u(DX)Q^{-1}e_u.             \tag{6.2}
$$

Here `ell_u=(1,sqrt2)/sqrt3` and
`Q^-1 e_u=(sqrt3/2,sqrt3/(2sqrt2))`. Also

$$
DX=\frac1{2\pi}
\begin{pmatrix}a_{pq}&a_{pp}\\-a_{qq}&-a_{qp}\end{pmatrix}.
$$

Multiplying in (6.2), the mixed derivatives cancel and give
`(a_pp-2a_qq)/(4*pi*sqrt2)`, proving (1.4).
The first variation of the geometric norm potential itself can
include the derivative of the coboundary in (6.1); (1.4) is exact
for the explicitly selected coordinate-expansion representative.

## 7. A usable Taylor remainder and remaining task

The quotient `(psi_s-psi_0)/s` extends holomorphically to zero and
has norm at most `10^11` on the disk of radius `R`. Cauchy's formula
and a geometric sum therefore give, for `|s|<=R/2`,

$$
\boxed{\left\|\psi_s-\psi_0-s\xi-
\frac{s^2}{2}\partial_s^2\psi_s|_0\right\|_\alpha
\le2\cdot10^{11}R^{-2}|s|^3
=2\cdot10^{43}|s|^3.}                                 \tag{7.1}
$$

This is a remainder for the potential, not yet for its pressure.
At `s=tau=10^-80`, its bound is `2*10^-197`. A rigorous pressure
remainder additionally requires a quantified perturbation theorem
for the pressure functional on this fixed Holder space (or an
appropriate coded/transfer space), with its hypotheses and constants
checked. That step is not supplied by parameter analyticity alone
and is not claimed here.
