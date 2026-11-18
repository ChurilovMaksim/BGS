# Explicit microscopic witnesses for the fixed kick at Pell dimensions

Keep the unitary matrices, $\tau=10^{-80}$, and the band-two test
$b_*=|\mathcal F^{-1}\phi|^2/(2I^2)$, $I=\int\phi$, of the
[standalone problem](../../record/remaining_breakthrough_task_20261021.md).
Here $\phi(s)=e^{-1/(1-s^2)}{\bf1}_{|s|<1}$. Write
$(1+\sqrt2)^k=h_k+v_k\sqrt2$, $H=\int b_*$, and
$w=|\widehat b_*|^2$. The signed defect includes the entire CUE
subtraction:
$$
 \Delta_{2,N}(b_*)=\frac1{N^2}\sum_{j=1}^{2N-1}
 w(j/N)\big(|\operatorname{Tr}U_N^j|^2-\min(j,N)\big).
$$

**Finite theorem.** At the actual fixed coupling,
$$
 \Delta_{2,h_{197}}(b_*)>21,\qquad
 \Delta_{2,h_{203}}(b_*)>1/100,\qquad
 \Delta_{2,h_{207}}(b_*)>1/1000.
$$
At $N=h_{203}$ the probability that the uniformly shifted spectrum
occupies an interval of unfolded length one is less than $7/25$.
For the unit-intensity Sine₂ process the same probability is at least
$1/2$. These estimates concern specified finite dimensions. In
particular, the $h_{207}$ bound concerns the band-two test, while the
earlier [TRACE-119](positive_time_spike.md) concerns the Abel statistic
at $h_{205}$.

## 1. The covering estimate

For odd $k$, $h_k^2-2v_k^2=-1$. The matrix $S$ of the frozen
map represents multiplication by $(1+\sqrt2)^2$ in the basis
$1,\sqrt2$. Therefore $S^k\equiv I\bmod h_k$. Exact Egorov
and irreducibility of the Weyl matrices give $M_N^k=\zeta I$,
$|\zeta|=1$, at $N=h_k$. See the
[Pell return](fixed_model_pell_crossover.md).

The literal diagonal and two hopping terms give
$\|A_N\|\le1+1/10+4(1/10+1/100)+2(4/200)<8/5$.
Every eigenphase of $\exp(iuA_N)M_N$ has angular distance at most
$|u|\|A_N\|$ from the spectrum at $u=0$. Indeed, over a short time
step $d$, the normal-matrix resolvent bound puts each eigenvalue
within chord distance $|d|\|A_N\|$ of the preceding spectrum.
Sum $2\arcsin(|d|\|A_N\|/2)$ over equal subdivisions and let the mesh
tend to zero. Thus the eigenphases of $U_N$ lie in at most $k$
arcs of length at most $8\tau N/15$ per arc on the circle of length
one, using $\pi>3$. The chance that an interval of unfolded length
$a$ hits any phase is at most $k(a/N+8\tau N/15)$.
For $k=203,a=1$ this is less than $7/25$. For Sine₂, the count
$X$ in that interval has $\mathbb E X=1$ and
$\mathbb E X(X-1)\le1$ by its two-point density. Cauchy–Schwarz yields
$\mathbb P(X>0)\ge1/2$.

## 2. Concentration of the smoothed count

Plancherel and Cauchy–Schwarz give $H=\int\phi^2/(2I^2)\ge1/4$.
The Fourier integral and integration by parts give, respectively,
$b_*\le1/2$ and $b_*(x)\le1/(9x^2)$ for $x\ne0$.
For the second bound use $\|\phi'\|_1=2e^{-1}$,
$I\ge e^{-4/3}$ from $[-1/2,1/2]$, $\pi>3$, and $e^{2/3}<2$.
For $|s|\le1/2$ this implies
$$
 b_N(s)=\sum_{\ell\in\mathbb Z} b_*(N(s+\ell))
 \le\tfrac12+\tfrac2{N^2}.
$$
Indeed the terms away from $\ell=0$ sum to at most
$8(1+\int_1^\infty x^{-2}\,dx)/(9N^2)$.

Enlarge the covering arcs on each side by $1000/N$. The enlarged union
$E$ has measure at most $k(2000/N+8\tau N/15)$.
For $S(\alpha)=\sum_l b_N(\theta_l-\alpha)$ the integral over $E$
is at least $H-2/9000$ since the interval of radius $1000/N$
about each $\theta_l$ lies in $E$. In particular it is greater than
$99H/100$. Thus $\mathbb E S^2\ge (99H/100)^2/|E|$.
The diagonal correction obeys
$N\int b_N^2\le(51/100)H$ for the dimensions used here.
The factorial moment is half the difference of these two terms.
The CUE reference is at most $H^2/2$ by positivity of $T_{N,b_*}$.
Consequently, with any upper bound $d$ for $|E|$,
$$
 \Delta_{2,N}(b_*)\ge
 \tfrac12\bigl[H^2((99/100)^2/d-1)-(51/100)H\bigr].
$$
For $k=197,203$ use $d=1/700,7/25$, respectively. The bracket
after factoring $H$ is positive and increasing in $H\ge1/4$,
giving lower bounds $68303/3200$ and $1289/89600$.

## 3. A Weyl-orthogonal return bound at $h_{207}$

Use $k=207$, $N=h_k$, $\eta=\tau N$, and the normalized
Hilbert–Schmidt norm $\|X\|_2=(\operatorname{Tr}X^*X/N)^{1/2}$.
Write $A=A_N$, $A_j=M_N^j A M_N^{-j}$,
$\bar A=k^{-1}\sum_j A_j$, and
$G=\sum_{j=0}^{k-1}c_j A_j$, $c_j=(k-1-2j)/(2k)$.
As in the [finite-symbol normal form](../../supplement/fixed_map/design-return/finite_symbol_normal_form.md),
$G-M_NGM_N^*=A-\bar A$. With $V=\exp(-i\eta G)$, two
applications of the unitary Duhamel commutator inequality give
$$
 \|VU_NV^*-\exp(i\eta\bar A)M_N\|_2
 \le \tfrac{\eta^2}{2}
 \left(\|[G,A]\|_2+\|[A,\bar A]\|_2+\|[G,\bar A]\|_2\right).
$$
The two commutators before the triangle inequality are
$[-G,A]$ and $[-G+A,\bar A]$. This inequality follows by
integrating the commutator in the derivative of
$e^{-iu(X+Y)}e^{iuX}e^{iuY}$. The normalized norm is unitarily
invariant, so telescoping $k$ powers multiplies the bound by $k$.
Also $\bar A$ commutes with $M_N$ and $M_N^k=\zeta I$.
The normalized trace difference is bounded by this norm.

The following estimates keep orthogonality before taking a norm.
Use label coordinates $(x,y)$ for which the action is
$C=\left(\begin{smallmatrix}3&2\\4&3\end{smallmatrix}\right)$
as in [TRACE-118](orbit_orthogonal_kick_spike.md). For $1\le d<k$
and a pair $v,w$ of nonzero support labels, put $r=v+C^dw\bmod N$.
A nonnegative majorant $b_{v,w,d}$ for the commutator coefficient
includes the magnitudes of both Fourier coefficients and
$$
 \min\left(2,\frac{44}{7N}\operatorname{dist}(\det(v,C^dw),N\mathbb Z)\right).
$$
This bounds $2|\sin(\pi\det(v,C^dw)/N)|$. Define the arrays
$$
 B_0(r)=\sum_{v+C^dw=r} b_{v,w,d},\quad
 B_1(r)=\sum_{v+C^dw=r} k|c_d|\, b_{v,w,d},\quad
 B_2(a)=\sum_{2r_1^2-r_2^2=a\bmod N} b_{v,w,d}.
$$
The last sum is over all triples with the indicated invariant of
their sum label. Weyl orthogonality gives
$k\|[A,\bar A]\|_2\le\|B_0\|_{\ell^2}$ and
$k\|[G,A]\|_2\le\|B_1\|_{\ell^2}$.
For the third commutator, write $k[G,\bar A]$ as the sum, over
$v,w,d$, of weighted orbit sums
$\sum_{j=0}^{k-1}c_j W_N(C^jr)$. Every label orbit has length
$L$ dividing $k$. The weight folded modulo $L$ at $a$ is
$(L-1-2a)/(2L)$, by summing the arithmetic progression. Thus the
norm of the orbit sum is $\sqrt{(L^2-1)/(12L)}\le\sqrt{k/12}$.
Orbits with different values of $2r_1^2-r_2^2\bmod N$ are orthogonal
because $C$ preserves this form. Within one bucket use the triangle
inequality. This gives
$k\|[G,\bar A]\|_2\le\sqrt{k/12}\|B_2\|_{\ell^2}$.
The proof works for the composite index $207$.

The [integer verifier](../../computations/verification/pell_window/verify.py)
uses the literal 32 coefficients of TRACE-118. It bounds each magnitude
strictly above on a grid of denominator $10^5$ and checks the summed
squares of all three arrays with integer arithmetic. The resulting
bounds are $7/5,13/5,14/5$, respectively. It also confirms from
the modular Weyl overlaps that
$\|k\bar A\|_2^2=k(1650797/4000000)$.
Use $\cos u\ge1-u^2/2$ for the real normalized trace of
$\exp(ik\eta\bar A)$. Combining it with the commutator error and
$\sqrt{k/12}<17/4$ gives
$$
 \frac{\operatorname{Re}\operatorname{Tr}(\overline\zeta U_N^k)}N
 \ \ge\ 1-\frac{\eta^2}{2}
 \left(k\frac{1650797}{4000000}+\frac75+\frac{13}5+\frac{17}4\frac{14}5\right)
 \ >\frac{31}{50}.
$$

The same single term gives $L_N(U_N;1) > 3/8$ at $N=h_{207}$:
multiply the squared bound by $e^{-2k/N}\ge 1-2k/N$.
The gap from the CUE limit $(1-e^{-2})/4$ exceeds $1/8$.

## 4. The full CUE subtraction at $h_{207}$

The autocorrelation formula gives
$\widehat b_*(s)/H=\int\phi(u-s/2)\phi(u+s/2)\,du/\int\phi^2$.
On the overlap of the supports, expand
$(1-x^2)^{-1}=\sum_{n\ge0}x^{2n}$. Each pair of even powers at
$u\pm s/2$ has average at least $u^{2n}+(s/2)^{2n}$ for
$n\ge1$. It follows that
$$
 w(s)/H^2\le g(s):=\exp\!\left(-s^2/(1-s^2/4)\right)
 \quad (0\le s<2).
$$
Put $g(2)=0$. For the discrete reference, use $\min(s,1)\le s$
and the monotonicity of $g$. Integration over the preceding mesh
interval bounds its $j$-th term by the integral of
$(s+1/N)g(s)$ there. Thus the reference divided by $H^2$
is at most $\int_0^2 s g(s)\,ds+2/N$. With
$x=s^2/(1-s^2/4)$, the integral equals
$\frac12\int_0^\infty e^{-x}(1+x/4)^{-2}\,dx<9/25$.
For the last inequality use mesh $1/16$ up to $8$, bound the
rational factor at each left endpoint and integrate the exponential.
The tail is at most $e^{-8}/2$. The exact verifier encloses
$e^{-1/16}$ by the cubic and quartic Taylor polynomials.

The autocorrelation also changes by at most
$2e^{-2}|s|/\int\phi^2<4|s|$ after normalization by its value
at zero, using $\|\phi\|_\infty\|\phi'\|_1=2e^{-2}$ and
$\int\phi^2\ge e^{-8/3}$. Hence $w(k/N)>99H^2/100$.
Keep the single nonnegative $j=k$ term on the actual side and
subtract the entire reference. With $H^2\ge1/16$, the result is
greater than
$$
 \frac1{16}
 \left(\frac{99}{100}\left(\frac{31}{50}\right)^2-\frac9{25}-\frac2N\right)
 >\frac1{1000}.
$$

For $\tau=0$, §1 gives $p_{h_k}(a)\le ak/h_k\to0$ in every
bounded window, so the translated point process tends vaguely
in probability to the empty process. For the fixed nonzero coupling,
the covering width and the normal-form remainder grow with $N$.
The signed pair limit and weak Sine₂ convergence at this coupling
remain open.
