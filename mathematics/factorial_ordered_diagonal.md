# Fixed-order factorial removal of the ordered-diagonal sector

Independently reviewed extension of BGS-TRACE-020, 6 October 2026. This is an exact projector-sector estimate for actual U_N under entrywise flatness. It is not a proof of the remaining joint traces or TRACE-005. The frozen long-cycle proof is unchanged.

## G1. Exact mixed projector interface

Fix N≥2 and M≥1. Work in E=End((C^N)^{tensor M}) with ordinary unnormalized Hilbert–Schmidt inner product. Let C_U=Ad(U^{tensor M}), P_H the full Haar-invariant projector, and i:D→E the inclusion of the ordered diagonal algebra. Put e=I/sqrt(N^M), P_0=|e><e|, H=i*P_H i, and H_c=H−P_0. Let P_ord be the orthogonal projector onto (I−P_H)i(e^perp).

For arbitrary slot permutations sigma,pi, let R(X)=C_sigma X C_pi*. R commutes with C_U and P_H but need not preserve the ordered-diagonal sector. Set B_R(U)=i*C_U R i and H_R=i*P_H R i. The accepted full-tensor Gram bound gives ||H_c||≤1/(N+1). Cyclicity and the Gram range projector give

 s_R(U):=Tr_E(R P_ord C_U)
       =Tr_D[(I−H_c)^−1(B_R(U)−H_R)].                       (G1)

The difference B_R(U)−H_R annihilates e on both sides, since R(I) and R*(I) are slot permutation matrices and hence Haar invariant. Thus the Neumann series can be written

 s_R(U)=sum_(j≥0) E[F_(Q_j)(U)−E_V F_(Q_j)(V)],            (G2)
 Q_j=P_(V1)...P_(Vj), Q_0=I,
 F_Q(U)=Tr_D[Q^{tensor M} B_R(U)].

Here V,V1,V2,... are independent Haar matrices, and P_U(a,b)=|U_ab|². This is first justified as the convergent H_c operator series; the bounds below prove absolute convergence after the indicated scalar subtraction. No separate convergent full-H series is asserted, and no R-invariance of P_ord is used.

## G2. Canonical cycles and cut network, including zero-length strings

Choose positive trace lengths p_1,...,p_r and negative trace lengths n_1,...,n_s, all positive integers with equal total M. Define sigma and pi to cycle the consecutive intervals of these respective lengths. This is a canonical replica presentation of the corresponding joint trace. It specifies the subspace whose sector is being removed; a different independent relabeling of ket and bra transports that subspace.

Let 0=e_0<e_1<...<e_h=M be the union of positive and negative interval endpoints. Thus h≤r+s. Chain j has start position e_(j−1)+1, end position e_j, and L_j=e_j−e_(j−1)−1≥0 common edges. The cut set contains an endpoint from every positive cycle, and therefore meets every common closed cycle; after deleting these edges every component is one of the listed open strings. There is no unlisted closed-loop index sum or extra factor of N. At cut position e_j, sigma and pi point to chain starts indexed by permutations alpha(j) and beta(j) of {1,...,h}. For any nonnegative doubly stochastic Q, define

 K=P_U Q,
 W_Q(a,c;b)=sum_x Q_(x,b) U_(a,x) conjugate(U_(c,x)).

Directly contracting the diagonal basis in G2 gives exactly

 F_Q(U)=sum_(a_1,...,a_h,b_1,...,b_h)
          product_(j=1)^h (K^{L_j})_(b_j,a_j)
                           W_Q(a_(alpha(j)),a_(beta(j));b_j).       (G3)

Every port value is allowed; there is no distinctness restriction. In particular L_j=0 means the exact Kronecker delta b_j=a_j, not a uniform link.

Suppose max_(a,b)|U_ab|²≤C/N, with C≥1. Then K and every positive power K^L have entries at most C/N, and Cauchy–Schwarz gives

 |W_Q(a,c;b)|≤sqrt(K_(a,b)K_(c,b))≤C/N.

If z of the L_j are zero, their deltas remove exactly z independent b sums. There remain 2h−z index sums and h+(h−z)=2h−z factors bounded by C/N. Hence

 |F_Q(U)|≤C^(2h−z)≤C^(2h),                               (G4)

uniformly in Q and every collection of cycle lengths. This accounts explicitly for adjacent cut edges and all zero-length matched strings.

## G3. The universal scalar and a length-uniform continuity bound

Let J_ab=1/N and Delta=Q−J. Since J^{tensor M}=P_0 on D,

 F_J(U)=<e,B_R(U)e>
       =N^−M Tr_W(C_sigma C_pi*)
       =N^(cycles(sigma pi^−1)−M).                       (G5)

This is independent of U. Equivalently, the cut network at J has W_J(a,c;b)=delta_(a,c)/N and evaluates to N^(cycles(alpha beta^−1)−h), including zero-length strings. G5 is the scalar canceled within each summand of G2.

For arbitrary unitary U, every nonzero-length link has

 ||K^L−J||≤||Delta|| for L≥1,

because K−J=(P_U−J)Delta, both factors are contractions, and K^L−J=(K−J)^L. Also

 |W_Q(a,c;b)−W_J(a,c;b)|≤||Delta||

by Cauchy–Schwarz on a column of Delta and the vector U_(a,x) conjugate(U_(c,x)), whose l2 norm is at most one. All individual link and cut factors have modulus at most one. Telescoping G3 over at most 2h factors, leaving zero-length deltas unchanged, gives the crude but length-uniform estimate

 |F_Q(U)−F_J(U)|≤2h N^(2h)||Q−J||.                       (G6)

No factor proportional to M occurs. Consequently the scalar difference in G2 is bounded by 4h N^(2h) E||Q_j−J||.

## G4. Independent Haar products give a fixed Neumann cutoff

On D_0, write T_V=P_V−J and d=N−1. The accepted exact Haar fourth-entry moments imply

 E(T_V*T_V)=I_d/(N+1),   ||T_V||≤1.

By conditioning successively on independent factors,

 E||T_1...T_j||_HS²=d/(N+1)^j,
 E||Q_j−J||≤sqrt(d)(N+1)^(-j/2).                          (G7)

For j=0 the second bound is still valid, though not sharp. Choose the integer cutoff L=4h+4. Combining G6–G7, the tail j≥L is at most

 4h N^(2h) sqrt(N−1) (N+1)^(-L/2)
                         /[1−(N+1)^(-1/2)]
 ≤C_h N^(-3/2).                                          (G8)

This bound does not use an unproved representation-uniform gap or replace the deterministic dynamics by a Markov process. The Haar products arise only from the exact Gram inverse.

## G5. Maximum-entry moments control the finite beginning

For Haar V let Y_N=N max_(a,b)|V_ab|²≥1. Each squared entry has the Beta(1,N−1) law: write a Haar column as a normalized independent complex Gaussian vector, and divide one exponential squared modulus by its sum with N−1 independent exponential variables. The resulting tail is (1−x)^(N−1) on 0≤x≤1. Thus for t≥0

 Pr(Y_N>t)≤min{1,N² exp(−t/2)}                            (G9)

(with zero probability once t≥N). Thus for each positive integer p,

 (E Y_N^p)^(1/p)≤4 log N+2(p!)^(1/p).                    (G10)

For example this follows by bounding (Y_N−4 log N)_+ by an exponential tail of rate 1/2 and applying Minkowski. Apply G4 with C=Y_N and p=2h. The first L terms of G2 are bounded by

 L [C^(2h)+(4 log N+2((2h)!)^(1/(2h)))^(2h)].              (G11)

Together G8 and G11 establish, for any flat unitary with N max|U_ab|²≤C,

 |s_R(U)|≤C_(h,C)(1+log N)^(2h),                         (G12)

uniformly over all positive cycle lengths, with no lower or upper length restriction. In particular this applies to the actual fixed-tau U_N using its accepted uniform entrywise flatness. A spectral gap for P_U is not needed for this weaker bound. The earlier exponential long-cycle result remains a separate strengthening.

## G6. Exact factorial normalization and zero-power hyperplanes

Fix factorial order k≥2 and a bounded compactly supported Fourier weight phihat on R^(k−1), with the project convention

 C_(k,N)=N^−k sum_(m in Z^(k−1)) phihat(m/N)
             sum_(partitions pi) mu(pi) product_(B in pi) Tr(U^(s_B)),
 m_k=−sum_(a<k)m_a,  s_B=sum_(a in B)m_a.

For each partition pi and each lattice point, extract all z zero block powers, each contributing N. If any nonzero powers remain, total zero implies at least one positive and one negative power. Present these canonically as in G2, and replace their joint trace by the exact decomposition

 Tr_E(R C_U)=Tr_E(R P_H)+s_R(U)
                        +Tr_E[R(I−P_H−P_ord)C_U].        (G13)

If all block powers vanish, set the ordered-diagonal contribution to zero: the product is the exact constant N^{|pi|}, so no positive replica degree is introduced.

On a stratum with exactly z zero block powers and some nonzero powers, the z linear equations s_B=0 are independent on the original zero-total frequency space. Indeed the disjoint block indicators are linearly independent modulo the total indicator unless all blocks are included. There are at least two omitted blocks in this stratum. Hence the compactly supported lattice has O_(k,phihat)(N^(k−1−z)) points. This remains an upper bound after imposing the nonzero conditions on other blocks. G12 has h≤number of nonzero blocks≤k. The N^z zero-trace factors therefore give

 N^−k N^z O(N^(k−1−z)) O((1+log N)^(2k))
                      =O((1+log N)^(2k)/N).             (G14)

There are only finitely many partitions and zero-block strata at fixed k, and their Mobius coefficients are fixed. Thus the complete ordered-diagonal-sector contribution to the compact-weight factorial Fourier expression is O_(k,phihat,C)((1+log N)^(2k)/N). Zero cycle powers, adjacent cuts, and short nonzero powers are all included.

## G7. Remaining obligation

G13 is an exact trace decomposition even though the mixed R need not commute with the residual projector. This result removes the specified ordered-diagonal sector from every fixed-order factorial trace presentation. It does not estimate the remaining projector term in G13, the full balanced occupation sum, or the off-charge defect. It preserves all repeated labels and prescribed common-origin averaging: no coordinate-phase average has been substituted for the original observable. The full TRACE-005 condition remains open.

## Review and remaining complement

The independent review and original source/replay hashes are mapped in
record/factorial_diagonal_promotion_mapping.json. The general theorem uses
entrywise flatness only; the exponential long-cycle companion additionally
uses its named singular-gap input. Their common ordered-sector projector
need not commute with a genuinely mixed two-sided permutation. The complete
signed factorial complement remains open; no BGS claim is made.
