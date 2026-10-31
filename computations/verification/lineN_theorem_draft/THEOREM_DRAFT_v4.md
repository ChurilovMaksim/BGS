# THEOREM_DRAFT v4 — conditional refutation of frozen R′ (TRACE-206) along m = 3p (Theorem R♯ path, modulus form)

*v4: Line N19b, 2026-11-01 (Asia/Yekaterinburg, UTC+5). v4 = v3 + referee lineN16 §4 edits E1–E7 (verbatim) + N16 referee minor notes (N16-1…N16-4) in the H1/H4 rows; see §10. v1, v2, v3 kept unchanged.*

*Repo copy (integration, 2026-11-01): one owner wording fix. In the §2 p₁ row and the §3 crossover row, the file reference "N18b a_crossover_v2.py with robin() corrected/fixed" now reads "N19b a_crossover_v3.py (robin() corrected; v2 in N18b had the bug)". The author original has sha256 6d6c88ed…616207 (/workspace/bgs-lineN/THEOREM_DRAFT_v4.md); the change is recorded in evidence/executions/20261101/lineNgas/README.md.*

*v3: Line N18b, 2026-11-01 (Asia/Yekaterinburg, UTC+5).*
- **Applies:** referee lineN15 §3 items 1–20, plus the N15 items affecting the draft (N15-F1, N15-F2, N15-F3). It also incorporates N16 §3 (gap (a) status table) and REPORT_N17b_v2 (N18b).
- **Kept unchanged:** v1 (THEOREM_DRAFT.md) and v2 (THEOREM_DRAFT_v2.md). The v2 → v3 changes are in §9.
- Nothing pushed.

**Plain summary.**
- **Nothing that refutes R′ is proved.** We prove a set of structural lemmas, certified constants and negative results (§3). Together they reduce a refutation of frozen R′ (W′_m = o(m)) along m = 3p to explicit open inputs H1–H8 (§2), and the reduction is bookkeeping.
- **The inputs are far from done.** The hardest are:
  - the collision lemma (H1), currently [H] with a ≈186× numerical margin;
  - the correlated core→true conversion and the G > 15 true-functional interaction tail (H4);
  - the composite-h_p mixed classes and cross lines (H5);
  - signed control at levels other than h_p (H7*), which is needed even when h_p is prime.
- **Restricting to prime h_p does not avoid this.** It removes H5 but not H7* (K_p levels), and the infinitude of prime h_p is itself open (⇔ ¬R_NSW).
- **Small-p evidence is numerical only.** Exact-enumeration W′ tables exist for m ≤ 17 (p ≤ 5); level data at m = 21, 33, 39 (p ≤ 13) come from the I2′ formula. All of it is [N] and is not evidence for the asymptotic statement.

**Labels.**
- [P] proof written out and refereed (or elementary).
- [P-sketch] argument complete in outline.
- [CA] rigorous arb/interval.
- [CA-fp] IEEE binary64 with derived a-priori rounding bounds under the stated model (IEEE standard model + libm ≤ 1 ulp).
- [CA*] float certificate reproduced, not interval.
- [N] numerics without error control.
- [H] hypothesis/heuristic.

## 0. Status
- **Frozen R′ is not refuted**, unconditionally or at any single p. The conditional statement is Theorem R♯-mod v3 (§2).
- **No input is routine.**
  - H6 contains, besides an explicit p₀ for C′, the squarefreeness of h_p. That is a Wieferich-type open question (N3-F8).
  - H4 currently has **no working route**: the H-product route is vacuous (N15 §5, GA 40–340). The vector-chain conversion works numerically per window, but it cannot control the G > 15 tail without a pair-minus-product difference form (N16 §2).
- **H7 is serious** (N17b/v2). W′ is a plain signed sum; the inclusion threshold excludes no (±2,8) level for m ≥ 15 (TRACE-273); and K_p levels, including prime powers, survive for prime h_p.

## 1. Objects (pointers only)
- **Map.** Kicked quantized cat map, λ = 3+2√2 = ε², ε = 1+√2. h_p are NSW numbers, λ^p ≡ 1 (mod h_p); h_{3p} = h_p·K_p, K_p = 4h_p² + 3, 7 | K_p, gcd(h_p, K_p) | 3.
- **Deviation.** W′_m (TRACE-206) = NR part + φ⁻¹Σ_{ρ,d incl} Dev_d(ρ) (TRACE-213). NR ≥ −RMT ≥ −4m.
- **Level-h_p sum.** φ⁻¹Dev_{h_p} ≥ S_ρ·(n/h_p)·(|1+X+Y|² − 1), S_ρ := φ⁻¹|Z_ρ|²/h_p (N6 §0.8, N11b §1):
  - X: isotropic sum. At composite h_p, X also contains the 2^{ω(h_p)} − 2 **cross lines** (N7-F6), which the gas does not code.
  - Y = Y_U + Y_mix + partially isotropic points.
- **Gas.** X_coded = 2[(1+Λ)^p e^{pΔ} − 1] − (dense part) (N11 §4). The lower bound used is |1 + X_coded| ≥ 2(1 + Re Λ_lo′)^p e^{−pδ} − 1, **not** with (1 + Re Λ − δ)^p (N11-F4).

## 2. Conditional main theorem (draft)
**Theorem R♯-mod v3 (draft) [P mod inputs H0–H8, assembly; v2 bookkeeping checked by referee lineN15 item 20, v3 not yet refereed].**
Let p be prime, m = 3p, p ≥ p_thr := max of the thresholds listed below. Assume H0–H8 at p. Put

  B_p := (n/h_p)·[(2(1+Re Λ_lo′)^p e^{−pδ} − 1 − |X_tail| − |X_cross| − |Y| − e^{−0.28p})² − 1] − I_p − ε_16 − ε_fl − ε_other,

- δ := the **true-functional** interaction constant, all G. What is known:
  - G ≤ 15: ≤ 2.470e-6 [P-sketch lemma + CA-fp numerics, N16];
  - G > 15 true tail: **OPEN** (H4);
  - for comparison only, the core functional: δ_int^core ≤ 5.14476e-7 [CA-fp] + core tail ≤ 1.56e-8 (Lemma D).
- Re Λ_lo′ = 6.234e-4.
- I_p := σ(K_p)/K_p − 1 ≤ e^γ ln ln K_p + 0.6483/ln ln K_p − 1 (Robin 1984, Thm 2).
- ε_16: the (±2,16) contribution (N7). ε_fl: floors of levels d ≥ L_fl. ε_other: H7* levels.

Then W′_{3p}/m ≥ −4 + m⁻¹Σ_{ρ=(±2,8)} S_ρ·B_p with S_ρ ≥ c·1.13287^m (TRACE-271; μ²/ε^{4/3} = 1.1328794). So if B_p ≥ κ > 0 for infinitely many p, W′_{3p}/m → ∞ and frozen R′ (W′ = o(m)) is false. Only B_p ≥ κ is needed (N17b_v2 §2).

**Thresholds (p₀-list; item 4):**

| threshold | value | status |
|---|---|---|
| C′ effective e^{o(p)} | p₀^{C′} | not computed (H6) |
| Prop X′ certified errors | p ≥ 1289 | a choice (N8-F5) |
| ε₁₆ (N7 two-term B16 form) | p ≥ 339 (crude form: 498, N7-F1) | [CA]+[P] |
| TRACE-227 | m ≥ 243 (p ≥ 81) | registered |
| TRACE-271 | m ≥ 495 (p ≥ 165) | registered |
| p₁: gas vs Robin (tails = Y = X_cross = ε = 0, n/h_p := 1) | all p ≥ 1386 (core δ) / 1390 (δ = 2.470e-6, G ≤ 15 part only; increases once the G > 15 tail is added); **first prime 1399** | [P-arith: float/mpmath evaluation + monotonicity] (N19b a_crossover_v3.py (robin() corrected; v2 in N18b had the bug); lineN16 §2a) |
| p₁ with all budgets | not computed | open |
| Theorem W (only if Weil coverage is invoked) | p ≳ 8.3e25 (m₁ uncomputed) | TRACE-252 |

**Gas vs divisor bounds [P-arith / P].**
- The gas growth beats the Robin bound on inherited levels for p ≥ p₁ under the stated idealization.
- It does **not** beat the unconditional τ(h_m) ≤ e^{Θ(p/log p)} (Nicolas–Robin 1983). So floors absorb only levels d ≥ L_fl ≈ 4τ(h_m)h_p/(G − I_p), and H7* is needed below.

**Hypotheses:**

| # | Hypothesis | Status / best partial result | Where |
|---|---|---|---|
| H0 | Standing package of N6 Theorem R♯ (Line F/J/J3/L16 trace representation; TRACE-197/199/207/212/213/228; Prop X architecture; n_cert) | taken as given; Prop X [P-sketch]; n_cert [CA] | N6 §5, N7 §0, N8 |
| H1 **(T)** collision lemma: lattice→collision reduction for shell sums with C ≤ 0.082 at J₀ = 12; plus the A_bad tail j > 12 | **OPEN, [H].** Proved: exact carry reduction (\|e\| ≤ 15 [P]; sharp \|e\| ≤ 14, 29 values, **633** reachable pair states, referee N15-F3) and the torus-mean identity [P]. [N]: carry sums with \|e\| ≤ 3 (n ≤ 6) and \|e\| ≤ 1 (n ≤ 12) equal the i.i.d. value to relative ≤ 1.7e-9 (≈1.35e-11 for n ≥ 5; reproduced without cancellation, lineN16); \|e\| ≥ 4 not computed ([H] negligible: isolated-carry entry weights 7e-3, 3e-8, 2e-15 for c = 1, 2, 3); N15's apparent prefactor non-convergence was an artefact of the share proxy (N16 §1). Labels (N16-1): the carry reduction and torus identity are [P]; the shell sums entering them are [CA-fp]. Missing: certified multi-step carry operators (phase-keeping certificate on 633 states) and box/aliasing constants of the Poisson step. Margin: collision constant C_emp 4.4e-4 vs 0.082 = **186×** [N] (the "≈150×" of v1/v2 was the N14 *budget* margin). Tail j > 12: 1.56e-8 is a **[H] placeholder** (N15-F1), not Lemma D | N14 §2, §6; N15 §3; N16 §1, §3 rows 13–17 |
| H2 **(I-core)** interaction, core functional | **met:** δ_int^core ≤ **5.14476e-7** [CA-fp; c3_mid, closed F14.1, confirmed lineN15 arb 5.1447502e-7] + Lemma D core tail G > 15 ≤ 1.56e-8 [P+N] | N15 c3_mid.py; N13/N14 Lemma D; audit lineN15 §1b |
| H3 **(KP)** polymer weight e^{a\|γ\|}, log→modulus | Explicit (N15 §4): a = 5.93e-6 at g₀ = 4, S₀ = 2.063e-6; S₀ + S₁/(1+g₀) ≤ a for g₀ = 2..6 (Lean kp_g2..g6); A_bad^KP + δ_int = 2.5774e-6 (kp_budget). KP criterion [P] (Kotecký–Preiss 1986, with the anchored-cluster corollary for the per-site log-correction: Ueltschi 2004, Fernández–Procacci 2007; N15-F2). Finite part [CA-fp]. Tail j > 12 = H1 ([H] placeholder). Background interplay and tail ℓ-weighting [P-sketch]. Polymer normalisation [P-sketch] | N15 §4, kp.py; N16 rows 8, 23 |
| H4 **(CT)** core→true conversion | **OPEN; now = "difference-form (pair-minus-product) conversion cancelling the per-step perturbation (dominant) and end-projector terms + G > 15 true-functional tail"** (lineN16 §5; N16-2: N16 §2's end-projector diagnosis is superseded). H-product route vacuous (N15 §5). Vector-chain conversion per window: E/\|r\| ≈ 2e-3 for singles, ≈ 8% (median) for pair windows, max 5.27 [P-sketch lemma (the written lemma must include the second-order dPi²·‖Q‖ term), CA-fp numerics], giving δ_true(G ≤ 15) ≤ 2.470e-6. Under box widening the G > 15 bound is flat (≈1.5e-7 per G), so it is not controlled. The pair-window error is dominated (≈93%) by the accumulated per-step core→true perturbation, so a difference-form conversion must cancel that term, not only the end-projector term (N16 §2; lineN16 §1). Single-core: ≤ 2.094e-8 relative [CA]+[P-sketch] | N13 (B), N15 §5, N16 §2, rows 18–20 |
| H5 **(composite h_p)** (a) mixed classes: (R-mix) E_{mixed,d} F_p ≤ e^{o(p)} d^c r₂^p, c < 0.387 uniformly in d \| h_p; (b) **cross lines**: the 2^{ω} − 2 further fully isotropic lines at composite h_p (in X, not coded by the gas) bounded within budget; (c) partially isotropic points. **Or** p ∈ 𝒫 = {h_p prime} (then (a)–(c) vanish) | OPEN. c_B = 0.7375 established at [P-sketch] (asymptotic, constants ignored), covering iso parts d ≤ 1.588^p. **p = 31** (h₃₁ = 424577·865087, balanced semiprime, θ_max = 0.250 < 0.262) is covered by this, **not** by 𝒫. Evidence c ≤ 0 [N]. No known theorem applies (N15b). (b) was omitted in v1/v2 (N7-F6; lineN10/11 item 4) | N13b, N14b, N15b, N16b, N7-F6 |
| H6 **(C′ inputs)** explicit p₀; h_p squarefree or conductor-q^a weights | C′ [P + CA* mod H6]. p₀ not computed. Squarefreeness open (Wieferich-type, N3-F8). The old "level 7h_p unit points" clause (N3-F9) is **subsumed** by the inherited-level floor I_p (7 \| K_p, so 7h_p = e·h_p), on or off 𝒫 | N2, N3, audit lineN3 |
| H7 **(levels ≠ h_p), precise form H7*** | For included d ∉ {h_p} ∪ {e·h_p}, d < L_fl = h_p^{1+o(1)}: \|Lin_d\| ≤ ε_d\|Z_ρ\|²/h_p with Σε_d ≤ κ₀, i.e. cross-correlation growth < T′ = 1.42785. **Covered:** d = 7 (TRACE-223, \|μ_{1:3}\| ≤ 1.2837144 [CA]; (±2,16) level-7 members via N7/TRACE-227, per the TRACE-215/217 caveat); inherited levels (I_p floor) [P]; d ≥ L_fl (floor) [P]; inclusion (TRACE-273). **Weil range:** OP proved (TRACE-244/251); Theorem W proved under standing inputs, non-vacuous only for p ≳ 8.3e25 (TRACE-252; m₁ uncomputed); extensions TRACE-280/281 (beyond-Weil non-empty only for p ≥ 10^264.5); composite conductors open (TRACE-282). **Covers nothing at realistic p.** **OPEN:** hp-div, mixed, and **all K_p levels including prime powers** (31² \| K₅, 7² \| K₇; rank 3p, TRACE-265). Floor analogue: Prop K2 (TRACE-238/275). Numerics [N]: non-h_p Dev small, mixed signs (REPORT_N17b_v2 §4) | N6 §5, N8b §8, N12b, N17b_v2 |
| H8 **(wrap)** deep wrap-around points of gap (a), composite h_p | prime h_p: reduces to H1 [P-sketch]. Composite: free (c = 0) if per-point weights are not d-amplified; otherwise need **c < 1.1718·ℓ₀/ln d = 0.6647·ℓ₀/log_λ d** (ρ̄_true = 0.28028; with ρ̄ = 0.30: 0.9678·ℓ₀/ln d = 0.5490·ℓ₀/log_λ d). Conditional on the subgroup second-moment lemma **and** H1 (q = (λρ̄²)^{3/2} from the ℓ³ ≤ ℓ² step). **Units:** N14 §3's "0.97·ℓ₀/log_λ d" mixes ρ̄ = 0.30 with the wrong log base (N16b §1(b), lineN15 §1g) | N14 §3, N15 §6, N16 row 21 |

**Subsequence version (corrected).**
- On 𝒫 (h_p prime):
  - H5 holds, including the cross lines;
  - H6's squarefree clause is trivial, and its 7h_p clause is subsumed by I_p;
  - H8 reduces to H1 [P-sketch].
- **Statement.** R′ fails along m = 3p, p ∈ 𝒫, if H0–H4, H6 (p₀ only) and H7* (K_p levels, including prime powers) hold, p ≥ p_thr (in particular p ≥ 1399), and 𝒫 is infinite.
- 𝒫 ∩ [5, 300] = {5, 7, 19, 29, 47, 59, 163, 257} (FLINT, lineN14). p = 3 is excluded by range.
- Infinitude of 𝒫 is equivalent to the failure of R_NSW (TRACE-210), and is open.

## 3. Ingredients that are proved (label, file)
| Ingredient | Label | File |
|---|---|---|
| Positivity lemma; sign identity; trivial floor; squarefree reduction | [P] | N6 §1, §5–6 |
| TRACE-213 identity, NR ≥ −4m, floor −(h_p/d)S_ρ, inclusion m₀ = 15 | [P] (TRACE-273) | N17b_v2 §1 |
| (±2,16) closed at all levels, p ≥ 339 | [CA]+[P], mod J3 rig_spec spectral containment (N7-F2) | N7 §1 |
| Lemma P; Lemma P′ (all isotropic points at q = h_p), with the 4-fixed-point correction (N8b-F3) | [P] | N7, N8b |
| Lemma P′_c, classification, weight amplification A_c | [P] | N8b §1–3 |
| Prop X′ explicit error, p ≥ 1289 | [P mod Line F certs + class CA], certified classes only; k-parity mechanism and E-family absorption [P-sketch] (N8-F3/F4) | N8 §2 |
| 15 small-depth classes (near-0 + 14) | [CA] | N8 §0 |
| Coding lemma | [P] | N11 §3 |
| \|1+X_gas\| ≥ 2(1+Re Λ)^p e^{−pδ} − 1 | [P given the model form] | N11 §0 |
| Re Λ_lo ≥ 6.238e-4 (Re Λ_lo′ = 6.234e-4 after charges) | [CA] | N11 §0, N14 |
| Adapted norm: cond_H 21.103, Lip_H 167.213, Q̃ 0.45 | [CA] | N13 b_arb.py |
| Quadratic step bound N_H ≤ 1 + 1.01e-12 + 4260t², **only for \|t\| ≤ 1/256** | [CA]+[P] (lineN13 partition) | N13 b2_quad.py |
| Step-norm table \|t\| > 1/256, max 2.91656, SVD-free | [CA-fp] (method refereed lineN15 §1a; values not independently recomputed) | N15 nh_table_rig.py |
| δ_int^core ≤ 5.14476e-7 | [CA-fp] (c3_mid; F14.1 closed, lineN15) | N15 |
| ρ̄ ≤ 0.28, eigen-solver-free residual certificate | [CA-fp]; core→true 0.28028 [P-sketch]; tensor joint-pair claim [H] | N14 b_cp2, N15 b_cp3 |
| A_bad finite part j ≤ 12, re-run with c3 radii: 2.031569e-6 at g₀ = 4 | [CA-fp] | N15 a_cert3.py |
| Short types Σ\|w\| = 9.970e-7 (173 rows incl. α = 4) | [CA-fp] | N14 |
| δ_true(G ≤ 15) ≤ 2.470e-6 | [CA-fp] numerics, [P-sketch] conversion lemma | N16 |
| Exact carry reduction \|e\| ≤ 15 (sharp 14, 633 states); torus identity | [P] (633/14: referee) | N15 §3, audit lineN15 §1e |
| Theorem C′ (unit points, rates 1.27440 / 1.20428) | [P + CA* mod H6] (Λ is [CA*], lineN3) | N2, N3 |
| Lemma 1 (sublattice separation; squarefree d, split primes) | [P] (refereed lineN16 §2b; C = 16λ²δ²h²λ^{−p}) | N14b §2, REPORT_N17b_v2 §6 |
| Lemma 2 (subgroup C′, c_B = 0.7375) | [P-sketch] | N14b §2 |
| Gas vs Robin crossover: all p ≥ 1386 (core) / 1390 (δ_true, G ≤ 15); first prime 1399 | [P-arith] (lineN16) | N19b a_crossover_v3.py (robin() corrected; v2 in N18b had the bug) |
| Negative results: D1 + G*_gas route dead (θ ∈ [1/16, 1/4]); 4-fold automaton ≥ 5.41151 > 2.611; letterwise CP bound diverges; H-product conversion vacuous | [N]+[P]; [CA (author), CA* (referee)]; [N]; [N]+[P] | N12b; N10b; N14 §2.3; N15 §5 |

## 4. What is unconditionally proved
- **No refutation of R′, and no single-p inequality** W′_{3p} > (any o(m) bound) in the large-p regime.
- **The lemmas of §3**, as labelled.
- **Small p are [N] only.** Exact W′ tables exist for m ≤ 17 (W′/m = −0.74, −0.31, −0.04, +0.47, +0.09 at m = 9…17). Level data (Dev_d, d ≤ DMAX) at m = 21, 33, 39 come from the I2′ formula [N] (N17b). The often-quoted "+2.95 at m = 57" is **not** an exact W′/m: m = 57 is p = 19, outside the full enumerations, and +2.95 is the TW-law [N] estimate of the h_p-level isotropic deviation alone (lineN5 table).
- For p ∈ 𝒫 the mixed-class input is vacuous, but H1–H4, H6–H7 remain.

## 5. Novelty (careful)
- Unchanged from v1. No systematic literature search for prior occurrences of Lemma P′, the polymer-gas structure, the collision-automaton certificate, or the subgroup separation lemma. These are "obtained in this project" and not claimed as new.
- The literature checked in N15b does not contain H5 and shows it is beyond known exponential-sum technology.

## 6. Superseded / withdrawn (do not cite)
- p-uniform Lemma A∞ (N7/N8).
- G (N8b); the G* route via D1 + gas.
- N12's tail "best cut"; "≈1.5% at G = 13".
- N14b's c_D = 0.899 as a ceiling.
- N14 §3's "0.97·ℓ₀/log_λ d".
- v1's uniform "−0.2" inherited constant (replaced by I_p).
- v1's subsequence version (omitted the K_p levels).
- **v3 additions:**
  - c2_mid radii (superseded by c3_mid);
  - δ_int values 5.14415e-7 / 5.14416e-7 (superseded by 5.14476e-7);
  - N17b §5(b) "372 = hp-div members" (wrong; the 372 are non-unit ν excluded by TRACE-206, and the counts coincide; n = 7371 stands; B1);
  - N15 kp.py's attribution of the j > 12 tail to "Lemma D" (it is H1, [H] placeholder; N15-F1);
  - v2's "Weil range covered conditional on OP" (B3);
  - (1 + Re Λ − δ)^p in v1/v2 B_p (N11-F4);
  - a = 6.2289e-4 (rounded up; correct ≥ 6.22885e-4);
  - "≈1500 with v1 budgets" (no script);
  - "p ≳ 415" for ε₁₆;
  - v2's "≈150× margin" for the collision constant (it is 186×; 150× is the budget margin);
  - the "+2.95 at m = 57" description.

- N18b a_crossover_v2.py Robin term 0.6483/ln K_p (should be /ln ln K_p): crossovers 1382/1386 and "12.77 at p = 1289" superseded by 1386/1390 and 12.85 (lineN16).

## 7. Referee findings reflected
- **lineN14:** N13b/N14b fixes (REPORT_N17b_v2 §5–6).
  - The 7743/7371 bullet of v2 §7 is corrected per B1: 7743 − 7371 = 372 non-unit ν, and the equality with n₂₃ + n₃₅₃ is a coincidence.
  - "δ_int printed as 5.14416e-7" and "ρ̄ needs a-priori constants or arb" are **closed by N15** (lineN15 §1a–1c).
- **lineN15:** §3 items 1–20 applied (map in §9). N15-F1 (H1/H3 rows), N15-F2 (H3 citation), N15-F3 (\|e\| ≤ 14, 633 states).
- **"What remains"** (lineN15 §4, merged):
  1. **H1:** phase-keeping carry certificate on 633 pair states, or an analytic Gram tail; box/aliasing constants; constant ≤ 0.082 at J₀ = 12; j > 12 tail.
  2. **H4:** difference-form conversion + G > 15 true tail.
  3. **H5:** R-mix + cross lines + partially isotropic points, or 𝒫 (open, ⇔ ¬R_NSW).
  4. **H7*:** hp-div, mixed and all K_p levels (incl. prime powers) below L_fl at rate < T′ = 1.42785. Needed even on 𝒫; Theorem W covers nothing at realistic p.
  5. **H6:** explicit p₀; squarefree or q^a weights.
  6. **Writing:** KP corollary + background interplay (H3); Lemma 1 done ([P], lineN16); Lemma 2 → [P]; k = O(1) stays; R₄ automaton; p₁ with all budgets.
  7. **Closed:** F14.1; ρ̄ eigen-solver-free; δ_int^core ≤ 5.14476e-7; "rigorous c2_mid constants" (old item 4).

## 8. Claim → file → referee map
| Claim | Value / label | File | Referee |
|---|---|---|---|
| TRACE-213 identity, NR ≥ −4m, floors | [P] | N17b §1 | lineN15 §2(f) ✓ |
| Inclusion m₀ = 15 | [P] | N17b g_threshold.py; TRACE-273 | lineN15 §2(c) ✓ |
| → ∞ step, B_p ≥ κ suffices | [P mod inputs] | N17b_v2 §2 | lineN15 §2(f), item 20 ✓ |
| Gas vs Robin, first prime 1399 | [P-arith] | N18b a_crossover_v2.py; corrected N19b a_crossover_v3.py | lineN15 §2(b); lineN16 §2a ✓ after robin() fix (1386/1390; first prime 1399); monotonicity ✓ |
| K_p identity, 7 \| K_p, h₁₅ = 7·31²·41 | [P] (Lean p = 5..13; numeric p ≤ 400) | N17b a_levels.py | lineN15 §2(d), §5 ✓ |
| Dev_7 at m = 15, 21, 33, 39 | [N] | N17b d_g3dev.py | lineN15 §2(a) ✓ reproduced |
| S = CRT, n = 7371 at h = 8119 | [P] | N17b_v2 §5(b) | lineN14 §1; lineN15 B1 (explanation fixed) |
| Lemma 1 | [P] | N14b §2; N17b_v2 §6 (erratum N19b REPORT_N17b_v3) | lineN16 §2b ✓ |
| Lemma 2 c_B = 0.7375 | [P-sketch] | N14b | lineN14 ✓ |
| p = 31 covered (H5, not 𝒫) | [P-sketch, asymptotic] | N14b | lineN14 ✓ (Lean p31_cover) |
| NSW primes ≤ 300 | [N, FLINT] | — | lineN14 ✓ |
| δ_int^core ≤ 5.14476e-7 | [CA-fp] | N15 c3_mid.py | lineN15 §1a–b ✓ |
| ρ̄ ≤ 0.28 | [CA-fp] | N15 b_cp3.py | lineN15 §1c ✓ |
| A_bad j ≤ 12 = 2.031569e-6 | [CA-fp] | N15 a_cert3.py | lineN14 ✓; lineN16 §1(e) ✓ (10 classes bit-identical; aggregate) |
| KP a = 5.93e-6 | [P]/[CA-fp]/[H] tail | N15 kp.py | lineN15 §1d (F1, F2) |
| \|e\| ≤ 14, 633 states; torus identity | [P] | N15 §3 | lineN15 §1e |
| Carry correction ≤ 2e-9 | [N] | N16 g_scalar.py, g_triple.py | lineN16 §1(a) ✓ reproduced |
| δ_true(G ≤ 15) ≤ 2.470e-6 | [CA-fp]+[P-sketch] | N16 conv_vec.py, f_post_true.json | lineN16 §1(c–d) ✓ numerics; lemma [P-sketch] |
| Wrap c < 1.1718·ℓ₀/ln d | [P] arithmetic, conditional | N15 §6, N16 row 21 | lineN15 §1g ✓ |
| Quadratic bound \|t\| ≤ 1/256 | [CA]+[P] | N13 | lineN13 ✓ |
| Step-norm table \|t\| > 1/256 | [CA-fp] | N15 | lineN15 §1a (method) |
| C′ rates 1.27440 / 1.20428 | [P + CA* mod H6] | N2, N3 | lineN3; lineN15 item 20 ✓ |
| (±2,16) p ≥ 339 | [CA]+[P] mod J3 | N7 | lineN7 (F1, F2) |
| Prop X′ | [P mod certs], [P-sketch] parts | N8 | lineN8 (F3–F5) |
| N15b literature note (H5) / N16b units note (H8) | author notes | N15b, N16b | not refereed |
| Theorem W range | proved under standing inputs, p ≳ 8.3e25 | TRACE-252 | lineN15 B3 |

## 9. Changes v2 → v3 (lineN15 §3 item → where)
1. §0: overclaims removed (H6 squarefree; H4 has no route).
2. §2: B_p uses (1+Re Λ)^p e^{−pδ}; n/h_p := 1; p₁ [P-arith, float + monotonicity], first prime 1399 (numbers corrected in v4: 1386/1390).
3. §2: single δ value — core 5.14476e-7 [CA-fp]; true-functional G ≤ 15 2.470e-6 (N16) clearly distinguished; duplicate formula paragraph removed.
4. §2: threshold list defines p_thr.
5. H5(b): cross lines added. They vanish on 𝒫.
6. H1: 186× vs 150× clarified; N15/N16 outcomes added.
7. H2: δ_int^core and "closed by N15 c3_mid".
8. H3: N15 §4 explicit; tail = H1 [H] placeholder; citation (N15-F2).
9. H4: H-product vacuous; now difference-form + G > 15 true tail (N16).
10. H5: "[P-sketch] (asymptotic, constants ignored)"; p = 31 moved here.
11. H7: Weil (B3), TRACE-223, TRACE-215/217 caveat, TRACE-273, prime powers.
12. H8: 0.6647 (ρ̄_true), not 0.667; dependence on the subgroup lemma and H1.
13. Subsequence version: (a) 7h_p clause subsumed by I_p; (b) H8→H1 [P-sketch]; (c) prime powers; (d) p ≥ 1399 and the thresholds; (e) ⇔ ¬R_NSW.
14. §3 labels: Prop X′, (±2,16), C′, Lemma P′, Lemma 1, automaton.
15. §3: norm bound scope \|t\| ≤ 1/256 and the \|t\| > 1/256 table.
16. §3: δ_int, ρ̄, A_bad rows replaced.
17. §4: m = 57 description corrected.
18. §6: errata added.
19. §7: corrected (B1; closed items).
20. Assembly label "[P mod inputs]". Lemma 1 written out (REPORT_N17b_v2 §6).

## 10. Changes v3 → v4 (referee lineN16 §4)
- **E1:** p₁ row, §3 crossover row and §8 crossover row now read 1386 (core) / 1390 (δ_true, G ≤ 15), first prime 1399. Robin term fixed (N19b a_crossover_v3.py reproduces lineN16 §2a; REPORT_N17b_v3).
- **E2:** H1 row [N] sentence replaced; N16-1 label split noted.
- **E3:** H4 row conversion sentence replaced; H4 definition now names the per-step perturbation term (N16-2).
- **E4:** scale 1.13287^m.
- **E5:** plain-summary small-p bullet replaced.
- **E6:** referee-status cells in §3, §8 and §7 item 6 updated; optional N15b/N16b author-notes row added.
- **E7:** §6 erratum for the N18b Robin term.
- Lemma 1 is now [P] (lineN16 §2b), with cosmetic fixes L1-a/L1-b in N19b/REPORT_N17b_v3.md.
