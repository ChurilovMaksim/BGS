# Line J3: towards an unconditional refutation of frozen R′ (TRACE-206)

31 Oct 2026. Work directory `/workspace/bgs-lineJ/J3/`; notes in `NOTES_J3.md`. Nothing was pushed.

**Labels.**
- [P] proved (pen and paper, written here or cited);
- [P-check] exact or arb verification of a proved identity;
- [CA] computer-assisted certificate (arb plus rigorous BLAS bounds);
- [N] numerical;
- [H] heuristic.

**Cited inputs, used as [P]:**
- Line J v2 (`../REPORT_v2.md`): Theorem J and its table M0(j), K_j, θ.
- TRACE-197: the lifted trace identity.
- TRACE-212 (Prop I2′), for every odd d | h.
- TRACE-213: the decomposition of W′.
- TRACE-216: the symmetries.
- TRACE-198/199: μ*, H₀, and the d = 7 cut-off for m ≥ 13.

## 0. Summary

**Not achieved: a fully unconditional refutation.** What is proved is a refutation along m = 3p (p prime) conditional on one analytic hypothesis, H♮, plus a mild Diophantine proviso, H_arg (§5).

**New results:**
1. **(±2,16) members: certified negligible [CA] (§1).**
   - The 64-state automaton splits exactly into 8 invariant 2-dimensional monomial blocks per operator case [P-check].
   - 32 distinct factors were built in arb, and all **576** rest certificates pass.
   - The rates are R_untw ≤ 1.6677 and R_tw ≤ 1.2587. The cross rate R_untw·R_tw ≤ 2.0991 is 0.854·ξ_lo, and the square rate is R_tw² ≤ 1.5843.
   - Their d = 7 contribution, including all composite-level copies, is ≤ 1 % of the Theorem J lower bound for every m ≥ 243.
2. **Inheritance theorem [P] + [P-check] (§2).** For d = 7D′ with gcd(7, D′) = 1 and β = D′β′, the level-d weight is
   W_{d,β} = (n_{D′}/D′²)·W_{7,β′}, with n_{D′} ≥ 0, and the twisted coefficient Ẑ is the d = 7 one.
   - So every composite-level copy of the d = 7 term is a **positive multiple** of it. It reinforces D7 and never cancels it.
   - The square parts of every Dev_d are ≥ 0.
3. **Prime levels have complete character sums [P] (§3).** For a prime q ∥ h:
   - |W_{q,β}| ≤ 2/q² for every non-isotropic β;
   - |W_{q,β}| = n_q/q² for the 2(q−1) isotropic β.
   - This kills the "slow-twist" danger [N, H].
4. **The subsequence is forced [N, H] (§4).**
   - Levels of small rank r(q) have twisted rates above the d = 7 rate 1.2836. Examples: 41, 239, 199, 353, 599, and the large primitive factors of h_17, …, h_53 in the slow-twist test.
   - Each such level dominates D7 along the multiples of its rank.
   - Only m = 3p avoids every fixed rank ≥ 5. On m = 3p all primes q ≠ 7 dividing h_m have rank p or 3p [P].
5. **Strongest proved statement (Theorem J3, §5).** On S⁺ ⊂ {3p} the bound is
   W′_m ≥ −4m + 0.99·K_j·1.0184224^m + φ⁻¹O♮_m.
   - S⁺ is infinite under H_arg (Vinogradov). arg ξ/2π is certified not to be a rational with denominator < 1339 [CA].
   - O♮_m collects only the *primitive* twisted parts of conductors ≠ 7: prime(-power) levels of rank p or 3p, and mixed 7q parts.
   - Hence: **R′ ⇒ φ⁻¹O♮_m ≤ −0.99K_j·1.0184^m + O(m) on S⁺**. Frozen R′ can hold only if the primitive large-conductor parts cancel D7 exponentially.

## 1. (±2,16) members [P-check, N, CA]

**Exact blocks [P-check].** `code/blocks16_exact.py` → `logs/blocks16_exact.{log,json}`, ALL EXACT CHECKS PASSED for all 16 cases (m mod 48 × a = ±2).
- Each case has 8 pairs (f₁, f₂) with entries in {0} ∪ ζ₁₆^ℤ, pairwise orthogonal (exact Z[ζ₁₆] arithmetic, unequal supports 32/64 handled).
- Each A_n acts monomially: diagonal or swap with ζ₁₆ phases.
- u lies in the span, so the read-out decomposes as Z = Σ_B tr(A_{B,w}J_B), with ‖J_B‖_F = ½ exactly.
- Float check [N] (`code/wordtest16.py`, `logs/wordtest16.log`): 3200 random words give max |diff| 1.1e−14.
- Deduplication by (sign, block action) leaves 32 distinct factors (`logs/blocks16_reps.json`).

**Certificates [CA].** Pipeline: `code/pipe16.py` and `run_pipe16.sh`.
- Builder: `code/certG_build16.py` = the Line J sector builder with a 2-state finite factor and phases /16 (`code/gstates16_block.py`).
  - V: K0=3, ρ=1.2, K=40, β=2.5.
  - E: K0=3, ρ=0.8, K=30.
- Certifier: `code/rig_spec.py`, the audited Line H v4, sha f346e22c, in "rest" mode with p = 64 and R = 1.02·top + 0.02.
- 32 factors × {V, E} × {untwisted, 8 d = 7 classes} = 576 certificates in `logs/cert/*_rest.json`, all `certified: true`.
- The .npy matrices were deleted after certification for disk reasons. Their sha256 are recorded in each certificate, and a rebuild is deterministic (about 1 min per factor).

Float tops [N]: untwisted max 1.61541 (= the twrad16 value), twisted max 1.21440, edge operators ≤ 0.336.

**Assembly [CA]** (`code/assemble16.py` → `logs/assemble16.{log,json}`).
- Per certificate, Cauchy and the certified resolvent give ‖T^{m−1}‖ ≤ R^m·fullR/(1−F). So |tr((J⊗P₀)T^m)| ≤ ½‖T‖₁R^m·fullR/(1−F).
- Crude weights: |W_C| ≤ 36/49, and sq ≤ 6((6/7)Σ|Ẑ_C|)² per ρ.
- Hence E16(m) ≤ 0.01·(K_min/2)·ξ_lo^m for m ≥ 213. Including the composite inheritance factor A ≤ σ(h)/h ≤ 1 + (m/2)ln λ, this holds for m ≥ 243.
- Here K_min = 0.009985, the minimum of K_j over the 28 residues.
- Modelling assumption, labelled: the read-out identity Z_ρ = (1−λ^{−m})Σ_B[tr_J V_B^m − tr_J E_B^m] is TRACE-197 with the exact block as the finite factor, as in Lines F/I. Only its finite part is re-verified here (wordtest16).

## 2. Inheritance theorem [P]

**Setting.** d = 7D′ | h, 7 ∥ h (i.e. 21 ∤ m), gcd(7, D′) = 1, and β = D′β′ with β′ ∈ O/7.

**Twist.** τ_i(β) = Tr(D′β′λ^i)/(7D′) = Tr(β′λ^i)/7. So Ẑ^{(d)}_β = Ẑ^{(7)}_{β′} exactly, by the definition of the twisted lifted trace (TRACE-212).

**Gauss sums.** Let D̄′D′ ≡ 1 (mod 7) and 7̄·7 ≡ 1 (mod D′). Then x/d ≡ xD̄′/7 + x7̄/D′ (mod 1), and CRT on g ∈ O/d gives
G^{(d)}_t(D′β′) = G^{(7)}_{tD̄′}(β′)·G^{(D′)}_{t7̄}(0).
- For u a unit mod D′, |G^{(D′)}_u(0)|² = D′². The form x² − 2y² is non-degenerate mod odd D′, and gcd(t, D′) = 1 because y′ is a unit mod h (h² + 1 = 2y′²).
- Hence conj G^{(d)}_t(0)·G^{(d)}_t(D′β′) = D′²·conj G^{(7)}_{tD̄′}(0)·G^{(7)}_{tD̄′}(β′).

**Members.** Under the frozen rule M_d = {ν ∈ U : bν ≡ a (2h/d), bν ≢ a (2h/d′) for d′ | d, d′ < d}, the members are ν = ν₀ + (2h/d)j.
- The exclusions say exactly that j is a unit mod d.
- The label is t = jy′ (mod d), the Line I rule from TRACE-212 and `verify_coset`.
- Mod 7: (2h/d) ≡ (2h/7)D̄′, so with j′ = D̄′j the unit condition at 7 and the label tD̄′ = j′y′ are exactly the level-7 ones.
- The conditions mod D′ are independent by CRT: j a unit mod D′, and ν a unit at every prime ℓ | D′ with v_ℓ(h) = v_ℓ(d). Their count is n_{D′} ≥ 0. For a prime: n_q = q − 2 if q ∥ h, and q − 1 if q² | h.

**Conclusion.** W_{d,D′β′} = (n_{D′}D′²/(7⁴D′⁴))·Σ_{level-7 t}(…) = (n_{D′}/D′²)·W_{7,β′}. ∎
- The cross part of the inherited β at level d is therefore (n_{D′}/D′²)·cross₇, the same for ρ and −ρ, so the 1:3 cancellation persists.
- Summing over the included levels gives A_m·cross₇ with A_m = 1 + Σ n_{D′}/D′² ∈ [1, σ(h)/h].

**Checks.**
- [P-check] `code/inherit_proof_check.py`: exact integer Gauss-sum histograms evaluated in arb (200 bits) for (m, a, q) = (15, 2, 41), (15, −2, 31), (33, 2, 23). Max |diff| ≤ 9e−56. ALL CHECKS PASSED.
- [N] `code/inherit7q.py`: the ratio is a positive real (39/41, 30/31, 21/23) and identical for all 8 classes.
- **Square parts.** Dev_d = Σ_t(2Re(conj(ω_tZ/d)Δ_t) + |Δ_t|²) with |ω_t| = 1. So every square part is ≥ 0 [P] and can be dropped on the positive side.

## 3. Prime levels: complete sums [P]

**Claim.** For q prime with q ∥ h, completing the square gives tN(g) + B(β,g) = tN(g + β̃/t) − N(β)/t. Hence conj G_t(0)G_t(β) = q²·e(N(β)·t̄/q).

**Proof.**
- The labels t = jy′ run over all of F_q* except one value t_b (the one with ν ≡ 0 mod q).
- Hence W_{q,β} = q⁻²·(−1 − e(N(β)t̄_b/q)) if N(β) ≢ 0, and W_{q,β} = (q−2)/q² if N(β) ≡ 0.
- 2 is a square mod q because 2y′² ≡ 1, so there are 2(q−1) isotropic β.
- If q² | h there is no missing label: |W| = 1/q² and (q−1)/q². ∎

**Checks.** [N] `code/primelevel_W.py` at q = 41: max q²|W| = 1.994 (non-isotropic) and 39 (isotropic, 80 β). At q = 31: 1.000 and 30.

**Consequence [H].**
- Slow β (|β| ~ 1, τ_i ≈ 0 for i < log_λ q from both ends of the period) can have per-step twisted radius up to 1.83 [N]. Example: the primitive q ≈ 4.9e17 of h_47 (`code/slowtwist.py`, `logs/slowtwist.log`).
- Such β are non-isotropic, so they carry weight ≤ 2/q². On m = 3p with q | h_p, this costs λ^{−2ρ/3} per step, where ρ = log_λ q/p.
- The effective rate is then ≈ 1.83·0.56 ≈ 1.03 (and ≈ 1.0 at ρ = 0.25, 0.32), well below 1.2836.
- Isotropic β have weight 1/q each and are ≥ √q in size. Their slow fraction is halved, and their effective rate is ~1.0 [H].

## 4. Which m: small-rank levels dominate [N]

**Surveys** (`code/levels_survey{,2}.py`, logs). These use a toy single-disc Galerkin, K = 40, which reproduces the certified 1.2837 and μ* = 1.9155. They give per-step max twisted radii:

| rank r(q) | level q | max twisted radius |
|---|---|---|
| 5 | 41 | 1.510 |
| 7 | 239 | 1.566 |
| 9 | 199 | 1.470 |
| 11 | 353 | 1.396 |
| 13 | 599 | 1.381 |

- All of these exceed the d = 7 survivor rate 1.2836.
- The ranks 17…53 have large primitive factors whose slow-β radius exceeds 1.2836 as well (§3).
- At a *fixed* level the weight 2/q² is constant, so such a level dominates D7 along multiples of its rank.
- Long periods are generic: r_max ≤ 1.06 for periods ≥ 35, and the Lyapunov exponent is e^γ ≈ 0.81 (`lyap.py`).

**Consequence: m = 3p (p prime) is essentially forced.**
- [P] For a Lucas sequence, q | h_m iff r(q) | m.
- On m = 3p the only ranks are 3 (q = 7) and p or 3p. Every other prime q | h_m has q ≡ ±1 (mod p), so q ≥ 2p − 1, and its twist period is ≥ p.
- 49 ∤ h, since 21 ∤ m.

## 5. Theorem J3 (strongest proved statement)

**Definitions.**
- m = 3p, p prime, m ≥ 495. The residue j = m mod 168 lies in 3·(Z/56)*.
- B_j, ξ = μ*μ₂:₁ and K_j are as in Theorem J (v2 table; K_j ≥ K_min = 0.009985).
- S⁺ = {m = 3p : cos(arg(B_jξ^m)) ≥ 0.84431} (the window arc of Theorem J).
- O♮_m = Σ_{ρ∈P*} Σ_{d included} 2Re(conj Z_ρ Σ_{β∈B♮_d} Ẑ_β W_{d,β}). Here B♮_d is the set of β ≠ 0 mod d that are *not* inherited from level 7 (β ∉ (d/7)O when 7 ∥ d).

**Theorem J3.**
1. **[P] Identity:** W′_m = W′_A + φ⁻¹[A_m·X7_m + X16_m + Q_m + O♮_m], where:
   - X7 is the d = 7 cross part of ρ = (±2,8);
   - X16 is the d = 7 part of (±2,16), including its inherited copies;
   - Q_m ≥ 0 collects all square parts;
   - A_m ≥ 1.
2. **[CA, Theorem J]:** X7_m ≥ (K_j/2)ξ_lo^m on S⁺, using cos ≥ 0.8443, m ≥ M0(j) and the certified error budget.
3. **[CA, §1]:** |X16_m| ≤ 0.01·(K_min/2)ξ_lo^m for m ≥ 243.
4. **[P, Prop I8]:** W′_A ≥ −4m.

Hence, on S⁺ (using φ < λ^{m/2}/2):
**W′_m ≥ −4m + 0.99·K_j·(1.0184224)^m + φ⁻¹O♮_m.**

**Size of S⁺.**
- [P, Vinogradov, primes in APs] If arg ξ/2π is irrational, then for every residue p₀ mod 56 the set S⁺ ∩ {p ≡ p₀} has relative density 2·0.5655/2π ≈ 0.18 among those primes. In particular it is infinite.
- [CA] `code/rat_excl.py`: arg ξ/2π lies in [0.88797591, 0.88797627] and is **not** a rational with denominator < 1339.
- The modulus-168 window lemma does not apply, because {3p} is not an arithmetic progression. The modulus 360360, which would fix m mod 5, 7, 9, 11, 13, is too coarse for the certified enclosure (`theta_big.py`: its θ-interval contains 0). The modulus 27720 works.

**Corollary (dichotomy).** Assume H_arg (arg ξ/2π ∉ ℚ). If frozen R′ holds, then along the infinite set S⁺ ⊂ {3p}:
φ⁻¹O♮_m ≤ −0.99K_j·1.0184^m + 4m + o(m).
So the primitive conductor-≠7 parts would have to cancel the d = 7 term exponentially.

**The remaining hypothesis.**

> **H♮:** On S⁺, O♮_m ≥ −(1−δ)·0.99·(K_j/2)·ξ_lo^m for some δ > 0. A sufficient form: |O♮_m| ≤ e^{o(m)}·r^m with r < ξ_lo = 2.4587.

Under H♮ and H_arg, **frozen R′ is false**: W′_m/m → +∞ along S⁺.

**What H♮ amounts to.**
- O♮_m runs over primitive conductors c | h_{3p}, c ≠ 7: prime powers of rank p or 3p, their products, and mixed 7·c parts.
- Using |W| ≤ 2/q² (§3), H♮ reduces to a uniform bound on weighted averages of twisted lifted traces Ẑ_β along cat-map orbits τ_i = Tr(βλ^i)/q, for all large q.
- Evidence [N/H]: the slow-twist survey gives effective ≈ 1.0, generic radii are ≤ 1.06, and e^γ ≈ 0.81. All of these are far below 1.2836 (μ*-normalised).
- Why it is not proved:
  - the set of conductors is unbounded (TRACE-219);
  - a Parseval approach gives Σ_β|Ẑ_β|² in terms of bulk moments of Z(ν) at that level, which is circular with R′_A;
  - a uniform certificate over infinitely many q needs an equidistribution theorem for twisted transfer-operator products along hyperbolic toral orbits. That is not available.
- H_arg is a side condition. It could be removed either by an explicit Jacobsthal-type gap argument for rationals of denominator ≥ 1339 (not done), or by a sharper μ* enclosure. The current enclosure is r = 2e−6 from Line F.

## 6. Files (SHA256 in `SHA256_J3.txt`)

**Code (`code/`):**
- `blocks16_exact.py`, `wordtest16.py`, `gstates16_block.py`, `certG_build16.py`, `pipe16.py`, `run_pipe16.sh`, `rig_spec.py` (f346e22c), `assemble16.py`;
- `inherit7q.py`, `inherit_proof_check.py`, `primelevel_W.py`;
- `levels_survey.py`, `levels_survey2.py`, `slowtwist.py`, `lyap.py`, `ranks.py`;
- `theta_big.py`, `rat_excl.py`;
- exploratory: `sector16*.py`, `validate16.py` (abandoned: OOM-prone, about 6.5 GB; replaced by wordtest16), `run_build16.sh` (superseded), `ftop16.py`.

**Logs (`logs/`):** the corresponding `.log`/`.json` files, and `cert/` (576 certificates plus build logs).

**Line J v2** (referee fixes F1–F11): `../REPORT_v2.md`, `../STRATEGY_v2.md`, `../logs/SHA256_v2.txt`.
