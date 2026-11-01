"""V5 assembly: THEOREM_DRAFT_v4.md + N20 v2 diff (patch) + N21 v2 + referee lineN20/lineN21/lineN21b + crossover decision.
usage: python3 assemble_v5.py  (reads /tmp/v5.md = v4 patched with N20/THEOREM_DRAFT_v4_to_v5_v2.diff; writes THEOREM_DRAFT_v5.md)"""
import sys
S=open('/tmp/v5.md').read()
def rep(old,new,count=1):
    global S
    n=S.count(old); assert n==count,(n,old[:80]); S=S.replace(old,new)

# ---- header
rep("# THEOREM_DRAFT v5 (proposed, not applied) — conditional","# THEOREM_DRAFT v5 — conditional")
rep("*v5 (proposed, N20 report v2 after referee lineN20): Line N20 — H1 re-scoped (Lemma J, Prop. F), H1 finite part to j ≤ 14, H3 conditional on H1 only (Prop. K); see §11.*",
"""*v5: final assembly, Grok Bot, 2026-11-01 (Asia/Yekaterinburg, UTC+5). v5 = v4 + N20 v2 diff (`N20/THEOREM_DRAFT_v4_to_v5_v2.diff`, refereed lineN20) + N21 v2 (refereed lineN21) + referee lineN21b (N_H table; budgets; crossover) + the crossover decision of §2 (A_bad^KP is charged). See §11. v1–v4 are kept unchanged. Nothing pushed; claims.json untouched (proposals in `V5/CLAIMS_PROPOSED_v5.md`).*""")

# ---- plain-language summary (replaces the v3/v4 plain summary)
i=S.index("**Plain summary.**"); j=S.index("**Labels.**")
S=S[:i]+"""**Plain-language summary (v5).**
- **What is proved unconditionally.** Frozen R′ is **not** refuted, unconditionally or at any single p. What is proved:
  - the structural lemmas and bookkeeping of §3 (positivity, TRACE-213 level identity, Lemmas P/P′, coding lemma, Lemma 1, K_p arithmetic, carry reductions) [P];
  - certified constants [CA]/[CA-fp]: Re Λ_lo′, adapted norm, step-norm table (now independently recomputed), δ_int^core;
  - **the true-functional interaction constant**: δ_true ≤ 5.0313e-6 for all G (N21 Lemmas C, Q, D^T) [P] + [CA-fp], refereed lineN21/lineN21b. **H4 is no longer an input.**
  - negative results that close routes: the H-product conversion is vacuous; the D1 + G*_gas route is dead; and (N20) **Lemma J / Prop. F**: no unrestricted carry/Bohr-mean bound can give H1.
- **What is conditional, and on what.** Theorem R♯-mod v5 (§2) turns "B_p ≥ κ > 0 for infinitely many primes p" into "W′_{3p}/m → ∞", i.e. frozen R′ fails along m = 3p. It is [P mod inputs] and needs these open inputs:
  - **H1** (re-scoped by N20): the bad-cluster (polymer-restricted) **joint second moment** on the ε-chain, Σ_{bad, shell j}|r_A r_B|² ≤ C·2^{j(1−β(0.28))} for j > J₀ = 12 with C ≤ 0.082, plus the lattice→main-term (near-collision/box) constants. [H]. Only the finite shells j ≤ 14 are certified (core functional), with a 186× margin.
  - **H3** (KP polymer bound): **follows from H1** (Prop. K) [P + CA mod H1-shell; span bound P-sketch], so it is not an independent input any more.
  - **H5**: composite h_p (mixed classes, cross lines, partially isotropic points), or restriction to 𝒫 = {h_p prime}, whose infinitude is open (⇔ ¬R_NSW).
  - **H6**: explicit p₀ for C′, and squarefreeness of h_p (Wieferich-type).
  - **H7\***: signed control of included levels d ∉ {h_p, e·h_p} below the floor L_fl (hp-div, mixed, all K_p levels incl. prime powers), at growth < T′ = 1.42785. Needed even on 𝒫.
  - **H8**: deep wrap-around points at composite h_p (reduces to H1 on 𝒫, [P-sketch]).
  - **H0**: the standing N6 package (taken as given).
- **The threshold p₁ moved (v5 correction, §2).** The bad-cluster rate A_bad^KP enters the gas exponent together with δ, and v4 left it out. With all rate budgets charged, p₁ depends on H1's constant:
  - first prime **3307** under H1 as stated (C ≤ 0.082);
  - first prime **1409** if H1 holds with C ≤ 8.8e-4 (2× the measured finite-shell constant).
  - v4's "first prime 1399" holds only with A_bad^KP = 0.
- **New problems formulated** (N20/N21):
  - (i) H1-bad as a polymer-restricted joint (A,B) second-moment problem on an ε-adic carry system (|e| ≤ 51, 6145 pair states), where Prop. F rules out every unrestricted method;
  - (ii) H1-ali, the near-collision/box constants;
  - (iii) a certified phase-keeping carry operator for the joint system;
  - (iv) closing p₁ with all *additive* budgets (tails, Y, X_cross, ε, n/h_p), which are still idealised.
- **Small-p evidence is numerical only.** Exact-enumeration W′ tables exist for m ≤ 17 (p ≤ 5), and the I2′ level data at m = 21, 33, 39 are [N]. None of it is evidence for the asymptotic statement.

"""+S[j:]

# ---- §0
rep("- **Frozen R′ is not refuted**, unconditionally or at any single p. The conditional statement is Theorem R♯-mod v3 (§2).",
    "- **Frozen R′ is not refuted**, unconditionally or at any single p. The conditional statement is Theorem R♯-mod v5 (§2).")
rep("  - H4 currently has **no working route**: the H-product route is vacuous (N15 §5, GA 40–340). The vector-chain conversion works numerically per window, but it cannot control the G > 15 tail without a pair-minus-product difference form (N16 §2).",
    "  - H4 is **met** in v5 (N21 v2: Lemma C two-sided conversion incl. the dPi² term; Lemma Q; difference-form Lemma D^T for G ≥ 37), giving δ_true ≤ 5.0313e-6 [P] + [CA-fp], refereed lineN21/lineN21b. The H-product route remains vacuous (N15 §5).\n  - H1 is the first open input. By N20 Prop. F, no unrestricted carry/torus-mean bound can prove it.")

# ---- §2 theorem
rep("**Theorem R♯-mod v3 (draft) [P mod inputs H0–H8, assembly; v2 bookkeeping checked by referee lineN15 item 20, v3 not yet refereed].**",
    "**Theorem R♯-mod v5 (draft) [P mod inputs H0, H1, H5–H8 (H2, H4 met; H3 ⇐ H1), assembly; v2 bookkeeping checked by referee lineN15 item 20; the v5 A_bad^KP correction of the exponent is not yet refereed].**")
rep("  B_p := (n/h_p)·[(2(1+Re Λ_lo′)^p e^{−pδ} − 1 − |X_tail| − |X_cross| − |Y| − e^{−0.28p})² − 1] − I_p − ε_16 − ε_fl − ε_other,",
    "  B_p := (n/h_p)·[(2(1+Re Λ_lo′)^p e^{−p(δ + A_bad^KP)} − 1 − |X_tail| − |X_cross| − |Y| − e^{−0.28p})² − 1] − I_p − ε_16 − ε_fl − ε_other,")
i=S.index("- δ := the **true-functional** interaction constant, all G. What is known:"); j=S.index("- Re Λ_lo′ = 6.234e-4.")
S=S[:i]+"""- δ := the **true-functional** interaction constant, all G: **δ ≤ 5.0313e-6** [P (N21 Lemmas C, Q, D^T; refereed lineN21) + CA-fp]. Its parts are 2.2102e-6 (G ≤ 15), 2.712658e-6 (16 ≤ G ≤ 36, box), 1.0843e-7 (G ≥ 37, Lemma D^T) and 3.1e-13 (G > 60). For comparison only, the core functional gives δ_int^core ≤ 5.14476e-7 [CA-fp].
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
  - v4's B_p and the N18b/N19b/N21 crossover charged δ alone. That cannot be justified: no argument shows that the bad clusters only *add* modulus. The v5 formula charges both. [P-sketch: the same log→modulus step as H3 (background interplay [P-sketch])]. **Flagged for the referee.**
"""+S[j:]

# ---- threshold rows
rep("| p₁: gas vs Robin (tails = Y = X_cross = ε = 0, n/h_p := 1) | all p ≥ 1386 (core δ) / 1390 (δ = 2.470e-6, G ≤ 15 part only; increases once the G > 15 tail is added); **first prime 1399** | [P-arith: float/mpmath evaluation + monotonicity] (N18b a_crossover_v2.py with robin() corrected to 0.6483/ln L; lineN16 §2a) |\n| p₁ with all budgets | not computed | open |",
"""| p₁: gas vs Robin, **all rate budgets charged**: δ_eff = δ_true + A_bad^KP (additive terms still idealised: tails = Y = X_cross = ε = 0, n/h_p := 1) | **H1 as stated (C ≤ 0.082):** δ_eff ≤ 3.4962e-4 → all p ≥ **3305**, first prime **3307**. **C ≤ 0.04:** 1.1691e-4 → 1726 / 1733. **C ≤ 8.8e-4** (2× measured finite-shell C): 7.4115e-6 → 1402 / **1409**. **C ≤ 4.4e-4:** 7.1864e-6 → 1402 / 1409. **v4-style A_bad^KP = 2.0629e-6** (with the withdrawn placeholder): 7.0944e-6 → 1401 / 1409 (= lineN21b). In every case there are no violations among primes ≤ 5000 and monotonicity holds | [P-arith: float/mpmath + monotonicity, N19b logic verbatim (`V5/code/crossover_v5.py`)], conditional on H1 through A_bad^KP |
| p₁, δ only (A_bad^KP = 0; **superseded**, kept for comparison) | δ_true = 5.0313e-6: all p ≥ 1397, first prime 1399 (N21 v2; referee lineN21 §4). Core δ: 1386. v4: 1390 | [P-arith], but **not** the theorem's threshold |
| p₁ with additive budgets (tails, Y, X_cross, ε, n/h_p) | not computed | open |""")

# ---- H3 row note (append) and H4 row
rep("v4's 0.082 is ≈ 0.8% above it (KP and positivity still hold at 0.082) | N15 §4; **N20 §3.4** |",
    "v4's 0.082 is ≈ 0.8% above it (KP and positivity still hold at 0.082). **v5:** A_bad^KP also enters the gas exponent (§2), so it moves p₁ (threshold table: 3307 at C = 0.082; 1409 at C ≤ 8.8e-4). Budget: A_bad^KP + δ_true at the v4-style value is 7.0942e-6 = Re Λ_lo′/87.87 (lineN21b); the N15 \"/200\" clause was display-only and fails (N21 Lean `kp_budget_200_fails`) | N15 §4; **N20 §3.4**; lineN21b Task 3 |")
i=S.index("| H4 **(CT)** core→true conversion |"); j=S.index("\n",i)
S=S[:i]+"| H4 **(CT)** core→true conversion | **MET [P] (N21 Lemmas C, Q, D^T; refereed lineN21, lineN21b) + [CA-fp]**; inputs N8/N13/F2/N6 taken as certified; the N15 N_H table (claim 323) is now independently recomputed and confirmed (lineN21b: max 2.916448 ≤ 2.91656, every cell ≤ N15's, [CA-fp], 20 cells incl. the max cell [CA]). δ_true ≤ **5.0313e-6** (all G) = 2.2102e-6 (G ≤ 15, Lemma C boxes) + 2.712658e-6 (16 ≤ G ≤ 36, box widening, flat ≈ 1.29e-7/G) + 1.0843e-7 (G ≥ 37, Lemma Q + difference-form Lemma D^T, arb sums) + 3.1e-13 (G > 60, geometric, arb). Lemma C includes the second-order dPi²‖ψ_T‖‖Φ_T‖‖P‖ term. Window numerics are [CA-fp], **not [CA]**. N16's \"93% per-step\" diagnosis was an artefact of a one-sided bound (F21-4) | **N21 v2** §2–5; audit lineN21, lineN21b |"+S[j:]

# ---- subsequence statement
rep("- **Statement.** R′ fails along m = 3p, p ∈ 𝒫, if H0–H4, H6 (p₀ only) and H7* (K_p levels, including prime powers) hold, p ≥ p_thr (in particular p ≥ 1399), and 𝒫 is infinite.",
    "- **Statement.** R′ fails along m = 3p, p ∈ 𝒫, if H0, H1 (which gives H3 by Prop. K), H6 (p₀ only) and H7* (K_p levels, including prime powers) hold, p ≥ p_thr, and 𝒫 is infinite. H2 and H4 are met. p_thr includes p₁ with all rate budgets: in particular p ≥ 3307 under H1 as stated, or p ≥ 1409 if C ≤ 8.8e-4.")

# ---- §3 rows
rep("| Step-norm table \\|t\\| > 1/256, max 2.91656, SVD-free | [CA-fp] (method refereed lineN15 §1a; values not independently recomputed) | N15 nh_table_rig.py |",
    "| Step-norm table \\|t\\| > 1/256, max 2.91656, SVD-free | [CA-fp]; **values independently recomputed** by a different method (lineN21b: SVD + residual certificate; max 2.916448, all 2048 cells ≤ N15's, min margin 3.93e-5); 20 cells incl. the max cell [CA] (arb) | N15 nh_table_rig.py; audit lineN21b |")
rep("| δ_true(G ≤ 15) ≤ 2.470e-6 | [CA-fp] numerics, [P-sketch] conversion lemma | N16 |",
    "| Lemma C: two-sided vector core→true conversion per window, incl. the dPi² term | [P] (refereed lineN21) | N21 v2 §2, conv_c.py |\n| Lemma Q: ‖(L₀/μ)^kQ‖ ≤ m(k); K₀ < 56.78, Rem < 1.591e-3 | [P] + [CA] constants (Lean arithmetic) | N21 v2 §4, tail_DT.py, LineN21Arith_v2.lean |\n| Lemma D^T: true-operator difference form of the interaction, G ≥ 37 | [P] (step 4 written out in v2; refereed lineN21) + [CA-fp] anchors + arb sums | N21 v2 §4 |\n| δ_true (all G) ≤ 5.0313e-6 (G ≤ 15: 2.2102e-6) | [P] + [CA-fp] | N21 v2 §5, final_delta.py |")
rep("| Gas vs Robin crossover: all p ≥ 1386 (core) / 1390 (δ_true, G ≤ 15); first prime 1399 | [P-arith] (lineN16) | N18b a_crossover_v2.py (robin() fixed) |",
    "| Gas vs Robin crossover with all rate budgets (δ_true + A_bad^KP): first prime 3307 (H1, C ≤ 0.082) / 1409 (C ≤ 8.8e-4); δ only: 1397/1399 (superseded as threshold) | [P-arith], conditional on H1 via A_bad^KP | V5/code/crossover_v5.py (N19b logic) |")

# ---- §4
rep("- For p ∈ 𝒫 the mixed-class input is vacuous, but H1–H4, H6–H7 remain.",
    "- For p ∈ 𝒫 the mixed-class input is vacuous. H2 and H4 are met (H4 in v5). H1 (and with it H3), H6 and H7* remain.")

# ---- §6 errata (append v5 items after N20's v5 bullet)
rep("- N18b a_crossover_v2.py Robin term 0.6483/ln K_p",
"""- **v5 (N21/lineN21/lineN21b):**
  - **"First prime 1399" as the theorem's p₁** is withdrawn. It charged δ only. With A_bad^KP charged: 3307 (C ≤ 0.082) / 1409 (C ≤ 8.8e-4) (§2).
  - **B_p with e^{−pδ}** (v3/v4) is superseded by e^{−p(δ + A_bad^KP)}.
  - **δ_true(G ≤ 15) ≤ 2.470e-6** (N16, [P-sketch] lemma) is superseded by 2.2102e-6 (N21 Lemma C, [P]). The N16 conv_vec bound had defects (F21-3; √cond instead of cond, which is non-conservative: F21-1).
  - **N16-2 "93% per-step perturbation"** was an artefact of the one-sided bound (F21-4).
  - **N14 digits.py at mp.dps = 34** is invalid for G ≥ 21 (ulp level; material for G ≳ 25). v4 numbers (G ≤ 15) are unaffected (F21-2).
  - **The N15 kp_budget "< Re Λ_lo′/200"** was display-only. The margin is 87.87× (lineN21b).
  - **N21 v1** "24 theorems" (it was 23) and "margin > 100×" are corrected in N21 v2.
- N18b a_crossover_v2.py Robin term 0.6483/ln K_p""")

# ---- §7 what remains item 2
rep("  2. **H4:** difference-form conversion + G > 15 true tail.",
    "  2. **H4: closed** (N21 v2, refereed lineN21/lineN21b). Optional upgrade: pure-arb window chains ([CA] instead of [CA-fp]).")
rep("  6. **Writing:** KP corollary + background interplay (H3); Lemma 1 done ([P], lineN16); Lemma 2 → [P]; k = O(1) stays; R₄ automaton; p₁ with all budgets.",
    "  6. **Writing:** KP corollary + background interplay (H3) and the A_bad^KP-in-exponent step (§2, [P-sketch], flagged); Lemma 1 done ([P], lineN16); Lemma 2 → [P]; k = O(1) stays; R₄ automaton; p₁ with the *additive* budgets (the rate budgets are done in v5).")

# ---- §8 map rows
rep("| Gas vs Robin, first prime 1399 | [P-arith] | N18b a_crossover_v2.py; corrected N19b a_crossover_v3.py | lineN15 §2(b); lineN16 §2a ✓ after robin() fix (1386/1390; first prime 1399); monotonicity ✓ |",
    "| Gas vs Robin, δ only: first prime 1399 (superseded as threshold) | [P-arith] | N18b a_crossover_v2.py; N19b a_crossover_v3.py; N21 crossover_N21.py | lineN16 §2a ✓; lineN21 §4 ✓ (1397/1399 at δ_true) |\n| Gas vs Robin, all rate budgets: 3307 (C ≤ 0.082) / 1409 (C ≤ 8.8e-4) | [P-arith], conditional on H1 | V5/code/crossover_v5.py | lineN21b Task 3 ✓ (1401/1409 at δ_eff = 7.0944e-6); A_bad-in-exponent step not yet refereed |")
rep("| δ_true(G ≤ 15) ≤ 2.470e-6 | [CA-fp]+[P-sketch] | N16 conv_vec.py, f_post_true.json | lineN16 §1(c–d) ✓ numerics; lemma [P-sketch] |",
    "| δ_true(G ≤ 15) ≤ 2.470e-6 (superseded) | [CA-fp]+[P-sketch] | N16 conv_vec.py | lineN16 §1(c–d); defects F21-1/3 (lineN21) |\n| Lemma C; δ_true(G ≤ 15) ≤ 2.2102e-6 | [P] + [CA-fp] | N21 conv_c.py, f_postC.py | lineN21 ✓ (bit-identical spot reruns; own aggregation) |\n| Lemma Q, Lemma D^T; G ≥ 37 ≤ 1.0843e-7 | [P] + [CA]/[CA-fp] | N21 tail_DT.py | lineN21 ✓ (independent re-implementation, F1/F2 applied) |\n| δ_true (all G) ≤ 5.0313e-6 | [P] + [CA-fp] | N21 final_delta.py, LineN21Arith_v2.lean | lineN21 ✓; lineN21b ✓ (delta check, Lean 24 theorems, axioms) |\n| Lemma J; Prop. F; Thm A (j ≤ 14); Prop. K; λ-carry graph + renewal | [P]; [P mod N13 CA]; [CA-fp]; [P + CA mod H1-shell, span P-sketch]; [P, Lean] | N20 v2 | lineN20 ✓ (after fixes 1–7) |")
rep("| Step-norm table \\|t\\| > 1/256 | [CA-fp] | N15 | lineN15 §1a (method) |",
    "| Step-norm table \\|t\\| > 1/256 | [CA-fp] (20 cells [CA]) | N15 | lineN15 §1a (method); **lineN21b ✓ values independently recomputed** |")

# ---- §11 change log (N20 wrote "## 11. Changes v4 → v5 (Line N20, proposed)")
rep("## 11. Changes v4 → v5 (Line N20, proposed)","## 11. Changes v4 → v5\n\n### 11a. Line N20 (applied verbatim from N20/THEOREM_DRAFT_v4_to_v5_v2.diff, refereed lineN20)")
S=S.rstrip("\n")+"""

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
  - a referee pass on the A_bad^KP-in-exponent step and on this assembly;
  - p₁ with additive budgets;
  - registry changes (proposed only: `V5/CLAIMS_PROPOSED_v5.md`).
"""
open('/workspace/bgs-lineN/THEOREM_DRAFT_v5.md','w').write(S+"\n")
print('ok',len(S))
