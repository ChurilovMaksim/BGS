# Line J report: the d = 7 twisted coefficient in frozen R′ (TRACE-206)

Line J. Box `/workspace/bgs-lineJ/`, 31 Oct 2026, times UTC+5. Nothing was pushed to the repo.

Labels used throughout:
- **[P]** proved by hand;
- **[P-check]** an exact (integer or cyclotomic) computer verification of a finite statement;
- **[CA]** computer-assisted, arb-certified;
- **[N]** floating-point numerics;
- **[H]** heuristic.

## 0. Short summary

1. **J1 is decided, with a twist.** The coefficient c(β) of every top twisted orbit is exactly ±(an 8th root of unity)/2, so it is non-zero.
   - This follows from an exact sector decomposition of the 16-state automaton [P-check].
   - In the combination that actually enters frozen R′ (the sum over ρ = (2,8) and (−2,8)), the leading class **1:3** (|μ| = 1.2837143) **cancels exactly** [P]. So do the classes 1:2 and 1:5. The cancellation comes from an antiunitary symmetry: sector a of ρ = (2,8) maps to sector a+4 of ρ = (−2,8), with c₂ = c₆ = ½ for both signs.
   - The classes in sectors 0 and 4 do **not** cancel; they **double**: B_C = 2c₀ᶠc₄⁽⁺⁾W_C ≠ 0. The surviving leading class is **2:1**:
     - |μ₂:₁| ∈ [1.28359503, 1.28359523] [CA];
     - ξ = μ*μ₂:₁ with |ξ| ≥ 2.4586893 > √λ = 2.4142136;
     - the growth rate |ξ|/√λ is ≥ 1.0184224 [CA].
2. **Explicit theorem (Theorem J, §3) [CA].** Take the frozen d = 7 deviation of the two primaries (±2,8),
   D7(m) = Σ_ρ Σ_{t∈M₇(ρ)} (|Z_t|² − |Z_ρ|²/49).
   - **Condition:** m ≡ 3 (mod 6), and let j = m mod 168.
   - **Conclusion:** every 6 consecutive terms m₀, m₀+168, …, m₀+840 of the class j with m₀ ≥ M0(j) contain an m⁺ and an m⁻ with
     D7(m^±)/(m·φ(2h_m)) ≷ ±K_j·1.0184224^m/m.
   - M0(j) ∈ [297, 495] and K_j > 0 are explicit (table in §3). From m₀ ≥ M1(j) ∈ [417, 621] both values are at least 1 in absolute value.
   - So the frozen d = 7, (±2,8) remainder in W′/m is **unbounded above and below**; it is not o(m).
   - Every competing term *inside* D7 is rigorously bounded: other twisted classes, other sectors, the edge operators E, subleading orbits, the Line F error of Z₀, the square term, and all Galerkin/truncation errors.
3. **What is NOT proved.** Frozen R′ itself is **not** refuted unconditionally.
   - We have W′ = W′_A + φ⁻¹(D7 + O_m) [P, TRACE-213]. Here O_m collects the deviations of all other (ρ, d): the other levels d | h_m (unbounded prime support), the (±2,16) members, and any other members of P*.
   - **O_m is not controlled.** Two partial checks:
     - (±2,16) at d = 7 [N]: the rate is 1.615413 × 1.2144 = 1.962 < √λ, so it is exponentially negligible (float only).
     - Other levels: no control at all.
   - **Proved corollary.** If O_m ≥ −C·m·φ(2h_m) for large m (a one-sided bound), then W′_m/m → +∞ along the m⁺ above, and frozen R′ is false.
   - Equivalently: frozen R′, R′_A and "O_m = o(mφ)" cannot all hold.
4. **Numerics [N], m = 201…453.** D7/(m·h) grows from ~10⁻² at m ≈ 200 to O(1) at m ≈ 430–450 (+2.18 at m = 447, −1.43 at m = 441), with oscillating sign. The two ρ halves of class 1:3 are equal and opposite to all printed digits. This is consistent with Theorem J (M1 ≈ 420–620).
   - Since φ(2h) < h, the true |D7|/(mφ) is larger than |D7|/(mh).
   - W′ itself cannot be computed at these m: F_m would need an exact 2h-sum with h ~ 10⁸⁰.
5. **J2:** see `STRATEGY.md`.

## 1. Set-up and the exact formulas

### Notation
- λ = 3+2√2; m ≡ 3 (mod 6), so 7 | h_m.
- c_m = 1 − λ^{−m}.
- ρ ∈ {(2,8), (−2,8)}, written ±.

### Member formula (Prop I2′, TRACE-212) [P]
Z_t = ω_t Z_ρ/7 + Δ_t, with Δ_t = 7⁻² Σ_{β≢0} Ẑ_ρ(β) G_t(β). Consequently:
- the d = 7 deviation of ρ is cross_ρ + sq_ρ, with sq_ρ = Σ_t |Δ_t|² ≥ 0;
- cross_ρ = 2 Re( conj(Z_ρ) Σ_C Ẑ_ρ,C W_C(ρ,m) ), where W_C = 7⁻⁴ Σ_{t∈M(ρ)} conj G_t(0) Σ_{β∈C} G_t(β), summed over the 8 classes C of size 6.

### Sector law [P]
This combines the Line I transfer law with the exact sector decomposition (`code/sectors_exact.py`, `logs/sectors_exact.json`, "ALL EXACT CHECKS PASSED") [P-check].
- **Sectors.** For every operator case (m mod 24 ∈ {9, 15, 21, 3}) and both signs, the 16-state automaton has four rank-1 sectors f_a, a ∈ {0, 2, 4, 6}, with A_n f_a = e(an/8) f_a.
- **Complement.** The complement is orthogonal to the read-out vector u, so it contributes 0.
- **Constants.** J = Σ_a c_a(·) with |c_a| = ½, exactly in Z[ζ₈].
- **Formula.** Ẑ_ρ(β) = c_m Σ_a c_a(case,ρ) · ⅓[Tr V_{β,a}^m − Tr E_{β,a}^m]. Here V_{β,a} and E_{β,a} are the twisted lattice and edge operators with the automaton replaced by the scalar e(an/8) (`code/gstates_sector.py`).
- **Numerical check [N].** The formula reproduces the Line I zpred class sums to 10⁻⁷ relative (`code/check_model.py`).

### Z₀ (Line F, TRACE-197/199, audited) [CA]
- Z_(−2,8) = c_m(c₄ᶠ μ*^m + ε) and conj Z_(2,8) = c_m(c₀ᶠ μ*^m + ε′).
- c₀ᶠ = e(κ/8)/2 = −c₄ᶠ, where κ = κ(m mod 8).
- |ε|, |ε′| ≤ H₀ = 2(T_V+T_E) ≤ 1506.18.
- μ* ∈ D(b₁₁, 2·10⁻⁶) and |μ*| ∈ [1.9154712, 1.9154753] (`certV_eta2_a4_tight.json`, sha c77348b6…).

### Symmetries [P] (Line I S4.1, audited D-2)
L^{(m,−2)}_β = J L^{(9,2)}_{−β} J⁻¹ with J antiunitary (K⊗X⊗I₃), and L_{−β} ≅ L_β by the reflection R⊗Y⊗I₃.
- Restricted to sectors, conjugating by K multiplies the letter weight by conj(e(an/8))(−1)ⁿ = e((4−a)n/8). The reflection n → −n then sends 4−a to a−4. Hence:
  - **σ(V^{(−2)}_{β,a+4}) = conj σ(V^{(+2)}_{β,a})**, and the same for E.
  - The certified sector of each top orbit agrees: 2:1 in s4/s0, 0:1 in s0/s4, 1:3 in s6/s2 (§2).
- In particular μ_{C,−}^m = conj(μ_{C,+})^m for 3 | m.

## 2. Certificates [CA]

All runs use nice -n 10 and 2 threads. Each run's JSON records its code SHA and input SHA in its provenance; the full manifest is in `logs/SHA256_*.txt`.

### Builder
`code/certG_build_sector.py` is Line I dom_v3 `certG_build.py` with the gstates import swapped (diff = import + provenance only). Builds via `code/run_cert_build.sh`:
- **V operators:** K0=5, ρ=1.2, K=60, β=2.5, D=1980. Errors: δ₁ 2.2e−13, δ₂ 3.7e−13, Δ 7.8e−14. Trace norm ≤ 2688.9.
- **E operators:** K0=4, ρ=0.8, K=40.
- **Cases:** a = +2 (case 9) and a = −2 (case 15). The other cases follow by exact symmetry.

### Top orbits
`code/rig_dom3b.py` is identical to Line I v3 (sha e4ff0f7f). `code/rig_disc.py` is new: the same machinery on a small circle |z−c| = r.

| block | count cert | disc cert (r = 1e−7) |
|---|---|---|
| 2:1, a=+2 s4 / a=−2 s0 | exactly 3 eigenvalues in \|z\| > 0.8 (F = 5.2e−7) | exactly 1 eigenvalue in D(1.2795445309020579+0.1018933656159788i, 1e−7) (F = 0.194); \|μ₂:₁\| ∈ [1.28359503, 1.28359523] |
| 0:1, a=+2 s0 / a=−2 s4 | 3 in \|z\| > 0.9 (F = 9.1e−7) | D(−1.068708899896592+0.672006237087771i, 1e−7) (F = 0.198); \|μ₀:₁\| ≤ 1.2624308 |
| 1:3, a=+2 s6 / a=−2 s2 | 3 in \|z\| > 1.0 (F = 1.2e−6) | D(−1.2554152882657945+0.268057540175505i, 1e−7); \|μ₁:₃\| ≤ 1.2837144 |

The Z/3 symmetry then gives orbits {μ, ωμ, ω²μ} with μ in the disc.

### Rest certificates
`code/rig_spec.py` is Line H v4 (sha f346e22c), mode "rest". All of the following are certified:
- **V blocks:** the other 58 (class, sector, sign) blocks, with R = min(1.25, float radius + 0.08).
  - The first pass used Neumann order p = 32 and failed in 58 cases. The rerun used p = 64 (`run_cert_rest2_*.sh`).
  - The largest R is 1.247 (classes 1:2/1:5 in s6, float radius 1.1671).
- **E blocks:** all 64, with R = 0.45 (float maximum 0.358).

### Weyl bounds
For each class C and sign, the non-top part of ⅓ΣTr is bounded by e_C(m) = (1/6) Σ_a (R_V^{m−1}T_V + R_E^{m−1}T_E).

## 3. Main results

### Proposition J-C (exact leading coefficient) [P + P-check]
Write Ẑ_±,C = c_m(c^±_C μ_{C,±}^m + ε^±_C) for the tracked classes. Then the leading part of cross₊ + cross₋ for class C is
2c_m² Re(B_C ξ_C^m), with ξ_C = μ*μ_{C,+} and **B_C = c₀ᶠ (c^+_C − conj c^-_C) W_C(+,m)**.

Proof:
- conj(Z_+)Ẑ_+W_+ has leading term c_m² c₀ᶠμ*^m c^+μ_+^m W_+.
- conj(Z_−)Ẑ_−W_− has leading term c_m² conj(c₄ᶠ)conj(μ*)^m c^- conj(μ_+)^m W_−.
- **W_− = conj W_+** [P]. Since conj G_t(β) = G_{−t}(−β), and C = −C, conj W(ρ) is W evaluated with the member set −M(ρ). Moreover ν₀(−ρ) = 2h − ν₀(ρ), so M(−ρ) = −M(ρ). This is also checked exactly in Z[ζ₇] (`exact_B.py`).
- The real part of the second term is therefore Re(c_m² c₄ᶠ conj(c^-) W_+ ξ^m).
- Use c₄ᶠ = −c₀ᶠ.

Exact values:
- **Sectors 2 and 6:** c^{(case,+2)}_a = +conj c^{(case,−2)}_{a+4} = ½ for a ∈ {2, 6}, so **B = 0**. This covers 1:3, 1:2 and 1:5.
- **Sectors 0 and 4:** c^{(case,+2)}_a = −conj c^{(case,−2)}_{a+4} for a ∈ {0, 4}, so B = 2c₀ᶠc_a^{(+)}W_C and |B| = |W_C|/2. This covers 2:1 and 0:1.
- Both relations hold for all 4 cases [P-check, `logs/exact_B.json`].
- W₂:₁ and W₀:₁ are non-zero in Z[ζ₇] for all 28 residues j mod 168 (m ≡ 3 mod 6). The period is 168 = lcm(24 case, 8 κ, 42 member set); W's period was checked over 3 periods, and the member sets are the exact unit conditions.
- The values are |W| = (12/49)|cos(π t̄ N_C/7)| ∈ {0.0545, 0.1527, 0.2206}, or 6/49 when 7 | m. ∎

### Window lemma [P]
Suppose θ ∈ [θ_lo, θ_up] ⊂ (0, π]. Then for any α, among N = ⌈2π/θ_lo⌉ consecutive k there is one with cos(α+kθ) ≥ cos(θ_up/2), and one with cos ≤ −cos(θ_up/2).

Proof: the closed arc of length θ_up ≥ θ around 0 (respectively π) cannot be jumped over by steps of length θ. Starting outside it, the first entry happens after ≤ ⌈(2π−θ)/θ⌉ ≤ N−1 steps. ∎

**Applied here:** θ = 168·arg ξ₂:₁ mod 2π ∈ [1.130677, 1.131054]. The uncertainty comes from the μ* disc (2e−6) and the μ₂:₁ disc (1e−7). This gives N = 6 and cos(θ_up/2) ≥ 0.844306.

### Theorem J [CA]
Let m ≡ 3 (mod 6), j = m mod 168, and use the per-residue table below (`logs/assemble.json`, `code/assemble.py`).

1. **Growth.** For m ≥ M0(j), in the expansion
   cross₊+cross₋ = 2c_m² Re(B₂:₁ ξ^m) + 2c_m² Re(B₀:₁ ξ₀:₁^m) + Err(m)
   (the 1:3 term vanishes exactly), the bound c·|B₂:₁||ξ|^m > |B₀:₁||ξ₀:₁|^m + |Err|/(2c_m²) holds.
   - Err covers the following, all rigorously bounded:
     - every non-top eigenvalue of every (class, sector, sign) block of V and E (Weyl bound);
     - the Line F error H₀ times every Ẑ;
     - the subleading Z₀;
     - all Galerkin errors, which sit inside the certificates.
   - The bracket divided by ξ_lo^m is increasing in m, because every subtracted rate is below ξ_lo:
     - ξ₀:₁/ξ ≤ 0.98352;
     - |μ*|·R_max/ξ ≤ 0.97150;
     - μ₁:₃/ξ ≤ 0.52212.
   - So positivity at M0 implies positivity for all m ≥ M0.
2. **Consequence.** In every 6 consecutive terms of the class j from M0(j) on, there are m⁺ and m⁻ with
   D7(m⁺)/(m φ(2h)) ≥ K_j·(1.0184224)^m/m and D7(m⁻)/(m φ(2h)) ≤ −K_j·(1.0184224)^m/m + sq/(mφ).
   - The square term satisfies sq ≤ Σ_ρ 6((6/7)Σ_C|Ẑ_C|)². Its rate is μ₁:₃²/ξ ≤ 0.670 relative, so it is negligible: rm = rp to the digits shown in the log.
   - This uses φ(2h) = φ(h) < h < λ^{m/2}/2 [P], since h² = (x_m − 1)/2.
3. **Threshold.** From m ≥ M1(j), both |·| are ≥ 1.

Per-residue table:

| j = m mod 168 | 7∣m | \|W₂:₁\| | \|B₂:₁\| ≥ | M0(j) | K_j | M1(j) |
|---|---|---|---|---|---|---|
| 3 |  | 0.22065 | 0.11032 | 339 | 0.2736 | 507 |
| 9 |  | 0.05449 | 0.02725 | 345 | 0.009975 | 513 |
| 15 |  | 0.15269 | 0.07635 | 351 | 0.1881 | 519 |
| 21 | yes | 0.12245 | 0.06122 | 357 | 0.1367 | 525 |
| 27 |  | 0.15269 | 0.07635 | 363 | 0.2084 | 531 |
| 33 |  | 0.05449 | 0.02725 | 369 | 0.05093 | 537 |
| 39 |  | 0.22065 | 0.11032 | 375 | 0.3371 | 543 |
| 45 |  | 0.22065 | 0.11032 | 381 | 0.3426 | 549 |
| 51 |  | 0.05449 | 0.02725 | 387 | 0.06753 | 555 |
| 57 |  | 0.15269 | 0.07635 | 393 | 0.2368 | 561 |
| 63 | yes | 0.12245 | 0.06122 | 399 | 0.1857 | 567 |
| 69 |  | 0.15269 | 0.07635 | 405 | 0.2428 | 573 |
| 75 |  | 0.05449 | 0.02725 | 411 | 0.07971 | 579 |
| 81 |  | 0.22065 | 0.11032 | 417 | 0.3616 | 417 |
| 87 |  | 0.22065 | 0.11032 | 423 | 0.3633 | 423 |
| 93 |  | 0.05449 | 0.02725 | 429 | 0.08465 | 597 |
| 99 |  | 0.15269 | 0.07635 | 435 | 0.2513 | 435 |
| 105 | yes | 0.12245 | 0.06122 | 441 | 0.2003 | 441 |
| 111 |  | 0.15269 | 0.07635 | 447 | 0.2531 | 447 |
| 117 |  | 0.05449 | 0.02725 | 453 | 0.08828 | 621 |
| 123 |  | 0.22065 | 0.11032 | 459 | 0.369 | 459 |
| 129 |  | 0.22065 | 0.11032 | 297 | 0.042 | 465 |
| 135 |  | 0.05449 | 0.02725 | 471 | 0.08975 | 471 |
| 141 |  | 0.15269 | 0.07635 | 309 | 0.02464 | 477 |
| 147 | yes | 0.12245 | 0.06122 | 483 | 0.2047 | 483 |
| 153 |  | 0.15269 | 0.07635 | 321 | 0.09275 | 489 |
| 159 |  | 0.05449 | 0.02725 | 495 | 0.09083 | 495 |
| 165 |  | 0.22065 | 0.11032 | 333 | 0.255 | 501 |

The table entries are computed as follows:
- K_j = 4·bracket(M0)/ξ_lo^{M0}, with a 10⁻³ safety margin.
- |W| comes from double-precision Gauss sums with a relative margin of 10⁻⁹. Its non-vanishing is exact (§3).
- For the residues with 7 | m (49 | h), the d = 7 level uses the 6 members as in Line I's convention.

### What Theorem J means for R′
- **Identity [P] (TRACE-213):** W′_m = W′_A,m + φ⁻¹(D7(m) + O_m).
- **Positivity [P]:** W′_m ≥ φ⁻¹ Σ_{all (ρ,d)} Dev − 4m.
- **Corollary J (conditional) [CA + hypothesis].** If O_m ≥ −C·m·φ(2h_m) for all large m, then W′_m/m ≥ K_j·1.0184^m/m − C − 4 along the m⁺. So W′_m/m → ∞ and frozen R′ fails along a positive-density subsequence of every residue class j.
- **Unconditionally [CA]:** R′ ∧ R′_A ⇒ φ⁻¹O_m/m is unbounded in both directions along m^∓. That is, the uncontrolled terms would have to cancel an exponentially growing oscillation with period 168·(2π/θ) in m.
- **Not controlled:**
  - the other levels d (d | h_m, d ≠ 7; prime support of h_m unbounded);
  - the (±2,16) members (float rate 1.962/√λ = 0.81^m [N], `logs/twrad16.log`: |Z₀| rate 1.615413, max twisted radius 1.2144, 64 states);
  - any further members of P*;
  - the bulk entering W′_A.

So the precise proved statement is: *the frozen d = 7 twisted contribution of ρ = (±2,8) alone grows at rate ≥ 1.0184224^m/m in W′/m, with both signs, in every residue class mod 168.*

## 4. Numerical check [N] (`code/numerics_large_m.py`, `logs/numerics_large_m.log`)

Method:
- Exact sector law with float spectra of the certified D = 1980 blocks.
- Z₀ from the Line F leading term; its relative error is ~10⁻⁸⁰ at these m.
- Normalised by m·h, which is smaller than m·φ.

Selected values:

| m | D7/(mh) | cross₊/(mh) | cross₋/(mh) | 1:3 parts (±) |
|---|---|---|---|---|
| 201 | −0.0023 | −0.025 | +0.023 | ∓0.024 |
| 249 | +0.164 | | | |
| 333 | −0.409 | | | |
| 375 | +0.969 | | | |
| 381 | −0.939 | | | |
| 435 | +1.38 | | | |
| 441 | −1.43 | | | |
| 447 | +2.18 | | | |

- The 1:3 parts are equal and opposite in every row, as Prop J-C predicts.
- Square terms are ≤ 10⁻³⁵ relative.
- The oscillating envelope grows like ~1.018^m, consistent with Theorem J. Separately, each single-ρ cross term carries the cancelled 1:3 part, which is of the same size.
- This explains the "partial cancellation of the two ρ" seen in Line I (REPORT_v2 iii).

## 5. Files

### Code (`code/`)
| file | role |
|---|---|
| sectors_exact.py | exact sectors |
| exact_B.py | exact B ingredients |
| gstates_sector.py, certG_build_sector.py | builder |
| run_cert_build.sh | builds |
| rig_dom3b.py, rig_disc.py, rig_spec.py | certificates |
| run_cert_tracked.sh, run_cert_rest.sh, run_cert_rest2_{0,1}.sh | certificate runs |
| float_cert_survey.py | float survey |
| assemble.py | theorem |
| numerics_large_m.py | §4 numerics |
| twrad16.py | (±2,16) float rates |
| model_cross.py, model_lead.py, check_model.py, check_z0.py | float model checks |

### Logs (`logs/`)
| file | content |
|---|---|
| sectors_exact.{log,json}, exact_B.{log,json} | exact checks |
| cert/*.json, cert/*.log | 6 count + 6 disc + 122 rest certificates; build logs |
| assemble.{log,json}, residue_table.md | theorem and table |
| numerics_large_m.{log,json} | §4 numerics |
| twrad16.log | (±2,16) float rates |

### SHA256
Manifests are `logs/SHA256_code.txt`, `logs/SHA256_logs.txt` and `logs/SHA256_build_json.txt`. Key hashes:
- assemble.py 351de016…, rig_disc.py 8b1a4800…, exact_B.py 20abf5e6…, certG_build_sector.py 14a5b369…, gstates_sector.py e7c42470…, sectors_exact.py d25d8124…;
- assemble.json 14dc3e12…, exact_B.json 6590bc01…, sectors_exact.json aff4384f…;
- Line F input c77348b6….

### Caveats for a referee
1. rig_disc.py is new code (a contour change to rig_dom3b v3) and has not been independently audited.
2. The sector law and the K-conjugation sector map (a ↦ a+4) are derived from audited Line I identities, but the sector-level form is new.
3. Z₀ and H₀ are taken from Line F (audited).
4. W is evaluated in double precision with a margin, while non-vanishing is exact.
5. The 7 | m residues rely on Line I's convention for the d = 7 level when 49 | h.
