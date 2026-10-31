# REPORT N10b — modulus-form target, D1 certificate pre-flight, R₄ automaton obstruction, D2 + stay count, h₁₃ line
Labels: [P] · [P-sketch] · [CA] arb · [CA*] float+margin · [N] · [H]. Nothing pushed; earlier lines untouched (one new note file in N11).
2026-10-31, Asia/Yekaterinburg (UTC+5). Inputs: N9b, N11 (REPORT_N11 §1–§6), referee lineN8.

## 0. Summary
| # | Result | Label |
|---|---|---|
| 1 | **N11's modulus-form claim verified.** In Dev_{h_p} ≥ (n\|Z\|²/h_p²)[(\|1+X_gas\| − \|X_tail\| − \|Y\|)² − 1] the budget grows like 2((1+6.238e-4)^p − 1). Gap (b) then needs **G\*(Γ < T′ = 1.4279, A = e^{o(p)})** and **neither Γ < 1.2329 nor any primality/ω(h_p) hypothesis**. The rank-p divisor sum is e^{o(p)} for every β > 1 and is absorbed. The rank-3p/unit margin needs β > 1 − 7.1e-4, i.e. Γ < 1.4282. | [P-sketch] (bookkeeping on top of N8b Lemma Σ + N11 Thm) |
| 2 | **D1 cone-field certificate: pre-flight shows it cannot pass as designed.** I did not launch an hours-long run. On 4000 random cells of the 1024-grid (outside the 1/8-boxes of all four slow fixed points), k-step cone invariance holds in only 41.6 / 52.9 / 58.4 % of cells for k = 6 / 8 / 12, even in an adapted (averaged-Lyapunov) norm. The worst s₂/\|α₀\| is 91–179. In the raw norm it is 0–18 %. k-step letters would need ~λ^{k−2}/w² cells (~4e10). | [N] |
| 3 | **4-fold collision automaton cannot certify R₄ ≤ 2.611.** The 4-fold Lemma-O1 majorant is the 2-fold carry automaton with ρ → ρ∗ρ. Its rate is ≥ ρ(M₄(0)) ≥ **5.41151** [CA, arb Collatz–Wielandt lower bound], > 2.611. Monotonicity in τ gives entrywise domination [P]. The loss is ρ̂(0)² = 31.5 against the true ≤ μ*⁴. This is the same 5.41 as N9's joint A+B rate. | [CA] + [P] |
| 4 | **R₄ via G\* instead:** R_s ≤ max(Γ_out(θ)^s, μ*^s/λ)·(gas). So R₄ ≤ 2.611 ⇐ Γ_out(θ) ≤ 1.2712 (periodic profile: 1.2624 at θ = 1/8, 1.2185 at 3/16). | [P-sketch] + [N] |
| 5 | **D2 (per-stay bound) [P]** with explicit certified constants, but K_stay is astronomically large (∝ exp(6e6·Σδ)). A usable version needs an adapted-norm certificate. That is **the same open item as N11 §2**: shared stay/bump lemma, note left in N11. | [P] + assessment |
| 6 | **Stay-count lemma [P]:** #{level-q points with a θ-stay of length ℓ at a given position} ≤ C_θ(1 + q²λ^{−ℓ})(1+ℓ). The "1" term is exactly the small-β points (\|r\| = 1.32e-3, flat in p). Multi-stay counting needs N11's coding lemma [P-sketch]. | [P] / [P-sketch] |
| 7 | **h₁₃ inconsistent line recomputed with all slow time:** Γ_raw = 1.367. Counting slow time at {0,½} only: still 1.367, because the top class sits near twists ¼/¾. Counting **all four** slow fixed twists: Γ_eff ≤ **1.181** (θ = 1/16), **1.104** (θ = 1/8). The full Z is slow at all of 0, ¼, ½, ¾ (rate 1.8817 each). | [N] |

**Net.** G\* reduces to D1 only if an adapted-norm D2 holds, which is shared with N11. D1's target is T′ = 1.4279. No D1 certificate exists, and the cone method as designed fails its pre-flight.

## 1. Modulus form: what G\* must deliver (verifies N11 §6)
- **Setting.**
  - N11 Theorem: Dev_{h_p} ≥ (n|Z|²/h_p²)[(2(1+ReΛ_lo−δ_int)^p − 1 − |X_tail| − |Y| − e^{−0.28p})² − 1] − 0.2(n|Z|²/h_p²).
  - X_tail contains the proper-divisor consistent classes; N9: they are deep (a)-classes at h_p with N(e) = (h_p/c)N(f).
  - Y = unit + mixed + partially isotropic.
  - Budget: |X_tail| + |Y| ≤ (1−θ)·2((1+b)^p − 1), with b = ReΛ_lo − δ_int ≈ 6.2e-4.
- **Lemma Σ\* (under G\*(Γ, A)).** Contributions relative to the old Lin normalisation F_m ≍ p·Re w* are:
  - (a) rank p: A·S_β·Σ_{d∣h_p,d>1} d^{1−β};
  - (b)–(d): A·e^{o(p)}·λ^{(p/2)(1−β)}.
  - In X/Y units, multiply by O(p).
- **(a) with β > 1.**
  - Σ_{d∣h_p,d>1} d^{1−β} ≤ exp(Σ_{r∣h_p} r^{1−β}/(1−r^{1−β})) − 1, prime powers allowed (referee F2).
  - The distinct primes satisfy r_j ≥ 2pj+1 and ω ≤ log h_p/log(2p+1) ≤ 0.89p/ln(2p).
  - So the sum is ≤ exp(C_β p^{2−β}(ln p)^{β−2}) = e^{o(p)} [P].
  - Absorbed for p ≥ p₁(β) [P]. p₁ is finite for every β > 1 but astronomically large when β → 1⁺ with worst-case ω; actual ω(h_p) ≤ 3 for p < 62.
- **(b)–(d).** Need (p/2)(1−β)ln λ + o(p) < p·ln(1+b), i.e. β > 1 − 2ln(1+b)/ln λ = 1 − 7.1e-4. This is Γ < T′·λ^{(1−β)/6} ≈ 1.4282.
  - Strictly β ≥ 1 is needed to keep S_β-type sums in (a) finite uniformly. Use β > 1, i.e. Γ < T′.
- **Conclusion [P-sketch].** In modulus form, gap (b) needs G\*(Γ < 1.4279) with A = e^{o(p)}, hence an all-large-p statement:
  - no primality of h_p (C2's 𝒫 and N9b's C2′ ω-condition are both unnecessary);
  - no 1.2329.
  - Caveat: A must be e^{o(p)} in the strict sense. A gas factor e^{zm} must have 3z < b − (budget used by X_tail) for rank-p pieces. Rank-3p pieces have exponential room λ^{(p/2)(β−1)}.
  - This is conditional on N11's open (I), (T), (Y = this G\*).

## 2. D1: cone-field certificate pre-flight (`code/b_conecheck.py`, `code/f_preflight.py`, `logs/f_preflight.{out,json}`, ckpt/)
- **Design.**
  - Cone K_C(a) = {x : ‖x_⊥‖ ≤ a|⟨u_C, x⟩|} around the rank-one direction u_C.
  - For M = P_k(y): invariance with growth g = |α₀| + a·s₁ requires |α₀| > s₂ and (|α₀| − s₂)² ≥ 4s₁b₀.
  - Here α₀ = ⟨u′, Mu⟩, s₁ = ‖u′*MΠ⊥‖, s₂ = ‖Π′⊥MΠ⊥‖ and b₀ = ‖Π′⊥Mu‖.
- **Fraction of points where invariance holds:**

| norm | k=1 | 2 | 4 | 6 | 8 | 12 |
|---|---|---|---|---|---|---|
| raw (40 pts) | 0% | 0% | 0% | 10% | 18% | — |
| averaged Lyapunov W, J=8 (40 pts) | 0% | 5% | 38% | 48% | 60% | — |
| W, 4000 cells of 1024-grid, outside all four 1/8-boxes | — | — | — | 41.6% | 52.9% | 58.4% |

- Median s₂/|α₀| on the grid is 0.52 / 0.24 / 0.12, but the maximum is 91 / 179 / 60.
- A certificate needs **every** cell and edge. Cells for k-step letters must keep all k twists within w: ~λ^{k−2}/w² cells (k = 8, w = 1e-3: ~4e10).
- **Verdict [N].** The certificate is not feasible as designed. I did not launch a multi-hour run that would certainly fail; the scaled pre-flight was run instead (checkpointed, done, 3 min).
- **What could work [H].**
  - A cell-dependent norm (e.g. N11's proposed adapted norm, or Line F's core basis with b12 = 10.76) in which the off-dominant part contracts at k ≤ 3. Then cells of size λ^{−2}w would be enough.
  - Alternatively, a Hilbert-metric cone (positive cones in a lattice-lifted space) if the transfer operators are positivity-improving there. Not checked.

## 3. D2 and the stay-count lemma (G\* ⇐ D1 + D2 + Lemma S)
- **D2 [P mod Line F/n_cert certificates].** Let b be a slow fixed twist, L_b with ‖L_bⁿ‖ ≤ Cpow·μⁿ (Cpow ≤ 3246.8 [CA, N11 logs]), and ‖L_τ − L_b‖ ≤ 2πN₁|τ − b| with N₁ = 573.59 [CA]. For a stay i = a..a+ℓ−1 with δ_i = |τ_i − b|:

  ‖∏L_{τ_i}‖ ≤ Cpow·μ^ℓ·∏_i(1 + Cpow·2πN₁δ_i/μ)   (expand the product over subsets S, and bound each run of L_b's by Cpow·μ^{run}).

  In a θ-stay of the hyperbolic twist map, δ_i ≤ c_θθ(λ^{−(i−a)} + λ^{−(a+ℓ−1−i)}). Hence Σδ_i ≤ 2c_θθλ/(λ−1) and **K_stay ≤ Cpow·exp(Cpow·2πN₁·2c_θθλ/((λ−1)μ))**. This is p- and ℓ-independent but astronomically large: the exponent is ~6e6·Σδ.
- **Consequence.**
  - With K_stay that large, the stay gas has fugacity ≫ 1 unless stays shorter than ~10⁶ are pushed into D1. That would make D1's target include near-fixed-point passages (rates 1.5–1.65 from the periodic profile, θ < 1/16).
  - **D2 is usable only with an adapted norm in which K_stay = O(1).** The measured stay/bump norms are O(1) (N11: bump factors |b_j| ~ |w*|^{1/2}). This is exactly N11 §2's missing prefactor certificate, so one adapted-norm certificate serves both lines.
- **Lemma S (single stay) [P].**
  - Level-q points ↔ β ∈ O/q, with twist τ_i a fixed linear form of Minkowski(λ^iβ)/q (N2 §1.1, N7 Lemma P).
  - If (τ_i, τ_{i+1}) stays within θ < 1/16 of a fixed twist pair for i ∈ [a, a+ℓ−1], the integer recurrence τ_{i+1} = 6τ_i − τ_{i−1} has no wrap (|6τ_i − τ_{i−1}| ≤ 7θ < ½). So one lift β̃ realises the real sequence.
  - It follows that |emb₁(λ^aβ̃)| ≤ c q θ λ^{−(ℓ−1)} and |emb₂(λ^aβ̃)| ≤ c q θ (shifted by the fixed point's lift).
  - O ↪ R² is a lattice with |N(γ)| ≥ 1 for γ ≠ 0 and unit group ±ε^Z. So an axis box of area A contains ≤ C(1 + A)(1 + log₊A) points.
  - Hence #{β : stay of length ≥ ℓ at position a} ≤ C_θ(1 + q²λ^{−ℓ})(1 + ℓ).
  - The term 1 is the small-β family (N9b's US class, |r| = 1.32e-3 flat in p). It has O(ℓ) members per position, so it is harmless against any 1/q² point weight.
- **Multi-stay [P-sketch].** For configurations of stays, a product bound needs injectivity of the configuration → β map. That is N11's coding lemma (§3; dilute configurations, gaps ≥ g₀ = 5) with bump seeds replaced by stay seeds. Joint lemma suggested to N11.
- **Assembly [P-sketch].**
  - Σ_x |r(x)| ≤ Σ_configurations (count by Lemma S + coding)·K_stay^{#stays}·C_out·Γ_out^{m−s}μ*^{s}/|Z₀|.
  - This gives Lemma Σ\* with a gas factor e^{z·m}, z = Σ_{ℓ≥1} K_stay C_out (μ*/(λΓ_out))^ℓ·C_θ(1+ℓ).
  - z must be < b/3 ≈ 2e-4 for rank-p pieces (§1), which forces K_stay·C_out·μ*/(λΓ) ≲ 1e-4. That requires either long minimum stay length or K = O(1).
  - **This is the quantitative reason the adapted norm is indispensable.**

## 4. R₄ (task 2) (`code/a_r4_float.py`, `code/e_r4_lower.py`, `logs/e_r4_lower.json`)
- **Reduction [P].** ‖A‖_HS⁴ ≤ C_pair²∏ρ̂_i(τ_i)², and ρ̂² = FT(ρ∗ρ) ≥ 0. Integrating over y keeps exact collisions of w = v+v′, so the 4-fold automaton is N2's carry automaton with letter weight ρ∗ρ. The carry bound becomes |e| ≤ ⌊2V/4⌋.
- **Rates.** Float: s = 2 gives 1.051116 (= N2's r_abs, sanity); s = 4 gives 5.411513 (E = 6, 10, 14 identical).
- **[CA] lower bound.** ρ(M₄(0)) ≥ 5.41151079436262 (arb, 128-bit, Collatz–Wielandt on a 75-state principal submatrix; Bessel truncation only lowers). The s = 2 sanity value is 1.05111584011868.
- **Lower bound for the method [P].** Middle letters have τ_j ≥ 0, ρ_d(τ) is increasing in τ, and C_pair ≥ 1. So the block matrix dominates M₄(0)^k entrywise, and r₄(k) ≥ 5.4115 > 2.611 for all k.
- **Alternative [P-sketch].** Use the variational principle for the subadditive potential s·log‖P‖ (Cao–Feng–Huang) plus zero entropy of stays: R_s ≤ max(Γ_out(θ)^s·e^{gas}, μ*^s/λ). R₄ ≤ 2.611 ⇐ Γ_out ≤ 1.2712. The periodic profile is 1.2624 at θ = 1/8 and 1.2185 at θ = 3/16 [N]. Thin margin; not certified.

## 5. h₁₃ inconsistent line (`code/d_h13.py`, derived from N8b b_cline.py read-only; `logs/d_h13.jsonl`)
- Setup: p = 13, c = 47321 = 79·599, line inc:79, all 1794 classes, m = 39.
- max|r| = 1.927e-6, so Γ_raw = 1.367 (A = 1, s = 0). N8b's 1.267 used forced windows only.
- Γ_eff counting slow time near {0, ½} only: 1.367 at θ = 1/16 and θ = 1/8. The top class s = 157 has no time near 0 or ½; it lingers near ¼ and ¾ (N8b's slow_q = 21).
- **Γ_eff counting all four fixed twists:** max 1.181 (θ = 1/16), 1.104 (θ = 1/8); the top class drops to 1.177 / 0.640.
- `code/c_constZ.py`: |Z(τ ≡ t)|^{1/39} = 1.8817 for t = 0, ¼, ½, ¾ (0.1250-twist: 1.4509). So **G\* must use the boxes of all four fixed twist pairs**. N9b's Γ_eff values (two boxes only) are therefore upper estimates.

## 6. Coordination
- `/workspace/bgs-lineN/N11/NOTE_FROM_N10b.md` (new file). It contains the modulus-form verification, the shared stay/bump lemma (D2 ≡ N11 gap splitting; one adapted-norm certificate serves both), Lemma S, and the four slow fixed twists.

## 7. Status / best route
- **Proved:** D2 (huge constant), Lemma S single stay, the R₄ automaton obstruction [CA], and the modulus-form bookkeeping [P-sketch].
- **Open:**
  - **D1** (Γ_out(1/8) < 1.4279, all four boxes): no certificate; the cone design fails its pre-flight.
  - The **adapted-norm certificate** (shared with N11), which makes D2 and the stay gas usable.
  - The multi-stay coding lemma.
- **Best next step:** the adapted-norm certificate. Construct a norm from Line F's spectral data (Π, κ = 0.4177) plus a finite bump/stay block list, in which K_stay = O(1) and the off-dominant part contracts at k ≤ 3. Then redo the cone pre-flight in that norm; cells at k ≤ 3 are ~1e6–1e7, which is feasible as [CA*].

## 8. Files
code: a_r4_float.py, b_conecheck.py, c_constZ.py, d_h13.py, e_r4_lower.py, f_preflight.py · logs: d_h13.jsonl, d_h13.out, e_r4_lower.json, f_preflight.{out,json} · ckpt/f_preflight.json · NOTES_N10b.md · SHA256_N10b.txt (+ .sha256)
