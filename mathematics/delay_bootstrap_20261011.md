# Random Schur elimination: a joint-delay bootstrap from entry flatness

**Stable claim:** BGS-TRACE-060. **State:** CONDITIONAL.
**Boundary:** This preceding proof gives the conditional joint barriers and killed second/third upper bounds at its displayed cutoffs. The [reviewed all-fixed-moment extension](all_moment_delay_bootstrap_20261011.md) improves the cutoff to ceil(log(2N)^(1+kappa)), bounds all fixed killed moments, and proves uniform second/third equality laws. The [fourth-delay continuation](fourth_delay_law_20261011.md) proves the diagonal-square and fourth trace laws. The later [all-fixed-order equality proof](conditional_clock_universality_20261011.md) closes that induction and identifies the full-depth clock measure. The probability of all-time flatness, growing-order/edge bounds, unrestricted exceptional-event moments and BGS remain open.
**Integration and review:** [11 October disposition](../archive/record/chat_integration_20261011.md).
**Original input:** [dated source](../evidence/executions/20261011/chat-research/original/delay_bootstrap.md).


Working derivation, 8 October 2026.  Base mathematical context: BGS main 8d750e360254c2a9ec4d318d0f39751ce3b0c207. This is a subsidiary theorem with independent internal reconstruction, not microscopic universality. External priority is not established.

## Exact process and claim

Let F_N(z)=z U_N, U_N deterministic unitary. At size u choose one remaining coordinate e uniformly, independently of the past, and reveal its independent uniform phase w. Eliminate that port by scalar unitary feedback. At z=1 put S_u=F_u(1), T_u=-i S_u^* d_theta F_u(e^{i theta})|_0, and Q_u=S_u T_u S_u^*. Initially T_N=Q_N=I. One-step feedback preserves unitarity and positivity, and T_u>=I. Phases already revealed are reused; the next phase is independent of the past.

Set ell=log(2N), m=ceil(ell^20), epsilon=1/ell, B=ell^6. Assume N sufficiently large, m<N. Define the entry-flat event A: max_ij |(S_u)_ij|^2 <= K ell/u for every N>=u>=m, for a fixed K. No probability estimate for A is assumed proved here.

Claim: P(A intersect {some u>=m has max_i |u(T_u)_ii/N-1|>epsilon or max_i |u(Q_u)_ii/N-1|>epsilon or u Tr(T_u^2)/N^2>B}) <= C_K ell^-5.

Consequently, if P(A^c)<=p_N, the full joint delay barrier fails with probability at most p_N+C_K ell^-5. Let tau be the first failure of any of these three barriers, including flatness. Kill Y_u=u Tr(T_u^2)/N^2 at tau, retaining the exit state only in the separate frozen quadratic-moment process. Then E[1_{alive at u} Y_u] <= c_N := max(1,2(1+epsilon)^2/(1-K ell/m)) = 2+O_K(ell^-1). Strict/non-strict stopping conventions must be kept consistent at a crossing.

## One-step algebra

Order the eliminated coordinate first and write

S=[[a,b],[c,D]], T=[[t,h*],[h,H]], Q=S T S*, d=1-|a|^2>0,
q=w/(1-aw), K_w=[q b; I].

The feedback boundary matrix is S'=D+c q b. Its incoming delay is

T'=K_w^* T K_w=H+q h b+conj(q)b* h*+t|q|^2 b*b.

The outgoing delay has the symmetric representation

Q'=J_w^* Q J_w, J_w=[conj(q)c*;I].

Indeed S K_w=[b/(1-aw);S'], and b S'^*=((conj(w)-a)/(1-conj(a)conj(w)))c*, so S K_w S'^*=J_w. The chain rule for constant phase feedback gives the stated delay congruence. It can also be obtained by differentiating the feedback formula and using S* S=I.

The exact phase integrals are

E q=E q^2=0,
E|q|^2=1/d,
E[q|q|^2]=conj(a)/d^2,
E|q|^4=(1+|a|^2)/d^3.

Use geometric series; all converge absolutely when |a|<1. Thus

E_w Tr T'=Tr T,
E_w Tr(T'^2)=Tr(T^2)+2 T_ee Q_ee/(1-|S_ee|^2).                 (1)

For a retained j,
E_w (T')_jj=T_jj+T_ee |S_ej|^2/d,
E_w (Q')_jj=Q_jj+Q_ee |S_je|^2/d.                           (2)

To verify (1), expand the square of T'. The difference from Tr(T^2) is
2t/d [b H b*+2 Re(conj(a) b h)+|a|^2 t]=2t Q_ee/d.
All cross terms are retained; neither T nor S is replaced by a diagonal or independent surrogate.

## Joint stopping and the quadratic clock

Stop on the first entry-flatness, incoming/outgoing diagonal, or Y-cap exit. Before a transition from u, t_e,Q_ee <= (1+epsilon)N/u, d>=1-K ell/u. By (1),

E[Tr(T_{u-1}^2)-Tr(T_u^2)|past] <= c_N N^2/u^2.

For the killed quantity, dropping the nonnegative exit contribution gives

E[Y_{u-1}^{kill}|past] <= (1-1/u)Y_u^{kill}+c_N/u.

Induction from Y_N=1 gives E Y_u^{kill}<=c_N. This step does not use a probability bound for the stop.

For maximal control, freeze Z=Tr(T^2) at the complete crossing state. The frozen Z is a nonnegative submartingale: before stopping its exact conditional increment is positive by (1), and afterward it is zero. Its expectation down to size v is <=N+c_N N^2 sum_{u=v+1}^N u^-2 <=C N^2/v.

In a dyadic size block u in [v/2,v], a first Y>B exit implies Z>B N^2/v. Doob's nonnegative-submartingale inequality, including the crossing state, bounds this event by C/B. A union over O(log N) dyadic blocks gives C ell/B=C ell^-5. Stops caused by either other barrier are frozen too. This establishes the Y-cap exit estimate without presupposing diagonal concentration after the stop.

## Diagonal martingales on a fixed set of labels

Track x_j=u T_jj/N while label j remains present. When j is eliminated, freeze its last value. After the joint stopping time, freeze every coordinate. Do the same with outgoing variables y_j=u Q_jj/N. This embeds each process into R^N with no changing-dimensional martingale convention.

For a live j, averaging over a uniform e among all u labels, and setting the increment to zero when e=j, equation (2) gives

E[Delta x_j|past] = kappa_u[-x_j+sum_{e!=j} c_ej x_e],
kappa_u=(u-1)/u^2, c_ej=|S_ej|^2/(1-|S_ee|^2).             (3)

For outgoing variables replace |S_ej|^2 by |S_je|^2. Both coefficients are nonnegative. Bistochasticity gives

|sum_{e!=j}c_ej-1| <= 2 delta_u, delta_u=K ell/u

when delta_u<=1/2. Hence, for the centered vector z=x-1,

Delta z=A_u z+b_u+xi_u,
||A_u||_{infty->infty}<=C/u,
I+A_u entrywise nonnegative,
||I+A_u||_{infty->infty}<=1+C delta_u/u,
||b_u||_infty<=C delta_u/u, E[xi_u|past]=0.                 (4)

Rows of removed or globally frozen labels are zero in A_u,b_u and xi_u. The same inequalities hold for the outgoing process. Future-dependent propagators will not be used inside a martingale inequality.

## Predictable variance and jump bounds

For e!=j, before the stop,

Delta x_j=-x_j/u+(u-1)/N [2 Re(q T_je S_ej)+T_ee |q|^2 |S_ej|^2].

Here |q|<=2 eventually. Positivity implies |T_je|^2<=T_jj T_ee and
(T^2)_jj<=||T|| T_jj<=2 N^2 sqrt(B)/u^(3/2).
Averaging over e and phase and using sum_e |S_ej|^2=1 yields

|xi_{u,j}|<=C sqrt(delta_u),
E[xi_{u,j}^2|past]<=C[1/u^2+u delta_u (T^2)_jj/N^2+delta_u/u]
 <=C_K ell sqrt(B)/u^(3/2).                              (5)

The input/outgoing covariance need not vanish; scalar martingale bounds and a union bound suffice. For Q, positivity and Tr Q^2=Tr T^2 give precisely the same estimates.

## Dyadic concentration without an N/m Gronwall loss

On a block u in [v/2,v], each centered martingale has predictable variance <=C_K ell^4/sqrt(v) and jumps <=C_K sqrt(ell/v). Freedman's maximal inequality with a_v=ell^3 v^-1/4 gives failure probability <=2 exp(-c_K ell^2). Union over 2N labels and O(log N) blocks remains <=exp(-c'_K ell^2) for sufficiently large N.

On the complementary event, every raw martingale oscillation within its block is <=a_v. Apply (4) pathwise. If M denotes that block's martingale partial sum, put z_t=M_t+r_t. Then
r_{t+1}=(I+A_t)r_t+A_t M_t+b_t.
The sum of ||A_t|| over one dyadic block is bounded by a constant, while the product of the homogeneous infinity norms over the entire trajectory is <=exp(C sum delta_u/u)<=exp(C_K ell/m). Thus the block noise cost is at most a fixed constant times a_v, not a factor N/m.

Summing dyadic blocks, including every intermediate time,

sup ||z_u||_infty <= C_K[sum_v a_v+ell/m]
 <=C_K[ell^3 m^-1/4+ell/m]=O_K(ell^-2)<epsilon.             (6)

Both diagonal processes start at 1. Their first epsilon exit (including an exit simultaneous with the Y cap) therefore lies in the exceptional martingale event. Together with the Y-cap and possible flatness exits this proves the claim.

## Scope and unresolved steps

This supplies joint delay barriers and a killed moment FROM an all-time entry-flatness hypothesis. It has not proved that all-time entry flatness from the original U_N hypotheses, the scalar cavity law, source-prefix covariance, analytic physical-source continuation, or deterministic/high-order BGS. No numerical run verifies the asymptotic theorem. Source novelty and correspondence to unpublished raw proofs remain unverified.

## Exact third-moment identity and a stopped cubic bound

There is a useful rank-two form of the feedback congruence. Put e for the eliminated coordinate unit vector and v=S*e. Then

K_w K_w*=I+q e v*+conj(q) v e*.

The upper-left identity is d|q|^2-1=2 Re(aq). Consequently the cubic expansion has only quadratic and cubic mixed phase contributions. With t=T_ee, s=Q_ee, gamma=(S T)_ee,

E_w Tr(T'^3)=Tr(T^3)
 +3/d [t (Q^2)_ee+s (T^2)_ee]
 +6ts Re(conj(a)gamma)/d^2.                              (7)

No entrywise-commutation assumption is used. The linear term averages to zero. The three cyclic words containing two q factors and one conjugate q each have trace ts gamma; their conjugates supply the real part. The two quadratic orientations give the displayed T^2 and Q^2 terms.

On the same pre-exit event, t,s<=(1+epsilon)N/u and |gamma|<=sqrt(ts) by positivity. Set delta_*=K ell/m, A0=1+epsilon and c_N=2 A0^2/(1-delta_*). For Z_u=u^2 Tr(T_u^3)/N^3, killed at the same stop,

E Z_{u-1}^{kill} <= ((u-1)/u)^2 E Z_u^{kill}
 +6 A0/(1-delta_*) (u-1)^2/u^3 E Y_u^{kill}
 +6 A0^3 sqrt(delta_*)/(1-delta_*)^2 (u-1)^2/u^3.

Since (u-1)^2/[u(2u-1)]<=1/2 and E Y_u^{kill}<=c_N, induction gives

E Z_u^{kill} <= max(1,
 3 A0 c_N/(1-delta_*)+3 A0^3 sqrt(delta_*)/(1-delta_*)^2)
 =6+O_K(ell^-1).                                       (8)

This is a killed expected cubic upper bound. It is not an unrestricted expectation, a concentration law, or a proof of the proposed exact polynomial 6-6u/N+(u/N)^2. It does not justify inserting a noninvariant stopping event into a circle-integrated jet inequality.


## General depth theorem and the improved logarithmic endpoint

Fix a>0, b>1 and eta>0. Replace epsilon by ell^-a, B by ell^b, and assume m>=ell^(4+4a+b+eta), m<N. The same argument proves

P(A intersect any delay-barrier failure) <= C_K ell^(1-b)+exp(-c ell^(1+eta/2)).

The constants and sufficiently-large-N threshold may depend on the fixed parameters. In each dyadic block use h_v=c epsilon (m/v)^(1/4), with c small enough that the sum of pathwise block costs is <epsilon/2. Now V_v<=C_K ell^(1+b/2)/sqrt(v). The ratio h_v^2/V_v is at least c' epsilon^2 sqrt(m)/ell^(1+b/2)>=c' ell^(1+eta/2). The bounded-jump contribution is smaller: J_v h_v/V_bound<=C_K c epsilon ell^(-(1+b)/2). The union over N times logarithmically many blocks still decays on the displayed exponential scale. The deterministic drift ell/m=o(epsilon). The quadratic-cap probability is O(ell/B).

For every fixed kappa>0 choose a=kappa/16, b=1+kappa/4, eta=kappa/2. Then

m=ceil(ell^(5+kappa)), epsilon=ell^(-kappa/16),
additional delay-failure probability O_K,kappa(ell^(-kappa/4)),
(epsilon+additional failure probability) log(2+m) ->0.

The killed second and third moments are bounded by 2+o(1) and 6+o(1), respectively, at every planned retained size. These upper bounds follow from the displayed explicit induction constants; they are not asserted limits or sharp constants for this stochastic process. Any all-time-flatness failure probability must still be added.

## Independent review and finite checks

A separate internal reviewer reconstructed the one-step formulas, both stopping arguments, dyadic concentration, the cubic identity, and the parameter strengthening. No substantive error was identified. The reviewer required the explicit intersection-probability formulation, full crossing-state retention for frozen processes, and fresh phase/uniform-coordinate averages taken only conditional on the past. Those qualifications are part of this statement. This is internal review, not external refereeing or formal verification.

Python checked 32 noncommuting cases in dimensions 2,3,5,9, with 4096-point phase quadrature. Maximum relative discrepancies were 6.2e-16 for the square identity and 9.4e-16 for the cube identity. Independent differentiation of the feedback curve and the outgoing congruence had maximum absolute error 1.6e-9. These are floating controls.

An independent C++20 implementation checked all three polynomial trace identities in 40 Gaussian-rational cases, dimensions 2 through 6. Its checked signed 128-bit rational arithmetic aborts on overflow; the final stated case set passed exactly. An initial Boost-based build was unavailable, and a larger intermediate case set exceeded the checked integer range; neither is counted as a passing run. No asymptotic probability statement is certified by these finite checks. Lean is not available in this current runtime, and the new analytic proof has not been formalized.

## The concentration inequality used

The only concentration theorem used is scalar Freedman, as stated in Joel A. Tropp, “Freedman's inequality for matrix martingales,” Electronic Communications in Probability 16 (2011), 262–270, Theorem 1.1, p. 263, https://tropp.caltech.edu/papers/Tro11-Freedmans-Inequality.pdf (crediting Freedman 1975, Theorem 1.6). For real martingale differences bounded above by R and predictable quadratic variation W,

P(exists k: M_k≥t and W_k≤v)≤exp(−t²/[2(v+Rt/3)]).

Apply to both signs of each stopped real diagonal martingale. Its increments obey the deterministic pre-exit bounds (5), its crossing increment is included, and each block's variation is bounded by the displayed deterministic block sum. The resulting two-sided maximal bound is 2 times the exponential. No matrix martingale theorem is needed.

The nonnegative-submartingale maximal estimate used for the frozen square has a short direct proof: at the first crossing of level L, conditional submartingality implies that the terminal expectation restricted to that crossing event is at least L times its probability. Nonnegativity lets us bound the restricted terminal expectation by the full terminal expectation. Thus P(max Z≥L)≤E Z_terminal/L.
