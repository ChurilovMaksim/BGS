# Independent audit of actual transversality and measure regularity

Date: 6 October 2026. This is an independent internal proof audit, not external refereeing or formal verification. No canonical or frozen source was edited.

## Normalized claim and primary verdict

**Primary verdict: proved as written, for the Section 1–3 target specified below.**

At the unchanged coupling τ=10^−80, let η=10^−70+10^−110 and let R denote the actual Hamilton–Jacobi edge correction, with the globally uniform real C² bound from `four_branch_parametrix.md`. Use the unique bounded infinite-chain correction from `winding_defect_locality.md`, not a first-response or arbitrary Hölder surrogate. Then:

1. The locality and Hölder estimates in Section 1 hold with β=29/5 and the displayed constants, including the finite-cycle/quadrature statements.
2. Hτ(q,p)=q+D∞(q,p) is strictly increasing in q for each p, has the stated torus lift rules, and is increasing in the stated open cone.
3. The inverse estimate (T1), the actual pushforward Frostman estimate (T2), non-atomicity, and the unweighted averaged Fourier estimate (T3) follow.

There is no missing load-bearing implication in this target. In particular, **the unbounded lifted backgrounds are compatible with the branch-dependent actual generating function**. The distinctions between local equations and bounded-operator equations, explained below, are essential.

This verdict does not certify pointwise Fourier decay, complete quantum amplitudes, other displacements, the signed trace hierarchy, or BGS. The manuscript preserves those boundaries correctly. The inherited first-response obstruction and the external theorem summary in Sections 4–5 are not re-certified in this audit.

## Pinned evidence

The reviewed target is exactly:

- `bgs_paired_box_cancellation/transversality_and_measure.md`
- SHA-256 `2bddd915330543828c5637ea966f8b2081ce79208655c4632342b3f351391ee9`

Dependencies read directly include `winding_defect_locality.md`, the prior `independent_review/review.md`, and the actual model and HJ sources `BGS/mathematics/fixed_map_path_model.md` and `BGS/mathematics/four_branch_parametrix.md`. Source hashes are recorded in `check_results.json`. The current project status still leaves TRACE-005 and BGS open. The earlier audit was treated as a comparison record; the decisive arguments below were reconstructed from the equations.

## Dependency graph and obligation matrix

- Actual global HJ graph, periodic symbol, and integer gluing → globally defined bounded analytic edge correction R.
- Uniform C² bound for R → bounded local forcing, small nearest-neighbour Hessian, bounded correction existence.
- Exact infinite Green kernel + cyclic periodization + weighted Neumann series → β-locality.
- Local periodic forcing + hyperbolic growth + weighted inverse → actual Hölder continuity.
- Cat recurrence + bounded corrections → local homogeneous equation for the difference of two lifted solutions.
- Negative off-diagonals + positive row mass + growth at both ends → actual monotonicity.
- Quantitative one-neighbour propagation → inverse Hölder bound → fibre preimage estimate → actual Frostman bound.
- Frostman bound + elementary Fejér identity/annuli → averaged squared Fourier bound.

| Obligation | Result | Reason |
|---|---|---|
| Actual fixed-τ object, branch and lift conventions | Passed | The global R₀ correction is used throughout; integer gluing preserves it |
| Uniform real domain for unbounded backgrounds | Passed | Source bounds are global in real x,y; only corrections need to be bounded |
| Infinite local equation and averaged Hessian | Passed | Each row has only three terms; no convergence of infinite actions is needed |
| β weighted Green and resolvent estimates | Passed | Exact weighted kernel formula, periodization, Neumann estimate |
| β locality and Hölder constants | Passed | Explicit inequalities below, independently checked over rational bounds |
| q and cone monotonicity | Passed | A global minimum exists because the difference tends to +∞ at both ends |
| Inverse estimate (T1) | Passed | Both δ regimes and the integer cutoff inequality retain correct constants |
| Circle-fibre inverse and Frostman (T2) | Passed | Continuous degree-one increasing lifts are circle homeomorphisms |
| Fejér bound (T3) | Passed | Full unweighted sum follows using a kernel of width 2M |
| One-sided conditional analyticity | Compatible, non-load-bearing here | It needs a common complex strip, available after shrinking a strip of the analytic periodic correction |
| Previously proved first-response obstruction | Not independently re-audited | Its exact scope is read and retained |
| Named external Fourier-decay theorem | Out of scope | No conclusion in Sections 1–3 imports that theorem |
| Pointwise decay and full weighted trace target | Not addressed | Neither follows from the audited estimates |

## 1. Unbounded backgrounds and branch compatibility

Write xⱼ⁰=(Sʲ(q,p))q on the real lift, bⱼ=xⱼ⁰+s gⱼ, and Xⱼ=bⱼ+uⱼ. The source HJ construction defines S₀(τ,x,y) globally on all real (x,y), since the characteristic projection is globally invertible. Its correction R₀=S₀(τ)−S₀(0) has uniform C² bounds on that entire domain. Consequently evaluating R₀ at arbitrarily large real pairs does not leave the stated domain.

The correction has the exact gluing

R₀(x+a,y+3a+4b)=R₀(x,y),  a,b∈ℤ.

Changing the initial cat lift by an integer vector changes each neighbouring pair by exactly such an integer cat increment. This preserves the local equation and its unique bounded correction. In particular D∞ is periodic. Although individual phases have nonperiodic quadratic/linear gluing terms, those terms cancel in R₀. The proof does not pretend that S₀ itself is a periodic function.

The cat recurrence K₀x⁰=0 and K₀g=e₀ hold coordinate by coordinate. Hence

K₀X−∇R(X)=s e₀

is a valid local equation. It is not an equation obtained by applying a bounded operator to an ℓ∞ vector X: X is generally unbounded. The contraction/inverse acts on u∈ℓ∞, which is the correct domain.

Likewise, when comparing two q values, W=X′−X is unbounded but each row of (K₀−Ē)W=0 is well-defined. The mean-value Hessian Ē is obtained on the finite-dimensional segment in the two arguments of each local edge. Its uniform bounds hold along the whole segment. No interpolation between integer branch labels or boundedness of W is needed. In particular, invertibility on ℓ∞ must not be used to conclude W=0; the manuscript does not make that mistake.

## 2. Sharper β estimates and constants

For β=29/5<λ=3+2√2,

Lβ=Σⱼ β^|j|gⱼ=(λ+β)/(√2(λ−β))<300.

On a cycle, distₘ(0,j mod m)≤|j|, so periodization gives the same bound without a period-dependent factor, also at m=1,2. The weighted matrix norm is submultiplicative by the metric triangle inequality. The edge Hessian gives

∥E∥β≤2η(1+β)<14η.

At m=1 the combined diagonal is bounded by 4η; at m=2 the repeated neighbour is combined before taking the weighted row sum. Both remain covered. Thus

∥Gτ∥β≤300/(1−4200η)≤301,
∥Gτ−G₀∥β≤301·14·300η=1,264,200η,
∥GτE∥β≤4214η.

For any integer L, triangle inequality gives

Σⱼ β^−|j|gⱼ₊ᴸ≤Lβ β^−|L|<300β^−|L|.

Summing the nonzero period shifts costs at most

600β^−m/(1−β^−m)≤[600β/(β−1)]β^−m=725β^−m.

The defect coefficient is therefore at most 4214·725η=3,055,150η, below the stated 4·10⁶η.

For the Hölder split, put α=log β/log λ and R=floor(log(1/t)/log λ), 0<t≤1. Direct geometric sums give

Σⱼ β^−|j|min(1,λ^|j|t)
≤[2λ/(λ−β)+2β/(β−1)]t^α<500t^α.

The local forcing at site j, with the correction offsets held fixed, is a periodic function of the cat point at that site. Its real C² edge bounds give the safe Lipschitz/bounded-difference coefficient 32η used implicitly in 9632=301·32. Therefore the 4 inside the hyperbolic comparison minimum costs 4^α≤4 and

9632·500·4=19,264,000<2·10⁷.

For 4d>1, the bounded correction estimate covers the same Hölder inequality. This argument compares bounded local periodic forcings; it does not differentiate the unbounded full orbit in ℓ∞. The finite-grid quadrature exponent is Uₘ^−α=O(β^−m/2), exactly as claimed. The choice β<λ is essential; its constants diverge at the endpoint, and no C¹ conclusion is justified.

## 3. Actual monotonicity

For fixed s,p and a positive q increment δ,

Wⱼ=aⱼδ+(u′ⱼ−uⱼ),  aⱼ=(λʲ+λ^−ʲ)/2,
|u′ⱼ−uⱼ|≤4η.

Hence Wⱼ→+∞ as j→±∞ and a global minimum is attained at a finite index. Set A=K₀−Ē. Each off-diagonal is negative, its diagonal is positive, and every row sum is at least 1−4η>0.

If W attains a negative minimum at j, then

(AW)ⱼ≤(row sum of A at j)Wⱼ<0,

contradicting AW=0. If its minimum is zero, both neighbouring nonnegative values must be zero; propagation gives W≡0, contradicting growth at infinity. Thus every Wⱼ>0.

Since Hτ=∫₀¹ Xₛ,₀ ds−g₀/2, this proves strict q-monotonicity. The lift rules follow from the correction gluing. For a general increment,

(SʲΔz)q=½λʲ(Δq+√2Δp)+½λ^−ʲ(Δq−√2Δp).

The strict cone condition makes both coefficients positive, so the same two-ended argument applies. No claim on the cone boundary is required.

## 4. Inverse estimate and actual measure

For δ≥8η, W₀≥δ−4η≥δ/2≥δ^p*/28, because δ≤1 and p*=log7/logλ>1.

For 0<δ<8η, choose the least nonnegative integer L with a_Lδ≥8η. Since a_L≥λᴸ/2,

L≤1+log(16η/δ)/logλ,  W_L≥4η.

All coordinates are positive. The local equation gives

Wⱼ≥[(1/4−η)/(3/2+2η)]Wⱼ₊₁≥Wⱼ₊₁/7.

The final comparison requires η≤1/36, and the actual η is far smaller. The manuscript's later condition η≤1/16 is used for a different inequality, so there is no mismatch of hypotheses. Iteration yields

W₀≥4η·7^−L≥(4η/7)(δ/(16η))^p*
=(1/28)(16η)^(1−p*)δ^p*≥δ^p*/28.

The same estimate holds for every s before integration. This is exactly (T1).

Continuity, strict increase, and the degree-one lift rule make each q fibre a circle homeomorphism. Lift the endpoints of an arc I in their increasing order. Its fibre preimage is an arc with length δ≤1 and its image increment is |I|, even when either arc crosses a coordinate seam. Therefore (T1) gives δ≤(28|I|)^γ, γ=1/p*. Integrating this bound in p proves (T2) for the actual pushforward. Shrinking arcs to a point proves non-atomicity. Neither absolute continuity nor a density is asserted or obtained.

## 5. An explicit Fejér check

Use Fᴷ(x)=K^−1|Σⱼ₌₀ᴷ⁻¹e(jx)|². Then

Fᴷ(x)≤min(K,1/[4K∥x∥²]),
∫∫Fᴷ(x−y)dμ(x)dμ(y)
=1+2Σₙ₌₁ᴷ⁻¹(1−n/K)|μ̂(n)|².

The Frostman estimate gives μ(B(x,r))≤(56r)^γ; for large r the right side is at least one, so the bound remains harmless. Split into ∥x−y∥≤1/K and the annuli 2ʲ/K<∥x−y∥≤2ʲ⁺¹/K. Since 0<γ<1,

∫Fᴷ(x−y)dμ(y)
≤56^γK^(1−γ)[1+2^(γ−2)Σⱼ≥₀2^j(γ−2)]
≤2·56^γK^(1−γ).

Take K=2M. The weights for 1≤n≤M are at least 1/2, so the displayed Fourier identity bounds the full unweighted positive-frequency sum. A safe explicit version of (T3) is

Σₙ₌₁ᴹ|μ̂(n)|²≤112 M^(1−γ),
M^−1Σₙ₌₁ᴹ|μ̂(n)|²≤112 M^−γ.

This elementary proof needs no external Fourier-decay theorem. It controls a Cesàro square average; it does not turn into decay at every integer, or at every odd integer, by discarding exceptional frequencies.

## 6. Secondary claims and exact remaining boundary

The one-sided analytic observation in Section 4 is consistent with the actual branch domain. The analytic correction is periodic under a full-rank lattice. Its real Hessian is uniformly tiny. By compactness of a fundamental domain and analytic continuation, one can shrink to a common complex neighbourhood where a strict contraction bound still holds. In the stable direction on positive time, the complex background increments decay like λ^−j, so one common initial-parameter radius works for all positive half-line lengths. This supplies the qualitative uniform-strip ingredient; no explicit radius is claimed. The opposite half-line uses the opposite eigendirection. Holding the boundary value fixed does not differentiate the matching value, and the manuscript correctly does not infer a full-phase C¹ bound.

The direct first-response obstruction file was read for scope, but its separate all-period Fourier/alias proof and its computational certificate were not re-audited here. The external expanding-map theorem is not an input to (T1)–(T3), so its source review is outside this audit rather than silently inherited as a new theorem certification.

The exact open implication remains: prove pointwise Fourier decay for this actual μτ, at this literal coupling, or find a different estimate that suffices for the required signed comparison. Even resolving that phase-only implication would leave determinant, transport, Gaussian-box/exact-integral weights and the complete displacement/time sum to control.

## Reproducible finite checks

Run:

`PYTHONDONTWRITEBYTECODE=1 python /workspace/shared/bgs_frostman_review/check_constants.py`

The independently written checker uses exact integer/Fraction arithmetic for every pass/fail decision. It verifies 17 constant/domain inequalities and exact β-weighted cat Green controls for m=1,…,24, including repeated neighbours. Decimal logarithms are display only. These controls support constants and small-cycle bookkeeping; they do not certify the nonlinear infinite-chain or asymptotic statements by computation. The analytic arguments above supply those conclusions.

The strongest safe statement is the actual fixed-τ transversality/Frostman/averaged-Fourier theorem as written. No correction to its Section 1–3 target is needed. The cheapest next mathematical check should address the specific pointwise-decay mechanism or an exact full-amplitude reduction, rather than reusing averaged decay as a replacement for either.
