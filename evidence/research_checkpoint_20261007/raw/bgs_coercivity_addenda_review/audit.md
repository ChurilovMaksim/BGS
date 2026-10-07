# Independent audit of three ordinary bosonic coercivity addenda

Date: 7 October 2026. Read-only canonical base: `d37c92e563d10d25bb1d6ab85bedffc1f160f773`, with an existing unrelated dirty integration overlay. This review wrote only its separate review directory. No canonical edit, integration, commit, publication, effective-startup claim, or BGS conclusion.

## Normalized claims and primary verdict

**Proved as written.** Each of the three separately frozen addenda is correct in its stated ordinary-body scope. The accepted scalar coercivity theorem and maintained FM-021 input are inherited at the exact pinned revisions below. The centered matrix-block consequence of the real-absorption addendum now also has a finalized, independently accepted dependency; its acceptance is imported explicitly rather than inferred from the author's wording.

The three claims are:

1. For the unchanged fixed-τ=10^(-80) quantum family, for all sufficiently large odd N, the scalar theorem may take C=5, ρ=1/2, K=5 and c=1/50. Thus S₁(Z)≥H(Z)/50 on the centered strict scalar disk slice. The startup is not made effective.
2. The radial substitution ψⱼ=zⱼ/√(1−|zⱼ|²) takes that slice exactly to Σⱼψⱼ/√(1+|ψⱼ|²)=0, with H=Σⱼlog(1+|ψⱼ|²). It gives the stated individual-coordinate Jacobian and the auxiliary centered coordinate-Lebesgue tail bound. It does not identify this auxiliary measure with the full balanced observable.
3. For every complex d×d matrix A with spectral radius at most one and every real α∈[0,1],

   |det(I−αA)| ≥ ((1+α)/2)^d |det(I−A)|.

   The constant is sharp. For the specified strict bosonic body with N sites and block size k, α=e^(−s/N), s≥0, this yields Sα≥S₁−ks/2. Hence centered coercivity yields Sα≥cH−ks/2. For arbitrary scalar disk tuples, only the bare-action Möbius invariance is used to obtain Sα(z)≥cH(w)−s/2, where w is the unique centered tuple.

Here N,k are positive integers. Strictness, centering and the flatness/singular-gap hypotheses remain exactly those of the imported theorem. The real-absorption determinant inequality itself needs neither centering nor operator-norm contractivity, only its stated spectral-radius bound. No correction to any frozen addendum is required.

## Frozen inputs, authorities and dependency graph

All supplied hashes match. `input_manifest.json` records source paths, byte-for-byte snapshots and SHA-256 values.

- Author packet `addenda_seal.json`: `ba9e7aea1b4d1db92cf0e0c30a76a559129d1c60c99ff4a48286765b3205ec81`.
- `actual_constants_addendum.md`: `23566b86660c089b6005f0165d4a4dee2d0528e7c7e99ee34a831ff475182ae8`.
- `radial_translation.md`: `9a061d64c39cc947e0060d20c96864a301b2fb88b53360cf1e5a44c9434bdcfb`.
- `real_absorption_addendum.md`: `267761a7e1e1f0ba649c976987a2166bf898f72515d000cdc8f1e27a37a2fd4e`.
- Scalar source `report.md`: `b6cf72d2d724e9b39b5726254a542dc417641ab96dd2f539f41b7fc5bbdb0b2e`; accepted scalar audit: `1247da77c991a84235ad7aae2a8cc5adb1a74a910c86060e2ce0e7dbb30db236`.
- FM-021 source `mathematics/position_chain_mixing.md`: `3a589f988defb569d12f075add16dda669c9409dabd4a81f59c4d0b5d5e44b09`, specifically §2's uniform four-branch amplitude/remainder and eventual singular gap.
- Matrix-block source: `8ff788d6194598606f1c88debe84fffc1571f6de1dfe090b1a7d95170b85eded`; finalized block audit: `96556a4d38ac60ef1ebc1fb90fc952db2e60d8d87f13aef96bc884a18d71bcf5`; block review seal: `b6bad3a8492b9bda06ffb9e463b1259f72aa92bfcb5eb9e26b67e29f1d6d37a9`.

Canonical AGENTS, source-of-truth hierarchy, conventions, RESEARCH, claim ledger/registry, results and open-question authorities were consulted read-only. Their relevant status is that FM-021 is an accepted project analytic input with independent internal review and exact finite controls, not an externally refereed or formally verified analytic theorem. TRACE-005 and BGS remain open. The review does not reopen or certify the entire inherited FM-021 parametrix proof.

Dependency closure:

- FM-021 uniform amplitude expansion → eventual C=5; FM-021 singular-gap limit → eventual ρ=1/2; accepted scalar coercivity → actual scalar c=1/50.
- Accepted scalar coercivity + exact radial algebra + the explicitly stated coordinate measure → the auxiliary radial-height tail.
- Elementary scalar eigenvalue inequality + determinant product over algebraic eigenvalues → the universal real-absorption determinant bound.
- Strict body domain + that determinant bound → Sα≥S₁+Nk log((1+α)/2)≥S₁−ks/2. This implication does not use block coercivity.
- Accepted scalar theorem, or separately accepted centered block theorem, → the corresponding cH conclusion.
- Accepted scalar bare Möbius invariance and unique centering → the uncentered scalar cH(w) conclusion. There is no block-gauge import.

There is no new external mathematical input in these addenda. The Bhatia EMI theorem remains an inherited leaf of the accepted coercivity proofs; its frozen primary PDF hash `dbd04403787b5ff2854d48b4ad83d14b0f46f76e96e7b790006e8843976d5f13` was matched to the author packet and the accepted reviews. This audit does not describe that inherited cache verification as a new download or fresh full literature audit. The earlier mapped-domain note is retained only to check consistency of the nonlinear-slice qualification; its source theorem is not newly imported.

## Obligation matrix

| Obligation | Result | Boundary |
|---|---|---|
| Exact frozen targets and inherited acceptance pins | Passed | No author file changed |
| Uniform amplitude remainder survives maximum over grid indices | Passed | Fixed τ; not a numerical startup |
| Triangle bound yields limsup N max|U|²<5 | Passed | No branch-cancellation or pointwise P≈J assumption |
| Eventual singular ρ=1/2 and common threshold | Passed | Inherited FM-021 limit, not eigenvalue gap substitution |
| K=5 and c=1/50 | Passed | All sufficiently large odd N only |
| Exact radial inverse, height and nonlinear slice | Passed | Σψ=0 is not substituted |
| Two-real-dimensional radial Jacobian | Passed | One coordinate; no product over N dependent coordinates |
| Auxiliary measure and cL/2 tail exponent | Passed | Coordinate Lebesgue measure, unnormalized, dimension-growing factor retained |
| α∈[0,1], unit-disk eigenvalues, λ=1 | Passed | No division by a zero determinant/eigenvalue factor |
| Nonnormal/Jordan matrices and spectral radius only | Passed | Operator norm may exceed one in the abstract lemma |
| Sharp determinant constant | Passed | A=−I; strict approximation A=−rI |
| Strict bosonic logarithms and Nk factor | Passed | All blocks strict contractions |
| α=e^(−s/N), exact log-cosh correction and −ks/2 | Passed | Real scalar regulator with the displayed convention |
| Centered k>1 cH conclusion | Passed via pinned accepted block input | No block centering gauge or block Jacobian follows |
| Uncentered scalar conclusion | Passed | Uses bare invariance after the absorption inequality |
| Absorbed action claimed invariant | Not claimed; false in general | An exact counterexample is given below |
| Generic complex-α extension by |α| | Refuted, as stated in the addendum | Auxiliary contraction counterexample only |
| Sources, derivatives, supermeasure, normalized asymptotic tails, BGS | Out of scope/open | None is supplied by this review |

## Independent reconstruction

### 1. Actual-family constants

Let ε=2·10^(−66). The uniform FM-021 expansion has a remainder bounded by M N^(−3/2) once its inherited expansion is valid, where M is independent of grid indices. Since every phase factor has modulus one and |aᵣ|≤1+ε,

√N maxⱼₖ|Uⱼₖ| ≤ 2(1+ε)+M/N.

Squaring and taking the odd-N limsup gives

limsup N maxⱼₖ|Uⱼₖ|² ≤ 4(1+ε)² < 5.

Uniformity of the remainder is what permits the maximum. No cancellation among the four branches is used. For example, after the unknown remainder is small enough that M/N≤1/10, the squared right side is already strictly below 5. This observation proves existence of a threshold; it supplies no numerical M or startup threshold.

Independently, FM-021 gives limsup||P−J||₂≤10^(−64)<1/2, so ||P−J||₂≤1/2 eventually. Take the larger of the two eventual thresholds. This is an operator/singular-gap input, not an assumption that P is normal and not pointwise closeness of its entries to 1/N.

The accepted scalar theorem therefore gives

K=1+√(5−1)/(1−1/2)=5,     1/(2K²)=1/50.

This neither changes the actual quantum operator nor omits small odd dimensions from an exact identity. It simply limits this particular eventual-constant corollary to its stated range. At a finite pre-startup dimension, the abstract theorem can still be used if its own explicit hypotheses are separately established.

### 2. Radial slice, Jacobian and measure

The componentwise map ψ=z/√(1−|z|²) is a smooth bijection from the open disk to the plane, with inverse z=ψ/√(1+|ψ|²). Consequently

1−|z|²=(1+|ψ|²)^(−1),

H=Σlog(1+|ψⱼ|²),

Σzⱼ=0 ⇔ Σψⱼ/√(1+|ψⱼ|²)=0.

There is no linear centering statement for ψ. An explicit strict centered disk tuple is z=(3/5,−3/10,−3/10), whose radial image has sum 3/4−6/√91>0. Positivity follows exactly from 9/16>36/91. This also shows why common centering must be adjusted if one changes to a different slice.

Writing ψ=x+iy and R²=x²+y², the derivative of (x,y)/√(1+R²) has tangential eigenvalue (1+R²)^(−1/2) and radial eigenvalue (1+R²)^(−3/2). Its real determinant is (1+R²)^(−2), including value one at R=0. Thus the displayed d²z formula is exact. It does not license multiplying N such determinants on a codimension-two slice. For N=2, z₂=−z₁ and ψ₂=−ψ₁; the independent-coordinate Jacobian is one factor (1+|ψ₁|²)^(−2), while the false N-coordinate product would square it.

The tail proof avoids this constrained radial Jacobian entirely. It integrates in independent disk variables z₁,…,z_(N−1), with z_N=−Σ_(j<N)zⱼ. This explicitly specified measure is not an unstated Euclidean hypersurface measure. In fact the latter would be N times the coordinate measure because the complex Gram matrix of the graph parametrization is I+11*, of determinant N. No such N belongs in the stated coordinate-measure formula.

On H≥L and with c>0, scalar coercivity gives

e^(−S₁)≤e^(−cH)≤e^(−cL/2)e^(−cH/2).

The last expression contains ∏ⱼ(1−|zⱼ|²)^(c/2). Its final factor is at most one, so removing it and enlarging Ω_N to the full product of N−1 disks bounds the integral by

e^(−cL/2) [∫_(|z|<1)(1−|z|²)^(c/2)d²z]^(N−1)

= e^(−cL/2) [π/(1+c/2)]^(N−1).

Here polar integration with t=|z|² gives π∫₀¹(1−t)^(c/2)dt. Both the half exponent and denominator are correct. At N=1 the domain is the single zero-dimensional centered point: the integral is one at L=0 and zero for L>0, so the same inequality is valid.

For c=1/50 the bound is e^(−L/100)(100π/101)^(N−1). The dimension-dependent factor is retained, and no normalization lower bound is available. This is a tail bound for that positive auxiliary scalar integral only, with no collective-coordinate factor, super-Berezinian, fermionic determinant, source pole, or boundary term silently inserted or omitted from a claimed full observable.

### 3. Determinant absorption and sharpness

For λ=x+iy with |λ|≤1 and 0≤α≤1, direct expansion gives

4|1−αλ|²−(1+α)²|1−λ|²

= (1−α)[(1+3α)(1−|λ|²)+2(1−α)(1+x)] ≥ 0.

Both factors on the right have their stated sign. Taking nonnegative square roots proves the scalar inequality. At λ=1 the right comparison factor is zero and the result still holds; no division is needed. At α=1 the identity holds, including when both sides vanish. The alternative real-part ratio proof is valid only for λ≠1, exactly as qualified in the source.

The characteristic polynomial factors over C, so det(I−αA)=∏ⱼ(1−αλⱼ), with algebraic multiplicity, whether or not A is diagonalizable. Multiplying the scalar inequalities proves the determinant statement. No norm estimate, eigenvector conditioning or Jordan-size factor is required. For example, adding arbitrarily large nilpotent superdiagonal parts to Jordan blocks does not alter the determinant factors; such matrices may have norm far above one while satisfying the hypothesis.

For α<1, λ=−1 gives equality. Thus A=−I attains ((1+α)/2)^d and rules out a larger uniform constant. If strict contractions are required, A=−rI gives the same infimum as r↑1. At α=1 the inequality is identically an equality. The spectral restriction is essential: in dimension one, A=2 and α=1/2 make the left side zero while the proposed right side would be 3/4.

For generic complex α, the stated negative control is exact: A=−3i/4 is a strict scalar contraction and α=i/2 give |1−αA|=5/8, whereas ((1+|α|)/2)|1−A|=15/16. This refutes that generic-contraction extension, not a claim about an actual quantum-map field or all possible complex-source estimates.

### 4. Body domain, microscopic scale and scalar centering

For Z=diag(Z₁,…,Z_N) with each finite block strict, let r=maxⱼ||Zⱼ||<1. Unitarity of Q=U⊗I_k yields

||QZQ*Z*||≤r²<1.

Therefore I−αQZQ*Z* is invertible throughout α∈[0,1], and I−ZZ* is positive definite. The action uses the real logarithm of a positive determinant magnitude in the numerator and the real logarithm of a positive determinant in the denominator; no complex logarithm branch is chosen.

Taking logarithms of the determinant inequality and subtracting the unchanged denominator gives exactly

Sα(Z)≥S₁(Z)+Nk log((1+α)/2).

With α=e^(−s/N), s finite and nonnegative,

(1+e^(−s/N))/2 = e^(−s/(2N)) cosh(s/(2N)).

Thus the correction is −ks/2+Nk logcosh(s/(2N))≥−ks/2. Equivalently, the inequality follows from (1+q²)/2≥q for q=e^(−s/(2N)). There is no expansion in s/N, so the result is valid for every s≥0, not merely a small-regulator asymptotic. The physical interpretation of s under a different regulator convention remains a separate translation.

The accepted scalar theorem supplies S₁≥cH on its centered scalar domain. The separately pinned block audit supplies exactly the same inequality for centered arbitrary nonnormal strict blocks. Those inputs establish A4 in their respective domains. A1–A3 do not depend on either coercivity result.

For a noncentered scalar tuple z, first apply Sα(z)≥S₁(z)−s/2. Only then apply the accepted identity S₁(z)=S₁(w), where w is the unique centered tuple, and the scalar coercivity theorem. This proves A5 without assuming invariance of the absorbed action. The latter is false already at N=1, U=1, z=1/2, α=1/2: e^(Sα(z))=(1−1/8)/(1−1/4)=7/6, while the centered tuple w=0 gives e^(Sα(w))=1.

Finally e^(−Sα)≤e^(s/2)e^(−cH) on the centered scalar domain, so the auxiliary tail proof above gains exactly the stated e^(s/2) factor. This is not a pushforward theorem for an uncentered full measure.

## Independent exact controls and execution boundary

`checks.py` was written before inspecting the author's diagnostic implementation. It imports no author code and uses a larger rational scalar grid, nontriangular rational similarities of Jordan blocks, a genuinely nonnormal block-body fixture, and separate radial/gauge controls. Independence means a fresh reconstruction and implementation of the supplied claims, not blind discovery or immunity to shared-model mistakes.

All 22 named control groups passed:

- 3,349 rational scalar disk cases: 197 points λ=(p+iq)/8 with p²+q²≤64 and 17 values α=j/16. This includes λ=1 at all 17 regulator values and 68 boundary evaluations.
- 140 determinant cases from 28 Jordan/similarity fixtures, dimensions 1–4, seven eigenvalues, and five regulator values. Twenty-one fixtures are both nonnormal and demonstrably not operator-norm contractions. Algebraic-multiplicity determinant formulas are checked exactly.
- 24 exact −I sharpness cases; the spectral-radius and complex-α negative controls.
- Five exact strict centered nonnormal k=2 body cases at N=2, with the strict domain independently certified by a rational Frobenius-norm bound.
- Exact complex scalar Möbius/bare-action control at N=3; the N=1 absorbed-action noninvariance witness.
- Symbolic radial defect and two-real-dimensional Jacobian identities, a nonlinear-centering witness, the N=2 dependent-coordinate Jacobian distinction, and the symbolic disk integral.
- Exact rational FM-021 constant margins, K=5, c=1/50, tail half-exponent 1/100 and volume ratio 100/101.

The N=1 tail endpoint is an analytic convention/domain check recorded alongside the algebraic tests, not a numerical quadrature claim. The universal verdict rests on the proof above and named inherited results, not the finite sample counts.

Execution used Python 3.12.14 and SymPy 1.14.0, exact rational/complex-rational/symbolic arithmetic, and no randomness. The v2 provenance record is `controls/manifest.json`; the declared result is `controls/results.json`. The run completed successfully in about 1.42 seconds under a 120-second wall cap, 90-second per-process CPU cap, 2-GiB address-space cap, one-core affinity and cooperative one-thread caps. The manifest validator passed, including input freshness and result hashes. The review directory is not a Git checkout; the runner honestly records its revision as unavailable while `input_manifest.json` separately records the canonical read-only base and dirty state.

The author absorption implementation was read afterward and is consistent with its advertised 441 scalar, 27 matrix and nine scalar body-shaped cases. Its stored output is pinned but was not rerun or used as evidence of this independent run. No full repository build, analytic formalization, quadrature of a full observable, actual fixed-τ U_N computation, or numerical startup estimate was performed.

## Remaining gap and strongest safe conclusion

No gap remains in the three frozen addenda under their stated and now-pinned inputs. For every sufficiently large odd N in the actual unchanged scalar family, centered strict disk fields satisfy

S_(e^(−s/N),U_N)(Z) ≥ H(Z)/50−s/2,   s≥0,

and the explicitly auxiliary coordinate-Lebesgue tail is at most

e^(s/2−L/100)(100π/101)^(N−1).

The uncentered scalar version uses H of the uniquely centered tuple. The ordinary centered block version uses the accepted block theorem and loses ks/2, with no claim of a global block centering map.

Complex or nonuniform source matrices, source derivatives, inverse factors produced by Grassmann integration, super-Berezinian and boundary terms, entropy/normalization, full balanced radial/torus comparison, all-order signed cancellation, deterministic off-charge control, and BGS remain open. The next consequential check belongs to an explicitly specified full source/measure expression; enlarging the finite determinant sample does not address those missing implications.
