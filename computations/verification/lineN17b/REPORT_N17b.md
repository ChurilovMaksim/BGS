# REPORT_N17b — H7 (levels other than h_p), the → ∞ step, and v2 fixes (N13b, N14b)

*Line N17b, 2026-11-01 (Asia/Yekaterinburg, UTC+5). Nothing pushed. N14/N14b/N13b files are not edited; corrections are stated here.*
Labels: [P] proved/elementary; [P-sketch]; [CA] interval; [CA-fp]; [N] float without error control; [H] heuristic.

## 0. Summary
1. **H7 is not trivial [P].**
   - W′_m is a plain linear sum (no max, no indicator except the inclusion test).
   - By TRACE-213, W′ = φ⁻¹Σ_NR(|Z|²−RMT) + φ⁻¹Σ_{ρ,d incl} Dev_d(ρ).
   - Each Dev_d has no sign; its only a-priori floor is −n_d|Z_ρ|²/d².
   - The inclusion threshold does not help. For ρ = (±2,8), **every** level d ≤ √h is included for all odd m ≥ 15 (m₀ = 15, [P given TRACE-199]).
   - Excluded (±2,16) levels only move members into the non-resonant part, which is ≥ −RMT ≥ −4m in total (harmless).
   - So levels d ≠ h_p **can** cancel the h_p gain. A negative Dev at d ≠ h_p is observed at m = 15 and 21.
2. **The step to → ∞, re-derived [P-sketch, bookkeeping].**
   - R′ asserts W′ = o(m). It suffices to show W′_{3p}/m ≥ κ > 0 infinitely often; in fact we get → ∞.
   - Exponential growth of the gas factor is **not** needed. Only a bracket that stays bounded below by a positive constant is needed, because the prefactor grows like 1.1329^m.
   - N10-F3's constant "0.2" for inherited levels is **not uniform in p**. Replace it by I_p ≤ σ(K_p)/K_p − 1 (Robin). With the gas bound alone (tails = 0, n = h_p), the bracket is positive from p ≥ 1386, not from 1289 (G = 10.99 vs I-bound 12.85 at p = 1289).
3. **What H7 needs (quantified) [P-sketch].**
   - Floors suffice only for levels d ≥ L_fl ≈ τ(h_m)·h_p/(G − I_p).
   - Below L_fl a signed (Lin) bound is needed at rate T′ ≈ 1.428: E_β|Ẑ_cross| ≲ e^{o(p)}·|Z_ρ|/h_p.
   - Uncovered classes:
     - hp-div levels (proper divisors of composite h_p; subgroup type, akin to R-mix);
     - K_p levels (divisors of K_p = 4h_p²+3, ord λ = 3p; needs equidistribution ≈3× past separation);
     - mixed levels.
   - Covered: d = 7 (Line J rate 1.2837 < T′, as registered), the Weil range (TRACE-244/245, conditional on OP), inherited levels (floor with I_p), and d ≥ L_fl (floor).
   - **Correction to THEOREM_DRAFT v1:** prime h_p does **not** remove H7. The K_p levels remain.
4. **Numerics (p = 3, 5, 7, 11, 13) [N].**
   - Non-h_p Dev values are tiny relative to their own main terms: |rel| ≤ 6.4e-3 at m = 21, ≤ 1.6e-5 at m = 33, ≤ 1e-6 at m = 39, and decreasing.
   - Their sum stays well below the h_p-level Dev where both are computed: m = 21, Σ_{d≠h_p} = +0.0043 / −0.0114 vs Dev_{239} = +0.214 / +0.211 (W′/m units).
   - Signs are mixed; negatives occur at K, hp-div and mixed levels.
   - Floors, by contrast, are O(1)–O(10³) times the actual values. So the data support H7, but its proof needs genuine cancellation (Lin) bounds.
5. **Units slip (N14 §3)** recorded in THEOREM_DRAFT_v2 (H8 row). **v2 fixes** for N13b/N14b per the lineN14 referee: §5 and §6 below.
6. **p = 17, q = 103 exact mixed run:** queued at nice 19 after the level runs (§7). It is running; no result yet.
7. **§2b** answers directly: per-level negative deviations are **not** bounded by an absolute constant a priori. Gas beats Robin (inherited levels) from p ≥ 1386 under stated hypotheses, but not a τ(h_m) bound.

## 1. W′ from the frozen definition (TRACE-206) [P]
- **Frozen definition.** For k1, η = 2, odd m, h = h_m, φ = φ(2h):
  - P* = {(±2,8), (±2,16)};
  - levels d | h with 1 < d ≤ √h;
  - members M_d(ρ) = {ν unit : bν ≡ a (2h/d), not (2h/d′) for d′ | d, d′ < d}, n_d = |M_d|;
  - level included iff |Z_ρ|²/d² ≥ 4m;
  - Res = φ⁻¹Σ_ρ[(|Z_ρ|² − RMT) + Σ_{d incl} n_d(|Z_ρ|²/d² − RMT)];
  - W′ = F − RMT − Res.
- **Rewriting.** F − RMT = φ⁻¹Σ_{ν unit}(|Z_ν|² − RMT). Splitting units into ρ-points, included members and the rest gives exactly the TRACE-213 identity:

  W′ = φ⁻¹Σ_{ν∈NR}(|Z_ν|² − RMT) + φ⁻¹Σ_ρΣ_{d incl} Dev_d(ρ),  Dev_d(ρ) = Σ_{ν∈M_d(ρ)}(|Z_ν|² − |Z_ρ|²/d²).

  Reproduced numerically to ≤ 5e-15 at m = 9…17 (b_exact_dev.py, exact tables).
- **Sign facts.**
  - (i) NR term ≥ −RMT·|NR|/φ ≥ −RMT ≥ −4m.
  - (ii) Dev_d ≥ −n_d|Z_ρ|²/d² (floor), and nothing better a priori. Dev_d < 0 occurs (m = 9 (−2,8) d = 7; m = 15 (−2,8) d = 31; m = 21 (±2,8) d = 7; m = 33 several, §4).
  - (iii) N6 positivity lemma: Dev_d ≥ Lin_d = (2/d²)Re(Z̄_ρ Σ_{β≠0} κ_d(Nβ)Ẑ(β)). The quadratic part is ≥ 0; only the linear cross term can be negative.
  - So W′ is **not** a max or an indicator. Each included level adds a signed amount whose negative part is controlled only by |Lin_d|.
- **Inclusion threshold.**
  - TRACE-199 gives |Z_ρ| ≥ ½(1 − λ^{−m})(1.9154712^m − 3012.3) for ρ = (±2,8).
  - Hence |Z_ρ|²/d² ≥ |Z_ρ|²/h ≥ 4m for every d ≤ √h once m ≥ 15. Checked exactly for odd 15 ≤ m ≤ 199 (g_threshold.py). For larger m the ratio grows like (1.9155²/ε)^m/m = 1.52^m/m.
  - So the threshold excludes **no** level for (±2,8) [P given TRACE-199].
  - For (±2,16), excluded levels contribute members to NR only (fact (i)). Included (±2,16) levels are handled by N7 §1 ([CA]+[P], p ≥ 339).

## 2. The step from the level-h_p inequality to W′_{3p}/m → ∞ [P-sketch]
- **Setup.** Fix p with m = 3p, and write S_ρ := φ⁻¹|Z_ρ|²/h_p.
- **h_p level** (N6 §0.8 / N11b §1): φ⁻¹Dev_{h_p}(ρ) ≥ S_ρ·(n/h_p)·G_ρ, where G_ρ = |1+X+Y|² − 1 and n = n_{h_p} (n = h_p − 1 for prime h_p).
- **Other levels** d ≠ h_p, ρ = (±2,8). Split them as:
  - **(a) inherited, d = e·h_p, e | K_p, e > 1:** floor n_d|Z|²/d² ≤ |Z|²/d, so φ⁻¹Σ ≥ −S_ρ·Σ_{e|K_p, e>1} 1/e ≥ −S_ρ·I_p, with I_p := σ(K_p)/K_p − 1 ≤ e^γ log log K_p + 0.6483/log log K_p − 1 (Robin 1984, n ≥ 3). Since log K_p ≈ 1.763p, I_p ≤ e^γ ln(1.763p) + o(1). This grows slowly; N10-F3's "0.2" is not uniform in p.
  - **(b) d ≥ L:** floor gives ≥ −S_ρ·h_p·τ(h_m)/L =: −S_ρ ε_fl(L).
  - **(c) d < L, d ∉ (a):** need |φ⁻¹Lin_d| ≤ S_ρ ε_d with Σ_d ε_d =: ε_other ≤ κ₀ (H7*).
- **(±2,16):** N7 §1 plus the TRACE-199-type bound for |Z_{(±2,16)}| ≤ C₁₆·1.6355^m give a total ≤ S_ρ·ε_16 with ε_16 ≲ C₁₆²(ε^{1/3}(1.6355/1.9154712)²)^m ≈ C·0.978^m. This is negligible for p ≳ 415 (constant from N7; [P-sketch]).
- **Result:**

  W′/m ≥ −4 + m⁻¹Σ_{ρ=(±2,8)} S_ρ·[(n/h_p)G_ρ − I_p − ε_16 − ε_fl − ε_other].

- **Scale.** φ ≍ h_m ≍ ε^m and h_p ≍ ε^{m/3}, so S_ρ ≥ c·(μ²/(ε·ε^{1/3}))^m = c·(3.66903/(2.41421·1.34148))^m = c·1.1329^m. Hence W′/m → ∞ as soon as the bracket is ≥ κ > 0 along the subsequence. **Gas growth beyond a constant is not needed.**
- **Bracket with the gas bound.** Take G ≥ (2(1+a)^p − 1)² − 1 with a = Re Λ_lo′ − δ_int = 6.2289e-4 (tails, Y, n/h_p − 1 ignored). Then G − I_bound > 0 first at p = 1386 (e_crossover.py; p = 1289: 10.99 vs 12.85; p = 1500: 15.72 vs 13.12).
  - With tails/Y/ε_16 the threshold moves up (≈1500 with the v1 budgets).
  - **Consequence:** the threshold p ≥ 1289 in v1 must become p ≥ max(p₁, p₀), with p₁ ≈ 1386–1500 [P-arith for the idealized number].
- **ε_fl and L.** Need τ(h_m)h_p/L ≤ (G − I_p)/4, i.e. L_fl ≈ 4τ(h_m)h_p/(G − I_p) = h_p^{1+o(1)}. Levels with d ≤ L_fl and d ∉ (a) are precisely what H7 must control.

## 2b. What bounds the other-level deviations? (answer to the explicit question)
Units: S_ρ = φ⁻¹|Z_ρ|²/h_p (the h_p-gain scale). The h_p level contributes ≥ S_ρ·(n/h_p)G.
- **Q1. Is the negative deviation per level bounded by an absolute constant (times S_ρ), so that the total is ≤ C·τ(h_m)·S_ρ?**
  - **No, not from anything proved.** The only a-priori bound is the floor φ⁻¹Dev_d ≥ −φ⁻¹n_d|Z_ρ|²/d² ≥ −(h_p/d)·S_ρ [P] (n_d ≤ d).
  - This is ≤ C·S_ρ only for d ≥ h_p/C. For small d it is h_p/d ≫ 1 (d = 7: h_p/7).
  - So "absolute constant per level" holds [P] exactly for levels d ≥ h_p/C, and fails a priori for d < h_p/C.
  - For those small levels a constant-per-level bound **is** H7* (signed Lin control at rate < T′ = 1.4279). It is OPEN except d = 7 (Line J) and the Weil range (conditional on OP).
  - Numerically [N] (§4), the worst negative non-h_p value in S units is
    - m = 15: −0.0034 (for (±2,8));
    - m = 21: −0.017;
    - m = 33: −3.2e-4;
    - m = 39: −4.9e-3, always d = 7.
    
    The h_p gain is +0.13…0.28 S at m = 15, 21. So per-level values are far below any constant, but this is not a bound.
- **Q2. Does the gas growth beat the divisor-type bound from p ≥ 1386?**
  - **Inherited levels (d = e·h_p, e | K_p) — yes, with hypotheses.** Their floors sum to ≤ I_p·S_ρ, I_p ≤ σ(K_p)/K_p − 1 ≤ e^γ ln ln K_p + 0.6483/ln ln K_p − 1 (Robin 1984, unconditional for K_p ≥ 3) [P].
    - G(p) := (2(1+a)^p − 1)² − 1 with a = Re Λ_lo′ − δ_int = 6.2289e-4 exceeds this bound for all p ≥ 1386 (e_crossover.py checks p ≤ 3000; for p > 3000 G grows exponentially while the bound grows like e^γ ln p) [P-arith, float evaluation].
    - **Hypotheses for this comparison:**
      - (i) the gas lower bound |1+X| ≥ 2(1+a)^p − 1 at p, i.e. H1–H4 with tails, Y and e^{−0.28p} set to 0;
      - (ii) n/h_p = 1 (prime h_p; for composite h_p multiply G by n/h_p = ∏(1−2/q));
      - (iii) ε_16 = ε_fl = ε_other = 0.
      
      With the v1 tail budgets the threshold moves to ≈1500.
  - **All other levels: a τ(h_m)-type bound is NOT beaten.** The floor route gives Σ_{d≥L, non-inh} h_p/d ≤ τ(h_m)·h_p/L.
    - Unconditionally τ(h_m) ≤ 2^{1.5379 ln h_m/ln ln h_m} (Nicolas–Robin 1983). With ln h_m ≈ 2.64p this is e^{Θ(p/log p)}, which dwarfs G = e^{O(10⁻³p)} for every relevant p (at p = 1386: exponent ≈ 476 vs ln G ≈ 2.6).
    - So the gas factor can absorb floors only for d ≥ L_fl ≈ 4τ(h_m)h_p/(G − I_p).
    - With the typical τ(h_m) = p^{O(1)} [H, not provable for this sequence], L_fl = h_p·p^{O(1)}; unconditionally L_fl may exceed √h_m, and then floors absorb nothing.
  - **Net:** the gas growth beats the Robin bound for inherited levels (p ≥ 1386, hypotheses (i)–(iii)). It does not replace H7* for the hp-div, K_p and mixed levels below L_fl.

## 3. What H7 needs, by class (m = 3p; h_m = h_p·K_p, K_p = 4h_p² + 3, 7 | K_p, gcd(h_p, K_p) | 3) [P-sketch]
- **Requirement (H7*).** For each level d < L_fl, d ∉ inherited:

  |Lin_d| ≤ (2/d²)|Z_ρ|·|Σ_{β≠0}κ_d(Nβ)Ẑ(β)| ≤ ε_d·|Z_ρ|²/h_p, with Σ ε_d ≤ κ₀.

  Since Σ_β|κ_d| ≲ d²·(avg), it suffices that E_{β mod d}|r_d(β)| ≲ e^{o(p)}·d^{O(1)}/(τ h_p) relative to |Z_ρ|, i.e. cross-correlation growth below T′ = μ/ε^{1/3} = 1.9154712/1.34148 = 1.4279 per m-step. The trivial sup bound gives 1.026× per step too much (Λ_free/μ* = 1.026), so H7* is beyond trivial bounds.
- **Classes:**

  | class | which d | status |
  |---|---|---|
  | d = 7 | 7 \| K_p always | covered as used in N6 §5/N8b §8: Line J rate \|μ_{1:3}\| ≤ 1.2837144 [CA] < T′. Caveat (TRACE-215/217): Line I left the (±2,16) level-7 members and the cross part open, and its operator-radius route fails (r_tw > 1.262). Our (±2,16) handling is N7 §1; the cross-rate input is Line J's |
  | Weil range | prime d with d ≤ q^{small} per Theorem W/W⁺ | covered conditional on OP (TRACE-244/245, as registered) |
  | inherited e·h_p | e \| K_p | floor with I_p (§2a) [P] |
  | d ≥ L_fl | any | floor [P] |
  | **hp-div** | d \| h_p, 1 < d < h_p (composite h_p only) | **OPEN.** Points ν_ρ + 2hj/d form subgroups (1/d)O/O of index (h_p/d)² in G_p; same nature as (R-mix), and no known theorem covers them (N15b) |
  | **K_p levels** | d \| K_p, d ≠ 7 (or 7·…) | **OPEN.** ord_d λ = 3p (except q = 7, ord 3); separation time 2log_λ d ≤ p ≪ 3p, so equidistribution well beyond Ehrenfest is needed |
  | **mixed** | d = d₁d₂, d₁ \| h_p, d₂ \| K_p, not inherited | **OPEN** (combination of the two) |

- **Prime h_p** removes hp-div and mixed levels but **not K_p levels**. So the v1 "subsequence version" needs H7 restricted to K_p levels.
  - Requiring K_p/7 to have no divisor in (7, L_fl) would remove them. Since K_p ≈ h_p^2 and L_fl = h_p^{1+o(1)}, [H] such p should be very rare, and nothing is provable either way at present.

## 4. Numerical data (exact tables m ≤ 17; TRACE-212 I2′ member formula for m = 21, 33, 39) [N]
- **Methods.**
  - **Exact:** b_exact_dev.py (Line E/G tables via audit/pr60 lineI loaders; decomposition error ≤ 5e-15).
  - **I2′:** d_g3dev.py: |Z(ν_ρ + 2hj/d)|² = |Σ_u e(t̄u/d)A_u|²/d², A_u = Σ_{Nβ≡u}Ẑ(β), with Ẑ from the TW law (L = 8, K = 16). It matches exact at m = 15 to 4–5 digits. Floats are not error-controlled.
- **Levels** (a_levels.py; all included):
  - p = 5: 7, 31, 217 (K), 41 (hp), 287 (inh); h_15 = 7·31²·41 is **not squarefree**.
  - p = 7: 7, 49, 4663 (K), 239 (hp), 1673 (inh).
  - p = 11: 7 (K), 23, 353 (hp-div), 161, 2471 (mixed), 8119 (hp), 56833 (inh), plus …
  - p = 13: 7, 313, 2191, 4088137 (K), 79, 599 (hp-div), six mixed, 47321 (hp), 2 inh.
- **Table** (Dev/(φm), W′/m units; "rel" = Dev/main of that level):
| m | ρ | d | class | Dev/(φm) | Dev/main | Dev/(S_ρ/m) |
|---|---|---|---|---|---|---|
| 15 | (-2,8) | 7 | K | +3.991e-02 | +1.8e-02 | +7.45e-02 |
| 15 | (-2,8) | 31 | K | -1.818e-03 | -2.7e-03 | -3.40e-03 |
| 15 | (-2,8) | 41 | hp | +7.108e-02 | +1.4e-01 | +1.33e-01 |
| 15 | (-2,8) | 217 | K | +2.450e-03 | +3.5e-02 | +4.58e-03 |
| 15 | (-2,8) | 287 | inherited | +1.484e-02 | +2.9e-01 | +2.77e-02 |
| 15 | (-2,16) | 7 | K | +2.408e-04 | +1.8e-02 | +7.46e-02 |
| 15 | (-2,16) | 31 | K | +4.724e-04 | +1.1e-01 | +1.46e-01 |
| 15 | (-2,16) | 41 | hp | +4.776e-03 | +1.6e+00 | +1.48e+00 |
| 15 | (2,8) | 7 | K | +1.197e-03 | +5.3e-04 | +2.24e-03 |
| 15 | (2,8) | 31 | K | +6.316e-04 | +9.2e-04 | +1.18e-03 |
| 15 | (2,8) | 41 | hp | +7.801e-02 | +1.5e-01 | +1.46e-01 |
| 15 | (2,8) | 217 | K | +1.754e-03 | +2.5e-02 | +3.28e-03 |
| 15 | (2,8) | 287 | inherited | +1.933e-02 | +3.7e-01 | +3.61e-02 |
| 15 | (2,16) | 7 | K | -2.222e-04 | -1.6e-02 | -6.89e-02 |
| 15 | (2,16) | 31 | K | +3.461e-04 | +8.4e-02 | +1.07e-01 |
| 15 | (2,16) | 41 | hp | +6.699e-03 | +2.2e+00 | +2.08e+00 |
| 21 | (-2,8) | 7 | K | -1.271e-02 | -5.7e-04 | -1.66e-02 |
| 21 | (-2,8) | 49 | K | +1.335e-03 | +5.0e-04 | +1.74e-03 |
| 21 | (-2,8) | 239 | hp | +2.108e-01 | +2.8e-01 | +2.75e-01 |
| 21 | (2,8) | 7 | K | -1.286e-02 | -5.7e-04 | -1.68e-02 |
| 21 | (2,8) | 49 | K | +1.712e-02 | +6.4e-03 | +2.23e-02 |
| 21 | (2,8) | 239 | hp | +2.136e-01 | +2.8e-01 | +2.79e-01 |
| 33 | (-2,8) | 7 | K | -7.184e-04 | -3.8e-07 | -3.16e-04 |
| 33 | (-2,8) | 23 | hp-div | +5.606e-05 | +7.6e-08 | +2.46e-05 |
| 33 | (-2,8) | 161 | mixed | -2.199e-05 | -2.9e-07 | -9.66e-06 |
| 33 | (-2,8) | 353 | hp-div | -4.853e-04 | -9.3e-06 | -2.13e-04 |
| 33 | (2,8) | 7 | K | +9.418e-03 | +5.0e-06 | +4.14e-03 |
| 33 | (2,8) | 23 | hp-div | -5.796e-05 | -7.9e-08 | -2.55e-05 |
| 33 | (2,8) | 161 | mixed | +3.660e-04 | +4.9e-06 | +1.61e-04 |
| 33 | (2,8) | 353 | hp-div | +8.230e-04 | +1.6e-05 | +3.62e-04 |
| 39 | (-2,8) | 7 | K | -8.456e-03 | -4.4e-07 | -2.14e-03 |
| 39 | (-2,8) | 79 | hp-div | +1.623e-05 | +7.0e-09 | +4.11e-06 |
| 39 | (-2,8) | 313 | K | +3.477e-08 | +5.9e-11 | +8.80e-09 |
| 39 | (-2,8) | 553 | mixed | -1.021e-04 | -4.3e-07 | -2.58e-05 |
| 39 | (-2,8) | 599 | hp-div | +1.396e-04 | +4.5e-07 | +3.53e-05 |
| 39 | (2,8) | 7 | K | -1.930e-02 | -1.0e-06 | -4.89e-03 |
| 39 | (2,8) | 79 | hp-div | +4.582e-05 | +2.0e-08 | +1.16e-05 |
| 39 | (2,8) | 313 | K | -8.993e-08 | -1.5e-10 | -2.28e-08 |
| 39 | (2,8) | 553 | mixed | -2.328e-04 | -9.9e-07 | -5.89e-05 |
| 39 | (2,8) | 599 | hp-div | +1.495e-04 | +4.8e-07 | +3.78e-05 |

(Rows with |rel| ≲ 1e-8 at m = 39 are below the method's resolution: I2′ matches exact at m = 15 to 4–5 digits, so they are noise-level [N]. (±2,16) levels at m ≥ 21 not computed: DMAX/exclusion, N7 covers them.)
- **Reading.**
  - Non-h_p levels have mixed signs. Relative to their own main terms they shrink fast with m: max |rel| 0.37 (m = 15), 6.4e-3 (21), ≲1.6e-5 (33), ≲1e-6 (39). In S_ρ units the worst negative non-h_p value is d = 7 at every m (§2b).
  - Where the h_p level was computed (m = 15, 21), Σ_{d≠h_p} Dev is ≤ 26% (m = 15, positive) and ≤ 5.4% in absolute value (m = 21) of Dev_{h_p}.
  - At m = 33, 39 the h_p level (8119, 47321) and large levels are out of reach of this method; the comparison uses the scale S_ρ/m.
- **Floors** are far from the truth (e.g. m = 15, d = 7: floor −2.24 vs Dev +1.2e-3). This confirms §3: H7 is a cancellation statement, not a positivity one.
- **Not computed:** levels > DMAX (m = 21: 1673, 4663; m = 33: 2471, 8119, 56833, …; m = 39: d > 650). These are [N]-unknown here.

## 5. REPORT_N13b — v2 fixes (lineN14 referee) [stated here; N13b files unchanged]
- **(a) Point count.** The number of mixed points at level d is 2^{ω(d)}·h²/d (not h²/d). Where N13b used h²/d, multiply by 2^{ω(d)} = d^{o(1)}. This does not change any exponent.
- **(b) S at composite h, defined explicitly.** S := CRT product of the prime-level sets S_q over q | h_p.
  - At h = 8119 = 23·353 this gives n = |S| = 7371 = (23−2)(353−2). The N6 rule applied directly at composite h yields unit part 7743 = φ(h) − 1.
  - **Reconciliation [P, checked].** 7743 − 7371 = 372 = (23−2) + (353−2) = n_23 + n_353. These are exactly the units ≡ ν_ρ modulo one prime factor but not the other, i.e. the members of the hp-div levels d = 23, 353 in TRACE-206's bookkeeping (n_23 = 21 confirmed in b_exact_dev m = 11).
  - So S (CRT) is the correct h_p-level set, and the 372 points belong to H7 (hp-div class), not to the h_p level.
- **(c)** μ*³/λ = **1.2058** (N13b printed 1.2061).
- **(d)** "decay e^{−0.8p}" softened to "numerics are consistent with decay at rate ≈ e^{−0.8p} over the tested range [N]".
- **(e)** p = 3 is excluded by range (h_3 = 7 prime; statements are for p ≥ 5).
- **Referee confirmations** recorded in v2: NSW primes h_p for prime p ≤ 300 are p ∈ {5, 7, 19, 29, 47, 59, 163, 257}; the p = 31 entry is confirmed.

## 6. REPORT_N14b — v2 fixes [N14b files unchanged]
- **Lemma 1** (sublattice separation), now [P] with:
  - (i) separation stated **per component**: the admissible set is a union of 2^{ω(d)} sublattices, and separation holds within each; the count gets the factor 2^{ω(d)} = d^{o(1)};
  - (ii) an explicit factor 8 from lifting through the inverse different (index of O^∨ ⊃ O, disc 8);
  - (iii) the Bowen count uses a partition into sub-boxes of side < separation, each containing ≤ 1 point per component.
- **Constant typo.** In a_cvalues.py the TRACE-199 constant μ = 1.9154732 → **1.9154712**. The relative change in ln μ is ≈1.6e-6, so c-values move in the 6th digit. Not re-run; the printed values carry this note.

## 7. p = 17, q = 103 exact mixed run
- CPU was free after (1)–(2): the d_g3dev chain finished at ≈03:06; a_cert3.py of another line uses 1 of 4 cores.
- **Queued and running:** `nice -n 19 a_mixed_majorant.py 17 103 exact`.
  - Script: a copy of N16b/code/a_mixed_majorant.py at N17b/code.
  - cwd: N17b/post_manifest; started 2026-11-01 03:06:43 +0500; ≈2.5e10 points, est. ≈2 h.
- Output goes to N17b/post_manifest/logs/ (p17_q103.out, a_mixed_p17_q103_exact.json). It is **deliberately outside the manifest** (still running at hashing time). No result is claimed here.
