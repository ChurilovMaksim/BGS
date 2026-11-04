# Scientific changelog

## 2026-11-04 — Lean batch 6b: TRACE-214 and TRACE-218 for summable kicks (no state changes)

Two new modules (`LineIRegroupSummable`, `LineIHorocycleSummable`; 10 theorems, no `sorry`, no `native_decide`, axioms
within {propext, Classical.choice, Quot.sound}). BGS-TRACE-218: regrouping of absolutely convergent pair series into
Σ_j C_Z(jq), so both identities (aliasing and Möbius in C_Z form) hold for every kick with Σ|Φ̂| < ∞. BGS-TRACE-214:
identities (a) and (b) of Lemma I5′ for every kick with Σ|Φ̂| < ∞. Both rows now state full coverage of the identities in
`formalization_scope` (remarks and heuristic assessment excluded); BGS-TRACE-222 unchanged. No boundary or state changed.
Combined with batch 6 (merged from `main`): 190 modules, 2426 `theorem`/`lemma` declarations; `lake build Bgs` 8897 jobs. Receipt: [lean_batch6b](evidence/executions/20261104/lean_batch6b/README.md).

## 2026-11-04 — Lean batch 6: TRACE-213 disjointness (no state changes)

New module `formalization/Bgs/LineI213Disjoint.lean` (7 `theorem`/`lemma` declarations, no `sorry`, no `native_decide`,
axioms within {propext, Classical.choice, Quot.sound}): the pairwise disjointness of the classes ν_ρ and the member sets
M_d(ρ) of the frozen definition (BGS-TRACE-206), derived from the congruence definition for h_m > 1 (h² + 1 = 2y′²), and
the exact identity of BGS-TRACE-213 with the disjointness hypothesis discharged (`reduction_congr`). BGS-TRACE-213 stays
**partial** ((E″), (T″), (D) ⇒ R′ not formalized); its `formalization_scope` is updated. `lake build` completed (8895 jobs);
171 non-open claims link Lean, out of 188 modules, 2416 declarations. Receipt:
[lean_batch6](evidence/executions/20261104/lean_batch6/README.md).

## research-2026.11.1 — release preparation (no state changes)

Release tag research-2026.11.1, prepared on 2026-11-03 from main at b6e0d26; it covers merged PRs #51–#80 since
research-2026.10.1 (2026-10-26). Version metadata updated in `CITATION.cff` (with `date-released`), `.zenodo.json`
and the citation paragraphs of `README.md` / `README.ru.md`. Summary of the period (details in the dated entries below):

- Lines A–N registered (TRACE-117 through TRACE-336), including Lines E–N on the fixed-kick cat map, the reduction
  of Conjecture R′, the polymer-gas route and Theorem R♯-mod v5 (BGS-TRACE-325, **conditional** on H0, H1, H5–H8).
- Final editorial pass: whole-programme README (EN/RU), generated RESULTS.md, Appendix A, rebuilt
  `manuscript/BGS_unified.pdf`.
- Lean batches 1–5: 171 non-open claims link Lean (all new links partial), 187 modules, 2409 `theorem`/`lemma`
  declarations; legacy `native_decide` uses reduced from 88 to 37.
- CI: restore `python_stdout.json` of momentum-phase-cue after verification (dirty-tree fix, #80).

Registry at this release: 419 claims = 338 proved / 21 conditional / 17 verification-pending / 42 open / 1 refuted.
BGS-BGS-001 (microscopic fixed-strength BGS) **remains open**; no proof of BGS is claimed.

## 2026-11-01 — Lean batch 5: TRACE-222, 214, 213/317, 218 summable Möbius, 293 composite (no state changes)

Five new modules (`LineJSectorConj`, `LineIHorocycle`, `LineIReduction`, `LineIMoebiusSummable`,
`LineN3SignConjComposite`; 23 theorems, no `sorry`, no `native_decide`, axioms within {propext, Classical.choice,
Quot.sound}). New Lean links: BGS-TRACE-222, TRACE-214, TRACE-213 and TRACE-317. Extended: BGS-TRACE-218 (Möbius formula
for summable kicks) and TRACE-293 (composite levels from the TRACE-228 inheritance, as hypothesis). Every link is **partial**
(see `formalization_scope`); no boundary was changed. `lake build` completed (8894 jobs); 171 non-open claims link Lean, out
of 187 modules. Receipt: [lean_batch5](evidence/executions/20261101/lean_batch5/README.md).

## 2026-11-01 — Lean batch 4: Line L collision form and decomposition, TRACE-204, 293, 267 closure, 218 regrouping, 273 (no state changes)

Seven new modules (`LineGDilution`, `LineN3SignConj`, `LineL3Quadrature`, `LineLCollisionForm`, `LineL2Decomp`,
`LineIRegroup`, `LineMInclusion`; 39 theorems, no `sorry`, no `native_decide`, axioms within {propext, Classical.choice,
Quot.sound}). New Lean links: BGS-TRACE-204, TRACE-293, TRACE-254, TRACE-255 and TRACE-273. Extended: BGS-TRACE-267
(Nm γ ≠ 0, |Nm γ| ≥ q on 𝔮∖0, the c₀ case), TRACE-259 (collision form of C_𝔮) and TRACE-218 (regrouping into Σ_j C_Z(jq)
and the Möbius formula in C_Z form, finite support). Every link is **partial** (see `formalization_scope`); no boundary was
changed. `lake build` completed (8889 jobs); 167 non-open claims link Lean, out of 182 modules. Receipt:
[lean_batch4](evidence/executions/20261101/lean_batch4/README.md).

## 2026-11-01 — Lean batch 3: Lemma A1/Q, batch-2 gap closures, TRACE-216, TRACE-143, FM-026, TRACE-178 (no state changes)

Eight new modules (`LineLLineOrth`, `LineIMoebius`, `LineISummable`, `LineJ3GaussSquare`, `LineIMonomial`, `LineCDFTStar`,
`Fm026Counts`, `LineBTorsionSplit`; 75 theorems, no `sorry`, no `native_decide`, axioms within {propext, Classical.choice,
Quot.sound}). New Lean links: BGS-TRACE-259, TRACE-267, TRACE-216, TRACE-143, FM-026 (sealed row, admitted via its amendment
row) and TRACE-178. Extended: BGS-TRACE-211 (now the full registered identity, including summable kicks), TRACE-218 (Möbius
formula, summable first identity) and TRACE-229 (completing the square, |G_t(0)|² = q², isotropic count). Dated Lean notes were
appended to the boundaries of TRACE-143 and TRACE-216. Except for TRACE-211, every link is **partial** (see `formalization_scope`).
`lake build` completed (8882 jobs); 162 non-open claims link Lean, out of 175 modules. Receipt:
[lean_batch3](evidence/executions/20261101/lean_batch3/README.md).

## 2026-11-01 — Lean batch 2: TRACE-297 corollary and four further partial formalizations (no state changes)

Five new modules (`LineN4GaugeTwist`, `LineIPhaseSplit`, `LineIAliasing`, `LineJ3PrimeLevel`, `ResonanceMarginConst`; 31
theorems, no `sorry`, no `native_decide`, axioms within {propext, Classical.choice, Quot.sound}). BGS-TRACE-297 gains the
geometric-twist product corollary (by induction from the gauge lemmas). BGS-TRACE-211, TRACE-218, TRACE-229 and RES-023 now
link Lean. Every link is **partial** and certifies only the statement named in its `formalization_scope`. `lake build`
completed (8874 jobs); 156 non-open claims link Lean, out of 167 modules. Receipt:
[lean_batch2](evidence/executions/20261101/lean_batch2/README.md).

## 2026-11-01 — Lean batch 1: partial formalization of eight proved claims (no state changes)

Seven new modules (`Fm001Exact`, `Fm009CubeArith`, `PellModuliArith`, `LineLCollision`, `LineM3Const`, `LineN3Order`,
`LineN4Gauge`; 55 theorems, no `sorry`, no `native_decide`, axioms within {propext, Classical.choice, Quot.sound}) and two
previously unlinked modules now link BGS-FM-001, FM-009, FM-036, RET-004, TRACE-248, TRACE-271, TRACE-291 and TRACE-297.
Every link is **partial** and certifies only the finite or algebraic statement named in the receipt. For example, FM-001
gets the §1 Weyl dictionary and the §3 Fourier data, but not the §2 dynamics. `lake build` completed (8869 jobs); 152
non-open claims link Lean, out of 162 modules. Inventory:
[lean_inventory](evidence/executions/20261101/lean_inventory/INVENTORY.md). Receipt:
[lean_batch1](evidence/executions/20261101/lean_batch1/README.md).

## 2026-11-01 — Legacy `native_decide` cleanup and the p = 17, q = 103 exact (R-mix) run (no claim changes)

51 of the 88 legacy `native_decide` proofs were replaced by kernel-checked `decide +kernel`; **37 uses in 8 older modules** remain
(memory guard, timeout or kernel recursion limit; SevenPrimary keeps all 22). Statements are unchanged; `lake build` completed
(8862 jobs). The boundary of BGS-CAYLEY-002 still says "by native_decide" for all five designs (a protected contract; now
conservative). The exact-mode (R-mix) majorant run at p = 17, q = 103 gives E_M/W0 = 0.3488, c_coll = −0.227 ([N], one prime;
evidence only, not registered). Receipts:
[native_decide_cleanup](evidence/executions/20261101/lineNgas/native_decide_cleanup/README.md),
[p17_q103_exact](evidence/executions/20261101/lineNgas/p17_q103_exact/README.md).

## 2026-11-01 — Final editorial pass: whole-programme README, reader guides and indexes (no claim changes)

README.md and README.ru.md rewritten as an overview of the whole programme (seven phases, Cayley arithmetic to Lines I–N), with
a results table across all phases. RESULTS.md (via `record/results_spec.json` and `render_results.py`) now has groups for
Phases I–III. RESEARCH.md summary, `mathematics/results.md`, `mathematics/open_questions.md`, the reader guides, the topic
indexes and the manuscript abstract and introduction updated to the v5 state and the full programme. The claim ledger gains the
missing narrative sections for Lines N2–N4 and N5–N19b. Registry states are unchanged. Receipt:
[evidence/executions/20261101/final_editorial/README.md](evidence/executions/20261101/final_editorial/README.md).

## 2026-11-01 — Lines N20, N21: Theorem R♯-mod v5, H4 met, H1 re-scoped (TRACE-325–336)

Referee lineN22 GO after E1–E12. New: 325 (Theorem R♯-mod v5, **conditional** on H0, H1, H5–H8; supersedes 299), 332 (Prop. K)
and 333 (crossover with all rate budgets) conditional on H1; 326–331 and 335 proved; 336 (H1 re-scoped) open. State changes:
302 (H4) open → proved; 322 and 323 verification-pending → proved. The proposed claim 334 is erratum ERR-065. See the
[claim ledger](record/claim_ledger.md). **BGS-TRACE-206 (frozen R′) stays open and is not refuted.**

## 2026-11-01 — Lines N5–N19b: the polymer-gas route and Theorem R♯-mod v4 (TRACE-299–324)

Referees lineN6–lineN16. Registered 299 (Theorem R♯-mod v4, conditional on H0–H8), the open hypotheses 300–306 (H2 met by 307),
proved ingredients 307–319 and 321, verification-pending 320, 322, 323, 324. No refutation of frozen R′ is claimed.

## 2026-10-31 — Lines N2–N4: the inherited level h_p, certified Λ, Theorem C′ (TRACE-286–298)

Register as project proofs. Line N2 (referee READY after N2-F1–N2-F9, applied by the author in REPORT_N2_v2/v3):
* BGS-TRACE-286: Theorem A, a proved implication from the open Ω-hypothesis 287 (like TRACE-257). It is not a refutation.
* 288: Theorem B, periodic-orbit sums over the index-4 subgroup G_p.
* 289: Theorem C, the pressure reduction, with Λ in the O1 space (N2-F1).
* 290: Prop E, with arb r₂(4000).

Line N3 (READY after N3-F1–N3-F11, applied by the author in v2):
* 291, 292: isotropic Lemmas 1.1 and 1.2.
* 293: M6 condition C3.
* 294: Lemma I, together with N4's Lemma I₁₆.

Line N4 (READY after N4-F1–N4-F9, applied at integration as REPORT_N4_v2.md §7, author file kept with its sha256):
* 295: the [CA] free-family bounds Λ^{8V} ≤ 1.9656353, Λ^{8E} ≤ 0.4915932, Λ^{16V} ≤ 2.9413897, Λ^{16E} ≤ 0.4474396. The 16V value is
  rounded up from the author's 2.9413896 because f + π = 2.94138961 (I-1).
* 296: Theorem C′ for p with h_p squarefree. Squarefreeness is not proved; the only evidence is [N].
* 297: the gauge lemma, up to a unimodular scalar.

Register as **open**: 287 (the Ω-hypothesis) and 298 (the isotropic part at q ∣ h_p).

Scope widenings (states unchanged):
* 222: to arbitrary twists and non-autonomous products (C1).
* 266: to composite conductors c with ord_c λ = p.

276 stays open; only C2 remains. Line N5 supersedes the single-slow-window analysis of N4 §3.3–§3.4, so its numbers (G ≤ 1.547, 1.4468,
1.2426/1.0672/0.9165) are **not registered**. Nothing from N5 is registered either (not yet refereed), and neither are the 7·h_p unit
points. New Lean modules: `Bgs.LineN2Arith`, `Bgs.LineN3Arith`, `Bgs.LineN4Arith` (referee files).

**BGS-TRACE-206 and 239 stay open, and 240 stays conditional.** No refutation is claimed. There is no BGS counterexample and no progress on
BGS-TRACE-148.

## 2026-10-31 — Lines M and N: conductor structure along m = 3p, Theorem W⁺, scarred conductors (TRACE-269–285)

Owner audit of PR #65 (MERGE after fixes), applied on the same branch: R1 the isotropic bound of N1.3 / Theorem W⁺ (TRACE-279, 280)
now uses the middle Cochrane–Pinner branch λq^{1/4}τ^{−5/8} (q^{1/2} < τ ≤ q^{2/3}/3) besides the Gauss and 5/8 branches; coverage
of the whole W⁺ range for every p is checked analytically and on a grid (lineN/integration_checks/iso_coverage.py); statement of W⁺
unchanged. R2 the Cochrane–Pinner Thm 1.1 range is 3p^{1/3} < |A| ≤ p^{1/2} (EXT-CP-2011 locator; preprint of 5 Oct 2009, published
text not accessible). R3 TRACE-278 budget sentence. S1–S3 family scope (±2,8), named statements in TRACE-284, annotational 283 edge
of TRACE-246/258. No state changes.

Register as project proofs (Line M, referee READY after M-F1–M-F12, applied by the author in REPORT_M_v2.md): BGS-TRACE-269 (M1,
strong divisibility; open conductors at distinct m = 3p disjoint), 270 (M2, averaged H♮ ⇒ H♮ with δ/2), 271 (M3, inherited-level no-go
for positivity methods, m = 3p ≥ 495, (±2,8); on the Line F certificate), 272 (M4a, P* families disjoint), 273 (M4b, (±2,8) rule
degenerate for odd m ≥ 15; on the Line F certificate), 275 (M5, refinement of Prop K2), 277 (M7a, arithmetic; Kurlberg–Rudnick
CMP 222 (2001) verified against the publisher, annotation only). Register as **open**: 274 (M4c) and 276 (M6, conditional on C1–C4).

Line N (referee READY after N-F1–N-F10; fixes applied at integration as REPORT_N_v2.md §12, author file kept with its sha256): project
proofs BGS-TRACE-278 (N0 reduction and budget ε_F), 279 (N1.1–N1.3; OSV Lemma 4.3, Voloch via OSV Lemma 2.1, Cochrane–Pinner Thm 1.1),
280 (Theorem W⁺, q ≤ max(c_W p², c_N p^{7/3}), c_N = 10^−113.80, beyond Weil only for p ≥ 10^264.5; under the standing inputs of
Theorem W, m₁ effective, not computed), 281 (prime q ≤ p^C via Bourgain JAMS 2005; p₀(C) effective, constants not computed), 283
(Theorem N3, scarred conductors carry the slow β = 1; on the TRACE-198 certificate; t_F and p₀ effective, not computed), 284
(Corollary N3′), 285 (N4, index 4 in Fix(T^p)). Register as **open**: 282 (composite c ≤ p^C, [H]). New external dependencies:
EXT-OSV-2023, EXT-OSV-2024, EXT-CP-2011, EXT-BOURGAIN-2005 (`literature/lineMN_sources_20261031.md`).

Annotations (states unchanged): 246 and 258 replace the [H] "covers all or most m" caveat by Theorem N3 and depend on 283; 247 and the
Line L §6 target: the unweighted "exclude slow λ-orbits" target is false on c ≥ λ^{θr/2+t} and is restated as a β-weighted target; 238
(refined by M5); 206. Wording (N-F6): "ineffective" → "effective, constants not computed" in lineK_harg_removal.md and REPORT_K2_v2.md
(§9 errata, with the N-F10 pointer). README standing-inputs wording aligned with the PR #64 R1 dependency rule. New Lean modules
`Bgs.LineMArith`, `Bgs.LineNArith` (referee files). **BGS-TRACE-206 stays open**; no refutation is claimed. There is no BGS
counterexample and no progress on BGS-TRACE-148.

## 2026-10-31 — Lines L, L2, L3: OP certified, Theorem W and K2′ without OP, the open range in frozen R′ (TRACE-248–268)

State reviews (referee tables): **BGS-TRACE-244 (OP) open → proved [P + CA]**: (OP_k, δ) holds for the four k1 lattice-lifted families
at the certified (k, ρ, β), δ ≈ 0.0162 for (±2,8)V. **BGS-TRACE-245 (Theorem W) and BGS-TRACE-246 (K2′) conditional → proved
[P + CA]**, under the standing inputs (TRACE-197 Line F/J trace representation, J3 with L16, S_Z (Prop K2), Weil), for m ≥ m₁
(effective, not computed), c_W = 10^−25.62, q₀ = 10^13.2; no explicit p₀ is claimed. Caveat on 246 (Prop S): K2′ is true, but it is not a
refutation route for the m covered by Prop S. BGS-TRACE-247 (C1) stays open.

Register as project proofs: BGS-TRACE-248 (collision structure), 249 (Lemma O1), 250 (Theorem OP_abs, cancellation-free), 251
(four-family arb certificate), 252 (T_k bound, c_W, q₀), 253 ((±2,16) narrowing to q < (1.6677²/ξ_lo)^{m(1+η)}), 254 (Theorem U;
the L² version of C1, does not imply it), 255 (L2 decomposition), 257 (H_mean ⇒ frozen R′ false; an implication), 258 (Prop S),
259 (Lemma A1), 260 (Prop A2, phase-blind barrier), 261 (Lemmas B1–B3), 262 (height zone and open range disjoint for large p).
Line L3 (structural/recursive route; it does not close the open range): BGS-TRACE-263 (S1, walk-measure form), 264 (S2, CRT split,
|D_𝔮| ≤ 2h/q, after L3-F1), 265 (S3, no Gauss-side folding; exceptional prime 7, after L3-F2), 266 (S4, spectral form at rank-p
levels, given the Line G/I transfer law), 267 (Lemma Q), 268 (Lemma E), all proved. Register as **open**: BGS-TRACE-256 (H_mean). Numerics (r_abs = 1.0511, the L2 level survey), the deficit identity [H] and the
negative assessments are in the note only.

The referee's L2 text fixes L2-F1–F4 and the Prop S block count, and the L3 fixes L3-F1–F4, were applied at integration as errata
sections of the repository copies of REPORT_L2.md and REPORT_L3.md (author files kept in `pre_polish/`). New Lean module: `Bgs.LineLConst` (scalar constant inequalities only).
Independent referee audit: `computations/verification/lineL/referee/REPORT.md`. **BGS-TRACE-206 stays open**; no refutation is claimed.
There is no BGS counterexample and no progress on BGS-TRACE-148.

## 2026-10-31 — Line K: H_arg removed, the light-cone identity and the Weil range in frozen R′ (TRACE-234–247)

Register as project proofs:
* BGS-TRACE-234 (Lemma K3, gap lemma; exact-integer check + paper sieve; Lean `Bgs.LineKFinite` for the finite part, the full gap
  range by kernel-`decide` chunk files kept **outside** `lake build Bgs` and recompiled at integration, the 100-modulus chunk 1547..1646
  re-split into five 20-modulus chunks for memory);
* BGS-TRACE-235 (**Theorem K3**: S⁺ ∩ {3p : p ≡ p₀ (56)} is infinite for every unit p₀, **unconditionally**; H_arg is bypassed by a
  case split, not proved);
* BGS-TRACE-236 (Corollary K3: the dichotomy on an infinite S⁺; the refutation of frozen R′ is conditional on H♮ alone);
* BGS-TRACE-237 (Theorem K1: light-cone identity at prime levels q ∥ h, 2 a square mod q; exact check q ≤ 47);
* BGS-TRACE-238 (Prop K2: levels d ≥ L_m absorbed by positivity; S_Z ≤ 0.5000001; non-vacuous only from m ≈ 1.68·10⁹ [N]);
* BGS-TRACE-241 (Lemma W1, modulo the Weil bound EXT-WEIL-1948), BGS-TRACE-242 (Lemma W2′, every bounded read-out, after referee
  W-F7 applied at integration), BGS-TRACE-243 (Lemma W3).

Register as **conditional**: BGS-TRACE-240 (Theorem K: frozen R′ false under H♮ or H♮_mid), BGS-TRACE-245 (Theorem W) and
BGS-TRACE-246 (Theorem K2′), both conditional on the operator input OP. Register as **open**: BGS-TRACE-239 (H♮_mid, an alternative to
H♮, not a weakening), BGS-TRACE-244 (OP) and BGS-TRACE-247 (Conjecture C1).

BGS-TRACE-231 stays conditional; its closure condition now needs only H♮ (BGS-TRACE-232). BGS-TRACE-233 (H_arg) stays open: it is no
longer needed for 231 and is **bypassed, not proved**. **BGS-TRACE-206 stays open**; no refutation is claimed.

New external theorem: EXT-WEIL-1948. New Lean module: `Bgs.LineKFinite`. Independent referee audit:
`computations/verification/lineK/referee/REPORT.md` (DELTA: ready to integrate; DELTA2: K2 ready after W-F7). There is no BGS
counterexample and no progress on BGS-TRACE-148.

## 2026-10-31 — Line J: the d = 7 twisted coefficient in frozen R′ (TRACE-221–233)

Register as project proofs:
* BGS-TRACE-221 (Prop J-C: exact sector law; exact leading d = 7 coefficient B_C; class 1:3 cancels exactly, classes 2:1 and 0:1
  survive; period 168; Lean core `Bgs.LineJArith`, mod-49 period only);
* BGS-TRACE-222 (sector-level antiunitary map);
* BGS-TRACE-224 (window lemma; Lean real-line core and constants);
* BGS-TRACE-226 (Lemma L16 for ρ = (±2,16));
* BGS-TRACE-228 (inheritance theorem; Lean counts only);
* BGS-TRACE-229 (prime-level complete-sum bound);
* BGS-TRACE-230 (r(q) lemma; Lean ring identity).

Register as computer-assisted proofs:
* BGS-TRACE-223 (certificates, |ξ| ≥ 2.4586893 > √λ);
* BGS-TRACE-225 (Theorem J: the frozen d = 7, (±2,8) contribution to W′/m is ≥ K_j·1.0184224^m/m in absolute value, with each sign,
  for some m in every 6 consecutive members of each class mod 168, m ≡ 3 (mod 6); a subsequence statement);
* BGS-TRACE-227 ((±2,16) at d = 7 is ≤ 1 % for m ≥ 243).

Register BGS-TRACE-231 (Theorem J3) as a **conditional** implication: frozen R′ is false along m = 3p under H♮ and H_arg; unconditionally,
if R′ holds, the conductor ∉ {1, 7} parts must cancel the d = 7 term exponentially on S⁺. H♮ (BGS-TRACE-232) and H_arg
(BGS-TRACE-233) are registered as **open**.

**BGS-TRACE-206 stays open**: its boundary and ledger are updated, and no refutation is claimed.

External theorems registered for BGS-TRACE-231: EXT-VINOGRADOV-1937, EXT-WEYL-1916 and EXT-DAVENPORT-1980. The cited IK Theorem 13.6
was checked and replaced, since it is the minor-arc estimate only.

Independent referee audit: `computations/verification/lineJ/referee/REPORT.md` (final DELTA3: ready to integrate). New Lean module:
`Bgs.LineJArith`. There is no BGS counterexample and no progress on BGS-TRACE-148.

## 2026-10-31 — Line I: reduction of Conjecture R′ and the d = 7 twisted certificates (TRACE-211–220)

Register BGS-TRACE-211 (relative phase split), BGS-TRACE-212 (dilation-coset L² law and per-member Gauss-sum formula for every odd d | h_m; Lean core `Bgs.LineI`, `Bgs.LineIArith`), BGS-TRACE-213 (exact reduction of R′ to (E″), (T″) and the dilation remainder (D), none of which is proved), BGS-TRACE-214 (Fourier/Ramanujan-sum expansion of weighted horocycle sums of |Z_ν|²), BGS-TRACE-216 (exact monomial intertwiners between the eight (m mod 24, a = ±2) operator cases), BGS-TRACE-218 (aliasing/Möbius identity for F_m) and BGS-TRACE-219 (h_m has a new odd prime factor for every m ≥ 16, so every finite prime set fails for all large m; modulo the Bilu–Hanrot–Voutier/Carmichael primitive-divisor theorem, which enters the Lean proof as a hypothesis) as project proofs. Register BGS-TRACE-215 (for the k1 kick at η = 2, d = 7 and every m ≡ 3 (mod 6): |Ẑ(β)| ≤ 6.769·10⁶·1.45^m + 6.859·10⁴ and the normalised square term 7Σ_u|δ_u|²/φ(2h_m) ≤ 0.01 for m ≥ 321; ρ = (±2,8) only, the (±2,16) level-7 members are not controlled) and BGS-TRACE-217 (classes 1:3 and 2:1 have exactly three simple twisted eigenvalues outside |z| = 1.22, with certified 1.262 < |μ| < 1.45, so r_tw > 1.262 > 1.260376 ≥ √λ/μ₀, μ₀ ≥ 1.9154712 from BGS-TRACE-198/199) as computer-assisted proofs (python-flint/arb and float BLAS with an a-priori rounding bound). Register the amended Conjecture R′_A (BGS-TRACE-220) as open, with float and heuristic evidence only. **BGS-TRACE-206 stays open**: its boundary now records the reduction, that the operator-radius route to the d = 7 cross term fails, and the heuristic, unproved risk that the frozen R′ fails at m of a few hundred (c(β) ≠ 0 is not certified). An independent referee audit (`computations/verification/lineI/referee/REPORT.md`) returned ACCEPT AFTER FIXES; rounds B1–B9 and R1–R7 and the delta fixes DF1–DF7 are applied (DF3: μ₀ from Line F's certified enclosure; DF4: `rig_dom3b` takes gmax over exact upper ends, and the class 1:3 and 2:1 certificates were rerun and remain certified at R = 1.262; DF5: I9 states the certified range; DF6/DF7: overstatements removed). Withdrawn statements ("diagonal invisible", "primitive prime p ~ h^c", "the resonance terms are exactly the large-e Möbius terms") are not registered. **Owner audit of PR #60 (MERGE AFTER FIXES):**
* BGS-TRACE-204 (Line G G3) moves **open → proved**, with a dependency on BGS-TRACE-212. The proof is the completing-the-square derivation from I2′, checked against brute force at composite d.
* External theorems registered: EXT-BHV-2001 (Bilu–Hanrot–Voutier Theorem 1.4) and EXT-CARMICHAEL-1913 for BGS-TRACE-219; EXT-RS-1962 (Rosser–Schoenfeld Theorem 15) for BGS-TRACE-215.
* BGS-TRACE-216 no longer lists a Lean formalisation.
* The heuristic growth rate is corrected to 1.0185^m.

There is no BGS counterexample and no progress on BGS-TRACE-148. New Lean modules: `Bgs.LineI`, `Bgs.LineIArith`.

## 2026-10-30 — Line H: certified 49-state spectrum for the Line B kick; Conjecture R refuted at η = 2 (TRACE-207–210)

Register BGS-TRACE-207 (the κ lemma, |c_b| = ½ for even b and 0 for odd b for every odd m with 3 ∤ m, and the full-alphabet 49-state lifted trace identity for the Line B kick f_B; paper proof, Lean parity core `Bgs.LineH`, exact check) as a project proof. Register BGS-TRACE-208 (certified spectrum of the lifted 49-state operators for f_B at η = 2, s = −1, N ≡ +196 mod h_m: V_0 has exactly one eigenvalue in |z| > 1.5, simple, with |μ*| ∈ [1.846834, 1.946835] > λ^(1/4); everything else certified inside) and BGS-TRACE-209 (W̃rest_m(2)/m ≥ 1.4·10⁴ for every odd m ≥ 47 with 3 ∤ m) as computer-assisted proofs (python-flint/arb and float BLAS with an a-priori rounding bound). **Consequence and state change:** Conjecture R (BGS-TRACE-179), as stated, is false — for every compact η-range containing 2, max_η |W̃rest_m(η)| is not o(m). The registry gains a `refuted` state (`ALLOWED_STATES` in `scientific_registry_audit.py`, `STATES` in `render_status.py`), and BGS-TRACE-179 moves from open to refuted with BGS-TRACE-209 as its evidence. Scope: R exactly as stated, for the Line B kick. R_NSW, originally part of BGS-TRACE-179, is split out as the open claim BGS-TRACE-210 (owner audit of this change): it is violated at every m ≥ 47 with h_m prime, and whether there are infinitely many such m is unknown. Not covered: odd m with 3 ∤ m in {17, 19, 23, 25, 29, 31, 35, 37, 41, 43} (m = 11, 13 are BGS-TRACE-195), every m with 3 | m, η ≠ 2, and s = +1. BGS itself (BGS-BGS-001) is neither proved nor disproved, and there is no progress on BGS-TRACE-148. BGS-TRACE-196 stays conditional as stated (its conclusion for s = −1 now holds on the lifted space of BGS-TRACE-197; H∞,7 as stated is neither proved nor needed); BGS-TRACE-194 and BGS-TRACE-197 are annotated. An independent referee audit (`computations/verification/lineH/referee/REPORT.md`) returned ACCEPT AFTER FIXES; fixes 1–5 (the referee's independent V_0 re-certification is the certificate of record, with the archived code re-run; rounding constant √2·γ_(2n+2); safe-direction padding of JSON inputs and outward-rounded outputs; corrected table, sign N ≡ +196 and citations, κ lemma; exact scope) and recommendations 6–10 are applied. The statements "R is not disproved" in the entries below describe the state at their dates.

## 2026-10-30 — Lines F and G: lifted transfer operators and the resonance classification (TRACE-197–206)

Register BGS-TRACE-197 (lifted vertex-minus-edge trace identity) and BGS-TRACE-203 (general partial-trace law, finite alphabet) as project proofs. Register BGS-TRACE-198, BGS-TRACE-199, BGS-TRACE-200 and BGS-TRACE-201 as computer-assisted proofs (python-flint/arb), for the single-cosine k1 kick (and f7 for 3 ∤ m) only. Register BGS-TRACE-202, BGS-TRACE-204 and BGS-TRACE-205 as open, and Conjecture R′ (BGS-TRACE-206) as open with a closure condition; the registry has no separate conjecture state. Both lines passed an independent referee audit (`computations/verification/lineFG/referee/`); its blocking fixes are applied: every quoted bound is rounded in the safe direction, BGS-TRACE-199 is stated as proving the conclusion of BGS-TRACE-188 on a different space (H∞ itself is not proved), η = 2.5 is included only with the added sector-6 = sector-2 reflection lemma and its certificate (completed after the audit), the Line G §3 overclaim is removed, G3 is open and G7 is a heuristic, and R′ is frozen to one definition for k1. The pre-registered m = 17 prediction for R′ is committed with its sha256; its outcome is not included in this change. BGS-TRACE-187, 188 and 196 and BGS-TRACE-179 are annotated; their states are unchanged. Conjecture R (BGS-TRACE-179) is not disproved; there is no BGS counterexample and no progress on TRACE-148. New Lean modules: `Bgs.LineF`, `Bgs.LineG`.

## 2026-10-30 — Line E: resonant residues of the fixed-kick cat map (TRACE-183–196)

Register BGS-TRACE-183 and BGS-TRACE-184 as project proofs. Register BGS-TRACE-185, BGS-TRACE-186 and BGS-TRACE-187 as computer-assisted proofs for the single-cosine k1 kick only. Register BGS-TRACE-193 (computer-assisted via 187), BGS-TRACE-194 and BGS-TRACE-195 (computer-assisted, m = 11 and 13 only) as proofs, after a second independent referee audit of the step-2 extension (`computations/verification/lineE/referee2/`; required fixes R1–R7 applied, including safe-direction rounding of every quoted certified bound). Register BGS-TRACE-188 and BGS-TRACE-196 as conditional. Register BGS-TRACE-189, BGS-TRACE-190, BGS-TRACE-191 and BGS-TRACE-192 as open (189, 190 and 192 are numerical records or identifications). Claims 183–192 passed an independent referee audit, and its required fixes F1–F13 are applied; the report is in `computations/verification/lineE/referee/`. BGS-TRACE-179, 180 and 182 are annotated, and their states are unchanged. Conjecture R is not disproved for any kick. The k1-kick analogue of R is violated on a finite range, and conditionally for all large m. For the Line B kick, |W̃rest_m(2)| > m is certified at m = 11 and 13 only; an m = 17 certificate is pending and nothing is claimed for it. There is no BGS counterexample and no progress on TRACE-148.

## 2026-10-29 — Fixed diagonal kick (TRACE-163–182)

Register BGS-TRACE-163, BGS-TRACE-165, BGS-TRACE-166, BGS-TRACE-167, BGS-TRACE-168, BGS-TRACE-169, BGS-TRACE-170, BGS-TRACE-171, BGS-TRACE-172, BGS-TRACE-173, BGS-TRACE-175 and BGS-TRACE-178 as project proofs, BGS-TRACE-164, BGS-TRACE-174 and BGS-TRACE-176 as conditional, and BGS-TRACE-177, BGS-TRACE-179, BGS-TRACE-180, BGS-TRACE-181 and BGS-TRACE-182 as open, for the fixed diagonal kick \(U=K_\eta M_N\). On main at 502af245 the highest registered TRACE id was BGS-TRACE-162, so 163 was the next free id and the packet's block was not renumbered. BGS-TRACE-177 is numerical-only and is filed as open. BGS-TRACE-173 is proved only with the directed-rounding constants; the authors' float constants are excluded. Nothing is proved at \(\tau=m/N=O(1)\). All results are fixed-\(m\) (diagonal / below Ehrenfest). This is not progress on BGS-BGS-001 or BGS-TRACE-148. "\(B_m\to 2m\)" is not claimed. Theorem N covers a finite list of certified NSW primes, and the infinitude of NSW primes is open. The Theorem D_cert arithmetic is IEEE float with an a-priori error bound (plus arb coefficients), not full interval arithmetic, until the full directed-rounding rerun. (Second-reader annotation, not part of the referee's verbatim text: that rerun has now been done, 93/93; non-claim 8 still applies to the authors' float grid, and BGS-TRACE-173 is proved with the directed-rounding constants only.) The parity crossover is the derandomized analogue of the known BGOS/Pandey–Mehta symmetry-breaking crossover. It is not a Keating–Mezzadri pseudo-symmetry, and the phenomenon is not new. Lean certifies finite arithmetic facts only. No new external dependency.

## 2026-10-29 — Band-limited random kicks (TRACE-149–162)

Register BGS-TRACE-149, BGS-TRACE-150, BGS-TRACE-151, BGS-TRACE-152, BGS-TRACE-154, BGS-TRACE-156, BGS-TRACE-157 and BGS-TRACE-160 as project proofs, BGS-TRACE-153 as verification-pending, BGS-TRACE-158 as conditional, and BGS-TRACE-155, BGS-TRACE-159, BGS-TRACE-161 and BGS-TRACE-162 as open, for \(U=e^{i\eta V_\theta}M_N\) with a fixed finite set of random cosine modes. The packet numbered these statements BGS-TRACE-149 through BGS-TRACE-162 and warned that a Line B packet uses the same block. On main at d6fa6e2a the highest registered TRACE id was BGS-TRACE-148, so 149 was the next free id. Historical gaps BGS-TRACE-138 and BGS-TRACE-139 were left unused. Line B had not merged, so the numbers were kept and no Line B claim id was added as a dependency. The exact bridge and the orbit form are Line B's Theorem 1 applied for each kick realisation and the Boasman–Keating mechanism, not new. The \(1/N\) remainder is not uniform in \(\eta\) or \(K\). The strong-kick value \(B_m^{\mathrm{sym}}\) is reached only under separation of dihedral classes, which is verified by computer for \(m\le 7\), not proved for general \(m\). \(B_m^{\mathrm{sym}}<2m\) is proved for every odd \(m\) and open for even \(m\) beyond the computed range. The decay \(c_1\to 0\) is conditional and Gaussian-only. The full-band result is only a transfer of BGS-TRACE-146. The intermediate band is a sketch. The crossover scaling is a conjecture with Monte Carlo diagnostics. Lean certifies only finite arithmetic facts. This does not prove BGS-TRACE-005 or BGS-BGS-001, and it says nothing about eigenvalue statistics beyond the second moment of \(\mathrm{Tr}\,U^m\) at fixed \(m\). No new external dependency.

## 2026-10-29 — Random-phase encounter pairs (TRACE-143–148)

Register BGS-TRACE-143 through BGS-TRACE-146 as project proofs, BGS-TRACE-147 as verification-pending, and BGS-TRACE-148 as an open conjecture, for the Haar diagonal-phase ensemble \(U=D M_p\) with \(S=\begin{pmatrix}3&4\\2&3\end{pmatrix}\). The packet's provisional numbers BGS-TRACE-138 through BGS-TRACE-143 were already partly occupied on main (BGS-TRACE-140 through BGS-TRACE-142), so the statements are numbered from BGS-TRACE-143. The coefficient of \(1/p\) is \(-2m^2\) for every \(m\ge 5\). Gnutzmann–Seif 2004 derived \(2\tau-2\tau^2\) diagrammatically for this ensemble, Gnutzmann–Altland 2005 and Pluhař–Weidenmüller 2014 predict the full COE form factor non-rigorously, and Berkolaiko–Keating 1999 did exact all-pairs combinatorics for random-phase star graphs; new here is only the rigorous fixed-\(m\) exact-in-\(p\) result, the complete classification including swaps, and the \(m\le 12\) expansions. BGS-TRACE-147 records those expansions. An independent referee engine reproduces every coefficient at 171 primes and is deposited; the claim stays verification-pending, and promotion is a separate status decision, as for BGS-RES-022. The values at \(m=1,2,3\) remain BGS-TRACE-127. This does not prove BGS-TRACE-005 or BGS-BGS-001, and it does not cover the fixed kick. No new external dependency.

## 2026-10-29 — Twisted closure, scalar-return revival, and half-period parity (TRACE-133–137)

Register BGS-TRACE-133, BGS-TRACE-134 and BGS-TRACE-135 as project proofs, and BGS-TRACE-136 and BGS-TRACE-137 as open conjectures, for the position-diagonal kick (\(\sigma_d=13203/32000\)). BGS-TRACE-133 gives the twisted closure formula with Pell cocycle \(\beta\) and \(|\Lambda_m|=N^{m-2}\). BGS-TRACE-134 gives a pointwise bound at the scalar return and the \(\exp(-\eta^2 t\sigma_d/2)\) limit on the minimal-period sequence; the explicit bound is non-informative at computable \(N\) (below \(1\) only from \(N\approx10^{191}\) at \(\lambda=1/4\)); only the limit is proved. BGS-TRACE-135 reduces \(\operatorname{Tr}U^t/\operatorname{Tr}M_N^t\) to \(N^{-1}\operatorname{Tr}(APA P)\) when \(S^{t/2}\equiv -I\). Monte Carlo rows for 136 and 137 and for the limit theorem are diagnostics only. Python, C++, and a Lean rational witness certify the stated integer facts; the operator identities and analytic bounds are not formalized. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Referee correction of TRACE-131 and TRACE-132

Symmetry of \(M_N(S)\) is the congruence \(\alpha\equiv\delta\pmod N\), not the integer equality \(\alpha=\delta\). The matrices \(\begin{pmatrix}6&1\\5&1\end{pmatrix}\) at \(N=5\), \(\begin{pmatrix}1&1\\3&4\end{pmatrix}\) at \(N=3\), and \(\begin{pmatrix}0&1\\-1&-3\end{pmatrix}\) at \(N=3\) are symmetric. For every diagonal unitary \(D\), \(\Theta'=DEK_0\) with \(E=\mathrm{diag}\,e_N(\kappa(\delta-\alpha)x^2)\) satisfies \((\Theta')^2=I\) and reverses \(DM_N\). It reduces to \(DK_0\) when \(\alpha\equiv\delta\pmod N\). This is the pseudo-symmetry of Keating and Mezzadri, Nonlinearity 13 (2000), 747–775, and it is why the fixed-time value \(2m\) holds for every hyperbolic \(S\). The limit \(1\) for \(\eta=o(N^{-2/3})\) holds along odd \(N\) coprime to \(\beta(2-u_m)\). Along \(N\) divisible by \(7\) (e.g. \(35,77,91,707\)) the time-\(3\) kernel has order at least \(49\), so the limit \(1\) fails when \(\gcd(N,\beta(2-u_m))>1\). The Bessel formula allows frequencies divisible by \(N\); the case \(\{1,5\}\) at \(p=5\) has \(D_2=-75/2\). \(D_2=\frac12 g''(0)\), and \(g\) is even in \(\eta\). The dependency of TRACE-131 on TRACE-127 is registered. Lean now decides the companion matrix identity and the determinant identity on listed examples, and the trace-\(-16\) kernels are reduced from the integer matrices. The arithmetic in `HyperbolicShortTime.lean` is labelled as arithmetic of displayed integers, not a formalization of the occupation bound. Prior comparisons are Keating, Nonlinearity 4 (1991), 309–341; Knabe, Journal of Physics A 23 (1990), 2013; Mezzadri, Nonlinearity 15 (2002); Diaconis–Shahshahani, Journal of Applied Probability 31A (1994), 49–62; and Rains, Probability Theory and Related Fields 107 (1997), 219–241. The factors \(2m\) and \(m\) are the counts of Tanner and of Pakoński–Życzkowski–Kuś. No new claim and no new external dependency. BGS-TRACE-005 and BGS-BGS-001 remain open.

## 2026-10-29 — Fixed-time limits for a general hyperbolic cat map

Register BGS-TRACE-132. For every hyperbolic \(S\) and every odd \(N\) coprime to the upper-right entry, Haar diagonal phases satisfy \(\lvert\mathbb E\lvert\operatorname{Tr} U^m\rvert^2-2m P(N,m)/N^m\rvert\le m!(1+m(m-1))/N\) for \(m\ge 3\). The fixed-time limit is \(2m\). The antiunitary \(\Theta'=DEK_0\) reverses \(DM_N\) for every hyperbolic \(S\). Times one and two tend to \(1\) and \(2\). A finite cosine with \(\eta=o(N^{-2/3})\) tends to \(1\) along odd \(N\) coprime to \(\beta(2-u_m)\); along \(N\) divisible by \(7\) (e.g. \(35,77,91,707\)) the time-\(3\) kernel has order at least \(49\), so the limit \(1\) fails when \(\gcd(N,\beta(2-u_m))>1\). If the frequencies \(\{1,\ldots,m\}\) are present, the limit \(\eta\to\infty\) and then \(N\to\infty\) recovers \(2m\). A second diagonal factor is conjugate to one diagonal times \(M_N(S)\) and does not produce the value \(m\). Row inversion on an odd prime not dividing the upper-right entry has limit \(m\). A momentum sine leaves the class, and its form factor is not identified. Python and C++ check the occupation inequalities; a Lean witness certifies the error constants and the comparison \(121\cdot 11>6\cdot 18\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Diagonal phase average for every hyperbolic cat map

Register BGS-TRACE-131. For every hyperbolic \(S\in\mathrm{SL}(2,\mathbb Z)\) and every odd \(N\) coprime to the upper-right entry, the position-basis quantization is unitary and flat, and symmetric exactly when the diagonal entries are congruent modulo \(N\). The antiunitary \(\Theta'=DEK_0\) reverses \(DM_N\) for every such \(S\). The pure squared trace equals the kernel order. A finite cosine kick with independent uniform phases has quantum average equal to a Bessel path sum. The order-two expansion is \(|\ker|+\eta^2 D_2+\rho\) with the remainder of TRACE-126. The trace determines \(u_n\), \(v_n\), \(\det(S^n-I)\), and, when \(p\) does not divide the upper-right entry, the prime kernel trichotomy and the splitting law \(p-(\Delta/p)\). Two matrices of trace \(-16\) have kernels \(9\) and \(3\) modulo \(3\); both upper-right entries are divisible by \(3\), so they lie outside the quantization hypothesis. At an identity revival \(D_2=-m(\sigma-\sigma_0)p^2\), including \(-42025/8\) and \(-375/8\) for the kick \(a_1=1\), \(a_2=1/2\). Time one equals \(1\) when \(\gcd(2-\operatorname{tr} S,N)=1\). The fixed-time limit and the all-order revival law are not claimed. Python and C++ recompute the integers and the floating-point checks; a Lean witness decides Cassini at ten pairs, the companion and determinant identities on the listed matrices, the kernels of those reductions, and the integer products \(42025\) and \(375\). Those products are not a formalization of \(D_2\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Unitary short-time value for momentum phases

Register BGS-TRACE-140, BGS-TRACE-141 and BGS-TRACE-142. Haar position phases and Haar momentum phases give \(\mathbb E\lvert\operatorname{Tr} U^m\rvert^2\to m\) on odd primes with \(\lambda\not\equiv -1\), with error at most \((m!)^2(1+2m(m-1))/p\). At time two the same congruence is required; if \(\delta\equiv -1\) the limits are \(4\) and \(2m\). The moment of order \(2k\) tends to \(k!\,m^k\). Gaussian momentum phases identify the main term \(m(1+e^{-vm})\); the non-injective remainder is not bounded, so that limit is verification-pending. The odd symbol energy is \(9/125000\). The choice \(v=\sigma_{\mathrm{odd}}\eta^2\) is a convention; partner-variance matching gives twice this. Python and C++ recompute the occupation buckets at the primes \(5\), \(7\) and \(11\). The recorded sample is \(600\) draws with mean \(3.709\), and an independent exact value is \(3.7555\) at \(p=29\), \(v=0.4\). Lean decides the odd energy, the constants \(468\) and \(20\), and the residues \(27\bmod 5,7,11,13\) (so \(3^3\not\equiv 1\) at \(5\), \(7\), \(11\) and \(3^3\equiv 1\) at \(13\); the conditions \(t=1,2\) are not formalized). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.


## 2026-10-29 — Self-red-team of the position-diagonal antiunitary

BGS-TRACE-130. Similarity to a symmetric unitary does not assign an orthogonal class, and it does not exclude a CUE form factor: \(O^T\Lambda O\) with orthogonal \(O\) and CUE eigenvalues is symmetric and has the CUE form factor. The proved statement is the antiunitary \(\Theta=DK_0\), with \(\Theta^2=1\) and \(\Theta U\Theta^{-1}=U^\dagger\). The class name is a heuristic. The symbol fails to be \(K_0\)-even only for almost every phase. The coefficient on the row \(\ell=1\) is \((-3-4i)r(k)\), not \((-3+4i)r(k)\). Lean certifies the cross-multiplication of \(1/4+1/4=1/2\), not the two arithmetic tautologies \(1+1=2\) and \(2\cdot 2=4\). No new external dependency.

## 2026-10-29 — Local antiunitary for a position-diagonal kick

Register BGS-TRACE-130. For every real diagonal kick, the antiunitary \(\Theta=DK_0\) satisfies \(\Theta^2=1\) and \(\Theta U\Theta^{-1}=U^\dagger\). The orthogonal-class name is a heuristic and does not exclude a CUE form factor. Each of the rows \(\ell=\pm 1\) has energy \(9/160000\). The momentum sine has symbol energy \(1/2\) and is not a function of position. Neither statement evaluates the averaged squared trace for \(m\ge 2\). The time-one value remains \(1+\rho_1\) from BGS-TRACE-129. The samples at \(N=201\) and \(N=203\) are not used, and the scale \(\eta^2 N\cdot 9/160000\) is not derived. Python and C++ check the symmetric conjugate and the momentum sine at \(N=3,5,7,11\); a Lean witness certifies the energy identity \(900/4000^2=9/160000\), \(\det(S-I)=-4\), and the cross-multiplication of \(1/4+1/4=1/2\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Self-red-team of the scalar-return Bessel identity

BGS-TRACE-129. The Bessel identity is the phase average of the classical position-diagonal orbit sum. It is not the quantum sixteen-phase average. A referee Monte Carlo, recorded in the proof, differs from that classical average by ≈1.7 at \(N=11\), \(m=12\), and by up to ≈6 at \(N=29\), \(m=10\) (\(\eta=2\)), and tracks it at zero quadruple excess for \(\lambda\lesssim 1\). The factor \(J_0\) and its products are classical. Time one equals \(1+\rho_1\), not the bare value \(1\). Each of \(\ell=\pm 1\) has energy \(9/160000\), so \(9/80000\) together. Lean does not certify that the order at \(p=11\) is exactly \(12\), and the quadruple rows at \(11\), \(31\), \(41\) and \(47\) are Python-only. No new external dependency.

## 2026-10-29 — Bessel form of the scalar-return orbit sum

Register BGS-TRACE-129. At a scalar return \(S^m\equiv I\), the cat-map propagator is a scalar and the kicked trace is the trace of the Egorov product. Modes congruent to \(0\) cancel in the squared modulus, and the time-one coefficient vanishes for every odd dimension, so the averaged squared trace equals \(1+\rho_1\) inside the perturbative window. For a position-diagonal kick the classical orbit sum has an exact phase average, a product of Bessel factors \(J_0\) indexed by pairs of torus points. That identity is not the quantum sixteen-phase average. Its degree-two jet is the exponential \(\exp(-m\sigma_{\mathrm{diag}}\eta^2)\). The degree-four gap is the additive excess of the position orbit: it vanishes at the primes \(7\), \(31\), \(41\) and \(47\), and it does not vanish at \(11\). Each of the rows \(\ell=\pm 1\) has energy \(9/160000\). No COE limit and no CUE crossover are claimed. Python and C++ check the orbit counts and the Bessel sum in floating point; a Lean rational witness certifies the orders at \(5\) and \(7\), the quadruple counts at those primes, and the energy identity. It does not certify minimality of the order \(12\) at \(p=11\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Self-red-team of the short-time diagonal-phase argument

BGS-TRACE-128. The Kloosterman scaling is \(S(ra,sa^{-1})=S(r,s)\). The identity \(S(ra,sa)=S(r,s)\) is false. The phase gap is \(\delta=3\cdot 4^{-1}-9\), and \(4\delta=-33\) is unchanged. The monomials \(x_a^{-1}x_b\) are distinct reduced monomials, not characters. A second diagonal is removed by conjugating with \(D_2\): \(D_2(D_1M_ND_2)D_2^{-1}=(D_2D_1)M_N\). The square-root conjugation is false. The limits are unchanged. No new external dependency.

## 2026-10-29 — Short-time limits of the diagonal-phase form factor

Register BGS-TRACE-128. For the symmetric cat map times independent uniform phases on the diagonal, the averaged squared trace at each fixed time \(m\ge 3\) tends to \(2m\), with an explicit \(O(m!/N)\) gap from the dihedral main term \(2m P(N,m)/N^m\). The same bound reaches \(m\le c\log N/\log\log N\) for \(c<1\) and does not reach \(m\le N^{\alpha}\). Inverting the rows by \(x\mapsto x^{-1}\) on an odd prime breaks the reversal and the limit is \(m\), with a Kloosterman error of order \(p^{-1/4}\). At \(p=3\) the inversion is the identity. A second independent diagonal is removed by conjugating with \(D_2\), not with \(D_2^{1/2}\). Python and C++ check the occupation sums in floating point; a Lean rational witness certifies the integer form of the symmetric error constant, the time-three comparison, and the Kloosterman quadruple counts at the primes 5 and 7. The dependency on BGS-TRACE-127 is the occupation expansion and the times one and two. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Self-red-team of the diagonal-phase symmetry

BGS-TRACE-127. The time-reversal is the antiunitary \(\Theta=DK_0\), with \(\Theta^2=1\) and \(\Theta U\Theta^{-1}=U^\dagger\). Similarity to \(D^{1/2}M_ND^{1/2}\) does not assign an orthogonal class. That class name is a heuristic, not a COE form factor. The Tanner locator is Section II.2, and Section IV.1 is the closest prior result for the heuristic. The symmetric conjugate is named \(\Sigma_D\). No counting identity changes. No new external dependency.

## 2026-10-29 — Diagonal random-phase form factor

Register BGS-TRACE-127. For a flat matrix times independent uniform phases on the diagonal, the averaged squared trace equals \(1\) at time one, \((2N-1)/N\) at time two, and is at most \(m!\) at every positive time. For the cat-map quantization the time-three value is \((6N^2-9N+4)/N^2\). The pure kernel has order \(1\) at time two, and order \(49\) or \(1\) at time three according as \(7\) divides the odd modulus. A draft formula \(7^{2v_7(N)}\) was rejected by the count at \(N=49\), which returns \(49\). The sixteen-phase ensemble of BGS-TRACE-126 is not identified with CUE or COE. Python and C++ check the occupation sums in floating point; a Lean rational witness certifies the integer factorisations and gaps. The dependency on BGS-TRACE-126 is the trace-closure lemma only. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Phase-averaged form factor

Register BGS-TRACE-126. For the auxiliary ensemble in which the 16 mode pairs of the kick carry independent uniform phases, the averaged squared trace equals \(|K_m|+\eta^2 D_2+\rho\), with \(D_2\) an explicit Gauss-sum coefficient and with an operator-norm remainder. At an odd prime \(p\) the second-order revival coefficient is \(-m(\sigma-\sigma_0(p))p^2\). The zero-mode energy is \(\sigma_0(3)=81/64000\), \(\sigma_0(5)=1/320000\), \(\sigma_0(7)=81/200\), and \(\sigma_0(p)=0\) for every prime \(p\ge 11\). The fixed kick has a linear term, nonzero at \(N=11\), \(m=3\). Parity and position-basis conjugation fail for the kicked propagator when \(0<\lvert\eta\rvert<\pi/B\), except at dimension \(7\), where \(A_7=(9/10)I\). A same-day self-red-team correction replaced the first formula \(-m\sigma N^2\), which omitted those three zero modes, and enlarged the remainder by the quartic term inside the Taylor polynomial. No revival limit is proved. The dependency on BGS-TRACE-117 is the phase-free conjugation only. Python, C++ and a Lean rational witness certify the symbol arithmetic. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Separation wording and the semiprime partner

Section 2 of `mathematics/fixed-map/offdiagonal_strategy.md` no longer treats an upper bound below \(5/7\) as a separation of \(L_N(U_N;1)\) from the CUE value: \(5/7\) is larger than \((1-e^{-2})/4\). A separation is a weighted one-term gap, an upper bound \(L_N(U_N;1)\le(1-e^{-2})/4-c\) for a fixed \(c>0\), or a lower bound above \(3/4\). The fixed-point count of a trace square is the lemma in Section 2 of BGS-TRACE-120, cited in Section 2 of BGS-TRACE-122. Theorem 3 of BGS-TRACE-122 states that the non-short partner of \(7\) is an inert prime of order \(q+1\), which already includes \(q=3\). No claim state changes. The Python, C++, and Lean certificates were not re-run.

## 2026-10-29 — Strategy note ranks the concrete model and the generalizations

Section 7 of `mathematics/fixed-map/offdiagonal_strategy.md` ranks open routes by significance and by realistic provability. Priority 1 is a correct statement about this \(U_N\). The signed sum at times of order \(N\) is the significant target and is not within reach. An exact symmetry test of the 32-mode symbol is the realistic concrete step; `BGS-FM-001` already excludes a classical \(C^1\) reversor and does not classify the quantum ensemble. Priority 2 records, without opening a claim, a pure-map statement for a general hyperbolic matrix in \(\mathrm{SL}(2,\mathbb Z)\), a general trigonometric kick, the monomials \(\tau^2 N^3\) and \(\tau^2 N^2\) already present in the second derivative of `BGS-TRACE-125`, and an ensemble classification. The classification and the scaled-coupling limit law are not within reach. No new claim ID.

## 2026-10-29 — Strategy note records an unverified reconnaissance

Section 6 of `mathematics/fixed-map/offdiagonal_strategy.md` records an external reconnaissance as a lead list. No constant from that report is adopted. The half-order divisibility in the report is the lemma already proved in BGS-TRACE-121 and corrected by ERR-061; no maintained note on this branch still uses \(t=(p+1)/2\) as a nonempty class. The hypothesis \(2t\ge p+1\) in BGS-TRACE-120 remains a lower bound and, on an odd prime, is exactly the inert full order. The next route named in the note is a symmetry-breaking reformulation of the kicked model. No new claim ID is opened. BGS-TRACE-005 and BGS-BGS-001 remain open.

## 2026-10-29 — Uniform Pell-orbit overlap

Register BGS-TRACE-125. For every odd integer \(n\ge5\), at \(N=u_n\), the fixed symbol overlaps only at lags \(1\) and \(n-1\), both with value \(-7/2000000\). The quadratic trace coefficient of the transported product is exactly \(n\cdot1650797/4000000\). The sequence \(u_n\) is exponential, not an arithmetic progression. The index \(n=5\) is a finite scan; every larger odd index is a size, archimedean, and quadratic-form argument. This is \(f''(0)\), not a bound on \(f(1)\). The claim does not assert that Kurlberg–Rudnick degeneracies fail to be eigenvalues of the kicked propagator: that sentence does not follow from BGS-FM-032. A separation of \(L_N(U_N;1)\) from the CUE value is a bound on the Abel sum, not a lower bound on one normalized trace. Prime squares, including \(315\), are placed by BGS-TRACE-124; \(315\) is short because its radical \(105\) is short. The ledger phrase says that Lean certifies integer comparisons only. Python, C++ and that Lean witness certify the integers. No new kick window is claimed. The third-order remainder, the signed off-diagonal sum, and the limit stay open. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Half-order errata and the odd-modulus assembly

ERR-061, ERR-062 and ERR-063 correct three statements already registered on this branch. The order \(t=(p+1)/2\) does not occur: a split order divides \((p-1)/2\), and an inert cofactor \((p+1)/t\) is odd. The long class is the inert full order. A split full-order tower and a non-short product of \(3\) with a short prime are empty, so they are not kick windows. The square-free window \(N=15r\) requires an odd prime \(r\ge7\); \(N=45\) is strongly short and is covered by \(8t\le3N\). Theorem 1 of BGS-TRACE-124 is assembled from BGS-TRACE-121 Theorems 1 and 2, BGS-TRACE-122 Theorem 3, BGS-TRACE-123 Theorem 1, and Sections 2--7 for a non-square-free modulus that is not a prime power. The ledger phrase for BGS-TRACE-117 through BGS-TRACE-124 now says that Lean certifies integer comparisons only. The inert-domain check compares \(\gamma<5\), not \(\gamma/q<5\). No claim state changes. BGS-TRACE-005 and BGS-BGS-001 remain open.

## 2026-10-29 — Every odd modulus lies above 3/4 or below 5/7

Register BGS-TRACE-124. Every odd modulus \(N\ge3\) satisfies \(L_N(M_N;1)>3/4\) or \(L_N(M_N;1)<5/7\). The modulus \(315=3^2\cdot5\cdot7\) is short because its radical \(105\) is short; no separate expansion at \(315\) is required. The fixed kick \(\tau=10^{-80}\) preserves the gap above \(3/4\) when \(8t(N)\le3N\) and \(N\le10^{39}\), through \(10^{26}\) on the ratio-preserving families whose pure margin exceeds \(13/420\), and through \(2\cdot10^{26}\) for \(N=15r\). The kick is not claimed for a ceiling tower: at \(3\cdot23\) the gap \(575/22594\) is smaller than \(13/420\). It is not claimed for an inert exponent-one partner \(q\ge40\), for \(15r>2\cdot10^{26}\), or at \(u_{207}\). Python, C++ and a Lean rational witness certify the integers. Lean certifies the closed comparisons, including the fraction at inert partner \(13\); the other twenty-six inert rows are recomputed only by the two integer programs. No density is proved. The signed off-diagonal sum stays open. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Square-free products of at least three primes

Register BGS-TRACE-123. Every square-free odd modulus with at least three distinct prime factors satisfies \(L_N(M_N;1)>3/4\), at distance greater than \(1/2\) from the CUE value. The fixed kick \(\tau=10^{-80}\) preserves that gap through \(10^{39}\) when there are at least four prime factors, and when the modulus is a product of three primes not divisible by \(15\). On \(N=15r\) the kick is preserved only through \(10^{26}\); above that window the pure sum remains above \(3/4\) and the kick is not claimed. The modulus \(N=195\) is not short, and the bound there is the eight-term subset expansion. A prime square is outside this note. The later note BGS-TRACE-124 places \(315=3^2\cdot5\cdot7\), which is short because its radical \(105\) is short. ERR-063 corrects the wording \(r\) other than \(5\). Semiprimes remain the dichotomy of BGS-TRACE-122. Python, C++ and a Lean rational witness certify the integers. No density is proved. The kick at \(u_{207}\) remains unresolved. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — Chinese product for the cat-map trace square

Register BGS-TRACE-122. For every odd modulus the pure trace square is the product of the trace squares at the prime-power factors, and the order is the least common multiple of the prime-power orders. The square-free Abel sum is a finite combination of geometric series. Every product of two odd primes is decided: short composite orders, non-short multiples of \(7\), and non-short products of \(3\) with a short prime lie above \(3/4\), and every remaining semiprime lies below \(5/7\). The fixed kick preserves the gap above \(3/4\) through \(10^{26}\) on \(N=21\). ERR-062 records that a split full-order multiple of \(7\) and a non-short product of \(3\) with a short prime do not occur. It is not transferred on the side below \(5/7\). A modulus with three distinct prime factors is not classified in this note; \(N=195\) is settled later by BGS-TRACE-123. Python, C++ and a Lean rational witness certify the integers. No density is proved. The kick at \(u_{207}\) remains unresolved. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-29 — cat-map order trichotomy

Register BGS-TRACE-121. The order of \(C\) modulo an odd prime divides \(p-\varepsilon\) and is short, long, or split-half. Short primes lie above \(3/4\), long primes lie below \(5/7\), and the only undecided prime of TRACE-120, \(p=7\), lies above \(3/4\). Every larger split-half prime lies below \(41/60\). The lifting depth decides every odd prime power: powers of \(7\) stay above \(3/4\), depth-one powers of a larger split-half prime stay below \(5/7\), and depth at least two puts the higher powers above \(3/4\). The fixed kick preserves these comparisons through \(10^{26}\), except the large split-half powers, which stop at \(10^{25}\). The pure map at every odd Pell dimension \(n\ge5\), including \(u_{207}\), is already above \(3/4\); the kick at \(u_{207}\) is not. Python, C++ and a Lean rational witness certify the integers. No density is proved. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-28 — cat-map order ladder

Register BGS-TRACE-120. The multiplicative order \(t(N)\) of the frequency matrix \(C\) decides the Abel statistic. If \(12t(N)\le5N\), the pure cat map satisfies \(L_N(M_N;1)>3/4\). If \(p\) is an odd prime and \(2t(p)\ge p+1\), the distance from \(L_p(M_p;1)\) to the CUE value is less than \(1/2\). The fixed kick preserves the short side for every such odd \(N\le10^{39}\) and the long side for every such prime \(p\le10^{26}\). At \(N=35\), not a Pell number, one return lies below \(3/4\) and the geometric ladder crosses it. Python, C++ and a Lean rational witness certify the integers. The kicked map at \(u_{207}\) is not decided. BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## 2026-10-28 — kick-blind arithmetic spikes

Register BGS-TRACE-119. At the single dimension \(N=u_{205}\) the fixed kick satisfies \(L_N(U_N;1)>3/4\). The argument is a positive-time diagram expansion: resonant diagrams of degree at most 11 are archimedean zeros, and indecomposable gaps are at most 4, so the activity remainder stays below the Abel budget. Python, C++ and a Lean rational witness certify the integers. The third-order operator-norm remainder and the Hilbert--Schmidt triangle remain silent at this index. At \(n=207\) the pure second-order center still lies below \(3/4\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

Register BGS-TRACE-118. At \(N=u_{203}\) the fixed kick still satisfies \(L_N(U_N;1)>3/4\), by a second-order trace expansion. The cat-map orbit of the symbol is trace-orthogonal except for one overlap of size \(7/10^6\). Python, C++ and a Lean rational witness certify the integers. The same third-order majorant is vacuous at \(n=205\). The Hilbert--Schmidt triangle is silent at that index as well, and at \(n=207\) the pure second-order center lies below \(3/4\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

Register BGS-TRACE-117. The pure cat map stays a fixed distance from the CUE Abel value on \(N=u_n\) for every odd \(n\ge5\). The fixed kick \(\tau=10^{-80}\) preserves that gap on the 99 odd indices \(5\le n\le201\), through the 77-digit dimension \(u_{201}\). Python, C++ and a Lean rational witness certify the integers. The one-term estimate stops beating \(3/4\) at \(n=203\). BGS-TRACE-005 and BGS-BGS-001 remain open. No new external dependency.

## Aristotle formalization integration, 28 October 2026

Adapted all 39 substantive modules from the older Aristotle snapshot into the existing Lean 4.33.1 graph. The [coverage map](formalization/MATHLIB_LAYER_RU.md) and [receipt](evidence/formalization/aristotle_20261027/receipt.json) record exact theorem scope, 589 axiom-audited declarations and the successful aggregate build. ERR-060 corrects the pure-loss scalar identity in the proof and manuscript. Current claim states, TRACE-114–116 and pinned dependencies are retained; no BGS closure is asserted.

## 2026-10-27 — operator-resolution continuation

Adopt TRACE-114/115/116 at their exact author-reviewed scopes; connect the uniform trace bound to compact pair-test transfer, and distinguish the short-trace barrier from the exact kicked family. Synchronize the registry, theorem index, dependency graph, topic views, bilingual introductions and unified manuscript. Consolidate the historical chat source into one immutable archived Markdown; avoid duplicate proofs and programs. Unreviewed candidate estimates remain explicitly unadopted.

## research-2026.10.1 — phase-5 release preparation

Layered licensing applied (decision R3): source code under MIT
(`LICENSE`), scholarly texts and data under CC BY 4.0
(`LICENSE-CC-BY-4.0.txt`); per-path map in `LICENSE_POLICY.md`.
License sections added to `README.md` / `README.ru.md`;
`CITATION.cff` and `.zenodo.json` license fields set (single-license
fields, D4 confirmed). No registry state, claim
status, or manuscript content changed by this package. Release tag research-2026.10.1; registry at freeze: 199 claims =
173 proved / 12 verification-pending / 9 conditional / 5 open
(BGS-BGS-001, BGS-CAYLEY-005, BGS-INFO-001, BGS-RES-003,
BGS-TRACE-005). The freeze receipt
(record/audits/freeze_receipt_research-2026.10.1.md) carries the
release commit.

## 2026-10-22 — full repository recheck

Restored and authenticated all 6,563 files of main at 7fb99b4 before editing.
Repaired five missing external dependencies for CAYLEY-006/007, 30 missing
source anchors and 19 malformed errata authority paths. Corrected a registry
audit false positive and added regression checks. Aligned the arithmetic
density main term with the checked source; synchronized generated views and
current English/Russian navigation. No claim state was changed by this recheck.
[Findings and actual checks](record/audits/repository_recheck_20261022/report.md).

## 2026-10-21/22 — trace closure and complete spectral edition

Integrated the 535-unit final spectral source edition and TRACE-106 through
TRACE-113. Analytic project proofs close the earlier TRACE-109/110 input
qualifications; TRACE-112 supplies an independent displacement-density route,
and TRACE-113 supplies the uniform power-trace input. Global matching has
order $1/\log N$, including a Pell lower order. Microscopic BGS remains open.
[Trace closure review](record/spectral_research/trace_closure.md) and
[source integration](record/spectral_research/spectral_final_integration.md).

## 2026-10-20 — repository reconciliation

Current navigation and complete dependency views are generated from the authorities.
Reconciled bibliographic coverage and explicit epochs; repaired optimized entry guards.
[Review and actual verification scope](archive/record/repository_reconciliation_20261020.md).

## 2026-10-19

- Integrated eleven missing research packets and the reviewed two-channel
  attachment with a 654-file SHA-256 inventory and preserved execution records.
- Added TRACE-095 through TRACE-105 with explicit conditional and auxiliary
  boundaries; synchronized source statements, ledger, registry/DAG, navigation
  and the manuscript continuation. Fixed-model BGS remains open.
- Completed the four-port and second-defect account, the joint quartic cluster
  theorem, and exact positive Cauchy-source laws with a signed-source obstruction.
- ERR-031 records stale source provenance of one historical failed run. New
  invalid/failed attempts are retained separately from corrected runs.

## 2026-10-16

- Reconciled the 15 October 103-section record, 16 original notes and all 90
  historical inventory entries against main e20825f. Preserved source hashes.
- Integrated 11 scoped theorem/reduction families, corrected resonance
  necessity, Hardy hypotheses and discrete Toeplitz grid requirements.
- Added reproducible source checks and execution receipts; synchronized the
  scientific registry, DAG, thematic navigation, RU/EN reading surfaces and
  manuscript section. Physical TRACE-005 and BGS remain open.

## 2026-10-06 — quantitative collective diffusion continuation

- FM-019: exact N^2 total-Weyl blocks and a universal two-copy diffusion
  gap on the whole identity/swap complement at every odd N>=3.
- All parity cases closed by shifted-grid annuli, geometric Hardy
  summation, cross twists and exact kernel compression; no external
  gap theorem or computed spectrum is imported.
- Exact pair-dephasing angle and explicit original m=1 rate; the stronger
  vanishing-noise Heisenberg estimate for that law stays open.
- Explicit refined shared-noise law at m=N^3 gives mass c_0u/4 for
  u=N^-alpha, 0<alpha<1. One-copy channel is exactly unchanged;
  higher-copy law is explicitly changed. Fixed-observable classical
  retention is mean-square HS, not microscopic spectral continuity.
- Two internal analytic passes by one fresh reviewer; bounded exact
  arithmetic and separate deterministic-start float64 diagnostics.
  Nonlinear functional, original signed comparison and BGS remain OPEN.

## 2026-10-06 — actual Weyl transfer and common-noise invariant classification

- FM-018: whole-growing-band twisted average, complete adjoint-arc
  frequency coercivity and explicit all-noise regularized singular gap
  for the unchanged actual fixed-coupling map; constants noneffective.
- Exact two-pair Gaussian realization and a microscopic massive quadratic
  block; finite nonlinear and fourth-moment discriminators retain the
  distinction between channel data and spectral statistics.
- Exact ordered common-noise higher-copy channel; identity/swap is the
  entire peripheral space in two copies at every finite odd dimension,
  including composite N. Uniform reduced shrinking-noise gap is open.
- Three analytic passes by one fresh reviewer, bounded exact arithmetic
  and six supplementary symbolic identities with preserved diagnostics.
  Full nonlinear control, original signed cancellation and BGS remain OPEN.

## 2026-10-04 — actual-start comparison and circular relaxation

- FLOW-012: original-chain comparison retaining the bounded-trace starting
  matrix and its exact centered Dyson reference; initial transient controlled.
- FLOW-013: schedule-dependent empty noisy limits with global uniformity,
  bounded fixed traces, simple spectra and all positive power traces nonzero.
- FM-017: initial Poisson regularity from FM-007's existing logarithmic
  trace window, two controlled heat-phase stationary points and exponential
  unweighted vertical-tail suppression at a slower vanishing time.
- FLOW-014: gap-independent resummed contour bounds, complete crossing
  residues and windings, confluence and full Fredholm convergence.
  Actual-start original-chain Sine_2 at t=8g, epsilon=N^-9/sqrt(t),
  floor(2t^3N^36) steps, with smooth Laplace error O_f(sqrt(g)).
- Independent internal checks and two bounded finite-control packets.
  Deterministic noise removal, faster actual-start relaxation and BGS OPEN;
  priority is unestablished.

## 2026-10-04 — polynomial original-coboundary joint limit

- FLOW-011: dimension-uniform coefficient and semigroup derivatives;
  positive microscopic Laplace test norm $C_fN^6$.
- Exactly $2N^{34}$ original random steps retain the $O_f(N^{-1/3})$
  clock-to-Sine rate. Independent internal checking covers the new estimates.
- ERR-026: a slower polynomial regime already follows from FLOW-010's
  previous bound; current scope surfaces corrected, dated evidence retained.
- Forty finite matrix controls, exact derivative partitions and Wolfram
  exponent checks; deterministic BGS and noise removal remain OPEN.

## 2026-10-04 — completion of the fixed-time input

- Explicit leading-Gaussian bound for FM-013: eventual first-two traces
  below 4 and 9, hence numerical K=20 without the historical Faure route.
- Higher-packet localization retained in the quantitative trace integral;
  the dimension threshold and Heisenberg estimates remain unavailable.
- Wolfram replay executes successfully after exact polynomial identity
  reduction; source typo and historical/current scope wording repaired.

## 2026-10-04 — fixed-time packet trace closure and auxiliary-expansion boundary

- FM-013: direct odd-N proof of O_j(1) fixed traces; sharper Faure amplitudes
  remain conditional. Earlier normalized trace vanishing is credited.
- FM-016: fixed-classical-map overlap and affine-quantizer separation.
- TRACE-013: primitive irreversible arithmetic word obstruction, exact tensor
  hierarchy, enlarged two-copy gap and factorial flat spectral exclusions.
- Reproducible finite character, orbit, channel and coherent-frame controls;
  frozen Heisenberg sector and full BGS remain OPEN.

This changelog records changes in scientific state. Ordinary formatting and
implementation-only commits need not appear here.

## 2026-10-01 — folded-square refinement of resonant cubic control

- `BGS-TRACE-012`: sharper signed sector estimate, explicit root
  allocation, strict realizable separation from the global fourth
  moment and exact factorial crowding thresholds;
- finite Fourier, convex-count, Gram and noncommuting controls, with
  recorded independent Wolfram symbolic values;
- actual-map coherence remains finite-dimensional; E/G asymptotics,
  nonresonant cancellation and BGS remain OPEN.

## 2026-09-23 — scoped classical and frozen-kick results

- `BGS-RES-005`: all-lag translated classical Riesz gap for the fixed physical
  symbol under linear cat-map transport, with an explicit weighted-Wiener
  neighborhood; the nonlinear analytic frontier remains open;
- `BGS-FM-005`: the actual frozen generator decomposes into `gcd(N,7)`
  irreducible Jacobi chains, yielding a qualitative exact kick-rank bound
  through a pinned classical transcendence theorem; its approximate-rank
  statement applies only before eigenphase wrapping;
- independent internal derivation review covers the classical estimate; the
  kick-rank review is a self-review. Neither result supplies fixed-strength
  Heisenberg joint-trace estimates or proves BGS.

## 2026-09-22 — finite-orbit and spectral-inference boundaries

- `BGS-RES-004`: finite signed-orbit smooth resonance-lag rigidity, with the
  arbitrary analytic infinite-orbit problem left open;
- `BGS-TRACE-006`: clustered Abel lower bound and an abstract counterexample
  to inferring a positive-time Heisenberg-window form factor from clustering;
  no assertion that this spectrum is the frozen quantum map.

## 2026-09-22 — repository institutionalization

- canonical project identity normalized to BGS;
- scientific README and source-of-truth hierarchy established;
- machine-readable claim and theorem-dependency registries introduced;
- stable claim-ID namespace introduced;
- contribution, referee, release, errata, and publication-candidate protocols
  introduced;
- no mathematical claim promoted by this infrastructure work.

## 2026-09-21 — fixed-map continuation

- fixed-model symmetry theorem promoted in its stated small-coupling scope;
- full-symbol odd-Pell crossover and necessary escape condition promoted;
- exact low-moment/transfer controls and repeated-clock falsifier promoted;
- three-orientation mixed-resolvent barrier promoted conditionally;
- Fourier-line resonance coercivity and local-jet obstruction promoted;
- fixed-strength microscopic BGS remained OPEN.

## Corrections

The permanent correction/retraction record is `record/retractions.md`.
`ERRATA.md` is the reader-facing index; it never replaces the full record.

