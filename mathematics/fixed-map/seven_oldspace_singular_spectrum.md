# The singular spectrum of the sevenfold arithmetic oldspace

Use the [prescribed kicked cat map](fixed_map_resolvent_frontier.md) at
$\tau=10^{-80}$. Let $N=49m$ with $m$ odd, and let $P$ project onto
the vectors supported on multiples of seven and invariant under
translation by $N/7$. Write $W=P U_N|_{\operatorname{ran} P}$.

**Theorem.** For each $t\in[0,1]$ and $\epsilon>0$ there are
$c>0$ and $N_0$ such that for every admissible $N\ge N_0$,
at least $c\sqrt N$ of the $m$ singular values of $W$ lie in
$(t-\epsilon,t+\epsilon)$. In particular, the singular spectra
converge to $[0,1]$ in Hausdorff distance and $\|W\|\to1$.

The [earlier oldspace calculation](../spectral_research/proofs/research_round2_2026_10_20/arithmetic_oldspace_escape.md)
proved exact escape at every finite dimension and mean squared retention
tending to $1/49$. These statements allow singular values tending to
one. The [vertical estimate](torsion_interference_vertical_outliers_20261118.md)
involves just one of the two support conditions. Here we use both.
Numerical checks and the exact scope of the Lean certificates are in the
[verification record](../../evidence/research/20261118_oldspace_spectrum/README.md).

## 1. The seven translates and their relative phases

Let $J:\mathbb C^m\to\mathbb C^N$ send the coordinate vector at $y$
to the normalized sum at $7y+jN/7$, $0\le j<7$. The exact kernel
identity $M_N J=J M_m$ gives $J^*U_NJ=C M_m$, where $C=J^*KJ$
and $K=\exp(i\tau N A_N)$. Thus $C$ and $W$ have the same
singular values.

Let $q_j=1/2+j/7$, $\theta_j=2\pi j/7$. The diagonal of $A_N$
is $V(x/N)$, and its forward hopping weight is
$e^{-i\alpha_0}r(1/2+(x+1/2)/N)/200$, where
$$
 r(q)=(1-\cos 14\pi q)(1+\cos 2\pi q),\qquad
 V(q)=\cos14\pi q-1/10+r(q)(1/10+\sin(2\pi q)/100).
$$
In particular, the shifted hopping profile vanishes quadratically at every
$q_j$. Put $F_j=\tau V'(q_j)$. Direct differentiation gives
$$
 b_j=F_j/(2\pi\tau)=\sin\theta_j/5+
             (\cos(2\theta_j)-\cos\theta_j)/50,\qquad b_0=0.
$$
For integer weights $h_j$, $1\le j\le6$, the condition
$\sum h_j b_j\in\mathbb Q$ forces all weights equal, and then the sum
vanishes. In $\mathbb Q(\zeta_7,i)$ the automorphism with exponent
15 modulo 28 fixes $\zeta_7$ and reverses $i$, so the sine sum
vanishes. The three sines at $j=1,2,3$ are rationally independent:
the antisymmetric polynomial of degree at most six has constant
coefficient zero and cannot be a nonzero multiple of $\Phi_7$.
Hence $h_j=h_{7-j}$. The cosine difference has trace zero in the
real cubic field, so a rational value must be zero. The three cosines
at $j=1,2,3$ are independent by the same polynomial argument with
symmetric coefficients. Doubling permutes the three sign classes
cyclically, so the three corresponding weights are equal. This proves the
claim. Because $7\tau$ is nonzero rational, the discrete rotation
$7(F_1,\ldots,F_6)$ is dense in the subtorus of angle vectors of sum
zero modulo $2\pi$. Indeed its annihilating integer characters are
precisely the multiples of the sum character.

The angle perpendicular to this subtorus will also matter. Set
$G(u)=\sum_{j=0}^6 V(q_j+u)-7V(q_0+u)$. Summing the first two
harmonics gives
$$
 G(u)=7(1+\cos14\pi u)
 \left(\cos(2\pi u)/10+(1-\cos2\pi u)\sin(2\pi u)/100\right).
$$
Thus $G(0)=7/5$, $G'(0)=0$, and
$\kappa=\tau G''(0)/2=-357\pi^2\tau/5\ne0$.

## 2. The law in windows smaller than the square-root scale

For $s=7/2+7l$, all $Nq_j+s$ are integer multiples of seven. On the
$L$ normalized combs with $0\le l<L$, the compression $C$
differs from the diagonal map with entries
$$
 d_l=\tfrac17\sum_{j=0}^6\exp(i\tau N V(q_j)+isF_j)
$$
in operator norm by $O_\tau((1+L)^2/N)$ whenever $L=o(\sqrt N)$.
Indeed the two hopping shifts on the union of the supports each have
this norm bound, as does the diagonal Taylor remainder. The diagonal
comparison preserves that union, so integrating the residual for time
one gives the bound without a dimension factor.

Let $L\to\infty$, $L=o(\sqrt N)$. Along a subsequence on which
$7\tau N/5\to\beta$ modulo $2\pi$, the empirical singular law of this
restricted input (the inverse cat image of the combs for $U_N$) is
the law of
$$
 Y_\beta=|1+\textstyle\sum_{j=1}^6 e^{ix_j}|/7,\qquad
 \sum_j x_j=\beta\pmod{2\pi},
$$
under Haar measure on the coset. For each nonconstant subtorus
character the geometric mean is $O_h(1/L)$ uniformly in the starting
phases. Trigonometric approximation proves the law, and the existence
of a finite orbit net gives convergence of the largest singular value
to the coset maximum. For $|\beta|\le\pi$ this maximum is
$|1+6e^{i\beta/6}|/7$. Indeed at a maximum the resultant has modulus
at least $|1+6e^{i\pi/6}|>6$, so every term has positive real
projection onto it. Constrained differentiation makes the six relative
sines equal. Positivity then makes the six phases equal, and the root
closest to one maximizes the modulus.

The moments of $Y_\beta^{2k}$ for $k\le5$ are independent of
$\beta$. At $k=6$ the moment is
$(27210169+1440\cos\beta)/7^{12}$.
In the product expansion a character survives only when the multiplicity
differences for letters 1 through 6 coincide. The first nonzero
difference uses these six letters once against six copies of letter
zero, or the reverse. Each contributes $6!$. The constant term is the
sum of squared multinomial coefficients of length six on seven letters.

To obtain arbitrarily large singular values in *every* admissible
dimension one must also vary the sum of relative phases. In windows at
offset of order $\sqrt N$ this sum varies by order one, as does the
hopping. The following construction handles both effects.

## 3. Propagation of finite packets at the square-root scale

Fix a compact range of $z>0$. Take $s=7/2+7l$ with $z_s=s^2/N$
in this range, and use the coordinate $n=x-Nq_j-s$ on patch $j$.
For fixed $R$, uniformly on $|n|\le R+1$, the matrix $\tau N A_N$
has diagonal $a_{j,N}(s)+F_j n+o(1)$ and forward weight
$z_s c_j+o(1)$, with
$$
 a_{j,N}(s)=\tau N V(q_j+s/N),\qquad
 c_j=\frac{98\pi^2\tau}{200}e^{-i\alpha_0}(1+\cos\theta_j).
$$
This follows from
$r(j/7+h)=98\pi^2(1+\cos\theta_j)h^2+O(h^3)$.
The half-lattice shift contributes $o(1)$.

With the diagonal and the weight above, a plane mode $e^{ipn}$
evolves at time $u$ into
$$
 \exp\left(iu a_{j,N}(s)+i(p+uF_j)n+
 iz_s\int_0^u 2\operatorname{Re}(c_j e^{i(p+vF_j)})\,dv\right).
$$
Substitute it in the time-dependent equation to check the formula.
Call the time-one integral $H_j(p)$, a first harmonic with zero
constant term. Multiply the mode by
$\chi_R(n)=(2R+1)^{-1/2}{\bf1}_{|n|\le R}$ and embed in the finite
matrix. A unit lattice shift changes this cutoff by $O(R^{-1/2})$
in norm. Substitution gives residual
$O(z_s|c_j|R^{-1/2})+o_{N\to\infty;R}(1)$, including the boundary
sites. Unitary variation of constants bounds the final error by the
integral of this residual. For any fixed finite combination of modes,
sum the errors with their coefficient magnitudes.

## 4. Simultaneous recurrence of the hopping phases

For large fixed integer $B$, take the following finite subset of the
momentum circle:
$$
 E=\left\{\sum_{j=1}^5 k_jF_j+2\pi h/7:
                  |k_j|\le B,\ 0\le h<7\right\}.
$$
Its elements are distinct by §1. Translation by $2\pi/7$ preserves
it, and translation by each $F_j$ changes a fraction $O(1/B)$,
including $F_6=-\sum_{j=1}^5F_j$. For a momentum $p$ to be chosen,
use the normalized packet proportional to
$\chi_R(n)|E|^{-1/2}\sum_{\gamma\in E}e^{i(p+\gamma)n}$.
It is supported on $7\mathbb Z$ because of the torsion translates.
As $R\to\infty$ the finite Gram matrix of the modes tends to the
identity. In particular its norm tends to one before normalization
and multiplication by $e^{iF_j n}$ changes it by squared norm tending
to $|(E+F_j)\triangle E|/|E|$. The Gram matrix also controls uniformly
the error of replacing unit-modulus multipliers by one on all of $E$.

Choose $p$ outside the zero sets of all expressions
$$
 h_0\kappa+\sum_{j,\gamma} h_{j\gamma}H_j(p+\gamma),
 \qquad h_0\in\mathbb Z\setminus\{0\},\quad h_{j\gamma}\in\mathbb Z.
$$
Each is a first harmonic plus a nonzero constant, hence its zero set
is finite or empty. This excludes at most countably many momenta.
For this $p$, the closure of the positive real orbit with velocity
$(\kappa,(H_j(p+\gamma))_{j,\gamma})$ contains the whole circle
$(a,0,\ldots,0)$. By the character criterion for a torus line, the
closure is the subgroup annihilated by all zero-frequency integer
characters. One can see this by averaging characters over $[0,T]$
and using density of trigonometric polynomials. The annihilating
characters here have first coordinate zero. For the discrete rotation
in §1 the criterion uses frequencies that are multiples of $2\pi$.

Thus for any target angle $a$ there is a $z>0$ with $\kappa z$
arbitrarily close to $a$ and all $z H_j(p+\gamma)$ arbitrarily
close to zero, modulo $2\pi$. Uniformly over target angles, one can
use finitely many closed intervals of positive length in $(0,\infty)$
such that at least one entire interval works for each target. Use a
strict margin and a finite subcover of the target circle.
Choose $B,p$, then the intervals, then $R$, then $N$. For $z_s$
in the chosen interval, §3 and the Gram matrix bounds show that $K$
acts on each translated packet within an arbitrarily small norm error
of multiplication by $e^{ia_{j,N}(s)}$. All estimates are uniform
in those centers for sufficiently large $N$.

## 5. Realizing the singular values

Choose six phases $x_j$ with
$|1+\sum e^{ix_j}|/7=t$. The phase torus is connected and the
resultant ranges from zero (the seven seventh roots of unity) to one
(all phases zero). Uniformly on the intervals of §4,
$$
 \sum_{j=1}^6(a_{j,N}(s)-a_{0,N}(s))
   =7\tau N/5+\kappa z_s+O_\tau(|s|^3/N^2).
$$
Use §4 with target $\sum x_j-7\tau N/5$. Inside a smaller concentric
interval there are $\gg\sqrt N$ admissible centers $s$, with a
uniform constant because the set of intervals is finite. Changing a
center by $7l$ for bounded $l$ changes its relative phases by
$7l(F_1,\ldots,F_6)+o(1)$ and its $z_s$ by $o(1)$, uniformly.
A finite-net segment of the dense rotation of §1 brings every
relative angle close to $x_j$ with a bounded adjustment: first
correct the small error in the angle sum in one component, then use
the net in its coset. Space the initial centers by more than twice
the packet width plus twice the maximum adjustment. The corrected
packets still number $\gg\sqrt N$, and all their supports are
disjoint including after translation by $jN/7$.

At each center combine its seven packets with equal weights to form
$Jv_s$. On its $j$-th component $K$ is close to multiplication
by $e^{ia_{j,N}(s)}$, while $K^*$ is close to multiplication by
its inverse with the same error by unitarity. For
$d_s=\frac17\sum_j e^{ia_{j,N}(s)}$, both
$\|(C-d_s)v_s\|$ and $\|(C^*-\overline d_s)v_s\|$ are arbitrarily
small, and $\big||d_s|-t\big|$ is arbitrarily small. Hence
$\|(C^*C-t^2)v_s\|\le\delta$ for any chosen $\delta>0$ with
appropriate tolerances. The $v_s$ are orthonormal. If $D$ is the
spectral projector of $C^*C$ onto $|\lambda-t^2|<\epsilon^2$,
then $\|Dv_s\|^2\ge1-\delta^2/\epsilon^4$. Sum over the packets
and use Bessel's inequality to bound the sum by $\operatorname{rank}D$.
Take $\delta<\epsilon^2/2$ and use
$|\sqrt\lambda-t|^2\le|\lambda-t^2|$. The Hausdorff conclusion follows
by taking a finite net in $[0,1]$.

## 6. Norms of polynomial observables of two projections

Put $p=P$ and $q=U_N P U_N^*=K P K^*$. For every noncommutative
star polynomial $f$,
$$
 \lim_N\|f(p,q)\|=\max_{0\le x\le1}\|f(p_0,q_x)\|,\qquad
 p_0=\begin{pmatrix}1&0\\0&0\end{pmatrix},\quad
 q_x=\begin{pmatrix}x&\sqrt{x(1-x)}\\\sqrt{x(1-x)}&1-x\end{pmatrix}.
$$
The block representation is classical (Raeburn and Sinclair,
[Math. Scand. 65 (1989), 278–290](https://doi.org/10.7146/math.scand.a-12283)).
An orthonormal eigenvector $v$ of $pqp$ on $\operatorname{ran}p$
with eigenvalue $0<x<1$ pairs with
$(qv-xv)/\sqrt{x(1-x)}$ to give the displayed block. The remaining
commuting cases occur in the endpoint blocks. The eigenvalues of
$pqp$ on $\operatorname{ran}p$ are the squared singular values of $W$.
The theorem supplies every block parameter in the limit, proving the
norm assertion. It also gives Hausdorff convergence to the whole unit
circle for the spectra of $(2p-I)(2q-I)$, whose two-dimensional
blocks have eigenvalues $2x-1\pm2i\sqrt{x(1-x)}$.

These are one-step assertions. The near-isometric input directions of
the full map are the inverse cat images of the constructed packets.
The signed trace sum at $k\asymp N$ and the local Sine₂ law remain open.
