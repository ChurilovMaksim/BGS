> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/arithmetic_iterated_uniform_all_old_logarithmic.md`. Embedded SHA256: `690910507ef2849d81aeb59350d145c84997cd692cbca784711509d6274480fd`.
> [Thematic guide](../../topics/arithmetic.md).

# Uniform logarithmic sector estimates and all canonical oldspaces

## Status and immutable inputs

This note concerns the exact original matrices, always with `tau=10^-80`.
It allows the arithmetic divisor to grow as a fixed positive power of
the dimension. In particular, the full commutant variance of the sum of
all canonical oldspaces is `O(1/log N)` along every odd dimension.
Repeated eigenvalues are allowed. These are matrix-element and
eigenvector-mass estimates, not a proof of `H_diag`.

| Proved input | SHA-256 |
|---|---|
| `arithmetic_iterated_logarithmic_horizon.md` | `37cae903cc22d77e04ba9848f00fdfd4f19920e9c3a22381de92e965588ce8c6` |
| `root_uniform_translation_contact.md` | `257afa4511da2fae8bd9260cc33a654bf045115f80aa0861bb8eae6a4f92347e` |
| `arithmetic_iterated_all_oldspaces.md` | `853aeae71f699d0af37aa071202112603eb518a0e8614a65ca1f91246d2bd5b8` |
| `arithmetic_iterated_effective_horizon.md` | `9739e62cc9a4282d39b379c50835f05fd3d46d664663cf6032b3337857751768` |

The first two proofs have been independently audited in full. They
supply exact inverse-curve contraction, finite-curve counting,
quantitative Egorov, and uniform contact as translations approach zero.
The latter includes C1 dependence in a fixed holomorphic norm and an
infinitesimal rigidity proof. The exact oldspace lattice from the third
input is reproduced below. Frozen inputs are not modified.

## 1. Constants and conclusions

There exist `C,N_0`, a positive integer `J`, and `r_0>=1`, depending
only on the original fixed map. Write

$$
\beta=1/J\le1,\quad
t_N=\left\lfloor\frac{\beta\log N}{4096}\right\rfloor,
\quad L_N=t_N+1,
\quad R_N=\left\lfloor\frac{\beta\log N}{8192}\right\rfloor,
\quad\varepsilon_N=C N^{-\beta/256}.                    \tag{1.1}
$$

The integer `J` is not numerically evaluated. Its finite-contact
definition and a terminating certification procedure appear in the
geometric inputs; it is independent of both `d` and `N`. All assertions
are for sufficiently large odd `N`, with `t_N>=r_0` and `R_N>=1`.

For every odd `d` satisfying

$$
d^2\mid N,\qquad3\le d\le N^{1/4096},                   \tag{1.2}
$$

set

$$
G_{d,N}(a,b)=T_N((N/d)a,(N/d)b),\quad
P_{\chi,d,N}=d^{-2}\sum_{g\in(\mathbb Z/d\mathbb Z)^2}
\overline{\chi(g)}G_{d,N}(g),\qquad c=d^{-2}.
$$

Uniformly over these divisors and all characters,

$$
\boxed{\left|N^{-1}\operatorname{Tr}
(P_{\chi,d,N}U_N^{-r}P_{\eta,d,N}U_N^r)-c^2\right|
\le\varepsilon_N,\qquad r_0\le|r|\le t_N.}              \tag{1.3}
$$

For the full matrix-commutant projection `E_U`, let `s_0=2r_0-1`. Then

$$
\boxed{N^{-1}\|\mathcal E_{U_N}(P_{\chi,d,N})-cI\|_{\rm HS}^2
\le\frac{s_0(c-c^2)}{L_N}+\varepsilon_N.}                \tag{1.4}
$$

The finite early lags are included in `s_0`; they are not asserted to
satisfy (1.3).

Let `P_old,N` project onto the sum of all canonical oldspaces and put
`c_N=rank(P_old,N)/N`. Along every odd dimension,

$$
\boxed{N^{-1}\|\mathcal E_{U_N}(P_{{\rm old},N})-c_NI\|_{\rm HS}^2
\le\frac{s_0}{2L_N}+\frac2{R_N}+2C N^{-15\beta/4096}
=O((\log N)^{-1}).}                                    \tag{1.5}
$$

For square-free dimensions the left side is exactly zero.

## 2. A uniform relative sublevel estimate

Use `Psi=S Phi_tau`, with `S=((3,4),(2,3))`, and
`kappa_(g,h,r)=Psi^r t_h Psi^-r t_g`. In fixed eigen-coordinates
`(u,s)`, both `||D Psi||,||D Psi^-1||<=6`. Distances below are quotient
distances in this fixed norm. Their comparison with the original
coordinates changes only constants. Stable graphs are
`x+t e_s+gamma_x(t)e_u`. Shrink a single fixed chart radius so that
the graph bounds of both geometric inputs hold on a common disk.

The uniform contact theorem supplies `J,c_*>0` such that

$$
F_{x,h,z}(t)=\gamma_x(t)-z-\gamma_{x+h+ze_u}(t)             \tag{2.1}
$$

satisfies, on a fixed real interval,

$$
\max_{0\le j\le J}|\partial_t^jF_{x,h,z}(t)|
\ge c_*(|h|_{\mathbb T}+|z|).                           \tag{2.2}
$$

The normalized functions and their fixed derivatives are uniformly
bounded. To specify its substantive input, `x -> gamma_x` is C1 into
a fixed holomorphic space. Compactifying the normalized family at
`(h,z)=(0,0)` gives
`-z_*-D_x gamma_x(t)(w+z_* e_u)`. Its value at zero detects `z_*`;
if `z_*=0`, the proved infinitesimal rigidity detects nonzero `w`.
That rigidity uses analyticity of `D sigma(.)w` along complete dense
stable leaves and the nonzero fundamental Fourier coefficients of the
exact stable leaf coordinate. Thus (2.2) uses no genericity assertion.

The finite-derivative argument gives relative sublevel length
`C min{1,(epsilon/|h|_T)^beta}`, where `beta=1/J`. It remains valid
under a `C^J` error at most `(c_*/2)|h|_T`, when normalized derivatives
through `J+1` remain bounded. We check this for exact iterates.

Suppose the ORIGINAL return-defect set at threshold `epsilon` is
nonempty. After `x=Psi^r(y)-g`, one of its points satisfies

$$
\operatorname{dist}_{\mathbb T}
(\Psi^r(y+h),\Psi^r(y)-g)\le C_0\epsilon.
$$

Therefore, before enlarging the set,

$$
|g|_{\mathbb T}\le6^r|h|_{\mathbb T}+C_0\epsilon.         \tag{2.3}
$$

At a center `z` of the finite forward target stable segment, its
translate by `-g` has graph `gamma_z` based at `z-g`. The actual
stable graph there is `gamma_(z-g)`. C1 dependence in the holomorphic
norm bounds their initial difference by `C|g|_T`. Exact inverse graph
contraction has factor at most `1/8` on a fixed disk. After `r` steps,
the graph error and its derivatives of each fixed order `j` are at most

$$
C_j8^{-r}|g|_{\mathbb T}
\le C_j(6/8)^r|h|_{\mathbb T}+C_jC_0 8^{-r}\epsilon.       \tag{2.4}
$$

When `epsilon<=c_0|h|_T`, one fixed `r_0`, independent of the
translations, makes the `C^J` error at most `(c_*/2)|h|_T`; the
normalized `J+1` derivative bound is also uniform. If instead
`epsilon>c_0|h|_T`, the area estimate below is trivial after increasing
its constant. An empty original set needs no estimate. In particular,
(2.3) must not be inferred from an enlarged tube intersection alone.

We spell out a needed re-centering. A nearby true target is initially
written `Delta_u+gamma_y(t-Delta_s)`, where `y=x+h+Delta`. Put
`z=Delta_u+gamma_y(-Delta_s)`. Uniqueness of stable graphs gives

$$
\Delta_u+\gamma_y(t-\Delta_s)
=z+\gamma_{x+h+ze_u}(t).                               \tag{2.5}
$$

Thus (2.1) covers every nearby target leaf. If its exact inverse
graph is `gamma_y+E`, the error after re-centering is
`E(t-Delta_s)` with the same inner-disk `C^J` bounds. Choose the fixed
covering patches small enough that `|z|` remains in the contact
theorem's range. Dividing by `|h|_T+|z|` improves the bound relative
to `|h|_T`.

Now apply the finite-curve proof from the logarithmic input. For a
source stable plaque `C`, the exact finite target

$$
D=\Psi^{-r}(\Psi^r(C)-g)
$$

has length at most `C_1 6^r` and admits at most `C_2 6^r` short inverse
graph patches. A return defect at most `epsilon` puts `y+h` within
distance `C_3 6^r epsilon` of this finite curve. Analytic extensions
handle local bounds and endpoints only; the complete dense leaf is
not used for the tube or its counting. Each patch contributes source
parameter length at most `C(6^r epsilon/|h|_T)^beta` by (2.2)--(2.5).
Bounded transverse Jacobians yield, uniformly for `r>=r_0`, `h!=0`,
arbitrary `g`, and `0<epsilon<=1`,

$$
\boxed{\operatorname{area}\left\{x:
\max_i|e^{2\pi i(\kappa_{g,h,r,i}(x)-x_i)}-1|\le\epsilon\right\}
\le C36^r\left(\frac{\epsilon}{|h|_{\mathbb T}}\right)^\beta.}
                                                               \tag{2.6}
$$

If the tube radius exceeds the fixed chart size, this follows from
total area one: then `6^r epsilon` has a fixed positive lower bound,
whereas `|h|_T` has a fixed upper bound. Since `beta<=1`, the factor
`36^r` absorbs that case. It also absorbs `epsilon>c_0|h|_T`.
Thus every threshold is covered.

The essential uniformity is the relative error (2.4). An absolute
`C8^-r` error would require waiting time proportional to `log(1/|h|_T)`.
The actual relative error requires only the single fixed `r_0`.

## 3. Quantum trace errors for growing denominators

For `N=d^2m`, let

$$
\mathscr F_{g,h,r,N}=G_{d,N}(g)U_N^{-r}G_{d,N}(h)U_N^r.
$$

A nonzero translation in the group has `|h|_T>=c_1/d` with a fixed
constant. The exact Egorov/trace-cutoff estimate (9.1) in the
logarithmic input and (2.6) give, for `r>=r_0`,

$$
\frac{|\operatorname{Tr}\mathscr F_{g,h,r,N}|}{N}
\le C6^r d^{\beta/2}\delta^{\beta/4}
+C(r+1)256^{10r}N^{-1}\delta^{-6}.                       \tag{3.1}
$$

The constants are independent of the denominator. Only two fixed
coordinate characters are propagated by Egorov; the varying cutoff
uses the exact Weyl products and Hilbert--Schmidt bound.

Take `delta=N^-1/48`, `d<=N^(1/4096)`, and `r<=beta log N/4096`.
Since `log6<2`, the first term's exponent is at most

$$
-\beta/192+\beta/8192+\beta/2048\le-\beta/256.            \tag{3.2}
$$

For the second, `log256<6`, `beta<=1`, and
`log N+1<=C N^1/32` give exponent at most
`-7/8+15/1024+1/32=-849/1024<-3/4`. Thus (3.1) is at most
`epsilon_N=C N^(-beta/256)`. If `h=0,g!=0` the trace is exactly zero;
the identity pair contributes `N`; the case `g=0,h!=0` also has zero
trace by cyclicity.

Expanding the projectors proves (1.3), since the identity-pair
coefficient is `d^-4` and the absolute values of the other pair
coefficients sum to at most one. Negative lags follow by cyclicity
and exchange of the projectors.

## 4. Early lags, full commutants, and spectral windows

For `B=P_(chi,d,N)-cI`, Cauchy--Schwarz gives at every lag

$$
|N^{-1}\operatorname{Tr}(BU_N^{-r}BU_N^r)|\le c-c^2.      \tag{4.1}
$$

Average its conjugates at times `0,...,t_N`. In the square of this
average, the lags `|r|<r_0` have total weight at most `s_0/L_N`,
where `s_0=2r_0-1`. Use (4.1) on them and (1.3) on the remaining lags:

$$
N^{-1}\left\|L_N^{-1}\sum_{j=0}^{L_N-1}U_N^{-j}BU_N^j\right\|_{\rm HS}^2
\le s_0(c-c^2)/L_N+\varepsilon_N.                        \tag{4.2}
$$

Orthogonal projection onto the full commutant is a contraction and
keeps the commutant component of this average. This proves (1.4),
including complete repeated-eigenvalue blocks.

For a Hermitian centered `B`, define the positive spectral measure

$$
\nu_{B,N}=N^{-1}\sum_{\zeta,\omega\in\operatorname{Spec}U_N}
\|\Pi_\zeta B\Pi_\omega\|_{\rm HS}^2
\delta_{(\arg\zeta-\arg\omega)/(2\pi)}.
$$

The normalized Fejer kernel of length `L_N` is at least `4/pi^2`
within `1/(2L_N)` of its center. Expanding it and applying the same
lag bounds with their phases proves, for the sector observable,

$$
\sup_\xi\nu_{B,N}\{t:\operatorname{dist}(t,\xi)\le1/(2L_N)\}
\le\frac{\pi^2}{4}\left(s_0(c-c^2)/L_N+\varepsilon_N\right).          \tag{4.3}
$$

## 5. Exact oldspace lattice and a prime-product bound

For `d^2|N`, the canonical oldspace is

$$
\mathcal H_{d,N}=\{\psi:\psi(x)=0\text{ if }d\nmid x,
\quad\psi(x+N/d)=\psi(x)\},
$$

and its projector has rank `N/d^2`. The exact identity is

$$
P_{d,N}P_{e,N}=P_{\operatorname{lcm}(d,e),N}.             \tag{5.1}
$$

Indeed the defining Weyl groups commute: their symplectic products
are multiples of `N^2/(de)`, itself a multiple of `N`, since `de|N`.
The common invariant subspace has support in multiples of `lcm(d,e)`
and shift invariance generated by `N/d,N/e`, namely `N/lcm(d,e)`.
This proves (5.1).

Every other oldspace is contained in a prime-index one. Hence

$$
P_{{\rm old},N}=I-\prod_{p^2\mid N}(I-P_{p,N}),\qquad
c_N=1-\prod_{p^2\mid N}(1-p^{-2}),\qquad0\le c_N<1/4.    \tag{5.2}
$$

Expand the product and use (5.1) for the rank formula. The bound is
`sum_(p>=3)p^-2 <= sum_(n>=1)(2n+1)^-2 <1/4`, obtained from
`(2n+1)^2>4n(n+1)` and a telescoping sum. Empty products give zero
oldspace projector.

For every integer `n>=1`, the elementary estimate

$$
\prod_{p\le n}p\le4^n                                  \tag{5.3}
$$

holds by induction. If `n=2m`, the primes in `(m,2m]` divide
`binom(2m,m)<=4^m`, and the product up to `m` is at most `4^m`.
If `n=2m+1>=3`, use the primes in `(m+1,2m+1]` dividing
`binom(2m+1,m)<=2^(2m)=4^m`; the odd binomial row has two equal
maximal terms. Multiply by the inductive bound `4^(m+1)`.
The case `n=1` is immediate. No asymptotic theorem on primes is used.

## 6. The sum of all oldspaces

Let `Q_N` use only primes `p<=R_N`, `p^2|N` in (5.2), and let
`q_N=rank Q_N/N`. If none occur, set `Q_N=0`; otherwise their product
`d_0` satisfies `d_0^2|N` and

$$
d_0\le4^{R_N}\le N^{\beta\log4/8192}\le N^{1/4096}.      \tag{6.1}
$$

Thus the uniform group trace estimate applies to this growing divisor.
If `s` primes occur, inclusion--exclusion expresses `Q_N` as a signed
sum of `2^s-1` projectors. Each is an average of a subgroup of
`G_(d_0,N)` with coefficient l1 norm one. The identity coefficient
of `Q_N` equals `q_N`, since every nonidentity group element has
zero trace. Thus `B_N=Q_N-q_NI` has zero identity coefficient and
coefficient l1 norm at most `2^s<=2^(R_N)`.

For `r_0<=|r|<=t_N`, the group trace estimate implies

$$
|N^{-1}\operatorname{Tr}(B_NU_N^{-r}B_NU_N^r)|
\le4^{R_N}\varepsilon_N.                               \tag{6.2}
$$

At smaller lags use directly `q_N-q_N^2<=1/4`, with no coefficient
norm factor. The finite average and full commutant projection give

$$
N^{-1}\|\mathcal E_{U_N}(Q_N)-q_NI\|_{\rm HS}^2
\le\frac{s_0}{4L_N}+4^{R_N}\varepsilon_N.               \tag{6.3}
$$

The difference `D_N=P_old,N-Q_N` is an orthogonal projector of rank
fraction `delta_N=c_N-q_N`, with

$$
\delta_N\le\sum_{p>R_N,\ p^2\mid N}p^{-2}
\le\sum_{n>R_N}n^{-2}\le1/R_N.                          \tag{6.4}
$$

Commutant projection is a contraction, so
`N^-1||E_U(D_N)-delta_N I||_HS^2<=delta_N-delta_N^2<=1/R_N`.
Combine with (6.3) by the squared triangle bound. Finally

$$
4^{R_N}\varepsilon_N
\le C N^{\beta/4096-\beta/256}
=C N^{-15\beta/4096}.                                  \tag{6.5}
$$

This proves (1.5) for all odd dimensions. If `d_0=1`, the small-prime
part vanishes and only the tail estimate is needed.

For any orthonormal eigenbasis, including arbitrary choices inside
degenerate eigenspaces,

$$
\frac1N\sum_j\left|\|P_{{\rm old},N}\psi_{j,N}\|^2-c_N\right|^2
\le\frac{s_0}{2L_N}+\frac2{R_N}+2C N^{-15\beta/4096}.     \tag{6.6}
$$

For fixed `eta>1/4`, the fraction with total oldspace mass at least
`eta` is therefore `O_eta(1/log N)`. For deviations of size `epsilon`
from the exact varying mean `c_N`, divide the same bound by `epsilon^2`.

## 7. Any individual oldspace and windows for the full sum

For every fixed `eta>1/9`, uniformly in the orthonormal eigenbasis,

$$
\boxed{\frac1N\#\{j:\exists d\ge3,\ d^2\mid N,
\ \|P_{d,N}\psi_{j,N}\|^2\ge\eta\}
\le\frac{s_0}{4L_N(\eta-1/9)^2}
+\frac{R_N\varepsilon_N}{(\eta-1/9)^2}
+\frac1{\eta R_N}
=O_\eta((\log N)^{-1}).}                               \tag{7.1}
$$

It suffices to consider prime-index oldspaces. For `p<=R_N`, use
(1.4), mean `p^-2<=1/9`, and Chebyshev. Sum the resulting bounds with
`sum_(p>=3)p^-2<1/4` and at most `R_N` primes. These primes satisfy
(1.2) for large `N`. For `p>R_N`, use the exact trace mean and the
union bound `eta^-1 sum_(p>R_N)p^-2<=1/(eta R_N)`.

Let `B_old=P_old,N-c_NI`. The positive measure from Section 4 obeys

$$
\boxed{\sup_\xi\nu_{B_{\rm old},N}
\{t:\operatorname{dist}(t,\xi)\le1/(2L_N)\}
\le\frac{\pi^2}{4}\left(\frac{s_0}{2L_N}+\frac2{R_N}
+2C N^{-15\beta/4096}\right).}                          \tag{7.2}
$$

To verify the tail term, split `B_old=(Q_N-q_NI)+(D_N-delta_NI)`.
Apply the time average with center-dependent phases. The first part
has squared normalized Hilbert--Schmidt norm bounded by (6.3), using
the same lag estimates. The average of the second is a contraction
by the triangle inequality, and its squared norm is at most
`delta_N-delta_N^2`. Apply the squared triangle bound and the Fejer
lower bound `4/pi^2` on the window. No estimate on the tail's separate
lag correlations is needed.

## 8. Exact limitations

The denominator range, the single fixed waiting time, and the
logarithmic horizon follow from uniform estimates for the original
map and matrices. The auxiliary finite time average occurs inside
a proved Hilbert--Schmidt inequality. There is no averaging over
dimensions, kick parameters, or independent random phases.

The results concern matrix-element weights and eigenvector mass.
No positive lower bound for those weights on every close eigenphase
pair has been proved. The estimates do not control every principal
angle and do not evaluate microscopic unweighted eigenphase
correlations. Even when (7.2) is restricted to narrower windows,
its measure retains the stated weights. The order-`N` signed quantum
trace cancellations required for `H_diag` remain unproved.
