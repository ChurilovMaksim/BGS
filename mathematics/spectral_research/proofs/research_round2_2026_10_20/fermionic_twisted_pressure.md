> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_twisted_pressure.md`. Embedded SHA256: `ef5257ebfdd1e8e88ca8c1a0596c9a667ec4ff2954593a9eaf3fa0331ce8d362`.
> [Thematic guide](../../topics/classical_trace.md).


# Uniform Weyl-twisted quantum traces from the actual pressure gap

Research continuation, 20 October 2026. All matrices in this note are
the original matrices in the question, with the fixed exact parameter
`tau=10^-80`. No perturbation averaging, restriction to prime dimensions,
or replacement of the quantum family is used.

The new result is a bound on all `N^2` Weyl-twisted traces simultaneously:

$$
\sup_{a,b\in\mathbb Z/N\mathbb Z}
 |\operatorname{Tr}(T_N(a,b)U_N^m)|
 \le C_\eta e^{(P_*+\eta)m}+2(0.421)^m.
\tag{A}
$$

Here `P_*<log(lambda)/2` is the strictly smaller pressure proved for
the actual classical map. For each fixed `eta>0`, the estimate holds
for every positive integer m and every sufficiently large odd N,
with one N threshold independent of m and of the Weyl index.
The proof extends the exact sector formula to a rational boundary
translation and identifies the leading Gaussian cocycle pointwise,
including its endpoint factor. It does not infer an open-orbit formula
merely from the previously known periodic products.

An actual consequence is quantitative separation from every Weyl
operator at the bare cat's Pell return times, together with a growing
lower bound on the number of significant Weyl coefficients. These
statements do not establish `H_diag` or a microscopic pair limit.

## 1. Frozen inputs and conventions

Put

$$
\lambda=3+2\sqrt2,\quad \rho=\lambda^{-1},\quad
L=\begin{pmatrix}3&-4\\-2&3\end{pmatrix},\quad
h=(2\pi N)^{-1},\quad t_*={\tau\over2\pi}.
$$

The ordinary Weyl symbol corresponding to the modular rule in the
question is

$$
a(q,p)=\cos(14\pi q)+{r(q)\over10}
 +{r(q)\sin(2\pi q)\over100}-{1\over10}
 +{r(q+1/2)\cos(2\pi p-\alpha_0)\over100}.
$$

The classical map is `Psi=phi_a^(-t_*) composed with L`. It has an
equivariant lift

$$
\Psi(x)=Lx+v(x),\qquad v(x+w)=v(x)\quad(w\in\mathbb Z^2).
\tag{1.1}
$$

In the maximum norm of fixed eigen-coordinates of L, use the relaxed
bound `kappa:=||Dv||<10^-69`. The bounded two-sided Green inverse of
`d_(j+1)-L d_j=e_j` has norm at most

$$
K=(1-\rho)^{-1}<1.21,\qquad K\kappa<1.
\tag{1.2}
$$

The one-step generating function and exact plane kernel are

$$
F(Q,q)=-{3Q^2-2Qq+3q^2\over8}+G(Q,q),
\qquad
K_V(Q,q)={e^{i\pi/4}\over\sqrt{8\pi h}}
                  e^{iF(Q,q)/h}B_h(Q,q).
\tag{1.3}
$$

They satisfy `p=-F_q`, `P=F_Q`, `Psi(q,p)=(Q,P)`. The second
derivatives of G have absolute value at most `eta_F<10^-70`.
The exact leading amplitude is

$$
B_0(Q,q)=2\sqrt{F_{Qq}(Q,q)}>0.
\tag{1.4}
$$

The following frozen files supply these facts and the indicated
quantum identities. Their relevant proofs are used as inputs, not
as names for additional assumptions.

| Input | SHA-256 |
|---|---|
| `../research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md` | `42832bfc27bbf307b154c781f7299912e7c3094e0a0c3ff2e3ade9f0e580764b` |
| `../research_continuation_2026_10_20/exact_amplitude.md` | `69cd85816766b26358fb13058b3b26f9c243886cf863e5f8f9a6c6570e1a542e` |
| `../research_continuation_2026_10_20/gaussian_cocycle_and_modulus.md` | `c1a863e613a327acb5fe43ff1093c4a8fe51b37ebd5dcee9fddf0ae0a91986f1` |
| `../research_continuation_2026_10_20/classical_trace_and_pair_diagonal.md` | `355f2c6deb1549c32ab7b7313774b8c27b1310d019013838fc5e3679721af55c` |
| `fermionic_pressure_transfer.md` | `90ebc84c3c9fb7c049a1a9d11e0d5dcb72c4fc89b362da3f848521a7bca79756` |

In particular, if `J^u(x)>0` is the unstable Jacobian in the fixed
Riemannian norm used in the last file and `varphi=log J^u`, then

$$
0<P_*:=P_{\rm top,\Psi}(-\varphi/2)
 <{1\over2}\log\lambda,
\qquad \Delta={1\over2}\log\lambda-P_*>0.
\tag{1.5}
$$

That file proves the hypotheses of the quoted Bowen--Ruelle theorems
by passing to the smooth unit-roof suspension. Its strictness argument
uses the actual fixed point with unstable multiplier greater than
lambda. The resulting number Delta is positive for the exact fixed
tau; no effective numerical lower bound on Delta is asserted here.

The contour construction in the third input defines trace-class
operators `K_h(x)` on the single fixed space `H=L^2(R)`. For all base
points x and one h threshold,

$$
K_h(x)=R_h(x)+\mathcal B_h(x),\qquad
R_h(x)=\gamma_h(x)v_h(\Psi x)\ell_h(x),
\tag{1.6}
$$

$$
\ell_h(x)v_h(x)=1,\quad
\|v_h(x)-e_0\|\le r_0,\quad
\|\ell_h(x)\|\le {1\over1-r_0},\qquad
r_0=2.5\cdot10^{-4},
\tag{1.7}
$$

$$
R_h(\Psi x)\mathcal B_h(x)=0
=\mathcal B_h(\Psi x)R_h(x),\qquad
\|\mathcal B_h(x)\|<0.174,\quad
\|\mathcal B_h(x)\|_1<0.209.
\tag{1.8}
$$

Here

$$
e_0(y)=\left({\sqrt2\over\pi}\right)^{1/4}e^{-y^2/\sqrt2}.
$$

The normalized right graph is unique among continuous sections
`v=e_0+w`, `<e_0,w>=0`, `||w||<=r_0`, satisfying its covariance.
The pointwise scalar expansion, not only its periodic consequence, is

$$
\gamma_h(x)=\gamma_0(x)+h\gamma_1(x)+O(h^2),\qquad
\gamma_0(x)>0,\quad \gamma_1(x)\in i\mathbb R,
$$

$$
\bigl|\log|\gamma_h(x)|^2-2\log\gamma_0(x)\bigr|
\le C_{\rm jet}h^2.
\tag{1.9}
$$

The error and h threshold in (1.9) are uniform in x. They follow from
the real finite-jet calculation in Sections 7--8 of that input.

## 2. The Gaussian scalar on every orbit segment

Write, at an edge `x=(q,p)` and `Psi x=(Q,P)`,

$$
\alpha(x)=F_{QQ}(Q,q),\quad \beta(x)=F_{Qq}(Q,q),\quad
\gamma(x)=F_{qq}(Q,q).
$$

The letter gamma without a subscript in this section denotes this
Hessian entry only; it is distinct from the cocycle scalar gamma_h.
The Gaussian limit of (1.6)'s operator is exactly

$$
K_0(x;y',y)=\lambda_0^{-1}2\sqrt{\beta(x)}
 \exp\bigl(\alpha(x)y'^2+2\beta(x)y'y+\gamma(x)y^2\bigr),
\qquad \lambda_0={2\sqrt\pi\over\sqrt\lambda}.
\tag{2.1}
$$

### 2.1 The unstable slope and its Riccati equation

Let `s(x)` be the physical slope of the unstable line, so that
`w(x)=(1,s(x))` spans it. This slope is globally defined and is close
to `s_0=-1/sqrt(2)`. Here is a direct quantitative construction from
the Hessian bounds, avoiding an unquantified choice of chart.

For any input slope s, differentiate the generating equations:

$$
\delta p=-\gamma\delta q-\beta\delta Q,\qquad
\delta P=\beta\delta q+\alpha\delta Q.
$$

When `delta p=s delta q`, the first-coordinate expansion and output
slope are respectively

$$
b(x)=-{s+\gamma(x)\over\beta(x)},\qquad
\Phi_x(s)=\alpha(x)-{\beta(x)^2\over\gamma(x)+s}.
\tag{2.2}
$$

At the cat values `alpha=gamma=-3/4`, `beta=1/4`, the slope s_0 is
fixed, and the corresponding b is lambda. On `|s-s_0|<=0.01` the
Hessian bounds give `|partial_s Phi_x|<0.04`; at s_0 the change from
the cat value is less than `2 eta_F`. These estimates follow directly
from `partial_s Phi=beta^2/(gamma+s)^2` and the three parameter
derivatives, whose absolute values have sum less than 2 in this
neighborhood. Thus the section transform

`s(x) -> Phi_(Psi^-1 x)(s(Psi^-1 x))`

is a contraction of the closed ball `||s-s_0||_infinity<=4 eta_F`.
Its fixed section is continuous, satisfies

$$
s(\Psi x)=\alpha(x)-{\beta(x)^2\over\gamma(x)+s(x)},
\qquad |s(x)-s_0|\le4\eta_F,
\tag{2.3}
$$

and its b in (2.2) is positive and greater than 5. Consequently this
line contracts uniformly in negative time and is the unstable line
of Psi. In particular,

$$
D\Psi(x)w(x)=b(x)w(\Psi x),\qquad b(x)>5.
\tag{2.4}
$$

### 2.2 Exact normalized Gaussian section

Put `d_0=(sqrt(2)/pi)^(1/4)` and

$$
C(x)=\left[\int_{\mathbb R}e_0(y)e^{s(x)y^2}\,dy\right]^{-1}
 ={\sqrt{-s(x)-s_0}\over d_0\sqrt\pi}>0,
\qquad v_0^G(x;y)=C(x)e^{s(x)y^2}.
\tag{2.5}
$$

Then `<e_0,v_0^G>=1`. This is a section in the same graph ball as
(1.6). For an explicit check, on `-0.72<=s<=-0.69`, the Gaussian
moment formulas give `||C(s)e^(s y^2)||<=2`,
`|C'(s)/C(s)|<=1`, and
`||y^2 C(s)e^(s y^2)||<=2||C(s)e^(s y^2)||`. Therefore the L2 norm
of its s derivative is at most 6. Since at s=s_0 it is e_0,

$$
\|v_0^G(x)-e_0\|\le 24\eta_F<r_0.
\tag{2.6}
$$

Complete the square in the ordinary convergent Gaussian integral
obtained by applying (2.1) to (2.5). Equations (2.2)--(2.3) give

$$
\begin{split}
K_0(x)v_0^G(x;y')
 &= {2\sqrt\beta\over\lambda_0}
       C(x)\sqrt{\pi\over-(\gamma+s(x))}
       e^{s(\Psi x)y'^2}\\
 &=\sqrt\lambda\,b(x)^{-1/2}
       {C(x)\over C(\Psi x)}v_0^G(\Psi x;y').
\end{split}
\tag{2.7}
$$

By uniqueness of the normalized near-e_0 right graph, this section
is the previously constructed v_0. Consequently its scalar is
identified pointwise:

$$
\boxed{\gamma_0(x)=\sqrt\lambda\,b(x)^{-1/2}
                     {C(x)\over C(\Psi x)}.}
\tag{2.8}
$$

The factor `2 sqrt(beta)` in the exact leading amplitude is necessary
for the factor sqrt(lambda) in (2.8).

### 2.3 The bounded endpoint factor and the open-product modulus

Let `n(x)=||w(x)||` in the fixed Riemannian norm defining J^u and
put `D(x)=C(x)/sqrt(n(x))`. Both are continuous positive functions
on the compact torus. Equation (2.4) gives

$$
J^u(x)=b(x){n(\Psi x)\over n(x)},\qquad
\gamma_0(x)=\sqrt\lambda\,[J^u(x)]^{-1/2}
                             {D(x)\over D(\Psi x)}.
\tag{2.9}
$$

For any x and any m, closed or open, define

$$
\Gamma_h(x,m)=\prod_{j=0}^{m-1}\gamma_h(\Psi^j x),\qquad
J_m^u(x)=\prod_{j=0}^{m-1}J^u(\Psi^j x).
$$

Telescoping (2.9) and then summing the uniform logarithmic error
in (1.9) prove the exact leading relation and its quantum estimate:

$$
\lambda^{-m/2}\Gamma_0(x,m)
 =[J_m^u(x)]^{-1/2}{D(x)\over D(\Psi^m x)},
\tag{2.10}
$$

$$
\left|\log\left(
\lambda^{-m}|\Gamma_h(x,m)|^2 J_m^u(x)
 {D(\Psi^m x)^2\over D(x)^2}\right)\right|
\le C_{\rm jet}mh^2.
\tag{2.11}
$$

In particular, with the fixed constant `C_end=max D/min D`,

$$
\boxed{
\lambda^{-m/2}|\Gamma_h(x,m)|
\le C_{\rm end}e^{C_{\rm jet}mh^2/2}[J_m^u(x)]^{-1/2}.
}
\tag{2.12}
$$

All quantifiers in (2.11)--(2.12) are simultaneous: one h threshold,
all x, and all m. This is not a consequence of periodic-product data
alone; it uses the actual kernel (2.1) and the actual unstable slope.

## 3. An exact finite trace identity with a rational translation

The physical plane Weyl operator is

$$
(\mathcal T_{(u,v)}\psi)(q)
 =e^{iv(q-u/2)/h}\psi(q-u).
$$

For integer vectors `w=(w_q,w_p)` let
`R_w=(-1)^(w_q w_p) mathcal T_w`. For odd N these form the honest
integer representation `R_w R_z=R_(w+z)`. Their invariant combs
identify with `C^N`. The plane operator V in (1.3) descends to
`zeta_N^-1 U_N`, where `zeta_N=e_8(3N-1)`.

Choose integer representatives a,b and set

$$
\xi=(a/N,-b/N).
\tag{3.1}
$$

On the invariant comb, `mathcal T_(-xi)` acts by

`u(x) -> exp(2 pi i b(x+a/2)/N) u(x+a)`.

The modular inverse of two may be represented by `(N+1)/2`.
Consequently, with every half in the displayed exponential an
ordinary real half,

$$
T_N(a,b)=(-1)^{ab}(\mathcal T_{-\xi})_N.
\tag{3.2}
$$

The rationality in (3.1) also gives

$$
\mathcal T_{-\xi}R_w=R_w\mathcal T_{-\xi}
\quad(w\in\mathbb Z^2),
\tag{3.3}
$$

because the Weyl commutator is
`exp(2 pi i N(-xi_p w_q+xi_q w_p))=1`.
Since `V^m R_w=R_(L^m w) V^m`, the operator
`W=mathcal T_(-xi)V^m` has the same deck covariance as V^m:

$$
WR_w=R_{L^mw}W.
\tag{3.4}
$$

It therefore preserves the comb quotient and commutes with its
periodizer `P=sum_w R_w`.

### 3.1 Coherent unfolding and its convergence

Use normalized plane coherent states `|z>` and the exact quotient
frame `N integral_[0,1]^2 |phi_z><phi_z| dz=I_N`. The corresponding
trace identity is

$$
\operatorname{Tr}W_N
 =N\sum_{n\in\mathbb Z^2}\int_{[0,1]^2}
                  \langle z|R_{-n}W|z\rangle\,dz.
\tag{3.5}
$$

The convergence checks from Sections 7--8 of the frozen odd-trace
file also apply here, for a precise reason. Its exact exponential
word expansion is a sum of translated metaplectic words
`sum_nu d_nu mathcal T_(w_nu) mu_L^m` with finite absolute
coefficient mass (indeed with every fixed exponential displacement
weight). Left multiplication by `mathcal T_(-xi)` merely changes
these real displacements and unimodular word factors. The Gaussian
lattice-sum bound and the whole-plane coherent integral bound for
one such word are independent of its displacement. Thus the lattice
sum, the unit-cell integrals, and each sector's plane integral in
(3.5) remain absolutely convergent for each fixed m,N,xi.

If `g_n(z)=<z|R_(-n)W|z>`, (3.4) and the honest integer Weyl law give

$$
g_{n_0}(z+w)=g_{n_0-(L^m-I)w}(z).
\tag{3.6}
$$

Choose one representative from each integer quotient class. Summing
(3.6) tiles the plane once, with no extra determinant multiplier.
Equations (3.2) and (3.5) yield the exact identity

$$
\boxed{
\operatorname{Tr}(T_N(a,b)U_N^m)
 =(-1)^{ab}\zeta_N^m
 \sum_{[n]\in\mathbb Z^2/(L^m-I)\mathbb Z^2}
             \mathfrak T_h(R_{-n}\mathcal T_{-\xi}V^m),
}
\tag{3.7}
$$

where

$$
\mathfrak T_h(B)={1\over2\pi h}
                         \int_{\mathbb R^2}\langle z|B|z\rangle dz.
$$

### 3.2 The boundary action and its unique critical point

The physical Weyl product gives

$$
R_{-n}\mathcal T_{-\xi}
 =\chi_{n,\xi}\mathcal T_{-(n+\xi)},\qquad
\chi_{n,\xi}=(-1)^{n_qn_p}
       \exp\left({i(n_p\xi_q-n_q\xi_p)\over2h}\right),
\quad |\chi_{n,\xi}|=1.
\tag{3.8}
$$

For `t=n+xi`, the exact Abel/Fresnel expression for the corresponding
sector is therefore chi times

$$
\lim_{\epsilon\downarrow0}\int_{\mathbb R^m}
 e^{-\epsilon\sum_jq_j^2}
 e^{-it_p(q_0+t_q/2)/h}
 \prod_{j=0}^{m-1}K_V(q_{j+1},q_j)\,d\mathbf q,
\qquad q_m=q_0+t_q.
\tag{3.9}
$$

The proof of this identity also retains its convergence after the
twist. Each term in the exact product word expansion has the same
negative definite quadratic Hessian
`-(6I-R-R^-1)/4`, where R is the cyclic shift, and a possibly changed
real linear term. The absolute bound for its damped Gaussian integral
is independent of that linear term. The finite total absolute word
mass consequently justifies composition and passage to the Abel
limit exactly as in the untwisted formula.

The full real action in (3.9) is

$$
S_{m,t}(\mathbf q)=\sum_{j=0}^{m-1}F(q_{j+1},q_j)
                         -t_p(q_0+t_q/2),\qquad q_m=q_0+t_q.
\tag{3.10}
$$

For every real t its Hessian differs from `-(6I-R-R^-1)/4` by a
matrix of norm less than `10^-68`, uniformly in m,t and the position
variables. The unperturbed spectrum lies in `[-2,-1]`, including
m=1,2 with coincident edges counted with multiplicity. Thus S is
uniformly strictly concave. Its quadratic part is coercive toward
minus infinity; its bounded perturbation and linear term do not
affect that conclusion. It has precisely one critical point.

Differentiating (3.10) matches the momenta on consecutive edges and
gives, at this critical point,

$$
\Psi^m x=x+n+\xi.
\tag{3.11}
$$

Changing the initial lift by an integer w changes n to
`n+(L^m-I)w`. Conversely, uniqueness of the critical point in each
lift sector proves that (3.7)'s classes correspond bijectively to

$$
E_{m,\xi}=\{x\in\mathbb T^2:\Psi^m x=x+\xi\}.
$$

This proves, for every m and every real torus translation xi,

$$
\#E_{m,\xi}=|\det(L^m-I)|
                  =\lambda^m+\lambda^{-m}-2<\lambda^m.
\tag{3.12}
$$

### 3.3 The exact open-orbit product and its summed residual

Let `x_j=Psi^j x` along the critical orbit in (3.11), and write each
position variable as its critical value plus z_j. Then `z_m=z_0`.
The edge linear terms telescope to `(p_m-p_0)z_0=t_p z_0`, which
exactly cancels the boundary linear term of (3.10). Hence, with
the globally defined centered edge phase from the frozen Gaussian
file,

$$
S_{m,t}-S_{m,t}^{\rm crit}
 =\sum_{j=0}^{m-1}\widetilde F_{x_j}(z_{j+1},z_j).
\tag{3.13}
$$

The bounded contour deformation depends only on the uniform analytic
strip, the centered Hessian bound, and the exact amplitude. Its
coercive estimates are uniform over all real base points, so (3.13)
gives the same absolutely convergent cyclic kernel integral and the
same one-edge h threshold as before. The external scalar per edge
is exactly lambda^-1/2. Thus there are phases of modulus one such
that the contribution of each critical point in (3.7) equals

$$
\omega_{m,N,a,b}(x)\lambda^{-m/2}
       \operatorname{Tr}\bigl(K_h(x_{m-1})\cdots K_h(x_0)\bigr).
\tag{3.14}
$$

Every odd-lattice and physical-translation factor in (3.2), (3.8),
and the critical action is included in omega; the global zeta_N^m
may also be included there. Representative independence follows
already from the exact coherent identity (3.6). No periodic
invariance under moving the starting point is asserted for this
open trajectory.

Now multiply (1.6). Because of (1.8), every mixed word vanishes.
Without assuming `x_m=x_0` on the torus, the rank-one product is
`Gamma_h(x,m) v_h(x_m) ell_h(x_0)`. Its trace is therefore

$$
\operatorname{Tr}\bigl(K_h(x_{m-1})\cdots K_h(x_0)\bigr)
 =\Gamma_h(x,m)\ell_h(x)v_h(\Psi^m x)+R_h^{(m)}(x),
\tag{3.15}
$$

$$
|\ell_h(x)v_h(\Psi^m x)|\le {1+r_0\over1-r_0},\qquad
|R_h^{(m)}(x)|\le0.209(0.174)^{m-1}.
\tag{3.16}
$$

Sum the residual over (3.12) and include lambda^-m/2. This gives

$$
|E^{\rm tw}_{m,N}(a,b)|
\le\lambda^{m/2}0.209(0.174)^{m-1}
<2(0.421)^m,
\tag{3.17}
$$

simultaneously for every Weyl index and every m, at one N threshold.
This establishes the full twisted quantum decomposition, not merely
its leading semiclassical stationary-phase expression.

## 4. Uniform separation of all translated return sets

Periodic expansivity alone does not immediately prove the needed
separation for E_(m,xi), because an orbit ending at x+xi need not
repeat under Psi. The following finite cyclic argument supplies it.

Let `ell_lat>0` be the shortest nonzero integer lattice norm in the
fixed eigen-coordinates. Choose a fixed radius e so small that

$$
e(1+\|L\|+\kappa)<\ell_{\rm lat},\qquad 2e<\ell_{\rm lat}.
\tag{4.1}
$$

Suppose x,y are in the same E_(m,xi), and their first m iterates
are within torus distance e in that norm. Choose actual plane
orbit lifts x_j,y_j. For `0<=j<m` choose integer vectors w_j so

`d_j=y_j-x_j-w_j`, `||d_j||<=e`.

By the common translated boundary condition,
`y_m-x_m=y_0-x_0+(n_y-n_x)`. Set
`w_m=w_0+n_y-n_x`; then `d_m=d_0`. Using (1.1) and periodicity of v,

$$
d_{j+1}-Ld_j-\bigl(v(x_j+d_j)-v(x_j)\bigr)
=Lw_j-w_{j+1}\in\mathbb Z^2.
\tag{4.2}
$$

Its norm is less than ell_lat by (4.1), so this integer vector is
zero. Extend the finite lists d_j and
`e_j=v(x_j+d_j)-v(x_j)` periodically with period m as lists of
vectors. Equation (4.2) then gives a bounded two-sided solution of
`d_(j+1)-Ld_j=e_j`. The Green estimate (1.2) yields

$$
\max_j\|d_j\|\le K\max_j\|e_j\|
               \le K\kappa\max_j\|d_j\|.
$$

Since K kappa is less than one, all d_j vanish, and x=y on the
torus. No periodic continuation of the actual nonlinear orbit was
used: only the finite difference sequence and its forcing were
continued. We have proved

$$
\boxed{E_{m,\xi}\text{ is }(m,e)\text{-separated,
 uniformly for all }m\ge1\text{ and all }\xi\in\mathbb T^2.}
\tag{4.3}
$$

Let `Z_m(-varphi/2,e)` be the supremum of the positive weighted
sums over all `(m,e)`-separated sets. By the separated-set definition
of topological pressure,

$$
\limsup_{m\to\infty}{1\over m}\log Z_m(-\varphi/2,e)\le P_*.
$$

For each positive eta, absorbing its finite initial range in a
constant, (4.3) therefore gives

$$
\boxed{
\sup_{\xi\in\mathbb T^2}
 \sum_{x\in E_{m,\xi}}[J_m^u(x)]^{-1/2}
\le C_\eta e^{(P_*+\eta)m}\qquad(m\ge1).
}
\tag{4.4}
$$

This step requires neither a transfer-operator spectral gap uniform
in xi nor a uniform periodic-orbit asymptotic. The same fixed
separated partition sum controls every translated return set.

## 5. The actual uniform twisted trace bound

### Theorem 5.1

For every fixed eta>0 there exist `C_eta,N_eta` such that every odd
`N>=N_eta`, every integer m>=1, and every a,b modulo N satisfy

$$
\boxed{
|\operatorname{Tr}(T_N(a,b)U_N^m)|
\le C_\eta e^{(P_*+\eta)m}+2q_*^m,
\qquad q_*=0.421.
}
\tag{5.1}
$$

**Proof.** Insert (3.15) into the exact finite sum (3.14). Apply
the endpoint bracket bound (3.16) and the open-product bound
(2.12), and then (4.4) with eta/2. The full principal contribution
is bounded by

$$
{1+r_0\over1-r_0}C_{\rm end}C_{\eta/2}
  \exp\bigl[(P_*+\eta/2+C_{\rm jet}h^2/2)m\bigr].
$$

Choose a single N_eta for the original one-edge h threshold and
`C_jet h^2/2<=eta/2`. None of these thresholds depends on m,xi,a,b.
Adding (3.17) proves (5.1). QED.

The factor `m h^2` was absorbed as a change in the exponential rate;
it was not assumed small. Thus the all-m statement is literal,
including m much larger than N^2, although the bound becomes weaker
than unitarity for sufficiently large m. One may always take its
minimum with N.

With `eta=Delta/2` the residual can be absorbed, because P_*>0,
and there are fixed constants C,N_0 such that

$$
\sup_{a,b}|\operatorname{Tr}(T_N(a,b)U_N^m)|
\le C a_{\rm eff}^m,\qquad
a_{\rm eff}=e^{P_*+\Delta/2}
            =\sqrt\lambda e^{-\Delta/2}<\sqrt\lambda.
\tag{5.2}
$$

## 6. Quantitative consequences for the exact quantum family

### 6.1 Separation from every Weyl operator at the Pell times

Define

$$
N_r={\lambda^r-\lambda^{-r}\over4\sqrt2}.
\tag{6.1}
$$

As proved in the pressure file, these are integers with
`N_(r+1)=6N_r-N_(r-1)`, `N_0=0`, `N_1=1`, and `N_r=r mod 2`.
For every odd r>=3 they are allowed dimensions, and the bare cat
matrix obeys `M_(N_r)^(2r)=scalar`. This last statement is only a
reference identifying the arithmetic time; all matrices in the
next assertions are the actual perturbed U.

For any fixed

$$
0<\delta<{2\Delta\over\log\lambda},
\tag{6.2}
$$

choose eta>0 sufficiently small in (5.1). Since
`lambda^r=4 sqrt(2) N_r+lambda^-r`, it follows that

$$
\boxed{
\max_{a,b\bmod N_r}{1\over N_r}
 |\operatorname{Tr}(T_{N_r}(a,b)U_{N_r}^{2r})|
=O(N_r^{-\delta})\quad(r\to\infty\text{ odd}).
}
\tag{6.3}
$$

In particular delta=Delta/log(lambda) is valid using (5.2).
For any pair of unitaries V,T, expansion of the Hilbert--Schmidt
norm gives

$$
\min_{|\omega|=1}{1\over N}\|V-\omega T\|_{\rm HS}^2
=2-2{|\operatorname{Tr}(T^*V)|\over N}.
$$

Since adjoints permute the Weyl family, (6.3) proves

$$
\boxed{
\min_{a,b,\,|\omega|=1}{1\over N_r}
 \|U_{N_r}^{2r}-\omega T_{N_r}(a,b)\|_{\rm HS}^2
=2-O(N_r^{-\delta}).
}
\tag{6.4}
$$

The assertion is uniform over all N_r^2 possible translation and
modulation returns, not only over scalar phases.

### 6.2 Weyl coefficient spreading

The exact finite Weyl orthogonality holds for every odd composite
dimension as well as for primes:

$$
\operatorname{Tr}(T_N(v)^*T_N(w))=N\mathbf1_{v=w}.
\tag{6.5}
$$

For a unitary V define its expansion coefficients

$$
V=\sum_{v\in(\mathbb Z/N\mathbb Z)^2}c_v(V)T_N(v),
\qquad c_v(V)={1\over N}\operatorname{Tr}(T_N(v)^*V).
$$

Parseval and unitarity give `sum_v |c_v(V)|^2=1`. Combining this
with (5.1), and absorbing its residual in a constant, yields for
every m and all sufficiently large odd N

$$
\max_v|c_v(U_N^m)|\le
 \min\{1,C_\eta e^{(P_*+\eta)m}/N\},
$$

$$
\sum_v|c_v(U_N^m)|^4
\le\min\{1,C_\eta^2 e^{2(P_*+\eta)m}/N^2\}.
\tag{6.6}
$$

At the Pell times, (6.3) gives

$$
\boxed{
\sum_v|c_v(U_{N_r}^{2r})|^4=O(N_r^{-2\delta}),\qquad
\left(\sum_v|c_v(U_{N_r}^{2r})|^4\right)^{-1}
\ge c_\delta N_r^{2\delta}.
}
\tag{6.7}
$$

There is also a direct approximation statement. If W is any unitary
whose Weyl expansion has at most K nonzero terms, Cauchy--Schwarz
and (6.3) imply

$$
{1\over N_r}|\operatorname{Tr}(W^*U_{N_r}^{2r})|
\le C_\delta\sqrt K\,N_r^{-\delta}.
\tag{6.8}
$$

Thus even unitaries supported on `K=o(N_r^(2 delta))` Weyl indices
have vanishing normalized overlap with the actual return-time
matrix. This is a consequence of an exact complete basis and a
uniform trace estimate, not a numerical inference about complexity.

## 7. The precise remaining limitation

The uniform estimate (5.1) is genuinely stronger than the scalar
trace estimate: it controls every Fourier coefficient of the
operator U_N^m in its Weyl basis. Nevertheless its effective range
before the unitarity bound takes over is still proportional to
log N. It does not give cancellation among the full products of
traces occurring in `H_diag` at m of order N.

In particular, the complete Weyl family considered here should not
be confused with a bound on the spectral-difference projection of
all N^2 Weyl observables under the superoperator `Ad U_N`. Such a
projection is a different sum, involving pairs of eigenvectors and
phases. Nor does the sum of squared Weyl coefficients add information
beyond Parseval: it equals one exactly at every m.

The new estimate supplies small individual overlaps at all Weyl
indices and quantifies the loss of the bare arithmetic return. It
does not yet prove even the order-one bound

$$
{1\over N^2}\sum_{m\ge1}e^{-2sm/N}
                  |\operatorname{Tr}U_N^m|^2=O_s(1),
\tag{7.1}
$$

let alone its CUE limit or the higher factorial moment comparisons.
The exact positive frame method in `fermionic_resolvent_frame.md`
currently gives order `N/log N` on the left of (7.1), with its strict
pressure improvement in the leading upper constant. No missing
mixed-phase or denominator estimate is inserted into this note.



---

