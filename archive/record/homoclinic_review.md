# Independent audit: exact stationary potential and homoclinic cocycle

Date: 6 October 2026. Independent internal mathematical audit, not external refereeing or formal verification. All evidence is outside the canonical repository. No canonical source or frozen candidate was edited.

## Normalized claim and primary verdict

**Primary verdict: proved as written.**

For the actual Hamilton–Jacobi branches attached to the unchanged odd-dimensional quantizer, at the literal fixed coupling τ=10^−80, the frozen candidate establishes (H1)–(H10): one Hölder stationary potential representing all real periodic action corrections; its exact homoclinic representation of the accepted unit-winding defect; the translation/renormalization compatibility identities; a full explicit C^α quadratic remainder; a nonzero actual Fourier orbit sum; and the resulting L² additive-gauge and distributional-derivative obstructions.

The target is exactly `mathematics/exact_homoclinic_potential.md (original frozen source)`, SHA-256 `0efc497da35a1ca67ae7998d274179e632aea4d99a49a3942e875284aea4dac7`. The source manifest was verified against every dependency's bytes. Its candidate remained unchanged at the end of the checks.

There is no missing load-bearing implication in this scoped target. In particular, the full Hölder remainder, the exact real stationary action rather than a phase modulo one, and the winding-to-homoclinic identification all survive reconstruction. The word “distributional” in the regularity conclusion is essential.

This result does not prove or disprove a measurable multiplicative gauge for exp(2πiND∞), does not identify the inverse-fibre pushforward density or its Fourier decay, and does not estimate the complete quantum weights, complete displacement sum, signed Heisenberg trace hierarchy, or BGS.

## Claim card and dependency graph

- Domain: the label torus T², S=[[3,4],[2,3]], λ=3+2√2, β=29/5 and α=log β/log λ∈(0,1).
- Coupling: one prescribed positive real value τ=10^−80. A Taylor integral along 0≤t≤τ is used solely to certify an error at this value.
- Quantizer: exactly the model in `BGS/mathematics/fixed_map_path_model.md`; no replacement of the raw Weyl sign, ordinary half-shift, or operator.
- Stationary correction: the unique bounded sequence solving (L8) with source s=0. Its background sequence can be unbounded; the correction and forcing are bounded.
- Cohomology target: the translation difference F(z+d)−F(z), d=(1/√2,−1/2) modulo Z². It is not the dynamical coboundary F−F∘S, though a hyperbolic Fourier orbit enters the obstruction.
- Fourier convention: V̂(k)=∫V(z)e(−k·z)dz; frequencies evolve by Sᵀ, consistent with the project's C_Af=f∘Aᵀ convention when A=Sᵀ.

Dependencies:

1. Exact model and global HJ graph/gluing + source C² Taylor certificate → actual real edge correction Rτ, with globally uniform bounds.
2. Edge bounds + exact Green kernel + β-weighted resolvent → unique bounded correction, shift covariance, torus periodicity and Hölder regularity.
3. Finite stationary equations + exact quadratic Hessian → (H1)–(H2), including one- and two-site cycles.
4. Homoclinic representatives + Hölder continuity + finite locality on dense periodic grids → (H3)–(H4).
5. Absolutely convergent differences → compatibility (H5).
6. Full Hölder composition/product estimates + exact actual-symbol isolation → (H7)–(H8).
7. Uniform homoclinic summation + Fourier change of variables → (H9).
8. Nonzero orbit sum + nonvanishing translation multipliers → additive L² obstruction and (H10).
9. Accepted actual monotonicity + (H10) → a nonzero singular component of the positive derivative measure ∂qH.

No external Fourier-decay theorem, cohomological classification theorem, or spectral theorem is imported. The Fourier obstruction is reconstructed directly below. The inherited HJ/ODE and locality arguments were read at their authoritative sources; prior review verdicts were not used as mathematical premises.

## Obligation matrix

| Obligation | Status | Decisive check |
|---|---|---|
| Fixed τ and unchanged quantizer | Passed | Exact raw-symbol action and HJ sign in the canonical sources |
| Global branch domain and integer gluing | Passed | Explicit quadratic increment and periodic HJ forcing |
| Existence, uniqueness, shift covariance, periodicity | Passed | Contraction on bounded corrections, not unbounded backgrounds |
| Uniform Hölder estimate before s-integration | Passed | β-weighted inverse and explicit geometric split |
| Real stationary correction and m=1,2 | Passed | Linear cancellation and cyclic Hessian with repeated/self terms |
| Finite-to-homoclinic identity on every label | Passed | Uniform centered sums plus dense-grid continuity argument |
| Compatibility identities | Passed | Reindexing/telescoping absolutely convergent differences |
| Full H7 norm at literal τ | Passed | Explicit independent sup-plus-seminorm certificate below |
| Support isolation and actual A_v≠0 | Passed | Exact symbol coefficient and all-time orbit escape |
| Fourier factor, sign, and negative times | Passed | Independent Fourier transformation and Pell congruences |
| Additive L² obstruction | Passed | Infinitely many equal nonzero Fourier coefficients |
| Distributional q derivative not L¹ | Passed | Exact nonzero Fourier-coefficient limit |
| Singular derivative measure | Passed | Positive finite measure plus failure of absolute continuity |
| Multiplicative gauge and inverse-pushforward decay | Out of scope | Additive obstruction provides neither conclusion |
| Full quantum weights and BGS | Out of scope | No corresponding cancellation estimate in this claim |

## 1. Actual branch gluing and the exact stationary potential

Write S₀⁰(x,y)=−(3x²−2xy+3y²)/8. For integers a,b, direct expansion gives

S₀⁰(x+a,y+3a+4b)−S₀⁰(x,y)
= b x−(2a+3b)y−3a²−8ab−6b².

The x derivative shifts by the integer b. Because g(x+a,p+b)=g(x,p), the shifted HJ solution minus this time-independent polynomial solves exactly the original initial-value problem. Uniqueness of the global characteristic graph therefore proves

Rτ(x+a,y+3a+4b)=Rτ(x,y).

This is gluing of the correction, not a false periodicity assertion for the full quadratic phase. The source certificate is uniform on the whole real plane. Evaluating its local gradient on an unbounded cat background is legitimate. Only the correction sequence belongs to ℓ∞; no inverse on ℓ∞ is applied to an unbounded background.

For source s=0, shifting the background orbit by one time step shifts the local equation. Uniqueness gives u_j(z)=u_0(S^jz). Integer changes of z give the displayed gluing at every neighbouring pair, hence leave the bounded solution unchanged. Thus u is periodic and (H1) is a genuine torus function.

For z∈G_m, choose the unwrapped cat coordinates q_j=(S^jz)_q, retain the final branch n_q=q_m−q_0, and retain the corresponding winding n_p. The corrected coordinates are q_j+u_j, with u_m=u_0 by uniqueness and gluing. This is the unique finite stationary correction: periodizing the local equation reproduces exactly the finite cyclic gradient, including both occurrences when m=1 or m=2.

The cat action is quadratic and stationary at the chosen cat lift with its branch and winding terms. Therefore every linear term in the displacement cancels exactly. Its Hessian is −K₀, K₀=(6I−P−Pᵀ)/4. The remaining quadratic term is

−½uᵀK₀u=Σ_j[−¾u_j²+¼u_ju_{j+1}].

For m=1 this is −u₀²/2, consistent with K₀=1. For m=2 it is −¾(u₀²+u₁²)+½u₀u₁; the repeated neighbour must be combined, as it is here. The nonlinear remainder is exactly the sum of Rτ on the corrected neighbouring coordinates. This proves (H2) as an equality of real action corrections. Gluing may change the separate stationary phases by a τ-independent integer, which cancels in their difference; there is no residual modulo-one ambiguity in Δτ,m.

## 2. Homoclinic identity and compatibility

For j≥0 a representative of S^jd is

λ^−j(1/√2,−1/2).

For j=−r<0 a congruent representative is

λ^−r(1/√2,+1/2).

Indeed the differences from the raw backward iterate are integer vectors, by a_r²−2b_r²=1 with a_r=(λ^r+λ^−r)/2 and b_r=(λ^r−λ^−r)/(2√2). These representatives give a summable majorant C[V]αβ^−|j| for the terms in (H3), uniformly in z. Thus the series is absolutely and uniformly convergent and defines a continuous function.

The canonical lift d_m=(b_m/(a_m−1),−1/2) obeys

b_m/(a_m−1)=(1/√2)(1+λ^−m)/(1−λ^−m),

so d_m−d=O(λ^−m). On the centered interval I_m, |j|≤m/2, and ∥S^j∥≤4λ^|j|. Replacing d_m by d in the centered sum therefore costs at most C m β^−m/2. Its omitted homoclinic tails cost Cβ^−m/2. Both are uniform on the entire label torus.

On G_m the centered finite sum equals Δτ,m(z+d_m)−Δτ,m(z) by (H2), since both labels are m-periodic. Accepted locality gives its uniform convergence there to the function defined directly by the source-s equation. The rectangular periodic grids have mesh O(λ^−m/2). For any z choose z_m∈G_m with z_m→z: continuity of both limits, together with the two uniform errors, proves equality at z. This supplies the precise dense-grid argument behind (H4); equality merely on a changing finite grid without these uniform estimates would not suffice.

For any homoclinic translations d,e, exponential tail representatives justify all sums separately. Subtracting and adding V(S^j(z+d)), shifting j, and comparing the two orders of translation prove (H5). Cayley–Hamilton gives S²d−6Sd+d=0. No infinite stationary action or conditionally rearranged action sum is used.

## 3. Independent full Hölder remainder certificate

The HJ source proves, with the correct positive sign,

∥Rτ−τf∥C²≤5·10^49τ²,
f(x,y)=g(x,(y−3x)/4)/(2π).

The canonical derivative bounds for g give every component derivative of f through order two a bound F=10^10. This is considerably looser than needed.

For completeness, the β resolvent bound can be used before integrating in s. The exact Green sum is

Lβ=(λ+β)/(√2(λ−β))<300.

With ∥E∥β<14η and η≤2·10^10τ, the inverse norm is at most 301. Holding correction offsets fixed, the local gradient as a function of the cat point at site j has bounded/Lipschitz difference at most 32η min(1,dist); this follows directly from the two edge gradients and the matrices S,S^−1. Thus the correction difference is bounded by

301·32η Σ_j β^−|j|min(1,4λ^|j|dist(z,z′)).

The explicit split constant is less than 500, since

2λ/(λ−β)+2β/(β−1)<500.

The factor 4 costs at most 4^α≤4. Consequently [u_0]α≤19,264,000η<10^9η, including at s=0. This estimate was not inferred backwards from a bound on the integrated defect.

Use the maximum torus metric and the full norm ∥h∥∞+[h]α. Set Y=(q,3q+4p), w=(u(z),u(Sz)), and

M=4·10^10τ,  B=2·10^20τ,  L=7.

Then ∥w∥∞≤M, [w]α≤B and local lifts of Y have Lipschitz constant L. The bound on composition with S uses ∥S∥∞=7<10. Nearest torus lifts, followed by the established integer gluing, make these chartwise inequalities valid globally; the chart seams introduce no jump.

For A(z)=f(Y+w)−f(Y), the integral identity A=∫₀¹Df(Y+tw)w dt gives the explicit full-norm bound

∥A∥Cα≤2FM+4FM(L+B)+2FB≤10^33τ.

The factors 2 and 4 account for the two-coordinate differential and Hessian in the maximum norm. This estimate retains both the variation of w and the variation of Df; an unscaled Hölder composition bound alone would lose the needed factor τ.

For E=Rτ−τf and A₀=5·10^49τ²,

∥E(Y+w)∥Cα≤A₀[1+2(L+B)]≤10^53τ².

Finally the quadratic term Q=−¾u²+¼u(u∘S) satisfies

∥Q∥Cα≤M²+2MB≤10^33τ².

Since f(Y)=g(q,p)/(2π), these three inequalities give

∥Vτ−τg/(2π)∥Cα
≤τ[2FM+4FM(L+B)+2FB]+5·10^49τ²[1+2(L+B)]+M²+2MB
≤10^60τ².

Every inequality was also evaluated exactly with rational arithmetic at τ=10^−80. In fact the aggregate is below 10^54τ²; the stated 10^60 certificate has ample slack. This is a full Hölder norm certificate, not a supremum-only or unspecified asymptotic remainder.

## 4. Nonzero actual orbit sum

Expanding the actual canonical symbol with rational complex coefficients gives exactly 32 nonzero modes and

c_(1,0)=1/20−i/200.

All its p frequencies satisfy |l|≤1. For k_j=(Sᵀ)^j(1,0), the second coordinate is sign(j)·2b_|j|; at every nonzero time its absolute value is at least 4. The recurrence increases b_r>0 for r≥1, proving isolation for all times rather than by finite sampling. The orbit of −v is separate because the first coordinate of every k_j is positive.

If R=Vτ−τg/(2π), a half-period translation in direction k gives

|R̂(k)|≤½[R]α(1/(2|k|))^α≤[R]α|k|^−α.

Since |k_j|≥λ^|j|/2,

Σ_j|R̂(k_j)|≤2(1+2/(β−1))·10^60τ²<3·10^60τ².

This proves absolute orbit-sum convergence and the error in (H8). A purely rational lower margin is enough: |c_v|≥1/20 and π<4 imply

|A_v|≥τ/160−3·10^60τ²≥τ/1000>0

at exactly τ=10^−80. No continuity argument with an unspecified permissible time is being substituted.

## 5. Fourier identity, additive gauge, and derivative measure

For the j-th difference in (H3), change variables y=S^jz in its Fourier integral. Its coefficient at k is

[e(k·d)−1] V̂τ((S^−T)^j k).

Uniform convergence allows termwise integration, and reversing the bilateral index proves (H9). The factor is independent of j; overlooking that cancellation would give the wrong small-divisor problem.

For j≥0,

k_j·d=a_j/√2−b_j=λ^−j/√2.

For j=−r, the raw phase is a_r/√2+b_r, which differs from λ^−r/√2 by the integer 2b_r. Thus every multiplier on this isolated orbit is nonzero, including negative time and j=0. Hyperbolic orbit sums are invariant under changing the representative k_j, so

D̂∞(k_j)=[e(λ^−|j|/√2)−1]A_v.

If D∞=F(·+d)−F+c with F∈L², each nonzero-frequency equation forces F̂(k_j)=A_v. The k_j are infinitely many distinct integer vectors. Bessel's inequality contradicts A_v≠0. The arbitrary additive constant has no effect at these frequencies.

For j→+∞, a_jλ^−j→1/2. Consequently

2πia_jD̂∞(k_j)→(2πi)²A_v/(2√2)=−√2π²A_v≠0.

These are precisely the Fourier coefficients of the distribution ∂qD∞. If it were represented by an L¹ function, approximation by trigonometric polynomials in L¹ would force these coefficients to tend to zero. This gives (H10) without any differentiability assumption on D∞. It rules out C¹ and W^(1,2), because on the compact torus an L² derivative is also L¹. It does not assert nonexistence of pointwise derivatives almost everywhere.

The actual monotonicity theorem makes H(q,p)=q+D∞(q,p) a continuous increasing degree-one lift in q. Fibrewise Stieltjes differentiation and integration in p give a positive finite measure ∂qH of total mass one on T². Since ∂qH=dqdp+∂qD∞, an absolutely continuous ∂qH would give an L¹ representative for ∂qD∞. This contradicts (H10), so its Lebesgue decomposition has a nonzero singular component.

This derivative measure is not μτ=(H mod 1)_*Leb. The latter is determined by inverse fibre homeomorphisms. No regularity or Fourier-decay conclusion about μτ follows from the singular part just proved. Likewise an exponential multiplicative gauge can have integer-valued winding terms on taking logarithms; the additive L² obstruction does not exclude it.

## 6. Source binding and attribution

The project's current status authority still leaves TRACE-005 and BGS open. `AGENTS.md`, `SOURCE_OF_TRUTH.md`, the repository conventions, research brief, claim-ledger/registry, results index and open-question context were inspected. There is no `.mathbox` ledger in this checkout, and no research-state or canonical status write was attempted.

The inherited cohomology methods are present at the stated source locators:

- `BGS/mathematics/periodic_point_trace_comparison.md`, Section 10, Theorem 6 and its displayed Fourier-tail construction, SHA-256 `8d42ade3a38add117ca7b2c58d985a84f7af0136c55b2478ac69357767c8d7cc`. This proves a smooth hyperbolic dynamical-coboundary criterion using oriented frequency orbits. The current candidate correctly attributes the orbit-sum method; it does not apply that smooth theorem to the merely Hölder stationary potential.
- `BGS/mathematics/pell_smooth_resonance.md`, Section 2, equation (10) and the subsequent bilateral tail construction proving Theorem B, SHA-256 `1e560706fa334ade2e307b9b0500165e1626d632b9f7e85988cfb11a2ec424ea`. This is a prior signed-orbit/even smooth cohomology treatment. The present non-even actual symbol instead uses oriented orbits and retains its complex Fourier phase.
- `BGS/mathematics/extremal_resonance_nondegeneracy.md`, Section 6, Corollary 2, SHA-256 `76b66aeb59e8b49fea086e0e8ea9a998dff939f82e6d3adbde8440172963cc82`. This explicitly records the nonzero constant Fourier-tail obstruction to an L² transfer. It is attributed as a prior method; its bracket theorem is not needed for the current translation cocycle.

All remaining source hashes, including the exact model, HJ certificate, accepted locality, transversality, and actual-symbol support proof, are verified in `check_results.json` against the frozen source manifest. The candidate is correctly a new application of prior methods to an exact nonlinear stationary object, not a novelty claim for Fourier cohomology itself.

## 7. Reproducibility, scope, and remaining boundary

Executed command:

`python computations/verification/exact_homoclinic.py` (portable replay; original audit command is retained in historical provenance)

Result: 366 passing exact controls, using integer/Fraction arithmetic and rational pairs for Q(√2) and complex coefficients. The checks include j=0,…,64 homoclinic representatives, phase congruences and Pell identities; exact full expansion of the fixed symbol; cyclic quadratic energies for m=1,…,16; literal-τ remainder and nonvanishing margins; weighted Green/Hölder constants; and every frozen source hash.

These finite controls support, but do not replace, the all-time/all-period analytic proofs above. No numerical nonlinear solution was substituted for the actual stationary correction. No external theorem search or external-source claim was needed for this elementary chain. The audit does not certify unrelated theorems elsewhere in the large canonical source files.

**Exact remaining gap in the audited target:** none.

**Strongest safe statement:** the literal-coupling exact potential/homoclinic identities, nonzero actual orbit sum, additive L² obstruction, and non-L¹ distributional q derivative, with the separate singular derivative-measure conclusion.

**Cheapest next substantive check:** any proposed multiplicative-gauge or oscillatory use of (H5) must explicitly control its integer-valued winding terms and identify the actual weighted operator being estimated. The inverse-pushforward measure and full quantum weights require their own analysis. Repeating the additive obstruction, or inferring pointwise Fourier decay from monotonicity, would not close those gaps.

## Publication mapping

This curated review preserves the full H1–H10 verdict and its exclusions.
Exact original bytes and original-to-public mappings are retained in
record/homoclinic_promotion_mapping.json. The maintained replay changes
execution packaging only: explicit failures, silent import, stdout output
and repository-relative source binding. Original execution outputs are
compared field-for-field on all exact checks.
