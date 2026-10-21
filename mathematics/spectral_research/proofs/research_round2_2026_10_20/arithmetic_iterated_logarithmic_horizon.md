> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_iterated_logarithmic_horizon.md`. Embedded SHA256: `37cae903cc22d77e04ba9848f00fdfd4f19920e9c3a22381de92e965588ce8c6`.
> [Thematic guide](../../topics/arithmetic.md).

# A logarithmic sector horizon from finite contact of exact stable curves

## Scope and immutable inputs

This note concerns the exact matrices in the question, always with the fixed
value `tau=10^-80`. It improves the arithmetic-sector horizon to a positive
constant times `log N`, for each fixed square divisor. Its exponent and time
constant are not asserted uniform over growing divisors. It does not prove
`H_diag` or identify unweighted eigenphase statistics.

The following proved inputs are read without alteration.

| Input | SHA-256 |
|---|---|
| `arithmetic_iterated_sector_covariance.md` | `c8e02b81819350ab52e7bc3dd791ffbeb1ae1a2192a9a99f1168c4c56d7123e2` |
| `arithmetic_iterated_effective_horizon.md` | `9739e62cc9a4282d39b379c50835f05fd3d46d664663cf6032b3337857751768` |
| `root_quantitative_trace_and_sectors.md` | `0a174f5de9d070c31311f4fdfd4ebc58b15df0b6bfd86baf5d6f169a99b2ef6a` |
| `fermionic_pressure_transfer.md` | `90ebc84c3c9fb7c049a1a9d11e0d5dcb72c4fc89b362da3f848521a7bca79756` |

The Green-conjugacy construction from the last input is reproduced below,
with the present convention for the classical map; that input's physical
map is our inverse. No differentiability of the topological conjugacy is
assumed.

## 1. Assertion and conventions

Fix odd `d>=3`, write `N=d^2 m` with odd `m`, and define the exact group
representation and its character projectors by

$$
G_N(\alpha,\beta)=T_N(dm\alpha,dm\beta),\qquad
P_{\chi,N}=d^{-2}\sum_{g\in(\mathbb Z/d\mathbb Z)^2}
                      \overline{\chi(g)}G_N(g),\qquad c=d^{-2}.
$$

Each projector has rank `cN`. There are a positive integer `M_d` and
constants `C_d,N_d` such that, setting

$$
T_{d,N}=\left\lfloor\frac{\log N}{1024M_d}\right\rfloor,       \tag{1.1}
$$

for all `N>=N_d`, all characters, and `1<=|r|<=T_(d,N)`,

$$
\boxed{\left|N^{-1}\operatorname{Tr}
(P_{\chi,N}U_N^{-r}P_{\eta,N}U_N^r)-c^2\right|
\le C_dN^{-1/(384M_d)}.}                                    \tag{1.2}
$$

For the orthogonal projection onto the full matrix commutant,
`E_U(B)=sum_zeta Pi_zeta B Pi_zeta`, this implies

$$
\boxed{N^{-1}\|\mathcal E_{U_N}(P_{\chi,N})-cI\|_{\rm HS}^2
\le\frac{c-c^2}{T_{d,N}+1}+C_dN^{-1/(384M_d)}
=O_d((\log N)^{-1}).}                                     \tag{1.3}
$$

Repeated eigenvalues are allowed. Section 11 gives a terminating
finite-certification description of admissible constants; no numerical
value of `M_d` is reported.

Use ordinary midpoint quantization `W_N(k,l)=(-1)^(kl)T_N(l,k)`. The actual
ordinary-Weyl symbol of `A_N` is

$$
a(q,p)=V(q)+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0),
$$

$$
V(q)=\frac9{10}\cos(14\pi q)
+\frac{(1-\cos(14\pi q))\cos(2\pi q)}{10}
+\frac{r(q)\sin(2\pi q)}{100}.
$$

Its Fourier support lies in `|k|<=9, |l|<=1`; its coefficient l1 norm is
at most `59/50`. Put

$$
S=\begin{pmatrix}3&4\\2&3\end{pmatrix},\quad
X=(a_p,-a_q)/(2\pi),\quad\Psi=S\Phi_\tau,\quad
\lambda=3+2\sqrt2,\quad\mu=\lambda^{-1}.
$$

Here `Phi_t` is the flow of `X`, and the Egorov convention is
`U_N Op_N(b)U_N^*=Op_N(b composed with Psi)+O_b(N^-2)`.
The group element `(alpha,beta)` translates the torus by
`(alpha/d,-beta/d)`.

Let `ell_u=(1,sqrt2)/sqrt3`, `ell_s=(1,-sqrt2)/sqrt3`, and let `Q` have
these two rows. In coordinates `z=Qx=(u,s)`, the lattice is `Lambda=Q Z^2`
and

$$
F=Q\Psi Q^{-1}=D+G,\qquad D=\operatorname{diag}(\lambda,\mu).
                                                               \tag{1.4}
$$

All curve and complex-domain estimates use the maximum norm in these
coordinates. Both `||Q||,||Q^-1||<2`. The map preserves area.

## 2. Uniform analytic stable curves and justified area charts

### 2.1 A fixed complex tube

On `max |Im x_i|<1/100`, direct Fourier differentiation gives

$$
\|X\|\le22,\quad\|DX\|\le2000,\quad\|D^2X\|\le10^5.    \tag{2.1}
$$

The last bound follows from
`2*(59/50)*9*(2*pi*10)^2<10^5`; the first two are recorded with their
calculation in the frozen effective note. The variational equations give,
for `|t|<=tau`,

$$
\|\Phi_t-\mathrm{Id}\|\le22|t|,\quad
\|D\Phi_t-I\|\le4000|t|,\quad
\|D^2\Phi_t\|\le2\cdot10^5|t|.                         \tag{2.2}
$$

These hold on the smaller tubes next used. Existence follows from
`|Im Phi_t(x)|<=exp(2000|t|)|Im x|`: integrate the real vector field along
a vertical segment to bound its imaginary part, and apply Gronwall.

Write `F^-1=D^-1+G^-`. The tube `max |Im z_i|<10^-4` enters each relevant
flow with imaginary part below `14*10^-4`, hence stays in (2.1).
Using `||S||=||S^-1||=7`, (2.2) gives, on this fixed tube,

$$
\boxed{\|G\|,\|DG\|,\|D^2G\|,
\|G^-\|,\|DG^-\|,\|D^2G^-\|\le\varepsilon_0:=10^{-60}.}  \tag{2.3}
$$

In fact every displayed quantity is bounded by `10^9 tau`, far below
`epsilon_0`. On real points,

$$
\|DF\|\le6,\qquad\|DF^{-1}\|\le6.                    \tag{2.4}
$$

### 2.2 Holomorphic local graphs

Set `a_0=10^-6`, `eta=1/4`. For a real base `z`, put `z_n=F^n z` and
`R_n(w)=G(z_n+w)-G(z_n)`. A forward-decaying difference orbit with
`w_0^s=t` satisfies

$$
\begin{split}
w_n^s&=\mu^nt+\sum_{j<n}\mu^{n-1-j}R_j^s(w_j),\\
w_n^u&=-\sum_{j\ge n}\lambda^{n-j-1}R_j^u(w_j).          \tag{2.5}
\end{split}
$$

For the sequence norm `sup_n eta^(-n)|w_n|`, the Green factors are
`1/(eta-mu)<20` and `1/(lambda-eta)<1`. For complex `|t|<8a_0`, (2.5)
is a contraction on the radius `16a_0` ball, with constant at most
`20 epsilon_0`; its arguments stay in (2.3). Iteration gives a
holomorphic fixed point satisfying

$$
|w_n(t)|\le9a_0\eta^n,\quad
\gamma_z(t):=w_0^u(t),\quad
\sup_{|t|<8a_0}|\gamma_z(t)|\le2\varepsilon_0a_0.          \tag{2.6}
$$

Thus `z+(gamma_z(t),t)` is an analytic local stable curve. Conversely,
a bounded real difference orbit with this stable initial coordinate
satisfies (2.5). In the unweighted sequence norm its Green factors
are at most `(1-mu)^(-1)<5/4`, so uniqueness applies. For arbitrary
real `t`, the weighted contraction is still valid on real sequences,
since `G` is globally Lipschitz there. It constructs the complete
stable curve as a graph over the entire real stable coordinate.
Graphs centered at other points of this curve agree by uniqueness.
Consequently the complete real graph is analytic at every finite
parameter value.

The map `z -> gamma_z` is periodic and continuous in the uniform norm
on closed disks of radius less than `8a_0`, and its derivatives are
continuous on smaller disks. For precision, this assertion does not
assume continuity of the full orbit sequence in the weighted norm.
Start iteration of (2.5) with `w_n=(0,mu^n t)`. For each fixed component,
each iterate is continuous in `z,t`; its infinite sums have uniformly
convergent geometric tails. The zeroth unstable component converges
uniformly by the contraction estimate. This proves its asserted
continuity; Cauchy's formula proves the derivative assertion.

### 2.3 A C1 stable direction and transverse Jacobians

Write

$$
DF(z)=\begin{pmatrix}\lambda+\alpha(z)&b(z)\\
c(z)&\mu+d(z)\end{pmatrix}.
$$

Its perturbation coefficients and their first derivatives are bounded
by `epsilon_0`. The projective transform for a slope `(sigma,1)` is

$$
(\mathcal T\sigma)(z)=
\frac{(\mu+d(z))\sigma(Fz)-b(z)}
{\lambda+\alpha(z)-c(z)\sigma(Fz)}.                    \tag{2.7}
$$

On `||sigma||<=1/100` its denominator exceeds five. Since `det DF=1`,
the derivative in its scalar argument has modulus at most `1/25`.
Iteration from zero therefore converges uniformly to a unique direction
with `||sigma||<=epsilon_0`.

This convergence also holds in `C^1`. If the fraction in (2.7) is
`R(z,t)`, differentiating its coefficients gives
`||partial_z R||<=10 epsilon_0`, `|partial_tR|<=1/25`. Therefore

$$
\|D(\mathcal T\sigma)\|
\le10\varepsilon_0+(6/25)\|D\sigma\|.
$$

Derivatives of the iterates are bounded by `20 epsilon_0`. Their
successive differences are bounded by `6/25` times the preceding
derivative difference, plus `C epsilon_0` times the preceding uniform
difference. This follows directly by subtracting the differentiated
rational expressions; all denominators exceed five. The uniform
differences decay with ratio `1/25`, so the derivatives are uniformly
Cauchy. Thus

$$
\sigma\in C^1,\qquad\|D\sigma\|\le20\varepsilon_0.     \tag{2.8}
$$

The tangent of the curves (2.6) is this direction: invariance, small
slope, and forward contraction identify it with the unique projective
fixed direction. Hence their real graphs are the integral curves of
the `C^1` field `(sigma(u,s),1)`.

For initial unstable coordinate `t` at fixed stable coordinate `s_0`,
let `u(t,v)` solve `partial_v u=sigma(u,s_0+v)`, `u(t,0)=t`. Then

$$
\partial_tu(t,v)=\exp\left(\int_0^v
\partial_u\sigma(u(t,w),s_0+w)\,dw\right).              \tag{2.9}
$$

For `|v|<=a_0`, this Jacobian is between `1/2` and `2`. A finite fixed
collection of these `C^1` charts covers the torus; plaques can be
restricted to `|v|<=a_0/4`. Area on each is bounded above and below
by fixed multiples of `dt dv`. This justifies the transverse Fubini
step used later, independently of any regularity of the conjugacy.

## 3. Topological conjugacy and density of complete stable curves

For continuous periodic `f`, the equation `k(Dz)-Dk(z)=f(z)` has the
Green solution

$$
(\mathcal Rf)^u=-\sum_{j\ge0}\lambda^{-j-1}f^u\circ D^j,
\qquad
(\mathcal Rf)^s=\sum_{j\ge1}\mu^{j-1}f^s\circ D^{-j}.
$$

Its norm is at most `K_0=(1-mu)^(-1)<5/4`. The contraction
`k -> R(G composed with (Id+k))` gives `K=Id+k` with `F K=K D`.
The same Green series along `F`, with forcing `-G`, gives `H=Id+h`
with `H F=D H`. All corrections are continuous, bounded, and periodic.

The map `H K` commutes with `D`. Its bounded displacement `v` obeys
`v(D^n z)=D^n v(z)` for every positive and negative integer `n`;
boundedness gives `v=0`, hence `H K=Id`. To prove `K H=Id`, compare
the two-sided orbits of `z` and `K H z`. Their difference is bounded
and satisfies a linear recurrence with forcing bounded by
`epsilon_0` times the difference. The two-sided Green bound gives
`sup |w_n|<=K_0 epsilon_0 sup |w_n|`, hence `w_n=0`.
Thus `H,K` are inverse homeomorphisms.

In the original coordinates the first coordinate of `H` is exactly

$$
H_u(x)=\ell_u x+v_\infty(x),\qquad
v_\infty(x)=\sum_{j\ge0}\lambda^{-j}\ell_u
(\Phi_\tau-\mathrm{Id})(\Psi^j x).                     \tag{3.1}
$$

This follows from the Green series and
`G^u=lambda ell_u(Phi_tau-Id)`; it also follows by uniqueness of a
bounded correction satisfying `H_u Psi=lambda H_u`.

Fibers of `H_u` are exactly the complete lifted stable curves. Equality
of the first coordinates gives convergence of the images under `H`
in forward time; uniform continuity of `K` gives convergence before
applying `H`. Conversely, a converging difference before `H` cannot
have a nonzero expanding coordinate after `H`. Uniqueness in (2.5)
then identifies each fiber with the complete analytic graph.

Every such curve is dense on the torus: under `H` it is a straight
stable line of `S` of irrational slope. Irrational straight lines
are dense by the elementary pigeonhole approximation for fractional
parts of multiples of an irrational number. The inverse homeomorphism
preserves density.

## 4. No translated stable-leaf germ can coincide

The all-iterate discounted calculation in the first frozen input proves

$$
\left\|v_r-\tau\sum_{j<r}\lambda^{-j}\ell_u X\circ S^j\right\|_\infty
\le3\cdot10^7\tau^2,
\qquad v_r=\lambda^{-r}\ell_u\Psi^r-\ell_u x.           \tag{4.1}
$$

It holds for every `r`, and hence for the uniform limit `r=infinity`.
For `j>=1` the frequencies `S^(-Tj)e_i` lie outside `|l|<=1`; thus the
fundamental coefficients of the linearized sum come only from `j=0`.
Their squared magnitudes are `101/60000` and `1/120000`. Consequently

$$
|\widehat v_\infty(e_i)|\ge\tau/800,
\qquad|\widehat v_r(e_i)|\ge\tau/800,
\quad i=1,2,\quad r\ge1.                               \tag{4.2}
$$

**Lemma 4.1.** If `h` is nonzero on the torus, the translate by `h` of
any stable-leaf germ differs from every stable-leaf germ.

**Proof.** Suppose two germs coincide. Complete lifted stable curves
are real analytic graphs over the entire real stable coordinate, by
Section 2. Equality of a translated graph and another graph on an
interval therefore extends along the whole real line by the analytic
identity theorem. The translation takes one complete stable curve
onto another.

On that curve `sigma(x+h)=sigma(x)`. Density of its projection and
continuity of the direction extend this equality to the whole torus.
Uniqueness of integral curves of the `C^1` field in Section 2 implies
that the translation preserves the full stable foliation.

It induces a continuous map `A` of the lifted leaf space:
`H_u(x+h)=A(H_u(x))`. Continuity follows, for example, from the
continuous section `K` on the horizontal axis in `H` coordinates.
Lattice equivariance gives

$$
A(t+\ell_u n)=A(t)+\ell_u n,\qquad n\in\mathbb Z^2.
$$

The group `ell_u Z^2` is dense, so continuity forces `A(t)=t+c`.
Equation (3.1) gives
`v_infinity(x+h)-v_infinity(x)=c-ell_u h`; integration shows the
constant on the right is zero. Its two Fourier coefficients in (4.2)
force `exp(2*pi*i*h_i)=1` for each coordinate. Thus the translation
is zero on the torus, a contradiction. `square`

The lemma is for the exact fixed time. It uses no genericity assertion.

## 5. Uniform finite contact with every nearby target leaf

Fix nonzero `h`, written in `Q` coordinates when added to a base point.
For a torus base `z` and `Delta=(Delta_u,Delta_s)` with `|Delta|<=a_0`,
consider the graph difference

$$
L_{z,\Delta,h}(t)=\gamma_z(t)-\Delta_u
-\gamma_{z+h+\Delta}(t-\Delta_s).                       \tag{5.1}
$$

The target is an arbitrary nearby stable leaf through `z+h+Delta`,
not merely the leaf through `z+h`. These functions are holomorphic
on `|t|<2a_0`, uniformly bounded, and continuous in their compact
parameter set with all derivatives on smaller disks. No member is
identically zero, by Lemma 4.1.

At every `(z,Delta,t)` with real `|t|<=a_0/4`, some derivative has
finite order and is nonzero; otherwise its analytic Taylor series
would vanish. Compactness therefore gives `J_h>=1`, `b_h>0` with

$$
\max_{0\le j\le J_h}|\partial_t^j L_{z,\Delta,h}(t)|\ge b_h,
\qquad |t|\le a_0/4.                                    \tag{5.2}
$$

Order zero is included. Cauchy's formula gives a uniform upper bound
on derivatives through `J_h+1`. The following consequence is stable
under perturbation of `C^(J_h)` norm at most `b_h/2`, provided this
upper bound on the next derivative is retained:

$$
|\{t\in I:|L(t)|\le\epsilon\}|\le C_h\epsilon^{1/J_h},
\quad I\subset[-a_0/4,a_0/4],\quad0<\epsilon\le1.         \tag{5.3}
$$

Here is a proof with its uniformity explicit. After the perturbation,
the maximum in (5.2) is at least `b_h/2`. Divide the interval into
a fixed number of sufficiently short intervals. The derivative
selected at each midpoint stays at least `b_h/4` on that interval,
by the bound on its next derivative. If order zero is selected, the
sublevel set is empty at small thresholds. For order `j>=1`, suppose
its sublevel set has length `l`. Select `j+1` points of this measurable
set with successive gaps at least a fixed multiple of `l/(j+1)`;
divide its measure into quantiles and approximate from within the
set. Their divided difference has modulus at most
`C_j epsilon/l^j`. The repeated real mean value theorem identifies
it with `L^(j)(xi)/j!`. Hence
`l<=C_j(epsilon/b_h)^(1/j)`. Summing the fixed cover and using
`j<=J_h` proves (5.3); larger thresholds follow by increasing the
constant. The graph functions in this argument are real on the real
axis.

A fixed finite collection of nonzero translations admits the maximum
of its contact orders and the minimum of its positive constants.
The same compactness argument applies to translations in any compact
set bounded away from zero, without a claimed rate as that distance
decreases.

## 6. Exact inverse curves converge in one fixed analytic disk

At a real center `z`, consider `u=A(s)`, where `A(0)=0`, `A` is
holomorphic on `|s|<4a_0`, and

$$
\|A\|_{4a_0}\le a_0/100.                               \tag{6.1}
$$

Its inverse image under `F^-1`, centered at `F^-1 z`, has coordinates

$$
\begin{split}
s'&=\lambda s+G_s^-(z+(A(s),s))-G_s^-(z),\\
u'&=\mu A(s)+G_u^-(z+(A(s),s))-G_u^-(z).                \tag{6.2}
\end{split}
$$

For each `|s'|<4a_0`, the first equation has a unique holomorphic
solution with `|s|<a_0`. To check this, rewrite it as a fixed-point
equation for `s` with factor `mu`. Schwarz's lemma bounds
`|A(s)|<=|s|/400` on the inner disk, and Cauchy's estimate bounds
`|A'(s)|<=1/300` there. The equation maps `|s|<=a_0` strictly inside
itself, since `4mu<4/5`, and has contraction constant at most
`2mu epsilon_0`. Its solution inserted in the second equation defines
the inverse graph transform `B_z A`, again obeying (6.1).

If two input graphs have outer-disk difference norm `D_0`, Schwarz's
lemma bounds their difference by `D_0/4` on the inner disk, since it
vanishes at zero. Their implicit parameters differ by at most
`epsilon_0 D_0`. Consequently

$$
\boxed{\|B_z A_1-B_z A_2\|_{4a_0}
\le\tfrac18\|A_1-A_2\|_{4a_0}.}                        \tag{6.3}
$$

Indeed the leading term is `mu D_0/4<D_0/20`; parameter changes
contribute at most `mu epsilon_0 D_0/300`, and the nonlinear term at
most `epsilon_0(D_0/4+2 epsilon_0 D_0)`. Their sum is less than
`D_0/8`. The output bound in (6.1) follows from
`mu*a_0/400+2 epsilon_0 a_0<a_0/100`.

The actual stable graphs satisfy

$$
B_z\gamma_z=\gamma_{F^{-1}z},                           \tag{6.4}
$$

since both sides describe the stable curve through the same center,
and the uniqueness in (2.5) applies.

Start with an arbitrary translated stable leaf and a point `z_0` on
it. Its graph through that center obeys (6.1), as does the actual
stable graph there. Iteration of (6.3) along the same inverse center
orbit shows that the graph `A_r` of its exact `r`-fold inverse image
through `z_r=F^-r z_0` satisfies

$$
\|A_r-\gamma_{z_r}\|_{4a_0}\le(a_0/50)8^{-r}.           \tag{6.5}
$$

This holds around every point of the inverse curve. Cauchy's formula
on real `|s|<=2a_0` gives, for every fixed `j`,

$$
\|\partial_s^j(A_r-\gamma_{z_r})\|
\le\frac{j!}{(2a_0)^j}\frac{a_0}{50}8^{-r}.             \tag{6.6}
$$

Choose `r_h` so that all these errors for `j<=J_h`, after the shifts
in (5.1), are at most `b_h/2`. For every `r>=r_h`, comparison of the
translated source leaf with the exact inverse image of any translated
target leaf then satisfies (5.3), with constants independent of `r`.
Uniform derivatives of order `J_h+1` follow from (6.1).

This conclusion holds for every sublevel threshold. The small error
in (6.6) is used to retain a finite nonzero jet, after which the
divided-difference argument is applied to the exact graph. It is
not a replacement of an exact graph inside a sublevel set by its
limit with an additive error floor.

## 7. From finite curves to a torus fixed-set neighborhood

Fix nonzero `h`, arbitrary `g`, and `r>=r_h`. Put

$$
\kappa_{g,h,r}=\Psi^r t_h\Psi^{-r}t_g,\qquad
f_i(x)=e^{2\pi i(\kappa_i(x)-x_i)}-1.                   \tag{7.1}
$$

The area-preserving change `x=Psi^r(y)-g` shows that `max_i|f_i|<=epsilon`
implies that the torus distance between `Psi^r(y+h)` and `Psi^r(y)-g`
is at most a fixed multiple of `epsilon`. Restrict `y` to a finite
source stable plaque `C`, with parameter `[-a_0/4,a_0/4]` from Section 2,
and define the **finite torus curve**

$$
D_{r,C,g}=\Psi^{-r}\bigl(\Psi^r(C)-g\bigr).              \tag{7.2}
$$

By (2.4), each point under consideration satisfies

$$
\operatorname{dist}(y+h,D_{r,C,g})\le
\delta_r:=10\,6^r\epsilon.                             \tag{7.3}
$$

There is only one finite torus curve in (7.2). Integer choices in a
lift change its inverse image by `S^-r n`, which represents the same
torus curve.

The length of `Psi^r(C)` is uniformly bounded, and in fact is
`O(eta^r)`: differentiate (2.6)'s bound for `w_r(t)` by Cauchy's formula
on the smaller plaque interval. Pullback by `Psi^-r` gives

$$
\operatorname{length}(D_{r,C,g})\le C_0 6^r.             \tag{7.4}
$$

The constants are uniform in the source plaque and translation. The
translated forward image lies on a translated stable leaf. Its inverse
image, including its endpoints, is locally one of the analytic graphs
of Section 6 and is in the vertical stable cone.

Cover the finite curve, in its intrinsic order, by at most
`C_1(1+length(D)/a_0)<=C_2 6^r` graph patches of real parameter radius
at most `a_0/16`. Each admits an analytic extension to `4a_0`: extend
the original finite segment along its complete translated stable
leaf, then apply the graph construction (6.2). These extensions are
used only for local graph bounds, comparison, and endpoint evaluation.
All covering and counting refer to the finite curve in (7.2).
Taking the tube of the entire projected complete leaf would be
incorrect, since the latter is dense.

First suppose `delta_r<a_0/100`. A covering patch whose
`delta_r`-neighborhood meets the translated source plaque has a lift
center `z+h+Delta` with `|Delta|<a_0`. That lift is unique in these
small neighborhoods: a nonzero vector of `Q Z^2` has maximum norm
at least `1/2`, while the relevant diameters are below `10a_0`.
Discard patches which do not meet.

The graph slopes are bounded. Hence distance at most `delta_r` from
one such patch implies a graph difference of magnitude at most
`C_3 delta_r` at the same stable coordinate. If the nearest point
is an endpoint, the local analytic extension supplies this nearby
evaluation; the parameter remains in the inner disk. The difference
has the form (5.1), with its target replaced by the exact inverse
graph. Sections 5 and 6 bound the contributing source parameter by
`C_h delta_r^(1/J_h)` for each patch.

Sum the at most `C_2 6^r` patches, integrate transversely with the
bounded Jacobians (2.9), and sum the finite source-chart cover. This
proves

$$
\operatorname{area}\{\max_i|f_i|\le\epsilon\}
\le C_h6^{(1+1/J_h)r}\epsilon^{1/J_h},\qquad r\ge r_h.   \tag{7.5}
$$

If `delta_r>=a_0/100`, (7.5) follows after enlarging `C_h` from total
area one: then `epsilon>=a_0/(1000*6^r)`, so the right side is at
least a fixed constant times `6^r`. All thresholds are therefore covered.

## 8. One sublevel exponent for every iterate

For the finitely many iterates below `r_h`, no map (7.1) is the identity.
Indeed, if it were, the periodic displacement
`Psi^r(y+h)-Psi^r(y)+g` would be a constant integer vector. Its projected
Fourier coefficients are

$$
\lambda^r(e^{2\pi i h_i}-1)\widehat v_r(e_i),
$$

and at least one is nonzero by (4.2).

For each such map, `v=sum_i|f_i|^2` is a nonzero nonnegative real
analytic function on the torus. At every zero some finite-order
directional derivative is nonzero; otherwise its Taylor series and
then analytic continuation would make the function zero identically.
A rational direction may be selected. On a small rectangle that
derivative is bounded below. A finite cover of the zero set, the
one-dimensional divided-difference proof from Section 5, and integration
on parallel lines bound the sublevel area by a positive power of the
threshold. Away from that cover there is a positive minimum.
This is the elementary analytic sublevel proof in the frozen root
trace note, with its hypotheses checked here.

For fixed `d` there are only finitely many `g,h` and finitely many
early iterates. Take the minimum of their positive exponents and the
geometric exponents `1/J_h`, and decrease it, if needed, to the
reciprocal of a positive integer: `beta_d=1/M_d<=1`. Increasing a finite
constant gives the uniform estimate

$$
\boxed{
\operatorname{area}\left\{x:
\max_i|e^{2\pi i(\kappa_{g,h,r,i}(x)-x_i)}-1|\le\epsilon\right\}
\le C_d36^r\epsilon^{\beta_d},
\quad r\ge1,\quad0<\epsilon\le1.}                       \tag{8.1}
$$

It holds for every nonzero `h` and every `g` in the fixed group.
In weakening (7.5), keep `6^(1+1/J_h)r<=36^r`, and use
`epsilon^(1/J_h)<=epsilon^beta_d`.

## 9. Quantum trace decay throughout a logarithmic horizon

Let

$$
\mathscr F_{g,h,r,N}=G_N(g)U_N^{-r}G_N(h)U_N^r,\qquad
\rho_r=(1000\,256^r)^{-1}.
$$

Before inserting its analytic sublevel estimate, Sections 3 and 5
of the frozen effective note prove

$$
\frac{|\operatorname{Tr}\mathscr F_{g,h,r,N}|}{N}
\le\operatorname{area}\{v\le2\delta\}^{1/2}
+C(r+1)\rho_r^{-10}N^{-1}\delta^{-6},\qquad0<\delta<1,    \tag{9.1}
$$

where `v=sum_i |b_i-b_i composed with kappa|^2` and
`b_i=exp(2*pi*i*x_i)`. The constant is absolute. To specify the imported
estimate: the transported coordinate characters are holomorphic and
bounded by two on the strip `rho_r`. The exact Weyl product and
Duhamel give their Egorov remainder `10^12 r rho_r^-5 N^-2`.
Cyclicity bounds the trace against `Op(a)` times either symbol defect
by the product and commutator errors. Apply the fixed scalar cutoff
`chi(v/delta)` from that note and express `1-chi` as a sum of defects
times `(1-chi) conjugate(defect)/v`. Cauchy--Schwarz and the exact
Weyl Hilbert--Schmidt bound give the area term; derivatives of the
symbols give the second term of (9.1). Only the two fixed coordinate
characters need Egorov. No propagation of a varying cutoff is used.

The defects in (8.1) have the same real moduli as those in `v`, so

$$
\boxed{\frac{|\operatorname{Tr}\mathscr F_{g,h,r,N}|}{N}
\le C_d6^r\delta^{\beta_d/4}
+C(r+1)256^{10r}N^{-1}\delta^{-6}.}                      \tag{9.2}
$$

The fixed factor `1000^10` is absorbed in the second constant. Choose
`delta=N^-1/48`, `r<=beta_d log N/1024`. Since `log6<2`, the first term
is bounded by

$$
C_dN^{-\beta_d/192+\beta_d/512}
\le C_dN^{-\beta_d/384}.                               \tag{9.3}
$$

Since `log256<6` and `beta_d<=1`, the second is at most

$$
C(\log N+1)N^{-7/8+15/256}\le C'N^{-3/4}                \tag{9.4}
$$

for large `N`. For example `log N+1<=C N^1/32` leaves exponent
`-201/256<-3/4`. This proves a normalized trace bound
`C_dN^(-1/(384M_d))` uniformly over the horizon (1.1), when `h!=0`.
If `h=0,g!=0`, the trace is exactly zero; the identity pair contributes
exactly `N`. The same zero holds for `g=0,h!=0`, by cyclicity.

Expand the exact projectors. The identity-pair coefficient is
`d^-4=c^2`, and all other absolute coefficients sum to at most one,
proving (1.2). Negative iterates follow by cyclicity and exchange
of the projectors.

## 10. Full-commutant variance and moving spectral windows

Set `B=P_(chi,N)-cI`, `L=T_(d,N)+1`, and

$$
\mathcal A_L(B)=L^{-1}\sum_{j=0}^{L-1}U_N^{-j}BU_N^j.
$$

Its zero-lag correlation is `c-c^2`; every other lag in the squared
Hilbert--Schmidt norm is bounded by (1.2). Thus

$$
N^{-1}\|\mathcal A_L(B)\|_{\rm HS}^2
\le(c-c^2)/L+C_dN^{-1/(384M_d)}.                         \tag{10.1}
$$

The full commutant projection is an orthogonal contraction and
`E_U A_L(B)=E_U B`, proving (1.3) without a simplicity assumption.

For actual matrix-element weights, define on `R/Z`

$$
\nu_{\chi,N}=N^{-1}\sum_{\zeta,\omega\in\operatorname{Spec}U_N}
\|\Pi_\zeta B\Pi_\omega\|_{\rm HS}^2
\delta_{(\arg\zeta-\arg\omega)/(2\pi)}.
$$

Its Fourier coefficients are the preceding correlations. The kernel
`|L^-1 sum_(j=0)^(L-1)exp(2*pi*i*j*t)|^2` is at least `4/pi^2` on
`dist(t,Z)<=1/(2L)`, by the sine formula. Expanding against `nu` at
any center and using the same coefficient bounds gives

$$
\boxed{\sup_{\xi\in\mathbb R/\mathbb Z}
\nu_{\chi,N}\{t:\operatorname{dist}(t,\xi)\le1/(2L)\}
\le\frac{\pi^2}{4}\left((c-c^2)/L+C_dN^{-1/(384M_d)}\right).}        \tag{10.2}
$$

This is `O_d(1/log N)` on windows of width comparable to `1/log N`,
uniformly in their center, and also on every narrower window.
It does not provide an unweighted close-pair count.

## 11. Effectiveness and the remaining boundary

The positive integer in (1.1) is independent of `N` and has a
terminating finite-certification description. The symbol, exact time,
and flows are computable with rigorous errors from (2.1)--(2.3).
Iteration of (2.5), with geometrically truncated tails, computes
`gamma_z` uniformly on smaller disks. Cauchy's formula computes any
fixed number of derivatives with uniform errors. The approximations
also give a computable modulus of continuity in the compact real
parameters: first use finite iterates and finite sums, then bound
their uniform tails by the displayed geometric estimates.

Enumerate jet order, numerical precision, and finite parameter meshes
in (5.2). Interval bounds and that modulus certify positivity of the
largest jet whenever it holds on the compact parameter set.
Compactness and Lemma 4.1 prove that some finite order has a positive
minimum, so this enumeration terminates. Its `J_h,b_h` give `r_h`
through (6.6). For the finitely many early defects, the same procedure,
allowing rational directions, supplies finite derivative lower bounds
and sublevel constants. Alternatively one can use the already checked
quantitative analytic theorem in the earlier effective note for this
finite set. Thus admissible `M_d,C_d,N_d` can in principle be found;
this note does not report their numerically evaluated values.

The structural improvement is the exact inverse graph transform:
absence of a translated leaf germ gives a uniform finite-contact
exponent for all sufficiently long iterates; a finite initial range
is treated separately. A uniform-distance estimate for the limiting
conjugacy coordinate would leave an additive `O(lambda^-r)` error,
which could not justify the arbitrarily small cutoffs in (9.1).
No such substitution occurs here.

The result still concerns arithmetic-sector matrix elements and
times of order `log N`. No lower bound on these weights for every
eigenphase pair has been proved. The full signed products of quantum
traces at times of order `N` remain unevaluated. Those are unproved
ingredients needed for `H_diag`; this note is neither a proof nor a
counterexample to that criterion.
