s=open('REPORT_N17b_v2.md').read()
def R(a,b,cnt=1):
    global s
    assert s.count(a)>=1, a[:80]
    s=s.replace(a,b) if cnt=='all' else s.replace(a,b,cnt)
R("# REPORT_N17b — H7","# REPORT_N17b v2 — H7")
R("*Line N17b, 2026-11-01 (Asia/Yekaterinburg, UTC+5). Nothing pushed. N14/N14b/N13b files are not edited; corrections are stated here.*",
"*Line N17b, 2026-11-01; **v2 written in Line N18b, 2026-11-01 (Asia/Yekaterinburg, UTC+5)** applying referee lineN15 (/workspace/audit/lineN15/REPORT.md §2: B1–B8, Lemma 1). The original N17b/REPORT_N17b.md is unchanged. Nothing pushed. Changes are listed in §9.*")
# B4 citations / inclusion
R("(m₀ = 15, [P given TRACE-199]).","(m₀ = 15, [P given TRACE-199]; registered as **TRACE-273**, proved for m ∈ [15, 20001] + monotonicity).")
R("  - So the threshold excludes **no** level for (±2,8) [P given TRACE-199].","  - So the threshold excludes **no** level for (±2,8) [P given TRACE-199; = TRACE-273].")
# B2
R("With the gas bound alone (tails = 0, n = h_p), the bracket is positive from p ≥ 1386, not from 1289 (G = 10.99 vs I-bound 12.85 at p = 1289).",
  "With the gas bound alone (tails = 0, n/h_p := 1), the bracket is positive for all p ≥ 1386 (first prime **1399**), not from 1289. At p = 1289: G = 10.99 vs the Robin bound at the exact K_p, 12.77. (v1 printed 12.85 from an approximate ln K_p.)")
R("""- **Bracket with the gas bound.** Take G ≥ (2(1+a)^p − 1)² − 1 with a = Re Λ_lo′ − δ_int = 6.2289e-4 (tails, Y, n/h_p − 1 ignored). Then G − I_bound > 0 first at p = 1386 (e_crossover.py; p = 1289: 10.99 vs 12.85; p = 1500: 15.72 vs 13.12).
  - With tails/Y/ε_16 the threshold moves up (≈1500 with the v1 budgets).
  - **Consequence:** the threshold p ≥ 1289 in v1 must become p ≥ max(p₁, p₀), with p₁ ≈ 1386–1500 [P-arith for the idealized number].""",
"""- **Bracket with the gas bound (B2-corrected form).**
  - Use the gas form G(p) = (2b^p − 1)² − 1 with b = (1 + Re Λ_lo′)·e^{−δ_int}, i.e. (1 + Re Λ_lo′)^p·e^{−pδ_int}.
  - v1/N17b's "(1 + Re Λ_lo′ − δ_int)^p" is the rewriting rejected in N11-F4: (1+a)e^{−δ} ≥ 1 + a − δ is false.
  - Equivalently b = 1 + a with a ≥ **6.22885e-4**, rounded down. N17b's 6.2289e-4 rounded a lower bound up (Lean `a_wrong_way`, lineN15).
  - Tails, Y, ε's are set to 0, and n/h_p := 1.
- **Crossover (N18b code/a_crossover_v2.py, logs/a_crossover_v2_d*.json) [P-arith: float evaluation with margin ≥ 2e-3 ≫ rounding, + monotonicity].**
  - **Envelope.** ln K_p ≤ (2p+1)ln ε for p ≥ 2, since K_p = 4h_p² + 3 ≤ (ε^p+1)² + 3 ≤ ε^{2p+1}. Robin's r(L) = e^γ ln L + 0.6483/L − 1 is increasing for L > 0.37, so I_p ≤ g(p) := r((2p+1)ln ε).
  - **Core δ_int = 5.14476e-7:** G(p) > g(p) first at the integer p = 1382 (margin 0.0152).
  - **True-functional δ = 2.470e-6** (N16 row 19, G ≤ 15 only): first at p = 1386 (margin 0.0023). This agrees with the referee's 1386.
  - **First prime 1399 in both cases.** With the exact Robin bound at K_p (big integers), there is no violation at any prime 1399 ≤ p ≤ 5000.
  - **Monotonicity beyond the scan [P].**
    - For p ≥ p* (= 1382 or 1386), G′(p) = 4x(2x − 1)·ln b with x = b^p is increasing in p, and G′(p*) ≥ 0.02188.
    - g′(p) = (2 ln ε/L)·(e^γ − 0.6483/L) ≤ 2e^γ/(2p+1) ≤ 0.00129 at p*, and decreasing.
    - So G − g is increasing on [p*, ∞) and positive at p*. Hence **G(p) > I_p for every p ≥ p***, in particular for every prime p ≥ 1399.
  - The v1/N17b remark "≈1500 with the v1 tail budgets" had no script and is **dropped** (B6). With nonzero tails/Y/ε the threshold p₁ is not computed.
  - **Consequence:** the threshold p ≥ 1289 in v1 must become p ≥ max(p₁, p₀-list), with p₁ ≥ 1399 (idealized) [P-arith].""")
R("""  - **Inherited levels (d = e·h_p, e | K_p) — yes, with hypotheses.** Their floors sum to ≤ I_p·S_ρ, I_p ≤ σ(K_p)/K_p − 1 ≤ e^γ ln ln K_p + 0.6483/ln ln K_p − 1 (Robin 1984, unconditional for K_p ≥ 3) [P].
    - G(p) := (2(1+a)^p − 1)² − 1 with a = Re Λ_lo′ − δ_int = 6.2289e-4 exceeds this bound for all p ≥ 1386 (e_crossover.py checks p ≤ 3000; for p > 3000 G grows exponentially while the bound grows like e^γ ln p) [P-arith, float evaluation].""",
"""  - **Inherited levels (d = e·h_p, e | K_p) — yes, with hypotheses.** Their floors sum to ≤ I_p·S_ρ, with I_p ≤ σ(K_p)/K_p − 1 ≤ e^γ ln ln K_p + 0.6483/ln ln K_p − 1 (Robin 1984, J. Math. Pures Appl. 63, Thm 2; unconditional for K_p ≥ 3) [P].
    - G(p) := (2b^p − 1)² − 1 with b = (1+Re Λ_lo′)e^{−δ_int} exceeds this bound for all p ≥ 1382 (core δ) / 1386 (true-functional δ); the first prime is 1399. See §2 for the envelope and monotonicity argument [P-arith].""")
R("""      With the v1 tail budgets the threshold moves to ≈1500.
""","""      With nonzero tails the threshold is not computed (the earlier "≈1500" is withdrawn, B6).
""")
R("(p ≥ 1386, hypotheses (i)–(iii))","(p ≥ 1386, first prime 1399, hypotheses (i)–(iii))")
R("Gas beats Robin (inherited levels) from p ≥ 1386 under stated hypotheses","Gas beats Robin (inherited levels) for all p ≥ 1386 (first prime 1399; corrected gas form, §2) under stated hypotheses")
R("- **Q2. Does the gas growth beat the divisor-type bound from p ≥ 1386?**","- **Q2. Does the gas growth beat the divisor-type bound from p ≥ 1386?** (gas form corrected per B2)")
# B3 Weil
weil_new="the Weil range — **status per TRACE-244/251/252/280–282 (B3):** OP is proved [P+CA]; Theorem W is proved under the standing inputs for m ≥ m₁ (m₁ not computed) and is non-vacuous only from p ≈ 8.3e25 (TRACE-252); TRACE-280/281 extend it (beyond-Weil range non-empty only for p ≥ 10^264.5; q ≤ p^C for p ≥ p₀(C), not computed); composite conductors are open (TRACE-282). **It removes nothing at any realistic p**"
R("the Weil range (TRACE-244/245, conditional on OP)", weil_new)
R("It is OPEN except d = 7 (Line J) and the Weil range (conditional on OP).","It is OPEN except d = 7 (Line J, TRACE-223) and the Weil range, which is proved under standing inputs but non-vacuous only for p ≳ 8.3e25 (B3).")
R("| Weil range | prime d with d ≤ q^{small} per Theorem W/W⁺ | covered conditional on OP (TRACE-244/245, as registered) |",
  "| Weil range | prime d in the Theorem W/W⁺ range | proved under standing inputs (OP proved, TRACE-244/251); non-vacuous only for p ≥ p_W ≈ 8.3e25 (TRACE-252; m₁ uncomputed); extensions TRACE-280/281; composite conductors open (TRACE-282). **Covers nothing at realistic p** |")
# B4 d=7 cite
R("| d = 7 | 7 \\| K_p always | covered as used","| d = 7 | 7 \\| K_p always | covered (TRACE-223) as used")
# B7
R("This is negligible for p ≳ 415 (constant from N7; [P-sketch]).",
  "Thresholds (B7): with N7's two-term B16 form, p₁₆ = 339; with the crude single-constant form, 498 (N7-F1). N17b's \"p ≳ 415\" had no stated source and is withdrawn. The base 0.97801 is confirmed (Lean `eps16`) [P-sketch for the assembly].")
# B5
R("""    - m = 39: −4.9e-3, always d = 7.""","""    - m = 39: −4.9e-3.
    
    At m = 21, 33, 39 the worst negative is d = 7. At m = 15 it is **d = 31 (−3.40e-3)** (B5; N17b wrongly said "always d = 7").""")
R("| m | ρ | d | class | Dev/(φm) | Dev/main | Dev/(S_ρ/m) |","| m | ρ | d | class | Dev/(φm) | Dev/main | Dev/(φS_ρ) [S_ρ units] |")
R("In S_ρ units the worst negative non-h_p value is d = 7 at every m (§2b).","In S_ρ units the worst negative non-h_p value is d = 7 for m ≥ 21, and d = 31 at m = 15 (§2b).")
# B8
R("| **K_p levels** | d \\| K_p, d ≠ 7 (or 7·…) |","| **K_p levels** | d \\| K_p, d ≠ 7, **including prime powers** (31² \\| K₅, 7² \\| K₇; N8b-F2) |")
R("ord_d λ = 3p (except q = 7, ord 3)","ord_q λ = 3p for primes q | K_p, q ≠ 7 (TRACE-265)")
R("- **Prime h_p** removes hp-div and mixed levels but **not K_p levels**.","- **Prime h_p** removes hp-div and mixed levels but **not K_p levels (including prime powers)**.")
R("- **Requirement (H7*).** For each level d < L_fl, d ∉ inherited:","- **Requirement (H7*).** For each level d < L_fl, d ∉ inherited (including prime-power levels such as 31², 7²; the floor analogue of L_fl is Prop K2, TRACE-238/275):")
# B1
R("""  - **Reconciliation [P, checked].** 7743 − 7371 = 372 = (23−2) + (353−2) = n_23 + n_353. These are exactly the units ≡ ν_ρ modulo one prime factor but not the other, i.e. the members of the hp-div levels d = 23, 353 in TRACE-206's bookkeeping (n_23 = 21 confirmed in b_exact_dev m = 11).
  - So S (CRT) is the correct h_p-level set, and the 372 points belong to H7 (hp-div class), not to the h_p level.""",
"""  - **Reconciliation (corrected, B1; referee enumeration at m = 33, lineN15 `CRT.diff_all_nonunit_nu = true`).** 7743 − 7371 = 372.
    - The 372 extra points in the N6 unit-t set are **non-unit residues ν** (ν ≡ 0 mod exactly one of 23, 353). TRACE-206 excludes these from every sum, so they belong to no level.
    - The equality 372 = 21 + 351 = n_23 + n_353 is a **coincidence of counts**. The hp-div members are a different set with the same sizes; in the N6 rule they are the 374 non-unit-t entries minus the 2 non-unit ν.
  - **n = 7371 stands** [P, Lean `crt_counts`, `nratio`: 7371/8119 = (21/23)(351/353)]. S (CRT) is the correct h_p-level set.
  - N17b's statement "the 372 points are the hp-div members" is **withdrawn**.""")
# Lemma 1
R("""- **Lemma 1** (sublattice separation), now [P] with:
  - (i) separation stated **per component**: the admissible set is a union of 2^{ω(d)} sublattices, and separation holds within each; the count gets the factor 2^{ω(d)} = d^{o(1)};
  - (ii) an explicit factor 8 from lifting through the inverse different (index of O^∨ ⊃ O, disc 8);
  - (iii) the Bowen count uses a partition into sub-boxes of side < separation, each containing ≤ 1 point per component.""",
open('code/lemma1_source.md').read().rstrip('\n'))
s=s.rstrip('\n')+"""

## 8. Registry citations (B4)
| Statement | TRACE |
|---|---|
| inclusion threshold, m₀ = 15 | TRACE-273 |
| h_p level included and open; scale 1.13287 | TRACE-271 |
| Prop K2 floor (analogue of L_fl) | TRACE-238/275 |
| rank 3p for primes q \\| K_p, q ≠ 7 | TRACE-265 |
| \\|μ_{1:3}\\| ≤ 1.2837144 [CA] (d = 7) | TRACE-223 |
| OP; Theorem W; extensions; composite conductors | TRACE-244/251; 252; 280/281; 282 |

## 9. Changes N17b → v2 (referee lineN15 §2)
- **B1:** §5(b) explanation corrected (372 = non-unit ν; counts coincide; n = 7371 stands).
- **B2:** gas form (1+Re Λ)^p e^{−pδ}; a ≥ 6.22885e-4 rounded down; crossover 1382/1386 (core/true δ); first prime 1399; monotonicity proof.
- **B3:** Weil-range status updated (§0, §2b, §3).
- **B4:** registry citations (§8).
- **B5:** worst negative at m = 15 is d = 31; table column relabelled.
- **B6:** "≈1500" dropped.
- **B7:** ε₁₆ thresholds 339/498 with source.
- **B8:** prime-power K_p levels in H7*.
- **Lemma 1:** written out (§6).
- **N16 input:** true-functional δ_int ≤ 2.470e-6 (G ≤ 15) used as the second crossover case.
- **§7 (p = 17 run):** status as of N18b — see NOTES_N18b.
"""
open('REPORT_N17b_v2.md','w').write(s)
print("ok")
