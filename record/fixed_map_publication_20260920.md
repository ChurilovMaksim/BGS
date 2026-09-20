# Fixed-map publication and verification review

Original goal: **OPEN**. This revision does not prove BGS for the fixed
family or claim a discovery of established external significance.

## Research result

The p=3 mixed loop equation was reduced exactly to a fourth-moment
identity. Eliminating the cubic term with p=2 and using Jensen gives a
conditional interval for subsequential Abel pair limits. The normalized
p=3 residual itself supplies the required moment boundedness. A separate
internal algebra audit checked signs and constants. Twenty-seven finite
cases compare the original loop expression, cotangent moments, and trace
sums, with maximum discrepancy below 2.85e-14. The residual hypotheses
for the frozen map are still unproved; the interval does not identify CUE.

See the maintained [chapter](../mathematics/fixed_map_resolvent_frontier.md)
and [detailed low-order proof](../supplement/fixed_map/resolvent-flow/low_order_bounds.md).

## Recovered materials and remote reconciliation

The local base was `e0ada2e2c44dfe10bebf928dc8a1d6526ae15cb7`.
Remote main was `59f6cd4c12347aac700f4d51afafb36c5669a7a0`.
The two remote-only shadow-history files were recovered with exact Git
blob hashes. The local trace bridge extends the remote version; both
that extension and all remote-only material are retained.

The supplement inventory contains 115 recovered files: mathematical
derivations, Python/C++/Wolfram programs, data and dated reviews. Full
third-party source PDFs, executables, caches and TeX temporary files are
excluded. Historical statements about nonpublication and execution remain
explicitly historical. The current chapter and claim ledger govern status.
The new publication authorization supersedes the earlier no-push condition.

## Verification

- Supplement: all 115 inventory hashes and all Python sources checked;
  28 isolated replay commands passed. Exact certificate replay in Python
  and C++ includes rejection of a corrupted certificate. Larger weighted
  minor checks reach N=23 with independent Jacobi assembly.
- Reproduction repair: the replay runner converts inherited Python search
  paths to absolute paths before changing working directories. This fixes
  dependency lookup without modifying mathematical source evidence.
- Whole-workspace verification: 121 distinct Python/C++ checks passed after
  two narrowly scoped reruns. The initial run passed 119/121; the repaired
  run passed both remaining checks. The runner now supplies the mandatory
  `--output` for `pell_harmonic_returns`; the structural recheck followed
  completion of this linked review. Initial and repaired reports are both
  retained, rather than rewriting a failed run as successful.
- Manuscript: three LaTeX passes passed the reference/overflow gate;
  225 pages, 1,703,442 bytes. Every page parsed and rendered with PyMuPDF.
  All four pages of the new chapter were visually inspected. Both
  Markdown-to-TeX synchronization checks passed.
- PDF SHA-256:
  `8d992423a5c0deac30047247d9b5b1861bd0730ea199d5a6ff1f45d33cb270c5`.

The [verification summary](../evidence/fixed_map_publication/summary.json)
and its initial/repaired reports are stored under
`evidence/fixed_map_publication/`. All final verifier source hashes were
checked against the working tree. Floating diagnostics are not interval enclosures or proofs of
asymptotic limits. Exploratory echo/monodromy simulations and Wolfram
scripts retain their dated results and are not counted as freshly run.

## Formalization boundary

`Bgs.CueLoopKernels` adds integer proofs for the positive-part cubic
reference and a cleared-denominator elimination kernel using `omega`.
No `sorry` or new axiom is introduced. These source statements do not
formalize Herglotz analysis, the external loop theorem, or BGS.

No Lean executable is available locally. The attempted pinned-release
download timed out. A successful historical build of 16 modules does not
certify this 17-module revision. The CI run for publication commit `3139f47` completed with failure before
any job steps executed: every returned job has an empty step list. No
Lean compilation therefore occurred. The job-log endpoint returned
`BlobNotFound`; the connected reader does not expose the annotation
endpoint, so the underlying pre-execution failure reason is not asserted.
The referenced `actions/checkout@v7` and `actions/setup-python@v7` tags
were checked and both exist; no speculative workflow downgrade was made.

## Publication gate

Publication preserves the remote head through a non-forced update and
does not overwrite independently added research. Repository synchronization
and software verification do not change the OPEN mathematical status.

## Remote verification

The publication commit is [3139f47](https://github.com/ChurilovMaksim/WoW/commit/3139f478c5147e6e487578d9af88bef0ffa97410). Its tree
`f908f55bfc13b78736d685c52e21685958fc63af` exactly matched the locally
staged tree. The update was a non-forced fast-forward of remote main.
The remote-only files and their original commits remain in the ancestry.

[Scientific CI run](https://github.com/ChurilovMaksim/WoW/actions/runs/35525732662)
and [manuscript CI run](https://github.com/ChurilovMaksim/WoW/actions/runs/35525732685)
failed before executing steps. These failures are recorded separately from
the successful local runs; they are not reported as passing CI.
