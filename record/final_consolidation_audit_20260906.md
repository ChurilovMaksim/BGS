# Final consolidation audit — 6 September 2026

This record closes the repository-recovery pass requested after the interrupted
main-branch integration. It distinguishes active mathematical claims, finite
verification, external theorem inputs, historical provenance, and publication
artifacts. No force update is required or intended.

## 1. What was checked

The audit covered four independent surfaces:

1. the complete list of surviving remote research branches and their relation
   to `main`;
2. the original 204-file consolidation delivery recovered from the user's
   ChatGPT Library;
3. the maintained source/build graph on `main` (Python, C++, Lean, TeX and
   provenance gates);
4. the mathematical/editorial boundary between exact project proofs, finite
   regressions, named external inputs and still-open BGS obligations.

The original delivery archive was recovered as
`WoW_consolidated_research.zip`, size 2,605,999 bytes, SHA-256
`8addfd45f0c8d3d43d06472477aa8c5aac8eb3f2b94082fe6b715b20a3447099`.
Its archive contains exactly 204 files with total uncompressed size 4,084,074
bytes. The companion patch has SHA-256
`366fe46e385b9af3f100fedc34d36413379ffde41cb2a2ddc08c749fb90081e8`.
The historical delivery manifest records a clean 204-file patch round-trip and
92-page consolidated build; those historical checks are preserved as
historical evidence rather than re-labelled as executions on the final commit.

## 2. Recovered omissions

Three research lines had been left outside the earlier recovery and were
restored byte-for-byte from their historical Git blobs:

- `mathematics/cayley_energy_curve_bound.md`,
  `computations/verification/cayley_energy_curve_regression.py`, and
  `formalization/Bgs/CayleyCurveEnergy.lean`;
- `mathematics/cayley_product_row_elliptic.md` and
  `computations/verification/cayley_product_rows.py`;
- `mathematics/cayley_product_row_projective_bezout.md` and
  `computations/verification/cayley_product_row_projective_bezout.py`.

Earlier in the same recovery sequence, the fixed-strength/locality,
smooth-cohomology, Pell coboundary, noncommuting return-word, resonance
nondegeneracy and unified-manuscript material had already been restored.

## 3. Branch-loss prevention

Every remote research branch that was not a strict ancestor of `main` is
preserved under `archive/branch-snapshots/` as its exact Git tree. These
snapshots are provenance only. They may contain stale build files, superseded
notation or exploratory claims; they do not override the maintained top-level
source tree or `record/claim_ledger.md`.

Branches proved to be strict ancestors of `main` were not duplicated because
normal Git history already preserves them.

## 4. Original 204-file packet preservation

The original outer ZIP remains the byte-authoritative container for the
historical repeated-run logs, frozen-input records and binary publication
artifacts. It was verified locally during this audit and remains preserved in
the user's ChatGPT Library. Its exact identity and the hashes of the two
compressed binary members are recorded in
`archive/delivery-20260906/README.md`.

A binary re-encoding of that ZIP is intentionally not committed through the
GitHub connector. Long base64 transfers can be truncated by the intermediate
transport; a possibly corrupted duplicate would be worse provenance than an
externally retained object with an independently checked SHA-256. The active
source tree and all divergent historical Git trees are preserved directly in
`main`; the external ZIP covers the residual historical logs and delivery
artifacts.

The two compressed binary members are:

- `manuscript/WoW_unified.pdf`: 880,886 bytes, SHA-256
  `0076d2feb521fe59819b9bf243423ead832dcfa64acafbce20012b6dc09c497d`;
- `evidence/consolidation_20260906/reproduction_inputs.zip`: 1,177,213 bytes,
  SHA-256
  `16a4a92bbc078d90334528065f561cdff8032fb536985a03ab9c77573c9d87c3`.

The PDF is a derived artifact from preserved TeX sources. The nested ZIP is a
frozen duplicate-input package. Neither is used as the mathematical
source-of-truth.

## 5. Structural defects found and repaired

The audit found several real integration defects that would have been hidden by
mere file-existence checks:

- `formalization/Bgs.lean` did not import every active module. The final entry
  point imports the complete `formalization/Bgs/*.lean` set, including
  `CayleyCurveEnergy`, `GeneralHyperbolicParity`, `LocalityKernels`,
  `PellCoboundary`, `PellEchoWeights` and `PellFourierKernel`.
- `CMakeLists.txt` initially omitted `fixed_strength_locality_exact.cpp` and
  `pell_coboundary_pairs.cpp`. A second source-enumeration pass then found the
  remaining orphan `return_word_certificate.cpp`. The active directory has 16
  C++ sources and the final CMake graph has 16 matching executable targets.
  The return-word source was independently compiled with C++20 plus
  `-Wall -Wextra -Wpedantic` and executed successfully: 30 geometry obligations
  and 11 free-word tests passed.
- `computations/verification/repository_audit.py` had a stale top-level
  whitelist predating `REPRODUCE_unified.md`, `requirements-nondegeneracy.txt`
  and the provenance archive. The final audit explicitly accepts the current
  publication surface while excluding `archive/` from maintained-source
  duplicate/link/language checks.
- the repository referred to `record/final_consolidation_audit_20260906.md`
  although that record had never been committed. This file closes that gap.
- the independent manuscript workflow built only the older arithmetic article.
  The final workflow uses `build_unified_manuscript.py` as the canonical
  fail-closed builder and keeps the old article as a separate legacy build.
- the unified builder's page-count parser could return `null` when TeX wrapped
  the word `pages` across a log line. The parser is now whitespace-tolerant and
  fails closed if the page count cannot be recovered.
- the first final `REPRODUCE_unified.md` invoked `verify_workspace.py` without
  its required `--build`, `--logs` and `--output` arguments. The reproduction
  commands now build CMake first and pass all required arguments explicitly.
- the first complete-workspace runner still invoked several active Python
  verifiers without their mandatory CLI arguments and attempted to write one
  generated result into committed evidence. The final `verify_workspace.py`
  redirects every generated output below `--logs`, treats committed evidence as
  read-only, supplies the detected required arguments, generates the radius-8
  resonance certificate before its strict replay, and defers the replay checker
  until the certificate exists. The exact orchestration change is commit
  `3a141579a93941d310b3c278c88c874b7868f8ba`.

## 6. Mathematical review of the recovered material

The restored Cayley curve note uses a bidegree-(2,2) subgroup-curve
specialization. Makarychev--Vyugin Theorem 2 was re-read in the primary paper:
with `m=n=2` and `g=h=1`, its displayed coefficient is
`12*m*n*g*(m+n)=192`. The note's range `K>=5725` safely enforces the theorem's
lower subgroup-size and `h<(320)^(-3)|G|^2` conditions, while the upper range is
`K<p^(3/4)/3`. This is an independent auxiliary route. It does **not** replace
the sharper maintained direct Cayley theorem `E_+(A)<34 K^(8/3)`.

The restored product-row elliptic note gives an exact algebraic reduction and
generic genus-one fibre-product description. It does not prove the desired
uniform `O(1)` row-intersection bound; that growing-parameter conclusion remains
open.

The restored projective Bezout note gives a specialization-safe rank/nullity
criterion and determinantal support description. It must not be confused with
the older dehomogenized `D'/G'` invariants whose converse failed at projective
infinity. The field-valued Bezout/gcd equivalence is a structural refinement;
a growing-`K` polynomial bound on the relevant integral support remains open.

No restored finite regression has been promoted into an asymptotic theorem.
No equality of support integers is inferred merely from equality of split-prime
support. No numerical or finite-matrix test is used as a substitute for a
Heisenberg-scale trace estimate.

## 7. BGS scope after consolidation

The repository now contains substantial exact arithmetic, cohomological,
recurrence, rigidity, obstruction and finite-certificate results. It also
contains explicit negative mechanisms showing why several tempting shortcuts
to BGS fail.

The positive microscopic BGS/GOE/COE universality problem remains **OPEN**.
The missing positive chain still requires, for a natural fixed nonarithmetic
family with the correct symmetry reduction and unfolding, weighted joint trace
(or equivalent local-resolvent) control at the Heisenberg scale together with
tail control beyond compact Fourier support. Nothing in this consolidation is
labelled as a complete solution of that open problem.

## 8. CI and publication status

The GitHub Actions attempts observed during the recovery failed before any
scientific step ran. For the workspace-runner fix commit
`3a141579a93941d310b3c278c88c874b7868f8ba`, Scientific verification run
`34019814414` completed with GitHub conclusion `failure`, but its manuscript,
computation and formalization jobs all expose `steps=null` and no job logs.
Accordingly this is runner/provisioning infrastructure evidence, not a failed
Python/C++, Lean, TeX or mathematical check, and no green cloud-CI result is
inferred from it.

The formerly un-runnable dependent resonance chain was then executed locally
with the corrected orchestration. Radius 8 produced status `CERTIFICATE`; the
independent replay returned `PASS` after 5,704 deductions (3,293 `P`, 1,077 `S`,
1,229 `D`, 105 `F`); the exact Hessian-obstruction check and the finite
quantum-variance check both returned `PASS`. Exact hashes and the cloud run/job
identifiers are recorded in `record/final_verification_followup_20260906.json`.
This targeted execution closes the runner's dependency/CLI defect; it is not
represented as a complete current-worktree green CI run.

A final local manuscript reconstruction was performed from the preserved
204-file manuscript corpus with the current `main` master TeX and
final-delivery-note blobs. The canonical builder completed three TeX passes,
kept every input hash unchanged, reported no forbidden warning, and produced a
93-page PDF of 886,866 bytes. Pages 1, 92 and 93 were rendered and visually
inspected; the same three page renders were byte-identical across two successive
successful builds. The exact scope and blob identities are recorded in
`record/final_manuscript_build_20260906.json`. The PDF binary itself is not
committed and byte-identical PDF reproduction is not claimed, because document
metadata/identifiers can change while rendered pages remain identical.

The next provisioned GitHub runner should exercise the corrected complete
C++/Python/Lean graph and the canonical unified TeX build. Source correctness,
cloud execution and mathematical correctness remain separate evidence layers.

## 9. Final authority rule

For scientific status, `record/claim_ledger.md` remains the repository-wide
claim authority. This audit records recovery and verification boundaries; it
does not silently promote historical claims absent from that ledger. For
publication, `manuscript/WoW_unified.tex` is the canonical editable entry point.
For lost-work prevention, `archive/branch-snapshots/` is a provenance-only
store and `archive/delivery-20260906/README.md` records the external byte-level
delivery provenance. Neither overrides maintained source files.
