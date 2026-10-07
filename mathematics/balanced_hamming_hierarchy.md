# Exponentially negligible balanced coordinate-Hamming hierarchy

Author candidate, 7 October 2026. Base `157277eeca8d8318976ea26bdbb1d3b1aa0d438a`. No canonical changes. This extends the accepted ordered-diagonal cyclic argument to a genuinely larger centered balanced subspace; the complete balanced complement remains open.

## 1. Exact subspace and claim

Let N>=2, m>=1, W=(C^N)^tensor m, E=End(W) with unnormalized HS, R=Ad(C_m) for one full slot cycle, C_U=Ad(U^tensor m), P_H the full Haar-invariant projector and Pi the coordinate-occupation balanced projector. For 0<=r<=m define

 B_r=span{|x><y| : n(x)=n(y), #{j:x_j!=y_j}<=r},
 Y_r=(I-P_H)|_(B_r), and P_r=orthogonal projector onto ran Y_r.

These are exact spans, not a sum over decorated copies. They contain every repeated label and every changed-coordinate placement exactly once. P_0 is precisely the accepted ordered-diagonal projector P_ord. Since B_0 subset B_r subset ran Pi and ran P_H subset ran Pi,

 Q_r=P_r-P_0

is an orthogonal projector with Q_r <= Pi-P_H-P_ord. For r=2, B_r consists of the full ordered diagonal plus every single-swap coherence |x><y|, where y swaps two unequal entries of x. No separation of swap positions or distinctness of other labels is required.

Put D=N^2-1, T_V=P_V-J on the traceless diagonal space, t=||T_U||, and

 n=m-2r,
 L=L_(N,m,r)=sum_(s=0)^r binom(m,s) b_N(s),
 b_N(s)=#{((a_1,b_1),...,(a_s,b_s)): a_j!=b_j, sum_j(e_(a_j)-e_(b_j))=0}.

Here b_N(0)=1; in particular b_N(1)=0 and b_N(2)=N(N-1). Thus L is exact, with

 L <= sum_(s=0)^r binom(m,s)[N(N-1)]^s <= (r+1)(mN^2)^r.

Let a_n=E_(V Haar)||T_V||^n. Whenever n>=1 and L a_n<1, the exact centered Hamming trace satisfies

 |Tr_E(R P_r C_U)| <= D L (t^n+a_n)/(1-L a_n).                 (1)

This bound is uniform in U; it makes no probabilistic replacement of U.

For the actual fixed-tau U_N, use the accepted eventual t<=1/2 and, for N>=20,

 a_n <= rho^n+4N^2 exp(-N/160),  rho=sqrt(159/160).             (2)

Fix 0<a<=b<infinity and let gamma_a=min{a log(1/rho),1/160}. For every fixed

 0<kappa<gamma_a/3,  0<c<gamma_a-3kappa,

uniformly for integers aN<=m<=bN and 0<=r<=kappa N/log N, at sufficiently large odd N,

 |Tr_E(R P_r C_(U_N))| <= exp(-cN),
 |Tr_E(R Q_r C_(U_N))| <= exp(-cN).                           (3)

The second inequality may initially have a fixed factor two, absorbed by the strict slack in c. Every fixed r is included. A compact-weight N^-2 sum of either sector is exponentially small. The original tau, coordinate basis, raw symbol, origin average and odd-dimensional sequence are unchanged.

## 2. Exact local support removes all proper subsets

Write the local operator space as C e direct-sum V, where e=I/sqrt(N) and V is traceless. Inside V let D_0 be traceless diagonal and let E_ab, a!=b, be the orthonormal offdiagonal matrix units. The diagonal algebra is C e direct-sum D_0.

The raw projector onto B_r is a sum of tensor-product projections: choose the offdiagonal marker positions and their labels (a,b), require total charge zero, put the rank-one projector onto E_ab at each marker, and put the full diagonal projector elsewhere. Distinct choices give orthogonal ranges. This is exactly the occupation constraint; it has not been dropped or treated as independent local constraints.

Expanding each unmarked diagonal factor into C e plus D_0 shows that B_r preserves every exact traceless-support summand E_S. Global Haar conjugation and C_U preserve these same summands. Hence Y_r and its true range projector P_r preserve them as well. R carries E_S to E_(C_m S). In the trace of R P_r C_U every nonempty proper S vanishes because a full m-cycle fixes no such subset. The empty support is Haar invariant and is annihilated by Y_r. Thus only E_[m]=V^tensor m contributes.

On this top support, let K be the raw B_r projector. It has the explicit orthogonal expansion

 K=sum_(alpha in A) K_alpha,   |A|=L,
 K_alpha=tensor_(i=1)^m p_(alpha,i),                            (4)

where each p is either P_(D0) or one rank-one E_ab projector, at most r factors are rank one, and the marker labels have total charge zero. This gives the exact b_N(s) count above. K commutes with the full slot cycle.

## 3. Haar Gram conditioning

Set A_V=Ad(V)|_V. Every A_V is unitary, and P_(D0) A_V P_(D0), restricted to D_0, is exactly T_V. All other local projector compressions have norm at most one.

For any alpha,beta in A, their marker sets have union of size at most 2r. Therefore

 ||K_alpha A_V^tensor m K_beta|| <= ||T_V||^(m-2r).

Let H=K P_H K restricted to ran K. It is positive self-adjoint because P_H is an orthogonal projector. Its alpha,beta block has norm at most a_n. For a vector v=direct-sum_beta v_beta,

 ||(Hv)_alpha|| <= a_n sum_beta ||v_beta||,
 ||Hv||^2 <= L^2 a_n^2 sum_beta ||v_beta||^2.

Thus ||H||<=L a_n<1. In particular the top-support centered inclusion Y=(I-P_H)|_(ran K) is injective and has Gram G=I-H. Its true orthogonal range projector is Y G^-1 Y*. No normalization by frame size or replica dimension is used.

As R preserves K and commutes with P_H and C_U, the range-projector trace is exactly

 s_r=Tr_(ran K)[R (I-H)^-1(B-H)],
 B=K A_U^tensor m K restricted to ran K.                       (5)

The usual invariant identity C_U P_H=P_H gives B-H. Expanding only this convergent Gram inverse gives

 s_r=sum_(j>=0) [Tr(R H^j B)-Tr(R H^(j+1))].                  (6)

## 4. Cyclic tensor contraction, including the shifted seam

For j>=0, expand the j+1 K factors in Tr(R H^j B) using (4), and realize the j Haar factors as independent V_1,...,V_j. A summand is

 Tr_(V^tensor m){R tensor_(i=1)^m
   [p_(1,i) A_(V1) p_(2,i) A_(V2) ... p_(j+1,i) A_U]}.

For j=0 the bracket is simply p_(1,i) A_U. The standard full-cycle tensor trace identity turns this into one ordinary D-dimensional trace, joining the end at slot i to the beginning at the next slot in the orientation of the chosen cycle. Insert each adjacent projection twice, using p^2=p, to view the product as successive compressed transitions.

For Haar stage ell, the transition A_(Vell) has endpoints p_(ell,i),p_(ell+1,i). Across all m slots at most 2r endpoints involve markers. Hence at least n=m-2r of its occurrences have both endpoints P_(D0), each contributing a factor ||T_(Vell)|| in the norm bound. The final transition A_U joins p_(j+1,i) to p_(1,next(i)), not p_(1,i). Both marker sets have size at most r even after that cyclic shift, so it too has at least n diagonal-to-diagonal occurrences. Every other compressed transition has norm at most one.

Consequently the absolute value of this individual summand is at most

 D t^n product_(ell=1)^j ||T_(Vell)||^n.

The initial factor is the ordinary trace bound |Tr Z|<=D||Z||. It is not N^m or D^m. Independence and the L^(j+1) choices yield

 |Tr(R H^j B)| <= D L^(j+1) t^n a_n^j.

For Tr(R H^(j+1)), use j+1 independent Haar stages, with the last Haar stage at the shifted seam. The identical argument gives

 |Tr(R H^(j+1))| <= D L^(j+1) a_n^(j+1).

Both scalar series converge absolutely when L a_n<1. Summing their bounds proves (1). Markers may collide between different stages, and all balanced repeated labels are already retained in L; neither introduces an additional summation factor.

## 5. Fixed and growing-radius consequence

For fixed r and aN<=m<=bN, L is polynomial in N while (2) is exponentially small, so (1) is exponentially small. For the stronger stated range r<=kappa N/log N, uniformly on the band,

 log L <= log(r+1)+r log(mN^2) <= (3kappa+o(1))N,
 n>=aN-o(N),
 a_n <= exp[-(gamma_a-o(1))N],
 t^n <= exp[-(a log 2-o(1))N].

Since log(1/rho)<log 2, gamma_a<=a log 2. Thus L a_n and L(t^n+a_n) are at most exp[-(gamma_a-3kappa-o(1))N]. The factor D is polynomial, the denominator tends to one, and any strict c below gamma_a-3kappa is allowed. This proves the first part of (3). Nested centered ranges imply Q_r=P_r-P_0, so its trace is s_r-s_0; applying the same estimate with a slightly larger c before absorbing the factor two proves the second part.

## 6. Exact remaining space and boundaries

The orthogonal decomposition is

 Pi-P_H-P_ord = Q_r + (Pi-P_H-P_r).                            (7)

The rightmost projector remains unestimated. For r=2 the new raw span includes all single-swapped coordinate pairs, at every distance and with arbitrary repeated values; Haar removal is implemented by the genuine range projector, not by subtracting an average path mask. The inherited three-/four-block results impose different once-counted path-family conditions, so no equality with their masks is asserted. This proof uses a different mechanism: sparse offdiagonal local markers plus long-cycle contraction.

The argument does not estimate arbitrary Hamming radius proportional to N, the complete decorated span, or the off-charge sector. It does not produce the plateau or higher factorial comparison. It needs no entrywise flatness and no nonlinear phase property beyond the inherited actual singular bound. Thus it also applies to other mixing unitaries and cannot by itself be a universality criterion.

No external theorem beyond the named accepted inputs is used. The tensor algebra and asymptotic inequalities are proved above; bounded exact computations serve only as convention and failure-mode checks. Independently reviewed; see record/balanced_hamming_review.md.
