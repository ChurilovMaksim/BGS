# Polynomial-step limits for the original Gaussian coboundary chain

**Claim ID: BGS-FLOW-011.** Project derivation, 4 October 2026.
Base: `a25c0d2573b5232a676cfccf1dc79da8e4cd2956`.
The arguments and their review boundary are recorded in
[`record/polynomial_coboundary_review_20261004.md`](../../archive/record/polynomial_coboundary_review_20261004.md).
No external priority, deterministic BGS theorem, or analytic Lean certificate
is asserted.

## 1. Exact target and two levels of improvement

Keep the original uncentered chain, with fresh independent normalized GUE:

$$
U_{j+1}^{\varepsilon}=
\exp\{i\varepsilon(G_j-U_j^{\varepsilon}G_jU_j^{\varepsilon *})\}
U_j^{\varepsilon},\qquad U_0^{\varepsilon}=C_N,
\quad C_N=\operatorname{diag}(e^{2\pi i l/N})_{l=0}^{N-1}.
\tag{P1}
$$

Here $N\ge3$ is odd, $\mathbb E(G_j)_{ab}(G_j)_{cd}
=N^{-1}\delta_{ad}\delta_{bc}$, $h=\varepsilon^4/2$, and
$n=\lfloor t/h\rfloor$. The observation origin is uniform on the circle.
For a nonnegative $f\in C_c^\infty(\mathbb R)$, write $\Phi_{N,f}$ for
the unfolded local Laplace functional, exactly as in FLOW-004/010.

**Elementary corollary of the existing FLOW-010 bound.** If
$L_N\to\infty$, $L_N=o(\log N)$, $t_N=L_N/N$ and
$\varepsilon_N=N^{-a}$ for any fixed $a>20$, then (P1) already has the
joint Sine$_2$ weak local limit. Indeed its previous last error is
$N^{20-a}\exp(C L_N)=N^{20-a+o(1)}$. Thus the earlier statement that
FLOW-010 supplies *no polynomial-step regime* was too strong. No new
semigroup estimate is needed for this corollary. This corrects current
status without rewriting the dated 30 September audit.

The stronger result below permits the original $t=N^{-2/3}$ rate, by
retaining the normalized matrix structure in the derivative estimates.

**Theorem.** There are absolute $C,\varepsilon_0>0$, and $C_f$ depending
on $f$, such that for $1/N\le t\le1/12$ and
$0<\varepsilon\le\varepsilon_0$,

$$
\left|\mathbb E\Phi_{N,f}(U_n^{\varepsilon})
-\Phi_{\mathrm{Sine}_2}(f)\right|
\le C_f\left[\sqrt t+\frac1{Nt}+\frac1{N^2}
+N^4\varepsilon+tN^9\varepsilon+tN^{10}\varepsilon^2\right].
\tag{P2}
$$

Consequently the explicit polynomial choice

$$
t_N=N^{-2/3},\qquad \varepsilon_N=N^{-26/3},\qquad
n_N=2N^{34}
\tag{P3}
$$

has discrepancy $O_f(N^{-1/3})$. The identity $n_Nh_N=t_N$ is exact;
there is no rounding error in (P3). The exponent 34 is a conservative
proof bound, not a practical algorithm or a complexity optimum.
Nonnegative $C_c^1$ tests have the weak limit by $L^1$ approximation.

## 2. Inputs retained from the previous proofs

This continuation uses the original FLOW-010 fast-coordinate, local
weak-generator and exit estimates, and the FLOW-009 projected diffusion.
It does not replace (P1) with centered or whitened random steps.
For the exact Möbius projection $\Pi$ and a smooth rotation-invariant
class function $F$ on its centered slice, the retained bounds are

$$
\rho=\varepsilon/N+\varepsilon^4,\qquad
\mathbb E[|m_1(U_j)|;j<\sigma]\le C\rho,
\tag{P4}
$$

$$
\mathbb E[\widetilde F(U_{j+1})-\widetilde F(U_j)\mid U_j]
=h\overline L F(\Pi U_j)+R_j,\qquad
|R_j|\le ChN^4\|F\|_6(|m_1(U_j)|+\varepsilon^2),
\tag{P5}
$$

$$
\mathbb P(\sigma\le n)
\le C[t/N^2+(t+1)N^4\varepsilon].
\tag{P6}
$$

They are FLOW-010 (6), (8), and (9), including the large-jump control.
The norm is the maximum of fixed-order multilinear Hilbert--Schmidt
derivative norms, including order zero; it never sums over all direction
tuples. The new estimates concern (a) the backward semigroup and
(b) the microscopic test norm in these same inequalities.

## 3. Dimension-uniform derivatives of the projected coefficients

Let $\mathcal H_0$ be the **fixed** real traceless Hermitian space with
scalar product $\operatorname{Tr}(TS)$; let $E_a$ be an orthonormal basis.
Use the exact covariance $\mathcal C_U$ in FLOW-003 (4), and put
$B_U=N\mathcal C_U|_{\mathcal H_0}$, $K_a=\mathcal C_U^{1/2}E_a$.
On $|m_2|\le3/5$, the spectrum of $B_U$ lies in $[2/5,13/5]$.

There are two distinct Hilbert--Schmidt norms here: the matrix norm and
the Hilbert--Schmidt norm of a linear operator on $\mathcal H_0$.
For every fixed $r\ge1$ and matrix directions $H_1,\ldots,H_r$ of
matrix Hilbert--Schmidt norm one,

$$
\|D^rB_U[H_1,\ldots,H_r]\|_{\rm op(\mathcal H_0)}\le C_r,
\qquad
\|D^rB_U[H_1,\ldots,H_r]\|_{\rm HS(\mathcal H_0)}\le C_r\sqrt N.
\tag{P7}
$$

Here and below derivatives can be taken in the local polar extension at
a unitary point. Its fixed-order derivatives have dimension-uniform
matrix Hilbert--Schmidt bounds, by the inverse-square-root power series
on a fixed operator-norm neighborhood of $I$.

To verify (P7) directly, $B_U$ is the identity plus
left/right matrix multiplication and rank-two trace terms in FLOW-003 (4).
For $T\mapsto LTR$, its operator Hilbert--Schmidt norm on the full
complex matrix space is $\|L\|_{\rm HS}\|R\|_{\rm HS}$.
Restriction to the real Hermitian subspace changes this estimate only
by an absolute factor. An undifferentiated unitary has norm $\sqrt N$;
a differentiated power of $U$ has norm at most $C_r$ times the product
of the direction norms. A derivative of a fixed normalized trace costs
at most $C_r/\sqrt N$. If both multiplication factors remain unitary,
the derivative of $m_2$ therefore pays $N/\sqrt N=\sqrt N$.
If one factor is differentiated, the cost is at most $\sqrt N$ directly.
The differentiated rank terms have rank bounded in terms of $r$ and
are no larger. This proves both assertions, with all directions included.

The square-root resolvent formula on the stated spectral interval gives

$$
\|D^r\mathcal C_U^{1/2}[H_1,\ldots,H_r]\|_{\rm HS(\mathcal H_0)}
\le C_r,\qquad r\ge1,
\quad \|\mathcal C_U^{1/2}\|_{\rm op}\le C/\sqrt N.
\tag{P8}
$$

In each differentiated resolvent product put one differentiated $B_U$
factor in the operator Hilbert--Schmidt norm, all others in operator
norm, and use (P7). The exterior $N^{-1/2}$ cancels $\sqrt N$.
This is the normalization lost in the earlier coarse estimate.

Use the exact FLOW-009 (9)--(10) coefficients:

$$
q=m_2,\quad d=1-|q|^2,\quad
f_a=\frac iN\operatorname{Tr}(K_aU),\quad
w_a=(f_a+q\bar f_a)/d,\quad
J_a=i(w_aU^*-\bar w_aU),\quad L_a=K_a+J_a.
\tag{P9}
$$

The map $K\mapsto J$ has rank at most two and bounded operator norm.
Its positive-order derivatives have operator Hilbert--Schmidt norm
$O_r(N^{-1/2})$: each rank term has the form
$N^{-1}V\otimes W$, with $\|V\|_{\rm HS},\|W\|_{\rm HS}=O(\sqrt N)$,
and differentiation replaces one factor by an $O_r(1)$ factor or
differentiates a normalized trace. Combining this with (P8), and with
$\|T\mapsto TH\|_{\rm HS}=\sqrt N\|H\|_{\rm HS}$, proves

$$
\left(\sum_a\|D^r(iL_aU)[H_1,\ldots,H_r]\|_{\rm HS}^2\right)^{1/2}
\le C_r,\qquad r\ge1.
\tag{P10}
$$

For clarity the contracted drift also has a dimension-uniform derivative
bound; a generic $O(N)$ contraction estimate is unnecessary. Directly
from FLOW-003 (1), for **every** unitary $U$,

$$
Q_K:=\sum_aK_a^2
=I-\tfrac12(q\bar m_1U^*+\bar q m_1U).
\tag{P11}
$$

Let $T=\sum_a\bar w_aK_a$, $v=\sum_a|w_a|^2$,
$\zeta=\sum_aw_a^2$. Because $T$ commutes with $U$,

$$
Q_L:=\sum_aL_a^2
=Q_K+2i(T^*U^*-TU)+2vI-\zeta U^{*2}-\bar\zeta U^2.
\tag{P12}
$$

The exact covariance formula expresses $T$ as $N^{-2}$ times a bounded
rational combination of fixed powers of $U$ and normalized traces,
with denominators powers of $d$. The same holds for $v,\zeta,\kappa,b$
and $A_\Pi$ in FLOW-009 (10). For example
$T=i\mathcal C_U(\bar qU-U^*)/(Nd)$ and
$\kappa=(2i/N)\operatorname{Tr}(TU^2)$.
The contractions $\sum f_a^2$ and $\sum|f_a|^2$ are traces against
$\mathcal C_U$, divided by $N^2$, so have the same rational form.
Thus every positive-order derivative of
$-Q_LU/2+iA_\Pi U$ has matrix Hilbert--Schmidt norm at most $C_r$.
Normalized-trace differentiation pays $N^{-1/2}$ before multiplying
an undifferentiated matrix of norm $\sqrt N$.

Multiply the noise by a smooth $\chi(|q|^2)$, equal to one on
$|q|\le9/20$ and zero on $|q|\ge3/5$, and the drift by $\chi^2$.
Every positive-order derivative of $\chi$ is $O_r(N^{-1/2})$.
The undifferentiated noise and drift have sizes $O(\sqrt N)$;
their cutoff terms therefore also satisfy (P10) and the drift bound.
This defines a smooth equation on the entire unitary group, by zero
extension through the cutoff, agreeing with the projected diffusion on
the centered slice. Its coefficients remain conjugation and rotation
equivariant. The formula for $A_\Pi$ is Hermitian on the full group, and
$Q_L$ is the covariance contraction, so the equation preserves unitarity.
On the centered slice the FLOW-009 trace constraint is unchanged.

If an ambient extension is used to differentiate the flow, take it equal
to the polar formula near the unitary group. A cutoff transverse to that
group is locally constant there. Bounds are needed for derivatives at
the unitary base trajectories, where all derivatives of this cutoff
vanish; no dimension-uniform bound outside that neighborhood is asserted.

## 4. Backward stability without an exponential in dimension

For the preceding localized diffusion write $S_s$ for its semigroup.
Differentiating its stochastic flow through six fixed initial directions,
the linear variation coefficients have bounds $C$ for the drift and
$C$ for the noise-coordinate Hilbert--Schmidt norm, by (P10)--(P12).
Itô's formula for even moments gives $e^{C_ps}$, with no factor $N$.
At order $r\ge2$, the inhomogeneous terms are products of lower variations
and bounded coefficient derivatives. Hölder, induction in $r$, and the
required higher even moments give, for $0\le s\le1$,

$$
\|S_sF\|_6\le C e^{Cs}\|F\|_6.
\tag{P13}
$$

This concerns multilinear derivative norms at unitary base points and
their polar extensions. It does not assert a spectral gap or elliptic
regularity estimate uniform on an unconstrained ambient matrix space.
The retained generator bound $\|\overline LF\|_k\le CN\|F\|_{k+2}$
is sufficient for the time increments.

Repeat FLOW-010's stopped backward telescoping, using (P4)--(P6) and
(P13) instead of its (11). For $0\le F\le1$ this gives

$$
|\mathbb EF(\Pi U_n)-S_tF(C_N)|
\le C\left[t/N^2+N^4\varepsilon
+tN^4\|F\|_6(\varepsilon/N+\varepsilon^2)\right].
\tag{P14}
$$

In the weak-generator sum retain
$\rho+\varepsilon^2\le\varepsilon/N+2\varepsilon^2$ rather than
replacing the fast-coordinate contribution by $O(\varepsilon)$.
The one-step time correction is $O(h^2N^2\|F\|_6)$, and its total
is $O(thN^2\|F\|_6)$. Relative to the quadratic part of the last
term its ratio is $\varepsilon^2/(2N^2)$.
The final interval is $O(hN\|F\|_6)$, with ratio
$\varepsilon^2/(2tN^3)\le\varepsilon^2/(2N^2)$.
Both are absorbed for $\varepsilon\le1$ and $t\ge1/N$.
The exit contribution is bounded using $0\le F,S_sF\le1$, rather than
by differentiating a killed boundary semigroup.

## 5. Positivity removes six unnecessary powers from the test norm

For a fixed origin $\alpha$, let $f_{N,\alpha}$ be the smooth circle
periodization of $f(N(\theta-\alpha)/(2\pi))$, and
$A(U)=\operatorname{Tr}f_{N,\alpha}(U)\ge0$.
Its Fourier coefficients satisfy
$\sum_k|k|^j|a_k|\le C_{f,j}N^j$, $j\ge1$.
The elementary inequality

$$
|f'(x)|^2\le2\|f''\|_\infty f(x),\qquad f\ge0,
\tag{P15}
$$

follows by using the quadratic Taylor upper bound at
$x-f'(x)/\|f''\|_\infty$; the zero-second-derivative case is constant.
For sufficiently large $N$ the periodized supports are disjoint, so the
same estimate, with a factor $C_fN^2$, holds on the circle.
For a unit Hilbert--Schmidt Hermitian tangent direction $H$,

$$
|DA(U)[iHU]|=|\operatorname{Tr}(f_{N,\alpha}'(U)H)|
\le C_fN\sqrt{A(U)}.
\tag{P16}
$$

For $j\ge2$, differentiate the Fourier series in the local exponential
chart. Each differentiated trace has $j$ direction factors, separated
by unitary factors, and at most $C_j|k|^j$ terms. Schatten Hölder puts
two direction factors in the matrix Hilbert--Schmidt norm and the
others in operator norm, so

$$
|D^jA(U)[H_1,\ldots,H_j]|
\le C_{f,j}N^j\prod_i\|H_i\|_{\rm HS},\qquad j\ge2.
\tag{P17}
$$

The same bound in a polar extension allows an additional
$C_jN\sqrt A$ term from its nonlinear change of chart; all derivatives
are thus bounded by $C_{f,j}N^j(1+\sqrt A)$.
The partition formula for derivatives of $e^{-A}$ then bounds every
order-$j$ term by $C_{f,j}N^j e^{-A}(1+\sqrt A)^j$.
Its last factor is bounded uniformly for $A\ge0$.
Integrating over $\alpha$, and composing with the dimension-uniform
projection/chart maps, gives

$$
\|\Phi_{N,f}\|_6\le C_fN^6.
\tag{P18}
$$

This argument includes repeated eigenvalues and arbitrarily large local
occupancy. Positivity is essential for the first derivative; a signed
test cannot be substituted in this estimate without a separate bound.

## 6. Completion, applications, and remaining boundaries

Insert (P18) into (P14). Terminal centering costs $C_f\rho$ by FLOW-009
(5), absorbed in $N^4\varepsilon$. FLOW-009 (15)--(16) and the credited
odd-clock Dyson kernel theorem give the remaining
$\sqrt t+(Nt)^{-1}+N^{-2}$ terms, including the localized exit.
This proves (P2). In (P3),
$tN^9\varepsilon=N^{-1/3}$,
$tN^{10}\varepsilon^2=N^{-8}$ and
$N^4\varepsilon=N^{-14/3}$, proving the stated rate.
Uniform-origin averaging has exactly unit mean intensity, so
$|\Phi_{N,f}-\Phi_{N,g}|\le\|f-g\|_1$ for every spectrum.
Smooth nonnegative approximation extends the convergence to $C_c^1$.

The result replaces an exponential number of random steps by an explicit
polynomial bound, and preserves the previous smooth-test convergence rate.
It is a weak local-process theorem. Unbounded factorial correlations need
their own uniform integrability, and large practical simulation counts are
not part of this claim.

**Bounded counting applications.** Let $X_N(I)$ be the number of unfolded
points in a fixed bounded interval $I$, at the parameters (P3). Then

$$
\mathbb E z^{X_N(I)}
\longrightarrow\det\!\left(I-(1-z)K_I\right),\qquad 0\le z\le1,
\quad K_I(u,v)=\frac{\sin\pi(u-v)}{\pi(u-v)}.
\tag{P19}
$$

For $z>0$, approximate $(-\log z)\mathbf1_I$ in $L^1$ by smooth
nonnegative tests and use unit mean intensity to bound the approximation
uniformly in $N$. The Sine$_2$ determinantal Laplace identity gives the
right side. For $z=0$, use
$0\le\mathbb E z^{X_N(I)}-\mathbb P(X_N(I)=0)\le z$ for $0<z<1$
and then continuity of the Fredholm determinant.
In particular the hole probabilities converge to $\det(I-K_I)$.
This corollary has no asserted rate for interval indicators and does not
establish uniform integrability of higher factorial moments.

The initial clock has rigid spacings and (P1) changes them to Sine$_2$.
No deterministic noise-removal implication follows. For the actual frozen
start, [FLOW-014](circular_dyson_actual_start.md) separately supplies the
Dyson-reference Laplace limit at $t_N=8g_N$,
$g_N=4\log J_N/J_N$, $J_N=\lfloor c\log N\rfloor$, and a weak local
limit for the original uncentered chain on its stated polynomial schedule.
[FLOW-017](coboundary_all_order_limit.md) supplies all fixed factorial
orders and one-chain origin averages in $L^2$ on a superpolynomial schedule
at that time; it does not strengthen the polynomial schedule (P3) here.
Relaxation of the actual start at the faster clock time $N^{-2/3}$,
deterministic noise removal and its Heisenberg-scale signed joint traces
remain open, as do **BGS-TRACE-005 and BGS-BGS-001**. A statement for every
classically chaotic quantum system is not obtained here.
