> **Repository copy.** Absolute scratch-directory paths of the audit machine are replaced by placeholders in angle brackets (`<referee-dir>` = the first referee's working tree, copied to `computations/verification/lineE/referee/`; `<referee2-dir>` = this audit's working tree, copied to `computations/verification/lineE/referee2/`; `<author-packet>` = the author packet; `<audit-clone>` = a fresh clone of the repository). They are not part of the repository. The text is otherwise unchanged.

# Referee + pre-merge audit of PR #57 (ChurilovMaksim/BGS, branch `lineE-resonant-transfer`)

- **Head audited:** `e3b83dcb5c6e7f8238cb26c6207af27548931928`. **Base:** `main` `347f1730`. The merge-base equals main.
- **Fresh clone:** `<audit-clone>`.
- **Auditor material:** `<referee2-dir>/{code,logs,lean,NOTES.md}`, backed up to `<backup-dir>/`.
- **Nothing was pushed, commented or merged.** The m = 17 certificate (pids 716309/716609) was not touched.
- **Gate applied** (user's wording): nothing enters the repo unless it has been numerically checked, formalized (preferably in Lean), and checked for hidden logical or factual errors and exaggerations.

## 0. Verdict: **MERGE AFTER FIXES**

No mathematical error was found in E11–E14.

I re-derived on paper:
- E11;
- E12, including the mod-8 and mod-a² bookkeeping, the 7-adic coupling γ and the condition 3 ∤ m;
- Prop. G, including the Gauss completion, the shift, the character term and the sign of the phase.

I also confirmed all four claims independently in code. The m = 11 **and** m = 13 bounds for the Line B kick f_B are reproduced by my own directed-rounding interval-arithmetic kernel, which shares no code with `zres`. The new Lean module builds. It has no `sorry`, no `native_decide` and no extra axioms, and its statements match the prose.

The blocking problems are of a different kind:
- **Several certified bounds are quoted rounded to nearest instead of in the safe direction.** One quoted inequality is literally false: "|Z|² ≥ 290544.5725" at m = 11. Its true value is 290544.57248. This affects E13 (new) and also the refereed E3/E5 tables, which the previous referee missed.
- There are a few logical and wording inaccuracies:
  - γ is m-independent, but the PR only *observes* this; it is used implicitly;
  - the E14 hypothesis/conclusion does not distinguish the two signs s;
  - "two residues alone";
  - README qualifiers.
- There are hygiene items: absolute scratch-directory paths and dangling references.

All the fixes are textual. None changes a status.

## 1. Per-claim verdicts and recommended statuses

| ID | # | verdict | status in PR | recommended status |
|---|---|---|---|---|
| 183–192 | E1–E10 | Refereed earlier. F1–F13 and the nits are applied faithfully (§5). **Exception:** the E3/E5 rounding (R1). | as registered | unchanged, after R1 |
| 193 | E11 | **Accept.** The paper proof is correct. Rigorous check at m = 7 with my interval kernel: Z_{f7} at N ≡ ∓196 equals Z_{k1} at N ≡ ∓4 to 1e-12. The m = 9 control fails as it should (196 is not invertible mod h_9). Lean `nsw_mod7` is correct. | verification-pending | proved (computer-assisted via 187), once the referee acceptance is recorded |
| 194 | E12 | **Accept, with fix R3.** Paper proof re-derived. Phase identity checked exactly using the theorem's *own* κ, γ formulas: 178/178 cases (a ∈ {1, 7, 17, 23, 31}, odd m ≤ 25, s = ±1, both roots). Trace law checked against my own 49-state Galerkin: 5e-15 to 7e-14. The γ+1 control fails at O(1). | verification-pending | proved (after R3) |
| 195 | E13 | **Accept, with fixes R1 and R2.** Prop. G re-derived, and checked against a brute n-sum for a non-even, complex-Fourier kick: 4e-8 at m = 3; 6e-6 at m = 5, L = 12, converging in L. The sign-flip control breaks it (rel. error 4.8 and 25). The zres rounding analysis was audited line by line and is sound. Bounds independently reproduced (§3). | verification-pending | proved (computer-assisted), m = 11, 13 only (after R1, R2) |
| 196 | E14 | **Accept as conditional, with fix R4.** The implication is correct for each s separately. As written, the hypothesis and conclusion mix the two signs. | conditional | conditional |
| 179 / 180 / 182 | — | Annotations are accurate. They stay open. There is no BGS-counterexample claim and no claim that R is disproved. Keating–Mezzadri is cited as an analogy only. | open | open (see nit N8 on the 182 wording) |

## 2. Paper re-derivations (summary)

**E11.**
- ĝ_{f7}(7n′) = ĝ_{k1}(n′) and ĝ_{f7} vanishes off 7Z. α_{7n′} = 7α_{n′}, so Nm(α_{7n′}) = 49·Nm(α_{n′}). Hence Z_{f7}(ν) = Z_{k1}(49ν).
- 7 | h_m ⟺ 3 | m. Lean: h_{2j+1} mod 7 cycles 1, 0, 6.
- So for 3 ∤ m, 49 is a unit mod 2h, and F and W̃rest coincide (B^sym is kick-independent and χ ≡ 1 for even kicks).
- The listed m-sets equal the E5 ranges minus the multiples of 3.

**E12.**
- *Real part.* With ν = (kh − s)/(4a²) and q = P/(4h): −2νq = s·q/(2a²) − kP/(8a²).
- *Mod-8 part.* 1/(8a²) = u/8 + v/a², and P ≡ y′(Σn)² (mod 8) by the E1 parity facts. This gives κ = −kuy′, which is odd.
- *Mod-a² part.*
  - ψ(d) = βλ^d + β̄λ^{−d}, with β = (2y′ − √2h)/4 and β̄ = (2y′ + √2h)/4.
  - ββ̄ = 1/8, and β̄/β = 8β̄² = 2h² + 1 + 2√2hy′ = λ^m. Hence ψ(d) = β̄(λ^{−d} + λ^{−(m−d)}).
  - The periodic-orbit identity (1 − ℓ^{−m})Σn_jσ_j = ℓ^{−m}Σn_j² + Σ_{i<j}(ℓ^{−d} + ℓ^{−(m−d)})n_in_j holds: the d and m−d pairing was re-derived.
  - Hence P ≡ 2B(1 − ℓ^{−m})[Σnσ + 2̄Σn²] (mod a²).
- *Condition (ii).* For a = 7, ℓ ≡ 2 or 4 (mod 7) has order 3, so (ii) ⟺ 3 ∤ m, and gcd(7, h) = 1 ⟺ 3 ∤ m.
- *Finite N.* sq/(2a²) + 2q/N = (sq/(2a²))(1 + s·4a²/N). Correct.
- **New, auditor:** γ = −s·ι(c) holds **for every m**, not only for m ≤ 41 as the PR says:
  - mod a², k ≡ s·h⁻¹ and v ≡ 8⁻¹;
  - B(1 − ℓ^{−m}) = ι(β̄ − β) = ι(√2h/2) = rh/2;
  - so γ = −s·h⁻¹·8⁻¹·2·rh/2 = −s·r/8 = −s·ι(1/(4√2)).
  - Hence the 49-state operators are m-independent (only c_b depends on m, through κ). E14 and the TeX statement of 194 need exactly this. See R3.

**Prop. G.**
- k_ν(ξ) = D⁻¹Σ_β e(−ν𝒬(β) − ⟨β,ξ⟩). With 𝒬(β+γ) = 𝒬(β) + 𝒬(γ) + 4βᵀH⁻¹γ and 𝒬 ≡ 2q (mod 1):
  k_ν(½𝟙 − 4νH⁻¹γ) = k_ν(½𝟙)·e(2νq(γ) − ⟨γ, ½𝟙⟩).
- Take γ = −t′Hw, w = z/h, t′ = (4ν)⁻¹ mod h. Then −4νH⁻¹γ ≡ w (mod Z^m).
- *Character term.* 𝟙ᵀH = 4𝟙ᵀ and h is odd, so h | Σz_j and ⟨γ, ½𝟙⟩ = −2t′Σz_j/h ∈ Z.
- *Phase.* 2νq(γ) = νt′²R(z)/h, with νt′² ≡ (16ν)⁻¹ (mod h). R mod h is independent of the lift of z, because Hz ≡ 0 (mod h).
- |k(½𝟙)| = 1/h (D_eff = h²). The sign is e(+tR/h), confirmed by the control in §1.

**E14.** For each s separately: H∞,7 for the s-family gives |Z(ν_{7,s})| ≍ |μ_s|^m, using |c_b| = ½, multiplicity 1 and 1 − λ^{−m} → 1. Then F ≥ |Z|²/φ(2h) ≥ 2|μ_s|^{2m}λ^{−m/2}. One s with |μ_s| > λ^{1/4} suffices to give W̃rest/m → ∞ along 3 ∤ m, which refutes R; R is a max over a compact η-range along all odd m. See R4 for the wording.

## 3. Independent computations (auditor code; no author code reused except the kick definition, asserted against `model.py`)

| check | auditor file | result |
|---|---|---|
| E12 phase identity, exact rationals, theorem's κ/γ formulas | `code/e12_phase.py` → `logs/e12_phase.log` | 178/178 OK; 20 correctly skipped (gcd or (ii)) |
| E12 trace law, own Galerkin on H²(D_ρ)⊗C^{49} vs brute n-sum | `code/e12_trace.py` → `logs/e12_trace.log` | 5e-15 to 7e-14 (m = 5, 7; a = 1, 7; s = ±1; both roots); γ+1 control off by 0.8 to 8.7 relative |
| Prop. G vs brute n-sum, non-even kick, all units | `code/propG_nsum.py` → `logs/propG_nsum*.log` | 4e-8 (m = 3); 2.8e-4 → 6e-6 (m = 5, L = 9 → 12); sign-flip control fails |
| **Rigorous f_B bounds**, FE_UPWARD interval kernel (outward-rounded arb tables at 160 bits, runtime rounding-mode self-test) | `code/ivsum.c`, `code/ivcert.py` → `logs/ivcert_m11*.out`, `logs/ivcert_m13.out` | see the table below |
| E11 rigorous at m = 7 | `ivcert.py f7/k1` | f7@∓196 = k1@∓4: [2220.05341290629, 2220.05341290657] vs [2220.05341290629, 2220.05341290657] |
| Author pipeline rerun | `<scratch-dir>` copy | `cert49_py`, `check_phase` logs byte-identical. `zres` rebuilt with the README flags: 0 FMA instructions, and m = 11 `cert_class` output bit-identical. `check_trace` reproduced its first lines (then timed out under load). `bounds.py` on `cert_L6` and `cert_L8b` reproduces the committed `_bounds.json`. |

**Rigorous f_B results at η = 2 (my interval kernel vs the PR):**

| m | quantity | auditor (interval) | PR (zres + a-priori bound) |
|---|---|---|---|
| 11 | \|Z\|² at N ≡ −196 | [290544.5724756, 290544.5724762] | ≥ 290544.5724647 |
| 11 | \|Z\|² at N ≡ +196 | [309515.7860440, 309515.7860447] | ≥ 309515.7860328 |
| 11 | F/2m ≥ (4 residues) | 3.52270646930 | 3.5227064692 |
| 11 | W̃rest/m ≥ | 3.04541293860 | 3.0454129383 |
| 13 | \|Z\|² at N ≡ −196 | [3628100.501866, 3628100.501904] | ≥ 3628100.500544 |
| 13 | \|Z\|² at N ≡ +196 | [4203360.860882, 4203360.860925] | ≥ 4203360.859460 |
| 13 | F/2m ≥ (4 residues) | 6.4579491729 | 6.4579491707 |
| 13 | W̃rest/m ≥ | 8.9158983459 | 8.9158983413 |
| 11 / 13 | from ±196 **alone** | F/2m ≥ 3.52214 / 6.45764; W̃/m ≥ 3.04428 / 8.91528 | (not stated) |

The S-enclosure widths are 5e-6 (m = 11) and 5e-4 (m = 13). The PR's a-priori bounds are 8.4e-5 and 1.7e-2: valid, and conservative.

**zres error analysis, audited line by line. Sound.**
- *Products.* The recursion e_{k+1} = e_k(1+ε)(1+√5u) + ε + √5u(1+ε) is correct, using the Brent–Percival–Zimmermann √5u bound for the naive complex product without FMA. The E factor is counted: there are m multiplications.
- *Row sums.* √2·γ_n·n·(1+e_m) per row, componentwise. Correct.
- *Long-double totals.* γ_{n+T+2}(2⁻⁶⁴)·n²(1+e_m)(1+γ_n). Correct for x86-64 80-bit.
- *Output.* The %.17Le print, float() parse and hypot are covered by the 2⁻⁵⁰ pad.
- *Tables.* ε is measured against arb at 96 bits, including the ball radius.
- *Integers.* No int64 overflow (h² < 2.6e12 at m = 17). The index updates U += D, D += 2Ct are correct.
- *Attempts to break it* (wrong t sign; 3 | m; FMA build): the FMA build *does* emit 10 FMA instructions without `-ffp-contract=off`, so the guarantee depends on the documented build flags (N4).

## 4. Lean

- `lake exe cache get`: no files to download, 8690 already decompressed. Mathlib was not built.
- `lake build Bgs.LineE Bgs.LineEResonance`: OK (40 s and 22 s). `Bgs.lean` imports both.
- `#print axioms` (`logs/lean_audit.out`): every new theorem is ⊆ {propext, Classical.choice, Quot.sound}. The `cert49_*` theorems use [propext] only. This matches `evidence/.../lean_axioms_LineE.log` (28 theorems).
- grep: the only `sorry` / `native_decide` matches are in comments. No `axiom`, `implemented_by` or `extern`.
- `LineE.lean` sha256 is b3a91202…, identical to the refereed copy.
- **Statement vs prose.**
  - `cert49` checks the coefficient identities against the **true** phase coefficients −νy′/g′ and −2νy′x_d/g′, from Nm(α_n) = Σn_in_jx_{|i−j|}, cleared by 392h². It does not go through Lemma Q.
  - Diagonal and pair weights, κ/8 vs κ/4, and 25 = 2⁻¹ mod 49 are all correct.
  - Only the root √2 ↦ 10 (ℓ⁻¹ = 32) is used. γ = 11 for s = +1 and 38 for s = −1, consistent with γ = −s·ι(c).
  - `nsw_mod7 : nsw j % 7 = 0 ↔ j % 3 = 1` is exactly "7 | h_m ⟺ 3 | m" for m = 2j+1.
- **Auditor false controls** (`lean/Audit57.lean`, `lean/Neg57.lean`): wrong κ, wrong γ, wrong ν, wrong s, and m = 9 all evaluate to `false`. `theorem … = true := by decide` fails with "decide proved that the proposition … is false". The PR's 5 controls are also correct.
- **Coverage (gate).** Lean covers finite instances only: m ∈ {5, 7, 11, 13, 17, 19} for E12, plus `nsw_mod7` for all m.
  - Not formalised: E11's one-line Fourier argument, general-m E12, Prop. G, and the certificates.
  - γ = −s·ι(c) for all m (§2) would be an easy general-m Lean target. Recommended, not required.

## 5. Previous referee fixes F1–F13: applied and faithful

| fix | where it is applied |
|---|---|
| F1 | §0, the 187/188 boundaries, README, CHANGELOG |
| F2 | §7 table; violation ranges re-verified from the `_bounds.json` |
| F3 | TRACE-180 annotation |
| F4 | §3 |
| F5 | §9 |
| F6 | §7 |
| F7 | review scripts import `lineB/common/model.py` by relative path; versions pinned; Lean under `formalization/Bgs`; no `claims.json` copy |
| F8 | `predict_finiteN.py` asserts ρ > L/(λ−1); L = 10, ρ = 2.6 |
| F9 | cache keyed by sector label; explicit Bessel tail with the ± factor 2; all 9 certificates regenerated, and `bounds.py` reproduces them |
| F10 | E2 proof detail |
| F11 | Appendix A |
| F12 | §9 |
| F13 | §4 |

**Missed by the previous referee:** the safe-direction rounding of E3/E5 quotes (R1).

## 6. Repository checks

| check | result |
|---|---|
| `scientific_registry_audit.py` | OK (280 claims) |
| `render_{bibliography,claim_registry,errata,research_views,status}.py --check` | all OK |
| `repository_audit.py` | PASS |
| `audit_manuscript_references.py --check` | OK |
| `sync_finite_orbit` / `sync_fixed_map --check` | SKIP (by design) |
| `bibliographic_metadata_audit.py --self-test` | exit 1 ("EXT-BR-1975 dependency graph changed"), **identical on pristine main** (pre-existing) |
| `sync_return_sections --check` | needs pandoc, which is not on this box. The author logged it as passing with pandoc 3.12.1. |

**Counts.** 266 + 14 = 280; proved +5, verification-pending +3, conditional +2, open +4. STATUS, README, results, atlas and CHANGELOG are consistent. The inventory `source_blob_sha` equals the git blob of `claims.json`.

**Evidence.** All 9 sha256 values in `receipt.json` match the files. No secrets were found.

**Statuses.**
- 179, 180 and 182 stay open.
- 193–195 are verification-pending and 196 is conditional, all with honest "not yet refereed" wording.
- Deps and closure conditions follow the repo convention: only open claims carry a `closure_condition`, and this is true repo-wide.

## 7. Required fixes

**R1 (factual; safe-direction rounding of certified bounds).** Every quoted certified bound must be rounded *down* for lower bounds and *outward* for enclosures. Current violations:
- **E13** (`mathematics/fixed-map/resonant_residue_lineE.md:451–452`):
  - "290544.5725" → 290544.5724. This one is **false as stated**: the true value is 290544.57248.
  - "4203360.8595" → 4203360.8594.
  - "8.9159" → 8.9158 (certified 8.915898).
  - The same 8.9159 appears in `record/claims.json:7157`, `record/claim_verification_inventory.json:10432` and `manuscript/unified_sections/resonant_residue_lineE.tex:65`; regenerate `claim_registry.md`.
- **E5** (`resonant_residue_lineE.md:238–239` and `:69`; `claims.json:6951`; `inventory:10147`): 5.99→5.98, 7.98→7.97, 20.3→20.2, 36.6→36.5, 36.0→35.9, 68.0→67.9, 84.3→84.2, 88.0→87.9, 172→171, 331→330, 1851→1850, 1355→1354, 2706→2705, 1426→1425, 2848→2847, 404→403, 804→803. The certified values are in `logs/cert_L6_bounds.json` and `cert_L8b_eta2_bounds.json`.
- **η = 1.25** (`resonant_residue_lineE.md:248`): "0.45 at most" → "< 0.448".
- **E3 enclosures** (`resonant_residue_lineE.md:211–219`; `claims.json:6900`; `inventory:10079`; `tex:34`): round outward. For example:
  - [1.9154751, 1.9154771] → [1.9154750, 1.9154771];
  - η = 1.25 upper 1.75975 → 1.75976;
  - η = 1.5 lower 1.76190 → 1.76189;
  - η = 1.75 lower 1.83180 → 1.83179;
  - upper endpoints at 2.25 / 2.5 / 2.75 → 1.96084 / 1.91758 / 1.83713;
  - η = 3.0 lower 1.62250 → 1.62249;
  - L8b upper 1.96547 → 1.96548.

**R2 (attribution).** `cert_class.py` sums all four residues (±196 and ±4) into `F_lower`, but the text attributes the bound to ±196 only.
- Either say "from the residues ±196 and ±4", or quote the ±196-only bounds: F/2m ≥ 3.5221 / 6.4576 and W̃/m ≥ 3.0442 / 8.9152 at m = 11 / 13.
- Locations: `resonant_residue_lineE.md:293, 444, 455`; `claims.json:6823` (TRACE-182 annotation, "from those two residues"); `inventory:9962`; `derandomized_fixed_kick.md:157`.

**R3 (logic).** `resonant_residue_lineE.md:388` labels γ = −s·ι(c) as "[N] … not needed". It **is** needed: TeX 194 (`resonant_residue_lineE.tex:58`, "m-independent operators") and E14 rely on m-independence of the 49-state operators. Replace the remark with the 3-line proof in §2: k ≡ sh⁻¹, v ≡ 8⁻¹ (mod a²) and B(1−ℓ^{−m}) = ι(√2h/2), so γ = −s·r/8. Also fix "(one value per root r)": for a fixed root, γ = 11 for s = +1 and 38 for s = −1.

**R4 (logic, E14).** `resonant_residue_lineE.md:465–476` (and `claims.json` 196, `tex:69`): state H∞,7 per sign s, with a dominant μ_s. Conclude |Z(ν_{7,s})| ≍ |μ_s|^m and F ≥ C·max_s(|μ_s|²λ^{−1/2})^m. As written, "|Z(ν_{7,±})| ≍ |μ∞|^m" with a single μ∞ is wrong for the sign whose leading eigenvalue is smaller (float values 1.884 vs 1.897).

**R5 (overstatement).**
- `README.md:15` and `README.ru.md:15`: "Z_m is then the trace of m-independent IFS transfer operators" → add "for finitely supported kicks". "The leading eigenvalue is certified" → "… of the L-truncated operators".
- Same fix in `mathematics/topics/fixed-map/README.md:33`.

**R6 (user gate: no absolute scratch-directory paths).**
- `computations/verification/lineE/referee/REPORT.md:3,4,310,369–373`
- `referee/NOTES.md:10`
- `referee/logs/lean_neg.out:1`
- `evidence/executions/20261030/lineE-resonant-transfer/lean_controls.log:3,8,13,18,23`

Replace these with repo-relative paths, or with a note "auditor scratch paths, not part of the repo". There is precedent on main (614 files), so this is cosmetic, but your gate asks for it.

**R7 (dangling references).**
- `evidence/.../README.md:43` cites `cert_m17_full.out`, which is not committed.
- `computations/verification/lineE/step2/cert_class.py:3` cites `step2/PROOF_G.md`, which does not exist. Point it to `resonant_residue_lineE.md` §10.3.

**Optional, same PR or a follow-up.** Record this audit, then move 193 → proved (computer-assisted via 187), 194 → proved and 195 → proved (computer-assisted, m = 11, 13), and replace the "not yet refereed" wording. This involves `claims.json` ledgers, CHANGELOG, README×2, RESEARCH, results, the evidence README and the receipt, then re-render. Include `<referee2-dir>/{code,logs,REPORT.md}` as `computations/verification/lineE/referee2/`, with paths scrubbed.

## 8. Nits

- **N1.** `resonant_residue_lineE.md:322`: "Z_{f7}(ν) = Z_{k1}(49ν) to ≤ 2e-8 absolute". The log measures the |Z|² difference (≤ 1.6e-8). Say so.
- **N2.** Prop. G "any kick" (`claims.json` 195, md §10.3): add the hypothesis Σ|ĝ(n)| < ∞, needed for the Poisson step of Theorem 3.
- **N3.** md §10.3 "Inputs": say that the F bound in `cert_class.jsonl` includes the ±4 residues (R2).
- **N4.** The `zres` guarantee depends on `-ffp-contract=off`; with `-march=native` alone GCC emits FMA. Add a build script or Makefile plus a guard, e.g. `#pragma GCC optimize("fp-contract=off")` or a runtime/objdump check. Alternatively, note that an FMA build would need its own analysis (Jeannerod et al. give a 2u bound for products, but the summation contraction changes the bound).
- **N5.** Pre-registration (§10.3): cite the pushed commit e3b83dcb (GitHub timestamp) as the external timestamp. The JSONL timestamps are self-written.
- **N6.** `check_finiteN`: the m = 7, N = 43 blow-up (1e198) is recorded honestly. "Outside its regime" would better read "float Galerkin numerically unstable at c(1+196/N) ≈ 5.6c". Also, L = 48 sits just below the n = 49 harmonic (J_7(1.8) ≈ 1e-4), which explains the 5e-5 residual. L ≥ 56 would be cleaner.
- **N7.** E13 header (md:449) "abs. error bound on S": also give the auditor's interval widths (5e-6 and 5e-4) if referee material is added.
- **N8.** TRACE-182 annotation (`claims.json:6823`, `derandomized_fixed_kick.md:157`): its closure condition concerns (m, η) = (11, 2) only, not "all m". Keeping it open is defensible, but the stated reason should be accurate: the ±196 share and the exact law are proved, while the residual F/2m ≈ 2.04 is not rigorously controlled. The 192 closure ("for all m … would also meet 182") moves 182's goalposts. Reword.
- **N9.** The pre-existing failures (bibliographic self-test; wave2 and sync with pandoc) are correctly attributed to main.
- **N10.** `referee/logs/T_*.npy` (~1.8 MB of binary evidence) are fine, but list them in the receipt with sha256.
- **N11.** STATUS/README wording is otherwise sober: no counterexample claim, KM as analogy only, and R not disproved.

## 9. Reproduce (auditor)

```
P=<python-venv>/bin/python; cd <referee2-dir>/code
gcc -O2 -fopenmp -frounding-math -fno-fast-math -ffp-contract=off -o ivsum ivsum.c -lm
$P ivcert.py full 11 2.0 196,-196,4,-4 8 ; $P ivcert.py full 13 2.0 196,-196,4,-4 8   # ~12 min under load 30
$P e12_phase.py ; $P e12_trace.py ; $P propG_nsum.py
cd ../BGS/formalization && lake exe cache get && lake build Bgs.LineE Bgs.LineEResonance && lake env lean ../../lean/Audit57.lean
```
