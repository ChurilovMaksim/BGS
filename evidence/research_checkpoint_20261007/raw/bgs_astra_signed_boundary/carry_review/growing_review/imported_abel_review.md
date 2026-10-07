# Independent audit of the compact projector and uniform Abel bound

Date: 7 October 2026. Scope: internal research review only. No changes were made to `/workspace/shared/BGS`; its observed base was `d37c92e563d10d25bb1d6ab85bedffc1f160f773`, with pre-existing unrelated working-tree changes. No publication, priority claim, or microscopic universality claim is approved by this report.

## Normalized claims and verdict

**Primary verdict for the two frozen claims: proved as written.** This is an independent mathematical reconstruction from the submitted definitions and a checked primary-source kernel, supported by new exact finite checks. It is not external referee certification or a formal proof-assistant certificate.

1. **Uniform Abel bound.** For every integer N≥1, every deterministic U∈U(N), and an independent Haar-diagonal D, put B_N(m)=E|Tr(DU)^m|². Then, for 0<q<1,

   0≤Σ_{m≥1}q^m B_N(m)≤N(1+q)/(2(1−q)).

   Consequently F_N(s)=N⁻²Σ_{m≥1}e^(−2sm/N)B_N(m)≤(2N)⁻¹coth(s/N)≤1/(2s)+1/(2N) for s>0. The stated single-absorption-variable derivative and normal-family consequences hold.

2. **Compact projector/source identity.** With the four local coefficient functionals C and the explicitly ordered supermatrices in the frozen source, for |a|,|b|<1 and arbitrary c,d∈C,

   E_D det(I−cDU)det(I−dU*D*)/[det(I−aDU)det(I−bU*D*)]
   = (∏_i C_i) SDet⁻¹[I−Ztilde(U⊗diag(a,c))Z(U*⊗diag(b,d))].

   Every compact coefficient integral on the right exists absolutely at fixed N, and differentiation on compact source subsets is valid. All boundary contributions are represented by the complete functional; no equality to an uncorrected flat bulk integral is asserted.

The second verdict does not assert dimension-uniform bounds for individual compact sectors. The first verdict bounds the complete matched-source mixed derivative and its derivatives in s, not every independent numerator-source derivative. A later addendum, if any, needs its own review.

## Frozen authorities and source authentication

The reviewed copies are in `frozen/`:

- `compact_projector.md`, SHA-256 `4b821bd3c4d67e0f07b32982be8ec06a5e7592d8574aa34c99f67b382b2060f3`.
- `uniform_abel_bound.md`, SHA-256 `ecd82a74edfabb89f6cbf46054d76c52dd41e5eb2d5a9790771b16a7c033da3f`.

The author confirmed these hashes and held those files fixed during review. The author's checker was read to identify its tested contract, but no code was imported into the independent implementation.

The source kernel was checked against Martin R. Zirnbauer, *Color-Flavor Transformation Revisited*, arXiv:2109.10272v1, printed pp.31–34, especially (4.36)–(4.40) and Table 1. The authorized cached primary PDF is `/workspace/shared/bgs_phase_integral_boundary_audit/sources/z21v1.pdf`, SHA-256 `a275027f5b760a31a8c26b645fb0e73e97d9d7e15b2b23772691c7bdd771ba59`. Its extracted text has SHA-256 `56d01823e8f0eb698aed03622baa425135a796213a1af7f5639b69f639a8890f`. Printed page 32 was rendered and visually inspected; the audit rendering is `source_table_page32.png`.

The source's displayed B-family is rephased by −1 in both the section and its dual in the submitted formula. This preserves their pairing. Its C and D families translate directly using tilde Z_11=−wbar. Table 1 pairs the B-family with tilde Z_10; the distinct tilde Z_01 in the printed (4.43) is indeed inconsistent with that table and is not used here. The local algebra below independently proves the needed pairing, so that typo is not a remaining theorem dependency.

## Dependency graph

**Abel chain:** coordinate-path Fourier averaging → conditional rank-one spectral averaging → cyclic rank-one interlacing → nested-arc factorial bound → positive layer cake for the Poisson kernel → common-phase Fourier orthogonality → Abel estimate → positivity/holomorphy consequences.

Every arrow in this chain is proved below from finite-dimensional facts. No imported localization theorem, external Minami estimate, BGS hypothesis, flatness, gap, or large-N asymptotic is required.

**Compact chain:** explicit four neutral oscillator families → local section/dual pairing under C → tensorized neutral projector → graded oscillator trace/finite Gaussian kernel → determinant-ratio identity → fixed-N compact analytic continuation and source differentiation.

The kernel convention is authenticated in the exact source cited above and is reconstructed below. Finite arithmetic checks support orientation, parity, and source placement; they do not replace this all-N argument.

## 1. Spectral averaging, interlacing, and constants

Fix the phases other than θ_i and write V_θ=e^(iθP_i)V_0. Every monomial contributing to the coordinate diagonal entry (V_θ^m)_ii for m≥1 contains at least one factor e^(iθ): its first matrix factor has row i. It contains only nonnegative powers of that phase. Thus its θ-average vanishes. Negative powers of V give the conjugate Fourier coefficients of the same scalar spectral measure. Its zero coefficient is 1. Uniqueness of finite measures by Fourier coefficients shows

∫〈i,1_A(V_θ)i〉dθ/(2π)=p_A

for every Borel A, not merely connected arcs. Summing over i after conditional averaging gives E N_A=Np_A. In particular fixed arc endpoints have zero expected eigenvalue multiplicity and hence almost surely zero multiplicity.

For completeness, interlacing has a direct degeneracy treatment stronger than the generic-approximation wording in the submitted proof. Let H_c be the cyclic subspace generated by e_i under V_0. H_c and its orthogonal complement reduce V_0; P_i vanishes on the complement, which therefore has exactly the same spectrum before and after the rank-one perturbation. On H_c the old eigenvalues are simple and the overlap weights w_j are all strictly positive. For t=θ−θ' not a multiple of 2π, the determinant lemma gives

Σ_j w_j cot((φ−φ_j)/2)=cot(t/2).

The sign follows from 1/(1−e^(ix))=1/2+(i/2)cot(x/2). In each cyclic spectral gap the left side decreases strictly from +∞ to −∞, so the new spectrum has exactly one point in each gap. Two strictly alternating cyclic point sets have count difference at most 1 in every connected proper arc with fixed endpoint conventions. The unchanged complement cancels, and t∈2πZ is immediate. The whole-circle difference is zero. This proves the needed interlacing for arbitrary U, including repeated eigenvalues and invariant coordinate subspaces.

For A⊆B connected, put h_i=〈i,1_A(V)i〉≥0 and independently resample θ_i to θ_i'. Pointwise,

N_B(V)−1≤N_B(V'),

and hence, conditioning on all other phases and θ_i',

E[h_i(N_B(V)−1)]≤p_A E N_B(V')=Np_Ap_B.

Summing i gives E[N_A(N_B−1)]≤N²p_Ap_B. Nesting identifies the left side with the ordered distinct-eigenvalue count and ensures nonnegativity. It also handles B equal to the whole circle. This proof does not give an arbitrary disjoint-arc product estimate, and no such estimate is used later.

For P_r(φ)=(1−r²)/|1−re^(iφ)|², the superlevel sets are concentric nested arcs, the whole circle, or the empty set. Tonelli applies to the nonnegative layer-cake representation of Σ_{j≠k}P_r(φ_j)P_r(φ_k). For either ordering of the two levels, use the smaller arc as A. Since ∫p_{A_t}dt=∫P_r=1, the off-diagonal expectation is at most N².

The diagonal contribution is exactly N∫P_r²=N(1+r²)/(1−r²). Common-phase invariance gives E Tr V^m=0 and E[Tr V^m Tr V^n]=0 for m,n≥1, while E[Tr V^m overline{Tr V^n}]=0 unless m=n. The Poisson series is uniformly absolutely convergent at fixed r<1, so

E(Σ_jP_r(φ_j))²=N²+2Σ_{m≥1}r^(2m)B_N(m).

Subtracting N² and setting q=r² proves the stated factor 1/2 without losing a sign. Finally (1+e^(−2x))/(1−e^(−2x))=coth x and coth x≤1+1/x prove the finite-N bound.

## 2. Matched-source and measure consequences

For the determinant ratio G, differentiation at c=a,d=b gives

∂_c∂_dG|matched
=E[Tr(V(I−aV)⁻¹)Tr(V*(I−bV*)⁻¹)]
=Σ_{m≥1}(ab)^(m−1)B_N(m).

Each first numerator derivative contributes a minus sign; the two signs multiply to plus. Common-phase orthogonality removes m≠n. Multiplication by ab gives exactly the Abel series. This also remains valid by analytic continuation at a=0 or b=0; one need not divide by ab there.

Let μ_N=N⁻²Σ_{m≥1}B_N(m)δ_{m/N}. For ε>0,

μ_N([0,ε])≤e F_N(1/(2ε))≤eε+e/(2N).

Thus any locally finite subsequential limit on [0,∞) has no atom at 0, by testing continuous functions supported near 0 and then shrinking the neighborhood. For R>0 and s>0,

∫_{t>R}e^(−2st)dμ_N(t)≤e^(−sR)F_N(s/2).

This is uniform exponential-tail control after weighting. It is not tightness of unweighted finite probability measures: μ_N generally has infinite total mass. The submitted discussion is valid in the locally finite/exponentially weighted sense supplied by these inequalities.

For complex s with Re s>0, coefficient positivity gives |F_N(s)|≤F_N(Re s)≤1/(2 Re s)+1/(2N). Fixed-N local normal convergence follows already from B_N(m)≤N². Hence the family is locally bounded and normal. For an explicit derivative bound, at a point with Re s≥σ>0 use a Cauchy circle of radius σ/2:

|F_N^(k)(s)|≤k!(2/σ)^k(1/σ+1/2).

Compact subsets are therefore uniformly controlled in every fixed s-derivative. If convergence to the analytic CUE candidate is separately proved on a set with an accumulation point inside the half-plane, every normal subsequential limit agrees there and hence everywhere by the identity theorem. Subsequence compactness then gives full locally uniform convergence and convergence of derivatives. Fixed-power asymptotics or an expansion only at s=∞ are not such an input.

The diagonal and single-cycle controls in the submitted source are exact. They show why this a priori upper bound does not identify the microscopic limit.

## 3. Local compact pairing and boundary accounting

Fix the odd order γ,β,α,δ. Use the displayed section order f_v e_w when applying C. For the A family, the circle integral gives δ_kl. For B and C, the only selected coefficient is −√(km)z^(k−1)zbar^(m−1), in αδ or γβ respectively. The negative sign in C cancels it, and

∫_{disk}z^(k−1)zbar^(m−1)d²z/π=δ_km/k.

Thus the normalized pairing is δ_km. For D_l and its dual, only the body term z^l zbar^m w wbar survives: its mixed w,wbar derivative gives the same circle pairing δ_lm. The odd cross terms and fourth-order term are killed by C. This includes l=0, where the omitted derivative terms must remain absent.

Between families, either a lone w or wbar, an unselected odd pair, odd total degree, or unmatched angular weight is left, so every cross pairing vanishes. Therefore C[f_v e_w]=δ_vw on the full four-family algebraic span. This is not merely a diagonal check. At fixed occupation k≥1 the four states correspond to the two independent fermion occupations (0,0),(0,1),(1,0),(1,1); the vacuum k=0 has only A_0. The neutral space is infinite-dimensional. The informal final phrase “four-state local projector” in the submitted source should be read as “four-family local projector”; its proof does not truncate that space to four states.

The product C_i is even, so the local functionals commute without extra Koszul signs. It represents exactly the tensorized projector on equality of retarded and advanced total occupation at every site. Its circle support and disk coefficient extractions are part of this identity, not negligible boundary decorations. No invariant positive measure is claimed, and there is no step replacing the signed complete functional by the absolute sum of its sectors.

## 4. Coupled kernel, transpose conventions, and convergence

Write the advanced determinant by transposition as det(I−bD*conjugate(U)), and similarly for d. The retarded one-particle transfer is U with sources diag(a,c); the advanced one is conjugate(U) with sources diag(b,d). Acting on a paired creation kernel therefore sends Z to (U⊗A)Z(U*⊗B). This is the reason for U*, rather than U^T or U, in the submitted kernel.

The local coherent ket is the exponential of

b_+† z b_-† + b_+† α f_-† + f_+† β b_-† + f_+† w f_-†.

Its neutral occupation coefficients give the four displayed sections, including the −lαβ term in D_l. The dual convention in the checked primary kernel supplies the displayed dual sections. Contracting the two exponentials after inserting the transfer gives SDet⁻¹(I−Ztilde(U⊗A)Z(U*⊗B)), by the finite bosonic and fermionic Wick expansion. The bosonic geometric determinant and finite fermionic determinant are the two ordinary factors of this Berezinian identity.

One parity point is important: the coherent matrix-element kernel is ordered e_v f_w, whereas the projector pairing is ordered f_w e_v. For the odd mixed families this reordering contributes −1. Consequently applying C to the scalar kernel gives the graded trace of the transfer, with weight (−1)^(F_++F_−). Those are precisely the signs producing det(I−cDU)det(I−dU*D*) in the original ratio. The A and D families are even and have positive graded weight. Thus the source orientation and the supersymmetric trace are both fixed, not inferred from an N=1 scalar coincidence.

For a completely finite argument, first work coefficientwise in all source variables or at a finite occupation cutoff. The neutral projector identity then involves only finite sums. The bosonic second-quantization operators are trace class when |a|,|b|<1, with nuclear norm bounded by (1−|a|)^(−N)(1−|b|)^(−N) times a finite fermionic factor. The limiting trace is the original ratio average.

Independently, the BB pivot for the inverse Berezinian gives a denominator involving only R=(I−ab Zbar U ZU*)⁻¹. Since every |z_i|≤1, its norm is at most (1−|ab|)⁻¹. The remaining odd algebra is finite-dimensional, and the numerator-source dependence is polynomial. Every selected compact coefficient is therefore bounded on compact source subsets with |ab|<1. Termwise coefficient integration is justified near the source origin; equality of the finite Taylor coefficients and holomorphy then prove (T) throughout its original |a|,|b|<1 domain. This argument does not require the boundary coherent vectors themselves to be Hilbert vectors.

The |ab|<1 right-side domain describes analytic continuation of this branch. It must not be reinterpreted as the value of the original phase integral in a different component with |a|>1 or |b|>1. The submitted theorem does not assert that extension of the raw phase integral.

## 5. Independent exact computations

`independent_checks.py` is new code. It uses exact Gaussian rationals, a sorted-tuple exterior algebra, and a BB-Schur-complement inverse Berezinian. In contrast, the author's checker uses bitmask exterior variables and a supertrace-exponential recurrence. The independent ordinary side is computed from principal minors of U and formal U(1)^N phase projection. A further closed-path dynamic program computes B_N(m) and checks the matched-source derivatives independently.

The implemented quotient discards only monomials in a multiplicative ideal annihilated by C: unselectable local odd supports, w or wbar powers above 1, and mixed odd/w monomials. Such a monomial cannot become selectable by further multiplication with nonnegative exponents. This quotient is exact for the final compact observable; it is not a claim about equality of the full unprojected superfunctions.

Completed finite scopes at report creation:

- N=1, U=i, all source coefficients through t^8.
- N=2, a non-real Gaussian-rational unitary, through t^8.
- N=3, a genuinely complex Gaussian-rational unitary made from three rational rotations and an intermediate phase, through t^6.
- N=4, a coupled non-real Gaussian-rational unitary, through t^6.
- At every run, the 26 displayed unnormalized local sections with A,D indices 0…6 and B,C indices 1…6 give all 676 expected pairings. The mixed norms are exactly 1/k before their √k normalization.
- Complete formal dependence on c,d is retained at each source degree under a=b=t and numerator sources ct,dt. Charge neutrality makes these coefficients an unambiguous check of the corresponding balanced total-degree coefficients of the full-source identity.
- Matched mixed derivatives agree exactly with separately computed squared-trace moments through the stated occupation orders.
- Diagonal and single-cycle Abel controls satisfy the full rational formula on N=1…8 and q∈{1/10,1/3,1/2,4/5,99/100}. These finite controls are not the proof of the bound.

The log files contain exact matrices, every retained source coefficient, software versions, and measured runtimes. The manifest records completed executions and hashes. The N=4 check completed successfully in about 119 seconds. Earlier exploratory logs are retained but excluded from the sealed execution manifest; the listed final logs were parsed afresh and contain the current local-pairing and trace-derivative checks.

## Obligation matrix and strongest safe conclusion

| Obligation | Status |
|---|---|
| Arbitrary finite unitary, including degeneracy and invariant coordinate blocks | Passed |
| Conditional spectral averaging and normalized Haar constants | Passed |
| Rank-one circular interlacing and whole-circle case | Passed |
| Nested-arc factorial count and layer-cake applicability | Passed |
| Abel factor 1/2 and finite-N coth scaling | Passed |
| Exact matched-source derivative identity | Passed |
| No limiting atom at zero and weighted tail control | Passed |
| Normality and every fixed s-derivative on Re s>0 | Passed |
| Four-family pairing, off-diagonal vanishing, l=0 | Passed |
| Source primary-version conventions and Table 1 signs | Passed |
| All-N coupled graded trace and U* orientation | Passed |
| Fixed-N compact integrability and differentiation | Passed |
| Independent finite computation | Passed in the explicit ranges above |
| Generic independent microscopic numerator-source neighborhood bounds | Not addressed by these two sources |
| Dimension-uniform absolute sector bounds or positive saddle measure | Not claimed; not supplied |
| Annealed CUE identification or deterministic BGS | Open and out of scope |

There is no remaining missing implication for the two stated finite-N/a priori claims. The next genuinely needed mathematical input for microscopic identification is model-specific information determining a subsequential limit, or a uniform estimate for a further source observable if that stronger route is pursued. The already established compact identity and Abel upper bound cannot supply such an identification merely by being combined.
