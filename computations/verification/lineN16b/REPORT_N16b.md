# REPORT_N16b — wrap-around requirement vs c_B; more (R-mix) evidence; THEOREM_DRAFT

Labels: [P], [P-sketch], [CA], [CA-fp], [N], [H]. Nothing pushed. Earlier lines are not modified.

## 1. N14 §3 (wrap-around deep points at composite h_p) vs what is proved
**(a) c_B does not transfer [P, scope].**
- c_B = 0.7375 (N14b Lemma 2) bounds the *first moment* E_{H_d}|r| of the full trace ratio against the C′ rate.
- Gap (a)'s wrap activity is bounded through the *second-moment* operator 𝒦 (ρ̄ ≤ 0.28/0.30 [CA-fp]) and ℓ³ ≤ ℓ². These are different objects, and no conversion is available.

**(b) Units [P, arithmetic].**
- 0.380 = (λρ̄²)^{3/2} is a per-λ-step factor (N14 §0).
- So d^c·0.380^{ℓ₀} → 0 iff c·ln d < 0.967·ℓ₀ (ℓ₀ in λ-steps), i.e. **c < 0.967ℓ₀/ln d = 0.549·ℓ₀/log_λ d.**
- N14 wrote 0.97·ℓ₀/log_λ d, which is off by the factor ln λ = 1.763 unless "log" meant ln. With ρ̄ = 0.28: c < 1.175ℓ₀/ln d = 0.667ℓ₀/log_λ d.

**(c) What is actually proved.**
- **(c1) Unit weights per point [P].** Suppose the deep points carry the same per-point weight as in the prime case (κ(0)/n = 1 for iso points) and form a subset S of a group Γ on which the Parseval/𝒦 identity is exact. Then positivity gives Σ_{S}|r_Ar_B|² ≤ Σ_Γ|r_Ar_B|². Hence **c = 0: no subgroup lemma is needed**, and only the H1 constant remains.
- **(c2) d-amplified weights [P].** Suppose instead the points carry weights ≍ d/h, as the mixed points in N13b's bookkeeping, so the sum is effectively an average over a coset of index d. Then positivity gives E_{coset} ≤ d·E_Γ. The weight sits outside the ℓ³ ≤ ℓ² power (Σ_S w|a|³ ≤ w(Σ_Γ|a|²)^{3/2}), so the loss on the final activity is **d¹ (c = 1)**, not d^{3/2}.
  - Covered: d ≤ e^{0.967ℓ₀} (ρ̄ = 0.30) or e^{1.175ℓ₀} (ρ̄ = 0.28).
  - With ℓ₀ = p/2 ε-steps = p/4 λ-steps: d ≤ 1.273^p (resp. 1.342^p), i.e. θ = log_λ d/p ≤ 0.137 (0.167).
  - **All** divisors (ln d ≤ 0.881p) are covered iff ℓ₀ ≥ 0.911p (ρ̄ = 0.30) or ≥ 0.750p (ρ̄ = 0.28) λ-steps. That is a design choice for gap (a): the window model would then have to cover spans up to that length.
- **(c3) Lemma-2-type second-moment analogue [P-sketch].** Window to the separation time plus sup on the last log_λ d steps. With the only d-independent one-step bound available, Nsum ≤ 8.3288 [CA] (N13), the cost per λ-step is ≳ 8.33⁴/(λρ̄²) ≫ λ. It is **worse than trivial**, so it is not pursued.

**Which case applies.** This depends on how gap (a) normalises its composite-level points. N14 §3 calls them "a coset of a subgroup H_d". For iso points at level h_p with κ(0)/n = 1, (c1) applies and the composite case costs nothing extra. Only if the deep points are counted at a sub-level with amplified weight (N8b A_c = h_p/c) does (c2) apply. **This needs confirmation by the gap-(a) owner (N14 line).**

## 2. (R-mix) evidence: majorant over mixed classes [N]
Script: code/a_mixed_majorant.py.
- **Majorant and sets.** F_p = ∏_{i<p} g(Tr(λ^iβ)/h), g = |Σ_a|J_a(1.8)|e(at)|². The mixed set {Nβ ≡ 0 (q), Nβ unit mod h/q} is enumerated directly on the sublattice a ≡ r·b (mod q); the conjugate ideal is covered by the Galois symmetry F(β′) = F(β).
- **Reference.** W0 = the exact collision mass of the majorant (carry automaton, |e| ≤ 10, |v| ≤ 40).
- **Statistic.** c_coll = log(E_M/W0)/log q. (R-mix) with c ≤ 0 means E_M/W0 ≤ e^{o(p)}.

| p | q (iso part) | mode | points | E_M | W0 | E_M/W0 | c_coll |
|---|---|---|---|---|---|---|---|
| 11 | 23 | exact | 2.85e6 | 0.2687 | 1.5441 | 0.174 | −0.56 |
| 11 | 353 | exact | 1.71e5 | 0.0520 | 1.5441 | 0.0337 | −0.58 |
| 13 | 79 | exact | 2.83e7 | 0.1807 | 1.7060 | 0.106 | −0.51 |
| 13 | 599 | exact | 3.64e6 | 0.0727 | 1.7060 | 0.0426 | −0.49 |
| 17 | 15607 | **exact** | 1.62e8 | 0.04415 | 2.0825 | 0.0212 | −0.40 |
| 17 | 103 | sampled | 2.2e7 of 2.5e10 | 0.136 | 2.0825 | 0.065 | −0.59 |
| 19 | — | h₁₉ = 9369319 prime: no mixed classes | | | | | |
| 23 | 6771937 | sampled | 2.1e7 | 0.00576 | 2.8086 | 0.00205 | −0.39 |
| 23 | 47 | sampled | 2.2e7 | 0.0128 | 2.8086 | 0.00455 | −1.40 |

- **All exact cases have E_M < W0.** That is (R-mix) with c ≤ 0 and constant 1, at the majorant level.
- **The sampled rows are heavy-tailed.** The single largest term is 19% (p = 17, q = 103) and 32–34% (p = 23) of the sample sum, so those means are not converged. They are indicative only.
- Exact p = 17, q = 103 needs about 2.5e10 points (≈ 2 h on the shared core). It was not run; it can be queued if wanted.
- These are majorant statements, which is the form C′'s chain needs (THEOREM_DRAFT H5). They are not statements about |r| itself.

## 3. THEOREM_DRAFT
Written at /workspace/bgs-lineN/THEOREM_DRAFT.md (hash in this manifest):
- the conditional theorem with hypotheses H0–H8, each with status and file;
- the proved ingredients table;
- the unconditional section: no refutation, and no single-p certified inequality in the large-p regime;
- the novelty caveat;
- the superseded claims.

The lineN14 referee report did not exist at drafting time, so it is not incorporated.
