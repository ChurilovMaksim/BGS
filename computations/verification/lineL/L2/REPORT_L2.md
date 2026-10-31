# Line L2 report: the open range c_W p² < q < L_m through the cat-map structure

31 Oct 2026. Labels: [P] proved here, [CA] computer-assisted (arb), [N] floating-point numerics, [H] heuristic,
[assessment] opinion on strategy. Standing inputs as in REPORT_L_v2 (Line F/J trace representation TRACE-197, J3, L16, S_Z).
REPORT_L.md / REPORT_L_v2.md are not edited here.

**Errata (referee L2-F1–F4 and the Prop S block count; applied at integration, 31 Oct 2026): see §7. Where §7 and the
text above differ, §7 governs.** The author's file before this change is `../pre_polish/L2/REPORT_L2.md`.

## 0. Summary

1. **What has to be bounded [P].** At an open prime level q ∥ h_m, the level contributes 2Re(conj Z_ρ·(D_iso − E_b/q))
   (Theorem K1, REPORT_v2). Since |Z_ρ| ≤ C_ρμ^m, the open range closes iff |D_iso − E_b/q| ≤ ((1−δ)·1.28359)^m
   for (±2,8) (resp. 1.4742 for (±2,16)), up to e^{o(m)} level counts. These are **averages** over β of Ẑ_β
   (weights 1/q on the two isotropic lines, ~1/q² elsewhere), **not** per-β bounds.
2. **K2′ is too weak to refute anything [P, given standing inputs].** Slow β exist unconditionally at every open prime
   q ∥ h_m with log_λ q ≥ C_k + 6.1·10⁻⁶·m (Prop S, §1; C_k exists but is not computed). So "frozen R′ ⇒ some open conductor has a slow β" (Theorem K2′)
   gives no contradiction for such m. The correct target is the mean statement H_mean (§1).
3. **(a) Cancellation-free collision counting: barrier [P].** What is proved is a lower bound on what any phase-blind
   collision bound can output. It is not a statement about D itself.
   - Exact reduction [P]: |D_𝔮|² ≤ (1 − 1/q)·C_𝔮, with C_𝔮 = Σ_{u∈O/𝔮}|A(u+𝔮)|² − |Z|²/q = (1/q)Σ_{β∈ℓ(𝔮)∖0}|Ẑ_β|².
   - Barrier [P]: every cancellation-free (phase-blind) collision bound is ≥ G^{2m}/q, G = Σ|J_n(1.8)| = 2.3693986 [CA].
     It gives |D| ≤ target^m only for q ≥ 3.4074^m (±2,8) or 2.5832^m (±2,16). Both are above √h ≈ 2.4142^m, so the method
     fails at **every** included level, not only in the open range.
   - [assessment] The open range must therefore be done **with the signs** of the TRACE-206 phases.
4. **(b) Height/norm argument: its validity zone is disjoint from the open range [P].**
   - Lemma B1 [P]: a sporadic folded collision F (F(λ) ∈ 𝔮∖0, length r) has ‖F‖_∞² ≥ q/(1.457·λ^{r−1}).
   - Lemma B2 [P]: conversely, nonzero F with F(ℓ) ≡ 0 and ‖F‖_∞ ≤ q^{1/r} always exist (Minkowski). For q < L_m, r ≥ p,
     that means ‖F‖_∞ ≤ 3.33^{1+η}.
   - Hence the height argument removes sporadic collisions only for q ≳ λ^{r} ≥ λ^{m/3} = 1.7996^m.
     - (±2,8): L_m = 1.4923^{m(1+η_m)} < 1.7996^m once η_m < 0.4678. That holds for all large p, since
       η_m ≤ (2.010+o(1))/log(2p+1).
     - (±2,16): 1.1311^{m(1+η)} < 1.7996^m for every p, since η^{(16)} ≤ (4.282+o(1))/log(2p+1) < 3.77.
   - So, as proved: the height lemma B1 excludes sporadic collisions only for q above λ^{r−1}·1.457·H², and that zone does
     not meet (c_W p², L_m) for large p. Within the open range, sporadic collisions of height ≤ 4 always exist (B2).
     It therefore closes neither (±2,16) nor any part of (±2,8).
   - [assessment] Refinements that keep the cancellation-free form are blocked by Prop A2 anyway.
5. **(c) Numerics [N]: equidistribution holds at every level tested, with margin.**
   - 23 (level, resonance) cases on isotropic lines (m = 15…183, q = 23…19609) and 6 full levels (m ≤ 51, q ≤ 239).
   - Worst isotropic |D_𝔮|^{1/m} = 1.120. Worst full K1 combination max_t|D_iso − E_b(t)/q|^{1/m} = 1.178, at (21,239).
     The target is 1.28359; the absolute margin there is 31 vs 189. Typical full-rank isotropic levels: 0.82–0.87.
   - Only (2,8) and (−2,8) were run; the (±2,16) resonances were **not** tested.
   - The worst cases are the **inherited levels** q | h_p (rank r = p = m/3), as the slow-orbit model predicts.
   - Individual |Ẑ_β| do exceed the target. Examples: non-isotropic max rate 1.56 at (21,239) and 1.44 at (15,41);
     isotropic max 1.278 at (21,239). This is consistent with point 2: only averages can work.
6. **New precise obstruction [assessment].** The open range is equivalent to a **signed sporadic-collision bound**,
   Σ_{v: α_v∈𝔮∖0} R(v) = |Z|²/q + O(((1−δ)·target)^{2m}), with R(v) the TRACE-206 autocorrelation of Theorem U.
   This bound is enough for D_𝔮; the E_b and qO parts need analogous signed sums. Exact collisions contribute 0
   (Theorem U), and no positivity is available. I see no proof.

## 1. Target, and why per-β statements (K2′) cannot close the range

**Decomposition [P].** Write ℓ(𝔞) ⊂ O/q for the annihilator of the ideal 𝔞 ⊇ qO under (β,x) ↦ e(Tr(βx)/q); ℓ(𝔮) and
ℓ(𝔮̄) are the two isotropic lines. Then:
- A(𝔞) = (1/[O:𝔞])Σ_{β∈ℓ(𝔞)}Ẑ_β (orthogonality).
- D_𝔮 := A(𝔮) − A_tot/q = (1/q)Σ_{β∈ℓ(𝔮)∖0}Ẑ_β.
- D_iso = D_𝔮 + D_𝔮̄ − (A(qO) − A_tot/q²), because 𝔮∩𝔮̄ = qO and (2q−1)/q² = 2/q − 1/q².
- A(qO) − A_tot/q² = (1/q²)Σ_{β≠0}Ẑ_β.

**H_mean (sufficient, [P] that it suffices, by Theorem K1 + Prop K2 + Theorem W).** For some δ > 0 and infinitely many
m ∈ S⁺: |D_iso(q) − E_b(q)/q| ≤ ((1−δ)·target)^m at every open prime level q, together with the analogue at open
composite levels. Then the open part of O♮ is o(ξ_lo^m), and frozen R′ is refuted (Theorem K, REPORT_v2).

**Proposition S (slow β exist) [P, given Line F: some (±2,8) family F has untwisted spectral radius ρ₀ ≥ μ* = 1.9155].**
Fix the family F and k = k_F from REPORT_L_v2. There is C_k such that, for every prime q ∥ h_m with log_λ q ≥ C_k + r·(T/ρ₀)^{2k}
(T = (1−δ/2)·1.28359), β = 1 is slow at q: (1/r)Σ_{i<r}f_k^F(λ^i/q) > T^{2k}.

*Proof.*
1. f_k^F(y) = ‖L_{τ_{k−1}}⋯L_{τ_0}‖²_HS depends only on τ_j = Tr(λ^j y). It is ≥ 0 and continuous (absolutely
   convergent Fourier series). Also f_k(0) ≥ ‖L_0^k‖² ≥ ρ₀^{2k}. So f_k ≥ ρ₀^{2k}/2 on [0, ε_k]^k for some ε_k > 0.
2. For β = 1, τ_i = Tr(λ^i)/q, and 0 < Tr(λ^{±i}) ≤ 2λ^{|i|}. So τ_i ∈ [0, ε_k] for |i| ≤ I := ⌊log_λ(ε_k q/2)⌋.
   That gives 2I − k + 2 blocks lying entirely inside, and their f_k values are ≥ ρ₀^{2k}/2.
3. Hence the orbit average is ≥ (2I − k + 2)ρ₀^{2k}/(2r). This exceeds T^{2k} once I ≥ k/2 + r(T/ρ₀)^{2k}. ∎

With k = 15 and ρ₀ ≥ μ*: (1.28359/1.9155)^{30} ≤ 6.1·10⁻⁶, and r ≤ 3p = m. So the threshold is
log_λ q ≥ C_k + 6.1·10⁻⁶·m, far below log_λ L_m ≈ 0.227·m(1+η).

- **Consequence:** whenever h_m has a prime q ∥ h_m in (max(c_W p², λ^{C_k + 6.1·10⁻⁶ m}), L_m), the conclusion of K2′
  holds unconditionally, so K2′ yields no contradiction. C_k (through ε_k) is not computed, so which m qualify is not
  determined. [H] The factor data (K2 `n2_factor_h.log`) show open-range primes of size 10⁵–10²⁸ for most m = 3p tested, so
  this should cover most m.
- K2′ remains *true*, but it is not a refutation route. [assessment] The right target is H_mean.
- J3 had already seen slow β numerically: radius up to 1.83 at q ≈ 4.9·10¹⁷ | h_47.
- The weight 1/q (isotropic) or ~1/q² (non-isotropic) is what makes slow β harmless in H_mean [H, supported by §4].

## 2. (a) Collision counts mod 𝔮

**Lemma A1 (exact second moment) [P].** Σ_{β∈ℓ(𝔮)}|Ẑ_β|² = q·Σ_{u∈O/𝔮}|A(u+𝔮)|². Hence, by Cauchy–Schwarz over the
q−1 nonzero β,
|D_𝔮|² ≤ ((q−1)/q²)·Σ_{β∈ℓ(𝔮)∖0}|Ẑ_β|² = (1 − 1/q)·C_𝔮, with C_𝔮 := Σ_u|A(u+𝔮)|² − |Z|²/q ≥ 0.
In collision form, Σ_u|A(u+𝔮)|² = Σ_{v: α_v∈𝔮}R(v), with R(v) = Σ_n w(n)·conj w(n−v) as in Theorem U.
- Exact collisions α_v = 0, v ≠ 0 contribute **0** (Theorem U).
- v = 0 contributes Σ|w|² = 1.
- So C_𝔮 = 1 + Σ_{α_v∈𝔮∖0}R(v) − |Z|²/q exactly. Only *sporadic* collisions α_v ∈ 𝔮∖{0} remain.

**Proposition A2 (phase-blind barrier) [P].** Let M(u) := Σ_{n: α_n ≡ u (𝔮)}|w(n)|, so Σ_u M(u) = G^m. Any bound of
C_𝔮 + |Z|²/q by a sum of |w(n)||w(n′)| over the pairs colliding mod 𝔮 is ≥ Σ_u M(u)² ≥ G^{2m}/q (Cauchy–Schwarz).
The exact-collision part of this abs sum is ≤ C·r_abs^m = C·1.0511^m [N; the automaton of Line L].
So a phase-blind bound certifies |D_𝔮| ≤ T^m only if G^{2m}/q ≤ T^{2m}, i.e.:

| family | need q ≥ | compare √h | compare L_m |
|---|---|---|---|
| (±2,8), T = 1.28359 | (G/T)^{2m} = **3.4074^m** | 2.4142^m | 1.4923^{m(1+η)} |
| (±2,16), T = 1.4742 | (G/T)^{2m} = **2.5832^m** | 2.4142^m | 1.1311^{m(1+η)} |

The constants are arb-certified (`code/barrier_consts.py`, `logs/barrier_consts.log`). Both thresholds exceed √h_m,
which is the top of the included range. So cancellation-free collision counting gives **nothing** at any included level.

- The user's heuristic is right: the weighted word count G^m ≫ q forces Σ_u M(u)² ≥ G^{2m}/q, so the abs collision
  count is dominated by sporadic collisions.
- Note also that the main term |Z|²/q (|Z| = (½+o(1))μ*^m, Prop K2 Z-bound) exceeds T^{2m} for every q < ¼·(μ*/T)^{2m} = ¼·2.2269^m [CA]. Any usable bound must
  therefore reproduce |Z|²/q to relative accuracy T^{2m}q/|Z|². This is a signed statement.
- (OP_abs worked in Theorem W because there the cancellation came from Weil (W1); OP_abs only handled γ = 0.)

**Numerics on the barrier [N].** The phase-blind deviation itself, M(𝔮) − G^m/q = (1/q)Σ_{β∈ℓ∖0}Π_iφ₁(τ_i)
(φ₁(t) = Σ|J_a|e(at); the |w| weights factorise), is tiny: 10⁻⁸ to 10⁻¹²⁸ relative to G^m/q (table §4, last column).
So the *positive* mass equidistributes extremely well. That fact does not bound D_𝔮, though, because
|A(𝔮) − Z/q| is not controlled by |M(𝔮) − G^m/q| [P: the phases differ].

## 3. (b) Height / norm argument

Positions are cyclic: λ^m ≡ 1 (mod 2h_m), and Ẑ is invariant along λ-orbits [N-checked, §4]. Modulo 𝔮, λ has order
r ∈ {p, 3p}, and a word difference v folds to F_v(X) = Σ_{s<r}(Σ_{t: s+tr<m}v_{s+tr})X^s.

**Lemma B1 [P].** If F ∈ Z^r and F(λ) ∈ 𝔮∖{0}, then q ≤ |N(F(λ))| ≤ (λ/(λ−1))²·λ^{r−1}·‖F‖_∞² ≤ 1.457·λ^{r−1}·‖F‖_∞².
*Proof.* r is odd (r ∈ {p, 3p}); put c = (r−1)/2 and G = λ^{−c}F(λ) ∈ 𝔮∖{0}. In either real embedding
|σ(G)| ≤ ‖F‖_∞·Σ_{|j|≤c}λ^{j} ≤ ‖F‖_∞·λ^{c}·λ/(λ−1). So |N(G)| ≤ ‖F‖_∞²·λ^{r−1}·(λ/(λ−1))², and (λ/(λ−1))² = 1.4571.
N(G) = N(F(λ)) is a nonzero integer divisible by q, hence |N(G)| ≥ q. ∎

**Lemma B2 [P].** Λ_𝔮 = {F ∈ Z^r : F(ℓ) = 0 in F_q} has index q in Z^r. So it contains F ≠ 0 with ‖F‖_∞ ≤ q^{1/r}
(Minkowski, cube). For q < L_m and r ≥ p = m/3: q^{1/r} < (1.4923^{3})^{1+η} = 3.323^{1+η}.

**Lemma B3 (summing over all prime ideals above h) [P].** Let v ∈ Z^m with α_v = Σ_{i<m}v_iλ^i ≠ 0 and ‖v‖_∞ ≤ H.
Distinct prime ideals 𝔮 | h that contain α_v are pairwise coprime, so their product divides (α_v). Hence
Σ_{𝔮|h: α_v∈𝔮} log N𝔮 ≤ log|N(α_v)| ≤ log(1.457·λ^{m−1}·H²) (Lemma B1 with r = m). Summing with the abs weights gives
Σ_{𝔮|h} log N𝔮·(Coll^{abs}_𝔮 − exact part) ≤ Σ_v Π_jρ(v_j)·log(1.457λ^{m−1}max(1,‖v‖_∞)²) = (1+o(1))·m·log λ·G^{2m}.
- So each sporadic collision is "used" by prime ideals of total log-norm ≤ m·log λ + O(log H). This is the dual
  (large-sieve-type) form of the height argument.
- [assessment] It does not help. The per-ideal lower bound Coll^{abs}_𝔮 ≥ G^{2m}/q (Prop A2) is compatible with it,
  since Σ_𝔮 log q/q ≪ m. Averaging over ideals cannot push any single 𝔮 below G^{2m}/q, and that is already far above T^{2m}.

**Consequence [P].** Sporadic collisions of height ≤ 4 exist at every open level, and with r ≥ p the height argument
excludes them only for q > 1.457·λ^{p−1}·H². In growth terms that is λ^{m/3} = 1.7996^m.
- (±2,8): log L_m/m = 0.40030(1+η_m) < log 1.7996 = 0.58757 ⇔ η_m < 0.4678. This is true for all large p, since
  η_m ≤ (2.010+o(1))/log(2p+1) (Prop K2).
- (±2,16): 0.12319(1+η^{(16)}) < 0.58757 ⇔ η^{(16)} < 3.770. This is true for all p, since
  η^{(16)} ≤ (4.282+o(1))/log(2p+1) (REPORT_L_v2 §5b).
- For r = 3p the threshold is λ^m, which is worse.
- **So the height zone and the open range are disjoint [P]** (for (±2,8): for all p with η_m < 0.4678; for (±2,16): all p).
  The argument closes neither (±2,16) nor any part of (±2,8).
- [assessment] Superexponential Bessel decay does not rescue it: Lemma B2's sporadic vectors have height O(1).

## 4. (c) Numerics: actual levels of h_{3p}

**Method [N].**
- `code/twlaw.py` gives Ẑ_β exactly as TRACE-206 sums, via the Line G/I transfer law (MC Galerkin on H²(D_ρ) plus the
  P-mod-b automaton) with per-step twists e(n_iτ_i), τ_i = Tr(βλ^i)/q.
- Validated against brute force at m = 5: all digits agree, for both position orders.
- λ-orbit invariance checked at m = 15 (q = 31, 41).
- Truncation (L = 8, K = 32) is stable: L = 10, K = 40 gives identical values at (21,239).
- Precision: double vs long double rel. err ≤ 5·10⁻¹², and K = 32 vs 40 identical, at (57,457) (`logs/prec_chk_57_457.log`).
  At (183,367): rel. err ≤ 4.5·10⁻⁹ and K = 32 vs 40 identical (`logs/prec_chk_183_367.log`).
- Resonance ν₀: (2,8), i.e. 8ν₀ ≡ 2 (mod 2h), and (−2,8) where marked. The (±2,16) resonances were **not** run.

**Isotropic lines** (`code/iso_survey.py`, `logs/iso_survey.jsonl`). r = order of λ mod 𝔮. The two lines gave identical
|D| in every case (a conjugation symmetry [N]), so one is shown.

| res | m | q | log q / m | r | \|Z\|/q | 1.28359^m | \|D_𝔮\| | \|D_𝔮\|^{1/m} | msq^{1/2m} | max\|Ẑ\|^{1/m} | phase-blind D/(G^m/q) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| (-2,8) | 15 | 41 | 0.248 | 5 | 209 | 42.3 | 1.01 | 1.0007 | 1.0363 | 1.0773 | -2.0e-08 |
| (2,8) | 15 | 41 | 0.248 | 5 | 209 | 42.3 | 0.452 | 0.9485 | 1.0316 | 1.0729 | -2.0e-08 |
| (-2,8) | 21 | 239 | 0.261 | 7 | 1.77e+03 | 189 | 10.5 | 1.1186 | 1.1948 | 1.2780 | -5.5e-10 |
| (2,8) | 21 | 239 | 0.261 | 7 | 1.77e+03 | 189 | 10.8 | 1.1199 | 1.1948 | 1.2780 | -5.5e-10 |
| (2,8) | 21 | 4663 | 0.402 | 21 | 90.8 | 189 | 0.0292 | 0.8451 | 0.9390 | 1.0099 | 4.4e-09 |
| (2,8) | 33 | 23 | 0.095 | 11 | 4.49e+07 | 3.79e+03 | 0.00231 | 0.8320 | 0.8331 | 0.8331 | -1.2e-23 |
| (2,8) | 33 | 353 | 0.178 | 11 | 2.93e+06 | 3.79e+03 | 0.858 | 0.9954 | 1.0417 | 1.0863 | -2.5e-18 |
| (2,8) | 39 | 79 | 0.112 | 13 | 6.46e+08 | 1.69e+04 | 0.0383 | 0.9198 | 0.9364 | 0.9486 | -5.4e-21 |
| (2,8) | 39 | 313 | 0.147 | 39 | 1.63e+08 | 1.69e+04 | 0.00234 | 0.8562 | 0.8756 | 0.8907 | -5.0e-24 |
| (-2,8) | 39 | 599 | 0.164 | 13 | 8.52e+07 | 1.69e+04 | 0.256 | 0.9656 | 1.0026 | 1.0406 | 7.1e-19 |
| (2,8) | 39 | 599 | 0.164 | 13 | 8.52e+07 | 1.69e+04 | 0.229 | 0.9629 | 0.9985 | 1.0349 | 7.1e-19 |
| (2,8) | 51 | 103 | 0.091 | 17 | 1.21e+12 | 3.39e+05 | 0.0266 | 0.9313 | 0.9417 | 0.9519 | -1.2e-32 |
| (2,8) | 51 | 409 | 0.118 | 51 | 3.04e+11 | 3.39e+05 | 0.000333 | 0.8547 | 0.8649 | 0.8765 | -1.7e-30 |
| (2,8) | 51 | 15607 | 0.189 | 17 | 7.97e+09 | 3.39e+05 | 138 | 1.1014 | 1.1660 | 1.2375 | -2.2e-17 |
| (2,8) | 57 | 457 | 0.107 | 57 | 1.35e+13 | 1.51e+06 | 8.01e-05 | 0.8475 | 0.8574 | 0.8677 | -3.6e-35 |
| (2,8) | 57 | 14593 | 0.168 | 57 | 4.21e+11 | 1.51e+06 | 0.000193 | 0.8607 | 0.8979 | 0.9295 | 3.8e-32 |
| (2,8) | 87 | 13921 | 0.110 | 87 | 1.3e+20 | 2.71e+09 | 2.27e-06 | 0.8612 | 0.8917 | 0.9085 | 5.7e-53 |
| (2,8) | 111 | 6217 | 0.079 | 111 | 1.73e+27 | 1.08e+12 | 1.44e-07 | 0.8677 | 0.8808 | 0.8941 | 2.2e-67 |
| (2,8) | 123 | 2297 | 0.063 | 41 | 1.14e+31 | 2.17e+13 | 0.000821 | 0.9439 | 0.9571 | 0.9701 | -9.4e-65 |
| (2,8) | 123 | 9103 | 0.074 | 123 | 2.88e+30 | 2.17e+13 | 7.68e-09 | 0.8591 | 0.8713 | 0.8817 | -9.9e-77 |
| (2,8) | 129 | 19609 | 0.077 | 43 | 6.61e+31 | 9.71e+13 | 0.000514 | 0.9430 | 0.9629 | 0.9832 | 3.4e-65 |
| (2,8) | 183 | 367 | 0.032 | 183 | 6.18e+48 | 6.95e+19 | 4.83e-16 | 0.8247 | 0.8247 | 0.8247 | -4.9e-128 |
| (2,8) | 183 | 7687 | 0.049 | 183 | 2.95e+47 | 6.95e+19 | 1.24e-13 | 0.8501 | 0.8605 | 0.8665 | 4.0e-119 |

(m = 21 and 51 rows with r = 7, 17 are inherited levels q | h_p.) q ≤ 19609 only: larger q (37223, 54121 at m = 111, 123; 34129 at m = 237) were dropped for cost.

**Full levels** (`code/full_level.py`, `logs/full_level.jsonl`): all q² twisted sums, the push-forward A(c), D_iso and
E_b(t) for every t ∈ F_q* (so every possible missing label t_b).

| res | m | q | \|Z\| | 1.28359^m | \|D_iso\| | max_t\|E_b\|/q | max_t\|D_iso − E_b/q\| | rate^{1/m} | max non-iso \|Ẑ\|^{1/m} | Σ_c\|A(c)\|² − \|Z\|²/q² |
|---|---|---|---|---|---|---|---|---|---|---|
| (2,8) | 15 | 41 | 8.57e+03 | 42.3 | 3.04 | 2.95 | 5.56 | 1.1212 | 1.4414 | 517 |
| (2,8) | 33 | 23 | 1.03e+09 | 3.79e+03 | 1.74 | 3.23 | 4.43 | 1.0461 | 1.1270 | — (fp) |
| (2,8) | 39 | 79 | 5.1e+10 | 1.69e+04 | 5.32 | 9.78 | 14.5 | 1.0710 | 1.1898 | — (fp) |
| (2,8) | 51 | 103 | 1.24e+14 | 3.39e+05 | 41.7 | 48.6 | 86.9 | 1.0915 | 1.2052 | — (fp) |
| (-2,8) | 15 | 41 | 8.57e+03 | 42.3 | 3.13 | 2.85 | 5.96 | 1.1264 | 1.4415 | 516.3 |
| (2,8) | 21 | 239 | 4.23e+05 | 189 | 24.8 | 6.5 | 31 | 1.1777 | 1.5616 | 5.436e+04 |

"— (fp)": the difference is below double precision relative to |Z|²/q².

**Reading [N/H].**
- At every tested level, the K1 combination satisfies |D_iso − E_b/q|^{1/m} ≤ 1.178 < 1.28359 (full levels, m ≤ 51),
  and the isotropic parts of full-rank levels are at 0.82–0.87.
  - Caveat [assessment]: the full-level data stop at m ≤ 51 and include small q (23, 41, 79, 103), where the full K1 rate
    rises slowly with m (1.046 → 1.071 → 1.092 for m = 33, 39, 51). Extrapolating from these runs is not reliable.
  - For m ≥ 39 the margin to the target is ≥ 10⁴ in absolute size.
  - The rate does not approach the target as m grows [N].
- The largest values are at **inherited levels** q | h_p (r = p): 239 | h_7, 15607 | h_17, 353 | h_11.
  - **Slow-orbit model [H]:** for isotropic β ≈ (small)·generator, about log_λ q positions per period have τ ≈ 0, with
    factor ≈ μ* each; the rest decay at the generic rate ≈ 0.86 per step.
  - For q ≈ h_p ≈ λ^{p/2} this gives max|Ẑ| ≈ (μ*·0.86)^{m/2} ≈ 1.28^m (observed 1.278 at (21,239)). The weight 1/q ≈ λ^{−m/6}
    then gives |D| ≈ (1.28/1.342)^m ≈ 0.96^m, up to orbit counts.
  - So inherited levels are not expected to break H_mean [H].
- Individual non-isotropic |Ẑ_β| reach rate 1.44–1.56 > 1.28359 at (15,41) and (21,239). This confirms that per-β methods cannot work in the
  open range and that the 1/q² weighting is essential.

## 5. Remaining obstruction and possible routes [assessment]

1. **Precise form.** Prove, for open prime levels q ∥ h_m:
   Σ_{v: α_v∈𝔮∖0}R(v) − |Z|²/q = O(((1−δ)·T)^{2m}), plus the analogous signed sums for qO and for the E_b Gauss twist.
   Here R(v) = e(ν₀P(v)/2h)·Π_jκ(v_j, θ_j(v)), with θ_j(v) = ν₀y′Tr(λ^{−j}α_v)/(2h) (Lemma U1).
   - For α_v ∈ 𝔮∖0 the θ_j are equidistribution-type quantities at the *complementary* level h/q (aliasing).
   - The problem is therefore self-similar across the divisor lattice of h.
2. **Inherited levels (r = p) [H].** For q | h_p, positions fold three times. One might relate D^{(3p)}_𝔮 to the level-q
   data of the m = p sum, where q ≈ λ^{p/2} is a *large* level and Prop K2-type positivity is available. Not attempted;
   it would need a factorisation of e(−ν₀P(n)/2h_{3p}) mod q over the three blocks. I have not verified that.
3. **What does not work** (§2, §3, Line L): Weil (q ≤ c_W p²); BGK (q ≤ p^C, ineffective); large sieve (loses 1.88^m);
   cancellation-free collisions (lose (G/T)^{2m}/q); height/norm (zone disjoint from the open range); per-β bounds
   (slow β exist, Prop S).

## 6. Files (/workspace/bgs-lineL/L2)

- `code/twlaw.py` (twisted transfer + brute validation), `code/orbit_chk.py`, `code/timing.py`, `code/prec_chk.py`.
- `code/iso_survey.py`, `code/run_iso.sh`, `code/run_iso2.sh`, `code/mktable.py`.
- `code/full_level.py`, `code/run_full.sh`, `code/mkfull.py`.
- `code/barrier_consts.py`.
- `logs/iso_survey.jsonl`, `logs/full_level.jsonl`, `logs/table_iso.md`, `logs/table_full.md`, `logs/barrier_consts.log`, `logs/prec_chk_*.log`, `logs/iso_trunc_21_239_L10K40.json`.
- `NOTES_L2.md`, `REPORT_L2.md`.
- `SHA256_L2.txt` (manifest), with its own hash in `SHA256_L2.txt.sha256`.

## 7. Errata L2-F1–F4 (referee, /workspace/audit/lineL/REPORT.md, L2 section; applied at integration, 31 Oct 2026)

Applied in the repository copy by the integrator, because the author was busy elsewhere. No claim changes direction.

| Item | Correction |
|---|---|
| **L2-F1** (§0.3, §2 table and text, "top of the included range") | h_m ≈ ½·λ^{m/2} = ½·2.4142^m (e.g. h_9 = 1393, h_21 = 54608393), so **√h_m ≈ 1.5538^m**, not 2.4142^m. The conclusion becomes stronger: the phase-blind thresholds 3.4074^m (±2,8) and 2.5832^m (±2,16) exceed **h_m itself**, so **no level q dividing h_m** satisfies them. The column "compare √h" should read 1.5538^m, and the barrier holds at every divisor of h_m, not only at included levels. |
| **L2-F2** (§0.4, §3 Lemma B2 and "Consequence") | "Sporadic collisions of height ≤ 4 exist at every open level" requires (i) q^{1/r} < 3.3233^{1+η} < 5, i.e. **η < 0.340**, which holds only for **large p**; and (ii) that the Minkowski vector is genuinely sporadic: a nonzero F ∈ Z^r with ‖F‖_∞ ≤ 4 cannot vanish at λ, by Cauchy's root bound (every root of F has modulus < 1 + ‖F‖_∞/|lead| ≤ 5, while λ = 3 + 2√2 = 5.83 > 5), so F(λ) ∈ 𝔮∖{0}. Lemmas B1 and B2 are stated for **split** q (q ≡ ±1 mod 8, the case q ∥ h_m); for inert q the lattice Λ has index q² and B2 gives ‖F‖_∞ ≤ q^{2/r}. |
| **L2-F3** (§0.4, §3 "Consequence") | For (±2,16), "for every p" → "**for all sufficiently large p**": the bound η^{(16)} ≤ (4.282 + o(1))/log(2p+1) carries the o(1) and O(log ℓ/m) terms, so η^{(16)} < 3.770 is guaranteed only for large p. Likewise the disjointness of the height zone and the open range holds for all sufficiently large p for both families. |
| **L2-F4** (§0.2, §1 "Consequence") | "K2′ is too weak to refute anything [P]" is too strong. What is **[P]** (given the standing inputs): for every m ∈ S⁺ such that h_m has a prime q ∥ h_m in (max(c_W p², λ^{C_k + 6.1·10⁻⁶·m}), L_m), the conclusion of K2′ holds unconditionally, so K2′ gives no contradiction at such m. That this covers **all or most** m is **[H]** (C_k is effective but not computed; the evidence is the factor data only). |
| Prop S, proof step 2 (referee nit) | The number of good blocks is **min(r, 2I − k + 2)** (indices are cyclic mod r), not 2I − k + 2. With C_k = log_λ(2/ε_k) + k/2 + 1 the threshold statement is unchanged. |

