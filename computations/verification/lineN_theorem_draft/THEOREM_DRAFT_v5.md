# THEOREM_DRAFT v5 — conditional refutation of frozen R′ (TRACE-206) along m = 3p (Theorem R♯ path, modulus form)

*v5: final assembly, Grok Bot, 2026-11-01 (Asia/Yekaterinburg, UTC+5). v5 = v4 + N20 v2 diff (`N20/THEOREM_DRAFT_v4_to_v5_v2.diff`, refereed lineN20) + N21 v2 (refereed lineN21) + referee lineN21b (N_H table; budgets; crossover) + the crossover decision of §2 (A_bad^KP is charged). See §11. v1–v4 are kept unchanged. Nothing pushed; claims.json untouched (proposals in `V5/CLAIMS_PROPOSED_v5.md`).*

*Repo copy (integration, 2026-11-01): referee lineN22 edits E1–E8 applied verbatim (GO after E1–E12; E9–E12 concern the claims proposal and are applied in `record/claims.json`/`record/errata.json`, not here). The author original has sha256 69bdea02…998ae4 (/workspace/bgs-lineN/THEOREM_DRAFT_v5.md; listed in `V5/SHA256_V5.txt`); the exact change is `THEOREM_DRAFT_v5_lineN22_edits.diff`. Paths `V5/…` resolve relative to this directory; N20/N21 packets and referee reports lineN20/lineN21/lineN21b/lineN22 are under `evidence/executions/20261101/lineNgas/`. Nothing else differs from the author original.*

*v4: Line N19b, 2026-11-01 (Asia/Yekaterinburg, UTC+5). v4 = v3 + referee lineN16 §4 edits E1–E7 (verbatim) + N16 referee minor notes (N16-1…N16-4) in the H1/H4 rows; see §10. v1, v2, v3 kept unchanged.*

*v3: Line N18b, 2026-11-01 (Asia/Yekaterinburg, UTC+5).*
- **Applies:** referee lineN15 §3 items 1–20, plus the N15 items affecting the draft (N15-F1, N15-F2, N15-F3). It also incorporates N16 §3 (gap (a) status table) and REPORT_N17b_v2 (N18b).
- **Kept unchanged:** v1 (THEOREM_DRAFT.md) and v2 (THEOREM_DRAFT_v2.md). The v2 → v3 changes are in §9.
- Nothing pushed.

**Plain-language summary (v5).**
- **What is proved unconditionally.** Frozen R′ is **not** refuted, unconditionally or at any single p. What is proved:
  - the structural lemmas and bookkeeping of §3 (positivity, TRACE-213 level identity, Lemmas P/P′, coding lemma, Lemma 1, K_p arithmetic, carry reductions) [P];
  - certified constants [CA]/[CA-fp]: Re Λ_lo′, adapted norm, step-norm table (now independently recomputed), δ_int^core;
  - **the true-functional interaction constant**: δ_true ≤ 5.0313e-6 for all G (N21 Lemmas C, Q, D^T) [P] + [CA-fp], refereed lineN21/lineN21b, given the standing-package constants taken as certified (N8 n_cert constants, N13 V1–V3b, Line F F2, N6 symmetry), as for H2. **H4 is no longer an input.**
  - negative results that close routes: the H-product conversion is vacuous; the D1 + G*_gas route is dead; and (N20) **Lemma J / Prop. F**: no unrestricted carry/Bohr-mean bound can give H1.
- **What is conditional, and on what.** Theorem R♯-mod v5 (§2) turns "B_p ≥ κ > 0 for infinitely many primes p" into "W′_{3p}/m → ∞", i.e. frozen R′ fails along m = 3p. It is [P mod inputs] and needs these open inputs:
  - **H1** (re-scoped by N20): the bad-cluster (polymer-restricted) **joint second moment** on the ε-chain, Σ_{bad, shell j}|r_A r_B|² ≤ C·2^{j(1−β(0.28))} for j > J₀ = 12 with C ≤ 0.082, plus the lattice→main-term (near-collision/box) constants. [H]. Only the finite shells j ≤ 14 are certified (core functional), with a 186× margin.
  - **H3** (KP polymer bound): **follows from H1** (Prop. K) [P + CA mod H1-shell; span bound and background interplay P-sketch], so it is not an independent input any more.
  - **H5**: composite h_p (mixed classes, cross lines, partially isotropic points), or restriction to 𝒫 = {h_p prime}, whose infinitude is open (⇔ ¬R_NSW).
  - **H6**: explicit p₀ for C′, and squarefreeness of h_p (Wieferich-type).
  - **H7\***: signed control of included levels d ∉ {h_p, e·h_p} below the floor L_fl (hp-div, mixed, all K_p levels incl. prime powers), at growth < T′ = 1.42785. Needed even on 𝒫.
  - **H8**: deep wrap-around points at composite h_p (reduces to H1 on 𝒫, [P-sketch]).
  - **H0**: the standing N6 package (taken as given).
- **The threshold p₁ moved (v5 correction, §2).** The bad-cluster rate A_bad^KP enters the gas exponent together with δ, and v4 left it out. With all rate budgets charged, p₁ depends on H1's constant:
  - first prime **3307** under H1 as stated (C ≤ 0.082), rate budgets only (additive budgets idealised, item (iv)), and sensitive to the [P-sketch] background normalisation of A_bad^KP (+1% → 3359; referee lineN22);
  - first prime **1409** under a strengthened H1 with C ≤ 8.8e-4 (2× the measured finite-shell constant; by Prop. F the finite shells are not evidence for the tail). This value is robust (1409 up to 2× A_bad^KP).
  - v4's "first prime 1399" holds only with A_bad^KP = 0.
- **New problems formulated** (N20/N21):
  - (i) H1-bad as a polymer-restricted joint (A,B) second-moment problem on an ε-adic carry system (|e| ≤ 51, 6145 pair states), where Prop. F rules out every unrestricted method;
  - (ii) H1-ali, the near-collision/box constants;
  - (iii) a certified phase-keeping carry operator for the joint system;
  - (iv) closing p₁ with all *additive* budgets (tails, Y, X_cross, ε, n/h_p), which are still idealised.
- **Small-p evidence is numerical only.** Exact-enumeration W′ tables exist for m ≤ 17 (p ≤ 5), and the I2′ level data at m = 21, 33, 39 are [N]. None of it is evidence for the asymptotic statement.

**Labels.**
- [P] proof written out and refereed (or elementary).
- [P-sketch] argument complete in outline.
- [CA] rigorous arb/interval.
- [CA-fp] IEEE binary64 with derived a-priori rounding bounds under the stated model (IEEE standard model + libm ≤ 1 ulp).
- [CA*] float certificate reproduced, not interval.
- [N] numerics without error control.
- [H] hypothesis/heuristic.

## 0. Status
- **Frozen R′ is not refuted**, unconditionally or at any single p. The conditional statement is Theorem R♯-mod v5 (§2).
- **No input is routine.**
  - H6 contains, besides an explicit p₀ for C′, the squarefreeness of h_p. That is a Wieferich-type open question (N3-F8).
  - H4 is **met** in v5 (N21 v2: Lemma C two-sided conversion incl. the dPi² term; Lemma Q; difference-form Lemma D^T for G ≥ 37), giving δ_true ≤ 5.0313e-6 [P] + [CA-fp], refereed lineN21/lineN21b. The H-product route remains vacuous (N15 §5).
  - H1 is the first open input. By N20 Prop. F, no unrestricted carry/torus-mean bound can prove it.
- **H7 is serious** (N17b/v2). W′ is a plain signed sum; the inclusion threshold excludes no (±2,8) level for m ≥ 15 (TRACE-273); and K_p levels, including prime powers, survive for prime h_p.

## 1. Objects (pointers only)
- **Map.** Kicked quantized cat map, λ = 3+2√2 = ε², ε = 1+√2. h_p are NSW numbers, λ^p ≡ 1 (mod h_p); h_{3p} = h_p·K_p, K_p = 4h_p² + 3, 7 | K_p, gcd(h_p, K_p) | 3.
- **Deviation.** W′_m (TRACE-206) = NR part + φ⁻¹Σ_{ρ,d incl} Dev_d(ρ) (TRACE-213). NR ≥ −RMT ≥ −4m.
- **Level-h_p sum.** φ⁻¹Dev_{h_p} ≥ S_ρ·(n/h_p)·(|1+X+Y|² − 1), S_ρ := φ⁻¹|Z_ρ|²/h_p (N6 §0.8, N11b §1):
  - X: isotropic sum. At composite h_p, X also contains the 2^{ω(h_p)} − 2 **cross lines** (N7-F6), which the gas does not code.
  - Y = Y_U + Y_mix + partially isotropic points.
- **Gas.** X_coded = 2[(1+Λ)^p e^{pΔ} − 1] − (dense part) (N11 §4). The lower bound used is |1 + X_coded| ≥ 2(1 + Re Λ_lo′)^p e^{−pδ} − 1, **not** with (1 + Re Λ − δ)^p (N11-F4). This is the model-gas bound; with the bad clusters (H3) the factor is e^{−p(δ + A_bad^KP)} (§2).

## 2. Conditional main theorem (draft)
**Theorem R♯-mod v5 (draft) [P mod inputs H0, H1, H5–H8 (H2, H4 met; H3 ⇐ H1), assembly; v2 bookkeeping checked by referee lineN15 item 20; the v5 A_bad^KP correction of the exponent is [P-sketch], refereed lineN22 (correct, necessary)].**
Let p be prime, m = 3p, p ≥ p_thr := max of the thresholds listed below. Assume H0–H8 at p. Put

  B_p := (n/h_p)·[(2(1+Re Λ_lo′)^p e^{−p(δ + A_bad^KP)} − 1 − |X_tail| − |X_cross| − |Y| − e^{−0.28p})² − 1] − I_p − ε_16 − ε_fl − ε_other,

- δ := the **true-functional** interaction constant, all G: **δ ≤ 5.0313e-6** [P (N21 Lemmas C, Q, D^T; refereed lineN21) + CA-fp]. Its parts are 2.2102e-6 (G ≤ 15), 2.712658e-6 (16 ≤ G ≤ 36, box), 1.0843e-7 (G ≥ 37, Lemma D^T) and 3.1e-13 (G > 60). For comparison only, the core functional gives δ_int^core ≤ 5.14476e-7 [CA-fp].
- A_bad^KP := S₀(a), the KP-weighted per-site bad-cluster activity of H3 (N15 §4, N20 Prop. K). It depends on H1's constant:

  | H1 constant C (J₀ = 12) | A_bad^KP |
  |---|---|
  | 0.082 | ≤ 3.4457e-4 |
  | 0.04 | ≤ 1.1182e-4 |
  | 8.8e-4 | ≤ 2.3798e-6 |
  | 4.4e-4 | ≤ 2.1548e-6 |

  These come from N20 `tail_kp_v2.json` [P + CA mod H1-shell]. v4's 2.0629e-6 contained the withdrawn [H] tail placeholder.
- **Why A_bad^KP is in the exponent (v5 correction; lineN21b Task 3).**
  - The per-site normalisation of the gas is Re Λ = 2Σ_model Re w, and every non-model cluster is a polymer with activity A_bad (N14 §1 item 4: "the target is A_bad < Re Λ_lo′ − δ_int").
  - KP (H3) controls the log of the polymer partition function only up to p·A_bad^KP. So the lower bound on |1 + X_coded| carries the factor e^{−p(δ + A_bad^KP)}, not e^{−pδ}.
  - v4's B_p and the N18b/N19b/N21 crossover charged δ alone. That cannot be justified: no argument shows that the bad clusters only *add* modulus. The v5 formula charges both. Precisely: |ln Ξ_bad| ≤ Σ_γ |w̃(γ)| e^{a|γ|} ≤ p·S₀(a) (anchored KP corollary, Ueltschi 2004 Thm 1), so |Ξ_bad| ≥ e^{−pS₀(a)}; the charge is the weighted S₀(a), not a. Here w̃ are the bad activities renormalised by the model background, and S₀ must be evaluated with w̃ [P-sketch, as H3 background interplay]. Refereed lineN22: correct and necessary (no sign information on bad clusters); 3307 moves by ≈ +50 per +1% in S₀, 1409 is stable.
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
| p₁: gas vs Robin, **all rate budgets charged**: δ_eff = δ_true + A_bad^KP (additive terms still idealised: tails = Y = X_cross = ε = 0, n/h_p := 1) | **H1 as stated (C ≤ 0.082):** δ_eff ≤ 3.4962e-4 → all p ≥ **3305**, first prime **3307**. **C ≤ 0.04:** 1.1691e-4 → 1726 / 1733. **C ≤ 8.8e-4** (2× measured finite-shell C): 7.4115e-6 → 1402 / **1409**. **C ≤ 4.4e-4:** 7.1864e-6 → 1402 / 1409. **v4-style A_bad^KP = 2.0629e-6** (with the withdrawn placeholder): 7.0944e-6 → 1401 / 1409 (= lineN21b). In every case there are no violations among primes ≤ 5000 and monotonicity holds | [P-arith: float + exact big-int K_p + monotonicity, N19b logic verbatim (`V5/code/crossover_v5.py`); independently reproduced in mpmath (referee lineN22; C = 0.04 with unrounded input: 1725/1733)], conditional on H1 through A_bad^KP |
| p₁, δ only (A_bad^KP = 0; **superseded**, kept for comparison) | δ_true = 5.0313e-6: all p ≥ 1397, first prime 1399 (N21 v2; referee lineN21 §4). Core δ: 1386. v4: 1390 | [P-arith], but **not** the theorem's threshold |
| p₁ with additive budgets (tails, Y, X_cross, ε, n/h_p) | not computed | open |
| Theorem W (only if Weil coverage is invoked) | p ≳ 8.3e25 (m₁ uncomputed) | TRACE-252 |

**Gas vs divisor bounds [P-arith / P].**
- The gas growth beats the Robin bound on inherited levels for p ≥ p₁ under the stated idealization.
- It does **not** beat the unconditional τ(h_m) ≤ e^{Θ(p/log p)} (Nicolas–Robin 1983). So floors absorb only levels d ≥ L_fl ≈ 4τ(h_m)h_p/(G − I_p), and H7* is needed below.

**Hypotheses:**

| # | Hypothesis | Status / best partial result | Where |
|---|---|---|---|
| H0 | Standing package of N6 Theorem R♯ (Line F/J/J3/L16 trace representation; TRACE-197/199/207/212/213/228; Prop X architecture; n_cert) | taken as given; Prop X [P-sketch]; n_cert [CA] | N6 §5, N7 §0, N8 |
| H1 **(T)** collision lemma, re-scoped (N20): H1 = **(H1-bad)** polymer-restricted joint second moment on the ε-chain (A even / B odd sites, ε-zero-runs < g₀): Σ_{bad, shell j}\|r_Ar_B\|² ≤ C·2^{j(1−β(0.28))}, C ≤ 0.082 at J₀ = 12; **+ (H1-ali)** lattice→main-term (near-collision / box) constants | **OPEN, [H].** Proved: finite part **j ≤ 14, core functional** (H4 not run) with C_cert ≤ 4.36e-4; ≤ 5.9e-5 for j ≥ 8, decreasing over j = 10…14 [CA-fp] (N20 Thm A); Lemma P0 (X 1-periodic) and **Lemma J**: the joint collision relation is ε-adic, carries \|e\| ≤ 51 (sharp), **6145** pair states [P] — the 633-state λ-system (\|e\| ≤ 14 [P, Lean]) is only the single-window subsystem; renewal Lemma R [P, Lean]; **Prop. F** (1 ≤ n ≤ 10¹⁰) [P mod N13 CA]: the *unrestricted* joint torus mean is ≥ 5.1e-7·λ^{−n} ≫ i.i.d. 3.45²·0.28^{2n} (ratio ≥ 4.3e-8·2.188ⁿ > 1 for 22 ≤ n ≤ 10¹⁰; ratio uses the N14 float 3.45 [N]), so no unrestricted carry/Bohr-mean bound can give H1; the bad restriction must enter the certificate. [N]: joint torus/iid = 1.86 ± 0.07 at n = 2 (single windows ≈ 1, as N15/N16); all-class lattice S2 flat in j. The single-window "torus = iid to 1e-11" (N16) is **not** evidence for H1. Margin: C_cert ≤ 4.4e-4 vs 0.082 (186×; ≥ 188× certified) — **finite-shell margin only** (j ≤ 14, core functional); by Prop. F it says nothing about the tail | N14 §2; N15 §3; N16 §1; **N20 §2–4** |
| H2 **(I-core)** interaction, core functional | **met:** δ_int^core ≤ **5.14476e-7** [CA-fp; c3_mid, closed F14.1, confirmed lineN15 arb 5.1447502e-7] + Lemma D core tail G > 15 ≤ 1.56e-8 [P+N] | N15 c3_mid.py; N13/N14 Lemma D; audit lineN15 §1b |
| H3 **(KP)** polymer weight e^{a\|γ\|}, log→modulus | **[P + CA mod H1-shell; span bound ℓ ≤ 2j + g₀ is P-sketch]** (N20 Prop. K, report v2): for every C ≤ 0.082 at J₀ = 12, KP holds with a ≤ 2.70e-3 and Re Λ_lo′ − A_bad^KP − δ_true ≥ 2.738e-4, using δ_true ≤ 5.0313e-6 (all G; N21 v2 §5, Lean `delta_true_sum`); with C = 8.8e-4 (2× measured): a = 8.25e-6, A_bad^KP = 2.38e-6, A_bad^KP + δ_true = 7.41e-6 < Re Λ_lo′/84 (≈ 84×; Lean `kp_J12_C88e5`). The 1.56e-8 placeholder is withdrawn. Finite part [CA-fp] j ≤ 14 (core functional); tail arithmetic [CA] (arb) + Lean; KP criterion [P] (Kotecký–Preiss 1986; anchored corollary Ueltschi 2004, Fernández–Procacci 2007). [P-sketch]: span ≤ 2j + g₀ (j ≥ 5), background interplay, polymer normalisation. Note: C_needed(12) = 0.0813 under the "tail ≤ ½ (Re Λ_lo′ − δ_true)" convention at a = 0 (N14 a_need), δ_true v2; v4's 0.082 is ≈ 0.8% above it (KP and positivity still hold at 0.082). **v5:** A_bad^KP also enters the gas exponent (§2), so it moves p₁ (threshold table: 3307 at C = 0.082; 1409 at C ≤ 8.8e-4). Budget: A_bad^KP + δ_true at the v4-style value is 7.0942e-6 = Re Λ_lo′/87.87 (lineN21b); the N15 "/200" clause was display-only and fails (N21 Lean `kp_budget_200_fails`) | N15 §4; **N20 §3.4**; lineN21b Task 3 |
| H4 **(CT)** core→true conversion | **MET [P] (N21 Lemmas C, Q, D^T; refereed lineN21, lineN21b) + [CA-fp]**; inputs N8/N13/F2/N6 taken as certified; the N15 N_H table (claim 323) is now independently recomputed and confirmed (lineN21b: max 2.916448 ≤ 2.91656, every cell ≤ N15's, [CA-fp], 20 cells incl. the max cell [CA]). δ_true ≤ **5.0313e-6** (all G) = 2.2102e-6 (G ≤ 15, Lemma C boxes) + 2.712658e-6 (16 ≤ G ≤ 36, box widening, flat ≈ 1.29e-7/G) + 1.0843e-7 (G ≥ 37, Lemma Q + difference-form Lemma D^T, arb sums) + 3.1e-13 (G > 60, geometric, arb). Lemma C includes the second-order dPi²‖ψ_T‖‖Φ_T‖‖P‖ term. Window numerics are [CA-fp], **not [CA]**. N16's "93% per-step" diagnosis was an artefact of a one-sided bound (F21-4) | **N21 v2** §2–5; audit lineN21, lineN21b |
| H5 **(composite h_p)** (a) mixed classes: (R-mix) E_{mixed,d} F_p ≤ e^{o(p)} d^c r₂^p, c < 0.387 uniformly in d \| h_p; (b) **cross lines**: the 2^{ω} − 2 further fully isotropic lines at composite h_p (in X, not coded by the gas) bounded within budget; (c) partially isotropic points. **Or** p ∈ 𝒫 = {h_p prime} (then (a)–(c) vanish) | OPEN. c_B = 0.7375 established at [P-sketch] (asymptotic, constants ignored), covering iso parts d ≤ 1.588^p. **p = 31** (h₃₁ = 424577·865087, balanced semiprime, θ_max = 0.250 < 0.262) is covered by this, **not** by 𝒫. Evidence c ≤ 0 [N]. No known theorem applies (N15b). (b) was omitted in v1/v2 (N7-F6; lineN10/11 item 4) | N13b, N14b, N15b, N16b, N7-F6 |
| H6 **(C′ inputs)** explicit p₀; h_p squarefree or conductor-q^a weights | C′ [P + CA* mod H6]. p₀ not computed. Squarefreeness open (Wieferich-type, N3-F8). The old "level 7h_p unit points" clause (N3-F9) is **subsumed** by the inherited-level floor I_p (7 \| K_p, so 7h_p = e·h_p), on or off 𝒫 | N2, N3, audit lineN3 |
| H7 **(levels ≠ h_p), precise form H7*** | For included d ∉ {h_p} ∪ {e·h_p}, d < L_fl = h_p^{1+o(1)}: \|Lin_d\| ≤ ε_d\|Z_ρ\|²/h_p with Σε_d ≤ κ₀, i.e. cross-correlation growth < T′ = 1.42785. **Covered:** d = 7 (TRACE-223, \|μ_{1:3}\| ≤ 1.2837144 [CA]; (±2,16) level-7 members via N7/TRACE-227, per the TRACE-215/217 caveat); inherited levels (I_p floor) [P]; d ≥ L_fl (floor) [P]; inclusion (TRACE-273). **Weil range:** OP proved (TRACE-244/251); Theorem W proved under standing inputs, non-vacuous only for p ≳ 8.3e25 (TRACE-252; m₁ uncomputed); extensions TRACE-280/281 (beyond-Weil non-empty only for p ≥ 10^264.5); composite conductors open (TRACE-282). **Covers nothing at realistic p.** **OPEN:** hp-div, mixed, and **all K_p levels including prime powers** (31² \| K₅, 7² \| K₇; rank 3p, TRACE-265). Floor analogue: Prop K2 (TRACE-238/275). Numerics [N]: non-h_p Dev small, mixed signs (REPORT_N17b_v2 §4) | N6 §5, N8b §8, N12b, N17b_v2 |
| H8 **(wrap)** deep wrap-around points of gap (a), composite h_p | prime h_p: reduces to H1 [P-sketch]. Composite: free (c = 0) if per-point weights are not d-amplified; otherwise need **c < 1.1718·ℓ₀/ln d = 0.6647·ℓ₀/log_λ d** (ρ̄_true = 0.28028; with ρ̄ = 0.30: 0.9678·ℓ₀/ln d = 0.5490·ℓ₀/log_λ d). Conditional on the subgroup second-moment lemma **and** H1 (q = (λρ̄²)^{3/2} from the ℓ³ ≤ ℓ² step). **Units:** N14 §3's "0.97·ℓ₀/log_λ d" mixes ρ̄ = 0.30 with the wrong log base (N16b §1(b), lineN15 §1g) | N14 §3, N15 §6, N16 row 21 |

**Subsequence version (corrected).**
- On 𝒫 (h_p prime):
  - H5 holds, including the cross lines;
  - H6's squarefree clause is trivial, and its 7h_p clause is subsumed by I_p;
  - H8 reduces to H1 [P-sketch].
- **Statement.** R′ fails along m = 3p, p ∈ 𝒫, if H0, H1 (which gives H3 by Prop. K), H6 (p₀ only) and H7* (K_p levels, including prime powers) hold, p ≥ p_thr, and 𝒫 is infinite. H2 and H4 are met. p_thr includes p₁ with all rate budgets: in particular p ≥ 3307 under H1 as stated, or p ≥ 1409 if C ≤ 8.8e-4.
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
| \|1+X_gas\| ≥ 2(1+Re Λ)^p e^{−pδ} − 1 (model gas; with bad clusters e^{−p(δ + A_bad^KP)}, §2) | [P given the model form]; bad-cluster factor [P-sketch] | N11 §0 |
| Re Λ_lo ≥ 6.238e-4 (Re Λ_lo′ = 6.234e-4 after charges) | [CA] | N11 §0, N14 |
| Adapted norm: cond_H 21.103, Lip_H 167.213, Q̃ 0.45 | [CA] | N13 b_arb.py |
| Quadratic step bound N_H ≤ 1 + 1.01e-12 + 4260t², **only for \|t\| ≤ 1/256** | [CA]+[P] (lineN13 partition) | N13 b2_quad.py |
| Step-norm table \|t\| > 1/256, max 2.91656, SVD-free | [CA-fp]; **values independently recomputed** by a different method (lineN21b: SVD + residual certificate; max 2.916448, all 2048 cells ≤ N15's, min margin 3.93e-5); 20 cells incl. the max cell [CA] (arb) | N15 nh_table_rig.py; audit lineN21b |
| δ_int^core ≤ 5.14476e-7 | [CA-fp] (c3_mid; F14.1 closed, lineN15) | N15 |
| ρ̄ ≤ 0.28, eigen-solver-free residual certificate | [CA-fp]; core→true 0.28028 [P-sketch]; tensor joint-pair claim [H] | N14 b_cp2, N15 b_cp3 |
| A_bad finite part j ≤ 12, re-run with c3 radii: 2.031569e-6 at g₀ = 4 | [CA-fp] | N15 a_cert3.py |
| Short types Σ\|w\| = 9.970e-7 (173 rows incl. α = 4) | [CA-fp] | N14 |
| Lemma C: two-sided vector core→true conversion per window, incl. the dPi² term | [P] (refereed lineN21) | N21 v2 §2, conv_c.py |
| Lemma Q: ‖(L₀/μ)^kQ‖ ≤ m(k); K₀ < 56.78, Rem < 1.591e-3 | [P] + [CA] constants (Lean arithmetic) | N21 v2 §4, tail_DT.py, LineN21Arith_v2.lean |
| Lemma D^T: true-operator difference form of the interaction, G ≥ 37 | [P] (step 4 written out in v2; refereed lineN21) + [CA-fp] anchors + arb sums | N21 v2 §4 |
| δ_true (all G) ≤ 5.0313e-6 (G ≤ 15: 2.2102e-6) | [P] + [CA-fp] | N21 v2 §5, final_delta.py |
| Exact carry reduction \|e\| ≤ 15 (sharp 14, 633 states); torus identity | [P] (633/14: referee) | N15 §3, audit lineN15 §1e |
| λ-carry graph: 633 states, \|e\| ≤ 14, ρ(adj) ≥ 20; renewal lemma | [P, Lean (kernel decide; renewal by induction)] | N20 §3.2–3.3, lean/ |
| Lemma J: joint (A,B) collisions are ε-adic, \|e\| ≤ 51, 6145 states | [P] (+ exact integer BFS; Lean: closed-form arithmetic 60·(2+√2)/4 ∈ (51,52) only) | N20 §2 |
| Prop. F: unrestricted joint torus mean ≥ 5.1e-7·λ^{−n} (≫ i.i.d.), 1 ≤ n ≤ 10¹⁰ | [P mod N13 CA]; ratio also N14 float 3.45 [N] | N20 §2 |
| Shell law finite part j ≤ 14, C_cert ≤ 4.36e-4 (core functional) | [CA-fp] | N20 §3.1 |
| H1-shell ⇒ KP (H3), any C ≤ 0.082; budget ≥ 2.738e-4 with δ_true v2 (N21) | [P + CA mod H1-shell; span bound ℓ ≤ 2j + g₀ P-sketch] | N20 §3.4 |
| Theorem C′ (unit points, rates 1.27440 / 1.20428) | [P + CA* mod H6] (Λ is [CA*], lineN3) | N2, N3 |
| Lemma 1 (sublattice separation; squarefree d, split primes) | [P] (refereed lineN16 §2b; C = 16λ²δ²h²λ^{−p}) | N14b §2, REPORT_N17b_v2 §6 |
| Lemma 2 (subgroup C′, c_B = 0.7375) | [P-sketch] | N14b §2 |
| Gas vs Robin crossover with all rate budgets (δ_true + A_bad^KP): first prime 3307 (H1, C ≤ 0.082) / 1409 (C ≤ 8.8e-4); δ only: 1397/1399 (superseded as threshold) | [P-arith], conditional on H1 via A_bad^KP | V5/code/crossover_v5.py (N19b logic) |
| Negative results: D1 + G*_gas route dead (θ ∈ [1/16, 1/4]); 4-fold automaton ≥ 5.41151 > 2.611; letterwise CP bound diverges; H-product conversion vacuous | [N]+[P]; [CA (author), CA* (referee)]; [N]; [N]+[P] | N12b; N10b; N14 §2.3; N15 §5 |

## 4. What is unconditionally proved
- **No refutation of R′, and no single-p inequality** W′_{3p} > (any o(m) bound) in the large-p regime.
- **The lemmas of §3**, as labelled.
- **Small p are [N] only.** Exact W′ tables exist for m ≤ 17 (W′/m = −0.74, −0.31, −0.04, +0.47, +0.09 at m = 9…17). Level data (Dev_d, d ≤ DMAX) at m = 21, 33, 39 come from the I2′ formula [N] (N17b). The often-quoted "+2.95 at m = 57" is **not** an exact W′/m: m = 57 is p = 19, outside the full enumerations, and +2.95 is the TW-law [N] estimate of the h_p-level isotropic deviation alone (lineN5 table).
- For p ∈ 𝒫 the mixed-class input is vacuous. H2 and H4 are met (H4 in v5). H1 (and with it H3), H6 and H7* remain.

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

- **v5 (N20):** N16 §1.3 "torus ≈ i.i.d., so essentially the whole margin is available to the box/aliasing constant" — withdrawn **for H1** (single windows only; joint torus/iid ≥ 4.3e-8·2.188ⁿ for n ≤ 10¹⁰, Prop. F). The H3 tail placeholder 1.56e-8 — withdrawn (replaced by Prop. K, conditional on H1).

- **v5 (N21/lineN21/lineN21b):**
  - **"First prime 1399" as the theorem's p₁** is withdrawn. It charged δ only. With A_bad^KP charged: 3307 (C ≤ 0.082) / 1409 (C ≤ 8.8e-4) (§2).
  - **B_p with e^{−pδ}** (v3/v4) is superseded by e^{−p(δ + A_bad^KP)}.
  - **δ_true(G ≤ 15) ≤ 2.470e-6** (N16, [P-sketch] lemma) is superseded by 2.2102e-6 (N21 Lemma C, [P]). The N16 conv_vec bound had defects (F21-3; √cond instead of cond, which is non-conservative: F21-1).
  - **N16-2 "93% per-step perturbation"** was an artefact of the one-sided bound (F21-4).
  - **N14 digits.py at mp.dps = 34** is invalid for G ≥ 21 (ulp level; material for G ≳ 25). v4 numbers (G ≤ 15) are unaffected (F21-2).
  - **The N15 kp_budget "< Re Λ_lo′/200"** was display-only. The margin is 87.87× (lineN21b).
  - **N21 v1** "24 theorems" (it was 23) and "margin > 100×" are corrected in N21 v2.
- N18b a_crossover_v2.py Robin term 0.6483/ln K_p (should be /ln ln K_p): crossovers 1382/1386 and "12.77 at p = 1289" superseded by 1386/1390 and 12.85 (lineN16).

## 7. Referee findings reflected
- **lineN14:** N13b/N14b fixes (REPORT_N17b_v2 §5–6).
  - The 7743/7371 bullet of v2 §7 is corrected per B1: 7743 − 7371 = 372 non-unit ν, and the equality with n₂₃ + n₃₅₃ is a coincidence.
  - "δ_int printed as 5.14416e-7" and "ρ̄ needs a-priori constants or arb" are **closed by N15** (lineN15 §1a–1c).
- **lineN15:** §3 items 1–20 applied (map in §9). N15-F1 (H1/H3 rows), N15-F2 (H3 citation), N15-F3 (\|e\| ≤ 14, 633 states).
- **"What remains"** (lineN15 §4, merged):
  1. **H1 (re-scoped, N20 §4):** (H1-bad) polymer-restricted joint second moment on the ε-chain (ε-carries \|e\| ≤ 51, 6145 states, 495⁴ blocks; an unrestricted torus/carry bound provably cannot work, Prop. F); (H1-ali) near-collision/box constants; tail j > 14. The 633-state λ-certificate is no longer sufficient (single-window only).
  2. **H4: closed** (N21 v2, refereed lineN21/lineN21b). Optional upgrade: pure-arb window chains ([CA] instead of [CA-fp]).
  3. **H5:** R-mix + cross lines + partially isotropic points, or 𝒫 (open, ⇔ ¬R_NSW).
  4. **H7*:** hp-div, mixed and all K_p levels (incl. prime powers) below L_fl at rate < T′ = 1.42785. Needed even on 𝒫; Theorem W covers nothing at realistic p.
  5. **H6:** explicit p₀; squarefree or q^a weights.
  6. **Writing:** KP corollary + background interplay (H3) and the A_bad^KP-in-exponent step (§2, [P-sketch], flagged); Lemma 1 done ([P], lineN16); Lemma 2 → [P]; k = O(1) stays; R₄ automaton; p₁ with the *additive* budgets (the rate budgets are done in v5).
  7. **Closed:** F14.1; ρ̄ eigen-solver-free; δ_int^core ≤ 5.14476e-7; "rigorous c2_mid constants" (old item 4).

## 8. Claim → file → referee map
| Claim | Value / label | File | Referee |
|---|---|---|---|
| TRACE-213 identity, NR ≥ −4m, floors | [P] | N17b §1 | lineN15 §2(f) ✓ |
| Inclusion m₀ = 15 | [P] | N17b g_threshold.py; TRACE-273 | lineN15 §2(c) ✓ |
| → ∞ step, B_p ≥ κ suffices | [P mod inputs] | N17b_v2 §2 | lineN15 §2(f), item 20 ✓ |
| Gas vs Robin, δ only: first prime 1399 (superseded as threshold) | [P-arith] | N18b a_crossover_v2.py; N19b a_crossover_v3.py; N21 crossover_N21.py | lineN16 §2a ✓; lineN21 §4 ✓ (1397/1399 at δ_true) |
| Gas vs Robin, all rate budgets: 3307 (C ≤ 0.082) / 1409 (C ≤ 8.8e-4) | [P-arith], conditional on H1 | V5/code/crossover_v5.py | lineN21b Task 3 ✓ (1401/1409 at δ_eff = 7.0944e-6); lineN22 ✓ (all rows reproduced; A_bad-in-exponent step correct, [P-sketch]) |
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
| KP a = 5.93e-6 (**superseded**: used the withdrawn tail placeholder; now a = a(C), Prop. K) | [P]/[CA-fp]/[H] tail | N15 kp.py | lineN15 §1d (F1, F2) |
| \|e\| ≤ 14, 633 states; torus identity | [P] | N15 §3 | lineN15 §1e |
| Carry correction ≤ 2e-9 | [N] | N16 g_scalar.py, g_triple.py | lineN16 §1(a) ✓ reproduced |
| δ_true(G ≤ 15) ≤ 2.470e-6 (superseded) | [CA-fp]+[P-sketch] | N16 conv_vec.py | lineN16 §1(c–d); defects F21-1/3 (lineN21) |
| Lemma C; δ_true(G ≤ 15) ≤ 2.2102e-6 | [P] + [CA-fp] | N21 conv_c.py, f_postC.py | lineN21 ✓ (bit-identical spot reruns; own aggregation) |
| Lemma Q, Lemma D^T; G ≥ 37 ≤ 1.0843e-7 | [P] + [CA]/[CA-fp] | N21 tail_DT.py | lineN21 ✓ (independent re-implementation, F1/F2 applied) |
| δ_true (all G) ≤ 5.0313e-6 | [P] + [CA-fp] | N21 final_delta.py, LineN21Arith_v2.lean | lineN21 ✓; lineN21b ✓ (delta check, Lean 24 theorems, axioms) |
| Lemma J; Prop. F; Thm A (j ≤ 14); Prop. K; λ-carry graph + renewal | [P]; [P mod N13 CA]; [CA-fp]; [P + CA mod H1-shell, span P-sketch]; [P, Lean] | N20 v2 | lineN20 ✓ (after fixes 1–7) |
| Wrap c < 1.1718·ℓ₀/ln d | [P] arithmetic, conditional | N15 §6, N16 row 21 | lineN15 §1g ✓ |
| Quadratic bound \|t\| ≤ 1/256 | [CA]+[P] | N13 | lineN13 ✓ |
| Step-norm table \|t\| > 1/256 | [CA-fp] (20 cells [CA]) | N15 | lineN15 §1a (method); **lineN21b ✓ values independently recomputed** |
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

## 11. Changes v4 → v5

### 11a. Line N20 (applied verbatim from N20/THEOREM_DRAFT_v4_to_v5_v2.diff, refereed lineN20)
- H1 row: re-scoped to (H1-bad) + (H1-ali); Lemma J, Prop. F (n ≤ 10¹⁰), Thm A (j ≤ 14, core functional; 186× is a finite-shell margin only) added; single-window [N] evidence marked as not evidence for H1.
- H3 row: [P + CA mod H1-shell; span bound P-sketch] (Prop. K); placeholder withdrawn; budget uses δ_true ≤ 5.0313e-6 (N21 v2) → ≥ 2.738e-4; half-budget threshold 0.0813.
- §3: five rows added (λ-carry graph + renewal; Lemma J; Prop. F; Thm A; Prop. K).
- §6: two withdrawals. §7 item 1 replaced.
- Plain summary unchanged in substance: H1 remains the first open input.

### 11b. Line N21 v2 + referee lineN21 / lineN21b + final assembly
- **Header and plain-language summary** rewritten (proved / conditional on exactly-stated inputs / new problems).
- **§0:** H4 met; H1 is the first open input.
- **§2:**
  - Theorem renamed R♯-mod v5; the inputs are now H0, H1, H5–H8 (H2 and H4 met, H3 ⇐ H1).
  - **B_p exponent: e^{−pδ} → e^{−p(δ + A_bad^KP)}** (lineN21b Task 3; [P-sketch], flagged).
  - δ bullet: δ_true ≤ 5.0313e-6.
  - A_bad^KP defined as a function of H1's C.
- **Threshold table:** p₁ with all rate budgets added (3305/3307 at C ≤ 0.082; 1402/1409 at C ≤ 8.8e-4; 1401/1409 at the v4-style value). The δ-only row (1397/1399) is kept as superseded. The additive budgets are still open.
- **H-table:**
  - H3 row: A_bad^KP moves p₁; margin 87.87×; /200 clause display-only.
  - H4 row: MET [P] + [CA-fp]; N_H caveat resolved by lineN21b.
  - Subsequence statement updated.
- **§3:**
  - Step-norm table row: values recomputed (lineN21b).
  - Lemma C, Lemma Q, Lemma D^T and δ_true rows added (replacing the N16 row).
  - Crossover row replaced.
- **§4:** the 𝒫 bullet is updated.
- **§6:** v5 errata (p₁ = 1399 withdrawn as threshold, B_p exponent, N16 values and diagnosis, F21-1/2, /200, N21 v1 counts).
- **§7:** H4 closed; the writing item is updated.
- **§8:** rows for N21 Lemmas C, Q, D^T, δ_true, N20 results and both crossover variants; step-norm referee cell.
- **Not done in v5:**
  - pure-arb windows for H4;
  - (done: referee lineN22, GO after E1–E12);
  - p₁ with additive budgets;
  - registry changes (proposed only: `V5/CLAIMS_PROPOSED_v5.md`).

