# Proposed claims.json changes for THEOREM_DRAFT_v5 (NOT applied; repo read-only)

Grok Bot, 2026-11-01 (UTC+5). Registry: `lineNgas/repo/record/claims.json`. The highest existing ID is BGS-TRACE-324. Its `id_policy` says IDs are immutable after publication, so where a title would change I propose a **new** claim and a ledger/boundary update to the old one. The maintainer decides whether title edits are allowed. States follow the registry vocabulary: proved / open / conditional / verification-pending / refuted.

## Existing claims
| ID | now | proposed state | proposed ledger / boundary change |
|---|---|---|---|
| 299 (Theorem R♯-mod v4) | conditional | conditional (unchanged) | Ledger: "superseded by BGS-TRACE-325 (v5)". Closure condition: drop H4 (met) and H3 (⇐ H1); add "p_thr with additive budgets". |
| 300 (H1) | open | open | Boundary: re-scoped per N20, H1 = (H1-bad) bad-cluster joint second moment Σ_{bad,shell j}\|r_Ar_B\|² ≤ C·2^{j(1−β(0.28))}, C ≤ 0.082, J₀ = 12, + (H1-ali) near-collision/box constants. Finite part j ≤ 14 certified (core functional, BGS-TRACE-331). By Prop. F (329), an unrestricted carry/torus bound cannot close it. If the title must change, register the re-scoped H1 as a new claim and mark 300 superseded. |
| 301 (H3) | open | **conditional** (on 300 alone) | "[P + CA mod H1-shell; span bound ℓ ≤ 2j + g₀ P-sketch] via Prop. K (332). The 1.56e-8 tail placeholder is withdrawn." It stays *conditional*, not proved, because of the H1 dependence and the P-sketch span bound. |
| 302 (H4) | open | **proved** (closure condition met) | Closure condition ("difference-form conversion … + bound on the G > 15 true tail") is met by Lemma D^T (327) + Lemma C (322) + δ_true (326). Ledger: "CLOSED [P] + [CA-fp] by BGS-TRACE-322/326/327; refereed lineN21, lineN21b; not [CA]". If the registry does not allow an "(open …)" title to become proved, set the ledger to "CLOSED — see BGS-TRACE-326" and keep the state as open, with superseded_by = 326. |
| 303 (H5), 304 (H6), 305 (H7*), 306 (H8) | open | open (unchanged) | 306: ledger note "reduces to 300 on 𝒫 [P-sketch]" (unchanged). No new results. |
| 318 (crossover) | proved | proved (as an arithmetic implication in the *input* δ; the statement is still true) | **Boundary/ledger fix:** "The values 1386/1390/1399 charge δ only (A_bad^KP = 0). They are NOT the theorem's p₁: B_p carries e^{−p(δ + A_bad^KP)} (v5 §2). With all rate budgets, see BGS-TRACE-333: first prime 3307 (H1 at C ≤ 0.082) / 1409 (C ≤ 8.8e-4). At δ_true = 5.0313e-6 alone: 1397/1399 (N21 v2)." |
| 322 (δ_true G ≤ 15) | verification-pending | **proved** [P] + [CA-fp] | Closure condition ("written proof of the conversion lemma incl. the second-order dPi² term") is met by N21 Lemma C (v2 §2), refereed lineN21. The title's bound (≤ 2.470e-6) holds a fortiori; N21 gives ≤ 2.2102e-6. Ledger: N16's own lemma/code had defects (F21-1/3); the claim stands on N21's proof. |
| 323 (N_H table) | verification-pending | **proved [CA-fp]** | Closure condition ("independent recomputation") is met by lineN21b. Different method (SVD + residual certificate). Max 2.916448 ≤ 2.91656, every cell ≤ N15's, min margin 3.93e-5. 20 cells incl. the max cell [CA] (arb). |

## New claims (next IDs 325–334)
| ID | title (short) | label | proposed state | dependencies | source / referee |
|---|---|---|---|---|---|
| 325 | Theorem R♯-mod v5 (conditional): inputs H0, H1, H5–H8 (H2, H4 met; H3 ⇐ H1); B_p with e^{−p(δ + A_bad^KP)} | [P mod inputs]; the A_bad-in-exponent step is [P-sketch] | conditional | 206, 213, 271, 273, 300, 301, 303–306, 307, 326, 333 | THEOREM_DRAFT_v5 §2; **not yet refereed** |
| 326 | H4 met: δ_true (all G) ≤ 5.0313e-6 = 2.2102e-6 + 2.712658e-6 + 1.0843e-7 + 3.1e-13 | [P] + [CA-fp] (not [CA]) | proved | 307, 311, 322, 323, 327, 328 | N21 v2 §5; lineN21, lineN21b |
| 327 | Lemma D^T (true-operator difference form; G ≥ 37 tail ≤ 1.0843e-7, remainder G > 60 ≤ 3.1e-13) | [P] (after F1/F2) + [CA-fp] anchors + arb sums | proved | 322, 328 | N21 v2 §4; lineN21 |
| 328 | Lemma Q (‖(L₀/μ)^kQ‖ ≤ m(k); K₀ < 56.78, Rem < 1.591e-3) | [P] + [CA] constants, Lean arithmetic | proved | 310, 311 | N21 v2 §4; lineN21 (independent arb recomputation) |
| — | Lemma C | — | **register under 322** (it is that claim's closure); no separate ID needed | | |
| 329 | Prop. F: unrestricted joint torus mean ≥ 5.1e-7·λ^{−n} ≫ i.i.d. for 1 ≤ n ≤ 10¹⁰ (no unrestricted method gives H1) | [P mod N13 CA]; ratio uses the N14 float 3.45 [N] | proved (negative result) | 311, 312 | N20 v2 §2; lineN20 |
| 330 | Lemma J: joint (A,B) collisions are ε-adic; carries \|e\| ≤ 51 (sharp), 6145 pair states; plus the λ-carry graph (633 states, ρ ≥ 20) and renewal Lemma R | [P] (+ exact BFS; Lean for closed-form arithmetic / renewal) | proved | 312 | N20 v2 §2–3; lineN20 |
| 331 | Thm A: shell-law finite part j ≤ 14, core functional, C_cert ≤ 4.36e-4 (≤ 5.9e-5 for j ≥ 8) | [CA-fp] (core functional; H4 conversion not run on these shells) | proved | 307, 311 | N20 v2 §3.1; lineN20 |
| 332 | Prop. K: H1-shell(C ≤ 0.082, J₀ = 12) ⇒ H3 with a ≤ 2.70e-3, budget left ≥ 2.738e-4 | [P + CA mod H1-shell; span bound ℓ ≤ 2j + g₀ P-sketch] | conditional | 300, 321, 326 | N20 v2 §3.4; lineN20 |
| 333 | Gas vs Robin crossover with all rate budgets (δ_true + A_bad^KP), additive terms idealised: C ≤ 0.082 → all p ≥ 3305, first prime 3307; C ≤ 0.04 → 1726/1733; C ≤ 8.8e-4 → 1402/1409; v4-style A_bad^KP 2.0629e-6 → 1401/1409 | [P-arith] (N19b logic verbatim, mpmath/float + monotonicity), conditional on 300 via A_bad^KP | conditional | 300, 318, 326, 332 | V5/code/crossover_v5.py; lineN21b Task 3 (1401/1409 reproduced) |
| 334 (optional) | Erratum claim: N14 digits.py mp.dps = 34 corrupts twists for G ≥ 21 (ulp), material for G ≳ 25; v4 numbers (G ≤ 15) unaffected | [N]/[P] (checked at dps 150/300/400) | proved | — | N21 F21-2; lineN21 |

## Not proposed
- No claim for "p₁ = 1399 as the theorem's threshold". It is withdrawn (v5 §6).
- No [CA] upgrade for H4: the window chains are [CA-fp].
