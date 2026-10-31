# Referee report: Line N11 (+ N9_v2, N10_v2) and Line N9b (+ N8b_v2 §6)
Grok Bot, 2026-10-31 23:35 (Asia/Yekaterinburg, UTC+5). Inputs are read-only. SHA256_N11 and SHA256_N9b (and their .sha256 files) verify OK. Nothing was pushed or modified outside /workspace/audit/lineN11.

## Verdicts
| Item | Verdict |
|---|---|
| N11 §7, REPORT_N9_v2: N9-F1..F4 applied? | **Yes**, all four. |
| N11 §8, REPORT_N10_v2: N10-F1..F6 applied? | **Yes.** F2 and F3 are built into Theorem N11. Small attribution error in F6 (N11-F7). |
| N9b §6, REPORT_N8b_v2: N8-F2, F6, F7, F8 applied? | **Yes**, plus the 0.52% bonus. Open: the h_13 inconsistent line has not been redone under G\*. |
| **N11** | **READY after fixes.** F1, F2 and F6 are required. |
| **N9b** | **READY after fixes.** F2, F3 and F6 are required. |

**Self-correction.** In my N10 report I endorsed the sinh combinatorics and wrote that background 0 carries only the configurations with no odd bumps (e^{pR} − 1). That was wrong. N11's erratum is right, and it is independently confirmed below.

## Independent re-checks (code/, logs/)
1. **Corrected gas formula at p=37 and p=59, exact twists** (`ref_gas2.py`, derived from my N10 `ref_gas.py`).
   - **Parity.** Every 2-odd-bump and 4-odd-bump e = 2(1 ± ε^n …) lies on z = 0 and not on z = ¼. Every 3-odd-bump and odd+√2 configuration lies on z = ¼ and not on z = 0. This is exactly N11's parity rule.
   - **Two odd bumps on background 0.** r/w\*² at ε-gap n = 8, 10, 11, 12, 14, 16, 20, 24 is:
     - 1.026−.254i / .941+.222i (n = 8);
     - 0.919 / 1.083 (n = 10);
     - 1.0002 (n = 11);
     - 0.976 / 1.024 (n = 12);
     - 1.007 / .993 (n = 14);
     - 1.005 / .995 (n = 16);
     - .9993 / 1.0007 (n = 20);
     - 1.0001 / .9999 (n = 24).

     These values are identical at p = 37 and p = 59. The ± partners mirror around 1, so the leading interaction is odd in the sign and cancels in the gas sum.
   - **Other configurations.**
     - Three odd bumps on z = ¼: r/w\*³ = 0.90/1.11 (gap 10/12), 0.98/1.02, 1.01/0.99.
     - Odd + √2 bump: r/(w\*c₀) = 0.998 → 1.000.
     - Four odd bumps on z = 0: 0.96 at p = 59. At p = 37 it is 0.51−0.65i, because the wrap-around gap is only 3 ε-steps (< g₀ = 5). That is the expected close-range breakdown.
   - **Conclusion.** X = 2[(1+Λ)^p − 1] is confirmed in structure [N].
2. **Corrected closed form** (`ref_genfun2.py`). Reproduced:
   - Λ = 7.4901e-4 + 3.7216e-4i;
   - first Re X < 0 at p = 4099 (product form) / 4097 (exp form);
   - Re X < 0 for 50.75% of odd p ≤ 2e5;
   - min over p ≥ 29 of |1+X| = 1.04402;
   - X(47) = 0.071324 + 0.036207i;
   - |X(1165)| = 3.086, |X(10001)| = 3577.
3. **Re Λ_lo = 6.23837e-4.** Reproduced exactly from the archived enclosures: 2(Re_w_lower of fam 2.88369e-4 + near0 2.35882e-5 + z0_e4 3.5457e-9) − 2·|w(e4s2)| (4.2424e-8).
   - The lower bounds 2.468 (p=1289), 4.962, 43.21 and 1020 are reproduced.
   - Lean proves > 2.45 at p=1289 and > 41 at p=5000 by chunked Bernoulli.
4. **κ certificates.** In the Line F cert_lift reruns, certified = True. r₂ = 0.80 exceeds the certified Y-block root 0.76905 (measured 0.769/1.915 = 0.4016). κ = 0.80/μ\*_lo = 0.41765 and 0.85/μ\* = 0.443755, which N11 rounds to 0.44376. All of this is consistent.
5. **Coding constants** (Lean).
   - c_min = 3 − 2√2 ✓ and g₀ = 5 ✓ (8/(ε⁵−1) < 3−2√2).
   - **G₀ is not 6** (N11-F2).
   - ε^p ≡ ±1 mod γ̄ is checked exactly at p = 29 (−1), 47 and 59 (+1).
6. **Completeness phase check** (`ref_match.py`, on N11's t_classes_p47_N2000.json). See N11-F1.
7. **N9b reruns.**
   - `rerun_a_per.py`, n ≤ 5: Γ_per table rows 1–5 reproduced exactly.
   - `rerun_f_Rs.py`, n ≤ 5: R₂ 1.0002, R₃ 1.4019, R₄ 2.3984 ✓.
   - `ref_US.py`, my own code: small-β unit points at p = 23 and 41. β = ±1±√2 (= ±ε^{±1}) gives |r| = 1.31543e-3 at both p, identical to 1e-8. β = ±3±3√2 gives 1.4527e-4. So the counterexample to G is reproduced.
8. **Lean** (`lean/LineN11Arith.lean`, builds clean, no sorry/native_decide). It checks:
   - the Λ components and Re Λ_lo;
   - bound1289 and bound5000;
   - c_min, g₀, ε⁵, ε⁶, ε⁷, and G₀ for coefficient bound B vs 2B;
   - κ (0.85 and 0.80) and κ > 0.4016;
   - the US Γ_eff (1/8: 1.102) and Γ_raw (p=61: 1.847);
   - |r_US| > |w\*| and |r_US| > Re Λ.

## N11 findings
- **N11-F1 (required): the completeness residual is understated.**
  - g_model2 "explains" a class whenever its |w| lies within a factor 2 of a gas product, with no phase check.
  - At p = 47, of 2.75e-6 "explained" weight, only 1.17e-6 matches the product in phase (to within 25%, with conjugate and sign allowed). 1.58e-6 matches by magnitude only.
  - Examples on background 0: α′ = (1,±2) (N=−7), (0,3), (4,0), (10,0), (0,7); on background q: (3,0). These are short-range clusters, not dilute products.
  - **The phase-consistent unexplained remainder is ≈ 1.7e-6, not 1.0e-7 (about 17× larger).** It is still about 1/370 of Re Λ_lo, so the conclusion survives.
  - Also state the units: this is a class-weight sum at p = 47, while Re Λ_lo is a per-site activity.
  - Label [N].
- **N11-F2 (required): Lemma C(ii) constant.**
  - δ = e(Γ) − e(Γ′) has coefficients β − β′ with |β − β′| ≤ 2B = 8, so the norm bound carries (2B)² = 64, not B².
  - Then 64(3+2√2) > ε⁶, so G₀ = 6 fails, while G₀ = 7 works (Lean G0_2B).
  - Consequences: injectivity holds for |Γ|+|Γ′| ≤ p/7, and the dense cutoff becomes n₀ = p/14 with e^{−0.23p}. Both are still fine.
  - Also put the hypothesis "all gaps ≥ g₀" explicitly in (ii), and note that ± closure of 𝒯 handles ε^p ≡ −1.
  - Part (i) is correct.
- **N11-F3: Re Λ_lo provenance.**
  - The number is right, but the script that produced lambda_cert.out is not archived. Archive it.
  - The type-4 activity (c₁₆, |·| ≈ 2.2e-9) has no certificate and must enter the absolute budget.
  - The [CA] label applies to "Re Λ_lo ≤ Re of the sum of listed certified activities". Its identification with the gas Λ is model-level.
- **N11-F4: Theorem N11 bookkeeping.**
  - (1+a)e^{−δ} ≥ 1+a−δ is false in general; the correct bound is (1+a)(1−δ). Write (1+Re Λ_lo)^p e^{−pδ_int} instead. The numerical effect is negligible.
  - The threshold "p ≥ 1289 (class certificates valid, E ≤ 1e-9)" has no derivation in the report or code. The bracket alone needs only p ≳ 75. Cite where E ≤ 1e-9 holds.
- **N11-F5: interaction section.**
  - Honest: the rate is proved and the prefactor (G_b ~ 4e8) is unusable.
  - g₁ ≈ 64 assumes #types ≈ 1. With 10 types it is about 68. Minor.
  - The measured close-range terms are exactly the F1 clusters, so §2 and §5(4) should reference each other.
- **N11-F6 (required): §6 "prime h_p not needed for Y" is overstated. Label it [H, conditional].** It is conditional on (I), (T), and G\* with a polynomial A. In addition:
  - (a) G\*'s own reduction yields (C_out K_box)^{#stays+1}, not a fixed A (N9b-F2).
  - (b) N9b's small-β unit points ±ε^{±1} have |r| = 1.315e-3, which exceeds |w\*| (3.3×) and Re Λ (1.8×). Unit and mixed "bumps" can therefore form their own gas inside Y.
  - (c) For mixed classes at a small prime factor q₂ ≥ 2p+1, the κ-suppression is only polynomial (~1/q₂).
  - What is needed is an explicit growth exponent for Y compared against Re Λ_lo − δ_int. "Y ≤ poly(p)" is asserted, not shown.
  - The squarefree statement (C′ gives exponentially small unit Y) stands.
- **N11-F7 (bookkeeping).** N10_v2-F6 says my R = 6.1838e-5 omitted c₈ and c₁₆. In fact it included both (+1.38e-8, −2.03e-9). The difference comes from N11 using the p=47 class weights c₀ = 2.98686e-5 and c₄ = 1.04450e-6 instead of the plateau values 2.98661e-5 and 1.04135e-6. This is immaterial.

## N9b findings
- **N9b-F1 (confirmed).** G with s = 0 for unit points is false [N, robust]. Independently, β = ±ε^{±1} gives |r| = 1.31543e-3 at p = 23 and 41, so Γ_raw → μ\*. Identify these as the unit-sector analogue of the family bump: heteroclinic to 0, with a 12-step core (m − s = 12 at θ = 1/8, which is why Γ_eff = 1.102 is flat in p).
- **N9b-F2 (required): G\* as stated is inconsistent with its own reduction.**
  - D1 + D2 give |r| ≤ (C_out K_box)^{#stays+1} Γ_out^{m−s} μ\*^{s}, which does not have a fixed A.
  - Restate G\* in gas form, and give the minimum stay length L making the fugacity z = C²(μ\*/(Γλ))^L small, with explicit C (σ₁ = 22–57, Cpow = 3246).
  - C2′ needs A_p to be polynomial. With the gas form, that requires the [P-sketch] claim that the factor acts only on excursions of length log_λ(dN f). Prove that claim.
- **N9b-F3 (required, scope).**
  - Γ_per(θ) is a max over periodic orbits with n ≤ 8. It is a **lower** bound for Γ_out(θ), not an estimate from above, and the cone-potential values (1.357 at grid 512) sit above it.
  - So "margin 0.165 to T′ at θ = 1/8" is not established. The honest statement is Γ_out(1/8) ∈ [1.262, ~1.36] [N].
  - The "1/16 box fails" entry (1.4296) comes from the period-4 orbit at sup-distance exactly 0.0625 = 1/16, i.e. on the box boundary. State whether the box is open or closed.
- **N9b-F4.** R₃ ≈ 1.405 and R₄ ≈ 2.402 are reproduced to n = 5. They are ρ-based (pressure = norm pressure only under domination); this is caveated. Fine as [N]. "R₃ ≤ 1.33 looks false" is reasonable.
- **N9b-F5.** C2′ (ω(h_p) ≤ p^δ) is a correct implication [P given G\*, A∞, package]. It inherits N9b-F2 and the A∞ dependence (flagged). The Euler-product F2 fix is correct.
- **N9b-F6 (required, honesty).** The NOTES_N9b timestamps conflict with the file mtimes:
  - the entries run to "23:15 … 23:55 … 00:35 (Nov 1)", yet all logs were finished by 22:52 and REPORT/NOTES were written at 23:02 on Oct 31, before 00:35 Nov 1;
  - "22:20 start" comes after b_mmc logs stamped 22:18.

  Correct the timestamps.

## What remains for an unconditional refutation (updated)
1. **(T) Absolute tail.** This covers all uncoded points, including the short-range clusters of N11-F1 (≈1.7e-6 at p=47 [N]). It must be p-uniform, with per-site activity < Re Λ_lo − δ_int. Coding surjectivity is the same item.
2. **(I) Interaction prefactor.** An adapted-norm certificate with C = O(1), then arb certification of the finite merged-polymer list (~10³ two-bump types). The rate κ = 0.41765 is done [CA].
3. **Y at all p, in modulus form.**
   - Unit part: C′ [P+CA] for squarefree h_p.
   - Composite h_p: mixed and partially isotropic classes (b′), with an explicit growth exponent compared against Re Λ_lo. This must include the unit-bump gas (±ε^{±1}, |r| = 1.3e-3).
   - Otherwise restrict to prime or squarefree h_p.
4. **Cross lines at composite h_p** (inside X). Open (b′).
5. **G\* in gas form.** A cone-field certificate for Γ_out(1/8) < T′ (grid ≳ 1024, [CA\*] at best), the D2 constants, and the stay-counting lemma. Needed for rank-3p, inconsistent and unit/mixed classes.
6. **Short cores (k < 20)** with p-uniform collective certificates (~10⁷ classes).
7. **Arithmetic input for infinitely many p.** Either C1 (β > 3/2, i.e. Γ < 1.2329, essentially no margin), or C2′ (infinitely many p with ω(h_p) ≤ p^δ, unproven).
8. **Mixed gap via the κ floor.** The R₄ automaton (s = 4) is not built.
9. **Bookkeeping.** Archive the Re Λ_lo script plus the c₁₆ budget; justify the p ≥ 1289 range; give a proved reference for I − 1 ≤ 0.2 in the inherited-level floor.

**Status.** Still conditional. The sign obstruction is gone for good, since |1+X_gas| ≥ 2(1+Re Λ_lo)^p − 1 with Re Λ_lo certified. The open items are absolute bounds (1–4) plus the G\*/arithmetic package (5–8).

## Artifacts
- code:
  - ref_gas2.py
  - ref_genfun2.py
  - ref_match.py
  - ref_US.py
  - rerun_a_per.py (unmodified N9b copy)
  - rerun_f_Rs.py (unmodified N9b copy)
- logs:
  - ref_gas2_p{37,59}
  - ref_genfun2.json
  - ref_match.json
  - ref_US_p{23,41}.json
  - rerun_*.out
  - a_per_a4.jsonl
  - f_Rs_a4.jsonl
- lean/LineN11Arith.lean
- SHA256.txt
