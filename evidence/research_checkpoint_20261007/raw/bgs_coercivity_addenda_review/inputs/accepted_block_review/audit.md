# Independent audit: ordinary matrix-block bosonic coercivity

Date: 7 October 2026. Review directory only; canonical `/workspace/shared/BGS` was read-only. No canonical edit, integration, commit, publication, or universality claim.

## Normalized claim and primary verdict

**Proved as written.** Let N,k be positive integers, U an N×N unitary, Q=U⊗I_k, P_ij=|U_ij|² and J_ij=1/N. Suppose max P_ij≤C/N and ||P−J||₂≤ρ<1. For arbitrary complex k×k strict contractions Z_j, including singular and nonnormal matrices, assume Σ_j Z_j=0 and set Z=diag(Z_j). Then

S=log|det(I−QZQ*Z*)|−logdet(I−ZZ*) ≥ H/(2K²),

H=Σ_j−logdet(I−Z_jZ_j*), K=1+√(C−1)/(1−ρ).

The constant has no dependence on k. The hypotheses imply C≥1 and ρ≥0 whenever the admissible class is nonempty. Strict contraction ensures all stated logarithms are finite: I−ZZ* is positive definite and ||QZQ*Z*||<1 ensures the numerator determinant is nonzero.

This verdict applies exactly to `inputs/matrix_block_extension.md`, SHA-256 `8ff788d6194598606f1c88debe84fffc1571f6de1dfe090b1a7d95170b85eded`. It concerns an ordinary finite-matrix action under an imposed centering condition. It neither constructs a block centering gauge nor identifies these matrices with full supersymmetric fields.

## Frozen dependency closure

1. **Reviewed extension:** the preceding pinned block source, authored in `/workspace/shared/bgs_global_phase_coercivity/matrix_block_extension.md`.
2. **Scalar argument imported in the extension:** `inputs/scalar_report.md`, SHA-256 `b6cf72d2d724e9b39b5726254a542dc417641ab96dd2f539f41b7fc5bbdb0b2e`. Relevant parts are §§2–5: J-unitary polar decomposition, EMI/majorization, inverse bounds, and convex centering. They are also reconstructed below at block size.
3. **Independent scalar verdict:** `inputs/scalar_audit.md`, SHA-256 `1247da77c991a84235ad7aae2a8cc5adb1a74a910c86060e2ce0e7dbb30db236`, originating in `/workspace/shared/bgs_global_coercivity_review/audit.md`, gives “proved as written.” Its seal is copied as `inputs/scalar_audit_seal.json`, SHA-256 `f70a75b3cf3e09a5ee50e9fc1376514ba9bb1de6691cc9c33daa9068a6031cd9`. The scalar audit was pending at this block review's start; its acceptance is now verified against these exact hashes, not presumed.
4. **External mathematical input:** Bhatia's generalized exponential metric increase (EMI), exact version and locator below. There is no additional external theorem needed for the block extension: the trace-convexity claim is proved directly below.
5. **Elementary internal steps:** SVD/polar calculus, determinant cyclicity, spectral trace differentiation, finite-dimensional convexity, Ky Fan norm convexity, scalar log-cosh scaling, and row/column bounds for a bistochastic resolvent.

The scalar gauge/Jacobian claims are not needed by the block theorem and are not promoted to block or super-coordinate statements. `actual_constants_addendum.md` and `radial_translation.md` are separate, unreviewed scopes and do not enter this verdict. The original bosonic source identification is not used to claim that arbitrary blocks represent the full SUSY action.

## Obligation matrix

- **Passed:** exact statement, strict-contraction domain and determinant orientation.
- **Passed:** right polar convention; independence of the polar extension on kernels.
- **Passed:** distinct left/right defect factors and positive exponential boost for nonnormal Z.
- **Passed:** J-unitary polar/Cartan decomposition, with exactly Nk nonnegative parameters.
- **Passed:** all-Ky-Fan EMI at dimension 2Nk; all factors of two.
- **Passed:** block pinching and the resulting sum of block log-cosh functionals.
- **Passed:** real convexity of Φ(A)=Tr logcosh|A|; no operator-convexity assumption.
- **Passed:** real-Hilbert–Schmidt gradient V tanh|A|, including singular and zero A.
- **Passed:** dimension-independent absolute row and column inverse bounds, including nonnormal P.
- **Passed:** Jensen for complex matrix arguments with signed coefficients and unused weight at zero.
- **Passed:** scalar quadratic scaling applied singular value by singular value.
- **Passed:** minimization follows from ΣZ_j=0, without assuming ΣW_j=0.
- **Passed:** k=1, N=1, C=1, zero blocks, singular blocks and arbitrarily close strict-boundary points.
- **Passed within declared scope:** exact finite identities and bounded floating/high-precision diagnostics.
- **Out of scope:** existence/Jacobian of matrix-valued centering; a super-Berezinian; fermions, sources, regulators, Grassmann-integrated bounds, large-N tails, signed factorial comparison or full BGS.

No failed, conditional, or unverified leaf remains in the stated finite-matrix implication after importing the pinned EMI theorem. This is a mathematical proof audit, not formal proof-assistant certification.

## Independent proof reconstruction

### 1. Correct nonnormal polar convention and boost

Put m=Nk. For each site choose a unitary extension V_j of the right polar partial isometry in Z_j=V_j|Z_j|, and define R_j=atanh|Z_j| and W_j=V_jR_j. The zero singular subspace contributes zero, so W_j is independent of the extension. Equivalently W_j=Z_j h(Z_j*Z_j), with h(t)=atanh(√t)/√t and h(0)=1. Then |W_j|=R_j and Z_j=V_j tanh|W_j|.

For W=diag W_j and X=[[0,W],[W*,0]], direct singular-value functional calculus gives

g=exp X=[[C_L,ZC_R],[Z*C_L,C_R]],

C_L=(I−ZZ*)^(−1/2), C_R=(I−Z*Z)^(−1/2).

The identities C_LZ=ZC_R and Z*C_L=C_RZ* follow from the SVD. There is no replacement C_L=C_R; generally they differ. The inverse boost changes the off-diagonal signs. With J₀=diag(I_m,−I_m), both g and diag(Q,Q) are J₀-unitary. Thus T=g^(−1)diag(Q,Q)g has upper blocks

F=C_L(Q−ZQZ*)C_L, G=C_L(QZ−ZQ)C_R,

and FF*−GG*=I_m.

Writing a=det(I−QZQ*Z*), one has

conjugate(a)=det(I−ZQZ*Q*)=det(I−Q*ZQZ*).

The second equality is cyclic determinant invariance. Consequently

|det F|=|a|/det(I−ZZ*)=exp S.

This orientation check remains valid for nonnormal Z. A separate exact control below uses a genuinely nonreal a, so its test is not reduced to a real-determinant special case.

### 2. Cartan factors and the EMI conversion

Take the ordinary polar decomposition T=V exp L, L=log|T|. J₀(T*T)J₀=(T*T)^(−1), so L anticommutes with J₀ and has form [[0,B],[B*,0]]. The polar unitary V is also J₀-unitary, hence is block diagonal. If t₁≥⋯≥t_m≥0 are the singular values of B, the singular values of T are exp(±t_l); those of F are cosh t_l. Therefore S=Σ_l logcosh t_l. No special diagonal or normal-block assumption was used.

Let Y=diag(Q,Q) X diag(Q*,Q*). Then T diag(Q*,Q*)=exp(−X)exp Y and

TT*=exp(−X)exp(2Y)exp(−X).

Apply Bhatia's EMI to Hermitian matrices 2Y and 2X with the Ky Fan 2ℓ norm, for every 1≤ℓ≤m. The left side is 4Σ_(j≤ℓ)s_j(W−QWQ*) and the right side is 4Σ_(j≤ℓ)t_j. Thus

s(W−QWQ*) ≺_w t.

For φ(s)=logcosh s on s≥0, convexity, monotonicity and φ(0)=0 turn these partial-sum inequalities into Φ(W−QWQ*)≤S. This implication follows directly by the positive-part representation of a convex increasing function; it is not an assumption about entrywise spectra.

Pinching onto the N site blocks is an average of N unitary conjugations by block-scalar roots of unity. Convexity and invariance of every Ky Fan norm show that pinching also decreases all singular-value partial sums. Its jth diagonal block is

D_j=W_j−Σ_l P_jl W_l.

Hence

S ≥ Σ_j Φ(D_j).                                                     (A)

The use of Q=U⊗I_k is important: it produces the scalar site coefficients P_jl while preserving each internal k×k block.

### 3. Trace convexity and gradient, including rank deficiency

For any complex rectangular A, put H_A=[[0,A],[A*,0]]. The nonzero eigenvalues of H_A occur in ± singular-value pairs, and remaining zeros contribute nothing to f(s)=logcosh s. Thus Φ(A)=½Tr f(H_A).

For completeness, Tr f is convex on Hermitian matrices for every scalar convex f. If M=tH+(1−t)K, choose an eigenbasis e_i of M. Apply scalar convexity to t⟨e_i,H e_i⟩+(1−t)⟨e_i,K e_i⟩ and scalar Jensen to the spectral probability measures of H and K in each e_i. Summing gives Tr f(M)≤tTr f(H)+(1−t)Tr f(K). This proves the needed trace convexity without claiming that f is operator convex. Since A↦H_A is real-linear, Φ is convex on the real vector space of complex matrices.

The trace derivative is D Tr f(H)[E]=Tr(f'(H)E), with no commutativity hypothesis. It follows, for example, by polynomial approximation to f and its derivative on a compact spectral neighborhood and cyclicity of trace. Here f'(H)=tanh H; the upper-right block of tanh H_A is V tanh|A| for A=V|A|. Therefore

DΦ(A)[B]=ReTr[(V tanh|A|)* B].

The real-Hilbert–Schmidt gradient is exactly V tanh|A|. This expression vanishes on ker|A| and is independent of polar extensions. Smoothness at zero and at repeated/zero singular values follows from the even analytic spectral lift f(H_A), so differentiating individual singular vectors is unnecessary.

In particular ∇Φ(W_j)=Z_j. The convex function F(B)=Σ_j Φ(W_j−B) has gradient −Σ_j Z_j=0 at B=0. Thus

Σ_j Φ(W_j−B) ≥ Σ_j Φ(W_j) for every k×k matrix B.                 (B)

Taking B to be the ordinary matrix mean of the W_j is allowed even when that mean is nonzero. This is the exact resolution of the distinction between ΣZ_j=0 and ΣW_j=0.

### 4. Site resolvent and matrix Jensen

Set A=P−J and R=(I−P+J)^(−1)=I+Σ_(n≥1)A^n. P is bistochastic. Each row and each column of A has squared Euclidean norm ≤(C−1)/N, since ΣP_ij²≤(C/N)ΣP_ij. One smoothing factor followed by ||A||₂^(n−1) and ℓ1≤√Nℓ2 gives every absolute row and column sum of A^n at most √(C−1)ρ^(n−1). Therefore

max_i Σ_j|R_ij|≤K and max_j Σ_i|R_ij|≤K.

This does not use normality, symmetry or reversibility of P. If C=1, bistochasticity gives P=J and R=I exactly.

Let W_j⁰=W_j−mean_l W_l. From R(I−P)=I−J, W⁰=RD in the site index. Because R is real, write each matrix W_i⁰/K as the convex combination of sign(R_ij)D_j with weights |R_ij|/K, filling the unused weight with zero. Evenness of Φ and Φ(0)=0 give the row Jensen inequality. Summing and applying the column bound yields

Σ_i Φ(W_i⁰/K) ≤ Σ_j Φ(D_j).                                    (C)

All arguments of Φ are complex matrices; the coefficients are real. More generally the same proof works for complex coefficients using Φ(e^(iθ)A)=Φ(A), so no real-entry restriction on the blocks is hidden here.

For K≥1, φ(s/K)≥K^(−2)φ(s): φ(s)/s² decreases on s>0, as verified from 2logcosh s−s tanh s≥0. Applying this to each singular value and combining (A), (C), and (B) gives

S ≥ K^(−2)Σ_j Φ(W_j⁰) ≥ K^(−2)Σ_j Φ(W_j).

Finally 1−tanh²r=sech²r implies H=2Σ_j Φ(W_j), proving the stated inequality with no k-dependent factor.

For N=1, centering forces Z₁=0. Zero/singular blocks are covered by the preceding functional calculus. All boundary approaches remain strict and finite; no interior cutoff entered the argument.

## Exact source check and additional-input boundary

Rajendra Bhatia, *On the exponential metric increasing property*, ISI preprint isid/ms/2002/14, May 10, 2002, Theorem 4, equations (15)–(16), printed p.5 (physical PDF page 6). Primary institutional locator: https://www.isid.ac.in/~statmath/2002/isid200214.pdf . Published metadata: *Linear Algebra and its Applications* 375 (2003), 211–220, DOI https://doi.org/10.1016/S0024-3795(03)00647-5 . The preprint numbering, not uninspected published numbering, is used.

The frozen PDF is `inputs/bhatia_emi_2002.pdf`, SHA-256 `dbd04403787b5ff2854d48b4ad83d14b0f46f76e96e7b790006e8843976d5f13`; its complete text extraction is pinned separately. I read the relevant primary text and visually inspected the rendered theorem page (`inputs/emi_page6.png`). The source specifies complex Hermitian matrices and every symmetric gauge/unitarily invariant norm. Its (16) is precisely

|||H−K||| ≤ |||log(exp(−K/2)exp(H)exp(−K/2))|||.

It is applicable at dimension 2Nk with each Ky Fan 2ℓ norm. The inherited source authentication is bound to the accepted scalar audit; this review reused that institutional copy rather than presenting a fresh download. No new external input, block Lie-group theorem, matrix operator-convexity result, or unverified literature citation is needed. No novelty search or priority conclusion is made.

## Independent controls, manifest and limitations

The preserved first control run was inspected before any rerun. A bounded replay then established fresh v2 execution provenance without overwriting that earlier output. `controls/block_controls.py` implements the determinant action directly; it was authored independently of the candidate author's check scripts. Independence here means fresh reconstruction/code review, not a claim of blind discovery or immunity to shared-model error.

Exact controls:

- Five centered rational/algebraic flat cases: three N=2,k=2 nilpotent pairs at radii 1/2, 99/100 and 1−10^(−20), one N=4,k=2 complex noncommuting tuple, and one N=4,k=3 singular nonnormal noncommuting tuple. Exact Sylvester positivity checks keep them inside the strict contraction domain. The flat coercivity condition is tested algebraically as |det(I−QZQ*Z*)|²≥det(I−ZZ*).
- An exact noncentered negative control has every Z_j equal to the same nonzero nilpotent block. It yields S=0 and H>0, confirming why centering cannot be omitted.
- A symbolic nonnormal sharpness control takes U=F₄ and blocks (rE₁₂,−rE₁₂,rE₁₂,−rE₁₂). Its numerator determinant is (1−r²)²(1+r²)² and its denominator is (1−r²)⁴; hence S/H→1/2 as r↑1. This shows sharpness in the arbitrary-block flat family, not in the actual BGS map.
- `controls/exact_algebra.py` separately checks a rational complex N=3,k=2 example whose numerator determinant has nonzero imaginary part, verifying opposite-orientation conjugacy. Its second example uses different rational left/right singular bases, singular values 3/5 and 5/13, and checks C_L≠C_R, both defect identities, J-unitarity, the F/G blocks, FF*−GG*=I and the determinant-action identity exactly.

Floating diagnostics:

- 312 complex128 cases at N=1,2,3,4,5,8 and k=1,2,3,4, including Fourier, Haar, near-identity, rank-deficient nilpotent, and N=1 zero families. Nontrivial radii reach 0.9999. All intermediate inequalities, both inverse bounds and all Ky Fan partial sums were checked at tolerance 10^(−7). The largest relative Cartan/action discrepancy was approximately 4.03×10^(−13); small negative modular margins were around 10^(−15).
- Nine real-direction finite-difference gradient checks cover zero, rank-deficient, and full-rank A at k=2,3,4. Maximum absolute discrepancy is about 1.02×10^(−10) with step 10^(−5).
- Four 120-digit determinant/centering checks use nonnormal noncommuting N=3,k=2 tuples up to radius 1−10^(−60). Three additional high-precision evaluations are of the proved symbolic sharpness formula. High precision is not interval certification or exact arithmetic.

The complex128 samples satisfy unitary/centering constraints only to roundoff; they are diagnostics, not exact members certified by interval bounds. Sampling is not exhaustive, not an asymptotic result, and not the basis of the universal verdict.

The successful provenance records are `runs/replay/manifest.json` and `runs/algebra/manifest.json`; outputs are their respective `results.json`. Both v2 manifests validate with input-before/after hashes and declared output hashes. Each run used a 120-second wall cap, 60-second per-process CPU cap, 4-GiB address-space cap, one-CPU affinity and cooperative numerical-library one-thread caps. Runs completed with exit status 0 in roughly 1.3 and 9.3 seconds. The review directory is not a Git checkout, so its runner revision is honestly “unavailable”; the separately recorded canonical read-only base is d37c92e563d10d25bb1d6ab85bedffc1f160f773 with an existing unrelated dirty overlay.

Reproduction commands and exact software versions are in the contracts, runner manifests and `reproduce.sh`. No analytic formalization, full repository build, actual fixed-coupling asymptotic computation, block centering-gauge computation, or fermionic calculation was performed.

## Remaining gap and strongest safe statement

There is no remaining gap in this pinned ordinary matrix-block inequality. Its strongest immediate consequence is the pointwise suppression

exp(−S) ≤ ∏_j det(I−Z_jZ_j*)^(1/(2K²))

on the imposed centered strict-contraction domain, uniformly in internal block size k. This does not supply a change of variables that puts the original integral on that domain. Matrix/super-coordinate centering and Jacobians, source and regulator poles, Grassmann-integrated estimates, entropy/normalization, signed cancellation and an N→∞ tail theorem remain separate obligations. BGS remains open.
