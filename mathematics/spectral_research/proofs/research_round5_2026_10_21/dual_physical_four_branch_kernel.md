> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round5_2026_10_21/dual_physical_four_branch_kernel.md`. Embedded SHA256: `0b8e8a685c619ba95fab9f9eac65f5328ee81123780ae94515e17f4e8e70235c`.
> [Thematic guide](../../topics/classical_trace.md).

# Exact four-branch physical kernel with a uniform WKB remainder

Research round 5, 21 October 2026. Owner: Weyl-dual branch.
Base checkpoint: round-4 package SHA256
e74f697134ea0d7d0ad5776c118ac267cf4999ae029e5b1f0252de364596fa4a.

## 1. The statement for the original matrices

All matrices, including their modular halves, are those in the original
question. Let
$$
 h=(2\pi N)^{-1},\qquad t=\tau/(2\pi),\qquad
 E_N(s)=e^{isA_N/h},\quad 0\le s\le t_0=10^{-10}.
$$
Then $U_N=E_N(t)M_N$. No $N$-dependent kick is introduced.

For each odd $N$, let $\nu=\nu_N\in\{1,3,5,7\}$ be the solution of
$\nu N\equiv-1\pmod8$. Put
$$
 z_\nu=e^{-3\pi i\nu/4},\qquad
 (g_0,g_1,g_2,g_3)=\tfrac12(z_\nu,1,-z_\nu,1),
$$
where the subscripts of $g$ are read modulo four, and set
$$
 d_{m,N}(y)=e^{-3\pi i\nu y^2/4}g_{m-\nu y}.
 \tag{1.1}
$$
Thus $|d_{m,N}(y)|=1/2$.

There are real analytic functions $\Phi_m(s,q,r)$ and positive real
analytic functions $B_m(s,q,r)$, for all integers $m$, which do not
depend on $N$, such that
$$
 \Phi_m(0,q,r)=\Theta_m(q,r)
 =-\frac{3q^2-2qr+3r^2}{8}+\frac{mq}{4},\qquad B_m(0,q,r)=1.
 \tag{1.2}
$$
Their derivatives of each fixed order are uniformly bounded on compact
coordinate domains for $0\le s\le t_0$, $m=0,1,2,3$.
Define
$$
 V_N(s)_{xy}
 =\frac1{\sqrt N}\sum_{m=0}^3 d_{m,N}(y)
 B_m(s,x/N,y/N)e^{i\Phi_m(s,x/N,y/N)/h}.
 \tag{1.3}
$$
The following bounds hold with a finite constant independent of $N,s,y$:
$$
 \boxed{\|(E_N(s)M_N-V_N(s))e_y\|_2\le Csh,\qquad
 \|E_N(s)M_N-V_N(s)\|_{\rm HS}\le Cs h\sqrt N.}
 \tag{1.4}
$$
In particular, at the original $t$, the maximum entry of $U_N$ is at
most $3/\sqrt N$ for every sufficiently large odd $N$.

Writing $S_m=\Phi_m-\Theta_m$, the functions $S_m,B_m$ are periodic
with period four in both $q,r$, and
$$
 \begin{split}
 |\partial_qS_m(s)|&\le350s,\qquad
 |\partial_rS_m(s)|\le50s,\qquad |S_m(s)|\le2s,\\
 \|S_m(s)-s a(q,(r-3q+m)/4)\|_\infty&\le35000s^2,\\
 |B_m(s)^2-1|&\le40000s.
 \end{split}
 \tag{1.5}
$$
The supremum bounds hold on the full real parameter plane and all integer
$m$. The exact symbol $a$ is given below.

For the physical matrices
$$
 P(U)_{xy}=|U_{xy}|^2,\qquad
 Q(U)_{xy}=U_{xy}\overline{U_{yx}},
$$
the approximation also satisfies
$$
 \boxed{\|P(U_N)-P(V_N(t))\|_{\rm HS}
       +\|Q(U_N)-Q(V_N(t))\|_{\rm HS}\le C/N.}
 \tag{1.6}
$$
These results provide the physical kernel input for oscillatory matrix
estimates. They do not assert pointwise convergence of $N|U_{xy}|^2$
to one, or evaluate the full spectral form factor.

## 2. Exact finite-shift formula and elementary bounds

The ordinary-half symbol corresponding to the original modular-half
quantization is
$$
 \begin{split}
 a(q,p)={}&\cos(14\pi q)+r(q)/10+r(q)\sin(2\pi q)/100-1/10\\
 &+r(q+1/2)\cos(2\pi p-\alpha_0)/100.
 \end{split}
 \tag{2.1}
$$
Indeed, if $c_{k,l}$ are the original Fourier coefficients, the
coefficients of $a$ are $a_{k,l}=(-1)^{kl}c_{k,l}$. Only the rows
$l=1,-1$ change, and multiplication by $(-1)^k$ translates their
$q$-coefficient by $1/2$. For every periodic sequence $\psi$ on
$\mathbb Z$, the original matrix acts exactly as
$$
 (A_N\psi)(x)=\sum_{k,l}a_{k,l}
 e^{2\pi i k(x/N+l/(2N))}\psi(x+l).
 \tag{2.2}
$$
To check this, substitute
$e_N(k2^{-1}l)=(-1)^{kl}e^{\pi ikl/N}$ in the original definition of
$T_N(l,k)$. This also checks (2.2) at a wrapped shift.

The finite support has $|k|+|l|\le9$, and
$\sum|a_{k,l}|<2$. For example, the original expansion has main norm
$9/10$, the three remaining pure cosine terms have total norm $1/5$,
and each of the last two products has norm at most $4/100$.
Multiplication of coefficients by signs preserves the norm.
Consequently, on the complex tube
$\max(|\operatorname{Im}q|,|\operatorname{Im}p|)\le2\cdot10^{-3}$,
$$
 |a_q|,|a_p|<200,\qquad
 \|D(-a_p,a_q)\|_{\infty\to\infty}<10000.
 \tag{2.3}
$$
The respective sufficient bounds are
$$
 2(2\pi)9e^{2\pi(2\cdot10^{-3})9}<200,\qquad
 2(2\pi)^2 9^2e^{2\pi(2\cdot10^{-3})9}<10000.
$$
Every derivative of fixed order has a finite bound on any smaller tube.
On the real torus, $|a|<2$.

## 3. Exact initial Gauss decomposition

Since $8^{-1}=(1+\nu N)/8$ for the appropriate integer representative,
the initial kernel splits into its ordinary quadratic phase and a root
of unity. In the $x$-dependent root of unity, the function
$$
 \gamma_\nu(x)=e^{-3\pi i\nu x^2/4}
$$
has period four. Its four values are
$(1,z_\nu,-1,z_\nu)$, whose discrete Fourier coefficients are exactly
$(g_0,g_1,g_2,g_3)$. Therefore
$$
 \gamma_\nu(x)=\sum_{j=0}^3g_j e^{2\pi i jx/4}.
$$
Multiplying this by the remaining root-of-unity factors gives
$$
 M_{xy}
 =N^{-1/2}e^{-2\pi i(3x^2-2xy+3y^2)/(8N)}
 e^{-3\pi i\nu y^2/4}
 \sum_{j=0}^3 g_j e^{2\pi i(j+\nu y)x/4}.
$$
Reindexing $m=j+\nu y\pmod4$ proves
$M_N=V_N(0)$ exactly. This calculation uses all four branches and is
valid for each odd $N$, including each class modulo eight.

## 4. Construction of the phase and amplitude

Let $(Q_s,P_s)$ be the Hamiltonian flow
$$
 \dot Q_s=-a_p(Q_s,P_s),\qquad
 \dot P_s=a_q(Q_s,P_s)
 \tag{4.1}
$$
with initial data
$$
 Q_0=u,\qquad P_0=p_0(u,r,m)=(-3u+r+m)/4.
$$
The vector field is globally bounded on the real plane and analytic in a
fixed complex tube. Picard iteration gives the flow throughout
$[0,t_0]$. From (2.3),
$$
 |Q_s-u|\le200s,\quad |P_s-p_0(u,r,m)|\le200s,\quad
 \|D(Q_s,P_s)-I\|_{\infty\to\infty}\le2\cdot10^4s,
 \tag{4.2}
$$
where the last derivative is with respect to the initial phase-space
coordinates. Along the initial graph its tangent is $(1,-3/4)$, so
$$
 J_s(u,r,m):=\partial_uQ_s(u,r,m),\qquad
 |J_s-1|\le2\cdot10^4s<1/2.
 \tag{4.3}
$$
Thus $u\mapsto Q_s(u,r,m)$ is an increasing global bijection of the
real line. Its inverse is analytic. For explicit analytic justification,
write $Q_s(u)=u+\eta_s(u)$; on a fixed smaller complex tube the equation
$u=q-\eta_s(u)$ is a contraction, since
$|\partial_u\eta_s|\le2\cdot10^4t_0<1$, while its displacement is at most
$200t_0$. The inverse stays inside the larger tube used in (2.3).
This gives uniform complex neighborhoods in $q,r$; differentiating
there gives the stated bounds at every fixed derivative order.

With $q=Q_s(u,r,m)$, define
$$
 \Phi_m(s,q,r)
 =\Theta_m(u,r)+\int_0^s
       [P_v\dot Q_v+a(Q_v,P_v)]\,dv,
 \quad
 B_m(s,q,r)=J_s(u,r,m)^{-1/2}.
 \tag{4.4}
$$
The positive square root is used on the real plane. The characteristic
action gives
$$
 \Phi_{m,q}=P_s,\qquad
 \Phi_{m,s}=a(q,\Phi_{m,q}),\qquad
 \Phi_{m,r}=u/4-3r/4.
 \tag{4.5}
$$
For completeness, variation of the action in (4.4) has interior part
$$
 \int(\dot Q_v\,dP_v+P_v\,d\dot Q_v
              +a_q\,dQ_v+a_p\,dP_v)\,dv.
$$
Integrating $P_v\,d\dot Q_v$ by parts and using (4.1) cancels the
interior terms. The initial boundary term cancels the $u$-variation
of $\Theta_m$. The final boundary is $P_s\,dq$; an $r$-variation
at fixed endpoint leaves $\partial_r\Theta_m(u,r)$, proving the first
and third equations in (4.5). A time variation at fixed endpoint leaves
$-H=a$, proving the second.

The Jacobian equation in (4.3) gives the exact transport equation
$$
 B_{m,s}=a_p(q,\Phi_{m,q})B_{m,q}
 +\frac12\bigl[a_{pq}(q,\Phi_{m,q})
       +a_{pp}(q,\Phi_{m,q})\Phi_{m,qq}\bigr]B_m.
 \tag{4.6}
$$
Indeed, along the characteristic, the derivative of $J_s$ is
$-[a_{pq}+a_{pp}\Phi_{qq}]J_s$. Taking its negative square root and
using $\dot Q_s=-a_p$ proves (4.6).

Now $|u-q|\le200s$, so (4.2) implies
$$
 |\Phi_{m,q}-p_0(q,r,m)|\le200s+\tfrac34(200s)=350s.
$$
The third equation in (4.5) gives $|S_{m,r}|\le50s$.
Integrating $\Phi_s=a(q,\Phi_q)$ at a fixed endpoint gives
$|S_m|\le2s$, and
$$
 |S_m(s)-s a(q,p_0(q,r,m))|
 \le\int_0^s 200(350v)\,dv=35000s^2.
$$
Finally (4.3) gives
$$
 |B_m^2-1|=|J_s^{-1}-1|
 \le\frac{20000s}{1-20000s}\le40000s.
$$
These are all the quantitative bounds in (1.5).

## 5. Periodic gluing of the branches

The following identities follow from uniqueness of the characteristic
solution and the periodicity of $a$ in each variable:
$$
 \begin{split}
 \Phi_{m+4}(s,q,r)&=\Phi_m(s,q,r)+q,\\
 \Phi_m(s,q+1,r)&=\Phi_{m-3}(s,q,r)+m/4-3/8+r/4,\\
 \Phi_m(s,q+4,r)&=\Phi_m(s,q,r)-3q-6+r+m,\\
 \Phi_m(s,q,r+4)&=\Phi_m(s,q,r)+q-3r-6.
 \end{split}
 \tag{5.1}
$$
For example adding $q$ shifts the momentum by one and therefore leaves
the Hamilton--Jacobi equation unchanged; it changes the initial phase
precisely from $\Theta_m$ to $\Theta_{m+4}$. Translating $q$ by one
changes the initial phase exactly as in the second identity, while the
symbol is periodic in $q$. The last two identities follow either
directly in the same way or by four repetitions of the first two.
The amplitudes obey the corresponding identities without additive terms.
In particular $S_m=\Phi_m-\Theta_m$ and $B_m$ have period four in
both real coordinates.

There is also a necessary root-of-unity identity:
$$
 g_{s-3}
 =e^{2\pi i(Ns/4-3N/8)}g_s,\qquad s\in\mathbb Z.
 \tag{5.2}
$$
It follows by substituting the four explicit values of $g$ and using
$N\equiv-\nu\pmod8$; the latter follows from
$\nu N\equiv-1\pmod8$ and $\nu^2\equiv1\pmod8$.
Since $(N\nu+1)y/4$ is an integer, (5.2) implies
$$
 d_{m,N}(y)
 e^{2\pi iN(m/4-3/8+(y/N)/4)}
 =d_{m-3,N}(y).
 \tag{5.3}
$$
Apply the second identity in (5.1) when $x$ is changed to $x+N$,
and then apply (5.3). Reindexing $m\mapsto m-3$ preserves the four
branches. When an index is reduced modulo four, the first identity
in (5.1) adds an integer multiple of $q$; at $q=x/N$, its
exponential is $e^{2\pi i jx}=1$. Consequently
$$
 V_N(s)_{x+N,y}=V_N(s)_{xy}
 \quad\text{for every integer }x.
 \tag{5.4}
$$
Thus the approximate column is an exactly periodic sequence for every
time in the construction. The finite-shift calculation may be performed
with its smooth branch extensions even at a wrapped matrix entry.
No unproved boundary condition for an individual branch is being imposed.

## 6. Direct finite-shift residual and the norm error

Fix one branch and suppress its parameters. Put $\psi(q)=B(q)e^{i\Phi(q)/h}$.
Since $l$ ranges over a fixed finite set, Taylor's formula with bounded
derivatives gives, uniformly in the sampled coordinates,
$$
 \begin{split}
 &\sum_{k,l}a_{k,l}e^{2\pi ik(q+\pi hl)}
 B(q+2\pi hl)e^{i\Phi(q+2\pi hl)/h}\\
 &\quad=e^{i\Phi(q)/h}\left\{
 a(q,\Phi_q)B
 -ih\left[
   a_p(q,\Phi_q)B_q
  +\tfrac12(a_{pq}(q,\Phi_q)+a_{pp}(q,\Phi_q)\Phi_{qq})B
       \right]+O(h^2)\right\}.
 \end{split}
 \tag{6.1}
$$
Here the remainder is bounded in absolute value by a fixed constant
times $h^2$. To check every first-order coefficient, expand
$$
 e^{2\pi ik(q+\pi hl)}
 =e^{2\pi ikq}(1+2\pi^2ihkl+O(h^2)),
$$
$$
 B(q+2\pi hl)=B+2\pi hlB_q+O(h^2),
$$
and
$$
 e^{i(\Phi(q+2\pi hl)-\Phi(q))/h}
 =e^{2\pi il\Phi_q}
       (1+2\pi^2ihl^2\Phi_{qq}+O(h^2)).
$$
Use $a_p=\sum 2\pi il\,a_{k,l}e^{2\pi i(kq+lp)}$,
$a_{pq}=-4\pi^2\sum kl\,a_{k,l}e^{2\pi i(kq+lp)}$, and the analogous
formula for $a_{pp}$. This proves (6.1), including its sign.

Equations (4.5)--(4.6) cancel both displayed terms in
$(\partial_s-iA_N/h)V_N$. The periodic gluing in (5.4) justifies using
(2.2) in this calculation at the boundary. The residual satisfies
$$
 |(\partial_s-iA_N/h)V_N(s)_{xy}|
 \le Ch/\sqrt N.
 \tag{6.2}
$$
It has Euclidean norm at most $Ch$ in each column. Since $A_N$ is
Hermitian, $E_N(s)$ is unitary, and $V_N(0)=M_N$. Duhamel's formula,
followed by the triangle inequality in Euclidean norm, gives
$$
 \|(E_N(s)M_N-V_N(s))e_y\|_2
 \le\int_0^s Ch\,dv=Csh.
$$
Summing the squared column bounds proves (1.4). This error estimate
has been obtained from the exact finite-shift equation, without a
semiclassical theorem whose uniformity in the discrete columns would
need to be assumed.

## 7. Consequences for entry bounds and physical pair kernels

By (1.3) and $\sum_m|d_m|=2$,
$$
 |V_N(t)_{xy}|\le2\sqrt{1+40000t}/\sqrt N.
$$
Each entry of the remainder is at most the column norm $Cth$.
For all sufficiently large odd $N$, this gives
$$
 |U_{xy}|\le3/\sqrt N,\qquad |V_N(t)_{xy}|\le3/\sqrt N.
 \tag{7.1}
$$
Writing $F=U-V$, the elementary identity for the difference of
squared absolute values implies
$$
 \|P(U)-P(V)\|_{\rm HS}
 \le(\max|U_{xy}|+\max|V_{xy}|)\|F\|_{\rm HS}\le C/N.
$$
For the reversal kernel use
$$
 U_{xy}\overline{U_{yx}}-V_{xy}\overline{V_{yx}}
 =F_{xy}\overline{U_{yx}}+V_{xy}\overline{F_{yx}}.
$$
Transposition preserves the Hilbert--Schmidt norm, so the same estimate
proves the second part of (1.6).

The self-products of the four branches give the nonoscillatory part of
$P(V)$,
$$
 P_{\rm self}(x,y)=\frac1{4N}\sum_{m=0}^3 B_m(t,x/N,y/N)^2.
 \tag{7.2}
$$
Thus every entry of $P_{\rm self}-\mathbf1\mathbf1^*/N$ has absolute
value at most $40000t/N$, and its operator norm is at most $40000t$,
by the elementary row-column Schur bound. The remaining twelve terms
have phases $\Phi_m-\Phi_{m'}$, $m\ne m'$, and are retained with their
exact coefficients. Showing their operator norms tend to zero is a
separate oscillatory-matrix step, not silently inferred from (7.1).

