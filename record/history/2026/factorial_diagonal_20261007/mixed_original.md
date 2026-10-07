# Ordered-diagonal interfaces for several and mismatched cycles

Author candidate, 6 October 2026. Depends on the accepted ordered-diagonal Gram construction and Haar tail. Fixed literal tau and actual U_N are unchanged. All traces below are ordinary unnormalized traces. This concerns one specified Haar-removed ordered-diagonal subspace in a chosen replica presentation, not the complete factorial observable.

## M1. General two-sided permutation interface

Let W=(C^N)^{tensor M}, E=End(W), C_U=Ad(U^{tensor M}), and let sigma,pi be arbitrary slot permutations. Define R_(sigma,pi)(X)=C_sigma X C_pi*. It commutes with C_U and P_H, because both slot permutation matrices commute with V^{tensor M} for every V. It need not preserve the ordered diagonal algebra or its Haar-removed image. Its full trace is the product of positive power traces indexed by sigma and conjugate power traces indexed by pi.

Let i:D→E include the full ordered diagonal algebra, let e=I/sqrt(N^M), and P_0=|e><e| on D. Put H=i*P_H i, H_c=H−P_0. On D_c=e^perp, the Gram G=I−H is invertible, with ||H_c||≤1/(N+1). This uses the exact traceless-support decomposition and the accepted two-leg fourth-moment bound on each nonempty support (the one-leg Haar compression is zero). Write Y=(I−P_H)i|D_c and P_ord=Y G^−1 Y*.

For B_R(U)=i*C_U R i and H_R=i*P_H R i, cyclicity gives the exact identity

 s_R(U):=Tr_E(R P_ord C_U)
       =Tr_Dc[G^−1 (B_R(U)−H_R)].                         (M1)

Indeed Y*C_U RY=i*(C_U R−P_H R)i. No R-invariance of P_ord was used. Both the column and row of B_R(U)−H_R in the direction e vanish: R(I)=C_sigma C_pi* and R*(I) are Haar invariant. Thus

 s_R(U)=sum_(k≥0) Tr_D[H^k(B_R(U)−H_R)].                   (M2)

This is justified first through H_c, whose Neumann series converges; H^k may replace H_c^k inside each trace because the scalar part annihilates the difference. One must not separate the two full-H series before finding their common scalar cancellation.

For independent Haar V_j, let Q_k=P_(V1)...P_(Vk), with Q_0=I. Since H=E P_V^{tensor M}, set

 F_Q(U)=Tr_D[Q^{tensor M} B_R(U)].

Then the exact series is

 s_R(U)=sum_(k≥0) E[F_(Q_k)(U)−E_V F_(Q_k)(V)],            (M3)

where the final Haar V is independent of Q_k. The bounds below justify absolute scalar summation in the specified cases. P_U has entries |U_ab|²; T_U=P_U−J acts on D_0, with d=N−1.

## M2. Matched several-cycle case

First choose sigma=pi with r cycles of lengths l_1,...,l_r. Here R is conjugation, so it intertwines Y with the slot permutation on D. Only nonempty supports that are unions of whole cycles contribute to the trace. For I a nonempty subset of {1,...,r}, put q_I=sum_(j in I) l_j. The contribution of that support is

 sum_(k≥0) E product_(j in I) Tr[(T_1...T_k T_U)^{l_j}]
 −sum_(k≥1) E product_(j in I) Tr[(T_1...T_k)^{l_j}].       (M4)

The same independent Haar matrices T_1,...,T_k appear in every factor; the traces are not independently averaged across cycles. If a_q=E_Haar||T_V||^q and t=||T_U||, the absolute value of this support contribution is at most

 d^{|I|}(t^{q_I}+a_(q_I))/(1−a_(q_I)).                    (M5)

Consequently for fixed r and all l_j≥aN, the accepted Haar tail and actual t≤1/2 eventually give exponential-in-N suppression, with a polynomial prefactor N^{r+2}. There is no upper-length restriction in this estimate. Equal cycle types can always be represented by this matched choice for the full observable, but independently relabeling ket and bra transports the chosen subspace: it does not prove the same assertion for the untransported standard diagonal subspace under arbitrary unequal permutations of the same cycle type.

## M3. First mixed pattern: two positive cycles, one negative cycle

Let M=l+r, sigma=(1...l)(l+1...M), and pi=(1...M), with l,r≥2. The ket and bra cycles differ at the two cut positions l,M. Let Q be any nonnegative doubly stochastic N×N matrix. Set

 K=P_U Q,   W_Q(a,c;b)=sum_x Q_(x,b) U_(a,x) conjugate(U_(c,x)).

With the permutation convention (C_sigma x)_i=x_(sigma^−1(i)), a direct diagonal-basis contraction gives

 F_Q(U)=sum_(a,c,b,d) (K^{l−1})_(b,a)(K^{r−1})_(d,c)
                          W_Q(a,c;b) W_Q(c,a;d).         (M6)

All four ports, including repeated ports, are retained. Common edges produce K; the two cut edges produce W_Q. This formula is valid for nonnormal Q and P_U. The bounds and identities needed below are

 sum_b W_Q(a,c;b)=delta_(a,c),
 W_Q(a,a;b)=K_(a,b),
 |W_Q(a,c;b)|≤sqrt(K_(a,b) K_(c,b))≤1.                    (M7)

The first uses the row sums of Q and orthogonality of distinct rows of U. Write T_K=K−J=T_U(Q−J). Expanding both long links as J+T_K^L gives the exact decomposition

 F_Q(U)=1/N + Tr(T_K^l)/N + Tr(T_K^r)/N + E_Q(U),          (M8)

where E_Q is M6 with both link matrices replaced by T_K^{l−1} and T_K^{r−1}. Hence

 |E_Q(U)|≤N^4 (||T_U|| ||Q−J||)^{M−2}.                   (M9)

The term 1/N is a repeated-port contribution, not an error. A uniform long link forces a=c; it does not make the unrestricted expression vanish. Thus applying a distinct-port marked-link lemma directly to M6 would omit a surviving contribution.

## M4. Haar subtraction cancels the repeated-port scalar

For Q_k as in M3, ||Q_k−J||≤product_(j≤k)||T_j|| (for k=0 the norm is one). The universal 1/N in M8 is identical for U and the independent final Haar V, so cancels inside every summand of M3. Independence now gives the explicit bound

 |s_R(U)| ≤ (d/N)[(t^l+a_l)/(1−a_l)+(t^r+a_r)/(1−a_r)]
                +N^4 (t^{M−2}+a_(M−2))/(1−a_(M−2)).     (M10)

All denominators are positive for N≥2 because a_q<1 for every q>0. This also proves absolute convergence of the scalar series after the exact common-term subtraction. No product of replica dimensions or number of occupation classes appears.

For the actual U_N, t≤1/2 eventually. For any fixed a>0 and l,r≥aN, take N large enough that aN≥2. Then l,r,M−2≥aN, and the accepted bound

 a_q≤rho^q+4N² exp(−N/160), rho=sqrt(159/160),

gives, with c_a=min{a log2,−a log rho,1/160},

 |s_R(U_N)|≤36 N^6 exp(−c_a N).                          (M11)

This is exponential in N, not uniformly exponential in m at fixed N. It has no upper-cycle-length restriction. A fixed compact Fourier support gives only polynomially many l,r values; therefore this sector remains negligible under any fixed polynomial Fourier normalization and bounded weights restricted to l,r≥aN.

## M5. Scope and exact unresolved remainder

The mixed interface did not replace R_(sigma,pi) by conjugation and did not assume it preserves P_ord. The exact decomposition is

 Tr_E(R C_U)=Tr_E(R P_H)+s_R(U)+Tr_E[R(I−P_H−P_ord) C_U].

P_H and P_ord are orthogonal projections. The final projector need not commute with this mixed R, and its remaining cyclic trace is unestimated. Thus M11 removes only the specified ordered-diagonal sector in this factorial replica presentation. It does not establish the full mixed factorial observable, and it does not cover frequency boundaries where one selected cycle length is o(N). The marked-link orthogonality in M7 is the same elementary unitary cancellation underlying FM-021, while the decisive extra interface here is the exact repeated-port 1/N term and its Haar-Gram subtraction in M8–M10.
