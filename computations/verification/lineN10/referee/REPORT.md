# Referee report: Line N9 + N10 (with N7_v2, N8_v2 fix-application)
Grok Bot, 2026-10-31 22:50 (Asia/Yekaterinburg, UTC+5). Inputs are read-only. SHA256_N9 and SHA256_N10 verify OK. Nothing was pushed or modified outside /workspace/audit/lineN10.

## Verdicts
| Item | Verdict |
|---|---|
| REPORT_N7_v2: did it apply N7-F1..F11? | **Yes.** F1 (two-term B16 + monotonicity [P]), F2, F3 (budget δ=0.01, θ_a=.25, θ_b=.72), F6 (cross lines → (b′); A∞ restricted to γ/γ̄), F8–F11 and the 4-fixed-point erratum are all applied. The missed z=0, e=4 class is acknowledged. |
| REPORT_N8_v2 (N10 §5): did it apply N8-F#? | **Yes.** F3: R₂ is direct and matches N8 to 1e-9 (I re-read f3_r2direct.json). F6: the short-block r₂ table matches e_r2_cert.jsonl, and "not the bottleneck" is withdrawn. F7, F8 (339) and F9 are applied. F_m = 2.32e-3 is adopted. |
| **N9** | **READY after minor fixes** (N9-F1..F4). |
| **N10** | **READY after fixes** (N10-F1..F6). F1, F2 and F3 are required. |

## Independent re-checks (code/, logs/)
1. **Gas activities at new p, with exact twists** (`ref_gas.py`, p=37 and p=59). The script builds exact line points and runs the TW law with L=8, K=16. Both p have h_p ≠ h_29, h_47, so these are fresh p.
   - The family ratio is w* = 3.43580e-4 + 1.95796e-4i at both p, identical to N10.
   - **Two-bump activities.** At z=¼, a second bump βλ^g with β=√2 gives φ → 2.9866e-5 − 6.599e-6i = **c₀** to 5 digits by g=12–14 (p=59). With β=2 it gives φ → 1.0413e-6 − 3.1164e-6i = **c₄**.
   - The plateau is flat in g. The deviation at small gaps is mostly odd in the sign s. Example at g=5: the ± pair averages to 2.9886e-5 vs c₀ = 2.9866e-5, whereas the individual values are 2.918e-5 and 3.059e-5. So the leading pair interaction largely cancels in the ±-symmetric gas sum. This is consistent with N10's small S.
   - At p=37 the curve is the same, except g=14 (gap 4 to the B-core at k=18) is perturbed, as expected.
   - **Three-bump classes.** r/w*³ = 0.946−0.276i (4,9), 0.925 (5,12), 0.977 (6,15), 1.007 (7,18) and 1.005 (8,20). Each ± partner mirrors around 1. This confirms N10's 0.95/0.92 and shows convergence to multiplicativity.
   - c₀ and c₄ recomputed at p=37/59 agree with N9/N10 to all printed digits.
   - **Conclusion.** The bump-activity picture (φ_√2 = c₀, φ_2 = c₄, multiplicative 3-bump) is independently confirmed at two new p. The p-uniformity is striking: values at p=37 and p=59 agree to about 1e-9 relative.
2. **Closed form X(p)** (`ref_genfun.py`, own code; inputs w*, R taken from N10).
   - X(47): Re X = 0.070632 vs Lin 0.070208. ✓
   - X(1165) = 1.892+1.178i, |X| = 2.229. ✓
   - |X| ≥ 2 first at p=1065. ✓
   - min|1+X| = 1.00450 at p=3. ✓
   - min G = 1.0058 at p=3. ✓
   - Re X < 0 on 50.65% of odd p ≤ 2e5. ✓
   - **First Re X < 0.** With the closed form e^{pR}, I agree with p=4287. With the exact per-site product (1+R±2w*)^p, it is p=4291, and the relative difference between the two forms reaches 7% at large p. This is immaterial, but the "4287" should say which form it uses.
   - **R.** R recomputed from the four listed activities gives 6.1838e-5 − 1.9410e-5i, vs the stated 6.185e-5 − 1.943e-5i (0.1% off). This is harmless.
3. **N9 automaton** (`rerun_b_automaton.py`: an unmodified copy of N9's code, with only the log path redirected). V=12: λ-base 1.05193, ε-base 2.32608, reproduced exactly.
   - Sanity: ε-rate ≈ A₂/ε = 5.614/2.414 = 2.325. The joint constraint costs only one generic 1/ε per ε-letter. So the joint A+B rate is A₂²/λ ≈ 5.41 per λ-step, not r₂² ≈ 1.1.
   - The mechanism is real: cores A and B share one seed ζ, so they cannot be averaged independently.
   - **Self-correction.** The referee's N7 suggestion (bound the class by product majorants over the cores and average) does not close for this reason.
4. **CS inequality.** Σ_t|Z+E′_t|² ≥ |Σ_t(Z+E′_t)|²/n = n|Z|²|1+X+Y|² with Y = mean_t U_t/Z. This gives Dev_h ≥ (n|Z|²/h²)(|1+X+Y|² − 1). It is correct [P], and the only thing dropped is the t-variance, which is ≥ 0.
5. **Lean** (`lean/LineN10Arith.lean`, builds clean, no sorry/native_decide). It checks:
   - (1.42785/1.2744)³ ∈ (1.406, 1.4066) < 1+√2;
   - 2.32569² > 5.408 and 1.481² < 2.1934;
   - R components within 2e-8 / 3e-8 of the activities sum;
   - 4·47·Re(w*+c₀) = 0.070208;
   - modulus gain |X|²/(2ReX) ∈ (0.04400, 0.04402) at p=47, i.e. the +4.4%;
   - 0.769/1.915 ∈ (0.4015, 0.4016);
   - 8V k20 1.47591 < 1.4810 < 16E k20 1.48126;
   - μ*⁶/λ ∈ (8.47, 8.48).

## Answers to the specific questions
- **Is the gas derivation sound?** Combinatorially yes, as a model.
  - Per line, single odd bumps give p positions × 2 orientations = 2p family points. This produces the 2p inside sinh.
  - z=¼ requires an odd number of odd bumps, which produces the odd part, sinh. Even bumps (φ_√2 = c₀, φ_2 = c₄, …) enter as e^{pR} with R = 2Σφ.
  - The configuration with no odd bumps gives the z=0 classes (e^{pR} − 1, excluding the empty configuration = the zero point).
  - The overall factor 2 is the two lines γ, γ̄.
  - The small-p limit is 4p(w*+c₀+c₄). ✓
  - **What is not proved:**
    - (i) Coding: line points ↔ bump configurations, bijectively. A counting check shows the configuration count (≥3^p) exceeds q ≈ ε^p/2, so the map cannot be injective for dense configurations. Only dilute configurations (density ~2|w*| ≈ 8e-4, entropy ≪ log q) carry weight, so this is plausible but unproved.
    - (ii) Multiplicativity with a summable interaction (KP condition). It is measured to decay at 0.40/step, not proved.
    - (iii) Completeness of the activity list (deep/chaotic bumps), i.e. the A∞ tail again.
  - So X(p) is **[H, model]**, as N10 labels it.
- **Re-test at p=29/47 and new p.** Done at new p=37 and 59 (above), with full agreement. At p=29/47 the N10 logs agree with the same c₀/c₄ plateaus.
- **Is the |1+X+Y| use legitimate given Y?** The inequality is legitimate. Using it needs a bound |Y| < |1+X| − 1 − |X_tail|.
  - For **prime (squarefree) h_p**, Y consists only of unit points. |Y| = |Lin_unit|/(2n|Z|²/h²) is then bounded in absolute value by the same Theorem C′ estimate (rate 1.274 vs T′ = 1.428), so it is controlled.
  - For **composite h_p**, Y also contains the mixed classes (isotropic at one prime, unit at another) and the partially isotropic ones. These are exactly the open gap (b′), and N10 l.118's "Y (unit points)" is incomplete.
  - Cross-line points are isotropic, so they belong to X, not Y, and are also uncontrolled (b′).
  - So Y is controlled exactly where Lin already was, and nowhere more.
- **Is the m=141 consistency statement honest?** Essentially yes.
  - The comparison is model vs. model: the gas Re X 0.070632 vs Lin 0.070208, and the modulus gain +4.4% (Lean-checked).
  - The caveats are stated: full enumeration only for p ≤ 13, and at p=13 the direct 0.019429 lies between Lin and gas. My closed form gives X(13) = 0.019490, which matches the stated gas value 0.019492.
  - "W′/m ≈ 1.12e5" = 1.07e5 × 1.044 × ~1.006 is arithmetically right. It should be labelled [model], not presented as a recomputation.

## N9 findings
- **N9-F1 (scope).** "Fourier-majorant route fails" is right only for *this* majorant. The claim should read "the HS/op product majorant with joint ζ-averaging cannot close (5.409 vs 2.193 per λ-step) [CA*]". The rates are reproduced and the mechanism is genuine (shared seed), but it is not a proof that no Fourier route exists.
- **N9-F2.** The C′ deep-route index argument is correct ((1.42785/1.2744)³ = 1.4065 < ε, Lean-checked). It should state that it uses the *current* C′ rate 1.274. Any improvement of C′ below 1.42785/ε^{1/3} = 1.0657 would reopen the route, which is unrealistic but should be said.
- **N9-F3 (label).** The "p-uniform A∞ is false (5-bump terms reach the budget at p ≈ 6.4e3)" claim must stay **[H]**. It is a consequence of the gas model, not a counterexample.
- **N9-F4.** The z0_e4 certificate (Re w ∈ [3.546e-9, 2.079e-6]) is fine; my c₄ = 1.0413e-6 − 3.1164e-6i lies in it. The e4s2 class with indeterminate Re should be listed explicitly as an absolute-value budget item (|w| ≤ 4.24e-8), not as positive.

## N10 findings
- **N10-F1 (required).** Replace "Y (unit points)" (l.118) and the "trivially satisfied beyond" with the correct statement:
  - Y = unit + mixed + partially isotropic parts;
  - controlled by C′ only for squarefree h_p;
  - for composite h_p the (b′) classes enter Y and X and remain open.
  "Trivially" must go: it still needs C′ for every p.
- **N10-F2 (required).** l.77 "Dev ≥ F_m·G(p)·(1 − tail − Y)" is not a valid rewriting, because Y and the tail are complex and enter inside a modulus. The correct statement is Dev_{h_p} ≥ (n|Z|²/h_p²)[(|1+X_gas| − |X_tail| − |Y|)² − 1], valid when the bracket base exceeds 1.
- **N10-F3 (required).** The inherited levels d = e·h_p, e > 1, still enter through Lin, ∝ 2 Re X. They turn negative together with Re X.
  - Either apply CS per inherited level, or bound them by the positivity lemma Dev_d ≥ −n_d|Z|²/d².
  - The total weight is ≤ (I−1) ≈ 0.2 of level h_p. At large p this is dominated by |X|² (e.g. p=10001: −600 vs +3.2e6 in units of n|Z|²/h²), but it must be written into the bound.
- **N10-F4.** "Re X < 0 first at p = 4287": state that this is the closed form. The exact per-site product gives 4291. Both are [H, model].
- **N10-F5.** min|1+X| = 1.0045 and G ≥ 1.005 are attained at p=3, outside both the theorem range and the validity of the model (no room for a bump at p ≤ 13). Quote the minimum over the theorem range instead (p ≥ 29 at least).
- **N10-F6.** Fix the bookkeeping: R as stated is 6.185e-5 − 1.943e-5i vs 6.1838e-5 − 1.9410e-5i from the listed activities. Label W′/m ≈ 1.12e5 as [model].

## What stands between us and an unconditional refutation (updated)
1. **(a) A∞ tail, now in absolute form.** For every p in range, an absolute bound |X_tail(p)| ≤ |1+X_cert(p)| − 1 − |Y(p)|, where X_cert is a *proved* lower-bounded certified part.
   - The real-part (one-sided) version is false under the model for about half of large p, so it is dead.
   - Realistic shape: prove the gas structure (items 2–3) at least as an inequality, |X − X_gas| ≤ ε_p|X_gas|.
2. **Coding lemma [open].** Every isotropic line point is a unique bump configuration modulo the period, at least for configurations of density ≲ 1e-2, with an explicit bound on the weight of the rest.
3. **Cluster/KP bound [open].** An explicit, proved interaction decay. The measured value is 0.40/step and the ±-pair cancellation was observed here. The proved bound must be good enough that |X_gas| is bounded below, using the fact that sinh has no zeros on the ray arg 2pw* = 0.518.
4. **(b′) mixed / cross-line / partially isotropic classes at composite h_p [open].** They now enter both X and Y. The alternative is to restrict the theorem to p with h_p prime (or squarefree with C′), at the cost of a weaker statement that depends on primality.
5. **Theorem C′ for every p in range** (unit part of Y). [P+CA] for squarefree h_p as audited. The CA range must cover every p used.
6. **Inherited levels under CS** (N10-F3). Routine, but it must be written.
7. **Short cores, N(e) ≲ λ^{10}** (N8-F6 table: 8V needs k ≥ 20, 16E k > 20). These need their own route, e.g. direct certification of the finitely many short-core classes per p. This is finite work, but the p-uniform part is open.
8. **Hypothesis G(Γ < 1.2329, A) and the κ floor 0.7060** (two-block). Inherited from N8; unchanged.
- **Overall.** As of N10, the refutation remains **conditional**. The modulus route removes the sign obstruction but replaces it with absolute-value requirements (items 1–4), and these are where the real mathematics lies. Strongest positive evidence: the gas activities are reproduced at fresh p=37/59 to 5 digits and three-bump multiplicativity holds to within ≤ 8% at gap 4, improving with gap.

## Artifacts
- code/ref_gas.py
- code/ref_genfun.py
- code/rerun_b_automaton.py
- logs/ref_gas_p{37,59}.{out,json}
- logs/ref_genfun.json
- logs/rerun_b_automaton.jsonl
- lean/LineN10Arith.lean
- SHA256.txt
