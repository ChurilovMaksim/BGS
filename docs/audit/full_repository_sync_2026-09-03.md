# Full repository synchronization audit — 2026-09-03

## Scope and conclusion

This audit re-read, re-indexed, and reclassified the full WoW/BGS research workspace after the first rebuild proved too minimal.  The objective was not aggressive deletion.  The repository is now organised by the rule **preserve broadly, trust narrowly**: useful code, data, negative results, manuscript material, and provenance remain available, while root `STATUS.md` and the canonical verification layer control current truth.

No scientific file from the uploaded pre-Git workspace was found to be irretrievably lost.  The intentionally omitted old contents are generated Lean/build artifacts, ignored `.out` review logs, and duplicate Tectonic executables/tools rather than scientific results.

## Audit coverage

Every visible working/research-corpus path outside the embedded `archive/legacy-workspace/` snapshot was hashed and inventoried.  The embedded legacy snapshot was separately compared with the pristine uploaded pre-Git workspace and pre-rebuild tree.  Exact duplicate contents were reviewed once and all duplicate paths were counted.

Content-bearing formats were handled as follows:

- all text-like files were UTF-8 decoded/scanned; theorem, proof, status, manuscript, review, roadmap, and run-history material received semantic review;
- all Python sources were syntax-compiled without writing bytecode;
- all JSON was parsed and producer/status fields were inspected;
- every unique NPZ dataset was opened and its keys/shapes inspected;
- every unique PDF was rendered and visually scanned page by page; duplicate PDFs were identified by content hash;
- every standalone TeX document was compiled with XeLaTeX; fragments and static cross-references were indexed;
- JavaScript/MJS and shell sources were syntax-checked;
- Lean sources were read at theorem/obligation level; Julia and Lean execution were unavailable in the audit runtime, so no new Julia/Lean execution result is claimed.

The compact inventory snapshot is `FILE_INVENTORY_SUMMARY.json`; regenerate the full path-level inventory with `code/maintenance/audit_inventory.py`.  Historical producer names are resolved in `PRODUCER_PATH_MAP.md`, and the mathematical status index is `CLAIM_STATUS_MAP.md`.

## Completeness against the uploaded workspace

The pristine uploaded workspace contained **1100 files**.  Its `.gitignore` excluded **70** generated/review files (48 Lean `.lake/build` outputs and 22 `*.out` files), leaving **1030 expected non-ignored source/research files**.

Hash comparison found a current/recoverable equivalent for every old non-ignored scientific content item.  The two intentionally omitted non-ignored contents are byte-identical Tectonic executables (`tools/tectonic.exe` and `data/tools/bin/tectonic.exe`).  They are tooling, not research results.  The complete old workspace is additionally recoverable through Git history and `archive/legacy-workspace/`.

## Current inventory and duplicates

The synchronized working/research surface contains **1069 file paths**, **817 unique SHA-256 contents**, **224 exact duplicate groups**, and **252 duplicate path copies**.  Duplicates are not blindly deleted because many are deliberate provenance snapshots in `data/legacy`, review/audit material, or historical paper locations.

Important PDF duplicate relations include historical `exact_wd_and_subgroup_moments.pdf` = `paper/final/cat_map_bgs_main.pdf`, historical `BGS_COMPLETE.pdf` = `paper/final/bgs_complete_paper.pdf`, historical `M4D_PROOF.pdf` = `paper/final/mobius_fiber_theorem.pdf`, and historical `BGS_PROOF.pdf` = `paper/final/h_coupling_research_note.pdf`.

## Source and data integrity

The full audit found zero UTF-8 decode failures in the working text corpus, zero Python syntax failures, zero JSON parse failures, zero JavaScript/MJS syntax failures, and zero shell syntax failures.  All three unique NPZ datasets opened successfully.  All 11 standalone TeX sources compiled successfully on a first XeLaTeX pass.  Static TeX reference indexing found one unresolved `thm:T17`, confined to an explicitly retracted historical run-11 note.

The final repository health gate additionally checks the canonical paths, quarantine placement, all `code/` Python syntax, controlled JSON roots, and semantic sentinels.

## Canonical computational reruns

`code/verification/baseline_r82.py` was rerun and reproduces the preserved fourth-moment curves with maximum absolute deviations `6.039613253960852e-14` at `N=199,K=11` and `2.353672812205332e-13` at `N=3571,K=17`.

`code/verification/h3_k2_exact_reduction.py` was rerun.  It gives `|P|=132=12*11` at `N=53,K=13` with identity deviation about `1.25e-12`, and `|P|=90=10*9` at `N=199,K=11` with identity deviation about `3.64e-10`.

`code/verification/theorem_ii_new_primes.py` was rerun with a direct scalar character-sum comparison independent of the production matrix contraction.  Maximum relative deviations are `1.4166352564530244e-11` at `N=461,K=23` and `1.2714969482034705e-10` at `N=19489,K=29`, both below the explicit `5e-10` tolerance.

The matched number-variance experiment was freshly rerun at `N=19489,K=29`; every tested `L in {1,2,3,5,8,12}` stays within `|z|<2` of the matched finite-dimensional GOE control.  The bounded spacing rerun freshly reproduced the `N=3571,K=17` row (`KS D=0.0139959 < 0.0210549`, `chi2/dof=1.297`).  The heavier `N=19489` spacing row remains a retained prior result and is marked as such because its full rerun did not finish inside the bounded audit execution window.

These are finite-N computational/numerical results, not proofs of a limiting spectral law.

## Corrected scientific status

The historical Möbius-fiber M1 proof remains invalid: it promotes `O(1/K^2)` to `o(1)` in a fixed-K regime, its own K=17 row violates its displayed envelope, cross-twist terms are not controlled, normalisations drift, and a required perfect-power exclusion is not proved.  M1 is therefore an `OPEN GAP`.

A second independent defect was found in the R86/R87 trace-fluctuation shortcut.  The draft expands `(C_q+C_q^*)^k` with the ordinary scalar binomial formula without establishing that `C_q` and `C_q^*` commute.  In general ordered noncommutative words must be retained.  The subsequent adjacent-pair factorisation/independence assertion is also unproved.  Thus the Cycle-2 additive toy and Cycle-3 finite-N measurements remain research experiments but cannot promote the lemma.

The word-trace proof engine remains incomplete: its stored output explicitly records unresolved rewrite closure for higher words.  The historical `N=95419` GOE driver is quarantined because it computes consecutive-gap ratios but compares the reported KS statistic with the ordinary spacing CDF.  The raw numbers are preserved under `results/historical-numerical/`.

## Rank-2 / Sp4 boundary

The rank-2 corpus contains valuable exact finite-design identities, especially at `N=53`: the diagonal identity, coset flatness/sector identity, hyperbolic period-4 structure, and a negative result for a naive product kernel.  These survive as finite-N exact research results.  They do not prove a uniform rank-2 theorem, a higher-genus Weil estimate, M4d, or general BGS.  `G0`, edge-mass, and trace-fluctuation measurements remain experimental/numerical.

## Formal boundary

The Lean source tree is preserved.  `formal/Bgs/OpLocal.lean` contains deliberate `sorry` obligations and an opaque spectral bound; it is a specification/open target rather than a proof.  Other finite certificate files must be read at their stated parameters.  Lean/Lake was unavailable in this audit runtime, so no fresh full build is claimed.

## Historical ledger and path migration

The full old ledger has systematic UTF-8/Windows-1251 mojibake.  A reversible encoding-only repair was verified locally and its before/after checksums/method are recorded in `HISTORY_ENCODING_REPAIR.json`.  The preserved 573 KB historical source is intentionally not silently rewritten in this structural sync.

Old `src/`, `artifacts/`, `LEDGER.md`, and similar strings remain in historical/research files by design.  Rewriting provenance would be worse than preserving migration debt.  Canonical runtime code is clean; recoverable old producer names are mapped in `PRODUCER_PATH_MAP.md`.

## Repository policy after this sync

1. `STATUS.md` is the only present-tense claim authority.
2. `results/verified/` is for audited reproducible computational certificates; `results/numerical/` is current numerical evidence; `results/historical-numerical/` is quarantine/superseded evidence.
3. Historical result JSON is not rewritten merely to modernise producer paths.
4. Research material stays in normal paths rather than being hidden because it is unfinished.
5. Generated caches/build trees and duplicate tool binaries stay out.
6. Failed routes are preserved with an explicit reason instead of silently deleted.
7. `code/maintenance/repo_health.py` and `audit_inventory.py` are the reproducible structural gates.

## Current frontier

Continue from `research/M1.md`: derive the exact ordered twist expansion, fix normalisations, keep all cross terms, prove degeneracy exclusions before applying finite-field estimates, state the `(N,K,m)` scaling regime, and obtain a genuinely vanishing remainder.  Any alternative route is legitimate only if it bypasses both the invalid historical M1 promotion and the invalid R86 noncommutative-binomial shortcut on its own merits.
