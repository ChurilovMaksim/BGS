# Inserted trace and the exact obstruction to a quantum coboundary

**Claim:** BGS-TRACE-109. **Status:** analytic proof with author check.
The continuation, author-checked on 22 October, closes the previously conditional one-step input
by an independent [finite-grid proof](finite_grid_one_step_trace.md).
It retains one transport correction and controls the complete trace error by
$O(N^{-1})$, without the all-time sector or pressure construction.

## Protected points and inserted trace

Use the original model in [TRACE-106](physical_kick_trace_decay.md).
There are sixteen protected points $q\in\{0,1/2\}$, $p=j/8$:
four fixed points and six two-cycles. The symbol takes the values
$9/10$ and $-11/10$ on the two protected lines. Their exact action,
index and monodromy tables are preserved in the
[Round 13 proof](../spectral_research/proofs/research_round13_2026_10_21/orbit_correlations/protected_actions_and_one_step_trace.md).
These finitely many orbits are not the full long-time interference sum.

Write $v=\pi\tau/125$ and

$$
\begin{array}{ll}
T_{00}=6+39212v,&T_{01}=6+39188v,\\
T_{10}=6-48612v,&T_{11}=6-49788v,\\
\mathsf A=(T_{00}-2)^{-1/2}-(T_{01}-2)^{-1/2},&
\mathsf B=(T_{10}-2)^{-1/2}+(T_{11}-2)^{-1/2}.
\end{array}
$$

Put $\zeta_N=e^{2\pi i(3N-1)/8}$ and $\eta_N=e^{-i\pi N/2}$.
The exact plane-amplitude and odd-sector trace construction in
[exact amplitude](../spectral_research/proofs/research_continuation_2026_10_20/exact_amplitude.md)
and [odd traces](../spectral_research/proofs/research_continuation_2026_10_20/odd_trace_and_algebraic_rigidity.md)
implies, by stationary phase at these fixed points,

$$
\operatorname{Tr}U_N
=\zeta_N\left[\mathsf A e^{.9i\tau N}
+\mathsf B\eta_Ne^{-1.1i\tau N}\right]+O(N^{-1}),
                                                               \tag{1}
$$
$$
\operatorname{Tr}(A_NU_N)
=\zeta_N\left[.9\mathsf A e^{.9i\tau N}
-1.1\mathsf B\eta_Ne^{-1.1i\tau N}\right]+O(N^{-1}). \tag{2}
$$

Equation (2) comes from inserting the finite Weyl sum in the amplitude;
its leading symbol is $a(Q,F_Q)B_0$. It is not obtained by
differentiating the remainder in (1). The
[complete inserted-trace derivation](../spectral_research/proofs/research_round14_2026_10_21/signed_sum/r14_inserted_trace_and_two_copy_coboundary.md)
records this separate remainder estimate.

The elementary bounds $|\mathsf A|\le1.5v$,
$\mathsf B\ge1+6150v$ give

$$
\liminf|\operatorname{Tr}(A_NU_N)|\ge
c_*:=1.1\mathsf B-.9|\mathsf A|
\ge1.1+\frac{135273}{20}v>1.1.                    \tag{3}
$$

Equations (1)--(3), including the one-step common-phase versus coordinate-phase
gap, are now proved directly by the finite-grid argument. The older sector
derivation remains a separately preserved proof route. Finite checks alone
are not the reason for this status change.

## Exact projection identity, with arbitrary multiplicities

For any unitary $U$, let $P_\lambda$ be the spectral projectors indexed by
distinct eigenvalues and put

$$
Q=\mathcal E_U(A)=\sum_\lambda P_\lambda AP_\lambda.
$$

On matrix Hilbert space, $\mathcal E_U$ is the orthogonal projection onto
$\ker(I-\operatorname{Ad}_U)$. The range of $I-\operatorname{Ad}_U$
is its orthogonal complement, since $\operatorname{Ad}_U$ is unitary.
Consequently, without a simplicity assumption,

$$
\inf_B\|A-(B-UBU^*)\|_{\rm HS}=\|Q\|_{\rm HS},\qquad
\operatorname{Tr}(QU)=\operatorname{Tr}(AU),\qquad
\|Q\|_{\rm HS}\ge\frac{|\operatorname{Tr}(AU)|}{\sqrt N}. \tag{4}
$$

The last inequality is Hilbert--Schmidt Cauchy--Schwarz and $\|U\|_{\rm HS}=\sqrt N$.
For the present model $\operatorname{Tr}A_N=0$ for $N>18$; subtracting
any scalar cannot reduce the trace-free projection norm in (4).
Using (2),

$$
\liminf N\inf_B
\frac{\|A_N-(B-U_NBU_N^*)\|_{\rm HS}}{\sqrt N}\ge c_*.
                                                               \tag{5}
$$

## Two copies

On matrix space write $\mathcal U=\operatorname{Ad}_U$ and
$\mathcal A=\operatorname{ad}_A$. Cesàro averaging shows that the
orthogonal projection of $\mathcal A$ onto the commutant of $\mathcal U$
is exactly $\operatorname{ad}_Q$. This handles coincidences of
eigenvalue ratios as well as eigenvalue multiplicities: conjugating
$\operatorname{ad}_A$ by $\mathcal U^j$ gives
$\operatorname{ad}_{U^jAU^{-j}}$, whose average is $\operatorname{ad}_Q$.
For Hermitian $Q$,

$$
\|\operatorname{ad}_Q\|_{\rm HS}^2
=2N\|Q\|_{\rm HS}^2-2(\operatorname{Tr}Q)^2.         \tag{6}
$$

Indeed in a $Q$ eigenbasis the superoperator eigenvalues are $q_a-q_b$;
summing their squares proves (6). Thus (3) gives

$$
\liminf\inf_{\mathcal B}
\frac{\|N\mathcal A-(\mathcal B-\mathcal U\mathcal B\mathcal U^*)\|_{\rm HS}}N
\ge\sqrt2c_*.
$$

These are obstructions to removing a generator by a quantum coboundary.
They are not lower bounds on the fixed-coupling microscopic pair defect.
