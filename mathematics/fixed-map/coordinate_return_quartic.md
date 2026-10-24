# Quartic coordinate return for the original fixed kick

**Claim:** BGS-TRACE-108. **Status:** analytic author proof with internal
reconstruction and self-review, 21 October 2026. No external refereeing,
formal verification or priority claim. This is a one-step intensity theorem.

## Model and conclusion

Use exactly the odd-modulus matrices, modular inverse conventions and fixed
$\tau=10^{-80}$ of [TRACE-106](physical_kick_trace_decay.md), §1.
The ordinary-half symbol is its equation (5), including the translation
$r(q+1/2)$ in the momentum-dependent coefficient. For $U_N=e^{i\tau NA_N}M_N$,

$$
\lim_{N\to\infty,\ N\text{ odd}}\sum_{x=0}^{N-1}|U_N(x,x)|^2
=1-\frac{25823\pi^4}{4800000000000}\tau^4+E,
\qquad |E|\le10^{56}\tau^5.                         \tag{1}
$$

In particular the limit is strictly less than $1-10^{-7}\tau^4$.
The limit is at fixed positive $\tau$, not a joint limit replacing it by
a vanishing coupling. The error term in (1) is a scalar independent of $N$.

## Four-sheet construction and the limit

Set $\kappa=2\pi$, $h=(\kappa N)^{-1}$ and $t_*=\tau/\kappa$.
For the ordinary-half symbol $a$, solve the Hamilton--Jacobi equation

$$
\partial_tF=a(Q,\partial_QF),\quad
F(0,Q,s)=-\frac{3Q^2-2Qs+3s^2}{8}=:F_0(Q,s).
                                                               \tag{2}
$$

The phase $G=F-F_0$ is periodic in the appropriate lifted variables.
Holomorphic characteristics give $|G|\le10|t|$ on the spatial strip
of width $.003$ for complex $|t|\le T=10^{-12}$. One can construct
these characteristics on the strip of width $.01$ using
$|a|<4$, $|X_a|<300$, $|DX_a|<20000$.

The exact Gauss decomposition has four sheets $s\mapsto s+m$,
$m=0,1,2,3$, each with prefactor $1/(2\sqrt N)$ and common phase
$e^{3\pi iN/4}$. Its transported amplitude is

$$
B_m(t,Q,s)=2\sqrt{F_{Qs}(t,Q,s+m)}.
$$

The positive root continues the value one at $t=0$. The exact lifted
Gauss identity, deck transformations, transport equation, residual and
Poisson estimates are given in the
[complete coordinate proof](../spectral_research/proofs/research_round14_2026_10_21/structural/r14_original_coordinate_phase_bridge_test.md),
§§2--6. These steps matter: treating the modular half as an ordinary half
would change (2) and lose the sheets.

For clarity, the error needed for (1) is only one-step error. Taylor expansion
of the finitely many Weyl shifts leaves an evolution residual
$O(h/\sqrt N)$ per entry. Unitary column Duhamel gives Hilbert--Schmidt
error $O(N^{-1/2})$. The diagonal vector of the leading approximation is
bounded in $\ell^2$, so the difference of diagonal squared norms is $o(1)$.

For two different sheets, odd sheet differences have a half-integer
separation from every discrete Fourier alias. For differences $\pm2$,
the integer linear part cancels on the grid, but the remaining analytic
phase is nonconstant: its values at $Q=0,1/4$ differ by at least $t_*/800$.
Poisson summation with endpoint cutoffs, summing all aliases, makes these
cross terms tend to zero. The equal-sheet contribution is therefore

$$
\int_0^1 k_{t_*}(q,q)\,dq,
\qquad k_t(Q,s)=\sum_{m=0}^3 F_{Qs}(t,Q,s+m).        \tag{3}
$$

## Exact quartic coefficient and remainder

The first three coefficients in (3) vanish. At time order $n$ the
momentum degree is at most $n$; summing four sheets keeps only multiples
of four, and the $s$ derivative kills the zero degree.

Here is a direct check of the first surviving coefficient. Put
$R(Q)=r(Q+1/2)$, $\ell=i\kappa$, $D_n=\partial_Q-3n\ell/4$, and
$u(Q)=(-3-4i)R(Q)/1000$. If $g_4$ is the coefficient of $t^4$ in $G$,
its highest momentum component is

$$
g_4=\frac{\ell^3}{96}D_4^3(u^4).
$$

With $z=e^{2\pi iQ}$,

$$
[z^2]R^4=\frac{245}{32},\quad (-3-4i)^4=-527-336i,
\quad
\frac{[z^2]g_4}{\kappa^6}
=-\frac{25823}{614400000000000}
-\frac{343i}{12800000000000}.                       \tag{4}
$$

The diagonal integrated coefficient is $8\kappa^2\Re[z^2]g_4$.
Substituting $t_*=\tau/\kappa$ gives the coefficient in (1).
The [quartic addendum](../spectral_research/proofs/research_round14_2026_10_21/structural/r14_quartic_return_addendum.md)
derives the four recursions and Fourier selection in full.

Cauchy's estimate applied to $|G|\le10|t|$ bounds the tail by
$20|t|^5/T^4$ for $|t|\le T/2$. Spatial differentiation costs at
most $10^6$ on the narrower strip; the four sheets give a bound below
$8\cdot10^{55}|t|^5\le10^{56}\tau^5$. This proves (1), including
its fixed-coupling remainder. The negative quartic term dominates that
remainder at $\tau=10^{-80}$.

## Scope

Fresh exact-arithmetic quartic and Gauss/deck checks are included in the
[execution packet](../../evidence/executions/20261021/spectral-final/README.md).
One checker references the pre-editorial phase source; the packet records
the exact historical-byte replay rather than claiming it verified a changed hash.
Finite checks support the algebra and do not certify the analytic limit.

Independent coordinate phases replace $|\operatorname{Tr}U_N|^2$ by
the diagonal sum in (1). They are a different ensemble. Fixed $m=1$
contributions have an additional $N^{-2}$ in the microscopic pair sum;
(1) neither proves nor disproves that sum or BGS.
