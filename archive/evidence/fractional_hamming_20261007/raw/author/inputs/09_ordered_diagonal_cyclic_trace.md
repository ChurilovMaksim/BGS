# Centered ordered-diagonal cyclic trace

Independently accepted supporting companion to BGS-TRACE-020, 6 October 2026. This enlarges the accepted collective hierarchy. It is an exact actual-U replica statement, without any independent phase average of the quantizer. No claim about the full balanced projector follows.

## O1. Space and projectors

Let W=(C^N)^{tensor m}, E=End(W), with ordinary unnormalized Hilbert–Schmidt inner product. Write C_U=Ad(U^{tensor m}), R=Ad(C_m), where C_m is a single m-cycle on slots. Thus Tr_E(R C_U)=|Tr U^m|^2 (either orientation of the slot cycle gives the same identity). Let P_H be the orthogonal Haar-invariant projector. Let D be the full ordered diagonal algebra, with inclusion i:D→E, and let D_c=D minus its scalar identity. Define Y=(I-P_H)i|D_c and P_ord as the orthogonal projector onto its range. The actual dimension is N^m−1, as injectivity is proved below. P_ord is not asserted to commute with C_U.

Take the unit local identity I/sqrt(N) and the traceless diagonal space D_0. There is an orthogonal decomposition D=direct sum_S D_S, where S runs over slot subsets and D_S has traceless factors precisely in S. Global Haar conjugation preserves the corresponding exact traceless-support subspaces of E: the conjugated identity remains identity and each conjugated traceless factor remains traceless. Consequently H=i*P_H i and B=i*C_U i preserve every S. On S of size q they equal H_q=E_Haar T_V^{tensor q} and B_q=T_U^{tensor q}, where T_U=P_U−J restricted to D_0. Here P_U(a,b)=|U_ab|^2 and J_ab=1/N. The normalized identity factors introduce no extra powers of N.

## O2. Gram inverse and cyclic trace

H_q is positive because it compresses P_H. H_1=0. The accepted Haar fourth-moment argument, on the full ordered tensor space before any symmetrization, gives ||H_q||≤1/(N+1) for q≥2. Indeed E(T_V*T_V)=E(T_V T_V*)=I/(N+1), ||T_V||≤1; factoring two distinct tensor legs and applying Cauchy–Schwarz proves the bound. Thus G=Y*Y=I−H is invertible on D_c for all N≥2, all m≥1. Also C_U P_H=P_H C_U=P_H, so Y*C_U Y=B−H. The exact range projector is Y G^−1 Y*, and RY=Y r, where r is the slot cycle on D_c. Therefore

 Tr_E(R P_ord C_U)=Tr_Dc[r G^−1(B−H)].                         (O1)

The operators G^−1 and B−H preserve each S, while r takes S to C_m S. A single m-cycle fixes no subset except the empty and full subsets. The empty subset was removed in D_c. All proper nonempty subsets therefore make zero contribution to O1, regardless of their shorter subset orbits. Only q=m remains:

 s_ord(m,U)=Tr_(D0^tensor m)[r (I−H_m)^−1(T_U^tensor m−H_m)].   (O2)

The trace formula uses the two-sided cyclic action; replacing it by a one-sided cycle on W would not justify O1.

## O3. Exact low-dimensional Neumann identity

For independent Haar V_1,V_2,... put T_j=P_Vj−J on D_0, and d=N−1. The Neumann series converges in operator norm. For any d-dimensional matrix A,

 Tr_(D0^tensor m)(r A^tensor m)=Tr_D0 A^m.

Also H_m^k=E[(T_1...T_k)^tensor m]. Hence, with the empty product equal to I,

 s_ord(m,U)
 =sum_(k≥0) E Tr[(T_1...T_k T_U)^m]
  −sum_(k≥1) E Tr[(T_1...T_k)^m].                            (O3)

For m=1, H_1=0; equivalently each k≥1 expectation vanishes by independence and E T_j=0. Formula O3 is exact for every N≥2,m≥1 and every unitary U. All traces and products are on D_0, and no division by d or replica dimension occurs.

For the fixed-N failure control N=2, D_0 is one-dimensional. Writing t=T_U, H_m=0 for odd m and H_m=1/(m+1) for even m. Thus s_ord=t^m for odd m, and s_ord=((m+1)t^m−1)/m for even m. At fixed N=2 and |t|<1 the even-m contribution is asymptotic to −1/m, not exponentially small in m. This agrees exactly with O3 and shows why the large-N quantifier below is essential.

## O4. Exponential bound at Heisenberg scale

Set a_m=E||T_V||^m. It is strictly less than one for each N≥2,m≥1: Haar matrices have strictly positive entries in P_V almost surely, whence the stochastic contraction on D_0 is strict almost surely. Thus the two scalar series in O3 converge absolutely, since independent factors give

 |E Tr[(T_1...T_k T_U)^m]|≤d a_m^k ||T_U||^m,
 |E Tr[(T_1...T_k)^m]|≤d a_m^k.

In particular

 |s_ord(m,U)|≤d (||T_U||^m+a_m)/(1−a_m).                    (O4)

For N≥20 the accepted explicit Haar-row tail gives, with rho=sqrt(159/160),

 a_m≤rho^m+4N^2 exp(−N/160).                               (O5)

For the actual fixed-tau U_N, inherited FM-021 gives ||T_U_N||≤1/2 eventually. For any fixed a>0, uniformly over every integer m≥aN (there is no upper-band restriction in O4–O5), define c_a=min{a log 2,−a log rho,1/160}>0. For sufficiently large N the denominator in O4 is at least 1/2, and

 |s_ord(m,U_N)|≤12 N^3 exp(−c_a N).                         (O6)

Thus on any compact Heisenberg band [a,b], the N^−2 weighted sum is exponentially small, retaining its original origin-average convention. This strengthens only the removal of a specified replica subspace. It is consistent with an O(1) collective contribution: the orthogonal complement of the collective subspace inside this ordered sector has a nontrivial cycle action and can cancel it.

## O5. Exact remainder and its boundary

The raw ordered diagonal space is balanced. P_H also lies in the balanced range Π. Hence P_H P_ord=0 and P_H+P_ord≤Π. All these projectors commute with R. Therefore

 |Tr U_N^m|^2=min(m,N)+s_ord(m,U_N)+Tr[R Q_ord C_U],
 Q_ord=I−P_H−P_ord=(Π−P_H−P_ord)+(I−Π).                    (O7)

This is an orthogonal decomposition, without any commutation with C_U. It leaves both the remaining balanced range and the off-charge range. Cycle-fixed residual vectors can remain; m=1 off-diagonal traceless matrices are a direct example. No equivalence with stationary-path masks is asserted. The plateau, the remaining unnormalized signed sum, and TRACE-005 remain open.

## Distinct bounds and review scope

The full ordered-diagonal and collective subspaces have different projectors
and cycle cancellations. The ordered exponential bound does not imply the
collective O(1) bound. O6 is exponential in N uniformly for m>=aN, not
exponential in m at fixed N. The remaining balanced and off-charge Q_ord
trace is unestimated. This companion inherits only FM-021 singular mixing,
not its separate flatness estimate. [The independent review](../record/ordered_diagonal_review.md)
retains the failed first resource cap separately from successful bounded checks.
