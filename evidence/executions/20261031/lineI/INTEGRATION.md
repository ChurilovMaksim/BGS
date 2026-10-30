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
| 215 | proved (computer-assisted) | Thm I6 v2: d = 7 square term ≤ 0.01 for m ≡ 3 (mod 6), m ≥ 321 (k1, η = 2) |
| 216 | proved | exact monomial intertwiners between the eight (m mod 24, a = ±2) cases, and the β → −β reflection |
| 217 | proved (computer-assisted) | Thm I9: three simple top twisted eigenvalues, certified 1.262 < \|μ\| < 1.45, so r_tw > √λ/μ₀ |
| 218 | proved | aliasing (Möbius) identity for F_m |
| 219 | proved (modulo BHV / Carmichael; Lean deduction) | h_m has a new odd prime factor for every m ≥ 16, so every finite prime set fails |
| 220 | open | Conjecture R′_A (amended mean law) |

BGS-TRACE-206 stays **open**. Its boundary and ledger_status are appended with the Line I reduction, the failure of the
operator-radius route, and the heuristic, unproved risk to the frozen definition. Its title, state, dependencies and closure
condition are unchanged. BGS-TRACE-204 is unchanged; a review of its state in light of I2′ (BGS-TRACE-212) is recommended but was
not done here. The following were withdrawn and are not registered: "diagonal invisible" (B6), "primitive prime p ~ h^c" (DF7),
and "the resonance terms are exactly the large-e Möbius terms" (DF6).

## Delta fixes DF1–DF7 (referee DELTA section)
* **DF1**: "Equivalent alternative" → "alternative sufficient hypothesis" (AUTHOR_REPORT_v2.md §1, Theorem I4; note §4).
* **DF2**: `cert_v3/bounds_sq_v3.py` (the referee's target) and `sym_v3/monomial_intertw.py` (the brief's "intertwiner script")
  now use paths relative to the script. Rerun results:
  * the bounds log is byte-identical to v2, and the JSON differs only in `version`/`code_sha256`;
  * the intertwiner JSON differs only in `code_sha256`.
* **DF3**: μ₀ is now taken from Line F's certified enclosure |μ*| ∈ [1.9154712, 1.9154753] (BGS-TRACE-198, certificate
  `computations/verification/lineF/`; BGS-TRACE-199 for all m). It is the same quantity as Line I's float 1.915473 (the growth rate of
  |Z_m(ν_ρ)|), but not literally the same operator.
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
2. Bilu–Hanrot–Voutier / Carmichael and Rosser–Schoenfeld are cited in prose and not registered as external dependencies
   (`external_dependencies` = []).
3. DF2 was applied to both scripts (see above).
4. Threshold 1.260376 (arb) instead of 1.260378; registered upper end 1.9154753.
5. `record/mathematics_topics.json` was edited (needed by the render check; Line H did the same).
6. Whether BGS-TRACE-204's state should change is left for review.

## Checks (all with `nice -n 10`)
| file | content |
|---|---|
| `lake_cache_get.log` | `lake exe cache get`: exit 0 |
| `lake_build_Bgs.log` | `lake build Bgs` on the final sources: "Build completed successfully (8815 jobs)", exit 0. A first full build at 02:27–02:35 also passed; it was rerun after the two extra `#print axioms` lines, replaying the cached modules |
| `lean_axioms_LineI.log` | 17 declarations; no sorryAx, no ofReduceBool |
| `axioms_coverage.log` | 1314/1314 |
| `checkers.log` | All pass: the six render `--check`, scientific_registry_audit (304 claims), repository_audit, wave3_integration_audit, audit_manuscript_references, sync_finite_orbit/fixed_map. wave2_integration_audit, sync_return_sections, check_spectral_edition, the bibliographic self-test and the unit tests fail identically on pristine main |
| `integration_reruns/` | identity and composite-d checks byte-identical; sym_v3 and cert_v3 sha-identical |
