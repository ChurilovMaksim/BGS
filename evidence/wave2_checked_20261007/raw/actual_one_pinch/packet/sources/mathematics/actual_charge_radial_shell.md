# Actual charge compactness and the radial switch boundary

Candidate theorem, 7 October 2026. The literal odd-dimensional operator U_N=exp(i 10^-80 N A_N)M_N is unchanged. This note does not prove the signed boundary integral. It determines what the switch regularization can and cannot do to its spectrum. Self-review only until a separate review is supplied.

## C1. Exact hypotheses and result

Let H_N=End(C^N), with squared normalized Hilbert–Schmidt norm ||X||_N^2=N^-1 Tr(X*X). This scalar normalization changes no operator norm. Let T_N=Ad(U_N), H_N^0=I^perp, and D_N=sum_c P_c T_N P_c, where P_c projects onto matrices supported on column minus row c modulo N. The identity direction is reducing for T_N and D_N. Put

    A_N(delta)=(1-delta)T_N+delta D_N.

The following statements concern this transfer A_N(delta), not the generator A_N in the definition of U_N. The distinct typography is suppressed in plain text; below write L_N(delta) for the transfer to avoid ambiguity.

Inputs: accepted all-translation source A8/A11 (uniform decay for growing centered charge), A12/A13 (fixed-charge compact norm limit), A15/A16 (ordinary Weyl dictionary), and the zero-charge norm limit proved in the accepted one-step gap source G2. Actual one-step Egorov and mixing are FM-018 O8/O11, with their recorded source/review boundaries. No quantitative rate beyond these accepted statements is assumed.

There are isometric Weyl embeddings I_N:H_N -> L2(T2) under which the extended D_N converge in operator norm to a compact operator K. On the centered subspaces:

(a) For any sequence epsilon_N -> 0, and any spectral arc projection E_N(zeta,epsilon_N) of T_N|H_N^0,

    sup_(|zeta|=1) ||D_N E_N(zeta,epsilon_N)|| -> 0,
    sup_(|zeta|=1) ||D_N* E_N(zeta,epsilon_N)|| -> 0.          (C1)

More generally, ||D_N X_N||+||D_N* X_N|| ->0 for any unit centered sequence with ||(T_N-zeta_N)X_N|| ->0, |zeta_N|=1.

(b) For every sequence 0<delta_N ->0, every eigenvalue lambda of L_N(delta_N)|H_N^0 satisfies, uniformly in lambda,

    |lambda| = 1-delta_N+o(delta_N).                         (C2)

In particular this specified channel has no enhanced spectral decay of order greater than delta_N. Its spectral gap 1-rad(L_N(delta_N)|H_N^0) is delta_N(1+o(1)). This is a matching statement, not only an upper radius bound.

(c) For each such eigenvalue there is an eigenvalue nu of T_N|H_N^0 with

    |lambda-(1-delta_N)nu|=o(delta_N).                       (C3)

This is one-sided spectral proximity; it is not an eigenvalue bijection or a microscopic spacing estimate.

These conclusions are not asserted uniformly over arbitrary N independent occupation phases. Such phases need not preserve the fixed smooth-symbol convergence used below. They do not improve T16 to an undamped signed trace bound.

## C2. Weyl embedding and norm compactness

Write centered integer labels a,b in B_N={-(N-1)/2,...,(N-1)/2}. The ordinary Weyl matrices W_N(a,b) are orthonormal for normalized HS, including their literal wrap conventions. Define

    I_N W_N(a,b) = e(bq+ap).

The range is the square trigonometric band V_N, whose orthogonal projections converge strongly to identity. Charge c=a is exactly the p-Fourier fiber. Thus D_N is block diagonal in a, and its (a,a) block is the accepted B_(N,a), expressed in the q-Fourier basis with the midpoint phase e(ba/(2N)).

For each fixed a, the accepted step-function embedding J_N gives J_N B_(N,a)J_N* -> K_a in operator norm, with K_a compact on L2(T). For a=0 the same result is G2/G3 in the accepted one-step proof. Negative fixed a follow by its exact B_(-a) antiunitary-conjugate relation (or the identical fixed-a expansion).

Here is why passing to the Fourier embedding does not silently lose high-frequency aliases. Let F_(N,a) map the normalized discrete vector with entries e(b(j+a/2)/N) to e(bq), for centered b. It is unitary from l2_N to the band. Put S_(N,a)=F_(N,a)J_N*. Both S_(N,a) and S_(N,a)* have norm at most one. For every fixed trigonometric polynomial f,

    S_(N,a) f -> f,    S_(N,a)* f -> f in L2.

Indeed, J_N* takes cell averages, whose value for e(bq) differs uniformly by O_(a,b)(N^-1) from the displayed midpoint sample, while the adjoint sends e(bq) to that midpoint-sampled step function. Density proves both strong convergences. Compactness therefore gives

    || S_(N,a) K_a S_(N,a)* - K_a || ->0.

Conjugating the accepted norm limit proves the identical norm convergence for the Weyl/Fourier embedding. No claim that step and Fourier embeddings are uniformly close on their entire bands is used.

By A11, for every eta>0 there are C_eta,N_eta such that all centered |a|>=C_eta have ||B_(N,a)||<=eta for odd N>=N_eta. The fixed-a norm limits imply ||K_a||<=eta for every |a|>=C_eta. Therefore the direct sum

    K = direct_sum_(a in Z) K_a

is compact: its finite-a truncations are finite sums of compact operators and its tail operator norm tends to zero. Compare the finite-a blocks, then bound both tails by eta, to obtain

    || I_N D_N I_N* - K || ->0.                            (C4)

This is collective compactness on a common Hilbert space. It is not a trace-norm convergence statement. The zero mode is the common constant/identity vector, and K and K* preserve its orthogonal complement.

For completeness, fixed-mode matrix elements and Egorov identify K as the compact charge pinching of the actual Koopman operator C_G:f -> f composed with G:

    K = direct_sum_a i_a* C_G i_a,    i_a f=f(q)e(ap).

The norm argument above, rather than weak Egorov alone, establishes compactness.

## C3. Strong quantum-to-classical convergence

Extend T_N by zero off V_N, writing Tbar_N=I_N T_N I_N*. Actual one-step Egorov and fixed-symbol trace/alias convergence imply

    Tbar_N f -> C_G f,     Tbar_N* f -> C_G* f               (C5)

strongly for every f in L2(T2). One may verify the first assertion on trigonometric polynomials, then use contractivity and density. The smooth image f composed with G is approximated by fixed trigonometric polynomials; the normalized HS norm of the quantization error tends to zero by the accepted Fourier/alias estimates. For the adjoint, take smooth g=C_G* f, use the first assertion on g and unitarity on V_N; fixed-band projections tend strongly to identity. Density completes the argument. There is no long-time Egorov estimate here.

Classical mixing in the actual area measure implies that C_G has no nonconstant L2 eigenfunction on the unit circle. Smooth mixing extends to L2 by approximation and unitarity. This inherited input is separate from the nonlinear phase argument proving C4.

## C4. Compact operators annihilate all centered quasimodes

Suppose ||X_N||=1, X_N centered, |zeta_N|=1, and ||(T_N-zeta_N)X_N|| ->0. Set x_N=I_NX_N. From any subsequence choose a further subsequence with zeta_N ->zeta and x_N weakly convergent to x. For every fixed test f, C5 gives

    <f,C_G x> = lim <Tbar_N* f,x_N>
              = lim <f,Tbar_N x_N> = zeta <f,x>.

Also <1,x>=0. Mixing forces x=0. Thus every weakly convergent subsequence has zero limit, so x_N ->0 weakly. Compactness of K,K* and C4 imply

    ||D_N X_N||+||D_N* X_N|| ->0.                           (C6)

This contradiction argument is uniform over all choices of centered quasimodes. A unit vector in a spectral arc of angular radius epsilon_N has residual at most epsilon_N, proving C1. It includes arbitrary linear combinations in the arc, all eigenvalue multiplicities and every odd N; no simplicity is used.

## C5. Every damped eigenvector is a vanishing-residual quasimode

Let delta=delta_N and let X be a normalized centered eigenvector of L_N(delta), with eigenvalue lambda. Since ||D_N||<=1,

    ||L_N(delta)-T_N||<=2delta,
    1-2delta <= |lambda| <=1.

For delta<1/4, zeta=lambda/|lambda| is defined and

    ||(T_N-zeta)X|| <= ||(T_N-lambda)X||+||lambda-zeta||
                    <=4delta.

C6 yields ||D_N X||=o(1), uniformly over every such eigenvector: a failure of uniformity would select a contradicting sequence. Now the eigenvalue equation gives both

    1-delta-delta||D_NX|| <= |lambda|
                          <=1-delta+delta||D_NX||,

which prove C2 directly. Moreover

    ||[(1-delta)T_N-lambda]X|| = delta||D_NX||=o(delta).

Normality of T_N implies distance from lambda to (1-delta)spec(T_N|H_N^0) is bounded by this residual, proving C3. No diagonalizability of L_N(delta) is needed. Its trace of powers still equals the sum of eigenvalue powers with algebraic multiplicity; C2 is uniform over that entire set because each eigenvalue has an eigenvector.

## C6. Relevance and non-closure

The older one-step gap gives radius <=1-kappa delta with possibly extremely small fixed kappa. C2 shows the actual leading radial loss is exactly delta as delta vanishes. In particular no argument based on an enhanced spectral gap delta^alpha with alpha<1, or a fixed positive gap surviving delta ->0, can bridge the signed boundary for this actual transfer.

At delta=A log N/N, this improves the untwisted spectral trace radius to exp[-(1-o(1))A m log N/N]. The N^2-dimensional trace prefactor and the occupation integral have not disappeared. The arbitrary occupation twists in T16 remain essential; the present compactness is not uniform in them. More fundamentally, C3 controls eigenvalues only to o(delta), which is generally far larger than 1/N at the known interior endpoint. Neither C2 nor C3 controls the needed signed trace subtraction. No BGS, CUE, full off-charge or balanced estimate follows.
