> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round2_2026_10_20/fermionic_signed_three_cell_profile.md`. Embedded SHA256: `edf6fa35b9f60dc9c19fbb4c588265c1157abe637f4bae94e2e4b2b88db68be5`.
> [Thematic guide](../../topics/histories.md).

# The full signed three-cell family: an actual oscillatory profile

Research continuation, 20 October 2026. The operator is the exact
family in the question, with the same fixed value
$\tau=10^{-80}$, and every limit below is along all odd dimensions.

## The result

The preceding coherent-pair theorem selected a sufficiently large
constant in its logarithmic buffer length to make every selected
cross term positive. Here that restriction is removed. The full
signed sum of the same three-cell permutation family has an explicit
asymptotic profile, with error $o(N)$ uniformly for
$N\le m\le3N/2$. Its leading profile is a positive trace cube.
Individual terms need not be positive.

Let $z_*$ be the actual image of the interior coded fixed point
$(1/2,0)$, let $\Lambda>5$ be its unstable multiplier for the
actual inverse map $\Psi$, and fix any integer $R_0\ge0$, including
$R_0=0$. Put

$$
 R=R_N=\left\lceil\frac{\log N}{2\log\Lambda}\right\rceil+R_0,
 \qquad k=2R,\qquad \varepsilon=\Lambda^{-k},
 \qquad x_N=N\varepsilon .
 \tag{T.1}
$$

Thus

$$
 \Lambda^{-2R_0-2}\le x_N\le\Lambda^{-2R_0}.
 \tag{T.2}
$$

The family $\mathcal A^{\rm full}_{m,N}$ consists of all good
three-cell pairs defined in Section 7 below. There is no test of
their phases and no further positivity selection. With the exact
principal-orbit weights $a_{p,N}$, define

$$
 E^{\rm full}_{m,N}
 =\sum_{(p,p')\in\mathcal A^{\rm full}_{m,N}}
            2m^2\operatorname{Re}
                 (a_{p,N}\overline{a_{p',N}}).
 \tag{T.3}
$$

Each unordered pair is counted once. The factor $2m^2$ comprises
the two ordered directions and all pointed pairs.

There are fixed positive constants $c_*,\kappa_{\rm esc},\chi$
and two explicitly defined actual probability measures
$\sigma,\upsilon$ of bounded support on $\mathbb R$, independent
of $m,N$, such that

$$
 \boxed{\displaystyle
 E^{\rm full}_{m,N}
  =\frac{c_*}{144}\,m^4\varepsilon^3
       e^{-\kappa_{\rm esc}m\varepsilon}
       \operatorname{Tr}(K_{2\pi\chi x_N}^{\,3})+o(N),
 \qquad N\le m\le3N/2.}
 \tag{T.4}
$$

The error is uniform in that interval. The operator on
$L^2(\sigma)$ is

$$
 (K_t f)(s)=\int
       \left[\int e^{it(s-s')u}\,d\upsilon(u)\right]
                      f(s')\,d\sigma(s').
 \tag{T.5}
$$

It is positive and trace class, with trace one, and
$\operatorname{Tr}(K_t^3)>0$ for every finite real $t$.
Consequently there are constants $c,C>0$ such that

$$
 cN\le E^{\rm full}_{m,N}\le CN
 \quad(N\le m\le3N/2,\ N\text{ sufficiently large odd}).
 \tag{T.6}
$$

For every continuous fixed weight $w$ on $[1,3/2]$, the
more precise pair-scale statement is

$$
 \boxed{\begin{aligned}
 \frac1{N^2}\sum_{N\le m\le3N/2}w(m/N)E^{\rm full}_{m,N}
  ={}&\frac{c_*}{144}x_N^3
       \operatorname{Tr}(K_{2\pi\chi x_N}^{\,3})\\
    &{}\times\int_1^{3/2}w(v)v^4e^{-\kappa_{\rm esc}x_Nv}\,dv
       +o(1).
 \end{aligned}}
 \tag{T.7}
$$

The bounded rounding parameter $x_N$ is retained exactly; its
convergence is not assumed. This is a theorem about an actual
signed subsum at Heisenberg time. It does not evaluate the
complementary orbit pairs or prove $H_{\rm diag}$.

## 1. Checked inputs and conventions

The following are proof inputs, identified by their frozen text.
All new transitions required for (T.4) are proved below.

| Input | SHA-256 |
|---|---|
| fermionic_coherent_pair_mass.md | dc6ff71218f427c6d4dc0da4d7c3b833d641cd7107eb43e65d9f11da4e498816 |
| fermionic_homoclinic_and_doubled_transfer.md | 85e74eda0116dbbda1e3ba7a1028fbeb36da97072b7a92b3addc5d3004024168 |
| fermionic_quantitative_pressure.md | d9efc87ad9c2977b1ae3ca78da26e5f974ce119a22585bcd87e2c76cab5a74b2 |

We use the notation of the first input. The twelve-edge Berg
shift has incidence $\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$,
and $\lambda=3+2\sqrt2$. A loop denoted $0$, at vertex $i$,
codes the interior fixed point $(1/2,0)$. The distinct loop
$a:i\to i$ is fixed. Write $o=000\cdots$. If two codes agree
on a central block of radius $j$, their actual points are within
$C\lambda^{-j/2}$. The exact equivariant conjugacy obeys

$$
 \Psi H\pi=H\pi\sigma^{-1}.
 \tag{1.1}
$$

Thus physical motion under $\Psi$ traverses coded cells backwards.
A physical cell input is its right coded endpoint, and its output
is its left coded endpoint.

The exact generating function, including its phase gauge, is

$$
 F(Q,q)=-(3Q^2-2Qq+3q^2)/8+G(Q,q),
 \qquad p=-F_q,\quad P=F_Q .
 \tag{1.2}
$$

It is real analytic, and every second derivative of $G$ is
smaller than $10^{-70}$ on the real plane. Its derivatives on
deck-related charts have the exact covariance proved in the
inputs. The negative open-chain Hessian is between
$0.49I$ and $2.01I$, independent of chain length and winding.

For odd $N$, with $h=(2\pi N)^{-1}$, the exact Landau bundle
and phase are

$$
 (z,u)\sim(z+n,e^{in_pq/h}u),\qquad
 (z,u)\longmapsto(\Psi z,e^{iF(Q,q)/h}u).
 \tag{1.3}
$$

This includes the cancellation of the original half-winding
phase against $(-1)^{n_qn_p}$. Therefore a fixed coded cell $e$
has the exact physical boundary action

$$
 \begin{split}
 W_e(q_{\rm out},q_{\rm in})
   &=\operatorname*{crit}_{q_1,\ldots,q_{d-1}}
                 \sum_{j=0}^{d-1}F(q_{j+1},q_j)
                    -(n_e)_p q_{\rm out},\\
 q_0&=q_{\rm in},\qquad
 q_d=q_{\rm out}+(n_e)_q ,
 \end{split}
 \tag{1.4}
$$

where $n_e$ is its constant coded branch displacement. It is the
same for homoclinic and periodic extensions. Its derivatives are

$$
 \partial_{\rm out}W_e=p_{\rm out},\qquad
 \partial_{\rm in}W_e=-p_{\rm in},\qquad
 0.49I\le-D^2W_e\le2.01I .
 \tag{1.5}
$$

The frozen proof establishes the branch assertion before using
stationary uniqueness: inverse strip labels are constant and are
transported by the equivariant lift conjugacy. Hence no change of
branch is inferred from closeness alone.

For the exact principal weight of any primitive period-$m$
orbit, the inputs prove

$$
 \left|\log(|a_{p,N}|^2\Lambda_p)\right|\le Cmh^2.
 \tag{1.6}
$$

If the same buffered cells are permuted, they also prove the
localized scalar-cocycle comparison

$$
 \left|\log\frac{\Gamma_h(p,m)}{\Gamma_h(p',m)}\right|
                \le C\theta^R,\qquad\theta=2/3,
 \tag{1.7}
$$

for three cells, independently of their lengths. It is the
sum of decaying distances from the cell boundaries, not
$m\theta^R$.

The actual positive transfer operator is

$$
 (\mathcal T f)(x)=
  \sum_{e:j\to i(x)}
    \frac{l_j}{\lambda l_{i(x)}}e^{v(ex)}f(ex),
 \quad l=(\sqrt2,1),\qquad
 \mathcal T^n=\mathfrak h\nu+O((9/10)^n)
 \tag{1.8}
$$

in the fixed one-sided Hölder Banach space $C_\theta$.
Here $\mathfrak h>0$, $\nu$ is positive,
$\nu(1)=\nu(\mathfrak h)=1$, and the rank-one term is the spectral
projection. The potential $v$ is that of the actual geometric
unstable Jacobian, expressed in the checked one-sided gauge. On
periodic codes of length $m$,

$$
 \lambda^{-m}e^{\sum_{j<m}v(\sigma^jx)}
                  =\Lambda_{H\pi x}^{-1}.
 \tag{1.9}
$$

For an edge $e$, let $J_e$ be its summand in (1.8); put
$J=J_0$ and $A=J_a$. For a chronological word $w=e_1\cdots e_K$,
write
$J_w=J_{e_K}\cdots J_{e_1}$.
The rightmost operator supplies the earliest edge. The zero branch
satisfies

$$
 \|\Lambda^jJ^j-g\delta_o\|_{C_\theta\to C_\theta}
       \le C\theta^j,\qquad
 g(o)=1,\quad Jg=\Lambda^{-1}g,\quad
 (J^jf)(o)=\Lambda^{-j}f(o).
 \tag{1.10}
$$

The function $g$ is zero off vertex $i$ and strictly positive
on that vertex. Its formula is
$$
 g(x)=\exp\sum_{j\ge1}[v(0^jx)-v(o)]\quad(i(x)=i).
 \tag{1.11}
$$

The constants appearing in (T.4) will be

$$
 c_*=[\nu(Ag)(A\mathfrak h)(o)]^3,\qquad
 \kappa_{\rm esc}=(1-\Lambda^{-1})\nu(g)\mathfrak h(o),
 \qquad\chi=s_{\rm s}-s_{\rm u}.
 \tag{1.12}
$$

The slopes $s_{\rm u}<0<s_{\rm s}$ are the unstable and stable
physical slopes $dp/dq$ at $z_*$. Their positivity difference
and their occurrence in the phase are checked next.

## 2. Exact scattering coordinates of a buffered excursion

### 2.1. Tail limits, including their normalization

The homoclinic construction in the first input is uniform over
every finite $i$-to-$i$ word $u$. For its extension
$0^\infty a u a0^\infty$, both endpoints of the cell
$0^R a u a0^R$ are within $C\Lambda^{-R}$ of $z_*$.
The input proves this by a local backward-sequence contraction,
followed by the scalar recurrence on a $C^2$ invariant curve.
We require the following sharper consequence of that same
recurrence and give the argument.

Use $t=q-q_*$ as coordinate on either local invariant curve.
Both curves are nonvertical since the map is the indicated tiny
perturbation of $L$. In the direction toward the fixed point,
the scalar map $f$ satisfies

$$
 f(t)=\Lambda^{-1}t+O(t^2),\qquad
 |f^j(t)|\le C\Lambda^{-j}|t|
 \tag{2.1}
$$

on a fixed interval. All estimates are uniform there. Therefore

$$
 |\Lambda^{j+1}f^{j+1}(t)-\Lambda^jf^j(t)|
             \le C\Lambda^{-j}|t|^2.
 \tag{2.2}
$$

The sequence converges uniformly to a limit $L_*(t)$, and

$$
 f^j(t)=\Lambda^{-j}L_*(t)+O(\Lambda^{-2j}).
 \tag{2.3}
$$

This limit is Lipschitz. Indeed
$$
 \Lambda^j(f^j)'(t)
   =\prod_{b=0}^{j-1}\Lambda f'(f^b(t)),
 \tag{2.4}
$$
and each factor is $1+O(\Lambda^{-b}|t|)$. The products are
uniformly bounded; the mean value inequality proves the asserted
Lipschitz bound. The common finite number of iterates needed to
enter the interval, already established uniformly in the input,
only changes these fixed constants.

Consequently there are bounded real coefficients $U(u),S(u)$
such that, with $\delta=\Lambda^{-R}$,

$$
 \begin{array}{ll}
 q_{\rm in}^{\rm hom}=q_*+\delta U(u)+O(\delta^2),
   &p_{\rm in}^{\rm hom}=p_*+s_{\rm u}\delta U(u)+O(\delta^2),\\
 q_{\rm out}^{\rm hom}=q_*+\delta S(u)+O(\delta^2),
   &p_{\rm out}^{\rm hom}=p_*+s_{\rm s}\delta S(u)+O(\delta^2).
 \end{array}
 \tag{2.5}
$$

Every error is uniform in $u$, its length, and $R$. The output
lies on the stable curve and the input on the unstable curve
because physical motion is backwards in the coded word.

The exact indexing is as follows. For an infinite future
$x=x_0x_1\cdots$ starting at $i$, form the two-sided code
whose negative edges are zero, whose edge zero is $a$, and whose
edges $1,2,\ldots$ are $x$. Define $S(x)$ by the limit
$\lim_{R\to\infty}\Lambda^R(q(H\pi\sigma^{-R}x^{\rm ext})-q_*)$,
in the local fixed-point chart. For an infinite past ending at
$i$, put that past before an edge $a$ at position $-1$, and
put zero edges at all nonnegative positions. Define $U$ by the
analogous limit with $\sigma^R$. This puts the cut exactly $R$
zero edges before the first $a$, or after the last $a$.
For a finite excursion,

$$
 S(u)=S(u a0^\infty),\qquad
 U(u)=U(0^\infty a u).
 \tag{2.6}
$$

There is no extra one-edge multiplier in these definitions.

### 2.2. Dependence only on the corresponding endpoint

The function $S$ has the following modulus: if two futures
have the same first $K$ edges, then

$$
 |S(x)-S(x')|\le C\lambda^{-K/2}.
 \tag{2.7}
$$

To prove it, choose the common fixed number of zero-tail steps
that puts every endpoint on the local stable curve. At that
point the two codes agree on a central block of radius at least
$K$, up to a fixed indexing constant. Equation (1.1) and its
stated Hölder coding bound give a distance $C\lambda^{-K/2}$.
The local limit coordinate (2.2)--(2.4), and the fixed finite
entry map, are Lipschitz. This proves (2.7).

The same proof for the inverse local curve shows that $U$
varies by at most $C\lambda^{-K/2}$ when the last $K$ past
edges agree. These arguments also define both functions on all
admissible one-sided endpoint sequences, by completion. Uniform
boundedness follows from the common entry neighborhood.

Thus each function has approximants $S_K,U_K$, constant on
the appropriate $K$-edge cylinders, satisfying

$$
 \|S-S_K\|_\infty+\|U-U_K\|_\infty
                         \le C\lambda^{-K/2}.
 \tag{2.8}
$$

An arbitrary admissible continuation can be chosen on each
cylinder. Its choice is immaterial for (2.8).

## 3. The uniform quadratic action limit

### 3.1. The limiting two-endpoint Hessian

For all long cells $0^R a u a0^R$, and for endpoint positions
within $C\delta$ of $(q_*,q_*)$, we claim

$$
 D^2W_e=
   \begin{pmatrix}s_{\rm u}&0\\0&-s_{\rm s}\end{pmatrix}
          +o(1)
 \tag{3.1}
$$

in the order $(q_{\rm out},q_{\rm in})$, uniformly over all
interior words of length at least $m/9$, $m\asymp N$.
This requires no differentiability of the global conjugacy or
of the invariant bundles.

Here is an elementary tridiagonal proof. The internal negative
Hessian has diagonal entries in $[1.49,1.51]$ and neighboring
entries $-b_j$, $b_j\in[.24,.26]$. Changing either boundary
position by $O(\delta)$ changes every internal stationary
position by $O(\delta)$, uniformly in the chain length. To see
this, differentiate the internal critical equations. The forcing
is supported at the first and last internal coordinates and
has norm $O(\delta)$. Strict diagonal dominance gives a uniform
row-sum bound for the inverse: after dividing by the diagonal,
the off-diagonal row sum is at most $.52/1.49<1$, so its Neumann
series is uniformly summable. Integration along the boundary
segment proves the same assertion for finite changes. Momentum
changes are also $O(\delta)$, by (1.2) and its bounded Hessian.

For the first and last $j\le\lfloor R/2\rfloor$ physical edges
the homoclinic path is within
$C\Lambda^{-(R-j)}$ of the fixed orbit. The modified stationary
path is consequently within
$C(\Lambda^{-R/2}+\delta)$ there. Exact deck reduction identifies
their generating-function Hessians with the fixed edge Hessian,
up to an error tending uniformly to zero.

Elimination of a tridiagonal internal block gives continued
fractions

$$
 d_j=a_j-\frac{b_j^2}{d_{j+1}},\qquad d_j\ge1.4.
 \tag{3.2}
$$

The lower bound is preserved since
$1.49-.26^2/1.4>1.4$. Dependence on the next denominator has
derivative at most $.26^2/1.4^2<.04$. Thus a fixed endpoint
Schur diagonal depends on coefficients beyond distance $j$
by at most $C(.04)^j$. On its first $\lfloor R/2\rfloor$
edges the coefficients converge uniformly to their fixed-point
values. This proves uniform convergence of each endpoint
diagonal. The off-diagonal endpoint entry tends to zero as well:
the tridiagonal inverse endpoint formula, or the same elimination,
bounds it by

$$
 C(.26/1.4)^{d-1}.
 \tag{3.3}
$$

Let $\alpha_*=F_{QQ}$, $\beta_*=F_{Qq}>0$, and
$\gamma_*=F_{qq}$ on the fixed lifted edge. The limiting
continued fraction is the larger positive solution

$$
 d_*=-\alpha_*-\gamma_*-\frac{\beta_*^2}{d_*}.
 \tag{3.4}
$$

The output and input Hessian limits are respectively
$\alpha_*+\beta_*^2/d_*$ and
$\gamma_*+\beta_*^2/d_*$. For an input slope $s$, differentiating
(1.2) gives the output slope and the horizontal expansion

$$
 s'=\alpha_*-\frac{\beta_*^2}{\gamma_*+s},
 \qquad b=-\frac{\gamma_*+s}{\beta_*}.
 \tag{3.5}
$$

Consequently

$$
 s_{\rm u}=\alpha_*+\frac{\beta_*^2}{d_*},\qquad
 s_{\rm s}=-\gamma_*-\frac{\beta_*^2}{d_*},\qquad
 \Lambda=\frac{d_*}{\beta_*}>5.
 \tag{3.6}
$$

The two expansions in (3.5) are $\Lambda$ and
$\Lambda^{-1}$, which identifies these as the actual eigen
slopes. In particular

$$
 \chi=s_{\rm s}-s_{\rm u}
            =\beta_*(\Lambda-\Lambda^{-1})>0.
 \tag{3.7}
$$

This completes the proof of (3.1). Its convergence was established
on the whole required boundary neighborhood, not just at one
point.

### 3.2. Stationary elimination and the phase polynomial

At the homoclinic endpoints, (1.5) gives the gradient of $W_e$
exactly. Translate both endpoint positions back to $q_*$, and
use (2.5) and (3.1). Uniformly over every cell,

$$
 \begin{split}
 \partial_{\rm out}W_e(q_*,q_*)&=
                 p_*+\chi\delta S(u)+o(\delta),\\
 \partial_{\rm in}W_e(q_*,q_*)&=
                -p_*+\chi\delta U(u)+o(\delta).
 \end{split}
 \tag{3.8}
$$

For a physical cyclic ordering of three cells, the gradient at
the constant cut vector therefore has components
$\chi\delta(S_{\rm previous}+U_{\rm next})+o(\delta)$.
Its Hessian is $-\chi I+o(1)$. The exact strong concavity
from (1.5) first places the critical cut vector within
$C\delta$ of that constant vector: apply the monotonicity
inequality for its gradient and the bound $O(\delta)$ at the
constant vector. Hence (3.1) is applicable throughout the segment
to the critical cut vector. Taylor's formula now gives the
critical-value increment

$$
 \frac{\chi\delta^2}{2}
       \sum_{\text{physical consecutive cells }i,j}
                      (S_i+U_j)^2+o(\delta^2).
 \tag{3.9}
$$

The error is uniform in all interiors and lengths. In more detail,
the critical displacement is
$\delta(S_i+U_j)_j+o(\delta)$; substitution in the linear plus
quadratic Taylor terms proves (3.9). No derivative of a
length-dependent symbolic observable is used.

The value at the constant cut vector is
$\sum_eW_e(q_*,q_*)$, independent of cell order. The squares
$S_i^2,U_i^2$ in (3.9) cancel when two orders are compared.
Let the first coded order be $123$ and the second $132$.
Their physical orders, with a cyclic rotation to start at cell
one, are respectively $132$ and $123$. Thus, with

$$
 Q(\mathbf S,\mathbf U)
 =S_1U_2+S_2U_3+S_3U_1
           -S_1U_3-S_3U_2-S_2U_1,
 \tag{3.10}
$$

their exact action difference is

$$
 \mathcal S_{123}-\mathcal S_{132}
                   =-\chi\delta^2 Q+o(\delta^2).
 \tag{3.11}
$$

These actions are the exact sums of the boundary functions
(1.4), including their deck terms. The cocycle identity (1.3)
proves their equality to the original orbit phases. Therefore
no constant phase can be discarded when obtaining (3.11).

Here $\delta^2=\varepsilon$ and $N\varepsilon$ is bounded.
Combining (3.11) with (1.6)--(1.7), for the two full orbit weights,
gives

$$
 \boxed{\displaystyle
 a_{123,N}\overline{a_{132,N}}
   =\Lambda_{123}^{-1}
       e^{-it_NQ(\mathbf S,\mathbf U)}(1+o(1)),
 \qquad t_N=2\pi\chi N\varepsilon.}
 \tag{3.12}
$$

The complex relative error is uniform over all interiors and
all lengths under consideration. The modulus error is
$O(N^{-1})$, the cocycle ratio error is $O(\theta^R)$, and
the action error becomes $N\,o(\varepsilon)=o(1)$.
Thus the oscillatory endpoint function has bounded frequency
in the rescaled scattering coordinates. This is the point at
which a possible uncontrolled frequency-$N$ mixing estimate
has been avoided by an actual calculation.

## 4. Exact avoidance of additional long zero runs

The earlier union bound is insufficient if $R_0$ is not chosen
large. We now evaluate the complete avoidance condition.

Let $\mathcal G_{k,\ell}$ be the sum of branch operators of all
length-$\ell$ words with no $k$ consecutive zero edges, and
put $B=\mathcal T-J$. All these operators are positive. Their
generating function has the exact noncommutative identity

$$
 \boxed{\displaystyle
 \mathcal G_k(z)=\sum_{\ell\ge0}z^\ell\mathcal G_{k,\ell}
   =(I-z^kJ^k)
          (I-z\mathcal T+z^{k+1}BJ^k)^{-1}.}
 \tag{4.1}
$$

To prove it, write
$A_k(z)=\sum_{b=0}^{k-1}(zJ)^b$.
Every allowed word is a sequence of zero blocks of lengths
less than $k$, separated by nonzero edges. Thus, initially
for sufficiently small $z$, its operator series is
$A_k(I-zBA_k)^{-1}$. The exact product

$$
 (I-zBA_k)(I-zJ)
      =I-z\mathcal T+z^{k+1}BJ^k
 \tag{4.2}
$$

and $A_k(I-zJ)=I-z^kJ^k$ prove (4.1). This checks the order of
every factor without commuting them.

Let $\Pi=\mathfrak h\nu$ and $Q_0=I-\Pi$. From (1.8),
$(I-z\mathcal T)^{-1}$ on $Q_0C_\theta$ is uniformly bounded
for $|z|\le1.05$, since $1.05(9/10)<1$. Moreover

$$
 J^k=\varepsilon(g\delta_o+O(\theta^k)).
 \tag{4.3}
$$

The denominator of (4.1) is a small analytic perturbation of
$I-z\mathcal T$, of norm at most
$C(1.05/\Lambda)^k$ on that disk. On the $Q_0$ block it
remains uniformly invertible. Its Schur scalar on the line
$\mathbb C\mathfrak h$ is, when $|z-1|\le C_0\varepsilon$,

$$
 s_k(z)=1-z+\kappa_{\rm esc}\varepsilon z^{k+1}
               +O(\varepsilon\theta^k+\varepsilon^2).
 \tag{4.4}
$$

Indeed the linear perturbation on that line is
$\nu(Bg)\mathfrak h(o)\varepsilon z^{k+1}$.
The Schur correction is quadratic in the perturbation.
Invariance of $\nu$ and $Jg=\Lambda^{-1}g$ give exactly

$$
 \nu(Bg)=(1-\Lambda^{-1})\nu(g).
 \tag{4.5}
$$

All constants in (4.4) are uniform in $k$.

For completeness, this local scalar accounts for all possible
singularities on $|z|\le1.05$. Outside a fixed small disk
about $1$, the unperturbed full resolvent is uniformly bounded,
and the Neumann perturbation series is valid. Inside that disk
the $Q_0$ block is invertible. On its boundary the Schur scalar
is $1-z+o(1)$, so the elementary argument principle, or
Rouché's theorem, gives exactly one zero. Applying the same
comparison on $|z-1|=C_0\varepsilon$, with $C_0$ fixed
sufficiently large, puts it in that smaller disk. Equation (4.4)
and its differentiated version then give a simple real zero

$$
 z_k=1+\kappa_{\rm esc}\varepsilon
                  +O(k\varepsilon^2+\varepsilon\theta^k)>1,
 \qquad s_k'(z_k)=-1+O(k\varepsilon).
 \tag{4.6}
$$

Reality follows from real coefficients and uniqueness. The
Schur numerator and the numerator in (4.1) now give the pole
part in the normalization

$$
 \mathcal G_k(z)=\frac{\Pi_k}{1-z/z_k}+\mathcal H_k(z),
 \qquad \Pi_k=\Pi+O(k\varepsilon).
 \tag{4.7}
$$

The remainder is analytic on $|z|\le1.05$, and uniformly
bounded on its boundary. The bound follows there from the
full resolvent and the small perturbation; subtracting the
bounded normalized pole part preserves it. Cauchy's coefficient
formula therefore yields an $O(1.05^{-\ell})$ remainder in
operator norm. If $\ell\asymp N$, with
$\varepsilon N$ in the fixed compact interval (T.2), then
(4.6) also gives

$$
 z_k^{-\ell}
   =e^{-\kappa_{\rm esc}\varepsilon\ell}
                 +O(k\varepsilon+\theta^k).
 \tag{4.8}
$$

We have proved the quantitative uniform estimate

$$
 \boxed{\displaystyle
 \mathcal G_{k,\ell}
 =e^{-\kappa_{\rm esc}\varepsilon\ell}\mathfrak h\nu
       +O(k\varepsilon+\theta^k+1.05^{-\ell}),
 \qquad cN\le\ell\le CN.}
 \tag{4.9}
$$

It is an operator estimate on the actual fixed Hölder space.
It will only be applied to endpoint cylinders of fixed length.

## 5. The actual endpoint probability laws

For an admissible chronological length-$K$ prefix word $w$
starting at $i$, define

$$
 P_K(w)=\frac{\nu(J_wAg)}{\nu(Ag)}.
 \tag{5.1}
$$

For an admissible chronological length-$K$ suffix word $v$
ending at $i$, define

$$
 Q_K(v)=\frac{(AJ_v\mathfrak h)(o)}
                        {(A\mathfrak h)(o)}.
 \tag{5.2}
$$

These are probability distributions. Summing $J_w$ or $J_v$
over all length-$K$ words inserts $\mathcal T^K$; (1.8) gives
$\nu\mathcal T^K=\nu$ and $\mathcal T^K\mathfrak h=\mathfrak h$.
The denominators are strictly positive by the positivity facts
following (1.8)--(1.11).

The distributions are consistent. Appending an edge to the
right of a prefix gives $J_{we}=J_eJ_w$, so summing the extension
uses $\nu\mathcal T=\nu$. Prepending an edge to a suffix gives
$J_{ev}=J_vJ_e$, so summing that extension uses
$\mathcal T\mathfrak h=\mathfrak h$. Incompatible edge
compositions vanish automatically. The consistent finite
cylinders thus define probability measures $P$ on future
sequences and $Q$ on past sequences at vertex $i$.

Define

$$
 \sigma=S_*P,\qquad \upsilon=U_*Q ,
 \tag{5.3}
$$

using the precisely normalized scattering functions of Section 2.
They are actual probability measures of bounded support. No
Lebesgue density or smoothness of these measures is assumed.
Their definitions also fix every normalization in (T.5).

## 6. Factorization with avoidance, proved at fixed cylinders

### 6.1. Exact word formula and its positive normalization

For fixed interior lengths $\ell_1,\ell_2,\ell_3$, consider

$$
 w=0^R a u_1 a0^{2R}a u_2 a0^{2R}a u_3 a0^R,\qquad
 m=6R+6+\ell_1+\ell_2+\ell_3.
 \tag{6.1}
$$

A word is good if its only cyclic zero runs of length at least
$k=2R$ are the three displayed ones. Each is exactly $k$
and is bracketed by $a$. Thus goodness is exactly the condition
that each $u_j$ avoid $k$ consecutive zeros. In particular
there are no further restrictions between interiors.

The open multiplier-weight sum of all good words is exactly

$$
 [J^R A\mathcal G_{k,\ell_3}A J^k
       A\mathcal G_{k,\ell_2}A J^k
       A\mathcal G_{k,\ell_1}A J^R1](o).
 \tag{6.2}
$$

As proved by a direct Hölder sum in the frozen input, each
open weight and the corresponding actual periodic multiplier
weight differ by $1+O(\theta^R)$, uniformly over the entire
word: the open continuation $w0^\infty$ and the periodic
continuation agree for at least $m+R$ edges.

Insert (1.10) and (4.9) in (6.2), first normalizing every zero
branch. The leading scalar is
$[\nu(Ag)(A\mathfrak h)(o)]^3=c_*$; the zero factors multiply
to $\Lambda^{-6R}=\varepsilon^3$.
The avoidance factors multiply to
$e^{-\kappa_{\rm esc}\varepsilon(\ell_1+\ell_2+\ell_3)}$.
Since the omitted $6R+6$ edges contribute $O(k\varepsilon)=o(1)$
to that exponent, we obtain

$$
 Z^{\rm good}_{R,\boldsymbol\ell}
   =c_*\varepsilon^3e^{-\kappa_{\rm esc}m\varepsilon}
                        (1+o(1)).
 \tag{6.3}
$$

This and all forthcoming $o(1)$ statements are uniform when
$\min\ell_j\ge m/9$ and $N\le m\le3N/2$.
In particular positive total weights are uniformly $O(\varepsilon^3)$.

### 6.2. Restricted endpoint cylinders

Fix $K$ independently of $N$. If $w_j$ is the first $K$
edges and $v_j$ the last $K$ edges of $u_j$, its branch
factor has order

$$
 A J_{v_j}\,
       \mathcal G_{k,\ell_j-2K}\,
                         J_{w_j}A.
 \tag{6.4}
$$

This expression forbids long zero runs within the middle block.
A run crossing either boundary of that middle block could
still be counted. The total weight of such exceptional words
is $O_K(\varepsilon)$ relative to the normalized total.
Here is a direct uniform proof. For $k>2K$, the fixed end
words cannot themselves contain a run of length $k$. A
crossing run forces at least $k-K$ consecutive zero edges
inside the adjacent end of the middle block. Its operator
contains $J^{k-K}$; (1.10) bounds its norm by
$C_K\varepsilon$. The other unrestricted positive factors
can be bounded by powers of $\mathcal T$, whose norms are
uniformly bounded. There are at most $2K$ possible crossing
starts for that cell. After reinstating the three external
zero-marker factors, the total exceptional weight is therefore
$O_K(\varepsilon^4)$. The same bound holds for periodic
weights by their uniform open comparison.

Applying (4.9) to the long middle of (6.4) gives the two
endpoint factors

$$
 \nu(J_{w_j}Ag),\qquad
 (AJ_{v_j}\mathfrak h)(o),
 \tag{6.5}
$$

with avoidance multiplier
$e^{-\kappa_{\rm esc}\varepsilon(\ell_j-2K)}$.
The change from $\ell_j-2K$ to $\ell_j$ is $1+O_K(\varepsilon)$.
Inserting all three cells in (6.2), the independent leading
weight for the six prescribed cylinders is

$$
 c_*\varepsilon^3 e^{-\kappa_{\rm esc}m\varepsilon}
        \prod_{j=1}^3 P_K(w_j)Q_K(v_j)+o_K(\varepsilon^3).
 \tag{6.6}
$$

All error bounds are uniform in the allowed lengths. For a fixed
$K$ only finitely many cylinder choices occur; summing them
preserves $o_K(\varepsilon^3)$. In particular the endpoint
factorization has been proved using (4.9), not inferred from
classical mixing without an observable norm bound.

### 6.3. Passing to the full oscillatory observable

Let $F_t(\mathbf S,\mathbf U)=e^{-itQ(\mathbf S,\mathbf U)}$,
with $Q$ from (3.10), and let $t$ range over any fixed
compact interval. The scattering coordinates are bounded, so
these functions are uniformly bounded and equicontinuous.
Replace $S,U$ by their fixed-cylinder approximants
$S_K,U_K$. Equation (2.8) gives a uniform observable error
at most $C_T\lambda^{-K/2}$.

For the approximants (6.6) gives the exact limiting product
measure. Let $N\to\infty$ at this fixed $K$, and then let
$K\to\infty$. The positive total weight estimate (6.3)
controls the two observable-approximation errors. We obtain

$$
 \boxed{\begin{aligned}
 &\sum_{\substack{u_1,u_2,u_3\ {\rm good}\\ |u_j|=\ell_j}}
        \Lambda_{123}^{-1}
             e^{-itQ(\mathbf S(\mathbf u),\mathbf U(\mathbf u))}\\
 &\quad =
 c_*\varepsilon^3 e^{-\kappa_{\rm esc}m\varepsilon}
       \int e^{-itQ(\mathbf S,\mathbf U)}
                d\sigma^{\otimes3}(\mathbf S)
                d\upsilon^{\otimes3}(\mathbf U)
       +o(\varepsilon^3).
 \end{aligned}}
 \tag{6.7}
$$

The convergence is uniform in the lengths and in $t$ on the
chosen compact interval. To spell out the quantifiers, for any
error tolerance first choose a single finite $K$ so that the
two equicontinuity errors are below one third of it. Then choose
a single $N_0(K)$ so that (6.6) holds for every $N\ge N_0(K)$
and every allowed length triple. This proves the asserted
uniform $o(1)$ after division by $\varepsilon^3$.
There is no passage to a subsequence and no need for $K$ to
grow at an unverified rate.

In particular (6.7) applies to $t=t_N$. This establishes the
actual endpoint factorization needed for the signed sum.

## 7. Oscillatory trace cube, counting, and the final error

### 7.1. The full signed endpoint integral

Denote the integral in (6.7) by $\mathcal I(t)$. Integrating
the three $U$ variables first, with
$\widehat\upsilon_+(v)=\int e^{ivu}\,d\upsilon(u)$, gives

$$
 \mathcal I(t)=
  \int
   \widehat\upsilon_+(t(S_1-S_2))
   \widehat\upsilon_+(t(S_2-S_3))
   \widehat\upsilon_+(t(S_3-S_1))\,d\sigma^{\otimes3}.
 \tag{7.1}
$$

This is exactly $\operatorname{Tr}(K_t^3)$ for (T.5).
For a direct positivity check define

$$
 (V_t f)(s)=\int e^{itsu}f(u)\,d\upsilon(u),
 \quad V_t:L^2(\upsilon)\to L^2(\sigma).
 \tag{7.2}
$$

It is Hilbert--Schmidt with squared Hilbert--Schmidt norm one,
and $K_t=V_tV_t^*$. Thus $K_t$ is positive trace class with
trace one. Its kernel is bounded and the measures are finite,
so composing the kernels and applying Fubini proves (7.1) and
the trace-cube identity. Equivalently, approximation of the
bounded kernels by finite-rank simple kernels gives the same
identity by Hilbert--Schmidt convergence.

Strict positivity needs no assumption on densities. In fact

$$
 \operatorname{Tr}(K_t^3)=\|V_t^*K_t\|_{\rm HS}^2.
 \tag{7.3}
$$

If this were zero, then
$K_t^2=V_t(V_t^*K_t)=0$, and positivity, or
$\|K_tf\|^2=\langle K_t^2f,f\rangle$, would give $K_t=0$.
That contradicts trace one. Also $0<\operatorname{Tr}(K_t^3)\le1$.
Since the scattering supports are bounded, dominated convergence
in (7.1) shows continuity in $t$. Therefore its minimum on any
fixed compact interval is positive.

This positivity is a property of the complete signed integral.
No part of (7.1) has been omitted on the basis of its phase.

### 7.2. Primitive pairs and the exact normalization

Choose the integer lengths by

$$
 \frac m8\le\ell_1\le\frac m6,\qquad
 \frac m4\le\ell_2\le\frac m3,\qquad
 \ell_3=m-6R-6-\ell_1-\ell_2.
 \tag{7.4}
$$

For all large $N$, the third interval lies between
$m/2-O(\log N)$ and $5m/8-O(\log N)$; hence all lengths
are at least $m/9$, and the three ranges are disjoint.
Every pair of choices for $\ell_1,\ell_2$ is admissible.
The number of triples is exactly

$$
 \begin{split}
 L_m&=
  \left(\left\lfloor m/6\right\rfloor
       -\left\lceil m/8\right\rceil+1\right)
  \left(\left\lfloor m/3\right\rfloor
       -\left\lceil m/4\right\rceil+1\right)\\
    &=m^2/288+O(m).
 \end{split}
 \tag{7.5}
$$

For every good triple of words make the coded pair $123,132$
of the three cells $0^R a u_j a0^R$. These are precisely all
pairs in $\mathcal A^{\rm full}_{m,N}$.

The primitive-period and anchor argument is independent of
the buffer offset $R_0$; we repeat it to fix the normalization.
There are exactly three cyclic zero runs of length at least
$k$. If the cyclic word were a proper repetition, its repetition
number would divide three. The only possibility is three, and
that would force all three successive marker gaps to have equal
length. Their lengths are different by (7.4). In particular
period-two repetition cannot occur. Both codes have primitive
period $m$.

The coding is injective on nonboundary periodic orbits; the
only periodic boundary point is the origin and its itinerary
fiber has at most four elements, as proved in the frozen Berg
input. A primitive code of period $m>4$ cannot lie in that
fiber: the cyclic shift would produce $m$ distinct itineraries.
Thus the actual geometric orbits are primitive too.

The cyclic marker-gap orders short--medium--long and
short--long--medium are different, so the two orbits are
different. On the first orbit the unique zero marker immediately
preceding the short gap has a unique middle cut, $R$ edges
from either end. That cut reconstructs all three words and the
lengths. The opposite gap orientation identifies the second
orbit. Therefore no unordered pair is counted twice, either
within a length triple or across different length choices.
Changing from physical reverse time to forward code shifts
does not change cyclic equivalence.

There is consequently no extra factor of $m$, $1/m$, or
two in (7.5). Each primitive orbit has $m$ pointed terms in
the exact principal trace, and each unordered pair has its
two cross directions. Its contribution is exactly (T.3).

### 7.3. The asymptotic with uniform $o(N)$

At each fixed length triple, insert (3.12) into (T.3). Its
uniform error, bounded by the positive total weight (6.3),
is $o(m^2\varepsilon^3)$. Then (6.7), at $t=t_N$, and
(7.1) give

$$
 2m^2c_*\varepsilon^3
       e^{-\kappa_{\rm esc}m\varepsilon}
                    \operatorname{Tr}(K_{t_N}^3)
             +o(m^2\varepsilon^3).
 \tag{7.6}
$$

The error is uniform in every allowed triple. Multiplying by
$L_m=m^2/288+O(m)$ proves (T.4). The leading coefficient is
exactly $2/288=1/144$. The rounding error contributes only
$O(m^3\varepsilon^3)=O(1)=o(N)$; the other error is
$o(m^4\varepsilon^3)=o(N)$, because
$\varepsilon\asymp N^{-1}$ and $m\asymp N$.

Strict positivity and continuity of the trace cube, (T.2),
and the fixed finite bounds on $m/N$, now prove (T.6).
Finally multiply (T.4) by $w(m/N)/N^2$ and sum. Its uniform
$o(N)$ error sums to $o(1)$. The leading sum is a Riemann
sum with parameter $x_N$ in a fixed compact interval; uniform
continuity in that parameter gives (T.7).

## 8. What this calculation resolves and what remains

This calculation resolves the complete signed contribution
of the specified three-cell family at times $m\asymp N$.
It retains the exact nonlinear scattering data, the geometric
weights, the odd-dimensional phase, and the finite avoidance
probability. The steps that turn the signed sum into a positive
trace cube are the stationary quadratic action limit and the
proved endpoint factorization (6.7).

For the fixed admissible test $b_*$ in the frozen pair
calculation, $w=|\widehat b_*|^2$ is strictly positive on
$[1,3/2]$. Equations (T.6)--(T.7) give a nonvanishing positive
contribution to its normalized off-diagonal expression.
This is compatible with either sign of the complete remaining
off-diagonal sum.

More explicitly, let $O_{m,N}$ be the full signed sum over
different geometric orbits in the exact pair calculation, and
put $E^{\rm full}_{m,N}=0$ outside this interval. That calculation
gives

$$
 \Delta_{2,N}(b_*)
  =N^{-2}\sum_{m<2N}w(m/N)O_{m,N}
                         +\eta_*+O(N^{-1}),\qquad\eta_*>0.
 \tag{8.1}
$$

Writing $O^{\rm rest}=O-E^{\rm full}$, even this one pair
test still requires the unproved estimate

$$
 \boxed{\displaystyle
 N^{-2}\sum_{m<2N}w(m/N)O^{\rm rest}_{m,N}
   =-\eta_*-
      \frac{c_*}{144}x_N^3\operatorname{Tr}(K_{2\pi\chi x_N}^3)
       \int_1^{3/2}w(v)v^4e^{-\kappa_{\rm esc}x_Nv}\,dv
       +o(1).}
 \tag{8.2}
$$

No estimate of (8.2) has been assumed or proved here.
The other correlation orders in $H_{\rm diag}$ remain beyond
this calculation as well. The theorem establishes an actual
oscillatory profile of a full, explicitly anchored encounter
family; it is not a universality theorem.
