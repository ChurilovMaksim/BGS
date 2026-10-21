> Source status: Imported research record or internal author audit; this is not a new independent review.
> Original source: `research_round3_2026_10_21/audit_phase_logtime_dispersion.md`. Embedded SHA256: `f806c3b85c026b11535f7dae1513171ddbba4df52a3c76075883dd0a8b8d92e2`.
> [Thematic guide](../../../../mathematics/spectral_research/topics/research_record.md).

# Independent audit of logarithmic-time dispersion and translated kicks

Date: 21 October 2026.

## Verdict and exact scope

The load-bearing arguments in Sections 3–7 of
phase_logtime_dispersion_and_missing_modes.md pass this independent audit.
The audited source SHA-256 is
40dd41555520f712b99f7467ed14fd41ff0369db4b44a9b78f21c7f5a8314b4b.
The source was read directly; earlier approval reports were not used as evidence.

I reconstructed the complex graph transform, the exact sampled kick,
the modular-eight quadratic decomposition, the Poisson normalization,
the stationary-phase remainder, and the iteration of errors.
These give fixed finite constants $C,A,N_0$ such that
$$
\max_{x,y}|(U_N^m)_{xy}|\le C A^m N^{-1/2}
$$
for every $m\ge1$ and every odd $N\ge N_0$.
The assertion becomes trivial at sufficiently long times. Its nontrivial
content is the exponential, rather than unspecified, dependence on $m$.

One minor detail merits explicit statement: the initial exact chirp has
slope $-3/4$, which lies in the original graph interval but outside the
narrower interval attained after the linear graph transform. Its initial
remainder is zero and entire, and the kick proof uses only the weaker
bound $|r|\le1$. Thus the same proof treats that first kick and gives
a remainder norm at most $33\tau$. This detail does not create a gap.

The same constants work for arbitrary sequences of real translations
of the given Hamiltonian, even if the translations depend on the dimension
and on the iterate. This extension is proved explicitly below.
No conclusion about a Heisenberg-time form factor or full $H_{\rm diag}$
is obtained from this audit.

## 1. Convention and the exact finite operator

This source uses $h=N^{-1}$, unlike the physical Weyl parameter
$(2\pi N)^{-1}$ used in the arithmetic commutator notes.
Its exact operator is
$$
 A_N\psi(x)=\sum_{k,l}d_{kl}
 e^{2\pi i k(xh+lh/2)}\psi(x+l),\qquad d_{kl}=(-1)^{kl}c_{kl}.
$$
The factor $(-1)^{kl}$ is forced by the odd modular inverse of two.
It is not an optional symbol convention. The corresponding real
ordinary symbol is
$$
 a(q,p)=V(q)+\frac{r(q+1/2)}{100}\cos(2\pi p-\alpha_0).
$$
The support is contained in $|k|\le9,\ |l|\le1$, and
$\sum|d_{kl}|<2$. These facts justify all finite-shift Taylor expansions
and complex bounds used below. The positive exponential
$e^{itA_N/h}$ has characteristic vector field
$$
 Y=(-a_p,a_q)/(2\pi).
$$

## 2. Global complex graph transform, including intercepts

Let
$$
 p(q)=r q+b+w(q),\quad -1\le r\le-1/2,\quad b\in\mathbb R,
 \quad \|w\|_\rho\le\eta,
 \qquad \rho=10^{-3},\quad\eta=100\tau .
$$
The norm is on the full horizontal strip. No real bound on $b$ is
needed in this analytic assertion.

For the linear map $L(q,p)=(3q-4p,-2q+3p)$, write $B=3-4r\in[5,7]$.
The inverse graph equation is
$$
 q=\frac{Q+4b+4w(q)}B.
$$
For $|\operatorname{Im}Q|<2\rho$, the affine center has imaginary
part at most $2\rho/5$. Its disk of radius $\rho/4$ stays strictly
within the input strip. The displacement is bounded by $4\eta/B$,
and the derivative by $16\eta/(B\rho)$, which is less than $1/2$.
The contraction therefore produces a global holomorphic inverse on
the output strip $2\rho$, uniformly in the real intercept.
On the real line the original map is increasing and onto, since its
derivative is $B-4w'>0$ and $w$ is bounded.

Direct substitution gives
$$
 r_1=\frac{-2+3r}{3-4r}\in[-5/7,-7/10],\quad
 b_1=b/B,\quad w_1(Q)=w(q(Q))/B,\quad
 \|w_1\|_{2\rho}\le\eta/5.
$$
Thus the linear step both controls the slope and restores a wider strip.

For the kick, start on $2\rho$. On initial points with
$|\operatorname{Im}q_0|<3\rho/2$, one has
$|\operatorname{Im}p_0|<2\rho$.
On the larger tube $|\operatorname{Im}q|\le3\rho$,
$|\operatorname{Im}p|\le4\rho$, finite Fourier bounds give
$$
 |Y_q|<3,\qquad |Y_p|<30.
$$
For instance every Fourier exponential has modulus at most
$\exp(2\pi(9\cdot3+1\cdot4)\rho)<1.22$.
Complex derivatives are uniformly bounded on this tube.
The analytic flow for time $\tau=10^{-80}$ exists uniformly and has
displacements $|\Delta q|\le3\tau,\ |\Delta p|\le30\tau$.
The map $q=q_0+\Delta q(q_0)$ has a holomorphic inverse on $\rho$
by the same disk argument, with derivative bounded through Cauchy
by $12\tau/\rho<1/2$.
The new nonlinear remainder is
$$
 w_{\rm new}(q)=w_1(q_0(q))+\Delta p(q_0(q))-r_1\Delta q(q_0(q)),
$$
so
$$
 \|w_{\rm new}\|_\rho\le\eta/5+33\tau<\eta.
$$
There is no accumulation of strip loss. Cauchy estimates supply all
required real jets, up to order eight, with constants independent of
the iterate.

For the first chirp, $r=-3/4,\ w=0$. The same kick argument starts
from an entire zero remainder and uses only $|r|\le1$; it yields
$\|w_{\rm new}\|_\rho\le33\tau$. Subsequent steps use the interval
for $r_1$ displayed above.

## 3. Exact sampling and the Schrödinger residual

A local piece is
$$
 v_h(x)=\sqrt h\sum_{\nu\in\mathbb Z}
 B(xh+\nu)e^{iF(xh+\nu)/h},\qquad F'=2\pi p.
$$
A fixed finite partition of unity uses lifted intervals of length $2/5$.
The kick moves their endpoints by at most $3\tau$, so their lengths
remain below $1/2$. Sampling and periodization have uniformly bounded
multiplicity.

Replacing $b$ by $b-n$ for an integer $n$, and $F(q)$ by
$F(q)-2\pi n q$, leaves every sampled piece exactly unchanged:
at $q=x/N+\nu$, the extra factor is
$\exp[-2\pi i n(x+N\nu)]=1$.
Periodicity of $a$ in momentum preserves the exact kick.
Thus the intercept may be normalized to $[-1/2,1/2]$ before each
finite Poisson cutoff. Normalization is not an approximation.

The eikonal and transport equations are
$$
 F_t=a(q,F_q/(2\pi)),\qquad
 B_t=vB_q+\tfrac12v'B,\qquad v=a_p(q,p)/(2\pi).
$$
Their characteristics are precisely $Y$.
The graph projection is invertible during the short kick. Transport
has the form $B(t,q(t,q_0))=B(0,q_0)J^{-1/2}$;
the graph jet bounds give a uniform linear $C^4$ amplitude bound.

Expanding the actual finite shift, rather than a substitute integral
operator, gives
$$
 A_N(Be^{iF/h})
 =e^{iF/h}\big[aB-ih(vB_q+\tfrac12v'B)+h^2E_h\big],
 \qquad \|E_h\|_\infty\le C\|B\|_{C^2}.
$$
To check the first-order coefficient, each Fourier mode contributes
$$
 l B_q+i\pi kl B+\tfrac i2 l^2F''B.
$$
Summing converts this into
$-i(vB_q+\tfrac12v'B)$.
The $F_t$ and $B_t$ equations therefore cancel orders zero and one
in $h\partial_t\psi-iA_N\psi$.

The normalization $\sqrt h$ makes the pointwise residual
$O(h^{5/2}\|B\|_{C^4})$. There are $N=h^{-1}$ sample points, so
its ordinary $\ell^2$ norm is $O(h^2\|B\|_{C^4})$.
Unitary Duhamel evolution divides by $h$ and integrates over the
fixed time $\tau$, yielding an $\ell^2$ error $O(h\|B\|_{C^4})$.
No expansion in $\tau/h$, and no exponential in $\tau/h$, is used.
Periodization commutes with the exact finite shifts, so no omitted
endpoint term is present.

## 4. Exact quadratic decomposition and Poisson normalization

For odd $N$, $8\overline8=1+s_NN$ with
$s_N\in\{1,3,5,7\}$, once the irrelevant dimension $N=1$ is excluded.
The exact kernel separates as
$$
 M_{xy}=\sqrt h\,e^{iS(xh,yh)/h}\chi_{s_N}(x,y),
 \quad
 S(Q,q)=-\frac\pi4(3Q^2-2Qq+3q^2),
$$
$$
 \chi_s(x,y)=\exp[-2\pi i s(3x^2-2xy+3y^2)/8].
$$
This identity holds for all integer lifts of $x,y$.
The correction is eight-periodic in both arguments, hence is an
exact sum of 64 characters. Parseval bounds the sum of coefficient
absolute values by eight. The corresponding one-variable expansion
for a fixed source column has coefficient sum at most $\sqrt8$.

The initial application to a coordinate vector therefore produces a
fixed finite number of exact chirps, each with
$$
 p(q)=-3q/4+yh/4+u/8,\qquad w=0.
$$
Individual modular characters need not be $N$-periodic.
Only their complete recombination is used when changing integer lifts;
the exact identity above supplies that periodicity.

Applying $M_N$ to one piece gives an expression with normalization
$h\sum_n$, not $\sqrt h\sum_n$.
Poisson summation consequently gives the integrals
$$
 \int B(y)e^{i\Phi_{v,k}(Q,y)/h}\,dy,\qquad
 \Phi_{v,k}=S(Q,y)+F(y)+2\pi(v/8-k)y.
$$
The output character contributes $2\pi uQ/8$ to the output phase.
This normalization is exactly what produces another $\sqrt h$
WKB piece after stationary phase.

## 5. Uniform stationary phase, including exterior critical points

Globally on the real axis,
$$
 \Phi_{yy}=2\pi(r+w'(y)-3/4)
$$
lies in a fixed strictly negative interval. Therefore the critical point
$y_c(Q)$ is unique, whether or not it belongs to the amplitude support.
After intercept normalization and using the fixed lifted charts,
$$
 \Phi_y/(2\pi)
 =Q/4+(r-3/4)y+b+w(y)+v/8-k .
$$
All terms apart from $k$ are uniformly bounded on the support.
For $|k|>20$, four integrations by parts give
$$
 O\big(h^4(1+|k|)^{-4}\|B\|_{C^4}\big).
$$
The summed tail is uniform. For the remaining 41 integers $k$,
the critical points themselves lie in one fixed bounded real interval.

For clarity, a global Morse coordinate proves the finite-$k$
stationary-phase assertion even if $y_c$ is outside the support:
$$
 z=\operatorname{sgn}(y-y_c)
      \sqrt{-2(\Phi(y)-\Phi(y_c))}.
$$
Strict concavity makes this a global increasing diffeomorphism.
The quotient
$$
 \frac{-2(\Phi(y)-\Phi(y_c))}{(y-y_c)^2}
 =-2\int_0^1(1-t)\Phi''(y_c+t(y-y_c))\,dt
$$
is bounded above and below. The previously established phase jets
bound the coordinate derivatives needed for a $C^4$ transformed
amplitude. Its support has uniformly bounded length and location.
Its $C^4$ norm is at most $C\|B\|_{C^4}$.

For the transformed amplitude $\widetilde B$, the Fourier Gaussian
identity, justified first with damping, gives
$$
 \int e^{-iz^2/(2h)}\widetilde B(z)\,dz
 =\sqrt{2\pi h}\,e^{-i\pi/4}
 \frac1{2\pi}\int\widehat{\widetilde B}(t)e^{iht^2/2}\,dt.
$$
Four integrations by parts at large Fourier frequencies show that
$\int t^2|\widehat{\widetilde B}(t)|\,dt
 \le C\|\widetilde B\|_{C^4}$.
Using $|e^{iht^2/2}-1|\le ht^2/2$ proves the remainder
$O(h^{3/2}\|B\|_{C^4})$, with leading term
$$
 \sqrt{2\pi h}\,e^{-i\pi/4}
 \frac{B(y_c)}{\sqrt{-\Phi_{yy}(Q,y_c)}}
 e^{i\Phi(Q,y_c)/h}.
$$
If the critical point is outside the support, $B(y_c)=0$;
the same estimate remains valid. No implicit interior-critical-point
assumption is needed.

After the fixed output partition, the sum of all leading amplitude
$C^4$ norms is at most $C_{\rm lin}\|B\|_{C^4}$.
The number of branches is bounded by $64\cdot41\cdot4$.
The implicit derivative $dy_c/dQ=(3-4r-4w')^{-1}$ and its higher
derivatives are uniformly controlled. Pointwise remainders of order
$h^{3/2}$ become $\ell^2$ remainders of order $h$.

## 6. Iteration and the translated extension

Let $S_m$ denote the sum of $C^4$ norms of every amplitude in the
representation after $m$ steps. The preceding bounds give
$$
 S_{m+1}\le A_0 S_m,\qquad
 \text{new error at step }m+1\le C_0hS_m.
$$
The initial sum is bounded independently of the source column and $N$.
All previous errors propagate under the actual unitary matrices and
do not grow in norm. Choosing $A>\max(2,A_0)$ bounds the full sum
of new errors by $ChA^m$ and the amplitude sum by $CA^m$.
Each sampled leading term has size at most $\sqrt h S_m$;
the error in one coordinate is at most its $\ell^2$ norm.
This proves the claimed kernel estimate with a single threshold $N_0$.

Now allow, at each step, any real translation
$$
 a_j(q,p)=a(q+q_j,p+p_j).
$$
Its coefficients are $d_{kl}e^{2\pi i(kq_j+lp_j)}$.
The support, coefficient absolute values, reality relation, and
coefficient sum are unchanged. Every tube bound, graph transform,
finite-shift remainder and amplitude estimate above therefore has
exactly the same uniform constant. Each kick is still unitary.
Consequently
$$
 \max_{x,y}\left|
 \left(e^{i\tau Q_N(a_m)/h}M_N\cdots
       e^{i\tau Q_N(a_1)/h}M_N\right)_{xy}\right|
 \le CA^mN^{-1/2}.
$$
The real translations may vary with both $N$ and $j$.
This conclusion requires no average over translations.
Further estimates involving sums of character histories still need
their separate exact coefficient and norm bounds.

## 7. Surviving consequences and limitation

The source's temporal-frame consequence is valid for every vector in
every eigenspace: the kernel estimate through a sufficiently small
multiple of $\log N$ bounds the corresponding coordinate mass by
$O(1/\log N)$. Degeneracies cause no exception.

If $\Pi_\lambda$ denotes an eigenspace projection, the largest possible
coordinate mass of a unit vector in that space is
$\Pi_{\lambda,xx}$. Therefore the source's uniform eigenvector bound
implies $\Pi_{\lambda,xx}\le\mu_N$, and
$$
 \sum_{\lambda,x}\Pi_{\lambda,xx}^2
 \le\mu_N\sum_{\lambda,x}\Pi_{\lambda,xx}=N\mu_N.
$$
The full commutant thus has at least $N-O(N/\log N)$ Hilbert–Schmidt
dimensions invisible to position-diagonal projection.
On the commutant, the doubled resolvent equals $(1-r_N)^{-1}I$.
Projecting its difference from any map with diagonal range onto the
orthogonal complement of that range proves the source's resolvent
approximation lower bound.

These statements do not evaluate the correlations between the missing
modes. An approximation-error lower bound is not a lower bound for the
difference of two squared norms, and the source correctly distinguishes
them. Full $H_{\rm diag}$ remains outside the proved scope.
