# A bounded-degree coherence theorem for the actual phase ensemble

Status: author mathematical proof, self-review and bounded checks only; independent review is pending. This does not prove the absorbed Ward obligation (13). All limits applied to the actual operator retain odd N, the raw Weyl physical half-shift, the centered symbol and fixed tau=10^-80. The checked snapshot and accepted Ward v2 are unchanged.

## 1. Exact finite-dimensional statement

Let U be an N-by-N unitary, D have independent uniform diagonal phases, V=DU, P_ab=|U_ab|^2, J_ab=1/N, and Q_ab=U_ab conjugate(U_ba). Suppose max P_ab<=C/N, C>=1, and put r=||Q||op. For m>=2 define

    e_m = m! [ C^(m-1) r + C^(m-1/2)/sqrt(N)
                         + m(m-1) C^m/N ].                       (1)

For h in C^N, let Z_m(h)=Tr(diag(conjugate(h)) V^m), and define the real symmetric matrix

    L_m = sum_(u=0)^(m-1) P^u circ (P^(m-u))^T,                  (2)

where circ is the entrywise product. In particular its u=0 term is diag((P^m)_aa). Then

    | E |Z_m(h)|^2 - h* L_m h | <= (e_m/N) ||h||_2^2.          (3)

For m=1 equality holds with L_1=diag(P_aa). Equation (3) is an operator-norm covariance estimate for arbitrary deterministic complex spatial weights, not merely a trace bound. The whole expectation includes repeated occupations; their correction is bounded in the last term of (1).

Two companion consequences, with p_m=Tr V^m, are

    |E |p_m|^2 - m Tr P^m| <= e_m,                             (4)
    |E p_u p_(m-u) conjugate(p_m)| <= e_m   (m>=3, 1<=u<m).           (5)

For m=2 the valid separate general bound is |E p_1^2 conjugate(p_2)|<=2C^2; (5) is not claimed at m=2. Section 8 supplies an additional actual-model kernel estimate which makes this exceptional moment tend to zero. All traces and Euclidean norms here are unnormalized. No eigenangle-conditioned Haar law is assumed.

## 2. Phase averaging and the collision error

Write a closed length-m path as x=(x_0,...,x_(m-1)), with amplitude A(x)=product_t U_(x_t,x_(t+1)), cyclic indices. Its phase monomial records the complete occupation vector of x. Integrating D preserves precisely pairs of paths with the same occupation vector.

If x has distinct coordinates, each surviving y has a unique representation y_t=x_(sigma(t)) for sigma in S_m. The two weight marks in (3) are conjugate(h_(x_0)) and h_(x_(sigma(0))). The permutations which preserve the directed cycle are exactly its m rotations. Their unrestricted sum is h*L_m h: cutting the cycle at positions 0,u gives (P^u)_ab (P^(m-u))_ba. This also proves L_m is symmetric. Positivity follows by grouping an unrestricted P-weighted closed cycle with its cyclic roots: the resulting weight is proportional to the squared modulus of the sum of its h marks.

Here is a uniform bound for every collision removal used below. For fixed positions a,b and a fixed equality x_i=x_j, i!=j,

    sum_(x:x_i=x_j) |h_(x_a) h_(x_b)|
          <= N^(m-2) ||h||_2^2.                              (6)

If the two marked positions coincide or are identified by the equality, sum |h|^2 at that free coordinate. Otherwise use ||h||_1^2<=N||h||_2^2. The remaining free coordinates give exactly (6). There are binom(m,2) possible equalities, so a union bound is legitimate. Each paired path amplitude is at most q^m, q=max P<=C/N.

For a repeated x, the representation by permutations need not be unique; this is not ignored. The original repeated-path contribution is bounded by the sum over all m! possible permutations. Passing first from the exact occupation sum to its distinct-coordinate part, and then back from the distinct permutation sums to unrestricted permutation sums, costs at most

    2 m! binom(m,2) N^(m-2) q^m ||h||_2^2
      <= [m! m(m-1) C^m/N^2] ||h||_2^2.                     (7)

Thus repeated and periodic occupations are retained through an explicit finite-color correction; unrestricted permutation sums are not asserted to equal the original expectation.

## 3. One unmatched edge estimates every noncyclic permutation

Fix a permutation which is not a rotation. Some directed edge i->i+1 of the original cycle is absent from the second cycle. If the reverse edge is present there, the two factors involving both selected variables form Q_(x_i,x_(i+1)). If the reverse is absent too, they form U_(x_i,x_(i+1)) alone. The remaining factors separate into a function of x_i, a function of x_(i+1), and factors depending on the other coordinates. A directed cycle on distinct formal vertices has no other edge involving both selected variables. Numerical coincidences in the unrestricted sum do not change this formal factorization.

Contract these two variables using ||Q||=r or ||U||=1. Every other matrix entry has modulus at most sqrt(q). If the two weight marks coincide, then sigma(0)=0 and the unmatched edge can be chosen away from vertex 0: preservation of all edges 1->2->...->m-1 would force the whole cycle to be preserved. For distinct marks, allow zero, one, or both marks on the selected endpoints.

In these four cases, Cauchy-Schwarz at a marked endpoint, ||h||_1<=sqrt(N)||h||_2 at an uncontracted mark, or direct summation of |h|^2 at the single coincident mark gives the same bound. Each noncyclic permutation contributes at most

    N^(m-2) q^(m-1) r ||h||_2^2,

or, in the single-U case,

    N^(m-2) q^(m-1/2) ||h||_2^2.                            (8)

For clarity, with two distinct marks off the selected endpoints, the contraction costs N and the other sums cost N^(m-4)||h||_1^2, at most N^(m-3)||h||_2^2. With one mark on an endpoint, the factors sqrt(N)||h||_2 and N^(m-3)||h||_1 give the same N^(m-2)||h||_2^2. With both marks on the endpoints it is immediate. With coincident marks, neither lies on the selected edge and the other sums cost N^(m-3)||h||_2^2. Empty cases at small m are simply absent.

There are at most m! noncyclic permutations. Equations (7)-(8) prove (3). The m=2 noncyclic class is empty. Taking h=1 proves (4), since 1*L_m1=m Tr P^m.

For (5), the two positive traces form two disjoint directed cycles on m formal vertices, whereas the negative trace forms one cycle. They cannot have the same directed edge set. Select an edge of the single cycle absent from the double cycle, and repeat the U/Q contraction. No h marks occur, so the analogue of (8) is multiplied by N. The same two collision removals cost m!m(m-1)C^m/N. This proves (5) for m>=3, including u=1 and loops in the double-cycle graph. The single cycle at m=2 uses both directed edges between its two vertices, so that case does not have the asserted one-edge factorization. Direct expansion gives E p_1^2 conjugate(p_2)=2 sum_(a,b) U_aa U_bb conjugate(U_ab U_ba)-sum_a |U_aa|^4. Bounding the distinct and diagonal summands separately gives at most (2N(N-1)+N)q^2<=2C^2. This exception is essential, as Section 7 records.

## 4. Actual coherence covariance, with an explicit classical leading term

Assume additionally ||P-J||<=rho<1. Put Pi=I-J and

    R=(I-P+J)^(-1),   H=R+R^T-I.

Let d_m(a)=(V^m)_aa and c_m=(I-P)d_m. These are precisely the Fourier sums of the Ward-v2 vectors:

    d_m(a)=sum_j exp(i m theta_j) w_ja,
    c_m(a)=sum_j exp(i m theta_j) c_ja.                       (9)

The covariance in (3) is S_m=E[d_m d_m*]. For m>=2 set

    k_m = m(C-1)rho^(m-2) + 2rho^m/(1-rho).                 (10)

Then

    || N Pi S_m Pi - Pi H Pi || <= e_m+k_m,                 (11)
    || N E[c_m c_m*] - (I-P P^T) ||
                   <= (1+rho)^2(e_m+k_m).                  (12)

These are complete signed Fourier-weighted coherence covariances; the expectation in (12) contains all j,k, including j=k. It is neither the native charge-pinching overlap matrix nor an assertion that G=P.

Proof of (11). Write Delta_u=P^u-J. The squared norm of every row or column of P-J is at most (C-1)/N. Hence for u>=1 these norms for Delta_u are at most (C-1)rho^(2u-2)/N. It follows that

    max_a |(Delta_m)_aa| <= (C-1)rho^(m-2)/N,
    ||Delta_u circ Delta_(m-u)^T|| <= (C-1)rho^(m-2)/N.

The second bound is the row/column Schur bound followed by Cauchy-Schwarz. Expanding (2), the constant (m-1)J/N disappears on Pi, its linear terms are N^-1 sum_(u=1)^(m-1)(Delta_u+Delta_u^T), and the remaining diagonal and quadratic terms have total norm at most m(C-1)rho^(m-2)/N. The geometric tail to H costs at most 2rho^m/[N(1-rho)]. Combine with (3).

For (12), multiply (11) by I-P and I-P^T, whose norms on Pi are at most 1+rho. Direct multiplication on the centered subspace gives

    (I-P)(R+R^T-I)(I-P^T)=I-P P^T.                         (13)

Both sides vanish on constants. This establishes the stated full-space identity and the covariance estimate.

The spatial leading term in (11) is the classical Green-Kubo covariance H, not silently I. The coherence leading term in (12) is I-PP^T. Initial mixing alone would not prove these formulas: the error e_m explicitly uses reverse decay to remove reversed unmatched edges and unitarity to remove unmatched single edges.

## 5. A complete signed Ward contraction in a slow growing window

Retain the exact v2 normalization, including its cotangent-gradient cancellation. The polynomial identity for its normalized CUE generator is

    A_N p_m = -(m/2)p_m - (m/(2N))sum_(u=1)^(m-1) p_u p_(m-u),

and its product cross term on p_m conjugate(p_m) is m^2. Consequently phase stationarity (v2 equation (8)) gives exactly

    E R_(G-G_H) |p_m|^2
      = [N/(N+1)] { m(E|p_m|^2-m)
           +(m/N) Re sum_(u=1)^(m-1) E p_u p_(m-u) conjugate(p_m) }. (14)

This is the whole signed Hessian-plus-cotangent contraction for this test. In particular no inverse eigenvalue gap has been estimated separately. Since

    |Tr P^m-1| <= (C-1)rho^(m-2)  (m>=2),

equations (4)-(5) prove, for m>=3,

    | E R_(G-G_H) |p_m|^2 |
      <= m^2(C-1)rho^(m-2) + m(1+m/N)e_m.                  (15)

The trace bound uses ||P-J||_HS^2<=C-1 and the ordinary Schatten trace inequality; normality of P is not assumed.

For the unchanged actual family, the accepted sources supply eventually C=5, rho=1/2, and r_N=||Q_N||->0. Thus (11)-(12) have k_m=(16m+4)2^-m. For an explicit possibly empty finite initial window, let T_N be the largest integer 2<=T<=floor(N^(1/4)) satisfying

    T! 5^T T^4 (r_N+N^(-1/2)) <= 1.                       (16)

Set T_N=1 if none exists. For every fixed T the inequality holds eventually, so T_N->infinity. Uniformly for ceil(T_N/2)<=m<=T_N, e_m<=2/T_N^4. Equations (11)-(12) therefore identify the centered spatial and coherence covariance, and (15) tends to zero uniformly on this growing window.

The actual startup and r_N decay rate remain noneffective. In particular T_N is not a Heisenberg window: its factorial constraint gives T_N=O(log N/log log N), and r_N may make it much smaller.

## 6. Absorption, controls, and the unresolved implication

For every s>0, multiplication of each test in (14)-(15) by the original factor exp(-2sm/N) preserves the bound. No boundary limit or delay second moment occurs. However this does not turn the test |p_m|^2 into the normalized CUE Poisson solution Psi_(N,s). That solution has an infinite legitimate expansion containing degrees of order N and above. Neither the bound nor its constants justify termwise absolute summation against that expansion.

Diagonal controls have rho=1 and r=1. A directed odd N-cycle with N>=3 has rho=1 and r=0. Both violate the dimension-uniform flatness and mixing hypotheses, although the finite bounds remain valid with C=N. The reviewed flat arithmetic family has C=1, rho=0 and r=N^-1/2; it does satisfy the annealed conclusion on the slow window. Its deterministic growing-period offcharge failure is fully compatible with this result. The reviewed flat tensor boundary-delay family also fits the hypotheses but its unregularized delay variance remains infinite; no such variance is used here.

The remaining implication is quantitative control of the same fully signed coherence contractions at the spectral degrees selected by Psi_(N,s), in particular m=Theta(N), with all its mixed trace terms. The factorial estimate in (1) cannot provide that control. The original Ward (13), the balanced microscopic limit, deterministic offcharge comparison and higher factorial hierarchy remain OPEN. This result is a smaller source-bound covariance theorem, not a solution or a novelty claim.


## 7. Preserved short-cycle correction

The initial unreviewed draft incorrectly included m=2 in (5). It is preserved as `weighted_coherence_v1_unreviewed.md`; it is not the current theorem. The defect is the two-vertex cycle having both directed edges between the selected variables, which invalidates the single-edge contraction.

An exact falsifier is available on N=p^2 coordinates x in F_p^2, for odd primes p. Let J_0=[[0,1],[-1,0]] and U(x,y)=p^-1 exp(2pi i x^T J_0 y/p). Character orthogonality gives U unitary and Hermitian, P=J, and ||Q||=1/p=N^-1/2. Also U_xx=1/p and U_xy U_yx=1/N, so for every diagonal phase D, p_2(DU)=p_1(DU)^2 exactly. Therefore E p_1^2 conjugate(p_2)=E|p_1|^4=2-1/N. This contradicts the false m=2 estimate e_2=4/sqrt(N)+4/N, which tends to zero.

This changed family refutes the omitted short-cycle qualification, not the corrected covariance theorem, actual operator, or balanced microscopic law. It also shows that these coarse inputs alone cannot yield all fixed-degree CUE trace moments. The m=2 contribution to the complete normalized generator is separately suppressed by its 1/N coefficient; no such exceptional term is discarded. The growing-window statements require m>=3 eventually.

## 8. The actual phase curvature removes the degree-two obstruction

Define B_N(a,b)=U_N(a,b)U_N(b,a), without complex conjugation. This is a complex symmetric matrix, different from both P and the Hermitian reverse kernel Q. For the unchanged actual fixed-tau family,

    ||B_N||op = O_tau(sqrt(log(2N)/N)).                       (17)

This input uses the literal branch phases and is not a consequence of initial flatness, P mixing or Q decay. The skew Hermitian control in Section 7 has B=J and violates (17).

The source is `mathematics/four_branch_parametrix.md`, Sections 1, 2 and 4-6, with its exact raw quantization, phase orientation and quantitative specified-time remainder. The four-branch expansion makes B_N a sum of sixteen N^-1-amplitude kernels with uniformly smooth amplitudes and phases

    Phi_rs(x,y)=S_r(tau,x,y)+S_s(tau,y,x),

plus an O(N^-2) entrywise remainder, hence an O(N^-1) operator remainder. At t=0 each S_r,xy=1/4, so Phi_rs,xy(0)=1/2. The initial HJ mixed derivative is (g_xp/4-3g_pp/16)/(2pi), evaluated at (x,(y+r-3x)/4), and has magnitude below 10^9. The source's C^2 Taylor remainder therefore gives, for every r,s,

    |Phi_rs,xy(tau)-1/2|
       <= 2*10^9 tau+10^50 tau^2 < 1/100.                  (18)

Here tau=10^-80 is literal and fixed. Thus 1/3<=Phi_rs,xy<=2/3 globally on the fundamental sampling square and enlarged real charts. This is a curvature statement at the actual specified time, not an extrapolation from a formal first derivative.

For completeness the alias argument extends the source's local lemma to this interval. For two rows x,x' with d=|x-x'|<=1, the column phase increments in the TT* sum have one sign and magnitudes in [d/3,2d/3]. Their distance to every integer is at least d/3: the distance to zero has this lower bound, and 1-2d/3>=d/3 handles the next alias. Their total variation is O(d), by the uniform smooth phase bounds. Discrete summation by parts with denominator (exp(2pi i Delta)-1) therefore bounds the weighted unnormalized sum by O(1/d). This includes its endpoint terms and does not assume individual branch periodicity. The diagonal TT* entries are O(1/N), and the offdiagonal ones are O(1/[N|i-i'|]). The Schur bound gives O(log(2N)/N) for the squared operator norm. Summing the sixteen branches and the remainder proves (17). No analytic zero-set removal is needed for this sum phase.

Writing v_a=U_aa, the exact exceptional moment from Section 3 satisfies

    |E p_1^2 conjugate(p_2)|
       <= 2||v||_2^2 ||B_N|| + sum_a |U_aa|^4
       <= 2C||B_N||+C^2/N
       = O_tau(sqrt(log(2N)/N))                             (19)

eventually at the actual C=5. The bilinear expression is v^T conjugate(B_N) v; its absolute value is bounded by the ordinary operator norm even for complex v. The estimate retains the diagonal repeated-occupation subtraction exactly before taking the modulus.

Consequently all mixed moments in (5) with a fixed total degree, including the exceptional degree two by (19), tend to zero for the actual map. This statement concerns that precise family of mixed moments; it does not assert all fixed-degree CUE trace moments, replace the nontrivial spatial Green-Kubo covariance in (11), or extend the growing window to microscopic scale. The new actual kernel estimate removes a specific obstruction inside the same coherence calculation while leaving Ward (13) open.

## Source and verification boundary

- [Accepted Ward v2](../snapshot/BGS/mathematics/phase_ward_identity.md), Sections 2-4: R normalization, phase stationarity, and the exact c_j vectors. The infinite absorbed Poisson solution is retained but not estimated here.
- [Actual position mixing](../snapshot/BGS/mathematics/position_chain_mixing.md), Sections 1-2, and [eventual constants](../snapshot/BGS/mathematics/actual_body_coercivity_constants.md): C=5 and rho=1/2, with noneffective startup.
- [Actual reverse decay](../snapshot/BGS/mathematics/reversed_path_decay.md), Theorem and Sections 2-3: r_N->0 through all odd dimensions at literal fixed tau.
- [Raw branch parametrix](../snapshot/BGS/mathematics/four_branch_parametrix.md), Sections 1, 2, 4-6: exact initial mixed derivative, quantitative actual-time C^2 control, kernel remainder, and the elementary summation-by-parts method used in Section 8.

`source_pins.json` gives exact hashes and original archive provenance. `verify_weighted_coherence.py` checks finite Gaussian-rational occupation coefficients, repeated occupations beyond N, permutation selection, the signed Ward normalization, and specified flat controls. Its floating phase grids and matrix norms are explicitly numerical; no finite execution certifies the analytic parametrix or arbitrary-N limit. `audit.md` records self-review and the remaining independent-review questions. No claim ledger or accepted proof source was modified.
