# Independent audit: dimension-uniform microscopic source bounds

Date: 7 October 2026. This is a separate review of the new addendum. It does not alter or enlarge the frozen acceptance of the first two sources. Canonical BGS remains untouched and publication remains outside this review.

## Claim card and primary verdict

**Verdict: proved as written.** The submitted proof supplies the stated uniform complex-resolvent moments, a genuine complex microscopic numerator-source neighborhood for any fixed finite number of retarded/advanced ratios, and every fixed derivative in those microscopic source variables. All constants survive independent recomputation. In particular, the integrated centered-count argument has no hidden log N loss.

Frozen source: `frozen/microscopic_source_bounds.md`, SHA-256 `9fcf9168a6ff39c8df8e4c1f106e969ce3e1cb3cfac963b7d81d2e9990b52b76`. The author was asked to keep this version fixed. It is reviewed independently of any later revision.

The quantified setting is N≥1, U any deterministic N×N unitary, and D diagonal with independent uniform phases. For Re s≥σ>0,

X_N(s)=N⁻¹Tr[e^(−s/N)V(I−e^(−s/N)V)⁻¹],  V=DU,

satisfies ‖X_N(s)‖_p≤L(σ)p for every integer p≥2, where L(σ)=100/(1−e^(−σ)). Consequently E exp(|X_N(s)|/(2eL(σ)))≤2 uniformly in N,U,s.

For fixed denominator absorptions with real parts ≥σ_*>0, the total microscopic numerator shift radius

ρ_*=[2e L(σ_*/2)]⁻¹

gives E|R_N|≤2 whenever the sum of the absolute values of all retarded and advanced shifts is ≤ρ_*. Here R_N is the product of the original determinant ratios, with numerator sources shifted by exp(−ξ/N) or exp(−η/N). This is the complete original ensemble observable, hence also the complete compact functional where that representation is available.

This is source regularity and uniform integrability, not identification of a limiting generating function. No individual compact sector estimate, higher-flavor color-one formula, annealed CUE theorem, or deterministic BGS theorem is being inferred.

## Dependency graph and status

1. Exact conditional phase averaging and cyclic rank-one interlacing: **passed**, separately audited in `review_first_pair.md`.
2. Same-arc and nested-arc factorial resampling: **passed**, all k with a direct nonnegative-count interpretation.
3. One-sided Poisson moment generating bound plus Var Z≤m: **passed**.
4. Upper centered-count moment and separately proved lower centered-count moment: **passed**.
5. Stieltjes integration by parts with cancellation of the two endpoints at π: **passed**.
6. Three kernel integrals, their N factors, and the loose constant 100: **passed**.
7. Complex absorption by common-phase rotation, and advanced sector by transposition: **passed**.
8. Exponential moment, logarithmic source increments, arbitrary correlations among the ratios, and multivariable Cauchy estimates: **passed**.
9. Positive Poisson-trace Laplace functional: **passed**.
10. Model-specific limiting-law identification and deterministic transfer: **not supplied; still open**.

The proof is self-contained after the first-pair lemmas. The prior spectral-counting citation is attribution, not an unverified load-bearing theorem substitution.

## 1. Resampling for every factorial order

For a connected arc A let Z=N_A and m=Np_A. With h_i=〈i,1_A(V)i〉, write

(Z)_k=Σ_i h_i (Z−1)_(k−1).

When Z=0 all h_i vanish, so the summand is defined as zero. When Z≥1, the old argument Z−1 is nonnegative, and rank-one resampling gives Z−1≤Z'. The falling factorial on nonnegative integer inputs is nonnegative and nondecreasing, including its initial zero range. Conditional integration of h_i gives p_A; the resampled full ensemble has its original law. Thus

E(Z)_k≤Np_A E(Z)_(k−1)≤m^k.

The k=0 convention is 1, k=1 gives the exact mean, and k>N is trivially zero. The empty and full-circle cases also obey this argument.

For nested arcs A_1⊆…⊆A_k with counts n_1≤…≤n_k, the number of ordered injective assignments is

J_k(n_1,…,n_k)=∏_{j=1}^k (n_j−j+1)_+.

Here x_+=max(x,0), on integer arguments. If an assignment is possible, choosing points in the stated order excludes precisely j−1 previously chosen points from A_j. If one of these factors vanishes, no assignment is possible. This is a coordinatewise nondecreasing function of the counts.

After choosing a point from A_1, the remaining injection count is J_(k−1)(n_2−1,…,n_k−1); when n_1≥1 all these counts are nonnegative. Rank-one resampling raises each available bound n_j−1 to at most the resampled count n_j'. Monotonicity and spectral averaging therefore give

E J_k≤Np_(A_1) E J_(k−1)(N'_(A_2),…,N'_(A_k)),

and induction proves N^k∏p_(A_j). This makes the submitted phrase “combinatorial nonnegative version” fully explicit. It avoids an invalid inequality between formal products containing negative factors.

For t≥0, expanding (1+(e^t−1))^Z and using the factorial bounds gives

E e^[t(Z−m)]≤exp[m(e^t−1−t)].

Every expansion coefficient is nonnegative. No step extends this to negative t. Also E Z=m and E(Z)_2≤m² give Var Z≤m exactly.

## 2. Both centered-count tails

For 0<t<3,

e^t−1−t≤t²/[2(1−t/3)].

Coefficientwise, 1/k!≤1/(2·3^(k−2)) for k≥2, with the all-degree inequality following by induction. For m>0 and x≥0, the Chernoff choice

t=√(2x/m)/(1+(1/3)√(2x/m))

gives the upper-tail threshold √(2mx)+x/3; the source's √(2mx)+2x is weaker and valid. The m=0 case has Z=0 almost surely.

Stochastic comparison with √(2mE)+2E, E an exponential random variable of mean 1, and Minkowski give

‖(Z−m)_+‖_p≤√(2mp)+2p.

The gamma moments satisfy (E E^(p/2))^(1/p)≤√p and (E E^p)^(1/p)≤p. No lower-tail estimate is inferred from the positive-t moment generating function.

For the lower tail, 0≤(m−Z)_+≤m and Var Z≤m give, for integer p≥2,

E(m−Z)_+^p≤m^(p−2)E(Z−m)²≤m^(p−1).

Treat m=0 separately to avoid a cosmetic 0^0 at p=2. Hence

‖Z−m‖_p≤√(2mp)+2p+m^(1−1/p).

This last, deliberately weaker lower-tail term is crucial. A false two-sided Poisson concentration assertion is neither stated nor needed.

## 3. Centered Cauchy-kernel representation

For real s>0 put r=e^(−s/N), δ=1−r, and f_r(θ)=re^(iθ)/(1−re^(iθ)). Its circular mean is zero. Apply integration by parts separately to the positive and negative half-circle counting measures, centered by N dθ/(2π). The result is

X_N(s)=−N⁻¹∫_0^π[f_r'(u)C_+(u)−f_r'(−u)C_−(u)]du.

The two boundary terms are f_r(π)C_+(π)+f_r(−π)C_−(π). They vanish jointly because f_r(π)=f_r(−π) and the two centered half-counts sum to zero. Fixed endpoints contain no eigenvalues almost surely by exact spectral averaging. One must combine these endpoint terms before estimating them; retaining only one half would introduce a spurious contribution.

The derivative satisfies

|f_r'(u)|=r/[δ²+4r sin²(u/2)]≤π²/(δ+u)²,  0≤u≤π.

Indeed sin(u/2)≥u/π and r(δ+u)²≤2rδ²+2ru²≤π²δ²+4ru², using 0≤r≤1. This bound remains valid for small r, not just r near 1.

With m=Nu/(2π), Minkowski and the centered-count estimate yield

‖X_N(s)‖_p≤(2π²/N)∫_0^π[√(Np u/π)+2p+(Nu/(2π))^(1−1/p)]/(δ+u)² du.

All three terms are nonnegative, so extending each integral to infinity is legitimate. Direct substitution u=δv gives

- ∫_0^∞u^(1/2)/(δ+u)²du=π/(2√δ).
- ∫_0^∞1/(δ+u)²du=1/δ.
- ∫_0^∞u^(1−1/p)/(δ+u)²du=δ^(−1/p)Γ(2−1/p)Γ(1/p).

The last product equals (1−1/p)π/sin(π/p), at most πp/2 because sin(π/p)≥2/p for p≥2. Combining every N and 2π factor gives the source's upper bound

π^(5/2)√[p/(Nδ)] + 4π²p/(Nδ) + π³p(Nδ)^(−1/p).

The third term's exact coefficient before this last simplification is π(2π)^(1/p)Γ(2−1/p)Γ(1/p), which is indeed ≤π³p. In particular its power is (Nδ)^(−1/p), not N^(1−1/p)δ^(−1/p) and not log N.

For s≥σ,

Nδ≥1−e^(−s)≥σ_0:=1−e^(−σ),

because 1−r^N=(1−r)(1+r+…+r^(N−1))≤N(1−r). Since σ_0<1 and p≥2, the displayed expression is bounded by

[(π^(5/2)+π³)σ_0^(−1/2)+4π²σ_0⁻¹]p≤100σ_0⁻¹p.

The constant does not depend on a decimal approximation: π<22/7 and √π<2 imply

π^(5/2)+π³+4π²<π³+6π²<(22/7)³+6(22/7)²=30976/343<100.

Thus (1) holds uniformly, with room to spare. Its purpose is robustness rather than an optimized radius.

## 4. Complex parameters and exponential integrability

For complex s, e^(−s/N)V equals e^(−Re s/N)V times a common scalar phase. Multiplying every independent Haar phase by that scalar leaves the joint law invariant. The same real-s bound therefore applies without dependence on Im s.

For V*, transposition gives (V*)^T=D*conjugate(U). This is another independent-phase ensemble with deterministic unitary conjugate(U). Trace resolvents and determinants are unchanged by transposition. Retarded and advanced variables need not be independent; all later estimates use Minkowski, not factorization of expectations.

If ‖X‖_p≤Lp for integers p≥2, then E|X|≤2L and p!≥(p/e)^p give, by a nonnegative moment expansion,

E exp(|X|/(2eL))≤1+1/e+Σ_(p≥2)2^(−p)=3/2+1/e<2.

This proves the stated exponential bound with its exact normalization.

## 5. Full determinant-ratio neighborhood and fixed derivatives

On Re s>0, the analytic logarithm of the determinant is given by its convergent trace series. Differentiating in s has a positive sign:

∂_s log det(I−e^(−s/N)V)=X_N(s).

Therefore the numerator/denominator logarithmic increment is ξ∫_0^1X_N(s+tξ)dt. The same formula holds in the advanced sector. The radius obeys

ρ_*=(1−e^(−σ_*/2))/(200e)<σ_*/(400e)<σ_*/2,

so every connecting segment stays in Re≥σ_*/2.

Let Y be the sum of the absolute values of all these logarithmic increments. Minkowski gives

‖Y‖_p≤L(σ_*/2)(Σ|ξ_j|+Σ|η_l|)p≤p/(2e).

Pointwise |R_N|≤e^Y. Applying the preceding exponential series at this normalization proves E|R_N|≤2. This controls a genuine complex neighborhood, including the imaginary components of every shift. The argument makes no unsupported assumption about phase cancellation after absolute values: cancellation was used earlier in the centered-count representation, before the L^p bound.

There is also an explicit stronger consequence useful for interpreting the final scope sentence:

E|R_N|^(3/2)≤E e^(3Y/2)≤1+3/(2e)+Σ_(p≥2)(3/4)^p
=1+3/(2e)+9/4<4.

Thus the products are genuinely uniformly integrable even on the entire stated closed shift ball. Bounded L¹ alone would not imply that, but the established exponential-moment slack does. This corollary is derived here from the same proof; it does not enlarge the frozen claim's hypotheses.

For K≥1 shifts, the polydisk of coordinate radius ρ_*/K lies in the allowed ℓ¹-ball. Finite-N sample functions are holomorphic in those numerator shifts, and the uniform L¹ bound gives expectation/Fubini control on Cauchy contours. Cauchy's formula yields

|∂^αH_N(0)|≤2α!(K/ρ_*)^|α|.

For K=0 the product is simply 1. Smaller polydisks give uniform derivative bounds at every interior point. These derivatives are in microscopic ξ,η coordinates; unscaled c,d derivatives carry the corresponding powers of N and are not asserted to be uniformly bounded without normalization.

For the original pair, ∂_ξ∂_ηH_N(0)=ab N⁻²∂_c∂_dG|matched. At a=b=e^(−s/N), this is exactly F_N(s) from the first audit. This verifies that the new derivative conventions agree with the earlier Abel normalization.

## 6. Positive Laplace functional

For f≥0 with connected superlevel arcs, layer-cake and the proved nested assignment bound control every ordered factorial coefficient of ∏_j(1+t f(λ_j)). The expected product is therefore at most exp[tN∫f]. Applying this to g=e^(tf)−1, whose superlevel sets are the same nested arcs, gives

E exp[tΣ_jf(λ_j)]≤exp[N∫(e^(tf)−1)].

Truncation and monotone convergence handle nonnegative measurable functions when needed; the application to P_r/N is bounded outright.

With f=P_r/N, its maximum is M=(1+r)/(N(1−r)) and N∫f=1. The convex chord inequality e^(tx)−1≤x(e^(tM)−1)/M gives exactly (14). For r=e^(−s/N), s≥σ>0,

M=N⁻¹coth(s/(2N))≤1+2/σ.

Thus this is genuinely uniform for every fixed positive Laplace parameter t. It is a positive-function corollary and is not substituted for the separate imaginary-resolvent argument.

## 7. Exact-source attribution check

The linked eScholarship landing page initially returned a JavaScript challenge; the direct institutional PDF was accessible and checked. The published primary source is Combes–Germinet–Klein, *Generalized Eigenvalue-Counting Estimates for the Anderson Model*, J. Stat. Phys. 135 (2009), 201–216, DOI 10.1007/s10955-009-9731-3. Theorem 2.1, printed p.204, equation (2.7), gives the nested two-interval count estimate. Theorem 2.3, printed p.205, (2.12)–(2.13), gives its higher nested and single-interval factorial versions. These are additive self-adjoint Anderson-model statements. They support the attribution of the resampling mechanism; they do not by themselves prove the multiplicative unitary claim. The submitted finite-unitary proof supplies that separate translation directly.

Verified URLs: [institutional published PDF](https://escholarship.org/content/qt0kh9c48w/qt0kh9c48w.pdf), [published record](https://doi.org/10.1007/s10955-009-9731-3), and [official arXiv v3 PDF](https://arxiv.org/pdf/0804.3202v3). The PDF was read through the web tool rather than downloaded into this audit directory, so no local content hash is claimed. No scoped or global novelty search was performed.

## 8. Independent exact finite controls

`check_source_bound_lemmas.py` is a fresh, deterministic exact-arithmetic check. Its result is `check_source_bound_lemmas.json`.

- 3,002 nested-cardinality chains, on universe sizes 0…7 with 0…5 sets, were checked by recursive injective-assignment enumeration against ∏(n_j−j+1)_+.
- 7,294 feasible one-coordinate count increases were checked for monotonicity.
- 240 exact diagonal/binomial and clock count laws were checked for N=1…20 and six rational arc fractions, including 0 and 1.
- 3,240 factorial-moment inequalities and 2,640 lower-deviation moment inequalities passed exactly, with p=2…12 for the latter.
- Chernoff Taylor coefficients were checked through degree 40; the written induction supplies the all-degree proof.
- The loose constant 100 has the exact rational upper certificate 30976/343 and margin 3324/343.

These are finite adversarial controls, not the proof of the analytic or dimension-uniform statements. No numerical quadrature or floating tolerance is used as theorem evidence.

## Remaining boundary and cheapest next mathematical task

There is no missing implication for the stated source-regularity theorem. A model-specific limit-identification argument is still required. The full complex neighborhood makes legitimate normal-family and fixed-source-derivative arguments available, but a uniform bound does not determine the limiting function. Nor do scalar one-variable limit data automatically identify a several-variable generating function. Diagonal and cyclic controls retain their distinct limiting statistics while obeying these universal estimates.

The compact representation may now be manipulated within this bounded complete-source neighborhood, provided any operation retains all local boundary/cancellation terms. Proving the required signed cancellation or evaluating a subsequential limit remains the next substantive task. Replacing the full functional by its individual absolute sectors would still require a new theorem.
