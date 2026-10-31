# Referee report — Lines N12b (+REPORT_N11b_v2) and N13 (+REPORT_N12_v2), combined
Referee: Grok Bot · 2026-11-01, 00:45–00:56 Asia/Yekaterinburg (UTC+5).
Nothing in the authors' trees was modified, and nothing was pushed. All my jobs ran at nice 19 with OMP=1, next to the live N13 replay.

**Integrity**
- N12b: SHA256_N12b.txt verifies, and its self-hash matches.
- N13: SHA256_N13.txt self-hash matches, but **NOTES_N13.md FAILS**. Its mtime is 00:44:00.053, 4 ms after the manifest, and the last line ("00:44 hashes written") was appended after hashing. The replay jsonl/out files are excluded by design (they are live).
- N10b: SHA256_N10b_v2.txt self-hash is 92a8bd0e…5b164 ✓.

## Verdicts
- **N12b: READY after minor fixes.** I confirm the negative result independently and robustly: the D1 + G*_gas route is dead. In fact it is dead more broadly than claimed, for every box size θ ∈ [1/16, 1/4], not only θ = 1/8. The cone-infeasibility estimate is an honest [N]/[H] cost estimate tied to one design.
- **REPORT_N11b_v2: accepted.** F1–F5 are all satisfactory. The NOTES_N10b timestamp fix is correct.
- **N13: READY after fixes.** Required: N13-F1 (Lemma D constant), N13-F2 (quadratic-sup step and the 4253 vs 4.26e3 wording), N13-F3 (replay radius statement and final f_post). The arb norm certificate, the 2×2 argument, the absolute-sum obstruction and the ℓ³ ≤ ℓ² step are all correct.

## Part 1 — N12b

### 1a. Periodic-orbit lower bounds (the key negative claim)
**How I checked.** Own code, `code/ref_perL.py` and `code/ref_perL_all.py`, with logs in `logs/`:
- my own orbit iteration (x, y) ↦ (y, 6y − x) mod D;
- my own enumeration of the periodic lattice;
- my own box-run statistic;
- rates ρ(∏)^{1/n}, normalised so that the slow fixed point gives μ*.

**Three operators agree to ≈1e-9.** The table below compares the Line-F lifted operator with N12b's parameters, a refined Line-F truncation (K0 = 4, K = 32, N0 = 14), and the **N6/N12 cert_core sector-4 operator (495-dim)**:

| orbit (seed / D) | n | max box run (θ=1/8) | Line-F default | Line-F refined | N12 core |
|---|---|---|---|---|---|
| (6560, 0)/6724 | 5 | 2 | 1.4336168 | 1.4336168 | 1.4336168 |
| (408, 72)/1152 | 4 | 2 | 1.4295636 | 1.4295636 | 1.4295636 |
| (1128, 984)/1152 | 4 | 1 | 1.3426207 | 1.3426207 | 1.3426207 |
| (28, 0)/196 | 3 | 0 | 1.2624293 | 1.2624293 | 1.2624293 |
| (410, 82)/6724 | 5 | 3 | 1.5096448 | 1.5096448 | 1.5096448 |

**Full table recomputed.** For n ≤ 6 the θ = 1/8 table of Γ_per(1/8, L) reproduces N12b exactly: 1.2624 / 1.3426 / **1.4336** / 1.5117 / 1.5683.

**Exact T′.** T′ ∈ (1.42785, 1.42786) (Lean: Tp_lower, Tp_upper). Both L = 3 witnesses exceed it: 1.43362, and 1.42956 (Lean: orbit_n4_above_Tp). The margins are 0.40% and 0.12%. Truncation stability is 1e-9, so numerically this is robust. It is still [N], not [CA].

**Box conventions.** Using the union of the four boxes around {0, ¼, ½, ¾} (the G*_gas definition) instead of the (0,0) box leaves the runs of all witnesses unchanged.

**Robustness in θ (new).** Γ_per(θ, L=3) (n ≤ 6):

| θ | 1/16 | 3/32 | 1/8 | 5/32 | 3/16 | 1/4 |
|---|---|---|---|---|---|---|
| Γ_per(θ, L=3) | 1.4336 | 1.4336 | 1.4336 | 1.4296 | 1.4296 | 1.4296 |

All exceed T′. The n=4 witness keeps its box run at 2 for every θ ∈ [1/16, 0.354), so **D1 with a minimum stay length L ≥ 3 is false for every box radius in that range**, not just θ = 1/8. Shrinking θ only makes it worse.

**Is this a false negative?** No. A periodic orbit's per-period spectral rate is a lower bound on the sup growth rate in any norm. This is the correct direction for refuting D1.

What is killed is precisely the *sup-rate D1 + gas factorisation*. The underlying sums are not killed: N12b says so itself, and that is correct.

### 1b. Fugacity bookkeeping
- **The z(L) formula is correct:** Σ_{ℓ≥L}(1+ℓ)q^ℓ = q^L[(1+L)/(1−q) + q/(1−q)²]. I recomputed N12b's 0.83 (L=1) and 0.26 (L=2).
- **But they evaluate q = μ*/(λΓ) at Γ = Γ_per(L).** That is a *lower* bound on Γ, so it overstates z. For a negative claim, the right choice is the most favourable admissible Γ (→ T′, q ≥ 0.23016).
  - That gives z/K > 0.687 (L=1) and > 0.2269 (L=2).
  - The rank-p requirement z < 2.08e-4 then forces **K < 3.03e-4 (L=1) and K < 9.17e-4 (L=2)**.
  - N12b had 2.4e-4 and 7.6e-4. The conclusion is unchanged (Lean: q_lower, zL1, zL2, K_L1, K_L2, z_req).
- **Notation:** N9b_v2 defines z with C²C_θ, while N12b writes K = C·C_θ. Harmonise.
- **"K ≳ 1"** is [N]/[H], not proved. An independent supporting heuristic: at θ = 1/8, box visits have density ≈ (2θ)² = 1/16 per site, and each carries a factor ≥ ~μ*/Γ > 1. A per-site gas cost below 2e-4 would therefore need per-visit charges ≪ 1, which is incompatible with N_H ≥ 1.
- **Verdict:** the L ≤ 2 branch fails, and the L ≥ 3 branch fails D1. G*_gas is not attainable (θ ∈ [1/16, 1/4]).

### 1c. Cone-certificate infeasibility
- The arithmetic checks out: 1/1e-5 × 1/3e-4 ≈ 3.3e8 cells, at 0.2 s each ≈ 2 CPU-years.
- It is an [N]/[H] estimate for *this* cell design: uniform cells, a stable-direction resolution of 1e-5 driven by the past-dependence of the cone direction. I find no error.
- Note that it is moot for the gas route, since D1(L ≥ 3) is false. D1 at L = 1 (Γ_out(1/8) ≥ 1.2624) remains open but is useless without a viable gas.
- The §4 restricted-pressure proposal is [H] and correctly labelled.

### 1d. NOTES_N10b fix and REPORT_N11b_v2
- **NOTES_N10b.** The diff against the preserved original shows only heading relabels plus an appended ERRATUM. Every cited mtime matches `stat`: 23:03:25, 23:05:49, 23:10:08, 23:10:28, 23:13:31, N11 note 23:10:42, 23:16:30. Since then, only NOTES_N10b.md and the v2 manifest have changed. ✓
- **REPORT_N11b_v2 F1–F5:** all ✓.
  - The rounding artifact is withdrawn.
  - 2h·q_u is fixed, and k = O(1) stays is labelled [P-sketch].
  - The C′ prefactor is stated as e^{o(p)} for p ≥ p₀, with p₀ not computed (honest).
  - The exact sums are cited for p ≤ 7.
  - The unit gas is now a cross-check.
  - The mixed class stays conditional on G*, which is now reformulated (§4).

**N12b fixes**
- F1: give the θ-robustness (or at least note it); it strengthens the claim.
- F2: evaluate q at Γ → T′ (numbers above), and harmonise C²C_θ with K.
- F3: label "K ≳ 1" [N]/[H].
- F4 (optional, if the kill is to be cited as a theorem): arb-certify ρ(P₄) and ρ(P₅) for the two witnesses, plus core→true.

## Part 2 — N13

### 2a. arb adapted-norm certificate [CA] ✓
- Defining H := T*T exactly in arb is a sound design.
- The results V1 (cond ≤ 21.103), V2, V3a, V3b at η = 1e-6 are consistent with my N12 arb replay (cond ≤ 21.062 for the float H).
- Float cross-check (`ref_lip_float.json`):
  - float Lip_H = 167.197, L2 = 4977.09, Nsum = 8.32795;
  - certified 167.213 / 4977.59 / 8.32878;
  - every certified c_n ≥ the float ‖M_n‖_H, with c_n/float = 1.0001 (designed margin). ✓

### 2b. Quadratic bound via the 2×2 argument — the argument is correct; one step needs a proof
I re-derived it line by line:
- v = aΦ + q;
- the row bounds for nP|ψw| and ‖Q̃w‖, using ψQ̃ = 0, Q̃A0 = A0Q̃ and V3a/V3b for ‖Q̃MQ̃‖ ≤ κ(1+η)²;
- the Taylor remainder ‖R‖_H ≤ L2t²/2;
- the Pythagoras defect: â² + ‖q‖² ≤ 1 + 2g‖ψ‖_*, and ‖w‖² ≤ X/(1 − 2g‖ψ‖_*);
- monotonicity of the nonnegative 2×2 norm in its entries.

All valid. The first-order term vanishes up to ε₀ = 5e-16 (‖ψE1Φ‖), and Lip·|1 − ψΦ| ≈ 3e-14 gives a negligible linear term.

Gaps:
- **(i) The grid-sup step is not a proof.** "C2 = max of coef over a 400-point grid" does not bound the continuum. I closed it rigorously (`ref_quad_partition.py`, arb at prec 200, with N13's certified scalars as inputs):
  - on a geometric partition (ratio 1.0005, 30,364 cells from 1e-9 to 1/256), monotonicity gives N_H(t) ≤ 1 + 1.01e-12 + **4260**·t² on [0, 1/256] ✓;
  - with C = 4253.4 the same check fails (partition slack). **So state 4.26e3, not 4253.4.**
- **(ii) A tiny omitted defect.** t·|1 − ψΦ|·b₁ ≈ 1e-17·t is not in τ₁. It is absorbed by the 1e-12 safety factor, but should be stated.

### 2c. Lemma D (mid-gap cut)
**What is correct:**
- **Superposition.** Twists are linear in the seed, and shifting a seed by λ^G shifts the index by G. So d_t = d^i_t + s·d^{j′}_{t+G} mod 1 exactly ✓. Tr ∈ Z isn't even needed beyond that.
- **The Q̃ term.** ψR_iQ̃L_jΦ ≤ Y_i X_j, with 0.45^{D} per side via ψ(A0/s)Q̃ = 0 and V3b ✓. With background tails, Y(D+1) ≤ 0.45(1+η)Y(D) + Ψ·Lip|d|, so the continuation beyond KK is a genuine [P-sketch] that can be completed.
- **Twist tails decay at λ^{−1/2} per unit G** ✓. At the mid-gap, the other bump's tail is ≈ a·λ^{−G/2}; the tail sums Σ_{t<−D}|d^i_t| = a₁λ^{−D−1}/(1 − 1/λ) are correct.
- **The rate** max(0.45, 0.414) = 0.45 is right (Lean: rateD).

**What is wrong (N13-F1, required — constant, not structure).** The cross term bounds ‖ψ dR‖ by Γ(e^{σ} − 1). The telescoping expansion of ∏(B + E) − ∏B gives Σ_{S≠∅}∏(sub-products)∏‖E_k‖. For E_k located *inside* the other bump's core, a first-order term carries two core sub-products, i.e. up to best²·outside rather than Γ = best·outside. Higher orders give Γ(e^{Γσ} − 1).
- Correct form: ‖ψ‖_*·Γ(e^{Γσ} − 1), with ‖ψ‖_* = 1 (I checked).
- Γ ≈ 1.9–3.1 here, so the tail grows by ≲ 3×: 5.76e-9 → ≲ 2e-8. This is immaterial.
- Independent validation at G = 16 (N13 bound vs N12's measured devs, 100 pairs): bound ≥ measured everywhere, min ratio **1050×**. At G = 10, N13 reports 1891×.

### 2d. Structural claim: absolute sums cannot fit ✓ [P] for the stated form
- Σ_types|w| = 4.2937e-4 per sign. Doubled for ±e (equal weights, by the N11b invariance), that is 8.59e-4 per site, which exceeds Re Λ_lo′ = 6.234e-4 and is consistent with |Λ| = 8.36e-4 (Lean: abs_vs_budget).
- Summing |weights| over all configurations containing a bad cluster gives ≥ p·A_bad·(1 + 8.6e-4)^{p−1}. That outgrows 2(1 + Re Λ)^p by e^{2.4e-4p}.
- So (T) must be a per-site activity / Kotecký–Preiss statement. Correct.
- Note: the replacement condition "A_bad < Re Λ_lo′ − δ_int" is the right shape, but the KP constant (the e^{a|γ|} weights and the log → modulus conversion) still needs to be written out: [P-sketch].

### 2e. Σ|w| ≤ (Σ|r_A r_B|²)^{3/2}: valid, and the direction is correct
- This is ‖x‖₃ ≤ ‖x‖₂. Formalised in Lean (`l3_le_l2`: (Σx³)² ≤ (Σx²)³, via Cauchy–Schwarz plus x_i² ≤ Σx²). No sup or operator-norm factor is needed. ✓
- The cost is a factor N^{1/2} relative to an i.i.d. third moment. It is still summable under λρ² < 1: λρ² = 0.4331 and (λρ²)^{3/2} = 0.285 per n (Lean: shell_rate).
- ρ(𝒦) = 0.27255 and the i.i.d. model are [N]/[H], correctly labelled. The usable statement is still the open cluster-language second-moment certificate.

### 2f. Replay spot-checks
- `ref_replay_spot.json`: 15 windows recomputed in float with my own twist and seed code (30 enclosures, A and B per window):
  - singles k = 0, 3, 5, 9;
  - odd+odd at G = 3, 4, 9, 15 for s = ±1;
  - odd+sq2 at G = 3–5.
- **All 30 float values lie inside the arb boxes** ✓.

**N13-F3 (required).** Relative ball radii grow by ≈ 2.9× per G from wrapping:

| G | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|
| max rad/\|r\| (253 jobs done) | 0.9% | 2.5% | 7.1% | 20% | **59%** |

The 59% is for odd+four. §7's "≈1.5% at G = 13" understates this. Certified dev upper bounds for G ≥ 14 are essentially vacuous: they bound |W_ij| + |W_iW_j|, not the deviation.
- This is still harmless for the budget, since all coded |w_i||w_j| summed is ≪ 6e-4.
- But the final [CA] δ_int must be quoted from the completed f_post (expected ≫ 6.99e-7), or the suggested mid-rad / H-norm error-propagation rerun must be done for G ≥ 12.
- Composite core→true conversion is still open (acknowledged).

### 2g. REPORT_N12_v2
- F1–F5 are accepted and addressed as described. The erratum that the N12 best cut was t = 0, which made N12's tail a pure assumption, is correct and honest.
- F4's sentence "for p ≥ 75 the wrap gap exceeds 16 λ-steps whenever ≤ p/7 bumps are present" is unclear and does not follow as stated: few bumps do not force every gap to be long. Replace it with "all statements use circular gaps".

**N13 fixes**
- F1: Lemma D cross-term constant (Γ² / e^{Γσ}).
- F2: quadratic sup via partition, quoted as 4.26e3.
- F3: radius statement; final certified δ_int from the completed replay (or a mid-rad rerun).
- F4 (minor): rehash NOTES_N13.md; fix the F4 wrap-gap sentence.
- F5 (minor): label "(ii) removes the barrier" as conditional on the second-moment certificate.

## What remains for an unconditional refutation (updated)
1. **Gap (b), mixed class.** The D1 + gas route is closed negatively (N12b, confirmed, any θ ∈ [1/16, 1/4]). It needs a new formulation, e.g. the restricted-pressure / transfer certificate (N12b §4 [H]), with short box visits carrying true weights. Nothing exists yet.
2. **(T)** in per-site KP form:
   - the cluster-language second-moment certificate (N13 §4.4);
   - certified activities for the 200 short types (in the replay queue);
   - deep wrap-around points via whatever replaces G*.
3. **(I)**:
   - the completed replay with a tight [CA] δ_int (fix the radius growth);
   - composite core→true conversion;
   - Lemma D with corrected constants, and single-chain norms / Γ in arb.
4. **Step norms** for |t| > 1/256 in arb (the table is still [N]), if any route needs them.
5. **Arithmetic inputs:** explicit C′ / p₀; rigorous k = O(1) stays; the R₄ automaton.

## Artifacts
All paths are under /workspace/audit/lineN13.
- **code/**
  - ref_perL.py, ref_perL_all.py
  - ref_quad_partition.py
  - ref_replay_spot.py
  - ref_lip_float.py
- **logs/**
  - ref_perL.json, ref_perL_all_n6.json, ref_perL_all.out
  - ref_quad_partition.json
  - ref_replay_spot.json
  - ref_lip_float.json
- **lean/LineN13Arith.lean**: built with the lineN12 project (mathlib cache). Exit 0, unused-variable warnings only, no sorry, no native_decide. Log in lean/build.log.
