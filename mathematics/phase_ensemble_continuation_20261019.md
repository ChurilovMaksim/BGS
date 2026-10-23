# Circular-phase ensembles: feedback, trace laws and signed clusters

19 October 2026. Author proofs and self-review, with preserved exact computations where stated. This file adopts the explicitly linked proof revisions below. It does not independently recertify the earlier corpus, establish priority, or prove the fixed-strength BGS claim.

The [integration record](../archive/record/chat_integration_20261019.md) distinguishes maintained conclusions, conditional inputs, finite observations and unsuccessful routes. The [complete source inventory](../archive/record/chat_integration_20261019_inventory.json) binds every imported file by SHA-256. Execution-era statements that the repository was unchanged describe those historical runs, before this integration.

## Models and the unchanged target

The general feedback problem starts with a deterministic unitary matrix with

$$
\max_{ij}|S_{ij}|^2\le C_0/N,\qquad
\|\,|S|^2-J\|\le1/100,
$$

and the separate stated reversal-channel hypothesis when needed. Coordinates are eliminated at random with fresh independent uniform phases. Results about this auxiliary process do not identify the microscopic spectrum of a fixed deterministic propagator.

The exact trace and cluster calculations use a more specific family. For an odd prime $p$, $d\ge1$, $N=p^{2d}$ and a nondegenerate alternating form $\Omega$ on $\mathbb F_p^{2d}$, set

$$
S_{xy}=N^{-1/2}e^{2\pi i\Omega(x,y)/p},\qquad U=DS,
$$

with independent uniform diagonal phases. Here $S=S^*$, $S^2=I$, $|S|^2=J$ and the reversal matrix has norm $N^{-1/2}$. These identities do not compare this family with the maintained frozen map $e^{i10^{-80}NA_N}M_N$. BGS-TRACE-005 and BGS-BGS-001 remain open.

## BGS-TRACE-095: dimension-uniform feedback limit

**Conditional author proof.** Under the exact trajectory, covariance and moment inputs pinned in the source, the Gaussian limit of every fixed selected block extends to every

$$
u_N\longrightarrow\infty,\qquad u_N/N\longrightarrow0.
$$

The complete principal block uses the source's additional reversal hypothesis. For the stated smooth bounded tests of disjoint entries, the error is of order $(u_N/N)^{1/4}+u_N^{-1/8}$. The stopping estimates count the current retained dimension rather than taking a union over all initial labels. This does not permit setting $u=2$.

Adopted proof and pinned hypotheses: [dimension-uniform feedback](../archive/evidence/executions/20261019/chat-research/bgs_focus_20261017/dimension_uniform_feedback.md), with [the original covariance proof](../archive/evidence/executions/20261019/chat-research/bgs_focus_20261016/deep_feedback_gaussian.md). The conditional review is [explicit](../archive/evidence/executions/20261019/chat-research/bgs_focus_20261017/self_review.md). This integration preserves that conditional status.

## BGS-TRACE-096: transmission and bounded eigenvector ratios

**Exact finite identities and an equivalence criterion.** For any deterministic unitary $S$, independent row phases and its open-port vector $X_i$, spectral averaging identifies the law of $X_i$ with the eigenvector-ratio law weighted by $|\psi_l(i)|^2$. If a two-port cavity has transmission $T$, closing the other port with a fresh uniform phase gives

$$
J=\frac{T}{|1-\sqrt{1-T}\,e^{i\phi}|^2},\qquad
Y=\frac{J}{1+J},\qquad
\mathbb E\left[\frac{J}{\lambda+J}\mid T\right]
=\frac{\sqrt T}{\sqrt{4\lambda+(1-\lambda)^2T}}.
$$

The resulting probability kernel is weakly continuous and injective. Consequently the transmission laws converge to Uniform$[0,1]$ if and only if the corresponding $Y$ laws converge to Beta$(1,2)$. This is not a proof of either convergence for the required deterministic startup.

Adopted full proof, endpoint conventions and prior scalar-delay attribution: [spectral averaging](../archive/evidence/executions/20261019/chat-research/bgs_focus_20261017/transmission_spectral_averaging.md). Only the successful v2 finite run has valid preserved input provenance. The original failed run has the explicit [ERR-031 disposition](../archive/record/chat_integration_20261019.md).

## BGS-TRACE-097: conditional positive Heisenberg path current

**Conditional on the stated fixed-level TV compactness TC.** The complete normalized positive path-clock current is controlled at arbitrary cutoffs $K_N\to\infty$. The adopted proof covers the noncommuting fixed-colligation tensor kernel and its infinite positive tail; it does not evaluate the finite-channel transmission law or the complete signed trace sum.

Exact hypotheses, normalization and conclusion: [uniform current theorem](../archive/evidence/executions/20261019/chat-research/bgs_continue_20261017/uniform_heisenberg_path_current.md) and [tensor kernel](../archive/evidence/executions/20261019/chat-research/bgs_continue_20261017/tensor_path_current_limit.md). TV compactness itself retains the full $G$ or rank condition $R$ specified in [its proof](../archive/evidence/executions/20261019/chat-research/bgs_review_20261017/fixed_channel_total_variation_compactness.md). None of these assumptions is silently discharged by a mesoscopic Gaussian block law.

## BGS-TRACE-098: fixed traces and secular coefficients

For the symplectic circular-phase family, let $t_m=\operatorname{Tr}U^m$. For each fixed $M$, jointly in distribution and all mixed moments,

$$
(t_1,t_2,t_3,\ldots,t_M)
\ \Rightarrow\ (Z,Z^2,\sqrt3Z_3,\ldots,\sqrt M Z_M),
$$

where the listed Gaussian variables are independent standard complex Gaussians. In particular $t_2=t_1^2$ exactly; the first two limiting traces are not independent CUE traces.

For total equal positive and negative length $L\ge1$, the mixed-moment error is at most

$$
\frac{L![1+\binom L2]}N.
$$

Unequal total lengths give zero exactly. The zero-rank permutation classes distinguish fixed points and transpositions from oriented cycles of length at least three. The same adopted source evaluates the secular hierarchy and states its whole-disk boundary.

Full proof, exact formulas and limitations: [secular and trace hierarchy](../archive/evidence/executions/20261019/chat-research/bgs_attempt_20261018/secular_hierarchy_ru.md). The [bilinear seed classification](../archive/evidence/executions/20261019/chat-research/bgs_attempt_20261018/bilinear_seed_classification_ru.md) is also preserved, with its complex Gauss factors retained. These results neither identify local spacings nor contradict a possible local Sine2 law.

## BGS-TRACE-099: polynomial trace windows

For the specified symplectic seeds, the signed mixed-moment comparison reaches trace powers $o(N^{1/5})$. For the generic fixed bilinear seeds of dimension $b$, the proved sufficient range is $o(N^{1/(6b)})$. Complex quadratic Gauss phases are retained in the latter case. The associated disk laws concern fixed compact subsets of $|z|<1$; they do not reach $z=e^{-s/N}$.

Adopted proofs: [symplectic window](../archive/evidence/executions/20261019/chat-research/bgs_boundary_20261018/polynomial_trace_window_ru.md) and [generic bilinear window](../archive/evidence/executions/20261019/chat-research/bgs_boundary_20261018/generic_bilinear_window_ru.md). Their [positive Gaussian comparison obstruction](../archive/evidence/executions/20261019/chat-research/bgs_boundary_20261018/gaussian_comparison_boundary_ru.md) explicitly prevents extending that positive bound to Heisenberg powers by the same argument.

## BGS-TRACE-100: exact signed expansion and low stable cancellations

Writing $V_m=\mathbb E|\operatorname{Tr}U^m|^2$, the exact phase average is a finite sum over cycle covers and set partitions. The original circular cumulants arise from

$$
\log\left(\sum_{n\ge0}\frac{x^n}{(n!)^2}\right)
=\sum_{n\ge1}a_n\frac{x^n}{n!},\qquad
a_1=1,\quad a_2=-\tfrac12,\quad a_3=\tfrac23,\quad a_4=-\tfrac{11}8.
$$

If $K=A_\sigma-A_\tau$, $H_\Pi$ is the block-incidence matrix of a partition and $c=m-|\Pi|$, each term has order

$$
N^{-h},\qquad h=c+\tfrac12\operatorname{rank}_{\mathbb F_p}(H_\Pi^{\mathsf T}KH_\Pi).
$$

The minimal core has size at most $8h$. Common-edge reconstruction and a complete rank-four finite enumeration prove

$$
V_m=m+O_m(N^{-3}),\qquad m\ge17,
$$

for every odd prime; the source gives the explicit factorial remainder. This remains a fixed-power conclusion.

Adopted proof chain: [exact formula](../archive/evidence/executions/20261019/chat-research/bgs_cancellation_20261018/signed_trace_formula_ru.md), [rank-two cancellation](../archive/evidence/executions/20261019/chat-research/bgs_cancellation_20261018/rank_two_cancellation_ru.md), [finite cores](../archive/evidence/executions/20261019/chat-research/bgs_cancellation_20261018/finite_core_expansion_ru.md), [rank-four enumeration and prime transfer](../archive/evidence/executions/20261019/chat-research/bgs_cancellation_20261018/second_order_cancellation_ru.md). [Taking every coefficient absolutely](../archive/evidence/executions/20261019/chat-research/bgs_cancellation_20261018/exact_absolute_barrier_ru.md) has a proved square-root-time obstruction.

## BGS-TRACE-101 to BGS-TRACE-103: finite schemes and their joint sum

The [neutral-peeling theorem](phase_neutral_primitives_20261019.md) proves that a connected cluster satisfies $j\le\delta+1$; after exact neutral cancellations a primitive has order at most $2\delta$ and size at most $16\delta$. This is finite at each fixed defect, without asserting a sum over all defects.

The [complete saturated-graph classification through rank six](phase_extremal_graphs_20261019.md) and exact open-channel enumeration close the missing connected $(j,\delta,e)=(3,2,4)$ kernel. Every one of its 24 channel polynomials is divisible by $1-z$ and is central in $S_4$. Its physical quotient at $z=1$ is $-191/12$.

The [complete second-defect theorem](phase_second_defect_20261019.md) resums every original order at **fixed total defect two**, for $0<\tau<1$, and yields $\deg_m b_h\le2h-3$ for $h\ge3$, $m>8h$. It does not prove $b_h=0$.

The [quartic cluster theorem](phase_quartic_cluster_sum_20261019.md) instead includes arbitrary numbers of all connected clusters of **individual defect one or two**, with all neutral additions and unbounded total defect. For $0<\tau<1/9$ its correction to $V_m/m$ converges to

$$
L_{\le2}(\tau)=\int_0^1\left[
e^{w_x+v(x)w_x^2}\frac{\tau}{w_xD_x}-1\right]dx,
$$

where

$$
\tau=w_x+w_x^2+\frac{q_3(x)}2w_x^3+\frac{q_4(x)}6w_x^4,
\quad D_x=1+2w_x+\tfrac32q_3(x)w_x^2+\tfrac23q_4(x)w_x^3,
$$

$$
v=\tfrac7{12}+\tfrac53x,\quad
q_3=2+\tfrac32x+\tfrac12x^2,\quad
q_4=6+\tfrac{25}2x+\tfrac{19}2x^2+2x^3.
$$

All five counting indices are controlled by one positive majorant. The tail is at most $11(9\tau_0)^{H+1}$ for $m/N\le\tau_0<1/9$, and the finite-size error is uniformly $O_{\tau_0}(N^{-1})$ for $9\le m\le\tau_0N$. The partial limit is

$$
L_{\le2}(\tau)=-3\tau^3+\frac{20893}{864}\tau^4+O(\tau^5).
$$

The earlier neutral, first-defect, maximal-primitive and second-defect contributions are included in this family; they must not be added a second time. Neither the wider $\tau<1$ fixed-defect result nor computability of the quartic integral extends the joint theorem's proved range.

## BGS-TRACE-104 and BGS-TRACE-105: Cauchy correspondence and positive sources

The [Cayley comparison](phase_cayley_cauchy_transfer_20261019.md) matches local factorial correlation tests for the iid phase ensemble of a Hermitian involution with those of $S-\operatorname{diag}(\mathrm{Cauchy})$, with error $O(N^{-1})$ at each fixed order. Universality of that particular dense deterministic hopping model remains a separate obligation.

The [positive-source theorem](cauchy_positive_source_boundary_20261019.md) proves exactly, for any finite Hermitian $B$, real $E$ and $A\ge0$, the Cauchy law of $\operatorname{Tr}(A(B-T-E)^{-1})$. For every non-diagonal Hermitian involution it proves positive-projection self-duality of H inverse and H/2, despite total variation distance one between their full matrix laws. This applies to the exact symplectic Fourier family in every dimension. The derivation uses classical bounded holomorphic Cauchy averaging, not a new universality theorem. The counterexample does not meet the original frozen-model hypotheses and does not refute BGS.

## Other adopted results and retained limits

The complete imported corpus also preserves:

- [Classical absorption for every remaining set](../archive/evidence/executions/20261019/chat-research/bgs_review_20261017/classical_compression_all_sizes.md), a classical estimate with no equality to a quantum phase average.
- [Positive Bernstein approximation of the full transmission law](../archive/evidence/executions/20261019/chat-research/bgs_review_20261017/positive_bernstein_path_law.md), with the separate conditional beta-smoothing statement and uncomputed limiting masses.
- [Clock and moment-window reconstruction](../archive/evidence/executions/20261019/chat-research/bgs_review_20261017/positive_clock_and_moment_window.md), credited to the supplied attachment where already present.
- [Rare-circuit Heisenberg obstruction](../archive/evidence/executions/20261019/chat-research/bgs_continue_20261017/rare_star_heisenberg.md) and [high-power comparison obstruction](../archive/evidence/executions/20261019/chat-research/bgs_focus_20261017/high_power_moment_barrier.md), whose iid matrices need not be unitary.
- [Failed closure mechanisms](../archive/evidence/executions/20261019/chat-research/bgs_attempt_20261018/closure_audit_ru.md): commuting phase generators do not produce unitary invariance, and all-order strong-absorption asymptotics alone do not identify the zero-absorption law.

## Exact remaining obligations

The connected $(j,\delta,e)=(3,3,3)$ source has only a direct prefix through size nine in the current run. Its full value is not known. A general open-channel cancellation starting with $(4,3,5)$, a uniform sum over all remaining connected types, the full signed mixed hierarchy, and transfer to the unchanged frozen model remain open. The missing source is not assigned the value 3 by fitting to CUE.
