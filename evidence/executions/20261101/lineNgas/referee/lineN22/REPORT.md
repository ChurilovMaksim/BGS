# Referee report lineN22: final pass on THEOREM_DRAFT_v5 (go/no-go)
Grok Bot, Sun 1 Nov 2026, 10:53–11:01 (UTC+5). Read-only on /workspace/bgs-lineN and /workspace/lineNgas. Peak memory below 0.3 GB, with no arb jobs; only mpmath and float code was run.

## Verdict: **GO after edits E1–E12** (verbatim below)
- No mathematical error was found.
- The new exponent step is correct, it is necessary, and its [P-sketch] tag is honest.
- The crossover table reproduces exactly with independent code.
- The edits fix two things:
  - wording that is stale or slightly overstated in the draft (E1–E8);
  - four points in the claims.json proposal (E9–E12). These matter, because the proposal as written would register a stale H3 value as "conditional on H1 alone" and would fold a defective method into a "proved" title.

**Integrity checks:**
- V5/SHA256_V5.txt and its .sha256 verify (run from the repo root).
- patch(v4, THEOREM_DRAFT_v4_to_v5.diff) reproduces v5 byte for byte.
- The N21 v2 manifest still verifies after the log move described in NOTES_V5.
- crossover_v5.py is N19b a_crossover_v3.py, identical except for the comment and the output path. crossover_N21.py, which produced 4 of the 6 V5 logs, is identical too.

## 1. A_bad^KP in the exponent, B_p ∝ e^{−p(δ + A_bad^KP)} [P-sketch]
- **Correct.** Write the bad-cluster part of the gas as a polymer partition function Ξ. KP holds with a(γ) = a|γ|; the criterion S₀ + S₁/(1+g₀) ≤ a, refereed in lineN15/lineN20, encodes the incompatibility count.
  - The anchored corollary (Ueltschi 2004 Thm 1; Fernández–Procacci 2007) gives Σ_{C∋γ}|φᵀ(C)w^C| ≤ |w(γ)|e^{a(γ)}.
  - Hence |ln Ξ| ≤ Σ_γ|w(γ)|e^{a|γ|} ≤ p·S₀(a), and so |Ξ| ≥ e^{−pS₀(a)}.
  - The right charge is therefore S₀(a), the e^{a|γ|}-weighted activity, **not** the KP weight a.
  - N20 tail_kp_v2.json does use the weighted S₀:
    - T₀ carries e^{ag₀}(qe^{2a})^j;
    - S₀^fin grows with a (2.0317e-6 at a = 8.25e-6, 2.0776e-6 at a = 2.69e-3);
    - A_bad^KP(C) = S₀ = S₀^fin + T₀.
  - All four §2 table values match the JSON, rounded up:
    - 0.082 → 3.44564e-4;
    - 0.04 → 1.11817e-4;
    - 8.8e-4 → 2.37978e-6;
    - 4.4e-4 → 2.15474e-6.
  - The J₀ = 12 rows are the ones used, consistent with H1 as stated.
  - The N20 "budget left" column equals Re Λ_lo′ − S₀ − δ_true to 1e-19. So v5's exponent is exactly the quantity N20 Prop K already budgets, and N14 §1 item 4 states the same target, "A_bad < Re Λ_lo′ − δ_int".
- **Necessary.** The bad activities are complex (phases of r_A r_B), and the only available inputs are modulus bounds (H1 is a second-moment bound). The first cluster term Σw(γ) has no proven sign, so |Ξ| < 1 cannot be excluded. Charging e^{−pS₀} is the best bound available without phase information, and v4's omission was an error.
  - What it would take to avoid the charge: a lower bound Re ln Ξ ≥ −(something smaller). That needs signed information about the bad clusters, which nothing in the project provides.
- **The tag is honest, with one caveat to state.** The step inherits H3's [P-sketch] "background interplay".
  - The cause: KP cannot be run on model and bad polymers together, because model activity ≈ 3e-4 ≫ a.
  - So the bad activities must be renormalised by the model background, w̃(γ) = w(γ)·Z_model(complement)/Z_model, and S₀ must be evaluated with w̃.
  - Heuristically |w̃| ≤ |w|·e^{O(|Λ|(|γ|+g₀))}, a relative change of order 1e-3·ℓ. That is my estimate, not a proof.
  - **Sensitivity** (logs/sens22.json):

    | A_bad^KP × | C = 0.082: first int / first prime | C = 8.8e-4: first int / first prime |
    |---|---|---|
    | 1.00 | 3305 / 3307 | 1402 / 1409 |
    | 1.01 | 3349 / 3359 | — |
    | 1.03 | 3441 / 3449 | — |
    | 1.10 | 3807 / 3821 | 1403 / 1409 |
    | 2.00 | — | 1408 / 1409 |

  - So **3307 is fragile** (a 1% change moves it), while **1409 is robust**. This must be said (E3).

## 2. Crossover, recomputed independently (code/xover22.py → logs/xover22.json)
- **Method.** My own lineN21b code: mpmath at 60 digits, exact K_p = 4h_p² + 3 through the recurrence (checked against sinh), the Robin 0.6483/ln ln K term, and a scan plus slope monotonicity. It shares no code with N19b.
- **Inputs.** δ_eff = 5.0313e-6 + S₀(C), taken unrounded from tail_kp_v2.json, plus V5's rounded inputs.

| case | δ_eff | first p (all p ≥, envelope) | first prime | violations among primes ≤ 5000 |
|---|---|---|---|---|
| C = 0.082 (exact S₀) | 3.49596e-4 | 3305 | 3307 | none |
| C = 0.04 (exact) | 1.16848e-4 | **1725** (V5's rounded-up input 1.1691e-4 gives 1726) | 1733 | none |
| C = 8.8e-4 | 7.41108e-6 | 1402 | 1409 | none |
| C = 4.4e-4 | 7.18604e-6 | 1402 | 1409 | none |
| v4-style 7.0944e-6 | — | 1401 | 1409 | none |
| δ only 5.0313e-6 | — | 1397 | 1399 | none |
| J₀ = 13 / 14 at C = 0.082 (for information) | 2.168e-4 / 1.367e-4 | 2177 / 1800 | 2179 / 1801 | none |

- **Every V5 number reproduces.** "1726" is conservative because of the rounded input.
- **Charging a instead of S₀ would be wrong** (overly conservative): at C ≥ 0.04 it would leave no crossover at all, since a > Re Λ_lo′, and at 8.8e-4 it would give 1417/1423. This supports §1 on which quantity is correct.

## 3. Consistency and stale numbers
I scanned every occurrence of the following in THEOREM_DRAFT_v5.md: 1386, 1390, 1397, 1399, 2.470e-6, /200, 186, 84×, 2.0629e-6, 0.0813, 5.93e-6, e^{−pδ}.
- **Consistent:**
  - 1386/1390/1399 appear only in the superseded δ-only row and the §6/§9/§10 history.
  - 2.470e-6 appears only in errata, the superseded row and §9.
  - /200 appears only as display-only/fails.
  - 186× carries "finite-shell margin only" wherever it is a current statement (lines 19, 112, 293). Line 194 is a v3 erratum, historical.
  - The δ parts sum to 5.031288e-6 ≤ 5.0313e-6. The 84× figure is correct (6.234e-4/7.411e-6 = 84.1).
  - The H, threshold, §3, §8 and §6 tables agree on 3307/1409 and on 1399 being superseded.
- **Stale:**
  - (a) §1 "Gas" (line 60) and §3 row (line 141) still state the bound with e^{−pδ} and no qualifier. That is true for the model gas only.
  - (b) §8 row "KP a = 5.93e-6" (line 241) is stale. That value used the withdrawn placeholder. Under Prop K, a = a(C) ≥ 6.49e-6 for C ≥ 4.4e-4 (8.25e-6 at 8.8e-4, 2.69e-3 at 0.082).
  - (c) "not yet refereed" in lines 63, 230 and 322.
  - (d) The line 98 tag says "float/mpmath", but crossover_v5.py is float with exact big-int K_p. The mpmath replay is this referee's.

## 4. Plain-language summary
- It is honest on the main points:
  - "Frozen R′ is **not** refuted" appears in both the summary and §0;
  - H1 is the first open input and is called OPEN [H];
  - small-p evidence is [N];
  - the additive budgets are listed as open, item (iv).
- Three mild overstatements:
  - (i) δ_true is listed under "proved unconditionally", but it rests on standing-package inputs taken as certified (N8 n_cert constants Pert/Xn/dPi/…, N13 V1–V3b, Line F F2, N6 symmetry). Same status as H2, but it should be said (E1).
  - (ii) "1409 if H1 holds with C ≤ 8.8e-4 (2× the measured finite-shell constant)" invites reading the measurement as evidence for the tail, which Prop. F rules out (E2).
  - (iii) "3307 under H1 as stated" omits that it covers rate budgets only and depends on the [P-sketch] normalisation (E2/E3). H3's summary line also omits the background-interplay P-sketch (E1).

## 5. claims.json mapping (simulated on a copy: code/claims_sim.py; the repo was not touched)
- Both the author's and my mapping pass the formal rule: no proved claim depends on a non-proved one other than TRACE-206. Seven unrelated violations already exist (TRACE-076/077/080/236, RES-015/023); they are out of scope.
- The semantic problems are below.

**Existing claims:**
- **302 (H4)** should become **proved**, but only with:
  - dependencies rewired to [307, 322, 326, 327, 328]. The author leaves them as [307, 322], so the closing claims would not be in its closure;
  - the status parenthetical in its title, "(open, no working route)", which is now false, replaced by "(met: BGS-TRACE-326)", with the change logged in claim_ledger.md. The ID is unchanged and the mathematical statement is unchanged.
  - If the maintainer forbids any title edit, the fallback is: state open, ledger "CLOSED: closure condition met by BGS-TRACE-326; not an open input of BGS-TRACE-325". In that case 325 must not list 302, and it does not.
- **301 (H3)** must **stay open, not conditional.** Its title fixes a = 5.93e-6, which Prop K does **not** deliver from H1 as stated (a = 2.69e-3 at C = 0.082; still 6.49e-6 at C = 4.4e-4). Ledger: "superseded in substance by BGS-TRACE-332 (KP with a = a(C)); a = 5.93e-6 used the withdrawn 1.56e-8 tail placeholder". 325 must depend on 332, not on 301.
- **318 stays proved.** It is a true arithmetic implication in the input δ, with proved deps 307/310. It needs the author's boundary/ledger fix, plus an update of its ledger phrase "delta_true <= 2.470e-6 IS BGS-TRACE-322, PENDING".
- **322:** do **not** register Lemma C "under 322". 322's title names N16's [P-sketch] vector-chain method, whose code used √cond, which is non-conservative (F21-1/3).
  - Register Lemma C + δ_true(G ≤ 15) ≤ 2.2102e-6 as a **new claim (BGS-TRACE-335)**, proved [P] + [CA-fp].
  - Then set 322 to proved *a fortiori* with deps [307, 335] and a ledger naming the defects. Keeping it verification-pending with a pointer to 335 is also acceptable.
- **323 becomes proved [CA-fp]** (closure condition met by lineN21b). Agreed.
- **299:** ledger "superseded by 325". Agreed. **300:** see 335/336 below. Prefer a new ID for the re-scoped H1 (the object changed from single-window to joint (A,B) and gained H1-ali): **BGS-TRACE-336**, open, with 300's ledger "re-scoped as 336". A boundary-only update is acceptable if the maintainer prefers.

**New claims:**
- **325** (conditional): use deps [206, 213, 271, 273, 300 (or 336), 303, 304, 305, 306, 307, 326, 332, 333], dropping 301. Tag "[P mod inputs; log→modulus/background-interplay step P-sketch]".
- **326** (proved): add deps 198 (F2) and 335. The boundary must name the unregistered standing-package inputs (N8 n_cert constants, N6 symmetry), following the 307 precedent.
- **327** (proved): deps [323, 328, 335] instead of 322.
- **328** (proved): fine.
- **329** (proved): **only the lower bound**, "unrestricted joint torus mean ≥ 5.1e-7·λ^{−n}, 1 ≤ n ≤ 10¹⁰ [P mod N13 CA]". The ratio > 1 and "no unrestricted method gives H1" use the N14 float 3.45 [N], so they belong in the boundary as [N], not in a proved title (lineN20 fix 4).
- **330:** fine.
- **331** (proved): add dep 321.
- **332** (conditional): add dep 331; tag both P-sketches (span bound, background interplay).
- **333:** conditional is fine. Add the sensitivity note.
- **334:** do **not** register. It is an erratum and belongs in errata.json/retractions.md; the registry scope is "core load-bearing claims".

## 6. Edits (verbatim; old → new in THEOREM_DRAFT_v5.md; E9–E12 in V5/CLAIMS_PROPOSED_v5.md)

**Plain-language summary:**
- **E1** (line 16): replace `[P] + [CA-fp], refereed lineN21/lineN21b. **H4 is no longer an input.**` with `[P] + [CA-fp], refereed lineN21/lineN21b, given the standing-package constants taken as certified (N8 n_cert constants, N13 V1–V3b, Line F F2, N6 symmetry), as for H2. **H4 is no longer an input.**`
  - Line 20: replace `[P + CA mod H1-shell; span bound P-sketch]` with `[P + CA mod H1-shell; span bound and background interplay P-sketch]`.
- **E2** (lines 27–28): replace them with
  `  - first prime **3307** under H1 as stated (C ≤ 0.082), rate budgets only (additive budgets idealised, item (iv)), and sensitive to the [P-sketch] background normalisation of A_bad^KP (+1% → 3359; referee lineN22);`
  `  - first prime **1409** under a strengthened H1 with C ≤ 8.8e-4 (2× the measured finite-shell constant; by Prop. F the finite shells are not evidence for the tail). This value is robust (1409 up to 2× A_bad^KP).`

**§1 and §2:**
- **E3** (line 82): replace `[P-sketch: the same log→modulus step as H3 (background interplay [P-sketch])]. **Flagged for the referee.**` with `Precisely: |ln Ξ_bad| ≤ Σ_γ |w̃(γ)| e^{a|γ|} ≤ p·S₀(a) (anchored KP corollary, Ueltschi 2004 Thm 1), so |Ξ_bad| ≥ e^{−pS₀(a)}; the charge is the weighted S₀(a), not a. Here w̃ are the bad activities renormalised by the model background, and S₀ must be evaluated with w̃ [P-sketch, as H3 background interplay]. Refereed lineN22: correct and necessary (no sign information on bad clusters); 3307 moves by ≈ +50 per +1% in S₀, 1409 is stable.`
- **E4** (line 60): after `(N11-F4).` add ` This is the model-gas bound; with the bad clusters (H3) the factor is e^{−p(δ + A_bad^KP)} (§2).`
  - Line 141: replace `| \|1+X_gas\| ≥ 2(1+Re Λ)^p e^{−pδ} − 1 | [P given the model form] |` with `| \|1+X_gas\| ≥ 2(1+Re Λ)^p e^{−pδ} − 1 (model gas; with bad clusters e^{−p(δ + A_bad^KP)}, §2) | [P given the model form]; bad-cluster factor [P-sketch] |`.
- **E5** (line 63): replace `the v5 A_bad^KP correction of the exponent is not yet refereed]` with `the v5 A_bad^KP correction of the exponent is [P-sketch], refereed lineN22 (correct, necessary)]`.

**Tables:**
- **E6** (line 98): replace `[P-arith: float/mpmath + monotonicity, N19b logic verbatim (`V5/code/crossover_v5.py`)]` with `[P-arith: float + exact big-int K_p + monotonicity, N19b logic verbatim (`V5/code/crossover_v5.py`); independently reproduced in mpmath (referee lineN22; C = 0.04 with unrounded input: 1725/1733)]`.
- **E7** (line 230): replace `A_bad-in-exponent step not yet refereed` with `lineN22 ✓ (all rows reproduced; A_bad-in-exponent step correct, [P-sketch])`.
  - Line 241: replace `| KP a = 5.93e-6 | [P]/[CA-fp]/[H] tail | N15 kp.py | lineN15 §1d (F1, F2) |` with `| KP a = 5.93e-6 (**superseded**: used the withdrawn tail placeholder; now a = a(C), Prop. K) | [P]/[CA-fp]/[H] tail | N15 kp.py | lineN15 §1d (F1, F2) |`.

**§11b:**
- **E8** (line 322): replace `  - a referee pass on the A_bad^KP-in-exponent step and on this assembly;` with `  - (done: referee lineN22, GO after E1–E12);`.

**Claims proposal (V5/CLAIMS_PROPOSED_v5.md):**
- **E9** (302 row): proposed state "proved", dependencies [307, 322, 326, 327, 328], title parenthetical "(open, no working route)" → "(met: BGS-TRACE-326)" logged in claim_ledger.md. Fallback as in §5.
- **E10** (301 row): proposed state **open** (not conditional). Ledger: "superseded in substance by BGS-TRACE-332; a = 5.93e-6 used the withdrawn placeholder; under Prop K a = a(C) ≥ 6.49e-6 (C ≥ 4.4e-4)". In 325's deps, replace 301 with 332.
- **E11** (Lemma C row and 322 row): replace "register under 322" with "new claim BGS-TRACE-335: Lemma C, δ_true(G ≤ 15) ≤ 2.2102e-6, [P] + [CA-fp], proved, deps [198, 307, 311, 323]". 322: proved a fortiori with deps [307, 335] and a ledger naming F21-1/F21-3. Deps: 326 += {198, 335}; 327: 322 → 335 (+ 323); 331 += 321; 332 += 331.
- **E12** (329 and 334 rows):
  - 329 title restricted to "unrestricted joint torus mean ≥ 5.1e-7·λ^{−n} for 1 ≤ n ≤ 10¹⁰ [P mod N13 CA]". The i.i.d. ratio and "no unrestricted method gives H1" go in the boundary as [N] (N14 float 3.45).
  - 334 is removed from the claims and recorded in errata.json instead.
  - Optional: re-scoped H1 as new BGS-TRACE-336 (300 ledger "re-scoped as 336").

## 7. Recommended final tags
| Item | Tag |
|---|---|
| Theorem R♯-mod v5 (325) | conditional, [P mod inputs H0, H1, H5–H8; log→modulus / background-interplay step P-sketch] |
| A_bad^KP-in-exponent step | [P-sketch] (correct, necessary; lineN22) |
| δ_true ≤ 5.0313e-6 (326), H4 (302) | proved, [P] + [CA-fp] (not [CA]), standing-package inputs as certified |
| Lemma C (335), Lemma D^T (327), Lemma Q (328) | proved, [P] + [CA-fp] / [CA] constants |
| N_H table (323) | proved, [CA-fp]; 20 cells [CA] |
| Prop K (332), H3 | conditional on H1; span bound and background interplay P-sketch |
| Crossover with all rate budgets (333) | conditional on H1, [P-arith]: 3307 (C ≤ 0.082, fragile) / 1409 (C ≤ 8.8e-4, robust); additive budgets open |
| 318 | proved, [P-arith] in the input δ; not the theorem's p₁ |
| Prop F (329) | proved, lower bound [P mod N13 CA]; ratio statement [N] |
| H1 (300/336), H5–H8 | open [H] |

## Files
- code/xover22.py, sens22.py, claims_sim.py, ref_crossover21b.py (copy of the crossover code from my lineN21b round)
- logs/xover22.json, sens22.json, claims_sim.out
- Manifest: SHA256.txt
