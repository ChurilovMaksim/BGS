# Line J integration record (31 October 2026, UTC+5)

* **Base.** `ChurilovMaksim/BGS` origin/main 195a24f9 (the merge of PR #60). Before pushing, main had moved to b96ef6bd (Line D orbit-pair Lean modules; BGS-TRACE-151 formalization list). It was merged into this branch (no rebase): the only conflict was the import list in `Bgs.lean` (both sets kept), the inventory row of BGS-TRACE-151 was re-mirrored and its blob sha refreshed, renders were unchanged, and every check below was rerun on the merged tree.
* **Branch.** `line-J-rprime-d7`.
* **Sources.**
  * Author: box `/workspace/bgs-lineJ/` (REPORT_v2, STRATEGY_v2, code, logs, SHA256_v2; J3/REPORT_J3_v2, SHA256_J3_v2).
  * Referee: `/workspace/audit/lineJ/REPORT.md`, with all sections and the final DELTA3 verdict "ready to integrate". It is copied to
    `computations/verification/lineJ/referee/REPORT.md`.

## Claim table (new ids after BGS-TRACE-220)

| id | content | label | state | Lean (only what it states) |
|---|---|---|---|---|
| BGS-TRACE-221 | Prop J-C: exact sector law, exact top-orbit coefficients (8th root)/2, B_C formula; sectors 2, 6 cancel exactly, sectors 0, 4 survive; period 168 | P + exact check | proved | `pell49_period`, `pell49_periodic`, `pell49_lambda_order` (mod-49 period only) |
| BGS-TRACE-222 | sector-level antiunitary map RK | P | proved | — |
| BGS-TRACE-223 | count/disc/rest certificates; \|μ₂:₁\| ∈ [1.28359503, 1.28359523]; \|ξ\| ≥ 2.4586893 > √λ | CA | proved | — |
| BGS-TRACE-224 | window lemma (N = 6, c_win = 0.8443062873) | P | proved | `window_step` (real-line core), `window_N` (constants) |
| BGS-TRACE-225 | Theorem J: d = 7, (±2,8) contribution ≥ K_j·1.0184224^m/m with both signs in every 6 consecutive members of each class mod 168 (m ≡ 3 mod 6, m ≥ M0(j)); M0/M1/K_j table | CA | proved | — |
| BGS-TRACE-226 | Lemma L16 ((±2,16) lifted trace formula on exact blocks) | P | proved | — |
| BGS-TRACE-227 | (±2,16) d = 7 negligibility (≤ 1 % of (K_min/2)ξ_lo^m, m ≥ 243) | CA | proved | — |
| BGS-TRACE-228 | inheritance theorem W_{ce,eβ′} = (n_e/e²)W_{c,β′} | P | proved | `count_excl_one`, `count_units` (counts only) |
| BGS-TRACE-229 | prime-level complete-sum bound | P | proved | — |
| BGS-TRACE-230 | r(q) lemma: q ∣ h_m ⇔ r(q) ∣ m (odd m) | P | proved | `rank_core` (ring identity), `pell49_lambda_order` |
| BGS-TRACE-231 | Theorem J3 (referee wording): frozen R′ is false along m = 3p under H♮ and H_arg; unconditionally, if R′ holds, the conductor ∉ {1, 7} parts must cancel the d = 7 term exponentially on S⁺ | CA, conditional | **conditional** | — |
| BGS-TRACE-232 | H♮ | hypothesis | **open** | — |
| BGS-TRACE-233 | H_arg (arg ξ/2π ∉ ℚ; denominators < 1339 excluded) | hypothesis | **open** | — |

**BGS-TRACE-206 stays open.** Its boundary and ledger_status gain a Line J paragraph (Theorem J, (±2,16) controlled, the
conditional J3), stating explicitly "not a refutation". The Line I heuristic sentence is marked as superseded. Its state is
unchanged.

**Not registered as claims.** These appear in the note §8 and the packet only:
* the numerics m = 201…453 [N];
* STRATEGY_v2 [assessment];
* the slow-twist and level surveys [N/H];
* the fact that the s6 tops of 1:2 and 1:5 are float-only;
* R′_corr (a suggestion).

## Registry changes
* **`record/claims.json`.** Adds 221–233 and appends the Line J text to 206 (script-generated, format-preserving). Dependencies are
  acyclic:
  * 232 does not depend on 231;
  * 223 does not list BGS-TRACE-217, because only its code `rig_dom3b.py` is reused, and listing it would wrongly pull EXT-RS-1962
    into the impact graph.
* **`record/claim_verification_inventory.json`.** Adds rows for 221–233 (207 template; open rows have methods
  `["unevidenced"]`; `formalization` is non-empty ⇔ `lean_formalization`), mirrors 206, and sets `source_blob_sha` to the git blob
  sha1 of `claims.json`.
* **`record/claim_integration_epochs.json`.**
  * after_wave3 gets rows for 221–233, and 206's disposition is appended.
  * `external_dependency_extension` gets `added_ids` +3, its scope text, and `source_reviews` + `literature/lineJ_sources_20261031.md`.
* **`record/mathematics_topics.json`, topic README, docs/corpus_atlas.md.** Register the note.
* **Literature.** `literature/external_dependencies.json` gets EXT-VINOGRADOV-1937, EXT-WEYL-1916 and EXT-DAVENPORT-1980, all used
  by BGS-TRACE-231. The review is in `literature/lineJ_sources_20261031.md`. There is a new metadata cache snapshot
  `evidence/source_metadata/registry_metadata_20261031_lineJ.json` (+ .sha256, pointer in `literature/metadata_audit.json`, review in
  `record/audits/metadata_cache_refresh_20261031_lineJ/report.md`). It carries the 60 old records forward unchanged and appends 3.
* **Data-list edits in maintenance/test scripts.** These are required for new EXT ids, as in PR #60. No check is weakened.
  * `computations/verification/wave2_integration_audit.py`: the hard-coded admitted-later set +3 ids; docstring 21 → 24.
  * `computations/maintenance/tests/test_external_epoch_preservation.py`: the expected `(39,21)` → `(39,24)`. The count is computed
    from the same allowed set, and 39 sealed contracts are unchanged.
  * `computations/maintenance/v4_negative_controls.py`: the tamper target points at the new digest-pinned cache.
* **Prose.**
  * Updated: CHANGELOG, README.md/README.ru.md, RESEARCH.md, mathematics/results.md (and the regenerated parts), open_questions,
    claim_ledger, formalization/README (LineJArith row, counts 28 / 100).
  * Line I and Line G notes: "later work" pointers.
  * Regenerated: STATUS.md, claim_registry.md, scientific_dependencies.json/graph, bibliography and the views.

## Integration polish (non-blocking referee items), in the packet copy `J3/REPORT_J3_v2.md`
The author's file is in `pre_polish/` with sha256 bf83ef6b…, which equals the author's manifest entry.
* **L16-a.** Wrote Σ_w|c_w|‖V_w‖₁ ≤ (Σ_n|ĝ(n)|‖V_n‖₁)^m < ∞.
* **L16-b.** J_B = G_B⁻¹F_B^*δ₀α_B^*G_B is the coordinate matrix in the orthogonal, non-normalised block basis (supports 32/64), and
  the norms are coordinate norms.
* **Iwaniec–Kowalski Theorem 13.6.** Verified to be Vinogradov's minor-arc estimate only, so it does not by itself give
  o(π(x)) for every irrational γ.
  * Replaced by Vinogradov's equidistribution theorem (EXT-VINOGRADOV-1937; Method of Trig. Sums Ch. XI, via the
    Kuipers–Niederreiter Notes).
  * IK Ch. 13 and Vaughan Ch. 3 are kept at chapter level only.
  * "Dirichlet" for the density is replaced by the PNT in progressions (EXT-DAVENPORT-1980). The Weyl criterion is located as KN
    Thm 2.1 (EXT-WEYL-1916).
* **J3-F8.** Recorded the sha256 of `blocks16_exact.json` used by the builds: 814e4659…3960 (`J3/logs/SHA256_blocks16_basis.txt`).
  * `integration_checks/lineJ_J3F8_basis_provenance.py` checks that this sha matches the v1/v2 manifests, that
    `gstates16_block.py` loads that path, that all 576 certificates are certified, and that the basis mtime precedes all 128 build
    logs.
  * The builders were not modified, since their code sha256 is recorded in the certificates.

## Lean
`formalization/Bgs/LineJArith.lean` is imported by `Bgs.lean`.
* No `sorry`; no `native_decide` (`decide` only for the mod-49 orbit).
* Axioms are subsets of {propext, Classical.choice, Quot.sound}.
* `lake exe cache get` ran first ("No files to download"). `nice -n 10 lake build Bgs` exited 0 with 8816 jobs before the merge and 8821 jobs after merging b96ef6bd (the log is the post-merge build).
* Claims carry `formalization` only where the Lean states the named core (221, 224, 228, 230). The ledger strings say exactly what
  is covered.

## Integration numerics
* **Reruns.** The author scripts were rerun in an isolated copy, and their outputs are identical (`integration_reruns/`).
* **Independent check.** `integration_checks/lineJ_arith_checks.py` was written from the definitions and ends ALL_OK:
  * r(q) lemma: 0 mismatches over odd m ≤ 61 and primes < 3000;
  * ord₄₉ = 42 and 21;
  * window lemma grid: 0 failures;
  * constants;
  * K_min ≥ the table minimum;
  * n_q counts.

## Deviations and limits
1. **Lidskii and Weyl.** The Lidskii theorem and the Weyl (Horn) inequality for trace-class operators are not registered as EXT, following the Line F/I precedent.
2. **Primary texts not read.** The primary texts of Vinogradov (1937 note, 1954 book) and Davenport, and the 1916 Weyl paper, were not
   read. Locators come from Kuipers–Niederreiter (read) and the publisher contents pages. EXT-VINOGRADOV-1937 and EXT-DAVENPORT-1980
   are `unverified_application`.
3. **Citation change.** The J3 citation changed from IK Theorem 13.6 to Vinogradov's theorem (polish, above).
4. **State of BGS-TRACE-231.** It is registered with state `conditional`, following the repository convention for conditional
   theorems (with a closure_condition), not `proved`.
5. **Maintenance edits.** The three maintenance/test scripts receive data-list edits only (above).
6. **Large files excluded.** `.npy`/`.npz` Galerkin matrices (regenerable) and `__pycache__` are excluded from the packet.
7. **Scratch paths.** Absolute scratch paths in packet files are whitelisted in `PROVENANCE_PATHS.md`, not edited.
8. **Stale wording in 217.** BGS-TRACE-217's boundary still says "NOT certified: c(beta) != 0", which is true of 217 itself. 221
   decides it, and the Line I note carries a pointer. 217 was not edited.
9. **K_min.** J3's K_min = 0.00998476 is min(K_j⁺, K_j⁻)·(1 − 10⁻⁶). It is not the margin-reduced table value 0.009975; the two are
   consistent (K_min ≥ table min), as stated in the note §5 and claim 227.

## Checks (all with nice -n 10)
`checkers.log` holds this branch (merged tree), and `checkers_baseline_main_195a24f9.log` holds pristine main (a detached worktree of 195a24f9). `checkers_baseline_main_b96ef6bd.log` holds the same checks on the new main b96ef6bd. That run differs from 195a24f9 only in that scientific_registry_audit exits 1 there ("claim verification inventory source blob is stale", because main edited claims.json without refreshing the inventory). The merge on this branch fixes that, and its unittest counts under parallel load were 117/104, the same flaky pattern noted below.

**Required checks, all exit 0:**
* render_bibliography, render_claim_registry, render_errata, render_research_views, render_spectral_research and render_status,
  each with `--check`;
* scientific_registry_audit;
* repository_audit;
* wave3_integration_audit.

The rest give the same outcome as main:
* audit_manuscript_references, sync_finite_orbit_section and sync_fixed_map_section: exit 0.
* wave2_integration_audit: exit 1 with "integrated wrapper mapping changed". It already fails this way on main, before it reaches
  the external-epoch check.
* sync_return_sections: exit 1, because pandoc is not installed on the box (same on main).
* check_spectral_edition: exit 1 (same on main).
* bibliographic_metadata_audit `--self-test`: exit 1, only on the pre-existing `EXT-BR-1975: dependency graph changed` line (same
  on main). The three new records match, and no other record's impact set changed.
* unittest discover (256 tests): 116 failures, 103 errors, 1 skipped, both here and on main. A per-test outcome diff (verbose runs)
  shows **0 differences**. Non-verbose branch runs under load showed one extra outcome. In one run it was identified as `test_fractional_routing` (a subprocess with a 30 s timeout, run while `lake build` was busy). That test passes alone on the branch, and its target `check_routing.py` exits 0 with and without `-O`, so this is load-dependent flakiness and not a regression. The counts in `checkers.log` come from that run.

`lake build Bgs` exit 0, 8821 jobs on the merged tree (`lake_build_Bgs.log`).
