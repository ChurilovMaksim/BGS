# Referee report — line N20 (H1 collision lemma; partial results, Prop. K)
Referee: Grok Bot (independent), 2026-11-01, 10:15–10:40 Asia/Yekaterinburg (UTC+5). Subject: /workspace/bgs-lineN/N20 (REPORT_N20.md, NOTES, code/, lean/, manifest, v4→v5 diff). Context: N15, N16, audits lineN15/lineN16, N21 v2.

## Verdict: **READY AFTER FIXES** (fixes 1–7 below; none changes a headline conclusion, but fix 1 changes printed numbers and breaks one Lean clause)

The negative findings hold up: H1 is not proved, the 633-state λ-system is only the single-window object, and an unrestricted joint torus/carry bound cannot give the H1 rate. Thm A and the Prop. K arithmetic reproduce to all printed digits. The main defect is that Prop. K's budget uses the old δ_true = 2.470e-6 (v4, G ≤ 15 only), not N21's δ_true ≤ 5.0313e-6. N21 v1 already had that value at 09:54, before N20's final tail_kp run (10:03).

## Tags each claim deserves
| Claim | N20 tag | Referee tag | Status |
|---|---|---|---|
| Lemma P0 (periodicity; d^A_t ≡ σ₁(μ)λ^t ≡ −σ₂(μ)λ^{−t}) | [P] | **[P]** ✓ | algebra checked; twists from the σ₁ branch for all t reproduce the c3_mid values on 12 classes |
| Lemma J: μ_B = −ε^{−1}μ_A, ε-adic joint relation, dual lattice | [P] | **[P]** ✓ | checked by hand: zB = −(√2−1)·zA exactly; trace-dual of (√2/4)O is O; Σu_kε′^k = 0 criterion is correct |
| Lemma J: \|e\| ≤ 51 sharp, 6145 states, 307 935 edges | [P, exact computation; Lean for Green bound] | **[P + exact integer computation]**. Lean only does the closed-form arithmetic (see fix 5) | reproduced: own BFS gives 6145 / 51 / 307 935, and box 60 gives the same; own Green ℓ¹ = 0.8535534 |
| "N15/N16 torus = iid to 1e-11 is not evidence for H1" | — | **correct (logical consequence of Lemma J)** | ✓ |
| [N] MC joint/iid 1.86, 3.6, 10.6 (n = 2, 3, 4) | [N] | **[N]** ✓ | own code (exact integer twist combinations, own exact S0): n=1 0.991±0.021; n=2 1.73±0.09 (N20 1.86±0.07, 1.2σ); n=3 3.95±0.48 (N20 3.64±0.32); n=4 not rerun |
| Prop. F lower bound 5.13e-7·λ^{−n} | [P with N13 CA] | **[P mod N13 [CA]]**, **only for n ≤ 10¹⁰** | arb: 5.1488e-7 ≥ 5.13e-7 |
| Prop. F ratio ≥ 4.31e-8·2.188ⁿ, > 1 for n ≥ 22, "→ ∞" | [P] | **[P mod N13 CA + N14 float 3.45]**, for 22 ≤ n ≤ 10¹⁰. "→ ∞" is not proved (fix 4) | arb: 4.3258e-8, 2.18843; n = 21: 0.60, n = 22: 1.32 |
| Corollary: no unrestricted bound gives H1 (ρ ≤ 0.414) | [P] | **[P]** (finite n suffices) | ✓ |
| Thm A: H1 shell law j ≤ 14, C ≤ 4.36e-4 | [CA-fp] | **[CA-fp], core functional only** | own arb aggregation reproduces every row; class counts = ideal counts; 12 classes recomputed |
| A_bad finite part j ≤ 14 = 2.0315895e-6 | [CA-fp] | **[CA-fp]** ✓ | own: 2.031589524e-6 |
| "C_cert decreasing for j ≥ 8" (v5 diff) | — | **false** (fix 3) | C(9) = 5.10e-5 < C(10) = 5.88e-5 |
| Prop. K: C ≤ 0.082 at J₀=12 ⇒ KP, a ≤ 2.70e-3 | [P + CA] | **[P + CA mod H1-shell + P-sketch (span ≤ 2j)]** | reproduced: a = 2.6925e-3, lhs 2.63970e-3 |
| Prop. K budget ≥ 2.76e-4 | [P + CA] | **wrong δ_true; ≥ 2.738e-4 with N21 v2** (fix 1) | own arb: 2.73804e-4 |
| Threshold correction 0.08168 | — | correct only under N14's dint = 1e-6 convention; **0.0813 with δ_true v2** | own arb: 0.081679 (N20 target); 0.081331 with (Re Λ′ − 5.0313e-6)/2 |
| Lemma R (renewal) | [P, Lean] | **[P, Lean]** ✓; the application is a framework with no certified ε_k | builds; axioms propext, choice, Quot.sound |
| Lemma G (633, \|e\| ≤ 14, ρ ≥ 20) | [P, Lean kernel decide] | **[P, Lean]** ✓ | builds (29 s), axioms [propext] only; own BFS 633 / 14 / 13 189 |
| O1 | [P]; threshold [N] | **[P]**; 0.012 **[N]**. Moot for H1 by Lemma J | ✓ |

## 1. Line-by-line proof checks
**Lemma P0.** Tr(μλ^t) = bx + ay ∈ ℤ for μ = b/2 + (a/4)√2 and λ^t = x + y√2, so σ₁(μ)λ^t ≡ −σ₂(μ)λ^{−t} (mod 1). ✓

**Lemma J.**
- digits.seeds gives zB = (−(a−b)/2, (a−2b)/4) = −(√2−1)·zA. This is an exact identity. ✓
- d^B_t = σ₁(μ_B)λ^t = −σ₁(μ)ε^{2t−1}. ✓
- Duality: L^∨ = ((√2/4)O)^∨ = (4/√2)·(1/(2√2))O = O. ✓
- Membership: (x, y) ∈ ι(O) ⇔ σ₂(x) = y ⇔ Σ_k u_kε′^k = 0. ✓
- x² − 2x − 1 is monic, so integer carries follow. ✓
- ‖g‖₁ = (1/(2√2))(1/√2 + (2+√2)/2) = (2+√2)/4. ✓ Confirmed by an explicit two-sided Green function (residual 6e-17).
- 60·0.85355 = 51.21. ✓
- Only the closed-path count (6145) is intrinsic. FW/BW counts depend on the box: 8377 at box 51, 10 147 at box 60. For λ: 769 at box 15, 1017 at box 20.

**Prop. F.** Every step was re-done in arb (`code/ref_propF.py`):
- Area Jacobian |ε′ − ε| = 2√2. ✓
- No reduction, since |τ_k| ≤ δ. ✓
- Σ|τ_k| ≤ δε/(ε−1) = 1.70711δ. ✓
- Exponent 0.030870. ✓
- Deviation 0.497546, giving |r| ≥ 0.502454. ✓
- Constant 5.1488e-7. ✓
- N13 inputs found in N13 logs:
  - Lip_H ≤ 167.2134;
  - resid_Phi_H 6.848e-16;
  - |1 − ψΦ| 1.746e-16;
  - nP = psi_dual = 1.0;
  - quadratic bound 4260 (refereed lineN13).
- Sanity [N]: at U_n corners (n = 2, 4, 8), |r_A|, |r_B| ≈ 0.99997. The bound is very conservative but valid.
- Caveat: the n·1.01e-12 term in the exponent restricts the proof to n ≤ 10¹⁰ (fix 4). The H1 conclusion needs only finite n (the ratio is > 1/C already at n ≈ 25), so the corollary stands.

**Thm A.**
- Class completeness: N20 per-shell class counts equal Σ_{m∈[2^j,2^{j+1})} Σ_{d|m} χ₈(d) for every j = 2…14, including 5100 (j = 13) and 10 225 (j = 14). Class number 1, units ±ε^ℤ.
- No duplicate classes across a_cert_ext and the three j = 14 shards. The sequential job's j = 13 log has no stray j = 14 rows.
- Own arb aggregation reproduces every S2_up, Σ|w|_up and C_cert (both ρ) to all printed digits:
  - max C = 4.3507e-4 (ρ = 0.2726), j = 5;
  - 3.9158e-4 (ρ = 0.28);
  - ℓ³ ≤ ℓ² holds per shell on the data.
- The float sums carry ×(1+1e-12) inflation. For 8487 terms, nu ≈ 9.4e-13 < 1e-12, so this is adequate but tight.

**Prop. K.**
- Σ|w| ≤ S2^{3/2} ✓; e^{aℓ} ≤ e^{a(2j+g₀)} ✓ (needs span ≤ 2j: [P-sketch]).
- Data: max span/j = 1.2 for bad classes with j ≥ 5, and max(span − 0.787j) = 2.77 for j ≤ 14 [N]. The report's "measured span/j ≤ 2" is true but loose.
- Σ_{j≥J} j r^j closed form ✓. I re-did it as a direct partial sum with a remainder bound.
- KP fixed point and arb check reproduced for (12, 0.082), (12, 8.8e-4) and (14, 0.082).
- C ≤ 1.78e-3 / 2.42e-3 / 3.29e-3 for T₀ ≤ 1e-6 reproduced.
- C_needed is computed at a = 0 (no e^{a(2j+g₀)} factor), matching N14's a_need convention. That is fine as a convention, but it should be said.

**Lemma R / O1.**
- The induction proof is correct.
- In the application, ΦΦ* ⪯ (Φ*Y_c⁻¹Φ)Y_c and |ψZψ*| ≤ ‖Z‖_{Y_c}·ψY_cψ* are correct. The induced order-unit norm is submultiplicative.
- Excursions have length ≥ 3: (0,0)→(0,c)→(c,0)→(0,0). So the "k ≥ 3" in the budget is right, and r = 0.30 gives a budget of 1/15. ✓

## 2. Independent computations (all in /workspace/audit/lineN20/code, logs in logs/)
1. `carries.py`, `green.py`: λ gives 633 / 14 / 13 189; ε gives 6145 / 51 / 307 935, unchanged with a larger box. Green ℓ¹ = 0.25 (λ) and 0.8535534 (ε).
2. `classcount.py`: per-shell class counts equal ideal counts (j = 2…14).
3. `ref_shell.py`: 12 classes, including the top-2 and 3 random classes at j = 13 and at j = 14, plus j = 8 and 12.
   - Method: own twists in mpmath (σ₁ branch for all t, μ_B = −ε^{−1}μ_A), own sparse operator in clongdouble.
   - Result: in all 12 cases (|r_A||r_B|)²_ref ≤ rArB2_up, with relative excess 2.6e-5 … 7.4e-4, consistent with the c3_mid radii.
4. `ref_propk.py`: Thm A table, A_bad, Prop. K table and thresholds in arb (numbers in §0 table).
5. `ref_mc.py`: own MC. Twists τ_k = (P_kτ₀ + Q_kτ₁) mod 1 with exact integer P_k, Q_k. Own i.i.d. reference S0 via the exact twist average K(Z) = Σ|c_n/s|²M_nZM_n* (equals N16's S0 to 1e-16).
   - n = 1: 0.991 ± 0.021;
   - n = 2: 1.726 ± 0.087;
   - joint/(product of single torus means) 1.79;
   - n = 3: **3.95 ± 0.48** (N20: 3.64 ± 0.32, 0.5σ).
   - n = 4 was not rerun (time and load).
6. `ref_propF.py`: Prop. F constants (§1).
7. **Lean**:
   - Both files rebuilt with `lake env lean` in /workspace/audit/lineN12/lean/proj after `lake exe cache get`. Nothing built from source.
   - LineN20.lean: 29 s, EXIT 0, no messages.
   - LineN20Tail.lean: 20 s, EXIT 0.
   - No sorry, admit, native_decide or implemented_by. `#print axioms` gives [propext] for the decide theorems and [propext, Classical.choice, Quot.sound] for the Tail theorems.
   - Semantics checked: `okb` ⇔ |c − 6b + a| ≤ 60 in offset coordinates; index 32 = (−14, −14); carry_cw is Collatz–Wielandt on the REACH-restricted graph.

## 3. Manifest and timestamps
- `sha256sum -c SHA256_N20.txt`: all 46 entries OK. The manifest covers every file except itself and its .sha256, which also verifies. THEOREM_DRAFT_v4.md is unchanged (mtime 03:46). The diff applies cleanly to v4 and reproduces scratch/v5_proposed exactly.
- NOTES entries are consistent with file mtimes:
  - carry_graph.json 09:09:16;
  - v1 Lean 09:13:54 + 8m19s ≈ 09:22;
  - shard outputs 09:58–09:59;
  - tail_kp 10:03:26;
  - Lean v2 10:13:13 with build log 10:13:32;
  - manifest 10:15:14.725, after REPORT and NOTES.
- No N20 jobs remain. run_ext.sh's j = 15 waiter is not running, and a_cert_ext15 never ran.
- Issues (fix 6):
  - The REPORT header says "09:00–10:04", but the work ran 09:06–10:15.
  - `code/joint_torus_mc.py` (mtime 09:40:08) was edited **after** logs/joint_torus_mc_n2.json (09:35:14). So the n = 2 headline number came from an earlier revision of the script. My rerun agrees within 1.2σ.
  - NOTES 09:22 "LineN20.lean §1–3 compiled (8m19s, no errors)" refers to v1, whose exit code was never captured. It is retracted only at 10:15.

## 4. Consistency with N21 v2 (δ_true ≤ 5.0313e-6, margin ≈ 88×)
**Prop. K does not use the new δ_true.** tail_kp.py and Lean `kp_*` hard-code 2.470e-6. With 5.0313e-6:

| case | budget left, N20 (δ = 2.470e-6) | with N21 v2 δ_true |
|---|---|---|
| J₀=12, C=0.082 | 2.764e-4 | **2.738e-4** |
| J₀=12, C=8.8e-4 | 6.186e-4 | **6.160e-4** |
| J₀=14, C=0.082 | 4.893e-4 | **4.867e-4** |

- KP itself is unaffected, since δ_true does not enter KP.
- Lean `kp_J12_C88e5`, second clause, **fails** with the new δ: 2.379785e-6 + 5.0313e-6 = 7.411e-6 > 6.234e-4/100. The margin at C = 8.8e-4 is ≈ 84×, consistent with N21's ≈ 88× at A_bad^KP = 2.063e-6.
- The half-budget threshold becomes C_needed(12) = 0.0813 (0.0812 if the finite part is also subtracted). v4's 0.082 is then about 0.8% above the convention, not 0.4%. Positivity and KP still hold at 0.082.

## 5. Required fixes
1. **Use δ_true ≤ 5.0313e-6 (N21 v2) in Prop. K**:
   - REPORT §0, §3.4 (last table column, "≥ 2.76e-4" → "≥ 2.73e-4") and §5;
   - tail_kp.py `budget_left`;
   - Lean `kp_J12_C082`, `kp_J14_C082` (swap the constant);
   - `kp_J12_C88e5`: replace "/100" by "/80" or drop that clause;
   - the v5 diff H3 row;
   - the threshold note: 0.08168 → 0.0813 under the half-budget convention with δ_true v2, stating the a = 0 convention.
2. **Prop. K tag**: "[P + CA mod H1-shell; span bound ℓ ≤ 2j + g₀ is P-sketch]". Change it in §0 and in the v5 §3 row "H1-shell ⇒ KP … [P + CA]". Background interplay and normalisation remain [P-sketch] as stated.
3. **Thm A wording**:
   - delete "decreasing for j ≥ 8" (v5 H1 row) and "C_cert is decreasing" (§3.1). Say instead "≤ 5.9e-5 for j ≥ 8, decreasing over j = 10…14";
   - state "core functional" next to every "H1 holds for j ≤ 14";
   - in the v5 H1 row, mark the 186× margin as a finite-part margin only. By Prop. F it says nothing about the tail.
4. **Prop. F scope**: "for every n" / "→ ∞" → "for 1 ≤ n ≤ 10¹⁰ (ratio > 1 for 22 ≤ n ≤ 10¹⁰)". Tag the ratio statement as using the N14 float constant 3.45 [N]. The lower bound alone is [P mod N13 CA].
5. **Lean attributions**:
   - `eps_green_l1` only equates two closed forms. The Green ℓ¹ evaluation and the 6145-state count are not in Lean. Change "Lean for the Green bound" to "Lean: closed-form arithmetic 60·(2+√2)/4 ∈ (51, 52)".
   - `l3_le_l2` is in LineN13Arith.lean (N13), not N20.
   - Mark the FW/BW counts (769, 8377) as box-dependent.
6. **Timestamps**:
   - REPORT header → 09:06–10:15;
   - note that joint_torus_mc.py was modified after the n = 2 run;
   - annotate NOTES 09:22 (v1 compile, exit code not captured).
7. **v5 diff**: carry fixes 1–4 into the H1 and H3 rows and §3. Add the N21 v2 cross-reference for δ_true in the H3 row.

Minor (optional):
- "measured span/j ≤ 2" → "≤ 1.2";
- list gen_lean_graph.py in §7;
- the 1+1e-12 summation inflation is tight for j = 14 (nu ≈ 9.4e-13); use 1+1e-11.

## 6. Overstatements found
- "H1 holds for every shell j ≤ 14": core functional only (H4 not run).
- "C_cert decreasing for j ≥ 8": false (fix 3).
- Prop. F "→ ∞": proved only for n ≤ 1e10 (fix 4).
- "Lean for the Green bound": arithmetic only (fix 5).
- Prop. K "[P + CA]": hides the span P-sketch (fix 2).
- Budget "≥ 2.76e-4": stale δ (fix 1).

Nothing else is overstated: H1 stays [H], H3 is conditional, and v1 Lean is correctly disclaimed.
