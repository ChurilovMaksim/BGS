# Breakthrough package audit (carried over from PR #84)

Sections 1–4 below are copied verbatim from the receipt of PR #84 (`repo-polish-1104`, head `0550302d`, written 2026-11-04 against main `6440a447`), together with its logs and `w2_independent_check.py`. Only the `evidence/breakthrough/` edits that this receipt describes (index wording for G3/G4b, the dated "What is NOT here" heading, and the 65 `sandbox://` links: 51 relinked, 14 marked "(not in repository)") are carried into the final polish branch, byte-identical to PR #84. PR #84's section 5 (SevenPrimary.lean, BGS-FORMAL-003 wording, its PDF build) is **not** carried over: `formalization/Bgs/SevenPrimary.lean` is hash-pinned by `computations/verification/seven_primary_certificate.py` (EXPECTED_LEAN), and PR #84's CI run 41886933866 failed on exactly that check. The registry counts quoted in section 2 (419 claims) are those of 6440a447; at this branch's base (4487e66a) the registry has 438 claims.

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

