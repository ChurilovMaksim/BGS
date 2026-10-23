# Transpose reduction of the right overlap

7 October 2026. Author verification of the parent's proposed shortcut; independent review remains pending. This is an alternative to the direct right-phase derivation in Section 2 of `right_overlap_and_unmasked_insertions.md`. It changes no model and requires no growing-lag estimate.

## Exact finite-dimensional identity

For any matrix U, let A_c(U) be its row-minus-column-c slice and C_U e_c=A_c(U)*. On ordinary complex Hilbert-Schmidt space define the **linear** map JX=X^T. It is a unitary involution: transposition permutes the matrix-unit orthonormal basis without conjugating coefficients. Let P e_c=e_{-c}; P=P*=P^-1. Entrywise,

    A_c(U)^T=A_{-c}(U^T),
    J C_U=C_{U^T} P,
    J R_U J=L_{U^T}.

The frame identity follows since (A_c*)^T=conjugate(A_c), while (A_c^T)*=conjugate(A_c). Therefore for every integer r>=0,

    C_U* R_U^r C_U
      =P C_{U^T}* L_{U^T}^r C_{U^T} P.                 (T1)

In particular their operator norms are equal. This does not assert that the already accepted left-overlap conclusion for U automatically holds for U^T; the analytic hypotheses must be transported as below.

## Reusable hypothesis of the accepted left-overlap proof

Sections 3--7 of the accepted prior proof, SHA256 `11c90c3dac599f63d6508685647db66ba78ebfb280955a61b29917daab7786cb`, prove their fixed-r conclusion for any unitary family satisfying the following kernel hypotheses:

1. A finite-branch approximation V has operator-norm error O(N^-3/2). Each branch has the form kappa_N N^-1/2 exp(2 pi i N S_alpha(x,y)) b_alpha,N(x,y), with bounded kappa_N, real smooth phase, and uniform-in-N amplitude bounds for each fixed number of derivatives on every needed compact set.
2. Its reference phases have a common quadratic part

       Q(x,y)=-(3x^2-2xy+3y^2)/8,

   plus arbitrary branch-dependent affine terms. Every Hessian entry of S_alpha minus its reference phase is globally less than eta=10^-60. Higher fixed derivatives have finite bounds on the compact sets used in stationary phase.
3. The full V kernel is exactly periodic in both sampled indices, including all branch and amplitude contributions. This permits inserting a compact smooth partition of unity before expanding the branches. Individual branch periodicity is not required.
4. The displacement frame is bounded, for example by the eventual actual flatness bound used in the prior proof.

Only the common quadratic Hessian enters the cyclic Hessian and Schur mixed derivative. Arbitrary affine terms change the stationary points and the relevant integer aliases, but not these Hessians. The small global Hessian bound preserves negative definiteness and the reduced mixed derivative interval [1/10,1/3]. Finite derivative bounds on the fixed compact sets then suffice for the same fixed-r Poisson, stationary-phase and discrete TT* argument. The exact number, affine shifts and physical origin of the branches are not further used. All relevant aliases and sampled boundary terms are still retained.

These hypotheses are sufficient for the estimate

    ||C_W* L_W^r C_W||=O_r(sqrt(log(2N)/N)),

for every fixed r>=1. This is a reusable statement extracted from that proof, not a general unitary-ensemble assertion.

## Verification for the literal transposed kernel

Take W_N=U_N^T and V'_N=V_N^T, where U and V are the literal model and its source-pinned four-branch parametrix. W is unitary, and transposition preserves operator norm, so

    ||W_N-V'_N||=||U_N-V_N||=O(N^-3/2).

Use S'_alpha(x,y)=S_alpha(y,x), b'_alpha,N(x,y)=b_alpha,N(y,x). Transposition leaves the original odd-N scalar factor unchanged; it is not complex conjugation. Since Q(y,x)=Q(x,y), the transposed cat reference phase is exactly

    S_alpha^0(y,x)
       =Q(x,y)+(alpha/4)y-(3 alpha/4)x-3 alpha^2/8.

Thus it has the required common quadratic part. Its correction Hessian is obtained by swapping coordinates, preserving every entry bound. Higher fixed derivative bounds on compact sets are transported by the same swap. Full sampled periodicity in the two indices is interchanged, hence preserved, with all amplitudes and aliases included. Flatness is also preserved entrywise; equivalently (T1) at r=0 identifies the two frame norms.

All the reusable hypotheses therefore hold for W_N. Applying the accepted left proof to W and using (T1) proves the right fixed-lag candidate. The source of W is only this exact algebraic transpose; no claim that it is a separately allowed quantization of the original classical map is needed. There is no alteration of the actual U in the target expression.

This supplies the proposed shorter proof of the right estimate and cross-checks the independent right-Hessian calculation. It supplies no growing-r constants and no T16 mask or deconvolution estimate. The fixed-B bound and native first-pinch interface remain exactly as stated in `RIGHT_FRAME_HANDOFF.md`.

`check_transpose.py` verifies the frame/intertwining/compression identities on nonsymmetric exact Gaussian-rational unitary fixtures and verifies the reference Hessian symbolically. These bounded controls do not certify the analytic hypothesis transport or its limit.
