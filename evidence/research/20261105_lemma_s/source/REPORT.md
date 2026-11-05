# research1105b — bad divisor levels in R′ (BGS-BGS-001, TRACE-206): harmless without cancellation?

Grok Bot, 2026-11-05 (CET). Repo ChurilovMaksim/BGS, main @ 6f69baa1. Shallow clone in `repo/` (depth 50), plus read-only fetch of
`research-grok46-1104` @ f7986a9f (grok47 `h5_xline`). No Mathlib cache. **Nothing pushed.**

**Labels.** [P] full proof here. [P-sketch] proof with routine gaps named. [CA] exact or rigorous computation.
[N] floating-point numerics (twb/L2 transfer law, L=8, K=16, validated in §3.1). [H] heuristic. [C] conjecture.

**Code and logs.** All code is in `code/`, all logs in `logs/`. Every number in this report has a log file; §6 lists them.

---

## 0. Main finding (short)

1. **What the bad levels contaminate** (§1). They enter only the level deviations Dev_d of the frozen R′ sum: at the top level h_p through ⟨E⟩ = X_iso + Y, and at the proper levels d | h_p.
   - Numerically [N] both are tiny next to the gas term. Two independent pipelines agree on every value, and this rests on fully exact enumeration at p = 11.
   - **No counterexample family is suggested** (§3). At m = 3p, the K- and hp-proper levels are 7–8× (K-level 7) and roughly 90–1000× (hp-divisor levels) below the gas Dev.
2. **Positivity, sign symmetry, monotone lower bounds and weaker targets are dead as mechanisms** (§2, [P] no-go statements). None of them removes a level whose |Z_ρ|²/d² is of gas size.
3. **New structural result (§4).** Cross-line points ("bad" lines: ε^p ≢ ±1 mod 𝔞̄) are small *pointwise*, not by cancellation.
   - Exact [N]: |X_cross|/ℓ1(cross) = 0.35 (p=11) and 0.62 (p=13). Meanwhile ℓ1(cross)/ℓ1(Binet) = 2.4e-3 and 6.8e-3.
   - So the smallness of X_line is **not** an averaging effect. That fits Theorem L (no cancellation exists to be had).
   - The arithmetic reason is proved:
     - **Lemma S (antipodal-window height bound) [P].** On a cross line every primitive point c satisfies G(cε^n) + G(cε^{n+p}) ≥ √max(d₊,d₋) for every n. There is no "vacuum": a cross line cannot carry the two antipodal resonant windows that build the Binet gas 2[(1+Λ)^p − 1].
       - Exhaustive check [N]: min over primitive points of max(G(n),G(n+p))/√D = 0.81 (p=11) and 0.89 (p=13); p=17 is in §4.2. On Binet lines the value is 1/√D (vacuum c = 1).
     - **Polymer gap lemma [P].** An ε-local seam-bridging defect of span k and coefficient size A is divisible by η₊η₋ (the full-level kernel) unless ε^k ≳ min(d₊,d₋)/(CA)².
     - **Binet lattice = (η_s) [P, CA p ≤ 73].**
     - **H5(b) exponential sufficiency [P].**
4. **Status.** H5(b) (cross lines) and the hp-proper-level part of the contamination reduce to *one* analytic input: a per-site cost bound for non-resonant ("seam") sites in the polymer expansion, of the same type as v5's H1/(I)/(T). No new arithmetic hypothesis on P⁻(h_p) is needed for the vacuum part, because max(d₊,d₋) ≥ √h_p always.
   - The polymer-bridged part still sees min(d₊,d₋) through the gap lemma. So for the 2p+1 family (TRACE-350) the Mersenne-type ceiling is **reduced but not removed**: it moves from "needs P⁻(h_p) large" to "needs a seam-polymer activity decay γ > γ* ≈ 0.87–0.99 per log_ε". This is [C]; see §5.

---

## 1. R′ exactly, and where bad levels enter

R′ as frozen in TRACE-206 (restated from `record/claims.json` and the THEOREM_DRAFT_v5 conventions):

- **Kick.** k1 kick ĝ(n) = iⁿJ_n(1.8). Take odd m, h = h_m, φ = φ(2h), and P* = {(±2,8), (±2,16)}.
  - For ρ = (a,b) ∈ P*, ν_ρ is defined by bν ≡ a (mod 2h), and Z_ρ = Z_m(ν_ρ).
- **Levels.** A level is a d | h with 1 < d ≤ √h. Its members are
  M_d = {ν unit mod 2h : bν ≡ a (mod 2h/d), and not mod 2h/d′ for any d′ | d with d′ < d}, with n_d = |M_d|.
  - Level d is *included* iff |Z_ρ|²/d² ≥ 4m. RMT = 4m − m²/h.
- **Residual.** Res = (1/φ) Σ_ρ [(|Z_ρ|² − RMT) + Σ_{d incl.} n_d (|Z_ρ|²/d² − RMT)], and W′ = F − RMT − Res.
- **R′ ⟺ W′_m = o(m).** A refutation needs |W′_m| ≥ c·m infinitely often, of either sign.
- **Line I identity (TRACE-213) [P].** W′ = NR + φ⁻¹ Σ_ρ Σ_d Dev_d, where Dev_d = Σ_{ν∈M_d}|Z(ν)|² − n_d|Z_ρ|²/d².
  - NR ≥ −4m, and Dev_d ≥ −n_d|Z_ρ|²/d² (the floor).
- **Member formula I2′ (TRACE-212) [P].** |Z(ν_j)|² = (|Z_ρ|²/D²)·|1 + E(t̄)|², with
  E(s) = Σ_{β≠0 mod D} e(s·Nm β/D)·Ẑ(β)/Z_ρ and t̄ = (j·y′)⁻¹ mod D. Hence

  Dev_D / main_D = |1 + ⟨E⟩|² − 1 + Var_t(E),  main_D = n_D|Z_ρ|²/D².

  - The mean is ⟨E⟩ = X_iso + Y_mix + Y_partial, with Ramanujan weights μ(e)/φ(e) on the classes.

**Contaminated quantities.** The bad levels at composite h_p (m = 3p, D | h_p) contaminate exactly two things:

- **(a) The top hp level D = h_p.** Through the linear term 2Re⟨E⟩. Specifically:
  - the cross-line part of X_iso (H5(b): X_line on lines with mixed ε^p-signs);
  - the mixed/partial classes Y (unit at some primes, isotropic at others). This is H5(a)/(b′).
- **(b) The proper levels d | h_p, 1 < d < h_p.** Whenever they are included. Their Dev_d is a signed quantity of relative size |Z_ρ|²/d² × (small).
  - The relative weight against the gas is amplified by (h_p/d)², and the floor gives only Dev_d ≥ −main_d, which is far too large.

Everything else in R′ (NR, the level h_p iso gas, the K-levels such as 7 | h_m) is untouched by the factorisation of h_p.

---

## 2. Mechanisms that would make bad levels harmless without cancellation

| mechanism | status | reason |
|---|---|---|
| positivity (TRACE-228 positive weights) | **dead** [P no-go] | Over the whole coset tower, Parseval makes the frozen prediction equal to the "α_n uniform mod D" model. For prime q, σ*(q) = 1 + 1/q − 1/q² exactly. Positivity then yields only floors Dev_d ≥ −main_d ~ \|Z_ρ\|²/P⁻(D)², which is ≫ the gas when P⁻ is small. |
| variance compensates a negative mean | **dead** [P] | If the mixed class distribution is flat, its E-contribution depends only on t mod e, and its variance part vanishes. Var ≥ 0 helps only the sign of Dev, never the size of 2Re⟨E⟩. |
| sign symmetry ρ ↔ −ρ | **dead** [P] + [N] | Z(−ν) is the conjugate of Z(ν) twisted by ½ at every site; it is not a sign flip. Data: Dev signs differ between ρ and −ρ (m33 d=7: +9.4e-3 vs −7.2e-4; §3.2). |
| lower bound on B_p monotone in added levels | **dead** [P] | Adding a level adds n_d(\|Z_ρ\|²/d² − RMT) to Res, and the true contribution can be at the floor. No monotone inequality holds without a lower bound on Dev_d/main_d, which is exactly the contaminated quantity. |
| weaker target (liminf, either sign) | **does not help** [P] | R′ is refuted by \|W′\| ≥ cm i.o. of either sign, so the refutation already uses the weakest form. The levels are still there. |
| exact-copy levels (closed form, Theorem 6) | **partially alive** [P] | Theorem 6 (grok47): 1 + X_line = h·W(𝔄̄)/Z0. The Binet line lattice is 𝔄 = (η_s), η_s = ζ − 1 − 2sζ^{(p+1)/2} [P; N(η_s) = h_p checked exactly for p ≤ 73, `logs/eta_norm.json`]. This gives the closed polymer structure on Binet lines, but no closed form for cross lines. |
| **pointwise suppression on cross lines (new)** | **alive: arithmetic part [P], analytic part open** | §4. |

---

## 3. Numerics (exact enumeration, independent recomputation)

### 3.1 Validation [N]
- **m = 15 vs exact Line G tables** (`logs/validate_m15.*`):
  - D = 41: Dev 261182.5 (exact) vs 261179.0 (law); for −ρ, 237985.7 vs 237984.0.
  - D = 31 and D = 7 also agree; |Z_ρ|² agrees to 2e-5 relative.
- **Truncation.** K=16 vs K=24 differ by 3.7e-14 absolute (`logs/kconv_m33.log`). L=10 is numerically broken (Z0 ~ 4e14), so L=8 is the standard.

### 3.2 Proper levels d | h_m, recomputed independently [N] (`code/run_proper.sh`, `logs/prop/`, `logs/final_levels.json`)
- **Method.** New pipeline: level.py enumerates *all* β mod D (orbit-reduced), then analyze.py with the I2′ member formula.
  - The earlier values came from lineN17b `b_exact_dev.py` / `d_g3dev.py` (logs d33.out, d39.out).
- **Units.** Dev/(φm), with φ = φ(2h_m).

| m | d | ρ=(2,8) new | ρ=(2,8) old | ρ=(−2,8) new | ρ=(−2,8) old |
|---|---|---|---|---|---|
| 33 | 7 (K) | 9.4177e-3 | 9.4e-3 | −7.1838e-4 | −7.2e-4 |
| 33 | 23 | −5.7959e-5 | −5.8e-5 | 5.6058e-5 | 5.6e-5 |
| 33 | 161 | 3.6603e-4 | 3.7e-4 | −2.1987e-5 | −2.2e-5 |
| 33 | 353 | 8.2296e-4 | 8.2e-4 | −4.8531e-4 | −4.9e-4 |
| 39 | 7 (K) | −1.9304e-2 | −1.93e-2 | −8.4559e-3 | −8.5e-3 |
| 39 | 79 | 4.5817e-5 | 4.6e-5 | 1.6229e-5 | 1.6e-5 |
| 39 | 553 | −2.3276e-4 | −2.3e-4 | −1.0208e-4 | −1.0e-4 |
| 39 | 599 | 1.4952e-4 | 1.5e-4 | 1.3960e-4 | 1.4e-4 |

All values agree to the printed digits.

### 3.3 Top level D = h_p, full decomposition
**p = 11 (m = 33, D = 8119 = 23·353, ρ=(2,8)): fully exact except uu** (`logs/p11_full_decomp.log`). The four classes:

| class | Σu (all β of the class) | Σ\|u\| | max\|u\| |
|---|---|---|---|
| ii (iso/iso = lines + axes) | 0.016493 + 0.008231i | 0.01901 | 3.956e-4 |
| ui (unit mod 23, iso mod 353) | −9.83e-4 + 5.97e-4i | 6.00e-3 | 4.20e-5 |
| iu (iso mod 23, unit mod 353), exact, 126 896 reps | 0.02410 + 0.03408i | 0.1868 | 3.26e-4 |
| uu (sampled, 4000) | −0.0517 + 0.0010i (est.) | 0.738 (est.) | 5.5e-6 |

- The member mean ⟨E⟩ is exact over ii+ui+iu: 0.0164166 + 0.0081227i.
  - Adding the sampled uu mean shifts it by +7.2e-6 + 2.4e-5i.
  - The Ramanujan weights kill most of the large raw class sums: Y_mix enters ⟨E⟩ at −7.6e-5 − 1.1e-4i (iu) and −9.3e-7 + 4.1e-5i (ui).
- **Dev/main.** 0.0338759 (exact, ii+ui+iu) = |1+⟨E⟩|² − 1 (0.0331686) + Var (7.07e-4). Member ratios lie in [0.928, 1.149].
- **Dev/(φm) ≈ 0.069** (gas level h_p).
  - Compare the proper levels: 23 → 5.8e-5, 353 → 8.2e-4, 161 → 3.7e-4, i.e. ratios ~1200, ~84, ~190.
  - The K-level 7 (9.4e-3) is ~7×.
- **ρ = (−2,8)** (ii+ui): Dev/main 0.033298, ⟨E⟩ = 0.016481 − 0.008186i.

**p = 13 (m = 39, D = 47321 = 79·599).**
- ii exact; iu, uu sampled; ui sampled (4000).
- ⟨E⟩ = 0.019463 + 0.009759i; Dev/main 0.039331; Dev/(φm) = 0.1510.
- Proper levels: 599 → 1.50e-4 (~1000× smaller), 79 → 4.6e-5, 553 → −2.3e-4; K-level 7 → −1.93e-2 (~8×).

**p = 17 (m = 51, D = 1607521 = 103·15607).** Mixed classes sampled only: only iu (iso mod 103, unit mod 15607) completed, sampled with 3000 points. Its estimated contribution to ⟨E⟩ is 5.6e-8 + 7.3e-8i (vs 1.3e-4 for iu at p=11). The ui/uu runs died without output; local_set for q = 15607 needs a 15607² grid (memory), and this was not retried. The exact ii (~1e5 reps) was dropped because the box was shared with another heavy job.

**Conclusion for item (3) [N].**
- At every computed composite h_p, the contaminated quantities are 1–3 orders of magnitude below the gas Dev that drives B_p.
- The hp-divisor-level margin *grows* with p (90× → 1000×).
- Nothing points to |W′| ≥ cm being produced by bad levels. The 2p+1 family member p = 23 (h = 47·6771937) gives the proper-level value in §3.4.

### 3.4 p = 23, proper level 47 (m = 69) [N]
- Both signs at m = 69, D = 47: all 2208 nonzero β mod 47 (48 orbit reps) give |Ẑ(β)/Z_ρ| ≤ 6e-20 (`logs/prop/m69_s*_D47_a.npz`). That is at or below double-precision resolution, so the honest statement is |u| ≲ 1e-16 [N].
- Hence Dev_47/main_47 ≲ 1e-15, and Dev_47/(φm) ≲ 1e-6 even though main_47/(φm) = 6.1e8 (the level is included). The gas level is O(0.1).
- **Mechanism [H].** Every β ≢ 0 mod 47 has twists Tr(βλ^i)/47 in (1/47)Z, and ord_47(λ) = 23 = p [CA]. A nonzero β cannot have Tr(βλ^i) ≡ 0 at all sites, so the orbit carries non-resonant sites in each of the 3 periods and pays the step cost there. The quantitative per-site cost is the same open analytic input as in §5.
- The 2p+1 proper level shrinks from dev/main −7.9e-8 (p=11, d=23) to ≲1e-15 (p=23, d=47). It is the opposite of a counterexample family.

### 3.5 Line split and the parent's grok47 data [N]
- `code/linesplit.py` reproduces grok47 exactly:
  - p=11: cross 7.958057e-6, Binet 9.214829e-3.
  - p=13: cross 4.760439e-5, Binet 1.0894644e-2.
- **ℓ1 masses (new).**

| p | line | \|X\| | ℓ1 | \|X\|/ℓ1 |
|---|---|---|---|---|
| 11 | Binet | 9.2148e-3 | 9.4831e-3 | 0.972 |
| 11 | cross | 7.9581e-6 | 2.2843e-5 | 0.348 |
| 13 | Binet | 1.0895e-2 | 1.1211e-2 | 0.972 |
| 13 | cross | 4.7604e-5 | 7.6702e-5 | 0.621 |

**Answer to the parent's key question.** "Is X_line small because it is an average of η(a) over a rather than a max?" **No** [N].
- The cross-line sum is only 0.35–0.62 of its own ℓ1 mass. The smallness is in ℓ1, i.e. in every term: max|u| on cross lines is ≤ 2e-6, against 3.96e-4 on Binet lines (`logs/seam_profile_p1{1,3}.json`).
- This is the right kind of smallness to exploit, because Theorem L says no cancellation is available.

### 3.6 Lattice data [N]
- Cross-line lattices have shortest vectors equal to the Binet length (η-type, ℓ2 ≈ 2.4) only for p ≤ 17. From p = 23 they follow the Gaussian heuristic (3.4–4.2 for p = 23–43) (`logs/svp_lines.*`).
- The Binet lattices always contain η_s (ℓ1 = 4).
- The low-norm truncation captures Binet lines (9.212e-3 vs exact 9.2148e-3) but *not* cross lines (3.7e-6 vs 7.96e-6) (`logs/lownorm_*`). Cross-line mass is spread over many orbits.
- **Consequence.** Exact cross lines at p ≥ 23 (~6.9e6 orbit reps per line, ~20 CPU-days) are infeasible here. I did not extrapolate.

---

## 4. Structural results

**Notation.**
- O = Z[√2], ε = 1+√2, λ = ε². h = h_p squarefree, with 𝔞 | h of norm h (a "line"), 𝔞 = γ₀O (class number 1), and O/𝔞̄ ≅ Z/h.
- λ^p ≡ 1 mod 𝔞̄ [P, grok47], so ε^p ≡ s mod 𝔞̄ with s ≡ σ_𝔮 ∈ {±1} at each prime 𝔮 | 𝔞̄.
- 𝔞̄_± = ∏_{σ_𝔮=±1} 𝔮, d_± = N𝔞̄_±, and d₊d₋ = h. A line is **Binet** iff min(d₊,d₋) = 1, and **cross** otherwise.
- **Points.** β = γ₀c (c ∈ O/𝔞̄). Twists: Tr(βλ^i)/h = ±Tr(cλ^i/γ̄₀) mod 1. The resonant boxes are twist ≈ 0 and ≈ ½; the ½ box corresponds to c ↦ 2c.
- **Height.** For a class x mod 𝔞̄, G(x) = min{max(|ρ|,|ρ′|) : ρ ≡ x mod 𝔞̄}.
- **Primitive.** c is primitive if c ∉ 𝔮 for every 𝔮 | 𝔞̄.

### 4.1 Binet generator [P] + [CA]
- η_s := ζ − 1 − 2sζ^{(p+1)/2} ∈ Z[ζ_p] generates the Binet lattice 𝔄_s. Reason: λ^{(p+1)/2} ≡ sε in the cyclotomic model, so η_s ∈ 𝔄_s, and N(η_s) = Φ_p(sε)Φ_p(sε̄) = h = [Z[ζ]:𝔄_s].
- Exact resultants give |N(η_s)| = h_p for every prime 5 ≤ p ≤ 73, and N(η₊η₋) = N(ζ²−6ζ+1) = h_p² (`code/eta_norm.py`, `logs/eta_norm.json`).
- η_s is a 3-site ε-local polymer. This is the arithmetic origin of the Binet gas (N11 coding lemma).

### 4.2 Lemma S (antipodal windows on cross lines) [P]
**Statement.** Let 𝔞 be a cross line and c primitive. Then for every n ∈ Z:

  G(cε^n) + G(cε^{n+p}) ≥ √max(d₊, d₋).

On a Binet line, G(cε^{n+p}) = G(cε^n) for all c, because ε^p ≡ ±1.

**Proof.**
1. Let ρ₁ ≡ cε^n and ρ₂ ≡ cε^{n+p} ≡ s·cε^n (mod 𝔞̄) be minimal representatives.
2. Then ρ₂ − ρ₁ ≡ (s−1)cε^n ≡ 0 mod 𝔞̄₊, and ρ₂ + ρ₁ ≡ (s+1)cε^n ≡ 0 mod 𝔞̄₋.
3. At a prime 𝔮 | 𝔞̄₋ we have ρ₂ − ρ₁ ≡ −2cε^n ≢ 0, since c is primitive and 2, ε are units mod 𝔮. So ρ₂ − ρ₁ ≠ 0 (here d₋ > 1 is used). Likewise ρ₂ + ρ₁ ≠ 0, using d₊ > 1.
4. Hence d₊ | N(ρ₂−ρ₁) ≠ 0 and d₋ | N(ρ₂+ρ₁) ≠ 0.
5. But |N(ρ₂ ± ρ₁)| ≤ (G₁ + G₂)², so (G₁ + G₂)² ≥ max(d₊,d₋). ∎

**Remarks.**
- The non-primitive points c ≡ 0 mod 𝔞̄₋ are the "axis" classes. They are level-d₊ objects; grok47 notes the primitive vs incl.-axis line values differ by < 3e-7.
- max(d₊,d₋) ≥ √h *always*. So no factorisation of h_p, not even 2p+1 · (rest), makes this bound weak.

**Exhaustive check [N]** (`code/lemmaS_check.py`, `logs/lemmaS_p*.json`). Q = min over primitive c and n of max(G(n),G(n+p)), compared with the guaranteed √D/2:

| p | D | Q (cross) | Q/√D (cross) | Q (Binet) |
|---|---|---|---|---|
| 11 | 353 | 15.24 | 0.811 | 1 (vacuum c=1) |
| 13 | 599 | 21.80 | 0.891 | 1 |
| 17 | 15607 | 68.00 | 0.544 | 1 |

At p = 17, Q/√D = 0.544, close to the proved 1/2, so Lemma S is nearly sharp there.

**Corollary S′ [P-sketch].** Gap: the ε-window ↔ height dictionary below is standard Bowen-box bookkeeping and has not been written out with constants.
- A resonant window (consecutive λ-sites with twist within δ ≤ 1/20 of one background) centred at ε-position n has λ-length ≤ p/2 − 2log_λ G(cε^n) + O_δ(1). The continuation is forced because nonzero elements of 𝔇⁻¹ have |N| ≥ 1/8.
- Hence two antipodal windows on a cross line have total length ≤ p − log_λ max(d₊,d₋) + O(1) ≤ 3p/4 + O(1).
- On a Binet line the vacuum c = 1 has all p sites resonant: core count = p at δ = 1/8 for some point, and the Binet gas is 2[(1+Λ)^p − 1].
- Exact twist statistics (`logs/twist_core_*`) illustrate the deficit. At δ = 1/200 the max core count is Binet 2/4/8 vs cross 2/3/5 for p = 11/13/17. These small p are dominated by chance coincidences, so this is an illustration only, not evidence.

### 4.3 Polymer gap for seam-bridging defects [P]
- Let f(ω) = Σ_{k=0}^{K} a_kω^k (|a_k| ≤ A) be an ε-local element of the cross lattice 𝔄_c = gcd(η₊,d₊)·gcd(η₋,d₋) ⊇ (η₊η₋).
- If f is not divisible by η₊η₋, then f(ε) ≠ 0 or f(−ε) ≠ 0. Say f(sε) ≠ 0 with the relevant sign, so 𝔞̄_± | f(sε) ⟹ d_± ≤ |N f(sε)| ≤ (CA)²ε^K.
- So K ≥ log_ε(min(d₊,d₋)/(CA)²).
- **Meaning.** A cross line can avoid the seam of Lemma S only through a polymer of ε-span ≥ log_ε min(d₊,d₋) − O(log A).
  - With a per-site activity decay r this gives |X_cross| ≲ poly(p)·min(d₊,d₋)^{−γ}, with γ = log(1/r)/log ε. This is grok47's empirical power law; the reduction from X_line to polymers is [H].

### 4.4 H5(b) exponential sufficiency [P]
- #lines ≤ 2^{ω(h_p)} = e^{o(p)}. So any uniform bound |X_line| ≤ Ce^{−cp} on cross lines with c > ln2·w_max(p)/p closes H5(b) for p ≥ p₀.
- At p = 3307 (w_max ≈ 228) this needs c > 0.048.

---

## 5. Assessment: which route, and what would make it a theorem

- **Route (3), counterexample.** **Not supported** [N].
  - All exactly computed contaminated quantities are 90–1000× below the gas at hp-divisor levels, and the margin grows with p.
  - The only same-order term is the K-level 7 (|Dev| ≈ gas/8). That is unrelated to h_p's factorisation and already part of v5's bookkeeping.
  - The 2p+1 family gives no anomaly at p = 23 level 47 (§3.4).
  - I see no mechanism producing |W′| ≥ cm from bad levels. It would need X_cross or Y = Θ(1) at level h_p, and every exact data point is ≤ 5e-5 (X_cross) or ≤ 1.1e-4 (Y in ⟨E⟩).
- **Route (2), harmlessness.** Positivity, sign, monotone and weaker-target arguments are dead [P no-go]. The **pointwise route** (§4) is alive and is the more promising of the two. What would make it a theorem:
  1. **(Seam cost.)** A bound, in the N11 polymer expansion (§1 there, exact identity [P mod Line F]), on the activity of polymers that cover λ-sites with twist outside the resonant boxes: ≤ C·r^{(#sites)}, with r < 1 and a *usable prefactor*.
     - This is the same missing item as N11 §2/§5(ii): an adapted norm with O(1) constants. The step-norm sup bound 1.2744/1.9155 = 0.665 per period-site (×3 periods → 0.29 per λ-site) is the natural candidate rate.
  2. **(Counting.)** A Bowen-type count of points with a given window pattern on a line, i.e. the coding lemma (N11 §3) extended from the closed Binet circle to the cross circle.
     - The cross circle is closed but carries the sign defect s. Lemma S says every primitive configuration contains a seam of ≥ log_λ max(d₊,d₋) − O(1) λ-sites *or* a bridging polymer as in 4.3. The two-window case is [P]; more windows is [C].
  3. **Then.**
     - The vacuum-type part of X_cross is ≤ e^{p·ReΛ}·r^{log_λ max(d₊,d₋)} ≤ e^{−c p} with c ≈ (ln(1/r))/4 ≫ 0.048, using max ≥ √h. This holds for every factorisation, so §4.4 applies.
     - The bridged part is ≤ poly(p)·min(d₊,d₋)^{−γ} with γ = log(1/r)/log ε. It meets grok47's γ* thresholds (0.8737 absolute, 0.9909 × M, binding at p = 3307) iff r < ε^{−0.99} ≈ 0.418 per ε-site.
     - Data [N]: the cross/Binet max-term ratio per seam λ-site is ≈ 0.1–0.23 (p = 11, 13; computed from max\|u\| cross/Binet over log_λ D). That is per ε-site ≈ 0.33–0.48. This is **borderline** against 0.418, so I do **not** claim a margin. [C]
  4. **The Y part** (mixed/partial classes at level h_p) is not addressed by Lemma S. Data: it enters ⟨E⟩ at ≤ 1.3e-4 (p=11 exact). It still needs v5's (b′)/H5(a). Unchanged.

**Net.** The smallness of bad-line contributions has a proved arithmetic cause: Lemma S plus the polymer gap. It is pointwise, which matches the no-cancellation Theorem L. What is missing is analytic (seam-site cost with usable constants, plus counting), and it is the same kind of input v5 already assumes as H1/(I)/(T).
- The Mersenne ceiling survives only in the bridged part, and only if the seam-polymer decay rate is slower than ε^{−0.99} per site.

---

## 6. Files
- **code/**
  - level.py, analyze.py, final_analysis.py — I2′ level decomposition.
  - run_main.sh, run_tail.sh, run_proper.sh — queues.
  - validate_m15.py, kconv.py, timing.py, zfast.py.
  - linesplit.py, lownorm.py, svp_lines.py.
  - twist_core.py — exact core statistics.
  - seam_profile.py, lemmaS_check.py — Lemma S.
  - vacuum.py — small-cofactor points.
  - eta_norm.py.
- **logs/**
  - validate_m15.*, kconv_m33.log
  - lvl/ (top-level npz + run.log), prop/ (proper levels), final_levels.json, p11_full_decomp.log
  - linesplit_p11/13.json, lownorm_p11_T*.json, svp_lines.*
  - twist_core_p*_d*.json, seam_profile_p11/13.json, lemmaS_p*.json, vacuum_p11_NC40.json, eta_norm.json
- **Reproduce.** `/workspace/lineNgas/venv/bin/python` (python-flint, numpy, sympy). twb/L2 law are read-only from /workspace/bgs-lineN/N6 and /workspace/bgs-lineL/L2.
