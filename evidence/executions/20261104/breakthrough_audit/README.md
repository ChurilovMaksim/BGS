# Breakthrough package audit and repository polish — 2026-11-04

Branch `repo-polish-1104` from `origin/main` 6440a447. Scope: the breakthrough
research record (`evidence/breakthrough/`, five commits 58478bfb..d4093ece,
receipt `evidence/executions/20261102/breakthrough-integration.md`), plus small
repository fixes listed at the end. No claim state changed. BGS (BGS-BGS-001)
and BGS-TRACE-005 stay open; BGS-TRACE-325 (Theorem R♯-mod v5) stays
conditional.

## 1. What the package claims

`evidence/breakthrough/README.md` presents a method-search record (day-1 swarm
M01–M10, waves 2–47x): wave notes, check scripts, working material and 16 Lean
drafts in `formalization/drafts/`. It states explicitly that promotion is not a
theorem, that `record/claims.json` is unchanged by the package, and that BGS in
full generality remains open. Individual notes label results as proved, proved
modulo named lemmas, census-confirmed, sampling, sketch, or draft with `sorry`.

## 2. Consistency with the registry and README status

* `record/claims.json`: 419 claims (proved 338, open 42, conditional 21,
  verification-pending 17, refuted 1) — identical to the counts in
  `DAY1_REPORT.md` and the root README. The five package commits did not touch
  `record/` or `formalization/Bgs.lean` (checked with `git diff --name-only`).
* No note claims BGS, BGS-TRACE-005 or R′ proved (grep for "BGS proved/solved",
  "implies BGS", "closes BGS" etc.: no hits). The package never mentions
  BGS-TRACE-325, so it cannot contradict its conditional status.
* Registry IDs cited in the package: 96 distinct; all exist except the
  shorthands `BGS-001`/`BGS-005` in two Russian working files
  (`working/frozen-map/TARGETS.md`, `TRACE_BARRIERS.md`), which mean
  BGS-BGS-001 / BGS-TRACE-005 and mark them open — consistent, left as is.
* The 15 `.lean` files under `working/g4check/` and `working/g4/` are working
  copies; the 7 in `g4check/` are byte-identical to the current
  `formalization/Bgs/` modules. They are not compiled and not imported.

## 3. Findings

1. **Unregistered results (by design, but note it).** Many statements are
   labelled "proved" in the notes (Full Blindness for odd p, DIV/PAR, S-tuple
   dihedral lemma, F1, ψ-analysis, M4/R40/R30, …). None is a registered claim;
   none has an independent proof review or a Lean proof in `Bgs.lean`. They are
   research-record statements only and must not be cited as project results
   until registered with receipts.
2. **Label collision "G3" (fixed in the index).** Wave 6
   (`working/numerics/wave6_task3_G3_analytic_bound.md`) calls the S-bound "G3"
   and says it is closed as an argument *modulo G4* at m = 3–6; wave 12
   (`methods/wave12_g3_common_pi.md`) calls "one common π across components"
   G3 and says it is **NOT proved**. The index line "G3 closed analytically"
   dropped "modulo G4" and the scope. The README line now states both senses.
   "G4b closed" now says "as an analytic argument (not in Lean)", as in
   `wave13_152_assembly.md` §6.
3. **Broken links (fixed).** 65 Markdown links in 17 wave notes pointed to
   `sandbox://workspace/bgs-breakthrough/...` (the original sandbox). 51 targets
   exist in the repository and now use relative links; 14 targets are excluded
   data/log files (`.json`, `.jsonl`, `.log`, `.txt`) and are now plain code
   spans marked "(not in repository)". Link text and note content are otherwise
   unchanged. The one remaining match of the link checker
   (`wave46_LemmaU_L3.md`, `N_x²+N_{x′}²`) is a formula, not a link.
4. **Pending items dated.** "What is NOT here" lists runs "still running"
   (Δ(48), DIV/PAR V3 Lean draft, PC triple intersections); the heading now
   says "as of the 2026-11-02 integration". Their results are not in the repo.
5. **Missing receipts.** 8 census data files (1.3 GB) and all run logs are not
   in the repository (declared in the README and receipt). The Lean draft
   headers report build results of a test-copy project (e.g. "8706 jobs,
   0 errors, 5 sorry"); no build log is in the repository and they were not
   rebuilt here (each needs 13–19 minutes). Header `sorry` counts are lower than
   a raw `grep -cw sorry` because comments also contain the word; not an error.
6. **Receipt file count.** The receipt says 842 files; the five commits add 841
   files and modify 1 (`evidence/README.md`), so 842 is the number of touched
   files. Breakdown matches: methods 774, working 47, 3 top-level documents,
   16 drafts, 1 receipt.
7. **"c_J = 8" at m = 60** (`wave37_Blindness_m60.md`) is a single-m bound, not
   polynomiality in m; the note itself says "One m proves nothing about SCJ in
   general". Arithmetic rechecked: 600·144 = 86,400; 5929·36·150·2·8 =
   512,265,600; product 4.43·10¹³ < 60⁸ = 1.68·10¹⁴; 2·60·60·(1−cos 72°) =
   4975.08; 3600·28800·11137·5929 = 6.85·10¹⁵ = 60^8.905.

No overclaim about BGS, TRACE-005, R′ or TRACE-325 was found.

## 4. Numerical re-runs (fresh, this audit)

Python `/workspace/lineNgas/venv`; logs in `logs/`. Different sample from the
four checks in the 2026-11-02 receipt.

| Check | Script | Result | Matches note |
|---|---|---|---|
| Full Blindness, odd p | `methods/wave37_FullBlindness_check.py` | ALL CHECKS PASS, 1 s | yes |
| B(60) | `methods/wave37_Blindness_m60.py` | 49/49 and 121/121 blind ⇒ 49·121 = 5929 | yes |
| Gap G at m = 64 | `methods/wave41_GapG_m64_check.py` | ALL CHECKS PASS (512/2048/8192 points, 0 symmetric) | yes |
| Pairing Lemma refutation (8192,17) | `methods/wave43_PairingLemma_check.py` | ALL CHECKS PASS; not a JBL counterexample | yes |
| W₂ (e(p) ≥ 2 primes) | `w2_independent_check.py` (new, independent: e ≥ 2 iff α^N ≡ 1 mod p², since p ∤ N/d) | to 10⁶: {13, 31}; to 2·10⁷: {13, 31, 1546463}; 78,497 odd primes ≤ 10⁶ | yes (note: 10⁶ → 13, 31; 1546463 at 10⁸) |
| e(1546463) exact | `methods/wave40_W2_verify.py 1546463 773231` | d = 773231, e = 2 exactly | yes |

The C++ sweep `wave40_W2_sweep.cpp` was not rerun: no C++ compiler on this box
and no root for apt. The independent Python check covers the range to 2·10⁷.
Heuristics in the W₂ note were rechecked: log log 10⁹ + M ≈ 3.29 and
Σ_p 1/p² ≈ 0.452 (that sum includes p = 2; over odd primes it is 0.202).

## 5. Other changes in this branch

* **Lean (task 3).** `formalization/Bgs/SevenPrimary.lean`: the 7 `degrees_k`
  and `order49` now use `decide +kernel` instead of `native_decide`
  (`#print axioms`: `degrees_k` → `[propext]`, `order49` → no axioms). The 7
  `product_k` and 7 `rabin_k` keep `native_decide`: a kernel trial of
  `product_0` was killed by the OOM killer (exit 137) on the shared box, as the
  2026-11-01 cleanup also found (timeouts and memory guard). FourCutKernel (2)
  is unchanged: the earlier unguarded trial reached 5.8 GB in 45 s, and the
  enumeration (≈10⁸ list steps) is out of kernel range. A kernel trial of
  `CayleyEnergy.k23_energy` was also killed (exit 137). Legacy `native_decide`
  count: 37 → 29 (RESULTS.md re-rendered).
* **BGS-CAYLEY-002 (task 5).** Its boundary said "by native_decide" for all
  five designs. It now states the actual mix: 19 of 21 theorems
  `decide +kernel`, K = 23 energy and excess `native_decide`. **BGS-FORMAL-003**
  boundary now records the SevenPrimary split. Both IDs are sealed historical
  rows, so the matching `historical_claim_amendments` entries in
  `record/claim_integration_epochs.json` were updated (fields.boundary,
  disposition, review), following the Ф.4 precedent. No state, title, source,
  evidence, verifier or dependency change. `claim_registry.md` and
  `claim_verification_inventory.json` (boundary + source blob) were regenerated.
* **Manuscript (task 4).** "eta two" → η = 2 in the Line H section title and
  the BGS-TRACE-198 theorem title; the visible "Draft note" in the conclusion is
  now "Scope note" (same text otherwise); "unnumbered/DRAFT additions" →
  "unnumbered additions" in the reading-map caption. The chapter order was NOT
  changed: sections are numbered globally in input order, and the root README
  and other text cite section numbers (e.g. "Section 126.1"); the earlier passes
  kept a deliberate no-reorder rule. Reordering needs a coordinated renumbering
  pass. PDF rebuilt with Tectonic 0.17.0: PASS, 381 pages, sha256
  `5b122d0278412e10e26d21187d833060c4f369891fe784a0b0a86ab72c83a708`
  (`manuscript_build_manifest.json`). A second build from the final sources gave
  the same sha256.
* **CI (task 2).** The last three "Scientific verification" runs on `main`
  passed (41814002051, 41645910453, 41645153987, 2026-11-03/04). The failures on
  2026-11-02/03 (41449610412, 41586034055) are older; every run since the
  PR #81 merge has passed. No CI change needed.
