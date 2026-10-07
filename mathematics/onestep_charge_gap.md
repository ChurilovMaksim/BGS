# Strict one-step contraction of every nonzero actual charge block

Maintained proof prepared 7 October 2026. Independent internal review: proved as written, relative to the scoped inherited inputs below. Literal odd-dimensional U_N=exp(i tau N A_N)M_N, tau=10^-80. This strengthens the finite-power theorem; constants and startup are existential. It is not a spectral-statistics theorem.

## G1. Exact claim and dependency boundary

There exist rho<1 and N0, depending on the prescribed fixed map, such that

    sup_(c!=0 mod N) ||B_(N,c)|| <= rho,  odd N>=N0,
    B_(N,c)(j,k)=U_N(j,k) conjugate(U_N(j+c,k+c)).                 (G1)

Consequently, on H0={X:Tr X=0} with ordinary Hilbert--Schmidt norm, the block-diagonal charge compression

    D_N=sum_c P_c Ad(U_N) P_c,   H_c=span{|j><j+c|},

satisfies ||D_N|H0||<=rho_*<1 eventually, where rho_* can be chosen as max(rho,1/2). The constants and startup are existential, with no uniformity as tau tends to zero.

The only analytic inputs used are the actual parametrix and phase certificate and the norm-limit/growing-charge parts A2--A5 of the accepted all-translation proof. The present proof does NOT use A6--A7, Egorov, classical mixing, or any conclusion obtained from those sections. FM-021 supplies only the accepted zero-charge bound and the explicit leading-amplitude positivity estimate. Exact input snapshots and section-level scopes are mapped in [the dependency contract](../record/charge_strengthening_dependency_contract.json); original source_manifest.json is retained in [historical evidence](../evidence/charge_strengthening_20261007/raw/author/source_manifest.json). In particular:

- accepted all-translation proof SHA256 c0059f000b4642de174097b3e971d22ba0eac09cdff684289f72ae11db00a7c7;
- acceptance SHA256 7b046dd79bdb000a0d84c150a1949d517fdb2043c3a3c81d6929e8c5e2ae17b4;
- actual parametrix SHA256 c696ebd39a52ca83205800a41fc30a9d570ebd3ed5dc96069f212948275600d7;
- FM-021 SHA256 3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09.

Every named input is frozen under [historical author inputs](../evidence/charge_strengthening_20261007/raw/author/inputs/). The nonlinear phase certificate is the literal specified-time certificate, not its first-order approximation.

## G2. The envelope is strictly positive and bistochastic

Write L=partial_x+partial_y. For each fixed positive integer c, A5 supplies operator-norm convergence after the isometric step-function embedding J_N:

    J_N B_(N,c) J_N* -> K_c,
    k_c(x,y)=sum_(r=0)^3 b_r(x,y) e(-c L S_r(x,y)),
    b_r=|a_(r,0)|^2/4.                                       (G2)

Here e(v)=exp(2 pi i v), and x,y lie in the fixed unit square with the accepted chart gluing. Each K_c is compact since its bounded smooth kernel is Hilbert--Schmidt. Its norm is at most one by exact quantum compression and norm convergence.

The same argument at c=0 gives

    J_N P_N J_N* -> K_0,     P_N=|U_N|^2,
    k_0=d=sum_r b_r.                                         (G3)

For clarity, this is not a new uniform-c statement: the twelve r!=s branches vanish in operator norm by the accepted nonzero phase certificate at u=0; the four r=s branches converge to the sampled smooth kernel d; the entrywise product remainder is O(N^-2), hence its operator norm is O(N^-1). This is exactly the FM-021 decomposition together with the step-function argument in A5.

The leading real transport equation and a_(r,0)(0)=1 imply positivity, and the explicit inherited estimate |a_(r,0)-1|<2*10^-66 implies b_r>0 uniformly on the closed square. No assertion about the sign of the higher amplitude correction is used.

Because P_N is doubly stochastic, its extended operator and adjoint both fix the constant function 1 exactly: J_N*1 is the constant vector and J_N1=1. Passing to the operator-norm limit and its adjoint gives K_0 1=1 and K_0*1=1. Therefore

    integral d(x,y) dy=1,   integral d(x,y) dx=1.              (G4)

These equalities initially hold almost everywhere and then everywhere by continuity. Thus d is a strictly positive bistochastic probability kernel on [0,1]. No identification with a classical Koopman compression or an invariant measure is required.

## G3. Equality in the positive-envelope bound is impossible

Fix c>=1. Suppose ||K_c||=1. Compactness gives a unit vector f in L2([0,1]) with ||K_c f||_2=1. Pointwise triangle inequality followed by the Markov/Jensen inequality gives

    |K_c f|(x) <= (K_0 |f|)(x),
    ||K_0 |f|||_2^2 <= integral integral d(x,y)|f(y)|^2 dy dx
                     = ||f||_2^2=1.                        (G5)

Since the first and last norms equal one, both inequalities are equalities. Equality in the second line is exactly zero of the nonnegative integral

    integral_x integral_y d(x,y)
             (|f(y)|-K_0|f|(x))^2 dy dx.

Since d>0 almost everywhere, |f(y)| is a constant almost everywhere; the unit norm makes this constant one. Equality in the first line holds for almost every x. For each such x, K_c f(x) is the integral over (y,r) of the unit-modulus quantities e(-c L S_r(x,y)) f(y), with strictly positive weights b_r(x,y) of total mass one. A probability average of unit complex numbers has modulus one only when those numbers agree almost everywhere. (Multiply by the conjugate of the average's unit phase; the nonnegative function 1-Re(z) has zero integral.)

In particular, canceling the nonzero common f(y) from the r=0 and r=1 branches gives

    e(-c L(S_0-S_1)(x,y))=1                                 (G6)

for almost every (x,y). Continuity makes this equality hold on the whole square. Hence the continuous real function c L(S_0-S_1) takes values in Z on a connected square and is constant there.

That contradicts the actual phase certificate, as follows. Put R_r=S_r-S_r^0. Its exact gluing is R_r(x,y)=R_0(x,y+r), with four-periodicity in each variable. At either nu_0=(-3/4,1/4) or nu_1=(1/4,1/4), the Fourier coefficient A_i of R_(0,xy) is nonzero, with |A_i|>=pi tau/6400. Since L(S_0^0-S_1^0)=1/2 is constant, the Fourier coefficient of partial_xy L(S_0-S_1) at nu_i is exactly

    2 pi i (nu_i,x+nu_i,y) A_i (1-e(1/4)).                  (G7)

Both frequency sums are nonzero (respectively -1/2 and 1/2), so (G7) is nonzero. Thus L(S_0-S_1) is not constant on R^2. It is real analytic; if constant on the open unit square it would be constant everywhere by analytic uniqueness. This contradicts (G6). Therefore

    ||K_c||<1  for each fixed nonzero integer c.             (G8)

The argument uses neither a quantitative lower bound for the gap nor decay under iteration. It retains all four positive branches; branch alignment cannot be assumed from the cat leading phase.

## G4. Uniformity over all nonzero modular charges

The accepted growing-charge result A11 gives integers C0,N1 such that

    ||B_(N,c)||<=1/2,  C0<=c<N/2, N>=N1.

There are only finitely many positive c<C0. By G8 their maximum limiting norm rho0 is strictly below one (take rho0=0 if the set is empty). For each of them G2 gives eventual norm at most (1+rho0)/2. Increase one N0 for the finite list, and put rho=max(1/2,(1+rho0)/2)<1. This proves G1 for positive representatives. The exact relation B_(N,-c)=T_(-c) conjugate(B_(N,c)) T_c preserves norms and covers all other nonzero residues in odd N.

The charge-zero block is P_N. Its constant vector is the global identity matrix, and its traceless diagonal part has norm ||P_N-J_N||<=1/2 eventually by FM-021. All charge blocks are mutually orthogonal and D_N is their direct sum. This proves the asserted norm bound on H0.

## G5. Boundaries and controls

At tau=0, a fixed even c gives a rank-one norm-one limit, and L(S_0-S_1)=1/2 is constant. Thus the proof correctly fails for the cat and cannot be a theorem from flatness or unitarity alone. The literal nonzero actual Fourier coefficient is essential. No finite numerical experiment at tau scaled to be visible can test the asserted eventual threshold.

Finite controls accompanying the global switch-transfer note check exact charge blocks, trace identities, occupation masks, Hamming grading and the cat norm-one obstruction. They do not certify G7 at floating precision or prove the analytic limit. G7 is inherited from the pinned actual phase certificate and differentiated exactly.

The conclusion is a new strict one-step block estimate, not contraction of Ad(U_N) on H0. The latter remains unitary. A full sum over switch histories requires its own signed bookkeeping; damping in the companion note is retained explicitly. No BGS, CUE plateau, or full undamped off-charge estimate is claimed.

## Review and reproduction record

The exact original candidate, independent reviews, source pins and bounded computational controls are preserved by [the promotion record](../record/charge_strengthening_promotion.md). No finite computation proves the analytic limit. This prepared overlay is not an integration or publication claim.
