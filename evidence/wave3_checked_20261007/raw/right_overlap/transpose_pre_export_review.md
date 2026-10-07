# Independent right-frame and fixed-B prefix audit

7 October 2026. No canonical repository mutations and no additional agents. The new Library packet could not be accessed: the supported preparation succeeded, but its current transfer helper returned HTTP 403. That denial was not bypassed. Accordingly this report independently reconstructs the precisely specified right-frame extension from the already accessible, accepted left proof; it does not purport to inspect the inaccessible candidate text.

**Primary verdict: proved as written**, for the normalized right-frame and fixed-B prefix claim below, with the accepted actual left-proof analytic inputs. The separated-insertion and Schatten-tail candidates are **not addressed** and are not accepted by this verdict. The candidate's reported 222 core controls were not available and were not reproduced.

## 1. Exact claim card and provenance

Let U=U_N be the unchanged literal odd-dimensional quantum map at tau=10^-80, with the ordinary physical midpoint symbol, raw Weyl aliases, and original scalar centering. On End(C^N) use the ordinary Hilbert–Schmidt inner product, linear in its second argument. Let

    (A_c(U))_(y+c,y)=U_(y+c,y), with all other entries zero,
    C_U e_c=A_c(U)*,
    L_U X=U X,       R_U X=X U,
    J X=X^T,         P e_c=e_(-c).

Indices are modulo N. Transpose here is complex-linear, not an adjoint or complex conjugation.

The normalized claim is

    C_U* R_U^r C_U = P C_(U^T)* L_(U^T)^r C_(U^T) P,
    ||C_U* R_U^r C_U|| <= C_r sqrt(log(2N)/N)

for every fixed integer r>=1 and all odd N, with constants allowed to depend on fixed r and the fixed map, not on N.

For any fixed b>0 define the right-frame echo

    F_(N,n)(B)=sum_c |tr(A_c(U) B U^n)|^2
             =(1/N) sum_a |tr(B U^n Z_a U Z_a*)|^2.

Then

    sup_(||B||op<=1, s in Z, 0<=M<=bN)
       N^-2 sum_(n=0)^(M-1) F_(N,s+n)(B) -> 0.

In particular this is uniform over every unitary B_N that is held fixed during its time sum. B may depend on N, on the starting time, and on the chosen prefix, because the operator estimate is uniform. The claim does not cover a separately changing B_n at each summand.

Accepted source: ../bgs_wave2_actual_one_pinch_review/packet/actual_fixed_lag_overlap.md, Sections 1–7, all 200 lines, SHA256 11c90c3dac599f63d6508685647db66ba78ebfb280955a61b29917daab7786cb. Its independent review is ../bgs_wave2_actual_one_pinch_review/independent_review.md, SHA256 74c5ffc2b30f22767bf27a35c8ff070dfa7ab093442ad9d45104c0a3c8846eb9.

The accepted four-branch parametrix source used below is its pinned sources/mathematics/four_branch_parametrix.md, SHA256 c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7.

Canonical BGS was checked clean at 129c676b8e6457e7e5f1bd6f786b3939cbd84653. No source/status promotion is made here.

Inaccessible candidate reference: Library libfile_4d3be7dc08188191a33eec4f52f1b2a6, backing file_00000000160081f580cdd67d8852c4a4, BGS_right_overlap_candidate_20261007_v2.zip. The parent-supplied expected archive hash be1b00e822a71b84624204e557dba62e026e74b9e857e1c37303f988fabeb675 and manifest hash 9a8c44486046458c6fca2f7fdba2caae7985efeee6cf3406e7ff8d29f7f1642c could not be verified against bytes.

## 2. Dependency graph

1. Exact finite-dimensional transpose and slice algebra gives the displayed right/left overlap identity.
2. The accepted full four-branch parametrix for U, transposed entrywise without conjugation, supplies the same analytic kernel assumptions for U^T.
3. The unchanged symmetric cat quadratic and affine branch changes give exactly the accepted cyclic Hessian and reduced mixed-derivative argument for that transposed kernel.
4. The accepted cutoff-before-expansion, all-alias stationary-phase, and alias-safe discrete TT* argument therefore proves fixed-lag left overlaps for U^T.
5. Exact transpose conjugacy transfers that estimate to right overlaps for U.
6. The right-evolution fixed-block Gram inequality bounds all prefixes uniformly over unit Hilbert–Schmidt seeds. Taking the seed B/sqrt(N) gives the asserted uniform B conclusion.

The inherited parametrix and accepted left analysis are reviewed project inputs. The newly used transpose and prefix implications are proved here, not inferred from finite tests. No external long-time trace theorem, mixing assumption, Egorov theorem, or microscopic density estimate is added.

## 3. Exact transpose and frame identity

For matrices X,Y,

    <JX,JY>HS = sum_ij conjugate(X_ji) Y_ji = <X,Y>HS.

Thus J is a complex-linear HS unitary involution. Direct multiplication gives

    J R_U J(X)=(X^T U)^T=U^T X=L_(U^T)(X).

The slice supports and values give

    A_c(U)^T=A_(-c)(U^T).

Consequently

    J C_U e_c=(A_c(U)*)^T=A_(-c)(U^T)*
              =C_(U^T) P e_c.

Since P*=P=P^-1 and J*=J, inserting J on both sides of R_U^r proves exactly

    C_U* R_U^r C_U
      =(J C_U)* [J R_U^r J] (J C_U)
      =P C_(U^T)* L_(U^T)^r C_(U^T) P.

All equalities hold for arbitrary complex U and nonnegative integer r. For unitary U they also hold for every integer r. No U=U^T assumption, physical time-reversal symmetry, or identification of U^T with the original factorization is needed.

## 4. The exact analytic assumptions survive transpose

Write the accepted approximant as

    V_N(j,k)=e(3N/8)/(2 sqrt(N))
               sum_(alpha=0)^3 e(N S_alpha(j/N,k/N))
                                  b_(alpha,N)(j/N,k/N),
    b_(alpha,N)=a_(alpha,0)+N^-1 a_(alpha,1),
    ||U_N-V_N||op=O(N^-3/2).

For U^T simply take V^T and define

    T_alpha(x,y)=S_alpha(y,x),
    beta_(alpha,N)(x,y)=b_(alpha,N)(y,x).

The scalar, all four branch labels, both amplitudes, and N normalizations remain exactly unchanged. Since singular values are invariant under transpose,

    ||U_N^T-V_N^T||op=||U_N-V_N||op=O(N^-3/2).

Unitarity survives transpose as well: (U^T)* U^T=overline(U U*)=I. Flatness and slice-synthesis bounds are identical. The accepted operator-level fixed-power comparison consequently applies to U^T before any branch expansion.

The FULL V^T sampled kernel is exactly periodic in each sampled index because the full V kernel is exactly periodic in each index. More explicitly, the accepted phase identities transpose to

    T_(alpha+4)-T_alpha = y-3x-3alpha-6,
    T_alpha(x+1,y)=T_(alpha+1)(x,y),
    T_alpha(x,y+1)-T_(alpha-3)(x,y)=-2alpha-2x+3.

On x=j/N,y=k/N, the real differences times N are integers. The matching identities for both amplitudes transpose too. Thus the full-kernel sampled-gluing input, including wraparound and the subleading transport amplitude, survives exactly. The original HJ/transport equations need not be reasserted for T_alpha; their consequences are inherited by transposing the already constructed kernel. Treating U^T as if it had the identical original kick factorization would be unnecessary and unjustified.

All fixed smooth derivative bounds on compact charts survive the coordinate swap. The accepted global coordinate Hessian smallness also survives:

    |partial_(i,j)(T_alpha-T_alpha^0)| < eta=10^-60

for every real (x,y), since each derivative is a coordinate-permuted original derivative. This is global smallness, not a smallness claim restricted to the sampling square.

Finally,

    T_alpha^0(x,y)=S_alpha^0(y,x)
       =S_0^0(x,y)+alpha y/4-3alpha x/4-3alpha^2/8,

because S_0^0(x,y)=-(3x^2-2xy+3y^2)/8 is symmetric. The difference from the unshifted cat phase is affine in x,y. Therefore every Hessian block of the r+2-factor cyclic phase, including external c,d blocks and boundary mixed vectors, is EXACTLY the same as in the accepted left proof:

    H^0=-(3/2)I+(P_r+P_r*)/4,
    Phi^0_cd=1/4,
    Phi^0_xc=(e_(r-1)-e_0)/4,
    Phi^0_xd=-Phi^0_xc.

The r=1 vector vanishes and H^0=-1. At r=2 the repeated neighboring link contributes the correct 1/2 off-diagonal entry. No generic-neighbor counting argument is substituted at these minimum cases.

The same composed-correction envelope remains below 64 eta<10^-50. Thus the accepted global negative definiteness, unique critical point for every alias, reduced mixed derivative interval [1/10,1/3], cutoff-before-expansion, smooth cutoff crossing, summable all-alias tails, and TT* integer-alias exclusion all apply. This verifies every extra assumption needed to use the accepted left proof for U^T.

This proves the stated right-overlap estimate for the actual U_N. It supplies no growing-r control or rate for the long-prefix limit.

## 5. Uniform fixed-B prefix bound

Let C=C_U, R=R_U, and K_r^R=C* R^r C. For fixed integer L>=1 set

    epsilon_(L,N)^R=max_(1<=r<L)||K_r^R||,

with epsilon=0 when L=1. Eventual flatness gives ||C||^2<=C_flat independently of N. Since R is unitary, K_(-r)^R=(K_r^R)*.

Consider the synthesis map with blocks R^-j C, j=0,...,L-1. Its block Gram has (j,k) block C*R^(j-k)C. The diagonal block norm is at most C_flat and each off-diagonal block norm at most epsilon. The block Schur bound gives

    ||(1/L) sum_(j=0)^(L-1) R^-j C C* R^j||
        <=C_flat/L+(1-1/L)epsilon_(L,N)^R =: a_(L,N).

Hence for every unit HS vector X and every start s,

    (1/L) sum_(j=0)^(L-1) ||C* R^(s+j) X||^2 <=a_(L,N).

The bound is an operator bound on all seeds, so uniformity over B follows before taking any limit. For ||B||op<=1, ||B/sqrt(N)||HS<=1, and

    F_(N,s+j)(B)/N
       =||C* R^(s+j)(B/sqrt(N))||^2.

Break any prefix of length M into full L-blocks and a final remainder of size t<L. Each remainder summand is at most C_flat. Therefore

    N^-2 sum_(n=0)^(M-1) F_(N,s+n)(B)
       <=(M/N) a_(L,N)+C_flat L/N
       <=b a_(L,N)+C_flat L/N,       0<=M<=bN.

The estimate includes M=0 and prefixes whose lengths do not themselves tend to infinity. It is uniform in B and s. At each fixed L the right fixed-lag theorem gives epsilon_(L,N)^R->0. Taking limsup_N and then L->infinity proves the claim.

For the alternative interval-average normalization, any M_N->infinity satisfies

    sup_(||B||op<=1,s) (N M_N)^-1
        sum_(n=0)^(M_N-1) F_(N,s+n)(B) ->0.

That version has no upper length restriction. Both results use fixed L before N->infinity; neither assumes a growing-r estimate.

Crucial scope: B is fixed along each summed orbit. Selecting an unrelated B_n independently at each time destroys the single-orbit Gram argument. This audit does not extend the prefix bound to such a family. It also does not show that arbitrary separated insertion words admit a representation within the fixed-B scope.

## 6. Obligation matrix and exact controls

- Complex-linear HS transpose, no adjoint confusion: passed by exact derivation.
- Slice sign flip and right/left multiplication conventions: passed.
- Scalar centering, raw branches, both amplitudes and transpose operator error: passed.
- Full sampled gluing before branch expansion: passed.
- Global, rather than chart-only, C² smallness: passed.
- Every fixed derivative bound after coordinate swap: passed.
- Symmetric cat quadratic, affine branch offsets, all Hessian blocks: passed.
- All aliases and fixed-r analytic norm argument: passed at the accepted left input's scope.
- B uniformity and prefix supremum with fixed B: passed by an operator estimate.
- Growing-r constants, effective prefix rate, separated insertion combinatorics: out of scope.
- Inaccessible packet's separated-insertion theorem: not addressed.
- Inaccessible packet's Schatten-tail theorem: not addressed.
- Inaccessible candidate's 222 core controls and byte/manifest identity: not addressed.

Reproduced the accessible accepted left checker in an isolated copy: 129 controls passed in ordinary Python and python -O. These test N=3,5 Gaussian-rational fixtures, cyclic Hessians r=1,...,16, and rational constant slack. They do not prove WKB or an analytic limit.

The independent check_transpose.py passed 72 controls in ordinary Python and python -O. Exactly 18 of those directly test transpose facts in nonsymmetric complex Gaussian-rational unitary fixtures at N=3,5, including complex linearity, the slice flip, the right/left intertwiner, and lags r=0,1,2,3. The additional controls test fixed-B frame traces and right evolution, every block of the L=3 right Gram, and the FULL cat Hessian including external variables at r=1,...,16. They are finite corroboration of the displayed analytic/algebraic proofs, not an extrapolation.

Commands:

    python3 accepted_left_controls/check_overlap.py
    python3 -O accepted_left_controls/check_overlap.py
    python3 check_transpose.py
    python3 -O check_transpose.py

Reports and stdout logs are saved beside this audit. These are newly executed controls on accessible sources, not the inaccessible author's broader suite.

## 7. Exact remaining gap and strongest safe statement

There is no mathematical gap identified in the specified right-frame/fixed-B prefix implication. It is safe to use that bounded theorem as an input to a separate native first-pinch resummation, provided that resummation actually produces one fixed B for the time prefix to which the bound is applied.

The new packet's stronger separated-insertion and Schatten-tail claims remain unaudited. The blocker is lack of authorized accessible contents after HTTP 403, not a proved defect in those unknown arguments. The cheapest next check is an authorized text export of those exact statements, proofs, and control sources, followed by separate audits. The easy transpose result cannot confer acceptance on them.

No Hamming mask, coefficient extraction, high-switch subtraction, deconvolution, logarithmically growing insertion hierarchy, T16, TRACE-005, or BGS claim follows from this report.

