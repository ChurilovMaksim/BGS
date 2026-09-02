# Review Findings — full-workspace referee pass (R83)

Date: 2026-08-31. Scope: the ENTIRE workspace (`paper/`, `src/`, `artifacts/`,
`formal/`, `review/`, `LEDGER/THEORY/ROADMAP/README/AGENTS`). Method: hostile
review per the workspace contract — every load-bearing claim re-executed where
a script exists, every paper citation traced to disk, every standing
retraction swept against the corpus. Chat: Russian; work product: English.

Companion document: `REVIEW_ERRORS.md` (the earlier partial pass, 2026-08-30).
This document SUPERSEDES it: two of its four "errors" are refuted below, one
is confirmed in a refined form, one is partially fixed.

---

## Part A — Verdicts on REVIEW_ERRORS.md (verified by re-execution)

### ERROR #1 (Theta preserves each eigenspace) — REFUTED; paper stands as printed
`review/referee/ref01_theta_stabilises_eigenspaces.py` re-run 2026-08-31
(artifact `artifacts/referee_r83/ref01_theta_stabilises_eigenspaces.json`,
reproduced identical to the 2026-08-31 16:59 artifact). Across 5 designs
(incl. N = 11, 13, 17, 19, 23): SAME-eigenspace residual ≤ 7.3e-16, the
"ERROR-#1 prediction" (Theta maps H_lambda to H_{lambda^{-1}}) residual
O(0.17-0.42). The error analysis in REVIEW_ERRORS #1 dropped the complex
conjugate: for an ANTIunitary Theta, U_A(Theta v) = conj(lambda)^{-1}(Theta v)
= lambda(Theta v) since |lambda| = 1. Theta stabilises every H_lambda with no
hypothesis. Status of the paper sentence (line 266): CORRECT.
**REVIEW_ERRORS #1 must not be applied; the proposed "fix" would have broken
a true statement.**

### ERROR #2 (cert-table script paths) — CONFIRMED, and FIXED only in the table
The certification table (tex lines 1861-1890) now cites 11/11 existing paths
(verified on disk). BUT four citations OUTSIDE the table still use the
pre-rebrand flat paths — see Finding F2.

### ERROR #3 (Theorem G norm estimates "sign error") — REFUTED; paper stands
`review/referee/ref02_theoremG_norm_ratio.py` re-run 2026-08-31 (artifact
`artifacts/referee_r83/ref02_theoremG_norm_ratio.json`). Measured exponents:
delta-case ||c_bar||_2/||c||_2 = K^{-0.5} exactly (6/6 designs), and
||c_bar||_1 = ||c||_1 exactly (the Birkhoff average REDISTRIBUTES l1 mass over
the orbit; it does not shrink it). Both printed inequalities of Theorem G hold
in all three regimes (generic delta / orbit-invariant / multi-orbit).
**REVIEW_ERRORS #3's proposed replacement text is itself wrong; do not apply.**

### ERROR #4 (Theorem II derivation gap) — diagnosis WRONG, but a REFINED
### genuine defect is CONFIRMED (Finding F1)
`review/referee/ref03_theoremII_jacobi_derivation.py` re-run 2026-08-31
(artifact `artifacts/referee_r83/ref03_theoremII_jacobi_derivation.json`).
REVIEW_ERRORS #4's own derivation used an additive shift and factored a
multiplicative character across a sum — wrong. The correct derivation
(multiplicative substitution x = n1*y) verifies the printed formula to
1.5e-14 for n1 != 0 at N = 23/31/41/61. HOWEVER it exposes a real defect the
paper shares: the printed theorem (tex line 1494-1512) omits the hypothesis
n1 != 0. On the n1 = 0 line the printed RHS vanishes identically
(conj(chi)(0) = 0) while the true matrix element is nonzero (measured up to
0.218 at N = 23, O(N^{-1/2})). See F1.

### Minor (S(10) = 31 vs 35) — CONFIRMED (Finding F3)
### Minor (z rounding 43.1/66.9/94.9) — cosmetic, no action.

---

## Part B — New findings (this pass)

### F1 [MEDIUM-HIGH, paper content] Theorem II (thm:jacobi) lacks the hypothesis n1 != 0
File: `paper/exact_wd_and_subgroup_moments.tex` lines 1494-1512.
The printed identity
`<f_chi|T(n)|f_psi> = e_N(-q/2) conj(chi)(n1) psi(n1) J(chi,psi;q)/(N-1)`
is FALSE on the line n1 = 0: LHS is O(N^{-1/2}) nonzero (measured 0.218 at
N = 23, 0.186 at N = 31, decaying ~ N^{-1/2}), RHS is identically 0.
Everything CERTIFIED about Theorem II is unaffected (the closed-form
reconstruction uses q = n1 n2 != 0 level sets, where n1 != 0 automatically;
the pipeline-vs-model agreement at 6.1e-14 / 2.4e-13 stands).
FIX (2 lines): add "for n1 != 0" to the theorem statement and one remark that
the n1 = 0 line (q = 0) is the degenerate pure-translation case where
`<f_chi|T((0,n2))|f_psi> = delta_{chi psi^{-1}} e_N(...)`-type Gauss-sum
formulae apply instead. Not applied yet — left to the next paper patch.

### F2 [MEDIUM, paper provenance] four stale flat script paths + two stale artifact paths
Lines 452 (`src/pstar_scan.py`, `artifacts/r71/Pstar_prime_k.json`),
508 (`src/compression_spacings.py`), 526 (`src/single_orbit_trend.py`),
602 (`src/hecke_centring_refutation.py`), 1853 (`artifacts/r71/`).
Real locations: `src/kloosterman/pstar_scan.py`,
`src/diagnostics/{compression_spacings,single_orbit_trend,hecke_centring_refutation}.py`,
`artifacts/legacy_runs/theorems/B_subgroup_kloosterman/Pstar_prime_k.json`.
A reader following the text cannot locate them. One-line fixes each.

### F3 [MEDIUM, paper content] shape census row S(10) disagrees with the recorded artifact
Line 1304: "S(R) = 1,1,1,3,8,31,64,105 for R = 5..12".
Artifact `artifacts/legacy_runs/theorems/H_shape_decomposition/shapes_t3_w16.json`:
R = 5..12 -> 1,1,1,3,8,**35**,64,105. Only R = 10 differs (31 vs 35; the 4
extra shapes are zero-padded concatenations of (1,-3,1), per the earlier
note). Either restate the census from the artifact or recompute under the
stated width cap and document the convention. Unresolved as of R83.

### F4 [MEDIUM, artifacts provenance] MANIFEST.md claim->artifact->script chain broken by the R82 rebrand
`artifacts/legacy_runs/MANIFEST.md` still cites flat paths
(`src/catmap_independent.py`, `src/r82f_torus_rigidity.py`,
`src/r80_jweight_dp.py`, ...) that moved to `src/{core,theorems,kloosterman,
shape_automaton,large_m}/...`, and artifact dirs `artifacts/r71..r82/` that
now live under `artifacts/legacy_runs/{theorems,ensemble_moments,
hecke_centring_void}/` and `artifacts/diagnostics/`. The R71 "known MANIFEST
defect" (run13_* provenance warning) is still open (`op:manifest_repair`).
The header still names the legacy paper `resonance_laws_catmaps.tex` as the
claim source. The "Lean formalisation" section cites the LOST external
project `C:\lean\bgs_formal\` without the [artifact lost] annotation that
R82.0/LESSON 82-E require. VERIFIED: all 18 spot-checked load-bearing
artifacts DO exist under the new layout (see Part C) — only the pointers are
stale, no numbers are lost.

### F5 [MEDIUM, hygiene] `review/scripts/smoke_test_src.py` is RED after the rebrand: 1/5 PASS
R82.0 recorded "smoke 5/5 PASS"; the topic-subfolder rebrand moved
`master_formula_strong.py` -> `src/theorems/`, `reduced_resonance.py` ->
`src/core/`, `audit_tail_bound.py` / `diag_conditional_prob.py` ->
`src/diagnostics/`, but the smoke test still inserts only `src/` on sys.path.
Re-produced today: 4x ModuleNotFoundError. FALSE ALARM (each module imports
and exposes the checked symbol when its real directory is on sys.path —
verified manually), but the workspace's self-test is currently red and the
"5/5 PASS" claim is no longer reproducible as stated. Fix the test's path
list (or import via `src.` packages); re-run; record.

### F6 [LOW-MEDIUM, docs] README.md drift
* Header/layout say "22 pp, 309 KiB, compiled 2026-08-30"; the current PDF is
  25 pages / ~313 KiB (log: "Output written ... (25 pages)").
* Environment section: "Julia 1.11.4 at AppData\...\Julia-1.11.4" — that
  install is GONE; the box now has Julia 1.11.9 at `C:\Tools\julia\julia-1.11.9`
  (fresh `~/.zcode/ENVIRONMENT.md`, probed 2026-08-31 17:13).
* Open-problems table lists `op:lean_rebuild` and `op:paper_recompile` as
  open — both are DONE (formal/ builds green in-workspace; tectonic compiles
  with 0 undefined refs). `op:pairing` is described by the DEAD
  crossing-matching picture (R82.25 replaced it by the family-second-moment
  identity); `op:cscale` (closed R82.33) is absent.
* The `artifacts/` layout tree is split by the "How to reproduce" section and
  renders as two broken fragments.

### F7 [MEDIUM, docs/ENV] AGENTS.md Julia note is now doubly wrong
AGENTS.md: "Julia: `C:\Users\churi\AppData\Local\Programs\Julia-1.11.4\bin\
julia.exe` (the `C:\Tools\julia` path in older text does not exist)". As of
2026-08-31 the 1.11.4 install does not exist and `C:\Tools\julia\julia-1.11.9`
DOES. Following AGENTS.md literally breaks every Julia run. (The run journal
ENV headers quoting 1.11.4 are historical records — fine — but the live
convention file must track the live box.)

### F8 [LOW, LEDGER internal] page-count drift inside the R82 narrative
R82.7 records 20 pages / 271.58 KiB; the R82 final handoff says 24 pages; the
shipped PDF (16:32 build, re-verified by this pass) is 25 pages / ~313 KiB.
Content-bearing claims unaffected; the narrative should state one number.

### F9 [LOW, notation hazard] two "Lucas" normalisations in play
R82.24/LEDGER writes the branch scale as `c = +-L_{(K-1)/2}`; the paper and
R82.12 write `c = L_{K-1}` with `N = L_K`. Both are correct but the sequences
differ: R82.24's `L_j` is the t-parametrised Lucas sequence
(L_j(3): 2,3,7,18,47,123,...), the paper's is the classical one
(1,3,4,7,11,18,...). Resolving identity: L_j(t=3) = classical L_{2j}
(a^j + a^{-j} = tr A^j with lambda = phi^2). Naive cross-reading gives an
apparent contradiction (classical L_5 = 11, 11^2 = 121 != 5 mod 199, while
L_10 = 123, 123^2 = 5 mod 199 — the Lean ScaleLaw certificate instantiates
the latter). One clarifying sentence in THEORY 19 / the paper would prevent
the confusion.

### F10 [PROCESS] no version control; interrupted review session left dangling state
The workspace is not a git repository; the README editorial notes record two
manual .tex edits that "cannot be reverted automatically". The 2026-08-31
review session that produced `REVIEW_ERRORS.md` and the three referee
artifacts left `REVIEW_FINDINGS.md` EMPTY (0 bytes) and no LEDGER entry —
this document and the RUN 83 ledger entry close that gap. Recommendation:
`git init` + commit at least the text layers (paper/, *.md, formal/Bgs/).

### F11 [INFO, positive] referee refutations prove the paper right in 2 of 4 cases
ERRORS #1 and #3 were refuted by machine check with 15-digit margins. Had the
proposed "fixes" been applied blindly, two TRUE statements would have been
corrupted. The verify-before-edit discipline (and the referee artifacts now
on disk) is exactly what the contract requires; keep the pattern.

### F12 [INFO, cosmetic] LaTeX warnings
0 undefined references/citations (grepped the kept log after a fresh
`tools/bin/tectonic.exe -X compile`, EXIT=0). Remaining: 1 font-shape warning
(TU/lmr/m/scit), 10 overfull boxes — the largest (118.5 pt) is the
certification table at lines 1856-1893; consider `\small`->`\footnotesize` or
column re-break. No mathematical impact.

---

## Part C — Reproduction log (re-executed 2026-08-31)

| Item | Result |
|---|---|
| `py -3 review/referee/ref01_theta_stabilises_eigenspaces.py` | PASS, verdict identical to stored artifact |
| `py -3 review/referee/ref02_theoremG_norm_ratio.py` | PASS, identical |
| `py -3 review/referee/ref03_theoremII_jacobi_derivation.py` | PASS, identical; refined defect F1 confirmed |
| `cd formal && lake build` | SUCCESS 5/5 jobs; C3_global_count + all four ScaleLaw theorems: NO axioms; C1a/C2/C4: native_decide axiom, disclosed as documented |
| tectonic recompile + log grep | EXIT=0; 0 undefined refs/citations; 25 pages |
| `review/scripts/smoke_test_src.py` | 1/5 PASS (F5 — false alarm, modules fine) |
| Artifact spot-check (18 load-bearing files incl. torus_rigidity.json, closed_form.json, q_curve_N3571.npz, jacobi_moments.json, family_second_moment.json, second_moment_raw.json, k0_law_final.log, inert_torus.json, Pstar_prime_k.json, jweight_dp.json, julia_bigdp.json, shapes_t3_w16.json) | ALL FOUND under legacy_runs/{theorems,ensemble_moments,hecke_centring_void}/ and diagnostics/ |
| R12-A retraction sweep (grep "p^{2/3}" across *.md, *.tex) | 0 live citations outside retraction notices — corpus clean |
| Review of census numbers, z-table rounding, cert table | table paths 11/11 OK; S(10) mismatch = F3; rounding cosmetic |

## Part D — Prioritised repairs (next run)

1. F1 — patch thm:jacobi (add `n_1\neq 0` + n1=0 remark); recompile; grep log. [paper]
2. F2 — 6 one-line path fixes in the tex; recompile; grep log. [paper]
3. F3 — adjudicate S(10) (31 vs 35) against the artifact convention; fix paper or artifact doc. [paper]
4. F4 — regenerate MANIFEST rows under the new layout; annotate the lost Lean row; fold in the run13 provenance warning resolution. [artifacts]
5. F5 — repoint smoke_test_src.py at the topic subfolders; re-run to 5/5. [review]
6. F6/F7 — refresh README (pages, Julia, open-problems, tree) and AGENTS.md (Julia path). [docs]
7. F8/F9 — one-line ledger/theory clarifications. [docs]
8. F10 — `git init` and commit the text layer. [process]

---

## Part E — Repairs executed (RUN 84, 2026-08-31, same day as Part A-D)

Every finding of Part B was closed; the workspace baseline is git commit
`643f2af`.

| # | Disposition | What was done |
|---|---|---|
| F1 | FIXED | thm:jacobi now states "for n1 != 0" and carries a remark: on the n1 = 0 line the RHS vanishes identically while the true matrix element is an O(N^{-1/2}) Gauss-sum diagonal object; all certified consequences use q != 0 level sets. |
| F2 | FIXED | 7 substitutions in the tex: src/kloosterman/pstar_scan.py, src/diagnostics/{compression_spacings,single_orbit_trend,hecke_centring_refutation}.py, artifact paths to legacy_runs/hecke_centring_void/ and legacy_runs/theorems/B_subgroup_kloosterman/, and the §numerics prose now points at artifacts/legacy_runs/ + artifacts/diagnostics/. |
| F3 | FIXED (adjudicated) | The R75.3 census IS the width-16 pass with S(10) = 35; the paper's 31 was the width-14 value. Paper corrected to 1,1,1,3,8,35,64,105 with the width-14 note (31,56,93) quoted, matching LEDGER R75.3 verbatim. |
| F4 | FIXED | artifacts/legacy_runs/MANIFEST.md regenerated in place by src/maintenance/repair_manifest_r84.py: all script rows repointed to topic subfolders, all artifact rows to their actual post-rebrand locations; the lost-Lean row annotated [ARTIFACT LOST — R82.0/LESSON 82-E]; header records the R84 repair; the run13 provenance warning retained. Post-repair disk check: 91/91 artifact tokens resolve. |
| F5 | FIXED | review/scripts/smoke_test_src.py rewritten for the topic-subfolder layout (multi-path sys.path + exit-code gate); re-run: 5/5 PASS + functional micro-check OK. |
| F6 | FIXED | README: 25 pp/314 KiB header, artifacts tree corrected (MANIFEST.md lives at legacy_runs/, referee_r83/ and diagnostics/ listed), certificates section repointed, per-run count 84, open-problems table rebuilt (closed ops struck through with closure references; op:local and op:k>=4 carry the R82 statements), env block refreshed (Python 3.14, Julia 1.11.9 at C:/Tools/julia, 12 cores), broken tree splice repaired, MIGRATION_PLAN/drafts lines removed. |
| F7 | FIXED | AGENTS.md Julia entry now `C:\Tools\julia\julia-1.11.9\bin\julia.EXE` with the history of the two stale notes. |
| F8 | FIXED | README quotes 25 pp (the R84 build); LEDGER R82 narrative numbers are historical records and stay as written (append-only). |
| F9 | FIXED | THEORY 19.1 carries a NOTATION note: L_j(3) = classical L_{2j}; the apparent 11^2 != 5 contradiction is resolved and tied to the Lean ScaleLaw instantiation (123^2 = 5 mod 199). |
| F10 | FIXED | git init -b main; .gitignore (pycache, LaTeX intermediates except kept logs, lake build dirs); baseline commit `643f2af` of the whole workspace (806 files). |
| F11 | — | Nothing to repair; discipline note stands. |
| F12 | PARTIAL | Certification table stays \small (content priority); 1 font-shape warning remains; 0 undefined refs. Overfull boxes unchanged — cosmetic only. |

Verification after all edits: tectonic recompile EXIT=0, grep of the kept log
= 0 undefined references/citations, 25 pages; smoke test 5/5; Lean build
replayed green (5/5 jobs); MANIFEST token check 91/91.
