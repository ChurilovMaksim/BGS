# Line I integration record (31 October 2026)

Branch `line-I-rprime`, created from `origin/main` at 4f5056b8 (the merge of PR #59). `git fetch` at 02:41 +0500 showed no later commits
on main. IDs: the highest registered claim on main was BGS-TRACE-210, so Line I takes BGS-TRACE-211..220. The layout follows the
Line H integration (PR #59): the packet is in `computations/verification/lineI/`, the note in `mathematics/fixed-map/`, and the
receipt and logs are here.

## Claims
| id | state | statement |
|---|---|---|
| 211 | proved | Prop I1: relative phase split Z_m(ν0+δ) = Z_m(ν0)·σ̂(δ) |
| 212 | proved (Lean core) | Prop I2/I2′: dilation-coset L² law (prime d ∥ h) and the per-member Gauss-sum formula (every odd d ∣ h) |
| 213 | proved | Thm I4: exact reduction W′ = non-resonant sum + φ⁻¹ΣDev, so R′ ⇐ (E″)+(T″)+(D) |
| 214 | proved | Lemma I5′: Fourier/Ramanujan expansion of weighted horocycle sums |
| 215 | proved (computer-assisted; EXT-RS-1962) | Thm I6 v2: d = 7 square term ≤ 0.01 for m ≡ 3 (mod 6), m ≥ 321 (k1, η = 2); ρ = (±2,8) only, the (±2,16) level-7 members are not controlled |
| 216 | proved | exact monomial intertwiners between the eight (m mod 24, a = ±2) cases, and the β → −β reflection |
| 217 | proved (computer-assisted) | Thm I9: three simple top twisted eigenvalues, certified 1.262 < \|μ\| < 1.45, so r_tw > √λ/μ₀ |
| 218 | proved | aliasing (Möbius) identity for F_m |
| 219 | proved (modulo BHV, EXT-BHV-2001; Carmichael EXT-CARMICHAEL-1913 corroborating; Lean deduction) | h_m has a new odd prime factor for every m ≥ 16, so every finite prime set fails |
| 220 | open | Conjecture R′_A (amended mean law) |

BGS-TRACE-206 stays **open**. Its boundary and ledger_status are appended with the Line I reduction, the failure of the
operator-radius route, and the heuristic, unproved risk to the frozen definition. Its title, state, dependencies and closure
condition are unchanged. BGS-TRACE-204 was unchanged at first integration. After the owner audit it was promoted to proved; see below. The following were withdrawn and are not registered: "diagonal invisible" (B6), "primitive prime p ~ h^c" (DF7),
and "the resonance terms are exactly the large-e Möbius terms" (DF6).

## Delta fixes DF1–DF7 (referee DELTA section)
* **DF1**: "Equivalent alternative" → "alternative sufficient hypothesis" (AUTHOR_REPORT_v2.md §1, Theorem I4; note §4).
* **DF2**: `cert_v3/bounds_sq_v3.py` (the referee's target) and `sym_v3/monomial_intertw.py` (the brief's "intertwiner script")
  now use paths relative to the script. Rerun results:
  * the bounds log is byte-identical to v2, and the JSON differs only in `version`/`code_sha256`;
  * the intertwiner JSON differs only in `code_sha256`.
* **DF3**: μ₀ is now taken from Line F's certified enclosure |μ*| ∈ [1.9154712, 1.9154753] (BGS-TRACE-198, certificate
  `computations/verification/lineF/`; BGS-TRACE-199 for all m). (Reworded by owner-audit fix R5: μ₀ := liminf |Z_m(ν*)|^(1/m), and
  the bound rests directly on BGS-TRACE-199's |Z_m(ν*)| ≥ ½(1−λ^(−m))(1.9154712^m − 3012.30), odd m ≥ 13.)
  * ρ = (−2, 8) is N ≡ −4 directly.
  * ρ = (2, 8) follows by conjugation: conj ĝ = (−1)ⁿĝ, and the sector coefficients shift c_a → c_{a−4}.
  * Arb gives √λ/1.9154712 = 1.2603758…, so √λ/μ₀ ≤ 1.260376. This is slightly sharper than the 1.260378 in the brief.
  * The registered upper end is 1.9154753, not 1.9154752; only the lower end is used.
* **DF4**: `dom_v3/rig_dom3b.py` (v3) takes gmax over the exact upper ends. It was rerun with nice -n 10 on unchanged inputs
  (sha256 equal to the v2 provenance). Both classes are certified at R = 1.22, 1.24, 1.25 and 1.262, with count 3.
  * Class 1:3: F(1.262) = 0.6842758739, unchanged.
  * Class 2:1: F(1.262) = 0.6489779088 (v2: 0.6488989); this equals the referee's rerun.
  * Logs and sha256 are in `dom_v3/logs/`.
* **DF5**: Theorem I9 states the certified range 1.262 < |μ| < 1.45; 1.28371 is a float diagnostic.
* **DF6**: the "exactly the large-e Möbius terms" sentence is downgraded to heuristic and moved out of the proved heading
  (`theory_session4.md` §4.1, AUTHOR_REPORT_session4.md §4.3, note §9.1).
* **DF7**: "p ~ h^c" is dropped. The prime-support statement is restated: h_m = V_m/2, U_2m = U_m V_m, and BHV Theorem 1.4 /
  Carmichael 1913 give for m ≥ 16 a primitive prime of U_2m, which is odd, divides h_m and divides no earlier h_m′. The S-arithmetic
  obstruction stays an [assessment].

The pre-fix documents are in `computations/verification/lineI/pre_delta/` (sha256 in `pre_delta/SHA256_pre_delta.txt`, mirrored in
`receipt.json`).

## Packet bytes
All 332 packet files other than `README.md` and `PROVENANCE_PATHS.md` are byte-identical to the scratch sources:
* the author tree `/workspace/bgs-lineI`, including the DF-edited documents and the v3 reruns;
* the referee tree `/workspace/audit/lineI`;
* the integration checks.

The author `REPORT*.md` and `NOTES.md` were renamed `AUTHOR_*`. The Galerkin `.npy` matrices (0.1–1 GB each) and `__pycache__` are
excluded and can be regenerated with the run scripts. Absolute scratch paths in hashed files are whitelisted, not edited:
[`PROVENANCE_PATHS.md`](../../../../computations/verification/lineI/PROVENANCE_PATHS.md).

## Lean
* `formalization/Bgs/LineI.lean` is `lean/LineI_v2.lean` with three changes: the namespace is `Bgs.LineI`, there is an integration
  note in the docstring, and `#print axioms` lines are added for all 6 declarations. `LineI.lean` (v1) differs from v2 only in its
  docstring and is not duplicated.
* `formalization/Bgs/LineIArith.lean` is new at integration (it imports `Bgs.LineG`). It contains:
  * the Pell identity;
  * ε = +1 for odd m;
  * 7 ∣ h_m ↔ m ≡ 3 (mod 6);
  * U_2m = 2h_mU_m;
  * the primitive-divisor deduction, with BHV as an explicit hypothesis.
* Both modules are imported in `formalization/Bgs.lean`. Neither uses `sorry` or `native_decide`. The axioms are subsets of
  propext, Classical.choice and Quot.sound.

## Registry
* `record/claims.json`: the only hand-edited registry file for claims. It has 10 new rows, the 206 boundary/ledger append and
  `updated` = 2026-10-31.
* `record/claim_verification_inventory.json`: 10 new rows, and the 206 row is mirrored. `source_blob_sha` = git blob sha1 of
  claims.json. Open 220 has methods ["unevidenced"].
* `record/claim_integration_epochs.json`: 10 after_wave3 rows.
* `record/mathematics_topics.json`: the new note is added under fixed-map. `render_research_views.py` requires every maintained
  note to be listed.
* Generated views are regenerated with `computations/maintenance/render_*.py`: claim_registry.md, STATUS.md, results.md table,
  scientific_dependencies.json, scientific_dependency_graph.md and corpus_atlas.md.
* Prose edited by hand: CHANGELOG, README(.ru), RESEARCH, claim_ledger, results, open_questions, the topic README, the "Later work"
  note in Line G, and formalization/README.

## Deviations from the brief / Line H layout
1. No manuscript section: `manuscript` = [] for 211–220. Line H added `lineH_49state_certificate.tex`; this was not requested here.
2. (Superseded by owner-audit fix R1.) At first integration, Bilu–Hanrot–Voutier / Carmichael and Rosser–Schoenfeld were cited
   in prose only. They are now registered as EXT-BHV-2001 and EXT-CARMICHAEL-1913 (on 219) and EXT-RS-1962 (on 215).
3. DF2 was applied to both scripts (see above).
4. Threshold 1.260376 (arb) instead of 1.260378; registered upper end 1.9154753.
5. `record/mathematics_topics.json` was edited (needed by the render check; Line H did the same).
6. (Resolved by owner decision, fix R6.) BGS-TRACE-204 is now proved.

## Checks (all with `nice -n 10`)
| file | content |
|---|---|
| `lake_cache_get.log` | `lake exe cache get`: exit 0 |
| `lake_build_Bgs.log` | `lake build Bgs` on the final sources: "Build completed successfully (8815 jobs)", exit 0. A first full build at 02:27–02:35 also passed; it was rerun after the two extra `#print axioms` lines, replaying the cached modules |
| `lean_axioms_LineI.log` | 17 declarations; no sorryAx, no ofReduceBool |
| `axioms_coverage.log` | 1314/1314 |
| `checkers.log` | All pass: the six render `--check`, scientific_registry_audit (304 claims), repository_audit, wave3_integration_audit, audit_manuscript_references, sync_finite_orbit/fixed_map. wave2_integration_audit, sync_return_sections, check_spectral_edition, the bibliographic self-test and the unit tests fail identically on pristine main |
| `integration_reruns/` | identity and composite-d checks byte-identical; sym_v3 and cert_v3 sha-identical |

## Owner audit of PR #60 (verdict MERGE AFTER FIXES), applied 31 October 2026
* **R1, external theorems.** `literature/external_dependencies.json` now registers the following:

  | ID | Theorem | Status |
  |---|---|---|
  | EXT-RS-1962 | Rosser–Schoenfeld, Theorem 15, pp. 71–72, (3.41)–(3.42) | primary scan read |
  | EXT-BHV-2001 | Bilu–Hanrot–Voutier, Theorem 1.4 | primary PDF **not** obtained (bot wall/paywall); number and statement corroborated by the abstract and a secondary citation; page not pinned |
  | EXT-CARMICHAEL-1913 | Carmichael 1913 | corroborating; locator XXIII vs 21 unverified |

  They are listed on 215 (RS) and 219 (BHV, Carmichael). Both claims stay proved. The review record is
  `literature/lineI_sources_20261031.md`.

  The bibliographic cache gained the 3 records in a new snapshot, `registry_metadata_20261031_lineI.json`, with review
  `record/audits/metadata_cache_refresh_20261031_lineI/report.md`. The self-test now fails only on the pre-existing EXT-BR-1975 line,
  exactly as on main. The v4 negative-control path was updated to point at the new cache.
* **R2, 215 scope.** "ρ = (±2,8) only; the (±2,16) level-7 members are not controlled" is carried in these places:
  * the 206 boundary and ledger_status, the 213 boundary, and the 215 boundary and ledger;
  * note §4;
  * README, README.ru, RESEARCH, CHANGELOG, the topic README and results.md;
  * the Line G "Later work" paragraph, the 215 epochs disposition, open_questions.md and the packet README.
* **R3.** 1.0187 → 1.0185 (1.915473·1.28371/2.414214 = 1.01851). Changed in the 206 and 217 boundaries, note §8 and open_questions.md.
* **R4.**
  * 216: `formalization` = []. The ledger now says the Lean module holds only the auxiliary lemma `seven_dvd_nsw_iff`, not the
    intertwiners, and the inventory drops `lean_formalization`.
  * 212 epochs disposition: "Gauss-sum algebra" → "coset L² algebra (c)–(d)".
* **R5.** 217: μ₀ := liminf |Z_m(ν*)|^(1/m). The bound rests directly on TRACE-199,
  |Z_m(ν*)| ≥ ½(1−λ^(−m))(1.9154712^m − 3012.30) for odd m ≥ 13. The phrase "same quantity, not the same operator" is dropped.
* **R6, BGS-TRACE-204 → proved** (dependencies [203, 212]).
  * Derivation, note §3: tNmγ + Trβγ = tNm(γ + t̄β̄) − t̄Nmβ, so G_t(β) = e(t̄Nmβ/d)·G_d(t). Substituting into I2′ gives exactly 204's
    G3 formula, with Line G's conventions (`check_dilution.py`).
  * Numerical check: `integration_checks/lineI_G3_form_check.py` covers 19 (m, d) pairs, including composite d = 217, 287, 961, 1271
    (m = 15) and 49, 1673 (m = 21), plus d = 287 and d = 49 as requested. Max errors: completing-the-square 8.4e−15, G3 formula
    8.3e−15. A negative control (−t̄β sign) fails with error 2.0. The log ends `ALL_OK` in ~47 s.
  * The main-term approximation stays unbounded and is not claimed.
  * Also updated: the Line G note G3 section, the manuscript remark and the claim index.
* **Nits.**
  * 215: 0.004574 is the exact-constant value; the rounded constants give 0.004575.
  * 220: dependency 213 added.
  * v1/v2 verifiers are marked superseded by v3 in the claim ledgers and the packet README: bounds_sq → cert_v3, sym → sym_v3,
    dom v2 → dom_v3, and LineI.lean v1 → v2.
* The inventory mirrors 204, 206, 212, 213, 215, 216, 217, 219 and 220, and `source_blob_sha` has been recomputed.
* **Maintenance data lists.** Three files changed so that the new EXT ids are admitted. No check was removed or relaxed.
  * `computations/verification/wave2_integration_audit.py`: the hard-coded set of admitted-later EXT ids gains
    EXT-RS-1962, EXT-BHV-2001 and EXT-CARMICHAEL-1913. The epoch store records the same ids in
    `external_dependency_extension.added_ids`, and its source_reviews gains the Line I review. This follows the precedent of
    commit 39efa322, which admitted EXT-BT-1971 and others.
  * `test_external_epoch_preservation.py`: the expected count changes from (39,18) to (39,21).
  * `v4_negative_controls.py`: tampers the new digest-pinned cache instead of the superseded one.
* **Checks after the audit fixes.** All runs used `nice -n 10`.
  * `lake exe cache get`: exit 0. `lake build Bgs`: "Build completed successfully (8815 jobs)". The Lean sources are unchanged.
  * `checkers.log` agrees line for line with the pristine-main baseline, except for these lines:
    * the claim/EXT counts (304 / 60);
    * a wave2 traceback line number, shifted by one because of the added id line.
  * The unit tests give 116 failures and 104 errors. These are the pre-existing failures plus `test_fractional_routing`, which times
    out because `check_routing.py` rglobs the 7.9 GB gitignored `.lake`. The auditor reports the same environment artefact.

