# Line N11 — the gas model toward a theorem: corrected model, certified κ, coding lemma, conditional modulus theorem; REPORT_N9_v2 / N10_v2
Grok Bot, 2026-10-31 (Asia/Yekaterinburg, UTC+5). No push. Earlier lines are untouched. Line F `cert_lift.py`, N2 code and N6 `twb.py` were run read-only, with all output in N11/logs.
Referee input: /workspace/audit/lineN10/REPORT.md.
Labels: [P] proved, [P-sketch], [CA] computer-assisted rigorous, [CA*] rigorous inequality evaluated in floating point, [N] numerical, [H] heuristic/model.
Convention: sg = +1.

## 0. Headline
1. **The N10 gas model was incomplete. Corrected [N, strong].**
   - Background 0 also carries configurations with an *even* number of odd ("family") bumps. The completeness scan found them:
     - every class with |N| ≤ 2000 at p = 47 (1863 classes, both backgrounds, exact twists);
     - each dyadic shell is dominated by two classes with |w| = |w*|² = 1.56e-7 and arg = 2·arg w* (1.03 rad).
   - Hence the per-line sum is ½σ[(1+R−2σw*)^p − (1+R+2σw*)^p] + ½[(..)^p + (..)^p] − 1, and sinh + cosh = exp gives
     **X_gas = 2[(1+Λ)^p − 1], with Λ = R + 2w* = 7.490e-4 + 3.722e-4 i.**
   - Consequence [P, given the model form]: **|1+X_gas| = |2(1+Λ)^p − 1| ≥ 2|1+Λ|^p − 1 ≥ 2(1+Re Λ)^p − 1 > 1 for every p.** There is no phase-crossing region and no p-window to check.
   - Certified: Re Λ ≥ 6.238e-4 [CA, from the N8/N9 enclosures of w*, c₀, c₄ and |w(e4s2)|]. This gives |1+X_gas| − 1 ≥ 2((1+6.238e-4)^p − 1): 2.47 at p = 1289, 43 at p = 5000, 1.0e3 at p = 10⁴.
   - Re X_gas < 0 first at p = 4099 (exact product; 4097 with the exp form). It is negative on 50.8% of odd p ≤ 2·10⁵, so the Lin route is still dead [H, model].
   - Small-p change versus N10: +4p²w*², i.e. +1% at p = 47 (X = 0.07132 + 0.03621i).
2. **Completeness [N].** After removing classes whose |w| matches a gas product (w*², w*c₀, w*c₄, c₀c₄, w*²c₀, w*³, w*c₈), the unexplained remainder per dyadic shell (p = 47, logs/g_model2.json) is:

   | shell j | unexplained |
   |---|---|
   | 3 | 4.5e-9 |
   | 5 | 1.4e-8 |
   | 6 | 7.4e-8 |
   | 7 | 6.3e-9 |
   | 8 | 8e-10 |
   | 9 | 2.5e-10 |
   | 10 | 5e-10 |

   - The total is 1.0e-7, which is 1/6000 of the certified budget Re Λ_lo = 6.24e-4 per position.
   - The raw (non-model) per-shell sums are flat (≈3.5e-7/shell). They are *entirely* gas terms (mainly 2-odd-bump in background 0).
   - Matching by magnitude is heuristic.
3. **Interaction rate certified [CA].** Line F sector-4 certificate rerun at contour radius r₂ < 1 (same code and parameters, only r₂ changed):

   | r₂ | R₂ | κ = r₂/μ*_lo |
   |---|---|---|
   | 1 (Line F) | 3224.84 | 0.52206 |
   | 0.85 | 7430.48 | **0.44376** |
   | 0.80 | 15206.2 | **0.41765** |

   - The quantity bounded is sup_n ‖L₄ⁿ(I−Π)‖/r₂ⁿ ≤ R₂. The measured rate is 0.4016.
   - **The obstruction is the prefactors, not the rate** (§2).
4. **Coding lemma [P] for dilute configurations.** This settles referee item (2). Dense configurations are exponentially negligible in the model (§3).
5. **What remains open** (§5):
   - (i) An absolute bound on the true weights of *uncoded* points (A∞ tail, absolute form). The budget is now generous and grows exponentially.
   - (ii) A proved interaction bound with usable prefactors.
   - (iii) Y = unit + mixed + partially-isotropic parts, i.e. (b′) at composite h_p.

## 1. Exact polymer identity [P mod Line F]
- **Setup.** For a point x on (γ) at level h_p with background b ∈ {0, ½}, the dominant sector gives Tr ∏_{i∈Z/m} L_{τ_i}. The other sectors are ≤ 0.932^m·poly relative [P mod Line F, N6/N8].
- **Bump set.** Fix a threshold and call S(x) the bump set: maximal runs of steps i with |τ_i − b| > η, padded by w₀ steps on each side. Write B_j for the product over bump j, and G_j for the product over the gap between bumps j and j+1, of length g_j.
- **Gap splitting.** Split G_j = μ^{g_j}(c_j Π + Ñ_j), with c_j = ⟨ℓ|G_j|r⟩/μ^{g_j}.
  - Then ‖Ñ_j‖ ≤ R₂κ^{g_j}·(1+O(Σ_{i∈gap}‖D_i‖)) + O(g_jκ^{g_j}Σ‖D_i‖). Here D_i = L_{τ_i} − L_b and ‖D_i‖ ≤ 2πN₁|τ_i − b|, with N₁ = 573.59 [CA, n_cert].
  - First-order cross terms ΠDÑ and ÑDΠ decay like κ^{g}, because |τ_i − b| ≤ c·λ^{−dist} and λ^{−1} < κ.
- **Exact expansion.** Expanding ∏_j(c_jΠ + Ñ_j) cyclically:
  - Ẑ_x/Z = (1+Tr N_m/μ^m)⁻¹ Σ_{T⊆gaps} ∏_{chains}⟨ℓ|B_{j₁}Ñ…Ñ B_{j_r}|r⟩/μ^{len}·∏_{j∈T}c_j + (wrap term T = ∅).
  - Terms where every gap is Π give the rank-one product ∏_j b_j·∏c_j, with b_j = ⟨ℓ|B_j|r⟩/μ^{ℓ_j}. This is σ∏φ.
  - Each Ñ-linked chain is a polymer whose activity is bounded by ∏‖B‖/μ^ℓ·∏R₂κ^{g}.
- **Status.** This is an exact identity [P]. The bound inputs (R₂, κ, N₁, ‖Π‖ ≤ 21.97, Cpow = sup‖Lⁿ‖/μⁿ ≤ 3246.8) are [CA, Line F / n_cert / N11 logs].

## 2. Interaction bound: proved rate, unusable prefactor (honest)
- **Measured** (p = 47, logs N10 + referee p = 37/59): |φ(g) − φ∞|/|φ∞| = 9.0e-3, 3.6e-3, 1.44e-3 at g = 6, 7, 8. That is a rate of 0.40 with O(1) prefactor, and the ± pair cancels at leading order.
- **Proved.**
  - Pair interaction at λ-gap g ≤ G_b²·R₂·κ^g, with G_b = Cpow²(1+ε₀)²G_c (G_c = 37.0 is the certified family-core norm). So G_b ~ 4e8.
  - For the summed interaction to stay below the certified budget 6.2e-4 per site, one needs κ^{g₁} ≤ 6e-4/(G_b²·R₂·#types). With κ = 0.4177 this gives **g₁ ≈ 64 λ-steps**.
  - Configurations with gaps < g₁ then have to be treated as merged polymers: about 5e4 two-bump and about 1e7 three-bump p-independent types. That is finite but not certifiable class by class.
- **Fix needed (well-posed, finite).** An *adapted norm* in which ‖Lⁿ(I−Π)‖ ≤ C κ'ⁿ with C = O(1), and bump-block norms are O(1). Examples: an ellipsoidal/Lyapunov norm from the certified spectral data (N2 c5_ellipsoid-type), or Line F's core basis with b12 = 10.76.
  - With C ~ 10 and block norms ~ 10, g₁ drops to about 15, and the merged list to about 10³ (two-bump), which arb can do.
  - **Not done here.**

## 3. Coding lemma [P] (`code/c_coding.py`, logs/c_coding.json)
- **Setting.** Types 𝒯 = {±1, ±√2, ±2, ±2√2, ±4} (B = 4). A configuration Γ is a set of (position n ∈ Z/p in ε-units, type β), with e(Γ) = Σβε^{n} read modulo γ̄ (background-0: α′; background-¼: α, odd digit count).
- **(i) Uniqueness in O.** If all gaps are ≥ g₀ = 5 ε-steps, then e(Γ) determines Γ.
  - Proof: compare the top terms. c_min = min|β − β′ε^{−s}| over (β,0) ≠ (β′,s) equals 0.17157 = 3 − 2√2. The remainder is ≤ 2Bε^{−g₀}/(1−ε^{−g₀}) < c_min for g₀ ≥ 5.
- **(ii) Injectivity mod γ̄.** If |Γ| + |Γ′| ≤ p/G₀ with G₀ = 6, then e(Γ) ≡ e(Γ′) (mod γ̄) implies Γ = Γ′.
  - Proof: the union leaves an empty arc of length ≥ G₀; cut the circle there. Then |N(δ)| ≤ B²(1−ε⁻¹)⁻²ε^{p−G₀} < ε^p/2 − 1 < q. A nonzero multiple of γ̄ has |N| ≥ q, so δ = 0, and (i) applies.
- **Exact check.** 0 collisions among 1.4–1.7e5 random dilute configurations at p = 29, 47, 59 (exact integer residues).
- **Dense configurations** (the referee's 3^p > q) are excluded by (ii), and their *model* weight is negligible. With A := Σ_types|φ| ≤ 1.03e-3 and n₀ = p/12, Σ_{n≥n₀}(pA)ⁿ/n! ≤ (e·12A)^{p/12} = e^{−0.28p}, far below |1+X_gas| − 1 ≥ 1.25e-3·p.
- **Not covered.** Surjectivity onto *all* points. Uncoded points (other bump types, merged clusters, deep/chaotic patterns) form the tail and need §5(i).

## 4. Conditional modulus theorem (KP form)
- **Theorem N11 [P mod (T), (I), (Y), Line F, certified classes].** Fix p ≥ 1289 (class certificates valid, E ≤ 1e-9). Split the level-h_p isotropic sum as X = X_coded + X_tail, where X_coded runs over dilute coded configurations of 𝒯 (Lemma C). Write the coded sum by KP as X_coded = 2[(1+Λ)^p·e^{pΔ} − 1] − (dense part), with |Δ| ≤ δ_int per site. Then:

  Dev_{h_p} ≥ (n|Z|²/h_p²)·[(2(1+Re Λ_lo − δ_int)^p − 1 − |X_tail| − |Y| − e^{−0.28p})² − 1] − 0.2·(n|Z|²/h_p²),

  - The last term is N10-F3: inherited levels e·h_p, using the positivity floor, total weight ≤ I−1 ≈ 0.2.
  - Re Λ_lo = 6.238e-4 [CA]. The bracket base exceeds √1.2 whenever δ_int < Re Λ_lo and |X_tail| + |Y| ≤ (1−θ)·2((1+ReΛ_lo−δ_int)^p − 1).
- **KP.** Take a = 0.01. The criterion Σ_{γ∋site}|z_γ|e^{a|γ|} ≤ a holds for the 𝒯-single-bump polymers (A ≤ 1.03e-3, span ≤ 3 sites) [P given certified boxes]. Then |Δ| ≤ (pair-interaction sum) + O(A²) [P-sketch, standard cluster bound].
- **Open hypotheses.**
  - **(I)** δ_int < 6.2e-4: proved rate, prefactor missing (§2). Measured: |S|·|w*| + Σ even ≈ 1e-6.
  - **(T)** |X_tail| absolute: unproved. Measured remainder 1e-7 per position.
  - **(Y)** See §6.
- **Superseded result.** The earlier N11 robustness scans (`r_robust*.py`; tail threshold 4e-5, crossover region p ≈ 2–3e3) were done under the N10 model and are superseded by the closed form. They are kept for the record.

## 5. Status of the referee's four items
1. **Absolute A∞ tail for every p:** OPEN.
   - Budget: the per-position remainder must be < 6.2e-4·(1−θ). Equivalently, |X_tail| ≤ (1−θ)·2((1+6.2e-4)^p − 1), which grows exponentially.
   - Evidence: remainder 1e-7, decaying across shells [N].
   - Long cores: the short-block r₂ table gives HS² decay for k ≥ 20 (8V). A *pointwise/absolute* bound still needs (R1) or G.
   - Short cores (k < 20) are p-independent but number about 10⁷ classes. A collective (digit-transfer) certificate is needed, not per-class certificates.
2. **Coding:** DONE for dilute configurations [P] (§3). Dense ones are negligible in the model.
3. **Cluster/interaction bound keeping |X_gas| away from 0:** the "away from 0" part is now trivial in the corrected model (|1+X_gas| ≥ 2(1+ReΛ)^p − 1). The interaction rate is proved (κ = 0.41765). The prefactor is open; it needs an adapted-norm certificate (§2).
4. **Completeness of the type list:** [N] at p = 29 and 47 (all classes |N| ≤ 400 / 2000). It found the missing 2-odd-bump background-0 term (now in the model). The residual is 1e-7. Not proved.

## 6. Y in modulus form; coordination with gap (b) (N9b)
- **Requirement.** |Y(p)| ≤ (1−θ)·2((1+Re Λ_lo − δ_int)^p − 1) − |X_tail|, where Y = unit + mixed + partially isotropic parts. Cross-line points belong to X and are also (b′).
- **The budget grows exponentially** (≥ 2.47 at p = 1289, ≥ 43 at p = 5000).
- **For N9b.**
  - Their C2′ divisor-sum obstruction (polynomial margin A_p·ω(h_p)(2p)^{1−β}) is **absorbed in modulus form** for all large p, because a polynomially growing |Y| loses to e^{6.2e-4·p}.
  - Primality of h_p is therefore not needed *for Y*, provided their G* gives |Y| ≤ poly(p) with p-independent constants. G itself (unit/mixed patterns) remains their open input.
  - For squarefree h_p, Theorem C′ already gives exponentially small unit Y [P+CA].
  - I have not edited N9b files. This is a statement for them to adopt or refute.

## 7. REPORT_N9_v2 (referee N9-F1..F4)
- **F1.** Restated: "the HS/op product majorant with joint ζ-averaging cannot close (5.409 vs 2.193 per λ-step) [CA*]". This is not a no-go for all Fourier routes.
- **F2.** The C′ deep-route index argument uses the *current* C′ rate 1.274 ((1.42785/1.2744)³ = 1.4065 < ε). It would reopen only if C′ < 1.0657.
- **F3.** "p-uniform real-part A∞ is false" is **[H, model]**.
- **F4.** z0_e4 is certified positive (Re ∈ [3.546e-9, 2.079e-6]). z0_e4s2 has indeterminate sign and goes in the absolute budget (|w| ≤ 4.24e-8), as done in Re Λ_lo above.

## 8. REPORT_N10_v2 (referee N10-F1..F6, plus the model erratum)
- **E0 (new, from N11).** The N10 model X = 2[e^{pR}(sinh(2pw*)+1) − 1] omitted background-0 configurations with an even number ≥ 2 of odd bumps.
  - Correct: X = 2[(1+R+2w*)^p − 1].
  - All N10 large-p numbers change:
    - Re X < 0 first at 4099, not 4287;
    - |X(1165)| = 3.09, not 2.23;
    - |X(10001)| = 3.6e3, not 1.8e3;
    - min over p ≥ 29 of |1+X| is 1.044.
  - Conclusions are unchanged in direction: the modulus route survives, now with a closed-form lower bound.
- **F1.** Y = unit + mixed + partially isotropic. It is controlled by C′ only for squarefree h_p. "Trivially satisfied" is withdrawn (§6).
- **F2.** The correct bound is Dev_{h_p} ≥ (n|Z|²/h_p²)[(|1+X_gas| − |X_tail| − |Y|)² − 1], used in §4.
- **F3.** Inherited levels e·h_p use the positivity floor (−(I−1) ≈ −0.2 in level-h_p units), included in §4.
- **F4.** The first Re X < 0 is stated per form (product / exp). Both are [H, model].
- **F5.** Minima are quoted for p ≥ 29, where the gas is meaningful: min|1+X| = 1.044 (corrected model). The theorem range is p ≥ 1289.
- **F6.** R is recomputed from the listed activities: 6.1850e-5 − 1.9431e-5 i, now including c₈ and c₁₆; the referee's 6.1838e-5 omitted them. W′/m ≈ 1.12e5 at m = 141 is **[model]**; with the corrected model it is ≈ +1.13e5.

## Files
- **code:**
  - t_classes.py: all classes |N| ≤ Nmax, both backgrounds.
  - t_summary.py, g_model2.py: corrected model and completeness residual.
  - c_coding.py: Lemma C constants and exact check.
  - r_robust.py, r_robust_grid.py: superseded, N10 model.
- **logs:**
  - certV_eta2_a4_r2_{0.85,0.80}.{json,out}: Line F cert_lift rerun, sector 4.
  - kappa_cert.out, lambda_cert.out.
  - t_classes_p29_N400.json, t_classes_p47_N2000.json, t_summary.out, t_signed.out, g_model2.json.
  - c_coding.json, r_robust*.
