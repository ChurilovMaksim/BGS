# Line K integration record (31 October 2026, UTC+5)

* **Base.** `ChurilovMaksim/BGS` origin/main 121df8b4. Main had moved past 64357925 (the merge of PR #62) with 0a6a798b and
  121df8b4: Line B / Line D Lean modules, and the `formalization` lists of BGS-TRACE-152, 154, 157, 163 and 175.
* **Branch.** `line-K-harg`.
* **Sources.**
  * Author: box `/workspace/bgs-lineK/`. This covers REPORT_v2 (§8 errata) with SHA256_v2.txt, K2/REPORT_K2_v2 with
    K2/SHA256_K2.txt, code/, logs/, and lean/ (K3Finite.lean and the K3Gaps chunks).
  * Referee: `/workspace/audit/lineK/` (REPORT.md with the first round, DELTA and DELTA2), copied to
    `computations/verification/lineK/referee/`.
  * The packet is copied unchanged to `computations/verification/lineK/`, except for the W-F7 edit to `K2/REPORT_K2_v2.md`. The
    author's original of that file is in `pre_polish/K2/`.

## Claim table (new ids after BGS-TRACE-233)

| id | content | label | state | Lean (only what it states) |
|---|---|---|---|---|
| BGS-TRACE-234 | Lemma K3 (gap lemma): b′ ≥ 447, b′ ∉ {504, 560, 616, 840} ⇒ every unit class mod gcd(56, b′) has max cyclic gap < A·b′ | P + CA | proved | `sieve_enumeration`, `sieve_survivors`, `big_prime_excluded`, `sixth_lt_A`, `gaps_447` (447..466) in `lake build Bgs`; full range 447..2645 by chunk files **outside** the build (`lean_gaps/`; chunk 1547..1646 re-split 5 × 20) |
| BGS-TRACE-235 | Theorem K3: S⁺ ∩ {3p : p ≡ p₀ (56)} infinite for every unit p₀; **unconditional** (H_arg removed by a case split) | P + CA (+ Dirichlet, Vinogradov, Davenport, Weyl) | **proved** | `no_small_denominator`, `noFrac_sound`, `exceptions_excluded`, `bprime_ge` (finite inputs only) |
| BGS-TRACE-236 | Corollary K3: frozen R′ ⇒ φ⁻¹O♮ ≤ −0.99K_j·1.0184224^m + 4m + o(m) on an infinite S⁺; H♮ alone refutes frozen R′ | CA | proved (dichotomy); refutation **conditional on H♮** | — |
| BGS-TRACE-237 | Theorem K1: light-cone identity Σ_{β≠0}Ẑ_βW_{q,β} = D_iso − E_b/q (q ∥ h, 2 a square mod q), with the push-forward reformulation | P (+ exact check q ≤ 47) | proved | — |
| BGS-TRACE-238 | Prop K2: levels d ≥ L_m absorbed; S_Z ≤ 0.5000001 (m ≥ 495); η_m ≤ (2.010 + o(1))/log(2p+1) | P + CA | proved (crossover ≈ 1.682·10⁹ is [N], boundary text only) | — |
| BGS-TRACE-239 | H♮_mid (an alternative to H♮, not a weakening) | hypothesis | **open** | — |
| BGS-TRACE-240 | Theorem K: frozen R′ false under H♮ or H♮_mid | P + CA | **conditional** | — |
| BGS-TRACE-241 | Lemma W1 (Weil bound over the orbit subgroup; degeneracy criterion) | P-cite (EXT-WEIL-1948) | proved | — |
| BGS-TRACE-242 | Lemma W2′ (non-cyclic block AM–GM, every bounded read-out, after W-F7) | P | proved | — |
| BGS-TRACE-243 | Lemma W3 (orbit average) | P | proved | — |
| BGS-TRACE-244 | operator input (OP_k, δ) | hypothesis | **open** | — |
| BGS-TRACE-245 | Theorem W (Weil range q ≤ c_k p²) | P, on OP | **conditional** | — |
| BGS-TRACE-246 | Theorem K2′ (frozen R′ ⇒ a slow λ-orbit at an open conductor) | P, on OP | **conditional** | — |
| BGS-TRACE-247 | Conjecture C1 (lim I_k^{1/k} = 1) | H | **open** | — |

**Changed claims (no state change):**
* **BGS-TRACE-231** stays `conditional`.
  * Its dependency on BGS-TRACE-233 is replaced by one on BGS-TRACE-235.
  * Its closure condition is now "H♮ (BGS-TRACE-232) is proved; S⁺ is infinite by BGS-TRACE-235".
  * Its boundary and ledger_status are annotated.
* **BGS-TRACE-233 (H_arg)** stays `open`. Its boundary, ledger_status and closure condition are annotated: "no longer needed for 231;
  bypassed by BGS-TRACE-235; not proved". The repository has no "superseded" state, so open plus this annotation is the honest
  encoding.
* **BGS-TRACE-206** stays `open`. A Line K paragraph is added, ending "This is NOT a refutation; R′ stays open".

**Not registered as claims** (note §7 and the packet only):
* the negative results (b) and (d), and the periodic-point and β-moment findings;
* the K4 toy rates, factorisations, toy level traces and W1 instances [N];
* the K1 interpretations [H];
* the Bourgain extension (see Deviations).

## Registry changes
* **`record/claims.json`.** Adds 234–247 and updates 231, 233 and 206 (`integ_logs/edit_claims.py`, format-preserving). The
  dependencies are acyclic:
  * 238 does not depend on 231;
  * 239 depends on 235 and 238;
  * 240 depends on 231, 232, 235–239.
* **`record/claim_verification_inventory.json`.**
  * Adds rows for 234–247 (BGS-TRACE-207 template; open rows have methods `["unevidenced"]`; non-empty `formalization` ⇔
    `lean_formalization`).
  * Re-mirrors 206, 231 and 233.
  * Also re-mirrors the `formalization` lists of 152, 154, 157, 163 and 175. Main had changed these in 0a6a798b and 121df8b4 without
    updating the inventory, so main's `source_blob_sha` was stale and `test_registry_nodes` failed twice on main. For those rows,
    `lean_formalization` is added to methods by the mechanical method rule; spof is not reassessed.
  * `source_blob_sha` is set to the git blob sha1 of `claims.json`.
* **`record/claim_integration_epochs.json`.**
  * after_wave3 gets rows for 234–247, and the dispositions of 206, 231 and 233 are appended.
  * `external_dependency_extension` gets `added_ids` + EXT-WEIL-1948, its scope text (24 → 25), and `source_reviews` +
    `literature/lineK_sources_20261031.md`.
* **`record/mathematics_topics.json`, topic README, docs/corpus_atlas.md (regenerated).** Register the note.
* **Literature.**
  * `literature/external_dependencies.json`:
    * new EXT-WEIL-1948 (used by 241);
    * `additional_uses` (claim BGS-TRACE-235) and `project_sources` entries for EXT-VINOGRADOV-1937, EXT-WEYL-1916 and
      EXT-DAVENPORT-1980.
    * EXT-DIRICHLET-1837 is a sealed historical contract (wave2 external epoch), so its fields are **not** edited. Its use by 235 is
      recorded in claims.json, in the cache impact refresh and in the source review.
  * The review is `literature/lineK_sources_20261031.md`.
  * New metadata snapshot `evidence/source_metadata/registry_metadata_20261031_lineK.json`, with:
    * a `.sha256` file;
    * the pointer in `literature/metadata_audit.json`;
    * the review `record/audits/metadata_cache_refresh_20261031_lineK/report.md`.
  * The snapshot refreshes the impact sets of Dirichlet, Vinogradov, Weyl and Davenport (listed in
    `current_review.older_record_impact_changes`) and appends Weil.
* **Data-list edits in maintenance/test scripts**, required for the new EXT id exactly as in PR #60 and #61. No check is weakened.
  * `computations/verification/wave2_integration_audit.py`: the admitted-later set gets EXT-WEIL-1948; docstring 24 → 25.
  * `computations/maintenance/tests/test_external_epoch_preservation.py`: `(39,24)` → `(39,25)` (twice). The count is computed from the
    same allowed set, and the 39 sealed contracts are unchanged.
  * `computations/maintenance/v4_negative_controls.py`: the tamper target points at the new digest-pinned cache.
* **Prose.**
  * Updated: CHANGELOG, README.md/README.ru.md, RESEARCH.md, mathematics/results.md, open_questions, claim_ledger, the topic
    README, formalization/README (LineKFinite row; counts 28 → 29 and 100 → 101; the 12 modules added on main in 0a6a798b/121df8b4
    are named as not yet counted).
  * The Line J and Line G notes get "later work" pointers.
  * Regenerated: STATUS.md, claim_registry.md, scientific_dependencies.json/graph and the views.

## W-F7 (referee DELTA2), applied at integration in `computations/verification/lineK/K2/REPORT_K2_v2.md`
The author was busy elsewhere, so W-F7 was applied by the integrator. The author's file is `pre_polish/K2/REPORT_K2_v2.md`
(sha256 c9f58c24…, equal to the referee's DELTA2 object).
* In Lemma W2′, the (±2,16) read-out I⊗J_B is **not** of finite rank (‖I⊗J_B‖₁ = ∞). The proof now uses the bounded-J argument as
  for J = I: |Tr(JX)| ≤ ‖J‖·‖X‖₁, with one leftover factor in trace norm. The constant is C_J = ‖J‖·sup‖L‖₁/sup‖L‖, with
  ‖I⊗J_B‖ = ‖J_B‖ ≤ ½ (as in J3 `assemble16`).
* The constant is written max(1, sup‖L‖)^{2k}.
* Theorem W step 3 and the "Effect" paragraph are adjusted to match.
* A new section "## 8. Errata W-F7 (referee DELTA2, 31 Oct 2026; applied at integration)" records the change. The conclusions of
  Theorem W / K2′ are unchanged (C′ = e^{O(k)}, independent of m).
* BGS-TRACE-242 is registered as W2′ [P] for all bounded read-outs. The patched file no longer matches its line in
  `K2/SHA256_K2.txt`; the receipt records both shas.

## Lean
`formalization/Bgs/LineKFinite.lean` (namespace `Bgs.LineK`; core Lean, no import) is imported by `Bgs.lean`.
* It contains the author's K3Finite theorems and the K3Gaps definitions with `gaps_447`. Statements are unchanged; they are wrapped
  in a namespace with a header docstring.
* No `sorry` and no `native_decide`; only `decide` and `decide +kernel`.
* `#print axioms` for all 9 theorems: none, except `noFrac_sound` and `bprime_ge`, which use [propext, Quot.sound]
  (`lean_axioms_LineKFinite.log`).
* `lake exe cache get` ran first ("No files to download"). Then `nice -n 10 lake build Bgs` exited 0 with "Build completed
  successfully (8834 jobs)".
* **K3Gaps chunks are kept outside `lake build Bgs`.**
  * A 100-modulus chunk needs 12 GB or more, and the author's 100-chunks above 1646 were OOM-killed. Lake would elaborate the
    chunks in parallel on this 15 GB box.
  * Instead, K3Finite.lean and the author's 62 chunk files were recompiled **sequentially** with `nice -n 10 lean` (Lean 4.33.1),
    using `lean_gaps/run.py`. 61 chunks exit 0 (`lean_gaps/summary.txt`, `log_*.txt`).
  * The 100-modulus chunk `K3Gaps_1547` was OOM-killed twice: in the pass (exit −9, under concurrent load) and alone (exit −9 at
    about 12.2 GB). The referee had compiled it on this box earlier (exit 0, 123 s; referee DELTA addendum).
  * Its range 1547..1646 was re-checked as five 20-modulus chunks `lean_gaps/split_1547/K3Gaps_split_{1547,…,1627}.lean`. These have
    the author's definitions byte-for-byte; only the theorem line `okRange lo 20` differs. All exit 0 with peak RSS ≈ 3.3 GB
    (`split_1547/summary.txt`).
  * Every `gaps_*` theorem "does not depend on any axioms".
  * The claim's Lean coverage is labelled accordingly. In `lake build Bgs`: the finite sieve part and the gap check on 447..466. The
    full gap range 447..2645 is covered by chunk files outside the build. Not formalised: the inclusion–exclusion inequality, the
    monotonicity for ℓ > 23, the arb bound on A, and CRT/Dirichlet/Vinogradov.

## Integration checks and reruns
* `computations/verification/lineK/integration_checks/lineK_checks.py` (written at integration; log `lineK_checks.log`): ALL_OK.
* Author reruns (`integration_reruns/`): `k3_harg`, `k1_cone_check`, `k2_SZ`, `k2_large_v2` and `w1_weil_check`. All logs are
  byte-identical, and all JSON outputs are byte-identical.
* Manifests:
  * `SHA256_v2.txt` verifies.
  * `K2/SHA256_K2.txt` verifies except for the W-F7-patched report.
  * `referee/SHA256.txt` is stale for `REPORT.md`, because DELTA and DELTA2 were appended after it was written. It is left
    unmodified.

## Deviations
1. **K3Gaps are not in `lake build Bgs`** (memory). Only `gaps_447` (n = 20) is in the build. The full range is evidence with logs.
   The author's chunk 1547..1646 (n = 100) does not fit in memory here, so it was re-checked as five n = 20 chunks written at integration.
2. **W-F7 was applied by the integrator**, not the author, as instructed. The pre-polish copy is kept.
3. **The Bourgain extension (q ≤ p^C, [P-cite], ineffective, conditional on OP) is not registered.** The referee's DELTA §D5 lists
   it, but the integration brief's registration list does not include it. Bourgain/BGK are not added as external dependencies.
4. **BGS-TRACE-233 stays `open`**, with the annotation "bypassed, not proved". There is no "superseded" state.
5. **EXT-WEIL-1948: the primary text was only partially read** (pp. 204–205 set-up in a search-index extract; fetches of doi.org and
   pnas.org timed out, PMC returned 403). The application status is `unverified_application`.
6. **EXT-DIRICHLET-1837** (sealed historical contract) gets no `additional_uses` entry. The new use is recorded elsewhere (see above).
7. **The stale referee manifest** (`referee/SHA256.txt` for REPORT.md) is documented, not fixed.
8. **The branch is based on 121df8b4, not 64357925**, because main had moved.
9. **Main's stale inventory** (`source_blob_sha` and the formalization lists of 152, 154, 157, 163 and 175) is re-mirrored here. This
   fixes two `test_registry_nodes` failures that are present on main.
10. **`k2_SZ.py` reads `/workspace/bgs-lineJ/J3` by absolute path.** It was rerun against the box copy (read-only). It is not
    portable as committed.
11. **`k2_SZ.json` stores `S_Z_upper` as the float 0.5.** The arb value is S_Z = 2C₈² + 2C₁₆² = ½ + O(10⁻¹³⁶), where
    C₈ ≤ (1 + λ^{−495})(½ + 1506.18·1.9154712^{−495}) and C₁₆ ≤ 3.8·10⁻²⁵. The registered bound 0.5000001 is therefore valid.

## Checks (`checkers.log`; baseline on pristine main 121df8b4 in `checkers_baseline_main_121df8b4.log`)
All checks were run with `nice -n 10` on the final tree.

| check | branch | main 121df8b4 |
|---|---|---|
| render_bibliography / claim_registry / errata / research_views / spectral_research / status `--check` (×6) | all OK | all OK |
| scientific_registry_audit | **OK** (331 claims, 64 external dependencies) | FAIL: inventory source blob is stale (fixed here) |
| repository_audit | PASS | PASS |
| wave3_integration_audit | OK | OK |
| `lake exe cache get` → `nice -n 10 lake build Bgs` | exit 0, 8834 jobs | — |
| wave2_integration_audit | FAIL "integrated wrapper mapping changed" | same (pre-existing) |
| audit_manuscript_references `--check` | OK | OK |
| sync_return_sections `--check` | FAIL (pandoc not installed) | same |
| sync_finite_orbit / sync_fixed_map `--check` | SKIP (exit 0) | same |
| check_spectral_edition | FAIL "source projection" (spectral_simplicity_certificates.json.gz) | same (pre-existing) |
| bibliographic_metadata_audit `--self-test` | FAIL on EXT-BR-1975 only | same (pre-existing) |
| unittest discover (256 tests) | 116 failures, 103 errors | 117 failures, 104 errors |

The per-test comparison (verbose runs) shows no new failures. Two tests fixed here: `test_registry_nodes` inventory drift, and
the snapshot test. A third, `test_fractional_routing`, timed out once on the branch working tree. `check_routing.py` walks the
whole tree, including the untracked, gitignored `formalization/.lake` (22 s versus 2 s on a clean checkout). It passed in the
final run.
