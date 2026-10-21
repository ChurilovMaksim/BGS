> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/root_uniform_translation_contact.md`. Embedded SHA256: `257afa4511da2fae8bd9260cc33a654bf045115f80aa0861bb8eae6a4f92347e`.
> [Thematic guide](../../topics/classical_trace.md).

# Uniform finite contact, including infinitesimal translations

Research continuation, 20 October 2026. This note concerns the exact
Egorov map of the original fixed-parameter quantum family. Its purpose
is to remove a dependence on a fixed nonzero translation that otherwise
prevents a uniform estimate for growing arithmetic denominators.

The result below is classical. It does not establish a local spectral
limit. Its application to iterated quantum traces also requires the
finite-curve and Egorov arguments in the companion note.

## 1. Actual map and previously proved inputs

Write
$$
F=S\circ\Phi_\tau,\qquad
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\qquad
\lambda=3+2\sqrt2,\qquad \rho=\lambda^{-1},
$$
where $\tau=10^{-80}$, and $\Phi$ is the flow of the corrected
ordinary Weyl symbol, with the convention in
arithmetic_iterated_sector_covariance.md. This F is the inverse of the
physical map used in the pressure notes.

The following already proved inputs are used.

* F has an equivariant analytic lift $F(x)=Sx+v(x)$, with periodic v.
  On a fixed complex neighborhood of the real torus its first and
  second derivatives are smaller than $10^{-50}$. This relaxed
  bound follows from the finite Fourier polynomial and the explicit
  short-time flow estimates. In the fixed eigen-coordinate norm
  $\|DF\|<6$.
* The bounded two-sided Green construction gives an equivariant
  homeomorphism $G=\operatorname{Id}+\text{periodic}$, satisfying
  $G F=S G$. Apply the construction in fermionic_pressure_transfer.md
  to the inverse map.
* With $\ell S=\lambda\ell$,
  $$
  H_u(x)=\ell G(x)=\ell x+v_\infty(x)
  $$
  also equals the limit of $\lambda^{-r}\ell F^r(x)$. The two Fourier
  coefficients of the periodic scalar $v_\infty$ at $(1,0),(0,1)$
  in the original torus coordinates are nonzero. The uniform estimates
  for $v_r$ in arithmetic_iterated_sector_covariance.md give their
  absolute values at least $\tau/800$, and the discounted sum
  converges uniformly as r tends to infinity.

All three properties refer to the original map at the original fixed
tau. No genericity condition is added here.

Choose fixed eigenvectors $e_s,e_u$ of S, of eigenvalues $\rho,\lambda$.
All norms below are equivalent fixed norms. The distance
$|h|_{\mathbb T}$ is that of the shortest representative of a torus
translation. Changing between original and eigen-coordinates changes
only constants.

## 2. C1 dependence of stable graphs in a fixed holomorphic space

This is stronger than the separate facts that the stable line field
is C1 and individual leaves are analytic. The stronger assertion is
needed for the infinitesimal argument.

Choose a fixed disk $D_R=\{|t|<R\}$ so small that the points
$x+t e_s+y e_u$, for real x and
$|t|<R,\ |y|\le10^{-40}|t|$, remain in the reserved complex
neighborhood. Use the Banach space
$$
\mathcal A_R=\{\gamma\text{ holomorphic on }D_R:\gamma(0)=0,\quad
 \|\gamma\|_*:=\sup_{0<|t|<R}|\gamma(t)|/|t|<\infty\}.
$$
Let $\mathcal B$ be its closed ball of radius $10^{-40}$. We construct
stable graphs
$$
\mathcal L_x(t)=x+t e_s+\gamma_x(t)e_u.                 \tag{2.1}
$$

For an input graph $\eta\in\mathcal B$ based at Fx, its inverse image
through x is determined by
$$
\gamma(t)=\lambda^{-1}\left[
\eta\!\left(\rho t+
v_s(x+t e_s+\gamma(t)e_u)-v_s(x)\right)
-\left(v_u(x+t e_s+\gamma(t)e_u)-v_u(x)\right)\right]. \tag{2.2}
$$
Denote its solution by $\mathcal G_x\eta$. The argument of eta has
absolute value at most $0.18|t|$. Cauchy's inequality applied to
$\eta(t)/t$ gives $|\eta'|\le2\cdot10^{-40}$ there. Hence (2.2),
as an iteration in gamma, contracts with constant less than $10^{-49}$
and maps $\mathcal B$ into itself. Its iterates and limit are holomorphic.

For two inputs the direct change on the right side is at most
$0.18\lambda^{-1}\|\eta_1-\eta_2\|_*|t|$. Absorbing the preceding
implicit-contraction error gives
$$
\|\mathcal G_x\eta_1-\mathcal G_x\eta_2\|_*
 \le q\|\eta_1-\eta_2\|_*,
 \qquad q<1/25.                                     \tag{2.3}
$$
There is a fixed margin between $0.18R$ and R. Cauchy's inequalities
on this margin, together with the derivatives of v, show that
$(x,\eta)\mapsto\mathcal G_x\eta$ is continuously differentiable in
real x and in eta, into $\mathcal A_R$. Its derivatives are locally
Lipschitz with uniform constants. This follows directly by differentiating
the convergent iteration of (2.2): each differentiated iteration has the
same implicit-contraction constant; its forcing is bounded by Cauchy
estimates on the smaller input disk. One further differentiation gives
the local Lipschitz bounds. No disk shrinks with the number of iterates.

Starting with the zero section, iterate
$$
\Gamma_{n+1}(x)=\mathcal G_x(\Gamma_n(Fx)).             \tag{2.4}
$$
The contraction gives a continuous limiting section $\gamma_x$.
Differentiating gives
$$
D\Gamma_{n+1}(x)
=\partial_x\mathcal G_x(\Gamma_n(Fx))
+D_\eta\mathcal G_x(\Gamma_n(Fx))D\Gamma_n(Fx)DF(x).   \tag{2.5}
$$
Since $q\|DF\|\le6/25<1$, this first bounds all $D\Gamma_n$.
Subtract consecutive equations and use the local Lipschitz bounds:
$$
\|D\Gamma_{n+1}-D\Gamma_n\|_\infty
\le(6/25)\|D\Gamma_n-D\Gamma_{n-1}\|_\infty+Cq^n.     \tag{2.6}
$$
The resulting sequence of differences is summable. Thus the section
is C1 in x with values in the fixed holomorphic space. The same
formulas and the small derivatives of v give
$\sup_x\|D_x\gamma_x\|_*\ll1$.

Equation (2.2) gives invariance. The stable coordinate contracts by
at least a factor 0.18 under F, so these graphs are the local stable
leaves. Their real continuations are global graphs over the stable
coordinate: the stable vector field has stable component one and
bounded unstable component, so its integral curves extend for every
real stable coordinate. Overlapping the uniformly analytic local
graphs makes these continuations real analytic.

The conjugacy G maps these global stable leaves onto straight stable
leaves of S. The stable eigendirection has irrational slope, so each
leaf is dense after projection to the torus.

## 3. Neither a foliation symmetry nor a single coincident germ

Suppose $t_h$ preserves the stable foliation. In the G coordinates
it induces a continuous map zeta of the real leaf-coordinate line:
$$
H_u(x+h)=\zeta(H_u(x)).                              \tag{3.1}
$$
Equivariance gives $\zeta(t+\ell n)=\zeta(t)+\ell n$ for all integer n.
Since $\ell(\mathbb Z^2)$ is dense, $\zeta(t)-t$ is constant.
Integrating the periodic part of (3.1) over the torus identifies that
constant as $\ell h$, and hence
$$
v_\infty(x+h)=v_\infty(x).                          \tag{3.2}
$$
The two specified Fourier coefficients force both coordinates of h
to be integers. Thus h is zero as a torus translation.

If the translate of a stable leaf agrees with another stable leaf
on an open segment, their global real analytic graphs agree by
analytic continuation on the real line. Write sigma for the unstable
component of the stable vector field. The agreement gives
$\sigma(y+h)=\sigma(y)$ along a dense leaf. Continuity extends this
identity to the whole torus. The translation then preserves the line
field and its foliation, which the preceding paragraph excludes for
nonzero h.

## 4. Infinitesimal coincidences also do not occur

Set $\sigma(x)=\partial_t\gamma_x(0)$. Section 2 makes this C1.
For a constant vector w set $z_w(t)=D_x\gamma_x(t)w$, holomorphic
on the fixed disk. Differentiate
$\sigma(\mathcal L_x(t))=\partial_t\gamma_x(t)$ in direction w:
$$
D\sigma(\mathcal L_x(t))w
=z_w'(t)-\partial_u\sigma(\mathcal L_x(t))z_w(t).     \tag{4.1}
$$
With $w=e_u$, this gives
$$
\partial_u\sigma(\mathcal L_x(t))
=\frac{z_{e_u}'(t)}{1+z_{e_u}(t)}.                  \tag{4.2}
$$
The denominator is nonzero on a fixed smaller disk, by the small
derivative bound. Consequently $D\sigma(\cdot)w$ is real analytic
along every stable leaf. This uses C1 dependence in the holomorphic
space, and does not follow merely from separately C1 and analytic
regularity.

If $D_x\gamma_x(t)w$ were identically zero on one disk, (4.1)
would make $D\sigma(\cdot)w$ zero on a leaf segment. Analytic
continuation extends the identity along the full connected leaf.
Density and continuity then give $D\sigma(y)w=0$ everywhere.
Integrating along the lines $y+sw$ shows that every $t_{sw}$
preserves the stable line field. Section 3 forces $sw=0$ on the
torus for every real s, so $w=0$. Thus
$$
\boxed{D_x\gamma_x(\cdot)w\equiv0\ \Longrightarrow\ w=0.} \tag{4.3}
$$

## 5. Uniform finite contact down to h=0

Fix a small $z_0>0$ within the local chart range. For
$x,h\in\mathbb T^2,\ |z|\le z_0$, define
$$
F_{x,h,z}(t)=\gamma_x(t)-z-\gamma_{x+h+z e_u}(t).    \tag{5.1}
$$
This compares the translate by h of the leaf through x with the
stable graph meeting the same stable-coordinate axis at an additional
unstable displacement z. In particular $F_{x,h,z}(0)=-z$.

Normalize by $a=|h|_{\mathbb T}+|z|>0$. The normalized functions
have compact closure in the holomorphic norm on a fixed smaller disk.
Away from $(h,z)=(0,0)$ this follows from compact-parameter continuity.
Near that point choose the shortest representative of h, pass to
directions $h/a\to w,\ z/a\to z_*$, and use the C1 holomorphic-space
dependence. The limiting functions are
$$
-z_*-D_x\gamma_x(t)(w+z_*e_u),
\qquad |w|+|z_*|=1.                                \tag{5.2}
$$
No member of this compact closure is identically zero. For actual
nonzero parameters, the value at zero detects z, and Section 3
excludes the remaining finite h. For (5.2), the value at zero is
$-z_*$, since $D_x\gamma_x(0)=0$. If this is zero, (4.3) detects
the remaining nonzero vector w.

At every real point, a nonzero holomorphic function has a nonzero
derivative of some finite order. Compactness of this closure, also
with respect to the point in a fixed compact interval
$I\subset(-R,R)$, gives one finite integer J and one c>0 such that
$$
\boxed{
\max_{0\le j\le J}|\partial_t^jF_{x,h,z}(t)|
\ge c(|h|_{\mathbb T}+|z|)
\ge c|h|_{\mathbb T}
}\qquad(t\in I).                                  \tag{5.3}
$$
Cauchy's inequalities give uniform bounds on all fixed derivatives
of the normalized family on slightly larger compact intervals.
J,c depend on the original map and chart, not on h or on an arithmetic
denominator.

## 6. Relative sublevel bound

Here is the elementary finite-derivative step. Suppose a family of
real functions has a common upper bound on derivatives through J+1
and satisfies $\max_{0\le j\le J}|f^{(j)}|\ge c$ pointwise. Cover the
fixed interval by a bounded number of pieces on each of which one
specified derivative has absolute value at least c/2. Uniform
derivative bounds make the number of pieces uniform.

On a piece with derivative order $j\ge1$, a sublevel set
$\{|f|\le u\}$ of length a contains j+1 ordered points separated
successively by at least $a/(2j+2)$. This follows by choosing
equal-measure quantiles, with arbitrarily small endpoint adjustments.
The divided-difference formula bounds their j-th divided difference
by $C_jua^{-j}$. Repeated Rolle's theorem identifies it with
$f^{(j)}(\xi)/j!$. Thus $a\le C_j(u/c)^{1/j}$.
Order zero excludes the sublevel set when u is small. Summing the
bounded number of pieces gives exponent $\beta=1/J$, with the
trivial length bound for large u.

Apply this to the normalized functions in Section 5. Fixed
$C,\beta>0$ satisfy
$$
\boxed{
\left|\{t\in I:|F_{x,h,z}(t)|\le\epsilon\}\right|
\le C\min\left\{1,
  \left(\frac{\epsilon}{|h|_{\mathbb T}}\right)^\beta\right\}
}\quad(h\ne0).                                    \tag{6.1}
$$
This remains true under an error whose derivatives through J are
at most $(c/2)|h|_{\mathbb T}$, provided its normalized derivatives
through J+1 remain uniformly bounded. Use the same argument with
c/2 in place of c.

## 7. A relative backward-graph error

This supplies the quantitative observation needed for finite
iterated curves; it does not replace their counting argument.
Suppose the ORIGINAL translated-return sublevel set is nonempty:
for at least one y,
$$
\operatorname{dist}_{\mathbb T}
 \bigl(F^r(y+h),F^r(y)-g\bigr)\le\epsilon.
$$
Then
$$
|g|_{\mathbb T}\le6^r|h|_{\mathbb T}+\epsilon.       \tag{7.1}
$$
At any center z of the finite target stable segment, its translate
by -g has graph $\gamma_z$ based at $z-g$; the actual stable
graph there is $\gamma_{z-g}$. Their initial holomorphic-norm
difference is at most $C|g|_{\mathbb T}$. Inverse graph contraction
and Cauchy's inequalities on fixed smaller disks bound the Cj error
after r inverse iterates, for every fixed j, by $C_j8^{-r}|g|_{\mathbb T}$.
The relaxed base 8 is smaller than the available graph contraction
base and satisfies $8>6$. Therefore
$$
C_j8^{-r}|g|_{\mathbb T}
 \le C_j(6/8)^r|h|_{\mathbb T}+C_j8^{-r}\epsilon.    \tag{7.2}
$$
For $\epsilon\le c_0|h|_{\mathbb T}$, one fixed threshold on r,
independent of h,g, makes this error small enough for the relative
contact estimate. For larger epsilon, the intended sublevel bound
is already trivial after increasing the constant.

Derive (7.1) from an actual original-set point BEFORE enlarging
the set to a tube union. An arbitrary tube intersection alone
does not justify (7.1). Any global leaf extension is used only for
analytic charts: the counting argument must retain the finite
target segment. The full global leaf is dense and is not a valid
finite target for a tube-volume estimate.

## 8. Scope

The proved new assertions are (5.3), (6.1), and (7.2). The actual
Fourier rigidity excludes even the limiting infinitesimal symmetries.
The passage to a uniform logarithmic quantum horizon is separate
and must include finite-segment counting and coordinate Egorov
bounds. No estimate for signed trace products at times of order N
is claimed here.

