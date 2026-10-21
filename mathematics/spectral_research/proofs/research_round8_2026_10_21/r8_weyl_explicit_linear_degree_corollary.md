> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_weyl_explicit_linear_degree_corollary.md`. Embedded SHA256: `227bf6ab1905006f57f54b30372419acb7f5db08c1a4b22f022f56f1d6097e52`.
> [Thematic guide](../../topics/approximation.md).

# An explicit necessary linear degree for approximation of the original kick

21 October 2026. Round 8, Weyl branch. This corollary is independent
of the quantitative addendum presently under separate audit. It uses
only the independently audited qualitative companion
`r8_weyl_sublinear_polynomial_obstruction.md`, whose SHA256 is
`32a014694531ea01284a146334c223a22686de457970bb39e4a5fa39c109c618`.
The necessary inputs and the additional proof are specified below.

## 1. Statement

Let the original matrices be

$$
E_N=e^{i\tau NA_N},\qquad U_N=E_NM_N,\qquad \tau=10^{-80},
$$

and let $\Phi_s=(Q_s,P_s)$ be the lifted Hamiltonian flow of
the **ordinary-half corrected** symbol, with the same conventions
as in the companion source:

$$
\begin{split}
a(q,p)&=V(q)+\frac{R(q)}{100}\cos(2\pi p-\alpha_0),\\
R(q)&=r(q+1/2)=4\cos^2(7\pi q)\sin^2(\pi q),\\
V(q)&=\cos(14\pi q)+\frac{r(q)}{10}
            +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10},\\
\frac{d}{ds}\Phi_s&=X\circ\Phi_s,\qquad
X=\frac1{2\pi}(a_p,-a_q).
\end{split}
$$

Define the fixed real constant

$$
D_\tau=\max_{(q,p)\in\mathbb T^2}|Q_\tau(q,p)-q|.
\tag{1.1}
$$

The displacement in (1.1) refers to the lift with
$\Phi_0=\operatorname{id}$; it is a continuous periodic
function. In particular the maximum exists.

**Corollary.** Suppose matrices $B_N$ have cyclic bandwidth at
most $d_N$, and either

$$
\|E_N-B_N\|_{\mathrm{op}}\longrightarrow0
\quad\text{or}\quad
\frac1{\sqrt N}\|E_N-B_N\|_{\mathrm{HS}}\longrightarrow0
\tag{1.2}
$$

along all odd $N$. Then

$$
\boxed{\liminf_{N\to\infty,\ N\mathrm{\ odd}}\frac{d_N}{N}
       \ \ge\ D_\tau\ >\ \frac{\tau}{40}.}
\tag{1.3}
$$

In particular, (1.2) with $B_N=p_N(A_N)$, where the
polynomial coefficients may depend arbitrarily on $N$, implies

$$
\deg p_N>\frac{\tau N}{40}
\qquad\text{for every sufficiently large odd }N.
\tag{1.4}
$$

The same conclusion holds if the approximation in (1.2) is instead
of $U_N$ by $p_N(A_N)M_N$. More generally, the conclusion
holds along any infinite sequence of odd dimensions on which
the indicated approximation error tends to zero.

Thus the lower bound is linear with a specified positive coefficient.
It is a necessary condition for an operator or normalized
Hilbert--Schmidt approximation. It asserts no defect of
$H_{\mathrm{diag}}$.

## 2. Transition mass forces the degree bound

The qualitative companion proves the following three inputs directly
from the original Weyl law, with all odd aliases included:

1. The probability measures

   $$
   \mu_N=\frac1N\sum_{x,y\bmod N}|(E_N)_{xy}|^2
                       \delta_{(x/N,y/N)}
   $$

   converge weakly on $\mathbb T^2$ to the pushforward of
   $dq\,dp$ by $(q,p)\mapsto(q,Q_\tau(q,p))$.
2. With $\delta=Q_\tau-q$,

   $$
   |\delta|\le18\tau<1/2,
   \qquad
   \|\Phi_\tau-\operatorname{id}-\tau X\|_\infty
                    <10000\tau^2.
   \tag{2.1}
   $$

   The first inequality follows by integration of
   $\|X\|_\infty\le18$; the second follows from
   $\|DX\|_\infty<1100$ and
   $\int_0^\tau1100\cdot18s\,ds=9900\tau^2$.
3. Writing

   $$
   m_{N,d}=\frac1N
      \sum_{\operatorname{dist}_N(x,y)\le d}|(E_N)_{xy}|^2,
   $$

   orthogonal projection onto that cyclic band gives exactly

   $$
   \inf_{B:\operatorname{bandwidth}(B)\le d}
        \frac1{\sqrt N}\|E_N-B\|_{\mathrm{HS}}
          =\sqrt{1-m_{N,d}}.
   \tag{2.2}
   $$

All these inputs are proved, respectively, in Sections 5--7 of the
companion source. The proof of (1.3) now needs a fixed nonzero tube
radius rather than the shrinking radius used there.

For $0\le a<D_\tau$, define the closed tube

$$
\mathcal D_a=\{(q,s):\operatorname{dist}_{\mathbb T}(q,s)\le a\}.
$$

Since $D_\tau<1/2$, the limiting measure satisfies

$$
\mu(\mathcal D_a)=\operatorname{Leb}\{|\delta|\le a\}<1.
\tag{2.3}
$$

For the strict inequality, the continuous function $|\delta|$
attains a value larger than $a$. It therefore exceeds $a$
on a nonempty open subset of the torus; that subset has positive
Lebesgue measure. No assertion about the boundary of the tube is
needed here.

If $d_N/N\le a$ along an infinite subsequence, then

$$
m_{N,d_N}\le\mu_N(\mathcal D_a),
\qquad
\limsup m_{N,d_N}\le\mu(\mathcal D_a)<1
\tag{2.4}
$$

on that subsequence. The second assertion is the closed-set
inequality for weak convergence. Equations (2.2) and (2.4) give
a strictly positive lower bound on the normalized Hilbert--Schmidt
error there. Since
$\|C\|_{\mathrm{HS}}/\sqrt N\le\|C\|_{\mathrm{op}}$,
they also give that lower bound for the operator-norm error.

Thus (1.2) precludes such a subsequence for every
$a<D_\tau$, which is exactly the first inequality in (1.3).

## 3. A point with displacement greater than $\tau/40$

Choose $q_*=3/7$ and choose $p_*\in\mathbb T$ satisfying
$\sin(2\pi p_*-\alpha_0)=1$. At this point,

$$
R(q_*)=4\sin^2(3\pi/7)>3.
\tag{3.1}
$$

Indeed $\sin(3\pi/7)=\cos(\pi/14)>\cos(\pi/6)=\sqrt3/2$.
The first component of the exact vector field is

$$
X_q(q,p)=-\frac{R(q)}{100}\sin(2\pi p-\alpha_0).
$$

Using (2.1) at $(q_*,p_*)$ therefore gives

$$
\begin{split}
D_\tau&\ge|\delta(q_*,p_*)|\\
&\ge\tau\frac{R(q_*)}{100}-10000\tau^2\\
&>\tau\left(\frac3{100}-10000\tau\right)
 >\frac{\tau}{40}.
\end{split}
\tag{3.2}
$$

For the last strict inequality it suffices that
$10000\tau<1/200$, which is satisfied by the fixed exact
$\tau=10^{-80}$. This proves the second inequality in (1.3).

Finally, every degree-$d$ polynomial in the original matrix
$A_N$ has cyclic bandwidth at most $d$: its Fourier symbol
uses only shifts $l=0,\pm1$, and each multiplication changes
the cyclic position by at most one additional step. This argument
includes every wrap on the odd cyclic lattice. Consequently (1.3)
applies to $p_N(A_N)$, and its strict gap above $\tau/40$
implies (1.4). Right multiplication by the unitary $M_N$
preserves both stated matrix norms. This completes the proof.

