# Referee report — N15 (+REPORT_N14_v2), N17b, THEOREM_DRAFT_v2
Grok Bot · 2026-11-01, 03:07–03:30 Asia/Yekaterinburg (UTC+5). Nothing in /workspace/bgs-lineN was modified and nothing was pushed. All jobs ran at nice 19 with OMP=1. The p = 17 mixed run (N17b, PID 864667) was left alone.
Integrity: SHA256_N15.txt is 100% OK. SHA256_N17b.txt (paths relative to bgs-lineN, also covers THEOREM_DRAFT{,_v2}.md) is 100% OK, and its self-hash is OK.
Ground truth for registry claims: /workspace/audit/pr66/wt_main/record/claims.json (latest ledger on the box, TRACE-001..285).

## Verdicts
| Item | Verdict |
|---|---|
| **N15** (incl. REPORT_N14_v2) | **READY after minor fixes.** F14.1 is **closed**: the c3_mid derivation is genuinely rigorous under the stated IEEE + libm ≤ 1 ulp model. One required relabel (N15-F1, KP tail). |
| **N17b** | **READY after fixes.** Required: B1 (the 372-point identification is wrong), B2 (gas form), B3 (Weil-range status outdated). |
| **THEOREM_DRAFT_v2** | **NOT-READY for the integration PR.** About 20 corrections are needed (§3), including wrong numbers, an omitted hypothesis (cross lines), a reintroduced invalid inequality (N11-F4), an undefined p₀, outdated registry status, and one misdescribed datum (W′/m = +2.95). None of them changes the overall *conditional* conclusion. |

---
## 1. N15
### 1a. c3_mid rounding derivation (F14.1) — rigorous under the stated model ✓
I read `c3_mid.py`, `rig.py`, `nh_table_rig.py` and `digits.py` line by line. Checks:
- **Twist range and phase.** d = red(·) ∈ [−½, ½) is computed in mpmath at 34 digits, so |arg| ≤ 2π·30·½ holds as assumed. Empirically, on this box (numpy 2.5.4, complex exp → libm), over 6·10⁴ random (n, d):
  - phase-argument error ≤ 2.25u·|arg| (bound used: 4u);
  - cos/sin ≤ 0.513 ulp (assumption: 1 ulp);
  - total |ê(nd) − e(nd)| ≤ 160u, against the ε_c budget of 393u.
  (`code/ref_ulp.py`, `logs/ref_ulp.json`.)
- **Structure.** einsum inner length 55 and M = 53 add.at contributions (computed in code, not asserted). The ABSDIV upper-bound step is right.
- **Error recursion.** e_k = N_H e_{k−1} + ‖T‖·loc is the correct H-norm recursion. The decomposition v − v̂ = X(v − v̂) + (Xv̂ − fl X̂v̂) is right.
- **Final read-out.** ‖ψT⁻¹‖ ≤ ‖ψTi‖/(1 − η_T) uses T⁻¹ = Ti(TTi)⁻¹, which is correct. The ratio-error formula |A/P − â/P̂| ≤ E_a/(|P̂| − ε_p) + |â|ε_p/(|P̂|(|P̂| − ε_p)) is correct, and the 1e-15|r̂| term covers complex division (√2γ₄ ≈ 6.3e-16).
- **N_H table.** Cells use (‖S(c)‖ + ferr)/(1 − η_T) + Lip_H·h/2 with Lip_H the [CA] value 167.213 (N13), so the continuum is covered. Scaled repeated squaring bounds λ_max correctly.
- **Minor (no effect on any number):**
  1. **κ_der is computed in float as (1+x)(1+y)… − 1, which cancels.** The exact value is **5.8779e-14**, not the printed 5.862e-14 (Lean `kapd_bound` gives < 5.879e-14). This is harmless: KAP = 1e-13 + 2u ≥ κ_der + 3u (Lean `kap_slack`). Print the exact value.
  2. **Data rounding total.** M̂ mid-rounding contributes u and COEF0 contributes 2u, so 3u relative is needed while the code adds 2u. The max(1e-13, ·) slack of 4.1e-14 covers it, but state it.
  3. "|d − d̂| ≤ 2.3e-16|d|" should read ≤ u|d| + O(10⁻³³)·|x|, since mpmath's absolute error is not relative to d. Negligible.
  4. **Citations.** Higham Lemma 3.5 is the single-complex-op lemma. Cite the inner-product consequence (§3.6) explicitly. State the BLAS: OpenBLAS 0.3.34 zgemm, standard algorithm, no 3M or Strassen. State that einsum without `optimize` uses non-BLAS loops.
  5. In `psd_lower`, the subtraction term should be γ₁(‖W‖ + ‖P‖), not γ₁‖W‖. The difference is ~1e-19, against a margin of 3.5e-6.
- **Cross-check against arb.** c3 midpoints equal c2 midpoints exactly, and the radius ratio is ≤ 6.94. Against the partial arb replay (1194 windows): 0 disjoint. On the 270 arb-tighter windows, max |mid diff|/rad_c3 = 1.25e-6 (`logs/ref_c3.json`).

### 1b. δ_int ≤ 5.14476e-7 ✓
- My own arb code (`code/ref_dint_arb.py`) on c3_mid boxes, using acb `**3`, gives **5.1447502e-7** and reproduces f_post3 exactly.
- With z·z·z (dependency blow-up) the enclosure is 5.144780e-7. That is also valid, just looser. The quoted bound is correct.

### 1c. ρ̄ ≤ 0.28 residual certificate (b_cp3) ✓
- λ_min(W) ≥ minΛ(1 − ‖V*V − I‖) − ‖R‖ is valid (minΛ ≥ 0, square V).
- 𝒦(Y_c) ⪯ 0.28Y_c with Y_c ≻ 0 gives ρ ≤ 0.28 (CP Perron–Frobenius).
- The same Y_c was certified independently in lineN14 by extended-precision Cholesky.
- Margin 3.49484e-6 vs 3.1e-13 ✓.
- ρ̄_true ≤ 0.280280 is the arithmetic of the (1+t)/(1+1/t) bound, which is **[P-sketch]**: the bound ΣΔΔ* ≤ (Pert/|s|)² is not written out. The label is honest.

### 1d. KP weight
- **The numbers check:** S₀ + S₁/(1+g₀) ≤ a holds for g₀ = 2..6 (Lean `kp_g2..g6`), and A_bad^KP + δ_int = 2.5774e-6 (Lean `kp_budget`). The 1D anchoring and incompatibility count are fine.
- **N15-F1 (required, label).** `kp.py` enters the j > 12 tail as TAIL = 1.56e-8, "Lemma D tail of 2Σ_{j>12}|w| (referee-confirmed)". That is a **misattribution.**
  - Lemma D (N13/N14) bounds the **interaction** tail beyond G₀ = 16 inside δ_int (H2).
  - The A_bad tail j > 12 is the **open collision lemma (H1)**, currently "≲ 4e-9 [H: extrapolation]" (N14 l.11).
  - 1.56e-8 is a conservative placeholder, not a proved bound. Relabel: "KP holds [CA-fp finite part j ≤ 12; tail j > 12 = H1, [H] placeholder; P-sketch tail ℓ-weighting and background interplay]".
- **N15-F2 (minor).** "Per-site log-correction ≤ S₀(a)" needs the anchored-cluster corollary of KP, not the bare KP condition. Cite it precisely (e.g. Kotecký–Preiss 1986 plus the standard anchored corollary; Ueltschi 2004; Fernández–Procacci 2007).

### 1e. Collision reduction |e| ≤ 15 [P] and torus-mean identity [P] ✓
- x² − 6x + 1 is monic and irreducible, so the Gauss lemma gives E ∈ ℤ[x]. Uniqueness of the bounded solution follows because λ^t and λ′^t are unbounded on ℤ.
- Green kernel: g(k) = λ^{−|k|}/(4√2) with Σg = 1/4 (Lean `green_ratio`, `green_sum`: (λ+1)/(λ−1) = √2).
- The torus identity is correct: (d_t, d_{t+1}) is uniform on T² because the cat map preserves Haar measure. The e ≡ 0 part is the i.i.d. 𝒦ⁿ.
- **Improvement (N15-F3, recommended).** v is finitely supported and g > 0, so |e_t| < 15 strictly, hence **|e| ≤ 14**. Exact reachability (states (e_{t−1}, e_t), |v| ≤ 60, closed paths from and to (0,0)) gives max|e| = 14, 29 values, and **633 reachable pair states, not 961** (`logs/ref_arith15.json`). This cuts the planned certificate by about 34%.

### 1f. Carry prefactor non-convergence ✓ (honest)
- 1/share = 4.26, 6.67, 8.67, 10.74 ✓.
- E = 3, 4 rates are 0.2725510 and 0.2725499 (log) ✓.
- The extrapolation to about 33 at E = 15 is [H] and correctly labelled.
- The ≈190× margin is 0.082/4.4e-4 = 186 ✓.

### 1g. Wrap-around exponent correction ✓
- Reproduced:
  - ρ̄ = 0.28028: q = 0.30982, ln(1/q) = 1.17178, i.e. 0.66475·ℓ₀/log_λ d;
  - ρ̄ = 0.30: q = 0.37992, ln(1/q) = 0.96780, i.e. 0.54903·ℓ₀/log_λ d.
  (Lean `wrap_q_028028`, `wrap_q_030`.)
- The brief's "0.97·ℓ₀/log_λ d" indeed mixes ρ̄ = 0.30 with the wrong log base. The correction is right.
- Label the statement as conditional on the subgroup second-moment lemma **and** the cluster-language second-moment certificate (H1), since q = (λρ̄²)^{3/2} comes from the ℓ³ ≤ ℓ² step of lineN13 §2e.

---
## 2. N17b
**Independent checks**
- **(a) Exact Dev_7 at m = 15, 21, 33, 39** (`code/ref_d7.py`). Own y′, own twists over **all 49 β** with no symmetry reduction, own member set and φ(2h); only the refereed twb transfer law is shared. All 8 table values reproduce to the printed digits:
  - m = 15: +1.197e-3 / +3.991e-2;
  - m = 21: −1.286e-2 / −1.271e-2;
  - m = 33: +9.418e-3 / −7.184e-4;
  - m = 39: −1.930e-2 / −8.456e-3.
  The β → β′ and β → −β symmetries used by d_g3dev hold to ≤ 3e-18 relative.
- **(b) Crossover.** Exact K_p (big integers), Robin bound, and the *correct* gas form (1+R)^p·e^{−pδ}: first p = **1386** (first prime **1399**). G − I_bound stays increasing through p = 5000. At p = 1289: 10.99 vs 12.85 ✓.
- **(c) Inclusion threshold.** m₀ = 15 confirmed exactly for odd m ≤ 399 (Lean `incl_15`, `incl_13_fails`). This is already registered as **TRACE-273** (proved, m ∈ [15, 20001] + monotonicity). Cite it.
- **(d) K_p facts.** h_{3p} = h_p(4h_p² + 3), 7 | K_p and gcd(h_p, K_p) | 3 for all primes 5 ≤ p ≤ 400 (Lean for p = 5, 7, 11, 13). Scale (μ²/ε^{4/3}) = 1.13288 (TRACE-271: 1.13287). ε₁₆ base 0.97801 (Lean `eps16`). Nicolas–Robin exponent at p = 1386 ≈ 476 ✓.
- **(e) Robin citation.** Robin (1984), J. Math. Pures Appl. 63, Théorème 2: σ(n)/n < e^γ ln ln n + 0.6483/ln ln n for n ≥ 3, unconditional; the constant is 0.6482…, attained near n = 12. Applied to K_p this is appropriate, since Σ_{e|K_p, e>1} 1/e = σ(K_p)/K_p − 1 dominates the inherited floors (n_d ≤ d). The Nicolas–Robin 1983 τ bound is cited correctly.
- **(f) Structure.**
  - The TRACE-213 identity is correct.
  - NR ≥ −RMT ≥ −4m holds (RMT_m = 4m − m²/h).
  - The floor −(h_p/d)S_ρ is correct.
  - The H7* formulation and the → ∞ step are sound bookkeeping: R′ is "W′ = o(m)" (TRACE-206), so B_p ≥ κ along an infinite set refutes it.

**Findings**
- **B1 (required): §5(b) misidentifies the 372 points.** The arithmetic 7743 − 7371 = 372 = 21 + 351 is right, but the 372 extra points in the N6 unit-t set are **non-unit residues** (ν ≡ 0 mod exactly one of 23, 353). TRACE-206 excludes them from every sum. They are **not** the hp-div members.
  - The hp-div members are a different set with the same counts: n₂₃ = 21, n₃₅₃ = 351. In the N6 rule they are the 374 non-unit-t entries minus the 2 non-unit ν.
  - Verified by enumeration at m = 33 (`CRT.diff_all_nonunit_nu = true`).
  - The conclusion (S = CRT, n = 7371) stands. Correct the explanation here and in THEOREM_DRAFT_v2 §7.
- **B2 (required): gas form.** N17b writes G ≥ (2(1+a)^p − 1)² − 1 with a = Re Λ_lo′ − δ_int.
  - That is the rewriting already rejected in N11-F4: (1+a)e^{−δ} ≥ 1 + a − δ is false. Use (1 + Re Λ_lo′)^p·e^{−pδ_int}.
  - Also, a = 6.2289e-4 rounds a *lower* bound **up**: the true value is 6.22886e-4 (Lean `a_wrong_way`).
  - The numerical effect is nil (still 1386), but the statement must be fixed.
  - Add the explicit monotonicity argument beyond the scan, and say "first prime 1399".
- **B3 (required): Weil-range status is outdated.** In the current ledger:
  - OP is **proved** [P+CA] (TRACE-244/251);
  - Theorem W is proved under standing inputs for m ≥ m₁ (*not computed*), and is **non-vacuous only from p ≈ 8.3e25** (TRACE-252);
  - TRACE-280/281 extend it (beyond-Weil range non-empty only for p ≥ 10^264.5; q ≤ p^C for p ≥ p₀(C), not computed);
  - composite conductors are open (TRACE-282).
  "Covered, conditional on OP" must become "proved under standing inputs, but only for p ≥ p_W (uncomputed, ≳ 8e25); removes nothing at any realistic p" (cf. N6-F8).
- **B4 (minor): cite the registry.** TRACE-273 (inclusion), TRACE-271 (h_p level included and open; scale 1.13287), TRACE-238/275 (Prop K2 floor analogue of L_fl), TRACE-265 (rank 3p for primes of K_p ≠ 7), TRACE-223 (|μ₁:₃| ≤ 1.2837144 [CA]).
- **B5 (minor): wording.**
  - §2b says "always d = 7". At m = 15 the worst negative (±2,8) non-h_p value is d = 31 (−3.40e-3).
  - The table header "Dev/(S_ρ/m)" actually lists Dev/(φS_ρ), i.e. S_ρ units. Rename it.
- **B6 (minor).** "≈1500 with the v1 tail budgets" has no script. Archive one, or label it [N, unverified].
- **B7 (minor).** ε₁₆ "p ≳ 415": state the B16 form used. The two-term form gives p₁₆ = 339; the crude single-constant form gives 498 (N7-F1).
- **B8 (minor).** K_p levels include **prime powers** (31² | K₅, 7² | K₇; N8b-F2). H7* must say so.
- **Lemma 1.** The v2 fixes (i)–(iii) are stated correctly, but only as bullets. The full proof still has to be written in the integration PR.

---
## 3. THEOREM_DRAFT_v2 — line-by-line (required unless marked minor)
Checked against lineN5…lineN15 and the pr66 ledger.

1. **§0 "no single one is close to routine except H6 (explicit p₀) and possibly H4": overclaim.**
   - H6 also contains h_p squarefreeness (a Wieferich-type open question, N3-F8).
   - H4 has no working route: N15 §5 shows the H-product route is vacuous (GA 40–340), and the vector-chain version is untested with an expected ~1e4× radius growth.
2. **§2 B_p uses (1 + Re Λ_lo′ − δ_int)^p.** This is the N11-F4 error; use (1 + Re Λ_lo′)^p·e^{−pδ_int}. Its p₁ "= 1386 [arith]" is confirmed with the corrected form (first prime 1399). Say "n/h_p := 1", not "n = h_p", and label it [P-arith, float + monotonicity].
3. **§2 lines 48 and 50:** a duplicated "(Formula …)" paragraph with contradictory δ_int (5.14416e-7 vs 5.14415e-7). Both are superseded: use **δ_int ≤ 5.14476e-7** [CA-fp: IEEE std model + libm ≤ 1 ulp; c3_mid, derived constants; confirmed lineN15]. Update H2 and §3 accordingly.
4. **§2 "p ≥ max(p₁, p₀)": p₀ is undefined.** List every threshold:
   - C′'s e^{o(p)} p₀ (uncomputed);
   - Prop X′ 1289 (a choice, N8-F5);
   - ε₁₆ (N7: 339 two-term);
   - TRACE-227 m ≥ 243, TRACE-271 m ≥ 495;
   - any Theorem-W threshold if Weil coverage is invoked.
5. **Missing hypothesis: cross lines.** At composite h_p there are 2^ω − 2 further fully isotropic lines (N7-F6; lineN10 item 4, lineN11 item 4). They lie in X, not in Y_mix, are not coded by the γ/γ̄ gas, and appear in no H-row. Add them to H5 (or H1) explicitly. They vanish on 𝒫.
6. **H1 row.**
   - "≈150× margin" is the N14 *budget* margin. The collision-constant margin is 186× (C_emp 4.4e-4 vs 0.082). Say which.
   - Add the N15 outcomes: reduction to |e| ≤ 15 [P] (sharp 14, 633 states); torus identity [P]; prefactor non-convergence [N]; lemma OPEN.
7. **H2 row.** The δ_int value and label must follow item 3. The text "referee F14.1" is now "closed by N15 c3_mid (lineN15)".
8. **H3 row.** Now explicit (N15 §4): a = 5.93e-6 at g₀ = 4, KP holds on the [CA-fp] finite part. The tail j > 12 is H1 ([H] placeholder 1.56e-8, see N15-F1). KP–background interplay and tail ℓ-weighting are [P-sketch].
9. **H4 row.** Add "H-product route vacuous (N15 §5); vector-chain version needed".
10. **H5 row.**
    - "Proved: c_B = 0.7375 [P-sketch]" is contradictory wording. Write "established at [P-sketch] (asymptotic, constants ignored)".
    - p = 31 belongs here, as a balanced semiprime with θ_max = 0.250 < 0.262, **not** in the 𝒫 bullet of the subsequence version, where it currently reads as if 31 ∈ 𝒫 (h₃₁ = 424577·865087).
11. **H7 row.**
    - Weil range: B3 above (OP proved; non-vacuous only for p ≳ 8.3e25; m₁ uncomputed; composite conductors open).
    - d = 7: cite TRACE-223, and carry the TRACE-215/217 caveat that the (±2,16) level-7 members are handled via N7/TRACE-227.
    - Inclusion: cite TRACE-273.
    - Add prime-power K_p levels.
12. **H8 row.** "e^{1.175ℓ₀} = λ^{0.667ℓ₀} (ρ̄ = 0.28)" rounds a coverage constant up: it is 0.6664. With ρ̄_true = 0.28028 it is 0.6647 (N15). State the dependence on the subgroup second-moment lemma and on H1.
13. **Subsequence version.**
    - (a) Dropping H6's "level 7h_p unit points" clause (N3-F9) needs a sentence. It is now subsumed by the inherited-level floor I_p (7 | K_p, 7h_p = e·h_p), and that is also true off 𝒫.
    - (b) "H8 reduces to H1" is [P-sketch]; label it.
    - (c) The K_p-level H7* must include prime powers.
    - (d) Also require p ≥ p₁ (≥ 1399) and the item-4 thresholds.
    - (e) Infinitude of 𝒫 is equivalent to the failure of R_NSW (TRACE-210). Worth one line of context.
14. **§3 table labels.**
    - Prop X′ → "[P mod Line F certs + class CA], certified classes only; k-parity mechanism and E-family absorption [P-sketch]" (N8-F3/F4).
    - (±2,16) → "[CA]+[P], mod J3 rig_spec spectral containment" (N7-F2).
    - Theorem C′ → "[P + CA* mod H6]" (Λ is [CA*], lineN3).
    - Lemma P′ → "with the 4-fixed-point correction (N8b-F3)".
    - Lemma 1 → "[P] once the stated fixes are written out" (the draft's own [P] definition requires a written, refereed proof).
    - 4-fold automaton: 5.41151 is [CA] per N10b, but the referee only reproduced it in float (lineN10, 5.41) → "[CA (author), CA* (referee)]".
15. **§3 adapted norm.** The quadratic bound is **1 + 1.01e-12 + 4260t²** on |t| ≤ 1/256 (lineN13 partition proof), not "1.0e-12 + 4.26e3t²" unqualified. For |t| > 1/256 the bound is now the N15 SVD-free table [CA-fp].
16. **§3 rows for δ_int, ρ̄ and A_bad.** Replace them with:
    - δ_int ≤ 5.14476e-7 [CA-fp];
    - ρ̄ ≤ 0.28 eigen-solver-free residual certificate [CA-fp] (core→true 0.28028 [P-sketch]; tensor claim [H]);
    - A_bad j ≤ 12 re-run with c3 radii, 2.031569e-6 at g₀ = 4 [CA-fp].
17. **§4 "e.g. W′/m = +2.95 at m = 57": misdescribed.**
    - m = 57 is p = 19, outside "p ≤ 13 full enumeration".
    - +2.95 is the TW-law [N] estimate of the **h_p-level isotropic deviation** alone (lineN5 table), not an exact W′/m.
    - Either remove it or relabel it accordingly.
18. **§6 additions.**
    - c2_mid radii (superseded by c3_mid).
    - N17b §5(b)'s "372 = hp-div members" (wrong, B1).
    - N15 kp.py's "Lemma D tail" attribution (N15-F1).
    - v2's own "conditional on OP" for the Weil range (B3).
19. **§7.**
    - The referee bullet about 7743/7371 must be corrected (B1).
    - "δ_int printed as 5.14416e-7" and "ρ̄ needs a-priori constants or arb" are superseded (closed by N15).
    - "What remains" item 4 (rigorous c2_mid constants) is **closed**.
20. **Minor.**
    - Assembly note: I checked the ⇒ chain: TRACE-213 identity, NR ≥ −4m, the CS inequality at h_p, floors, H7* via the positivity lemma Dev ≥ Lin, and (±2,16) via N7. It is correct bookkeeping *given* items 2 and 5. It can be labelled "[P mod inputs]" once those are fixed.
    - The "15 small-depth classes" matches N8 (near-0 + 14) ✓.
    - C′ rates 1.27440 / 1.20428 ✓.
    - NSW list not re-checked this round.
    - h₁₅ = 7·31²·41 ✓ (Lean).
    - K_p identity ✓.

---
## 4. What remains for an unconditional refutation (updated)
1. **H1 collision lemma.**
   - A phase-keeping certificate for the carry system: now 633 pair states with |e| ≤ 14, not 961. Or an analytic Gram tail.
   - The box/aliasing constants of the Poisson reduction.
   - Its constant must be ≤ 0.082 at J₀ = 12. The tail j > 12 enters KP (N15-F1).
2. **H4 composite core→true** in vector-chain form (the H-product route is vacuous).
3. **H5 composite h_p.** Subgroup-C′ with c < 0.387 (R-mix) **plus cross lines and partially isotropic points**; or restrict to 𝒫 (whose infinitude is open, ⇔ ¬R_NSW).
4. **H7*.** Signed control at hp-div, mixed and **all K_p levels (incl. prime powers)** below L_fl = h_p^{1+o(1)} at rate < T′ = 1.42785. This is needed even on 𝒫. Theorem W/W⁺ covers nothing at realistic p.
5. **H6.** Explicit C′ p₀; h_p squarefree or conductor-q^a weights. The 7h_p clause is now subsumed by the I_p floor.
6. **Writing.**
   - KP corollary citation and background interplay (H3);
   - Lemma 1 written out;
   - Lemma 2 [P-sketch] → [P];
   - k = O(1) stays;
   - the R₄ automaton;
   - explicit p₀ list and p₁ with all budgets.
7. **Closed in this round:** F14.1 (c3_mid rigorous under the IEEE + libm model); ρ̄ eigen-solver-free; δ_int ≤ 5.14476e-7.

## 5. Lean (`lean/LineN15Arith.lean`; lineN12 project, mathlib cache; EXIT 0; no sorry, no native_decide; log `lean/build.log`)
- hP recursion: h_{3p} = h_p(4h_p² + 3) and 7 | K_p for p = 5, 7, 11, 13; h₁₅ = 7·31²·41; h₁₁ = 23·353.
- tot8119 (φ = 7744); crt_counts; nratio (7371/8119 = (21/23)(351/353)).
- epsc_bound, kapd_bound (< 5.879e-14), kap_slack.
- kp_g2..g6, kp_budget.
- dint_round, a_wrong_way.
- green_ratio, green_sum, carry_bound.
- wrap_q_028028, wrap_q_030.
- eps16.
- incl_15, incl_13_fails.

## 6. Artifacts (/workspace/audit/lineN15)
- **code/:** ref_c3.py, ref_dint_arb.py, ref_ulp.py, ref_d7.py, ref_arith15.py
- **logs/:** ref_c3.{json,out}, ref_dint_arb.json, rerun_f_post3.json (the authors' f_post2 on c3_mid, output in my directory), ref_ulp.{json,out}, ref_d7.{json,out}, ref_arith15.{json,out}
- **lean/:** LineN15Arith.lean, build.log
- **SHA256.txt**
