> **Packet copy (Line B, IDs BGS-TRACE-163 to 182).** On main at 502af245 the highest TRACE id is BGS-TRACE-162, so 163 is the next free id; the block was not renumbered. This is the detailed phase report cited by `../derandomized_fixed_kick.md`, copied unchanged below this box. Its status labels ([P], [P-sketch], [N], [C], [Cert], [L], [H]) are the working labels; the **integration status of every claim is the one in `../derandomized_fixed_kick.md` and `record/claims.json`**, which follow the referee's table (audit §8.10) with the second-reader upgrades of 167, 169 and 173 (`computations/verification/lineB/second_reader/SECOND_READER_REPORT.md`). Path map: `code/`, `logs/` (relative to phase4) → `computations/verification/lineB/phase4/`, `…/phase4/logs/`; `lean/Phase4Checks.lean` → `formalization/Bgs/LineBPhase4.lean` (`Bgs.LineB.Phase4`).

# Phase 4 report: rigorous parity term, Conjecture R, torsion

[ref8-fix] Status vocabulary for integration (referee §8.10): proved / verification-pending / conditional / numerical-only / open. Theorem D_cert is verification-pending (computer-assisted); fixed-η decay is conditional on (I1)–(I3).
Labels: [P] proved here; [P-sketch] proof outline whose cited inputs are not re-verified; [Cert] machine certificate (rigorous given IEEE-754 semantics and arb; see §1.3); [N] numerics; [C] conjecture; [H] heuristic; [L] Lean-checked finite instance.
Conventions follow the referee audits: ξ ∈ Fix(T^m), T = [[0,1],[−1,6]]; h = h_m (NSW); V^_odd ≅ (Z/h)² via (x₀,x₁); σ² := ‖u‖₂² = 4‖f_odd‖² = 3.75·10⁻⁴.
**Split used throughout (referee item (a)):** F_m(η) = B^sym_m + 2mχ_m(η) + W̃^rest_m(η), with W̃^rest := W^rest + E (|E| ≤ 4m²/h). Every "W^rest" number of phase 3 is a W̃^rest number. REPORT2/REPORT3 were not edited during the work; the referee's wording fixes were applied at the end (§6).

## 0. Summary of what is proved

1. **Lower bound, all η, all odd m ≥ 5 [P; finite cases L].** χ_m(η) ≥ 1 − ½mσ²η². Ingredient: Lemma V (no short 2-sparse relation n ∈ HZ^m + Z𝟙), proved for m ≥ 9 by a norm inequality and for m = 5, 7 by a finite check. It fails at m = 3 (n = 7e₀), where E X² = 0.003 ≠ 3σ² = 0.001125 [N].
2. **Certified exponential decay on a compact η-range [Cert].** For every η ∈ 𝓘 = [1, 81.574] (93 certified intervals, §1.4) and every odd m,
   |χ_m(η)| ≤ C_I · ρ_I^{m−1}, with ρ_I ∈ [0.853, 0.99986] and C_I ≤ 3.64·10⁶ certified per interval I.
   - η ∈ (81.6, 100] is not certified: the tilted majorant with β = 0.1 has ρ → 1 there, and smaller β needs boxes ≫ 5.5·10⁵ states. The decay there is [N] (phase-3 spectrum) plus the conditional argument of item 3.
   Hence 2m|χ_m(η)| ≤ 2m C_I ρ_I^{m−1} → 0 exponentially, with an explicit crossover m ≥ m^+(η,δ) := 1 + log(C_I/δ)/(−log ρ_I) ⇒ |χ_m| ≤ δ.
3. **Decay at every fixed η ≠ 0 [conditional on (I1)–(I3); ref8-fix].** Conditional on three cited inputs (§1.6): (I1) Faure–Roy / Rugh Ruelle–Pollicott spectral theory for real-analytic Anosov maps with an analytic weight, (I2) the mean ergodic theorem for peripheral resonances, (I3) Livšic / Pollicott–Walkden for S¹-valued cocycles. Then the leading resonance has modulus μ(η) < 1 for every η ≠ 0 and |χ_m| ≤ C_η(μ(η)+ε)^m. Last step (referee): a peripheral eigenvalue would make the cocycle a continuous coboundary, which sums to zero on every periodic orbit, so X ≡ 0 on 𝒮, contradicting Prop L. The inputs are cited, not re-verified; C_η is not explicit.
4. **Two-sided crossover [P/Cert].**
   - For m ≤ 2δ/(σ²η²): χ_m ≥ 1 − δ (all η).
   - For m ≥ m^+(η,δ): |χ_m| ≤ δ (η ∈ 𝓘).
   - The two scales are far apart: at η ∈ [1, 1.1] and δ = 0.01, the lower window is m ≤ 44, the Gaussian prediction log(1/δ)/(σ²η²/2) is 24561, and the certified m^+ is 138785.
   - The gap has two sources: the constant C_I ≈ 3·10⁶ (log C_I ≈ 15) and the interval-inflated ρ_I. The certified rate −log ρ_I equals 0.27–0.62 of the Gaussian σ²η²/2 for η ≤ 2 (table column), and less at larger η, where the Gaussian law itself fails (referee: −log μ/η² = 1.25·10⁻⁴ at η = 50).
   - So the asymptotic law μ(η) ≈ exp(−σ²η²/2) is **not** turned into a sharp two-sided bound. What is proved is a lower bound on χ_m in the window m ≲ 1/(σ²η²) and a certified exponential upper bound with an explicit but non-sharp rate.
5. **Conjecture R [C], restated precisely** (§2) with the referee's corrections: no torsion-removal clause is needed (it is replaced by an exact torsion-class split, which shows the torsion classes carry no anomaly at η ≥ 10). The literature check confirms that none of the known tools apply in this minimal-period regime. No power saving, subsequence result or reduction to a standard named conjecture was obtained.
6. **Torsion [P identity, N].** The exact split F = F_gen + F_tor over the norm classes r ≡ 0 (mod p) is computed for m = 9 (p = 7, 199) and m = 11 (p = 23, 353). **Negative finding:** the m = 11, η = 2 outlier (F/2m = 5.56) is *not* carried by the 23-torsion classes. The generic classes alone give the normalised excess +3.25. So the phase-3 attribution (mechanism (b)) is withdrawn; the outlier remains unexplained.
7. Fixed-η CLT via higher moments: **not attempted** (time spent on 1–2).

## 1. The parity term

### 1.1 Lower bound [P]

**Lemma V.** Let m ≥ 5 be odd, Λ = HZ^m + Z𝟙 (the dual lattice of Theorem T). Then no nonzero n ∈ Λ has |supp n| ≤ 2 and ‖n‖_∞ ≤ 18.

*Proof.*
- Let O = Z[√2], λ = 3+2√2, ε = 1+√2. Then λ^m − 1 = ε^m(ε^m − ε^{−m}) = 2hε^m, so λ^m ≡ 1 (mod hO).
- The map O/hO → V^_odd, γ ↦ (Tr(γλ^j))_j is a bijection: injectivity follows from Tr γ ≡ Tr(γλ) ≡ 0 ⇒ γ ≡ 0, since h is odd.
- Σ_j n_j x_j = Tr(γα_n) with α_n = Σ n_jλ^j. So n ∈ Λ ⇔ Tr(γα_n) ≡ 0 for all γ ⇔ α_n ∈ hD⁻¹ ∩ O = hO. The inverse different is (2√2)⁻¹O, and h is coprime to 2√2.
- Hence h² | Nm(α_n).
- By shift and reversal invariance, take n = a e₀ + b e_d with 0 ≤ d ≤ (m−1)/2. Then Nm(a + bλ^d) = a² + b² + abT_d with T_d = λ^d + λ^{−d}. This is nonzero for (a,b) ≠ 0, since λ^d is irrational for d > 0, and for d = 0 it equals (a+b)² ≤ 324 < h².
- Also |Nm| ≤ 324(2 + T_{(m−1)/2}) < (T_m − 2)/4 = h² for m ≥ 9 [L: m9_norm, h9_sq; the ratio grows by ≈ λ^{1/2} per step].
- For m = 5, 7 (h = 41, 239 prime) use the q-sequence with x = (0,1): x_d = U_{d−1}, and h ∤ U_{d−1} for 1 ≤ d < m [L: m5_U, m7_U, m5_prime, m7_prime]. So h | bU_{d−1} forces b = 0, and then h | a forces a = 0. ∎
- Brute-force confirmation for all odd m ≤ 61 [N, logs/lemmaV.log]. m = 3: 52 violations, e.g. 7e₀.

**Proposition L.** For odd m ≥ 5 and all real η: E X = 0, E X² = mσ², χ_m(η) = E cos(ηX) ≥ 1 − ½mσ²η², where X(x) = S(½+x/h) − S(½−x/h) and the expectation is uniform over V^_odd.

*Proof.* X = Σ_j u(x_j/h + ½) is a trigonometric polynomial with modes |k| ≤ 9 in each coordinate. E[e(⟨n,x⟩/h)] = 𝟙[n ∈ Λ] (characters of V^_odd; the ½-twist is a phase that is trivial on the pairs that survive). The terms of E X² have |supp| ≤ 2 and ‖n‖_∞ ≤ 18. By Lemma V only n = 0 survives, i.e. the same j and k′ = −k, which gives m·Σ|û_k|² = mσ². Also χ_m is real because X is odd under x ↦ −x, and cos y ≥ 1 − y²/2. ∎

Check [N, logs/lowercheck.log; independent p2lib code]: E X² = 0.001875, 0.002625, 0.003375 = mσ² exactly (to 10 digits) for m = 5, 7, 9; χ ≥ LB at all tested η. m = 3: E X² = 0.003, and the bound fails (χ₃(1) = 0.998502 < 0.999437).

### 1.2 Majorant and cycle inequality [P]
- States s = (p,q) ∈ Z², transitions s → Ts + (0, a − n) with weight ŵ_η(n); T(p,q) = (q, 6q − p) (Theorem T).
- Eigen-coordinates u_s, t_s along λ, λ⁻¹. N(s) = |u_s| + |t_s|, L(s) = |u_s| − |t_s|.
- L(Ts) − L(s) ≥ γ₀N(s) with γ₀ = 1 − λ⁻¹ = 2√2 − 2. A kick (0, δ) changes L by ≤ c|δ| with c = 1/(2√2). Around any closed cycle: γ₀ΣN(s_j) ≤ cΣ|n_j − a|.
- Hence for β > 0 the tilted matrix A_a[s→s′] = e^{−βγ₀N(s)} b(n) e^{βc|n−a|}, with b(n) ≥ sup_{η∈I}|ŵ_η(n)|, satisfies |Tr M_a(η)^m| ≤ Tr A_a^m for all η ∈ I (cycle products of the tilt are ≥ 1).
- Used constants (rounded safely): γ₀ ≥ 0.8284, c ≤ 0.35356 [L: G0_SAFE_ok, CC_SAFE_ok].
- Collatz–Wielandt trace bound: if v > 0 and A v ≤ ρv on all of Z², then Tr A^m ≤ ρ^{m−1} Σ_s (Av)(s)/v(s), because A^{m−1}(Av) ≤ ρ^{m−1}Av.

### 1.3 The certificate [Cert] (code/certify3.py, code/grid.py)
For each η-interval I = [η₀, η₁]:
1. **Coefficient envelopes.**
   - ŵ_{η₀}(n) is enclosed with arb (python-flint, 128-bit) as a product of Bessel sequences with a rigorous truncation tail.
   - Over I a Gronwall/Taylor bound applies: |ŵ_{η₀+t}| ≤ Σ_{i≤4} t^i (|D|*)^i|ŵ_{η₀}| + geometric remainder in tilted ℓ¹, where D is the coefficient sequence of u, ‖D‖₁ = 0.06.
   - **Truncation tail and edge mass (gaps G1, G2) [ref8-fix]; code/certify_v2.py.**
     - The J-truncation tail of the Bessel product is bounded directly in the tilted norm ‖f‖_τ = Σ|f(n)|e^{τ|n|}. This norm is submultiplicative under convolution.
     - Per factor k: Σ_{|j|>J}|J_j(x_k)|e^{τk|j|} ≤ 2y^{J+1}/(J+1)!·e^{y}, with y = |x_k|e^{τk}/2, using |J_j(x)| ≤ (|x|/2)^j/j!.
     - Errors combine as err ← err(L_k + t_k) + L_{<k}t_k. Over the interval they are multiplied by 1/(1 − ε‖D‖_τ), covering all Taylor orders.
     - With J = 60 the tilted tail is ≤ 10⁻²⁰⁴ at η = 1 and ≤ 2.1·10⁻⁸⁶ at η = 81.6, far below the 10⁻³⁰ demanded. This replaces the unproved `tl·1e40`.
     - The coefficient arrays are padded by 36 = 4·9 zeros on each side before the four Taylor convolutions. The mass leaving the array is computed exactly (edge parts of the full convolution) and added to the remainder, tilted at the worst |n|; it is exactly 0 in all runs.
   - Independent FFT check (no arb): max |ŵ_η(n)|/b(n) ≤ 0.99996 on 12 sampled η in each of 24 intervals (every 4th; logs/check_bounds.log).
2. **Test vector on a box.**
   - Box S_{K₂} = {N ≤ K₂} with K₂ = λ(K_mid + c·x₂) + 1; between 1.2·10⁵ and 5.5·10⁵ states.
   - v = max(φ, v_iter), where v_iter is the float Perron vector (ARPACK) refined by value iteration v ← max(φ, (Av + b_out)/ρ_t), and φ = θe^{−κN} with θ = 10⁻⁹, κ = β/2, β = 0.1.
   - Outside the box: v = C e^{−κN}. C is chosen with C ≥ sup_{N≥K_mid} v e^{κN} (checked).
3. **A-posteriori verification.**
   - (A v)(s) ≤ ρ_in v(s) is checked on every box state, with the outside contributions b_out (exact sums against C e^{−κN}) and the dropped coefficient mass (≤ Vg with Vg ≥ max v, checked).
   - All sums have nonnegative terms of ≤ ~400 summands, so IEEE rounding error is ≤ 400u ≈ 10⁻¹³ relative. This is covered by the factor SAFE = 1 + 10⁻⁹.
4. **Outside the box (analytic).** ρ_out ≤ e^{−(β−κ)γ₀K₂}W_{β+κ} + e^{−(βγ₀−κ)K₂}·T_{x₂}Vg/C. The second term covers landings in the core, which need |n − a| ≥ x₂.
5. **Result.** ρ_I = max_a max(ρ_in, ρ_out) and C_I = Σ_a [Σ_{box}(Av)/v + (W + T·Vg/C)·lattice tail], where the lattice tail uses #{N ≤ R} ≤ (2R+1)(2λR+1).
- For a = 1, 2, 3 the target ρ_t is floored at min(0.95, ρ_t(a=0)) to keep C small. These a have float radii ≈ 0.08–0.4 for η ≲ 11, increasing to ≈ 0.98 near η = 81 [ref8-fix].

What is not interval arithmetic: the matrix–vector products are IEEE float. The argument in step 3 is the standard a-priori bound for summing nonnegative terms, not directed rounding. arb is used for the coefficients. **Hypothesis [ref8-fix]: the a-priori bound also assumes that libm exp/log are accurate to ≤ 4 ulp** (true for glibc; not an IEEE-754 guarantee); the factor SAFE − 1 = 10⁻⁹ absorbs this with a margin of ~10⁶. There are no subnormals (smallest product ≈ 10⁻⁶²). An independent directed-rounding re-certification (referee, audit code t9_cert.py: arb ball envelopes, nextafter after every float operation) confirms 6 of the 93 intervals, with certified ρ ≤ the values here. Status for integration: **verification-pending (computer-assisted)** until all 93 are re-certified with directed rounding. **[second-reader, 2026-10-29]** The full directed-rounding re-certification has been done by the second reader with t9_cert.py (unmodified): 93/93 intervals valid, contiguous on [1, 81.57406988332305], max ρ' = 0.999820, max C' = 1.43e+07 (for a ≠ 0 t9 floors ρ' at 0.9). Theorem D_cert is therefore proved (computer-assisted) **with the directed-rounding constants**, not with the float constants of §1.4. See packet `computations/verification/lineB/second_reader/`.

**Rerun with the fixed envelopes (G1/G2) [ref8-fix].** code/rerun_grid.py recomputes every one of the 93 intervals with certify_v2.bounds_v2 and the original parameters (logs/grid_v2_w0/w1.jsonl, summary logs/grid_v2_summary.json, code/summarize_v2.py). Result: all 93/93 intervals certify again; coverage [1.0, 81.57407] contiguous; max_a ρ ∈ [0.852733, 0.999860], largest change against the original grid 6.7e-16; max Σ_a C = 3.639e+06; largest remainder mass 4.92e-04; largest tilted truncation tail 2.0e-86; edge spill 0 everywhere. The table of §1.4 is therefore unchanged. This rerun uses the same IEEE-float method with the a-priori bound (not interval arithmetic, not directed rounding), so it does not discharge blocker B1: the status of Theorem D_cert stays **verification-pending (computer-assisted)**.

### 1.4 Certified table
Coverage ([(1.0, 81.57407)]); 93 certified intervals, all four a valid with max_a ρ_a < 1. Full table: logs/grid_summary.txt; raw: logs/grid_s*.jsonl.
Every 3rd row is shown below. Columns: ρ_I and C_I (summed over a); the ratio of the certified rate −log ρ_I to the Gaussian rate σ²η₁²/2; m⁺ for δ = 0.01; the Gaussian prediction m_gauss = log(100)/(σ²η₀²/2); the lower-bound window m_lo (χ ≥ 0.99).

| η₀ | η₁ | ρ_I | C_I | rate ratio | m⁺(0.01) | m_gauss | m_lo | box states |
|---|---|---|---|---|---|---|---|---|
| 1.0000 | 1.1000 | 0.999860 | 2.8e+06 | 0.618 | 138785 | 24561 | 44 | 116319 |
| 1.4360 | 1.7104 | 0.999803 | 3e+06 | 0.360 | 98911 | 11911 | 18 | 116319 |
| 2.6324 | 3.3853 | 0.999789 | 3e+06 | 0.098 | 92632 | 3544 | 4 | 135123 |
| 4.6503 | 5.0000 | 0.996865 | 3.3e+06 | 0.670 | 6248 | 1136 | 2 | 135123 |
| 5.7200 | 6.3080 | 0.995739 | 3.2e+06 | 0.572 | 4588 | 751 | 1 | 154013 |
| 8.2837 | 9.0904 | 0.991253 | 3.4e+06 | 0.567 | 2238 | 358 | 0 | 166455 |
| 11.0104 | 12.1173 | 0.987067 | 3.5e+06 | 0.473 | 1514 | 203 | 0 | 187353 |
| 15.0000 | 15.5000 | 0.967712 | 3.4e+06 | 0.729 | 600 | 109 | 0 | 217445 |
| 17.1800 | 18.5520 | 0.977389 | 3.5e+06 | 0.354 | 861 | 83 | 0 | 243483 |
| 20.8570 | 22.7393 | 0.995731 | 3.5e+06 | 0.044 | 4597 | 56 | 0 | 277631 |
| 25.9017 | 27.1931 | 0.947305 | 3.2e+06 | 0.390 | 363 | 37 | 0 | 321835 |
| 30.0000 | 30.5000 | 0.898361 | 3e+06 | 0.615 | 184 | 27 | 0 | 352647 |
| 32.1800 | 33.5520 | 0.936565 | 3.1e+06 | 0.310 | 300 | 24 | 0 | 369303 |
| 36.8174 | 38.6997 | 0.954556 | 3e+06 | 0.166 | 421 | 18 | 0 | 437409 |
| 41.8621 | 43.1535 | 0.915968 | 2.8e+06 | 0.251 | 223 | 14 | 0 | 491643 |
| 46.2268 | 47.9985 | 0.947708 | 2.9e+06 | 0.124 | 364 | 11 | 0 | 540569 |
| 50.5000 | 51.2000 | 0.862820 | 2.8e+06 | 0.300 | 133 | 10 | 0 | 549927 |
| 53.5520 | 55.4728 | 0.969992 | 3e+06 | 0.053 | 643 | 9 | 0 | 549927 |
| 58.6997 | 60.0174 | 0.967934 | 3.1e+06 | 0.048 | 601 | 7 | 0 | 549927 |
| 62.2311 | 63.1350 | 0.948019 | 3.1e+06 | 0.071 | 368 | 6 | 0 | 549927 |
| 65.2863 | 65.9064 | 0.938752 | 3.2e+06 | 0.078 | 311 | 6 | 0 | 549927 |
| 67.3823 | 68.2330 | 0.975106 | 3.3e+06 | 0.029 | 779 | 5 | 0 | 549927 |
| 69.6623 | 70.0000 | 0.945420 | 3.2e+06 | 0.061 | 351 | 5 | 0 | 549927 |
| 70.7200 | 71.3080 | 0.965689 | 3.3e+06 | 0.037 | 563 | 5 | 0 | 549927 |
| 72.7074 | 73.5142 | 0.996012 | 3.4e+06 | 0.004 | 4916 | 5 | 0 | 549927 |
| 74.4742 | 75.0276 | 0.980836 | 3.4e+06 | 0.018 | 1016 | 4 | 0 | 549927 |
| 75.9574 | 76.3370 | 0.976203 | 3.4e+06 | 0.022 | 817 | 4 | 0 | 549927 |
| 77.2406 | 77.7614 | 0.990739 | 3.4e+06 | 0.008 | 2114 | 4 | 0 | 549927 |
| 78.6365 | 78.9938 | 0.985364 | 3.4e+06 | 0.013 | 1335 | 4 | 0 | 549927 |
| 79.8443 | 80.0894 | 0.985038 | 3.4e+06 | 0.013 | 1305 | 4 | 0 | 549927 |
| 80.6728 | 81.0091 | 0.995662 | 3.5e+06 | 0.004 | 4526 | 4 | 0 | 549927 |
| 81.2445 | 81.5741 | 0.999848 | 3.5e+06 | 0.000 | 129734 | 4 | 0 | 549927 |

### 1.5 Explicit theorem [Cert + P]
**Theorem D_cert.** For every η ∈ 𝓘 (coverage above) and every odd m ≥ 5:
 1 − ½mσ²η² ≤ χ_m(η) and |χ_m(η)| ≤ C_I ρ_I^{m−1}, with C_I, ρ_I from the row containing η.

**Non-claim [ref8-fix].** The upper bound is < 1 only for m ≥ m⁺(η) (≈ 1.4·10⁵ at η = 1, ≈ 6·10³ at η = 5, 10²–10³ for η ≳ 15). It is a qualitative decay statement with explicit but large thresholds and gives no information at m ≤ 13, i.e. at the m where the numerics live, nor (for η ≲ 10) at the NSW-prime m of Theorem N.
In particular 2m|χ_m(η)| ≤ 2mC_Iρ_I^{m−1}, which is ≤ δ for m ≥ m^+ (column m+(.01) for δ = 0.01).
- The lower window m ≤ 2δ/(σ²η²) (column m_lo(.99)) is nonempty only for η ≲ 7 at δ = 0.01.
- The Gaussian scale m_gauss is shown for comparison only; per the referee it is meaningful only for η ≲ 25.

The constants are not optimised: C_I ≈ 3·10⁶ comes from the crude lattice-tail count, and ρ_I is inflated by the interval width (adaptive widths grow ×1.4 after each success). Narrower intervals bring ρ_I to within ~10⁻⁵ of the float Perron root (e.g. ρ_I = 0.999860 vs float 0.999855 at [1, 1.1]).

### 1.6 Every fixed η ≠ 0 [P-sketch → status: conditional on inputs (I1)–(I3)] [ref8-fix]
Setting. T(x₁,x₂) = (x₂, −x₁ + 6x₂) on T² (linear Anosov, eigenvalues λ^{±1}, λ = 3 + 2√2). g = e^{iηu(x₁)} is real-analytic and unimodular. ζ_a(x) = e(−a·θ(x)) is a character whose class in H¹ (characters modulo (Tᵗ − I)Z²) has order dividing |det(T − I)| = 4. 𝓛_a φ := ζ_a·g·(φ∘T⁻¹). By Theorem T and the Poisson step, M_a is the Fourier matrix of 𝓛_a, and χ_m = Σ_a(−1)^a Tr M_a^m.

**Claim.** For every η ≠ 0 there are μ(η) < 1 and C_η < ∞ with |χ_m(η)| ≤ C_η μ(η)^m for all odd m.

Inputs, with citations and hypothesis matching:
- **(I1) Trace class and trace formula.** Faure–Roy, *Ruelle–Pollicott resonances for real analytic hyperbolic maps*, Nonlinearity 19 (2006) 1233–1252.
  - Their torus section treats real-analytic hyperbolic maps of T². After conjugation by an anisotropic analytic weight Â (Fourier multiplier e^{−a|stable component|+a|unstable component|}), the matrix elements of R = Â𝓜Â⁻¹ decay like e^{−c(|n|+|n′|)}, so R is trace class (their Thm 1 and its torus analogue). Its trace satisfies the periodic-orbit formula (their Prop 5 and its torus analogue): Tr R^t = Σ_{Fix(M^t)} 1/|det(DM^t − I)|.
  - Hypothesis match: they treat the unweighted pull-back of a linear (or analytic) hyperbolic map. Our 𝓛_a adds multiplication by the analytic function ζ_a g. In the Fourier basis that multiplication is convolution with ŵ_η (which decays super-exponentially, |ŵ_η(n)| ≤ C_b e^{−b|n|} for every b), times a fixed shift.
  - So the exponential decay of the conjugated matrix elements, which is the only property used, survives with c replaced by c − ε. The trace formula gains the weight Π_j(ζ_a g)(T^j x). This is the analytic-weight extension; for general analytic weights see Rugh, Nonlinearity 5 (1992) 1237–1263 (Fredholm determinants for analytic hyperbolic maps with analytic weights).
  - **Not re-verified here:** the weighted torus statement is written out in neither paper in exactly this form.
  - Consequence: Tr M_a^m = Tr R_a^m = Σ_k ν_{a,k}^m with Σ_k|ν_{a,k}| < ∞.
  - |ν| ≤ 1 (referee): |Tr R_a^m| ≤ #Fix(T^m)/|det(I − T^m)| = 1, so Σ_m Tr(R_a^m) z^m = Σ_k ν z/(1 − νz) is analytic in |z| < 1.
- **(I2) Peripheral resonances are L^∞ eigenvalues.**
  - Let |ν| = 1 be a resonance, with spectral projector Π = Σ_j φ_j ⊗ ψ_j of R_a (finite rank). For analytic test functions φ, ψ, the correlation ⟨𝓛_a^m φ, ψ⟩ equals the trace-class expansion Σ_k ν_k^m c_k(φ,ψ) (Faure–Roy §2.1.4–2.1.5 / torus analogue).
  - 𝓛_a is unitary on L²(T²), since T preserves Lebesgue measure and |ζ_a g| = 1. By von Neumann's mean ergodic theorem (e.g. Walters, *An Introduction to Ergodic Theory*, Thm 1.14 / Reed–Simon I, Thm II.11) the Cesàro means (1/M)Σ_{m<M} ν̄^m𝓛_a^m converge strongly to the orthogonal projector P onto ker(𝓛_a − ν).
  - Comparing with the expansion gives ⟨Pφ, ψ⟩ = c_ν(φ,ψ), which is ≠ 0 for some analytic φ, ψ because Π ≠ 0 and analytic functions are dense. Hence P ≠ 0.
  - For φ ∈ L^∞ the Cesàro means are bounded by ‖φ‖_∞, so Pφ ∈ L^∞ (weak-* limit). This is the standard argument; it uses only (I1).
- **(I3) Measurable ⇒ continuous Livšic for S¹-valued cocycles.**
  - Livšic, *Cohomology of dynamical systems*, Izv. Akad. Nauk SSSR Ser. Mat. 36 (1972) 1296–1320: for a transitive Anosov diffeomorphism with a Gibbs (equilibrium) measure of Hölder potential, a measurable solution ψ of f = ψ∘T·ψ⁻¹ a.e., with f Hölder and valued in a group with a bi-invariant metric, has a Hölder version.
  - As restated in Pollicott–Walkden, *Livšic theorems for connected Lie groups*, Trans. AMS 353 (2001) 2879–2895, §1 (Property (R) "holds for any connected Lie group with a bi-invariant metric", in particular for G = S¹; their Theorem A covers more general G).
  - Hypothesis match: T is a linear Anosov automorphism, transitive. Lebesgue measure is its measure of maximal entropy, i.e. the equilibrium state of the zero potential. f = ν̄ζ_a g is analytic, hence Hölder. G = S¹ is compact abelian.

**Argument.**
1. A resonance |ν| = 1 gives, by (I2) and (I3), a continuous ψ: T² → S¹ with ζ_a g = ν·ψ∘T/ψ.
2. Raise to the 4th power. ζ_a⁴ is a character coboundary, so after absorbing it, e^{4iηu} = ν⁴Ψ∘T/Ψ with Ψ continuous.
3. Write Ψ = e^{2πi(⟨k,x⟩ + φ(x))} with k ∈ Z² and φ: T² → R continuous. The lifted identity on R² reads 4ηu(x) − θ₀ − 2π⟨(Tᵗ − I)k, x⟩ − 2π(φ∘T − φ)(x) ∈ 2πZ. The left side is continuous, so it is constant; a nonzero linear term is unbounded, so (Tᵗ − I)k = 0, i.e. k = 0. Integrating against Lebesgue measure (∫u = 0) fixes the constant, so 4ηu = 2π(φ∘T − φ) + 2πN with N ∈ Z, and N = 0.
4. **Simpler last step (referee).** A continuous coboundary has zero sum over every periodic orbit. The support points ½𝟙 + x/h of 𝒮 are T-periodic orbits of length m (q-sequences), and X(x) = Σ_j u(ξ_j) is exactly that orbit sum. Hence X ≡ 0 on 𝒮 for every odd m. This contradicts Prop L (E X² = mσ² > 0 for any single odd m ≥ 5).
5. So every resonance has |ν_{a,k}| < 1. Since Σ_k|ν_{a,k}| < ∞, the moduli accumulate only at 0, so μ(η) := max_{a,k}|ν_{a,k}| < 1, and |χ_m(η)| ≤ (Σ_{a,k}|ν_{a,k}|)·μ(η)^{m−1}.

**Limitations.** There are no explicit constants. Uniformity in η would need one anisotropic space for a whole η-range, and that is not claimed. Status for integration: **conditional on (I1)–(I3)**. (I2) and (I3) are standard with matched hypotheses. (I1) needs a written weighted-torus version of Faure–Roy, or Rugh's analytic-weight result checked for this setting.

## 2. Conjecture R

### 2.1 Literature (checked this phase; complements the referee's §3.6)
- **Large sieve with quadratic structure**: Baier–Zhao (square moduli), quadratic-polynomial moduli (Acta Arith.), Baier's quadratic amplitudes. All of these concern *many moduli* and one variable. Here there is one modulus h, m variables, and product weights. Not applicable.
- **Kurlberg–Rudnick (Duke 103 (2000) 47–77)**: Hecke equidistribution for cat maps. Their exponential-sum bounds (and the later ord(λ) > N^{1/2+ε} QUE results) need a large order of λ mod N. Here ord_h(λ) = m ≈ 2 log h/log λ is minimal.
- **Bourgain (LNM 1910, 2007); Bourgain–Glibichuk–Konyagin (2006); Bourgain–Gamburd expansion**: sum-product bounds for sums over multiplicative subgroups need |⟨λ⟩| ≥ h^δ. Here |⟨λ⟩| = m ≈ log h, so these are structurally unavailable. Bourgain–Gamburd expansion in SL₂(Z/q) concerns non-elementary generating sets; our group is cyclic (Pell), so it is not applicable either.
- **Faure–Nonnenmacher–De Bièvre (CMP 239 (2003) 449–492)**: scarred eigenstates exist exactly at minimal-period moduli. This is a warning that equidistribution-type statements can *fail* in this regime. Conjecture R is about a different (second-moment, product-weight) object and is not contradicted, but no "QUE-type" input can be borrowed.
- **Duke–Friedlander–Iwaniec bilinear forms**: these give cancellation in Σ α_m β_n e(a\bar m/n)-type sums over many moduli. Here the sum would be over pairs of short lattice vectors with a single modulus; I found no formulation that reduces to DFI.
- **Conclusion**: no reduction to a standard named conjecture was found. The "quadratic large sieve" phrasing of phase 3 is Parseval (referee), and is withdrawn.

### 2.2 Precise statement [C]
**Conjecture R.** Fix 0 < η₀ ≤ η₁ < ∞. Then max_{η∈[η₀,η₁]} |W̃^rest_m(η)|/m → 0 as m → ∞ through odd integers.
- Version R_NSW: the same along odd m with h_m prime. This sequence is not known to be infinite. (Registered separately as BGS-TRACE-210 since 2026-10-30; BGS-TRACE-179 is Conjecture R only.)
- No torsion-removal clause: by §2.3 the torsion classes carry no extra mass at η ≥ 10, and at small η the anomaly is not torsion-supported. The phase-3 clause "after removing classes with gcd(r,h) divisible by p ≤ 28m" is withdrawn.
- Evidence [N] (W̃^rest/2m, phase-3 logs plus the referee's true-W^rest table): |W̃^rest|/2m ≤ 0.11, 0.05, 0.018, 0.008 at m = 7, 9, 11, 13 for η ∈ [10, 400] [ref8-fix]. At m = 13 and η = 25 the value is below the resolution |E|/2m.
- Not obtained: O(m^{1−δ}), density-one or prime-h subsequence results. I report no partial theorem.

### 2.3 Exact torsion-class split [P identity; N]
For a prime p | h, let R_p = {r : p | r}. These are exactly the norm classes of x with x mod p on an isotropic line of q mod p (the lines exist iff 2 is a square mod p). There are #{x : p | q(x)} = (2p − 1)h²/p² points [N: share s_p = (2p−1)/p² reproduced exactly].
Prop C splits as F = F_gen + F_tor, where F_gen sums the pairs with r, r′ ∉ R_p (code/torsion2.py; logs/torsion2_m9.log, torsion2_m11.log).

Normalised excesses e_gen := F_gen/(2m(1−s_p)) − (1+χ) and e_tor := F_tor/(2m s_p) − (1+χ):

| m, p | η | W̃^rest/2m | e_gen | e_tor | F_tor/2m |
|---|---|---|---|---|---|
| 11, 23 | 2 | +3.571 | +3.248 | +7.03 | 0.767 |
| 11, 23 | 5 | +0.147 | +0.127 | +0.36 | 0.196 |
| 11, 23 | 10 | +0.016 | +0.020 | −0.03 | 0.152 |
| 11, 23 | 25 | +0.005 | −0.0003 | +0.05 | 0.116 |
| 11, 23 | 50 | +0.009 | +0.003 | +0.07 | 0.094 |
| 11, 23 | 100 | +0.016 | +0.019 | −0.03 | 0.084 |
| 9, 7 | 10 | −0.019 | +0.084 | −0.32 | 0.406 |
| 9, 7 | 50 | −0.031 | −0.030 | −0.05 | 0.272 |

Reading:
- The 23-torsion classes are over-coherent at η = 2 (e_tor = 7.0), consistent with the large |A_r| seen in phase 3. But they hold only 0.77·2m of F = 5.56·2m. Removing them leaves e_gen = 3.25, so **the outlier is not a torsion effect**.
- For η ≥ 10 both parts agree with 1 + χ within 0.02 (p = 23) and within 0.08 (p = 7, where s_p = 0.27 and finite-m noise is larger).
- I also tried the Fourier-side alternative, removing the components of e^{iηS} invariant under p-torsion translations along the isotropic lines (code/torsion.py, logs/torsion_m11.log). This removes ≈ 2/p of the mass uniformly (F(g°)/F ≈ 0.91 for η ≥ 5), and again leaves the η = 2 excess (+2.80).
- So the "exact correction term" requested is available as an identity, but it does **not** isolate the outlier. The phase-3 mechanism (b) is withdrawn; the m = 11, η = 2 outlier is open [N].

## 3. Files
- code/: wcoef.py (arb coefficients), transfer.py, certify.py (envelopes, remainder, lattice tail), certify3.py (certificate), grid.py (adaptive grid driver), summarize_grid.py, check_bounds.py (independent FFT check), lemmaV.py, lowercheck.py, torsion.py, torsion2.py, explore*.py, diag1.py.
- logs/: grid_s1–s6.jsonl/.out, grid_summary.txt, check_bounds.log, lemmaV.log, lowercheck.log, torsion_m11.log, torsion2_m9.log, torsion2_m11.log, lean_phase4.log, certify3_test.log, explore*.log.
- lean/Phase4Checks.lean (built as Bgs.Phase4Checks; `#print axioms`: none, [propext], or [propext, Classical.choice, Quot.sound] (from norm_num); no sorry/native_decide; logs/lean_phase4_axioms.log): U2_value, sigma2_decimal, G0_SAFE_ok, CC_SAFE_ok, m5_prime, m5_U, m7_prime, m7_U, m3_relation (7e₀ = H₃(1,0,0) + 𝟙) [ref8-fix], m9_norm, T4, h9_sq. Checked with `lake env lean` in my private copy phase3/build (Mathlib from the `lake exe cache get` cache, never built from source). It uses norm_num/decide only, with no native_decide; it compiled with no errors.

## 4. Reproduce
```
P=/workspace/bgs-derand/phase3/venv/bin/python; cd /workspace/bgs-derand/phase4/code
$P lemmaV.py; $P lowercheck.py                      # seconds
OMP_NUM_THREADS=2 $P grid.py 1 5 s1 0.1             # etc. per segment (s1..s6); ~30-60 s per interval, <=3 GB
$P summarize_grid.py; $P check_bounds.py
$P torsion2.py 11 23,353 0.5,1,2,3,5,10,25,50,100   # ~2 min
cd ../../phase3/build && lake env lean ../../phase4/lean/Phase4Checks.lean
```

## 5. Literature added
Bohigas–Giannoni–Ozorio de Almeida–Schmit, Nonlinearity 8 (1995) 203 (the parity crossover is the derandomized analogue of this weak breaking of a classical symmetry; not a Keating–Mezzadri pseudo-symmetry); Pandey–Mehta 1983; Rugh 1992; Faure–Roy 2006; Slipantschuk–Bandtlow–Just 2017; Faure–Nonnenmacher–De Bièvre 2003; Kurlberg–Rudnick 2000/2001; Bourgain 2007; Bourgain–Glibichuk–Konyagin 2006; Baier–Zhao 2008.

## 6. Referee (phases 2+3) wording fixes applied at the end [ref23-fix]
Backups: phase4/REPORT.md.pre_referee23_backup, REPORT2.md.pre_referee23_backup, REPORT3.md.pre_referee23_backup. Scripts: code/apply_ref23_r2.py, code/apply_ref23_r3.py (string replacements, each asserted unique).
- Item 1 (REPORT.md): F1 (δ_m distinctness wording) and F2 (Theorem N bound nontrivial only from m = 29; B_7 by exact ND).
- Items 2–7 (REPORT2): c̃_{±7} = (−360,0); "admissible" deleted, with the automatic-admissibility lemma credited to the referee; B_m → 2m replaced by the explicit bound (O(m⁵/h), m ≥ 29, 11 listed m, NSW-prime infinitude open); C5 "40-digit floating point"; ND^(≤k) includes unequal-length relations; conditional-CLT wording; D2 Reduction [S]; Theorem U: N ∈ (X, 2X], gcd(N, D_m) = 1, (0.20, 0.66) for η ∈ [0.5, 100], and the interpretation fix (N-average reproduces F_m(η), not 2m). Also "frozen except for the [ref-fix] items".
- Items 8–16 (REPORT3): Gauss-sum proof of Prop C for all odd m; self-duality for s, s′ units with h prime; Lemma P(iii) count; W̃^rest defined, with all tables relabelled; tail bound with ‖ŵ‖₁^{m−1}; validation limited to η ≤ 200; decay claim relabelled [N] with the Ruelle–Pollicott pointer; m_* scope (η ≲ 25), Ehrenfest comparison (η ≲ 9 at X = 10^{160}), BGOS replacing the Keating–Mezzadri attribution; Parseval wording, minimal-period caution, Conjecture R restated; §5 small-η outliers, KS as a heuristic yardstick, doubled variance [H]; literature added. In addition, the phase-3 torsion attribution of the η = 2 outlier is marked withdrawn (phase-4 finding).

## 7. Referee phase-4 audit (§8) fixes [ref8-fix]
Backups: phase4/backups_pre_ref8/. Script: code/apply_ref8.py (+ this file).
- REPORT3 §4(b) R1/R2: two regimes ((a) pre-mixing, (c) generic); mechanism (b) proposed and withdrawn. REPORT2 §H aligned with C4 (every NSW-prime m with h > 28m; the 11 listed m have certified prime h_m; nontrivial from m = 29). Conjecture R evidence: ≤ 0.05 at m = 9 (−0.05 at η = 400).
- §1.3: libm ≤ 4 ulp hypothesis stated; G1 (proved tilted truncation tail, replacing tl·1e40) and G2 (padding + exact edge spill) fixed in code/certify_v2.py; full 93-interval rerun above.
- §1.5: non-claim that the certified decay bound bites only for m ≥ m⁺(η) (10²–10⁵) and says nothing at m ≤ 13.
- §1.6: precise citations with hypothesis matching for (I1)–(I3); the referee's simpler last step (continuous coboundary ⇒ zero periodic-orbit sums ⇒ X ≡ 0, contradicting Prop L); status conditional on (I1)–(I3) (also §0 item 3).
- Lean: m3_obstruction replaced by the explicit relation m3_relation (7e₀ = H₃(1,0,0) + 𝟙), rebuilt (logs/lean_phase4_build.log, logs/lean_phase4_axioms.log).
- Integration packet: /workspace/lineB_packet.tgz (provisional IDs BGS-TRACE-163 to 182; status table of audit §8.10).
