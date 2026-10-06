# Arithmetic translation exclusion: curated independent review

This is a publication-facing copy of the independent internal quantitative review, with transient location references removed. The original review remains unchanged; its SHA-256 is recorded in `record/history/2026/next_proofs_20261006/divisor/provenance/accepted_inputs.json`. The verdict below applies to the accepted derivation at the pinned hash. The consolidated canonical source adds the full model dictionary, an explicit derivation of the already-used kick Egorov estimate, and fixed-divisor/nonzero-centered-projector corollaries; it does not strengthen the reviewed quantitative estimate. The consolidation and portable verifier are separately checked in the integration record.

# Independent bounded audit: quantitative growing-divisor exclusion

## Claim card and verdict

**Primary verdict: proved as written.** This verdict concerns the quantitative compression theorem (T), its stated small-power consequences, and the supporting Sections 2–6 of the pinned candidate. It is an independent internal mathematical audit, not an external referee certificate or formal verification.

For the actual fixed frozen map U_N at τ=10^−80, every odd divisor d≥3 of odd N has a (d²−1)-dimensional normalized-HS orthonormal traceless translation space E^0_(d,N). There exists C_τ independent of N,d and grid labels such that

||Π^0_(d,N) Ad(U_N) Π^0_(d,N)|| ≤ min{1,C_τ(d^262/N)^(1/129)}.

In particular d≤N^(1/524) gives compression at most C_τN^−1/258 and a squared unit-vector residual differing from 2 by at most twice that amount. More generally, d≤N^δ with fixed δ<1/262 gives the stated decay. No unrestricted growing-divisor result, full commutant result, arbitrary projector exclusion or microscopic BGS conclusion follows.

Target: `record/history/2026/next_proofs_20261006/divisor/provenance/quantitative_source_accepted.md`
Pinned SHA-256: 96a0edb7ac319710c9a8b008c528471749fa9f502943ca50eb5e8d7572990d69.
Repository base: 0ffb20cc152d0ddd2620887e46d21d1120b95fd8.

The prior fixed-divisor review remains unchanged, with its original hash preserved in the provenance record. This new candidate adds quantitative inputs absent from the prior qualitative proof; it does not obtain a growing-divisor rate merely by relabeling FM-016.

## Dependencies and obligation matrix

The chain is: physical finite Fourier symbol → complex-flow remainder retaining translation distance → two primitive-mode differential filters → uniform finite type → uniform sublevel area → quantitative Egorov trace intertwining with cutoffs → normalized-HS square-root area bound including aliases → entry estimate → d² whole-span norm conversion.

| Obligation | Verdict and boundary |
|---|---|
| Correct physical symbol and filter support | Passed; independent Q(i) Laurent expansion |
| Complex strip and Cauchy bounds | Passed; reconstructed below |
| Extra derivative and factor r | Passed; retained at all required orders |
| Mixed partial finite type | Passed, order 16 |
| Uniform sublevel bound | Passed by explicit directional/patch/slice argument |
| Uniform Egorov of conjugated translations | Passed from maintained O7 and uniform fixed-map composition |
| Cutoff derivatives through order 3 | Passed; ε^−3 and ε^−4 costs |
| Fourier alias-tail estimate | Passed; N^−2H³ in two dimensions |
| HS square-root loss | Passed; no positivity shortcut |
| Optimization and dimension loss | Passed; exponent 262/129 includes d² |
| Effective numerical startup or unrestricted d_N | Not claimed and not established |

## 1. Analytic remainder with the shrinking translation factor

The physical g and exact Fourier moment were already independently reconstructed in the fixed-d audit. A second independent polynomial assembly here verifies the rectangular frequency support used by the filters. The mean does not affect X_g. At complex |Im q|,|Im p|≤ρ=1/100, the support |k|+|l|≤10 gives exponential amplification <2. Thus complex Euclidean vector and Jacobian norms are bounded by 4π·52<1000 and 8π²·52<5000 respectively. The same Fourier triangle inequality applies to complex arguments; no real-only norm bound is reused without justification.

For initial points in the half-strip, the real-time complexified flow exists throughout |t|≤|κ|<10^−80 and stays in the full strip: before any possible exit its displacement is at most 1000|t|<ρ/2, which prevents exit and allows continuation. The integral equation and the Jacobian bound give a holomorphic remainder R with ||R||≤2,500,000κ² on the half-strip. Cauchy on polydiscs of radius ρ/4 then gives the stated α!400^|α| derivative bound at real points.

For any real translation representative ξ and r=||ξ||∞, integrate the derivative along x+sξ, 0≤s≤1. For a derivative of total order j the translated remainder has bound
2r·2,500,000κ²·(j+1)!400^(j+1).
For normalized D derivatives divide this by (2π)^j; replacing 2π by 6 only enlarges the bound. Our check independently maximizes this expression over every j=0,…,16, rather than assuming the endpoint controls all orders. After the filter coefficient norm ≤6 the bound is <10^55κ²r. Ordinary derivatives through order 17 similarly have maximum prefactor <10^70. Thus the r factor genuinely survives uniformly as d grows; there is no hidden d≪1/κ hypothesis.

For the leading term, the finite Fourier support gives ||∂^αX||≤1000·100^|α| through order 18. Translating an order-17 derivative costs one extra derivative and a factor ≤2r, giving after normalization at most 2·1000·100^18=2·10^39. The normalized remainder contributes <10^70|κ|<10^−10. Hence 10^40 is a valid generous upper bound for all derivatives of normalized translated displacement through order 17. It is independent of ξ,η,N,d and additive integer constants.

## 2. Filters and pointwise finite type

At frequency (k,l), D_q,D_p act by ik,il. Independently evaluating the two filter polynomials on every one of the 45 points in the stated rectangular support gives precisely:

- P_q: only (-1,0) survives, multiplier −4/3;
- P_p: only (0,-1) survives, multiplier −2;
- both have total degree 16, no constant term, and coefficient ℓ¹ norm 6409325/1143072<6.

The physical primitive coefficients are 1/20−i/200 and (-3−4i)/1000. The relevant vector-field components therefore have primitive coefficient modulus at least π/100. For whichever coordinate realizes r, |e^(2πiξ_j)−1|≥4r. The isolated leading filter output has modulus at least 4π|κ|r/75>4|κ|r/25 at every x. There is only one surviving exponential, so no location-dependent cancellation remains.

Subtracting the translated-remainder filter error <10^−25|κ|r and dividing by the filter coefficient sum <6 gives a maximum mixed derivative strictly greater than |κ|r/100. Constants involving ξ−η−n are annihilated because both filters lack a constant term. The chosen scalar component depends only on which coordinate realizes r. It is a real scalar function even though complex-coefficient filters were used to obtain a derivative lower bound. Applying a complex filter is legitimate: the modulus of its value is at most its coefficient ℓ¹ norm times the maximum modulus of the real derivatives.

Consequently normalization by |κ|r leaves uniform positive finite type of order at most 16 and a uniform C^17 derivative upper bound. Neither an unquantified compactness argument nor mere nonvanishing of a Fourier coefficient is being mistaken for pointwise finite type.

## 3. Uniform finite type implies the stated sublevel estimate

Here the additive constant can be arbitrarily large after normalization, but the argument never needs a bound on it.

For each order j≤16, the homogeneous polynomial in t given by (∂_q+t∂_p)^j f has coefficients equal to fixed binomial multiples of the mixed derivatives. Its values at t=0,…,j determine those coefficients through a fixed invertible Vandermonde matrix. Thus if one order-j mixed derivative has size at least a, at least one of finitely many fixed directional derivatives has size at least c_j a. Normalizing those directions changes constants only by a fixed factor.

The uniform order-(j+1) upper bound supplies a uniform Lipschitz bound for that directional derivative. At any patch center choose its successful direction and order; on a sufficiently small fixed-radius ball the same derivative remains bounded below in modulus by half its center bound. A fixed finite grid of such balls covers the torus, independently of f. One can work in small lifted charts to avoid torus coordinate seams.

On each convex patch, slices parallel to that direction are intervals. If the jth derivative on an interval has modulus ≥λ, its sublevel set {|f|≤s} has length at most C_j(s/λ)^(1/j): if its measure were μ, choose j+1 suitably separated points from that set, spaced at least a constant times μ/j; their divided difference is bounded by C_js/μ^j, while the mean-value formula and the derivative lower bound give at least λ/j!. This proves the one-dimensional estimate without assuming the sublevel set is an interval or connected.

Integrate along transverse slices and sum over the fixed finite cover. For 0<s≤1, s^(1/j)≤s^(1/16). Hence area{|f|≤s}≤C_(a,A)s^(1/16), uniformly over the entire normalized family. For s>1 use the trivial area bound and enlarge C. This verifies precisely the uniformity required by (3.4)–(3.5).

The four embedding coordinates compare displacements modulo integers. Near-coincidence |B|≤2ε implies the selected scalar displacement is within Cε of one of a uniformly bounded number of integers: ξ,η have bounded representatives and u has uniformly tiny norm. Summing these scalar sublevel bounds and changing variables by area-preserving Ψ gives area{|B|≤2ε}≤C_τmin{1,(dε)^(1/16)}, since a nonzero d-grid representative has r≥1/d. For larger ε the same bound follows by enlarging C_τ; no small-angle implication is used outside its valid range.

## 4. Quantitative quantum overlap, including composition and aliasing

The exact raw translation Egorov map of T_N((N/d)(a,b)) is (q,p)↦(q−a/d,p+b/d). In the K*Op(f)K convention, products have map F_(AB)=F_A∘F_B. Therefore Q T Q* has map H_ξ=Ψ∘t_ξ∘Ψ⁻¹ exactly in the direction used in the candidate.

Maintained FM-018(O7) gives the kick generator error C_gN^−2||a||_(H5). Duhamel on fixed time gives the corresponding kick Egorov bound. To compose Q,T,Q*, the intermediate symbols belong to uniformly bounded smooth families: translations preserve all Sobolev norms, and composition by the fixed smooth Ψ and Ψ⁻¹ has uniform H5 bounds. The derivatives of H_ξ are bounded uniformly for all ξ because the translations are inserted only between these two fixed maps. Thus the O(N^−2) trace intertwining error for each fixed embedding coordinate is uniform in d,N and labels.

For the product remainder, exact integer-labeled ordinary Weyl multiplication remains valid even past the fundamental Fourier box. Bounding its phase difference by C|k||l|/N gives the first Fourier moments. In two dimensions,
Σ|k||ĉ(k)|≤C||c||_(H3), since Σ|k|²(1+|k|²)^−3 converges.
Likewise Σ|ĉ(k)|≤C||c||_(H2). These prove (5.2) and the operator-norm bound used with (5.1), without eliminating aliases. Cyclic normalized trace then yields (5.3).

The cutoff is a fixed smooth function of B/ε, so its order-s derivatives cost at most ε^−s. The smooth divided vector z↦(1−χ(|z|²/ε²))z_j/|z|² has order-s derivative bounded by C_sε^−s−1, globally: it vanishes near zero, scales on the transition shell, and its derivatives decay away from that shell. Uniform fixed-order derivatives of B then give the candidate's C³/C² costs, hence N^−1ε^−4+N^−2ε^−3 for the good-set trace.

For the bad set, HS Cauchy–Schwarz uses ||K*L||_N=1 and gives ||Op(χ_ε)||_N, not its trace and not the area itself. The centered N×N Fourier box consists of exactly orthonormal Weyl modes under normalized HS, including odd composite N. Its truncated normalized-HS norm is bounded by ||χ_ε||_L². Outside the box,
Σ|ĉ(k)|≤(Σ_outside(1+|k|²)^−3)^(1/2)||c||_(H3)≤CN^−2||c||_(H3).
The normalized-HS norm of each Weyl mode is one, so triangle inequality controls all aliased tail contributions. Thus the bad-set term is at most sqrt(area{|B|≤2ε})+CN^−2ε^−3. This validates the essential square-root loss and all three terms of (5.7).

## 5. Optimization and scope

With ε=N^−32/129 d^−1/129≤1, both (dε)^1/32 and N^−1ε^−4 equal N^−1/129d^4/129. The remaining term is N^−162/129d^3/129 and is smaller for N,d≥1. Therefore every compression entry is bounded by C_τ(d^4/N)^1/129.

The m=d²−1 basis elements are exactly orthonormal and traceless; the cat merely permutes their labels. The matrix norm estimate ||E||≤||E||_F≤m max|E_ij| genuinely loses d². Its exponent is 2+4/129=262/129, giving (T). Compression of the HS-unitary Ad(U_N) also has norm ≤1. The residual identity and substitutions d≤N^δ give (T1)–(T2) exactly.

This is a polynomially growing family with an extremely small permitted exponent and constants depending severely on literal τ. The proof does not assert a useful numerical startup threshold. A zero centered projector has no normalized residual; nontrivial projectors actually lying in the indicated algebra are the relevant sector interpretation. Approximate membership in the span would require an additional error estimate, not supplied or claimed here.

## Computation, provenance and remaining gap

Independent review controls used a separate exact symbolic reconstruction. The promotion overlay additionally includes a standard-library portable reconstruction and fresh execution receipt. The historical independent check_filters.py reconstructs g, checks all filter support values, both exact ℓ¹ norms, every required translated-remainder order, the normalized derivative upper bound, the finite-type lower-bound arithmetic and exponent algebra. That historical script uses SymPy 1.14.0 exact Q(i)/rational arithmetic, without randomness. It neither computes a flow at tiny τ nor certifies the asymptotic theorem; the analytic reconstruction above is essential.

The prior fixed-d review supplied the directly checked primitive coefficients, fixed-model conventions and FM-016 overlap architecture; this review rechecks and quantitatively strengthens every newly load-bearing estimate. No external theorem beyond the elementary analytic/ODE/Fourier facts explicitly reconstructed here is used as an unchecked leaf. No repository files were edited, and prior review artifacts were preserved.

**Exact remaining gap in (T): none identified.** The pinned accepted source hash was rechecked during consolidation; the canonical editorial additions are described in the integration record. The next mathematical extension would need better or different estimates to go beyond the stated δ<1/262 range; that extension is not established by this review.
