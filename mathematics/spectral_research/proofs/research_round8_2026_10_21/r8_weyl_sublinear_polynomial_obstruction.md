> Source status: Imported author proof or research attempt; consult the review matrix before using it as a theorem.
> Original source: `research_round8_2026_10_21/r8_weyl_sublinear_polynomial_obstruction.md`. Embedded SHA256: `32a014694531ea01284a146334c223a22686de457970bb39e4a5fa39c109c618`.
> [Thematic guide](../../topics/approximation.md).

# Round 8: the original kick cannot be approximated by sublinear bandwidth

Date: 21 October 2026. Branch: Weyl propagation and long-time resummation.

## 1. Status and precise scope

This document proves a theorem about the **original** kick

$$
E_N=\exp(i\tau N A_N),\qquad \tau=10^{-80},
$$

along **all odd** dimensions. It rules out approximating this kick by
polynomials in its nearest-neighbour generator whose degree is $o(N)$,
even when the polynomial coefficients are chosen optimally and may depend
on $N$. The obstruction holds in operator norm and, more generally, for
every matrix of sublinear cyclic bandwidth.

This is an obstruction to a proposed method of approximating the exact
kick. It is **not** a counterexample to $H_{\mathrm{diag}}$, and it gives
neither a proof nor a disproof of the desired local spectral limit.
In particular, it does not exclude a successful nontruncated resummation
of the long-time Weyl expansion. No claim of historical priority is made.

All quantization conventions, the small fixed time, the all-odd limit,
and the position-displacement argument used in the proof are checked
below. No general Egorov theorem is invoked without proof.

## 2. The theorem

Write $\operatorname{dist}_N(x,y)=\min_{j\in\mathbb Z}|x-y+jN|$
for cyclic distance on $\mathbb Z/N\mathbb Z$. For a nonnegative integer
$d$, let

$$
\mathcal B_{N,d}
=\{B\in M_N(\mathbb C):B_{xy}=0
       \text{ whenever }\operatorname{dist}_N(x,y)>d\}.
$$

The Hilbert--Schmidt norm is unnormalized:
$\|B\|_{\mathrm{HS}}^2=\operatorname{Tr}(B^*B)$.

**Theorem 2.1.** For every sequence of nonnegative integers $d_N$
with $d_N/N\to0$, along all odd $N\to\infty$,

$$
m_{N,d_N}:=
\frac1N\sum_{\operatorname{dist}_N(x,y)\le d_N}|(E_N)_{xy}|^2
\longrightarrow0.
\tag{2.1}
$$

Consequently,

$$
\inf_{B\in\mathcal B_{N,d_N}}
\frac{\|E_N-B\|_{\mathrm{HS}}}{\sqrt N}
=\sqrt{1-m_{N,d_N}}\longrightarrow1,
\tag{2.2}
$$

and

$$
\inf_{B\in\mathcal B_{N,d_N}}\|E_N-B\|_{\mathrm{op}}
\longrightarrow1.
\tag{2.3}
$$

In particular,

$$
\inf_{\substack{p\in\mathbb C[z]\\\deg p\le d_N}}
\frac{\|E_N-p(A_N)\|_{\mathrm{HS}}}{\sqrt N}
\longrightarrow1,
\qquad
\inf_{\substack{p\in\mathbb C[z]\\\deg p\le d_N}}
\|E_N-p(A_N)\|_{\mathrm{op}}
\longrightarrow1.
\tag{2.4}
$$

Here the zero polynomial is included. Since $M_N$ is unitary, the same
two limits hold with $E_N-p(A_N)$ replaced by
$U_N-p(A_N)M_N$.

The proof occupies §§3--7. A useful feature of (2.4) is that it does not
merely show failure of a particular Taylor estimate: it applies to the
best polynomial of the allowed degree.

## 3. Exact symbol and Weyl conventions

For integer frequency vectors $u=(k,l)$, define

$$
W_N(k,l)=T_N(l\bmod N,k\bmod N),
\qquad
\widetilde W_N(k,l)=(-1)^{kl}W_N(k,l).
$$

Because $N$ is odd, one may take the integer representative
$2^{-1}=(N+1)/2$. Therefore

$$
(\widetilde W_N(k,l)\psi)(x)
=\exp\!\left(\frac{2\pi i}{N}k(x+l/2)\right)\psi(x+l).
\tag{3.1}
$$

The ordinary half in (3.1) is now a real half. We retain all integer
labels, including those outside a fundamental box; this avoids
discarding any alias signs. For

$$
\omega((k,l),(k',l'))=lk'-kl',
$$

direct multiplication of (3.1) gives the exact relation

$$
\widetilde W_N(u)\widetilde W_N(v)
=e^{\pi i\omega(u,v)/N}\widetilde W_N(u+v)
\qquad(u,v\in\mathbb Z^2).
\tag{3.2}
$$

For a smooth function $F$ on $\mathbb T^2$, put

$$
\operatorname{Op}_N(F)
=\sum_{v\in\mathbb Z^2}\widehat F(v)\widetilde W_N(v).
\tag{3.3}
$$

This series converges in operator norm, since smooth Fourier
coefficients are absolutely summable. Also

$$
\|\operatorname{Op}_N(F)\|_{\mathrm{op}}
\le\sum_v|\widehat F(v)|.
\tag{3.4}
$$

The original finite Fourier quantization is exactly

$$
A_N=\operatorname{Op}_N(a),
\tag{3.5}
$$

where

$$
\begin{aligned}
a(q,p)&=V(q)+\frac{r(q+1/2)}{100}
                        \cos(2\pi p-\alpha_0),\\
V(q)&=\cos(14\pi q)+\frac{r(q)}{10}
             +\frac{r(q)\sin(2\pi q)}{100}-\frac1{10}.
\end{aligned}
\tag{3.6}
$$

Indeed the original coefficient at $(k,l)$ is multiplied by
$(-1)^{kl}$ when it is expressed in the basis (3.1). The terms
independent of $p$ have $l=0$ and do not change. The remaining terms
have $l=\pm1$, so their $q$-Fourier coefficients acquire $(-1)^k$,
which is exactly the shift $q\mapsto q+1/2$ in their factor $r$.
Thus the shift in (3.6) is required by the original modular halves.

The elementary expansion

$$
r(q)=1+\cos(2\pi q)-\cos(14\pi q)
       -\tfrac12\cos(16\pi q)-\tfrac12\cos(12\pi q)
\tag{3.7}
$$

has Fourier coefficient sum $4$. The sum for a cosine or a sine is
$1$, Fourier coefficient sums are submultiplicative, and shifts preserve
them. Hence

$$
\sum_v|\widehat a(v)|
\le1+\frac4{10}+\frac4{100}+\frac1{10}+\frac4{100}
=1.58<2,
\qquad
\widehat a(v)=0\quad\text{if }|v|_1>9.
\tag{3.8}
$$

Finally, $\int_0^1r(q)\,dq=1$, and the chosen angle gives

$$
\widehat a(0,1)=\frac{e^{-i\alpha_0}}{200}
              =\frac{-3-4i}{1000},
\qquad |\widehat a(0,1)|=\frac1{200}.
\tag{3.9}
$$

These estimates are deliberately coarse; their role is to verify a
strictly nonzero classical displacement at the exact time $\tau$.

## 4. Fixed-time Egorov estimate proved from the Weyl product

Define the real Hamiltonian vector field and its lifted flow by

$$
X(q,p)=\frac1{2\pi}\bigl(a_p(q,p),-a_q(q,p)\bigr),
\qquad
\frac{d}{ds}\Phi_s(z)=X(\Phi_s(z)),\qquad \Phi_0(z)=z.
\tag{4.1}
$$

The vector field is periodic, so the lift satisfies
$\Phi_s(z+n)=\Phi_s(z)+n$ for $n\in\mathbb Z^2$.
Write

$$
\Phi_s(q,p)=(Q_s(q,p),P_s(q,p)),\qquad
E_N(s)=e^{isNA_N}.
$$

For every fixed smooth function $F$, uniformly for $0\le s\le\tau$,

$$
\left\|E_N(s)\operatorname{Op}_N(F)E_N(s)^*
           -\operatorname{Op}_N(F\circ\Phi_s)\right\|_{\mathrm{op}}
\le \frac{C_F}{N^2}.
\tag{4.2}
$$

Here and below constants may depend on the fixed symbol, the fixed time
$\tau$, and the fixed test function, but not on the odd dimension.

**Proof.** By (3.2), the coefficient multiplying
$\widehat a(u)\widehat F(v)\widetilde W_N(u+v)$ in
$iN[A_N,\operatorname{Op}_N(F)]$ is

$$
-2N\sin\!\left(\frac{\pi\omega(u,v)}N\right).
$$

Direct differentiation in (4.1) shows that the corresponding coefficient
in $\operatorname{Op}_N(X\cdot\nabla F)$ is $-2\pi\omega(u,v)$.
The real inequality $|\sin x-x|\le |x|^3/6$ gives

$$
\begin{split}
&\left\|iN[A_N,\operatorname{Op}_N(F)]
             -\operatorname{Op}_N(X\cdot\nabla F)\right\|_{\mathrm{op}}\\
&\quad\le
\frac{\pi^3}{3N^2}
\sum_{u,v}|\widehat a(u)|\,|\widehat F(v)|\,|\omega(u,v)|^3.
\end{split}
\tag{4.3}
$$

The sum in $u$ is finite. The sum in $v$ is finite because
$F$ is smooth. For example, applying $(1-\Delta)^4$ before Fourier
transformation bounds $|\widehat F(v)|$ by a constant times
$(1+|v|^2)^{-4}$, which is sufficient after multiplication by
$(1+|v|)^3$ in dimension two.

Let $F_s=F\circ\Phi_s$. It solves
$\partial_sF_s=X\cdot\nabla F_s$. All its derivatives of any fixed
order are bounded uniformly on the compact time interval. Thus the sum
in (4.3), with $F_s$ in place of $F$, is bounded uniformly in $s$.
Differentiate

$$
E_N(s)^*\operatorname{Op}_N(F_s)E_N(s).
$$

Its derivative is the unitary conjugate of
$\operatorname{Op}_N(\partial_sF_s)
-iN[A_N,\operatorname{Op}_N(F_s)]$, which has norm $O_F(N^{-2})$
by (4.3). Integration gives (4.2).

Every identity here uses the full integer lattice in (3.2)--(3.3), so
there is no omission of modular wraps or of aliases at composite odd
dimensions. $\square$

We also need the elementary trace limit

$$
\frac1N\operatorname{Tr}
  \bigl(\operatorname{Op}_N(G)\operatorname{Op}_N(F)\bigr)
\longrightarrow\int_{\mathbb T^2}G(z)F(z)\,dz
\tag{4.4}
$$

for fixed smooth $F,G$. To prove it first take finite Fourier
polynomials. The trace of $\widetilde W_N(w)$ vanishes unless both
coordinates of $w$ are divisible by $N$: a nontrivial shift has zero
diagonal, and a diagonal nonconstant additive character has zero sum.
For a fixed finite set of frequencies and sufficiently large $N$, the
only surviving total label is consequently $u+v=0$. Its phase in
(3.2) is $1$. This proves (4.4) exactly for those polynomials once
$N$ is sufficiently large. Approximation in the sum of absolute
Fourier coefficients, (3.4), and
$|N^{-1}\operatorname{Tr}B|\le\|B\|_{\mathrm{op}}$ prove the smooth
case. This also proves that the limit is independent of the prime
factorization of $N$.

## 5. The transition measure of the exact kick

Define probability measures on $\mathbb T^2$ by

$$
\mu_N=\frac1N\sum_{x,y\bmod N}|(E_N)_{xy}|^2
                         \delta_{(x/N,y/N)}.
\tag{5.1}
$$

Their total mass is $1$, because $E_N$ is unitary. We claim

$$
\mu_N\Longrightarrow\mu,
\qquad
\mu=(q,p\mapsto(q,Q_\tau(q,p)\bmod1))_*\,dq\,dp.
\tag{5.2}
$$

Here $dq\,dp$ is normalized Lebesgue measure on the torus.

For trigonometric polynomials $g,h$ on $\mathbb T$, let $D_g$
and $D_h$ be their values on the $N$-point position grid. Then
$D_g=\operatorname{Op}_N(g(q))$ and similarly for $h$. Directly
from the matrix entries,

$$
\int g(q)h(s)\,d\mu_N(q,s)
=\frac1N\operatorname{Tr}(D_gE_ND_hE_N^*).
\tag{5.3}
$$

Equations (4.2) and (4.4) give

$$
\frac1N\operatorname{Tr}(D_gE_ND_hE_N^*)
\longrightarrow
\int_{\mathbb T^2}g(q)h(Q_\tau(q,p))\,dq\,dp.
\tag{5.4}
$$

Finite sums of these products contain all trigonometric polynomials
on the product torus and are uniformly dense in its continuous
functions. Since both sides are probability measures, (5.4) proves
(5.2).

This limit concerns the physical matrix entries of the kick. It is
proved here from the exact Weyl law and does not invoke a stochastic
surrogate for coherent powers of $U_N$.

## 6. The limiting measure has no mass on the position diagonal

Let

$$
\delta(q,p)=Q_\tau(q,p)-q
\tag{6.1}
$$

be the first component of the periodic lifted displacement. We prove
that it is real analytic, is not identically zero, and has absolute
value less than $1/2$.

From (3.8), for the vector maximum norm and its induced matrix norm,

$$
\|X\|_\infty\le18,
\qquad
\|DX\|_{\infty\to\infty}
\le2\pi\sum_v|\widehat a(v)|\,|v|_1^2
<324\pi<1100.
\tag{6.2}
$$

Therefore, on the real lift, for $0\le s\le\tau$,

$$
\|\Phi_s(z)-z\|_\infty\le18s,
\tag{6.3}
$$

and

$$
\begin{split}
\|\Phi_\tau-\operatorname{id}-\tau X\|_\infty
&\le\int_0^\tau
       1100\|\Phi_s-\operatorname{id}\|_\infty\,ds\\
&\le9900\tau^2<10000\tau^2.
\end{split}
\tag{6.4}
$$

The $(0,1)$-Fourier coefficient of $X_q=a_p/(2\pi)$ is
$i\widehat a(0,1)$. Consequently, by (3.9) and (6.4),

$$
|\widehat\delta(0,1)|
\ge\frac\tau{200}-10000\tau^2
\ge\frac\tau{400}>0.
\tag{6.5}
$$

The second inequality uses the fixed exact number $\tau=10^{-80}$,
and is vastly strict. Thus $\delta\not\equiv0$. Equation (6.3) also
gives $|\delta|\le18\tau<1/2$.

For completeness, analyticity follows directly from a complex Picard
construction. On the strip
$\{z\in\mathbb C^2:|\operatorname{Im}z_j|<\rho\}$,
$\rho=1/100$, the factor multiplying any Fourier coefficient has
modulus at most
$e^{2\pi\rho|v|_1}\le e^{18\pi/100}<2$. Hence on that strip

$$
\|X\|_\infty<36,
\qquad \|DX\|_{\infty\to\infty}<648\pi<2100.
$$

For initial points in the strip of width $\rho/2$, the integral map

$$
w_s(z)\mapsto\int_0^sX(z+w_u(z))\,du
$$

maps the ball $\sup_{s,z}|w_s(z)|_\infty\le\rho/2$ into itself,
because $36\tau<\rho/2$, and is a contraction, because
$2100\tau<1/2$. Picard iterates are holomorphic in $z$, periodic
as displacements, and converge uniformly on the smaller strip.
Their limit is therefore holomorphic there; on the real torus it is
the unique real flow. This proves the asserted real analyticity of
$\delta$.

We include an elementary proof of the particular zero-set fact needed
here. Because the analytic periodic function $\delta(q,p)$ is not
identically zero, some integer $j\ge0$ makes

$$
c(q)=\partial_p^j\delta(q,0)
$$

a nonzero analytic function of $q$. Otherwise every derivative at
$p=0$ would vanish for every $q$, and one-variable analytic
continuation in $p$ would make $\delta$ identically zero. The zero
set of this particular nonzero $c$ on the circle is finite. Outside
that finite set of values of $q$, the analytic function
$p\mapsto\delta(q,p)$ is not identically zero, so it too has only
finitely many zeros on the circle. Fubini's theorem now gives

$$
\operatorname{Leb}\{(q,p):\delta(q,p)=0\}=0.
\tag{6.6}
$$

Since $|\delta|<1/2$, equality
$Q_\tau(q,p)=q\pmod1$ is equivalent to $\delta(q,p)=0$.
If $D=\{(q,s)\in\mathbb T^2:q=s\}$, (5.2) and (6.6) therefore imply

$$
\mu(D)=0.
\tag{6.7}
$$

The argument does not assume that the position displacement is nonzero
everywhere. In fact the vanishing hopping amplitude has classical
barrier positions. What is proved and needed is the zero measure of
the full zero-displacement set.

## 7. Proof of the bandwidth and polynomial conclusions

For $\eta>0$, let

$$
D_\eta=\{(q,s)\in\mathbb T^2:
                  \operatorname{dist}_{\mathbb T}(q,s)\le\eta\}.
$$

This is closed. If $d_N/N\le\eta$, then (5.1) gives
$m_{N,d_N}\le\mu_N(D_\eta)$. The elementary upper bound for closed
sets under weak convergence on a compact metric space, applied to
(5.2), yields

$$
\limsup_{N\ \mathrm{odd}}m_{N,d_N}\le\mu(D_\eta).
$$

Letting $\eta\downarrow0$, continuity from above for the probability
measure $\mu$ and (6.7) give (2.1).

For clarity, the closed-set upper bound just used follows by choosing
continuous functions between the indicator of $D_\eta$ and that of
an arbitrarily small open neighbourhood, applying weak convergence,
and then shrinking the neighbourhood. Thus no moment convergence or
unbounded-observable implication is hidden in this step.

Entrywise orthogonality for the Hilbert--Schmidt norm shows that the
best approximation to $E_N$ in $\mathcal B_{N,d_N}$ keeps its
entries inside the band and sets its other entries to zero. Since
$\|E_N\|_{\mathrm{HS}}^2=N$, its squared error is
$N(1-m_{N,d_N})$. This proves (2.2).

Every matrix $C$ satisfies
$\|C\|_{\mathrm{HS}}\le\sqrt N\|C\|_{\mathrm{op}}$. Hence (2.2)
implies

$$
\inf_{B\in\mathcal B_{N,d_N}}\|E_N-B\|_{\mathrm{op}}
\ge\sqrt{1-m_{N,d_N}}.
$$

The zero matrix is allowed and $\|E_N\|_{\mathrm{op}}=1$, providing
the opposite upper bound $1$. This proves (2.3).

Finally, the only $p$-frequencies in the original symbol are
$l=0,\pm1$. The exact original definition of $A_N$ consequently
has

$$
(A_N)_{xy}=0\quad\text{when }\operatorname{dist}_N(x,y)>1.
\tag{7.1}
$$

Multiplication of matrices, or induction on nearest-neighbour walks
on the cycle, proves
$(A_N^j)_{xy}=0$ when $\operatorname{dist}_N(x,y)>j$.
This induction uses cyclic distance and remains true across the wrap
from $N-1$ to $0$, regardless of any additional zero hopping
edges. Therefore every polynomial in $A_N$ of degree at most
$d_N$ lies in $\mathcal B_{N,d_N}$. Equations (2.2)--(2.3) give
the lower bounds in (2.4); the zero polynomial gives the upper bounds.
Unitary invariance of both norms proves the assertion for $U_N$.
This completes the proof. $\square$

## 8. Interpretation for a long-time Weyl expansion

Although $\tau$ is exceptionally small, it is fixed. The classical
position change in one kick is of order $\tau$, while one lattice
step is $1/N$. Thus a physically nontrivial part of the exact kick
requires a number of position steps proportional to $N$, with a
very small fixed proportionality constant. Sections 4--7 make this
observation into a norm theorem without substituting any numerical
value for $e^{i\tau NA_N}$.

For example, a Taylor truncation

$$
\sum_{j=0}^{d_N}\frac{(i\tau NA_N)^j}{j!},
\qquad d_N=o(N),
$$

cannot have operator-norm error tending to zero. Its error is in fact
asymptotically at least $1$. The same lower bound holds after any
choice of different coefficients at those degrees. This explains why
the literal growth of $\tau N$ cannot be repaired by optimizing a
sublinear-degree polynomial.

There are several boundaries to this conclusion:

1. A degree $cN$, with fixed positive $c$, is outside the theorem,
   even when $c$ is tiny. Such a degree is not $o(N)$.
2. The theorem concerns polynomial/band approximations to the **single
   exact kick**. It makes no assertion that every useful resummation of
   $U_N^m$ must first approximate that kick in operator norm.
3. In particular, an observable may admit cancellation even when a
   proposed operator approximation is poor. No lower bound on
   $|\Delta_{k,N}(b)|$ follows from (2.1)--(2.4).
4. The proof does not evaluate the signed sum of closed Weyl paths at
   $m\asymp N$, nor does it yield the CUE form factor.

For the original family, the first signed pair estimate still lacking
a proof in this branch is

$$
\frac1{N^2}\sum_{m\ge1}|\widehat b(m/N)|^2
   \left(|\operatorname{Tr}U_N^m|^2-\min(m,N)\right)
\longrightarrow0
\tag{8.1}
$$

for every fixed permitted $b$, with the sum finite by its fixed
Fourier support. By the exact formula in the problem, (8.1) is precisely
the $k=2$ diagonal comparison. Higher fixed $k$ remain required
for the stated success criterion. No unproved long-time cancellation
has been inserted into the proof above.
